from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CUE_TRIAL_RE = re.compile(r"^(?P<q1>\d+)_(?P<q1d>\d+)_(?P<q2>\d+)_(?P<q2d>\d+)$")
DIFFICULTY_RANGE_RE = re.compile(r"^(?P<qmin>\d+(?:\.\d+)?)-(?P<qmax>\d+(?:\.\d+)?)$")


@dataclass(frozen=True)
class EventRow:
    row_index: int
    onset: float
    duration: float | None
    trial_type: str
    difficulty_range: str | None
    outcome: str | None
    response_accuracy: int | None
    is_tutorial: bool | None
    dropped_samples: int | None
    marker: str
    marker_stream: str


def _as_float(value: str | None) -> float | None:
    if value is None:
        return None
    text = value.strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _as_int(value: str | None) -> int | None:
    if value is None:
        return None
    text = value.strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        return int(text)
    except ValueError:
        return None


def _as_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    text = value.strip().lower()
    if text in ("true", "1"):
        return True
    if text in ("false", "0"):
        return False
    return None


def _normalize_optional(value: str | None) -> str | None:
    if value is None:
        return None
    text = value.strip()
    if not text or text.lower() == "n/a":
        return None
    return text


def _format_float(value: float, decimals: int = 6) -> str:
    return f"{value:.{decimals}f}"


def _cue_to_difficulty(trial_type: str) -> str | None:
    match = CUE_TRIAL_RE.match(trial_type.strip())
    if not match:
        return None
    return (
        f"{int(match.group('q1'))}.{int(match.group('q1d'))}"
        f"-{int(match.group('q2'))}.{int(match.group('q2d'))}"
    )


def _difficulty_bounds(difficulty_range: str) -> tuple[float | None, float | None]:
    match = DIFFICULTY_RANGE_RE.match(difficulty_range)
    if not match:
        return None, None
    return float(match.group("qmin")), float(match.group("qmax"))


def _read_events(path: Path) -> list[EventRow]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows: list[EventRow] = []
        for idx, row in enumerate(reader, start=1):
            onset = _as_float(row.get("onset"))
            if onset is None:
                continue
            rows.append(
                EventRow(
                    row_index=idx,
                    onset=onset,
                    duration=_as_float(row.get("duration")),
                    trial_type=(row.get("trial_type") or "").strip(),
                    difficulty_range=_normalize_optional(row.get("difficulty_range")),
                    outcome=_normalize_optional(row.get("outcome")),
                    response_accuracy=_as_int(row.get("response_accuracy")),
                    is_tutorial=_as_bool(row.get("istutorial")),
                    dropped_samples=_as_int(row.get("dropped_samples")),
                    marker=(row.get("marker") or "").strip(),
                    marker_stream=(row.get("marker_stream") or "").strip(),
                )
            )
    rows.sort(key=lambda x: (x.onset, x.row_index))
    return rows


def _read_participant_flags(bids_root: Path) -> dict[str, str]:
    participants_tsv = bids_root / "participants.tsv"
    if not participants_tsv.exists():
        return {}

    flags: dict[str, str] = {}
    with participants_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            subject = (row.get("participant_id") or "").strip()
            if not subject:
                continue
            included = (row.get("analysis_included") or "n/a").strip().lower()
            if included not in ("true", "false"):
                included = "n/a"
            flags[subject] = included
    return flags


def _sum_dropped_samples(dropouts: list[EventRow], start_s: float, end_s: float) -> int:
    total = 0
    for row in dropouts:
        if start_s <= row.onset < end_s and row.dropped_samples is not None:
            total += row.dropped_samples
    return total


def _is_outcome_trial(row: EventRow) -> bool:
    if row.difficulty_range is None:
        return False
    if row.outcome not in ("Correct", "Wrong"):
        return False
    if row.response_accuracy not in (0, 1):
        return False
    return True


def _task_from_bids_root(bids_root: Path) -> str:
    lower_name = bids_root.name.lower()
    if "arithmetic" in lower_name:
        return "arithmetic"
    raise ValueError(f"Could not infer task from BIDS root name: {bids_root}")


def _resolve_bids_root(bids_root_arg: str) -> Path:
    direct = Path(bids_root_arg).expanduser()
    if direct.is_absolute():
        return direct.resolve()

    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd

    repo_root = Path(__file__).resolve().parent.parent
    from_repo = (repo_root / direct).resolve()
    return from_repo


def _default_out_path(bids_root: Path) -> Path:
    base_dir = Path(__file__).resolve().parent
    return base_dir / "reports" / f"trial_table_{bids_root.name}.tsv"


def _default_summary_path(out_path: Path) -> Path:
    return out_path.with_name(f"{out_path.stem}_summary.json")


def _build_subject_trials(
    subject: str,
    task: str,
    events: list[EventRow],
    analysis_included: str,
    trial_duration_s: float,
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    pending_cues: dict[str, list[EventRow]] = defaultdict(list)
    dropouts = [
        row for row in events if row.trial_type == "dropped_samples" and row.dropped_samples is not None
    ]

    rows: list[dict[str, str]] = []
    anomalies: list[str] = []
    block_counter: dict[str, int] = defaultdict(int)
    block_difficulty_counter: dict[tuple[str, str], int] = defaultdict(int)

    for event in events:
        cue_difficulty = _cue_to_difficulty(event.trial_type)
        if cue_difficulty is not None:
            pending_cues[cue_difficulty].append(event)
            continue

        if not _is_outcome_trial(event):
            continue

        difficulty_range = event.difficulty_range
        assert difficulty_range is not None

        queued = pending_cues.get(difficulty_range, [])
        if not queued:
            anomalies.append(
                f"Outcome without matching cue for difficulty {difficulty_range} at events row {event.row_index}."
            )
            continue
        cue_event = queued.pop(0)

        is_tutorial = event.is_tutorial if event.is_tutorial is not None else False
        block = "tutorial" if is_tutorial else "main"
        block_counter[block] += 1
        block_difficulty_counter[(block, difficulty_range)] += 1

        trial_index_subject = len(rows) + 1
        cue_onset_s = cue_event.onset
        calc_start_s = cue_onset_s - trial_duration_s
        calc_end_s = cue_onset_s
        answer_start_s = cue_onset_s
        answer_end_s = event.onset
        response_time_s = answer_end_s - answer_start_s
        if response_time_s < 0:
            anomalies.append(
                f"Negative response time at events row {event.row_index} (rt={response_time_s:.6f}s)."
            )

        dropped_calc = _sum_dropped_samples(dropouts, calc_start_s, calc_end_s)
        dropped_answer = _sum_dropped_samples(dropouts, answer_start_s, answer_end_s)
        dropped_total = _sum_dropped_samples(dropouts, calc_start_s, answer_end_s)
        qmin, qmax = _difficulty_bounds(difficulty_range)

        rows.append(
            {
                "participant_id": subject,
                "analysis_included": analysis_included,
                "task": task,
                "source_events_file": f"{subject}/eeg/{subject}_task-{task}_events.tsv",
                "trial_id": f"{subject}_trial-{trial_index_subject:03d}",
                "trial_index_subject": str(trial_index_subject),
                "trial_index_block": str(block_counter[block]),
                "trial_index_block_difficulty": str(block_difficulty_counter[(block, difficulty_range)]),
                "block": block,
                "is_tutorial": "true" if is_tutorial else "false",
                "difficulty_range": difficulty_range,
                "difficulty_qmin": "" if qmin is None else _format_float(qmin, 1),
                "difficulty_qmax": "" if qmax is None else _format_float(qmax, 1),
                "response_accuracy": str(event.response_accuracy),
                "outcome": event.outcome or "",
                "cue_event_row": str(cue_event.row_index),
                "outcome_event_row": str(event.row_index),
                "cue_marker_onset_s": _format_float(cue_onset_s),
                "calc_start_s": _format_float(calc_start_s),
                "calc_end_s": _format_float(calc_end_s),
                "calc_duration_s": _format_float(trial_duration_s),
                "answer_start_s": _format_float(answer_start_s),
                "answer_end_s": _format_float(answer_end_s),
                "response_time_s": _format_float(response_time_s),
                "dropped_samples_calc": str(dropped_calc),
                "dropped_samples_answer": str(dropped_answer),
                "dropped_samples_trial": str(dropped_total),
                "cue_marker": cue_event.marker,
                "outcome_marker": event.marker,
                "cue_marker_stream": cue_event.marker_stream,
                "outcome_marker_stream": event.marker_stream,
            }
        )

    unmatched_cues = sum(len(queue) for queue in pending_cues.values())
    if unmatched_cues:
        anomalies.append(f"Unmatched cue markers remaining after pairing: {unmatched_cues}.")

    summary = {
        "subject": subject,
        "total_trials": len(rows),
        "tutorial_trials": block_counter.get("tutorial", 0),
        "main_trials": block_counter.get("main", 0),
        "started_arithmetic_markers": sum(1 for row in events if row.trial_type == "started_arithmetic"),
        "finished_arithmetic_markers": sum(1 for row in events if row.trial_type == "finished_arithmetic"),
        "started_tutorial_markers": sum(1 for row in events if row.trial_type == "started_tutorial_artihmetic"),
        "finished_tutorial_markers": sum(1 for row in events if row.trial_type == "finished_tutorial_arithmetic"),
        "anomalies": anomalies,
    }
    return rows, summary


def _write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build a canonical trial table from BIDS events files. "
            "Each output row is one arithmetic outcome trial with paired cue timing."
        )
    )
    parser.add_argument("--bids-root", required=True, help="Path to BIDS root.")
    parser.add_argument(
        "--task",
        default=None,
        help="Task name. Defaults to inferring from BIDS root name.",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output TSV path. Defaults to analysis_pipeline/reports/trial_table_<bids-root>.tsv.",
    )
    parser.add_argument(
        "--summary-json",
        default=None,
        help="Summary JSON output path. Defaults to <out>_summary.json.",
    )
    parser.add_argument(
        "--trial-duration",
        type=float,
        default=6.0,
        help="Expected calculation window duration in seconds before each cue marker.",
    )
    parser.add_argument(
        "--expected-total-trials",
        type=int,
        default=70,
        help="Expected total trials per subject. Set <=0 to disable.",
    )
    parser.add_argument(
        "--expected-main-trials",
        type=int,
        default=63,
        help="Expected non-tutorial trials per subject. Set <=0 to disable.",
    )
    parser.add_argument(
        "--expected-tutorial-trials",
        type=int,
        default=7,
        help="Expected tutorial trials per subject. Set <=0 to disable.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero code if any anomalies are detected.",
    )
    args = parser.parse_args()

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)

    task = args.task or _task_from_bids_root(bids_root)
    out_path = Path(args.out).resolve() if args.out else _default_out_path(bids_root)
    summary_path = Path(args.summary_json).resolve() if args.summary_json else _default_summary_path(out_path)
    participant_flags = _read_participant_flags(bids_root)

    subject_dirs = sorted(path for path in bids_root.glob("sub-*") if path.is_dir())
    if not subject_dirs:
        raise FileNotFoundError(f"No subject directories found in {bids_root}")

    all_rows: list[dict[str, str]] = []
    subject_summaries: list[dict[str, Any]] = []
    all_anomalies: list[str] = []

    for subject_dir in subject_dirs:
        subject = subject_dir.name
        events_path = subject_dir / "eeg" / f"{subject}_task-{task}_events.tsv"
        if not events_path.exists():
            all_anomalies.append(f"{subject}: Missing events file {events_path.name}.")
            continue

        events = _read_events(events_path)
        subject_rows, subject_summary = _build_subject_trials(
            subject=subject,
            task=task,
            events=events,
            analysis_included=participant_flags.get(subject, "n/a"),
            trial_duration_s=args.trial_duration,
        )
        all_rows.extend(subject_rows)

        if args.expected_total_trials > 0 and subject_summary["total_trials"] != args.expected_total_trials:
            subject_summary["anomalies"].append(
                f"Expected total_trials={args.expected_total_trials}, got {subject_summary['total_trials']}."
            )
        if args.expected_main_trials > 0 and subject_summary["main_trials"] != args.expected_main_trials:
            subject_summary["anomalies"].append(
                f"Expected main_trials={args.expected_main_trials}, got {subject_summary['main_trials']}."
            )
        if (
            args.expected_tutorial_trials > 0
            and subject_summary["tutorial_trials"] != args.expected_tutorial_trials
        ):
            subject_summary["anomalies"].append(
                f"Expected tutorial_trials={args.expected_tutorial_trials}, got {subject_summary['tutorial_trials']}."
            )

        for anomaly in subject_summary["anomalies"]:
            all_anomalies.append(f"{subject}: {anomaly}")
        subject_summaries.append(subject_summary)

    all_rows.sort(key=lambda row: (row["participant_id"], int(row["trial_index_subject"])))
    fieldnames = [
        "participant_id",
        "analysis_included",
        "task",
        "source_events_file",
        "trial_id",
        "trial_index_subject",
        "trial_index_block",
        "trial_index_block_difficulty",
        "block",
        "is_tutorial",
        "difficulty_range",
        "difficulty_qmin",
        "difficulty_qmax",
        "response_accuracy",
        "outcome",
        "cue_event_row",
        "outcome_event_row",
        "cue_marker_onset_s",
        "calc_start_s",
        "calc_end_s",
        "calc_duration_s",
        "answer_start_s",
        "answer_end_s",
        "response_time_s",
        "dropped_samples_calc",
        "dropped_samples_answer",
        "dropped_samples_trial",
        "cue_marker",
        "outcome_marker",
        "cue_marker_stream",
        "outcome_marker_stream",
    ]
    _write_tsv(out_path, fieldnames, all_rows)

    included = [row for row in all_rows if row["analysis_included"] == "true"]
    summary: dict[str, Any] = {
        "bids_root": str(bids_root),
        "task": task,
        "subjects_processed": len(subject_summaries),
        "total_trials": len(all_rows),
        "total_main_trials": sum(1 for row in all_rows if row["block"] == "main"),
        "total_tutorial_trials": sum(1 for row in all_rows if row["block"] == "tutorial"),
        "total_trials_analysis_included": len(included),
        "out_tsv": str(out_path),
        "subject_summaries": subject_summaries,
        "anomalies": all_anomalies,
    }
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote trial table: {out_path}")
    print(f"Wrote summary JSON: {summary_path}")
    print(f"Subjects processed: {len(subject_summaries)}")
    print(
        f"Trials written: {len(all_rows)} "
        f"(main={summary['total_main_trials']}, tutorial={summary['total_tutorial_trials']})"
    )
    print(f"Anomalies: {len(all_anomalies)}")
    if all_anomalies:
        for line in all_anomalies:
            print(f"  - {line}")
    if args.strict and all_anomalies:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

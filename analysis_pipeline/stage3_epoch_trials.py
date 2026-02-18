from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import mne
import numpy as np


@dataclass(frozen=True)
class Segment:
    start_s: float
    end_s: float
    segment_index: int
    is_subwindow: bool
    note: str


@dataclass(frozen=True)
class SubjectModalities:
    subject: str
    eeg_data: np.ndarray | None
    eeg_times: np.ndarray | None
    eeg_sfreq: float | None
    eeg_ch_names: list[str]
    eeg_input: Path | None
    ecg_cols: dict[str, np.ndarray] | None
    ecg_sfreq: float | None
    ecg_input: Path | None
    pupil_cols: dict[str, np.ndarray] | None
    pupil_sfreq: float | None
    pupil_input: Path | None


def _as_float(value: str | None) -> float | None:
    if value is None:
        return None
    text = value.strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if not math.isfinite(number):
        return None
    return number


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


def _format_float(value: float | None, decimals: int = 6) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{decimals}f}"


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_cleaned_root() -> Path:
    return _analysis_root() / "derivatives" / "cleaned"


def _default_epochs_root() -> Path:
    return _analysis_root() / "derivatives" / "epochs"


def _resolve_bids_root(bids_root_arg: str) -> Path:
    direct = Path(bids_root_arg).expanduser()
    if direct.is_absolute():
        return direct.resolve()

    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd

    repo_root = Path(__file__).resolve().parent.parent
    return (repo_root / direct).resolve()


def _task_from_bids_root(bids_root: Path) -> str:
    lower_name = bids_root.name.lower()
    if "arithmetic" in lower_name:
        return "arithmetic"
    raise ValueError(f"Could not infer task from BIDS root name: {bids_root}")


def _default_trial_table_path(bids_root: Path) -> Path:
    return _reports_dir() / f"trial_table_{bids_root.name}.tsv"


def _default_manifest_path() -> Path:
    return _reports_dir() / "epoch_manifest.tsv"


def _default_summary_path() -> Path:
    return _reports_dir() / "epoch_summary.json"


def _default_drop_log_path() -> Path:
    return _reports_dir() / "epoch_drop_log.tsv"


def _read_trial_table(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = [{k: (v or "") for k, v in row.items()} for row in reader]
    if not rows:
        raise ValueError(f"No rows found in trial table: {path}")
    return rows


def _infer_sfreq(times: np.ndarray) -> float | None:
    if times.size < 3:
        return None
    diffs = np.diff(times)
    diffs = diffs[np.isfinite(diffs) & (diffs > 0)]
    if diffs.size == 0:
        return None
    dt = float(np.median(diffs))
    if dt <= 0:
        return None
    return 1.0 / dt


def _read_numeric_tsv(path: Path, required_columns: list[str]) -> dict[str, np.ndarray]:
    if not path.exists():
        raise FileNotFoundError(path)
    data: dict[str, list[float]] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError(f"Missing header in {path}")
        for col in required_columns:
            if col not in reader.fieldnames:
                raise ValueError(f"Missing required column '{col}' in {path}")
            data[col] = []
        for row in reader:
            parsed: dict[str, float] = {}
            ok = True
            for col in required_columns:
                value = _as_float(row.get(col))
                if value is None:
                    ok = False
                    break
                parsed[col] = value
            if ok:
                for col in required_columns:
                    data[col].append(parsed[col])
    return {k: np.asarray(v, dtype=np.float64) for k, v in data.items()}


def _load_subject_modalities(
    subject: str,
    task: str,
    cleaned_root: Path,
) -> SubjectModalities:
    subject_root = cleaned_root / subject

    eeg_input = subject_root / "eeg" / f"{subject}_task-{task}_desc-preproc_eeg_raw.fif"
    eeg_data: np.ndarray | None = None
    eeg_times: np.ndarray | None = None
    eeg_sfreq: float | None = None
    eeg_ch_names: list[str] = []
    if eeg_input.exists():
        raw = mne.io.read_raw_fif(eeg_input, preload=True, verbose="ERROR")
        eeg_data = raw.get_data().astype(np.float32, copy=False)
        eeg_times = raw.times.astype(np.float64, copy=False)
        eeg_sfreq = float(raw.info["sfreq"])
        eeg_ch_names = list(raw.ch_names)

    ecg_input = subject_root / "ecg" / f"{subject}_task-{task}_desc-preproc-ecg.tsv"
    ecg_cols: dict[str, np.ndarray] | None = None
    ecg_sfreq: float | None = None
    if ecg_input.exists():
        ecg_cols = _read_numeric_tsv(
            ecg_input,
            required_columns=["time", "cardiac_raw", "cardiac_broad", "cardiac_peak"],
        )
        ecg_sfreq = _infer_sfreq(ecg_cols["time"])

    pupil_input = subject_root / "pupil" / f"{subject}_task-{task}_desc-preproc-pupil.tsv"
    pupil_cols: dict[str, np.ndarray] | None = None
    pupil_sfreq: float | None = None
    if pupil_input.exists():
        pupil_cols = _read_numeric_tsv(
            pupil_input,
            required_columns=[
                "time",
                "pupil_size_clean",
                "x_coordinate_clean",
                "y_coordinate_clean",
                "confidence_clean",
            ],
        )
        pupil_sfreq = _infer_sfreq(pupil_cols["time"])

    return SubjectModalities(
        subject=subject,
        eeg_data=eeg_data,
        eeg_times=eeg_times,
        eeg_sfreq=eeg_sfreq,
        eeg_ch_names=eeg_ch_names,
        eeg_input=eeg_input if eeg_input.exists() else None,
        ecg_cols=ecg_cols,
        ecg_sfreq=ecg_sfreq,
        ecg_input=ecg_input if ecg_input.exists() else None,
        pupil_cols=pupil_cols,
        pupil_sfreq=pupil_sfreq,
        pupil_input=pupil_input if pupil_input.exists() else None,
    )


def _window_bounds_for_trial(row: dict[str, str], args: argparse.Namespace) -> tuple[float, float]:
    calc_start = _as_float(row.get("calc_start_s"))
    answer_start = _as_float(row.get("answer_start_s"))
    answer_end = _as_float(row.get("answer_end_s"))
    if calc_start is None or answer_start is None or answer_end is None:
        raise ValueError("Missing trial window timings.")

    if args.window_mode == "calc_fixed":
        start_s = calc_start
        end_s = calc_start + args.fixed_window_s
    elif args.window_mode == "full_trial":
        start_s = calc_start
        end_s = answer_end
    elif args.window_mode == "answer_only":
        start_s = answer_start
        end_s = answer_end
    else:
        raise ValueError(f"Unknown window mode: {args.window_mode}")

    if not math.isfinite(start_s) or not math.isfinite(end_s):
        raise ValueError("Non-finite trial window.")
    if end_s <= start_s:
        raise ValueError("Non-positive trial window duration.")
    return start_s, end_s


def _build_segments(start_s: float, end_s: float, args: argparse.Namespace) -> list[Segment]:
    if args.sliding_window_s is None:
        return [
            Segment(
                start_s=start_s,
                end_s=end_s,
                segment_index=0,
                is_subwindow=False,
                note="",
            )
        ]

    window_s = args.sliding_window_s
    step_s = args.sliding_step_s if args.sliding_step_s is not None else window_s
    if window_s <= 0 or step_s <= 0:
        raise ValueError("sliding window and step must be > 0.")
    if (not args.allow_overlap) and (step_s < window_s):
        raise ValueError("Overlap disabled but sliding step is smaller than sliding window.")

    parent_duration = end_s - start_s
    if parent_duration < window_s:
        if args.drop_short_windows:
            return []
        return [
            Segment(
                start_s=start_s,
                end_s=end_s,
                segment_index=0,
                is_subwindow=False,
                note="short_parent_window_kept",
            )
        ]

    out: list[Segment] = []
    i = 0
    cursor = start_s
    eps = 1e-9
    while cursor + window_s <= end_s + eps:
        seg_end = min(cursor + window_s, end_s)
        out.append(
            Segment(
                start_s=cursor,
                end_s=seg_end,
                segment_index=i,
                is_subwindow=True,
                note="",
            )
        )
        i += 1
        cursor += step_s
    return out


def _bool_text(value: bool) -> str:
    return "true" if value else "false"


def _select_indices(times: np.ndarray, start_s: float, end_s: float) -> np.ndarray:
    return np.where((times >= start_s) & (times < end_s))[0]


def _coverage_from_samples(samples: int, duration_s: float, sfreq: float | None) -> float:
    if duration_s <= 0:
        return 0.0
    if sfreq is None or sfreq <= 0:
        return 0.0
    expected = max(1, int(round(duration_s * sfreq)))
    return float(samples) / float(expected)


def _safe_nonnegative(value: float | None) -> float | None:
    if value is None:
        return None
    if not math.isfinite(value):
        return None
    if value < 0:
        return 0.0
    return float(value)


def _dropped_samples_source_for_window_mode(window_mode: str) -> str:
    if window_mode == "calc_fixed":
        return "calc"
    if window_mode == "answer_only":
        return "answer"
    return "trial"


def _segment_dropped_samples(
    trial: dict[str, str],
    segment: Segment,
    parent_start_s: float,
    parent_end_s: float,
    args: argparse.Namespace,
) -> dict[str, str]:
    source = args.dropped_samples_source
    if source == "auto":
        source = _dropped_samples_source_for_window_mode(args.window_mode)

    source_value = _safe_nonnegative(_as_float(trial.get(f"dropped_samples_{source}")))
    source_from = source
    if source_value is None and source != "trial":
        source_value = _safe_nonnegative(_as_float(trial.get("dropped_samples_trial")))
        if source_value is not None:
            source_from = "trial_fallback"

    segment_duration = max(0.0, float(segment.end_s - segment.start_s))
    parent_duration = max(0.0, float(parent_end_s - parent_start_s))
    scaled = False
    used_value = source_value
    if (
        source_value is not None
        and args.scale_dropped_samples_by_segment
        and parent_duration > 0
        and segment_duration >= 0
    ):
        used_value = source_value * (segment_duration / parent_duration)
        scaled = True

    return {
        "source": source_from,
        "source_value": _format_float(source_value, 3),
        "used_value": _format_float(used_value, 3),
        "scaled": _bool_text(scaled),
    }


def _write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _save_npz(path: Path, overwrite: bool, **arrays: Any) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, **arrays)
    return True


def _extract_eeg_epoch(
    modalities: SubjectModalities,
    start_s: float,
    end_s: float,
    out_path: Path,
    dropped_samples_used: float | None,
    dropped_samples_source: str,
    args: argparse.Namespace,
) -> dict[str, str]:
    if modalities.eeg_data is None or modalities.eeg_times is None:
        return {
            "has": "false",
            "keep": "false",
            "reason": "missing_input",
            "samples": "0",
            "sfreq_hz": "n/a",
            "coverage": "0.000",
            "file": "",
            "dropped_samples_used": "n/a",
            "dropped_samples_threshold": _format_float(args.max_dropped_samples_eeg, 3),
            "dropped_samples_source": dropped_samples_source,
            "dropped_samples_triggered": "false",
        }

    idx = _select_indices(modalities.eeg_times, start_s, end_s)
    duration = end_s - start_s
    samples = int(idx.size)
    coverage = _coverage_from_samples(samples, duration, modalities.eeg_sfreq)
    reason = ""
    keep = True
    if samples < 2:
        keep = False
        reason = "too_few_samples"
    elif coverage < args.min_coverage:
        keep = False
        reason = "low_coverage"
    elif (
        args.max_dropped_samples_eeg is not None
        and dropped_samples_used is not None
        and dropped_samples_used > args.max_dropped_samples_eeg
    ):
        keep = False
        reason = "dropped_samples_threshold"

    saved = False
    if keep:
        t_abs = modalities.eeg_times[idx].astype(np.float64, copy=False)
        t_rel = t_abs - float(start_s)
        x = modalities.eeg_data[:, idx].astype(np.float32, copy=False)
        saved = _save_npz(
            out_path,
            overwrite=args.overwrite,
            time=t_rel,
            time_abs=t_abs,
            data=x,
        )
        if not saved and not args.overwrite:
            reason = "file_exists_no_overwrite"

    return {
        "has": "true",
        "keep": _bool_text(keep and (saved or out_path.exists())),
        "reason": reason,
        "samples": str(samples),
        "sfreq_hz": _format_float(modalities.eeg_sfreq, 3),
        "coverage": _format_float(coverage, 3),
        "file": str(out_path) if (keep and (saved or out_path.exists())) else "",
        "dropped_samples_used": _format_float(dropped_samples_used, 3),
        "dropped_samples_threshold": _format_float(args.max_dropped_samples_eeg, 3),
        "dropped_samples_source": dropped_samples_source,
        "dropped_samples_triggered": _bool_text(reason == "dropped_samples_threshold"),
    }


def _extract_ecg_epoch(
    modalities: SubjectModalities,
    start_s: float,
    end_s: float,
    out_path: Path,
    dropped_samples_used: float | None,
    dropped_samples_source: str,
    args: argparse.Namespace,
) -> dict[str, str]:
    if modalities.ecg_cols is None:
        return {
            "has": "false",
            "keep": "false",
            "reason": "missing_input",
            "samples": "0",
            "sfreq_hz": "n/a",
            "coverage": "0.000",
            "file": "",
            "dropped_samples_used": "n/a",
            "dropped_samples_threshold": _format_float(args.max_dropped_samples_ecg, 3),
            "dropped_samples_source": dropped_samples_source,
            "dropped_samples_triggered": "false",
        }

    times = modalities.ecg_cols["time"]
    idx = _select_indices(times, start_s, end_s)
    duration = end_s - start_s
    samples = int(idx.size)
    coverage = _coverage_from_samples(samples, duration, modalities.ecg_sfreq)
    reason = ""
    keep = True

    if args.drop_short_windows and duration < args.min_ecg_window_s:
        keep = False
        reason = "short_window_for_ecg"
    elif samples < 2:
        keep = False
        reason = "too_few_samples"
    elif coverage < args.min_coverage:
        keep = False
        reason = "low_coverage"
    elif (
        args.max_dropped_samples_ecg is not None
        and dropped_samples_used is not None
        and dropped_samples_used > args.max_dropped_samples_ecg
    ):
        keep = False
        reason = "dropped_samples_threshold"

    saved = False
    if keep:
        t_abs = times[idx].astype(np.float64, copy=False)
        t_rel = t_abs - float(start_s)
        saved = _save_npz(
            out_path,
            overwrite=args.overwrite,
            time=t_rel,
            time_abs=t_abs,
            cardiac_raw=modalities.ecg_cols["cardiac_raw"][idx].astype(np.float32, copy=False),
            cardiac_broad=modalities.ecg_cols["cardiac_broad"][idx].astype(np.float32, copy=False),
            cardiac_peak=modalities.ecg_cols["cardiac_peak"][idx].astype(np.float32, copy=False),
        )
        if not saved and not args.overwrite:
            reason = "file_exists_no_overwrite"

    return {
        "has": "true",
        "keep": _bool_text(keep and (saved or out_path.exists())),
        "reason": reason,
        "samples": str(samples),
        "sfreq_hz": _format_float(modalities.ecg_sfreq, 3),
        "coverage": _format_float(coverage, 3),
        "file": str(out_path) if (keep and (saved or out_path.exists())) else "",
        "dropped_samples_used": _format_float(dropped_samples_used, 3),
        "dropped_samples_threshold": _format_float(args.max_dropped_samples_ecg, 3),
        "dropped_samples_source": dropped_samples_source,
        "dropped_samples_triggered": _bool_text(reason == "dropped_samples_threshold"),
    }


def _extract_pupil_epoch(
    modalities: SubjectModalities,
    start_s: float,
    end_s: float,
    out_path: Path,
    args: argparse.Namespace,
) -> dict[str, str]:
    if modalities.pupil_cols is None:
        return {
            "has": "false",
            "keep": "false",
            "reason": "missing_input",
            "samples": "0",
            "sfreq_hz": "n/a",
            "coverage": "0.000",
            "file": "",
        }

    times = modalities.pupil_cols["time"]
    idx = _select_indices(times, start_s, end_s)
    duration = end_s - start_s
    samples = int(idx.size)
    coverage = _coverage_from_samples(samples, duration, modalities.pupil_sfreq)
    reason = ""
    keep = True

    if samples < 2:
        keep = False
        reason = "too_few_samples"
    else:
        valid_mask = (
            np.isfinite(modalities.pupil_cols["pupil_size_clean"][idx])
            & np.isfinite(modalities.pupil_cols["x_coordinate_clean"][idx])
            & np.isfinite(modalities.pupil_cols["y_coordinate_clean"][idx])
            & np.isfinite(modalities.pupil_cols["confidence_clean"][idx])
        )
        valid_ratio = float(np.count_nonzero(valid_mask)) / float(samples)
        effective_coverage = coverage * valid_ratio
        if effective_coverage < args.min_coverage:
            keep = False
            reason = "low_coverage"
        coverage = effective_coverage

    saved = False
    if keep:
        t_abs = times[idx].astype(np.float64, copy=False)
        t_rel = t_abs - float(start_s)
        saved = _save_npz(
            out_path,
            overwrite=args.overwrite,
            time=t_rel,
            time_abs=t_abs,
            pupil_size_clean=modalities.pupil_cols["pupil_size_clean"][idx].astype(np.float32, copy=False),
            x_coordinate_clean=modalities.pupil_cols["x_coordinate_clean"][idx].astype(np.float32, copy=False),
            y_coordinate_clean=modalities.pupil_cols["y_coordinate_clean"][idx].astype(np.float32, copy=False),
            confidence_clean=modalities.pupil_cols["confidence_clean"][idx].astype(np.float32, copy=False),
        )
        if not saved and not args.overwrite:
            reason = "file_exists_no_overwrite"

    return {
        "has": "true",
        "keep": _bool_text(keep and (saved or out_path.exists())),
        "reason": reason,
        "samples": str(samples),
        "sfreq_hz": _format_float(modalities.pupil_sfreq, 3),
        "coverage": _format_float(coverage, 3),
        "file": str(out_path) if (keep and (saved or out_path.exists())) else "",
    }


def _subject_list(rows: list[dict[str, str]], subset: set[str] | None) -> list[str]:
    subjects = sorted({row.get("participant_id", "").strip() for row in rows if row.get("participant_id")})
    if subset is None:
        return subjects
    return [s for s in subjects if s in subset]


def _write_subject_modality_metadata(
    subject: str,
    task: str,
    modalities: SubjectModalities,
    out_subject_root: Path,
    args: argparse.Namespace,
) -> None:
    meta_common = {
        "subject": subject,
        "task": task,
        "window_mode": args.window_mode,
        "fixed_window_s": args.fixed_window_s,
        "min_coverage": args.min_coverage,
        "max_dropped_samples_eeg": args.max_dropped_samples_eeg,
        "max_dropped_samples_ecg": args.max_dropped_samples_ecg,
        "dropped_samples_source": args.dropped_samples_source,
        "scale_dropped_samples_by_segment": args.scale_dropped_samples_by_segment,
        "sliding_window_s": args.sliding_window_s,
        "sliding_step_s": args.sliding_step_s,
        "allow_overlap": args.allow_overlap,
        "drop_short_windows": args.drop_short_windows,
        "min_ecg_window_s": args.min_ecg_window_s,
    }

    if modalities.eeg_data is not None:
        eeg_meta = {
            **meta_common,
            "input": str(modalities.eeg_input),
            "n_channels": modalities.eeg_data.shape[0],
            "sfreq_hz": modalities.eeg_sfreq,
            "ch_names": modalities.eeg_ch_names,
        }
        path = out_subject_root / "eeg" / f"{subject}_task-{task}_desc-epochs-eeg_meta.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(eeg_meta, indent=2) + "\n", encoding="utf-8")

    if modalities.ecg_cols is not None:
        ecg_meta = {
            **meta_common,
            "input": str(modalities.ecg_input),
            "sfreq_hz": modalities.ecg_sfreq,
            "columns": ["cardiac_raw", "cardiac_broad", "cardiac_peak"],
        }
        path = out_subject_root / "ecg" / f"{subject}_task-{task}_desc-epochs-ecg_meta.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(ecg_meta, indent=2) + "\n", encoding="utf-8")

    if modalities.pupil_cols is not None:
        pupil_meta = {
            **meta_common,
            "input": str(modalities.pupil_input),
            "sfreq_hz": modalities.pupil_sfreq,
            "columns": [
                "pupil_size_clean",
                "x_coordinate_clean",
                "y_coordinate_clean",
                "confidence_clean",
            ],
        }
        path = out_subject_root / "pupil" / f"{subject}_task-{task}_desc-epochs-pupil_meta.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(pupil_meta, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 3 trial epoching from canonical trial table. "
            "Creates modality-specific epoch files and a keep/drop manifest."
        )
    )
    parser.add_argument("--bids-root", required=True, help="Path to BIDS root.")
    parser.add_argument("--task", default=None, help="Task name (default: infer from BIDS root).")
    parser.add_argument(
        "--trial-table",
        default=None,
        help="Path to canonical trial table TSV (default: analysis_pipeline/reports/trial_table_<bids_root>.tsv).",
    )
    parser.add_argument(
        "--cleaned-root",
        default=None,
        help="Path to cleaned derivatives root (default: analysis_pipeline/derivatives/cleaned).",
    )
    parser.add_argument(
        "--out-root",
        default=None,
        help="Path to epoch derivatives root (default: analysis_pipeline/derivatives/epochs).",
    )
    parser.add_argument(
        "--manifest-out",
        default=None,
        help="Output TSV for global epoch manifest (default: analysis_pipeline/reports/epoch_manifest.tsv).",
    )
    parser.add_argument(
        "--summary-json",
        default=None,
        help="Output JSON for epoch summary (default: analysis_pipeline/reports/epoch_summary.json).",
    )
    parser.add_argument(
        "--drop-log-out",
        default=None,
        help="Output TSV with dropped EEG/ECG segments (default: analysis_pipeline/reports/epoch_drop_log.tsv).",
    )
    parser.add_argument(
        "--window-mode",
        choices=["calc_fixed", "full_trial", "answer_only"],
        default="calc_fixed",
    )
    parser.add_argument("--fixed-window-s", type=float, default=6.0)
    parser.add_argument("--min-coverage", type=float, default=0.80)
    parser.add_argument(
        "--max-dropped-samples-eeg",
        type=float,
        default=None,
        help="Optional max dropped-sample estimate per EEG segment; segment is dropped when exceeded.",
    )
    parser.add_argument(
        "--max-dropped-samples-ecg",
        type=float,
        default=None,
        help="Optional max dropped-sample estimate per ECG segment; segment is dropped when exceeded.",
    )
    parser.add_argument(
        "--dropped-samples-source",
        choices=["auto", "calc", "answer", "trial"],
        default="auto",
        help="Dropped-sample column source (auto picks by window mode).",
    )
    parser.add_argument(
        "--scale-dropped-samples-by-segment",
        dest="scale_dropped_samples_by_segment",
        action="store_true",
        default=True,
        help="Scale dropped-sample counts by segment duration relative to parent window (default: true).",
    )
    parser.add_argument(
        "--no-scale-dropped-samples-by-segment",
        dest="scale_dropped_samples_by_segment",
        action="store_false",
        help="Disable dropped-sample scaling; apply full source count to each segment.",
    )
    parser.add_argument("--sliding-window-s", type=float, default=None)
    parser.add_argument("--sliding-step-s", type=float, default=None)
    parser.add_argument("--allow-overlap", action="store_true")
    parser.add_argument(
        "--drop-short-windows",
        dest="drop_short_windows",
        action="store_true",
        default=True,
        help="Drop parent windows shorter than sliding window length; also drop short ECG windows.",
    )
    parser.add_argument(
        "--keep-short-windows",
        dest="drop_short_windows",
        action="store_false",
        help="Keep short windows and mark them in notes.",
    )
    parser.add_argument(
        "--min-ecg-window-s",
        type=float,
        default=4.0,
        help="Minimum epoch duration for ECG when --drop-short-windows is enabled.",
    )
    parser.add_argument(
        "--subjects",
        nargs="*",
        default=None,
        help="Optional subset of subject IDs (e.g., sub-001 sub-003).",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing epoch files.")
    args = parser.parse_args()

    if args.fixed_window_s <= 0:
        raise ValueError("--fixed-window-s must be > 0.")
    if args.min_coverage <= 0 or args.min_coverage > 1:
        raise ValueError("--min-coverage must be in (0, 1].")
    if args.min_ecg_window_s <= 0:
        raise ValueError("--min-ecg-window-s must be > 0.")
    if args.max_dropped_samples_eeg is not None and args.max_dropped_samples_eeg < 0:
        raise ValueError("--max-dropped-samples-eeg must be >= 0 when provided.")
    if args.max_dropped_samples_ecg is not None and args.max_dropped_samples_ecg < 0:
        raise ValueError("--max-dropped-samples-ecg must be >= 0 when provided.")

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)
    task = args.task or _task_from_bids_root(bids_root)

    trial_table_path = Path(args.trial_table).resolve() if args.trial_table else _default_trial_table_path(bids_root)
    cleaned_root = Path(args.cleaned_root).resolve() if args.cleaned_root else _default_cleaned_root()
    out_root = Path(args.out_root).resolve() if args.out_root else _default_epochs_root()
    manifest_out = Path(args.manifest_out).resolve() if args.manifest_out else _default_manifest_path()
    summary_out = Path(args.summary_json).resolve() if args.summary_json else _default_summary_path()
    drop_log_out = Path(args.drop_log_out).resolve() if args.drop_log_out else _default_drop_log_path()

    rows = _read_trial_table(trial_table_path)
    requested_subjects = set(args.subjects) if args.subjects else None
    subjects = _subject_list(rows, requested_subjects)
    if not subjects:
        raise FileNotFoundError("No subject rows found after subject filtering.")

    rows_by_subject: dict[str, list[dict[str, str]]] = {subject: [] for subject in subjects}
    for row in rows:
        subject = (row.get("participant_id") or "").strip()
        if subject in rows_by_subject:
            rows_by_subject[subject].append(row)
    for subject in subjects:
        rows_by_subject[subject].sort(
            key=lambda r: (_as_int(r.get("trial_index_subject")) or 0, r.get("trial_id", ""))
        )

    manifest_rows: list[dict[str, str]] = []
    subject_summary_rows: list[dict[str, str]] = []

    for subject in subjects:
        subject_rows = rows_by_subject[subject]
        modalities = _load_subject_modalities(subject, task, cleaned_root)
        subject_out = out_root / subject
        _write_subject_modality_metadata(subject, task, modalities, subject_out, args)

        subject_manifest: list[dict[str, str]] = []
        subject_skipped_trials = 0
        subject_segment_count = 0

        for trial in subject_rows:
            trial_id = trial.get("trial_id", "").strip()
            if not trial_id:
                continue

            try:
                parent_start_s, parent_end_s = _window_bounds_for_trial(trial, args)
            except Exception as e:
                subject_skipped_trials += 1
                manifest_rows.append(
                    {
                        "participant_id": subject,
                        "analysis_included": (trial.get("analysis_included") or "n/a").strip().lower(),
                        "task": trial.get("task", task),
                        "trial_id": trial_id,
                        "trial_index_subject": trial.get("trial_index_subject", ""),
                        "trial_index_block": trial.get("trial_index_block", ""),
                        "block": trial.get("block", ""),
                        "is_tutorial": trial.get("is_tutorial", ""),
                        "difficulty_range": trial.get("difficulty_range", ""),
                        "response_accuracy": trial.get("response_accuracy", ""),
                        "outcome": trial.get("outcome", ""),
                        "window_mode": args.window_mode,
                        "parent_window_start_s": "n/a",
                        "parent_window_end_s": "n/a",
                        "parent_window_duration_s": "n/a",
                        "segment_index": "n/a",
                        "is_subwindow": "false",
                        "epoch_id": "",
                        "epoch_start_s": "n/a",
                        "epoch_end_s": "n/a",
                        "epoch_duration_s": "n/a",
                        "dropped_samples_source": "n/a",
                        "dropped_samples_source_value": "n/a",
                        "dropped_samples_segment_used": "n/a",
                        "dropped_samples_segment_scaled": "false",
                        "has_eeg": "false",
                        "eeg_keep": "false",
                        "eeg_drop_reason": "trial_window_parse_error",
                        "eeg_samples": "0",
                        "eeg_sfreq_hz": "n/a",
                        "eeg_coverage": "0.000",
                        "eeg_dropped_samples_used": "n/a",
                        "eeg_dropped_samples_threshold": _format_float(args.max_dropped_samples_eeg, 3),
                        "eeg_dropped_samples_source": "n/a",
                        "eeg_drop_due_dropped_samples": "false",
                        "eeg_epoch_file": "",
                        "has_ecg": "false",
                        "ecg_keep": "false",
                        "ecg_drop_reason": "trial_window_parse_error",
                        "ecg_samples": "0",
                        "ecg_sfreq_hz": "n/a",
                        "ecg_coverage": "0.000",
                        "ecg_dropped_samples_used": "n/a",
                        "ecg_dropped_samples_threshold": _format_float(args.max_dropped_samples_ecg, 3),
                        "ecg_dropped_samples_source": "n/a",
                        "ecg_drop_due_dropped_samples": "false",
                        "ecg_epoch_file": "",
                        "has_pupil": "false",
                        "pupil_keep": "false",
                        "pupil_drop_reason": "trial_window_parse_error",
                        "pupil_samples": "0",
                        "pupil_sfreq_hz": "n/a",
                        "pupil_coverage": "0.000",
                        "pupil_epoch_file": "",
                        "keep_multimodal": "false",
                        "notes": f"trial_error:{e}",
                    }
                )
                continue

            segments = _build_segments(parent_start_s, parent_end_s, args)
            if not segments:
                subject_skipped_trials += 1
                manifest_rows.append(
                    {
                        "participant_id": subject,
                        "analysis_included": (trial.get("analysis_included") or "n/a").strip().lower(),
                        "task": trial.get("task", task),
                        "trial_id": trial_id,
                        "trial_index_subject": trial.get("trial_index_subject", ""),
                        "trial_index_block": trial.get("trial_index_block", ""),
                        "block": trial.get("block", ""),
                        "is_tutorial": trial.get("is_tutorial", ""),
                        "difficulty_range": trial.get("difficulty_range", ""),
                        "response_accuracy": trial.get("response_accuracy", ""),
                        "outcome": trial.get("outcome", ""),
                        "window_mode": args.window_mode,
                        "parent_window_start_s": _format_float(parent_start_s),
                        "parent_window_end_s": _format_float(parent_end_s),
                        "parent_window_duration_s": _format_float(parent_end_s - parent_start_s),
                        "segment_index": "n/a",
                        "is_subwindow": "false",
                        "epoch_id": "",
                        "epoch_start_s": "n/a",
                        "epoch_end_s": "n/a",
                        "epoch_duration_s": "n/a",
                        "dropped_samples_source": "n/a",
                        "dropped_samples_source_value": "n/a",
                        "dropped_samples_segment_used": "n/a",
                        "dropped_samples_segment_scaled": "false",
                        "has_eeg": _bool_text(modalities.eeg_data is not None),
                        "eeg_keep": "false",
                        "eeg_drop_reason": "short_parent_window",
                        "eeg_samples": "0",
                        "eeg_sfreq_hz": _format_float(modalities.eeg_sfreq, 3),
                        "eeg_coverage": "0.000",
                        "eeg_dropped_samples_used": "n/a",
                        "eeg_dropped_samples_threshold": _format_float(args.max_dropped_samples_eeg, 3),
                        "eeg_dropped_samples_source": "n/a",
                        "eeg_drop_due_dropped_samples": "false",
                        "eeg_epoch_file": "",
                        "has_ecg": _bool_text(modalities.ecg_cols is not None),
                        "ecg_keep": "false",
                        "ecg_drop_reason": "short_parent_window",
                        "ecg_samples": "0",
                        "ecg_sfreq_hz": _format_float(modalities.ecg_sfreq, 3),
                        "ecg_coverage": "0.000",
                        "ecg_dropped_samples_used": "n/a",
                        "ecg_dropped_samples_threshold": _format_float(args.max_dropped_samples_ecg, 3),
                        "ecg_dropped_samples_source": "n/a",
                        "ecg_drop_due_dropped_samples": "false",
                        "ecg_epoch_file": "",
                        "has_pupil": _bool_text(modalities.pupil_cols is not None),
                        "pupil_keep": "false",
                        "pupil_drop_reason": "short_parent_window",
                        "pupil_samples": "0",
                        "pupil_sfreq_hz": _format_float(modalities.pupil_sfreq, 3),
                        "pupil_coverage": "0.000",
                        "pupil_epoch_file": "",
                        "keep_multimodal": "false",
                        "notes": "segments_empty",
                    }
                )
                continue

            for segment in segments:
                epoch_id = f"{trial_id}_seg-{segment.segment_index:03d}"
                eeg_out = subject_out / "eeg" / f"{epoch_id}_eeg.npz"
                ecg_out = subject_out / "ecg" / f"{epoch_id}_ecg.npz"
                pupil_out = subject_out / "pupil" / f"{epoch_id}_pupil.npz"

                segment_drop = _segment_dropped_samples(
                    trial=trial,
                    segment=segment,
                    parent_start_s=parent_start_s,
                    parent_end_s=parent_end_s,
                    args=args,
                )
                drop_used_value = _as_float(segment_drop["used_value"])
                drop_source = segment_drop["source"]

                eeg_result = _extract_eeg_epoch(
                    modalities,
                    segment.start_s,
                    segment.end_s,
                    eeg_out,
                    dropped_samples_used=drop_used_value,
                    dropped_samples_source=drop_source,
                    args=args,
                )
                ecg_result = _extract_ecg_epoch(
                    modalities,
                    segment.start_s,
                    segment.end_s,
                    ecg_out,
                    dropped_samples_used=drop_used_value,
                    dropped_samples_source=drop_source,
                    args=args,
                )
                pupil_result = _extract_pupil_epoch(modalities, segment.start_s, segment.end_s, pupil_out, args)

                keep_multimodal = (
                    eeg_result["keep"] == "true"
                    and ecg_result["keep"] == "true"
                    and pupil_result["keep"] == "true"
                )

                line = {
                    "participant_id": subject,
                    "analysis_included": (trial.get("analysis_included") or "n/a").strip().lower(),
                    "task": trial.get("task", task),
                    "trial_id": trial_id,
                    "trial_index_subject": trial.get("trial_index_subject", ""),
                    "trial_index_block": trial.get("trial_index_block", ""),
                    "block": trial.get("block", ""),
                    "is_tutorial": trial.get("is_tutorial", ""),
                    "difficulty_range": trial.get("difficulty_range", ""),
                    "response_accuracy": trial.get("response_accuracy", ""),
                    "outcome": trial.get("outcome", ""),
                    "window_mode": args.window_mode,
                    "parent_window_start_s": _format_float(parent_start_s),
                    "parent_window_end_s": _format_float(parent_end_s),
                    "parent_window_duration_s": _format_float(parent_end_s - parent_start_s),
                    "segment_index": str(segment.segment_index),
                    "is_subwindow": _bool_text(segment.is_subwindow),
                    "epoch_id": epoch_id,
                    "epoch_start_s": _format_float(segment.start_s),
                    "epoch_end_s": _format_float(segment.end_s),
                    "epoch_duration_s": _format_float(segment.end_s - segment.start_s),
                    "dropped_samples_source": segment_drop["source"],
                    "dropped_samples_source_value": segment_drop["source_value"],
                    "dropped_samples_segment_used": segment_drop["used_value"],
                    "dropped_samples_segment_scaled": segment_drop["scaled"],
                    "has_eeg": eeg_result["has"],
                    "eeg_keep": eeg_result["keep"],
                    "eeg_drop_reason": eeg_result["reason"],
                    "eeg_samples": eeg_result["samples"],
                    "eeg_sfreq_hz": eeg_result["sfreq_hz"],
                    "eeg_coverage": eeg_result["coverage"],
                    "eeg_dropped_samples_used": eeg_result["dropped_samples_used"],
                    "eeg_dropped_samples_threshold": eeg_result["dropped_samples_threshold"],
                    "eeg_dropped_samples_source": eeg_result["dropped_samples_source"],
                    "eeg_drop_due_dropped_samples": eeg_result["dropped_samples_triggered"],
                    "eeg_epoch_file": eeg_result["file"],
                    "has_ecg": ecg_result["has"],
                    "ecg_keep": ecg_result["keep"],
                    "ecg_drop_reason": ecg_result["reason"],
                    "ecg_samples": ecg_result["samples"],
                    "ecg_sfreq_hz": ecg_result["sfreq_hz"],
                    "ecg_coverage": ecg_result["coverage"],
                    "ecg_dropped_samples_used": ecg_result["dropped_samples_used"],
                    "ecg_dropped_samples_threshold": ecg_result["dropped_samples_threshold"],
                    "ecg_dropped_samples_source": ecg_result["dropped_samples_source"],
                    "ecg_drop_due_dropped_samples": ecg_result["dropped_samples_triggered"],
                    "ecg_epoch_file": ecg_result["file"],
                    "has_pupil": pupil_result["has"],
                    "pupil_keep": pupil_result["keep"],
                    "pupil_drop_reason": pupil_result["reason"],
                    "pupil_samples": pupil_result["samples"],
                    "pupil_sfreq_hz": pupil_result["sfreq_hz"],
                    "pupil_coverage": pupil_result["coverage"],
                    "pupil_epoch_file": pupil_result["file"],
                    "keep_multimodal": _bool_text(keep_multimodal),
                    "notes": segment.note,
                }
                manifest_rows.append(line)
                subject_manifest.append(line)
                subject_segment_count += 1

        if subject_manifest:
            subject_manifest_path = subject_out / f"{subject}_epoch_manifest.tsv"
            _write_tsv(subject_manifest_path, list(subject_manifest[0].keys()), subject_manifest)
        subject_summary_rows.append(
            {
                "participant_id": subject,
                "trials_in_table": str(len(subject_rows)),
                "segments_written": str(subject_segment_count),
                "skipped_trials": str(subject_skipped_trials),
                "eeg_kept": str(sum(1 for r in subject_manifest if r["eeg_keep"] == "true")),
                "eeg_dropped": str(sum(1 for r in subject_manifest if r["eeg_keep"] == "false")),
                "eeg_drop_due_dropped_samples": str(
                    sum(1 for r in subject_manifest if r.get("eeg_drop_due_dropped_samples") == "true")
                ),
                "ecg_kept": str(sum(1 for r in subject_manifest if r["ecg_keep"] == "true")),
                "ecg_dropped": str(sum(1 for r in subject_manifest if r["ecg_keep"] == "false")),
                "ecg_drop_due_dropped_samples": str(
                    sum(1 for r in subject_manifest if r.get("ecg_drop_due_dropped_samples") == "true")
                ),
                "pupil_kept": str(sum(1 for r in subject_manifest if r["pupil_keep"] == "true")),
                "multimodal_kept": str(sum(1 for r in subject_manifest if r["keep_multimodal"] == "true")),
            }
        )
        print(
            f"{subject}: segments={subject_segment_count} "
            f"multimodal_kept={subject_summary_rows[-1]['multimodal_kept']}"
        )

    if not manifest_rows:
        raise RuntimeError("No epoch manifest rows were generated.")

    fieldnames = list(manifest_rows[0].keys())
    _write_tsv(manifest_out, fieldnames, manifest_rows)

    drop_log_rows = [
        {
            "participant_id": row.get("participant_id", ""),
            "trial_id": row.get("trial_id", ""),
            "epoch_id": row.get("epoch_id", ""),
            "window_mode": row.get("window_mode", ""),
            "segment_index": row.get("segment_index", ""),
            "epoch_duration_s": row.get("epoch_duration_s", ""),
            "dropped_samples_source": row.get("dropped_samples_source", ""),
            "dropped_samples_source_value": row.get("dropped_samples_source_value", ""),
            "dropped_samples_segment_used": row.get("dropped_samples_segment_used", ""),
            "dropped_samples_segment_scaled": row.get("dropped_samples_segment_scaled", ""),
            "eeg_keep": row.get("eeg_keep", ""),
            "eeg_drop_reason": row.get("eeg_drop_reason", ""),
            "eeg_samples": row.get("eeg_samples", ""),
            "eeg_coverage": row.get("eeg_coverage", ""),
            "eeg_dropped_samples_used": row.get("eeg_dropped_samples_used", ""),
            "eeg_dropped_samples_threshold": row.get("eeg_dropped_samples_threshold", ""),
            "eeg_drop_due_dropped_samples": row.get("eeg_drop_due_dropped_samples", ""),
            "ecg_keep": row.get("ecg_keep", ""),
            "ecg_drop_reason": row.get("ecg_drop_reason", ""),
            "ecg_samples": row.get("ecg_samples", ""),
            "ecg_coverage": row.get("ecg_coverage", ""),
            "ecg_dropped_samples_used": row.get("ecg_dropped_samples_used", ""),
            "ecg_dropped_samples_threshold": row.get("ecg_dropped_samples_threshold", ""),
            "ecg_drop_due_dropped_samples": row.get("ecg_drop_due_dropped_samples", ""),
            "notes": row.get("notes", ""),
        }
        for row in manifest_rows
        if row.get("eeg_keep") == "false" or row.get("ecg_keep") == "false"
    ]
    drop_log_fieldnames = [
        "participant_id",
        "trial_id",
        "epoch_id",
        "window_mode",
        "segment_index",
        "epoch_duration_s",
        "dropped_samples_source",
        "dropped_samples_source_value",
        "dropped_samples_segment_used",
        "dropped_samples_segment_scaled",
        "eeg_keep",
        "eeg_drop_reason",
        "eeg_samples",
        "eeg_coverage",
        "eeg_dropped_samples_used",
        "eeg_dropped_samples_threshold",
        "eeg_drop_due_dropped_samples",
        "ecg_keep",
        "ecg_drop_reason",
        "ecg_samples",
        "ecg_coverage",
        "ecg_dropped_samples_used",
        "ecg_dropped_samples_threshold",
        "ecg_drop_due_dropped_samples",
        "notes",
    ]
    _write_tsv(drop_log_out, drop_log_fieldnames, drop_log_rows)

    drop_reason_counts = {"eeg": {}, "ecg": {}, "pupil": {}}
    for modality in ("eeg", "ecg", "pupil"):
        key = f"{modality}_drop_reason"
        counts: dict[str, int] = {}
        for row in manifest_rows:
            reason = (row.get(key) or "").strip()
            if not reason:
                continue
            counts[reason] = counts.get(reason, 0) + 1
        drop_reason_counts[modality] = dict(sorted(counts.items()))

    summary = {
        "bids_root": str(bids_root),
        "task": task,
        "trial_table": str(trial_table_path),
        "cleaned_root": str(cleaned_root),
        "epochs_root": str(out_root),
        "window_mode": args.window_mode,
        "fixed_window_s": args.fixed_window_s,
        "sliding_window_s": args.sliding_window_s,
        "sliding_step_s": args.sliding_step_s,
        "allow_overlap": args.allow_overlap,
        "min_coverage": args.min_coverage,
        "max_dropped_samples_eeg": args.max_dropped_samples_eeg,
        "max_dropped_samples_ecg": args.max_dropped_samples_ecg,
        "dropped_samples_source": args.dropped_samples_source,
        "scale_dropped_samples_by_segment": args.scale_dropped_samples_by_segment,
        "drop_short_windows": args.drop_short_windows,
        "min_ecg_window_s": args.min_ecg_window_s,
        "subjects_processed": len(subjects),
        "manifest_rows": len(manifest_rows),
        "drop_log_rows": len(drop_log_rows),
        "kept_counts": {
            "eeg": sum(1 for row in manifest_rows if row["eeg_keep"] == "true"),
            "ecg": sum(1 for row in manifest_rows if row["ecg_keep"] == "true"),
            "pupil": sum(1 for row in manifest_rows if row["pupil_keep"] == "true"),
            "multimodal": sum(1 for row in manifest_rows if row["keep_multimodal"] == "true"),
        },
        "dropped_counts": {
            "eeg": sum(1 for row in manifest_rows if row["eeg_keep"] == "false"),
            "ecg": sum(1 for row in manifest_rows if row["ecg_keep"] == "false"),
            "pupil": sum(1 for row in manifest_rows if row["pupil_keep"] == "false"),
            "multimodal": sum(1 for row in manifest_rows if row["keep_multimodal"] == "false"),
        },
        "dropped_samples_rejections": {
            "eeg": sum(1 for row in manifest_rows if row.get("eeg_drop_due_dropped_samples") == "true"),
            "ecg": sum(1 for row in manifest_rows if row.get("ecg_drop_due_dropped_samples") == "true"),
        },
        "drop_reasons": {
            "eeg": sorted({row["eeg_drop_reason"] for row in manifest_rows if row["eeg_drop_reason"]}),
            "ecg": sorted({row["ecg_drop_reason"] for row in manifest_rows if row["ecg_drop_reason"]}),
            "pupil": sorted({row["pupil_drop_reason"] for row in manifest_rows if row["pupil_drop_reason"]}),
        },
        "drop_reason_counts": drop_reason_counts,
        "subject_summary": subject_summary_rows,
        "manifest_out": str(manifest_out),
        "drop_log_out": str(drop_log_out),
    }
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote epoch manifest: {manifest_out}")
    print(f"Wrote epoch drop log: {drop_log_out}")
    print(f"Wrote epoch summary: {summary_out}")


if __name__ == "__main__":
    main()

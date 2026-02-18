from __future__ import annotations

import argparse
import csv
import json
import math
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MODALITY_TABLES: dict[str, str] = {
    "eeg": "features_eeg.tsv",
    "ecg": "features_ecg.tsv",
    "pupil": "features_pupil.tsv",
}

STAGE4_PREFIX_COLUMNS = [
    "participant_id",
    "trial_id",
    "epoch_id",
    "block",
    "difficulty_range",
    "response_accuracy",
    "outcome",
    "window",
    "segment_index",
    "is_subwindow",
    "epoch_start_s",
    "epoch_end_s",
    "epoch_duration_s",
    "baseline_start_s",
    "baseline_end_s",
    "preproc_version",
]

FUSION_METADATA_COLUMNS = [
    "participant_id",
    "analysis_included",
    "trial_id",
    "epoch_id",
    "block",
    "is_tutorial",
    "difficulty_range",
    "difficulty_bin",
    "difficulty_bin_index",
    "target_label",
    "response_accuracy",
    "outcome",
    "window",
    "segment_index",
    "is_subwindow",
    "epoch_start_s",
    "epoch_end_s",
    "epoch_duration_s",
    "dropout_policy",
    "dropout_threshold_value",
    "dropout_keep",
    "dropped_samples_trial",
    "split_group",
]

COMMON_METADATA_COLUMNS = set(
    STAGE4_PREFIX_COLUMNS
    + [
        "analysis_included",
        "is_tutorial",
        "difficulty_bin",
        "difficulty_bin_index",
        "target_label",
        "dropout_policy",
        "dropout_threshold_value",
        "dropout_keep",
        "dropped_samples_trial",
        "split_group",
        "modality",
        "ml_keep",
        "ml_row_id",
        "fused_row_id",
        "has_eeg",
        "has_ecg",
        "has_pupil",
        "modalities_selected",
        "modalities_present",
        "n_modalities_present",
    ]
)

TRIAL_ID_RE = re.compile(r"_trial-(?P<num>\d+)")
DIFFICULTY_RE = re.compile(r"^(?P<qmin>\d+(?:\.\d+)?)-(?P<qmax>\d+(?:\.\d+)?)$")


@dataclass(frozen=True)
class TrialMeta:
    participant_id: str
    analysis_included: str
    block: str
    is_tutorial: bool
    difficulty_range: str
    response_accuracy: str
    outcome: str
    dropped_samples_trial: float | None
    trial_index_subject: int | None


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _features_dir_default() -> Path:
    return _analysis_root() / "features"


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


def _default_fused_out(features_dir: Path) -> Path:
    return features_dir / "features_fused.tsv"


def _default_split_manifest_out(features_dir: Path) -> Path:
    return features_dir / "split_manifest.json"


def _default_summary_out() -> Path:
    return _reports_dir() / "fusion_summary.json"


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


def _bool_text(value: bool) -> str:
    return "true" if value else "false"


def _format_float(value: float | None, decimals: int = 6) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{decimals}f}"


def _read_tsv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return [{k: (v or "") for k, v in row.items()} for row in reader]


def _write_tsv(path: Path, rows: list[dict[str, str]], preferred_prefix: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        fieldnames = preferred_prefix
    else:
        keys = set().union(*(row.keys() for row in rows))
        ordered = [k for k in preferred_prefix if k in keys]
        remaining = sorted(k for k in keys if k not in ordered)
        fieldnames = ordered + remaining

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def _difficulty_bounds(label: str) -> tuple[float | None, float | None]:
    match = DIFFICULTY_RE.match(label.strip())
    if not match:
        return None, None
    return float(match.group("qmin")), float(match.group("qmax"))


def _difficulty_sort_key(label: str) -> tuple[float, float, str]:
    qmin, qmax = _difficulty_bounds(label)
    if qmin is None or qmax is None:
        return float("inf"), float("inf"), label
    return qmin, qmax, label


def _percentile(values: list[float], percentile: float) -> float | None:
    if not values:
        return None
    if percentile <= 0:
        return float(min(values))
    if percentile >= 100:
        return float(max(values))
    sorted_vals = sorted(float(v) for v in values)
    rank = (percentile / 100.0) * (len(sorted_vals) - 1)
    lo = int(math.floor(rank))
    hi = int(math.ceil(rank))
    if lo == hi:
        return sorted_vals[lo]
    frac = rank - lo
    return sorted_vals[lo] + frac * (sorted_vals[hi] - sorted_vals[lo])


def _row_sort_key(row: dict[str, str]) -> tuple[str, int, int, str]:
    participant = (row.get("participant_id") or "").strip()
    trial_id = (row.get("trial_id") or "").strip()
    trial_match = TRIAL_ID_RE.search(trial_id)
    trial_num = int(trial_match.group("num")) if trial_match else 10_000_000
    seg_idx = _as_int(row.get("segment_index")) or 0
    epoch_id = (row.get("epoch_id") or "").strip()
    return participant, trial_num, seg_idx, epoch_id


def _load_trial_index(
    trial_rows: list[dict[str, str]],
    subject_subset: set[str] | None,
) -> dict[str, TrialMeta]:
    index: dict[str, TrialMeta] = {}
    for row in trial_rows:
        trial_id = (row.get("trial_id") or "").strip()
        participant = (row.get("participant_id") or "").strip()
        if not trial_id or not participant:
            continue
        if subject_subset is not None and participant not in subject_subset:
            continue
        block = (row.get("block") or "").strip().lower()
        is_tutorial = (row.get("is_tutorial") or "").strip().lower() == "true" or block == "tutorial"
        index[trial_id] = TrialMeta(
            participant_id=participant,
            analysis_included=((row.get("analysis_included") or "n/a").strip().lower()),
            block="tutorial" if is_tutorial else "main",
            is_tutorial=is_tutorial,
            difficulty_range=(row.get("difficulty_range") or "").strip(),
            response_accuracy=(row.get("response_accuracy") or "").strip(),
            outcome=(row.get("outcome") or "").strip(),
            dropped_samples_trial=_as_float(row.get("dropped_samples_trial")),
            trial_index_subject=_as_int(row.get("trial_index_subject")),
        )
    return index


def _difficulty_bin_map_from_trials(
    trial_index: dict[str, TrialMeta],
    include_tutorial: bool,
) -> dict[str, int]:
    labels = {
        meta.difficulty_range
        for meta in trial_index.values()
        if meta.difficulty_range and (include_tutorial or not meta.is_tutorial)
    }
    ordered = sorted(labels, key=_difficulty_sort_key)
    return {label: idx for idx, label in enumerate(ordered)}


def _compute_subject_dropout_thresholds(
    trial_index: dict[str, TrialMeta],
    include_tutorial: bool,
    percentile: float,
) -> dict[str, float]:
    grouped: dict[str, list[float]] = defaultdict(list)
    for meta in trial_index.values():
        if not include_tutorial and meta.is_tutorial:
            continue
        if meta.dropped_samples_trial is None:
            continue
        grouped[meta.participant_id].append(meta.dropped_samples_trial)

    out: dict[str, float] = {}
    for participant, values in grouped.items():
        threshold = _percentile(values, percentile)
        if threshold is not None:
            out[participant] = threshold
    return out


def _dropout_decision(
    participant_id: str,
    dropped_samples: float | None,
    policy: str,
    absolute_threshold: float,
    subject_thresholds: dict[str, float],
) -> tuple[bool, float | None]:
    if policy == "none":
        return True, None
    if dropped_samples is None:
        return False, None
    if policy == "absolute":
        return dropped_samples <= absolute_threshold, absolute_threshold
    if policy == "subject_percentile":
        threshold = subject_thresholds.get(participant_id)
        if threshold is None:
            return False, None
        return dropped_samples <= threshold, threshold
    raise ValueError(f"Unknown dropout policy: {policy}")


def _mode_feature_columns(rows: list[dict[str, str]]) -> list[str]:
    cols: set[str] = set()
    for row in rows:
        cols.update(row.keys())
    return sorted(col for col in cols if col not in COMMON_METADATA_COLUMNS)


def _primary_epoch_key(row: dict[str, str]) -> tuple[str, str]:
    participant = (row.get("participant_id") or "").strip()
    epoch_id = (row.get("epoch_id") or "").strip()
    if epoch_id:
        return participant, epoch_id
    trial_id = (row.get("trial_id") or "").strip()
    segment = (row.get("segment_index") or "0").strip()
    window = (row.get("window") or "").strip()
    return participant, f"{trial_id}|{segment}|{window}"


def _build_modality_ml_rows(
    modality: str,
    source_rows: list[dict[str, str]],
    trial_index: dict[str, TrialMeta],
    include_tutorial: bool,
    difficulty_map: dict[str, int],
    dropout_policy: str,
    dropout_threshold: float,
    subject_dropout_thresholds: dict[str, float],
    keep_dropout_failed: bool,
) -> tuple[list[dict[str, str]], dict[str, int]]:
    stats = {
        "input_rows": len(source_rows),
        "missing_trial_meta": 0,
        "tutorial_filtered": 0,
        "missing_difficulty": 0,
        "dropout_filtered": 0,
        "rows_out": 0,
    }
    out: list[dict[str, str]] = []
    for row in source_rows:
        trial_id = (row.get("trial_id") or "").strip()
        participant = (row.get("participant_id") or "").strip()
        if not trial_id or not participant:
            stats["missing_trial_meta"] += 1
            continue
        trial_meta = trial_index.get(trial_id)
        if trial_meta is None:
            stats["missing_trial_meta"] += 1
            continue

        if not include_tutorial and trial_meta.is_tutorial:
            stats["tutorial_filtered"] += 1
            continue

        difficulty = trial_meta.difficulty_range or (row.get("difficulty_range") or "").strip()
        if not difficulty or difficulty not in difficulty_map:
            stats["missing_difficulty"] += 1
            continue

        dropout_keep, threshold_used = _dropout_decision(
            participant_id=participant,
            dropped_samples=trial_meta.dropped_samples_trial,
            policy=dropout_policy,
            absolute_threshold=dropout_threshold,
            subject_thresholds=subject_dropout_thresholds,
        )
        if not dropout_keep:
            stats["dropout_filtered"] += 1
            if not keep_dropout_failed:
                continue

        row_out = dict(row)
        row_out["analysis_included"] = trial_meta.analysis_included
        row_out["block"] = trial_meta.block
        row_out["is_tutorial"] = _bool_text(trial_meta.is_tutorial)
        row_out["difficulty_range"] = difficulty
        row_out["difficulty_bin"] = difficulty
        row_out["difficulty_bin_index"] = str(difficulty_map[difficulty])
        row_out["target_label"] = difficulty
        row_out["response_accuracy"] = row_out.get("response_accuracy", "") or trial_meta.response_accuracy
        row_out["outcome"] = row_out.get("outcome", "") or trial_meta.outcome
        row_out["dropout_policy"] = dropout_policy
        row_out["dropout_threshold_value"] = _format_float(threshold_used, 3)
        row_out["dropout_keep"] = _bool_text(dropout_keep)
        row_out["dropped_samples_trial"] = _format_float(trial_meta.dropped_samples_trial, 3)
        row_out["split_group"] = participant
        row_out["modality"] = modality
        row_out["ml_keep"] = _bool_text(dropout_keep)
        out.append(row_out)

    out.sort(key=_row_sort_key)
    for idx, row in enumerate(out, start=1):
        row["ml_row_id"] = f"{modality}_row-{idx:06d}"
    stats["rows_out"] = len(out)
    return out, stats


def _build_fused_rows(
    selected_modalities: list[str],
    modality_rows: dict[str, list[dict[str, str]]],
    feature_columns_by_modality: dict[str, list[str]],
    require_all_selected_modalities: bool,
) -> tuple[list[dict[str, str]], dict[str, int]]:
    modality_maps: dict[str, dict[tuple[str, str], dict[str, str]]] = {}
    duplicate_counts: dict[str, int] = {}
    for modality in selected_modalities:
        keyed: dict[tuple[str, str], dict[str, str]] = {}
        duplicates = 0
        for row in modality_rows.get(modality, []):
            key = _primary_epoch_key(row)
            if key in keyed:
                duplicates += 1
                continue
            keyed[key] = row
        modality_maps[modality] = keyed
        duplicate_counts[modality] = duplicates

    if not selected_modalities:
        return [], duplicate_counts

    key_sets = [set(modality_maps[mod].keys()) for mod in selected_modalities]
    if require_all_selected_modalities:
        final_keys = set.intersection(*key_sets) if key_sets else set()
    else:
        final_keys = set.union(*key_sets) if key_sets else set()

    fused_rows: list[dict[str, str]] = []
    for key in sorted(final_keys):
        available = [mod for mod in selected_modalities if key in modality_maps[mod]]
        if require_all_selected_modalities and len(available) != len(selected_modalities):
            continue
        if not available:
            continue
        base = modality_maps[available[0]][key]
        fused_row: dict[str, str] = {}
        for col in FUSION_METADATA_COLUMNS:
            if col in base:
                fused_row[col] = base[col]

        fused_row["modalities_selected"] = ",".join(selected_modalities)
        fused_row["modalities_present"] = ",".join(available)
        fused_row["n_modalities_present"] = str(len(available))

        for modality in selected_modalities:
            row = modality_maps[modality].get(key)
            fused_row[f"has_{modality}"] = _bool_text(row is not None)
            if row is not None:
                fused_row[f"preproc_version_{modality}"] = row.get("preproc_version", "")
                fused_row[f"baseline_start_s_{modality}"] = row.get("baseline_start_s", "")
                fused_row[f"baseline_end_s_{modality}"] = row.get("baseline_end_s", "")
                for col in feature_columns_by_modality.get(modality, []):
                    fused_row[col] = row.get(col, "n/a")
            else:
                for col in feature_columns_by_modality.get(modality, []):
                    fused_row[col] = "n/a"
        fused_rows.append(fused_row)

    fused_rows.sort(key=_row_sort_key)
    for idx, row in enumerate(fused_rows, start=1):
        row["fused_row_id"] = f"fused_row-{idx:06d}"
    return fused_rows, duplicate_counts


def _dataset_stats(rows: list[dict[str, str]], target_col: str) -> dict[str, Any]:
    participants = sorted({(row.get("participant_id") or "").strip() for row in rows if row.get("participant_id")})
    class_counts = Counter((row.get(target_col) or "").strip() for row in rows if row.get(target_col))
    rows_per_participant = Counter((row.get("participant_id") or "").strip() for row in rows if row.get("participant_id"))
    class_counts_by_participant: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        participant = (row.get("participant_id") or "").strip()
        label = (row.get(target_col) or "").strip()
        if participant and label:
            class_counts_by_participant[participant][label] += 1

    return {
        "rows": len(rows),
        "participants": participants,
        "n_participants": len(participants),
        "class_counts": dict(sorted(class_counts.items(), key=lambda x: _difficulty_sort_key(x[0]))),
        "rows_per_participant": dict(sorted(rows_per_participant.items())),
        "class_counts_by_participant": {
            p: dict(sorted(c.items(), key=lambda x: _difficulty_sort_key(x[0])))
            for p, c in sorted(class_counts_by_participant.items())
        },
    }


def _build_loso_splits(participants: list[str]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if len(participants) < 2:
        return out
    for participant in participants:
        train_participants = [p for p in participants if p != participant]
        out.append(
            {
                "split_id": f"loso_{participant}",
                "strategy": "leave_one_participant_out",
                "test_participants": [participant],
                "train_participants": train_participants,
            }
        )
    return out


def _build_group_holdout_splits(
    participants: list[str],
    fractions: list[float],
    repeats: int,
    random_seed: int,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if len(participants) < 2:
        return out
    for fraction in fractions:
        if fraction <= 0 or fraction >= 1:
            continue
        n_test = int(round(fraction * len(participants)))
        n_test = max(1, min(n_test, len(participants) - 1))
        for rep in range(1, repeats + 1):
            seed = random_seed + int(round(fraction * 1000)) + rep
            rng = random.Random(seed)
            test_participants = sorted(rng.sample(participants, n_test))
            test_set = set(test_participants)
            train_participants = [p for p in participants if p not in test_set]
            out.append(
                {
                    "split_id": f"group_holdout_frac{fraction:.3f}_rep{rep:02d}",
                    "strategy": "group_holdout",
                    "test_fraction": fraction,
                    "repeat_index": rep,
                    "seed": seed,
                    "test_participants": test_participants,
                    "train_participants": train_participants,
                }
            )
    return out


def _build_within_participant_plan(
    primary_stats: dict[str, Any],
    dataset_stats_by_name: dict[str, dict[str, Any]],
    min_within_rows: int,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    participants = list(primary_stats.get("participants", []))
    class_counts_by_participant = primary_stats.get("class_counts_by_participant", {})
    rows_per_participant = primary_stats.get("rows_per_participant", {})
    for participant in participants:
        primary_class_counts = class_counts_by_participant.get(participant, {})
        n_rows_primary = int(rows_per_participant.get(participant, 0))
        n_classes = len(primary_class_counts)
        min_class_support = min(primary_class_counts.values()) if primary_class_counts else 0
        recommended_n_splits = min(5, min_class_support) if n_classes >= 2 else 0
        eligible = (
            n_rows_primary >= min_within_rows
            and n_classes >= 2
            and recommended_n_splits >= 2
        )
        rows_by_dataset = {
            dataset_name: int(stats.get("rows_per_participant", {}).get(participant, 0))
            for dataset_name, stats in dataset_stats_by_name.items()
        }
        out.append(
            {
                "participant_id": participant,
                "rows_primary_dataset": n_rows_primary,
                "rows_by_dataset": rows_by_dataset,
                "class_counts_primary_dataset": primary_class_counts,
                "n_classes_primary_dataset": n_classes,
                "eligible_for_within_participant_cv": eligible,
                "recommended_n_splits": recommended_n_splits if eligible else 0,
                "notes": (
                    ""
                    if eligible
                    else f"Needs >= {min_within_rows} rows and >=2 classes with >=2 samples each class."
                ),
            }
        )
    return out


def _parse_modalities(modalities: list[str]) -> list[str]:
    normalized = [m.strip().lower() for m in modalities if m.strip()]
    if not normalized:
        raise ValueError("At least one modality must be provided.")
    invalid = [m for m in normalized if m not in MODALITY_TABLES]
    if invalid:
        raise ValueError(f"Unknown modalities: {', '.join(sorted(set(invalid)))}")
    deduped = list(dict.fromkeys(normalized))
    return deduped


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 5 multimodal ML table assembly. Builds unimodal ML tables, "
            "a fused multimodal table, and split metadata for per-participant, "
            "leave-one-participant-out, and grouped holdout evaluation."
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
        "--features-dir",
        default=None,
        help="Directory containing Stage 4 feature tables (default: analysis_pipeline/features).",
    )
    parser.add_argument(
        "--modalities",
        nargs="+",
        default=["eeg", "ecg", "pupil"],
        help="Modalities to include (subset of: eeg ecg pupil).",
    )
    parser.add_argument(
        "--include-tutorial",
        action="store_true",
        help="Include tutorial trials. Default excludes tutorial trials.",
    )
    parser.add_argument(
        "--target",
        choices=["difficulty_bin"],
        default="difficulty_bin",
        help="Target label definition. Current supported option: difficulty_bin.",
    )
    parser.add_argument(
        "--dropout-policy",
        choices=["none", "absolute", "subject_percentile"],
        default="absolute",
        help=(
            "Dropout gating policy based on trial_table dropped_samples_trial. "
            "'absolute' uses --dropout-threshold. "
            "'subject_percentile' uses --dropout-percentile."
        ),
    )
    parser.add_argument(
        "--dropout-threshold",
        type=float,
        default=35.0,
        help="Absolute dropped_samples_trial threshold used when --dropout-policy absolute.",
    )
    parser.add_argument(
        "--dropout-percentile",
        type=float,
        default=95.0,
        help="Per-subject percentile used when --dropout-policy subject_percentile.",
    )
    parser.add_argument(
        "--keep-dropout-failed",
        action="store_true",
        help="Keep dropout-failed epochs in outputs but mark dropout_keep=false (default is to drop them).",
    )
    parser.add_argument(
        "--require-all-selected-modalities",
        dest="require_all_selected_modalities",
        action="store_true",
        default=True,
        help="For fused output, keep only epochs present in every selected modality (default: true).",
    )
    parser.add_argument(
        "--allow-partial-modalities",
        dest="require_all_selected_modalities",
        action="store_false",
        help="For fused output, allow epochs missing one or more selected modalities.",
    )
    parser.add_argument(
        "--group-holdout-fracs",
        nargs="*",
        type=float,
        default=[0.10, 0.20],
        help="Participant holdout fractions for grouped split plans (example: 0.1 0.2).",
    )
    parser.add_argument(
        "--group-holdout-repeats",
        type=int,
        default=5,
        help="Number of random repeats per group holdout fraction.",
    )
    parser.add_argument(
        "--random-seed",
        type=int,
        default=42,
        help="Random seed for split planning.",
    )
    parser.add_argument(
        "--min-within-rows",
        type=int,
        default=28,
        help="Minimum rows per participant for within-participant CV eligibility in split manifest.",
    )
    parser.add_argument(
        "--subjects",
        nargs="*",
        default=None,
        help="Optional subset of participant IDs (e.g., sub-001 sub-003).",
    )
    parser.add_argument(
        "--fused-out",
        default=None,
        help="Fused table output TSV path (default: analysis_pipeline/features/features_fused.tsv).",
    )
    parser.add_argument(
        "--split-manifest-out",
        default=None,
        help="Split manifest JSON output path (default: analysis_pipeline/features/split_manifest.json).",
    )
    parser.add_argument(
        "--summary-json",
        default=None,
        help="Fusion summary JSON output path (default: analysis_pipeline/reports/fusion_summary.json).",
    )
    parser.add_argument(
        "--unimodal-tag",
        default="",
        help=(
            "Optional tag appended to unimodal filenames, e.g. --unimodal-tag main_abs35 "
            "writes features_ml_eeg_main_abs35.tsv. Default writes features_ml_<modality>.tsv."
        ),
    )
    args = parser.parse_args()

    if args.dropout_threshold < 0:
        raise ValueError("--dropout-threshold must be >= 0.")
    if args.dropout_percentile <= 0 or args.dropout_percentile >= 100:
        raise ValueError("--dropout-percentile must be within (0, 100).")
    if args.group_holdout_repeats <= 0:
        raise ValueError("--group-holdout-repeats must be > 0.")
    if args.min_within_rows <= 0:
        raise ValueError("--min-within-rows must be > 0.")

    selected_modalities = _parse_modalities(args.modalities)
    subject_subset = set(args.subjects) if args.subjects else None

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)
    task = args.task or _task_from_bids_root(bids_root)
    if task != "arithmetic":
        raise ValueError("This pipeline currently supports the arithmetic task only.")

    features_dir = Path(args.features_dir).resolve() if args.features_dir else _features_dir_default()
    trial_table_path = Path(args.trial_table).resolve() if args.trial_table else _default_trial_table_path(bids_root)
    fused_out = Path(args.fused_out).resolve() if args.fused_out else _default_fused_out(features_dir)
    split_manifest_out = (
        Path(args.split_manifest_out).resolve()
        if args.split_manifest_out
        else _default_split_manifest_out(features_dir)
    )
    summary_out = Path(args.summary_json).resolve() if args.summary_json else _default_summary_out()

    trial_rows = _read_tsv_rows(trial_table_path)
    trial_index = _load_trial_index(trial_rows, subject_subset=subject_subset)
    if not trial_index:
        raise ValueError("No trial metadata rows available after filters.")

    difficulty_map = _difficulty_bin_map_from_trials(
        trial_index=trial_index,
        include_tutorial=args.include_tutorial,
    )
    if not difficulty_map:
        raise ValueError("Could not derive any difficulty bins from the trial table.")

    subject_dropout_thresholds: dict[str, float] = {}
    if args.dropout_policy == "subject_percentile":
        subject_dropout_thresholds = _compute_subject_dropout_thresholds(
            trial_index=trial_index,
            include_tutorial=args.include_tutorial,
            percentile=args.dropout_percentile,
        )

    modality_rows_out: dict[str, list[dict[str, str]]] = {}
    modality_stats: dict[str, dict[str, int]] = {}
    feature_columns_by_modality: dict[str, list[str]] = {}
    unimodal_paths: dict[str, str] = {}
    unimodal_suffix = f"_{args.unimodal_tag.strip()}" if args.unimodal_tag and args.unimodal_tag.strip() else ""

    for modality in selected_modalities:
        source_path = features_dir / MODALITY_TABLES[modality]
        source_rows = _read_tsv_rows(source_path)
        if subject_subset is not None:
            source_rows = [
                row
                for row in source_rows
                if (row.get("participant_id") or "").strip() in subject_subset
            ]
        rows_out, stats = _build_modality_ml_rows(
            modality=modality,
            source_rows=source_rows,
            trial_index=trial_index,
            include_tutorial=args.include_tutorial,
            difficulty_map=difficulty_map,
            dropout_policy=args.dropout_policy,
            dropout_threshold=args.dropout_threshold,
            subject_dropout_thresholds=subject_dropout_thresholds,
            keep_dropout_failed=args.keep_dropout_failed,
        )
        modality_rows_out[modality] = rows_out
        modality_stats[modality] = stats
        feature_columns_by_modality[modality] = _mode_feature_columns(rows_out)

        unimodal_out = features_dir / f"features_ml_{modality}{unimodal_suffix}.tsv"
        unimodal_paths[modality] = str(unimodal_out)
        _write_tsv(
            unimodal_out,
            rows_out,
            preferred_prefix=(
                [
                    "ml_row_id",
                    "modality",
                ]
                + FUSION_METADATA_COLUMNS
                + ["baseline_start_s", "baseline_end_s", "preproc_version", "ml_keep"]
            ),
        )

    fused_rows, duplicate_counts = _build_fused_rows(
        selected_modalities=selected_modalities,
        modality_rows=modality_rows_out,
        feature_columns_by_modality=feature_columns_by_modality,
        require_all_selected_modalities=args.require_all_selected_modalities,
    )
    _write_tsv(
        fused_out,
        fused_rows,
        preferred_prefix=["fused_row_id"] + FUSION_METADATA_COLUMNS,
    )

    dataset_rows_by_name: dict[str, list[dict[str, str]]] = {
        **{modality: rows for modality, rows in modality_rows_out.items()},
        "fused": fused_rows,
    }
    dataset_paths_by_name: dict[str, str] = {
        **unimodal_paths,
        "fused": str(fused_out),
    }
    dataset_stats_by_name = {
        name: _dataset_stats(rows, target_col="target_label")
        for name, rows in dataset_rows_by_name.items()
    }

    primary_dataset_name = "fused" if fused_rows else selected_modalities[0]
    primary_stats = dataset_stats_by_name[primary_dataset_name]
    primary_participants = list(primary_stats.get("participants", []))

    split_manifest = {
        "bids_root": str(bids_root),
        "task": task,
        "target": args.target,
        "target_column": "target_label",
        "difficulty_bins": [
            {"label": label, "index": idx}
            for label, idx in sorted(difficulty_map.items(), key=lambda x: x[1])
        ],
        "include_tutorial": args.include_tutorial,
        "dropout_policy": args.dropout_policy,
        "dropout_threshold": args.dropout_threshold,
        "dropout_percentile": args.dropout_percentile,
        "keep_dropout_failed": args.keep_dropout_failed,
        "modalities_selected": selected_modalities,
        "require_all_selected_modalities": args.require_all_selected_modalities,
        "primary_dataset_for_splits": primary_dataset_name,
        "datasets": {
            name: {
                "path": dataset_paths_by_name[name],
                "rows": stats["rows"],
                "n_participants": stats["n_participants"],
                "participants": stats["participants"],
                "class_counts": stats["class_counts"],
                "rows_per_participant": stats["rows_per_participant"],
            }
            for name, stats in dataset_stats_by_name.items()
        },
        "strategies": {
            "leave_one_participant_out": _build_loso_splits(primary_participants),
            "group_holdout": _build_group_holdout_splits(
                participants=primary_participants,
                fractions=args.group_holdout_fracs,
                repeats=args.group_holdout_repeats,
                random_seed=args.random_seed,
            ),
            "within_participant": _build_within_participant_plan(
                primary_stats=primary_stats,
                dataset_stats_by_name=dataset_stats_by_name,
                min_within_rows=args.min_within_rows,
            ),
        },
    }
    split_manifest_out.parent.mkdir(parents=True, exist_ok=True)
    split_manifest_out.write_text(json.dumps(split_manifest, indent=2) + "\n", encoding="utf-8")

    trial_rows_considered = [
        meta
        for meta in trial_index.values()
        if args.include_tutorial or not meta.is_tutorial
    ]
    dropped_values = [meta.dropped_samples_trial for meta in trial_rows_considered if meta.dropped_samples_trial is not None]

    summary = {
        "bids_root": str(bids_root),
        "task": task,
        "trial_table": str(trial_table_path),
        "features_dir": str(features_dir),
        "target": args.target,
        "include_tutorial": args.include_tutorial,
        "modalities_selected": selected_modalities,
        "dropout_policy": args.dropout_policy,
        "dropout_threshold": args.dropout_threshold,
        "dropout_percentile": args.dropout_percentile,
        "keep_dropout_failed": args.keep_dropout_failed,
        "require_all_selected_modalities": args.require_all_selected_modalities,
        "subjects_filter": sorted(subject_subset) if subject_subset else None,
        "trial_rows_considered": len(trial_rows_considered),
        "trial_drop_samples_distribution": {
            "n": len(dropped_values),
            "p50": _percentile([float(x) for x in dropped_values], 50.0),
            "p90": _percentile([float(x) for x in dropped_values], 90.0),
            "p95": _percentile([float(x) for x in dropped_values], 95.0),
            "p99": _percentile([float(x) for x in dropped_values], 99.0),
            "max": max(dropped_values) if dropped_values else None,
        },
        "modality_stats": modality_stats,
        "modality_duplicate_keys_ignored": duplicate_counts,
        "rows_out": {
            **{modality: len(modality_rows_out[modality]) for modality in selected_modalities},
            "fused": len(fused_rows),
        },
        "dataset_class_counts": {
            name: stats["class_counts"] for name, stats in dataset_stats_by_name.items()
        },
        "outputs": {
            **{f"features_ml_{modality}_tsv": path for modality, path in unimodal_paths.items()},
            "features_fused_tsv": str(fused_out),
            "split_manifest_json": str(split_manifest_out),
        },
    }
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print("Stage 5 complete.")
    for modality in selected_modalities:
        print(f"  Wrote unimodal ML table ({modality}): {unimodal_paths[modality]}")
    print(f"  Wrote fused ML table: {fused_out}")
    print(f"  Wrote split manifest: {split_manifest_out}")
    print(f"  Wrote fusion summary: {summary_out}")


if __name__ == "__main__":
    main()

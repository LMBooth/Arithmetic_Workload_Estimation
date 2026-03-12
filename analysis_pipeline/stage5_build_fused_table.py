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


def _default_epoch_manifest_path() -> Path:
    return _reports_dir() / "epoch_manifest.tsv"


def _verification_stem_from_summary(summary_out: Path) -> str:
    stem = summary_out.stem
    if stem.startswith("fusion_summary"):
        return stem.replace("fusion_summary", "fusion_verification", 1)
    return f"{stem}_verification"


def _default_verification_json_out(summary_out: Path) -> Path:
    return summary_out.with_name(f"{_verification_stem_from_summary(summary_out)}.json")


def _default_verification_md_out(summary_out: Path) -> Path:
    return summary_out.with_name(f"{_verification_stem_from_summary(summary_out)}.md")


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


def _load_modality_subject_filters(
    qc_summary_path: Path | None,
    selected_modalities: list[str],
    subject_subset: set[str] | None,
) -> dict[str, set[str]] | None:
    if qc_summary_path is None:
        return None
    if not qc_summary_path.exists():
        raise FileNotFoundError(qc_summary_path)

    payload = json.loads(qc_summary_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"QC summary is not a JSON object: {qc_summary_path}")

    carry_map = payload.get("subjects_carried_forward_after_qc_by_modality", {}) or {}
    if not isinstance(carry_map, dict) or not carry_map:
        return None

    fallback = set(str(x).strip() for x in (payload.get("subjects_carried_forward_after_qc", []) or []) if str(x).strip())
    filters: dict[str, set[str]] = {}
    for modality in selected_modalities:
        values = carry_map.get(modality)
        if isinstance(values, list):
            modality_subjects = {str(x).strip() for x in values if str(x).strip()}
        else:
            modality_subjects = set(fallback)
        if subject_subset is not None:
            modality_subjects &= set(subject_subset)
        filters[modality] = modality_subjects
    return filters


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
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    stats = {
        "input_rows": len(source_rows),
        "missing_trial_meta": 0,
        "tutorial_filtered": 0,
        "missing_difficulty": 0,
        "dropout_filtered": 0,
        "rows_out": 0,
    }
    dropout_filtered_by_participant: Counter[str] = Counter()
    rows_out_by_participant: Counter[str] = Counter()
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
            dropout_filtered_by_participant[participant] += 1
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
        rows_out_by_participant[participant] += 1

    out.sort(key=_row_sort_key)
    for idx, row in enumerate(out, start=1):
        row["ml_row_id"] = f"{modality}_row-{idx:06d}"
    stats["rows_out"] = len(out)
    stats["dropout_filtered_by_participant"] = dict(sorted(dropout_filtered_by_participant.items()))
    stats["rows_out_by_participant"] = dict(sorted(rows_out_by_participant.items()))
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


def _rows_to_key_map(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    keyed: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        key = _primary_epoch_key(row)
        if not key[0] or not key[1]:
            continue
        if key not in keyed:
            keyed[key] = row
    return keyed


def _rows_for_participants(
    rows_per_participant: dict[str, int],
    participants: list[str],
) -> int:
    return sum(int(rows_per_participant.get(participant, 0)) for participant in participants)


def _markdown_table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    if not rows:
        return "_None_"
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = [
        "| " + " | ".join(str(row.get(col, "")) for col in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, sep, *body])


def _build_fusion_verification(
    *,
    selected_modalities: list[str],
    source_rows_by_modality: dict[str, list[dict[str, str]]],
    modality_rows_out: dict[str, list[dict[str, str]]],
    fused_rows: list[dict[str, str]],
    dataset_stats_by_name: dict[str, dict[str, Any]],
    split_manifest: dict[str, Any],
    require_all_selected_modalities: bool,
    epoch_manifest_rows: list[dict[str, str]] | None,
    epoch_manifest_path: Path | None,
) -> dict[str, Any]:
    source_key_maps = {
        modality: _rows_to_key_map(source_rows_by_modality.get(modality, []))
        for modality in selected_modalities
    }
    ml_key_maps = {
        modality: _rows_to_key_map(modality_rows_out.get(modality, []))
        for modality in selected_modalities
    }
    fused_key_map = _rows_to_key_map(fused_rows)
    selected_key_sets = [set(ml_key_maps[modality].keys()) for modality in selected_modalities]
    selected_intersection = set.intersection(*selected_key_sets) if selected_key_sets else set()
    selected_union = set.union(*selected_key_sets) if selected_key_sets else set()
    source_key_sets = [set(source_key_maps[modality].keys()) for modality in selected_modalities]
    source_intersection = set.intersection(*source_key_sets) if source_key_sets else set()
    source_union = set.union(*source_key_sets) if source_key_sets else set()

    row_counts = {
        modality: {
            "stage4_source_rows": len(source_rows_by_modality.get(modality, [])),
            "stage5_ml_rows": len(modality_rows_out.get(modality, [])),
            "rows_lost_before_fusion": len(source_rows_by_modality.get(modality, []))
            - len(modality_rows_out.get(modality, [])),
            "rows_lost_when_fused": len(set(ml_key_maps[modality].keys()) - set(fused_key_map.keys())),
        }
        for modality in selected_modalities
    }
    row_counts["fused"] = {
        "stage4_source_rows": "n/a",
        "stage5_ml_rows": len(fused_rows),
        "rows_lost_before_fusion": "n/a",
        "rows_lost_when_fused": 0,
    }

    warnings: list[str] = []
    if require_all_selected_modalities and set(fused_key_map.keys()) != selected_intersection:
        warnings.append(
            "Fused rows do not match the intersection of Stage 5 unimodal rows, despite require_all_selected_modalities=true."
        )
    if not require_all_selected_modalities and not set(fused_key_map.keys()).issubset(selected_union):
        warnings.append("Fused rows include keys outside the union of selected unimodal rows.")
    stage5_ml_keys_identical_across_modalities = len({frozenset(keys) for keys in selected_key_sets}) <= 1

    epoch_manifest_consistency: dict[str, Any] = {
        "available": epoch_manifest_rows is not None,
        "epoch_manifest_path": str(epoch_manifest_path) if epoch_manifest_path else None,
    }
    if epoch_manifest_rows is not None:
        manifest_key_map = _rows_to_key_map(epoch_manifest_rows)
        expected_kept_rows_by_modality: dict[str, int] = {}
        source_contains_rows_not_kept: dict[str, int] = {}
        manifest_kept_rows_missing_from_source: dict[str, int] = {}
        sample_source_rows_not_kept: dict[str, list[dict[str, Any]]] = {}

        for modality in selected_modalities:
            keep_col = f"{modality}_keep"
            reason_col = f"{modality}_drop_reason"
            kept_keys = {
                key
                for key, row in manifest_key_map.items()
                if (row.get(keep_col) or "").strip().lower() == "true"
            }
            source_keys = set(source_key_maps[modality].keys())
            source_not_kept = sorted(source_keys - kept_keys)
            kept_missing = sorted(kept_keys - source_keys)
            expected_kept_rows_by_modality[modality] = len(kept_keys)
            source_contains_rows_not_kept[modality] = len(source_not_kept)
            manifest_kept_rows_missing_from_source[modality] = len(kept_missing)
            sample_rows: list[dict[str, Any]] = []
            for key in source_not_kept[:10]:
                manifest_row = manifest_key_map.get(key, {})
                sample_rows.append(
                    {
                        "participant_id": key[0],
                        "epoch_id": key[1],
                        "keep_flag": manifest_row.get(keep_col, ""),
                        "drop_reason": manifest_row.get(reason_col, ""),
                    }
                )
            sample_source_rows_not_kept[modality] = sample_rows

            if len(source_rows_by_modality.get(modality, [])) != len(kept_keys):
                warnings.append(
                    f"Stage 4 {modality} table row count ({len(source_rows_by_modality.get(modality, []))}) "
                    f"does not match epoch-manifest keep count ({len(kept_keys)})."
                )
            if source_not_kept:
                warnings.append(
                    f"Stage 4 {modality} table contains {len(source_not_kept)} rows whose {keep_col}=false in the current epoch manifest."
                )
            if kept_missing:
                warnings.append(
                    f"Stage 4 {modality} table is missing {len(kept_missing)} rows whose {keep_col}=true in the current epoch manifest."
                )

        epoch_manifest_consistency.update(
            {
                "manifest_rows": len(epoch_manifest_rows),
                "expected_kept_rows_by_modality": expected_kept_rows_by_modality,
                "source_contains_rows_not_kept_in_epoch_manifest": source_contains_rows_not_kept,
                "manifest_kept_rows_missing_from_source": manifest_kept_rows_missing_from_source,
                "sample_source_rows_not_kept": sample_source_rows_not_kept,
            }
        )

    dataset_rows_per_participant = {
        name: {str(k): int(v) for k, v in stats.get("rows_per_participant", {}).items()}
        for name, stats in dataset_stats_by_name.items()
    }

    split_examples: dict[str, list[dict[str, Any]]] = {
        "leave_one_participant_out": [],
        "group_holdout": [],
        "within_participant": [],
    }
    fused_less_than_unimodal_in_any_split = False
    for split in split_manifest.get("strategies", {}).get("leave_one_participant_out", [])[:3]:
        train_participants = [str(x) for x in split.get("train_participants", [])]
        test_participants = [str(x) for x in split.get("test_participants", [])]
        rows_by_dataset = {
            name: {
                "train": _rows_for_participants(rows_per, train_participants),
                "test": _rows_for_participants(rows_per, test_participants),
            }
            for name, rows_per in dataset_rows_per_participant.items()
        }
        split_examples["leave_one_participant_out"].append(
            {"split_id": split.get("split_id", ""), "rows_by_dataset": rows_by_dataset}
        )
    for split in split_manifest.get("strategies", {}).get("group_holdout", [])[:2]:
        train_participants = [str(x) for x in split.get("train_participants", [])]
        test_participants = [str(x) for x in split.get("test_participants", [])]
        rows_by_dataset = {
            name: {
                "train": _rows_for_participants(rows_per, train_participants),
                "test": _rows_for_participants(rows_per, test_participants),
            }
            for name, rows_per in dataset_rows_per_participant.items()
        }
        split_examples["group_holdout"].append(
            {"split_id": split.get("split_id", ""), "rows_by_dataset": rows_by_dataset}
        )
    for row in split_manifest.get("strategies", {}).get("within_participant", [])[:5]:
        split_examples["within_participant"].append(
            {
                "participant_id": row.get("participant_id", ""),
                "rows_by_dataset": row.get("rows_by_dataset", {}),
            }
        )
    for strategy_name in ("leave_one_participant_out", "group_holdout"):
        for split in split_manifest.get("strategies", {}).get(strategy_name, []):
            train_participants = [str(x) for x in split.get("train_participants", [])]
            test_participants = [str(x) for x in split.get("test_participants", [])]
            for participants in (train_participants, test_participants):
                fused_rows_here = _rows_for_participants(dataset_rows_per_participant.get("fused", {}), participants)
                unimodal_rows_here = [
                    _rows_for_participants(dataset_rows_per_participant.get(modality, {}), participants)
                    for modality in selected_modalities
                ]
                if fused_rows_here < max(unimodal_rows_here, default=0):
                    fused_less_than_unimodal_in_any_split = True
                    break
            if fused_less_than_unimodal_in_any_split:
                break
        if fused_less_than_unimodal_in_any_split:
            break
    if not fused_less_than_unimodal_in_any_split:
        for row in split_manifest.get("strategies", {}).get("within_participant", []):
            rows_by_dataset = row.get("rows_by_dataset", {}) or {}
            fused_rows_here = int(rows_by_dataset.get("fused", 0) or 0)
            unimodal_rows_here = [int(rows_by_dataset.get(modality, 0) or 0) for modality in selected_modalities]
            if fused_rows_here < max(unimodal_rows_here, default=0):
                fused_less_than_unimodal_in_any_split = True
                break

    if not fused_less_than_unimodal_in_any_split:
        warnings.append(
            "Fused train/test availability is not smaller than unimodal availability in any checked split."
        )
    source_rows_extra_before_stage5 = {
        modality: len(set(source_key_maps[modality].keys()) - source_intersection)
        for modality in selected_modalities
    }
    if (
        not fused_less_than_unimodal_in_any_split
        and any(value > 0 for value in source_rows_extra_before_stage5.values())
        and stage5_ml_keys_identical_across_modalities
    ):
        warnings.append(
            "Stage 4 modality-specific row differences existed, but Stage 5 trial-level dropout filtering removed them before fusion, so the unimodal ML tables ended up with identical keys."
        )

    return {
        "selected_modalities": selected_modalities,
        "require_all_selected_modalities": require_all_selected_modalities,
        "row_counts": row_counts,
        "stage4_source_intersection_rows": len(source_intersection),
        "stage4_source_union_rows": len(source_union),
        "stage4_source_rows_extra_before_stage5": source_rows_extra_before_stage5,
        "selected_modality_intersection_rows": len(selected_intersection),
        "selected_modality_union_rows": len(selected_union),
        "stage5_ml_keys_identical_across_modalities": stage5_ml_keys_identical_across_modalities,
        "fused_rows_match_selected_intersection": set(fused_key_map.keys()) == selected_intersection,
        "rows_lost_when_fusing_vs_stage5_ml": {
            modality: len(set(ml_key_maps[modality].keys()) - set(fused_key_map.keys()))
            for modality in selected_modalities
        },
        "epoch_manifest_consistency": epoch_manifest_consistency,
        "split_examples": split_examples,
        "fused_less_than_unimodal_in_any_checked_split": fused_less_than_unimodal_in_any_split,
        "warnings": warnings,
    }


def _fusion_verification_markdown(verification: dict[str, Any]) -> str:
    lines = ["# Fusion Verification", ""]
    lines.append(f"- Selected modalities: `{', '.join(verification.get('selected_modalities', []))}`")
    lines.append(
        f"- Require all selected modalities: `{verification.get('require_all_selected_modalities')}`"
    )
    lines.append(
        f"- Stage 4 source intersection / union: `{verification.get('stage4_source_intersection_rows')}` / `{verification.get('stage4_source_union_rows')}`"
    )
    lines.append(
        f"- Fused matches selected-modality intersection: `{verification.get('fused_rows_match_selected_intersection')}`"
    )
    lines.append(
        f"- Stage 5 unimodal ML keys identical across modalities: `{verification.get('stage5_ml_keys_identical_across_modalities')}`"
    )
    lines.append(
        f"- Fused smaller than unimodal in any checked split: `{verification.get('fused_less_than_unimodal_in_any_checked_split')}`"
    )
    lines.append("")

    row_counts = verification.get("row_counts", {}) or {}
    dataset_rows = []
    for dataset, stats in row_counts.items():
        dataset_rows.append(
            {
                "dataset": dataset,
                "stage4_source_rows": stats.get("stage4_source_rows", ""),
                "stage5_ml_rows": stats.get("stage5_ml_rows", ""),
                "rows_lost_before_fusion": stats.get("rows_lost_before_fusion", ""),
                "rows_lost_when_fused": stats.get("rows_lost_when_fused", ""),
                "extra_before_stage5": (verification.get("stage4_source_rows_extra_before_stage5", {}) or {}).get(dataset, ""),
            }
        )
    lines.append("## Dataset Counts")
    lines.append(_markdown_table(
        dataset_rows,
        ["dataset", "stage4_source_rows", "stage5_ml_rows", "rows_lost_before_fusion", "rows_lost_when_fused", "extra_before_stage5"],
    ))
    lines.append("")

    epoch_check = verification.get("epoch_manifest_consistency", {}) or {}
    lines.append("## Epoch Manifest Check")
    if not epoch_check.get("available"):
        lines.append("_Epoch manifest not available._")
    else:
        rows = []
        expected = epoch_check.get("expected_kept_rows_by_modality", {}) or {}
        source_not_kept = epoch_check.get("source_contains_rows_not_kept_in_epoch_manifest", {}) or {}
        missing = epoch_check.get("manifest_kept_rows_missing_from_source", {}) or {}
        row_counts = verification.get("row_counts", {}) or {}
        for modality in verification.get("selected_modalities", []):
            rows.append(
                {
                    "modality": modality,
                    "manifest_keep_rows": expected.get(modality, ""),
                    "stage4_source_rows": row_counts.get(modality, {}).get("stage4_source_rows", ""),
                    "source_rows_not_kept": source_not_kept.get(modality, ""),
                    "manifest_keep_missing_from_source": missing.get(modality, ""),
                }
            )
        lines.append(_markdown_table(
            rows,
            ["modality", "manifest_keep_rows", "stage4_source_rows", "source_rows_not_kept", "manifest_keep_missing_from_source"],
        ))
        sample_rows = []
        for modality, items in (epoch_check.get("sample_source_rows_not_kept", {}) or {}).items():
            for item in items[:3]:
                sample_rows.append({"modality": modality, **item})
        if sample_rows:
            lines.append("")
            lines.append("Sample Stage 4 rows that disagree with the current epoch manifest:")
            lines.append(_markdown_table(
                sample_rows,
                ["modality", "participant_id", "epoch_id", "keep_flag", "drop_reason"],
            ))
    lines.append("")

    lines.append("## Split Examples")
    split_rows = []
    for strategy_name in ("leave_one_participant_out", "group_holdout"):
        for item in verification.get("split_examples", {}).get(strategy_name, []):
            rows_by_dataset = item.get("rows_by_dataset", {}) or {}
            fused_counts = rows_by_dataset.get("fused", {}) or {}
            split_rows.append(
                {
                    "strategy": strategy_name,
                    "split_id": item.get("split_id", ""),
                    "fused_train": fused_counts.get("train", ""),
                    "fused_test": fused_counts.get("test", ""),
                    "eeg_train": (rows_by_dataset.get("eeg", {}) or {}).get("train", ""),
                    "eeg_test": (rows_by_dataset.get("eeg", {}) or {}).get("test", ""),
                    "pupil_train": (rows_by_dataset.get("pupil", {}) or {}).get("train", ""),
                    "pupil_test": (rows_by_dataset.get("pupil", {}) or {}).get("test", ""),
                }
            )
    for item in verification.get("split_examples", {}).get("within_participant", []):
        rows_by_dataset = item.get("rows_by_dataset", {}) or {}
        split_rows.append(
            {
                "strategy": "within_participant",
                "split_id": item.get("participant_id", ""),
                "fused_train": "n/a",
                "fused_test": rows_by_dataset.get("fused", ""),
                "eeg_train": "n/a",
                "eeg_test": rows_by_dataset.get("eeg", ""),
                "pupil_train": "n/a",
                "pupil_test": rows_by_dataset.get("pupil", ""),
            }
        )
    lines.append(_markdown_table(
        split_rows,
        ["strategy", "split_id", "fused_train", "fused_test", "eeg_train", "eeg_test", "pupil_train", "pupil_test"],
    ))
    lines.append("")

    lines.append("## Warnings")
    warnings = verification.get("warnings", []) or []
    if not warnings:
        lines.append("- None")
    else:
        for warning in warnings:
            lines.append(f"- {warning}")
    lines.append("")
    return "\n".join(lines)


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
    counts: list[int] | None,
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
                    "selection_mode": "fraction",
                    "test_fraction": fraction,
                    "test_participant_count": n_test,
                    "repeat_index": rep,
                    "seed": seed,
                    "test_participants": test_participants,
                    "train_participants": train_participants,
                }
            )

    for count in counts or []:
        if count <= 0 or count >= len(participants):
            continue
        n_test = int(count)
        for rep in range(1, repeats + 1):
            seed = random_seed + 5000 + (n_test * 100) + rep
            rng = random.Random(seed)
            test_participants = sorted(rng.sample(participants, n_test))
            test_set = set(test_participants)
            train_participants = [p for p in participants if p not in test_set]
            out.append(
                {
                    "split_id": f"group_holdout_n{n_test:02d}_rep{rep:02d}",
                    "strategy": "group_holdout",
                    "selection_mode": "count",
                    "test_fraction": float(n_test) / float(len(participants)),
                    "test_participant_count": n_test,
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
        "--epoch-manifest",
        default=None,
        help="Optional Stage 3 epoch manifest TSV used for verification (default: analysis_pipeline/reports/epoch_manifest.tsv).",
    )
    parser.add_argument(
        "--qc-summary-json",
        default=None,
        help=(
            "Optional Stage 1 qc_dataset_summary.json. When present, Stage 5 applies "
            "modality-specific subject carry-forward sets before building unimodal and fused tables."
        ),
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
        "--group-holdout-counts",
        nargs="*",
        type=int,
        default=None,
        help=(
            "Explicit participant counts for grouped split plans "
            "(example: 2 3 leaves out exactly 2 or 3 participants per split)."
        ),
    )
    parser.add_argument(
        "--group-holdout-repeats",
        type=int,
        default=5,
        help="Number of random repeats per grouped holdout setting.",
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
        "--verification-json",
        default=None,
        help="Verification JSON output path (default follows fusion summary name).",
    )
    parser.add_argument(
        "--verification-md",
        default=None,
        help="Verification Markdown output path (default follows fusion summary name).",
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
    if args.group_holdout_counts and any(count <= 0 for count in args.group_holdout_counts):
        raise ValueError("--group-holdout-counts values must be > 0.")
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
    verification_json_out = (
        Path(args.verification_json).resolve()
        if args.verification_json
        else _default_verification_json_out(summary_out)
    )
    verification_md_out = (
        Path(args.verification_md).resolve()
        if args.verification_md
        else _default_verification_md_out(summary_out)
    )
    epoch_manifest_path = (
        Path(args.epoch_manifest).resolve()
        if args.epoch_manifest
        else _default_epoch_manifest_path()
    )
    qc_summary_path = Path(args.qc_summary_json).resolve() if args.qc_summary_json else None
    if args.epoch_manifest and not epoch_manifest_path.exists():
        raise FileNotFoundError(epoch_manifest_path)
    epoch_manifest_rows = _read_tsv_rows(epoch_manifest_path) if epoch_manifest_path.exists() else None

    modality_subject_filters = _load_modality_subject_filters(
        qc_summary_path=qc_summary_path,
        selected_modalities=selected_modalities,
        subject_subset=subject_subset,
    )
    effective_subject_subset = set(subject_subset) if subject_subset is not None else None
    if modality_subject_filters:
        modality_union = set().union(*modality_subject_filters.values()) if modality_subject_filters else set()
        effective_subject_subset = modality_union if effective_subject_subset is None else (effective_subject_subset & modality_union)

    trial_rows = _read_tsv_rows(trial_table_path)
    trial_index = _load_trial_index(trial_rows, subject_subset=effective_subject_subset)
    if not trial_index:
        raise ValueError("No trial metadata rows available after filters.")

    difficulty_map = _difficulty_bin_map_from_trials(
        trial_index=trial_index,
        include_tutorial=args.include_tutorial,
    )
    if not difficulty_map:
        raise ValueError("Could not derive any difficulty bins from the trial table.")
    print(
        f"Stage 5 starting. task={task} modalities={','.join(selected_modalities)} "
        f"trial_rows={len(trial_rows)} include_tutorial={bool(args.include_tutorial)}"
    )

    subject_dropout_thresholds: dict[str, float] = {}
    if args.dropout_policy == "subject_percentile":
        subject_dropout_thresholds = _compute_subject_dropout_thresholds(
            trial_index=trial_index,
            include_tutorial=args.include_tutorial,
            percentile=args.dropout_percentile,
        )

    modality_rows_out: dict[str, list[dict[str, str]]] = {}
    source_rows_by_modality: dict[str, list[dict[str, str]]] = {}
    modality_stats: dict[str, dict[str, Any]] = {}
    feature_columns_by_modality: dict[str, list[str]] = {}
    unimodal_paths: dict[str, str] = {}
    unimodal_suffix = f"_{args.unimodal_tag.strip()}" if args.unimodal_tag and args.unimodal_tag.strip() else ""

    for modality_idx, modality in enumerate(selected_modalities, start=1):
        print(f"[Modality {modality_idx}/{len(selected_modalities)}] Building {modality} ML table")
        source_path = features_dir / MODALITY_TABLES[modality]
        source_rows = _read_tsv_rows(source_path)
        modality_subject_subset = (
            modality_subject_filters.get(modality)
            if modality_subject_filters is not None
            else effective_subject_subset
        )
        if modality_subject_subset is not None:
            source_rows = [
                row
                for row in source_rows
                if (row.get("participant_id") or "").strip() in modality_subject_subset
            ]
        source_rows_by_modality[modality] = list(source_rows)
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
    print(f"Built fused table rows: {len(fused_rows)}")
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
    participants_considered = sorted(
        {
            meta.participant_id
            for meta in trial_index.values()
            if meta.participant_id and (args.include_tutorial or not meta.is_tutorial)
        }
    )
    dataset_participant_sets = {
        name: set(str(p) for p in stats.get("participants", []))
        for name, stats in dataset_stats_by_name.items()
    }
    participants_omitted_by_dataset = {
        name: sorted(set(participants_considered) - participant_set)
        for name, participant_set in dataset_participant_sets.items()
    }
    participants_omitted_from_primary_dataset = list(participants_omitted_by_dataset.get(primary_dataset_name, []))
    participants_omitted_from_all_datasets = sorted(
        p
        for p in participants_considered
        if all(p not in dataset_participant_sets[name] for name in dataset_stats_by_name)
    )

    split_manifest = {
        "bids_root": str(bids_root),
        "task": task,
        "target": args.target,
        "target_column": "target_label",
        "epoch_manifest": str(epoch_manifest_path) if epoch_manifest_path.exists() else None,
        "qc_summary_json": str(qc_summary_path) if qc_summary_path is not None else None,
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
        "participants_considered": participants_considered,
        "subjects_filter": sorted(effective_subject_subset) if effective_subject_subset else None,
        "subjects_filter_by_modality": (
            {
                modality: sorted(subjects)
                for modality, subjects in modality_subject_filters.items()
            }
            if modality_subject_filters
            else None
        ),
        "participants_omitted": {
            "by_dataset": participants_omitted_by_dataset,
            "from_primary_dataset": participants_omitted_from_primary_dataset,
            "from_all_datasets": participants_omitted_from_all_datasets,
        },
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
                counts=args.group_holdout_counts,
                repeats=args.group_holdout_repeats,
                random_seed=args.random_seed,
            ),
            "within_participant": _build_within_participant_plan(
                primary_stats=primary_stats,
                dataset_stats_by_name=dataset_stats_by_name,
                min_within_rows=args.min_within_rows,
            ),
        },
        "dataset_strategies": {
            name: {
                "leave_one_participant_out": _build_loso_splits(list(stats.get("participants", []))),
                "group_holdout": _build_group_holdout_splits(
                    participants=list(stats.get("participants", [])),
                    fractions=args.group_holdout_fracs,
                    counts=args.group_holdout_counts,
                    repeats=args.group_holdout_repeats,
                    random_seed=args.random_seed,
                ),
                "within_participant": _build_within_participant_plan(
                    primary_stats=stats,
                    dataset_stats_by_name=dataset_stats_by_name,
                    min_within_rows=args.min_within_rows,
                ),
            }
            for name, stats in dataset_stats_by_name.items()
        },
    }
    split_manifest_out.parent.mkdir(parents=True, exist_ok=True)
    split_manifest_out.write_text(json.dumps(split_manifest, indent=2) + "\n", encoding="utf-8")
    print(
        "Built split strategies: "
        f"loso={len(split_manifest['strategies']['leave_one_participant_out'])}, "
        f"group_holdout={len(split_manifest['strategies']['group_holdout'])}, "
        f"within_participant={len(split_manifest['strategies']['within_participant'])}"
    )

    trial_rows_considered = [
        meta
        for meta in trial_index.values()
        if args.include_tutorial or not meta.is_tutorial
    ]
    dropped_values = [meta.dropped_samples_trial for meta in trial_rows_considered if meta.dropped_samples_trial is not None]
    verification = _build_fusion_verification(
        selected_modalities=selected_modalities,
        source_rows_by_modality=source_rows_by_modality,
        modality_rows_out=modality_rows_out,
        fused_rows=fused_rows,
        dataset_stats_by_name=dataset_stats_by_name,
        split_manifest=split_manifest,
        require_all_selected_modalities=args.require_all_selected_modalities,
        epoch_manifest_rows=epoch_manifest_rows,
        epoch_manifest_path=epoch_manifest_path if epoch_manifest_rows is not None else None,
    )
    verification_json_out.parent.mkdir(parents=True, exist_ok=True)
    verification_json_out.write_text(json.dumps(verification, indent=2) + "\n", encoding="utf-8")
    verification_md_out.parent.mkdir(parents=True, exist_ok=True)
    verification_md_out.write_text(_fusion_verification_markdown(verification), encoding="utf-8")

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
        "subjects_filter": sorted(effective_subject_subset) if effective_subject_subset else None,
        "subjects_filter_by_modality": (
            {
                modality: sorted(subjects)
                for modality, subjects in modality_subject_filters.items()
            }
            if modality_subject_filters
            else None
        ),
        "qc_summary_json": str(qc_summary_path) if qc_summary_path is not None else None,
        "participants_considered": participants_considered,
        "participants_omitted": {
            "by_dataset": participants_omitted_by_dataset,
            "from_primary_dataset": participants_omitted_from_primary_dataset,
            "from_all_datasets": participants_omitted_from_all_datasets,
        },
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
        "dataset_rows_per_participant": {
            name: stats["rows_per_participant"] for name, stats in dataset_stats_by_name.items()
        },
        "verification": verification,
        "outputs": {
            **{f"features_ml_{modality}_tsv": path for modality, path in unimodal_paths.items()},
            "features_fused_tsv": str(fused_out),
            "split_manifest_json": str(split_manifest_out),
            "verification_json": str(verification_json_out),
            "verification_md": str(verification_md_out),
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
    print(f"  Wrote fusion verification JSON: {verification_json_out}")
    print(f"  Wrote fusion verification Markdown: {verification_md_out}")
    print(
        "  Participant omissions: "
        f"primary_dataset={len(participants_omitted_from_primary_dataset)}, "
        f"all_datasets={len(participants_omitted_from_all_datasets)}"
    )


if __name__ == "__main__":
    main()

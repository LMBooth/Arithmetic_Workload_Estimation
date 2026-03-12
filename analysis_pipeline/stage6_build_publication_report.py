from __future__ import annotations

import argparse
import glob
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_out_md() -> Path:
    return _reports_dir() / "publication_full_report.md"


def _default_out_json() -> Path:
    return _reports_dir() / "publication_full_report.json"


def _default_qc_summary() -> Path:
    return _reports_dir() / "qc_dataset_summary.json"


def _default_epoch_summary() -> Path:
    return _reports_dir() / "epoch_summary.json"


def _default_feature_summary() -> Path:
    return _reports_dir() / "feature_summary.json"


def _default_run_manifest() -> Path:
    return _reports_dir() / "run_manifest.json"


def _resolve_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (Path.cwd() / direct).resolve()


def _resolve_maybe(path_text: str | None) -> Path | None:
    if path_text is None:
        return None
    text = str(path_text).strip()
    if not text:
        return None
    return _resolve_path(text)


def _display_path(path: Path | None) -> str:
    if path is None:
        return "n/a"
    try:
        return str(path.relative_to(Path.cwd()))
    except Exception:  # noqa: BLE001
        return str(path)


def _load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _load_json_optional(path: Path | None) -> tuple[dict[str, Any] | None, Path | None]:
    if path is None:
        return None, None
    if not path.exists():
        return None, path
    payload = _load_json(path)
    if isinstance(payload, dict):
        return payload, path
    return {"_payload": payload}, path


def _dedupe_keep_order(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    out: list[Path] = []
    for path in paths:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        out.append(path.resolve())
    return out


def _collect_paths_by_glob(pattern_text: str | None) -> list[Path]:
    if pattern_text is None:
        return []
    pattern = str(pattern_text).strip()
    if not pattern:
        return []
    expanded = Path(pattern).expanduser()
    if expanded.is_absolute():
        resolved_pattern = str(expanded)
    else:
        resolved_pattern = str((Path.cwd() / expanded).resolve())
    matches = sorted(Path(p).resolve() for p in glob.glob(resolved_pattern, recursive=True))
    files = [path for path in matches if path.is_file()]
    return _dedupe_keep_order(files)


def _pick_latest(paths: list[Path]) -> Path | None:
    if not paths:
        return None
    return max(paths, key=lambda p: p.stat().st_mtime)


def _to_markdown_table(df: pd.DataFrame, decimals: int = 4) -> str:
    if df.empty:
        return "_no rows_\n"
    headers = list(df.columns)
    lines: list[str] = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for _, row in df.iterrows():
        cells: list[str] = []
        for col in headers:
            val = row[col]
            if isinstance(val, float):
                cells.append(f"{val:.{decimals}f}")
            else:
                cells.append(str(val))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def _fmt_int(value: Any) -> str:
    try:
        return str(int(value))
    except Exception:  # noqa: BLE001
        return "n/a"


def _fmt_num(value: Any, decimals: int = 3) -> str:
    try:
        number = float(value)
    except Exception:  # noqa: BLE001
        return "n/a"
    if number.is_integer():
        return str(int(number))
    return f"{number:.{decimals}f}"


def _fmt_pct(num: Any, den: Any) -> str:
    try:
        numerator = float(num)
        denominator = float(den)
        if denominator <= 0:
            return "n/a"
        return f"{(100.0 * numerator / denominator):.2f}%"
    except Exception:  # noqa: BLE001
        return "n/a"


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:  # noqa: BLE001
        return default


def _as_float(value: Any) -> float | None:
    try:
        return float(value)
    except Exception:  # noqa: BLE001
        return None


def _collect_stage6_result_paths(explicit: list[str] | None, glob_pattern: str | None) -> list[Path]:
    paths: list[Path] = []
    for item in explicit or []:
        path = _resolve_path(str(item))
        if path.exists() and path.is_file():
            paths.append(path)
    if glob_pattern:
        paths.extend(_collect_paths_by_glob(glob_pattern))
    return _dedupe_keep_order(paths)


def _build_stage6_frames(result_paths: list[Path]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    scenario_rows: list[dict[str, Any]] = []
    best_rows: list[dict[str, Any]] = []
    aggregate_rows: list[dict[str, Any]] = []

    for idx, result_path in enumerate(result_paths):
        payload = _load_json(result_path)
        config = payload.get("config", {})
        counts = payload.get("counts", {})
        class_scenario = config.get("class_scenario", {}) or {}
        scenario_name = str(class_scenario.get("name") or config.get("run_tag") or result_path.stem)

        datasets = [str(x) for x in config.get("datasets", [])]
        protocols = [str(x) for x in config.get("protocols", [])]
        models = [str(x) for x in config.get("models", [])]

        scenario_rows.append(
            {
                "scenario_rank": idx,
                "scenario": scenario_name,
                "n_evaluations": _as_int(counts.get("n_evaluations"), 0),
                "n_aggregate_rows": _as_int(counts.get("n_aggregate_rows"), 0),
                "n_datasets": len(datasets),
                "n_protocols": len(protocols),
                "n_models": len(models),
                "results_json": str(result_path),
            }
        )

        for row in payload.get("best_models", []):
            best_rows.append(
                {
                    "scenario_rank": idx,
                    "scenario": scenario_name,
                    "dataset": str(row.get("dataset", "")),
                    "protocol": str(row.get("protocol", "")),
                    "best_model": str(row.get("best_model", "")),
                    "best_feature_selector": str(row.get("best_feature_selector", "none")),
                    "best_pipeline": str(
                        row.get(
                            "best_pipeline",
                            f"{row.get('best_model', '')}+{row.get('best_feature_selector', 'none')}",
                        )
                    ),
                    "balanced_accuracy_mean": _as_float(row.get("balanced_accuracy_mean")),
                    "macro_f1_mean": _as_float(row.get("macro_f1_mean")),
                    "n_evaluations": _as_int(row.get("n_evaluations"), 0),
                    "results_json": str(result_path),
                }
            )

        for row in payload.get("aggregates", []):
            aggregate_rows.append(
                {
                    "scenario_rank": idx,
                    "scenario": scenario_name,
                    "dataset": str(row.get("dataset", "")),
                    "protocol": str(row.get("protocol", "")),
                    "model": str(row.get("model", "")),
                    "feature_selector": str(row.get("feature_selector", "none")),
                    "pipeline_id": str(
                        row.get(
                            "pipeline_id",
                            f"{row.get('model', '')}+{row.get('feature_selector', 'none')}",
                        )
                    ),
                    "balanced_accuracy_mean": _as_float(row.get("balanced_accuracy_mean")),
                    "macro_f1_mean": _as_float(row.get("macro_f1_mean")),
                    "n_evaluations": _as_int(row.get("n_evaluations"), 0),
                    "results_json": str(result_path),
                }
            )

    scenario_df = pd.DataFrame(scenario_rows)
    best_df = pd.DataFrame(best_rows)
    agg_df = pd.DataFrame(aggregate_rows)

    if not scenario_df.empty:
        scenario_df = scenario_df.sort_values(["scenario_rank", "scenario"]).reset_index(drop=True)
    if not best_df.empty:
        best_df = best_df.sort_values(["scenario_rank", "dataset", "protocol"]).reset_index(drop=True)
    if not agg_df.empty:
        agg_df = agg_df.sort_values(
            ["scenario_rank", "dataset", "protocol", "balanced_accuracy_mean"],
            ascending=[True, True, True, False],
        ).reset_index(drop=True)

    return scenario_df, best_df, agg_df


def _build_global_best_table(best_df: pd.DataFrame) -> pd.DataFrame:
    if best_df.empty:
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    grouped = best_df.groupby(["dataset", "protocol"], sort=True)
    for (dataset, protocol), group in grouped:
        ranked = group.sort_values(["balanced_accuracy_mean", "macro_f1_mean"], ascending=[False, False]).reset_index(
            drop=True
        )
        top = ranked.iloc[0]
        rows.append(
            {
                "dataset": str(dataset),
                "protocol": str(protocol),
                "scenario": str(top["scenario"]),
                "best_pipeline": str(top["best_pipeline"]),
                "balanced_accuracy_mean": _as_float(top["balanced_accuracy_mean"]),
                "macro_f1_mean": _as_float(top["macro_f1_mean"]),
            }
        )
    return pd.DataFrame(rows).sort_values(["dataset", "protocol"]).reset_index(drop=True)


def _participants_with_drops(
    epoch_payload: dict[str, Any] | None,
) -> tuple[list[str], list[str], list[str], pd.DataFrame]:
    payload = epoch_payload or {}
    preferred_rows = payload.get("epoch_drop_counts_by_participant", []) or []
    rows: list[dict[str, Any]] = []

    if isinstance(preferred_rows, list) and preferred_rows:
        for entry in preferred_rows:
            if not isinstance(entry, dict):
                continue
            participant_id = str(entry.get("participant_id", "")).strip()
            if not participant_id:
                continue
            eeg_count = _as_int(entry.get("eeg_dropped_windows"), 0)
            ecg_count = _as_int(entry.get("ecg_dropped_windows"), 0)
            pupil_count = _as_int(entry.get("pupil_dropped_windows"), 0)
            pupil_low_conf_count = _as_int(entry.get("pupil_low_confidence_drops"), 0)
            pupil_mean_conf_count = _as_int(entry.get("pupil_mean_confidence_drops"), 0)
            rows.append(
                {
                    "participant_id": participant_id,
                    "eeg_dropped_windows": eeg_count,
                    "ecg_dropped_windows": ecg_count,
                    "pupil_dropped_windows": pupil_count,
                    "pupil_low_confidence_drops": pupil_low_conf_count,
                    "pupil_mean_confidence_drops": pupil_mean_conf_count,
                    "eeg_total_samples": _as_int(entry.get("eeg_total_samples"), 0),
                    "eeg_dropped_samples_total": _as_float(entry.get("eeg_dropped_samples_total")) or 0.0,
                    "eeg_dropped_sample_percent": _as_float(entry.get("eeg_dropped_sample_percent")) or 0.0,
                    "ecg_total_samples": _as_int(entry.get("ecg_total_samples"), 0),
                    "ecg_dropped_samples_total": _as_float(entry.get("ecg_dropped_samples_total")) or 0.0,
                    "ecg_dropped_sample_percent": _as_float(entry.get("ecg_dropped_sample_percent")) or 0.0,
                    "pupil_total_samples": _as_int(entry.get("pupil_total_samples"), 0),
                    "pupil_total_windows": _as_int(entry.get("pupil_total_windows"), 0),
                    "pupil_dropped_window_percent": _as_float(entry.get("pupil_dropped_window_percent")) or 0.0,
                    "total_dropped_windows": _as_int(
                        entry.get("total_dropped_windows"),
                        eeg_count + ecg_count + pupil_count,
                    ),
                }
            )
    else:
        legacy_payload = payload.get("dropped_samples_rejections_by_participant", {}) or {}
        for participant_id in sorted(legacy_payload.keys()):
            stats = legacy_payload.get(participant_id, {}) or {}
            eeg_count = _as_int(stats.get("eeg"), 0)
            ecg_count = _as_int(stats.get("ecg"), 0)
            rows.append(
                {
                    "participant_id": participant_id,
                    "eeg_dropped_windows": eeg_count,
                    "ecg_dropped_windows": ecg_count,
                    "pupil_dropped_windows": 0,
                    "pupil_low_confidence_drops": 0,
                    "pupil_mean_confidence_drops": 0,
                    "eeg_total_samples": 0,
                    "eeg_dropped_samples_total": 0.0,
                    "eeg_dropped_sample_percent": 0.0,
                    "ecg_total_samples": 0,
                    "ecg_dropped_samples_total": 0.0,
                    "ecg_dropped_sample_percent": 0.0,
                    "pupil_total_samples": 0,
                    "pupil_total_windows": 0,
                    "pupil_dropped_window_percent": 0.0,
                    "total_dropped_windows": eeg_count + ecg_count,
                }
            )

    rows = sorted(
        rows,
        key=lambda item: (
            -_as_int(item.get("total_dropped_windows"), 0),
            -_as_int(item.get("pupil_dropped_windows"), 0),
            -_as_int(item.get("eeg_dropped_windows"), 0),
            -_as_int(item.get("ecg_dropped_windows"), 0),
            str(item.get("participant_id", "")),
        ),
    )
    eeg_subjects = sorted(row["participant_id"] for row in rows if _as_int(row.get("eeg_dropped_windows"), 0) > 0)
    ecg_subjects = sorted(row["participant_id"] for row in rows if _as_int(row.get("ecg_dropped_windows"), 0) > 0)
    pupil_subjects = sorted(row["participant_id"] for row in rows if _as_int(row.get("pupil_dropped_windows"), 0) > 0)
    return eeg_subjects, ecg_subjects, pupil_subjects, pd.DataFrame(rows)


def _stage1_strict_mode(manifest_payload: dict[str, Any] | None) -> str:
    if not manifest_payload:
        return "unknown"
    steps = manifest_payload.get("steps", [])
    stage1_steps = [row for row in steps if str(row.get("stage")) == "stage1"]
    if not stage1_steps:
        return "unknown"
    for step in stage1_steps:
        command = [str(part) for part in step.get("command", [])]
        if "--strict" in command:
            return "enabled"
    return "disabled"


def _relative_results_table(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "results_json" in out.columns:
        out["results_json"] = [_display_path(Path(p)) for p in out["results_json"].astype(str)]
    return out


def _markdown_from_components(
    *,
    generated_utc: str,
    result_paths: list[Path],
    qc_payload: dict[str, Any] | None,
    qc_path: Path | None,
    epoch_payload: dict[str, Any] | None,
    epoch_path: Path | None,
    feature_payload: dict[str, Any] | None,
    feature_path: Path | None,
    fusion_payload: dict[str, Any] | None,
    fusion_path: Path | None,
    run_manifest_payload: dict[str, Any] | None,
    run_manifest_path: Path | None,
    stage6_scenarios: pd.DataFrame,
    stage6_best: pd.DataFrame,
    stage6_global_best: pd.DataFrame,
    dropped_windows_table: pd.DataFrame,
) -> str:
    lines: list[str] = []
    lines.append("# Full Publication Reporting Snapshot")
    lines.append("")
    lines.append(f"- Generated (UTC): `{generated_utc}`")
    lines.append(f"- Stage 6 result files loaded: `{len(result_paths)}`")
    lines.append("")

    lines.append("## Inputs")
    lines.append(f"- Stage 1 QC summary: `{_display_path(qc_path)}`")
    lines.append(f"- Stage 3 epoch summary: `{_display_path(epoch_path)}`")
    lines.append(f"- Stage 4 feature summary: `{_display_path(feature_path)}`")
    lines.append(f"- Stage 5 fusion summary: `{_display_path(fusion_path)}`")
    lines.append(f"- Run manifest: `{_display_path(run_manifest_path)}`")
    lines.append("")

    lines.append("## Stage 1 QC Gate Snapshot")
    if qc_payload is None:
        lines.append("- Stage 1 QC summary not found.")
    else:
        coverage = qc_payload.get("modality_coverage", {}) or {}
        qc_policy = str(qc_payload.get("qc_decision_policy") or "n/a")
        flagged_after_qc = list(qc_payload.get("subjects_flagged_by_any_qc_anomaly", []) or [])
        rejected_after_qc = list(qc_payload.get("subjects_rejected_after_qc", []) or [])
        rejected_after_qc_any = list(qc_payload.get("subjects_rejected_after_qc_any_modality", []) or [])
        rejected_after_qc_by_modality = dict(qc_payload.get("subjects_rejected_after_qc_by_modality", {}) or {})
        carried_forward_after_qc = list(qc_payload.get("subjects_carried_forward_after_qc", []) or [])
        carried_forward_after_qc_by_modality = dict(
            qc_payload.get("subjects_carried_forward_after_qc_by_modality", {}) or {}
        )
        reason_map = dict(qc_payload.get("rejection_reasons_by_subject", {}) or {})
        reason_map_any = dict(qc_payload.get("rejection_reasons_by_subject_any_modality", {}) or {})
        if not reason_map:
            reason_map = dict(qc_payload.get("qc_reasons_by_subject", {}) or {})
        if not reason_map_any:
            reason_map_any = dict(qc_payload.get("qc_reasons_by_subject", {}) or {})
        eeg_flags = list((qc_payload.get("subjects_flagged_by_dropped_samples_thresholds", {}) or {}).get("eeg", []))
        ecg_flags = list((qc_payload.get("subjects_flagged_by_dropped_samples_thresholds", {}) or {}).get("ecg", []))
        anomalies = list(qc_payload.get("anomalies", []) or [])
        lines.append(f"- Subjects processed: `{_fmt_int(coverage.get('n_subjects'))}`")
        lines.append(
            "- Modality coverage (EEG/ECG/Pupil/All): "
            f"`{_fmt_int(coverage.get('n_with_eeg'))}/"
            f"{_fmt_int(coverage.get('n_with_ecg'))}/"
            f"{_fmt_int(coverage.get('n_with_pupil'))}/"
            f"{_fmt_int(coverage.get('n_with_all_modalities'))}`"
        )
        lines.append(f"- Stage 1 QC decision policy: `{qc_policy}`")
        lines.append(f"- QC anomalies: `{_fmt_int(qc_payload.get('anomaly_count'))}`")
        lines.append(
            "- Subjects flagged by any QC anomaly: "
            f"`{', '.join(flagged_after_qc) if flagged_after_qc else 'none'}`"
        )
        lines.append(
            "- Subjects rejected after Stage 1 QC in all modalities: "
            f"`{', '.join(rejected_after_qc) if rejected_after_qc else 'none'}`"
        )
        lines.append(
            "- Subjects rejected after Stage 1 QC in any modality: "
            f"`{', '.join(rejected_after_qc_any) if rejected_after_qc_any else 'none'}`"
        )
        lines.append(
            "- Subjects carried forward after Stage 1 QC in any modality: "
            f"`{len(carried_forward_after_qc)}`"
        )
        if carried_forward_after_qc_by_modality:
            lines.append(
                "- Subjects carried forward by modality (EEG/ECG/Pupil): "
                f"`{len(list(carried_forward_after_qc_by_modality.get('eeg', []) or []))}/"
                f"{len(list(carried_forward_after_qc_by_modality.get('ecg', []) or []))}/"
                f"{len(list(carried_forward_after_qc_by_modality.get('pupil', []) or []))}`"
            )
        if rejected_after_qc_by_modality:
            lines.append(
                "- Subjects rejected by modality (EEG/ECG/Pupil): "
                f"`{len(list(rejected_after_qc_by_modality.get('eeg', []) or []))}/"
                f"{len(list(rejected_after_qc_by_modality.get('ecg', []) or []))}/"
                f"{len(list(rejected_after_qc_by_modality.get('pupil', []) or []))}`"
            )
        lines.append(f"- EEG dropped-sample flagged subjects: `{', '.join(eeg_flags) if eeg_flags else 'none'}`")
        lines.append(f"- ECG dropped-sample flagged subjects: `{', '.join(ecg_flags) if ecg_flags else 'none'}`")
        if rejected_after_qc and reason_map:
            lines.append("- Fully rejected subjects and reasons:")
            for subject in rejected_after_qc:
                reasons = list(reason_map.get(subject, []) or [])
                reason_text = "; ".join(str(reason) for reason in reasons) if reasons else "n/a"
                lines.append(f"  - {subject}: {reason_text}")
        elif rejected_after_qc_any and reason_map_any:
            lines.append("- Any-modality rejected subjects and reasons:")
            for subject in rejected_after_qc_any:
                reasons = list(reason_map_any.get(subject, []) or [])
                reason_text = "; ".join(str(reason) for reason in reasons) if reasons else "n/a"
                lines.append(f"  - {subject}: {reason_text}")
        if anomalies:
            preview = anomalies[:5]
            lines.append("- Example anomalies:")
            for item in preview:
                lines.append(f"  - {item}")
            if len(anomalies) > len(preview):
                lines.append(f"  - ... and `{len(anomalies) - len(preview)}` more")
    lines.append("")

    lines.append("## Stage 3 Segmentation Window Drop Counts")
    if epoch_payload is None:
        lines.append("- Stage 3 epoch summary not found.")
    else:
        dropped_window_counts = epoch_payload.get("dropped_window_counts", {}) or {}
        dropped_rejections = epoch_payload.get("dropped_samples_rejections", {}) or {}
        dropped_counts = epoch_payload.get("dropped_counts", {}) or {}
        dropped_eeg = _as_int(dropped_rejections.get("eeg"), _as_int(dropped_counts.get("eeg"), 0))
        dropped_ecg = _as_int(dropped_rejections.get("ecg"), _as_int(dropped_counts.get("ecg"), 0))
        dropped_pupil = _as_int(dropped_window_counts.get("pupil"), _as_int(dropped_counts.get("pupil"), 0))
        pupil_low_conf = _as_int((epoch_payload.get("pupil_low_confidence_rejections", {}) or {}).get("total"), 0)
        pupil_mean_conf = _as_int((epoch_payload.get("pupil_mean_confidence_rejections", {}) or {}).get("total"), 0)
        manifest_rows = _as_int(epoch_payload.get("manifest_rows"), 0)
        drop_ratio_summary = epoch_payload.get("drop_ratio_summary", {}) or {}
        figure_path = (
            (epoch_payload.get("figure_paths", {}) or {}).get("segmentation_dropped_windows_due_missing_samples_eeg_ecg")
            or "n/a"
        )
        omitted = epoch_payload.get("participants_omitted", {}) or {}

        lines.append(f"- EEG windows dropped due missing-sample threshold: `{dropped_eeg}` ({_fmt_pct(dropped_eeg, manifest_rows)})")
        lines.append(f"- ECG windows dropped due missing-sample threshold: `{dropped_ecg}` ({_fmt_pct(dropped_ecg, manifest_rows)})")
        lines.append(f"- Pupil windows dropped during segmentation: `{dropped_pupil}` ({_fmt_pct(dropped_pupil, manifest_rows)})")
        lines.append(
            "- Pupil confidence-triggered drops "
            f"(mean-threshold / low-confidence coverage): `{pupil_mean_conf}` / `{pupil_low_conf}`"
        )
        lines.append(
            "- Participants omitted after Stage 3 (EEG/ECG/Pupil/Multimodal): "
            f"`{len(list(omitted.get('from_eeg', []) or []))}/"
            f"{len(list(omitted.get('from_ecg', []) or []))}/"
            f"{len(list(omitted.get('from_pupil', []) or []))}/"
            f"{len(list(omitted.get('from_multimodal', []) or []))}`"
        )
        if drop_ratio_summary:
            eeg_ratio = drop_ratio_summary.get("eeg", {}) or {}
            ecg_ratio = drop_ratio_summary.get("ecg", {}) or {}
            pupil_ratio = drop_ratio_summary.get("pupil", {}) or {}
            lines.append(
                "- EEG usable samples / dropped samples: "
                f"`{_fmt_num(eeg_ratio.get('total_samples'))} / {_fmt_num(eeg_ratio.get('dropped_samples_total'))}` "
                f"(`{_fmt_num(eeg_ratio.get('dropped_sample_percent'), 3)}%` dropped)"
            )
            lines.append(
                "- ECG usable samples / dropped samples: "
                f"`{_fmt_num(ecg_ratio.get('total_samples'))} / {_fmt_num(ecg_ratio.get('dropped_samples_total'))}` "
                f"(`{_fmt_num(ecg_ratio.get('dropped_sample_percent'), 3)}%` dropped)"
            )
            lines.append(
                "- Pupil total windows / dropped windows: "
                f"`{_fmt_num(pupil_ratio.get('total_windows'))} / {_fmt_num(pupil_ratio.get('dropped_windows'))}` "
                f"(`{_fmt_num(pupil_ratio.get('dropped_window_percent'), 3)}%` dropped; "
                f"`{_fmt_num(pupil_ratio.get('total_samples'))}` total pupil samples)"
            )
        lines.append(f"- Drop-count figure: `{figure_path}`")
        if not dropped_windows_table.empty:
            lines.append("")
            lines.append("### Participant Segmentation Drop Counts")
            lines.append(
                "_EEG/ECG percentages use dropped samples / (usable samples + dropped samples); "
                "pupil percentage uses dropped windows / total windows._"
            )
            lines.append(_to_markdown_table(dropped_windows_table, decimals=3))
    lines.append("")

    lines.append("## Stage 4/5 Omission Snapshot")
    if feature_payload is None and fusion_payload is None:
        lines.append("- Stage 4/5 summaries not found.")
    else:
        if feature_payload is not None:
            feature_omitted = feature_payload.get("participants_omitted", {}) or {}
            lines.append("- Stage 4 feature omissions:")
            lines.append(f"  - from EEG: `{len(list(feature_omitted.get('from_eeg', []) or []))}`")
            lines.append(f"  - from ECG: `{len(list(feature_omitted.get('from_ecg', []) or []))}`")
            lines.append(f"  - from Pupil: `{len(list(feature_omitted.get('from_pupil', []) or []))}`")
            lines.append(f"  - from Multimodal: `{len(list(feature_omitted.get('from_multimodal', []) or []))}`")
        if fusion_payload is not None:
            fusion_omitted = (fusion_payload.get("participants_omitted", {}) or {}).get("by_dataset", {}) or {}
            lines.append("- Stage 5 fusion omissions:")
            lines.append(f"  - from EEG: `{len(list(fusion_omitted.get('eeg', []) or []))}`")
            lines.append(f"  - from ECG: `{len(list(fusion_omitted.get('ecg', []) or []))}`")
            lines.append(f"  - from Pupil: `{len(list(fusion_omitted.get('pupil', []) or []))}`")
            lines.append(f"  - from Fused: `{len(list(fusion_omitted.get('fused', []) or []))}`")
    lines.append("")

    lines.append("## Stage 6 Model Output Snapshot")
    if stage6_scenarios.empty:
        lines.append("- No Stage 6 scenario summaries available.")
    else:
        lines.append("### Scenario Coverage")
        lines.append(_to_markdown_table(_relative_results_table(stage6_scenarios), decimals=0))
    if not stage6_best.empty:
        lines.append("### Best Pipeline by Scenario, Dataset, and Protocol")
        best_table = _relative_results_table(
            stage6_best[
                [
                    "scenario",
                    "dataset",
                    "protocol",
                    "best_pipeline",
                    "balanced_accuracy_mean",
                    "macro_f1_mean",
                    "n_evaluations",
                    "results_json",
                ]
            ]
        )
        lines.append(_to_markdown_table(best_table))
    if not stage6_global_best.empty:
        lines.append("### Global Best Pipeline per Dataset and Protocol")
        lines.append(_to_markdown_table(stage6_global_best))
    lines.append("")

    stage1_strict_state = _stage1_strict_mode(run_manifest_payload)
    lines.append("## 9. Publication Reporting Recommendations")
    lines.append(
        "- Report participant counts and modality coverage from Stage 1 (`qc_dataset_summary.json`) for the analyzed run."
    )
    lines.append(
        "- Report objective QC thresholds for EEG/ECG dropped samples (Stage 1) and segmentation missing-sample thresholds (Stage 3)."
    )
    lines.append("- Report anomaly totals and taxonomy with participant-level IDs.")
    lines.append(
        "- Report segmentation window drops as explicit counts for EEG and ECG, plus participant IDs with any dropped windows."
    )
    lines.append(
        "- Report participant omission counts across Stage 3, Stage 4, and Stage 5 before model fitting."
    )
    lines.append("- Report whether Stage 1 strict-gate mode (`--strict`) was active.")
    lines.append(f"- Stage 1 strict-gate status from run manifest: `{stage1_strict_state}`.")
    lines.append(
        "- Report Stage 1 rejected-subject counts and participant-level rejection reasons when strict QC is enabled."
    )
    lines.append(
        "- Archive and cite lineage artifacts: `qc_dataset_summary.json`, `epoch_summary.json`, `fusion_summary*.json`, `ml_results*.json`."
    )
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build a single publication-facing report that combines QC, segmentation-window drops, "
            "feature/fusion omission stats, and Stage 6 model outputs."
        )
    )
    parser.add_argument(
        "--results-json",
        nargs="*",
        default=None,
        help="Optional explicit list of Stage 6 ml_results*.json files.",
    )
    parser.add_argument(
        "--results-json-glob",
        default="analysis_pipeline/reports/ml_results_*.json",
        help="Glob fallback for Stage 6 ml_results*.json files.",
    )
    parser.add_argument(
        "--qc-summary-json",
        default=str(_default_qc_summary()),
        help="Path to Stage 1 qc_dataset_summary.json.",
    )
    parser.add_argument(
        "--epoch-summary-json",
        default=str(_default_epoch_summary()),
        help="Path to Stage 3 epoch_summary.json.",
    )
    parser.add_argument(
        "--feature-summary-json",
        default=str(_default_feature_summary()),
        help="Path to Stage 4 feature_summary.json (optional).",
    )
    parser.add_argument(
        "--fusion-summary-json",
        default=None,
        help="Path to Stage 5 fusion_summary*.json (optional). If omitted, latest matching --fusion-summary-glob is used.",
    )
    parser.add_argument(
        "--fusion-summary-glob",
        default="analysis_pipeline/reports/fusion_summary*.json",
        help="Glob used to auto-pick the newest fusion summary when --fusion-summary-json is not provided.",
    )
    parser.add_argument(
        "--run-manifest-json",
        default=str(_default_run_manifest()),
        help="Optional run manifest path to detect Stage 1 strict mode.",
    )
    parser.add_argument("--out-md", default=None, help="Output markdown report path.")
    parser.add_argument("--out-json", default=None, help="Output JSON report path.")
    args = parser.parse_args()

    out_md = _resolve_path(args.out_md) if args.out_md else _default_out_md()
    out_json = _resolve_path(args.out_json) if args.out_json else _default_out_json()

    result_paths = _collect_stage6_result_paths(args.results_json, args.results_json_glob)
    if not result_paths:
        raise ValueError("No Stage 6 result JSON files found.")

    qc_payload, qc_path = _load_json_optional(_resolve_maybe(args.qc_summary_json))
    epoch_payload, epoch_path = _load_json_optional(_resolve_maybe(args.epoch_summary_json))
    feature_payload, feature_path = _load_json_optional(_resolve_maybe(args.feature_summary_json))

    fusion_path = _resolve_maybe(args.fusion_summary_json)
    if fusion_path is None:
        fusion_candidates = _collect_paths_by_glob(args.fusion_summary_glob)
        fusion_path = _pick_latest(fusion_candidates)
    fusion_payload, fusion_path = _load_json_optional(fusion_path)

    run_manifest_payload, run_manifest_path = _load_json_optional(_resolve_maybe(args.run_manifest_json))

    stage6_scenarios, stage6_best, _stage6_agg = _build_stage6_frames(result_paths)
    stage6_global_best = _build_global_best_table(stage6_best)

    eeg_drop_subjects, ecg_drop_subjects, pupil_drop_subjects, dropped_windows_table = _participants_with_drops(
        epoch_payload
    )

    generated_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    md_text = _markdown_from_components(
        generated_utc=generated_utc,
        result_paths=result_paths,
        qc_payload=qc_payload,
        qc_path=qc_path,
        epoch_payload=epoch_payload,
        epoch_path=epoch_path,
        feature_payload=feature_payload,
        feature_path=feature_path,
        fusion_payload=fusion_payload,
        fusion_path=fusion_path,
        run_manifest_payload=run_manifest_payload,
        run_manifest_path=run_manifest_path,
        stage6_scenarios=stage6_scenarios,
        stage6_best=stage6_best,
        stage6_global_best=stage6_global_best,
        dropped_windows_table=dropped_windows_table,
    )

    summary_payload: dict[str, Any] = {
        "generated_utc": generated_utc,
        "inputs": {
            "results_json": [str(path) for path in result_paths],
            "qc_summary_json": str(qc_path) if qc_path else None,
            "epoch_summary_json": str(epoch_path) if epoch_path else None,
            "feature_summary_json": str(feature_path) if feature_path else None,
            "fusion_summary_json": str(fusion_path) if fusion_path else None,
            "run_manifest_json": str(run_manifest_path) if run_manifest_path else None,
        },
        "stage1_qc": qc_payload or {},
        "stage3_epoch": epoch_payload or {},
        "stage4_feature": feature_payload or {},
        "stage5_fusion": fusion_payload or {},
        "stage6": {
            "scenario_rows": stage6_scenarios.to_dict(orient="records"),
            "best_rows": stage6_best.to_dict(orient="records"),
            "global_best_by_dataset_protocol": stage6_global_best.to_dict(orient="records"),
        },
        "segmentation_dropped_windows": {
            "subjects_with_eeg_drops": eeg_drop_subjects,
            "subjects_with_ecg_drops": ecg_drop_subjects,
            "subjects_with_pupil_drops": pupil_drop_subjects,
            "by_participant": dropped_windows_table.to_dict(orient="records"),
        },
        "publication_reporting_recommendations": {
            "strict_mode_from_manifest": _stage1_strict_mode(run_manifest_payload),
            "required_artifacts": [
                "qc_dataset_summary.json",
                "epoch_summary.json",
                "fusion_summary*.json",
                "ml_results*.json",
            ],
        },
    }

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md_text, encoding="utf-8")
    out_json.write_text(json.dumps(summary_payload, indent=2) + "\n", encoding="utf-8")

    print("Full publication report complete.")
    print(f"  Output markdown: {out_md}")
    print(f"  Output json: {out_json}")
    print(f"  Stage 6 result files: {len(result_paths)}")
    print(f"  EEG drop-window participants: {len(eeg_drop_subjects)}")
    print(f"  ECG drop-window participants: {len(ecg_drop_subjects)}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import platform
import shlex
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class PlannedStep:
    stage: str
    name: str
    command: list[str]
    outputs: list[str]
    output_globs: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class OutputLayout:
    root: Path
    reports_dir: Path
    features_dir: Path
    models_dir: Path
    cleaned_dir: Path
    epochs_dir: Path


STAGE_ORDER = [
    "stage0",
    "stage1",
    "stage2",
    "stage3",
    "stage4",
    "stage5",
    "stage6",
    "stage6_confusions",
    "stage6_publication_report",
    "stage7_significance",
]


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _features_dir() -> Path:
    return _analysis_root() / "features"


def _models_dir() -> Path:
    return _analysis_root() / "models"


def _cleaned_dir() -> Path:
    return _analysis_root() / "derivatives" / "cleaned"


def _epochs_dir() -> Path:
    return _analysis_root() / "derivatives" / "epochs"


def _config_default() -> Path:
    return _analysis_root() / "config" / "pipeline_unified_classic_nn_baseline_preproc.yaml"


def _manifest_default() -> Path:
    return _reports_dir() / "run_manifest.json"


def _resolve_output_layout(config: dict[str, Any], repo_root: Path) -> OutputLayout:
    outputs_cfg = config.get("outputs", {})
    root = _resolve_path(outputs_cfg.get("root"), repo_root) or _analysis_root()
    root = root.resolve()
    default_root = _analysis_root().resolve()
    if root == default_root:
        return OutputLayout(
            root=default_root,
            reports_dir=_reports_dir().resolve(),
            features_dir=_features_dir().resolve(),
            models_dir=_models_dir().resolve(),
            cleaned_dir=_cleaned_dir().resolve(),
            epochs_dir=_epochs_dir().resolve(),
        )
    return OutputLayout(
        root=root,
        reports_dir=(root / "reports").resolve(),
        features_dir=(root / "features").resolve(),
        models_dir=(root / "models").resolve(),
        cleaned_dir=(root / "derivatives" / "cleaned").resolve(),
        epochs_dir=(root / "derivatives" / "epochs").resolve(),
    )


def _is_relative_to(path: Path, other: Path) -> bool:
    try:
        path.relative_to(other)
        return True
    except ValueError:
        return False


def _expand_output_placeholders(value: Any, layout: OutputLayout) -> Any:
    if isinstance(value, dict):
        return {key: _expand_output_placeholders(val, layout) for key, val in value.items()}
    if isinstance(value, list):
        return [_expand_output_placeholders(item, layout) for item in value]
    if not isinstance(value, str):
        return value

    replacements = {
        "output_root": str(layout.root),
        "reports_dir": str(layout.reports_dir),
        "features_dir": str(layout.features_dir),
        "models_dir": str(layout.models_dir),
        "cleaned_dir": str(layout.cleaned_dir),
        "epochs_dir": str(layout.epochs_dir),
    }
    text = value
    for key, replacement in replacements.items():
        text = text.replace(f"{{{key}}}", replacement)
    return text


def _prepare_output_root(config: dict[str, Any], layout: OutputLayout, dry_run: bool) -> tuple[bool, bool]:
    outputs_cfg = config.get("outputs", {})
    clean_start = bool(outputs_cfg.get("clean_start", False))
    root = layout.root.resolve()
    root_exists = root.exists()

    if clean_start:
        analysis_root = _analysis_root().resolve()
        repo_root = analysis_root.parent.resolve()
        if root == analysis_root:
            raise ValueError(
                "Refusing to clean outputs.root because it points at the analysis_pipeline source tree. "
                "Set outputs.root to a dedicated run directory first."
            )
        if root == repo_root:
            raise ValueError(
                "Refusing to clean outputs.root because it points at the repository root. "
                "Set outputs.root to a dedicated run directory first."
            )
        if root.parent == root:
            raise ValueError(f"Refusing to clean filesystem root: {root}")
        if _is_relative_to(analysis_root, root) or _is_relative_to(repo_root, root):
            raise ValueError(
                "Refusing to clean outputs.root because it is an ancestor of the source tree. "
                "Set outputs.root to a dedicated run directory first."
            )

    if dry_run:
        return root_exists, clean_start

    if clean_start and root_exists:
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)
    return root_exists, clean_start


def _resolve_path(path_text: str | None, base_dir: Path) -> Path | None:
    if path_text is None:
        return None
    text = str(path_text).strip()
    if not text:
        return None
    direct = Path(text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (base_dir / direct).resolve()


def _resolve_config_path(path_text: str | None) -> Path:
    if not path_text:
        return _config_default()
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    from_cwd = direct.resolve()
    if from_cwd.exists():
        return from_cwd
    repo_root = _analysis_root().parent.resolve()
    from_repo_root = (repo_root / direct).resolve()
    if from_repo_root.exists():
        return from_repo_root
    from_config_dir = (_analysis_root() / "config" / direct.name).resolve()
    if from_config_dir.exists():
        return from_config_dir
    return from_repo_root


def _display_repo_relative(path: Path) -> str:
    repo_root = _analysis_root().parent.resolve()
    resolved = path.resolve()
    if _is_relative_to(resolved, repo_root):
        return str(resolved.relative_to(repo_root))
    return str(resolved)


def _known_config_paths(extra_dir: Path | None = None) -> list[Path]:
    candidates: list[Path] = []
    seen: set[Path] = set()
    dirs: list[Path] = []
    if extra_dir is not None and extra_dir.exists():
        dirs.append(extra_dir.resolve())
    config_dir = (_analysis_root() / "config").resolve()
    if config_dir.exists() and config_dir not in dirs:
        dirs.append(config_dir)
    for directory in dirs:
        for pattern in ("*.yaml", "*.yml"):
            for candidate in sorted(directory.glob(pattern)):
                resolved = candidate.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                candidates.append(resolved)
    return candidates


def _resolve_bids_root(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd
    return (_analysis_root().parent / direct).resolve()


def _resolve_output_path_or_default(value: Any, default_path: Path, repo_root: Path) -> Path:
    if value is None:
        return default_path.resolve()
    text = str(value).strip()
    if not text:
        return default_path.resolve()
    resolved = _resolve_path(text, repo_root)
    return (resolved or default_path).resolve()


def _setdefault_arg(arg_map: dict[str, Any], key: str, value: Any) -> None:
    if value is None:
        return
    existing = arg_map.get(key)
    if existing is None:
        arg_map[key] = str(value) if isinstance(value, Path) else value
        return
    if isinstance(existing, str) and not existing.strip():
        arg_map[key] = str(value) if isinstance(value, Path) else value


def _default_trial_table_out(bids_root: Path) -> Path:
    return _reports_dir() / f"trial_table_{bids_root.name}.tsv"


def _default_trial_table_summary(out_path: Path) -> Path:
    return out_path.with_name(f"{out_path.stem}_summary.json")


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug(text: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "_" for ch in text.strip())
    out = "_".join(part for part in out.split("_") if part)
    return out or "default"


def _to_cli_args(arg_map: dict[str, Any] | None) -> list[str]:
    if not arg_map:
        return []
    cli: list[str] = []
    for key, value in arg_map.items():
        flag = f"--{str(key).strip().replace('_', '-')}"
        if value is None:
            continue
        if isinstance(value, bool):
            if value:
                cli.append(flag)
            continue
        if isinstance(value, list):
            if not value:
                continue
            cli.append(flag)
            cli.extend(str(item) for item in value)
            continue
        cli.extend([flag, str(value)])
    return cli


def _load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        message = f"Config file not found: {path}"
        candidates = _known_config_paths(path.parent)
        if candidates:
            matches = difflib.get_close_matches(
                path.name,
                [candidate.name for candidate in candidates],
                n=3,
                cutoff=0.45,
            )
            if matches:
                suggested = []
                seen: set[str] = set()
                for match in matches:
                    for candidate in candidates:
                        if candidate.name != match:
                            continue
                        display = _display_repo_relative(candidate)
                        if display in seen:
                            continue
                        seen.add(display)
                        suggested.append(display)
                if suggested:
                    message = f"{message}\nClosest matches:\n" + "\n".join(
                        f"  - {item}" for item in suggested
                    )
            else:
                available = ", ".join(_display_repo_relative(candidate) for candidate in candidates[:5])
                if available:
                    message = f"{message}\nAvailable configs: {available}"
        raise FileNotFoundError(message)
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Config root must be a mapping: {path}")
    return payload


def _stage_enabled(config: dict[str, Any], stage: str) -> bool:
    stages = config.get("stages", {})
    value = stages.get(stage, False)
    return bool(value)


def _append_stage_if_enabled(
    planned: list[PlannedStep],
    config: dict[str, Any],
    stage: str,
    only: set[str] | None,
    name: str,
    command: list[str],
    outputs: list[str],
    output_globs: list[str] | None = None,
) -> None:
    if not _stage_enabled(config, stage):
        return
    if only and stage not in only:
        return
    planned.append(
        PlannedStep(
            stage=stage,
            name=name,
            command=command,
            outputs=outputs,
            output_globs=list(output_globs or []),
        )
    )


def _plan_pipeline(
    config: dict[str, Any],
    config_path: Path,
    only: set[str] | None,
    scenario_filter: set[str] | None,
    auto_stage6_confusions: bool,
) -> tuple[list[PlannedStep], Path]:
    analysis_root = _analysis_root()
    repo_root = analysis_root.parent
    output_layout = _resolve_output_layout(config, repo_root)
    config = _expand_output_placeholders(config, output_layout)

    paths_cfg = config.get("paths", {})
    python_exe = str(paths_cfg.get("python_executable", sys.executable or "python"))
    bids_root = _resolve_bids_root(str(paths_cfg.get("bids_root", "./bids_arithmetic")))

    reports_cfg = config.get("reports", {})
    manifest_out = _resolve_path(reports_cfg.get("run_manifest"), repo_root) or (
        output_layout.reports_dir / "run_manifest.json"
    )

    stage_cfg = config.get("stage_args", {})
    selected_stages = {
        stage_name: _stage_enabled(config, stage_name) and (not only or stage_name in only)
        for stage_name in STAGE_ORDER
    }

    planned: list[PlannedStep] = []

    stage0_args = dict(stage_cfg.get("stage0", {}))
    stage0_out = _resolve_output_path_or_default(
        stage0_args.get("out"),
        output_layout.reports_dir / f"trial_table_{bids_root.name}.tsv",
        repo_root=repo_root,
    )
    stage0_summary = _resolve_output_path_or_default(
        stage0_args.get("summary_json"),
        _default_trial_table_summary(stage0_out),
        repo_root=repo_root,
    )
    _setdefault_arg(stage0_args, "out", stage0_out)
    _setdefault_arg(stage0_args, "summary_json", stage0_summary)
    cmd0 = [python_exe, str(analysis_root / "build_trial_table.py"), "--bids-root", str(bids_root)] + _to_cli_args(
        stage0_args
    )
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage0",
        only=only,
        name="stage0_trial_table",
        command=cmd0,
        outputs=[str(stage0_out), str(stage0_summary)],
    )

    stage1_args = dict(stage_cfg.get("stage1", {}))
    if selected_stages["stage0"]:
        _setdefault_arg(stage1_args, "trial_table", stage0_out)
    stage1_subject_table = _resolve_output_path_or_default(
        stage1_args.get("out_subject_table"),
        output_layout.reports_dir / "qc_subject_table.tsv",
        repo_root=repo_root,
    )
    stage1_summary = _resolve_output_path_or_default(
        stage1_args.get("out_summary_json"),
        output_layout.reports_dir / "qc_dataset_summary.json",
        repo_root=repo_root,
    )
    stage1_bids_sample_drop_summary_csv = _resolve_output_path_or_default(
        stage1_args.get("participant_bids_sample_drop_summary_csv"),
        output_layout.reports_dir / "participant_bids_sample_drop_summary.csv",
        repo_root=repo_root,
    )
    stage1_fig_dir = _resolve_output_path_or_default(
        stage1_args.get("fig_dir"),
        output_layout.reports_dir / "figures",
        repo_root=repo_root,
    )
    _setdefault_arg(stage1_args, "out_subject_table", stage1_subject_table)
    _setdefault_arg(stage1_args, "out_summary_json", stage1_summary)
    _setdefault_arg(stage1_args, "participant_bids_sample_drop_summary_csv", stage1_bids_sample_drop_summary_csv)
    _setdefault_arg(stage1_args, "fig_dir", stage1_fig_dir)
    stage1_figures = [
        stage1_fig_dir / "dropped_samples_main_per_subject.png",
        stage1_fig_dir / "dropped_samples_flagged_subjects_eeg_ecg.png",
        stage1_fig_dir / "pupil_mean_confidence_per_subject.png",
        stage1_fig_dir / "ecg_mean_hr_per_subject.png",
        stage1_fig_dir / "ecg_baseline_vs_task_hr_per_subject.png",
        stage1_fig_dir / "modality_coverage_heatmap.png",
    ]
    cmd1 = [python_exe, str(analysis_root / "stage1_qc_summary.py"), "--bids-root", str(bids_root)] + _to_cli_args(
        stage1_args
    )
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage1",
        only=only,
        name="stage1_qc",
        command=cmd1,
        outputs=[
            str(stage1_subject_table),
            str(stage1_summary),
            str(stage1_bids_sample_drop_summary_csv),
            *[str(path) for path in stage1_figures],
        ],
    )

    stage2_args = dict(stage_cfg.get("stage2", {}))
    stage2_out_root = _resolve_output_path_or_default(
        stage2_args.get("out_root"),
        output_layout.cleaned_dir,
        repo_root=repo_root,
    )
    stage2_reports_dir = _resolve_output_path_or_default(
        stage2_args.get("reports_dir"),
        output_layout.reports_dir,
        repo_root=repo_root,
    )
    stage2_log = _resolve_output_path_or_default(
        stage2_args.get("preprocess_log_out"),
        stage2_reports_dir / "preprocess_log.tsv",
        repo_root=repo_root,
    )
    stage2_summary = _resolve_output_path_or_default(
        stage2_args.get("summary_json"),
        stage2_reports_dir / "preprocess_summary.json",
        repo_root=repo_root,
    )
    _setdefault_arg(stage2_args, "out_root", stage2_out_root)
    _setdefault_arg(stage2_args, "reports_dir", stage2_reports_dir)
    _setdefault_arg(stage2_args, "preprocess_log_out", stage2_log)
    _setdefault_arg(stage2_args, "summary_json", stage2_summary)
    cmd2 = [python_exe, str(analysis_root / "stage2_preprocess.py"), "--bids-root", str(bids_root)] + _to_cli_args(
        stage2_args
    )
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage2",
        only=only,
        name="stage2_preprocess",
        command=cmd2,
        outputs=[str(stage2_log), str(stage2_summary)],
    )

    stage3_args = dict(stage_cfg.get("stage3", {}))
    if selected_stages["stage0"]:
        _setdefault_arg(stage3_args, "trial_table", stage0_out)
    if selected_stages["stage2"]:
        _setdefault_arg(stage3_args, "cleaned_root", stage2_out_root)
    stage3_out_root = _resolve_output_path_or_default(
        stage3_args.get("out_root"),
        output_layout.epochs_dir,
        repo_root=repo_root,
    )
    stage3_manifest = _resolve_output_path_or_default(
        stage3_args.get("manifest_out"),
        output_layout.reports_dir / "epoch_manifest.tsv",
        repo_root=repo_root,
    )
    stage3_summary = _resolve_output_path_or_default(
        stage3_args.get("summary_json"),
        output_layout.reports_dir / "epoch_summary.json",
        repo_root=repo_root,
    )
    stage3_drop_log = _resolve_output_path_or_default(
        stage3_args.get("drop_log_out"),
        output_layout.reports_dir / "epoch_drop_log.tsv",
        repo_root=repo_root,
    )
    stage3_participant_sample_summary_csv = _resolve_output_path_or_default(
        stage3_args.get("participant_sample_summary_csv"),
        output_layout.reports_dir / "participant_sample_capture_drop_summary.csv",
        repo_root=repo_root,
    )
    stage3_fig_dir = _resolve_output_path_or_default(
        stage3_args.get("fig_dir"),
        output_layout.reports_dir / "figures",
        repo_root=repo_root,
    )
    _setdefault_arg(stage3_args, "out_root", stage3_out_root)
    _setdefault_arg(stage3_args, "manifest_out", stage3_manifest)
    _setdefault_arg(stage3_args, "summary_json", stage3_summary)
    _setdefault_arg(stage3_args, "drop_log_out", stage3_drop_log)
    _setdefault_arg(stage3_args, "participant_sample_summary_csv", stage3_participant_sample_summary_csv)
    _setdefault_arg(stage3_args, "fig_dir", stage3_fig_dir)
    cmd3 = [python_exe, str(analysis_root / "stage3_epoch_trials.py"), "--bids-root", str(bids_root)] + _to_cli_args(
        stage3_args
    )
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage3",
        only=only,
        name="stage3_epoch",
        command=cmd3,
        outputs=[
            str(stage3_manifest),
            str(stage3_summary),
            str(stage3_drop_log),
            str(stage3_participant_sample_summary_csv),
            str(stage3_fig_dir / "segmentation_dropped_windows_due_missing_samples_eeg_ecg.png"),
        ],
        output_globs=[str(stage3_out_root / "**" / "*.npz")],
    )

    stage4_args = dict(stage_cfg.get("stage4", {}))
    if selected_stages["stage3"]:
        _setdefault_arg(stage4_args, "epoch_manifest", stage3_manifest)
    if selected_stages["stage2"]:
        _setdefault_arg(stage4_args, "cleaned_root", stage2_out_root)
    stage4_out_dir = _resolve_output_path_or_default(
        stage4_args.get("out_dir"),
        output_layout.features_dir,
        repo_root=repo_root,
    )
    stage4_summary = _resolve_output_path_or_default(
        stage4_args.get("summary_json"),
        output_layout.reports_dir / "feature_summary.json",
        repo_root=repo_root,
    )
    _setdefault_arg(stage4_args, "out_dir", stage4_out_dir)
    _setdefault_arg(stage4_args, "summary_json", stage4_summary)
    if selected_stages["stage2"]:
        _setdefault_arg(stage4_args, "preprocess_summary_json", stage2_summary)
    cmd4 = [python_exe, str(analysis_root / "stage4_extract_features.py"), "--bids-root", str(bids_root)] + _to_cli_args(
        stage4_args
    )
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage4",
        only=only,
        name="stage4_features",
        command=cmd4,
        outputs=[
            str(stage4_out_dir / "features_eeg.tsv"),
            str(stage4_out_dir / "features_ecg.tsv"),
            str(stage4_out_dir / "features_pupil.tsv"),
            str(stage4_summary),
        ],
    )

    stage5_args = dict(stage_cfg.get("stage5", {}))
    if selected_stages["stage0"]:
        _setdefault_arg(stage5_args, "trial_table", stage0_out)
    if selected_stages["stage3"]:
        _setdefault_arg(stage5_args, "epoch_manifest", stage3_manifest)
    stage5_features_dir = _resolve_output_path_or_default(
        stage5_args.get("features_dir"),
        output_layout.features_dir,
        repo_root=repo_root,
    )
    stage5_fused_out = _resolve_output_path_or_default(
        stage5_args.get("fused_out"),
        stage5_features_dir / "features_fused.tsv",
        repo_root=repo_root,
    )
    stage5_split_manifest = _resolve_output_path_or_default(
        stage5_args.get("split_manifest_out"),
        stage5_features_dir / "split_manifest.json",
        repo_root=repo_root,
    )
    stage5_summary = _resolve_output_path_or_default(
        stage5_args.get("summary_json"),
        output_layout.reports_dir / "fusion_summary.json",
        repo_root=repo_root,
    )
    _setdefault_arg(stage5_args, "features_dir", stage5_features_dir)
    _setdefault_arg(stage5_args, "fused_out", stage5_fused_out)
    _setdefault_arg(stage5_args, "split_manifest_out", stage5_split_manifest)
    _setdefault_arg(stage5_args, "summary_json", stage5_summary)
    modalities_raw = stage5_args.get("modalities", ["eeg", "ecg", "pupil"])
    modalities_list = modalities_raw if isinstance(modalities_raw, list) else [modalities_raw]
    selected_modalities = [
        str(modality).strip().lower() for modality in modalities_list if str(modality).strip()
    ] or ["eeg", "ecg", "pupil"]
    selected_modalities = list(dict.fromkeys(selected_modalities))
    unimodal_tag = str(stage5_args.get("unimodal_tag", "")).strip()
    unimodal_suffix = f"_{unimodal_tag}" if unimodal_tag else ""
    stage5_unimodal_outputs = [
        stage5_features_dir / f"features_ml_{modality}{unimodal_suffix}.tsv" for modality in selected_modalities
    ]
    cmd5 = [python_exe, str(analysis_root / "stage5_build_fused_table.py"), "--bids-root", str(bids_root)] + _to_cli_args(
        stage5_args
    )
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage5",
        only=only,
        name="stage5_fusion",
        command=cmd5,
        outputs=[
            *[str(path) for path in stage5_unimodal_outputs],
            str(stage5_fused_out),
            str(stage5_split_manifest),
            str(stage5_summary),
        ],
    )

    run_stage6 = _stage_enabled(config, "stage6") and (not only or "stage6" in only)
    only_for_confusions = only
    run_stage6_confusions = _stage_enabled(config, "stage6_confusions") and (not only or "stage6_confusions" in only)
    if auto_stage6_confusions and run_stage6 and only and "stage6_confusions" not in only:
        run_stage6_confusions = True
        only_for_confusions = set(only)
        only_for_confusions.add("stage6_confusions")

    stage6_results_for_report: list[Path] = []
    if run_stage6 or run_stage6_confusions:
        stage6_cfg = config.get("stage6", {})
        stage6_base = dict(stage6_cfg.get("base_args", {}))
        scenarios = list(stage6_cfg.get("class_scenarios", []))
        if not scenarios:
            scenarios = [{"name": "default"}]

        for scenario in scenarios:
            scenario_name = str(scenario.get("name", "default"))
            scenario_slug = _slug(scenario_name)
            if scenario_filter and scenario_slug not in scenario_filter and scenario_name not in scenario_filter:
                continue

            args6 = dict(stage6_base)
            args6["class_scenario_name"] = scenario_name
            if selected_stages["stage5"]:
                _setdefault_arg(args6, "split_manifest", stage5_split_manifest)
            if scenario.get("include_labels"):
                args6["class_include_labels"] = list(scenario.get("include_labels", []))
            if scenario.get("drop_labels"):
                args6["class_drop_labels"] = list(scenario.get("drop_labels", []))
            merge_map = scenario.get("merge_map", {}) or {}
            merge_args: list[str] = []
            for src, dst in merge_map.items():
                merge_args.append(f"{src}->{dst}")

            results_template = str(
                stage6_cfg.get("results_json_template", str(output_layout.reports_dir / "ml_results_{scenario}.json"))
            )
            summary_template = str(
                stage6_cfg.get("summary_md_template", str(output_layout.reports_dir / "ml_summary_{scenario}.md"))
            )
            run_tag_prefix = str(stage6_cfg.get("run_tag_prefix", "stage7"))
            results_json = results_template.format(scenario=scenario_slug)
            summary_md = summary_template.format(scenario=scenario_slug)
            results_json_resolved = _resolve_path(results_json, repo_root) or (repo_root / results_json).resolve()
            summary_md_resolved = _resolve_path(summary_md, repo_root) or (repo_root / summary_md).resolve()
            live_conf_pngs_enabled = bool(args6.get("live_confusion_pngs", True))
            eeg_condition_psd_enabled = bool(args6.get("eeg_condition_psd_plots", True))
            live_conf_globs: list[str] = []
            if live_conf_pngs_enabled:
                live_conf_dir = _resolve_output_path_or_default(
                    args6.get("live_confusion_png_dir"),
                    output_layout.reports_dir / "confusion_pngs_live",
                    repo_root=repo_root,
                )
                _setdefault_arg(args6, "live_confusion_png_dir", live_conf_dir)
                live_conf_globs.append(str(live_conf_dir / scenario_slug / "**" / "*.png"))
            eeg_condition_psd_outputs: list[str] = []
            if eeg_condition_psd_enabled:
                eeg_condition_psd_dir = _resolve_output_path_or_default(
                    args6.get("eeg_condition_psd_dir"),
                    output_layout.reports_dir / "eeg_condition_psd",
                    repo_root=repo_root,
                )
                _setdefault_arg(args6, "eeg_condition_psd_dir", eeg_condition_psd_dir)
                eeg_condition_psd_outputs.append(str(eeg_condition_psd_dir / scenario_slug / "manifest.json"))
                datasets_raw = args6.get("datasets")
                datasets_list = datasets_raw if isinstance(datasets_raw, list) else ([datasets_raw] if datasets_raw else [])
                datasets_norm = [str(item).strip().lower() for item in datasets_list if str(item).strip()]
                if not datasets_norm or "eeg" in datasets_norm:
                    live_conf_globs.append(str(eeg_condition_psd_dir / scenario_slug / "**" / "*.png"))
            models_root = _resolve_output_path_or_default(
                args6.get("models_root"),
                output_layout.models_dir,
                repo_root=repo_root,
            )
            _setdefault_arg(args6, "models_root", models_root)
            run_tag = f"{run_tag_prefix}_{scenario_slug}"

            cmd6 = [
                python_exe,
                str(analysis_root / "stage6_train_classic_ml.py"),
                "--bids-root",
                str(bids_root),
                "--run-tag",
                run_tag,
                "--results-json",
                results_json,
                "--summary-md",
                summary_md,
            ] + _to_cli_args(args6)
            for merge_arg in merge_args:
                cmd6.extend(["--class-merge", merge_arg])

            if run_stage6:
                stage6_results_for_report.append(results_json_resolved)
                _append_stage_if_enabled(
                    planned=planned,
                    config=config,
                    stage="stage6",
                    only=only,
                    name=f"stage6_ml_{scenario_slug}",
                    command=cmd6,
                    outputs=[str(results_json_resolved), str(summary_md_resolved), *eeg_condition_psd_outputs],
                    output_globs=live_conf_globs,
                )

            if run_stage6_confusions:
                conf_cfg = config.get("stage6_confusions", {})
                conf_args = dict(conf_cfg.get("args", {}))
                conf_out_json_tmpl = str(
                    conf_cfg.get(
                        "out_json_template",
                        str(output_layout.reports_dir / "confusion_highlights_{scenario}.json"),
                    )
                )
                conf_out_md_tmpl = str(
                    conf_cfg.get(
                        "out_md_template",
                        str(output_layout.reports_dir / "confusion_highlights_{scenario}.md"),
                    )
                )
                conf_out_json = conf_out_json_tmpl.format(scenario=scenario_slug)
                conf_out_md = conf_out_md_tmpl.format(scenario=scenario_slug)
                conf_out_json_resolved = _resolve_path(conf_out_json, repo_root) or (repo_root / conf_out_json).resolve()
                conf_out_md_resolved = _resolve_path(conf_out_md, repo_root) or (repo_root / conf_out_md).resolve()
                conf_png_dir = _resolve_output_path_or_default(
                    conf_args.get("out_png_dir"),
                    output_layout.reports_dir / "confusion_pngs",
                    repo_root=repo_root,
                )
                _setdefault_arg(conf_args, "out_png_dir", conf_png_dir)
                conf_png_glob = str(conf_png_dir / _slug(Path(results_json).stem) / "**" / "*.png")
                cmd_conf = [
                    python_exe,
                    str(analysis_root / "stage6_highlight_confusions.py"),
                    "--results-json",
                    results_json,
                    "--out-json",
                    conf_out_json,
                    "--out-md",
                    conf_out_md,
                ] + _to_cli_args(conf_args)
                _append_stage_if_enabled(
                    planned=planned,
                    config=config,
                    stage="stage6_confusions",
                    only=only_for_confusions,
                    name=f"stage6_confusions_{scenario_slug}",
                    command=cmd_conf,
                    outputs=[
                        str(conf_out_json_resolved),
                        str(conf_out_md_resolved),
                    ],
                    output_globs=[conf_png_glob],
                )

    stage6_pub_cfg = config.get("stage6_publication_report", {})
    stage6_pub_args = dict(stage6_pub_cfg.get("args", {}))
    if stage6_results_for_report and "results_json" not in stage6_pub_args and "results_json_glob" not in stage6_pub_args:
        stage6_pub_args["results_json"] = [str(path) for path in stage6_results_for_report]
    if "qc_summary_json" not in stage6_pub_args:
        stage6_pub_args["qc_summary_json"] = str(stage1_summary)
    if "epoch_summary_json" not in stage6_pub_args:
        stage6_pub_args["epoch_summary_json"] = str(stage3_summary)
    if "feature_summary_json" not in stage6_pub_args:
        stage6_pub_args["feature_summary_json"] = str(stage4_summary)
    if "fusion_summary_json" not in stage6_pub_args:
        stage6_pub_args["fusion_summary_json"] = str(stage5_summary)
    if "run_manifest_json" not in stage6_pub_args:
        stage6_pub_args["run_manifest_json"] = str(manifest_out)

    stage6_pub_out_md = _resolve_output_path_or_default(
        stage6_pub_args.get("out_md"),
        output_layout.reports_dir / "publication_full_report.md",
        repo_root=repo_root,
    )
    stage6_pub_out_json = _resolve_output_path_or_default(
        stage6_pub_args.get("out_json"),
        output_layout.reports_dir / "publication_full_report.json",
        repo_root=repo_root,
    )
    _setdefault_arg(stage6_pub_args, "out_md", stage6_pub_out_md)
    _setdefault_arg(stage6_pub_args, "out_json", stage6_pub_out_json)
    cmd_stage6_pub = [python_exe, str(analysis_root / "stage6_build_publication_report.py")] + _to_cli_args(stage6_pub_args)
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage6_publication_report",
        only=only,
        name="stage6_publication_report",
        command=cmd_stage6_pub,
        outputs=[str(stage6_pub_out_md), str(stage6_pub_out_json)],
    )

    # ------------------------------------------------------------------
    # Stage 7 — significance and bootstrap statistics
    # ------------------------------------------------------------------
    stage7_cfg = config.get("stage7_significance", {})
    stage7_args = dict(stage7_cfg.get("args", {}))
    if "baseline_reports" not in stage7_args:
        stage7_args["baseline_reports"] = str(output_layout.reports_dir)
    stage7_out_json = _resolve_output_path_or_default(
        stage7_args.get("out_json"),
        output_layout.reports_dir / "significance_summary.json",
        repo_root=repo_root,
    )
    stage7_out_md = _resolve_output_path_or_default(
        stage7_args.get("out_md"),
        output_layout.reports_dir / "significance_summary.md",
        repo_root=repo_root,
    )
    _setdefault_arg(stage7_args, "out_json", stage7_out_json)
    _setdefault_arg(stage7_args, "out_md", stage7_out_md)
    cmd_stage7 = [
        python_exe,
        "-m",
        "analysis_pipeline.stage7_significance",
    ] + _to_cli_args(stage7_args)
    _append_stage_if_enabled(
        planned=planned,
        config=config,
        stage="stage7_significance",
        only=only,
        name="stage7_significance",
        command=cmd_stage7,
        outputs=[str(stage7_out_json), str(stage7_out_md)],
    )

    return planned, manifest_out


def _resolve_runtime_path(path_text: str, workdir: Path) -> Path:
    direct = Path(str(path_text)).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (workdir / direct).resolve()


def _verify_step_outputs(step: PlannedStep, workdir: Path) -> dict[str, Any]:
    checks: dict[str, Any] = {
        "paths": [],
        "globs": [],
        "missing_paths": [],
        "missing_globs": [],
        "ok": True,
    }

    for output_text in step.outputs:
        output_path = _resolve_runtime_path(output_text, workdir)
        exists = output_path.exists()
        checks["paths"].append({"path": str(output_path), "exists": bool(exists)})
        if not exists:
            checks["missing_paths"].append(str(output_path))

    for pattern in step.output_globs:
        resolved_pattern = str(_resolve_runtime_path(pattern, workdir))
        matches = sorted({str(Path(item).resolve()) for item in glob.glob(resolved_pattern, recursive=True)})
        checks["globs"].append({"pattern": resolved_pattern, "matches": matches, "matched_count": len(matches)})
        if not matches:
            checks["missing_globs"].append(resolved_pattern)

    checks["ok"] = not checks["missing_paths"] and not checks["missing_globs"]
    return checks


def _extract_flag_list_values(command: list[str], flag: str) -> list[str] | None:
    try:
        start = command.index(flag)
    except ValueError:
        return None

    values: list[str] = []
    for part in command[start + 1 :]:
        if part.startswith("--"):
            break
        values.append(part)
    return values


def _replace_flag_list_values(command: list[str], flag: str, values: list[str]) -> list[str]:
    updated: list[str] = []
    inserted = False
    idx = 0
    while idx < len(command):
        part = command[idx]
        if part == flag:
            inserted = True
            if values:
                updated.append(flag)
                updated.extend(values)
            idx += 1
            while idx < len(command) and not command[idx].startswith("--"):
                idx += 1
            continue
        updated.append(part)
        idx += 1

    if not inserted and values:
        updated.append(flag)
        updated.extend(values)
    return updated


def _replace_flag_value(command: list[str], flag: str, value: str | None) -> list[str]:
    updated: list[str] = []
    inserted = False
    idx = 0
    while idx < len(command):
        part = command[idx]
        if part == flag:
            inserted = True
            if value is not None:
                updated.extend([flag, value])
            idx += 2
            continue
        updated.append(part)
        idx += 1

    if not inserted and value is not None:
        updated.extend([flag, value])
    return updated


def _load_stage1_subject_filter(summary_path: Path) -> list[str] | None:
    if not summary_path.exists():
        raise FileNotFoundError(summary_path)

    payload = json.loads(summary_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Stage 1 summary is not a JSON object: {summary_path}")

    if not bool(payload.get("strict_mode", False)):
        return None

    carried_forward = list(payload.get("subjects_carried_forward_after_qc", []) or [])
    carried_forward = sorted({str(subject).strip() for subject in carried_forward if str(subject).strip()})
    if not carried_forward:
        raise RuntimeError(
            "Stage 1 strict QC rejected all subjects; no participants remain to carry forward."
        )
    return carried_forward


def _apply_subject_filter_to_step(
    step: PlannedStep,
    carried_forward_subjects: list[str],
    stage1_summary_path: Path | None = None,
) -> PlannedStep:
    if step.stage not in {"stage2", "stage3", "stage4", "stage5"}:
        return step

    existing_subjects = _extract_flag_list_values(step.command, "--subjects")
    if existing_subjects is None:
        filtered_subjects = list(carried_forward_subjects)
    else:
        carried_forward_set = set(carried_forward_subjects)
        filtered_subjects = [subject for subject in existing_subjects if subject in carried_forward_set]

    if not filtered_subjects:
        raise RuntimeError(
            f"Stage 1 strict QC left no subjects available for downstream step {step.name}."
        )

    updated_command = _replace_flag_list_values(step.command, "--subjects", filtered_subjects)
    if step.stage == "stage5" and stage1_summary_path is not None:
        updated_command = _replace_flag_value(
            updated_command,
            "--qc-summary-json",
            str(stage1_summary_path),
        )

    return PlannedStep(
        stage=step.stage,
        name=step.name,
        command=updated_command,
        outputs=step.outputs,
        output_globs=step.output_globs,
    )


def _run_step(
    step: PlannedStep,
    workdir: Path,
    logs_dir: Path,
    dry_run: bool,
    strict_outputs: bool,
) -> dict[str, Any]:
    start = _utc_now()
    record: dict[str, Any] = {
        "stage": step.stage,
        "name": step.name,
        "command": step.command,
        "command_shell": " ".join(shlex.quote(part) for part in step.command),
        "cwd": str(workdir),
        "started_utc": start,
        "outputs": step.outputs,
        "output_globs": step.output_globs,
    }

    if dry_run:
        record["ended_utc"] = _utc_now()
        record["return_code"] = 0
        record["status"] = "dry_run"
        return record

    logs_dir.mkdir(parents=True, exist_ok=True)
    stdout_log = logs_dir / f"{step.name}.stdout.log"
    stderr_log = logs_dir / f"{step.name}.stderr.log"
    record["stdout_log"] = str(stdout_log)
    record["stderr_log"] = str(stderr_log)

    with stdout_log.open("w", encoding="utf-8") as out_f, stderr_log.open("w", encoding="utf-8") as err_f:
        proc = subprocess.run(step.command, cwd=workdir, text=True, stdout=out_f, stderr=err_f, check=False)

    record["ended_utc"] = _utc_now()
    record["return_code"] = int(proc.returncode)
    record["status"] = "ok" if proc.returncode == 0 else "failed"
    if proc.returncode == 0:
        output_checks = _verify_step_outputs(step=step, workdir=workdir)
        record["output_checks"] = output_checks
        if strict_outputs and not output_checks.get("ok", False):
            record["status"] = "failed_outputs"
            record["return_code"] = 99
            record["error"] = (
                "Expected outputs were not produced. "
                "See output_checks.missing_paths and output_checks.missing_globs."
            )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Pipeline entrypoint. Executes configured stages and writes a run manifest "
            "with commands, logs, outputs, and status."
        )
    )
    parser.add_argument("--config", default=None, help="Path to pipeline YAML config.")
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help=f"Optional stage filter. Valid: {', '.join(STAGE_ORDER)}",
    )
    parser.add_argument(
        "--stage6-scenarios",
        nargs="*",
        default=None,
        help="Optional Stage 6 scenario name/slug filter.",
    )
    parser.add_argument(
        "--no-auto-stage6-confusions",
        action="store_true",
        help=(
            "Do not auto-run stage6_confusions when running --only stage6. "
            "Default behavior is to auto-run confusion generation so PNGs are produced with Stage 6."
        ),
    )
    parser.add_argument(
        "--no-strict-outputs",
        action="store_true",
        help=(
            "Do not fail the run if a step returns code 0 but expected outputs are missing. "
            "Missing outputs are still reported in logs and run manifest."
        ),
    )
    parser.add_argument("--dry-run", action="store_true", help="Plan and print commands without executing.")
    args = parser.parse_args()

    config_path = _resolve_config_path(args.config)
    config = _load_config(config_path)
    output_layout = _resolve_output_layout(config, _analysis_root().parent)
    output_root_preexisting, output_root_clean_start = _prepare_output_root(
        config=config,
        layout=output_layout,
        dry_run=bool(args.dry_run),
    )

    only = set(args.only) if args.only else None
    if only:
        unknown = sorted(only - set(STAGE_ORDER))
        if unknown:
            raise ValueError(f"Unknown --only stages: {', '.join(unknown)}")
    scenario_filter = set(args.stage6_scenarios) if args.stage6_scenarios else None

    steps, manifest_out = _plan_pipeline(
        config=config,
        config_path=config_path,
        only=only,
        scenario_filter=scenario_filter,
        auto_stage6_confusions=not bool(args.no_auto_stage6_confusions),
    )
    if not steps:
        raise ValueError("No steps were selected. Check stage toggles, --only, and --stage6-scenarios.")

    run_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    logs_dir = manifest_out.parent / "run_logs" / run_stamp
    workdir = _analysis_root().parent
    pipeline_start = time.time()
    total_steps = len(steps)
    strict_outputs = not bool(args.no_strict_outputs)
    carried_forward_subjects: list[str] | None = None
    stage1_summary_path: Path | None = None

    print("Pipeline run starting.")
    print(f"  Config: {config_path}")
    print(f"  Working directory: {workdir}")
    print(f"  Dry run: {bool(args.dry_run)}")
    print(f"  Strict outputs: {strict_outputs}")
    print(f"  Output root: {output_layout.root}")
    print(f"  Output root existed: {output_root_preexisting}")
    print(f"  Output root clean_start: {output_root_clean_start}")
    print(f"  Planned steps: {total_steps}")
    for idx, step in enumerate(steps, start=1):
        print(
            f"    {idx}. [{step.stage}] {step.name} "
            f"(expected_paths={len(step.outputs)}, expected_globs={len(step.output_globs)})"
        )

    manifest: dict[str, Any] = {
        "pipeline_started_utc": _utc_now(),
        "pipeline_finished_utc": None,
        "status": "running",
        "config_path": str(config_path),
        "manifest_path": str(manifest_out),
        "dry_run": bool(args.dry_run),
        "system": {
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "hostname": platform.node(),
            "pid": os.getpid(),
        },
        "working_directory": str(workdir),
        "output_root": {
            "path": str(output_layout.root),
            "preexisting": bool(output_root_preexisting),
            "clean_start": bool(output_root_clean_start),
        },
        "steps": [],
    }

    try:
        for step_index, planned_step in enumerate(steps, start=1):
            step = planned_step
            if carried_forward_subjects is not None and step.stage in {"stage2", "stage3", "stage4", "stage5"}:
                step = _apply_subject_filter_to_step(
                    step=step,
                    carried_forward_subjects=carried_forward_subjects,
                    stage1_summary_path=stage1_summary_path,
                )
            step_start = time.time()
            print(f"[{step_index}/{total_steps}] [{step.stage}] {step.name}")
            if carried_forward_subjects is not None and step.stage in {"stage2", "stage3", "stage4", "stage5"}:
                print(
                    "  Stage 1 QC carry-forward subjects: "
                    f"{len(carried_forward_subjects)}"
                )
            print("  " + " ".join(shlex.quote(part) for part in step.command))
            if step.outputs:
                print("  Expected paths:")
                for output in step.outputs:
                    print(f"    - {output}")
            if step.output_globs:
                print("  Expected globs:")
                for pattern in step.output_globs:
                    print(f"    - {pattern}")
            step_result = _run_step(
                step=step,
                workdir=workdir,
                logs_dir=logs_dir,
                dry_run=args.dry_run,
                strict_outputs=strict_outputs,
            )
            manifest["steps"].append(step_result)
            elapsed_s = time.time() - step_start
            print(f"  Status: {step_result['status']} (elapsed={elapsed_s:.1f}s)")
            if step.stage == "stage1" and step_result["status"] == "ok" and not args.dry_run:
                stage1_summary_output = next(
                    (
                        output
                        for output in step.outputs
                        if Path(str(output)).name == "qc_dataset_summary.json"
                    ),
                    step.outputs[1] if len(step.outputs) > 1 else None,
                )
                if stage1_summary_output is None:
                    raise RuntimeError("Could not determine Stage 1 QC summary output path.")
                stage1_summary_path = _resolve_runtime_path(stage1_summary_output, workdir)
                carried_forward_subjects = _load_stage1_subject_filter(stage1_summary_path)
                if carried_forward_subjects is not None:
                    step_result["subjects_carried_forward_after_qc"] = carried_forward_subjects
                    step_result["stage1_qc_summary_json"] = str(stage1_summary_path)
                    print(
                        "  Stage 1 strict QC carry-forward set: "
                        f"{', '.join(carried_forward_subjects)}"
                    )
                else:
                    print(
                        "  Stage 1 strict QC carry-forward filter inactive; "
                        "later stages keep their configured subject scope."
                    )
            output_checks = step_result.get("output_checks")
            if output_checks:
                path_checks = list(output_checks.get("paths", []))
                glob_checks = list(output_checks.get("globs", []))
                path_ok = sum(1 for row in path_checks if row.get("exists"))
                print(f"  Output check (paths): {path_ok}/{len(path_checks)}")
                for pattern_check in glob_checks:
                    print(
                        "  Output check (glob): "
                        f"{pattern_check.get('matched_count', 0)} match(es) for {pattern_check.get('pattern', '')}"
                    )
                missing_paths = list(output_checks.get("missing_paths", []))
                missing_globs = list(output_checks.get("missing_globs", []))
                if missing_paths:
                    print("  Missing expected paths:")
                    for missing in missing_paths:
                        print(f"    - {missing}")
                if missing_globs:
                    print("  Missing expected globs:")
                    for missing in missing_globs:
                        print(f"    - {missing}")
            if step_result["return_code"] != 0 or step_result["status"] not in ("ok", "dry_run"):
                if step_result.get("stdout_log"):
                    print(f"  stdout log: {step_result['stdout_log']}")
                if step_result.get("stderr_log"):
                    print(f"  stderr log: {step_result['stderr_log']}")
                raise RuntimeError(
                    f"Step failed: {step.name} "
                    f"(status={step_result['status']}, return_code={step_result['return_code']})"
                )
        manifest["status"] = "dry_run" if args.dry_run else "success"
    except Exception as exc:  # noqa: BLE001
        manifest["status"] = "failed"
        manifest["error"] = str(exc)
        raise
    finally:
        manifest["pipeline_finished_utc"] = _utc_now()
        manifest_out.parent.mkdir(parents=True, exist_ok=True)
        manifest_out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        status_counts: dict[str, int] = {}
        for step_record in manifest.get("steps", []):
            status_name = str(step_record.get("status", "unknown"))
            status_counts[status_name] = status_counts.get(status_name, 0) + 1
        print(f"Pipeline status: {manifest['status']}")
        print(f"Pipeline elapsed seconds: {time.time() - pipeline_start:.1f}")
        print(f"Step status counts: {json.dumps(status_counts, sort_keys=True)}")
        print(f"Run manifest: {manifest_out}")


if __name__ == "__main__":
    main()

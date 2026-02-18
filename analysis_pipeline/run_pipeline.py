from __future__ import annotations

import argparse
import json
import os
import platform
import shlex
import subprocess
import sys
from dataclasses import dataclass
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


STAGE_ORDER = ["stage0", "stage1", "stage2", "stage3", "stage4", "stage5", "stage6", "stage6_confusions"]


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _config_default() -> Path:
    return _analysis_root() / "config" / "pipeline.yaml"


def _manifest_default() -> Path:
    return _reports_dir() / "run_manifest.json"


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


def _resolve_bids_root(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd
    return (_analysis_root().parent / direct).resolve()


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
        raise FileNotFoundError(path)
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
) -> None:
    if not _stage_enabled(config, stage):
        return
    if only and stage not in only:
        return
    planned.append(PlannedStep(stage=stage, name=name, command=command, outputs=outputs))


def _plan_pipeline(
    config: dict[str, Any],
    config_path: Path,
    only: set[str] | None,
    scenario_filter: set[str] | None,
) -> tuple[list[PlannedStep], Path]:
    analysis_root = _analysis_root()
    repo_root = analysis_root.parent

    paths_cfg = config.get("paths", {})
    python_exe = str(paths_cfg.get("python_executable", sys.executable or "python"))
    bids_root = _resolve_bids_root(str(paths_cfg.get("bids_root", "./bids_arithmetic")))

    reports_cfg = config.get("reports", {})
    manifest_out = _resolve_path(reports_cfg.get("run_manifest"), repo_root) or _manifest_default()

    stage_cfg = config.get("stage_args", {})

    planned: list[PlannedStep] = []

    stage0_args = dict(stage_cfg.get("stage0", {}))
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
        outputs=[],
    )

    stage1_args = dict(stage_cfg.get("stage1", {}))
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
        outputs=[],
    )

    stage2_args = dict(stage_cfg.get("stage2", {}))
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
        outputs=[],
    )

    stage3_args = dict(stage_cfg.get("stage3", {}))
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
        outputs=[],
    )

    stage4_args = dict(stage_cfg.get("stage4", {}))
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
        outputs=[],
    )

    stage5_args = dict(stage_cfg.get("stage5", {}))
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
        outputs=[],
    )

    run_stage6 = _stage_enabled(config, "stage6") and (not only or "stage6" in only)
    run_stage6_confusions = _stage_enabled(config, "stage6_confusions") and (not only or "stage6_confusions" in only)

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
            if scenario.get("include_labels"):
                args6["class_include_labels"] = list(scenario.get("include_labels", []))
            if scenario.get("drop_labels"):
                args6["class_drop_labels"] = list(scenario.get("drop_labels", []))
            merge_map = scenario.get("merge_map", {}) or {}
            merge_args: list[str] = []
            for src, dst in merge_map.items():
                merge_args.append(f"{src}->{dst}")

            results_template = str(stage6_cfg.get("results_json_template", "analysis_pipeline/reports/ml_results_{scenario}.json"))
            summary_template = str(stage6_cfg.get("summary_md_template", "analysis_pipeline/reports/ml_summary_{scenario}.md"))
            run_tag_prefix = str(stage6_cfg.get("run_tag_prefix", "stage7"))
            results_json = results_template.format(scenario=scenario_slug)
            summary_md = summary_template.format(scenario=scenario_slug)
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
                _append_stage_if_enabled(
                    planned=planned,
                    config=config,
                    stage="stage6",
                    only=only,
                    name=f"stage6_ml_{scenario_slug}",
                    command=cmd6,
                    outputs=[results_json, summary_md],
                )

            if run_stage6_confusions:
                conf_cfg = config.get("stage6_confusions", {})
                conf_out_json_tmpl = str(
                    conf_cfg.get(
                        "out_json_template",
                        "analysis_pipeline/reports/confusion_highlights_{scenario}.json",
                    )
                )
                conf_out_md_tmpl = str(
                    conf_cfg.get(
                        "out_md_template",
                        "analysis_pipeline/reports/confusion_highlights_{scenario}.md",
                    )
                )
                cmd_conf = [
                    python_exe,
                    str(analysis_root / "stage6_highlight_confusions.py"),
                    "--results-json",
                    results_json,
                    "--out-json",
                    conf_out_json_tmpl.format(scenario=scenario_slug),
                    "--out-md",
                    conf_out_md_tmpl.format(scenario=scenario_slug),
                ] + _to_cli_args(dict(conf_cfg.get("args", {})))
                _append_stage_if_enabled(
                    planned=planned,
                    config=config,
                    stage="stage6_confusions",
                    only=only,
                    name=f"stage6_confusions_{scenario_slug}",
                    command=cmd_conf,
                    outputs=[
                        conf_out_json_tmpl.format(scenario=scenario_slug),
                        conf_out_md_tmpl.format(scenario=scenario_slug),
                    ],
                )

    return planned, manifest_out


def _run_step(
    step: PlannedStep,
    workdir: Path,
    logs_dir: Path,
    dry_run: bool,
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
    return record


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 7 pipeline entrypoint. Executes configured stages and writes a run manifest "
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
    parser.add_argument("--dry-run", action="store_true", help="Plan and print commands without executing.")
    args = parser.parse_args()

    config_path = Path(args.config).resolve() if args.config else _config_default()
    config = _load_config(config_path)

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
    )
    if not steps:
        raise ValueError("No steps were selected. Check stage toggles, --only, and --stage6-scenarios.")

    run_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    logs_dir = _reports_dir() / "run_logs" / run_stamp
    workdir = _analysis_root().parent

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
        "steps": [],
    }

    try:
        for step in steps:
            print(f"[{step.stage}] {step.name}")
            print("  " + " ".join(shlex.quote(part) for part in step.command))
            step_result = _run_step(step=step, workdir=workdir, logs_dir=logs_dir, dry_run=args.dry_run)
            manifest["steps"].append(step_result)
            if step_result["return_code"] != 0:
                raise RuntimeError(f"Step failed: {step.name} (return_code={step_result['return_code']})")
        manifest["status"] = "dry_run" if args.dry_run else "success"
    except Exception as exc:  # noqa: BLE001
        manifest["status"] = "failed"
        manifest["error"] = str(exc)
        raise
    finally:
        manifest["pipeline_finished_utc"] = _utc_now()
        manifest_out.parent.mkdir(parents=True, exist_ok=True)
        manifest_out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Run manifest: {manifest_out}")


if __name__ == "__main__":
    main()

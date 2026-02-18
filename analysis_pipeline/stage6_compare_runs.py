from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_out_json() -> Path:
    return _reports_dir() / "ml_compare_runs.json"


def _default_out_md() -> Path:
    return _reports_dir() / "ml_compare_runs.md"


def _resolve_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (Path.cwd() / direct).resolve()


def _load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _feature_selector_from_row(row: dict[str, Any]) -> str:
    return str(row.get("feature_selector", "none"))


def _pipeline_id_from_row(row: dict[str, Any]) -> str:
    model = str(row.get("model", ""))
    selector = _feature_selector_from_row(row)
    return str(row.get("pipeline_id", f"{model}+{selector}"))


def _scenario_name(payload: dict[str, Any], fallback: str) -> str:
    config = payload.get("config", {}) if isinstance(payload.get("config", {}), dict) else {}
    class_scenario = config.get("class_scenario", {}) if isinstance(config.get("class_scenario", {}), dict) else {}
    return str(class_scenario.get("name") or config.get("run_tag") or fallback)


def _best_by_track(payload: dict[str, Any], metric: str) -> dict[tuple[str, str], dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in payload.get("aggregates", []):
        dataset = str(row.get("dataset", ""))
        protocol = str(row.get("protocol", ""))
        if not dataset or not protocol:
            continue
        grouped[(dataset, protocol)].append(row)

    out: dict[tuple[str, str], dict[str, Any]] = {}
    for key, rows in grouped.items():
        ranked = sorted(
            rows,
            key=lambda x: (
                float(x.get(metric, 0.0)),
                float(x.get("macro_f1_mean", 0.0)),
                float(x.get("balanced_accuracy_mean", 0.0)),
            ),
            reverse=True,
        )
        if ranked:
            out[key] = ranked[0]
    return out


def _status(delta: float, tolerance: float) -> str:
    if delta > tolerance:
        return "BETTER_CANDIDATE"
    if delta < -tolerance:
        return "BETTER_BASELINE"
    return "SAME"


def _to_markdown_table(rows: list[dict[str, Any]]) -> str:
    headers = [
        "dataset",
        "protocol",
        "status",
        "baseline_score",
        "candidate_score",
        "delta",
        "baseline_pipeline",
        "candidate_pipeline",
    ]
    lines: list[str] = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["dataset"]),
                    str(row["protocol"]),
                    str(row["status"]),
                    f"{float(row['baseline_score']):.4f}" if row["baseline_score"] is not None else "n/a",
                    f"{float(row['candidate_score']):.4f}" if row["candidate_score"] is not None else "n/a",
                    f"{float(row['delta']):+.4f}" if row["delta"] is not None else "n/a",
                    str(row["baseline_pipeline"] or "n/a"),
                    str(row["candidate_pipeline"] or "n/a"),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two Stage 6 result JSON files and label each dataset/protocol track as "
            "BETTER_CANDIDATE, BETTER_BASELINE, or SAME."
        )
    )
    parser.add_argument("--baseline-results", required=True, help="Baseline Stage 6 results JSON.")
    parser.add_argument("--candidate-results", required=True, help="Candidate Stage 6 results JSON.")
    parser.add_argument(
        "--metric",
        choices=["balanced_accuracy_mean", "macro_f1_mean", "accuracy_mean", "weighted_f1_mean"],
        default="balanced_accuracy_mean",
        help="Metric used for best-pipeline selection and deltas.",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=1e-6,
        help="Absolute delta tolerance below which rows are tagged SAME.",
    )
    parser.add_argument("--out-json", default=None, help="Output JSON path.")
    parser.add_argument("--out-md", default=None, help="Output markdown path.")
    args = parser.parse_args()

    if args.tolerance < 0:
        raise ValueError("--tolerance must be >= 0")

    baseline_path = _resolve_path(args.baseline_results)
    candidate_path = _resolve_path(args.candidate_results)
    out_json = _resolve_path(args.out_json) if args.out_json else _default_out_json()
    out_md = _resolve_path(args.out_md) if args.out_md else _default_out_md()

    baseline_payload = _load_json(baseline_path)
    candidate_payload = _load_json(candidate_path)

    baseline_scenario = _scenario_name(baseline_payload, baseline_path.stem)
    candidate_scenario = _scenario_name(candidate_payload, candidate_path.stem)

    baseline_best = _best_by_track(baseline_payload, metric=args.metric)
    candidate_best = _best_by_track(candidate_payload, metric=args.metric)

    track_keys = sorted(set(baseline_best.keys()) | set(candidate_best.keys()))
    rows: list[dict[str, Any]] = []
    for dataset, protocol in track_keys:
        b_row = baseline_best.get((dataset, protocol))
        c_row = candidate_best.get((dataset, protocol))
        baseline_score = float(b_row.get(args.metric, 0.0)) if b_row else None
        candidate_score = float(c_row.get(args.metric, 0.0)) if c_row else None
        delta = None
        status = "MISSING_BOTH"
        if baseline_score is None and candidate_score is not None:
            status = "ONLY_CANDIDATE"
        elif baseline_score is not None and candidate_score is None:
            status = "ONLY_BASELINE"
        elif baseline_score is not None and candidate_score is not None:
            delta = candidate_score - baseline_score
            status = _status(delta, args.tolerance)

        rows.append(
            {
                "dataset": dataset,
                "protocol": protocol,
                "status": status,
                "baseline_score": baseline_score,
                "candidate_score": candidate_score,
                "delta": delta,
                "baseline_model": str(b_row.get("model", "")) if b_row else None,
                "baseline_feature_selector": _feature_selector_from_row(b_row) if b_row else None,
                "baseline_pipeline": _pipeline_id_from_row(b_row) if b_row else None,
                "candidate_model": str(c_row.get("model", "")) if c_row else None,
                "candidate_feature_selector": _feature_selector_from_row(c_row) if c_row else None,
                "candidate_pipeline": _pipeline_id_from_row(c_row) if c_row else None,
            }
        )

    rows = sorted(rows, key=lambda x: (x["dataset"], x["protocol"]))
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["status"]] += 1

    payload = {
        "baseline_results": str(baseline_path),
        "candidate_results": str(candidate_path),
        "baseline_scenario": baseline_scenario,
        "candidate_scenario": candidate_scenario,
        "metric": args.metric,
        "tolerance": args.tolerance,
        "counts": dict(sorted(counts.items())),
        "rows": rows,
    }
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    md_lines: list[str] = []
    md_lines.append("# Stage 6 Before/After Comparison")
    md_lines.append("")
    md_lines.append(f"- Baseline: `{baseline_path}` ({baseline_scenario})")
    md_lines.append(f"- Candidate: `{candidate_path}` ({candidate_scenario})")
    md_lines.append(f"- Metric: `{args.metric}`")
    md_lines.append(f"- Tolerance: `{args.tolerance}`")
    md_lines.append("")
    md_lines.append("## Status Counts")
    for key in sorted(counts.keys()):
        md_lines.append(f"- `{key}`: {counts[key]}")
    md_lines.append("")
    md_lines.append("## Track-Level Results")
    md_lines.append(_to_markdown_table(rows))
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print("Stage 6 comparison complete.")
    print(f"  Output JSON: {out_json}")
    print(f"  Output Markdown: {out_md}")
    print(f"  Compared tracks: {len(rows)}")


if __name__ == "__main__":
    main()

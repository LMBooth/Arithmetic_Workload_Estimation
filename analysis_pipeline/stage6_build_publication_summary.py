from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_out_md() -> Path:
    return _reports_dir() / "model_modality_output_summary.md"


def _default_out_dir() -> Path:
    return _reports_dir() / "tables" / "publication_summary"


def _resolve_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (Path.cwd() / direct).resolve()


def _load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _ensure_pipeline_cols(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "feature_selector" not in out.columns:
        out["feature_selector"] = "none"
    if "pipeline_id" not in out.columns:
        out["pipeline_id"] = out["model"].astype(str) + "+" + out["feature_selector"].astype(str)
    return out


def _fmt(value: Any, decimals: int = 4) -> str:
    if value is None:
        return "n/a"
    try:
        number = float(value)
    except Exception:  # noqa: BLE001
        return str(value)
    return f"{number:.{decimals}f}"


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except Exception:  # noqa: BLE001
        return str(path)


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
                cells.append(_fmt(val, decimals=decimals))
            else:
                cells.append(str(val))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def _build_track_best_table(best_df: pd.DataFrame) -> pd.DataFrame:
    if best_df.empty:
        return pd.DataFrame()
    work = best_df.copy()
    if "best_feature_selector" not in work.columns:
        work["best_feature_selector"] = "none"
    if "best_pipeline" not in work.columns:
        work["best_pipeline"] = work["best_model"].astype(str) + "+" + work["best_feature_selector"].astype(str)
    cols = [
        "dataset",
        "protocol",
        "best_model",
        "best_feature_selector",
        "best_pipeline",
        "balanced_accuracy_mean",
        "macro_f1_mean",
        "n_evaluations",
    ]
    keep = [c for c in cols if c in work.columns]
    out = work[keep].copy()
    return out.sort_values(["dataset", "protocol"]).reset_index(drop=True)


def _build_model_modality_table(agg_df: pd.DataFrame) -> pd.DataFrame:
    if agg_df.empty:
        return pd.DataFrame()
    work = _ensure_pipeline_cols(agg_df)
    rows: list[dict[str, Any]] = []
    for (dataset, model), group in work.groupby(["dataset", "model"], sort=True):
        ranked = group.sort_values(
            ["balanced_accuracy_mean", "macro_f1_mean"],
            ascending=[False, False],
        ).reset_index(drop=True)
        top = ranked.iloc[0]
        rows.append(
            {
                "dataset": str(dataset),
                "model": str(model),
                "n_protocols": int(group["protocol"].nunique()),
                "n_pipelines": int(group["pipeline_id"].nunique()),
                "mean_balanced_accuracy": float(group["balanced_accuracy_mean"].mean()),
                "max_balanced_accuracy": float(group["balanced_accuracy_mean"].max()),
                "mean_macro_f1": float(group["macro_f1_mean"].mean()),
                "top_pipeline": str(top["pipeline_id"]),
                "top_pipeline_selector": str(top.get("feature_selector", "none")),
                "top_pipeline_protocol": str(top["protocol"]),
            }
        )
    out = pd.DataFrame(rows)
    return out.sort_values(["dataset", "mean_balanced_accuracy"], ascending=[True, False]).reset_index(drop=True)


def _build_top_pipelines_table(agg_df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    if agg_df.empty:
        return pd.DataFrame()
    work = _ensure_pipeline_cols(agg_df)
    rows: list[dict[str, Any]] = []
    for (dataset, protocol), group in work.groupby(["dataset", "protocol"], sort=True):
        ranked = group.sort_values(
            ["balanced_accuracy_mean", "macro_f1_mean"],
            ascending=[False, False],
        ).head(top_n)
        for rank, (_, row) in enumerate(ranked.iterrows(), start=1):
            rows.append(
                {
                    "dataset": str(dataset),
                    "protocol": str(protocol),
                    "rank": rank,
                    "model": str(row["model"]),
                    "feature_selector": str(row.get("feature_selector", "none")),
                    "pipeline_id": str(row["pipeline_id"]),
                    "balanced_accuracy_mean": float(row["balanced_accuracy_mean"]),
                    "macro_f1_mean": float(row["macro_f1_mean"]),
                }
            )
    return pd.DataFrame(rows).sort_values(["dataset", "protocol", "rank"]).reset_index(drop=True)


def _build_protocol_summary(agg_df: pd.DataFrame) -> pd.DataFrame:
    if agg_df.empty:
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for (dataset, protocol), group in agg_df.groupby(["dataset", "protocol"], sort=True):
        rows.append(
            {
                "dataset": str(dataset),
                "protocol": str(protocol),
                "n_models": int(group["model"].nunique()),
                "n_pipelines": int(group["pipeline_id"].nunique()),
                "mean_balanced_accuracy": float(group["balanced_accuracy_mean"].mean()),
                "max_balanced_accuracy": float(group["balanced_accuracy_mean"].max()),
                "mean_macro_f1": float(group["macro_f1_mean"].mean()),
            }
        )
    return pd.DataFrame(rows).sort_values(["dataset", "protocol"]).reset_index(drop=True)


def _build_markdown(
    *,
    results_path: Path,
    compare_path: Path | None,
    config: dict[str, Any],
    counts: dict[str, Any],
    track_best: pd.DataFrame,
    protocol_summary: pd.DataFrame,
    model_modality: pd.DataFrame,
    top_pipelines: pd.DataFrame,
    compare_payload: dict[str, Any] | None,
    tables_dir: Path,
) -> str:
    lines: list[str] = []
    lines.append("# Model and Modality Classification Output Summary")
    lines.append("")
    lines.append("## Inputs")
    lines.append(f"- Results JSON: `{_display_path(results_path)}`")
    if compare_path is not None:
        lines.append(f"- Comparison JSON: `{_display_path(compare_path)}`")
    lines.append("")
    lines.append("## Run Snapshot")
    lines.append(f"- Scenario: `{config.get('class_scenario', {}).get('name', 'unknown')}`")
    lines.append(f"- Datasets: `{', '.join(config.get('datasets', []))}`")
    lines.append(f"- Protocols: `{', '.join(config.get('protocols', []))}`")
    lines.append(f"- Models: `{', '.join(config.get('models', []))}`")
    lines.append(f"- Feature selectors: `{', '.join(config.get('feature_selectors', ['none']))}`")
    lines.append(f"- Evaluations: `{counts.get('n_evaluations', 'n/a')}`")
    lines.append(f"- Aggregate rows: `{counts.get('n_aggregate_rows', 'n/a')}`")
    lines.append("")

    lines.append("## Best Pipeline by Modality and Protocol")
    lines.append(_to_markdown_table(track_best))

    lines.append("## Protocol-Level Summary by Modality")
    lines.append(_to_markdown_table(protocol_summary))

    lines.append("## Model Performance by Modality")
    lines.append(_to_markdown_table(model_modality))

    lines.append("## Top Pipelines per Modality and Protocol")
    lines.append(_to_markdown_table(top_pipelines))

    if compare_payload is not None:
        lines.append("## Before/After Comparison Snapshot")
        lines.append(f"- Metric: `{compare_payload.get('metric')}`")
        lines.append(f"- Status counts: `{compare_payload.get('counts', {})}`")
        compare_rows = pd.DataFrame(compare_payload.get("rows", []))
        if not compare_rows.empty:
            show_cols = [
                "dataset",
                "protocol",
                "status",
                "baseline_score",
                "candidate_score",
                "delta",
                "baseline_pipeline",
                "candidate_pipeline",
            ]
            have_cols = [c for c in show_cols if c in compare_rows.columns]
            lines.append(_to_markdown_table(compare_rows[have_cols]))

    lines.append("## Exported Tables")
    lines.append(f"- All pipelines: `{_display_path(tables_dir / 'all_pipeline_aggregates.csv')}`")
    lines.append(f"- Best by track: `{_display_path(tables_dir / 'best_pipeline_by_modality_protocol.csv')}`")
    lines.append(f"- Protocol summary: `{_display_path(tables_dir / 'protocol_summary_by_modality.csv')}`")
    lines.append(f"- Model-by-modality summary: `{_display_path(tables_dir / 'model_summary_by_modality.csv')}`")
    lines.append(f"- Top pipelines: `{_display_path(tables_dir / 'top_pipelines_by_track.csv')}`")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build publication-friendly output summary tables from Stage 6 results."
    )
    parser.add_argument("--results-json", required=True, help="Path to stage6 ml_results*.json")
    parser.add_argument(
        "--compare-json",
        default=None,
        help="Optional path to stage6_compare_runs output JSON for before/after context.",
    )
    parser.add_argument("--top-n", type=int, default=3, help="Top N pipelines per dataset+protocol in summary table.")
    parser.add_argument("--out-md", default=None, help="Output markdown summary path.")
    parser.add_argument("--tables-dir", default=None, help="Output directory for CSV tables.")
    args = parser.parse_args()

    if args.top_n < 1:
        raise ValueError("--top-n must be >= 1")

    results_path = _resolve_path(args.results_json)
    out_md = _resolve_path(args.out_md) if args.out_md else _default_out_md()
    tables_dir = _resolve_path(args.tables_dir) if args.tables_dir else _default_out_dir()
    compare_path = _resolve_path(args.compare_json) if args.compare_json else None

    payload = _load_json(results_path)
    compare_payload = _load_json(compare_path) if compare_path is not None else None

    config = payload.get("config", {})
    counts = payload.get("counts", {})

    agg_df = _ensure_pipeline_cols(pd.DataFrame(payload.get("aggregates", [])))
    best_df = pd.DataFrame(payload.get("best_models", []))

    track_best = _build_track_best_table(best_df)
    protocol_summary = _build_protocol_summary(agg_df)
    model_modality = _build_model_modality_table(agg_df)
    top_pipelines = _build_top_pipelines_table(agg_df, top_n=args.top_n)

    tables_dir.mkdir(parents=True, exist_ok=True)
    agg_df.to_csv(tables_dir / "all_pipeline_aggregates.csv", index=False)
    track_best.to_csv(tables_dir / "best_pipeline_by_modality_protocol.csv", index=False)
    protocol_summary.to_csv(tables_dir / "protocol_summary_by_modality.csv", index=False)
    model_modality.to_csv(tables_dir / "model_summary_by_modality.csv", index=False)
    top_pipelines.to_csv(tables_dir / "top_pipelines_by_track.csv", index=False)

    md_text = _build_markdown(
        results_path=results_path,
        compare_path=compare_path,
        config=config,
        counts=counts,
        track_best=track_best,
        protocol_summary=protocol_summary,
        model_modality=model_modality,
        top_pipelines=top_pipelines,
        compare_payload=compare_payload,
        tables_dir=tables_dir,
    )
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md_text, encoding="utf-8")

    print("Publication summary complete.")
    print(f"  Output markdown: {out_md}")
    print(f"  Tables dir: {tables_dir}")
    print(f"  Aggregate rows: {len(agg_df)}")


if __name__ == "__main__":
    main()

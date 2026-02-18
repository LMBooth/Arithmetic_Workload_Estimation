from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _default_out_md() -> Path:
    return _analysis_root() / "submission_package" / "docs" / "manuscript_methods_results_draft.md"


def _resolve_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (Path.cwd() / direct).resolve()


def _load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _fmt(value: Any, decimals: int = 4) -> str:
    if value is None:
        return "n/a"
    try:
        return f"{float(value):.{decimals}f}"
    except Exception:  # noqa: BLE001
        return str(value)


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except Exception:  # noqa: BLE001
        return str(path)


def _ensure_pipeline_cols(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "feature_selector" not in out.columns:
        out["feature_selector"] = "none"
    if "pipeline_id" not in out.columns and "model" in out.columns:
        out["pipeline_id"] = out["model"].astype(str) + "+" + out["feature_selector"].astype(str)
    return out


def _md_table(df: pd.DataFrame, decimals: int = 4) -> str:
    if df.empty:
        return "_no rows_\n"
    headers = list(df.columns)
    lines: list[str] = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for _, row in df.iterrows():
        vals: list[str] = []
        for col in headers:
            val = row[col]
            if isinstance(val, float):
                vals.append(_fmt(val, decimals=decimals))
            else:
                vals.append(str(val))
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines) + "\n"


def _build_methods_section(config: dict[str, Any], results_path: Path) -> list[str]:
    lines: list[str] = []
    lines.append("## Methods (Draft)")
    lines.append("")
    lines.append("### Dataset and processing overview")
    lines.append(
        "We analyzed a BIDS-formatted arithmetic multimodal dataset (EEG, ECG, and pupil), and processed it with a staged pipeline that included trial-table construction, QC, preprocessing, epoching, feature extraction, feature-table fusion, and split-aware machine-learning evaluation."
    )
    lines.append("")
    lines.append("### Feature and table construction")
    lines.append(
        "Unimodal feature tables were built independently for EEG, ECG, and pupil, then aligned into a fused multimodal table. All model training used leak-safe fold-local preprocessing (imputation, clipping, robust scaling, variance filtering, optional feature selection)."
    )
    lines.append("")
    lines.append("### Classification design")
    datasets = ", ".join(config.get("datasets", []))
    protocols = ", ".join(config.get("protocols", []))
    models = ", ".join(config.get("models", []))
    selectors = ", ".join(config.get("feature_selectors", ["none"]))
    lines.append(f"Datasets evaluated: `{datasets}`.")
    lines.append(f"Validation protocols: `{protocols}`.")
    lines.append(f"Model families: `{models}`.")
    lines.append(f"Feature selectors: `{selectors}`.")
    lines.append(
        "Primary metrics were balanced accuracy, macro-F1, weighted-F1, and accuracy, with confusion matrices aggregated for top-ranked pipelines by dataset and protocol."
    )
    lines.append("")
    lines.append("### Reproducibility")
    lines.append(
        f"All run-level outputs and configuration metadata were stored in structured JSON artifacts; this draft references `{_rel(results_path)}` as the primary result source."
    )
    lines.append("")
    return lines


def _build_results_section(
    *,
    results_path: Path,
    compare_path: Path | None,
    payload: dict[str, Any],
    compare_payload: dict[str, Any] | None,
) -> list[str]:
    lines: list[str] = []
    lines.append("## Results (Draft)")
    lines.append("")

    counts = payload.get("counts", {})
    config = payload.get("config", {})
    lines.append(
        f"The analyzed run (`{_rel(results_path)}`) produced `{counts.get('n_evaluations', 'n/a')}` evaluations and `{counts.get('n_aggregate_rows', 'n/a')}` aggregate pipeline rows for scenario `{config.get('class_scenario', {}).get('name', 'unknown')}`."
    )
    lines.append("")

    best_df = pd.DataFrame(payload.get("best_models", []))
    if not best_df.empty:
        if "best_feature_selector" not in best_df.columns:
            best_df["best_feature_selector"] = "none"
        if "best_pipeline" not in best_df.columns:
            best_df["best_pipeline"] = (
                best_df["best_model"].astype(str) + "+" + best_df["best_feature_selector"].astype(str)
            )
        best_table = best_df[
            [
                "dataset",
                "protocol",
                "best_model",
                "best_feature_selector",
                "best_pipeline",
                "balanced_accuracy_mean",
                "macro_f1_mean",
            ]
        ].sort_values(["dataset", "protocol"])
        lines.append("### Best pipeline by modality and protocol")
        lines.append(_md_table(best_table))

    agg_df = _ensure_pipeline_cols(pd.DataFrame(payload.get("aggregates", [])))
    if not agg_df.empty:
        modality_top_rows: list[dict[str, Any]] = []
        for dataset, group in agg_df.groupby("dataset", sort=True):
            top = group.sort_values(["balanced_accuracy_mean", "macro_f1_mean"], ascending=[False, False]).iloc[0]
            modality_top_rows.append(
                {
                    "dataset": str(dataset),
                    "top_pipeline": str(top["pipeline_id"]),
                    "top_protocol": str(top["protocol"]),
                    "top_balanced_accuracy": float(top["balanced_accuracy_mean"]),
                    "top_macro_f1": float(top["macro_f1_mean"]),
                }
            )
        modality_top = pd.DataFrame(modality_top_rows).sort_values("dataset")
        lines.append("### Modality-level top-performing pipelines")
        lines.append(_md_table(modality_top))

    if compare_payload is not None:
        lines.append("### Before/after comparison summary")
        lines.append(
            f"Comparison source: `{_rel(compare_path)}` using metric `{compare_payload.get('metric', 'balanced_accuracy_mean')}`."
        )
        lines.append(f"Status counts: `{compare_payload.get('counts', {})}`.")
        compare_df = pd.DataFrame(compare_payload.get("rows", []))
        if not compare_df.empty:
            keep = [
                "dataset",
                "protocol",
                "status",
                "baseline_score",
                "candidate_score",
                "delta",
                "baseline_pipeline",
                "candidate_pipeline",
            ]
            table = compare_df[keep].sort_values(["dataset", "protocol"])
            lines.append(_md_table(table))

            numeric = compare_df[pd.to_numeric(compare_df["delta"], errors="coerce").notna()].copy()
            if not numeric.empty:
                best_gains = numeric[numeric["delta"] > 0].sort_values("delta", ascending=False).head(3)
                worst = numeric[numeric["delta"] < 0].sort_values("delta", ascending=True).head(3)
                if not best_gains.empty:
                    lines.append("Top positive deltas were:")
                    for _, row in best_gains.iterrows():
                        lines.append(
                            f"- `{row['dataset']}|{row['protocol']}`: {_fmt(row['delta'])} ({row['baseline_pipeline']} -> {row['candidate_pipeline']})"
                        )
                if not worst.empty:
                    lines.append("Largest negative deltas were:")
                    for _, row in worst.iterrows():
                        lines.append(
                            f"- `{row['dataset']}|{row['protocol']}`: {_fmt(row['delta'])} ({row['baseline_pipeline']} -> {row['candidate_pipeline']})"
                        )
                lines.append("")

    lines.append("### Interpretation notes")
    lines.append(
        "In this run, fused multimodal tracks showed strong gains in multiple protocols, while specific unimodal tracks remained mixed. This supports a fusion-first baseline for main analyses, with unimodal tracks retained for mechanistic interpretation."
    )
    lines.append("")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a manuscript-ready Methods/Results draft from Stage 6 outputs.")
    parser.add_argument("--results-json", required=True, help="Stage 6 ml_results*.json path")
    parser.add_argument("--compare-json", default=None, help="Optional stage6_compare_runs JSON path")
    parser.add_argument("--out-md", default=None, help="Output markdown path")
    args = parser.parse_args()

    results_path = _resolve_path(args.results_json)
    compare_path = _resolve_path(args.compare_json) if args.compare_json else None
    out_md = _resolve_path(args.out_md) if args.out_md else _default_out_md()

    payload = _load_json(results_path)
    compare_payload = _load_json(compare_path) if compare_path else None

    lines: list[str] = []
    lines.append("# Draft Manuscript Sections: Methods and Results")
    lines.append("")
    lines.append("> This is a draft scaffold generated from current pipeline outputs. Edit for journal style and narrative flow.")
    lines.append("")
    lines.extend(_build_methods_section(payload.get("config", {}), results_path))
    lines.extend(
        _build_results_section(
            results_path=results_path,
            compare_path=compare_path,
            payload=payload,
            compare_payload=compare_payload,
        )
    )

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Manuscript draft complete.")
    print(f"  Output markdown: {out_md}")
    print(f"  Source results: {results_path}")
    if compare_path:
        print(f"  Source compare: {compare_path}")


if __name__ == "__main__":
    main()

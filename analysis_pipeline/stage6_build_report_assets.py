from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_out_dir() -> Path:
    return _reports_dir() / "figures" / "stage6_reports"


def _resolve_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()
    return (Path.cwd() / direct).resolve()


def _slug(text: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "_" for ch in str(text).strip())
    out = "_".join(part for part in out.split("_") if part)
    return out or "default"


def _load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


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


def _collect_paths_from_manifest(run_manifest: Path) -> tuple[list[Path], list[Path]]:
    payload = _load_json(run_manifest)
    steps = payload.get("steps", [])
    results: list[Path] = []
    confusions: list[Path] = []
    for step in steps:
        stage = str(step.get("stage", "")).strip()
        cwd_text = str(step.get("cwd", "")).strip()
        if not cwd_text:
            continue
        cwd = Path(cwd_text)
        outputs = step.get("outputs", []) or []
        for out in outputs:
            out_path = Path(str(out))
            if not out_path.is_absolute():
                out_path = (cwd / out_path).resolve()
            if stage == "stage6" and out_path.name.startswith("ml_results") and out_path.suffix == ".json":
                results.append(out_path)
            if stage == "stage6_confusions" and out_path.name.startswith("confusion_highlights") and out_path.suffix == ".json":
                confusions.append(out_path)
    return _dedupe_keep_order(results), _dedupe_keep_order(confusions)


def _collect_paths_by_glob(glob_pattern: str) -> list[Path]:
    pattern_path = _resolve_path(glob_pattern)
    parent = pattern_path.parent
    if not parent.exists():
        return []
    return _dedupe_keep_order(sorted(parent.glob(pattern_path.name)))


def _to_markdown(df: pd.DataFrame, float_decimals: int = 4) -> str:
    if df.empty:
        return "_no rows_\n"
    headers = list(df.columns)
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for _, row in df.iterrows():
        cells: list[str] = []
        for col in headers:
            value = row[col]
            if isinstance(value, float) and math.isfinite(value):
                cells.append(f"{value:.{float_decimals}f}")
            else:
                cells.append(str(value))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def _build_result_frames(
    result_paths: list[Path],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, dict[str, Any]], dict[str, str]]:
    best_rows: list[dict[str, Any]] = []
    aggregate_rows: list[dict[str, Any]] = []
    class_dist_rows: list[dict[str, Any]] = []
    scenario_meta: dict[str, dict[str, Any]] = {}
    path_to_scenario: dict[str, str] = {}

    for scenario_rank, path in enumerate(result_paths):
        payload = _load_json(path)
        config = payload.get("config", {})
        class_scenario = config.get("class_scenario", {})
        scenario = str(class_scenario.get("name") or config.get("run_tag") or path.stem).strip()
        final_labels = [str(x) for x in class_scenario.get("final_labels", [])]
        label_rank_map = {label: idx for idx, label in enumerate(final_labels)}
        class_count = len(final_labels)
        scenario_meta[scenario] = {
            "scenario": scenario,
            "scenario_rank": scenario_rank,
            "class_count": class_count,
            "final_labels": final_labels,
            "results_path": str(path),
        }
        path_to_scenario[str(path.resolve())] = scenario

        for row in payload.get("best_models", []):
            best_model = str(row.get("best_model", ""))
            best_selector = str(row.get("best_feature_selector", "none"))
            best_pipeline = str(row.get("best_pipeline", f"{best_model}+{best_selector}"))
            best_rows.append(
                {
                    "scenario": scenario,
                    "scenario_rank": scenario_rank,
                    "class_count": class_count,
                    "dataset": str(row.get("dataset", "")),
                    "protocol": str(row.get("protocol", "")),
                    "best_model": best_model,
                    "best_feature_selector": best_selector,
                    "best_pipeline": best_pipeline,
                    "balanced_accuracy_mean": float(row.get("balanced_accuracy_mean", 0.0)),
                    "macro_f1_mean": float(row.get("macro_f1_mean", 0.0)),
                    "n_evaluations": int(row.get("n_evaluations", 0)),
                    "results_json": str(path),
                }
            )

        for row in payload.get("aggregates", []):
            model = str(row.get("model", ""))
            feature_selector = str(row.get("feature_selector", "none"))
            pipeline_id = str(row.get("pipeline_id", f"{model}+{feature_selector}"))
            aggregate_rows.append(
                {
                    "scenario": scenario,
                    "scenario_rank": scenario_rank,
                    "class_count": class_count,
                    "dataset": str(row.get("dataset", "")),
                    "protocol": str(row.get("protocol", "")),
                    "model": model,
                    "feature_selector": feature_selector,
                    "pipeline_id": pipeline_id,
                    "n_evaluations": int(row.get("n_evaluations", 0)),
                    "accuracy_mean": float(row.get("accuracy_mean", 0.0)),
                    "accuracy_std": float(row.get("accuracy_std", 0.0)),
                    "balanced_accuracy_mean": float(row.get("balanced_accuracy_mean", 0.0)),
                    "balanced_accuracy_std": float(row.get("balanced_accuracy_std", 0.0)),
                    "macro_f1_mean": float(row.get("macro_f1_mean", 0.0)),
                    "macro_f1_std": float(row.get("macro_f1_std", 0.0)),
                    "weighted_f1_mean": float(row.get("weighted_f1_mean", 0.0)),
                    "weighted_f1_std": float(row.get("weighted_f1_std", 0.0)),
                    "results_json": str(path),
                }
            )

        for ds in payload.get("dataset_stats", []):
            dataset = str(ds.get("dataset", ""))
            class_counts = ds.get("class_counts", {}) or {}
            for fallback_rank, (label, count) in enumerate(class_counts.items()):
                label_text = str(label)
                class_dist_rows.append(
                    {
                        "scenario": scenario,
                        "scenario_rank": scenario_rank,
                        "class_count": class_count,
                        "dataset": dataset,
                        "label": label_text,
                        "label_rank": int(label_rank_map.get(label_text, len(label_rank_map) + fallback_rank)),
                        "count": int(count),
                        "results_json": str(path),
                    }
                )

    return (
        pd.DataFrame(best_rows),
        pd.DataFrame(aggregate_rows),
        pd.DataFrame(class_dist_rows),
        scenario_meta,
        path_to_scenario,
    )


def _select_dataset(df: pd.DataFrame, dataset_preference: str | None) -> pd.DataFrame:
    if df.empty:
        return df
    if dataset_preference:
        want = str(dataset_preference).strip()
        filtered = df[df["dataset"] == want]
        if not filtered.empty:
            return filtered.copy()
    if "fused" in set(df["dataset"].astype(str).tolist()):
        return df[df["dataset"] == "fused"].copy()
    return df.copy()


def _scenario_labels(df: pd.DataFrame) -> dict[str, str]:
    labels: dict[str, str] = {}
    for _, row in df.drop_duplicates(subset=["scenario"]).iterrows():
        labels[str(row["scenario"])] = f"{row['scenario']}\n({int(row['class_count'])} cls)"
    return labels


def _ordered_scenarios(df: pd.DataFrame, scenario_order_arg: list[str] | None) -> list[str]:
    if df.empty:
        return []
    existing = df.drop_duplicates(subset=["scenario"])[["scenario", "scenario_rank"]]
    by_rank = [str(x) for x in existing.sort_values("scenario_rank")["scenario"].tolist()]
    if not scenario_order_arg:
        return by_rank
    requested = [str(x) for x in scenario_order_arg]
    picked = [x for x in requested if x in set(by_rank)]
    for name in by_rank:
        if name not in picked:
            picked.append(name)
    return picked


def _plot_grouped_metric(
    best_df: pd.DataFrame,
    scenario_order: list[str],
    metric_col: str,
    title: str,
    out_path: Path,
) -> None:
    if best_df.empty or not scenario_order:
        return
    protocols = ["pooled_stratified", "group_holdout", "loso", "within_participant"]
    protocols = [p for p in protocols if p in set(best_df["protocol"].tolist())]
    if not protocols:
        protocols = sorted(set(best_df["protocol"].tolist()))
    if not protocols:
        return

    label_map = _scenario_labels(best_df)
    grouped = (
        best_df.groupby(["scenario", "protocol"], as_index=False)[metric_col]
        .mean()
        .sort_values(["scenario", "protocol"])
    )
    x = np.arange(len(scenario_order))
    width = 0.8 / max(len(protocols), 1)

    fig, ax = plt.subplots(figsize=(max(10.0, len(scenario_order) * 2.2), 5.5))
    for idx, protocol in enumerate(protocols):
        vals = []
        for scenario in scenario_order:
            match = grouped[(grouped["scenario"] == scenario) & (grouped["protocol"] == protocol)]
            vals.append(float(match[metric_col].iloc[0]) if not match.empty else 0.0)
        ax.bar(x + (idx - (len(protocols) - 1) / 2.0) * width, vals, width=width, label=protocol)

    ax.set_ylabel(metric_col)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels([label_map.get(s, s) for s in scenario_order], rotation=0)
    ax.set_ylim(0.0, max(1.0, float(grouped[metric_col].max()) * 1.15))
    ax.legend(loc="upper left")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)


def _plot_metric_heatmap(
    best_df: pd.DataFrame,
    scenario_order: list[str],
    metric_col: str,
    title: str,
    out_path: Path,
) -> None:
    if best_df.empty or not scenario_order:
        return
    protocols = ["pooled_stratified", "group_holdout", "loso", "within_participant"]
    protocols = [p for p in protocols if p in set(best_df["protocol"].tolist())]
    if not protocols:
        protocols = sorted(set(best_df["protocol"].tolist()))
    if not protocols:
        return

    grouped = best_df.groupby(["scenario", "protocol"], as_index=False)[metric_col].mean()
    matrix = np.zeros((len(scenario_order), len(protocols)), dtype=np.float64)
    matrix[:] = np.nan
    for i, scenario in enumerate(scenario_order):
        for j, protocol in enumerate(protocols):
            match = grouped[(grouped["scenario"] == scenario) & (grouped["protocol"] == protocol)]
            if not match.empty:
                matrix[i, j] = float(match[metric_col].iloc[0])

    label_map = _scenario_labels(best_df)
    fig, ax = plt.subplots(figsize=(max(8.0, len(protocols) * 2.0), max(4.0, len(scenario_order) * 0.8)))
    im = ax.imshow(matrix, cmap="viridis", vmin=0.0, vmax=np.nanmax(matrix) if np.isfinite(np.nanmax(matrix)) else 1.0)
    ax.set_xticks(np.arange(len(protocols)))
    ax.set_xticklabels(protocols)
    ax.set_yticks(np.arange(len(scenario_order)))
    ax.set_yticklabels([label_map.get(s, s) for s in scenario_order])
    ax.set_title(title)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            val = matrix[i, j]
            text = "n/a" if not math.isfinite(val) else f"{val:.3f}"
            ax.text(j, i, text, ha="center", va="center", color="white", fontsize=8)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(metric_col)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)


def _plot_model_wins(
    best_df: pd.DataFrame,
    scenario_order: list[str],
    out_path: Path,
    winner_col: str,
    title: str,
) -> None:
    if best_df.empty or not scenario_order:
        return
    if winner_col not in best_df.columns:
        return
    wins = best_df.groupby(["scenario", winner_col], as_index=False).size()
    pivot = wins.pivot(index="scenario", columns=winner_col, values="size").fillna(0.0)
    pivot = pivot.reindex(index=scenario_order)
    if pivot.empty:
        return

    fig, ax = plt.subplots(figsize=(max(10.0, len(scenario_order) * 2.0), 5.5))
    bottom = np.zeros(len(pivot), dtype=np.float64)
    x = np.arange(len(pivot))
    for model in sorted(pivot.columns):
        vals = pivot[model].to_numpy(dtype=np.float64)
        ax.bar(x, vals, bottom=bottom, label=model)
        bottom += vals

    label_map = _scenario_labels(best_df)
    ax.set_xticks(x)
    ax.set_xticklabels([label_map.get(s, s) for s in pivot.index.tolist()], rotation=0)
    ax.set_ylabel("count of wins")
    ax.set_title(title)
    ax.legend(loc="upper left")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)


def _build_confusion_recall_frame(
    confusion_paths: list[Path],
    path_to_scenario: dict[str, str],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for path in confusion_paths:
        payload = _load_json(path)
        source_results = str(payload.get("source_results_json", ""))
        scenario = path_to_scenario.get(str(Path(source_results).resolve()), Path(path).stem.replace("confusion_highlights_", ""))
        for highlight in payload.get("highlights", []):
            labels = [str(x) for x in highlight.get("labels", [])]
            recalls = [float(x) for x in highlight.get("class_recall", [])]
            supports = [int(x) for x in highlight.get("class_support", [])]
            model = str(highlight.get("model", ""))
            feature_selector = str(highlight.get("feature_selector", "none"))
            pipeline_id = str(highlight.get("pipeline_id", f"{model}+{feature_selector}"))
            for label_rank, (label, recall, support) in enumerate(zip(labels, recalls, supports)):
                rows.append(
                    {
                        "scenario": scenario,
                        "dataset": str(highlight.get("dataset", "")),
                        "protocol": str(highlight.get("protocol", "")),
                        "model": model,
                        "feature_selector": feature_selector,
                        "pipeline_id": pipeline_id,
                        "label": label,
                        "label_rank": int(label_rank),
                        "recall": recall,
                        "support": support,
                        "aggregate_metric": float(highlight.get("aggregate_metric", 0.0)),
                        "confusion_json": str(path),
                    }
                )
    return pd.DataFrame(rows)


def _plot_confusion_panels(
    confusion_paths: list[Path],
    path_to_scenario: dict[str, str],
    out_dir: Path,
    dataset_preference: str | None,
) -> list[Path]:
    outputs: list[Path] = []
    for path in confusion_paths:
        payload = _load_json(path)
        source_results = str(payload.get("source_results_json", ""))
        scenario = path_to_scenario.get(str(Path(source_results).resolve()), Path(path).stem.replace("confusion_highlights_", ""))
        highlights = payload.get("highlights", [])
        if dataset_preference:
            filtered = [h for h in highlights if str(h.get("dataset", "")) == dataset_preference]
            highlights = filtered if filtered else highlights
        if not highlights:
            continue
        by_protocol = {str(h.get("protocol", "")): h for h in highlights}
        protocol_order = ["pooled_stratified", "group_holdout", "loso", "within_participant"]
        ordered = [by_protocol[p] for p in protocol_order if p in by_protocol] + [
            h for h in highlights if str(h.get("protocol", "")) not in protocol_order
        ]
        n = len(ordered)
        fig, axes = plt.subplots(
            1,
            n,
            figsize=(max(4.5 * n, 7.0), 4.6),
            squeeze=False,
            constrained_layout=True,
        )
        axes_flat = axes[0]
        for idx, highlight in enumerate(ordered):
            ax = axes_flat[idx]
            matrix = np.asarray(highlight.get("confusion_row_normalized", []), dtype=np.float64)
            labels = [str(x) for x in highlight.get("labels", [])]
            im = ax.imshow(matrix, cmap="Blues", vmin=0.0, vmax=1.0)
            ax.set_xticks(np.arange(len(labels)))
            ax.set_yticks(np.arange(len(labels)))
            ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=8)
            ax.set_yticklabels(labels, fontsize=8)
            ax.set_xlabel("predicted")
            if idx == 0:
                ax.set_ylabel("true")
            model = str(highlight.get("model", ""))
            feature_selector = str(highlight.get("feature_selector", "none"))
            pipeline_id = str(highlight.get("pipeline_id", f"{model}+{feature_selector}"))
            title = (
                f"{highlight.get('protocol', '')}\n"
                f"model={model} selector={feature_selector}\n"
                f"pipeline={pipeline_id}\n"
                f"metric={float(highlight.get('aggregate_metric', 0.0)):.3f}"
            )
            ax.set_title(title, fontsize=9)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    ax.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center", color="black", fontsize=7)

        cbar = fig.colorbar(im, ax=axes_flat.tolist(), fraction=0.02, pad=0.02)
        cbar.set_label("row-normalized proportion")
        dataset_label = dataset_preference or "all"
        fig.suptitle(f"Confusion Highlights: {scenario} ({dataset_label})", fontsize=12)
        out_path = out_dir / f"confusion_panel_{_slug(scenario)}.png"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, dpi=180)
        plt.close(fig)
        outputs.append(out_path)
    return outputs


def _build_pipeline_ranking_table(agg_df: pd.DataFrame) -> pd.DataFrame:
    if agg_df.empty:
        return pd.DataFrame()
    work = agg_df.copy()
    if "feature_selector" not in work.columns:
        work["feature_selector"] = "none"
    if "pipeline_id" not in work.columns:
        work["pipeline_id"] = work["model"].astype(str) + "+" + work["feature_selector"].astype(str)
    if "balanced_accuracy_std" not in work.columns:
        work["balanced_accuracy_std"] = 0.0
    rows: list[dict[str, Any]] = []
    group_cols = ["scenario", "dataset", "protocol"]
    for _, group in work.groupby(group_cols, sort=False):
        ranked = group.sort_values(
            ["balanced_accuracy_mean", "macro_f1_mean", "balanced_accuracy_std"],
            ascending=[False, False, True],
        ).reset_index(drop=True)
        if ranked.empty:
            continue
        best_score = float(ranked.loc[0, "balanced_accuracy_mean"])
        for rank, (_, row) in enumerate(ranked.iterrows(), start=1):
            score = float(row["balanced_accuracy_mean"])
            gap = max(0.0, best_score - score)
            rows.append(
                {
                    "scenario": str(row["scenario"]),
                    "scenario_rank": int(row["scenario_rank"]),
                    "dataset": str(row["dataset"]),
                    "protocol": str(row["protocol"]),
                    "rank_in_track": rank,
                    "status": "BEST" if rank == 1 else f"WORSE_BY_{gap:.4f}",
                    "model": str(row["model"]),
                    "feature_selector": str(row["feature_selector"]),
                    "pipeline_id": str(row["pipeline_id"]),
                    "balanced_accuracy_mean": score,
                    "macro_f1_mean": float(row["macro_f1_mean"]),
                    "n_evaluations": int(row["n_evaluations"]),
                }
            )
    return pd.DataFrame(rows)


def _write_report_bundle(
    *,
    out_dir: Path,
    best_df: pd.DataFrame,
    agg_df: pd.DataFrame,
    class_df: pd.DataFrame,
    confusion_paths: list[Path],
    path_to_scenario: dict[str, str],
    dataset_for_plots: str | None,
    scenario_order_arg: list[str] | None,
) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    best_plot_df = _select_dataset(best_df, dataset_for_plots)
    scenario_order = _ordered_scenarios(best_plot_df if not best_plot_df.empty else best_df, scenario_order_arg)

    best_csv = out_dir / "table_best_models_by_scenario_protocol.csv"
    best_md = out_dir / "table_best_models_by_scenario_protocol.md"
    agg_csv = out_dir / "table_all_model_aggregates.csv"
    agg_md = out_dir / "table_all_model_aggregates.md"
    class_csv = out_dir / "table_class_distribution.csv"
    class_md = out_dir / "table_class_distribution.md"
    ranking_csv = out_dir / "table_pipeline_rankings.csv"
    ranking_md = out_dir / "table_pipeline_rankings.md"
    recall_csv = out_dir / "table_confusion_class_recall.csv"
    recall_md = out_dir / "table_confusion_class_recall.md"

    if not best_df.empty:
        best_table = best_df.sort_values(["scenario_rank", "dataset", "protocol"]).reset_index(drop=True)
        best_table.to_csv(best_csv, index=False)
        best_md.write_text(_to_markdown(best_table), encoding="utf-8")
    if not agg_df.empty:
        agg_table = agg_df.sort_values(
            ["scenario_rank", "dataset", "protocol", "model", "feature_selector"],
        ).reset_index(drop=True)
        agg_table.to_csv(agg_csv, index=False)
        agg_md.write_text(_to_markdown(agg_table), encoding="utf-8")
    ranking_df = _build_pipeline_ranking_table(agg_df)
    if not ranking_df.empty:
        ranking_df = ranking_df.sort_values(
            ["scenario_rank", "dataset", "protocol", "rank_in_track"],
        ).reset_index(drop=True)
        ranking_df.to_csv(ranking_csv, index=False)
        ranking_md.write_text(_to_markdown(ranking_df), encoding="utf-8")
    if not class_df.empty:
        class_sort_cols = ["scenario_rank", "dataset"]
        if "label_rank" in class_df.columns:
            class_sort_cols.append("label_rank")
        class_sort_cols.append("label")
        class_table = class_df.sort_values(class_sort_cols, kind="stable").reset_index(drop=True)
        class_table_out = class_table.drop(columns=["label_rank"], errors="ignore")
        class_table_out.to_csv(class_csv, index=False)
        class_md.write_text(_to_markdown(class_table_out, float_decimals=0), encoding="utf-8")

    _plot_grouped_metric(
        best_df=best_plot_df,
        scenario_order=scenario_order,
        metric_col="balanced_accuracy_mean",
        title=f"Best Balanced Accuracy by Scenario and Protocol ({dataset_for_plots or 'all'})",
        out_path=out_dir / "plot_best_balanced_accuracy.png",
    )
    _plot_grouped_metric(
        best_df=best_plot_df,
        scenario_order=scenario_order,
        metric_col="macro_f1_mean",
        title=f"Best Macro-F1 by Scenario and Protocol ({dataset_for_plots or 'all'})",
        out_path=out_dir / "plot_best_macro_f1.png",
    )
    _plot_metric_heatmap(
        best_df=best_plot_df,
        scenario_order=scenario_order,
        metric_col="balanced_accuracy_mean",
        title=f"Balanced Accuracy Heatmap ({dataset_for_plots or 'all'})",
        out_path=out_dir / "plot_balanced_accuracy_heatmap.png",
    )
    _plot_model_wins(
        best_df=best_plot_df,
        scenario_order=scenario_order,
        out_path=out_dir / "plot_model_wins.png",
        winner_col="best_model",
        title="Best-Model Wins Across Protocols",
    )
    _plot_model_wins(
        best_df=best_plot_df,
        scenario_order=scenario_order,
        out_path=out_dir / "plot_pipeline_wins.png",
        winner_col="best_pipeline",
        title="Best-Pipeline Wins Across Protocols",
    )

    confusion_panel_outputs: list[Path] = []
    recall_df = pd.DataFrame()
    if confusion_paths:
        confusion_panel_outputs = _plot_confusion_panels(
            confusion_paths=confusion_paths,
            path_to_scenario=path_to_scenario,
            out_dir=out_dir,
            dataset_preference=dataset_for_plots,
        )
        recall_df = _build_confusion_recall_frame(confusion_paths=confusion_paths, path_to_scenario=path_to_scenario)
        if dataset_for_plots:
            recall_df = recall_df[recall_df["dataset"] == dataset_for_plots].reset_index(drop=True)
        if not recall_df.empty:
            recall_sort_cols = ["scenario", "dataset", "protocol", "model", "feature_selector"]
            if "label_rank" in recall_df.columns:
                recall_sort_cols.append("label_rank")
            recall_sort_cols.append("label")
            recall_df = recall_df.sort_values(recall_sort_cols, kind="stable").reset_index(drop=True)
            recall_out = recall_df.drop(columns=["label_rank"], errors="ignore")
            recall_out.to_csv(recall_csv, index=False)
            recall_md.write_text(_to_markdown(recall_out), encoding="utf-8")

    return {
        "out_dir": str(out_dir),
        "dataset_for_plots": dataset_for_plots,
        "scenario_order": scenario_order,
        "outputs": {
            "tables": {
                "best_models_csv": str(best_csv),
                "best_models_md": str(best_md),
                "all_aggregates_csv": str(agg_csv),
                "all_aggregates_md": str(agg_md),
                "class_distribution_csv": str(class_csv),
                "class_distribution_md": str(class_md),
                "pipeline_rankings_csv": str(ranking_csv),
                "pipeline_rankings_md": str(ranking_md),
                "confusion_class_recall_csv": str(recall_csv),
                "confusion_class_recall_md": str(recall_md),
            },
            "plots": {
                "best_balanced_accuracy": str(out_dir / "plot_best_balanced_accuracy.png"),
                "best_macro_f1": str(out_dir / "plot_best_macro_f1.png"),
                "balanced_accuracy_heatmap": str(out_dir / "plot_balanced_accuracy_heatmap.png"),
                "model_wins": str(out_dir / "plot_model_wins.png"),
                "pipeline_wins": str(out_dir / "plot_pipeline_wins.png"),
                "confusion_panels": [str(p) for p in confusion_panel_outputs],
            },
        },
        "counts": {
            "n_best_rows": int(best_df.shape[0]),
            "n_aggregate_rows": int(agg_df.shape[0]),
            "n_ranking_rows": int(ranking_df.shape[0]) if not ranking_df.empty else 0,
            "n_recall_rows": int(recall_df.shape[0]) if not recall_df.empty else 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build tables and plots from Stage 6 ml_results/confusion outputs. "
            "Works directly from a run manifest or from file globs."
        )
    )
    parser.add_argument("--run-manifest", default=None, help="Optional run_manifest JSON to collect Stage 6 outputs.")
    parser.add_argument(
        "--results-json-glob",
        default="analysis_pipeline/reports/ml_results_*.json",
        help="Glob fallback for Stage 6 result JSON files.",
    )
    parser.add_argument(
        "--confusion-json-glob",
        default="analysis_pipeline/reports/confusion_highlights_*.json",
        help="Glob fallback for confusion highlight JSON files.",
    )
    parser.add_argument("--dataset-for-plots", default="fused", help="Dataset to prioritize in plots (default: fused).")
    parser.add_argument(
        "--dataset-reports",
        nargs="*",
        default=["eeg", "ecg", "pupil", "fused"],
        help="Per-dataset report bundles to generate (default: eeg ecg pupil fused).",
    )
    parser.add_argument(
        "--skip-overall-report",
        action="store_true",
        help="Skip writing the top-level aggregate report bundle.",
    )
    parser.add_argument("--scenario-order", nargs="*", default=None, help="Optional explicit scenario order.")
    parser.add_argument("--out-dir", default=None, help="Output directory for tables and plots.")
    args = parser.parse_args()

    out_dir = _resolve_path(args.out_dir) if args.out_dir else _default_out_dir()
    out_dir.mkdir(parents=True, exist_ok=True)

    result_paths: list[Path] = []
    confusion_paths: list[Path] = []

    if args.run_manifest:
        run_manifest = _resolve_path(args.run_manifest)
        result_paths, confusion_paths = _collect_paths_from_manifest(run_manifest)
    if not result_paths:
        result_paths = _collect_paths_by_glob(args.results_json_glob)
    if not confusion_paths:
        confusion_paths = _collect_paths_by_glob(args.confusion_json_glob)

    if not result_paths:
        raise ValueError("No Stage 6 result JSON files found.")

    best_df, agg_df, class_df, scenario_meta, path_to_scenario = _build_result_frames(result_paths)
    available_datasets = sorted(set(best_df.get("dataset", pd.Series(dtype=str)).astype(str).tolist()))
    requested_datasets = [str(x).strip() for x in (args.dataset_reports or []) if str(x).strip()]
    requested_datasets = list(dict.fromkeys(requested_datasets))

    overall_bundle = None
    if not args.skip_overall_report:
        overall_bundle = _write_report_bundle(
            out_dir=out_dir,
            best_df=best_df,
            agg_df=agg_df,
            class_df=class_df,
            confusion_paths=confusion_paths,
            path_to_scenario=path_to_scenario,
            dataset_for_plots=args.dataset_for_plots,
            scenario_order_arg=args.scenario_order,
        )

    per_dataset_bundles: dict[str, dict[str, Any]] = {}
    skipped_datasets: list[str] = []
    for dataset_name in requested_datasets:
        if dataset_name not in available_datasets:
            skipped_datasets.append(dataset_name)
            continue
        ds_best = best_df[best_df["dataset"] == dataset_name].reset_index(drop=True)
        ds_agg = agg_df[agg_df["dataset"] == dataset_name].reset_index(drop=True)
        ds_class = class_df[class_df["dataset"] == dataset_name].reset_index(drop=True)
        bundle = _write_report_bundle(
            out_dir=out_dir / f"dataset_{_slug(dataset_name)}",
            best_df=ds_best,
            agg_df=ds_agg,
            class_df=ds_class,
            confusion_paths=confusion_paths,
            path_to_scenario=path_to_scenario,
            dataset_for_plots=dataset_name,
            scenario_order_arg=args.scenario_order,
        )
        per_dataset_bundles[dataset_name] = bundle

    manifest = {
        "generated_utc": pd.Timestamp.utcnow().isoformat(),
        "out_dir": str(out_dir),
        "inputs": {
            "run_manifest": str(_resolve_path(args.run_manifest)) if args.run_manifest else None,
            "result_jsons": [str(p) for p in result_paths],
            "confusion_jsons": [str(p) for p in confusion_paths],
            "dataset_for_plots": args.dataset_for_plots,
            "dataset_reports_requested": requested_datasets,
            "dataset_reports_skipped": skipped_datasets,
            "scenario_order": args.scenario_order or [],
        },
        "available_datasets": available_datasets,
        "scenario_meta": scenario_meta,
        "outputs": {
            "overall": overall_bundle,
            "per_dataset": per_dataset_bundles,
        },
        "counts": {
            "n_result_files": len(result_paths),
            "n_confusion_files": len(confusion_paths),
            "n_best_rows": int(best_df.shape[0]),
            "n_aggregate_rows": int(agg_df.shape[0]),
            "n_dataset_reports_written": len(per_dataset_bundles),
        },
    }
    (out_dir / "report_assets_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print("Stage 6 report assets complete.")
    print(f"  Output dir: {out_dir}")
    print(f"  Result files: {len(result_paths)}")
    print(f"  Confusion files: {len(confusion_paths)}")
    print(f"  Best rows: {best_df.shape[0]}")
    print(f"  Aggregate rows: {agg_df.shape[0]}")
    print(f"  Dataset bundles written: {len(per_dataset_bundles)}")


if __name__ == "__main__":
    main()

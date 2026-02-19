from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_out_json() -> Path:
    return _reports_dir() / "confusion_highlights.json"


def _default_out_md() -> Path:
    return _reports_dir() / "confusion_highlights.md"


def _default_out_png_dir() -> Path:
    return _reports_dir() / "confusion_pngs"


def _slug(text: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "_" for ch in str(text).strip())
    out = "_".join(part for part in out.split("_") if part)
    return out or "item"


def _resolve_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute():
        return direct.resolve()

    return (Path.cwd() / direct).resolve()


def _load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _passes_filter(item: dict[str, Any], key: str, allowed: set[str] | None) -> bool:
    if not allowed:
        return True
    return str(item.get(key, "")) in allowed


def _feature_selector_from_row(row: dict[str, Any]) -> str:
    return str(row.get("feature_selector", "none"))


def _pipeline_id_from_row(row: dict[str, Any]) -> str:
    model = str(row.get("model", ""))
    feature_selector = _feature_selector_from_row(row)
    return str(row.get("pipeline_id", f"{model}+{feature_selector}"))


def _label_sort_key(label: str, fallback_order: dict[str, int]) -> tuple[float, int]:
    text = str(label).strip()
    lower = text.lower()
    if lower.startswith("baseline") or lower in {"baseline", "rest", "resting"}:
        return 10_000.0, fallback_order.get(text, 10_000)
    if "-" in text:
        left = text.split("-", 1)[0].strip()
        try:
            return float(left), fallback_order.get(text, 10_000)
        except ValueError:
            pass
    digits = []
    token = ""
    for ch in text:
        if ch.isdigit() or ch == ".":
            token += ch
        else:
            if token:
                digits.append(token)
                token = ""
    if token:
        digits.append(token)
    for dig in digits:
        try:
            return float(dig), fallback_order.get(text, 10_000)
        except ValueError:
            continue
    if "low" in lower:
        return 1000.0, fallback_order.get(text, 10_000)
    if "mid" in lower:
        return 2000.0, fallback_order.get(text, 10_000)
    if "high" in lower:
        return 3000.0, fallback_order.get(text, 10_000)
    return 9000.0, fallback_order.get(text, 10_000)


def _is_baseline_label(label: str) -> bool:
    lower = str(label).strip().lower()
    return lower.startswith("baseline") or lower in {"baseline", "rest", "resting"}


def _reorder_labels(labels: list[str], strategy: str) -> tuple[list[str], list[int]]:
    ordered = [str(x) for x in labels]
    if strategy == "as_is" or len(ordered) < 2:
        return ordered, list(range(len(ordered)))

    if strategy == "baseline_first":
        fallback = {label: idx for idx, label in enumerate(ordered)}
        reordered = sorted(ordered, key=lambda x: (0 if _is_baseline_label(x) else 1, _label_sort_key(x, fallback)))
        index_map = [ordered.index(label) for label in reordered]
        return reordered, index_map

    baseline_candidates = [label for label in ordered if _is_baseline_label(label)]
    if not baseline_candidates:
        return ordered, list(range(len(ordered)))
    baseline = baseline_candidates[0]
    non_baseline = [label for label in ordered if label != baseline]
    if not non_baseline:
        return ordered, list(range(len(ordered)))
    fallback = {label: idx for idx, label in enumerate(non_baseline)}
    easiest = min(non_baseline, key=lambda x: _label_sort_key(x, fallback))
    insert_idx = non_baseline.index(easiest) + 1
    reordered = non_baseline[:insert_idx] + [baseline] + non_baseline[insert_idx:]
    index_map = [ordered.index(label) for label in reordered]
    return reordered, index_map


def _select_target_rows(
    aggregates: list[dict[str, Any]],
    top_k_per_protocol: int,
    metric: str,
    include_all: bool,
    datasets: set[str] | None,
    protocols: set[str] | None,
    models: set[str] | None,
    feature_selectors: set[str] | None,
    explicit_selection: list[dict[str, str]] | None,
) -> list[dict[str, Any]]:
    if explicit_selection:
        selected: list[dict[str, Any]] = []
        for item in explicit_selection:
            dataset = str(item.get("dataset", ""))
            protocol = str(item.get("protocol", ""))
            pipeline_id = str(item.get("pipeline_id", "")).strip()
            model = str(item.get("model", ""))
            feature_selector = str(item.get("feature_selector", "none"))
            row = None
            for candidate in aggregates:
                if str(candidate.get("dataset", "")) != dataset:
                    continue
                if str(candidate.get("protocol", "")) != protocol:
                    continue
                if pipeline_id:
                    if _pipeline_id_from_row(candidate) == pipeline_id:
                        row = candidate
                        break
                else:
                    if str(candidate.get("model", "")) == model and _feature_selector_from_row(candidate) == feature_selector:
                        row = candidate
                        break
            if row is not None:
                selected.append(row)
        return selected

    filtered_rows: list[dict[str, Any]] = []
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in aggregates:
        if not _passes_filter(row, "dataset", datasets):
            continue
        if not _passes_filter(row, "protocol", protocols):
            continue
        if not _passes_filter(row, "model", models):
            continue
        if feature_selectors and _feature_selector_from_row(row) not in feature_selectors:
            continue
        filtered_rows.append(row)
        grouped[(str(row["dataset"]), str(row["protocol"]))].append(row)

    if include_all:
        return sorted(
            filtered_rows,
            key=lambda x: (
                str(x.get("dataset", "")),
                str(x.get("protocol", "")),
                -float(x.get(metric, 0.0)),
                str(x.get("model", "")),
                str(_feature_selector_from_row(x)),
                str(_pipeline_id_from_row(x)),
            ),
        )

    out: list[dict[str, Any]] = []
    for _, rows in sorted(grouped.items()):
        ranked = sorted(
            rows,
            key=lambda x: (
                float(x.get(metric, 0.0)),
                float(x.get("macro_f1_mean", 0.0)),
                float(x.get("balanced_accuracy_mean", 0.0)),
            ),
            reverse=True,
        )
        out.extend(ranked[:top_k_per_protocol])
    return out


def _aggregate_confusions(
    evaluations: list[dict[str, Any]],
    dataset: str,
    protocol: str,
    model: str,
    feature_selector: str | None,
    pipeline_id: str | None,
    label_order_strategy: str,
) -> dict[str, Any] | None:
    rows: list[dict[str, Any]] = []
    for row in evaluations:
        if str(row.get("dataset", "")) != dataset:
            continue
        if str(row.get("protocol", "")) != protocol:
            continue
        if str(row.get("model", "")) != model:
            continue
        row_feature_selector = _feature_selector_from_row(row)
        row_pipeline_id = _pipeline_id_from_row(row)
        if feature_selector is not None and row_feature_selector != str(feature_selector):
            continue
        if pipeline_id is not None and row_pipeline_id != str(pipeline_id):
            continue
        rows.append(row)
    if not rows:
        return None

    labels: list[str] = []
    matrix_sum: np.ndarray | None = None
    for row in rows:
        metrics = row.get("metrics", {})
        row_labels = [str(x) for x in metrics.get("confusion_matrix_labels", [])]
        row_matrix = np.asarray(metrics.get("confusion_matrix", []), dtype=np.float64)
        if not row_labels or row_matrix.size == 0:
            continue
        if matrix_sum is None:
            labels = row_labels
            matrix_sum = np.zeros_like(row_matrix, dtype=np.float64)
        if row_labels != labels:
            continue
        if row_matrix.shape != matrix_sum.shape:
            continue
        matrix_sum += row_matrix

    if matrix_sum is None:
        return None

    labels, idx_order = _reorder_labels(labels, strategy=label_order_strategy)
    matrix_sum = matrix_sum[np.ix_(idx_order, idx_order)]

    support = matrix_sum.sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        row_norm = np.divide(matrix_sum, support[:, None], where=support[:, None] > 0.0)
    row_norm = np.nan_to_num(row_norm, nan=0.0, posinf=0.0, neginf=0.0)
    recalls = np.diag(row_norm)

    return {
        "dataset": dataset,
        "protocol": protocol,
        "model": model,
        "feature_selector": str(feature_selector) if feature_selector is not None else "none",
        "pipeline_id": str(pipeline_id) if pipeline_id is not None else f"{model}+{feature_selector or 'none'}",
        "n_splits": len(rows),
        "labels": labels,
        "confusion_sum": matrix_sum.astype(int).tolist(),
        "confusion_row_normalized": row_norm.round(6).tolist(),
        "class_support": support.astype(int).tolist(),
        "class_recall": recalls.round(6).tolist(),
    }


def _build_markdown(highlights: list[dict[str, Any]], source_results: Path, metric: str) -> str:
    lines: list[str] = []
    lines.append("# Confusion Matrix Highlights")
    lines.append("")
    lines.append(f"- Source results: `{source_results}`")
    lines.append(f"- Ranking metric: `{metric}`")
    lines.append("")

    for item in highlights:
        lines.append(
            f"## {item['dataset']} | {item['protocol']} | {item['model']} | {item.get('feature_selector', 'none')} "
            f"[{item.get('pipeline_id', '')}] "
            f"(splits={item['n_splits']}, {metric}={item['aggregate_metric']:.4f})"
        )
        lines.append("")
        png_path = str(item.get("confusion_png", "")).strip()
        if png_path:
            lines.append(f"- Confusion PNG: `{png_path}`")
            lines.append("")
        labels = item["labels"]
        lines.append("### Class Recall")
        for label, recall, support in zip(labels, item["class_recall"], item["class_support"]):
            lines.append(f"- `{label}`: recall={float(recall):.4f}, support={int(support)}")
        lines.append("")
        lines.append("### Confusion (row-normalized)")
        header = "| true\\pred | " + " | ".join(labels) + " |"
        sep = "|" + "---|" * (len(labels) + 1)
        lines.append(header)
        lines.append(sep)
        for idx, label in enumerate(labels):
            vals = " | ".join(f"{float(v):.3f}" for v in item["confusion_row_normalized"][idx])
            lines.append(f"| {label} | {vals} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def _write_confusion_png(
    item: dict[str, Any],
    out_png_dir: Path,
    source_results: Path,
    cmap: str,
    dpi: int,
) -> Path:
    labels = [str(x) for x in item.get("labels", [])]
    norm = np.asarray(item.get("confusion_row_normalized", []), dtype=np.float64)
    counts = np.asarray(item.get("confusion_sum", []), dtype=np.int64)
    if norm.ndim != 2 or counts.ndim != 2:
        raise ValueError("Confusion matrices must be 2D.")
    if norm.shape != counts.shape:
        raise ValueError("Confusion normalized matrix shape must match count matrix shape.")

    n_classes = max(1, len(labels))
    fig_w = max(8.0, min(18.0, 1.2 * n_classes + 3.0))
    fig_h = max(7.0, min(16.0, 1.1 * n_classes + 3.0))
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    im = ax.imshow(norm, cmap=cmap, vmin=0.0, vmax=1.0)
    cbar = fig.colorbar(im, ax=ax, shrink=0.85)
    cbar.set_label("Row-normalized proportion")

    ax.set_xticks(range(n_classes))
    ax.set_yticks(range(n_classes))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)
    ax.set_xlabel("Predicted label")
    ax.set_ylabel("True label")
    ax.set_title(
        f"{item.get('dataset', '')} | {item.get('protocol', '')} | {item.get('pipeline_id', '')}\n"
        f"splits={item.get('n_splits', 0)}"
    )

    # Annotate each cell with percentage + count for quick interpretation.
    for i in range(norm.shape[0]):
        for j in range(norm.shape[1]):
            val = float(norm[i, j])
            cnt = int(counts[i, j])
            text_color = "white" if val >= 0.55 else "black"
            ax.text(
                j,
                i,
                f"{val:.2f}\n({cnt})",
                ha="center",
                va="center",
                color=text_color,
                fontsize=8,
            )

    fig.tight_layout()
    out_subdir = (
        out_png_dir
        / _slug(source_results.stem)
        / _slug(item.get("dataset", ""))
        / _slug(item.get("protocol", ""))
    )
    out_subdir.mkdir(parents=True, exist_ok=True)
    file_name = f"{_slug(item.get('pipeline_id', 'pipeline'))}.png"
    out_path = out_subdir / file_name
    fig.savefig(out_path, dpi=max(72, int(dpi)))
    plt.close(fig)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Post-hoc confusion matrix highlighter for Stage 6. "
            "Selects top runs and aggregates confusion matrices across their outer splits."
        )
    )
    parser.add_argument("--results-json", required=True, help="Path to Stage 6 ml_results.json.")
    parser.add_argument("--out-json", default=None, help="Output JSON path (default: reports/confusion_highlights.json).")
    parser.add_argument("--out-md", default=None, help="Output markdown path (default: reports/confusion_highlights.md).")
    parser.add_argument(
        "--out-png-dir",
        default=None,
        help="Output directory for confusion matrix PNG images (default: reports/confusion_pngs).",
    )
    parser.add_argument("--png-cmap", default="Blues", help="Matplotlib colormap for confusion PNGs.")
    parser.add_argument("--png-dpi", type=int, default=180, help="PNG DPI (default: 180).")
    parser.add_argument("--top-k-per-protocol", type=int, default=1, help="Top K models per dataset+protocol.")
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include all filtered aggregate rows (all model/selector pipelines), ignoring top-k.",
    )
    parser.add_argument(
        "--metric",
        choices=["balanced_accuracy_mean", "macro_f1_mean", "accuracy_mean", "weighted_f1_mean"],
        default="balanced_accuracy_mean",
        help="Aggregate metric used for top-k ranking.",
    )
    parser.add_argument("--datasets", nargs="*", default=None, help="Optional dataset filter.")
    parser.add_argument("--protocols", nargs="*", default=None, help="Optional protocol filter.")
    parser.add_argument("--models", nargs="*", default=None, help="Optional model filter.")
    parser.add_argument("--feature-selectors", nargs="*", default=None, help="Optional feature-selector filter.")
    parser.add_argument(
        "--selection-json",
        default=None,
        help=(
            "Optional JSON list of explicit selections. "
            "Format: [{\"dataset\":\"fused\",\"protocol\":\"loso\",\"model\":\"mlp\",\"feature_selector\":\"anova\"}, ...]"
        ),
    )
    parser.add_argument(
        "--label-order-strategy",
        choices=["baseline_first", "baseline_after_easiest", "as_is"],
        default="baseline_first",
        help="Label ordering for confusion outputs.",
    )
    args = parser.parse_args()

    if not args.include_all and args.top_k_per_protocol < 1:
        raise ValueError("--top-k-per-protocol must be >= 1")

    results_path = _resolve_path(args.results_json)
    out_json = _resolve_path(args.out_json) if args.out_json else _default_out_json()
    out_md = _resolve_path(args.out_md) if args.out_md else _default_out_md()
    out_png_dir = _resolve_path(args.out_png_dir) if args.out_png_dir else _default_out_png_dir()

    payload = _load_json(results_path)
    aggregates = payload.get("aggregates", [])
    evaluations = payload.get("evaluations", [])

    explicit_selection = None
    if args.selection_json:
        explicit_selection = _load_json(_resolve_path(args.selection_json))
        if not isinstance(explicit_selection, list):
            raise ValueError("--selection-json must be a JSON list.")

    selected = _select_target_rows(
        aggregates=aggregates,
        top_k_per_protocol=args.top_k_per_protocol,
        metric=args.metric,
        include_all=bool(args.include_all),
        datasets=set(args.datasets) if args.datasets else None,
        protocols=set(args.protocols) if args.protocols else None,
        models=set(args.models) if args.models else None,
        feature_selectors=set(args.feature_selectors) if args.feature_selectors else None,
        explicit_selection=explicit_selection,
    )

    highlights: list[dict[str, Any]] = []
    for row in selected:
        dataset = str(row.get("dataset", ""))
        protocol = str(row.get("protocol", ""))
        model = str(row.get("model", ""))
        feature_selector = _feature_selector_from_row(row)
        pipeline_id = _pipeline_id_from_row(row)
        summary = _aggregate_confusions(
            evaluations,
            dataset=dataset,
            protocol=protocol,
            model=model,
            feature_selector=feature_selector,
            pipeline_id=pipeline_id,
            label_order_strategy=args.label_order_strategy,
        )
        if summary is None:
            continue
        summary["aggregate_metric"] = float(row.get(args.metric, 0.0))
        summary["aggregate_row"] = row
        png_path = _write_confusion_png(
            summary,
            out_png_dir=out_png_dir,
            source_results=results_path,
            cmap=str(args.png_cmap),
            dpi=int(args.png_dpi),
        )
        summary["confusion_png"] = str(png_path)
        highlights.append(summary)

    result_payload = {
        "source_results_json": str(results_path),
        "metric": args.metric,
        "top_k_per_protocol": args.top_k_per_protocol,
        "include_all": bool(args.include_all),
        "filters": {
            "datasets": args.datasets or [],
            "protocols": args.protocols or [],
            "models": args.models or [],
            "feature_selectors": args.feature_selectors or [],
            "selection_json": str(_resolve_path(args.selection_json)) if args.selection_json else None,
        },
        "label_order_strategy": args.label_order_strategy,
        "n_highlights": len(highlights),
        "highlights": highlights,
    }
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result_payload, indent=2) + "\n", encoding="utf-8")

    markdown_text = _build_markdown(highlights=highlights, source_results=results_path, metric=args.metric)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_text, encoding="utf-8")

    print("Confusion highlights complete.")
    print(f"  Selected combinations: {len(highlights)}")
    print(f"  Output JSON: {out_json}")
    print(f"  Output Markdown: {out_md}")
    print(f"  Output PNG dir: {out_png_dir}")


if __name__ == "__main__":
    main()

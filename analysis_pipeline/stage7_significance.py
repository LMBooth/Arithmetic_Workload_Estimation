"""Stage 7 — peer-review-grade significance and bootstrap statistics.

This stage consumes the per-cell aggregate results emitted by Stage 6
(``ml_results_<scenario>_classic_nn.json``) for one or two run profiles
and reproduces every inferential statistic referenced in the
manuscript Section "Statistical Significance Procedures (Stage 7)":

1. **Paired Wilcoxon signed-rank test** of the per-cell best-model
   mean balanced accuracies for two profiles (typically the 6 s
   baseline and the 3 s overlap runs). One scalar per cell (best
   model in that scenario × dataset × protocol cell), paired across
   matched cells.
2. **2000-sample non-parametric bootstrap** of the per-cell mean
   balanced accuracy over outer-fold scores, producing
   percentile-method 95 % confidence intervals.
3. **One-sided Wilcoxon signed-rank test against chance**
   (``alternative='greater'``) on outer-fold balanced-accuracy
   values vs the per-scenario chance level
   ``1 / n_classes``.
4. **Label-shuffle permutation test** on held-out predicted-label
   vectors reconstructed from the per-fold confusion matrices
   (10 000 permutations by default), with Bonferroni correction over
   the full cell grid.

Optionally also computes the paired Wilcoxon signed-rank test on the
participant-level baseline-vs-task heart-rate values used in the
quality-check section of the manuscript.

The output is written as both a machine-readable JSON
(``significance_summary.json``) and a human-readable Markdown
(``significance_summary.md``) so the manuscript can quote individual
numbers directly and reviewers can audit the test machinery.

Typical invocation (matches the YAML stanzas added in
``config/pipeline_unified_classic_nn_baseline_*_preproc.yaml``)::

    python -m analysis_pipeline.stage7_significance \\
        --baseline-reports analysis_pipeline/runs/pipeline_unified_classic_nn_baseline_preproc/reports \\
        --overlap-reports  analysis_pipeline/runs/pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc/reports \\
        --out-json significance_summary.json \\
        --out-md   significance_summary.md \\
        --n-bootstrap 2000 \\
        --n-permutations 10000 \\
        --random-seed 42
"""
from __future__ import annotations

import argparse
import json
import logging
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import numpy as np

try:
    from scipy.stats import wilcoxon
except ImportError as err:  # pragma: no cover - SciPy is a hard dep
    raise SystemExit(
        "scipy is required for stage7_significance; install with `pip install scipy`."
    ) from err

LOGGER = logging.getLogger("stage7_significance")

# ---------------------------------------------------------------------------
# Domain types
# ---------------------------------------------------------------------------

# Five configured class scenarios in the published benchmark.
SCENARIOS = (
    "baseline_all_bins",
    "baseline_omit_easiest",
    "baseline_omit_hardest",
    "baseline_low_high_omit_hardest",
    "baseline_grouped_4class_omit_hardest",
)

DATASETS = ("eeg", "ecg", "pupil", "fused")
PROTOCOLS = ("within_participant", "pooled_stratified", "group_holdout")


@dataclass
class CellRecord:
    """Per (scenario, dataset, protocol) best-model record."""

    scenario: str
    dataset: str
    protocol: str
    best_model: str
    best_pipeline: str
    n_classes: int
    chance: float
    mean_balanced_accuracy: float
    outer_fold_balanced_accuracies: list[float]
    confusion_matrices: list[list[list[int]]]  # one per outer fold
    confusion_labels: list[str]

    @property
    def cell_key(self) -> tuple[str, str, str]:
        return (self.scenario, self.dataset, self.protocol)


@dataclass
class CellSignificance:
    cell_key: tuple[str, str, str]
    profile: str
    best_pipeline: str
    n_outer_folds: int
    mean_ba: float
    bootstrap_ci_low: float
    bootstrap_ci_high: float
    chance: float
    wilcoxon_vs_chance_stat: float | None
    wilcoxon_vs_chance_p: float | None
    permutation_p: float
    permutation_n_iterations: int
    permutation_observed_ba: float
    bonferroni_threshold: float
    survives_bonferroni: bool


@dataclass
class PairedComparison:
    paired_n: int
    matched_cells: list[dict]
    mean_baseline: float
    mean_overlap: float
    delta_mean: float
    mean_macro_f1_baseline: float | None
    mean_macro_f1_overlap: float | None
    delta_macro_f1: float | None
    matched_improved: int
    matched_worsened: int
    matched_unchanged: int
    winning_model_changed: int
    wilcoxon_statistic: float
    wilcoxon_pvalue: float


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def _scenario_results_path(reports_dir: Path, scenario: str) -> Path | None:
    """Find the ml_results_<scenario>_*.json file inside ``reports_dir``."""
    candidates = sorted(reports_dir.glob(f"ml_results_{scenario}_*.json"))
    if not candidates:
        return None
    # Prefer the canonical "_classic_nn.json" variant when present.
    for path in candidates:
        if path.name.endswith("_classic_nn.json"):
            return path
    return candidates[0]


def _load_results(reports_dir: Path) -> dict[str, dict]:
    """Load every available scenario JSON in ``reports_dir``."""
    out: dict[str, dict] = {}
    for scenario in SCENARIOS:
        path = _scenario_results_path(reports_dir, scenario)
        if path is None:
            LOGGER.warning("No ml_results JSON for scenario %s in %s", scenario, reports_dir)
            continue
        try:
            with path.open("r", encoding="utf-8") as fh:
                out[scenario] = json.load(fh)
        except (OSError, json.JSONDecodeError) as err:
            LOGGER.error("Failed to load %s: %s", path, err)
    return out


def _extract_best_models(scenario_payload: dict) -> dict[tuple[str, str], dict]:
    """Index ``best_models[]`` by ``(dataset, protocol)``."""
    best_models = scenario_payload.get("best_models") or []
    indexed: dict[tuple[str, str], dict] = {}
    for entry in best_models:
        ds = entry.get("dataset")
        proto = entry.get("protocol")
        if ds and proto:
            indexed[(ds, proto)] = entry
    return indexed


def _collect_outer_folds(
    scenario_payload: dict, dataset: str, protocol: str, model: str, feature_selector: str
) -> tuple[list[float], list[list[list[int]]], list[str]]:
    """Return (outer-fold balanced accuracies, confusion matrices, labels)."""
    outer_ba: list[float] = []
    cms: list[list[list[int]]] = []
    cm_labels: list[str] = []
    for ev in scenario_payload.get("evaluations", []):
        if (
            ev.get("dataset") == dataset
            and ev.get("protocol") == protocol
            and ev.get("model") == model
            and ev.get("feature_selector", feature_selector) == feature_selector
        ):
            metrics = ev.get("metrics") or {}
            ba = metrics.get("balanced_accuracy")
            if ba is None:
                continue
            outer_ba.append(float(ba))
            cm = metrics.get("confusion_matrix")
            if cm is not None:
                cms.append(cm)
            labels = metrics.get("confusion_matrix_labels")
            if labels and not cm_labels:
                cm_labels = list(labels)
    return outer_ba, cms, cm_labels


def _build_cell_records(
    scenario: str, payload: dict
) -> dict[tuple[str, str, str], CellRecord]:
    """Build one CellRecord per (dataset, protocol) for the scenario's winners."""
    final_labels = (
        payload.get("config", {}).get("class_scenario", {}).get("final_labels") or []
    )
    n_classes = max(2, len(final_labels))
    chance = 1.0 / n_classes
    best_index = _extract_best_models(payload)
    records: dict[tuple[str, str, str], CellRecord] = {}
    for (dataset, protocol), entry in best_index.items():
        best_model = entry.get("best_model") or entry.get("model")
        feature_selector = (
            entry.get("best_feature_selector") or entry.get("feature_selector") or "none"
        )
        if not best_model:
            continue
        outer_ba, cms, cm_labels = _collect_outer_folds(
            payload, dataset, protocol, best_model, feature_selector
        )
        if not outer_ba:
            LOGGER.warning(
                "No outer-fold values for %s/%s/%s/%s in scenario %s",
                dataset,
                protocol,
                best_model,
                feature_selector,
                scenario,
            )
            continue
        record = CellRecord(
            scenario=scenario,
            dataset=dataset,
            protocol=protocol,
            best_model=best_model,
            best_pipeline=entry.get("best_pipeline") or f"{best_model}+{feature_selector}",
            n_classes=n_classes,
            chance=chance,
            mean_balanced_accuracy=float(entry.get("balanced_accuracy_mean") or np.mean(outer_ba)),
            outer_fold_balanced_accuracies=outer_ba,
            confusion_matrices=cms,
            confusion_labels=cm_labels or list(final_labels),
        )
        records[record.cell_key] = record
    return records


def _macro_f1_lookup(payload: dict) -> dict[tuple[str, str], float]:
    """Return mean macro-F1 by (dataset, protocol) from the best-models block."""
    best_index = _extract_best_models(payload)
    return {
        key: float(entry.get("macro_f1_mean", float("nan")))
        for key, entry in best_index.items()
    }


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------


def _balanced_accuracy_from_cm(cm: np.ndarray) -> float:
    """Macro-averaged recall (= balanced accuracy) from a confusion matrix.

    Rows are true classes, columns are predicted classes. Empty rows
    contribute nothing (consistent with sklearn's behaviour).
    """
    cm = np.asarray(cm, dtype=float)
    if cm.size == 0:
        return float("nan")
    row_sums = cm.sum(axis=1)
    valid = row_sums > 0
    if not np.any(valid):
        return float("nan")
    diag = np.diag(cm)
    recalls = np.where(valid, diag / np.where(valid, row_sums, 1.0), 0.0)
    return float(recalls[valid].mean())


def _reconstruct_labels_from_cm(
    cm: np.ndarray, labels: list[str]
) -> tuple[np.ndarray, np.ndarray]:
    """Reconstruct (y_true, y_pred) integer arrays from a confusion matrix.

    The exact ordering of samples within a (true, pred) cell is irrelevant
    for permutation tests on confusion-matrix-derived metrics.
    """
    cm = np.asarray(cm, dtype=int)
    n = cm.shape[0]
    y_true_chunks: list[np.ndarray] = []
    y_pred_chunks: list[np.ndarray] = []
    for i in range(n):
        for j in range(n):
            count = int(cm[i, j])
            if count <= 0:
                continue
            y_true_chunks.append(np.full(count, i, dtype=int))
            y_pred_chunks.append(np.full(count, j, dtype=int))
    if not y_true_chunks:
        return np.empty(0, dtype=int), np.empty(0, dtype=int)
    return np.concatenate(y_true_chunks), np.concatenate(y_pred_chunks)


def _bootstrap_ci(
    outer_fold_values: list[float], n_bootstrap: int, rng: np.random.Generator, alpha: float = 0.05
) -> tuple[float, float, float]:
    """Percentile-method bootstrap CI of the mean over outer-fold values."""
    arr = np.asarray(outer_fold_values, dtype=float)
    if arr.size == 0:
        return float("nan"), float("nan"), float("nan")
    point = float(arr.mean())
    if arr.size == 1:
        return point, point, point
    boot_means = np.empty(n_bootstrap, dtype=float)
    n = arr.size
    for b in range(n_bootstrap):
        idx = rng.integers(0, n, size=n)
        boot_means[b] = arr[idx].mean()
    lo = float(np.quantile(boot_means, alpha / 2.0))
    hi = float(np.quantile(boot_means, 1.0 - alpha / 2.0))
    return point, lo, hi


def _wilcoxon_vs_chance(
    outer_fold_values: list[float], chance: float
) -> tuple[float | None, float | None]:
    """One-sided Wilcoxon signed-rank: H1 = outer-fold BA > chance.

    Returns (statistic, p-value) or (None, None) when the test is not
    well defined (e.g. <2 non-zero residuals).
    """
    arr = np.asarray(outer_fold_values, dtype=float) - chance
    if arr.size < 2:
        return None, None
    if not np.any(arr != 0):
        return None, None
    try:
        result = wilcoxon(arr, alternative="greater", zero_method="wilcox", correction=False)
    except ValueError:
        return None, None
    return float(result.statistic), float(result.pvalue)


def _label_shuffle_permutation_p(
    confusion_matrices: list[list[list[int]]],
    n_permutations: int,
    rng: np.random.Generator,
    batch_size: int = 500,
) -> tuple[float, float]:
    """Label-shuffle permutation p-value on pooled per-fold predictions.

    Reconstruct (y_true, y_pred) per fold from the stored confusion
    matrices, pool across folds, then shuffle the predicted labels
    against the held-out true labels and recompute balanced accuracy.
    The inner loop is vectorised over a configurable batch of
    permutations to keep wall-clock time reasonable for ``n_permutations``
    in the 10 000 range.

    Returns (p_value, observed_balanced_accuracy).
    """
    if not confusion_matrices:
        return float("nan"), float("nan")

    y_true_parts: list[np.ndarray] = []
    y_pred_parts: list[np.ndarray] = []
    for cm in confusion_matrices:
        cm_arr = np.asarray(cm, dtype=int)
        if cm_arr.size == 0:
            continue
        yt, yp = _reconstruct_labels_from_cm(cm_arr, [])
        if yt.size:
            y_true_parts.append(yt)
            y_pred_parts.append(yp)
    if not y_true_parts:
        return float("nan"), float("nan")
    y_true = np.concatenate(y_true_parts).astype(np.int64)
    y_pred = np.concatenate(y_pred_parts).astype(np.int64)
    n = y_true.size
    n_classes = int(max(int(y_true.max()) + 1, int(y_pred.max()) + 1))

    # Per-class true-count denominators for balanced accuracy.
    true_counts = np.bincount(y_true, minlength=n_classes).astype(float)
    valid_classes = true_counts > 0
    n_valid = int(valid_classes.sum())
    if n_valid == 0:
        return float("nan"), float("nan")
    safe_counts = np.where(valid_classes, true_counts, 1.0)

    # Observed balanced accuracy from the pooled CM.
    obs_cm = np.zeros((n_classes, n_classes), dtype=float)
    np.add.at(obs_cm, (y_true, y_pred), 1.0)
    observed = _balanced_accuracy_from_cm(obs_cm)

    # Vectorised permutation block.
    # For each batch of B perms we draw a (B, n) integer array whose rows
    # are independent shuffles of y_pred indices, then compute B balanced
    # accuracies in parallel via flat-bincount over composite indices.
    n_at_least = 1  # plus-one numerator -> empirical floor 1/(N+1)
    arange_n = np.arange(n)
    composite_base = (y_true * n_classes).astype(np.int64)  # for diag extraction
    perms_left = n_permutations
    while perms_left > 0:
        batch = min(batch_size, perms_left)
        # rng.permuted with a tiled arange == B independent permutations.
        perm_idx = rng.permuted(np.broadcast_to(arange_n, (batch, n)), axis=1)
        y_pred_perm = y_pred[perm_idx]  # shape (batch, n)
        # For each row, the diagonal of the CM is the count of i such that
        # y_pred_perm[b, i] == y_true[i]. Per-class diagonal = bincount.
        # Composite key = y_true * n_classes + y_pred_perm picks out the
        # full (true, pred) cells; we only need the diagonal.
        # Compute per-row, per-true-class diagonal counts:
        #   match_mask[b, i] = (y_pred_perm[b, i] == y_true[i])
        match_mask = (y_pred_perm == y_true[None, :])
        # Sum per true class via bincount weighted by match_mask.
        # Vectorise across batch with a flat representation.
        if n_valid > 0:
            # weights of shape (batch, n)
            weights = match_mask.astype(np.float64)
            # For each batch row, accumulate per-true-class.
            # Use add.at on a (batch, n_classes) array.
            diag = np.zeros((batch, n_classes), dtype=np.float64)
            # Vectorise via a single np.add.at on flattened indices.
            row_idx = np.broadcast_to(np.arange(batch)[:, None], (batch, n)).ravel()
            col_idx = np.broadcast_to(y_true, (batch, n)).ravel()
            np.add.at(diag, (row_idx, col_idx), weights.ravel())
            recalls = diag / safe_counts[None, :]
            # zero out invalid classes before averaging
            recalls = recalls * valid_classes[None, :]
            ba_batch = recalls.sum(axis=1) / n_valid
            n_at_least += int((ba_batch >= observed).sum())
        perms_left -= batch
    p_value = n_at_least / (n_permutations + 1)
    return float(p_value), float(observed)


# ---------------------------------------------------------------------------
# Optional: paired HR test for the QC sanity check
# ---------------------------------------------------------------------------


def _paired_hr_test(qc_summary_path: Path | None) -> dict | None:
    """Paired Wilcoxon signed-rank on baseline-vs-task heart rate.

    Reads the Stage 1 QC dataset summary JSON and looks for paired
    per-participant HR values (``hr_baseline_mean`` and ``hr_task_mean``).
    Returns ``None`` if those fields aren't present (older QC outputs);
    the test is then skipped silently.
    """
    if qc_summary_path is None or not qc_summary_path.exists():
        return None
    try:
        with qc_summary_path.open("r", encoding="utf-8") as fh:
            payload = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None

    rows = payload.get("participant_hr_pairs") or payload.get("subjects") or []
    baseline: list[float] = []
    task: list[float] = []
    for row in rows:
        b = row.get("hr_baseline_mean") or row.get("hr_baseline_bpm")
        t = row.get("hr_task_mean") or row.get("hr_task_bpm")
        if b is None or t is None:
            continue
        try:
            baseline.append(float(b))
            task.append(float(t))
        except (TypeError, ValueError):
            continue
    if len(baseline) < 2:
        return None
    diff = np.asarray(task) - np.asarray(baseline)
    if not np.any(diff != 0):
        return None
    try:
        result = wilcoxon(diff, alternative="greater", zero_method="wilcox", correction=False)
    except ValueError:
        return None
    return {
        "n_paired_participants": len(baseline),
        "mean_hr_baseline_bpm": float(np.mean(baseline)),
        "mean_hr_task_bpm": float(np.mean(task)),
        "delta_bpm": float(np.mean(diff)),
        "wilcoxon_statistic": float(result.statistic),
        "wilcoxon_pvalue": float(result.pvalue),
        "alternative": "task > baseline",
    }


# ---------------------------------------------------------------------------
# Pipeline orchestration
# ---------------------------------------------------------------------------


def _per_cell_significance(
    profile_label: str,
    cell_records: dict[tuple[str, str, str], CellRecord],
    n_bootstrap: int,
    n_permutations: int,
    bonferroni_threshold: float,
    rng: np.random.Generator,
) -> list[CellSignificance]:
    out: list[CellSignificance] = []
    for key in sorted(cell_records.keys()):
        rec = cell_records[key]
        point, lo, hi = _bootstrap_ci(rec.outer_fold_balanced_accuracies, n_bootstrap, rng)
        w_stat, w_p = _wilcoxon_vs_chance(rec.outer_fold_balanced_accuracies, rec.chance)
        perm_p, obs_ba = _label_shuffle_permutation_p(
            rec.confusion_matrices, n_permutations, rng
        )
        out.append(
            CellSignificance(
                cell_key=key,
                profile=profile_label,
                best_pipeline=rec.best_pipeline,
                n_outer_folds=len(rec.outer_fold_balanced_accuracies),
                mean_ba=point,
                bootstrap_ci_low=lo,
                bootstrap_ci_high=hi,
                chance=rec.chance,
                wilcoxon_vs_chance_stat=w_stat,
                wilcoxon_vs_chance_p=w_p,
                permutation_p=perm_p,
                permutation_n_iterations=n_permutations,
                permutation_observed_ba=obs_ba,
                bonferroni_threshold=bonferroni_threshold,
                survives_bonferroni=(perm_p < bonferroni_threshold) if not math.isnan(perm_p) else False,
            )
        )
    return out


def _paired_overlap_vs_baseline(
    baseline_records: dict[tuple[str, str, str], CellRecord],
    overlap_records: dict[tuple[str, str, str], CellRecord],
    baseline_macro_f1: dict[tuple[str, str], float],
    overlap_macro_f1: dict[tuple[str, str], float],
) -> PairedComparison:
    matched_keys = sorted(set(baseline_records.keys()) & set(overlap_records.keys()))
    if not matched_keys:
        raise SystemExit(
            "No matched cells between baseline and overlap profiles; cannot run paired Wilcoxon."
        )

    baseline_ba: list[float] = []
    overlap_ba: list[float] = []
    f1_baseline: list[float] = []
    f1_overlap: list[float] = []
    matched_cells: list[dict] = []
    improved = worsened = unchanged = winners_changed = 0
    for key in matched_keys:
        scenario, dataset, protocol = key
        b_rec = baseline_records[key]
        o_rec = overlap_records[key]
        b_ba = b_rec.mean_balanced_accuracy
        o_ba = o_rec.mean_balanced_accuracy
        baseline_ba.append(b_ba)
        overlap_ba.append(o_ba)
        delta = o_ba - b_ba
        if delta > 0:
            improved += 1
        elif delta < 0:
            worsened += 1
        else:
            unchanged += 1
        if b_rec.best_model != o_rec.best_model:
            winners_changed += 1
        f1b = baseline_macro_f1.get((dataset, protocol), float("nan"))
        f1o = overlap_macro_f1.get((dataset, protocol), float("nan"))
        f1_baseline.append(f1b)
        f1_overlap.append(f1o)
        matched_cells.append(
            {
                "scenario": scenario,
                "dataset": dataset,
                "protocol": protocol,
                "baseline_best_pipeline": b_rec.best_pipeline,
                "overlap_best_pipeline": o_rec.best_pipeline,
                "baseline_balanced_accuracy": b_ba,
                "overlap_balanced_accuracy": o_ba,
                "delta_balanced_accuracy": delta,
                "winner_changed": b_rec.best_model != o_rec.best_model,
            }
        )

    diff = np.asarray(overlap_ba) - np.asarray(baseline_ba)
    try:
        result = wilcoxon(
            diff, alternative="greater", zero_method="wilcox", correction=False
        )
        stat = float(result.statistic)
        pval = float(result.pvalue)
    except ValueError:
        stat = float("nan")
        pval = float("nan")

    f1_b_arr = np.asarray(f1_baseline, dtype=float)
    f1_o_arr = np.asarray(f1_overlap, dtype=float)
    f1_b_mean = float(np.nanmean(f1_b_arr)) if f1_b_arr.size else None
    f1_o_mean = float(np.nanmean(f1_o_arr)) if f1_o_arr.size else None
    delta_f1 = (
        f1_o_mean - f1_b_mean if (f1_b_mean is not None and f1_o_mean is not None) else None
    )

    return PairedComparison(
        paired_n=len(matched_keys),
        matched_cells=matched_cells,
        mean_baseline=float(np.mean(baseline_ba)),
        mean_overlap=float(np.mean(overlap_ba)),
        delta_mean=float(np.mean(diff)),
        mean_macro_f1_baseline=f1_b_mean,
        mean_macro_f1_overlap=f1_o_mean,
        delta_macro_f1=delta_f1,
        matched_improved=improved,
        matched_worsened=worsened,
        matched_unchanged=unchanged,
        winning_model_changed=winners_changed,
        wilcoxon_statistic=stat,
        wilcoxon_pvalue=pval,
    )


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def _format_p(p: float | None) -> str:
    if p is None or (isinstance(p, float) and math.isnan(p)):
        return "n/a"
    if p < 1e-4:
        return f"{p:.2e}"
    return f"{p:.4f}"


def _cell_significance_to_dict(rec: CellSignificance) -> dict:
    return {
        "scenario": rec.cell_key[0],
        "dataset": rec.cell_key[1],
        "protocol": rec.cell_key[2],
        "profile": rec.profile,
        "best_pipeline": rec.best_pipeline,
        "n_outer_folds": rec.n_outer_folds,
        "mean_balanced_accuracy": rec.mean_ba,
        "bootstrap_ci_95": [rec.bootstrap_ci_low, rec.bootstrap_ci_high],
        "chance_level": rec.chance,
        "wilcoxon_vs_chance_statistic": rec.wilcoxon_vs_chance_stat,
        "wilcoxon_vs_chance_pvalue": rec.wilcoxon_vs_chance_p,
        "permutation_pvalue": rec.permutation_p,
        "permutation_n_iterations": rec.permutation_n_iterations,
        "permutation_observed_balanced_accuracy": rec.permutation_observed_ba,
        "bonferroni_threshold": rec.bonferroni_threshold,
        "survives_bonferroni": rec.survives_bonferroni,
    }


def _write_markdown(out_md: Path, summary: dict) -> None:
    pc = summary.get("paired_overlap_vs_baseline")
    lines: list[str] = []
    lines.append("# Stage 7 — Significance Summary\n")
    lines.append(f"- Generated by: `analysis_pipeline/stage7_significance.py`")
    lines.append(f"- Bootstrap iterations: `{summary['n_bootstrap']}`")
    lines.append(f"- Permutation iterations: `{summary['n_permutations']}`")
    lines.append(f"- Bonferroni threshold (n_cells={summary['n_cells_total']}): `{summary['bonferroni_threshold']:.3e}`")
    lines.append(f"- Random seed: `{summary['random_seed']}`")
    lines.append("")

    if pc is not None:
        lines.append("## Paired Wilcoxon — 3 s overlap vs 6 s baseline (best-model balanced accuracy)\n")
        lines.append(f"- Paired n = `{pc['paired_n']}` matched cells")
        lines.append(f"- Mean balanced accuracy (6 s baseline): `{pc['mean_baseline']:.4f}`")
        lines.append(f"- Mean balanced accuracy (3 s overlap):  `{pc['mean_overlap']:.4f}`")
        lines.append(f"- Mean delta: `{pc['delta_mean']:+.4f}`")
        if pc['mean_macro_f1_baseline'] is not None:
            lines.append(f"- Mean macro-F1 (6 s baseline): `{pc['mean_macro_f1_baseline']:.4f}`")
        if pc['mean_macro_f1_overlap'] is not None:
            lines.append(f"- Mean macro-F1 (3 s overlap):  `{pc['mean_macro_f1_overlap']:.4f}`")
        if pc['delta_macro_f1'] is not None:
            lines.append(f"- Mean macro-F1 delta: `{pc['delta_macro_f1']:+.4f}`")
        lines.append(f"- Cells improved / worsened / unchanged: `{pc['matched_improved']}` / `{pc['matched_worsened']}` / `{pc['matched_unchanged']}`")
        lines.append(f"- Winning model identity changed in: `{pc['winning_model_changed']}` cells")
        lines.append(
            f"- Wilcoxon paired (3 s > 6 s): W = `{pc['wilcoxon_statistic']:.0f}`, p = `{_format_p(pc['wilcoxon_pvalue'])}`"
        )
        lines.append("")

    lines.append("## Per-cell significance (best model in each scenario × dataset × protocol)\n")
    header = "| profile | scenario | dataset | protocol | best_pipeline | n_folds | mean_BA | 95% CI | chance | Wilcoxon p (vs chance) | perm p | survives Bonferroni? |"
    sep = "|" + "|".join(["---"] * 12) + "|"
    lines.append(header)
    lines.append(sep)
    for rec in summary["per_cell"]:
        lines.append(
            "| {profile} | {scenario} | {dataset} | {protocol} | {pipe} | {nf} | {ba:.4f} | [{lo:.4f}, {hi:.4f}] | {ch:.4f} | {wp} | {pp} | {bonf} |".format(
                profile=rec["profile"],
                scenario=rec["scenario"],
                dataset=rec["dataset"],
                protocol=rec["protocol"],
                pipe=rec["best_pipeline"],
                nf=rec["n_outer_folds"],
                ba=rec["mean_balanced_accuracy"],
                lo=rec["bootstrap_ci_95"][0],
                hi=rec["bootstrap_ci_95"][1],
                ch=rec["chance_level"],
                wp=_format_p(rec["wilcoxon_vs_chance_pvalue"]),
                pp=_format_p(rec["permutation_pvalue"]),
                bonf="yes" if rec["survives_bonferroni"] else "no",
            )
        )
    lines.append("")

    counts = summary["per_cell_summary_counts"]
    lines.append("## Aggregate counts\n")
    lines.append(f"- Total cells analysed: `{counts['n_cells']}`")
    lines.append(
        f"- Cells with one-sided Wilcoxon vs chance p<0.05 (uncorrected): `{counts['n_wilcoxon_vs_chance_below_005']}` / `{counts['n_cells_with_wilcoxon']}`"
    )
    lines.append(
        f"- Cells surviving Bonferroni (perm p < {summary['bonferroni_threshold']:.3e}): `{counts['n_survives_bonferroni']}` / `{counts['n_cells']}`"
    )
    lines.append(
        f"- Cells with permutation p at empirical floor 1/(N+1) = `{1.0 / (summary['n_permutations'] + 1):.3e}`: `{counts['n_at_perm_floor']}`"
    )
    lines.append("")

    hr = summary.get("hr_baseline_vs_task")
    if hr is not None:
        lines.append("## Heart-rate sanity check (baseline vs task)\n")
        lines.append(f"- Paired participants: `{hr['n_paired_participants']}`")
        lines.append(f"- Mean baseline HR: `{hr['mean_hr_baseline_bpm']:.3f}` bpm")
        lines.append(f"- Mean task HR:     `{hr['mean_hr_task_bpm']:.3f}` bpm")
        lines.append(f"- Delta:            `{hr['delta_bpm']:+.3f}` bpm")
        lines.append(
            f"- Wilcoxon (task > baseline): W = `{hr['wilcoxon_statistic']:.0f}`, p = `{_format_p(hr['wilcoxon_pvalue'])}`"
        )
        lines.append("")

    out_md.write_text("\n".join(lines), encoding="utf-8")


def _summarise_counts(per_cell: list[dict]) -> dict:
    n_total = len(per_cell)
    n_with_wilcoxon = sum(1 for r in per_cell if r["wilcoxon_vs_chance_pvalue"] is not None)
    n_below_005 = sum(
        1
        for r in per_cell
        if r["wilcoxon_vs_chance_pvalue"] is not None and r["wilcoxon_vs_chance_pvalue"] < 0.05
    )
    n_bonf = sum(1 for r in per_cell if r["survives_bonferroni"])
    floor_count = sum(
        1
        for r in per_cell
        if (
            r["permutation_pvalue"] is not None
            and not math.isnan(r["permutation_pvalue"])
            and abs(r["permutation_pvalue"] - 1.0 / (r["permutation_n_iterations"] + 1)) < 1e-12
        )
    )
    return {
        "n_cells": n_total,
        "n_cells_with_wilcoxon": n_with_wilcoxon,
        "n_wilcoxon_vs_chance_below_005": n_below_005,
        "n_survives_bonferroni": n_bonf,
        "n_at_perm_floor": floor_count,
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def _build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Stage 7 — significance and bootstrap statistics for the Stage 6 results.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--baseline-reports",
        type=Path,
        required=True,
        help="Reports directory of the 6 s baseline run profile.",
    )
    parser.add_argument(
        "--overlap-reports",
        type=Path,
        default=None,
        help="Reports directory of the 3 s overlap run profile (omit to disable the paired Wilcoxon).",
    )
    parser.add_argument(
        "--baseline-qc-summary",
        type=Path,
        default=None,
        help="Optional path to the baseline run's qc_dataset_summary.json (for HR Wilcoxon).",
    )
    parser.add_argument(
        "--out-json",
        type=Path,
        default=Path("significance_summary.json"),
    )
    parser.add_argument(
        "--out-md",
        type=Path,
        default=Path("significance_summary.md"),
    )
    parser.add_argument("--n-bootstrap", type=int, default=2000)
    parser.add_argument("--n-permutations", type=int, default=10000)
    parser.add_argument("--random-seed", type=int, default=42)
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    return parser


def _resolve_paired_macro_f1(payload_by_scenario: dict[str, dict]) -> dict[tuple[str, str, str], float]:
    """Return macro-F1 mean keyed by (scenario, dataset, protocol)."""
    out: dict[tuple[str, str, str], float] = {}
    for scenario, payload in payload_by_scenario.items():
        for entry in payload.get("best_models", []) or []:
            ds = entry.get("dataset")
            pr = entry.get("protocol")
            if ds and pr:
                out[(scenario, ds, pr)] = float(entry.get("macro_f1_mean", float("nan")))
    return out


def _f1_lookup_by_dataset_protocol(
    f1_full: dict[tuple[str, str, str], float], scenario: str
) -> dict[tuple[str, str], float]:
    return {(ds, pr): val for (sc, ds, pr), val in f1_full.items() if sc == scenario}


def main(argv: list[str] | None = None) -> int:
    args = _build_argparser().parse_args(argv)
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)s %(name)s | %(message)s",
    )

    baseline_payloads = _load_results(args.baseline_reports)
    if not baseline_payloads:
        LOGGER.error("No baseline ml_results JSON loaded from %s", args.baseline_reports)
        return 2

    overlap_payloads: dict[str, dict] = {}
    if args.overlap_reports is not None:
        overlap_payloads = _load_results(args.overlap_reports)
        if not overlap_payloads:
            LOGGER.warning(
                "No overlap ml_results JSON loaded from %s; paired Wilcoxon will be skipped",
                args.overlap_reports,
            )

    baseline_records: dict[tuple[str, str, str], CellRecord] = {}
    for scenario, payload in baseline_payloads.items():
        baseline_records.update(_build_cell_records(scenario, payload))

    overlap_records: dict[tuple[str, str, str], CellRecord] = {}
    for scenario, payload in overlap_payloads.items():
        overlap_records.update(_build_cell_records(scenario, payload))

    rng = np.random.default_rng(args.random_seed)
    n_cells_total = len(baseline_records) + len(overlap_records)
    bonferroni_threshold = 0.05 / max(1, n_cells_total)

    baseline_significance = _per_cell_significance(
        "6s_baseline",
        baseline_records,
        args.n_bootstrap,
        args.n_permutations,
        bonferroni_threshold,
        rng,
    )
    overlap_significance = (
        _per_cell_significance(
            "3s_overlap",
            overlap_records,
            args.n_bootstrap,
            args.n_permutations,
            bonferroni_threshold,
            rng,
        )
        if overlap_records
        else []
    )
    per_cell_dicts = [
        _cell_significance_to_dict(r) for r in baseline_significance + overlap_significance
    ]

    paired_summary: PairedComparison | None = None
    paired_dict: dict | None = None
    if baseline_records and overlap_records:
        f1_full_baseline = _resolve_paired_macro_f1(baseline_payloads)
        f1_full_overlap = _resolve_paired_macro_f1(overlap_payloads)
        # Run per-scenario lookups so that f1 values match the cells we paired.
        # We collapse to a single dict per profile because the public best_models
        # block already keys macro-F1 by (dataset, protocol) per scenario.
        paired_summary = _paired_overlap_vs_baseline(
            baseline_records,
            overlap_records,
            {(ds, pr): f1_full_baseline.get((sc, ds, pr), float("nan"))
             for (sc, ds, pr) in baseline_records.keys()},
            {(ds, pr): f1_full_overlap.get((sc, ds, pr), float("nan"))
             for (sc, ds, pr) in overlap_records.keys()},
        )
        paired_dict = paired_summary.__dict__.copy()

    hr_dict = _paired_hr_test(args.baseline_qc_summary)

    summary = {
        "n_bootstrap": args.n_bootstrap,
        "n_permutations": args.n_permutations,
        "random_seed": args.random_seed,
        "n_cells_total": n_cells_total,
        "bonferroni_threshold": bonferroni_threshold,
        "per_cell": per_cell_dicts,
        "per_cell_summary_counts": _summarise_counts(per_cell_dicts),
        "paired_overlap_vs_baseline": paired_dict,
        "hr_baseline_vs_task": hr_dict,
        "inputs": {
            "baseline_reports": str(args.baseline_reports),
            "overlap_reports": str(args.overlap_reports) if args.overlap_reports else None,
            "baseline_qc_summary": str(args.baseline_qc_summary) if args.baseline_qc_summary else None,
        },
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    with args.out_json.open("w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, default=float)
    _write_markdown(args.out_md, summary)

    LOGGER.info("Wrote %s and %s", args.out_json, args.out_md)
    if paired_summary is not None:
        LOGGER.info(
            "Paired Wilcoxon (3 s > 6 s): W=%.0f, p=%s, n=%d",
            paired_summary.wilcoxon_statistic,
            _format_p(paired_summary.wilcoxon_pvalue),
            paired_summary.paired_n,
        )
    LOGGER.info(
        "Per-cell counts: %s",
        json.dumps(summary["per_cell_summary_counts"]),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
ict(r) for r in baseline_significance + overlap_significance
    ]

    paired_summary: PairedComparison | None = None
    paired_dict: dict | None = None
    if baseline_records and overlap_records:
        f1_full_baseline = _resolve_paired_macro_f1(baseline_payloads)
        f1_full_overlap = _resolve_paired_macro_f1(overlap_payloads)
        paired_summary = _paired_overlap_vs_baseline(
            baseline_records,
            overlap_records,
            {(ds, pr): f1_full_baseline.get((sc, ds, pr), float("nan"))
             for (sc, ds, pr) in baseline_records.keys()},
            {(ds, pr): f1_full_overlap.get((sc, ds, pr), float("nan"))
             for (sc, ds, pr) in overlap_records.keys()},
        )
        paired_dict = paired_summary.__dict__.copy()

    hr_dict = _paired_hr_test(args.baseline_qc_summary)

    summary = {
        "n_bootstrap": args.n_bootstrap,
        "n_permutations": args.n_permutations,
        "random_seed": args.random_seed,
        "n_cells_total": n_cells_total,
        "bonferroni_threshold": bonferroni_threshold,
        "per_cell": per_cell_dicts,
        "per_cell_summary_counts": _summarise_counts(per_cell_dicts),
        "paired_overlap_vs_baseline": paired_dict,
        "hr_baseline_vs_task": hr_dict,
        "inputs": {
            "baseline_reports": str(args.baseline_reports),
            "overlap_reports": str(args.overlap_reports) if args.overlap_reports else None,
            "baseline_qc_summary": str(args.baseline_qc_summary) if args.baseline_qc_summary else None,
        },
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    with args.out_json.open("w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, default=float)
    _write_markdown(args.out_md, summary)

    LOGGER.info("Wrote %s and %s", args.out_json, args.out_md)
    if paired_summary is not None:
        LOGGER.info(
            "Paired Wilcoxon (3 s > 6 s): W=%.0f, p=%s, n=%d",
            paired_summary.wilcoxon_statistic,
            _format_p(paired_summary.wilcoxon_pvalue),
            paired_summary.paired_n,
        )
    LOGGER.info(
        "Per-cell counts: %s",
        json.dumps(summary["per_cell_summary_counts"]),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
ilcoxon_pvalue),
            paired_summary.paired_n,
        )
    LOGGER.info(
        "Per-cell counts: %s",
        json.dumps(summary["per_cell_summary_counts"]),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

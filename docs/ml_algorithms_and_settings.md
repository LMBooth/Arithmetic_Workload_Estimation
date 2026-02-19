# ML Algorithms and Settings

This document summarizes the exact Stage 6 training stack and the settings used in the current baseline runs.

## Core Training Script

- `analysis_pipeline/stage6_train_classic_ml.py`

## Fold-Safe Preprocessing Stack

Each outer/inner fold uses this pipeline order:

1. `SimpleImputer(strategy="median")`
2. `QuantileClipper(lower_q=0.01, upper_q=0.99)`
3. `RobustScaler(with_centering=True)`
4. `VarianceThreshold(threshold=0.0)`
5. optional feature selector
6. estimator

This is fit only on training folds to avoid leakage.

## Feature Selectors (Implemented)

- `none`
- `anova` -> `SelectPercentile(f_classif)` with percentile in `[25, 50, 75]`
- `mutual_info` -> `SelectPercentile(mutual_info_classif)` with percentile in `[25, 50, 75]`
- `l1` -> `SelectFromModel(LogisticRegression penalty="l1", solver="saga")` with threshold in `["mean", "median"]`
- `tree` -> `SelectFromModel(ExtraTreesClassifier)` with threshold in `["mean", "median"]`

Current baseline runs use `feature_selectors: ["none"]`.

## Classic Models and Search Spaces

Implemented classic models:

- `logreg`:
- estimator: balanced logistic regression
- grid: `C` in `[0.1, 1.0, 5.0, 10.0]`
- `svm`:
- estimator: RBF SVM with class balancing
- grid: `C` in `[0.5, 1.0, 3.0, 10.0]`, `gamma` in `["scale", "auto"]`
- `gaussian_nb`:
- grid: `var_smoothing` in `[1e-9, 1e-8, 1e-7]`
- `decision_tree`:
- grid: `criterion` in `[gini, entropy]`, `max_depth` in `[None, 8, 16, 24]`, `min_samples_leaf` in `[1, 2, 4]`
- `knn`:
- grid: `n_neighbors` in `[3, 5, 9, 13]`, `weights` in `[uniform, distance]`, `p` in `[1, 2]`
- `mlp`:
- grid: `hidden_layer_sizes` in `[(64,), (128,), (64, 32)]`, `alpha` in `[1e-4, 1e-3]`, `learning_rate_init` in `[1e-3, 5e-4]`
- `rf`:
- estimator: 400-tree balanced random forest
- grid: `max_depth` in `[None, 10, 20]`, `min_samples_leaf` in `[1, 2, 4]`, `max_features` in `["sqrt", 0.5]`

## Advanced Neural Models and Search Spaces

Implemented neural models (PyTorch):

- `lstm1d`
- `gru1d`
- `cnn1d`
- `transformer`
- `bilstm1d`
- `bigru1d`
- `cnn1d_deep`
- `transformer_xl`

Each model has a base config plus parameter grid sampled during tuning, for example:

- `lstm1d`: hidden_dim `[64, 96]`, n_layers `[1, 2]`, lr `[1e-3, 5e-4]`, dropout `[0.1, 0.2]`
- `bilstm1d`: hidden_dim `[96, 128]`, n_layers `[1, 2]`, lr `[1e-3, 5e-4]`, dropout `[0.2, 0.3]`
- `gru1d`: hidden_dim `[64, 96]`, n_layers `[1, 2]`, lr `[1e-3, 5e-4]`, dropout `[0.1, 0.2]`
- `bigru1d`: hidden_dim `[96, 128]`, n_layers `[1, 2]`, lr `[1e-3, 5e-4]`, dropout `[0.2, 0.3]`
- `cnn1d`: hidden_dim `[64, 96]`, lr `[1e-3, 5e-4]`, dropout `[0.1, 0.2]`
- `cnn1d_deep`: hidden_dim `[96, 128, 160]`, lr `[1e-3, 5e-4]`, dropout `[0.15, 0.25]`, weight_decay `[1e-4, 5e-4]`
- `transformer`: hidden_dim `[32, 64]`, n_layers `[1, 2]`, lr `[1e-3]`, dropout `[0.1]`
- `transformer_xl`: hidden_dim `[96, 128]`, n_heads `[4, 8]`, n_layers `[2, 3]`, lr `[1e-3, 5e-4]`, dropout `[0.1, 0.2]`

## Evaluation Protocols

Protocols:

- `loso` (`leave_one_participant_out`)
- `group_holdout`
- `within_participant`

Inner CV for tuning:

- `GroupKFold` for LOSO and group-holdout
- `StratifiedKFold` for within-participant

Metrics:

- `accuracy`
- `balanced_accuracy`
- `macro_f1`
- `weighted_f1`
- confusion matrix

## Tuning Budget Controls Used in Current Runs

The baseline runs use a quick-sweep budget:

- `inner_folds: 2`
- `max_param_combos: 2`
- `max_outer_splits_per_protocol: 2`

This means results are controlled comparisons, not full exhaustive grids.

## Baseline Scenario Configurations

Classic baseline config:

- `analysis_pipeline/config/pipeline_baseline_variants.yaml`
- models: classic only (`logreg`, `knn`, `svm`, `gaussian_nb`, `decision_tree`, `mlp`, `rf`)

Advanced baseline config:

- `analysis_pipeline/config/pipeline_baseline_advanced_nn.yaml`
- models: advanced NN only (`lstm1d`, `gru1d`, `cnn1d`, `transformer`, `bilstm1d`, `bigru1d`, `cnn1d_deep`, `transformer_xl`)

Shared class scenarios:

- `baseline_all_bins`
- `baseline_omit_hardest` (drop `6.0-6.9`)
- `baseline_low_high_omit_hardest` (low=`1-3`, high=`4-6`, keep baseline, drop hardest)
- `baseline_grouped_4class_omit_hardest` (low=`1-2`, mid=`3-4`, high=`5-6`, keep baseline, drop hardest)
- `baseline_omit_easiest` (drop `0.6-1.5`)

Both configs use:

- `baseline_from_tutorial_label: "baseline"`
- datasets: `eeg`, `ecg`, `pupil`, `fused`
- protocols: `loso`, `group_holdout`, `within_participant`

## GPU and Compute Notes

Device behavior in Stage 6:

- `--torch-device auto` selects CUDA when available, else CPU.
- Deep models use the selected torch device.
- CPU-heavy tree methods use `n_jobs=-1` for parallelism.

Observed run log (`analysis_pipeline/reports/run_logs/20260219T184306Z/stage6_ml_baseline_all_bins.stdout.log`):

- Torch available: `True`
- Torch device effective: `cuda`
- CUDA device: `NVIDIA GeForce RTX 4090`

There is no explicit user-level setting in this script for manual GPU stream/thread tuning; runtime scheduling is handled by PyTorch/CUDA.

## Confusion Matrix Export Settings

Script:

- `analysis_pipeline/stage6_highlight_confusions.py`

Current baseline configs use:

- `metric: balanced_accuracy_mean`
- `top_k_per_protocol: 1`
- `include_all: true` (export all model/protocol combinations)
- `label_order_strategy`: default is `baseline_first`
- PNG output root: `analysis_pipeline/reports/confusion_pngs`

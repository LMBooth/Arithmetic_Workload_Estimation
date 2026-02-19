# Exact Feature and ML Technique Reference

This document is an implementation-level reference for the current pipeline code and latest classic run artifacts.

## Scope

- Feature extraction code: `analysis_pipeline/stage4_extract_features.py`
- Fusion/split planning code: `analysis_pipeline/stage5_build_fused_table.py`
- ML training/evaluation code: `analysis_pipeline/stage6_train_classic_ml.py`
- Latest classic run outputs: `analysis_pipeline/reports/ml_results_all_bins.json`, `analysis_pipeline/reports/run_manifest.json`

## Feature Extraction: Exact Definitions

### EEG features
Implemented bands (`BANDS_HZ`):
- delta: 1-4 Hz
- theta: 4-8 Hz
- alpha: 8-13 Hz
- beta: 13-30 Hz
- highbeta: 30-40 Hz

Implemented ROIs (`ROI_CHANNELS`) plus global:
- frontal: `Fp1, Fp2, F3, F4, F7, F8, Fz`
- central: `C3, C4, Cz`
- parietal: `P3, P4, P7, P8, Pz`
- temporal: `T7, T8`
- occipital: `O1, O2`
- global: all channels

Per ROI feature families:
- absolute band power: `eeg_abs_<band>_<roi>`
- relative band power: `eeg_rel_<band>_<roi>`
- band ratios: `eeg_ratio_theta_alpha_<roi>`, `eeg_ratio_theta_beta_<roi>`, `eeg_ratio_alpha_beta_<roi>`
- time-domain summaries: `eeg_var_<roi>`, `eeg_rms_<roi>`, `eeg_mav_<roi>`, `eeg_line_length_<roi>`
- signal-magnitude summaries: `eeg_mean_power_<roi>`, `eeg_median_power_<roi>`
- waveform complexity counts: `eeg_zero_crossings_<roi>`, `eeg_zero_crossings_rate_<roi>`, `eeg_ssc_<roi>`, `eeg_ssc_rate_<roi>`
- Hjorth: `eeg_hjorth_activity_<roi>`, `eeg_hjorth_mobility_<roi>`, `eeg_hjorth_complexity_<roi>`
- spectral entropy: `eeg_spectral_entropy_<roi>`

Global EEG special features:
- `eeg_frontal_alpha_asymmetry_f4_minus_f3`
- `eeg_fz_theta_abs`
- `eeg_fz_theta_rel`

Baseline delta features:
- For theta/alpha/beta absolute powers by ROI, baseline-normalized deltas are added:
- `eeg_abs_<band>_<roi>_delta_base`

### ECG features
Peak/HRV feature families:
- `ecg_detected_peak_count`
- `ecg_valid_rr_count`
- `ecg_rr_coverage_ratio`
- `ecg_hr_mean_bpm`, `ecg_hr_median_bpm`, `ecg_hr_std_bpm`, `ecg_hr_min_bpm`, `ecg_hr_max_bpm`
- `ecg_rr_mean_ms`, `ecg_sdnn_ms`, `ecg_rmssd_ms`, `ecg_rr_iqr_ms`, `ecg_pnn50_pct`, `ecg_rr_cv`
- `ecg_nn50_count`
- baseline deltas: `ecg_hr_mean_bpm_delta_base`, `ecg_rmssd_ms_delta_base`
- quality label from feature extraction: `ecg_quality_flag` (string flag; not used as numeric predictor in Stage 6)

### Pupillometry features
Pupil size and dynamics:
- `pupil_valid_coverage_ratio`
- `pupil_mean`, `pupil_median`, `pupil_std`, `pupil_iqr`, `pupil_min`, `pupil_max`, `pupil_p10`, `pupil_p90`
- `pupil_slope_per_s`
- `pupil_peak_dilation`, `pupil_peak_time_s`, `pupil_tepr_latency_s`
- `pupil_auc_above_mean`
- `pupil_vel_mean_abs`, `pupil_vel_max_abs`
- `pupil_conf_mean`, `pupil_low_conf_ratio`
- baseline deltas: `pupil_mean_delta_base`, `pupil_peak_dilation_delta_base`

Gaze summaries:
- `gaze_x_mean`, `gaze_x_std`, `gaze_y_mean`, `gaze_y_std`, `gaze_path_length`

### Baseline reference policy
Per participant baseline window is the first valid 60 s before the first `started_arithmetic` marker.

## Exact Numeric Feature Columns Used by Stage 6 (Latest Classic Run)

Stage 6 excludes metadata columns, coerces remaining columns to numeric, and drops columns that are fully non-numeric/empty.

Generated column lists (latest run):
- EEG numeric features: `docs/tables/ml_numeric_feature_columns_eeg.csv` (141)
- ECG numeric features: `docs/tables/ml_numeric_feature_columns_ecg.csv` (16)
- Pupil numeric features: `docs/tables/ml_numeric_feature_columns_pupil.csv` (23)
- Fused numeric features: `docs/tables/ml_numeric_feature_columns_fused.csv` (180)

Prefix count summary:
- `docs/tables/ml_numeric_feature_prefix_counts.csv`

## Fusion and Split Construction

From `stage5_build_fused_table.py`:
- target: `difficulty_bin` mapped to `target_label`
- tutorial rows excluded by default (`include_tutorial=false` in current run)
- dropout policy used in current run: `absolute`, threshold `35.0`
- fused table requirement: all selected modalities present (`require_all_selected_modalities=true`)
- split manifest includes:
  - LOSO (`leave_one_participant_out`)
  - grouped holdout (default fractions 0.10 and 0.20, 5 repeats in manifest generation)
  - within-participant CV eligibility and recommended splits

## ML Techniques: Exact Pipeline

Stage 6 preprocessing stack (per fold, leak-safe):
1. `SimpleImputer(strategy='median')`
2. `QuantileClipper(lower_q=0.01, upper_q=0.99)` (defaults in current config)
3. `RobustScaler(with_centering=True)`
4. `VarianceThreshold(threshold=0.0)`
5. optional feature selector
6. estimator

Metrics:
- accuracy
- balanced_accuracy
- macro_f1
- weighted_f1
- confusion_matrix

## Models and Hyperparameter Grids (Implemented)

Classic models:
- `logreg` (`LogisticRegression`, class_weight balanced)
  - `C`: [0.1, 1.0, 5.0, 10.0]
- `svm` (`SVC`, RBF, class_weight balanced)
  - `C`: [0.5, 1.0, 3.0, 10.0]
  - `gamma`: [scale, auto]
- `gaussian_nb`
  - `var_smoothing`: [1e-9, 1e-8, 1e-7]
- `decision_tree` (class_weight balanced)
  - `criterion`: [gini, entropy]
  - `max_depth`: [None, 8, 16, 24]
  - `min_samples_leaf`: [1, 2, 4]
- `knn`
  - `n_neighbors`: [3, 5, 9, 13]
  - `weights`: [uniform, distance]
  - `p`: [1, 2]
- `mlp`
  - `hidden_layer_sizes`: [(64,), (128,), (64, 32)]
  - `alpha`: [1e-4, 1e-3]
  - `learning_rate_init`: [1e-3, 5e-4]
- `rf` (`RandomForestClassifier`, 400 trees, balanced_subsample)
  - `max_depth`: [None, 10, 20]
  - `min_samples_leaf`: [1, 2, 4]
  - `max_features`: [sqrt, 0.5]

Optional deep models (if torch installed):
- `lstm1d`, `gru1d`, `cnn1d`, `transformer`

## Feature Selectors (Implemented)

- `none` (default in current classic run)
- `anova`: `SelectPercentile(f_classif)` with percentile [25, 50, 75]
- `mutual_info`: `SelectPercentile(mutual_info_classif)` with percentile [25, 50, 75]
- `l1`: `SelectFromModel(LogisticRegression penalty='l1', solver='saga')`, threshold [mean, median]
- `tree`: `SelectFromModel(ExtraTreesClassifier)`, threshold [mean, median]

## Cross-Validation and Tuning Logic

- Protocols: `loso`, `group_holdout`, `within_participant`
- Inner CV for tuning:
  - group-aware inner CV (`GroupKFold`) for LOSO/group_holdout
  - stratified inner CV (`StratifiedKFold`) for within-participant
- Current pipeline config (`analysis_pipeline/config/pipeline.yaml`):
  - `inner_folds=2`
  - `max_param_combos=2` (sampled from full grid)
  - `max_outer_splits_per_protocol=2`

This means current outputs are controlled benchmark sweeps, not exhaustive full-grid runs.

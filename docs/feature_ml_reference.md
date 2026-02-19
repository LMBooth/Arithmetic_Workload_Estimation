# Feature Reference

This is the detailed feature-definition reference for the current extraction and ML tables.

Primary implementation:

- `analysis_pipeline/stage4_extract_features.py`
- `analysis_pipeline/stage5_build_fused_table.py`
- `analysis_pipeline/stage6_train_classic_ml.py`

## Current Feature Inventory (Docs Tables)

These tables were refreshed from the current tutorial-baseline ML tables:

- `analysis_pipeline/features/features_ml_eeg_tutorial_baseline.tsv`
- `analysis_pipeline/features/features_ml_ecg_tutorial_baseline.tsv`
- `analysis_pipeline/features/features_ml_pupil_tutorial_baseline.tsv`
- `analysis_pipeline/features/features_fused_tutorial_baseline.tsv`

Column inventories:

- EEG feature columns: `docs/tables/ml_feature_columns_eeg.csv` (183)
- ECG feature columns: `docs/tables/ml_feature_columns_ecg.csv` (18)
- Pupil feature columns: `docs/tables/ml_feature_columns_pupil.csv` (25)
- Fused feature columns: `docs/tables/ml_feature_columns_fused.csv` (226)

Numeric feature inventories used by Stage 6:

- EEG numeric features: `docs/tables/ml_numeric_feature_columns_eeg.csv` (183)
- ECG numeric features: `docs/tables/ml_numeric_feature_columns_ecg.csv` (17)
- Pupil numeric features: `docs/tables/ml_numeric_feature_columns_pupil.csv` (25)
- Fused numeric features: `docs/tables/ml_numeric_feature_columns_fused.csv` (225)

Prefix summaries:

- All feature prefixes: `docs/tables/ml_feature_prefix_counts.csv`
- Numeric feature prefixes: `docs/tables/ml_numeric_feature_prefix_counts.csv`

## Baseline Policy

Baseline features are computed per participant from the first valid 60 seconds before first `started_arithmetic`.

Baseline range fields are carried as:

- `baseline_start_s`
- `baseline_end_s`

Baseline-delta columns are suffixed with `_delta_base`.

## EEG Features

Bands:

- delta: `1-4 Hz`
- theta: `4-8 Hz`
- alpha: `8-13 Hz`
- beta: `13-30 Hz`
- highbeta: `30-40 Hz`

ROIs:

- frontal, central, parietal, temporal, occipital, global

### EEG feature families and naming

- Absolute band power: `eeg_abs_<band>_<roi>` (30 columns)
- Relative band power: `eeg_rel_<band>_<roi>` (30 columns)
- Baseline deltas on absolute theta/alpha/beta: `eeg_abs_<band>_<roi>_delta_base` (18 columns)
- Band ratios:
- `eeg_ratio_theta_alpha_<roi>`
- `eeg_ratio_theta_beta_<roi>`
- `eeg_ratio_alpha_beta_<roi>` (18 columns)
- Time-domain summaries:
- `eeg_var_<roi>`
- `eeg_rms_<roi>`
- `eeg_mav_<roi>`
- `eeg_mean_power_<roi>`
- `eeg_median_power_<roi>`
- `eeg_line_length_<roi>` (36 columns)
- Waveform complexity/count features:
- `eeg_zero_crossings_<roi>`
- `eeg_zero_crossings_rate_<roi>`
- `eeg_ssc_<roi>`
- `eeg_ssc_rate_<roi>` (24 columns)
- Hjorth features:
- `eeg_hjorth_activity_<roi>`
- `eeg_hjorth_mobility_<roi>`
- `eeg_hjorth_complexity_<roi>` (18 columns)
- Spectral entropy: `eeg_spectral_entropy_<roi>` (6 columns)
- Frontal asymmetry and Fz theta:
- `eeg_frontal_alpha_asymmetry_f4_minus_f3`
- `eeg_fz_theta_abs`
- `eeg_fz_theta_rel` (3 columns)

## ECG Features

ECG peak/HRV features are extracted from `cardiac_peak` epochs.

Feature list:

- `ecg_detected_peak_count`
- `ecg_valid_rr_count`
- `ecg_rr_coverage_ratio`
- `ecg_hr_mean_bpm`
- `ecg_hr_median_bpm`
- `ecg_hr_std_bpm`
- `ecg_hr_min_bpm`
- `ecg_hr_max_bpm`
- `ecg_rr_mean_ms`
- `ecg_sdnn_ms`
- `ecg_rmssd_ms`
- `ecg_rr_iqr_ms`
- `ecg_nn50_count`
- `ecg_pnn50_pct`
- `ecg_rr_cv`
- `ecg_hr_mean_bpm_delta_base`
- `ecg_rmssd_ms_delta_base`
- `ecg_quality_flag` (string, non-numeric; dropped from numeric model matrix)

## Pupil and Gaze Features

Pupil features:

- Coverage/quality:
- `pupil_valid_coverage_ratio`
- `pupil_conf_mean`
- `pupil_low_conf_ratio`
- Distribution:
- `pupil_mean`
- `pupil_median`
- `pupil_std`
- `pupil_iqr`
- `pupil_min`
- `pupil_max`
- `pupil_p10`
- `pupil_p90`
- Dynamics and response:
- `pupil_slope_per_s`
- `pupil_peak_dilation`
- `pupil_peak_time_s`
- `pupil_tepr_latency_s`
- `pupil_auc_above_mean`
- `pupil_vel_mean_abs`
- `pupil_vel_max_abs`
- Baseline deltas:
- `pupil_mean_delta_base`
- `pupil_peak_dilation_delta_base`

Gaze features:

- `gaze_x_mean`
- `gaze_x_std`
- `gaze_y_mean`
- `gaze_y_std`
- `gaze_path_length`

## Fused Table Features

The fused table concatenates selected modality feature sets on aligned epoch keys.

Current fused feature set composition:

- EEG-prefixed features: 183
- ECG-prefixed features: 18
- Pupil-prefixed features: 20
- Gaze-prefixed features: 5
- Total: 226

Stage 6 numeric coercion drops only non-numeric feature columns, yielding 225 numeric fused predictors in the current baseline runs.

## Exact Column Lists

Use these files for exact, ordered column references:

- `docs/tables/ml_feature_columns_eeg.csv`
- `docs/tables/ml_feature_columns_ecg.csv`
- `docs/tables/ml_feature_columns_pupil.csv`
- `docs/tables/ml_feature_columns_fused.csv`
- `docs/tables/ml_numeric_feature_columns_eeg.csv`
- `docs/tables/ml_numeric_feature_columns_ecg.csv`
- `docs/tables/ml_numeric_feature_columns_pupil.csv`
- `docs/tables/ml_numeric_feature_columns_fused.csv`

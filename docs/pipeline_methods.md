# Pipeline Methods (ML Psychology Focus)

This document describes the end-to-end analysis used to estimate cognitive workload resolution from physiological signals (EEG, ECG, pupil).

## Data Source and Scope

- Input is a BIDS-formatted arithmetic task dataset.
- This repository is analysis-only and should remain separate from the BIDS data-descriptor repository used for data publication.
- Modalities: EEG, ECG, pupil.

## Stage-by-Stage Process

1. Trial table construction (`build_trial_table.py`)
- Converts BIDS event markers into canonical trial rows.
- Stores aligned timing for:
  - `calc_start_s` to `calc_end_s`
  - `answer_start_s` to `answer_end_s`
- Preserves per-trial metadata (difficulty, correctness, tutorial/main block labels).

2. QC (`stage1_qc_summary.py`)
- Quantifies coverage and quality by participant and modality before preprocessing.
- Generates machine-readable summaries and figures.

3. Preprocessing (`stage2_preprocess.py`)
- EEG: filtering, channel handling, rereferencing, optional ICA.
- ECG: cleaned cardiac trace and peaks.
- Pupil: confidence-aware cleaning and interpolation.

4. Epoching (`stage3_epoch_trials.py`)
- Uses trial table windows only (no ad hoc marker parsing at this stage).
- Benchmark default:
  - `window_mode=calc_fixed`
  - `fixed_window_s=6.0`
- This explicitly models the 6-second arithmetic presentation window.

### From 6-second trials to more epochs

- Baseline benchmark: one epoch per trial (no overlap), minimizing leakage risk.
- Optional segmentation mode:
  - `--sliding-window-s <length>`
  - `--sliding-step-s <step>`
  - `--allow-overlap` (if required)
- In segmented mode, multiple sub-windows are produced from one parent trial.
- All sub-windows from the same trial should remain in the same outer CV fold.

5. Feature extraction (`stage4_extract_features.py`)
- Trial/epoch-level unimodal features:
  - EEG spectral + temporal descriptors
  - ECG HR/RR variability descriptors
  - Pupil dynamics, confidence, and gaze summaries
- Writes unimodal tables with provenance fields.

6. Fused table and split manifest (`stage5_build_fused_table.py`)
- Aligns unimodal features into a fused table.
- Builds split plans for:
  - LOSO
  - Group holdout
  - Within-participant

7. ML benchmarking (`stage6_train_classic_ml.py`)
- Trains and evaluates across modalities and protocols.
- Reports per-split and aggregated metrics:
  - accuracy
  - balanced accuracy
  - macro/weighted F1
  - confusion matrices

## Class-Resolution Comparisons

For comparing binary/4-class/7-class/8-class setups, use chance-adjusted balanced accuracy:

`cBA = (BA - 1/K) / (1 - 1/K)`

- `K` is class count.
- `cBA=0` is chance-level.
- `cBA=1` is perfect.

This allows fairer comparison of workload resolution across different label granularities.

## Reproducibility

- Run via `run_pipeline.py` with pinned YAML config.
- Save output manifests from `analysis_pipeline/reports/`.
- Keep dataset and analysis repos separate for publication hygiene.

## Exact Technical Reference

For explicit implementation details (exact feature families, exact numeric feature columns used in the latest run, exact model/search spaces, and CV/tuning logic), see:

- `docs/feature_ml_reference.md`
- `docs/tables/ml_numeric_feature_columns_eeg.csv`
- `docs/tables/ml_numeric_feature_columns_ecg.csv`
- `docs/tables/ml_numeric_feature_columns_pupil.csv`
- `docs/tables/ml_numeric_feature_columns_fused.csv`
- `docs/tables/ml_numeric_feature_prefix_counts.csv`

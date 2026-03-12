# Pipeline Reference

This document explains how the checked-in pipeline profiles map to the executable code, runtime behavior, and output structure.

## Canonical entry points

- `analysis_pipeline/run_pipeline.py`
- `analysis_pipeline/config/pipeline_unified_classic_nn_baseline_preproc.yaml`
- `analysis_pipeline/config/pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc.yaml`
- `scripts/download_bids.py`
- `scripts/run_end_to_end.ps1`

## Execution model

`run_pipeline.py` reads a YAML profile, expands output placeholders, plans the enabled stages, executes them in order, verifies expected outputs, and writes a run manifest with commands, logs, and output checks.

Important runtime behavior:

- `outputs.root` defines a dedicated run directory. The checked-in profiles write to `analysis_pipeline/runs/<profile_name>/`.
- `outputs.clean_start: true` removes that dedicated run directory before the run starts. The orchestrator explicitly refuses to clean the repository root, the source tree, or an ancestor of the source tree.
- Expected output paths and globs are verified after every step. Use `--no-strict-outputs` only for debugging partial runs.
- If Stage 1 strict QC is active, the subject carry-forward list is applied automatically to Stages 2 to 5.
- If `--only stage6` is passed, `stage6_confusions` is auto-included unless `--no-auto-stage6-confusions` is used.
- `--dry-run` prints the planned commands and expected outputs without executing any stage.

## Checked-in profiles

| Profile | Config file | Key differences |
| --- | --- | --- |
| Fixed-window baseline | `analysis_pipeline/config/pipeline_unified_classic_nn_baseline_preproc.yaml` | Stage 3 uses `window_mode=calc_fixed` with `fixed_window_s=6.0`. |
| Overlap-window baseline | `analysis_pipeline/config/pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc.yaml` | Stage 3 uses `sliding_window_s=3.0`, `sliding_step_s=1.5`, `allow_overlap=true`, and `min_ecg_window_s=3.0`. |

Common settings across both profiles:

- BIDS root: `./data/bids_arithmetic`
- Stage 1 strict QC enabled
- Stage 2 EEG preprocessing uses a Butterworth pipeline with `eeg_l_freq=2.0` and `eeg_h_freq=40.0`
- Stage 5 builds `features_fused_tutorial_baseline.tsv` and `split_manifest_tutorial_baseline.json`
- Stage 6 benchmarks `eeg`, `ecg`, `pupil`, and `fused`
- Stage 6 evaluates `pooled_stratified`, `group_holdout`, and `within_participant`
- Stage 6 sweeps classic models plus optional deep models
- Stage 6 confusions and publication report generation are enabled

## Stage-by-stage reference

### Stage 0: Trial table

Script: `analysis_pipeline/build_trial_table.py`

Purpose:

- Read BIDS `events.tsv` files
- Build one canonical trial table across participants
- Derive calculation and answer window timing metadata
- Preserve per-trial dropped-sample counts when present in the event rows

Primary outputs:

- `<run_root>/reports/trial_table_bids_arithmetic.tsv`
- `<run_root>/reports/trial_table_bids_arithmetic_summary.json`

### Stage 1: QC summary

Script: `analysis_pipeline/stage1_qc_summary.py`

Purpose:

- Inspect EEG, ECG, and pupil availability before cleaning
- Summarize dropped samples and modality coverage
- Apply optional strict participant rejection thresholds
- Emit participant-level and dataset-level QC summaries

Primary outputs:

- `<run_root>/reports/qc_subject_table.tsv`
- `<run_root>/reports/qc_dataset_summary.json`
- `<run_root>/reports/participant_bids_sample_drop_summary.csv`
- `<run_root>/reports/figures/*.png`

### Stage 2: Preprocessing

Script: `analysis_pipeline/stage2_preprocess.py`

Purpose:

- Clean EEG, ECG, and pupil time series
- Normalize EEG units when needed
- Support EEG filtering, optional interpolation, and optional ICA
- Filter ECG streams and prepare downstream peak and HR extraction inputs
- Smooth and resample pupil traces for downstream feature extraction

Primary outputs:

- `<run_root>/derivatives/cleaned/<participant>/...`
- `<run_root>/reports/preprocess_log.tsv`
- `<run_root>/reports/preprocess_summary.json`

### Stage 3: Epoching

Script: `analysis_pipeline/stage3_epoch_trials.py`

Purpose:

- Convert trial windows into epoch segments for ML
- Support fixed windows and overlapping subwindows
- Enforce EEG, ECG, and pupil drop rules at the epoch level
- Prefer exact dropped-sample counts from `events.tsv` when available

Primary outputs:

- `<run_root>/derivatives/epochs/<participant>/...`
- `<run_root>/reports/epoch_manifest.tsv`
- `<run_root>/reports/epoch_summary.json`
- `<run_root>/reports/epoch_drop_log.tsv`
- `<run_root>/reports/participant_sample_capture_drop_summary.csv`
- `<run_root>/reports/figures/segmentation_dropped_windows_due_missing_samples_eeg_ecg.png`

### Stage 4: Feature extraction

Script: `analysis_pipeline/stage4_extract_features.py`

Purpose:

- Extract unimodal engineered features from the Stage 3 epochs
- Compute EEG band-power features by ROI
- Derive ECG summary statistics such as heart-rate variability features
- Derive pupil summary features such as dilation magnitude and variability

Primary outputs:

- `<run_root>/features/features_eeg.tsv`
- `<run_root>/features/features_ecg.tsv`
- `<run_root>/features/features_pupil.tsv`
- `<run_root>/reports/feature_summary.json`

### Stage 5: Fused-table assembly

Script: `analysis_pipeline/stage5_build_fused_table.py`

Purpose:

- Combine unimodal feature tables into ML-ready unimodal and fused datasets
- Apply modality dropout rules
- Build split manifests for Stage 6 protocols
- Write verification summaries describing subject and row retention

Primary outputs:

- `<run_root>/features/features_fused_tutorial_baseline.tsv`
- `<run_root>/features/split_manifest_tutorial_baseline.json`
- `<run_root>/reports/fusion_summary_tutorial_baseline.json`
- `<run_root>/reports/fusion_verification_tutorial_baseline.json`
- `<run_root>/reports/fusion_verification_tutorial_baseline.md`

### Stage 6: Split-aware ML benchmarking

Script: `analysis_pipeline/stage6_train_classic_ml.py`

Purpose:

- Evaluate dataset, protocol, and class-scenario combinations from the Stage 5 split manifest
- Run classic sklearn models and optional PyTorch sequence models
- Emit aggregate metrics, best-model summaries, and scenario markdown summaries
- Optionally emit per-evaluation confusion PNGs and EEG PSD/topomap QC figures

Default preprocessing stack inside classic pipelines:

1. Median imputation
2. Quantile clipping
3. Robust scaling
4. Zero-variance filtering
5. Optional feature selector
6. Estimator

Primary outputs:

- `<run_root>/reports/ml_results_<scenario>_classic_nn.json`
- `<run_root>/reports/ml_summary_<scenario>_classic_nn.md`
- `<run_root>/models/...`
- `<run_root>/reports/confusion_pngs_live/<scenario>/...`
- `<run_root>/reports/eeg_condition_psd/<scenario>/...`

The checked-in configs define these class scenarios:

- `baseline_all_bins`
- `baseline_omit_easiest`
- `baseline_omit_hardest`
- `baseline_low_high_omit_hardest`
- `baseline_grouped_4class_omit_hardest`

### Stage 6 post-processing

Confusion curation:

- Script: `analysis_pipeline/stage6_highlight_confusions.py`
- Outputs: `<run_root>/reports/confusion_highlights_<scenario>_classic_nn.json`, markdown, and PNGs

Report-asset aggregation:

- Script: `analysis_pipeline/stage6_build_report_assets.py`
- Purpose: aggregate multiple Stage 6 results and confusion selections into tables and figures

Publication report:

- Script: `analysis_pipeline/stage6_build_publication_report.py`
- Outputs: `<run_root>/reports/publication_full_report.md` and `.json`

## YAML structure

The orchestrator consumes these top-level sections:

- `paths`
  Runtime paths such as `bids_root` and `python_executable`.
- `outputs`
  Dedicated run root and cleanup policy.
- `reports`
  Optional explicit run-manifest path.
- `stages`
  Boolean toggles for Stage 0 through Stage 6 post-processing.
- `stage_args`
  Per-stage CLI arguments for Stages 0 to 5.
- `stage6`
  Stage 6 templates, shared arguments, and class-scenario definitions.
- `stage6_confusions`
  Confusion-selection templates and arguments.
- `stage6_publication_report`
  Publication-report arguments and output paths.

Available output placeholders:

- `{output_root}`
- `{reports_dir}`
- `{features_dir}`
- `{models_dir}`
- `{cleaned_dir}`
- `{epochs_dir}`

Under `stage_args.<stage_name>`, keys map directly to CLI flags by converting underscores to hyphens. For example, `fixed_window_s` becomes `--fixed-window-s`.

## Common commands

Full run with the default profile:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml
```

Dry run:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml `
  --dry-run
```

Run only Stage 6 for selected scenarios:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml `
  --only stage6 `
  --stage6-scenarios baseline_all_bins baseline_omit_hardest
```

Run Stage 6 without auto-running confusion selection:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml `
  --only stage6 `
  --no-auto-stage6-confusions
```

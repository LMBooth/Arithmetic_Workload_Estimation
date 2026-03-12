# Analysis Pipeline Package

This directory contains the executable stages, config profiles, and supporting modules that drive the end-to-end workload analysis workflow.

## Canonical entry points

- `run_pipeline.py`: orchestrates configured runs, output verification, and run manifests.
- `config/pipeline_unified_classic_nn_baseline_preproc.yaml`: default fixed-window profile.
- `config/pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc.yaml`: overlap-window profile.
- `../scripts/run_end_to_end.ps1`: dataset download plus pipeline execution.

## Stage scripts

1. `build_trial_table.py`
   Builds the canonical trial table from BIDS events and writes stage-level trial metadata.
2. `stage1_qc_summary.py`
   Produces participant-level QC tables, dropped-sample summaries, and modality coverage figures.
3. `stage2_preprocess.py`
   Cleans EEG, ECG, and pupil recordings and writes preprocessed derivatives.
4. `stage3_epoch_trials.py`
   Segments trials into fixed or overlapping epochs and records dropped-window accounting.
5. `stage4_extract_features.py`
   Extracts modality-specific engineered features for EEG, ECG, and pupil.
6. `stage5_build_fused_table.py`
   Builds fused and unimodal ML tables, split manifests, and verification summaries.
7. `stage6_train_classic_ml.py`
   Runs split-aware benchmarking for classic and optional deep models and can emit live confusion PNGs plus EEG PSD/topomap QC figures.
8. `stage6_highlight_confusions.py`
   Curates confusion matrices from Stage 6 result JSON files.
9. `stage6_build_report_assets.py`
   Aggregates Stage 6 results and confusion selections into tables and publication figures.
10. `stage6_build_publication_report.py`
    Builds the run-level publication report snapshot.

Supporting modules:

- `eeg_condition_psd.py`: Stage 6 EEG PSD and topomap report generation.
- `eeg_units.py`: EEG unit normalization helpers.

## Output layout

When the checked-in YAML profiles are used through `run_pipeline.py`, outputs are written under:

- `analysis_pipeline/runs/<profile_name>/derivatives/`
- `analysis_pipeline/runs/<profile_name>/features/`
- `analysis_pipeline/runs/<profile_name>/models/`
- `analysis_pipeline/runs/<profile_name>/reports/`

If the stage scripts are run directly without an output-root override, their legacy defaults still point at the top-level local folders:

- `analysis_pipeline/derivatives/`
- `analysis_pipeline/features/`
- `analysis_pipeline/models/`
- `analysis_pipeline/reports/`

## Runtime behavior

- The orchestrator prints planned steps, expected outputs, and per-step verification.
- By default, missing expected outputs fail the run even if a stage exits with code `0`.
- Stage 1 strict QC carry-forward is applied automatically to Stages 2 to 5.
- Running `--only stage6` through the orchestrator auto-runs confusion generation unless `--no-auto-stage6-confusions` is set.

See `../docs/pipeline_reference.md` for the detailed pipeline reference and `../docs/reproducibility.md` for artifact and handoff guidance.

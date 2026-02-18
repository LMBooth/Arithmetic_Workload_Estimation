# Analysis Pipeline

This folder contains the staged multimodal workload analysis workflow.

## Stages

1. `build_trial_table.py`
- Parses BIDS events into one canonical trial table.
- Defines `calc_start_s`, `calc_end_s`, `answer_start_s`, `answer_end_s`, and trial metadata.

2. `stage1_qc_summary.py`
- Produces dataset and modality quality summaries before cleaning.

3. `stage2_preprocess.py`
- Cleans EEG, ECG, and pupil streams and writes preprocessed derivatives.

4. `stage3_epoch_trials.py`
- Converts trial windows into epochs for ML.
- Default benchmark uses fixed 6-second calculation windows (`window_mode=calc_fixed`, `fixed_window_s=6.0`).
- Optional segmentation can generate multiple sub-windows per trial with fixed step sizes.

5. `stage4_extract_features.py`
- Extracts modality-specific features from epochs.
- Outputs unimodal feature tables for EEG, ECG, and pupil.

6. `stage5_build_fused_table.py`
- Builds fused and unimodal ML-ready tables and split manifests.

7. `stage6_train_classic_ml.py`
- Runs split-aware model benchmarking (`loso`, `group_holdout`, `within_participant`).

## Entrypoint

Use `run_pipeline.py` with a YAML config:

```powershell
python .\analysis_pipeline\run_pipeline.py --config .\analysis_pipeline\config\pipeline.yaml
```

## Default Outputs

- `analysis_pipeline/derivatives/`
- `analysis_pipeline/features/`
- `analysis_pipeline/models/`
- `analysis_pipeline/reports/`

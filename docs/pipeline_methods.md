# Pipeline Methods

This is the implementation-level reference for the end-to-end workload pipeline in `analysis_pipeline/`.

## Entrypoint and Stage Order

Use:

```bash
python analysis_pipeline/run_pipeline.py --config analysis_pipeline/config/pipeline.yaml
```

The orchestrator runs stages in this order:

1. `stage0` -> `build_trial_table.py`
2. `stage1` -> `stage1_qc_summary.py`
3. `stage2` -> `stage2_preprocess.py`
4. `stage3` -> `stage3_epoch_trials.py`
5. `stage4` -> `stage4_extract_features.py`
6. `stage5` -> `stage5_build_fused_table.py`
7. `stage6` -> `stage6_train_classic_ml.py`
8. `stage6_confusions` -> `stage6_highlight_confusions.py`

Each executed step writes stdout/stderr logs under `analysis_pipeline/reports/run_logs/<timestamp>/` and writes a manifest JSON (`run_manifest*.json`) with command lines, outputs, and return codes.

## Stage 0: Canonical Trial Table

Script: `analysis_pipeline/build_trial_table.py`

Main behavior:

- Parses BIDS events and pairs cue markers with outcome markers.
- Builds canonical timing columns per trial:
- `calc_start_s`, `calc_end_s`
- `answer_start_s`, `answer_end_s`
- Calculates dropped-sample summaries:
- `dropped_samples_calc`
- `dropped_samples_answer`
- `dropped_samples_trial`
- Carries task metadata:
- tutorial/main block
- difficulty bin/range
- response accuracy and outcome

Main output:

- `analysis_pipeline/reports/trial_table_<bids_root_name>.tsv`

## Stage 1: Dataset QC and Sanity Checks

Script: `analysis_pipeline/stage1_qc_summary.py`

Main behavior:

- Computes per-subject modality availability and quality summaries.
- ECG quality checks:
- ECG sample count/range
- peak detection stability
- physiological HR range checks
- baseline minute vs task HR windows
- Pupil quality checks:
- confidence distributions
- missing confidence and nonpositive pupil size
- Event-table checks:
- cue/outcome counts
- arithmetic start/finish marker counts
- Builds anomaly lists per subject and overall.

Main outputs:

- `analysis_pipeline/reports/qc_subject_table.tsv`
- `analysis_pipeline/reports/qc_dataset_summary.json`
- `analysis_pipeline/reports/figures/*.png`

## Stage 2: Modality Preprocessing

Script: `analysis_pipeline/stage2_preprocess.py`

### EEG preprocessing

- Reads BrainVision EEG.
- Optional notch filter at `--eeg-notch-hz` (default `50.0`).
- Band-pass filter `--eeg-l-freq` to `--eeg-h-freq` (defaults `1.0` to `40.0`).
- Detects bad channels by robust channel-level variance criteria.
- Applies 10-20 channel alias normalization and montage.
- Optional bad-channel interpolation (enabled by default).
- Sets average EEG reference.
- Optional ICA (`--run-ica`) with ECG-correlated component exclusion.

### ECG preprocessing

- Reads ECG physio series.
- Creates two filtered traces:
- broad band (`0.5-40.0` Hz by default)
- peak band (`5.0-25.0` Hz by default)
- Detects peaks and writes HR summary metadata.

### Pupil preprocessing

- Applies confidence threshold mask (`--pupil-conf-threshold`, default `0.60`).
- Interpolates invalid segments for pupil/x/y/confidence.
- Smooths with moving-average window (`--pupil-smooth-seconds`, default `0.20`).
- Resamples to `--pupil-target-sfreq` (default `100.0` Hz).

Main outputs:

- `analysis_pipeline/derivatives/cleaned/<sub>/...`
- `analysis_pipeline/reports/preprocess_log.tsv`
- `analysis_pipeline/reports/preprocess_summary.json`

## Stage 3: Epoching, Windowing, and Filtering

Script: `analysis_pipeline/stage3_epoch_trials.py`

This stage controls how continuous time series become model epochs.

### Parent trial window selection

`--window-mode` options:

- `calc_fixed` (default): `[calc_start_s, calc_start_s + fixed_window_s]`, default `fixed_window_s=6.0`
- `full_trial`: `[calc_start_s, answer_end_s]`
- `answer_only`: `[answer_start_s, answer_end_s]`

### Optional sliding sub-windowing

- If `--sliding-window-s` is not set: one epoch per trial window.
- If set:
- window length = `sliding_window_s`
- step = `sliding_step_s` (or equals window length if omitted)
- overlap requires `--allow-overlap`
- short parent windows can be dropped (`--drop-short-windows`, default true) or kept (`--keep-short-windows`)

### Dropped-sample handling and gating

- Source columns come from Stage 0 (`dropped_samples_calc`, `dropped_samples_answer`, `dropped_samples_trial`).
- `--dropped-samples-source auto` maps by window mode:
- `calc_fixed -> calc`
- `answer_only -> answer`
- `full_trial -> trial`
- Optional segment scaling is enabled by default:
- `segment_used = source_value * (segment_duration / parent_duration)`
- Threshold gates:
- `--max-dropped-samples-eeg`
- `--max-dropped-samples-ecg`

### Coverage and keep/drop logic

- Minimum coverage threshold `--min-coverage` (default `0.80`).
- EEG drops for:
- missing input
- too few samples
- low coverage
- dropped-samples threshold exceedance
- ECG drops for:
- missing input
- short window (if enabled, default min ECG window `4.0s`)
- too few samples
- low coverage
- dropped-samples threshold exceedance
- Pupil drops for:
- missing input
- too few samples
- low effective coverage after valid-sample masking

### Stage 3 outputs

- Per-epoch NPZ files by modality.
- Global manifest and drop logs:
- `analysis_pipeline/reports/epoch_manifest.tsv`
- `analysis_pipeline/reports/epoch_drop_log.tsv`
- `analysis_pipeline/reports/epoch_summary.json`

## Stage 4: Feature Extraction

Script: `analysis_pipeline/stage4_extract_features.py`

Main behavior:

- Loads epoch manifest and modality NPZ epochs.
- Computes per-epoch unimodal features (EEG, ECG, pupil/gaze).
- Computes per-subject baseline features from the first valid 60s before first `started_arithmetic`.
- Adds baseline-delta features for selected EEG/ECG/pupil metrics.

Outputs:

- `analysis_pipeline/features/features_eeg.tsv`
- `analysis_pipeline/features/features_ecg.tsv`
- `analysis_pipeline/features/features_pupil.tsv`
- `analysis_pipeline/reports/feature_summary.json`

## Stage 5: Fusion and Split Planning

Script: `analysis_pipeline/stage5_build_fused_table.py`

Main behavior:

- Builds unimodal ML tables and fused multimodal table.
- Applies tutorial inclusion/exclusion (`--include-tutorial`).
- Applies dropout policy:
- `none`
- `absolute` (`--dropout-threshold`, default `35.0`)
- `subject_percentile` (`--dropout-percentile`, default `95.0`)
- Builds split manifest for:
- LOSO
- grouped holdout
- within-participant planning
- Optionally requires full modality intersection for fused rows (default true).

Outputs:

- `analysis_pipeline/features/features_ml_<modality>*.tsv`
- `analysis_pipeline/features/features_fused*.tsv`
- `analysis_pipeline/features/split_manifest*.json`
- `analysis_pipeline/reports/fusion_summary*.json`

## Stage 6: ML Training and Evaluation

Script: `analysis_pipeline/stage6_train_classic_ml.py`

Main behavior:

- Reads split manifest and dataset tables.
- Applies class scenario mapping (include/drop/merge labels).
- Uses leakage-safe preprocessing per fold:
- median imputation
- quantile clipping
- robust scaling
- zero-variance filter
- optional feature selector
- model fitting
- Evaluates by protocol:
- `loso`
- `group_holdout`
- `within_participant`

Core metric outputs:

- accuracy
- balanced accuracy
- macro F1
- weighted F1
- confusion matrix

Outputs:

- `analysis_pipeline/reports/ml_results_*.json`
- `analysis_pipeline/reports/ml_summary_*.md`
- `analysis_pipeline/models/stage6_<timestamp>_<tag>/...`

## Stage 6 Confusions: Highlight and PNG Export

Script: `analysis_pipeline/stage6_highlight_confusions.py`

Main behavior:

- Selects aggregate pipelines (top-k or all).
- Aggregates confusion matrices over outer splits.
- Reorders labels with `--label-order-strategy` (default `baseline_first`).
- Writes markdown + JSON highlight summaries.
- Renders per-model confusion PNGs to organized folders.

Outputs:

- `analysis_pipeline/reports/confusion_highlights_*.json`
- `analysis_pipeline/reports/confusion_highlights_*.md`
- `analysis_pipeline/reports/confusion_pngs/<results_name>/<dataset>/<protocol>/<pipeline>.png`

## Progress Checkpoints and Monitoring

Progress print statements are built into all stages:

- Stage 2 prints per-subject modality status.
- Stage 3 prints per-subject trial counts and completion summaries.
- Stage 4 prints baseline progress and periodic epoch extraction checkpoints.
- Stage 5 prints per-modality table-building status.
- Stage 6 prints dataset/protocol/split/model sweep checkpoints and selected runtime device.
- `run_pipeline.py` prints step-level status and elapsed seconds.

## Related Docs

- Features: `docs/feature_ml_reference.md`
- ML settings: `docs/ml_algorithms_and_settings.md`
- Outcomes: `docs/ml_outcomes.md`

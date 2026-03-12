# Physiological Workload ML Pipeline

Analysis repository for the OpenNeuro study [`ds007262` version `1.0.6`](https://openneuro.org/datasets/ds007262/versions/1.0.6), titled `Cognitive Workload 8-level arithmetic` (DOI `10.18112/openneuro.ds007262.v1.0.6`). The codebase covers dataset acquisition, trial-table construction, QC, preprocessing, epoching, unimodal feature extraction, fused-table assembly, split-aware machine learning, confusion analysis, and publication-oriented reporting for this specific study snapshot.

## Repository layout

- `analysis_pipeline/`: executable stage scripts, pipeline configs, and supporting modules.
- `analysis_pipeline/config/`: checked-in YAML profiles for reproducible runs.
- `scripts/`: dataset download, end-to-end execution, and report/manuscript helpers.
- `docs/`: GitHub-facing documentation plus manuscript handoff material.
- `data/`: local BIDS dataset root (ignored).
- `analysis_pipeline/runs/`: run-specific outputs (ignored).

This repository is intentionally separate from the OpenNeuro dataset record itself. Track code, configs, and documentation here; keep raw data and generated outputs local.

## Quick start

### 1. Create the environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`requirements.txt` covers the classic ML and signal-processing stack. Install PyTorch separately if you plan to run deep Stage 6 models such as `lstm1d`, `gru1d`, `cnn1d`, or `transformer`.

### 2. Acquire the BIDS dataset

OpenNeuro dataset snapshot for this repository:

```powershell
python .\scripts\download_bids.py `
  --dataset-id ds007262 `
  --snapshot 1.0.6 `
  --target .\data\bids_arithmetic
```

Direct archive URL:

```powershell
python .\scripts\download_bids.py `
  --archive-url https://example.org/your_bids_archive.zip `
  --target .\data\bids_arithmetic
```

One-command download plus pipeline execution for `ds007262` `v1.0.6`:

```powershell
.\scripts\run_end_to_end.ps1 -DatasetId ds007262 -Snapshot 1.0.6 -ForceDownload
```

### 3. Run a checked-in profile

Default fixed-window profile:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml
```

Alternative overlap profile:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc.yaml
```

The checked-in profiles assume a local copy of OpenNeuro `ds007262` `v1.0.6` under `data/bids_arithmetic`. They write under `analysis_pipeline/runs/<profile_name>/`. Both set `outputs.clean_start: true`, so rerunning the same profile replaces that profile's run directory only. If you want to preserve an existing run, copy the YAML and change `outputs.root` or set `clean_start: false`.

### 4. Run stage subsets

Run through feature extraction:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml `
  --only stage0 stage1 stage2 stage3 stage4 stage5
```

Run Stage 6 only:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline_unified_classic_nn_baseline_preproc.yaml `
  --only stage6
```

When `--only stage6` is used through the orchestrator, `stage6_confusions` is auto-run unless `--no-auto-stage6-confusions` is passed.

## Pipeline summary

| Stage | Script | Main purpose | Main outputs |
| --- | --- | --- | --- |
| 0 | `build_trial_table.py` | Build the canonical trial table from BIDS events. | `<run_root>/reports/trial_table_bids_arithmetic.tsv` |
| 1 | `stage1_qc_summary.py` | Summarize modality coverage, dropped samples, and participant QC. | `<run_root>/reports/qc_dataset_summary.json`, figures, subject table |
| 2 | `stage2_preprocess.py` | Clean EEG, ECG, and pupil streams and write derivatives. | `<run_root>/derivatives/cleaned/`, preprocess logs |
| 3 | `stage3_epoch_trials.py` | Convert trials into fixed or overlapping epochs with drop accounting. | `<run_root>/derivatives/epochs/`, `epoch_manifest.tsv`, `epoch_summary.json` |
| 4 | `stage4_extract_features.py` | Extract modality-specific engineered features. | `<run_root>/features/features_eeg.tsv`, `features_ecg.tsv`, `features_pupil.tsv` |
| 5 | `stage5_build_fused_table.py` | Build unimodal and fused ML tables plus split manifests. | `<run_root>/features/features_fused_tutorial_baseline.tsv`, `split_manifest_tutorial_baseline.json` |
| 6 | `stage6_train_classic_ml.py` | Benchmark classic and optional deep models across datasets, protocols, and class scenarios. | `<run_root>/reports/ml_results_*.json`, `<run_root>/reports/ml_summary_*.md`, `<run_root>/models/` |
| 6b | `stage6_highlight_confusions.py` | Curate top confusion matrices from Stage 6 results. | `<run_root>/reports/confusion_highlights_*.json`, markdown, PNGs |
| 6c | `stage6_build_publication_report.py` | Assemble a publication-facing run summary. | `<run_root>/reports/publication_full_report.md`, `.json` |

Stage 6 can also emit live confusion PNGs during training and EEG PSD/topomap QC figures when EEG is part of the selected dataset list.

## Checked-in profiles

| Profile | File | Intended use |
| --- | --- | --- |
| Baseline fixed-window run | `analysis_pipeline/config/pipeline_unified_classic_nn_baseline_preproc.yaml` | Canonical reproducible run: fixed 6 s calculation windows, classic plus deep model sweep, publication report enabled. |
| Overlap-window run | `analysis_pipeline/config/pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc.yaml` | Same pipeline family with 3 s windows, 1.5 s step size, and overlap enabled for Stage 3. |

Both profiles benchmark the `baseline_all_bins`, `baseline_omit_easiest`, `baseline_omit_hardest`, `baseline_low_high_omit_hardest`, and `baseline_grouped_4class_omit_hardest` class scenarios.

## Reproducibility notes

- `run_pipeline.py` expands output placeholders such as `{reports_dir}`, `{features_dir}`, and `{models_dir}` from `outputs.root`.
- Expected outputs are verified after every step. Use `--no-strict-outputs` only when debugging incomplete runs.
- Stage 1 strict QC carry-forward is propagated automatically into Stages 2 to 5.
- `--dry-run` prints planned commands and expected outputs without executing them.
- Stage 6 resolves both Windows and WSL-style dataset paths stored in split manifests.

## Documentation map

- `docs/pipeline_reference.md`: explicit stage-by-stage and config-by-config pipeline reference.
- `docs/reproducibility.md`: artifact policy, rerun guidance, and Linux-to-Windows handoff instructions.
- `analysis_pipeline/README.md`: package-level map of stage scripts and outputs.
- local manuscript handoff material can live under `docs/paper_handoff/` without changing the reproducible pipeline entry points.

## License

CC0 1.0 Universal (see `LICENSE`).

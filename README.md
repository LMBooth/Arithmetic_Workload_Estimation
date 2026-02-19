# Physiological Workload ML Pipeline (Standalone)

This repository is intentionally separated from the BIDS data-descriptor repository.

It contains only the code and documentation needed to:
1. Download a BIDS dataset snapshot.
2. Build trial tables and extract multimodal physiological features.
3. Train and evaluate machine-learning models for cognitive workload (task difficulty) resolution.

## Repository Scope

- `analysis_pipeline/`: staged processing scripts (trial table -> QC -> preprocessing -> epoching -> features -> ML).
- `analysis_pipeline/config/`: YAML configs for full runs and class-variant runs.
- `scripts/download_bids.py`: automatic BIDS download helper (OpenNeuro CLI or archive URL).
- `docs/`: explicit methods notes for journal write-up.

This repo should not be used to publish final BIDS data artifacts. Keep those in your separate data-descriptor repository.

## Quick Start

### 1) Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2) Download BIDS Dataset (automatic)

Option A: OpenNeuro dataset ID

```powershell
python .\scripts\download_bids.py `
  --dataset-id dsXXXXXX `
  --target .\data\bids_arithmetic
```

Option B: Direct archive URL (`.zip`, `.tar`, `.tar.gz`, `.tgz`)

```powershell
python .\scripts\download_bids.py `
  --archive-url https://example.org/your_bids_archive.zip `
  --target .\data\bids_arithmetic
```

One-command end-to-end example:

```powershell
.\scripts\run_end_to_end.ps1 -DatasetId dsXXXXXX -ForceDownload
```

### 3) Run Full Pipeline

```powershell
python .\analysis_pipeline\run_pipeline.py --config .\analysis_pipeline\config\pipeline.yaml
```

By default this runs Stage 0->6 and writes outputs under:
- `analysis_pipeline/derivatives/`
- `analysis_pipeline/features/`
- `analysis_pipeline/models/`
- `analysis_pipeline/reports/`

### 4) Stage-Focused Commands (feature extraction + ML)

If you want to run up to feature extraction first:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline.yaml `
  --only stage0 stage1 stage2 stage3 stage4 stage5
```

Then run ML only:

```powershell
python .\analysis_pipeline\run_pipeline.py `
  --config .\analysis_pipeline\config\pipeline.yaml `
  --only stage6 stage6_confusions
```

## Linux -> Windows Handoff (Baseline Reports)

`git pull` alone is not enough to reproduce baseline report assets on Windows. Large ML/report artifacts are intentionally ignored in `.gitignore`:

- `analysis_pipeline/reports/ml_results*.json`
- `analysis_pipeline/reports/confusion_highlights*.json`
- `analysis_pipeline/reports/confusion_pngs/`
- `analysis_pipeline/features/` (entire folder)

If the Linux machine already produced the baseline runs, copy these files from Linux into the same paths on Windows.

Required files to rebuild all baseline confusion reports on Windows:

- `analysis_pipeline/reports/ml_results_baseline_*_baseline.json` (classic baseline track, 5 files)
- `analysis_pipeline/reports/ml_results_baseline_*_baseline_advanced_nn.json` (advanced NN baseline track, 5 files)

Expected scenarios in those filenames:

- `baseline_all_bins`
- `baseline_omit_hardest`
- `baseline_low_high_omit_hardest`
- `baseline_grouped_4class_omit_hardest`
- `baseline_omit_easiest`

If you need to rerun baseline ML on Windows (not only regenerate confusion reports), also copy:

- `analysis_pipeline/features/` (all feature tables/manifests referenced by Stage 6)
- especially `analysis_pipeline/features/split_manifest_tutorial_baseline.json`

Rebuild confusion reports for all available `ml_results*.json` files (includes baseline + advanced if present):

```powershell
Get-ChildItem .\analysis_pipeline\reports\ml_results*.json | ForEach-Object {
  $scenario = $_.BaseName -replace '^ml_results_', ''
  python .\analysis_pipeline\stage6_highlight_confusions.py `
    --results-json $_.FullName `
    --out-json ("analysis_pipeline/reports/confusion_highlights_{0}.json" -f $scenario) `
    --out-md ("analysis_pipeline/reports/confusion_highlights_{0}.md" -f $scenario) `
    --metric balanced_accuracy_mean `
    --top-k-per-protocol 1 `
    --include-all `
    --out-png-dir analysis_pipeline/reports/confusion_pngs
}
```

Quick check that baseline inputs arrived:

```powershell
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline_*_baseline.json | Measure-Object
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline_*_baseline_advanced_nn.json | Measure-Object
```

Each command should report `Count = 5`.

## Stage Summary

- Stage 0: canonical trial table from BIDS events.
- Stage 1: QC summary.
- Stage 2: preprocessing (EEG/ECG/pupil).
- Stage 3: epoching from trial windows.
- Stage 4: feature extraction (unimodal).
- Stage 5: fused ML table + split manifest.
- Stage 6: split-aware ML benchmarking.

See `docs/pipeline_methods.md` for explicit methodological details, including how fixed 6-second arithmetic windows are converted into epochs and optional sub-windows.
For exact feature/model implementation details, see `docs/feature_ml_reference.md`.

## Notes for Manuscript Framing

This codebase is designed for ML-psychology style reporting of physiological workload resolution:
- modality-wise benchmarking (EEG, ECG, pupil, fused),
- protocol-wise benchmarking (LOSO, group_holdout, within_participant),
- class-resolution comparisons (binary/4/7/8 classes).

For deep models (`lstm1d`, `gru1d`, `cnn1d`, `transformer`), install PyTorch and run:

```powershell
python .\analysis_pipeline\run_pipeline.py --config .\analysis_pipeline\config\pipeline_with_deep_models.yaml
```

## License

CC0 1.0 Universal (see `LICENSE`).

# Reproducibility and Artifact Policy

This repository is intended to keep the pipeline implementation, configs, and human-written documentation under version control while keeping raw data and generated outputs local for the OpenNeuro `ds007262` `v1.0.6` study snapshot.

## What belongs in git

Track:

- Python source under `analysis_pipeline/`
- YAML configs under `analysis_pipeline/config/`
- helper scripts under `scripts/`
- repository-facing documentation under `README.md` and `docs/`

Keep local or regenerate:

- raw BIDS data under `data/`
- cleaned derivatives, feature tables, trained models, and run directories
- generated report outputs under `analysis_pipeline/reports/` and `analysis_pipeline/runs/`
- manuscript transfer bundles such as `.docx`, `.zip`, and one-off figure transfer folders

## Safe rerun behavior

The checked-in configs use dedicated output roots:

- `analysis_pipeline/runs/pipeline_unified_classic_nn_baseline_preproc/`
- `analysis_pipeline/runs/pipeline_unified_classic_nn_baseline_overlap3s_50pct_preproc/`

Both configs set `outputs.clean_start: true`. Rerunning either profile replaces only that profile's run directory. To preserve an existing run:

1. Copy the YAML profile.
2. Change `outputs.root` to a new run directory.
3. Or set `clean_start: false`.

## Recommended local workflow

1. Create the Python environment and install `requirements.txt`.
2. Download or place OpenNeuro `ds007262` `v1.0.6` under `data/bids_arithmetic`.
3. Run one of the checked-in profiles through `analysis_pipeline/run_pipeline.py`.
4. If Stage 0 to 5 outputs are already available, rerun only `stage6` or `stage6_confusions` as needed.
5. Build manuscript-facing assets only after the underlying `ml_results*.json` inputs are present locally.

Recommended download command:

```powershell
python .\scripts\download_bids.py `
  --dataset-id ds007262 `
  --snapshot 1.0.6 `
  --target .\data\bids_arithmetic
```

## Linux to Windows handoff for baseline outputs

If Linux already ran the classic and deep baseline training jobs, treat the Linux outputs as the source of truth. On Windows, prefer copying the Stage 6 result artifacts and rebuilding the downstream confusion and reporting assets from those files instead of rerunning Stage 6.

Do not assume `git pull` is enough. The key ML and reporting artifacts are intentionally ignored.

### Minimum files required to rebuild baseline confusion and report assets

Classic baseline result JSON files:

- `analysis_pipeline/reports/ml_results_baseline_all_bins_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline.json`

Advanced neural baseline result JSON files:

- `analysis_pipeline/reports/ml_results_baseline_all_bins_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline_advanced_nn.json`

Baseline split manifest referenced by Stage 6:

- `analysis_pipeline/features/split_manifest_tutorial_baseline.json`

If Windows must rerun Stage 6 instead of just rebuilding confusion and report assets, also copy:

- `analysis_pipeline/features/features_fused_tutorial_baseline.tsv`
- any other feature tables referenced by the copied split manifest

### Required verification before a rebuild

Run:

```powershell
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline_*_baseline.json | Measure-Object
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline_*_baseline_advanced_nn.json | Measure-Object
```

Each command must report `Count = 5`.

If either count is below 5:

- stop
- sync the missing files from Linux
- do not claim full classic plus advanced coverage
- do not rebuild confusion reports yet

### Missing-artifact audit

Use this exact check to list the missing baseline result files:

```powershell
$expected = @(
  "ml_results_baseline_all_bins_baseline.json",
  "ml_results_baseline_omit_hardest_baseline.json",
  "ml_results_baseline_low_high_omit_hardest_baseline.json",
  "ml_results_baseline_grouped_4class_omit_hardest_baseline.json",
  "ml_results_baseline_omit_easiest_baseline.json",
  "ml_results_baseline_all_bins_baseline_advanced_nn.json",
  "ml_results_baseline_omit_hardest_baseline_advanced_nn.json",
  "ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn.json",
  "ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn.json",
  "ml_results_baseline_omit_easiest_baseline_advanced_nn.json"
)
$present = Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline*.json |
  Select-Object -ExpandProperty Name
$missing = $expected | Where-Object { $_ -notin $present }
$missing
```

If the output list is non-empty, stop and sync those files before proceeding.

### Rebuild commands after the artifact set is complete

Rebuild confusion outputs:

```powershell
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline*.json | ForEach-Object {
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

Rebuild aggregate report assets:

```powershell
python .\analysis_pipeline\stage6_build_report_assets.py `
  --results-json-glob "analysis_pipeline/reports/ml_results_baseline*.json" `
  --confusion-json-glob "analysis_pipeline/reports/confusion_highlights_baseline*.json" `
  --out-dir analysis_pipeline/reports/report_assets_baseline_classic_and_advanced
```

### Naming conventions

Expected confusion markdown naming:

- Classic: `confusion_highlights_baseline_{scenario}_baseline.md`
- Advanced neural: `confusion_highlights_baseline_{scenario}_baseline_advanced_nn.md`

Supported baseline scenarios:

- `all_bins`
- `omit_hardest`
- `low_high_omit_hardest`
- `grouped_4class_omit_hardest`
- `omit_easiest`

## Direct Stage 6 reproduction notes

- Install PyTorch if you want to run the deep model names listed in the checked-in YAML profiles.
- Stage 6 reads the Stage 5 split manifest and evaluates dataset and protocol combinations from that file.
- The classic-model preprocessing stack is fit inside each split to avoid leakage.
- Run-level publication summaries depend on Stage 1, Stage 3, Stage 4, Stage 5, and Stage 6 artifacts all being present.

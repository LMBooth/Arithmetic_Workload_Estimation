# AGENTS.md

Scope: applies to this repository (`analysis_pipeline`) and all subdirectories.

## Cross-Machine Workflow (Linux Source of Truth)

If the Linux machine already ran classic + deep neural model training, treat Linux outputs as the source of truth.

When switching to Windows for documentation work:

- Do not rerun Stage 6 model training unless the user explicitly asks.
- Copy result artifacts from Linux first.
- Regenerate plots/reports from copied `ml_results*.json` files.

This saves time and avoids unnecessary retraining.

## Baseline/Deep Handoff Rule (Linux -> Windows)

When asked to rebuild baseline confusion reports on Windows, do **not** assume `git pull` is enough.

Reason: key ML/report artifacts are gitignored (large/reproducible), including:

- `analysis_pipeline/reports/ml_results*.json`
- `analysis_pipeline/reports/confusion_highlights*.json`
- `analysis_pipeline/reports/confusion_pngs/`
- `analysis_pipeline/features/`

## Required Linux Artifacts (Minimum for Plot/Report Regeneration)

Copy these from Linux into the same paths on Windows:

- Classic baseline results:
  - `analysis_pipeline/reports/ml_results_baseline_all_bins_baseline.json`
  - `analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline.json`
  - `analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline.json`
  - `analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline.json`
  - `analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline.json`
- Advanced NN baseline results:
  - `analysis_pipeline/reports/ml_results_baseline_all_bins_baseline_advanced_nn.json`
  - `analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline_advanced_nn.json`
  - `analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn.json`
  - `analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn.json`
  - `analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline_advanced_nn.json`
- Baseline split manifest used by stage6 configs:
  - `analysis_pipeline/features/split_manifest_tutorial_baseline.json`

If Stage 6 rerun is explicitly requested, copy full baseline feature artifacts from Linux as well, at minimum:

- `analysis_pipeline/features/split_manifest_tutorial_baseline.json`
- `analysis_pipeline/features/features_fused_tutorial_baseline.tsv`

## Required Verification Before Rebuild

Run:

```powershell
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline_*_baseline.json | Measure-Object
Get-ChildItem .\analysis_pipeline\reports\ml_results_baseline_*_baseline_advanced_nn.json | Measure-Object
```

Each should report `Count = 5`.

If either count is below 5:

- Stop.
- Ask user to sync missing Linux artifacts.
- Do not claim full baseline/deep coverage.

## Rebuild Command (All Baseline + Advanced JSONs Present)

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

Then regenerate documentation assets (tables/plots markdown + PNG):

```powershell
python .\analysis_pipeline\stage6_build_report_assets.py `
  --results-json-glob "analysis_pipeline/reports/ml_results_baseline*.json" `
  --confusion-json-glob "analysis_pipeline/reports/confusion_highlights_baseline*.json" `
  --out-dir analysis_pipeline/reports/report_assets_baseline_classic_and_advanced
```

## Output Naming Convention

Baseline confusion markdown names should follow:

- Classic: `confusion_highlights_baseline_{scenario}_baseline.md`
- Advanced NN: `confusion_highlights_baseline_{scenario}_baseline_advanced_nn.md`

Where `{scenario}` is one of:

- `all_bins`
- `omit_hardest`
- `low_high_omit_hardest`
- `grouped_4class_omit_hardest`
- `omit_easiest`

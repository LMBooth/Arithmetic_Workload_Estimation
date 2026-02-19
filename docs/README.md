# Documentation Index

This folder now has a split documentation layout so each part of the pipeline is easy to find:

- `docs/pipeline_methods.md`: Stage-by-stage implementation reference (Stage 0 to Stage 6 + confusion PNG generation).
- `docs/feature_ml_reference.md`: Detailed feature definitions and the current feature column inventories used for ML.
- `docs/ml_algorithms_and_settings.md`: ML algorithms, preprocessing stack, hyperparameter search spaces, and run settings.
- `docs/ml_outcomes.md`: Current ML outcome summary from the baseline scenario runs (classic vs advanced neural nets).

Supporting tables are in `docs/tables/`, including:

- `docs/tables/ml_feature_columns_eeg.csv`
- `docs/tables/ml_feature_columns_ecg.csv`
- `docs/tables/ml_feature_columns_pupil.csv`
- `docs/tables/ml_feature_columns_fused.csv`
- `docs/tables/ml_numeric_feature_columns_eeg.csv`
- `docs/tables/ml_numeric_feature_columns_ecg.csv`
- `docs/tables/ml_numeric_feature_columns_pupil.csv`
- `docs/tables/ml_numeric_feature_columns_fused.csv`
- `docs/tables/ml_feature_prefix_counts.csv`
- `docs/tables/ml_numeric_feature_prefix_counts.csv`

## Cross-Machine Note (Linux -> Windows)

Baseline ML result JSONs are large and gitignored, so they do not come through `git pull`.

To regenerate full baseline confusion reports on Windows, copy from Linux:

- `analysis_pipeline/reports/ml_results_baseline_*_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_*_baseline_advanced_nn.json`

Then run `analysis_pipeline/stage6_highlight_confusions.py` on those files to rebuild:

- `analysis_pipeline/reports/confusion_highlights_baseline_*.md`
- `analysis_pipeline/reports/confusion_highlights_baseline_*.json`
- `analysis_pipeline/reports/confusion_pngs/*`

See the handoff checklist and commands in `README.md`.

# ML Outcomes

This file summarizes the latest baseline-scenario ML outcomes produced on February 19, 2026 (UTC).

## Source Result Files

Classic baseline runs:

- `analysis_pipeline/reports/ml_results_baseline_all_bins_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline.json`

Advanced NN baseline runs:

- `analysis_pipeline/reports/ml_results_baseline_all_bins_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn.json`
- `analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline_advanced_nn.json`

Run metadata snapshot:

- Fused rows by scenario: `1200` (`baseline_all_bins`), `1045` (omit-hardest variants), `1044` (`baseline_omit_easiest`)
- Fused numeric features in these runs: `225`
- Protocol budgets: `group_holdout=2 outer splits`, `loso=2 outer splits`, `within_participant=10 evaluations`

## Best Fused Pipelines: Classic Track

| Scenario | Protocol | Best pipeline | BA | Macro-F1 | n_splits |
|---|---|---|---:|---:|---:|
| baseline_all_bins | group_holdout | `rf+none` | 0.2016 | 0.1718 | 2 |
| baseline_all_bins | loso | `rf+none` | 0.2192 | 0.1605 | 2 |
| baseline_all_bins | within_participant | `rf+none` | 0.3438 | 0.2971 | 10 |
| baseline_omit_hardest | group_holdout | `svm+none` | 0.2016 | 0.1837 | 2 |
| baseline_omit_hardest | loso | `svm+none` | 0.2256 | 0.2052 | 2 |
| baseline_omit_hardest | within_participant | `rf+none` | 0.3643 | 0.3348 | 10 |
| baseline_low_high_omit_hardest | group_holdout | `svm+none` | 0.4685 | 0.4641 | 2 |
| baseline_low_high_omit_hardest | loso | `svm+none` | 0.5139 | 0.4854 | 2 |
| baseline_low_high_omit_hardest | within_participant | `rf+none` | 0.7289 | 0.6966 | 10 |
| baseline_grouped_4class_omit_hardest | group_holdout | `svm+none` | 0.3439 | 0.3376 | 2 |
| baseline_grouped_4class_omit_hardest | loso | `svm+none` | 0.4613 | 0.4132 | 2 |
| baseline_grouped_4class_omit_hardest | within_participant | `rf+none` | 0.6292 | 0.5967 | 10 |
| baseline_omit_easiest | group_holdout | `decision_tree+none` | 0.1869 | 0.1702 | 2 |
| baseline_omit_easiest | loso | `mlp+none` | 0.2268 | 0.1843 | 2 |
| baseline_omit_easiest | within_participant | `rf+none` | 0.3214 | 0.2738 | 10 |

## Best Fused Pipelines: Advanced NN Track

| Scenario | Protocol | Best pipeline | BA | Macro-F1 | n_splits |
|---|---|---|---:|---:|---:|
| baseline_all_bins | group_holdout | `bilstm1d+none` | 0.1501 | 0.1205 | 2 |
| baseline_all_bins | loso | `bilstm1d+none` | 0.1637 | 0.0827 | 2 |
| baseline_all_bins | within_participant | `bilstm1d+none` | 0.1688 | 0.0887 | 10 |
| baseline_omit_hardest | group_holdout | `gru1d+none` | 0.1757 | 0.1285 | 2 |
| baseline_omit_hardest | loso | `bilstm1d+none` | 0.1757 | 0.0710 | 2 |
| baseline_omit_hardest | within_participant | `cnn1d+none` | 0.2500 | 0.1875 | 10 |
| baseline_low_high_omit_hardest | group_holdout | `lstm1d+none` | 0.3969 | 0.2874 | 2 |
| baseline_low_high_omit_hardest | loso | `bigru1d+none` | 0.4104 | 0.2785 | 2 |
| baseline_low_high_omit_hardest | within_participant | `cnn1d+none` | 0.5656 | 0.4213 | 10 |
| baseline_grouped_4class_omit_hardest | group_holdout | `gru1d+none` | 0.2949 | 0.2487 | 2 |
| baseline_grouped_4class_omit_hardest | loso | `lstm1d+none` | 0.3542 | 0.2254 | 2 |
| baseline_grouped_4class_omit_hardest | within_participant | `cnn1d_deep+none` | 0.4333 | 0.3693 | 10 |
| baseline_omit_easiest | group_holdout | `bilstm1d+none` | 0.1563 | 0.1228 | 2 |
| baseline_omit_easiest | loso | `cnn1d+none` | 0.1429 | 0.0370 | 2 |
| baseline_omit_easiest | within_participant | `bilstm1d+none` | 0.1857 | 0.1240 | 10 |

## Advanced vs Classic Delta (Fused BA)

`Delta = advanced_nn BA - classic BA`

| Scenario | Protocol | Classic BA | Advanced BA | Delta |
|---|---|---:|---:|---:|
| baseline_all_bins | group_holdout | 0.2016 | 0.1501 | -0.0515 |
| baseline_all_bins | loso | 0.2192 | 0.1637 | -0.0556 |
| baseline_all_bins | within_participant | 0.3438 | 0.1688 | -0.1750 |
| baseline_omit_hardest | group_holdout | 0.2016 | 0.1757 | -0.0259 |
| baseline_omit_hardest | loso | 0.2256 | 0.1757 | -0.0499 |
| baseline_omit_hardest | within_participant | 0.3643 | 0.2500 | -0.1143 |
| baseline_low_high_omit_hardest | group_holdout | 0.4685 | 0.3969 | -0.0716 |
| baseline_low_high_omit_hardest | loso | 0.5139 | 0.4104 | -0.1035 |
| baseline_low_high_omit_hardest | within_participant | 0.7289 | 0.5656 | -0.1633 |
| baseline_grouped_4class_omit_hardest | group_holdout | 0.3439 | 0.2949 | -0.0490 |
| baseline_grouped_4class_omit_hardest | loso | 0.4613 | 0.3542 | -0.1071 |
| baseline_grouped_4class_omit_hardest | within_participant | 0.6292 | 0.4333 | -0.1958 |
| baseline_omit_easiest | group_holdout | 0.1869 | 0.1563 | -0.0306 |
| baseline_omit_easiest | loso | 0.2268 | 0.1429 | -0.0839 |
| baseline_omit_easiest | within_participant | 0.3214 | 0.1857 | -0.1357 |

## Top Single Best Rows (All Datasets/Protocols)

- Classic best aggregate row: `baseline_low_high_omit_hardest`, dataset `fused`, protocol `within_participant`, pipeline `rf+none`, BA=`0.7289`, Macro-F1=`0.6966`.
- Advanced NN best aggregate row: `baseline_low_high_omit_hardest`, dataset `fused`, protocol `within_participant`, pipeline `cnn1d+none`, BA=`0.5656`, Macro-F1=`0.4213`.

## Confusion Matrix Outputs

Per-result confusion PNG counts:

- Classic baseline scenario files: `84` PNGs each (`4 datasets * 3 protocols * 7 models`)
- Advanced NN baseline scenario files: `96` PNGs each (`4 datasets * 3 protocols * 8 models`)

PNG root:

- `analysis_pipeline/reports/confusion_pngs/`

## Comparison and Report Asset Bundles

Per-scenario classic-vs-advanced comparisons:

- `analysis_pipeline/reports/ml_compare_classic_vs_advanced_baseline_all_bins.md`
- `analysis_pipeline/reports/ml_compare_classic_vs_advanced_baseline_omit_hardest.md`
- `analysis_pipeline/reports/ml_compare_classic_vs_advanced_baseline_low_high_omit_hardest.md`
- `analysis_pipeline/reports/ml_compare_classic_vs_advanced_baseline_grouped_4class_omit_hardest.md`
- `analysis_pipeline/reports/ml_compare_classic_vs_advanced_baseline_omit_easiest.md`

Combined report assets for baseline classic + advanced:

- `analysis_pipeline/reports/report_assets_baseline_classic_and_advanced/report_assets_manifest.json`
- `analysis_pipeline/reports/report_assets_baseline_classic_and_advanced/table_best_models_by_scenario_protocol.csv`
- `analysis_pipeline/reports/report_assets_baseline_classic_and_advanced/table_all_model_aggregates.csv`
- `analysis_pipeline/reports/report_assets_baseline_classic_and_advanced/table_confusion_class_recall.csv`

## Interpretation Note

Under the current quick-sweep settings (`inner_folds=2`, `max_param_combos=2`, `max_outer_splits_per_protocol=2`), classic pipelines outperform the advanced NN set on fused data for all listed baseline scenarios and protocols.

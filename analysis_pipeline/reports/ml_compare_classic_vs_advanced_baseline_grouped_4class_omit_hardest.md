# Stage 6 Before/After Comparison

- Baseline: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline.json` (baseline_grouped_4class_omit_hardest)
- Candidate: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn.json` (baseline_grouped_4class_omit_hardest)
- Metric: `balanced_accuracy_mean`
- Tolerance: `1e-06`

## Status Counts
- `BETTER_BASELINE`: 10
- `BETTER_CANDIDATE`: 2

## Track-Level Results
| dataset | protocol | status | baseline_score | candidate_score | delta | baseline_pipeline | candidate_pipeline |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | BETTER_CANDIDATE | 0.2801 | 0.3097 | +0.0296 | mlp+none | transformer+none |
| ecg | loso | BETTER_BASELINE | 0.3282 | 0.3046 | -0.0237 | svm+none | gru1d+none |
| ecg | within_participant | BETTER_BASELINE | 0.3792 | 0.3396 | -0.0396 | gaussian_nb+none | bilstm1d+none |
| eeg | group_holdout | BETTER_BASELINE | 0.3712 | 0.3441 | -0.0272 | rf+none | gru1d+none |
| eeg | loso | BETTER_CANDIDATE | 0.4252 | 0.4344 | +0.0092 | logreg+none | cnn1d+none |
| eeg | within_participant | BETTER_BASELINE | 0.5292 | 0.4750 | -0.0542 | logreg+none | cnn1d+none |
| fused | group_holdout | BETTER_BASELINE | 0.3439 | 0.2949 | -0.0490 | svm+none | gru1d+none |
| fused | loso | BETTER_BASELINE | 0.4613 | 0.3542 | -0.1071 | svm+none | lstm1d+none |
| fused | within_participant | BETTER_BASELINE | 0.6292 | 0.4333 | -0.1958 | rf+none | cnn1d_deep+none |
| pupil | group_holdout | BETTER_BASELINE | 0.3272 | 0.2900 | -0.0373 | svm+none | bigru1d+none |
| pupil | loso | BETTER_BASELINE | 0.3690 | 0.2901 | -0.0790 | mlp+none | bilstm1d+none |
| pupil | within_participant | BETTER_BASELINE | 0.6479 | 0.4625 | -0.1854 | decision_tree+none | cnn1d_deep+none |


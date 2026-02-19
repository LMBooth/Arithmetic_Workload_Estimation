# Stage 6 Before/After Comparison

- Baseline: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_all_bins_baseline.json` (baseline_all_bins)
- Candidate: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_all_bins_baseline_advanced_nn.json` (baseline_all_bins)
- Metric: `balanced_accuracy_mean`
- Tolerance: `1e-06`

## Status Counts
- `BETTER_BASELINE`: 12

## Track-Level Results
| dataset | protocol | status | baseline_score | candidate_score | delta | baseline_pipeline | candidate_pipeline |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | BETTER_BASELINE | 0.1678 | 0.1555 | -0.0123 | decision_tree+none | transformer+none |
| ecg | loso | BETTER_BASELINE | 0.1885 | 0.1474 | -0.0410 | gaussian_nb+none | cnn1d_deep+none |
| ecg | within_participant | BETTER_BASELINE | 0.2125 | 0.2000 | -0.0125 | rf+none | cnn1d_deep+none |
| eeg | group_holdout | BETTER_BASELINE | 0.1777 | 0.1611 | -0.0167 | mlp+none | cnn1d_deep+none |
| eeg | loso | BETTER_BASELINE | 0.2428 | 0.2411 | -0.0017 | logreg+none | cnn1d_deep+none |
| eeg | within_participant | BETTER_BASELINE | 0.3312 | 0.2188 | -0.1125 | mlp+none | cnn1d_deep+none |
| fused | group_holdout | BETTER_BASELINE | 0.2016 | 0.1501 | -0.0515 | rf+none | bilstm1d+none |
| fused | loso | BETTER_BASELINE | 0.2192 | 0.1637 | -0.0556 | rf+none | bilstm1d+none |
| fused | within_participant | BETTER_BASELINE | 0.3438 | 0.1688 | -0.1750 | rf+none | bilstm1d+none |
| pupil | group_holdout | BETTER_BASELINE | 0.1728 | 0.1474 | -0.0254 | rf+none | lstm1d+none |
| pupil | loso | BETTER_BASELINE | 0.1843 | 0.1607 | -0.0236 | decision_tree+none | gru1d+none |
| pupil | within_participant | BETTER_BASELINE | 0.3250 | 0.2062 | -0.1188 | rf+none | bilstm1d+none |


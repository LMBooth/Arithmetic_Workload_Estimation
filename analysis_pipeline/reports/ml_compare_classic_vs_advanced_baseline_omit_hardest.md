# Stage 6 Before/After Comparison

- Baseline: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline.json` (baseline_omit_hardest)
- Candidate: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline_advanced_nn.json` (baseline_omit_hardest)
- Metric: `balanced_accuracy_mean`
- Tolerance: `1e-06`

## Status Counts
- `BETTER_BASELINE`: 10
- `BETTER_CANDIDATE`: 2

## Track-Level Results
| dataset | protocol | status | baseline_score | candidate_score | delta | baseline_pipeline | candidate_pipeline |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | BETTER_CANDIDATE | 0.1750 | 0.1779 | +0.0029 | decision_tree+none | cnn1d+none |
| ecg | loso | BETTER_CANDIDATE | 0.2127 | 0.2306 | +0.0179 | mlp+none | bilstm1d+none |
| ecg | within_participant | BETTER_BASELINE | 0.2286 | 0.2214 | -0.0071 | rf+none | cnn1d+none |
| eeg | group_holdout | BETTER_BASELINE | 0.2233 | 0.2088 | -0.0145 | logreg+none | cnn1d+none |
| eeg | loso | BETTER_BASELINE | 0.2608 | 0.2459 | -0.0149 | rf+none | gru1d+none |
| eeg | within_participant | BETTER_BASELINE | 0.3643 | 0.2500 | -0.1143 | mlp+none | cnn1d+none |
| fused | group_holdout | BETTER_BASELINE | 0.2016 | 0.1757 | -0.0259 | svm+none | gru1d+none |
| fused | loso | BETTER_BASELINE | 0.2256 | 0.1757 | -0.0499 | svm+none | bilstm1d+none |
| fused | within_participant | BETTER_BASELINE | 0.3643 | 0.2500 | -0.1143 | rf+none | cnn1d+none |
| pupil | group_holdout | BETTER_BASELINE | 0.1866 | 0.1669 | -0.0198 | mlp+none | gru1d+none |
| pupil | loso | BETTER_BASELINE | 0.2324 | 0.1576 | -0.0748 | decision_tree+none | bilstm1d+none |
| pupil | within_participant | BETTER_BASELINE | 0.3857 | 0.3000 | -0.0857 | rf+none | cnn1d_deep+none |


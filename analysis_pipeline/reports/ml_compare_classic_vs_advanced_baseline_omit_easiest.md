# Stage 6 Before/After Comparison

- Baseline: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline.json` (baseline_omit_easiest)
- Candidate: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline_advanced_nn.json` (baseline_omit_easiest)
- Metric: `balanced_accuracy_mean`
- Tolerance: `1e-06`

## Status Counts
- `BETTER_BASELINE`: 9
- `BETTER_CANDIDATE`: 3

## Track-Level Results
| dataset | protocol | status | baseline_score | candidate_score | delta | baseline_pipeline | candidate_pipeline |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | BETTER_CANDIDATE | 0.1760 | 0.1987 | +0.0227 | knn+none | transformer_xl+none |
| ecg | loso | BETTER_BASELINE | 0.2075 | 0.1705 | -0.0370 | gaussian_nb+none | bilstm1d+none |
| ecg | within_participant | BETTER_CANDIDATE | 0.2286 | 0.2357 | +0.0071 | knn+none | cnn1d+none |
| eeg | group_holdout | BETTER_CANDIDATE | 0.1861 | 0.1875 | +0.0015 | logreg+none | cnn1d_deep+none |
| eeg | loso | BETTER_BASELINE | 0.2355 | 0.2242 | -0.0113 | logreg+none | bilstm1d+none |
| eeg | within_participant | BETTER_BASELINE | 0.3214 | 0.2929 | -0.0286 | svm+none | cnn1d+none |
| fused | group_holdout | BETTER_BASELINE | 0.1869 | 0.1563 | -0.0306 | decision_tree+none | bilstm1d+none |
| fused | loso | BETTER_BASELINE | 0.2268 | 0.1429 | -0.0839 | mlp+none | cnn1d+none |
| fused | within_participant | BETTER_BASELINE | 0.3214 | 0.1857 | -0.1357 | rf+none | bilstm1d+none |
| pupil | group_holdout | BETTER_BASELINE | 0.1691 | 0.1622 | -0.0068 | mlp+none | bigru1d+none |
| pupil | loso | BETTER_BASELINE | 0.1576 | 0.1429 | -0.0147 | mlp+none | cnn1d+none |
| pupil | within_participant | BETTER_BASELINE | 0.4214 | 0.1929 | -0.2286 | rf+none | lstm1d+none |


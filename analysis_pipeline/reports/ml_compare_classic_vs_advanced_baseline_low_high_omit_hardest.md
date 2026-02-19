# Stage 6 Before/After Comparison

- Baseline: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline.json` (baseline_low_high_omit_hardest)
- Candidate: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn.json` (baseline_low_high_omit_hardest)
- Metric: `balanced_accuracy_mean`
- Tolerance: `1e-06`

## Status Counts
- `BETTER_BASELINE`: 9
- `BETTER_CANDIDATE`: 3

## Track-Level Results
| dataset | protocol | status | baseline_score | candidate_score | delta | baseline_pipeline | candidate_pipeline |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | BETTER_CANDIDATE | 0.3867 | 0.3883 | +0.0016 | mlp+none | cnn1d_deep+none |
| ecg | loso | BETTER_BASELINE | 0.4346 | 0.4246 | -0.0100 | logreg+none | gru1d+none |
| ecg | within_participant | BETTER_CANDIDATE | 0.4889 | 0.5100 | +0.0211 | svm+none | transformer+none |
| eeg | group_holdout | BETTER_BASELINE | 0.4874 | 0.4524 | -0.0349 | svm+none | cnn1d_deep+none |
| eeg | loso | BETTER_BASELINE | 0.6015 | 0.5313 | -0.0702 | logreg+none | cnn1d_deep+none |
| eeg | within_participant | BETTER_BASELINE | 0.5800 | 0.5189 | -0.0611 | logreg+none | cnn1d_deep+none |
| fused | group_holdout | BETTER_BASELINE | 0.4685 | 0.3969 | -0.0716 | svm+none | lstm1d+none |
| fused | loso | BETTER_BASELINE | 0.5139 | 0.4104 | -0.1035 | svm+none | bigru1d+none |
| fused | within_participant | BETTER_BASELINE | 0.7289 | 0.5656 | -0.1633 | rf+none | cnn1d+none |
| pupil | group_holdout | BETTER_CANDIDATE | 0.3982 | 0.4015 | +0.0033 | svm+none | bigru1d+none |
| pupil | loso | BETTER_BASELINE | 0.5318 | 0.4581 | -0.0738 | svm+none | lstm1d+none |
| pupil | within_participant | BETTER_BASELINE | 0.6933 | 0.5167 | -0.1767 | rf+none | cnn1d+none |


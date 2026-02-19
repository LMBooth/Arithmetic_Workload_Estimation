# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `three_level_merged`
- Final labels: `low, mid, high`

## Dataset Snapshot
- `eeg`: rows=1081, features=183, participants=18, classes=3
- `ecg`: rows=1081, features=17, participants=18, classes=3
- `pupil`: rows=1081, features=25, participants=18, classes=3
- `fused`: rows=1081, features=225, participants=18, classes=3

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `rf+none` (balanced_acc=0.4102, macro_f1=0.4053, n=2)
- `ecg` + `loso` -> `rf+none` (balanced_acc=0.4253, macro_f1=0.3693, n=2)
- `ecg` + `within_participant` -> `logreg+none` (balanced_acc=0.3356, macro_f1=0.3195, n=10)
- `eeg` + `group_holdout` -> `logreg+none` (balanced_acc=0.4560, macro_f1=0.4513, n=2)
- `eeg` + `loso` -> `logreg+none` (balanced_acc=0.4543, macro_f1=0.3746, n=2)
- `eeg` + `within_participant` -> `svm+none` (balanced_acc=0.5261, macro_f1=0.5224, n=10)
- `fused` + `group_holdout` -> `mlp+none` (balanced_acc=0.4492, macro_f1=0.4397, n=2)
- `fused` + `loso` -> `rf+none` (balanced_acc=0.4753, macro_f1=0.3569, n=2)
- `fused` + `within_participant` -> `logreg+none` (balanced_acc=0.6528, macro_f1=0.6324, n=10)
- `pupil` + `group_holdout` -> `rf+none` (balanced_acc=0.4268, macro_f1=0.4097, n=2)
- `pupil` + `loso` -> `mlp+none` (balanced_acc=0.4907, macro_f1=0.3921, n=2)
- `pupil` + `within_participant` -> `rf+none` (balanced_acc=0.6389, macro_f1=0.6210, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3919 | 0.3910 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3430 | 0.3110 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.3676 | 0.3644 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.3332 | 0.3249 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.3362 | 0.3182 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.4102 | 0.4053 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.3733 | 0.3654 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.3713 | 0.3359 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.4109 | 0.3463 |
| ecg | loso | knn | none | knn+none | 2 | 0.3233 | 0.2977 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.3844 | 0.3556 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.3557 | 0.3068 |
| ecg | loso | rf | none | rf+none | 2 | 0.4253 | 0.3693 |
| ecg | loso | svm | none | svm+none | 2 | 0.4175 | 0.3774 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3167 | 0.3010 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3172 | 0.3050 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.3300 | 0.2815 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.3356 | 0.3195 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.3089 | 0.2952 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.3189 | 0.3067 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.2744 | 0.2650 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3789 | 0.3736 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3596 | 0.2787 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.3955 | 0.3970 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.4560 | 0.4513 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.4166 | 0.4100 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.3784 | 0.3778 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.4465 | 0.4508 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.3387 | 0.3329 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3485 | 0.2177 |
| eeg | loso | knn | none | knn+none | 2 | 0.3834 | 0.3003 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.4543 | 0.3746 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.4129 | 0.3382 |
| eeg | loso | rf | none | rf+none | 2 | 0.4334 | 0.3713 |
| eeg | loso | svm | none | svm+none | 2 | 0.4350 | 0.3599 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.4267 | 0.4131 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.4639 | 0.4381 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.4506 | 0.4305 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.5256 | 0.5167 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.5228 | 0.5051 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.5189 | 0.5013 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.5261 | 0.5224 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.4285 | 0.4276 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3299 | 0.1816 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.4161 | 0.4161 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.3343 | 0.2339 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.4492 | 0.4397 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.4208 | 0.3797 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.4467 | 0.4292 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.4512 | 0.4125 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3333 | 0.1491 |
| fused | loso | knn | none | knn+none | 2 | 0.3333 | 0.3104 |
| fused | loso | logreg | none | logreg+none | 2 | 0.3333 | 0.1752 |
| fused | loso | mlp | none | mlp+none | 2 | 0.4259 | 0.3563 |
| fused | loso | rf | none | rf+none | 2 | 0.4753 | 0.3569 |
| fused | loso | svm | none | svm+none | 2 | 0.4753 | 0.3684 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.5211 | 0.5144 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3539 | 0.2266 |
| fused | within_participant | knn | none | knn+none | 10 | 0.5061 | 0.4643 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.6528 | 0.6324 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.5783 | 0.5528 |
| fused | within_participant | rf | none | rf+none | 10 | 0.6083 | 0.5749 |
| fused | within_participant | svm | none | svm+none | 10 | 0.4983 | 0.4331 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3595 | 0.3523 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3299 | 0.1816 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.3810 | 0.3766 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.3367 | 0.2372 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.4033 | 0.3568 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.4268 | 0.4097 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.4065 | 0.3803 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.4811 | 0.4571 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3333 | 0.1491 |
| pupil | loso | knn | none | knn+none | 2 | 0.3611 | 0.2930 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.3333 | 0.1752 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.4907 | 0.3921 |
| pupil | loso | rf | none | rf+none | 2 | 0.4722 | 0.3814 |
| pupil | loso | svm | none | svm+none | 2 | 0.3951 | 0.3211 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.6150 | 0.5843 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3733 | 0.2431 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.6161 | 0.5991 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.6067 | 0.5780 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.5711 | 0.5312 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.6389 | 0.6210 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.5094 | 0.4413 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 45
- ConvergenceWarning: lbfgs failed to converge (status=1):: 36
- ConvergenceWarning: lbfgs failed to converge (status=2):: 24


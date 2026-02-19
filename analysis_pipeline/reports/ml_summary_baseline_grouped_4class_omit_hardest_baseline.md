# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_grouped_4class_omit_hardest`
- Final labels: `low_1_2, baseline, mid_3_4, high_5_6`

## Dataset Snapshot
- `eeg`: rows=1045, features=183, participants=18, classes=4
- `ecg`: rows=1045, features=17, participants=18, classes=4
- `pupil`: rows=1045, features=25, participants=18, classes=4
- `fused`: rows=1045, features=225, participants=18, classes=4

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `mlp+none` (balanced_acc=0.2801, macro_f1=0.2707, n=2)
- `ecg` + `loso` -> `svm+none` (balanced_acc=0.3282, macro_f1=0.2315, n=2)
- `ecg` + `within_participant` -> `gaussian_nb+none` (balanced_acc=0.3792, macro_f1=0.3295, n=10)
- `eeg` + `group_holdout` -> `rf+none` (balanced_acc=0.3712, macro_f1=0.3776, n=2)
- `eeg` + `loso` -> `logreg+none` (balanced_acc=0.4252, macro_f1=0.3388, n=2)
- `eeg` + `within_participant` -> `logreg+none` (balanced_acc=0.5292, macro_f1=0.5007, n=10)
- `fused` + `group_holdout` -> `svm+none` (balanced_acc=0.3439, macro_f1=0.3376, n=2)
- `fused` + `loso` -> `svm+none` (balanced_acc=0.4613, macro_f1=0.4132, n=2)
- `fused` + `within_participant` -> `rf+none` (balanced_acc=0.6292, macro_f1=0.5967, n=10)
- `pupil` + `group_holdout` -> `svm+none` (balanced_acc=0.3272, macro_f1=0.2974, n=2)
- `pupil` + `loso` -> `mlp+none` (balanced_acc=0.3690, macro_f1=0.2734, n=2)
- `pupil` + `within_participant` -> `decision_tree+none` (balanced_acc=0.6479, macro_f1=0.6123, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.2735 | 0.2152 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.2419 | 0.2205 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.2582 | 0.2481 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.2235 | 0.1978 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.2801 | 0.2707 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.2658 | 0.2556 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.2429 | 0.2274 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.2495 | 0.2151 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3193 | 0.2660 |
| ecg | loso | knn | none | knn+none | 2 | 0.2778 | 0.2356 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.2937 | 0.2180 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.3047 | 0.2897 |
| ecg | loso | rf | none | rf+none | 2 | 0.3233 | 0.2685 |
| ecg | loso | svm | none | svm+none | 2 | 0.3282 | 0.2315 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3354 | 0.2770 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3792 | 0.3295 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.3479 | 0.2967 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.3187 | 0.2922 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.3208 | 0.2925 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.3375 | 0.2911 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.3021 | 0.2579 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.2417 | 0.2280 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3097 | 0.2560 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.3247 | 0.3262 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.3697 | 0.3651 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.3376 | 0.3403 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.3712 | 0.3776 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.3439 | 0.3357 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.3006 | 0.2646 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3041 | 0.2307 |
| eeg | loso | knn | none | knn+none | 2 | 0.2960 | 0.2372 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.4252 | 0.3388 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.3596 | 0.3251 |
| eeg | loso | rf | none | rf+none | 2 | 0.3244 | 0.2514 |
| eeg | loso | svm | none | svm+none | 2 | 0.3451 | 0.3088 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3604 | 0.3350 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.4333 | 0.3928 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.3750 | 0.3319 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.5292 | 0.5007 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.5062 | 0.4940 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.4521 | 0.4482 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.4812 | 0.4627 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.2812 | 0.2722 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.2702 | 0.1560 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.3076 | 0.3083 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.2597 | 0.1598 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.2986 | 0.2873 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.3306 | 0.3104 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.3439 | 0.3376 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.2886 | 0.2903 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2500 | 0.1147 |
| fused | loso | knn | none | knn+none | 2 | 0.2609 | 0.2348 |
| fused | loso | logreg | none | logreg+none | 2 | 0.2609 | 0.1091 |
| fused | loso | mlp | none | mlp+none | 2 | 0.2986 | 0.2312 |
| fused | loso | rf | none | rf+none | 2 | 0.3512 | 0.2671 |
| fused | loso | svm | none | svm+none | 2 | 0.4613 | 0.4132 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.5146 | 0.4868 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.4229 | 0.3515 |
| fused | within_participant | knn | none | knn+none | 10 | 0.4937 | 0.4568 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.5875 | 0.5583 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.5354 | 0.5130 |
| fused | within_participant | rf | none | rf+none | 10 | 0.6292 | 0.5967 |
| fused | within_participant | svm | none | svm+none | 10 | 0.4771 | 0.4320 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3123 | 0.2991 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.2702 | 0.1560 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.3070 | 0.3045 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.2337 | 0.1410 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.3076 | 0.2692 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.3241 | 0.2896 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.3272 | 0.2974 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.2949 | 0.2643 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2500 | 0.1147 |
| pupil | loso | knn | none | knn+none | 2 | 0.2712 | 0.2138 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.2609 | 0.1091 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.3690 | 0.2734 |
| pupil | loso | rf | none | rf+none | 2 | 0.2639 | 0.1618 |
| pupil | loso | svm | none | svm+none | 2 | 0.3026 | 0.2294 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.6479 | 0.6123 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.4021 | 0.3299 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.5021 | 0.4593 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.5458 | 0.4904 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.4125 | 0.3824 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.5771 | 0.5369 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.5062 | 0.4448 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 46
- ConvergenceWarning: lbfgs failed to converge (status=1):: 40
- ConvergenceWarning: lbfgs failed to converge (status=2):: 5


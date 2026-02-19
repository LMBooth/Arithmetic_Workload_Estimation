# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_low_high_omit_hardest`
- Final labels: `low_1_2_3, baseline, high_4_5_6`

## Dataset Snapshot
- `eeg`: rows=1045, features=183, participants=18, classes=3
- `ecg`: rows=1045, features=17, participants=18, classes=3
- `pupil`: rows=1045, features=25, participants=18, classes=3
- `fused`: rows=1045, features=225, participants=18, classes=3

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `mlp+none` (balanced_acc=0.3867, macro_f1=0.3750, n=2)
- `ecg` + `loso` -> `logreg+none` (balanced_acc=0.4346, macro_f1=0.3158, n=2)
- `ecg` + `within_participant` -> `svm+none` (balanced_acc=0.4889, macro_f1=0.4446, n=10)
- `eeg` + `group_holdout` -> `svm+none` (balanced_acc=0.4874, macro_f1=0.4844, n=2)
- `eeg` + `loso` -> `logreg+none` (balanced_acc=0.6015, macro_f1=0.5328, n=2)
- `eeg` + `within_participant` -> `logreg+none` (balanced_acc=0.5800, macro_f1=0.5618, n=10)
- `fused` + `group_holdout` -> `svm+none` (balanced_acc=0.4685, macro_f1=0.4641, n=2)
- `fused` + `loso` -> `svm+none` (balanced_acc=0.5139, macro_f1=0.4854, n=2)
- `fused` + `within_participant` -> `rf+none` (balanced_acc=0.7289, macro_f1=0.6966, n=10)
- `pupil` + `group_holdout` -> `svm+none` (balanced_acc=0.3982, macro_f1=0.3785, n=2)
- `pupil` + `loso` -> `svm+none` (balanced_acc=0.5318, macro_f1=0.5190, n=2)
- `pupil` + `within_participant` -> `rf+none` (balanced_acc=0.6933, macro_f1=0.6757, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3553 | 0.3134 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3340 | 0.3139 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.3653 | 0.3668 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.3038 | 0.2789 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.3867 | 0.3750 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.3514 | 0.3326 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.3464 | 0.3171 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.4123 | 0.3614 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3811 | 0.3310 |
| ecg | loso | knn | none | knn+none | 2 | 0.3451 | 0.3033 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.4346 | 0.3158 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.3785 | 0.3404 |
| ecg | loso | rf | none | rf+none | 2 | 0.3514 | 0.3052 |
| ecg | loso | svm | none | svm+none | 2 | 0.4181 | 0.2701 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3867 | 0.3711 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.4156 | 0.3680 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.3822 | 0.3499 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.4433 | 0.4212 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.4711 | 0.4661 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.4533 | 0.4151 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.4889 | 0.4446 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3290 | 0.3061 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3936 | 0.3385 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.4204 | 0.4185 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.4673 | 0.4581 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.4101 | 0.3985 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.4414 | 0.4413 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.4874 | 0.4844 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.5314 | 0.5220 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.5370 | 0.5441 |
| eeg | loso | knn | none | knn+none | 2 | 0.3974 | 0.3540 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.6015 | 0.5328 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.4408 | 0.4341 |
| eeg | loso | rf | none | rf+none | 2 | 0.4049 | 0.3394 |
| eeg | loso | svm | none | svm+none | 2 | 0.4847 | 0.4633 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.4589 | 0.4357 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.5389 | 0.4905 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.3967 | 0.3767 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.5800 | 0.5618 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.5367 | 0.5295 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.5656 | 0.5304 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.5467 | 0.5261 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.2903 | 0.2960 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3647 | 0.2471 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.3881 | 0.3737 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.3097 | 0.1733 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.3495 | 0.3332 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.4418 | 0.4332 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.4685 | 0.4641 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.4349 | 0.3977 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3333 | 0.2030 |
| fused | loso | knn | none | knn+none | 2 | 0.4168 | 0.4114 |
| fused | loso | logreg | none | logreg+none | 2 | 0.3272 | 0.1356 |
| fused | loso | mlp | none | mlp+none | 2 | 0.4485 | 0.4189 |
| fused | loso | rf | none | rf+none | 2 | 0.4621 | 0.4062 |
| fused | loso | svm | none | svm+none | 2 | 0.5139 | 0.4854 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.6567 | 0.6262 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.5078 | 0.4280 |
| fused | within_participant | knn | none | knn+none | 10 | 0.6378 | 0.5971 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.7044 | 0.6782 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.6767 | 0.6370 |
| fused | within_participant | rf | none | rf+none | 10 | 0.7289 | 0.6966 |
| fused | within_participant | svm | none | svm+none | 10 | 0.5922 | 0.5429 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.3824 | 0.3663 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.3647 | 0.2471 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.3785 | 0.3635 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.3182 | 0.1776 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.3401 | 0.3010 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.3966 | 0.3515 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.3982 | 0.3785 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.4551 | 0.4289 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.3333 | 0.2030 |
| pupil | loso | knn | none | knn+none | 2 | 0.4062 | 0.3762 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.3272 | 0.1356 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.4805 | 0.4483 |
| pupil | loso | rf | none | rf+none | 2 | 0.4198 | 0.3372 |
| pupil | loso | svm | none | svm+none | 2 | 0.5318 | 0.5190 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.6522 | 0.6201 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.4600 | 0.3727 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.6233 | 0.6055 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.6700 | 0.6586 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.5633 | 0.5447 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.6933 | 0.6757 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.5856 | 0.5651 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 40
- ConvergenceWarning: lbfgs failed to converge (status=1):: 39
- ConvergenceWarning: lbfgs failed to converge (status=2):: 6


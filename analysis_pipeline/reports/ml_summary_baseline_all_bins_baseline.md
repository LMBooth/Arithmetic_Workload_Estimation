# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_all_bins`
- Final labels: `0.6-1.5, baseline, 1.5-2.4, 2.4-3.3, 3.3-4.2, 4.2-5.1, 5.1-6.0, 6.0-6.9`

## Dataset Snapshot
- `eeg`: rows=1200, features=183, participants=18, classes=8
- `ecg`: rows=1200, features=17, participants=18, classes=8
- `pupil`: rows=1200, features=25, participants=18, classes=8
- `fused`: rows=1200, features=225, participants=18, classes=8

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `decision_tree+none` (balanced_acc=0.1678, macro_f1=0.1577, n=2)
- `ecg` + `loso` -> `gaussian_nb+none` (balanced_acc=0.1885, macro_f1=0.1048, n=2)
- `ecg` + `within_participant` -> `rf+none` (balanced_acc=0.2125, macro_f1=0.1792, n=10)
- `eeg` + `group_holdout` -> `mlp+none` (balanced_acc=0.1777, macro_f1=0.1654, n=2)
- `eeg` + `loso` -> `logreg+none` (balanced_acc=0.2428, macro_f1=0.1959, n=2)
- `eeg` + `within_participant` -> `mlp+none` (balanced_acc=0.3312, macro_f1=0.2883, n=10)
- `fused` + `group_holdout` -> `rf+none` (balanced_acc=0.2016, macro_f1=0.1718, n=2)
- `fused` + `loso` -> `rf+none` (balanced_acc=0.2192, macro_f1=0.1605, n=2)
- `fused` + `within_participant` -> `rf+none` (balanced_acc=0.3438, macro_f1=0.2971, n=10)
- `pupil` + `group_holdout` -> `rf+none` (balanced_acc=0.1728, macro_f1=0.1490, n=2)
- `pupil` + `loso` -> `decision_tree+none` (balanced_acc=0.1843, macro_f1=0.1688, n=2)
- `pupil` + `within_participant` -> `rf+none` (balanced_acc=0.3250, macro_f1=0.2753, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1678 | 0.1577 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1370 | 0.1122 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.1414 | 0.1361 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.1152 | 0.0951 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.1366 | 0.1289 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.1500 | 0.1468 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.1567 | 0.1449 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.1200 | 0.0820 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1885 | 0.1048 |
| ecg | loso | knn | none | knn+none | 2 | 0.1338 | 0.1182 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.1693 | 0.1125 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.1395 | 0.1176 |
| ecg | loso | rf | none | rf+none | 2 | 0.1465 | 0.1303 |
| ecg | loso | svm | none | svm+none | 2 | 0.1226 | 0.0858 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.1875 | 0.1608 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2062 | 0.1437 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.1938 | 0.1607 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.1938 | 0.1577 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.1812 | 0.1615 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.2125 | 0.1792 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.1875 | 0.1516 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1417 | 0.1330 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1531 | 0.1074 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.1522 | 0.1463 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.1771 | 0.1521 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.1777 | 0.1654 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.1475 | 0.1272 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.1519 | 0.1344 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.1999 | 0.1762 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1894 | 0.1108 |
| eeg | loso | knn | none | knn+none | 2 | 0.1962 | 0.1473 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.2428 | 0.1959 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.1952 | 0.1786 |
| eeg | loso | rf | none | rf+none | 2 | 0.2212 | 0.1496 |
| eeg | loso | svm | none | svm+none | 2 | 0.1885 | 0.1512 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.1875 | 0.1557 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2875 | 0.2331 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.2375 | 0.1956 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.3063 | 0.2782 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.3312 | 0.2883 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.3125 | 0.2693 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.3063 | 0.2705 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1807 | 0.1775 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1129 | 0.0307 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.1658 | 0.1676 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.1306 | 0.0658 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.1512 | 0.1468 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.2016 | 0.1718 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.1808 | 0.1718 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.1270 | 0.0857 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1250 | 0.0287 |
| fused | loso | knn | none | knn+none | 2 | 0.1319 | 0.1086 |
| fused | loso | logreg | none | logreg+none | 2 | 0.1131 | 0.0440 |
| fused | loso | mlp | none | mlp+none | 2 | 0.1974 | 0.1264 |
| fused | loso | rf | none | rf+none | 2 | 0.2192 | 0.1605 |
| fused | loso | svm | none | svm+none | 2 | 0.1865 | 0.1676 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2812 | 0.2505 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1187 | 0.0442 |
| fused | within_participant | knn | none | knn+none | 10 | 0.2437 | 0.2132 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.3438 | 0.2756 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.3312 | 0.2803 |
| fused | within_participant | rf | none | rf+none | 10 | 0.3438 | 0.2971 |
| fused | within_participant | svm | none | svm+none | 10 | 0.2500 | 0.1949 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1568 | 0.1548 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1129 | 0.0307 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.1340 | 0.1210 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.1264 | 0.0539 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.1648 | 0.1447 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.1728 | 0.1490 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.1651 | 0.1413 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.1843 | 0.1688 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1250 | 0.0287 |
| pupil | loso | knn | none | knn+none | 2 | 0.1250 | 0.0890 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.1131 | 0.0451 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.1128 | 0.0704 |
| pupil | loso | rf | none | rf+none | 2 | 0.1687 | 0.0906 |
| pupil | loso | svm | none | svm+none | 2 | 0.1597 | 0.0928 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2750 | 0.2214 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1187 | 0.0449 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.2625 | 0.2216 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.2687 | 0.2157 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.2625 | 0.1990 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.3250 | 0.2753 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.2750 | 0.2031 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 68
- ConvergenceWarning: lbfgs failed to converge (status=1):: 44
- ConvergenceWarning: lbfgs failed to converge (status=2):: 19


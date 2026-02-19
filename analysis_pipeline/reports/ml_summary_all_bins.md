# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `all_bins`
- Final labels: `0.6-1.5, 1.5-2.4, 2.4-3.3, 3.3-4.2, 4.2-5.1, 5.1-6.0, 6.0-6.9`

## Dataset Snapshot
- `eeg`: rows=1081, features=183, participants=18, classes=7
- `ecg`: rows=1081, features=17, participants=18, classes=7
- `pupil`: rows=1081, features=25, participants=18, classes=7
- `fused`: rows=1081, features=225, participants=18, classes=7

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `svm+none` (balanced_acc=0.1827, macro_f1=0.1686, n=2)
- `ecg` + `loso` -> `rf+none` (balanced_acc=0.1966, macro_f1=0.1675, n=2)
- `ecg` + `within_participant` -> `gaussian_nb+none` (balanced_acc=0.2143, macro_f1=0.1550, n=10)
- `eeg` + `group_holdout` -> `mlp+none` (balanced_acc=0.2071, macro_f1=0.1977, n=2)
- `eeg` + `loso` -> `rf+none` (balanced_acc=0.2347, macro_f1=0.1680, n=2)
- `eeg` + `within_participant` -> `mlp+none` (balanced_acc=0.3286, macro_f1=0.2838, n=10)
- `fused` + `group_holdout` -> `rf+none` (balanced_acc=0.2473, macro_f1=0.2223, n=2)
- `fused` + `loso` -> `decision_tree+none` (balanced_acc=0.1984, macro_f1=0.1788, n=2)
- `fused` + `within_participant` -> `logreg+none` (balanced_acc=0.2643, macro_f1=0.2204, n=10)
- `pupil` + `group_holdout` -> `rf+none` (balanced_acc=0.1935, macro_f1=0.1768, n=2)
- `pupil` + `loso` -> `decision_tree+none` (balanced_acc=0.2401, macro_f1=0.2184, n=2)
- `pupil` + `within_participant` -> `rf+none` (balanced_acc=0.3286, macro_f1=0.2913, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1098 | 0.0982 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1590 | 0.1359 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.1605 | 0.1540 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.1437 | 0.1201 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.1661 | 0.1536 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.1627 | 0.1568 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.1827 | 0.1686 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.1290 | 0.1082 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1599 | 0.0899 |
| ecg | loso | knn | none | knn+none | 2 | 0.1427 | 0.1370 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.1878 | 0.1326 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.1368 | 0.1110 |
| ecg | loso | rf | none | rf+none | 2 | 0.1966 | 0.1675 |
| ecg | loso | svm | none | svm+none | 2 | 0.1355 | 0.1002 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.1286 | 0.1092 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2143 | 0.1550 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.2000 | 0.1581 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.1929 | 0.1585 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.1643 | 0.1269 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.1857 | 0.1567 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.1786 | 0.1222 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1881 | 0.1865 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1592 | 0.1034 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.1867 | 0.1758 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.1920 | 0.1648 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.2071 | 0.1977 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.1649 | 0.1512 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.1669 | 0.1563 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.1301 | 0.1166 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1983 | 0.1116 |
| eeg | loso | knn | none | knn+none | 2 | 0.1789 | 0.1342 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.1542 | 0.0893 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.1695 | 0.1446 |
| eeg | loso | rf | none | rf+none | 2 | 0.2347 | 0.1680 |
| eeg | loso | svm | none | svm+none | 2 | 0.2321 | 0.1676 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2714 | 0.2522 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2571 | 0.2188 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.2714 | 0.2266 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.3143 | 0.2684 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.3286 | 0.2838 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.2500 | 0.2158 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.3214 | 0.2869 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1639 | 0.1588 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1291 | 0.0381 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.1952 | 0.1928 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.1276 | 0.0600 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.1859 | 0.1679 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.2473 | 0.2223 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.1738 | 0.1465 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.1984 | 0.1788 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1429 | 0.0360 |
| fused | loso | knn | none | knn+none | 2 | 0.1429 | 0.1332 |
| fused | loso | logreg | none | logreg+none | 2 | 0.1032 | 0.0281 |
| fused | loso | mlp | none | mlp+none | 2 | 0.1984 | 0.1424 |
| fused | loso | rf | none | rf+none | 2 | 0.1905 | 0.1293 |
| fused | loso | svm | none | svm+none | 2 | 0.1825 | 0.1609 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2429 | 0.2037 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1714 | 0.0912 |
| fused | within_participant | knn | none | knn+none | 10 | 0.1643 | 0.1315 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.2643 | 0.2204 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.1571 | 0.1357 |
| fused | within_participant | rf | none | rf+none | 10 | 0.2214 | 0.1919 |
| fused | within_participant | svm | none | svm+none | 10 | 0.2429 | 0.1537 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1798 | 0.1697 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1291 | 0.0381 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.1553 | 0.1357 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.1235 | 0.0576 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.1935 | 0.1692 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.1935 | 0.1768 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.1676 | 0.1369 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.2401 | 0.2184 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1429 | 0.0360 |
| pupil | loso | knn | none | knn+none | 2 | 0.1270 | 0.0837 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.1032 | 0.0280 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.1508 | 0.0799 |
| pupil | loso | rf | none | rf+none | 2 | 0.2222 | 0.1437 |
| pupil | loso | svm | none | svm+none | 2 | 0.1825 | 0.1136 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2786 | 0.2439 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1786 | 0.0923 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.3143 | 0.2657 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.2000 | 0.1483 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.3143 | 0.2369 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.3286 | 0.2913 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.2500 | 0.1677 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 66
- ConvergenceWarning: lbfgs failed to converge (status=1):: 42
- ConvergenceWarning: lbfgs failed to converge (status=2):: 20


# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_omit_easiest`
- Final labels: `1.5-2.4, baseline, 2.4-3.3, 3.3-4.2, 4.2-5.1, 5.1-6.0, 6.0-6.9`

## Dataset Snapshot
- `eeg`: rows=1044, features=183, participants=18, classes=7
- `ecg`: rows=1044, features=17, participants=18, classes=7
- `pupil`: rows=1044, features=25, participants=18, classes=7
- `fused`: rows=1044, features=225, participants=18, classes=7

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `knn+none` (balanced_acc=0.1760, macro_f1=0.1765, n=2)
- `ecg` + `loso` -> `gaussian_nb+none` (balanced_acc=0.2075, macro_f1=0.1167, n=2)
- `ecg` + `within_participant` -> `knn+none` (balanced_acc=0.2286, macro_f1=0.1912, n=10)
- `eeg` + `group_holdout` -> `logreg+none` (balanced_acc=0.1861, macro_f1=0.1659, n=2)
- `eeg` + `loso` -> `logreg+none` (balanced_acc=0.2355, macro_f1=0.1694, n=2)
- `eeg` + `within_participant` -> `svm+none` (balanced_acc=0.3214, macro_f1=0.2731, n=10)
- `fused` + `group_holdout` -> `decision_tree+none` (balanced_acc=0.1869, macro_f1=0.1702, n=2)
- `fused` + `loso` -> `mlp+none` (balanced_acc=0.2268, macro_f1=0.1843, n=2)
- `fused` + `within_participant` -> `rf+none` (balanced_acc=0.3214, macro_f1=0.2738, n=10)
- `pupil` + `group_holdout` -> `mlp+none` (balanced_acc=0.1691, macro_f1=0.1578, n=2)
- `pupil` + `loso` -> `mlp+none` (balanced_acc=0.1576, macro_f1=0.1071, n=2)
- `pupil` + `within_participant` -> `rf+none` (balanced_acc=0.4214, macro_f1=0.3605, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1580 | 0.1331 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1599 | 0.1311 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.1760 | 0.1765 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.1366 | 0.1192 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.1200 | 0.1147 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.1592 | 0.1503 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.1388 | 0.1326 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.1009 | 0.0720 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2075 | 0.1167 |
| ecg | loso | knn | none | knn+none | 2 | 0.1484 | 0.1348 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.2037 | 0.1411 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.1346 | 0.1191 |
| ecg | loso | rf | none | rf+none | 2 | 0.1584 | 0.1280 |
| ecg | loso | svm | none | svm+none | 2 | 0.2003 | 0.1412 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.1714 | 0.1427 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2000 | 0.1521 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.2286 | 0.1912 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.2000 | 0.1504 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.2143 | 0.1793 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.2214 | 0.1861 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.2000 | 0.1633 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1328 | 0.1265 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1718 | 0.1189 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.1678 | 0.1576 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.1861 | 0.1659 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.1740 | 0.1590 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.1830 | 0.1737 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.1801 | 0.1708 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.1747 | 0.1709 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2174 | 0.1397 |
| eeg | loso | knn | none | knn+none | 2 | 0.1789 | 0.1342 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.2355 | 0.1694 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.1538 | 0.1285 |
| eeg | loso | rf | none | rf+none | 2 | 0.2086 | 0.1399 |
| eeg | loso | svm | none | svm+none | 2 | 0.1825 | 0.1459 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2357 | 0.2085 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3143 | 0.2674 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.2643 | 0.2190 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.2357 | 0.2196 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.3071 | 0.2505 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.3000 | 0.2848 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.3214 | 0.2731 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1869 | 0.1702 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1388 | 0.0418 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.1518 | 0.1520 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.1201 | 0.0746 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.1819 | 0.1740 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.1774 | 0.1543 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.1730 | 0.1660 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.1810 | 0.1560 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1429 | 0.0370 |
| fused | loso | knn | none | knn+none | 2 | 0.1620 | 0.1532 |
| fused | loso | logreg | none | logreg+none | 2 | 0.1349 | 0.0317 |
| fused | loso | mlp | none | mlp+none | 2 | 0.2268 | 0.1843 |
| fused | loso | rf | none | rf+none | 2 | 0.1973 | 0.1202 |
| fused | loso | svm | none | svm+none | 2 | 0.2052 | 0.1799 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2714 | 0.2338 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1357 | 0.0703 |
| fused | within_participant | knn | none | knn+none | 10 | 0.2357 | 0.1881 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.3071 | 0.2502 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.2429 | 0.2151 |
| fused | within_participant | rf | none | rf+none | 10 | 0.3214 | 0.2738 |
| fused | within_participant | svm | none | svm+none | 10 | 0.2214 | 0.1717 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1608 | 0.1548 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1388 | 0.0418 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.1602 | 0.1465 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.1301 | 0.0860 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.1691 | 0.1578 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.1564 | 0.1379 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.1528 | 0.1336 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.1190 | 0.0910 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1429 | 0.0370 |
| pupil | loso | knn | none | knn+none | 2 | 0.0952 | 0.0598 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.1349 | 0.0317 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.1576 | 0.1071 |
| pupil | loso | rf | none | rf+none | 2 | 0.1451 | 0.0702 |
| pupil | loso | svm | none | svm+none | 2 | 0.1111 | 0.0653 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3429 | 0.2819 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1429 | 0.0670 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.2857 | 0.2546 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.2714 | 0.1961 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.2357 | 0.1858 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.4214 | 0.3605 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.3000 | 0.2434 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 56
- ConvergenceWarning: lbfgs failed to converge (status=1):: 43
- ConvergenceWarning: lbfgs failed to converge (status=2):: 14


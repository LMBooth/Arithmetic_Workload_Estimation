# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `omit_hardest`
- Final labels: `0.6-1.5, 1.5-2.4, 2.4-3.3, 3.3-4.2, 4.2-5.1, 5.1-6.0`

## Dataset Snapshot
- `eeg`: rows=926, features=183, participants=18, classes=6
- `ecg`: rows=926, features=17, participants=18, classes=6
- `pupil`: rows=926, features=25, participants=18, classes=6
- `fused`: rows=926, features=225, participants=18, classes=6

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `svm+none` (balanced_acc=0.1985, macro_f1=0.1850, n=2)
- `ecg` + `loso` -> `knn+none` (balanced_acc=0.2123, macro_f1=0.1828, n=2)
- `ecg` + `within_participant` -> `gaussian_nb+none` (balanced_acc=0.2500, macro_f1=0.1956, n=10)
- `eeg` + `group_holdout` -> `mlp+none` (balanced_acc=0.2460, macro_f1=0.2419, n=2)
- `eeg` + `loso` -> `svm+none` (balanced_acc=0.2816, macro_f1=0.2071, n=2)
- `eeg` + `within_participant` -> `mlp+none` (balanced_acc=0.4167, macro_f1=0.3706, n=10)
- `fused` + `group_holdout` -> `decision_tree+none` (balanced_acc=0.2557, macro_f1=0.2549, n=2)
- `fused` + `loso` -> `decision_tree+none` (balanced_acc=0.2419, macro_f1=0.2180, n=2)
- `fused` + `within_participant` -> `logreg+none` (balanced_acc=0.3167, macro_f1=0.2792, n=10)
- `pupil` + `group_holdout` -> `rf+none` (balanced_acc=0.1998, macro_f1=0.1795, n=2)
- `pupil` + `loso` -> `decision_tree+none` (balanced_acc=0.2407, macro_f1=0.2166, n=2)
- `pupil` + `within_participant` -> `svm+none` (balanced_acc=0.3917, macro_f1=0.3272, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1637 | 0.1504 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1754 | 0.1501 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.1727 | 0.1650 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.1685 | 0.1496 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.1742 | 0.1612 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.1900 | 0.1841 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.1985 | 0.1850 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.1677 | 0.1533 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1865 | 0.1164 |
| ecg | loso | knn | none | knn+none | 2 | 0.2123 | 0.1828 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.2098 | 0.1591 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.1966 | 0.1713 |
| ecg | loso | rf | none | rf+none | 2 | 0.1964 | 0.1645 |
| ecg | loso | svm | none | svm+none | 2 | 0.2044 | 0.1442 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.1333 | 0.0928 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2500 | 0.1956 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.2333 | 0.2017 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.2250 | 0.1994 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.1917 | 0.1739 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.2417 | 0.1946 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.2083 | 0.1699 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1807 | 0.1593 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1809 | 0.1176 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.2339 | 0.2254 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.2254 | 0.1991 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.2460 | 0.2419 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.2185 | 0.2006 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.2334 | 0.2143 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.2412 | 0.2433 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2221 | 0.1304 |
| eeg | loso | knn | none | knn+none | 2 | 0.2298 | 0.1770 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.1733 | 0.0908 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.2350 | 0.2067 |
| eeg | loso | rf | none | rf+none | 2 | 0.2553 | 0.1701 |
| eeg | loso | svm | none | svm+none | 2 | 0.2816 | 0.2071 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2583 | 0.2201 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3417 | 0.2913 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.3583 | 0.3032 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.4000 | 0.3562 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.4167 | 0.3706 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.3417 | 0.2934 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.3667 | 0.3165 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.2557 | 0.2549 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1617 | 0.0551 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.2136 | 0.2070 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.1507 | 0.0687 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.2069 | 0.1809 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.2372 | 0.1977 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.2050 | 0.1727 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.2419 | 0.2180 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1667 | 0.0480 |
| fused | loso | knn | none | knn+none | 2 | 0.2037 | 0.1837 |
| fused | loso | logreg | none | logreg+none | 2 | 0.1574 | 0.0457 |
| fused | loso | mlp | none | mlp+none | 2 | 0.2222 | 0.1616 |
| fused | loso | rf | none | rf+none | 2 | 0.2130 | 0.1282 |
| fused | loso | svm | none | svm+none | 2 | 0.2037 | 0.1608 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2583 | 0.2187 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2000 | 0.1550 |
| fused | within_participant | knn | none | knn+none | 10 | 0.2833 | 0.2257 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.3167 | 0.2792 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.2750 | 0.2464 |
| fused | within_participant | rf | none | rf+none | 10 | 0.2667 | 0.2351 |
| fused | within_participant | svm | none | svm+none | 10 | 0.2500 | 0.1999 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1769 | 0.1735 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1617 | 0.0551 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.1882 | 0.1674 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.1576 | 0.0725 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.1932 | 0.1622 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.1998 | 0.1795 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.1675 | 0.1220 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.2407 | 0.2166 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1667 | 0.0480 |
| pupil | loso | knn | none | knn+none | 2 | 0.2130 | 0.1759 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.1574 | 0.0457 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.2037 | 0.1239 |
| pupil | loso | rf | none | rf+none | 2 | 0.2130 | 0.1256 |
| pupil | loso | svm | none | svm+none | 2 | 0.2315 | 0.1351 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3750 | 0.3153 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2000 | 0.1561 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.3250 | 0.2612 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.3083 | 0.2462 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.3083 | 0.2307 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.3667 | 0.2987 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.3917 | 0.3272 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 66
- ConvergenceWarning: lbfgs failed to converge (status=1):: 43
- ConvergenceWarning: lbfgs failed to converge (status=2):: 1


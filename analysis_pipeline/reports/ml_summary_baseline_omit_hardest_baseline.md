# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_omit_hardest`
- Final labels: `0.6-1.5, baseline, 1.5-2.4, 2.4-3.3, 3.3-4.2, 4.2-5.1, 5.1-6.0`

## Dataset Snapshot
- `eeg`: rows=1045, features=183, participants=18, classes=7
- `ecg`: rows=1045, features=17, participants=18, classes=7
- `pupil`: rows=1045, features=25, participants=18, classes=7
- `fused`: rows=1045, features=225, participants=18, classes=7

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `decision_tree+none` (balanced_acc=0.1750, macro_f1=0.1728, n=2)
- `ecg` + `loso` -> `mlp+none` (balanced_acc=0.2127, macro_f1=0.1827, n=2)
- `ecg` + `within_participant` -> `rf+none` (balanced_acc=0.2286, macro_f1=0.1836, n=10)
- `eeg` + `group_holdout` -> `logreg+none` (balanced_acc=0.2233, macro_f1=0.1982, n=2)
- `eeg` + `loso` -> `rf+none` (balanced_acc=0.2608, macro_f1=0.1887, n=2)
- `eeg` + `within_participant` -> `mlp+none` (balanced_acc=0.3643, macro_f1=0.3299, n=10)
- `fused` + `group_holdout` -> `svm+none` (balanced_acc=0.2016, macro_f1=0.1837, n=2)
- `fused` + `loso` -> `svm+none` (balanced_acc=0.2256, macro_f1=0.2052, n=2)
- `fused` + `within_participant` -> `rf+none` (balanced_acc=0.3643, macro_f1=0.3348, n=10)
- `pupil` + `group_holdout` -> `mlp+none` (balanced_acc=0.1866, macro_f1=0.1626, n=2)
- `pupil` + `loso` -> `decision_tree+none` (balanced_acc=0.2324, macro_f1=0.2173, n=2)
- `pupil` + `within_participant` -> `rf+none` (balanced_acc=0.3857, macro_f1=0.3360, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1750 | 0.1728 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1348 | 0.1119 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.1386 | 0.1354 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.1359 | 0.1209 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.1318 | 0.1339 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.1506 | 0.1472 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.1670 | 0.1554 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.0916 | 0.0793 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2052 | 0.1272 |
| ecg | loso | knn | none | knn+none | 2 | 0.1866 | 0.1657 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.1810 | 0.1315 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.2127 | 0.1827 |
| ecg | loso | rf | none | rf+none | 2 | 0.1300 | 0.0898 |
| ecg | loso | svm | none | svm+none | 2 | 0.1798 | 0.1379 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2000 | 0.1677 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1929 | 0.1370 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.1929 | 0.1531 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.2214 | 0.1879 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.1714 | 0.1557 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.2286 | 0.1836 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.1929 | 0.1509 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1074 | 0.0968 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1709 | 0.1208 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.1837 | 0.1803 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.2233 | 0.1982 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.2049 | 0.1837 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.1763 | 0.1524 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.2000 | 0.1862 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.2173 | 0.2071 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.2164 | 0.1359 |
| eeg | loso | knn | none | knn+none | 2 | 0.2185 | 0.1721 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.2222 | 0.1689 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.1705 | 0.1450 |
| eeg | loso | rf | none | rf+none | 2 | 0.2608 | 0.1887 |
| eeg | loso | svm | none | svm+none | 2 | 0.2256 | 0.1862 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3000 | 0.2648 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.3429 | 0.2946 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.2929 | 0.2495 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.3500 | 0.2932 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.3643 | 0.3299 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.3143 | 0.2865 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.2714 | 0.2310 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1537 | 0.1533 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1406 | 0.0436 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.1844 | 0.1838 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.1372 | 0.0626 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.1933 | 0.1692 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.1912 | 0.1789 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.2016 | 0.1837 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.2211 | 0.1953 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1429 | 0.0370 |
| fused | loso | knn | none | knn+none | 2 | 0.1349 | 0.1035 |
| fused | loso | logreg | none | logreg+none | 2 | 0.1769 | 0.0894 |
| fused | loso | mlp | none | mlp+none | 2 | 0.1950 | 0.1669 |
| fused | loso | rf | none | rf+none | 2 | 0.2109 | 0.1479 |
| fused | loso | svm | none | svm+none | 2 | 0.2256 | 0.2052 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3071 | 0.2681 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1929 | 0.1583 |
| fused | within_participant | knn | none | knn+none | 10 | 0.2357 | 0.2103 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.3571 | 0.3220 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.3000 | 0.2615 |
| fused | within_participant | rf | none | rf+none | 10 | 0.3643 | 0.3348 |
| fused | within_participant | svm | none | svm+none | 10 | 0.2786 | 0.2089 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1384 | 0.1221 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1406 | 0.0436 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.1743 | 0.1632 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.1399 | 0.0688 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.1866 | 0.1626 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.1860 | 0.1510 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.1825 | 0.1537 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.2324 | 0.2173 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1429 | 0.0370 |
| pupil | loso | knn | none | knn+none | 2 | 0.1667 | 0.1315 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.1429 | 0.0476 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.1769 | 0.1083 |
| pupil | loso | rf | none | rf+none | 2 | 0.1429 | 0.0593 |
| pupil | loso | svm | none | svm+none | 2 | 0.1825 | 0.0946 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3786 | 0.3255 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2214 | 0.1707 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.2857 | 0.2541 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.3000 | 0.2480 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.3000 | 0.2581 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.3857 | 0.3360 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.3286 | 0.2799 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 60
- ConvergenceWarning: lbfgs failed to converge (status=1):: 43
- ConvergenceWarning: lbfgs failed to converge (status=2):: 3


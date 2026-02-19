# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `omit_easiest`
- Final labels: `1.5-2.4, 2.4-3.3, 3.3-4.2, 4.2-5.1, 5.1-6.0, 6.0-6.9`

## Dataset Snapshot
- `eeg`: rows=925, features=183, participants=18, classes=6
- `ecg`: rows=925, features=17, participants=18, classes=6
- `pupil`: rows=925, features=25, participants=18, classes=6
- `fused`: rows=925, features=225, participants=18, classes=6

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `rf+none` (balanced_acc=0.2196, macro_f1=0.2089, n=2)
- `ecg` + `loso` -> `logreg+none` (balanced_acc=0.2191, macro_f1=0.1642, n=2)
- `ecg` + `within_participant` -> `knn+none` (balanced_acc=0.2250, macro_f1=0.1543, n=10)
- `eeg` + `group_holdout` -> `mlp+none` (balanced_acc=0.1990, macro_f1=0.1925, n=2)
- `eeg` + `loso` -> `rf+none` (balanced_acc=0.2262, macro_f1=0.1404, n=2)
- `eeg` + `within_participant` -> `svm+none` (balanced_acc=0.2500, macro_f1=0.2367, n=10)
- `fused` + `group_holdout` -> `rf+none` (balanced_acc=0.2192, macro_f1=0.1904, n=2)
- `fused` + `loso` -> `svm+none` (balanced_acc=0.2222, macro_f1=0.1308, n=2)
- `fused` + `within_participant` -> `decision_tree+none` (balanced_acc=0.2667, macro_f1=0.2556, n=10)
- `pupil` + `group_holdout` -> `decision_tree+none` (balanced_acc=0.2629, macro_f1=0.2474, n=2)
- `pupil` + `loso` -> `decision_tree+none` (balanced_acc=0.2731, macro_f1=0.2389, n=2)
- `pupil` + `within_participant` -> `knn+none` (balanced_acc=0.3833, macro_f1=0.3401, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1488 | 0.1361 |
| ecg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1929 | 0.1658 |
| ecg | group_holdout | knn | none | knn+none | 2 | 0.1991 | 0.1933 |
| ecg | group_holdout | logreg | none | logreg+none | 2 | 0.1565 | 0.1372 |
| ecg | group_holdout | mlp | none | mlp+none | 2 | 0.1815 | 0.1703 |
| ecg | group_holdout | rf | none | rf+none | 2 | 0.2196 | 0.2089 |
| ecg | group_holdout | svm | none | svm+none | 2 | 0.2105 | 0.1978 |
| ecg | loso | decision_tree | none | decision_tree+none | 2 | 0.1076 | 0.1046 |
| ecg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1865 | 0.1139 |
| ecg | loso | knn | none | knn+none | 2 | 0.1400 | 0.1323 |
| ecg | loso | logreg | none | logreg+none | 2 | 0.2191 | 0.1642 |
| ecg | loso | mlp | none | mlp+none | 2 | 0.1662 | 0.1322 |
| ecg | loso | rf | none | rf+none | 2 | 0.1870 | 0.1682 |
| ecg | loso | svm | none | svm+none | 2 | 0.1911 | 0.1441 |
| ecg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.1250 | 0.1025 |
| ecg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2250 | 0.1612 |
| ecg | within_participant | knn | none | knn+none | 10 | 0.2250 | 0.1543 |
| ecg | within_participant | logreg | none | logreg+none | 10 | 0.2167 | 0.1829 |
| ecg | within_participant | mlp | none | mlp+none | 10 | 0.2083 | 0.1642 |
| ecg | within_participant | rf | none | rf+none | 10 | 0.2083 | 0.1496 |
| ecg | within_participant | svm | none | svm+none | 10 | 0.2167 | 0.1635 |
| eeg | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1981 | 0.1814 |
| eeg | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1832 | 0.1222 |
| eeg | group_holdout | knn | none | knn+none | 2 | 0.1847 | 0.1732 |
| eeg | group_holdout | logreg | none | logreg+none | 2 | 0.1867 | 0.1725 |
| eeg | group_holdout | mlp | none | mlp+none | 2 | 0.1990 | 0.1925 |
| eeg | group_holdout | rf | none | rf+none | 2 | 0.1803 | 0.1707 |
| eeg | group_holdout | svm | none | svm+none | 2 | 0.1750 | 0.1591 |
| eeg | loso | decision_tree | none | decision_tree+none | 2 | 0.1334 | 0.1300 |
| eeg | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1890 | 0.0978 |
| eeg | loso | knn | none | knn+none | 2 | 0.1442 | 0.1093 |
| eeg | loso | logreg | none | logreg+none | 2 | 0.1888 | 0.1267 |
| eeg | loso | mlp | none | mlp+none | 2 | 0.1743 | 0.1206 |
| eeg | loso | rf | none | rf+none | 2 | 0.2262 | 0.1404 |
| eeg | loso | svm | none | svm+none | 2 | 0.1997 | 0.1230 |
| eeg | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2000 | 0.1821 |
| eeg | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.2500 | 0.2211 |
| eeg | within_participant | knn | none | knn+none | 10 | 0.2083 | 0.1817 |
| eeg | within_participant | logreg | none | logreg+none | 10 | 0.2500 | 0.2215 |
| eeg | within_participant | mlp | none | mlp+none | 10 | 0.2250 | 0.2034 |
| eeg | within_participant | rf | none | rf+none | 10 | 0.2500 | 0.2269 |
| eeg | within_participant | svm | none | svm+none | 10 | 0.2500 | 0.2367 |
| fused | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.1909 | 0.1880 |
| fused | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1595 | 0.0567 |
| fused | group_holdout | knn | none | knn+none | 2 | 0.1677 | 0.1665 |
| fused | group_holdout | logreg | none | logreg+none | 2 | 0.1647 | 0.1097 |
| fused | group_holdout | mlp | none | mlp+none | 2 | 0.2050 | 0.1806 |
| fused | group_holdout | rf | none | rf+none | 2 | 0.2192 | 0.1904 |
| fused | group_holdout | svm | none | svm+none | 2 | 0.1866 | 0.1644 |
| fused | loso | decision_tree | none | decision_tree+none | 2 | 0.1875 | 0.1676 |
| fused | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1667 | 0.0480 |
| fused | loso | knn | none | knn+none | 2 | 0.1678 | 0.1550 |
| fused | loso | logreg | none | logreg+none | 2 | 0.1296 | 0.0467 |
| fused | loso | mlp | none | mlp+none | 2 | 0.2072 | 0.1697 |
| fused | loso | rf | none | rf+none | 2 | 0.2037 | 0.1266 |
| fused | loso | svm | none | svm+none | 2 | 0.2222 | 0.1308 |
| fused | within_participant | decision_tree | none | decision_tree+none | 10 | 0.2667 | 0.2556 |
| fused | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1583 | 0.0791 |
| fused | within_participant | knn | none | knn+none | 10 | 0.2167 | 0.1842 |
| fused | within_participant | logreg | none | logreg+none | 10 | 0.2417 | 0.2137 |
| fused | within_participant | mlp | none | mlp+none | 10 | 0.2083 | 0.1746 |
| fused | within_participant | rf | none | rf+none | 10 | 0.2333 | 0.2072 |
| fused | within_participant | svm | none | svm+none | 10 | 0.2333 | 0.1923 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 2 | 0.2629 | 0.2474 |
| pupil | group_holdout | gaussian_nb | none | gaussian_nb+none | 2 | 0.1595 | 0.0567 |
| pupil | group_holdout | knn | none | knn+none | 2 | 0.1698 | 0.1515 |
| pupil | group_holdout | logreg | none | logreg+none | 2 | 0.1580 | 0.0946 |
| pupil | group_holdout | mlp | none | mlp+none | 2 | 0.1702 | 0.1478 |
| pupil | group_holdout | rf | none | rf+none | 2 | 0.1934 | 0.1765 |
| pupil | group_holdout | svm | none | svm+none | 2 | 0.1423 | 0.1031 |
| pupil | loso | decision_tree | none | decision_tree+none | 2 | 0.2731 | 0.2389 |
| pupil | loso | gaussian_nb | none | gaussian_nb+none | 2 | 0.1667 | 0.0480 |
| pupil | loso | knn | none | knn+none | 2 | 0.1204 | 0.0775 |
| pupil | loso | logreg | none | logreg+none | 2 | 0.1296 | 0.0482 |
| pupil | loso | mlp | none | mlp+none | 2 | 0.1852 | 0.1100 |
| pupil | loso | rf | none | rf+none | 2 | 0.1759 | 0.0834 |
| pupil | loso | svm | none | svm+none | 2 | 0.1204 | 0.0766 |
| pupil | within_participant | decision_tree | none | decision_tree+none | 10 | 0.3167 | 0.2504 |
| pupil | within_participant | gaussian_nb | none | gaussian_nb+none | 10 | 0.1750 | 0.1003 |
| pupil | within_participant | knn | none | knn+none | 10 | 0.3833 | 0.3401 |
| pupil | within_participant | logreg | none | logreg+none | 10 | 0.1750 | 0.1372 |
| pupil | within_participant | mlp | none | mlp+none | 10 | 0.3333 | 0.2457 |
| pupil | within_participant | rf | none | rf+none | 10 | 0.3667 | 0.3156 |
| pupil | within_participant | svm | none | svm+none | 10 | 0.2917 | 0.2110 |

## Warning Summary
- ConvergenceWarning: Stochastic Optimizer: Maximum iterations (800) reached and the optimization hasn't converged yet.: 56
- ConvergenceWarning: lbfgs failed to converge (status=1):: 42
- ConvergenceWarning: lbfgs failed to converge (status=2):: 25


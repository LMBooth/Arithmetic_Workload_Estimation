# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `lstm1d, gru1d, cnn1d, transformer, bilstm1d, bigru1d, cnn1d_deep, transformer_xl`
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
- `ecg` + `group_holdout` -> `cnn1d+none` (balanced_acc=0.1779, macro_f1=0.1573, n=2)
- `ecg` + `loso` -> `bilstm1d+none` (balanced_acc=0.2306, macro_f1=0.1669, n=2)
- `ecg` + `within_participant` -> `cnn1d+none` (balanced_acc=0.2214, macro_f1=0.1719, n=10)
- `eeg` + `group_holdout` -> `cnn1d+none` (balanced_acc=0.2088, macro_f1=0.1893, n=2)
- `eeg` + `loso` -> `gru1d+none` (balanced_acc=0.2459, macro_f1=0.1580, n=2)
- `eeg` + `within_participant` -> `cnn1d+none` (balanced_acc=0.2500, macro_f1=0.2155, n=10)
- `fused` + `group_holdout` -> `gru1d+none` (balanced_acc=0.1757, macro_f1=0.1285, n=2)
- `fused` + `loso` -> `bilstm1d+none` (balanced_acc=0.1757, macro_f1=0.0710, n=2)
- `fused` + `within_participant` -> `cnn1d+none` (balanced_acc=0.2500, macro_f1=0.1875, n=10)
- `pupil` + `group_holdout` -> `gru1d+none` (balanced_acc=0.1669, macro_f1=0.1160, n=2)
- `pupil` + `loso` -> `bilstm1d+none` (balanced_acc=0.1576, macro_f1=0.0751, n=2)
- `pupil` + `within_participant` -> `cnn1d_deep+none` (balanced_acc=0.3000, macro_f1=0.2414, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1339 | 0.1046 |
| ecg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1563 | 0.1235 |
| ecg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1779 | 0.1573 |
| ecg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1526 | 0.1380 |
| ecg | group_holdout | gru1d | none | gru1d+none | 2 | 0.1559 | 0.1090 |
| ecg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1460 | 0.1287 |
| ecg | group_holdout | transformer | none | transformer+none | 2 | 0.1613 | 0.1311 |
| ecg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1473 | 0.1161 |
| ecg | loso | bigru1d | none | bigru1d+none | 2 | 0.1495 | 0.1105 |
| ecg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.2306 | 0.1669 |
| ecg | loso | cnn1d | none | cnn1d+none | 2 | 0.1674 | 0.1442 |
| ecg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1832 | 0.1575 |
| ecg | loso | gru1d | none | gru1d+none | 2 | 0.1616 | 0.1153 |
| ecg | loso | lstm1d | none | lstm1d+none | 2 | 0.1512 | 0.1036 |
| ecg | loso | transformer | none | transformer+none | 2 | 0.1801 | 0.1282 |
| ecg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1881 | 0.1193 |
| ecg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.2143 | 0.1534 |
| ecg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1643 | 0.0707 |
| ecg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2214 | 0.1719 |
| ecg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.1786 | 0.1467 |
| ecg | within_participant | gru1d | none | gru1d+none | 10 | 0.2071 | 0.1190 |
| ecg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1643 | 0.0787 |
| ecg | within_participant | transformer | none | transformer+none | 10 | 0.2071 | 0.1404 |
| ecg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1786 | 0.1436 |
| eeg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1522 | 0.1212 |
| eeg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1881 | 0.1464 |
| eeg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.2088 | 0.1893 |
| eeg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1701 | 0.1487 |
| eeg | group_holdout | gru1d | none | gru1d+none | 2 | 0.1648 | 0.1205 |
| eeg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.2037 | 0.1712 |
| eeg | group_holdout | transformer | none | transformer+none | 2 | 0.1410 | 0.1243 |
| eeg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1624 | 0.1227 |
| eeg | loso | bigru1d | none | bigru1d+none | 2 | 0.2334 | 0.1442 |
| eeg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1620 | 0.0876 |
| eeg | loso | cnn1d | none | cnn1d+none | 2 | 0.2425 | 0.1662 |
| eeg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2392 | 0.1675 |
| eeg | loso | gru1d | none | gru1d+none | 2 | 0.2459 | 0.1580 |
| eeg | loso | lstm1d | none | lstm1d+none | 2 | 0.2313 | 0.1554 |
| eeg | loso | transformer | none | transformer+none | 2 | 0.1973 | 0.1464 |
| eeg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.2255 | 0.1769 |
| eeg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1857 | 0.1063 |
| eeg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.2071 | 0.1160 |
| eeg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2500 | 0.2155 |
| eeg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2143 | 0.2049 |
| eeg | within_participant | gru1d | none | gru1d+none | 10 | 0.2000 | 0.1056 |
| eeg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1714 | 0.0876 |
| eeg | within_participant | transformer | none | transformer+none | 10 | 0.2357 | 0.1351 |
| eeg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.2429 | 0.1887 |
| fused | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1587 | 0.1229 |
| fused | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1650 | 0.1114 |
| fused | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1475 | 0.0591 |
| fused | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1467 | 0.0611 |
| fused | group_holdout | gru1d | none | gru1d+none | 2 | 0.1757 | 0.1285 |
| fused | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1642 | 0.0891 |
| fused | group_holdout | transformer | none | transformer+none | 2 | 0.1429 | 0.0371 |
| fused | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0371 |
| fused | loso | bigru1d | none | bigru1d+none | 2 | 0.1474 | 0.0618 |
| fused | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1757 | 0.0710 |
| fused | loso | cnn1d | none | cnn1d+none | 2 | 0.1429 | 0.0373 |
| fused | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1429 | 0.0373 |
| fused | loso | gru1d | none | gru1d+none | 2 | 0.1451 | 0.0577 |
| fused | loso | lstm1d | none | lstm1d+none | 2 | 0.1145 | 0.0351 |
| fused | loso | transformer | none | transformer+none | 2 | 0.1429 | 0.0370 |
| fused | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0370 |
| fused | within_participant | bigru1d | none | bigru1d+none | 10 | 0.2214 | 0.1485 |
| fused | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1786 | 0.0932 |
| fused | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2500 | 0.1875 |
| fused | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2286 | 0.1650 |
| fused | within_participant | gru1d | none | gru1d+none | 10 | 0.1500 | 0.0871 |
| fused | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1357 | 0.0554 |
| fused | within_participant | transformer | none | transformer+none | 10 | 0.2071 | 0.0975 |
| fused | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1857 | 0.1115 |
| pupil | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1579 | 0.1131 |
| pupil | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1542 | 0.1000 |
| pupil | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1506 | 0.0673 |
| pupil | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1437 | 0.0560 |
| pupil | group_holdout | gru1d | none | gru1d+none | 2 | 0.1669 | 0.1160 |
| pupil | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1447 | 0.0754 |
| pupil | group_holdout | transformer | none | transformer+none | 2 | 0.1429 | 0.0371 |
| pupil | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0371 |
| pupil | loso | bigru1d | none | bigru1d+none | 2 | 0.1474 | 0.0658 |
| pupil | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1576 | 0.0751 |
| pupil | loso | cnn1d | none | cnn1d+none | 2 | 0.1349 | 0.0352 |
| pupil | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1429 | 0.0373 |
| pupil | loso | gru1d | none | gru1d+none | 2 | 0.1553 | 0.0638 |
| pupil | loso | lstm1d | none | lstm1d+none | 2 | 0.1293 | 0.0711 |
| pupil | loso | transformer | none | transformer+none | 2 | 0.1429 | 0.0370 |
| pupil | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0370 |
| pupil | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1857 | 0.1081 |
| pupil | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1929 | 0.1165 |
| pupil | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2857 | 0.2126 |
| pupil | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.3000 | 0.2414 |
| pupil | within_participant | gru1d | none | gru1d+none | 10 | 0.1357 | 0.0755 |
| pupil | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1357 | 0.0556 |
| pupil | within_participant | transformer | none | transformer+none | 10 | 0.1786 | 0.0861 |
| pupil | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.2071 | 0.1303 |

## Warning Summary
- none


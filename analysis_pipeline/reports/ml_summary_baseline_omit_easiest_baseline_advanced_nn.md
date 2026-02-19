# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `lstm1d, gru1d, cnn1d, transformer, bilstm1d, bigru1d, cnn1d_deep, transformer_xl`
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
- `ecg` + `group_holdout` -> `transformer_xl+none` (balanced_acc=0.1987, macro_f1=0.1582, n=2)
- `ecg` + `loso` -> `bilstm1d+none` (balanced_acc=0.1705, macro_f1=0.1330, n=2)
- `ecg` + `within_participant` -> `cnn1d+none` (balanced_acc=0.2357, macro_f1=0.1888, n=10)
- `eeg` + `group_holdout` -> `cnn1d_deep+none` (balanced_acc=0.1875, macro_f1=0.1693, n=2)
- `eeg` + `loso` -> `bilstm1d+none` (balanced_acc=0.2242, macro_f1=0.1419, n=2)
- `eeg` + `within_participant` -> `cnn1d+none` (balanced_acc=0.2929, macro_f1=0.2237, n=10)
- `fused` + `group_holdout` -> `bilstm1d+none` (balanced_acc=0.1563, macro_f1=0.1228, n=2)
- `fused` + `loso` -> `cnn1d+none` (balanced_acc=0.1429, macro_f1=0.0370, n=2)
- `fused` + `within_participant` -> `bilstm1d+none` (balanced_acc=0.1857, macro_f1=0.1240, n=10)
- `pupil` + `group_holdout` -> `bigru1d+none` (balanced_acc=0.1622, macro_f1=0.1204, n=2)
- `pupil` + `loso` -> `cnn1d+none` (balanced_acc=0.1429, macro_f1=0.0373, n=2)
- `pupil` + `within_participant` -> `lstm1d+none` (balanced_acc=0.1929, macro_f1=0.0960, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1783 | 0.1621 |
| ecg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1401 | 0.1167 |
| ecg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1522 | 0.1469 |
| ecg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1239 | 0.1121 |
| ecg | group_holdout | gru1d | none | gru1d+none | 2 | 0.1785 | 0.1531 |
| ecg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1372 | 0.1269 |
| ecg | group_holdout | transformer | none | transformer+none | 2 | 0.1748 | 0.1510 |
| ecg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1987 | 0.1582 |
| ecg | loso | bigru1d | none | bigru1d+none | 2 | 0.1368 | 0.1122 |
| ecg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1705 | 0.1330 |
| ecg | loso | cnn1d | none | cnn1d+none | 2 | 0.1569 | 0.1208 |
| ecg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1450 | 0.1200 |
| ecg | loso | gru1d | none | gru1d+none | 2 | 0.1470 | 0.0951 |
| ecg | loso | lstm1d | none | lstm1d+none | 2 | 0.1189 | 0.1030 |
| ecg | loso | transformer | none | transformer+none | 2 | 0.1266 | 0.0986 |
| ecg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1053 | 0.0751 |
| ecg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1857 | 0.1118 |
| ecg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1500 | 0.0692 |
| ecg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2357 | 0.1888 |
| ecg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2143 | 0.1860 |
| ecg | within_participant | gru1d | none | gru1d+none | 10 | 0.1286 | 0.0583 |
| ecg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1786 | 0.0717 |
| ecg | within_participant | transformer | none | transformer+none | 10 | 0.1929 | 0.1201 |
| ecg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1571 | 0.1078 |
| eeg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1637 | 0.1442 |
| eeg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1327 | 0.0955 |
| eeg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1759 | 0.1540 |
| eeg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1875 | 0.1693 |
| eeg | group_holdout | gru1d | none | gru1d+none | 2 | 0.1799 | 0.1499 |
| eeg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1380 | 0.1139 |
| eeg | group_holdout | transformer | none | transformer+none | 2 | 0.1626 | 0.1117 |
| eeg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1580 | 0.1535 |
| eeg | loso | bigru1d | none | bigru1d+none | 2 | 0.2095 | 0.1390 |
| eeg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.2242 | 0.1419 |
| eeg | loso | cnn1d | none | cnn1d+none | 2 | 0.2071 | 0.1614 |
| eeg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1665 | 0.1280 |
| eeg | loso | gru1d | none | gru1d+none | 2 | 0.2061 | 0.1318 |
| eeg | loso | lstm1d | none | lstm1d+none | 2 | 0.1845 | 0.1033 |
| eeg | loso | transformer | none | transformer+none | 2 | 0.2075 | 0.1534 |
| eeg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1756 | 0.1253 |
| eeg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.2357 | 0.1677 |
| eeg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.2214 | 0.1487 |
| eeg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2929 | 0.2237 |
| eeg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2786 | 0.2256 |
| eeg | within_participant | gru1d | none | gru1d+none | 10 | 0.2071 | 0.1170 |
| eeg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1857 | 0.0968 |
| eeg | within_participant | transformer | none | transformer+none | 10 | 0.2500 | 0.1586 |
| eeg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.2857 | 0.2145 |
| fused | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1539 | 0.1233 |
| fused | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1563 | 0.1228 |
| fused | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1515 | 0.0652 |
| fused | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1526 | 0.0694 |
| fused | group_holdout | gru1d | none | gru1d+none | 2 | 0.1388 | 0.1011 |
| fused | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1473 | 0.1050 |
| fused | group_holdout | transformer | none | transformer+none | 2 | 0.1429 | 0.0372 |
| fused | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0372 |
| fused | loso | bigru1d | none | bigru1d+none | 2 | 0.1179 | 0.0380 |
| fused | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1156 | 0.0552 |
| fused | loso | cnn1d | none | cnn1d+none | 2 | 0.1429 | 0.0370 |
| fused | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1349 | 0.0352 |
| fused | loso | gru1d | none | gru1d+none | 2 | 0.1224 | 0.0551 |
| fused | loso | lstm1d | none | lstm1d+none | 2 | 0.1417 | 0.0667 |
| fused | loso | transformer | none | transformer+none | 2 | 0.1429 | 0.0370 |
| fused | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0370 |
| fused | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1643 | 0.1106 |
| fused | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1857 | 0.1240 |
| fused | within_participant | cnn1d | none | cnn1d+none | 10 | 0.1643 | 0.0826 |
| fused | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.1429 | 0.0697 |
| fused | within_participant | gru1d | none | gru1d+none | 10 | 0.1786 | 0.0820 |
| fused | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1714 | 0.0791 |
| fused | within_participant | transformer | none | transformer+none | 10 | 0.1429 | 0.0376 |
| fused | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1286 | 0.0328 |
| pupil | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1622 | 0.1204 |
| pupil | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1132 | 0.0860 |
| pupil | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1427 | 0.0610 |
| pupil | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1496 | 0.0629 |
| pupil | group_holdout | gru1d | none | gru1d+none | 2 | 0.1267 | 0.0930 |
| pupil | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1481 | 0.1070 |
| pupil | group_holdout | transformer | none | transformer+none | 2 | 0.1429 | 0.0372 |
| pupil | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0372 |
| pupil | loso | bigru1d | none | bigru1d+none | 2 | 0.1224 | 0.0325 |
| pupil | loso | bilstm1d | none | bilstm1d+none | 2 | 0.0986 | 0.0434 |
| pupil | loso | cnn1d | none | cnn1d+none | 2 | 0.1429 | 0.0373 |
| pupil | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1429 | 0.0373 |
| pupil | loso | gru1d | none | gru1d+none | 2 | 0.1179 | 0.0542 |
| pupil | loso | lstm1d | none | lstm1d+none | 2 | 0.1338 | 0.0590 |
| pupil | loso | transformer | none | transformer+none | 2 | 0.1429 | 0.0370 |
| pupil | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1429 | 0.0370 |
| pupil | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1786 | 0.1328 |
| pupil | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1714 | 0.1007 |
| pupil | within_participant | cnn1d | none | cnn1d+none | 10 | 0.1714 | 0.0984 |
| pupil | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.1357 | 0.0740 |
| pupil | within_participant | gru1d | none | gru1d+none | 10 | 0.1786 | 0.0817 |
| pupil | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1929 | 0.0960 |
| pupil | within_participant | transformer | none | transformer+none | 10 | 0.1286 | 0.0328 |
| pupil | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1357 | 0.0400 |

## Warning Summary
- none


# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `lstm1d, gru1d, cnn1d, transformer, bilstm1d, bigru1d, cnn1d_deep, transformer_xl`
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
- `ecg` + `group_holdout` -> `transformer+none` (balanced_acc=0.1555, macro_f1=0.1202, n=2)
- `ecg` + `loso` -> `cnn1d_deep+none` (balanced_acc=0.1474, macro_f1=0.1234, n=2)
- `ecg` + `within_participant` -> `cnn1d_deep+none` (balanced_acc=0.2000, macro_f1=0.1689, n=10)
- `eeg` + `group_holdout` -> `cnn1d_deep+none` (balanced_acc=0.1611, macro_f1=0.1434, n=2)
- `eeg` + `loso` -> `cnn1d_deep+none` (balanced_acc=0.2411, macro_f1=0.1771, n=2)
- `eeg` + `within_participant` -> `cnn1d_deep+none` (balanced_acc=0.2188, macro_f1=0.1844, n=10)
- `fused` + `group_holdout` -> `bilstm1d+none` (balanced_acc=0.1501, macro_f1=0.1205, n=2)
- `fused` + `loso` -> `bilstm1d+none` (balanced_acc=0.1637, macro_f1=0.0827, n=2)
- `fused` + `within_participant` -> `bilstm1d+none` (balanced_acc=0.1688, macro_f1=0.0887, n=10)
- `pupil` + `group_holdout` -> `lstm1d+none` (balanced_acc=0.1474, macro_f1=0.1207, n=2)
- `pupil` + `loso` -> `gru1d+none` (balanced_acc=0.1607, macro_f1=0.0762, n=2)
- `pupil` + `within_participant` -> `bilstm1d+none` (balanced_acc=0.2062, macro_f1=0.1211, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1440 | 0.1326 |
| ecg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1280 | 0.1136 |
| ecg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1503 | 0.1367 |
| ecg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1460 | 0.1297 |
| ecg | group_holdout | gru1d | none | gru1d+none | 2 | 0.1292 | 0.1027 |
| ecg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1330 | 0.1148 |
| ecg | group_holdout | transformer | none | transformer+none | 2 | 0.1555 | 0.1202 |
| ecg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1427 | 0.1178 |
| ecg | loso | bigru1d | none | bigru1d+none | 2 | 0.0978 | 0.0675 |
| ecg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1327 | 0.1136 |
| ecg | loso | cnn1d | none | cnn1d+none | 2 | 0.1177 | 0.1036 |
| ecg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1474 | 0.1234 |
| ecg | loso | gru1d | none | gru1d+none | 2 | 0.0843 | 0.0695 |
| ecg | loso | lstm1d | none | lstm1d+none | 2 | 0.1259 | 0.0533 |
| ecg | loso | transformer | none | transformer+none | 2 | 0.1189 | 0.0823 |
| ecg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1257 | 0.0785 |
| ecg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1750 | 0.1076 |
| ecg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.2000 | 0.1246 |
| ecg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.1812 | 0.1526 |
| ecg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2000 | 0.1689 |
| ecg | within_participant | gru1d | none | gru1d+none | 10 | 0.1500 | 0.0758 |
| ecg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1437 | 0.0682 |
| ecg | within_participant | transformer | none | transformer+none | 10 | 0.1688 | 0.1021 |
| ecg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1625 | 0.1210 |
| eeg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1388 | 0.1143 |
| eeg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1288 | 0.1001 |
| eeg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1482 | 0.1198 |
| eeg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1611 | 0.1434 |
| eeg | group_holdout | gru1d | none | gru1d+none | 2 | 0.1454 | 0.1171 |
| eeg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1364 | 0.0991 |
| eeg | group_holdout | transformer | none | transformer+none | 2 | 0.1394 | 0.0853 |
| eeg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1455 | 0.1150 |
| eeg | loso | bigru1d | none | bigru1d+none | 2 | 0.2003 | 0.1440 |
| eeg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1802 | 0.1079 |
| eeg | loso | cnn1d | none | cnn1d+none | 2 | 0.1825 | 0.1184 |
| eeg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2411 | 0.1771 |
| eeg | loso | gru1d | none | gru1d+none | 2 | 0.1684 | 0.0894 |
| eeg | loso | lstm1d | none | lstm1d+none | 2 | 0.1704 | 0.0731 |
| eeg | loso | transformer | none | transformer+none | 2 | 0.1910 | 0.1667 |
| eeg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1448 | 0.1033 |
| eeg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1812 | 0.1134 |
| eeg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1375 | 0.0756 |
| eeg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2188 | 0.1735 |
| eeg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2188 | 0.1844 |
| eeg | within_participant | gru1d | none | gru1d+none | 10 | 0.1750 | 0.0994 |
| eeg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.2000 | 0.0979 |
| eeg | within_participant | transformer | none | transformer+none | 10 | 0.1625 | 0.1054 |
| eeg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1875 | 0.1412 |
| fused | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1467 | 0.1125 |
| fused | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1501 | 0.1205 |
| fused | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1327 | 0.0553 |
| fused | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1327 | 0.0547 |
| fused | group_holdout | gru1d | none | gru1d+none | 2 | 0.1366 | 0.0875 |
| fused | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1290 | 0.1005 |
| fused | group_holdout | transformer | none | transformer+none | 2 | 0.1250 | 0.0288 |
| fused | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1250 | 0.0288 |
| fused | loso | bigru1d | none | bigru1d+none | 2 | 0.1528 | 0.1035 |
| fused | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1637 | 0.0827 |
| fused | loso | cnn1d | none | cnn1d+none | 2 | 0.1250 | 0.0288 |
| fused | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1181 | 0.0272 |
| fused | loso | gru1d | none | gru1d+none | 2 | 0.1498 | 0.0659 |
| fused | loso | lstm1d | none | lstm1d+none | 2 | 0.1567 | 0.0737 |
| fused | loso | transformer | none | transformer+none | 2 | 0.1250 | 0.0287 |
| fused | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1250 | 0.0287 |
| fused | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1625 | 0.0863 |
| fused | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.1688 | 0.0887 |
| fused | within_participant | cnn1d | none | cnn1d+none | 10 | 0.1375 | 0.0466 |
| fused | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.1250 | 0.0536 |
| fused | within_participant | gru1d | none | gru1d+none | 10 | 0.1313 | 0.0650 |
| fused | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1625 | 0.0627 |
| fused | within_participant | transformer | none | transformer+none | 10 | 0.1187 | 0.0273 |
| fused | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1187 | 0.0338 |
| pupil | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.1370 | 0.0990 |
| pupil | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.1387 | 0.1120 |
| pupil | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.1205 | 0.0457 |
| pupil | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1292 | 0.0525 |
| pupil | group_holdout | gru1d | none | gru1d+none | 2 | 0.1219 | 0.0716 |
| pupil | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.1474 | 0.1207 |
| pupil | group_holdout | transformer | none | transformer+none | 2 | 0.1250 | 0.0288 |
| pupil | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.1250 | 0.0288 |
| pupil | loso | bigru1d | none | bigru1d+none | 2 | 0.1389 | 0.0854 |
| pupil | loso | bilstm1d | none | bilstm1d+none | 2 | 0.1518 | 0.0762 |
| pupil | loso | cnn1d | none | cnn1d+none | 2 | 0.1250 | 0.0288 |
| pupil | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.1250 | 0.0288 |
| pupil | loso | gru1d | none | gru1d+none | 2 | 0.1607 | 0.0762 |
| pupil | loso | lstm1d | none | lstm1d+none | 2 | 0.1240 | 0.0638 |
| pupil | loso | transformer | none | transformer+none | 2 | 0.1250 | 0.0287 |
| pupil | loso | transformer_xl | none | transformer_xl+none | 2 | 0.1250 | 0.0287 |
| pupil | within_participant | bigru1d | none | bigru1d+none | 10 | 0.1562 | 0.0822 |
| pupil | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.2062 | 0.1211 |
| pupil | within_participant | cnn1d | none | cnn1d+none | 10 | 0.1250 | 0.0565 |
| pupil | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.1562 | 0.0874 |
| pupil | within_participant | gru1d | none | gru1d+none | 10 | 0.1313 | 0.0650 |
| pupil | within_participant | lstm1d | none | lstm1d+none | 10 | 0.1750 | 0.0714 |
| pupil | within_participant | transformer | none | transformer+none | 10 | 0.1125 | 0.0254 |
| pupil | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.1313 | 0.0379 |

## Warning Summary
- none


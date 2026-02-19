# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `lstm1d, gru1d, cnn1d, transformer, bilstm1d, bigru1d, cnn1d_deep, transformer_xl`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_grouped_4class_omit_hardest`
- Final labels: `low_1_2, baseline, mid_3_4, high_5_6`

## Dataset Snapshot
- `eeg`: rows=1045, features=183, participants=18, classes=4
- `ecg`: rows=1045, features=17, participants=18, classes=4
- `pupil`: rows=1045, features=25, participants=18, classes=4
- `fused`: rows=1045, features=225, participants=18, classes=4

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `transformer+none` (balanced_acc=0.3097, macro_f1=0.2349, n=2)
- `ecg` + `loso` -> `gru1d+none` (balanced_acc=0.3046, macro_f1=0.2134, n=2)
- `ecg` + `within_participant` -> `bilstm1d+none` (balanced_acc=0.3396, macro_f1=0.2472, n=10)
- `eeg` + `group_holdout` -> `gru1d+none` (balanced_acc=0.3441, macro_f1=0.3191, n=2)
- `eeg` + `loso` -> `cnn1d+none` (balanced_acc=0.4344, macro_f1=0.3706, n=2)
- `eeg` + `within_participant` -> `cnn1d+none` (balanced_acc=0.4750, macro_f1=0.4254, n=10)
- `fused` + `group_holdout` -> `gru1d+none` (balanced_acc=0.2949, macro_f1=0.2487, n=2)
- `fused` + `loso` -> `lstm1d+none` (balanced_acc=0.3542, macro_f1=0.2254, n=2)
- `fused` + `within_participant` -> `cnn1d_deep+none` (balanced_acc=0.4333, macro_f1=0.3693, n=10)
- `pupil` + `group_holdout` -> `bigru1d+none` (balanced_acc=0.2900, macro_f1=0.2567, n=2)
- `pupil` + `loso` -> `bilstm1d+none` (balanced_acc=0.2901, macro_f1=0.2355, n=2)
- `pupil` + `within_participant` -> `cnn1d_deep+none` (balanced_acc=0.4625, macro_f1=0.3782, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.2526 | 0.2009 |
| ecg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.2103 | 0.1648 |
| ecg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.2727 | 0.2506 |
| ecg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2480 | 0.2457 |
| ecg | group_holdout | gru1d | none | gru1d+none | 2 | 0.2420 | 0.2032 |
| ecg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.2471 | 0.1646 |
| ecg | group_holdout | transformer | none | transformer+none | 2 | 0.3097 | 0.2349 |
| ecg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.3064 | 0.2400 |
| ecg | loso | bigru1d | none | bigru1d+none | 2 | 0.2808 | 0.1711 |
| ecg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.2917 | 0.1735 |
| ecg | loso | cnn1d | none | cnn1d+none | 2 | 0.2868 | 0.2558 |
| ecg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2870 | 0.2584 |
| ecg | loso | gru1d | none | gru1d+none | 2 | 0.3046 | 0.2134 |
| ecg | loso | lstm1d | none | lstm1d+none | 2 | 0.2609 | 0.1495 |
| ecg | loso | transformer | none | transformer+none | 2 | 0.2817 | 0.2002 |
| ecg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.2624 | 0.2150 |
| ecg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.2625 | 0.2025 |
| ecg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.3396 | 0.2472 |
| ecg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.2729 | 0.2416 |
| ecg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.2646 | 0.2374 |
| ecg | within_participant | gru1d | none | gru1d+none | 10 | 0.2708 | 0.1861 |
| ecg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.2729 | 0.1971 |
| ecg | within_participant | transformer | none | transformer+none | 10 | 0.3187 | 0.2284 |
| ecg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.3125 | 0.2791 |
| eeg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.3297 | 0.3148 |
| eeg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.3390 | 0.3101 |
| eeg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.3160 | 0.2972 |
| eeg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3327 | 0.2993 |
| eeg | group_holdout | gru1d | none | gru1d+none | 2 | 0.3441 | 0.3191 |
| eeg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.3154 | 0.2880 |
| eeg | group_holdout | transformer | none | transformer+none | 2 | 0.2650 | 0.2153 |
| eeg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.3188 | 0.2875 |
| eeg | loso | bigru1d | none | bigru1d+none | 2 | 0.3487 | 0.3114 |
| eeg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.3531 | 0.2912 |
| eeg | loso | cnn1d | none | cnn1d+none | 2 | 0.4344 | 0.3706 |
| eeg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3738 | 0.3312 |
| eeg | loso | gru1d | none | gru1d+none | 2 | 0.3512 | 0.2761 |
| eeg | loso | lstm1d | none | lstm1d+none | 2 | 0.2825 | 0.2069 |
| eeg | loso | transformer | none | transformer+none | 2 | 0.4086 | 0.3740 |
| eeg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.3430 | 0.3071 |
| eeg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.3812 | 0.3030 |
| eeg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.3500 | 0.2855 |
| eeg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.4750 | 0.4254 |
| eeg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.4021 | 0.3706 |
| eeg | within_participant | gru1d | none | gru1d+none | 10 | 0.3875 | 0.2946 |
| eeg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.3146 | 0.2392 |
| eeg | within_participant | transformer | none | transformer+none | 10 | 0.3667 | 0.3278 |
| eeg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.3563 | 0.3141 |
| fused | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.2851 | 0.2484 |
| fused | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.2722 | 0.2242 |
| fused | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.2649 | 0.1608 |
| fused | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2581 | 0.1539 |
| fused | group_holdout | gru1d | none | gru1d+none | 2 | 0.2949 | 0.2487 |
| fused | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.2824 | 0.1737 |
| fused | group_holdout | transformer | none | transformer+none | 2 | 0.2500 | 0.0486 |
| fused | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.2500 | 0.0486 |
| fused | loso | bigru1d | none | bigru1d+none | 2 | 0.2321 | 0.0860 |
| fused | loso | bilstm1d | none | bilstm1d+none | 2 | 0.2966 | 0.1942 |
| fused | loso | cnn1d | none | cnn1d+none | 2 | 0.2569 | 0.1285 |
| fused | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2569 | 0.1285 |
| fused | loso | gru1d | none | gru1d+none | 2 | 0.2698 | 0.1620 |
| fused | loso | lstm1d | none | lstm1d+none | 2 | 0.3542 | 0.2254 |
| fused | loso | transformer | none | transformer+none | 2 | 0.2500 | 0.0519 |
| fused | loso | transformer_xl | none | transformer_xl+none | 2 | 0.2500 | 0.0519 |
| fused | within_participant | bigru1d | none | bigru1d+none | 10 | 0.3750 | 0.3055 |
| fused | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.3458 | 0.2812 |
| fused | within_participant | cnn1d | none | cnn1d+none | 10 | 0.4042 | 0.3343 |
| fused | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.4333 | 0.3693 |
| fused | within_participant | gru1d | none | gru1d+none | 10 | 0.3458 | 0.2651 |
| fused | within_participant | lstm1d | none | lstm1d+none | 10 | 0.3042 | 0.2402 |
| fused | within_participant | transformer | none | transformer+none | 10 | 0.3917 | 0.2402 |
| fused | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.3417 | 0.2114 |
| pupil | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.2900 | 0.2567 |
| pupil | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.2668 | 0.1947 |
| pupil | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.2545 | 0.1476 |
| pupil | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2547 | 0.1479 |
| pupil | group_holdout | gru1d | none | gru1d+none | 2 | 0.2879 | 0.2184 |
| pupil | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.2795 | 0.1704 |
| pupil | group_holdout | transformer | none | transformer+none | 2 | 0.2500 | 0.0486 |
| pupil | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.2500 | 0.0486 |
| pupil | loso | bigru1d | none | bigru1d+none | 2 | 0.2391 | 0.1553 |
| pupil | loso | bilstm1d | none | bilstm1d+none | 2 | 0.2901 | 0.2355 |
| pupil | loso | cnn1d | none | cnn1d+none | 2 | 0.2500 | 0.1147 |
| pupil | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.2569 | 0.1285 |
| pupil | loso | gru1d | none | gru1d+none | 2 | 0.2688 | 0.1461 |
| pupil | loso | lstm1d | none | lstm1d+none | 2 | 0.2341 | 0.1304 |
| pupil | loso | transformer | none | transformer+none | 2 | 0.2500 | 0.0519 |
| pupil | loso | transformer_xl | none | transformer_xl+none | 2 | 0.2500 | 0.0519 |
| pupil | within_participant | bigru1d | none | bigru1d+none | 10 | 0.3687 | 0.3101 |
| pupil | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.3438 | 0.2797 |
| pupil | within_participant | cnn1d | none | cnn1d+none | 10 | 0.4375 | 0.3464 |
| pupil | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.4625 | 0.3782 |
| pupil | within_participant | gru1d | none | gru1d+none | 10 | 0.3458 | 0.2635 |
| pupil | within_participant | lstm1d | none | lstm1d+none | 10 | 0.3104 | 0.2404 |
| pupil | within_participant | transformer | none | transformer+none | 10 | 0.3458 | 0.2282 |
| pupil | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.3083 | 0.1834 |

## Warning Summary
- none


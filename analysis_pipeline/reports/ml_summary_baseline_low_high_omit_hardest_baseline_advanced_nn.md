# Stage 6 ML Summary

## Config
- Target: `difficulty_bin` (`target_label`)
- Protocols: `loso, group_holdout, within_participant`
- Models: `lstm1d, gru1d, cnn1d, transformer, bilstm1d, bigru1d, cnn1d_deep, transformer_xl`
- Feature selectors: `none`
- Datasets: `eeg, ecg, pupil, fused`
- Inner folds: `2`
- Max param combos/model: `2`
- Class scenario: `baseline_low_high_omit_hardest`
- Final labels: `low_1_2_3, baseline, high_4_5_6`

## Dataset Snapshot
- `eeg`: rows=1045, features=183, participants=18, classes=3
- `ecg`: rows=1045, features=17, participants=18, classes=3
- `pupil`: rows=1045, features=25, participants=18, classes=3
- `fused`: rows=1045, features=225, participants=18, classes=3

## Best By Dataset/Protocol
- `ecg` + `group_holdout` -> `cnn1d_deep+none` (balanced_acc=0.3883, macro_f1=0.3759, n=2)
- `ecg` + `loso` -> `gru1d+none` (balanced_acc=0.4246, macro_f1=0.3619, n=2)
- `ecg` + `within_participant` -> `transformer+none` (balanced_acc=0.5100, macro_f1=0.4548, n=10)
- `eeg` + `group_holdout` -> `cnn1d_deep+none` (balanced_acc=0.4524, macro_f1=0.4093, n=2)
- `eeg` + `loso` -> `cnn1d_deep+none` (balanced_acc=0.5313, macro_f1=0.5117, n=2)
- `eeg` + `within_participant` -> `cnn1d_deep+none` (balanced_acc=0.5189, macro_f1=0.4993, n=10)
- `fused` + `group_holdout` -> `lstm1d+none` (balanced_acc=0.3969, macro_f1=0.2874, n=2)
- `fused` + `loso` -> `bigru1d+none` (balanced_acc=0.4104, macro_f1=0.2785, n=2)
- `fused` + `within_participant` -> `cnn1d+none` (balanced_acc=0.5656, macro_f1=0.4213, n=10)
- `pupil` + `group_holdout` -> `bigru1d+none` (balanced_acc=0.4015, macro_f1=0.3404, n=2)
- `pupil` + `loso` -> `lstm1d+none` (balanced_acc=0.4581, macro_f1=0.3828, n=2)
- `pupil` + `within_participant` -> `cnn1d+none` (balanced_acc=0.5167, macro_f1=0.4290, n=10)

## Aggregates
| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |
|---|---|---|---|---|---:|---:|---:|
| ecg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.3289 | 0.2857 |
| ecg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.3329 | 0.2840 |
| ecg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.3561 | 0.3425 |
| ecg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3883 | 0.3759 |
| ecg | group_holdout | gru1d | none | gru1d+none | 2 | 0.3375 | 0.2537 |
| ecg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.3495 | 0.3330 |
| ecg | group_holdout | transformer | none | transformer+none | 2 | 0.3805 | 0.3359 |
| ecg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.3736 | 0.3279 |
| ecg | loso | bigru1d | none | bigru1d+none | 2 | 0.3759 | 0.2809 |
| ecg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.3712 | 0.2802 |
| ecg | loso | cnn1d | none | cnn1d+none | 2 | 0.3706 | 0.3402 |
| ecg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3695 | 0.3358 |
| ecg | loso | gru1d | none | gru1d+none | 2 | 0.4246 | 0.3619 |
| ecg | loso | lstm1d | none | lstm1d+none | 2 | 0.3652 | 0.3141 |
| ecg | loso | transformer | none | transformer+none | 2 | 0.3405 | 0.2930 |
| ecg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.3571 | 0.2540 |
| ecg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.4244 | 0.3130 |
| ecg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.4289 | 0.3726 |
| ecg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.4100 | 0.3644 |
| ecg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.4411 | 0.3940 |
| ecg | within_participant | gru1d | none | gru1d+none | 10 | 0.4356 | 0.3424 |
| ecg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.3644 | 0.3257 |
| ecg | within_participant | transformer | none | transformer+none | 10 | 0.5100 | 0.4548 |
| ecg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.4044 | 0.3608 |
| eeg | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.3759 | 0.3508 |
| eeg | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.3444 | 0.3227 |
| eeg | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.4200 | 0.3698 |
| eeg | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.4524 | 0.4093 |
| eeg | group_holdout | gru1d | none | gru1d+none | 2 | 0.3922 | 0.3714 |
| eeg | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.3769 | 0.2839 |
| eeg | group_holdout | transformer | none | transformer+none | 2 | 0.3682 | 0.3026 |
| eeg | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.3637 | 0.3087 |
| eeg | loso | bigru1d | none | bigru1d+none | 2 | 0.4551 | 0.3870 |
| eeg | loso | bilstm1d | none | bilstm1d+none | 2 | 0.3784 | 0.3654 |
| eeg | loso | cnn1d | none | cnn1d+none | 2 | 0.5085 | 0.5144 |
| eeg | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.5313 | 0.5117 |
| eeg | loso | gru1d | none | gru1d+none | 2 | 0.4153 | 0.3958 |
| eeg | loso | lstm1d | none | lstm1d+none | 2 | 0.4281 | 0.3924 |
| eeg | loso | transformer | none | transformer+none | 2 | 0.4629 | 0.3247 |
| eeg | loso | transformer_xl | none | transformer_xl+none | 2 | 0.4790 | 0.3840 |
| eeg | within_participant | bigru1d | none | bigru1d+none | 10 | 0.4256 | 0.3701 |
| eeg | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.4444 | 0.3895 |
| eeg | within_participant | cnn1d | none | cnn1d+none | 10 | 0.5144 | 0.4883 |
| eeg | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.5189 | 0.4993 |
| eeg | within_participant | gru1d | none | gru1d+none | 10 | 0.4011 | 0.3492 |
| eeg | within_participant | lstm1d | none | lstm1d+none | 10 | 0.4078 | 0.3247 |
| eeg | within_participant | transformer | none | transformer+none | 10 | 0.4333 | 0.3825 |
| eeg | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.4089 | 0.3638 |
| fused | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.3925 | 0.2975 |
| fused | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.3554 | 0.3225 |
| fused | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.3444 | 0.2588 |
| fused | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3382 | 0.2442 |
| fused | group_holdout | gru1d | none | gru1d+none | 2 | 0.3835 | 0.3258 |
| fused | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.3969 | 0.2874 |
| fused | group_holdout | transformer | none | transformer+none | 2 | 0.3333 | 0.0648 |
| fused | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.3333 | 0.0648 |
| fused | loso | bigru1d | none | bigru1d+none | 2 | 0.4104 | 0.2785 |
| fused | loso | bilstm1d | none | bilstm1d+none | 2 | 0.3933 | 0.3056 |
| fused | loso | cnn1d | none | cnn1d+none | 2 | 0.3395 | 0.2161 |
| fused | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3395 | 0.2161 |
| fused | loso | gru1d | none | gru1d+none | 2 | 0.3739 | 0.2516 |
| fused | loso | lstm1d | none | lstm1d+none | 2 | 0.3995 | 0.3054 |
| fused | loso | transformer | none | transformer+none | 2 | 0.3333 | 0.0691 |
| fused | loso | transformer_xl | none | transformer_xl+none | 2 | 0.3333 | 0.0691 |
| fused | within_participant | bigru1d | none | bigru1d+none | 10 | 0.4622 | 0.3668 |
| fused | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.4500 | 0.3590 |
| fused | within_participant | cnn1d | none | cnn1d+none | 10 | 0.5656 | 0.4213 |
| fused | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.5511 | 0.4490 |
| fused | within_participant | gru1d | none | gru1d+none | 10 | 0.4556 | 0.3426 |
| fused | within_participant | lstm1d | none | lstm1d+none | 10 | 0.3478 | 0.2645 |
| fused | within_participant | transformer | none | transformer+none | 10 | 0.4822 | 0.2931 |
| fused | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.5122 | 0.3431 |
| pupil | group_holdout | bigru1d | none | bigru1d+none | 2 | 0.4015 | 0.3404 |
| pupil | group_holdout | bilstm1d | none | bilstm1d+none | 2 | 0.3983 | 0.3790 |
| pupil | group_holdout | cnn1d | none | cnn1d+none | 2 | 0.3414 | 0.2483 |
| pupil | group_holdout | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3368 | 0.2405 |
| pupil | group_holdout | gru1d | none | gru1d+none | 2 | 0.3809 | 0.3297 |
| pupil | group_holdout | lstm1d | none | lstm1d+none | 2 | 0.3635 | 0.2460 |
| pupil | group_holdout | transformer | none | transformer+none | 2 | 0.3333 | 0.0648 |
| pupil | group_holdout | transformer_xl | none | transformer_xl+none | 2 | 0.3333 | 0.0648 |
| pupil | loso | bigru1d | none | bigru1d+none | 2 | 0.4089 | 0.3376 |
| pupil | loso | bilstm1d | none | bilstm1d+none | 2 | 0.4510 | 0.3581 |
| pupil | loso | cnn1d | none | cnn1d+none | 2 | 0.3333 | 0.2030 |
| pupil | loso | cnn1d_deep | none | cnn1d_deep+none | 2 | 0.3395 | 0.2161 |
| pupil | loso | gru1d | none | gru1d+none | 2 | 0.3686 | 0.2689 |
| pupil | loso | lstm1d | none | lstm1d+none | 2 | 0.4581 | 0.3828 |
| pupil | loso | transformer | none | transformer+none | 2 | 0.3333 | 0.0691 |
| pupil | loso | transformer_xl | none | transformer_xl+none | 2 | 0.3333 | 0.0691 |
| pupil | within_participant | bigru1d | none | bigru1d+none | 10 | 0.4756 | 0.3966 |
| pupil | within_participant | bilstm1d | none | bilstm1d+none | 10 | 0.4933 | 0.3944 |
| pupil | within_participant | cnn1d | none | cnn1d+none | 10 | 0.5167 | 0.4290 |
| pupil | within_participant | cnn1d_deep | none | cnn1d_deep+none | 10 | 0.5156 | 0.4565 |
| pupil | within_participant | gru1d | none | gru1d+none | 10 | 0.4511 | 0.3186 |
| pupil | within_participant | lstm1d | none | lstm1d+none | 10 | 0.3611 | 0.2958 |
| pupil | within_participant | transformer | none | transformer+none | 10 | 0.4011 | 0.2347 |
| pupil | within_participant | transformer_xl | none | transformer_xl+none | 10 | 0.3889 | 0.2294 |

## Warning Summary
- none


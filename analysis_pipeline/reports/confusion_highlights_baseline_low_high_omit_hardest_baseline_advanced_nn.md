# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3883)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `low_1_2_3`: recall=0.3291, support=158
- `high_4_5_6`: recall=0.5385, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.216 | 0.378 | 0.405 |
| low_1_2_3 | 0.247 | 0.329 | 0.424 |
| high_4_5_6 | 0.244 | 0.218 | 0.538 |

## ecg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3805)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `low_1_2_3`: recall=0.6646, support=158
- `high_4_5_6`: recall=0.2436, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.243 | 0.622 | 0.135 |
| low_1_2_3 | 0.177 | 0.665 | 0.158 |
| high_4_5_6 | 0.154 | 0.603 | 0.244 |

## ecg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3736)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `low_1_2_3`: recall=0.6709, support=158
- `high_4_5_6`: recall=0.1923, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.297 | 0.595 | 0.108 |
| low_1_2_3 | 0.209 | 0.671 | 0.120 |
| high_4_5_6 | 0.212 | 0.596 | 0.192 |

## ecg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3561)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `low_1_2_3`: recall=0.3101, support=158
- `high_4_5_6`: recall=0.5192, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.189 | 0.486 | 0.324 |
| low_1_2_3 | 0.323 | 0.310 | 0.367 |
| high_4_5_6 | 0.276 | 0.205 | 0.519 |

## ecg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3495)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `low_1_2_3`: recall=0.7152, support=158
- `high_4_5_6`: recall=0.2628, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.108 | 0.730 | 0.162 |
| low_1_2_3 | 0.076 | 0.715 | 0.209 |
| high_4_5_6 | 0.077 | 0.660 | 0.263 |

## ecg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3375)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.5946, support=37
- `low_1_2_3`: recall=0.1456, support=158
- `high_4_5_6`: recall=0.2756, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.595 | 0.189 | 0.216 |
| low_1_2_3 | 0.633 | 0.146 | 0.222 |
| high_4_5_6 | 0.494 | 0.231 | 0.276 |

## ecg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3329)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4595, support=37
- `low_1_2_3`: recall=0.1835, support=158
- `high_4_5_6`: recall=0.3590, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.459 | 0.162 | 0.378 |
| low_1_2_3 | 0.525 | 0.184 | 0.291 |
| high_4_5_6 | 0.494 | 0.147 | 0.359 |

## ecg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.3289)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4054, support=37
- `low_1_2_3`: recall=0.2342, support=158
- `high_4_5_6`: recall=0.3590, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.405 | 0.243 | 0.351 |
| low_1_2_3 | 0.475 | 0.234 | 0.291 |
| high_4_5_6 | 0.436 | 0.205 | 0.359 |

## ecg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.4246)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.5918, support=49
- `high_4_5_6`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.500 | 0.214 |
| low_1_2_3 | 0.102 | 0.592 | 0.306 |
| high_4_5_6 | 0.321 | 0.302 | 0.377 |

## ecg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.3759)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.3673, support=49
- `high_4_5_6`: recall=0.2264, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.357 | 0.143 |
| low_1_2_3 | 0.612 | 0.367 | 0.020 |
| high_4_5_6 | 0.566 | 0.208 | 0.226 |

## ecg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3712)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.4286, support=49
- `high_4_5_6`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.429 | 0.071 |
| low_1_2_3 | 0.551 | 0.429 | 0.020 |
| high_4_5_6 | 0.642 | 0.208 | 0.151 |

## ecg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3706)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.4286, support=49
- `high_4_5_6`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.286 |
| low_1_2_3 | 0.367 | 0.429 | 0.204 |
| high_4_5_6 | 0.340 | 0.283 | 0.377 |

## ecg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3695)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.4694, support=49
- `high_4_5_6`: recall=0.3962, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.286 |
| low_1_2_3 | 0.163 | 0.469 | 0.367 |
| high_4_5_6 | 0.189 | 0.415 | 0.396 |

## ecg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3652)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.7143, support=49
- `high_4_5_6`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.714 | 0.071 |
| low_1_2_3 | 0.265 | 0.714 | 0.020 |
| high_4_5_6 | 0.396 | 0.453 | 0.151 |

## ecg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3571)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.2857, support=49
- `high_4_5_6`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.143 |
| low_1_2_3 | 0.694 | 0.286 | 0.020 |
| high_4_5_6 | 0.698 | 0.151 | 0.151 |

## ecg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3405)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.5714, support=49
- `high_4_5_6`: recall=0.2075, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.643 | 0.143 |
| low_1_2_3 | 0.347 | 0.571 | 0.082 |
| high_4_5_6 | 0.340 | 0.453 | 0.208 |

## ecg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.5100)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.6296, support=54
- `high_4_5_6`: recall=0.4074, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.357 | 0.214 |
| low_1_2_3 | 0.167 | 0.630 | 0.204 |
| high_4_5_6 | 0.167 | 0.426 | 0.407 |

## ecg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.4411)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.4815, support=54
- `high_4_5_6`: recall=0.5370, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.357 |
| low_1_2_3 | 0.167 | 0.481 | 0.352 |
| high_4_5_6 | 0.130 | 0.333 | 0.537 |

## ecg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.4356)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.1667, support=54
- `high_4_5_6`: recall=0.6852, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.286 |
| low_1_2_3 | 0.407 | 0.167 | 0.426 |
| high_4_5_6 | 0.222 | 0.093 | 0.685 |

## ecg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.4289)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.4259, support=54
- `high_4_5_6`: recall=0.6667, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.286 |
| low_1_2_3 | 0.148 | 0.426 | 0.426 |
| high_4_5_6 | 0.111 | 0.222 | 0.667 |

## ecg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.4244)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.1296, support=54
- `high_4_5_6`: recall=0.6296, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.357 |
| low_1_2_3 | 0.463 | 0.130 | 0.407 |
| high_4_5_6 | 0.222 | 0.148 | 0.630 |

## ecg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.4100)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.4074, support=54
- `high_4_5_6`: recall=0.5185, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.357 |
| low_1_2_3 | 0.185 | 0.407 | 0.407 |
| high_4_5_6 | 0.148 | 0.333 | 0.519 |

## ecg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.4044)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.5556, support=54
- `high_4_5_6`: recall=0.4259, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.286 |
| low_1_2_3 | 0.074 | 0.556 | 0.370 |
| high_4_5_6 | 0.148 | 0.426 | 0.426 |

## ecg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.3644)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/ecg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2_3`: recall=0.3704, support=54
- `high_4_5_6`: recall=0.6667, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.071 | 0.643 | 0.286 |
| low_1_2_3 | 0.222 | 0.370 | 0.407 |
| high_4_5_6 | 0.130 | 0.204 | 0.667 |

## eeg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.4524)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.3784, support=37
- `low_1_2_3`: recall=0.2342, support=158
- `high_4_5_6`: recall=0.7244, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.378 | 0.135 | 0.486 |
| low_1_2_3 | 0.272 | 0.234 | 0.494 |
| high_4_5_6 | 0.154 | 0.122 | 0.724 |

## eeg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.4200)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `low_1_2_3`: recall=0.1582, support=158
- `high_4_5_6`: recall=0.7821, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.297 | 0.135 | 0.568 |
| low_1_2_3 | 0.285 | 0.158 | 0.557 |
| high_4_5_6 | 0.128 | 0.090 | 0.782 |

## eeg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3922)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `low_1_2_3`: recall=0.3038, support=158
- `high_4_5_6`: recall=0.5833, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.243 | 0.297 | 0.459 |
| low_1_2_3 | 0.215 | 0.304 | 0.481 |
| high_4_5_6 | 0.167 | 0.250 | 0.583 |

## eeg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3769)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `low_1_2_3`: recall=0.7405, support=158
- `high_4_5_6`: recall=0.1987, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.162 | 0.676 | 0.162 |
| low_1_2_3 | 0.120 | 0.741 | 0.139 |
| high_4_5_6 | 0.115 | 0.686 | 0.199 |

## eeg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.3759)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `low_1_2_3`: recall=0.2278, support=158
- `high_4_5_6`: recall=0.6731, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.189 | 0.270 | 0.541 |
| low_1_2_3 | 0.184 | 0.228 | 0.589 |
| high_4_5_6 | 0.122 | 0.205 | 0.673 |

## eeg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3682)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4054, support=37
- `low_1_2_3`: recall=0.1139, support=158
- `high_4_5_6`: recall=0.5769, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.405 | 0.054 | 0.541 |
| low_1_2_3 | 0.323 | 0.114 | 0.563 |
| high_4_5_6 | 0.365 | 0.058 | 0.577 |

## eeg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3637)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2_3`: recall=0.1139, support=158
- `high_4_5_6`: recall=0.6218, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.324 | 0.216 | 0.459 |
| low_1_2_3 | 0.304 | 0.114 | 0.582 |
| high_4_5_6 | 0.282 | 0.096 | 0.622 |

## eeg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3444)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2_3`: recall=0.2785, support=158
- `high_4_5_6`: recall=0.4872, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.324 | 0.297 | 0.378 |
| low_1_2_3 | 0.335 | 0.278 | 0.386 |
| high_4_5_6 | 0.269 | 0.244 | 0.487 |

## eeg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.5313)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.8367, support=49
- `high_4_5_6`: recall=0.3208, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.500 | 0.071 |
| low_1_2_3 | 0.061 | 0.837 | 0.102 |
| high_4_5_6 | 0.075 | 0.604 | 0.321 |

## eeg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.5085)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.6531, support=49
- `high_4_5_6`: recall=0.5849, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.571 | 0.143 |
| low_1_2_3 | 0.061 | 0.653 | 0.286 |
| high_4_5_6 | 0.094 | 0.321 | 0.585 |

## eeg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.4790)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.6327, support=49
- `high_4_5_6`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.357 | 0.000 |
| low_1_2_3 | 0.265 | 0.633 | 0.102 |
| high_4_5_6 | 0.415 | 0.415 | 0.170 |

## eeg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.4629)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.8571, support=14
- `low_1_2_3`: recall=0.1224, support=49
- `high_4_5_6`: recall=0.3962, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.857 | 0.000 | 0.143 |
| low_1_2_3 | 0.714 | 0.122 | 0.163 |
| high_4_5_6 | 0.566 | 0.038 | 0.396 |

## eeg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.4551)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.3673, support=49
- `high_4_5_6`: recall=0.6038, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.357 | 0.286 |
| low_1_2_3 | 0.245 | 0.367 | 0.388 |
| high_4_5_6 | 0.094 | 0.302 | 0.604 |

## eeg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.4281)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.4286, support=49
- `high_4_5_6`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.500 | 0.143 |
| low_1_2_3 | 0.327 | 0.429 | 0.245 |
| high_4_5_6 | 0.189 | 0.321 | 0.491 |

## eeg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.4153)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2_3`: recall=0.5510, support=49
- `high_4_5_6`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.143 | 0.571 | 0.286 |
| low_1_2_3 | 0.041 | 0.551 | 0.408 |
| high_4_5_6 | 0.075 | 0.377 | 0.547 |

## eeg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3784)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.5306, support=49
- `high_4_5_6`: recall=0.3962, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.571 | 0.214 |
| low_1_2_3 | 0.204 | 0.531 | 0.265 |
| high_4_5_6 | 0.189 | 0.415 | 0.396 |

## eeg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.5189)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.5556, support=54
- `high_4_5_6`: recall=0.6111, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.214 |
| low_1_2_3 | 0.056 | 0.556 | 0.389 |
| high_4_5_6 | 0.037 | 0.352 | 0.611 |

## eeg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.5144)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.5556, support=54
- `high_4_5_6`: recall=0.6481, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.357 | 0.214 |
| low_1_2_3 | 0.093 | 0.556 | 0.352 |
| high_4_5_6 | 0.056 | 0.296 | 0.648 |

## eeg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.4444)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.2963, support=54
- `high_4_5_6`: recall=0.6852, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.429 |
| low_1_2_3 | 0.222 | 0.296 | 0.481 |
| high_4_5_6 | 0.093 | 0.222 | 0.685 |

## eeg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.4333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.4815, support=54
- `high_4_5_6`: recall=0.4630, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.500 | 0.143 |
| low_1_2_3 | 0.241 | 0.481 | 0.278 |
| high_4_5_6 | 0.241 | 0.296 | 0.463 |

## eeg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.4256)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.2593, support=54
- `high_4_5_6`: recall=0.6667, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.429 |
| low_1_2_3 | 0.296 | 0.259 | 0.444 |
| high_4_5_6 | 0.185 | 0.148 | 0.667 |

## eeg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.4089)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.4815, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.286 |
| low_1_2_3 | 0.204 | 0.444 | 0.352 |
| high_4_5_6 | 0.259 | 0.259 | 0.481 |

## eeg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.4078)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.3148, support=54
- `high_4_5_6`: recall=0.5556, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.286 |
| low_1_2_3 | 0.296 | 0.315 | 0.389 |
| high_4_5_6 | 0.204 | 0.241 | 0.556 |

## eeg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.4011)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/eeg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.3148, support=54
- `high_4_5_6`: recall=0.5926, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.214 | 0.429 |
| low_1_2_3 | 0.278 | 0.315 | 0.407 |
| high_4_5_6 | 0.130 | 0.278 | 0.593 |

## fused | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3969)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4737, support=38
- `low_1_2_3`: recall=0.0988, support=162
- `high_4_5_6`: recall=0.6875, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.474 | 0.079 | 0.447 |
| low_1_2_3 | 0.340 | 0.099 | 0.562 |
| high_4_5_6 | 0.219 | 0.094 | 0.688 |

## fused | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.3925)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=38
- `low_1_2_3`: recall=0.0679, support=162
- `high_4_5_6`: recall=0.6500, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.053 | 0.447 |
| low_1_2_3 | 0.358 | 0.068 | 0.574 |
| high_4_5_6 | 0.294 | 0.056 | 0.650 |

## fused | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3835)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2895, support=38
- `low_1_2_3`: recall=0.1667, support=162
- `high_4_5_6`: recall=0.7250, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.289 | 0.158 | 0.553 |
| low_1_2_3 | 0.204 | 0.167 | 0.630 |
| high_4_5_6 | 0.169 | 0.106 | 0.725 |

## fused | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3554)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3947, support=38
- `low_1_2_3`: recall=0.2901, support=162
- `high_4_5_6`: recall=0.4500, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.395 | 0.289 | 0.316 |
| low_1_2_3 | 0.358 | 0.290 | 0.352 |
| high_4_5_6 | 0.275 | 0.275 | 0.450 |

## fused | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3444)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `low_1_2_3`: recall=0.0926, support=162
- `high_4_5_6`: recall=0.8750, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.079 | 0.132 | 0.789 |
| low_1_2_3 | 0.068 | 0.093 | 0.840 |
| high_4_5_6 | 0.044 | 0.081 | 0.875 |

## fused | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3382)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `low_1_2_3`: recall=0.0556, support=162
- `high_4_5_6`: recall=0.8875, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.079 | 0.132 | 0.789 |
| low_1_2_3 | 0.074 | 0.056 | 0.870 |
| high_4_5_6 | 0.069 | 0.044 | 0.887 |

## fused | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2_3`: recall=0.0000, support=162
- `high_4_5_6`: recall=0.0000, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## fused | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2_3`: recall=0.0000, support=162
- `high_4_5_6`: recall=0.0000, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## fused | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.4104)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.1667, support=54
- `high_4_5_6`: recall=0.4151, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.071 | 0.286 |
| low_1_2_3 | 0.519 | 0.167 | 0.315 |
| high_4_5_6 | 0.509 | 0.075 | 0.415 |

## fused | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3995)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2_3`: recall=0.4630, support=54
- `high_4_5_6`: recall=0.5849, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.500 |
| low_1_2_3 | 0.037 | 0.463 | 0.500 |
| high_4_5_6 | 0.189 | 0.226 | 0.585 |

## fused | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3933)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.5849, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.571 |
| low_1_2_3 | 0.037 | 0.444 | 0.519 |
| high_4_5_6 | 0.302 | 0.113 | 0.585 |

## fused | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3739)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.4074, support=54
- `high_4_5_6`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.500 |
| low_1_2_3 | 0.093 | 0.407 | 0.500 |
| high_4_5_6 | 0.377 | 0.132 | 0.491 |

## fused | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3395)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.0185, support=54
- `high_4_5_6`: recall=1.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.000 | 1.000 |
| low_1_2_3 | 0.000 | 0.019 | 0.981 |
| high_4_5_6 | 0.000 | 0.000 | 1.000 |

## fused | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3395)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.0185, support=54
- `high_4_5_6`: recall=1.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.000 | 1.000 |
| low_1_2_3 | 0.000 | 0.019 | 0.981 |
| high_4_5_6 | 0.000 | 0.000 | 1.000 |

## fused | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2_3`: recall=0.0000, support=54
- `high_4_5_6`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## fused | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2_3`: recall=0.0000, support=54
- `high_4_5_6`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## fused | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.5656)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `low_1_2_3`: recall=0.2963, support=54
- `high_4_5_6`: recall=0.4528, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.929 | 0.071 | 0.000 |
| low_1_2_3 | 0.500 | 0.296 | 0.204 |
| high_4_5_6 | 0.415 | 0.132 | 0.453 |

## fused | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.5511)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `low_1_2_3`: recall=0.3519, support=54
- `high_4_5_6`: recall=0.5660, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.786 | 0.071 | 0.143 |
| low_1_2_3 | 0.333 | 0.352 | 0.315 |
| high_4_5_6 | 0.245 | 0.189 | 0.566 |

## fused | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.5122)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `low_1_2_3`: recall=0.2593, support=54
- `high_4_5_6`: recall=0.3585, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.929 | 0.071 | 0.000 |
| low_1_2_3 | 0.537 | 0.259 | 0.204 |
| high_4_5_6 | 0.509 | 0.132 | 0.358 |

## fused | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.4822)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `low_1_2_3`: recall=0.1111, support=54
- `high_4_5_6`: recall=0.4340, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.929 | 0.071 | 0.000 |
| low_1_2_3 | 0.611 | 0.111 | 0.278 |
| high_4_5_6 | 0.547 | 0.019 | 0.434 |

## fused | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.4622)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.3889, support=54
- `high_4_5_6`: recall=0.4528, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.143 |
| low_1_2_3 | 0.278 | 0.389 | 0.333 |
| high_4_5_6 | 0.283 | 0.264 | 0.453 |

## fused | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.4556)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.5370, support=54
- `high_4_5_6`: recall=0.2453, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.357 | 0.000 |
| low_1_2_3 | 0.278 | 0.537 | 0.185 |
| high_4_5_6 | 0.396 | 0.358 | 0.245 |

## fused | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.4500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.4151, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.357 | 0.214 |
| low_1_2_3 | 0.222 | 0.444 | 0.333 |
| high_4_5_6 | 0.189 | 0.396 | 0.415 |

## fused | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.3478)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/fused/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.429 | 0.143 |
| low_1_2_3 | 0.296 | 0.444 | 0.259 |
| high_4_5_6 | 0.358 | 0.377 | 0.264 |

## pupil | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.4015)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3684, support=38
- `low_1_2_3`: recall=0.1728, support=162
- `high_4_5_6`: recall=0.6875, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.368 | 0.079 | 0.553 |
| low_1_2_3 | 0.253 | 0.173 | 0.574 |
| high_4_5_6 | 0.181 | 0.131 | 0.688 |

## pupil | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3983)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1579, support=38
- `low_1_2_3`: recall=0.4012, support=162
- `high_4_5_6`: recall=0.6562, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.158 | 0.342 | 0.500 |
| low_1_2_3 | 0.105 | 0.401 | 0.494 |
| high_4_5_6 | 0.069 | 0.275 | 0.656 |

## pupil | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3809)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2632, support=38
- `low_1_2_3`: recall=0.1790, support=162
- `high_4_5_6`: recall=0.7312, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.263 | 0.158 | 0.579 |
| low_1_2_3 | 0.185 | 0.179 | 0.636 |
| high_4_5_6 | 0.163 | 0.106 | 0.731 |

## pupil | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3635)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3158, support=38
- `low_1_2_3`: recall=0.0123, support=162
- `high_4_5_6`: recall=0.8063, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.316 | 0.053 | 0.632 |
| low_1_2_3 | 0.216 | 0.012 | 0.772 |
| high_4_5_6 | 0.156 | 0.037 | 0.806 |

## pupil | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3414)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `low_1_2_3`: recall=0.0617, support=162
- `high_4_5_6`: recall=0.8938, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.079 | 0.132 | 0.789 |
| low_1_2_3 | 0.062 | 0.062 | 0.877 |
| high_4_5_6 | 0.062 | 0.044 | 0.894 |

## pupil | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3368)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `low_1_2_3`: recall=0.4012, support=162
- `high_4_5_6`: recall=0.5813, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.026 | 0.500 | 0.474 |
| low_1_2_3 | 0.025 | 0.401 | 0.574 |
| high_4_5_6 | 0.031 | 0.388 | 0.581 |

## pupil | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2_3`: recall=0.0000, support=162
- `high_4_5_6`: recall=0.0000, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## pupil | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2_3`: recall=0.0000, support=162
- `high_4_5_6`: recall=0.0000, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## pupil | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.4581)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.4630, support=54
- `high_4_5_6`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.357 | 0.286 |
| low_1_2_3 | 0.074 | 0.463 | 0.463 |
| high_4_5_6 | 0.208 | 0.245 | 0.547 |

## pupil | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.4510)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.4259, support=54
- `high_4_5_6`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.286 |
| low_1_2_3 | 0.111 | 0.426 | 0.463 |
| high_4_5_6 | 0.358 | 0.151 | 0.491 |

## pupil | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.4089)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.3519, support=54
- `high_4_5_6`: recall=0.5094, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.357 |
| low_1_2_3 | 0.130 | 0.352 | 0.519 |
| high_4_5_6 | 0.415 | 0.075 | 0.509 |

## pupil | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3686)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2_3`: recall=0.4259, support=54
- `high_4_5_6`: recall=0.5283, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.500 |
| low_1_2_3 | 0.074 | 0.426 | 0.500 |
| high_4_5_6 | 0.340 | 0.132 | 0.528 |

## pupil | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3395)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.0185, support=54
- `high_4_5_6`: recall=1.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.000 | 1.000 |
| low_1_2_3 | 0.000 | 0.019 | 0.981 |
| high_4_5_6 | 0.000 | 0.000 | 1.000 |

## pupil | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.5000, support=54
- `high_4_5_6`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.500 | 0.500 |
| low_1_2_3 | 0.000 | 0.500 | 0.500 |
| high_4_5_6 | 0.000 | 0.509 | 0.491 |

## pupil | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2_3`: recall=0.0000, support=54
- `high_4_5_6`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## pupil | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2_3`: recall=0.0000, support=54
- `high_4_5_6`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 |
| low_1_2_3 | 1.000 | 0.000 | 0.000 |
| high_4_5_6 | 1.000 | 0.000 | 0.000 |

## pupil | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.5167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2_3`: recall=0.3148, support=54
- `high_4_5_6`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.143 |
| low_1_2_3 | 0.352 | 0.315 | 0.333 |
| high_4_5_6 | 0.283 | 0.170 | 0.547 |

## pupil | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.5156)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.3704, support=54
- `high_4_5_6`: recall=0.6792, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.357 |
| low_1_2_3 | 0.204 | 0.370 | 0.426 |
| high_4_5_6 | 0.132 | 0.189 | 0.679 |

## pupil | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.4933)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.5000, support=54
- `high_4_5_6`: recall=0.3962, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.214 |
| low_1_2_3 | 0.222 | 0.500 | 0.278 |
| high_4_5_6 | 0.208 | 0.396 | 0.396 |

## pupil | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.4756)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.4259, support=54
- `high_4_5_6`: recall=0.4528, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.143 | 0.214 |
| low_1_2_3 | 0.259 | 0.426 | 0.315 |
| high_4_5_6 | 0.283 | 0.264 | 0.453 |

## pupil | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.4511)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2_3`: recall=0.5370, support=54
- `high_4_5_6`: recall=0.1887, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.714 | 0.286 | 0.000 |
| low_1_2_3 | 0.259 | 0.537 | 0.204 |
| high_4_5_6 | 0.415 | 0.396 | 0.189 |

## pupil | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.4011)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2_3`: recall=0.1481, support=54
- `high_4_5_6`: recall=0.3585, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.714 | 0.214 | 0.071 |
| low_1_2_3 | 0.648 | 0.148 | 0.204 |
| high_4_5_6 | 0.528 | 0.113 | 0.358 |

## pupil | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.3889)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2_3`: recall=0.1296, support=54
- `high_4_5_6`: recall=0.3396, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.143 |
| low_1_2_3 | 0.556 | 0.130 | 0.315 |
| high_4_5_6 | 0.547 | 0.113 | 0.340 |

## pupil | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.3611)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline_advanced_nn/pupil/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.429 | 0.143 |
| low_1_2_3 | 0.333 | 0.444 | 0.222 |
| high_4_5_6 | 0.340 | 0.358 | 0.302 |


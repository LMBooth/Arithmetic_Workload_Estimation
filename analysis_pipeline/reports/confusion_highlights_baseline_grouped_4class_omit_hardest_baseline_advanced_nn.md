# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.3097)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4595, support=37
- `low_1_2`: recall=0.6075, support=107
- `mid_3_4`: recall=0.0192, support=104
- `high_5_6`: recall=0.1650, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.459 | 0.405 | 0.081 | 0.054 |
| low_1_2 | 0.280 | 0.607 | 0.000 | 0.112 |
| mid_3_4 | 0.385 | 0.510 | 0.019 | 0.087 |
| high_5_6 | 0.233 | 0.602 | 0.000 | 0.165 |

## ecg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3064)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.5676, support=37
- `low_1_2`: recall=0.2710, support=107
- `mid_3_4`: recall=0.2308, support=104
- `high_5_6`: recall=0.1748, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.568 | 0.135 | 0.243 | 0.054 |
| low_1_2 | 0.393 | 0.271 | 0.224 | 0.112 |
| mid_3_4 | 0.481 | 0.192 | 0.231 | 0.096 |
| high_5_6 | 0.427 | 0.243 | 0.155 | 0.175 |

## ecg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2727)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `low_1_2`: recall=0.2710, support=107
- `mid_3_4`: recall=0.1538, support=104
- `high_5_6`: recall=0.3689, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.216 | 0.243 | 0.243 | 0.297 |
| low_1_2 | 0.290 | 0.271 | 0.131 | 0.308 |
| mid_3_4 | 0.288 | 0.163 | 0.154 | 0.394 |
| high_5_6 | 0.330 | 0.175 | 0.126 | 0.369 |

## ecg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2526)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4865, support=37
- `low_1_2`: recall=0.2336, support=107
- `mid_3_4`: recall=0.0481, support=104
- `high_5_6`: recall=0.2718, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.486 | 0.189 | 0.189 | 0.135 |
| low_1_2 | 0.467 | 0.234 | 0.093 | 0.206 |
| mid_3_4 | 0.577 | 0.221 | 0.048 | 0.154 |
| high_5_6 | 0.437 | 0.223 | 0.068 | 0.272 |

## ecg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2480)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `low_1_2`: recall=0.3178, support=107
- `mid_3_4`: recall=0.1827, support=104
- `high_5_6`: recall=0.3301, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.162 | 0.243 | 0.378 | 0.216 |
| low_1_2 | 0.262 | 0.318 | 0.187 | 0.234 |
| mid_3_4 | 0.240 | 0.163 | 0.183 | 0.413 |
| high_5_6 | 0.272 | 0.175 | 0.223 | 0.330 |

## ecg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2471)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5135, support=37
- `low_1_2`: recall=0.1495, support=107
- `mid_3_4`: recall=0.0385, support=104
- `high_5_6`: recall=0.3010, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.514 | 0.243 | 0.000 | 0.243 |
| low_1_2 | 0.561 | 0.150 | 0.047 | 0.243 |
| mid_3_4 | 0.558 | 0.192 | 0.038 | 0.212 |
| high_5_6 | 0.476 | 0.194 | 0.029 | 0.301 |

## ecg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2420)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.1869, support=107
- `mid_3_4`: recall=0.1731, support=104
- `high_5_6`: recall=0.3107, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.189 | 0.243 | 0.243 |
| low_1_2 | 0.327 | 0.187 | 0.215 | 0.271 |
| mid_3_4 | 0.365 | 0.212 | 0.173 | 0.250 |
| high_5_6 | 0.243 | 0.243 | 0.204 | 0.311 |

## ecg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2103)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `low_1_2`: recall=0.1495, support=107
- `mid_3_4`: recall=0.1731, support=104
- `high_5_6`: recall=0.2524, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.297 | 0.243 | 0.297 | 0.162 |
| low_1_2 | 0.411 | 0.150 | 0.243 | 0.196 |
| mid_3_4 | 0.433 | 0.221 | 0.173 | 0.173 |
| high_5_6 | 0.369 | 0.194 | 0.184 | 0.252 |

## ecg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3046)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.4062, support=32
- `mid_3_4`: recall=0.3235, support=34
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.429 | 0.286 | 0.143 |
| low_1_2 | 0.031 | 0.406 | 0.531 | 0.031 |
| mid_3_4 | 0.118 | 0.353 | 0.324 | 0.206 |
| high_5_6 | 0.250 | 0.250 | 0.194 | 0.306 |

## ecg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2917)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.3750, support=32
- `mid_3_4`: recall=0.0000, support=34
- `high_5_6`: recall=0.1667, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.071 | 0.071 |
| low_1_2 | 0.562 | 0.375 | 0.031 | 0.031 |
| mid_3_4 | 0.588 | 0.353 | 0.000 | 0.059 |
| high_5_6 | 0.667 | 0.167 | 0.000 | 0.167 |

## ecg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2870)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.3750, support=32
- `mid_3_4`: recall=0.2353, support=34
- `high_5_6`: recall=0.2778, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.143 | 0.357 |
| low_1_2 | 0.219 | 0.375 | 0.219 | 0.188 |
| mid_3_4 | 0.412 | 0.147 | 0.235 | 0.206 |
| high_5_6 | 0.222 | 0.194 | 0.306 | 0.278 |

## ecg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2868)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.2812, support=32
- `mid_3_4`: recall=0.2059, support=34
- `high_5_6`: recall=0.4167, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.143 | 0.286 |
| low_1_2 | 0.281 | 0.281 | 0.156 | 0.281 |
| mid_3_4 | 0.294 | 0.176 | 0.206 | 0.324 |
| high_5_6 | 0.222 | 0.139 | 0.222 | 0.417 |

## ecg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2817)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.4375, support=32
- `mid_3_4`: recall=0.1176, support=34
- `high_5_6`: recall=0.1667, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.429 | 0.071 | 0.143 |
| low_1_2 | 0.375 | 0.438 | 0.156 | 0.031 |
| mid_3_4 | 0.441 | 0.353 | 0.118 | 0.088 |
| high_5_6 | 0.528 | 0.222 | 0.083 | 0.167 |

## ecg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2808)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.3125, support=32
- `mid_3_4`: recall=0.0000, support=34
- `high_5_6`: recall=0.1944, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.071 | 0.143 |
| low_1_2 | 0.656 | 0.312 | 0.000 | 0.031 |
| mid_3_4 | 0.559 | 0.324 | 0.000 | 0.118 |
| high_5_6 | 0.667 | 0.139 | 0.000 | 0.194 |

## ecg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.2624)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.2188, support=32
- `mid_3_4`: recall=0.2059, support=34
- `high_5_6`: recall=0.1389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.214 | 0.143 |
| low_1_2 | 0.594 | 0.219 | 0.156 | 0.031 |
| mid_3_4 | 0.618 | 0.118 | 0.206 | 0.059 |
| high_5_6 | 0.444 | 0.111 | 0.306 | 0.139 |

## ecg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2609)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.0000, support=32
- `mid_3_4`: recall=0.3235, support=34
- `high_5_6`: recall=0.1667, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.357 | 0.071 |
| low_1_2 | 0.406 | 0.000 | 0.562 | 0.031 |
| mid_3_4 | 0.618 | 0.000 | 0.324 | 0.059 |
| high_5_6 | 0.611 | 0.000 | 0.222 | 0.167 |

## ecg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.3396)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.2500, support=36
- `mid_3_4`: recall=0.1667, support=36
- `high_5_6`: recall=0.7222, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.214 | 0.214 |
| low_1_2 | 0.250 | 0.250 | 0.083 | 0.417 |
| mid_3_4 | 0.194 | 0.167 | 0.167 | 0.472 |
| high_5_6 | 0.056 | 0.139 | 0.083 | 0.722 |

## ecg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.3187)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.0556, support=36
- `high_5_6`: recall=0.3611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.429 | 0.071 | 0.143 |
| low_1_2 | 0.139 | 0.444 | 0.194 | 0.222 |
| mid_3_4 | 0.139 | 0.500 | 0.056 | 0.306 |
| high_5_6 | 0.167 | 0.389 | 0.083 | 0.361 |

## ecg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.3125)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.1667, support=36
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.429 | 0.071 | 0.143 |
| low_1_2 | 0.167 | 0.389 | 0.278 | 0.167 |
| mid_3_4 | 0.250 | 0.389 | 0.167 | 0.194 |
| high_5_6 | 0.167 | 0.417 | 0.111 | 0.306 |

## ecg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2729)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.2222, support=36
- `high_5_6`: recall=0.3333, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.143 | 0.214 |
| low_1_2 | 0.194 | 0.278 | 0.278 | 0.250 |
| mid_3_4 | 0.139 | 0.306 | 0.222 | 0.333 |
| high_5_6 | 0.139 | 0.250 | 0.278 | 0.333 |

## ecg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.2729)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.1111, support=36
- `high_5_6`: recall=0.5833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.071 | 0.286 |
| low_1_2 | 0.167 | 0.306 | 0.167 | 0.361 |
| mid_3_4 | 0.167 | 0.333 | 0.111 | 0.389 |
| high_5_6 | 0.056 | 0.139 | 0.222 | 0.583 |

## ecg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.2708)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.0000, support=36
- `high_5_6`: recall=0.5278, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.000 | 0.286 |
| low_1_2 | 0.222 | 0.389 | 0.056 | 0.333 |
| mid_3_4 | 0.306 | 0.278 | 0.000 | 0.417 |
| high_5_6 | 0.194 | 0.278 | 0.000 | 0.528 |

## ecg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2646)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.2500, support=36
- `high_5_6`: recall=0.2778, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.143 | 0.357 |
| low_1_2 | 0.111 | 0.278 | 0.222 | 0.389 |
| mid_3_4 | 0.167 | 0.306 | 0.250 | 0.278 |
| high_5_6 | 0.167 | 0.306 | 0.250 | 0.278 |

## ecg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.2625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/ecg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.1389, support=36
- `mid_3_4`: recall=0.0833, support=36
- `high_5_6`: recall=0.5000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.000 | 0.357 |
| low_1_2 | 0.278 | 0.139 | 0.139 | 0.444 |
| mid_3_4 | 0.333 | 0.167 | 0.083 | 0.417 |
| high_5_6 | 0.167 | 0.222 | 0.111 | 0.500 |

## eeg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3441)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.3832, support=107
- `mid_3_4`: recall=0.2692, support=104
- `high_5_6`: recall=0.3786, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.243 | 0.108 | 0.324 |
| low_1_2 | 0.140 | 0.383 | 0.168 | 0.308 |
| mid_3_4 | 0.212 | 0.260 | 0.269 | 0.260 |
| high_5_6 | 0.194 | 0.223 | 0.204 | 0.379 |

## eeg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3390)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3514, support=37
- `low_1_2`: recall=0.3458, support=107
- `mid_3_4`: recall=0.1154, support=104
- `high_5_6`: recall=0.5340, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.351 | 0.243 | 0.189 | 0.216 |
| low_1_2 | 0.262 | 0.346 | 0.084 | 0.308 |
| mid_3_4 | 0.298 | 0.154 | 0.115 | 0.433 |
| high_5_6 | 0.272 | 0.126 | 0.068 | 0.534 |

## eeg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3327)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.3514, support=37
- `low_1_2`: recall=0.1402, support=107
- `mid_3_4`: recall=0.4423, support=104
- `high_5_6`: recall=0.3786, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.351 | 0.081 | 0.378 | 0.189 |
| low_1_2 | 0.336 | 0.140 | 0.355 | 0.168 |
| mid_3_4 | 0.269 | 0.029 | 0.442 | 0.260 |
| high_5_6 | 0.175 | 0.049 | 0.398 | 0.379 |

## eeg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.3297)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `low_1_2`: recall=0.3832, support=107
- `mid_3_4`: recall=0.1442, support=104
- `high_5_6`: recall=0.5437, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.162 | 0.405 | 0.162 | 0.270 |
| low_1_2 | 0.140 | 0.383 | 0.196 | 0.280 |
| mid_3_4 | 0.144 | 0.288 | 0.144 | 0.423 |
| high_5_6 | 0.155 | 0.214 | 0.087 | 0.544 |

## eeg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3188)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.3514, support=37
- `low_1_2`: recall=0.2430, support=107
- `mid_3_4`: recall=0.2115, support=104
- `high_5_6`: recall=0.3981, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.351 | 0.135 | 0.243 | 0.270 |
| low_1_2 | 0.243 | 0.243 | 0.196 | 0.318 |
| mid_3_4 | 0.192 | 0.192 | 0.212 | 0.404 |
| high_5_6 | 0.184 | 0.165 | 0.252 | 0.398 |

## eeg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.3160)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `low_1_2`: recall=0.1776, support=107
- `mid_3_4`: recall=0.3654, support=104
- `high_5_6`: recall=0.4563, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.270 | 0.108 | 0.378 | 0.243 |
| low_1_2 | 0.364 | 0.178 | 0.318 | 0.140 |
| mid_3_4 | 0.250 | 0.029 | 0.365 | 0.356 |
| high_5_6 | 0.165 | 0.058 | 0.320 | 0.456 |

## eeg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3154)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.1963, support=107
- `mid_3_4`: recall=0.3077, support=104
- `high_5_6`: recall=0.3981, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.189 | 0.243 | 0.243 |
| low_1_2 | 0.196 | 0.196 | 0.355 | 0.252 |
| mid_3_4 | 0.298 | 0.115 | 0.308 | 0.279 |
| high_5_6 | 0.320 | 0.058 | 0.223 | 0.398 |

## eeg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2650)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.0748, support=107
- `mid_3_4`: recall=0.3846, support=104
- `high_5_6`: recall=0.2524, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.054 | 0.405 | 0.216 |
| low_1_2 | 0.308 | 0.075 | 0.402 | 0.215 |
| mid_3_4 | 0.288 | 0.077 | 0.385 | 0.250 |
| high_5_6 | 0.291 | 0.068 | 0.388 | 0.252 |

## eeg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.4344)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.7812, support=32
- `mid_3_4`: recall=0.0882, support=34
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.357 | 0.071 | 0.000 |
| low_1_2 | 0.062 | 0.781 | 0.062 | 0.094 |
| mid_3_4 | 0.265 | 0.529 | 0.088 | 0.118 |
| high_5_6 | 0.111 | 0.472 | 0.111 | 0.306 |

## eeg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.4086)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.1875, support=32
- `mid_3_4`: recall=0.2353, support=34
- `high_5_6`: recall=0.6389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.071 | 0.143 |
| low_1_2 | 0.281 | 0.188 | 0.281 | 0.250 |
| mid_3_4 | 0.265 | 0.324 | 0.235 | 0.176 |
| high_5_6 | 0.167 | 0.139 | 0.056 | 0.639 |

## eeg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.3738)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.8125, support=32
- `mid_3_4`: recall=0.0882, support=34
- `high_5_6`: recall=0.1667, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.500 | 0.071 | 0.000 |
| low_1_2 | 0.062 | 0.812 | 0.094 | 0.031 |
| mid_3_4 | 0.059 | 0.735 | 0.088 | 0.118 |
| high_5_6 | 0.028 | 0.667 | 0.139 | 0.167 |

## eeg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.3531)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.5625, support=32
- `mid_3_4`: recall=0.0294, support=34
- `high_5_6`: recall=0.5000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.000 | 0.286 |
| low_1_2 | 0.000 | 0.562 | 0.000 | 0.438 |
| mid_3_4 | 0.029 | 0.588 | 0.029 | 0.353 |
| high_5_6 | 0.000 | 0.389 | 0.111 | 0.500 |

## eeg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.3512)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.6562, support=32
- `mid_3_4`: recall=0.0000, support=34
- `high_5_6`: recall=0.5833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.571 | 0.071 | 0.214 |
| low_1_2 | 0.031 | 0.656 | 0.000 | 0.312 |
| mid_3_4 | 0.118 | 0.471 | 0.000 | 0.412 |
| high_5_6 | 0.056 | 0.333 | 0.028 | 0.583 |

## eeg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.3487)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.2500, support=32
- `mid_3_4`: recall=0.2353, support=34
- `high_5_6`: recall=0.3889, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.071 | 0.214 |
| low_1_2 | 0.188 | 0.250 | 0.156 | 0.406 |
| mid_3_4 | 0.265 | 0.235 | 0.235 | 0.265 |
| high_5_6 | 0.250 | 0.083 | 0.278 | 0.389 |

## eeg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.3430)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.5000, support=32
- `mid_3_4`: recall=0.0882, support=34
- `high_5_6`: recall=0.3611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.500 | 0.071 | 0.000 |
| low_1_2 | 0.281 | 0.500 | 0.031 | 0.188 |
| mid_3_4 | 0.235 | 0.529 | 0.088 | 0.147 |
| high_5_6 | 0.167 | 0.444 | 0.028 | 0.361 |

## eeg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.5625, support=32
- `mid_3_4`: recall=0.0588, support=34
- `high_5_6`: recall=0.4722, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.714 | 0.071 | 0.214 |
| low_1_2 | 0.000 | 0.562 | 0.000 | 0.438 |
| mid_3_4 | 0.029 | 0.647 | 0.059 | 0.265 |
| high_5_6 | 0.000 | 0.444 | 0.083 | 0.472 |

## eeg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.4750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.6389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.143 | 0.071 |
| low_1_2 | 0.111 | 0.444 | 0.250 | 0.194 |
| mid_3_4 | 0.083 | 0.250 | 0.361 | 0.306 |
| high_5_6 | 0.028 | 0.111 | 0.222 | 0.639 |

## eeg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.4021)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.5278, support=36
- `mid_3_4`: recall=0.2222, support=36
- `high_5_6`: recall=0.4722, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.357 | 0.143 | 0.071 |
| low_1_2 | 0.056 | 0.528 | 0.222 | 0.194 |
| mid_3_4 | 0.056 | 0.361 | 0.222 | 0.361 |
| high_5_6 | 0.028 | 0.194 | 0.306 | 0.472 |

## eeg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.3875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.4722, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.143 | 0.143 |
| low_1_2 | 0.306 | 0.306 | 0.194 | 0.194 |
| mid_3_4 | 0.111 | 0.278 | 0.361 | 0.250 |
| high_5_6 | 0.056 | 0.250 | 0.222 | 0.472 |

## eeg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.3812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.1944, support=36
- `mid_3_4`: recall=0.5000, support=36
- `high_5_6`: recall=0.4444, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.143 | 0.286 |
| low_1_2 | 0.278 | 0.194 | 0.306 | 0.222 |
| mid_3_4 | 0.111 | 0.111 | 0.500 | 0.278 |
| high_5_6 | 0.083 | 0.111 | 0.361 | 0.444 |

## eeg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.3667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.3333, support=36
- `high_5_6`: recall=0.6111, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.357 | 0.143 | 0.214 |
| low_1_2 | 0.250 | 0.306 | 0.306 | 0.139 |
| mid_3_4 | 0.111 | 0.222 | 0.333 | 0.333 |
| high_5_6 | 0.139 | 0.167 | 0.083 | 0.611 |

## eeg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.3563)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3611, support=36
- `mid_3_4`: recall=0.1944, support=36
- `high_5_6`: recall=0.6389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.071 | 0.214 |
| low_1_2 | 0.167 | 0.361 | 0.222 | 0.250 |
| mid_3_4 | 0.056 | 0.389 | 0.194 | 0.361 |
| high_5_6 | 0.083 | 0.194 | 0.083 | 0.639 |

## eeg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.3500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.2222, support=36
- `mid_3_4`: recall=0.5556, support=36
- `high_5_6`: recall=0.3333, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.143 | 0.357 |
| low_1_2 | 0.139 | 0.222 | 0.361 | 0.278 |
| mid_3_4 | 0.111 | 0.139 | 0.556 | 0.194 |
| high_5_6 | 0.056 | 0.083 | 0.528 | 0.333 |

## eeg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.3146)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/eeg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.1111, support=36
- `mid_3_4`: recall=0.5000, support=36
- `high_5_6`: recall=0.3889, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.286 | 0.214 |
| low_1_2 | 0.167 | 0.111 | 0.417 | 0.306 |
| mid_3_4 | 0.139 | 0.111 | 0.500 | 0.250 |
| high_5_6 | 0.028 | 0.028 | 0.556 | 0.389 |

## fused | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2949)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2368, support=38
- `low_1_2`: recall=0.2037, support=108
- `mid_3_4`: recall=0.0926, support=108
- `high_5_6`: recall=0.7075, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.237 | 0.105 | 0.105 | 0.553 |
| low_1_2 | 0.102 | 0.204 | 0.074 | 0.620 |
| mid_3_4 | 0.093 | 0.120 | 0.093 | 0.694 |
| high_5_6 | 0.075 | 0.151 | 0.066 | 0.708 |

## fused | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2851)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `low_1_2`: recall=0.2778, support=108
- `mid_3_4`: recall=0.1852, support=108
- `high_5_6`: recall=0.6321, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.132 | 0.132 | 0.184 | 0.553 |
| low_1_2 | 0.065 | 0.278 | 0.130 | 0.528 |
| mid_3_4 | 0.093 | 0.120 | 0.185 | 0.602 |
| high_5_6 | 0.019 | 0.179 | 0.170 | 0.632 |

## fused | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2824)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3684, support=38
- `low_1_2`: recall=0.0370, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.7642, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.368 | 0.053 | 0.000 | 0.579 |
| low_1_2 | 0.231 | 0.037 | 0.000 | 0.731 |
| mid_3_4 | 0.231 | 0.019 | 0.000 | 0.750 |
| high_5_6 | 0.179 | 0.057 | 0.000 | 0.764 |

## fused | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2722)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `low_1_2`: recall=0.2407, support=108
- `mid_3_4`: recall=0.0926, support=108
- `high_5_6`: recall=0.6792, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.105 | 0.211 | 0.132 | 0.553 |
| low_1_2 | 0.111 | 0.241 | 0.083 | 0.565 |
| mid_3_4 | 0.093 | 0.176 | 0.093 | 0.639 |
| high_5_6 | 0.075 | 0.189 | 0.057 | 0.679 |

## fused | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2649)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `low_1_2`: recall=0.0185, support=108
- `mid_3_4`: recall=0.0556, support=108
- `high_5_6`: recall=0.8679, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.132 | 0.079 | 0.000 | 0.789 |
| low_1_2 | 0.074 | 0.019 | 0.056 | 0.852 |
| mid_3_4 | 0.056 | 0.046 | 0.056 | 0.843 |
| high_5_6 | 0.066 | 0.019 | 0.047 | 0.868 |

## fused | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2581)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `low_1_2`: recall=0.0741, support=108
- `mid_3_4`: recall=0.0185, support=108
- `high_5_6`: recall=0.8962, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.053 | 0.132 | 0.000 | 0.816 |
| low_1_2 | 0.046 | 0.074 | 0.009 | 0.870 |
| mid_3_4 | 0.046 | 0.083 | 0.019 | 0.852 |
| high_5_6 | 0.009 | 0.066 | 0.028 | 0.896 |

## fused | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2`: recall=0.0000, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.0000, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## fused | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2`: recall=0.0000, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.0000, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.3542)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.9167, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.000 | 0.000 | 0.500 |
| low_1_2 | 0.278 | 0.000 | 0.083 | 0.639 |
| mid_3_4 | 0.229 | 0.029 | 0.000 | 0.743 |
| high_5_6 | 0.028 | 0.000 | 0.056 | 0.917 |

## fused | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2966)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.5278, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.500 |
| low_1_2 | 0.056 | 0.444 | 0.000 | 0.500 |
| mid_3_4 | 0.229 | 0.314 | 0.000 | 0.457 |
| high_5_6 | 0.444 | 0.028 | 0.000 | 0.528 |

## fused | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2698)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.0833, support=36
- `mid_3_4`: recall=0.0571, support=35
- `high_5_6`: recall=0.5833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.000 | 0.571 |
| low_1_2 | 0.278 | 0.083 | 0.028 | 0.611 |
| mid_3_4 | 0.229 | 0.229 | 0.057 | 0.486 |
| high_5_6 | 0.250 | 0.056 | 0.111 | 0.583 |

## fused | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2569)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.0278, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=1.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 1.000 |
| low_1_2 | 0.000 | 0.028 | 0.000 | 0.972 |
| mid_3_4 | 0.000 | 0.000 | 0.000 | 1.000 |
| high_5_6 | 0.000 | 0.000 | 0.000 | 1.000 |

## fused | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2569)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.0278, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=1.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 1.000 |
| low_1_2 | 0.000 | 0.028 | 0.000 | 0.972 |
| mid_3_4 | 0.000 | 0.000 | 0.000 | 1.000 |
| high_5_6 | 0.000 | 0.000 | 0.000 | 1.000 |

## fused | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2321)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.5000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.000 | 0.071 | 0.500 |
| low_1_2 | 0.306 | 0.000 | 0.083 | 0.611 |
| mid_3_4 | 0.457 | 0.057 | 0.000 | 0.486 |
| high_5_6 | 0.361 | 0.000 | 0.139 | 0.500 |

## fused | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.4333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.5000, support=36
- `high_5_6`: recall=0.4286, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.286 | 0.143 |
| low_1_2 | 0.139 | 0.278 | 0.361 | 0.222 |
| mid_3_4 | 0.139 | 0.111 | 0.500 | 0.250 |
| high_5_6 | 0.086 | 0.171 | 0.314 | 0.429 |

## fused | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.4042)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.2500, support=36
- `mid_3_4`: recall=0.4722, support=36
- `high_5_6`: recall=0.3714, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.286 | 0.143 |
| low_1_2 | 0.111 | 0.250 | 0.444 | 0.194 |
| mid_3_4 | 0.139 | 0.111 | 0.472 | 0.278 |
| high_5_6 | 0.086 | 0.143 | 0.400 | 0.371 |

## fused | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.3917)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `low_1_2`: recall=0.2222, support=36
- `mid_3_4`: recall=0.0278, support=36
- `high_5_6`: recall=0.4286, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.929 | 0.071 | 0.000 | 0.000 |
| low_1_2 | 0.611 | 0.222 | 0.000 | 0.167 |
| mid_3_4 | 0.583 | 0.028 | 0.028 | 0.361 |
| high_5_6 | 0.514 | 0.057 | 0.000 | 0.429 |

## fused | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.3750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.3333, support=36
- `high_5_6`: recall=0.3429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.214 | 0.214 |
| low_1_2 | 0.167 | 0.389 | 0.250 | 0.194 |
| mid_3_4 | 0.222 | 0.167 | 0.333 | 0.278 |
| high_5_6 | 0.229 | 0.314 | 0.114 | 0.343 |

## fused | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.3458)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.2286, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.500 | 0.214 |
| low_1_2 | 0.139 | 0.472 | 0.278 | 0.111 |
| mid_3_4 | 0.167 | 0.250 | 0.361 | 0.222 |
| high_5_6 | 0.229 | 0.314 | 0.229 | 0.229 |

## fused | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.3458)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.1944, support=36
- `high_5_6`: recall=0.3429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.143 | 0.214 |
| low_1_2 | 0.167 | 0.444 | 0.167 | 0.222 |
| mid_3_4 | 0.167 | 0.333 | 0.194 | 0.306 |
| high_5_6 | 0.343 | 0.314 | 0.000 | 0.343 |

## fused | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.3417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `low_1_2`: recall=0.2222, support=36
- `mid_3_4`: recall=0.0556, support=36
- `high_5_6`: recall=0.2000, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.929 | 0.000 | 0.000 | 0.071 |
| low_1_2 | 0.583 | 0.222 | 0.056 | 0.139 |
| mid_3_4 | 0.528 | 0.139 | 0.056 | 0.278 |
| high_5_6 | 0.514 | 0.086 | 0.200 | 0.200 |

## fused | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.3042)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/fused/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.2500, support=36
- `high_5_6`: recall=0.3429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.357 | 0.214 |
| low_1_2 | 0.139 | 0.389 | 0.222 | 0.250 |
| mid_3_4 | 0.250 | 0.194 | 0.250 | 0.306 |
| high_5_6 | 0.286 | 0.229 | 0.143 | 0.343 |

## pupil | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2900)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2`: recall=0.2963, support=108
- `mid_3_4`: recall=0.2222, support=108
- `high_5_6`: recall=0.5566, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.184 | 0.211 | 0.158 | 0.447 |
| low_1_2 | 0.065 | 0.296 | 0.130 | 0.509 |
| mid_3_4 | 0.074 | 0.130 | 0.222 | 0.574 |
| high_5_6 | 0.028 | 0.217 | 0.198 | 0.557 |

## pupil | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2879)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2895, support=38
- `low_1_2`: recall=0.1852, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.7075, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.289 | 0.158 | 0.000 | 0.553 |
| low_1_2 | 0.185 | 0.185 | 0.000 | 0.630 |
| mid_3_4 | 0.157 | 0.120 | 0.000 | 0.722 |
| high_5_6 | 0.160 | 0.132 | 0.000 | 0.708 |

## pupil | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2795)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3947, support=38
- `low_1_2`: recall=0.0093, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.7547, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.395 | 0.053 | 0.000 | 0.553 |
| low_1_2 | 0.250 | 0.009 | 0.000 | 0.741 |
| mid_3_4 | 0.231 | 0.000 | 0.000 | 0.769 |
| high_5_6 | 0.179 | 0.066 | 0.000 | 0.755 |

## pupil | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2668)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3158, support=38
- `low_1_2`: recall=0.1759, support=108
- `mid_3_4`: recall=0.0926, support=108
- `high_5_6`: recall=0.5472, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.316 | 0.158 | 0.132 | 0.395 |
| low_1_2 | 0.315 | 0.176 | 0.083 | 0.426 |
| mid_3_4 | 0.269 | 0.167 | 0.093 | 0.472 |
| high_5_6 | 0.236 | 0.160 | 0.057 | 0.547 |

## pupil | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2547)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `low_1_2`: recall=0.0185, support=108
- `mid_3_4`: recall=0.0463, support=108
- `high_5_6`: recall=0.9057, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.053 | 0.132 | 0.000 | 0.816 |
| low_1_2 | 0.037 | 0.019 | 0.056 | 0.889 |
| mid_3_4 | 0.046 | 0.056 | 0.046 | 0.852 |
| high_5_6 | 0.028 | 0.047 | 0.019 | 0.906 |

## pupil | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2545)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `low_1_2`: recall=0.3519, support=108
- `mid_3_4`: recall=0.0278, support=108
- `high_5_6`: recall=0.5283, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.105 | 0.474 | 0.000 | 0.421 |
| low_1_2 | 0.065 | 0.352 | 0.056 | 0.528 |
| mid_3_4 | 0.074 | 0.380 | 0.028 | 0.519 |
| high_5_6 | 0.057 | 0.377 | 0.038 | 0.528 |

## pupil | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2`: recall=0.0000, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.0000, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## pupil | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=38
- `low_1_2`: recall=0.0000, support=108
- `mid_3_4`: recall=0.0000, support=108
- `high_5_6`: recall=0.0000, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2901)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.0857, support=35
- `high_5_6`: recall=0.5833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.143 | 0.286 |
| low_1_2 | 0.056 | 0.278 | 0.167 | 0.500 |
| mid_3_4 | 0.086 | 0.400 | 0.086 | 0.429 |
| high_5_6 | 0.139 | 0.222 | 0.056 | 0.583 |

## pupil | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2688)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.3611, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.5000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.500 |
| low_1_2 | 0.056 | 0.361 | 0.083 | 0.500 |
| mid_3_4 | 0.143 | 0.371 | 0.000 | 0.486 |
| high_5_6 | 0.472 | 0.028 | 0.000 | 0.500 |

## pupil | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2569)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.0278, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=1.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 1.000 |
| low_1_2 | 0.000 | 0.028 | 0.000 | 0.972 |
| mid_3_4 | 0.000 | 0.000 | 0.000 | 1.000 |
| high_5_6 | 0.000 | 0.000 | 0.000 | 1.000 |

## pupil | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.5143, support=35
- `high_5_6`: recall=0.5000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.500 | 0.500 |
| low_1_2 | 0.000 | 0.000 | 0.500 | 0.500 |
| mid_3_4 | 0.000 | 0.000 | 0.514 | 0.486 |
| high_5_6 | 0.000 | 0.000 | 0.500 | 0.500 |

## pupil | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=1.0000, support=14
- `low_1_2`: recall=0.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 1.000 | 0.000 | 0.000 | 0.000 |
| low_1_2 | 1.000 | 0.000 | 0.000 | 0.000 |
| mid_3_4 | 1.000 | 0.000 | 0.000 | 0.000 |
| high_5_6 | 1.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2391)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.1944, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.3333, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.000 | 0.429 |
| low_1_2 | 0.583 | 0.194 | 0.083 | 0.139 |
| mid_3_4 | 0.400 | 0.286 | 0.000 | 0.314 |
| high_5_6 | 0.556 | 0.111 | 0.000 | 0.333 |

## pupil | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2341)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.4444, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.500 |
| low_1_2 | 0.056 | 0.278 | 0.167 | 0.500 |
| mid_3_4 | 0.143 | 0.400 | 0.000 | 0.457 |
| high_5_6 | 0.444 | 0.083 | 0.028 | 0.444 |

## pupil | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.4625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.5833, support=36
- `high_5_6`: recall=0.4000, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.214 | 0.214 |
| low_1_2 | 0.194 | 0.306 | 0.333 | 0.167 |
| mid_3_4 | 0.194 | 0.056 | 0.583 | 0.167 |
| high_5_6 | 0.143 | 0.057 | 0.400 | 0.400 |

## pupil | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.4375)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.5000, support=36
- `high_5_6`: recall=0.3429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.714 | 0.071 | 0.143 | 0.071 |
| low_1_2 | 0.333 | 0.278 | 0.306 | 0.083 |
| mid_3_4 | 0.306 | 0.028 | 0.500 | 0.167 |
| high_5_6 | 0.171 | 0.171 | 0.314 | 0.343 |

## pupil | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.3687)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.3333, support=36
- `high_5_6`: recall=0.4286, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.286 | 0.214 |
| low_1_2 | 0.139 | 0.389 | 0.250 | 0.222 |
| mid_3_4 | 0.222 | 0.139 | 0.333 | 0.306 |
| high_5_6 | 0.200 | 0.314 | 0.057 | 0.429 |

## pupil | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.3458)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.1944, support=36
- `high_5_6`: recall=0.3429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.071 | 0.286 |
| low_1_2 | 0.167 | 0.444 | 0.167 | 0.222 |
| mid_3_4 | 0.167 | 0.333 | 0.194 | 0.306 |
| high_5_6 | 0.343 | 0.314 | 0.000 | 0.343 |

## pupil | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.3458)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2`: recall=0.1667, support=36
- `mid_3_4`: recall=0.1389, support=36
- `high_5_6`: recall=0.4000, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.143 | 0.000 |
| low_1_2 | 0.556 | 0.167 | 0.111 | 0.167 |
| mid_3_4 | 0.639 | 0.028 | 0.139 | 0.194 |
| high_5_6 | 0.543 | 0.029 | 0.029 | 0.400 |

## pupil | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.3438)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.4722, support=36
- `high_5_6`: recall=0.2286, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.500 | 0.214 |
| low_1_2 | 0.139 | 0.472 | 0.278 | 0.111 |
| mid_3_4 | 0.139 | 0.167 | 0.472 | 0.222 |
| high_5_6 | 0.229 | 0.314 | 0.229 | 0.229 |

## pupil | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.3104)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3611, support=36
- `mid_3_4`: recall=0.2778, support=36
- `high_5_6`: recall=0.3714, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.429 | 0.143 |
| low_1_2 | 0.139 | 0.361 | 0.306 | 0.194 |
| mid_3_4 | 0.250 | 0.222 | 0.278 | 0.250 |
| high_5_6 | 0.257 | 0.229 | 0.143 | 0.371 |

## pupil | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.3083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline_advanced_nn/pupil/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2`: recall=0.1389, support=36
- `mid_3_4`: recall=0.1111, support=36
- `high_5_6`: recall=0.3143, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.143 | 0.000 |
| low_1_2 | 0.583 | 0.139 | 0.111 | 0.167 |
| mid_3_4 | 0.639 | 0.000 | 0.111 | 0.250 |
| high_5_6 | 0.543 | 0.029 | 0.114 | 0.314 |


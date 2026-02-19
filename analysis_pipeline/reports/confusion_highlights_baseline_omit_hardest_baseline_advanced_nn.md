# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline_advanced_nn.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1779)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.1698, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.1373, support=51
- `5.1-6.0`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.081 | 0.135 | 0.135 | 0.108 | 0.162 | 0.108 |
| 0.6-1.5 | 0.151 | 0.170 | 0.132 | 0.057 | 0.075 | 0.170 | 0.245 |
| 1.5-2.4 | 0.259 | 0.167 | 0.074 | 0.167 | 0.056 | 0.130 | 0.148 |
| 2.4-3.3 | 0.196 | 0.039 | 0.176 | 0.078 | 0.118 | 0.157 | 0.235 |
| 3.3-4.2 | 0.208 | 0.075 | 0.057 | 0.057 | 0.170 | 0.094 | 0.340 |
| 4.2-5.1 | 0.314 | 0.118 | 0.039 | 0.039 | 0.059 | 0.137 | 0.294 |
| 5.1-6.0 | 0.250 | 0.115 | 0.038 | 0.077 | 0.135 | 0.096 | 0.288 |

## ecg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1613)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.0000, support=53
- `1.5-2.4`: recall=0.2963, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.1569, support=51
- `5.1-6.0`: recall=0.4231, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.000 | 0.243 | 0.135 | 0.000 | 0.216 | 0.270 |
| 0.6-1.5 | 0.038 | 0.000 | 0.189 | 0.075 | 0.019 | 0.151 | 0.528 |
| 1.5-2.4 | 0.093 | 0.000 | 0.296 | 0.148 | 0.037 | 0.093 | 0.333 |
| 2.4-3.3 | 0.118 | 0.000 | 0.235 | 0.137 | 0.020 | 0.078 | 0.412 |
| 3.3-4.2 | 0.151 | 0.000 | 0.226 | 0.094 | 0.038 | 0.075 | 0.415 |
| 4.2-5.1 | 0.098 | 0.000 | 0.176 | 0.098 | 0.020 | 0.157 | 0.451 |
| 5.1-6.0 | 0.096 | 0.000 | 0.231 | 0.135 | 0.000 | 0.115 | 0.423 |

## ecg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1563)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3514, support=37
- `0.6-1.5`: recall=0.0000, support=53
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.351 | 0.000 | 0.162 | 0.081 | 0.162 | 0.243 | 0.000 |
| 0.6-1.5 | 0.358 | 0.000 | 0.151 | 0.038 | 0.132 | 0.208 | 0.113 |
| 1.5-2.4 | 0.370 | 0.000 | 0.222 | 0.056 | 0.167 | 0.093 | 0.093 |
| 2.4-3.3 | 0.392 | 0.000 | 0.275 | 0.020 | 0.098 | 0.176 | 0.039 |
| 3.3-4.2 | 0.377 | 0.000 | 0.226 | 0.019 | 0.151 | 0.132 | 0.094 |
| 4.2-5.1 | 0.235 | 0.000 | 0.157 | 0.098 | 0.176 | 0.255 | 0.078 |
| 5.1-6.0 | 0.385 | 0.000 | 0.173 | 0.096 | 0.077 | 0.192 | 0.077 |

## ecg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1559)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `0.6-1.5`: recall=0.0377, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.3725, support=51
- `5.1-6.0`: recall=0.0000, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.027 | 0.135 | 0.054 | 0.243 | 0.243 | 0.000 |
| 0.6-1.5 | 0.283 | 0.038 | 0.075 | 0.057 | 0.189 | 0.358 | 0.000 |
| 1.5-2.4 | 0.204 | 0.074 | 0.148 | 0.074 | 0.204 | 0.296 | 0.000 |
| 2.4-3.3 | 0.314 | 0.059 | 0.176 | 0.039 | 0.176 | 0.235 | 0.000 |
| 3.3-4.2 | 0.321 | 0.000 | 0.132 | 0.019 | 0.189 | 0.340 | 0.000 |
| 4.2-5.1 | 0.235 | 0.059 | 0.098 | 0.059 | 0.176 | 0.373 | 0.000 |
| 5.1-6.0 | 0.269 | 0.077 | 0.135 | 0.077 | 0.154 | 0.288 | 0.000 |

## ecg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1526)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.108 | 0.108 | 0.162 | 0.162 | 0.216 | 0.081 |
| 0.6-1.5 | 0.132 | 0.208 | 0.151 | 0.057 | 0.132 | 0.245 | 0.075 |
| 1.5-2.4 | 0.278 | 0.185 | 0.111 | 0.074 | 0.130 | 0.074 | 0.148 |
| 2.4-3.3 | 0.216 | 0.118 | 0.059 | 0.078 | 0.157 | 0.235 | 0.137 |
| 3.3-4.2 | 0.189 | 0.113 | 0.057 | 0.113 | 0.170 | 0.189 | 0.170 |
| 4.2-5.1 | 0.275 | 0.118 | 0.078 | 0.020 | 0.176 | 0.216 | 0.118 |
| 5.1-6.0 | 0.231 | 0.154 | 0.038 | 0.096 | 0.192 | 0.154 | 0.135 |

## ecg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1473)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.0755, support=53
- `4.2-5.1`: recall=0.0196, support=51
- `5.1-6.0`: recall=0.4038, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.135 | 0.108 | 0.081 | 0.189 | 0.108 | 0.270 |
| 0.6-1.5 | 0.057 | 0.226 | 0.094 | 0.075 | 0.038 | 0.057 | 0.453 |
| 1.5-2.4 | 0.056 | 0.241 | 0.093 | 0.185 | 0.093 | 0.019 | 0.315 |
| 2.4-3.3 | 0.098 | 0.157 | 0.157 | 0.137 | 0.039 | 0.039 | 0.373 |
| 3.3-4.2 | 0.094 | 0.189 | 0.208 | 0.019 | 0.075 | 0.094 | 0.321 |
| 4.2-5.1 | 0.137 | 0.137 | 0.118 | 0.118 | 0.039 | 0.020 | 0.431 |
| 5.1-6.0 | 0.077 | 0.192 | 0.173 | 0.096 | 0.038 | 0.019 | 0.404 |

## ecg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1460)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.2037, support=54
- `2.4-3.3`: recall=0.2353, support=51
- `3.3-4.2`: recall=0.0000, support=53
- `4.2-5.1`: recall=0.2353, support=51
- `5.1-6.0`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.108 | 0.081 | 0.324 | 0.000 | 0.216 | 0.162 |
| 0.6-1.5 | 0.075 | 0.057 | 0.283 | 0.132 | 0.000 | 0.151 | 0.302 |
| 1.5-2.4 | 0.037 | 0.111 | 0.204 | 0.241 | 0.000 | 0.056 | 0.352 |
| 2.4-3.3 | 0.098 | 0.039 | 0.176 | 0.235 | 0.000 | 0.137 | 0.314 |
| 3.3-4.2 | 0.057 | 0.019 | 0.245 | 0.226 | 0.000 | 0.094 | 0.358 |
| 4.2-5.1 | 0.098 | 0.078 | 0.137 | 0.196 | 0.000 | 0.235 | 0.255 |
| 5.1-6.0 | 0.019 | 0.115 | 0.269 | 0.192 | 0.000 | 0.212 | 0.192 |

## ecg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1339)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.0000, support=53
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.2745, support=51
- `5.1-6.0`: recall=0.0192, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.000 | 0.189 | 0.054 | 0.243 | 0.243 | 0.000 |
| 0.6-1.5 | 0.321 | 0.000 | 0.151 | 0.057 | 0.170 | 0.226 | 0.075 |
| 1.5-2.4 | 0.167 | 0.019 | 0.259 | 0.074 | 0.259 | 0.148 | 0.074 |
| 2.4-3.3 | 0.235 | 0.000 | 0.333 | 0.020 | 0.196 | 0.176 | 0.039 |
| 3.3-4.2 | 0.245 | 0.000 | 0.358 | 0.019 | 0.132 | 0.170 | 0.075 |
| 4.2-5.1 | 0.216 | 0.000 | 0.157 | 0.078 | 0.196 | 0.275 | 0.078 |
| 5.1-6.0 | 0.269 | 0.000 | 0.173 | 0.077 | 0.192 | 0.269 | 0.019 |

## ecg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2306)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.000 | 0.143 | 0.143 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.688 | 0.000 | 0.188 | 0.062 | 0.000 | 0.000 | 0.062 |
| 1.5-2.4 | 0.500 | 0.000 | 0.188 | 0.312 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.412 | 0.000 | 0.118 | 0.471 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.471 | 0.000 | 0.059 | 0.294 | 0.059 | 0.118 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.222 | 0.000 | 0.222 | 0.056 |
| 5.1-6.0 | 0.611 | 0.000 | 0.000 | 0.111 | 0.167 | 0.111 | 0.000 |

## ecg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1881)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.3125, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.286 | 0.143 | 0.071 | 0.000 | 0.071 | 0.143 |
| 0.6-1.5 | 0.438 | 0.312 | 0.125 | 0.000 | 0.000 | 0.000 | 0.125 |
| 1.5-2.4 | 0.438 | 0.438 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.529 | 0.353 | 0.000 | 0.059 | 0.000 | 0.000 | 0.059 |
| 3.3-4.2 | 0.353 | 0.294 | 0.118 | 0.118 | 0.000 | 0.059 | 0.059 |
| 4.2-5.1 | 0.333 | 0.222 | 0.000 | 0.111 | 0.000 | 0.167 | 0.167 |
| 5.1-6.0 | 0.444 | 0.000 | 0.056 | 0.056 | 0.056 | 0.056 | 0.333 |

## ecg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1832)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1875, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.4118, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.214 | 0.143 | 0.000 | 0.143 | 0.143 |
| 0.6-1.5 | 0.125 | 0.188 | 0.312 | 0.000 | 0.062 | 0.188 | 0.125 |
| 1.5-2.4 | 0.188 | 0.188 | 0.125 | 0.375 | 0.000 | 0.000 | 0.125 |
| 2.4-3.3 | 0.176 | 0.118 | 0.000 | 0.412 | 0.000 | 0.118 | 0.176 |
| 3.3-4.2 | 0.412 | 0.000 | 0.176 | 0.235 | 0.059 | 0.000 | 0.118 |
| 4.2-5.1 | 0.111 | 0.056 | 0.056 | 0.389 | 0.111 | 0.167 | 0.111 |
| 5.1-6.0 | 0.111 | 0.222 | 0.000 | 0.167 | 0.167 | 0.167 | 0.167 |

## ecg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1801)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.5000, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.500 | 0.143 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.312 | 0.000 | 0.500 | 0.125 | 0.000 | 0.000 | 0.062 |
| 1.5-2.4 | 0.375 | 0.000 | 0.500 | 0.062 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.412 | 0.000 | 0.412 | 0.176 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.294 | 0.000 | 0.353 | 0.176 | 0.000 | 0.176 | 0.000 |
| 4.2-5.1 | 0.222 | 0.000 | 0.278 | 0.111 | 0.000 | 0.333 | 0.056 |
| 5.1-6.0 | 0.389 | 0.000 | 0.278 | 0.222 | 0.000 | 0.111 | 0.000 |

## ecg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1674)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1875, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.3529, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.143 | 0.286 | 0.000 | 0.143 | 0.071 |
| 0.6-1.5 | 0.188 | 0.188 | 0.312 | 0.062 | 0.000 | 0.000 | 0.250 |
| 1.5-2.4 | 0.250 | 0.312 | 0.062 | 0.250 | 0.000 | 0.062 | 0.062 |
| 2.4-3.3 | 0.235 | 0.059 | 0.118 | 0.353 | 0.000 | 0.118 | 0.118 |
| 3.3-4.2 | 0.294 | 0.059 | 0.235 | 0.118 | 0.000 | 0.176 | 0.118 |
| 4.2-5.1 | 0.222 | 0.056 | 0.056 | 0.278 | 0.000 | 0.167 | 0.222 |
| 5.1-6.0 | 0.222 | 0.222 | 0.167 | 0.111 | 0.000 | 0.056 | 0.222 |

## ecg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1616)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.4118, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.000 | 0.500 | 0.143 | 0.143 | 0.000 |
| 0.6-1.5 | 0.125 | 0.125 | 0.062 | 0.375 | 0.312 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.188 | 0.000 | 0.438 | 0.188 | 0.000 | 0.125 |
| 2.4-3.3 | 0.059 | 0.176 | 0.000 | 0.412 | 0.059 | 0.235 | 0.059 |
| 3.3-4.2 | 0.235 | 0.059 | 0.000 | 0.353 | 0.118 | 0.235 | 0.000 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.278 | 0.167 | 0.389 | 0.056 |
| 5.1-6.0 | 0.278 | 0.000 | 0.000 | 0.278 | 0.222 | 0.222 | 0.000 |

## ecg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1512)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.000 | 0.500 | 0.000 | 0.071 | 0.071 |
| 0.6-1.5 | 0.188 | 0.000 | 0.062 | 0.375 | 0.312 | 0.000 | 0.062 |
| 1.5-2.4 | 0.375 | 0.000 | 0.000 | 0.625 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.471 | 0.000 | 0.059 | 0.471 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.294 | 0.000 | 0.000 | 0.412 | 0.059 | 0.118 | 0.118 |
| 4.2-5.1 | 0.389 | 0.000 | 0.000 | 0.222 | 0.000 | 0.111 | 0.278 |
| 5.1-6.0 | 0.556 | 0.000 | 0.000 | 0.167 | 0.111 | 0.111 | 0.056 |

## ecg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1495)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.000 | 0.357 | 0.214 | 0.143 | 0.143 | 0.000 |
| 0.6-1.5 | 0.125 | 0.000 | 0.312 | 0.062 | 0.438 | 0.000 | 0.062 |
| 1.5-2.4 | 0.312 | 0.000 | 0.250 | 0.312 | 0.125 | 0.000 | 0.000 |
| 2.4-3.3 | 0.412 | 0.000 | 0.353 | 0.176 | 0.059 | 0.000 | 0.000 |
| 3.3-4.2 | 0.294 | 0.000 | 0.118 | 0.235 | 0.176 | 0.176 | 0.000 |
| 4.2-5.1 | 0.333 | 0.000 | 0.167 | 0.167 | 0.000 | 0.278 | 0.056 |
| 5.1-6.0 | 0.389 | 0.000 | 0.056 | 0.111 | 0.278 | 0.167 | 0.000 |

## ecg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.214 | 0.214 | 0.071 | 0.000 | 0.286 | 0.000 |
| 0.6-1.5 | 0.056 | 0.333 | 0.056 | 0.278 | 0.167 | 0.000 | 0.111 |
| 1.5-2.4 | 0.389 | 0.000 | 0.056 | 0.222 | 0.000 | 0.222 | 0.111 |
| 2.4-3.3 | 0.111 | 0.278 | 0.000 | 0.222 | 0.111 | 0.167 | 0.111 |
| 3.3-4.2 | 0.111 | 0.278 | 0.111 | 0.111 | 0.167 | 0.167 | 0.056 |
| 4.2-5.1 | 0.111 | 0.056 | 0.278 | 0.167 | 0.167 | 0.222 | 0.000 |
| 5.1-6.0 | 0.000 | 0.278 | 0.000 | 0.111 | 0.111 | 0.222 | 0.278 |

## ecg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.2143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.000 | 0.429 | 0.143 | 0.071 | 0.214 | 0.000 |
| 0.6-1.5 | 0.222 | 0.222 | 0.222 | 0.056 | 0.056 | 0.222 | 0.000 |
| 1.5-2.4 | 0.167 | 0.000 | 0.167 | 0.222 | 0.056 | 0.333 | 0.056 |
| 2.4-3.3 | 0.222 | 0.000 | 0.278 | 0.222 | 0.111 | 0.167 | 0.000 |
| 3.3-4.2 | 0.111 | 0.056 | 0.111 | 0.222 | 0.000 | 0.333 | 0.167 |
| 4.2-5.1 | 0.056 | 0.000 | 0.000 | 0.167 | 0.056 | 0.611 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.278 | 0.111 | 0.167 | 0.278 | 0.111 |

## ecg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.286 | 0.071 | 0.214 | 0.071 | 0.286 | 0.000 |
| 0.6-1.5 | 0.111 | 0.222 | 0.167 | 0.222 | 0.167 | 0.111 | 0.000 |
| 1.5-2.4 | 0.167 | 0.111 | 0.056 | 0.222 | 0.167 | 0.222 | 0.056 |
| 2.4-3.3 | 0.111 | 0.167 | 0.000 | 0.389 | 0.222 | 0.111 | 0.000 |
| 3.3-4.2 | 0.111 | 0.167 | 0.000 | 0.167 | 0.167 | 0.278 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.000 | 0.167 | 0.167 | 0.500 | 0.000 |
| 5.1-6.0 | 0.167 | 0.278 | 0.056 | 0.111 | 0.222 | 0.167 | 0.000 |

## ecg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.143 | 0.000 | 0.071 | 0.143 | 0.143 |
| 0.6-1.5 | 0.167 | 0.278 | 0.167 | 0.056 | 0.056 | 0.000 | 0.278 |
| 1.5-2.4 | 0.167 | 0.167 | 0.056 | 0.111 | 0.056 | 0.111 | 0.333 |
| 2.4-3.3 | 0.167 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 | 0.222 |
| 3.3-4.2 | 0.333 | 0.056 | 0.111 | 0.056 | 0.000 | 0.222 | 0.222 |
| 4.2-5.1 | 0.167 | 0.000 | 0.167 | 0.056 | 0.056 | 0.444 | 0.111 |
| 5.1-6.0 | 0.167 | 0.167 | 0.167 | 0.111 | 0.111 | 0.167 | 0.111 |

## ecg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.071 | 0.143 | 0.214 | 0.071 |
| 0.6-1.5 | 0.111 | 0.222 | 0.222 | 0.111 | 0.111 | 0.056 | 0.167 |
| 1.5-2.4 | 0.111 | 0.111 | 0.111 | 0.333 | 0.000 | 0.278 | 0.056 |
| 2.4-3.3 | 0.111 | 0.111 | 0.222 | 0.222 | 0.056 | 0.167 | 0.111 |
| 3.3-4.2 | 0.278 | 0.167 | 0.056 | 0.111 | 0.056 | 0.222 | 0.111 |
| 4.2-5.1 | 0.111 | 0.000 | 0.167 | 0.111 | 0.222 | 0.333 | 0.056 |
| 5.1-6.0 | 0.167 | 0.222 | 0.111 | 0.111 | 0.167 | 0.167 | 0.056 |

## ecg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.143 | 0.000 | 0.071 | 0.357 | 0.071 |
| 0.6-1.5 | 0.056 | 0.222 | 0.167 | 0.222 | 0.167 | 0.000 | 0.167 |
| 1.5-2.4 | 0.278 | 0.111 | 0.056 | 0.167 | 0.056 | 0.222 | 0.111 |
| 2.4-3.3 | 0.167 | 0.278 | 0.000 | 0.167 | 0.111 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.167 | 0.167 | 0.056 | 0.167 | 0.278 | 0.056 |
| 4.2-5.1 | 0.278 | 0.000 | 0.167 | 0.167 | 0.167 | 0.111 | 0.111 |
| 5.1-6.0 | 0.000 | 0.222 | 0.000 | 0.056 | 0.167 | 0.222 | 0.333 |

## ecg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.000 | 0.214 | 0.429 | 0.000 | 0.143 | 0.071 |
| 0.6-1.5 | 0.167 | 0.111 | 0.167 | 0.278 | 0.056 | 0.167 | 0.056 |
| 1.5-2.4 | 0.111 | 0.111 | 0.111 | 0.333 | 0.056 | 0.167 | 0.111 |
| 2.4-3.3 | 0.278 | 0.056 | 0.167 | 0.278 | 0.000 | 0.167 | 0.056 |
| 3.3-4.2 | 0.222 | 0.111 | 0.056 | 0.167 | 0.000 | 0.333 | 0.111 |
| 4.2-5.1 | 0.167 | 0.056 | 0.056 | 0.222 | 0.000 | 0.333 | 0.167 |
| 5.1-6.0 | 0.000 | 0.111 | 0.111 | 0.333 | 0.056 | 0.222 | 0.167 |

## ecg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/ecg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.357 | 0.000 | 0.214 | 0.000 | 0.143 |
| 0.6-1.5 | 0.167 | 0.111 | 0.333 | 0.000 | 0.222 | 0.000 | 0.167 |
| 1.5-2.4 | 0.222 | 0.111 | 0.167 | 0.000 | 0.222 | 0.167 | 0.111 |
| 2.4-3.3 | 0.333 | 0.000 | 0.222 | 0.000 | 0.111 | 0.222 | 0.111 |
| 3.3-4.2 | 0.222 | 0.111 | 0.111 | 0.000 | 0.278 | 0.111 | 0.167 |
| 4.2-5.1 | 0.111 | 0.000 | 0.111 | 0.000 | 0.333 | 0.222 | 0.222 |
| 5.1-6.0 | 0.111 | 0.056 | 0.222 | 0.000 | 0.278 | 0.111 | 0.222 |

## eeg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2088)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.3784, support=37
- `0.6-1.5`: recall=0.1698, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.2308, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.378 | 0.054 | 0.000 | 0.108 | 0.135 | 0.081 | 0.243 |
| 0.6-1.5 | 0.340 | 0.170 | 0.019 | 0.113 | 0.226 | 0.019 | 0.113 |
| 1.5-2.4 | 0.315 | 0.074 | 0.037 | 0.130 | 0.167 | 0.093 | 0.185 |
| 2.4-3.3 | 0.255 | 0.059 | 0.039 | 0.157 | 0.176 | 0.137 | 0.176 |
| 3.3-4.2 | 0.113 | 0.057 | 0.019 | 0.094 | 0.151 | 0.208 | 0.358 |
| 4.2-5.1 | 0.176 | 0.078 | 0.059 | 0.118 | 0.118 | 0.255 | 0.196 |
| 5.1-6.0 | 0.231 | 0.038 | 0.019 | 0.115 | 0.269 | 0.096 | 0.231 |

## eeg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2037)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3784, support=37
- `0.6-1.5`: recall=0.3396, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.0784, support=51
- `5.1-6.0`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.378 | 0.216 | 0.000 | 0.216 | 0.162 | 0.027 | 0.000 |
| 0.6-1.5 | 0.226 | 0.340 | 0.000 | 0.132 | 0.151 | 0.113 | 0.038 |
| 1.5-2.4 | 0.204 | 0.259 | 0.037 | 0.130 | 0.222 | 0.056 | 0.093 |
| 2.4-3.3 | 0.255 | 0.078 | 0.000 | 0.216 | 0.216 | 0.098 | 0.137 |
| 3.3-4.2 | 0.132 | 0.208 | 0.000 | 0.340 | 0.170 | 0.019 | 0.132 |
| 4.2-5.1 | 0.235 | 0.118 | 0.020 | 0.255 | 0.157 | 0.078 | 0.137 |
| 5.1-6.0 | 0.250 | 0.192 | 0.019 | 0.231 | 0.154 | 0.000 | 0.154 |

## eeg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1881)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4324, support=37
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.432 | 0.135 | 0.081 | 0.108 | 0.000 | 0.027 | 0.216 |
| 0.6-1.5 | 0.321 | 0.226 | 0.057 | 0.113 | 0.019 | 0.189 | 0.075 |
| 1.5-2.4 | 0.389 | 0.167 | 0.037 | 0.019 | 0.056 | 0.204 | 0.130 |
| 2.4-3.3 | 0.392 | 0.098 | 0.000 | 0.118 | 0.039 | 0.176 | 0.176 |
| 3.3-4.2 | 0.415 | 0.094 | 0.000 | 0.094 | 0.038 | 0.113 | 0.245 |
| 4.2-5.1 | 0.333 | 0.059 | 0.020 | 0.118 | 0.020 | 0.176 | 0.275 |
| 5.1-6.0 | 0.327 | 0.096 | 0.019 | 0.077 | 0.000 | 0.192 | 0.288 |

## eeg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1701)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `0.6-1.5`: recall=0.0755, support=53
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.2075, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.081 | 0.135 | 0.081 | 0.216 | 0.000 | 0.189 |
| 0.6-1.5 | 0.358 | 0.075 | 0.019 | 0.038 | 0.245 | 0.038 | 0.226 |
| 1.5-2.4 | 0.241 | 0.074 | 0.056 | 0.111 | 0.278 | 0.074 | 0.167 |
| 2.4-3.3 | 0.196 | 0.059 | 0.000 | 0.098 | 0.314 | 0.078 | 0.255 |
| 3.3-4.2 | 0.113 | 0.019 | 0.000 | 0.038 | 0.208 | 0.151 | 0.472 |
| 4.2-5.1 | 0.137 | 0.059 | 0.039 | 0.078 | 0.235 | 0.118 | 0.333 |
| 5.1-6.0 | 0.135 | 0.058 | 0.019 | 0.077 | 0.269 | 0.135 | 0.308 |

## eeg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1648)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.3019, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=51
- `3.3-4.2`: recall=0.0943, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.5192, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.432 | 0.027 | 0.000 | 0.027 | 0.054 | 0.243 |
| 0.6-1.5 | 0.151 | 0.302 | 0.038 | 0.038 | 0.057 | 0.019 | 0.396 |
| 1.5-2.4 | 0.148 | 0.352 | 0.000 | 0.000 | 0.074 | 0.000 | 0.426 |
| 2.4-3.3 | 0.216 | 0.314 | 0.000 | 0.000 | 0.020 | 0.020 | 0.431 |
| 3.3-4.2 | 0.189 | 0.283 | 0.038 | 0.000 | 0.094 | 0.075 | 0.321 |
| 4.2-5.1 | 0.176 | 0.255 | 0.000 | 0.000 | 0.020 | 0.039 | 0.510 |
| 5.1-6.0 | 0.115 | 0.231 | 0.000 | 0.000 | 0.019 | 0.115 | 0.519 |

## eeg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1624)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `0.6-1.5`: recall=0.0000, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.2264, support=53
- `4.2-5.1`: recall=0.2941, support=51
- `5.1-6.0`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.189 | 0.000 | 0.216 | 0.162 | 0.108 | 0.243 | 0.081 |
| 0.6-1.5 | 0.302 | 0.000 | 0.208 | 0.038 | 0.208 | 0.189 | 0.057 |
| 1.5-2.4 | 0.111 | 0.037 | 0.148 | 0.019 | 0.259 | 0.259 | 0.167 |
| 2.4-3.3 | 0.157 | 0.000 | 0.098 | 0.098 | 0.216 | 0.255 | 0.176 |
| 3.3-4.2 | 0.151 | 0.019 | 0.151 | 0.038 | 0.226 | 0.208 | 0.208 |
| 4.2-5.1 | 0.157 | 0.000 | 0.098 | 0.078 | 0.216 | 0.294 | 0.157 |
| 5.1-6.0 | 0.154 | 0.019 | 0.115 | 0.058 | 0.231 | 0.269 | 0.154 |

## eeg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1522)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.0189, support=53
- `4.2-5.1`: recall=0.1569, support=51
- `5.1-6.0`: recall=0.4423, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.324 | 0.000 | 0.054 | 0.027 | 0.108 | 0.351 |
| 0.6-1.5 | 0.094 | 0.189 | 0.038 | 0.113 | 0.113 | 0.151 | 0.302 |
| 1.5-2.4 | 0.111 | 0.241 | 0.000 | 0.167 | 0.056 | 0.056 | 0.370 |
| 2.4-3.3 | 0.196 | 0.176 | 0.000 | 0.098 | 0.020 | 0.196 | 0.314 |
| 3.3-4.2 | 0.132 | 0.208 | 0.000 | 0.132 | 0.019 | 0.151 | 0.358 |
| 4.2-5.1 | 0.098 | 0.176 | 0.000 | 0.059 | 0.039 | 0.157 | 0.471 |
| 5.1-6.0 | 0.115 | 0.096 | 0.058 | 0.058 | 0.000 | 0.231 | 0.442 |

## eeg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1410)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.1132, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.3654, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.243 | 0.108 | 0.027 | 0.135 | 0.054 | 0.270 |
| 0.6-1.5 | 0.094 | 0.113 | 0.132 | 0.057 | 0.170 | 0.170 | 0.264 |
| 1.5-2.4 | 0.111 | 0.130 | 0.000 | 0.037 | 0.185 | 0.130 | 0.407 |
| 2.4-3.3 | 0.039 | 0.059 | 0.039 | 0.039 | 0.196 | 0.255 | 0.373 |
| 3.3-4.2 | 0.075 | 0.000 | 0.075 | 0.094 | 0.151 | 0.245 | 0.358 |
| 4.2-5.1 | 0.078 | 0.059 | 0.098 | 0.020 | 0.176 | 0.255 | 0.314 |
| 5.1-6.0 | 0.096 | 0.058 | 0.077 | 0.077 | 0.115 | 0.212 | 0.365 |

## eeg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2459)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.8125, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.643 | 0.071 | 0.000 | 0.000 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.812 | 0.000 | 0.000 | 0.000 | 0.000 | 0.188 |
| 1.5-2.4 | 0.000 | 0.688 | 0.062 | 0.000 | 0.000 | 0.000 | 0.250 |
| 2.4-3.3 | 0.000 | 0.824 | 0.000 | 0.000 | 0.000 | 0.000 | 0.176 |
| 3.3-4.2 | 0.000 | 0.706 | 0.118 | 0.000 | 0.059 | 0.000 | 0.118 |
| 4.2-5.1 | 0.111 | 0.556 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 |
| 5.1-6.0 | 0.056 | 0.278 | 0.000 | 0.000 | 0.000 | 0.056 | 0.611 |

## eeg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2425)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.5625, support=16
- `1.5-2.4`: recall=0.5625, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.357 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.000 | 0.562 | 0.375 | 0.000 | 0.000 | 0.000 | 0.062 |
| 1.5-2.4 | 0.062 | 0.125 | 0.562 | 0.000 | 0.000 | 0.062 | 0.188 |
| 2.4-3.3 | 0.000 | 0.353 | 0.471 | 0.059 | 0.000 | 0.000 | 0.118 |
| 3.3-4.2 | 0.118 | 0.294 | 0.294 | 0.000 | 0.000 | 0.000 | 0.294 |
| 4.2-5.1 | 0.000 | 0.333 | 0.500 | 0.111 | 0.000 | 0.000 | 0.056 |
| 5.1-6.0 | 0.000 | 0.167 | 0.278 | 0.167 | 0.000 | 0.056 | 0.333 |

## eeg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2392)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.5625, support=16
- `1.5-2.4`: recall=0.5625, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.429 | 0.071 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.062 | 0.562 | 0.375 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.125 | 0.000 | 0.562 | 0.125 | 0.000 | 0.000 | 0.188 |
| 2.4-3.3 | 0.059 | 0.471 | 0.353 | 0.000 | 0.000 | 0.000 | 0.118 |
| 3.3-4.2 | 0.176 | 0.235 | 0.353 | 0.000 | 0.000 | 0.059 | 0.176 |
| 4.2-5.1 | 0.056 | 0.056 | 0.500 | 0.167 | 0.000 | 0.000 | 0.222 |
| 5.1-6.0 | 0.000 | 0.111 | 0.389 | 0.056 | 0.056 | 0.056 | 0.333 |

## eeg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2334)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `0.6-1.5`: recall=0.3750, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.000 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.438 | 0.375 | 0.000 | 0.000 | 0.000 | 0.000 | 0.188 |
| 1.5-2.4 | 0.375 | 0.125 | 0.000 | 0.000 | 0.000 | 0.125 | 0.375 |
| 2.4-3.3 | 0.529 | 0.118 | 0.000 | 0.000 | 0.000 | 0.235 | 0.118 |
| 3.3-4.2 | 0.353 | 0.235 | 0.000 | 0.000 | 0.059 | 0.059 | 0.294 |
| 4.2-5.1 | 0.389 | 0.111 | 0.000 | 0.056 | 0.056 | 0.056 | 0.333 |
| 5.1-6.0 | 0.111 | 0.167 | 0.056 | 0.056 | 0.000 | 0.167 | 0.444 |

## eeg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.2313)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.571 | 0.000 | 0.000 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.125 | 0.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.125 |
| 1.5-2.4 | 0.062 | 0.625 | 0.000 | 0.000 | 0.000 | 0.000 | 0.312 |
| 2.4-3.3 | 0.353 | 0.412 | 0.000 | 0.000 | 0.000 | 0.059 | 0.176 |
| 3.3-4.2 | 0.176 | 0.706 | 0.000 | 0.000 | 0.000 | 0.059 | 0.059 |
| 4.2-5.1 | 0.056 | 0.556 | 0.000 | 0.000 | 0.056 | 0.111 | 0.222 |
| 5.1-6.0 | 0.056 | 0.278 | 0.000 | 0.000 | 0.000 | 0.222 | 0.444 |

## eeg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.2255)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.143 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.375 | 0.125 | 0.188 | 0.250 | 0.000 | 0.000 | 0.062 |
| 1.5-2.4 | 0.500 | 0.062 | 0.000 | 0.250 | 0.000 | 0.062 | 0.125 |
| 2.4-3.3 | 0.294 | 0.294 | 0.059 | 0.235 | 0.000 | 0.000 | 0.118 |
| 3.3-4.2 | 0.412 | 0.059 | 0.118 | 0.059 | 0.000 | 0.059 | 0.294 |
| 4.2-5.1 | 0.500 | 0.167 | 0.000 | 0.056 | 0.000 | 0.111 | 0.167 |
| 5.1-6.0 | 0.222 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.611 |

## eeg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1973)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.5000, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.071 | 0.000 | 0.000 | 0.071 | 0.071 |
| 0.6-1.5 | 0.188 | 0.500 | 0.062 | 0.125 | 0.000 | 0.125 | 0.000 |
| 1.5-2.4 | 0.500 | 0.312 | 0.000 | 0.062 | 0.062 | 0.062 | 0.000 |
| 2.4-3.3 | 0.176 | 0.647 | 0.118 | 0.000 | 0.059 | 0.000 | 0.000 |
| 3.3-4.2 | 0.235 | 0.412 | 0.059 | 0.000 | 0.000 | 0.294 | 0.000 |
| 4.2-5.1 | 0.278 | 0.333 | 0.222 | 0.000 | 0.000 | 0.111 | 0.056 |
| 5.1-6.0 | 0.111 | 0.167 | 0.111 | 0.056 | 0.000 | 0.278 | 0.278 |

## eeg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1620)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.5000, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.714 | 0.000 | 0.071 | 0.000 | 0.000 | 0.143 |
| 0.6-1.5 | 0.188 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.312 |
| 1.5-2.4 | 0.188 | 0.562 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 |
| 2.4-3.3 | 0.353 | 0.412 | 0.000 | 0.059 | 0.000 | 0.000 | 0.176 |
| 3.3-4.2 | 0.118 | 0.588 | 0.000 | 0.000 | 0.000 | 0.000 | 0.294 |
| 4.2-5.1 | 0.056 | 0.611 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 |
| 5.1-6.0 | 0.000 | 0.389 | 0.000 | 0.167 | 0.000 | 0.000 | 0.444 |

## eeg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.5556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.071 | 0.143 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.167 | 0.222 | 0.278 | 0.167 | 0.056 | 0.111 | 0.000 |
| 1.5-2.4 | 0.167 | 0.222 | 0.111 | 0.111 | 0.111 | 0.167 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.167 | 0.333 | 0.111 | 0.167 | 0.056 |
| 3.3-4.2 | 0.167 | 0.222 | 0.333 | 0.111 | 0.111 | 0.000 | 0.056 |
| 4.2-5.1 | 0.056 | 0.056 | 0.222 | 0.167 | 0.222 | 0.056 | 0.222 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.056 | 0.111 | 0.167 | 0.556 |

## eeg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.2429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.214 | 0.214 | 0.071 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.278 | 0.222 | 0.167 | 0.056 | 0.167 | 0.056 | 0.056 |
| 1.5-2.4 | 0.222 | 0.111 | 0.111 | 0.167 | 0.056 | 0.111 | 0.222 |
| 2.4-3.3 | 0.111 | 0.056 | 0.000 | 0.333 | 0.056 | 0.278 | 0.167 |
| 3.3-4.2 | 0.222 | 0.111 | 0.167 | 0.222 | 0.000 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.056 | 0.056 | 0.056 | 0.333 | 0.333 |
| 5.1-6.0 | 0.111 | 0.056 | 0.056 | 0.056 | 0.056 | 0.167 | 0.500 |

## eeg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.143 | 0.071 | 0.071 | 0.000 | 0.214 |
| 0.6-1.5 | 0.278 | 0.000 | 0.111 | 0.333 | 0.000 | 0.056 | 0.222 |
| 1.5-2.4 | 0.278 | 0.000 | 0.111 | 0.222 | 0.056 | 0.000 | 0.333 |
| 2.4-3.3 | 0.111 | 0.000 | 0.000 | 0.444 | 0.056 | 0.056 | 0.333 |
| 3.3-4.2 | 0.222 | 0.000 | 0.111 | 0.333 | 0.000 | 0.222 | 0.111 |
| 4.2-5.1 | 0.222 | 0.000 | 0.111 | 0.222 | 0.056 | 0.000 | 0.389 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.056 | 0.000 | 0.111 | 0.722 |

## eeg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.214 | 0.071 | 0.214 | 0.000 | 0.071 |
| 0.6-1.5 | 0.111 | 0.333 | 0.222 | 0.111 | 0.056 | 0.167 | 0.000 |
| 1.5-2.4 | 0.167 | 0.167 | 0.111 | 0.167 | 0.056 | 0.167 | 0.167 |
| 2.4-3.3 | 0.000 | 0.111 | 0.111 | 0.278 | 0.167 | 0.278 | 0.056 |
| 3.3-4.2 | 0.167 | 0.222 | 0.111 | 0.111 | 0.056 | 0.167 | 0.167 |
| 4.2-5.1 | 0.000 | 0.111 | 0.111 | 0.222 | 0.333 | 0.056 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.111 | 0.056 | 0.111 | 0.167 | 0.500 |

## eeg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.6111, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.071 | 0.214 | 0.000 | 0.143 | 0.214 |
| 0.6-1.5 | 0.444 | 0.111 | 0.000 | 0.167 | 0.000 | 0.111 | 0.167 |
| 1.5-2.4 | 0.278 | 0.056 | 0.000 | 0.389 | 0.000 | 0.222 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.000 | 0.611 | 0.056 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.000 | 0.056 | 0.444 | 0.000 | 0.222 | 0.167 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.444 | 0.000 | 0.222 | 0.222 |
| 5.1-6.0 | 0.167 | 0.000 | 0.000 | 0.500 | 0.056 | 0.111 | 0.167 |

## eeg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.5556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.071 | 0.143 | 0.071 | 0.286 | 0.000 |
| 0.6-1.5 | 0.111 | 0.222 | 0.167 | 0.167 | 0.167 | 0.111 | 0.056 |
| 1.5-2.4 | 0.111 | 0.000 | 0.056 | 0.444 | 0.278 | 0.111 | 0.000 |
| 2.4-3.3 | 0.000 | 0.056 | 0.000 | 0.556 | 0.222 | 0.167 | 0.000 |
| 3.3-4.2 | 0.056 | 0.056 | 0.167 | 0.389 | 0.167 | 0.167 | 0.000 |
| 4.2-5.1 | 0.056 | 0.000 | 0.000 | 0.444 | 0.222 | 0.222 | 0.056 |
| 5.1-6.0 | 0.056 | 0.056 | 0.000 | 0.167 | 0.333 | 0.333 | 0.056 |

## eeg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.5000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.143 | 0.071 | 0.143 | 0.071 | 0.143 |
| 0.6-1.5 | 0.333 | 0.000 | 0.222 | 0.000 | 0.167 | 0.222 | 0.056 |
| 1.5-2.4 | 0.278 | 0.056 | 0.000 | 0.389 | 0.056 | 0.056 | 0.167 |
| 2.4-3.3 | 0.056 | 0.000 | 0.056 | 0.500 | 0.056 | 0.167 | 0.167 |
| 3.3-4.2 | 0.167 | 0.167 | 0.000 | 0.278 | 0.111 | 0.222 | 0.056 |
| 4.2-5.1 | 0.056 | 0.056 | 0.111 | 0.333 | 0.056 | 0.222 | 0.167 |
| 5.1-6.0 | 0.167 | 0.000 | 0.111 | 0.167 | 0.111 | 0.278 | 0.167 |

## eeg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/eeg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.000 | 0.143 | 0.071 | 0.143 | 0.000 | 0.214 |
| 0.6-1.5 | 0.333 | 0.000 | 0.222 | 0.111 | 0.111 | 0.056 | 0.167 |
| 1.5-2.4 | 0.111 | 0.111 | 0.111 | 0.222 | 0.167 | 0.222 | 0.056 |
| 2.4-3.3 | 0.167 | 0.000 | 0.056 | 0.389 | 0.111 | 0.222 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.167 | 0.222 | 0.000 | 0.222 | 0.222 |
| 4.2-5.1 | 0.056 | 0.056 | 0.111 | 0.111 | 0.222 | 0.278 | 0.167 |
| 5.1-6.0 | 0.167 | 0.000 | 0.056 | 0.278 | 0.278 | 0.111 | 0.111 |

## fused | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1757)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0741, support=54
- `4.2-5.1`: recall=0.1321, support=53
- `5.1-6.0`: recall=0.5094, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.289 | 0.132 | 0.026 | 0.132 | 0.026 | 0.395 |
| 0.6-1.5 | 0.019 | 0.296 | 0.185 | 0.000 | 0.111 | 0.037 | 0.352 |
| 1.5-2.4 | 0.000 | 0.278 | 0.241 | 0.000 | 0.056 | 0.000 | 0.426 |
| 2.4-3.3 | 0.000 | 0.204 | 0.204 | 0.000 | 0.111 | 0.056 | 0.426 |
| 3.3-4.2 | 0.000 | 0.093 | 0.241 | 0.019 | 0.074 | 0.037 | 0.537 |
| 4.2-5.1 | 0.019 | 0.189 | 0.208 | 0.019 | 0.057 | 0.132 | 0.377 |
| 5.1-6.0 | 0.019 | 0.113 | 0.208 | 0.019 | 0.057 | 0.075 | 0.509 |

## fused | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1650)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `0.6-1.5`: recall=0.2037, support=54
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.1887, support=53
- `5.1-6.0`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.211 | 0.079 | 0.000 | 0.000 | 0.158 | 0.368 |
| 0.6-1.5 | 0.130 | 0.204 | 0.111 | 0.000 | 0.000 | 0.185 | 0.370 |
| 1.5-2.4 | 0.056 | 0.148 | 0.130 | 0.000 | 0.000 | 0.148 | 0.519 |
| 2.4-3.3 | 0.130 | 0.111 | 0.093 | 0.000 | 0.000 | 0.222 | 0.444 |
| 3.3-4.2 | 0.093 | 0.093 | 0.037 | 0.000 | 0.000 | 0.259 | 0.519 |
| 4.2-5.1 | 0.057 | 0.170 | 0.075 | 0.000 | 0.000 | 0.189 | 0.509 |
| 5.1-6.0 | 0.075 | 0.075 | 0.151 | 0.000 | 0.000 | 0.208 | 0.491 |

## fused | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1642)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `0.6-1.5`: recall=0.2222, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0741, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.8113, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.132 | 0.000 | 0.000 | 0.132 | 0.000 | 0.632 |
| 0.6-1.5 | 0.019 | 0.222 | 0.000 | 0.000 | 0.111 | 0.000 | 0.648 |
| 1.5-2.4 | 0.019 | 0.185 | 0.000 | 0.000 | 0.056 | 0.037 | 0.704 |
| 2.4-3.3 | 0.000 | 0.222 | 0.019 | 0.000 | 0.111 | 0.000 | 0.648 |
| 3.3-4.2 | 0.037 | 0.111 | 0.000 | 0.000 | 0.074 | 0.000 | 0.778 |
| 4.2-5.1 | 0.019 | 0.132 | 0.000 | 0.000 | 0.057 | 0.000 | 0.792 |
| 5.1-6.0 | 0.019 | 0.075 | 0.038 | 0.000 | 0.057 | 0.000 | 0.811 |

## fused | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1587)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `0.6-1.5`: recall=0.2407, support=54
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.1296, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.237 | 0.026 | 0.105 | 0.105 | 0.000 | 0.395 |
| 0.6-1.5 | 0.093 | 0.241 | 0.111 | 0.074 | 0.130 | 0.019 | 0.333 |
| 1.5-2.4 | 0.056 | 0.241 | 0.074 | 0.037 | 0.167 | 0.056 | 0.370 |
| 2.4-3.3 | 0.037 | 0.185 | 0.093 | 0.056 | 0.167 | 0.093 | 0.370 |
| 3.3-4.2 | 0.111 | 0.093 | 0.019 | 0.037 | 0.130 | 0.056 | 0.556 |
| 4.2-5.1 | 0.038 | 0.094 | 0.057 | 0.000 | 0.264 | 0.038 | 0.509 |
| 5.1-6.0 | 0.075 | 0.094 | 0.094 | 0.038 | 0.170 | 0.038 | 0.491 |

## fused | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1475)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.0370, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.8868, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.158 | 0.000 | 0.000 | 0.026 | 0.000 | 0.789 |
| 0.6-1.5 | 0.019 | 0.037 | 0.000 | 0.000 | 0.111 | 0.000 | 0.833 |
| 1.5-2.4 | 0.000 | 0.056 | 0.000 | 0.019 | 0.074 | 0.000 | 0.852 |
| 2.4-3.3 | 0.037 | 0.093 | 0.000 | 0.000 | 0.056 | 0.000 | 0.815 |
| 3.3-4.2 | 0.019 | 0.019 | 0.000 | 0.000 | 0.093 | 0.000 | 0.870 |
| 4.2-5.1 | 0.000 | 0.075 | 0.000 | 0.000 | 0.075 | 0.000 | 0.849 |
| 5.1-6.0 | 0.000 | 0.057 | 0.000 | 0.019 | 0.038 | 0.000 | 0.887 |

## fused | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1467)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.8868, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.105 | 0.026 | 0.000 | 0.000 | 0.026 | 0.789 |
| 0.6-1.5 | 0.019 | 0.019 | 0.056 | 0.000 | 0.056 | 0.019 | 0.833 |
| 1.5-2.4 | 0.074 | 0.019 | 0.019 | 0.000 | 0.000 | 0.019 | 0.870 |
| 2.4-3.3 | 0.019 | 0.093 | 0.019 | 0.000 | 0.037 | 0.019 | 0.815 |
| 3.3-4.2 | 0.037 | 0.037 | 0.056 | 0.000 | 0.000 | 0.000 | 0.870 |
| 4.2-5.1 | 0.019 | 0.019 | 0.038 | 0.000 | 0.019 | 0.057 | 0.849 |
| 5.1-6.0 | 0.038 | 0.038 | 0.019 | 0.000 | 0.019 | 0.000 | 0.887 |

## fused | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1757)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.071 | 0.000 | 0.000 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.111 | 0.333 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.278 | 0.056 | 0.167 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.294 | 0.176 | 0.059 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

## fused | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1474)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.071 | 0.000 | 0.000 | 0.071 | 0.500 |
| 0.6-1.5 | 0.000 | 0.389 | 0.000 | 0.056 | 0.000 | 0.056 | 0.500 |
| 1.5-2.4 | 0.111 | 0.333 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.111 | 0.111 | 0.278 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.176 | 0.059 | 0.294 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.333 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.611 |
| 5.1-6.0 | 0.389 | 0.056 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |

## fused | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1451)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.286 | 0.000 | 0.000 | 0.143 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.389 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.056 | 0.389 | 0.000 | 0.000 | 0.056 | 0.000 | 0.500 |
| 3.3-4.2 | 0.118 | 0.353 | 0.000 | 0.000 | 0.059 | 0.000 | 0.471 |
| 4.2-5.1 | 0.222 | 0.000 | 0.000 | 0.000 | 0.278 | 0.000 | 0.500 |
| 5.1-6.0 | 0.389 | 0.056 | 0.000 | 0.000 | 0.056 | 0.056 | 0.444 |

## fused | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.944 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## fused | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 1.5-2.4 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.944 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## fused | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1145)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.000 | 0.071 | 0.000 | 0.000 | 0.571 |
| 0.6-1.5 | 0.333 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.667 |
| 1.5-2.4 | 0.333 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.611 |
| 2.4-3.3 | 0.222 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.778 |
| 3.3-4.2 | 0.412 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.588 |
| 4.2-5.1 | 0.278 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.722 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.056 | 0.444 |

## fused | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.071 | 0.143 | 0.000 | 0.143 | 0.071 |
| 0.6-1.5 | 0.056 | 0.056 | 0.222 | 0.278 | 0.056 | 0.111 | 0.222 |
| 1.5-2.4 | 0.111 | 0.056 | 0.167 | 0.278 | 0.056 | 0.111 | 0.222 |
| 2.4-3.3 | 0.000 | 0.056 | 0.167 | 0.333 | 0.111 | 0.167 | 0.167 |
| 3.3-4.2 | 0.111 | 0.000 | 0.111 | 0.222 | 0.222 | 0.167 | 0.167 |
| 4.2-5.1 | 0.118 | 0.059 | 0.000 | 0.176 | 0.118 | 0.176 | 0.353 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.222 | 0.167 | 0.222 | 0.278 |

## fused | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.714 | 0.071 | 0.071 | 0.071 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.278 | 0.111 | 0.222 | 0.111 | 0.000 | 0.111 | 0.167 |
| 1.5-2.4 | 0.278 | 0.056 | 0.056 | 0.278 | 0.167 | 0.056 | 0.111 |
| 2.4-3.3 | 0.222 | 0.056 | 0.333 | 0.167 | 0.056 | 0.111 | 0.056 |
| 3.3-4.2 | 0.222 | 0.000 | 0.167 | 0.111 | 0.167 | 0.278 | 0.056 |
| 4.2-5.1 | 0.294 | 0.059 | 0.000 | 0.118 | 0.118 | 0.176 | 0.235 |
| 5.1-6.0 | 0.278 | 0.056 | 0.111 | 0.000 | 0.111 | 0.222 | 0.222 |

## fused | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.071 | 0.143 | 0.214 | 0.143 | 0.000 |
| 0.6-1.5 | 0.333 | 0.278 | 0.222 | 0.167 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.222 | 0.333 | 0.278 | 0.056 | 0.000 | 0.111 | 0.000 |
| 2.4-3.3 | 0.278 | 0.056 | 0.167 | 0.333 | 0.056 | 0.056 | 0.056 |
| 3.3-4.2 | 0.389 | 0.056 | 0.167 | 0.111 | 0.056 | 0.056 | 0.167 |
| 4.2-5.1 | 0.235 | 0.176 | 0.059 | 0.235 | 0.000 | 0.118 | 0.176 |
| 5.1-6.0 | 0.278 | 0.167 | 0.167 | 0.056 | 0.056 | 0.167 | 0.111 |

## fused | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.111 | 0.500 | 0.167 | 0.000 | 0.000 | 0.056 | 0.167 |
| 1.5-2.4 | 0.056 | 0.611 | 0.000 | 0.000 | 0.000 | 0.056 | 0.278 |
| 2.4-3.3 | 0.111 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.389 |
| 3.3-4.2 | 0.056 | 0.500 | 0.000 | 0.056 | 0.000 | 0.056 | 0.333 |
| 4.2-5.1 | 0.000 | 0.471 | 0.000 | 0.000 | 0.000 | 0.059 | 0.471 |
| 5.1-6.0 | 0.056 | 0.500 | 0.000 | 0.056 | 0.000 | 0.000 | 0.389 |

## fused | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.500 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.556 | 0.278 | 0.056 | 0.000 | 0.111 | 0.000 |
| 1.5-2.4 | 0.056 | 0.667 | 0.111 | 0.056 | 0.000 | 0.056 | 0.056 |
| 2.4-3.3 | 0.000 | 0.556 | 0.000 | 0.056 | 0.167 | 0.056 | 0.167 |
| 3.3-4.2 | 0.056 | 0.500 | 0.000 | 0.278 | 0.000 | 0.056 | 0.111 |
| 4.2-5.1 | 0.000 | 0.529 | 0.000 | 0.000 | 0.118 | 0.176 | 0.176 |
| 5.1-6.0 | 0.056 | 0.611 | 0.056 | 0.056 | 0.111 | 0.056 | 0.056 |

## fused | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.286 | 0.286 | 0.000 | 0.143 | 0.071 |
| 0.6-1.5 | 0.111 | 0.222 | 0.333 | 0.222 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.056 | 0.222 | 0.222 | 0.222 | 0.000 | 0.111 | 0.167 |
| 2.4-3.3 | 0.111 | 0.111 | 0.111 | 0.278 | 0.000 | 0.222 | 0.167 |
| 3.3-4.2 | 0.056 | 0.111 | 0.111 | 0.389 | 0.000 | 0.167 | 0.167 |
| 4.2-5.1 | 0.235 | 0.176 | 0.059 | 0.294 | 0.000 | 0.059 | 0.176 |
| 5.1-6.0 | 0.222 | 0.167 | 0.056 | 0.167 | 0.000 | 0.222 | 0.167 |

## fused | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.000 | 0.143 | 0.214 | 0.143 | 0.286 | 0.143 |
| 0.6-1.5 | 0.111 | 0.222 | 0.222 | 0.278 | 0.056 | 0.111 | 0.000 |
| 1.5-2.4 | 0.056 | 0.278 | 0.167 | 0.167 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.111 | 0.111 | 0.167 | 0.167 | 0.278 | 0.056 |
| 3.3-4.2 | 0.167 | 0.111 | 0.056 | 0.222 | 0.278 | 0.167 | 0.000 |
| 4.2-5.1 | 0.118 | 0.176 | 0.000 | 0.235 | 0.235 | 0.118 | 0.118 |
| 5.1-6.0 | 0.056 | 0.222 | 0.000 | 0.333 | 0.056 | 0.278 | 0.056 |

## fused | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/fused/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.071 | 0.071 | 0.000 | 0.500 | 0.143 | 0.071 |
| 0.6-1.5 | 0.167 | 0.111 | 0.389 | 0.000 | 0.167 | 0.111 | 0.056 |
| 1.5-2.4 | 0.111 | 0.222 | 0.333 | 0.000 | 0.222 | 0.111 | 0.000 |
| 2.4-3.3 | 0.333 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.278 | 0.111 | 0.222 | 0.000 | 0.278 | 0.056 | 0.056 |
| 4.2-5.1 | 0.294 | 0.059 | 0.118 | 0.000 | 0.353 | 0.000 | 0.176 |
| 5.1-6.0 | 0.333 | 0.222 | 0.056 | 0.000 | 0.278 | 0.111 | 0.000 |

## pupil | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1669)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.2778, support=54
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0741, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.211 | 0.132 | 0.026 | 0.132 | 0.000 | 0.474 |
| 0.6-1.5 | 0.000 | 0.278 | 0.148 | 0.000 | 0.111 | 0.000 | 0.463 |
| 1.5-2.4 | 0.000 | 0.259 | 0.222 | 0.000 | 0.056 | 0.000 | 0.463 |
| 2.4-3.3 | 0.019 | 0.185 | 0.204 | 0.000 | 0.111 | 0.019 | 0.463 |
| 3.3-4.2 | 0.019 | 0.093 | 0.204 | 0.000 | 0.074 | 0.074 | 0.537 |
| 4.2-5.1 | 0.019 | 0.132 | 0.226 | 0.000 | 0.057 | 0.038 | 0.528 |
| 5.1-6.0 | 0.019 | 0.170 | 0.132 | 0.038 | 0.057 | 0.038 | 0.547 |

## pupil | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1579)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2632, support=38
- `0.6-1.5`: recall=0.2222, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.263 | 0.132 | 0.079 | 0.000 | 0.079 | 0.053 | 0.395 |
| 0.6-1.5 | 0.185 | 0.222 | 0.074 | 0.056 | 0.037 | 0.019 | 0.407 |
| 1.5-2.4 | 0.111 | 0.167 | 0.093 | 0.019 | 0.111 | 0.037 | 0.463 |
| 2.4-3.3 | 0.167 | 0.148 | 0.056 | 0.019 | 0.111 | 0.056 | 0.444 |
| 3.3-4.2 | 0.241 | 0.056 | 0.056 | 0.019 | 0.019 | 0.037 | 0.574 |
| 4.2-5.1 | 0.094 | 0.094 | 0.075 | 0.038 | 0.151 | 0.000 | 0.547 |
| 5.1-6.0 | 0.057 | 0.113 | 0.132 | 0.019 | 0.113 | 0.019 | 0.547 |

## pupil | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1542)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1579, support=38
- `0.6-1.5`: recall=0.2222, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.1698, support=53
- `5.1-6.0`: recall=0.5283, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.158 | 0.289 | 0.026 | 0.000 | 0.053 | 0.132 | 0.342 |
| 0.6-1.5 | 0.167 | 0.222 | 0.111 | 0.000 | 0.000 | 0.093 | 0.407 |
| 1.5-2.4 | 0.093 | 0.259 | 0.019 | 0.000 | 0.000 | 0.204 | 0.426 |
| 2.4-3.3 | 0.148 | 0.167 | 0.074 | 0.000 | 0.056 | 0.093 | 0.463 |
| 3.3-4.2 | 0.093 | 0.130 | 0.000 | 0.056 | 0.019 | 0.130 | 0.574 |
| 4.2-5.1 | 0.057 | 0.132 | 0.113 | 0.000 | 0.000 | 0.170 | 0.528 |
| 5.1-6.0 | 0.057 | 0.113 | 0.151 | 0.019 | 0.019 | 0.113 | 0.528 |

## pupil | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1506)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.3519, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0370, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.105 | 0.395 | 0.000 | 0.000 | 0.026 | 0.421 |
| 0.6-1.5 | 0.037 | 0.019 | 0.333 | 0.000 | 0.093 | 0.019 | 0.500 |
| 1.5-2.4 | 0.037 | 0.019 | 0.352 | 0.000 | 0.019 | 0.037 | 0.537 |
| 2.4-3.3 | 0.056 | 0.093 | 0.333 | 0.000 | 0.019 | 0.019 | 0.481 |
| 3.3-4.2 | 0.074 | 0.019 | 0.315 | 0.000 | 0.037 | 0.000 | 0.556 |
| 4.2-5.1 | 0.000 | 0.019 | 0.396 | 0.000 | 0.019 | 0.057 | 0.509 |
| 5.1-6.0 | 0.019 | 0.057 | 0.340 | 0.019 | 0.000 | 0.019 | 0.547 |

## pupil | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1447)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `0.6-1.5`: recall=0.0741, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.7736, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.158 | 0.000 | 0.000 | 0.211 | 0.000 | 0.579 |
| 0.6-1.5 | 0.037 | 0.074 | 0.019 | 0.000 | 0.167 | 0.037 | 0.667 |
| 1.5-2.4 | 0.000 | 0.074 | 0.019 | 0.019 | 0.148 | 0.037 | 0.704 |
| 2.4-3.3 | 0.019 | 0.093 | 0.000 | 0.000 | 0.185 | 0.019 | 0.685 |
| 3.3-4.2 | 0.019 | 0.056 | 0.000 | 0.019 | 0.111 | 0.019 | 0.778 |
| 4.2-5.1 | 0.038 | 0.000 | 0.000 | 0.000 | 0.151 | 0.000 | 0.811 |
| 5.1-6.0 | 0.019 | 0.019 | 0.057 | 0.000 | 0.113 | 0.019 | 0.774 |

## pupil | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1437)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.8868, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.105 | 0.053 | 0.000 | 0.000 | 0.026 | 0.789 |
| 0.6-1.5 | 0.037 | 0.019 | 0.000 | 0.000 | 0.019 | 0.093 | 0.833 |
| 1.5-2.4 | 0.056 | 0.019 | 0.000 | 0.000 | 0.000 | 0.056 | 0.870 |
| 2.4-3.3 | 0.019 | 0.093 | 0.000 | 0.000 | 0.037 | 0.037 | 0.815 |
| 3.3-4.2 | 0.074 | 0.019 | 0.000 | 0.000 | 0.019 | 0.019 | 0.870 |
| 4.2-5.1 | 0.019 | 0.038 | 0.019 | 0.000 | 0.000 | 0.057 | 0.868 |
| 5.1-6.0 | 0.019 | 0.057 | 0.000 | 0.019 | 0.000 | 0.019 | 0.887 |

## pupil | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1576)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.214 | 0.000 | 0.071 | 0.000 | 0.429 |
| 0.6-1.5 | 0.000 | 0.389 | 0.167 | 0.000 | 0.000 | 0.000 | 0.444 |
| 1.5-2.4 | 0.111 | 0.333 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.222 | 0.056 | 0.222 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.294 | 0.000 | 0.235 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.444 | 0.111 | 0.000 | 0.000 | 0.000 | 0.000 | 0.444 |

## pupil | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1553)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.000 | 0.000 | 0.071 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.389 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.056 | 0.389 | 0.000 | 0.000 | 0.056 | 0.000 | 0.500 |
| 3.3-4.2 | 0.118 | 0.353 | 0.000 | 0.000 | 0.059 | 0.000 | 0.471 |
| 4.2-5.1 | 0.278 | 0.000 | 0.000 | 0.000 | 0.222 | 0.000 | 0.500 |
| 5.1-6.0 | 0.389 | 0.056 | 0.000 | 0.000 | 0.056 | 0.056 | 0.444 |

## pupil | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1474)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.143 | 0.000 | 0.000 | 0.000 | 0.571 |
| 0.6-1.5 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.333 | 0.000 | 0.056 | 0.056 | 0.000 | 0.500 |
| 2.4-3.3 | 0.222 | 0.111 | 0.167 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.294 | 0.059 | 0.176 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.444 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.556 |
| 5.1-6.0 | 0.444 | 0.056 | 0.056 | 0.000 | 0.000 | 0.000 | 0.444 |

## pupil | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 | 0.944 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## pupil | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1349)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.000 | 0.056 | 0.444 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.000 | 0.000 | 0.529 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |

## pupil | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1293)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.286 | 0.071 | 0.000 | 0.071 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.389 | 0.000 | 0.111 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.389 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.056 | 0.333 | 0.111 | 0.000 | 0.056 | 0.056 | 0.389 |
| 3.3-4.2 | 0.059 | 0.353 | 0.000 | 0.000 | 0.000 | 0.000 | 0.588 |
| 4.2-5.1 | 0.278 | 0.000 | 0.000 | 0.000 | 0.167 | 0.000 | 0.556 |
| 5.1-6.0 | 0.222 | 0.111 | 0.000 | 0.056 | 0.056 | 0.111 | 0.444 |

## pupil | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.4118, support=17
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.000 | 0.071 | 0.071 | 0.000 | 0.286 | 0.071 |
| 0.6-1.5 | 0.222 | 0.222 | 0.111 | 0.167 | 0.056 | 0.222 | 0.000 |
| 1.5-2.4 | 0.111 | 0.167 | 0.167 | 0.111 | 0.056 | 0.333 | 0.056 |
| 2.4-3.3 | 0.167 | 0.000 | 0.000 | 0.167 | 0.278 | 0.278 | 0.111 |
| 3.3-4.2 | 0.111 | 0.000 | 0.111 | 0.167 | 0.222 | 0.278 | 0.111 |
| 4.2-5.1 | 0.118 | 0.000 | 0.059 | 0.176 | 0.059 | 0.412 | 0.176 |
| 5.1-6.0 | 0.056 | 0.000 | 0.000 | 0.111 | 0.111 | 0.333 | 0.389 |

## pupil | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.143 | 0.071 | 0.000 | 0.000 | 0.214 |
| 0.6-1.5 | 0.167 | 0.111 | 0.167 | 0.222 | 0.111 | 0.056 | 0.167 |
| 1.5-2.4 | 0.167 | 0.167 | 0.278 | 0.056 | 0.000 | 0.056 | 0.278 |
| 2.4-3.3 | 0.222 | 0.000 | 0.056 | 0.278 | 0.167 | 0.000 | 0.278 |
| 3.3-4.2 | 0.222 | 0.056 | 0.056 | 0.278 | 0.167 | 0.000 | 0.222 |
| 4.2-5.1 | 0.353 | 0.118 | 0.059 | 0.118 | 0.000 | 0.118 | 0.235 |
| 5.1-6.0 | 0.167 | 0.000 | 0.000 | 0.167 | 0.167 | 0.000 | 0.500 |

## pupil | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.643 | 0.000 | 0.071 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.111 | 0.611 | 0.056 | 0.056 | 0.000 | 0.000 | 0.167 |
| 1.5-2.4 | 0.111 | 0.556 | 0.056 | 0.056 | 0.000 | 0.111 | 0.111 |
| 2.4-3.3 | 0.111 | 0.500 | 0.056 | 0.111 | 0.056 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.500 | 0.056 | 0.000 | 0.167 | 0.000 | 0.222 |
| 4.2-5.1 | 0.118 | 0.529 | 0.059 | 0.000 | 0.000 | 0.000 | 0.294 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.056 | 0.056 | 0.111 | 0.278 |

## pupil | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.071 | 0.286 | 0.071 | 0.214 | 0.071 |
| 0.6-1.5 | 0.056 | 0.222 | 0.222 | 0.167 | 0.056 | 0.111 | 0.167 |
| 1.5-2.4 | 0.056 | 0.222 | 0.278 | 0.222 | 0.000 | 0.111 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.278 | 0.000 | 0.278 | 0.167 |
| 3.3-4.2 | 0.000 | 0.056 | 0.111 | 0.500 | 0.056 | 0.167 | 0.111 |
| 4.2-5.1 | 0.176 | 0.176 | 0.059 | 0.294 | 0.000 | 0.059 | 0.235 |
| 5.1-6.0 | 0.167 | 0.222 | 0.056 | 0.167 | 0.000 | 0.222 | 0.167 |

## pupil | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.071 | 0.071 | 0.214 | 0.214 | 0.000 |
| 0.6-1.5 | 0.333 | 0.278 | 0.167 | 0.167 | 0.056 | 0.000 | 0.000 |
| 1.5-2.4 | 0.167 | 0.333 | 0.278 | 0.056 | 0.056 | 0.111 | 0.000 |
| 2.4-3.3 | 0.333 | 0.222 | 0.111 | 0.111 | 0.056 | 0.111 | 0.056 |
| 3.3-4.2 | 0.222 | 0.111 | 0.167 | 0.167 | 0.056 | 0.111 | 0.167 |
| 4.2-5.1 | 0.294 | 0.176 | 0.059 | 0.235 | 0.000 | 0.118 | 0.118 |
| 5.1-6.0 | 0.278 | 0.167 | 0.167 | 0.056 | 0.056 | 0.222 | 0.056 |

## pupil | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.571 | 0.000 | 0.143 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.111 | 0.500 | 0.167 | 0.056 | 0.000 | 0.000 | 0.167 |
| 1.5-2.4 | 0.111 | 0.556 | 0.056 | 0.056 | 0.000 | 0.111 | 0.111 |
| 2.4-3.3 | 0.167 | 0.500 | 0.000 | 0.056 | 0.000 | 0.000 | 0.278 |
| 3.3-4.2 | 0.111 | 0.500 | 0.000 | 0.111 | 0.056 | 0.056 | 0.167 |
| 4.2-5.1 | 0.118 | 0.529 | 0.000 | 0.000 | 0.000 | 0.000 | 0.353 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.111 | 0.000 | 0.056 | 0.333 |

## pupil | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.143 | 0.143 | 0.143 | 0.286 | 0.143 |
| 0.6-1.5 | 0.111 | 0.222 | 0.222 | 0.278 | 0.056 | 0.111 | 0.000 |
| 1.5-2.4 | 0.056 | 0.333 | 0.167 | 0.111 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.167 | 0.111 | 0.111 | 0.111 | 0.222 | 0.222 | 0.056 |
| 3.3-4.2 | 0.167 | 0.167 | 0.056 | 0.222 | 0.222 | 0.167 | 0.000 |
| 4.2-5.1 | 0.118 | 0.176 | 0.000 | 0.118 | 0.294 | 0.118 | 0.176 |
| 5.1-6.0 | 0.056 | 0.222 | 0.000 | 0.222 | 0.167 | 0.278 | 0.056 |

## pupil | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline_advanced_nn/pupil/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.071 | 0.071 | 0.000 | 0.500 | 0.143 | 0.071 |
| 0.6-1.5 | 0.167 | 0.111 | 0.389 | 0.000 | 0.167 | 0.111 | 0.056 |
| 1.5-2.4 | 0.111 | 0.222 | 0.333 | 0.056 | 0.167 | 0.111 | 0.000 |
| 2.4-3.3 | 0.333 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.278 | 0.111 | 0.222 | 0.000 | 0.278 | 0.056 | 0.056 |
| 4.2-5.1 | 0.294 | 0.059 | 0.176 | 0.000 | 0.353 | 0.000 | 0.118 |
| 5.1-6.0 | 0.333 | 0.222 | 0.056 | 0.000 | 0.278 | 0.111 | 0.000 |


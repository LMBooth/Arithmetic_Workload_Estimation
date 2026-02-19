# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_all_bins_baseline_advanced_nn.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1555)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0270, support=37
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.2353, support=51
- `3.3-4.2`: recall=0.0943, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.5000, support=52
- `6.0-6.9`: recall=0.1731, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.027 | 0.108 | 0.027 | 0.243 | 0.081 | 0.081 | 0.243 | 0.189 |
| 0.6-1.5 | 0.000 | 0.057 | 0.057 | 0.057 | 0.094 | 0.075 | 0.528 | 0.132 |
| 1.5-2.4 | 0.000 | 0.130 | 0.056 | 0.241 | 0.019 | 0.019 | 0.370 | 0.167 |
| 2.4-3.3 | 0.000 | 0.020 | 0.059 | 0.235 | 0.078 | 0.118 | 0.373 | 0.118 |
| 3.3-4.2 | 0.019 | 0.057 | 0.113 | 0.132 | 0.094 | 0.038 | 0.491 | 0.057 |
| 4.2-5.1 | 0.020 | 0.078 | 0.020 | 0.157 | 0.078 | 0.176 | 0.353 | 0.118 |
| 5.1-6.0 | 0.000 | 0.115 | 0.019 | 0.135 | 0.038 | 0.096 | 0.500 | 0.096 |
| 6.0-6.9 | 0.019 | 0.115 | 0.077 | 0.192 | 0.058 | 0.173 | 0.192 | 0.173 |

## ecg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1503)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `0.6-1.5`: recall=0.2453, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.1569, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.108 | 0.135 | 0.081 | 0.054 | 0.162 | 0.054 | 0.162 |
| 0.6-1.5 | 0.208 | 0.245 | 0.170 | 0.000 | 0.057 | 0.151 | 0.094 | 0.075 |
| 1.5-2.4 | 0.296 | 0.204 | 0.148 | 0.037 | 0.093 | 0.037 | 0.111 | 0.074 |
| 2.4-3.3 | 0.216 | 0.118 | 0.098 | 0.039 | 0.157 | 0.118 | 0.196 | 0.059 |
| 3.3-4.2 | 0.189 | 0.094 | 0.038 | 0.094 | 0.170 | 0.132 | 0.245 | 0.038 |
| 4.2-5.1 | 0.314 | 0.157 | 0.078 | 0.020 | 0.098 | 0.157 | 0.157 | 0.020 |
| 5.1-6.0 | 0.250 | 0.154 | 0.135 | 0.038 | 0.115 | 0.077 | 0.192 | 0.038 |
| 6.0-6.9 | 0.192 | 0.231 | 0.058 | 0.096 | 0.077 | 0.154 | 0.154 | 0.038 |

## ecg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1460)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.1132, support=53
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.2075, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.135 | 0.054 | 0.054 | 0.243 | 0.135 | 0.054 | 0.108 |
| 0.6-1.5 | 0.132 | 0.113 | 0.170 | 0.019 | 0.075 | 0.226 | 0.151 | 0.113 |
| 1.5-2.4 | 0.278 | 0.111 | 0.130 | 0.037 | 0.093 | 0.056 | 0.222 | 0.074 |
| 2.4-3.3 | 0.216 | 0.059 | 0.078 | 0.098 | 0.157 | 0.137 | 0.235 | 0.020 |
| 3.3-4.2 | 0.170 | 0.075 | 0.075 | 0.094 | 0.208 | 0.132 | 0.151 | 0.094 |
| 4.2-5.1 | 0.275 | 0.098 | 0.020 | 0.039 | 0.118 | 0.196 | 0.176 | 0.078 |
| 5.1-6.0 | 0.173 | 0.135 | 0.077 | 0.096 | 0.192 | 0.115 | 0.173 | 0.038 |
| 6.0-6.9 | 0.154 | 0.212 | 0.096 | 0.115 | 0.096 | 0.115 | 0.173 | 0.038 |

## ecg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1440)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.1569, support=51
- `5.1-6.0`: recall=0.2115, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.054 | 0.108 | 0.027 | 0.054 | 0.270 | 0.135 | 0.216 | 0.135 |
| 0.6-1.5 | 0.094 | 0.057 | 0.113 | 0.038 | 0.113 | 0.075 | 0.340 | 0.170 |
| 1.5-2.4 | 0.037 | 0.130 | 0.148 | 0.111 | 0.130 | 0.037 | 0.222 | 0.185 |
| 2.4-3.3 | 0.039 | 0.020 | 0.275 | 0.078 | 0.196 | 0.078 | 0.235 | 0.078 |
| 3.3-4.2 | 0.113 | 0.000 | 0.226 | 0.075 | 0.189 | 0.075 | 0.245 | 0.075 |
| 4.2-5.1 | 0.059 | 0.137 | 0.118 | 0.098 | 0.137 | 0.157 | 0.196 | 0.098 |
| 5.1-6.0 | 0.077 | 0.077 | 0.192 | 0.058 | 0.077 | 0.173 | 0.212 | 0.135 |
| 6.0-6.9 | 0.058 | 0.115 | 0.135 | 0.000 | 0.115 | 0.192 | 0.115 | 0.269 |

## ecg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1427)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0270, support=37
- `0.6-1.5`: recall=0.1132, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.027 | 0.216 | 0.027 | 0.243 | 0.162 | 0.000 | 0.135 | 0.189 |
| 0.6-1.5 | 0.057 | 0.113 | 0.075 | 0.094 | 0.245 | 0.057 | 0.226 | 0.132 |
| 1.5-2.4 | 0.074 | 0.185 | 0.093 | 0.167 | 0.148 | 0.000 | 0.148 | 0.185 |
| 2.4-3.3 | 0.059 | 0.137 | 0.137 | 0.216 | 0.157 | 0.039 | 0.235 | 0.020 |
| 3.3-4.2 | 0.019 | 0.057 | 0.208 | 0.189 | 0.151 | 0.038 | 0.302 | 0.038 |
| 4.2-5.1 | 0.020 | 0.137 | 0.098 | 0.216 | 0.137 | 0.059 | 0.176 | 0.157 |
| 5.1-6.0 | 0.038 | 0.212 | 0.058 | 0.096 | 0.173 | 0.058 | 0.192 | 0.173 |
| 6.0-6.9 | 0.058 | 0.096 | 0.135 | 0.135 | 0.115 | 0.058 | 0.115 | 0.288 |

## ecg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1330)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.0377, support=53
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.0755, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.0769, support=52
- `6.0-6.9`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.081 | 0.189 | 0.162 | 0.027 | 0.135 | 0.000 | 0.270 |
| 0.6-1.5 | 0.264 | 0.038 | 0.226 | 0.094 | 0.019 | 0.113 | 0.094 | 0.151 |
| 1.5-2.4 | 0.130 | 0.111 | 0.278 | 0.130 | 0.000 | 0.056 | 0.093 | 0.204 |
| 2.4-3.3 | 0.255 | 0.020 | 0.216 | 0.118 | 0.078 | 0.078 | 0.039 | 0.196 |
| 3.3-4.2 | 0.283 | 0.000 | 0.245 | 0.075 | 0.075 | 0.094 | 0.094 | 0.132 |
| 4.2-5.1 | 0.216 | 0.059 | 0.157 | 0.157 | 0.000 | 0.176 | 0.098 | 0.137 |
| 5.1-6.0 | 0.212 | 0.077 | 0.212 | 0.154 | 0.019 | 0.212 | 0.077 | 0.038 |
| 6.0-6.9 | 0.077 | 0.077 | 0.173 | 0.154 | 0.077 | 0.269 | 0.096 | 0.077 |

## ecg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1292)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.0755, support=53
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.0755, support=53
- `4.2-5.1`: recall=0.3725, support=51
- `5.1-6.0`: recall=0.0000, support=52
- `6.0-6.9`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.054 | 0.081 | 0.081 | 0.081 | 0.189 | 0.000 | 0.297 |
| 0.6-1.5 | 0.226 | 0.075 | 0.019 | 0.132 | 0.075 | 0.340 | 0.019 | 0.113 |
| 1.5-2.4 | 0.093 | 0.148 | 0.019 | 0.148 | 0.111 | 0.296 | 0.019 | 0.167 |
| 2.4-3.3 | 0.196 | 0.059 | 0.098 | 0.196 | 0.059 | 0.275 | 0.020 | 0.098 |
| 3.3-4.2 | 0.170 | 0.000 | 0.132 | 0.151 | 0.075 | 0.340 | 0.019 | 0.113 |
| 4.2-5.1 | 0.118 | 0.078 | 0.078 | 0.118 | 0.098 | 0.373 | 0.000 | 0.137 |
| 5.1-6.0 | 0.192 | 0.096 | 0.096 | 0.135 | 0.058 | 0.346 | 0.000 | 0.077 |
| 6.0-6.9 | 0.058 | 0.115 | 0.000 | 0.173 | 0.038 | 0.481 | 0.000 | 0.135 |

## ecg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1280)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.0000, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.2264, support=53
- `4.2-5.1`: recall=0.1373, support=51
- `5.1-6.0`: recall=0.1346, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.081 | 0.189 | 0.000 | 0.216 | 0.108 | 0.054 | 0.189 |
| 0.6-1.5 | 0.302 | 0.000 | 0.094 | 0.038 | 0.170 | 0.075 | 0.189 | 0.132 |
| 1.5-2.4 | 0.222 | 0.074 | 0.111 | 0.074 | 0.204 | 0.056 | 0.148 | 0.111 |
| 2.4-3.3 | 0.235 | 0.000 | 0.235 | 0.039 | 0.216 | 0.118 | 0.118 | 0.039 |
| 3.3-4.2 | 0.302 | 0.000 | 0.170 | 0.019 | 0.226 | 0.057 | 0.189 | 0.038 |
| 4.2-5.1 | 0.176 | 0.039 | 0.157 | 0.020 | 0.196 | 0.137 | 0.157 | 0.118 |
| 5.1-6.0 | 0.308 | 0.038 | 0.115 | 0.058 | 0.192 | 0.077 | 0.135 | 0.077 |
| 6.0-6.9 | 0.173 | 0.096 | 0.115 | 0.058 | 0.173 | 0.115 | 0.077 | 0.192 |

## ecg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1474)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.3529, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.071 | 0.143 | 0.000 | 0.143 | 0.143 | 0.214 |
| 0.6-1.5 | 0.125 | 0.000 | 0.188 | 0.125 | 0.125 | 0.062 | 0.125 | 0.250 |
| 1.5-2.4 | 0.062 | 0.188 | 0.125 | 0.312 | 0.000 | 0.125 | 0.125 | 0.062 |
| 2.4-3.3 | 0.059 | 0.000 | 0.059 | 0.353 | 0.059 | 0.235 | 0.118 | 0.118 |
| 3.3-4.2 | 0.118 | 0.000 | 0.118 | 0.176 | 0.000 | 0.176 | 0.118 | 0.294 |
| 4.2-5.1 | 0.000 | 0.000 | 0.056 | 0.222 | 0.111 | 0.444 | 0.056 | 0.111 |
| 5.1-6.0 | 0.111 | 0.111 | 0.111 | 0.056 | 0.167 | 0.222 | 0.111 | 0.111 |
| 6.0-6.9 | 0.056 | 0.167 | 0.222 | 0.333 | 0.056 | 0.111 | 0.056 | 0.000 |

## ecg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1327)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.000 | 0.143 | 0.214 | 0.000 | 0.000 | 0.357 | 0.143 |
| 0.6-1.5 | 0.250 | 0.000 | 0.125 | 0.000 | 0.312 | 0.000 | 0.312 | 0.000 |
| 1.5-2.4 | 0.375 | 0.000 | 0.188 | 0.062 | 0.000 | 0.000 | 0.375 | 0.000 |
| 2.4-3.3 | 0.294 | 0.000 | 0.059 | 0.294 | 0.000 | 0.000 | 0.353 | 0.000 |
| 3.3-4.2 | 0.118 | 0.000 | 0.176 | 0.176 | 0.118 | 0.000 | 0.176 | 0.235 |
| 4.2-5.1 | 0.167 | 0.000 | 0.000 | 0.111 | 0.056 | 0.000 | 0.333 | 0.333 |
| 5.1-6.0 | 0.222 | 0.000 | 0.056 | 0.222 | 0.167 | 0.000 | 0.222 | 0.111 |
| 6.0-6.9 | 0.278 | 0.000 | 0.056 | 0.111 | 0.111 | 0.000 | 0.333 | 0.111 |

## ecg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1259)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.571 | 0.286 | 0.000 | 0.000 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.000 | 0.875 | 0.062 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.688 | 0.312 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.588 | 0.235 | 0.000 | 0.000 | 0.000 | 0.176 |
| 3.3-4.2 | 0.000 | 0.000 | 0.471 | 0.294 | 0.000 | 0.000 | 0.000 | 0.235 |
| 4.2-5.1 | 0.000 | 0.000 | 0.278 | 0.167 | 0.000 | 0.000 | 0.056 | 0.500 |
| 5.1-6.0 | 0.000 | 0.000 | 0.389 | 0.389 | 0.000 | 0.000 | 0.000 | 0.222 |
| 6.0-6.9 | 0.000 | 0.000 | 0.556 | 0.222 | 0.000 | 0.000 | 0.167 | 0.056 |

## ecg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1257)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.286 | 0.000 | 0.357 | 0.000 | 0.000 | 0.143 | 0.143 |
| 0.6-1.5 | 0.188 | 0.125 | 0.000 | 0.438 | 0.062 | 0.000 | 0.188 | 0.000 |
| 1.5-2.4 | 0.000 | 0.375 | 0.000 | 0.500 | 0.000 | 0.000 | 0.125 | 0.000 |
| 2.4-3.3 | 0.118 | 0.235 | 0.000 | 0.471 | 0.059 | 0.059 | 0.000 | 0.059 |
| 3.3-4.2 | 0.118 | 0.118 | 0.000 | 0.294 | 0.118 | 0.000 | 0.118 | 0.235 |
| 4.2-5.1 | 0.056 | 0.167 | 0.000 | 0.333 | 0.111 | 0.000 | 0.056 | 0.278 |
| 5.1-6.0 | 0.056 | 0.000 | 0.000 | 0.444 | 0.167 | 0.000 | 0.222 | 0.111 |
| 6.0-6.9 | 0.056 | 0.056 | 0.000 | 0.333 | 0.056 | 0.056 | 0.444 | 0.000 |

## ecg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1189)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.000 | 0.071 | 0.071 | 0.000 | 0.143 | 0.143 |
| 0.6-1.5 | 0.688 | 0.000 | 0.000 | 0.000 | 0.125 | 0.000 | 0.188 | 0.000 |
| 1.5-2.4 | 0.625 | 0.000 | 0.062 | 0.000 | 0.062 | 0.000 | 0.250 | 0.000 |
| 2.4-3.3 | 0.588 | 0.000 | 0.000 | 0.176 | 0.000 | 0.059 | 0.176 | 0.000 |
| 3.3-4.2 | 0.529 | 0.000 | 0.000 | 0.000 | 0.118 | 0.000 | 0.118 | 0.235 |
| 4.2-5.1 | 0.278 | 0.000 | 0.000 | 0.278 | 0.000 | 0.000 | 0.167 | 0.278 |
| 5.1-6.0 | 0.611 | 0.000 | 0.000 | 0.111 | 0.111 | 0.000 | 0.056 | 0.111 |
| 6.0-6.9 | 0.556 | 0.000 | 0.056 | 0.000 | 0.111 | 0.056 | 0.167 | 0.056 |

## ecg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1177)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.3529, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.071 | 0.214 | 0.000 | 0.143 | 0.214 | 0.214 |
| 0.6-1.5 | 0.062 | 0.062 | 0.312 | 0.000 | 0.062 | 0.062 | 0.188 | 0.250 |
| 1.5-2.4 | 0.188 | 0.062 | 0.062 | 0.312 | 0.000 | 0.062 | 0.250 | 0.062 |
| 2.4-3.3 | 0.059 | 0.059 | 0.059 | 0.353 | 0.059 | 0.118 | 0.118 | 0.176 |
| 3.3-4.2 | 0.176 | 0.000 | 0.118 | 0.235 | 0.000 | 0.118 | 0.000 | 0.353 |
| 4.2-5.1 | 0.111 | 0.000 | 0.056 | 0.333 | 0.000 | 0.111 | 0.111 | 0.278 |
| 5.1-6.0 | 0.056 | 0.222 | 0.056 | 0.167 | 0.000 | 0.111 | 0.222 | 0.167 |
| 6.0-6.9 | 0.222 | 0.056 | 0.222 | 0.167 | 0.000 | 0.111 | 0.167 | 0.056 |

## ecg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.0978)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.000 | 0.143 | 0.000 | 0.000 | 0.500 | 0.000 |
| 0.6-1.5 | 0.562 | 0.062 | 0.000 | 0.000 | 0.062 | 0.000 | 0.312 | 0.000 |
| 1.5-2.4 | 0.500 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.000 |
| 2.4-3.3 | 0.529 | 0.059 | 0.000 | 0.059 | 0.059 | 0.000 | 0.294 | 0.000 |
| 3.3-4.2 | 0.471 | 0.118 | 0.000 | 0.000 | 0.118 | 0.000 | 0.294 | 0.000 |
| 4.2-5.1 | 0.222 | 0.056 | 0.000 | 0.000 | 0.111 | 0.000 | 0.500 | 0.111 |
| 5.1-6.0 | 0.389 | 0.056 | 0.000 | 0.000 | 0.222 | 0.056 | 0.167 | 0.111 |
| 6.0-6.9 | 0.444 | 0.000 | 0.000 | 0.000 | 0.056 | 0.111 | 0.389 | 0.000 |

## ecg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.0843)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.000 | 0.214 | 0.500 | 0.000 | 0.000 | 0.000 | 0.214 |
| 0.6-1.5 | 0.125 | 0.062 | 0.250 | 0.250 | 0.250 | 0.000 | 0.000 | 0.062 |
| 1.5-2.4 | 0.062 | 0.188 | 0.125 | 0.375 | 0.000 | 0.062 | 0.000 | 0.188 |
| 2.4-3.3 | 0.059 | 0.294 | 0.176 | 0.176 | 0.000 | 0.059 | 0.000 | 0.235 |
| 3.3-4.2 | 0.176 | 0.059 | 0.059 | 0.353 | 0.059 | 0.235 | 0.000 | 0.059 |
| 4.2-5.1 | 0.167 | 0.000 | 0.000 | 0.222 | 0.000 | 0.111 | 0.000 | 0.500 |
| 5.1-6.0 | 0.278 | 0.000 | 0.000 | 0.278 | 0.167 | 0.000 | 0.000 | 0.278 |
| 6.0-6.9 | 0.111 | 0.056 | 0.056 | 0.333 | 0.111 | 0.278 | 0.000 | 0.056 |

## ecg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.000 | 0.286 | 0.214 | 0.071 | 0.143 | 0.071 | 0.143 |
| 0.6-1.5 | 0.056 | 0.056 | 0.167 | 0.167 | 0.056 | 0.000 | 0.111 | 0.389 |
| 1.5-2.4 | 0.056 | 0.000 | 0.111 | 0.222 | 0.000 | 0.056 | 0.111 | 0.444 |
| 2.4-3.3 | 0.056 | 0.000 | 0.167 | 0.389 | 0.000 | 0.111 | 0.000 | 0.278 |
| 3.3-4.2 | 0.111 | 0.000 | 0.111 | 0.111 | 0.000 | 0.222 | 0.000 | 0.444 |
| 4.2-5.1 | 0.056 | 0.000 | 0.167 | 0.056 | 0.000 | 0.333 | 0.000 | 0.389 |
| 5.1-6.0 | 0.056 | 0.000 | 0.222 | 0.056 | 0.000 | 0.111 | 0.222 | 0.333 |
| 6.0-6.9 | 0.111 | 0.000 | 0.278 | 0.056 | 0.056 | 0.056 | 0.056 | 0.389 |

## ecg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.000 | 0.071 | 0.357 | 0.143 | 0.000 |
| 0.6-1.5 | 0.056 | 0.222 | 0.000 | 0.111 | 0.167 | 0.000 | 0.222 | 0.222 |
| 1.5-2.4 | 0.167 | 0.167 | 0.111 | 0.111 | 0.056 | 0.000 | 0.167 | 0.222 |
| 2.4-3.3 | 0.111 | 0.167 | 0.056 | 0.278 | 0.111 | 0.056 | 0.111 | 0.111 |
| 3.3-4.2 | 0.056 | 0.167 | 0.056 | 0.111 | 0.167 | 0.167 | 0.111 | 0.167 |
| 4.2-5.1 | 0.111 | 0.000 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.056 |
| 5.1-6.0 | 0.056 | 0.167 | 0.000 | 0.167 | 0.167 | 0.167 | 0.278 | 0.000 |
| 6.0-6.9 | 0.000 | 0.278 | 0.167 | 0.167 | 0.111 | 0.111 | 0.000 | 0.167 |

## ecg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.1812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.000 | 0.000 | 0.357 | 0.071 | 0.071 |
| 0.6-1.5 | 0.111 | 0.167 | 0.000 | 0.167 | 0.167 | 0.000 | 0.167 | 0.222 |
| 1.5-2.4 | 0.278 | 0.167 | 0.056 | 0.167 | 0.000 | 0.056 | 0.167 | 0.111 |
| 2.4-3.3 | 0.111 | 0.167 | 0.167 | 0.111 | 0.167 | 0.167 | 0.056 | 0.056 |
| 3.3-4.2 | 0.056 | 0.111 | 0.167 | 0.000 | 0.167 | 0.167 | 0.111 | 0.222 |
| 4.2-5.1 | 0.056 | 0.000 | 0.167 | 0.222 | 0.111 | 0.222 | 0.111 | 0.111 |
| 5.1-6.0 | 0.000 | 0.167 | 0.111 | 0.111 | 0.111 | 0.167 | 0.333 | 0.000 |
| 6.0-6.9 | 0.000 | 0.222 | 0.278 | 0.111 | 0.056 | 0.111 | 0.000 | 0.222 |

## ecg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.143 | 0.357 | 0.000 | 0.143 | 0.000 | 0.143 |
| 0.6-1.5 | 0.222 | 0.111 | 0.167 | 0.111 | 0.056 | 0.056 | 0.111 | 0.167 |
| 1.5-2.4 | 0.278 | 0.056 | 0.056 | 0.167 | 0.111 | 0.111 | 0.000 | 0.222 |
| 2.4-3.3 | 0.222 | 0.111 | 0.000 | 0.278 | 0.056 | 0.167 | 0.000 | 0.167 |
| 3.3-4.2 | 0.111 | 0.111 | 0.056 | 0.222 | 0.000 | 0.222 | 0.056 | 0.222 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.167 | 0.111 | 0.500 | 0.000 | 0.222 |
| 5.1-6.0 | 0.111 | 0.056 | 0.056 | 0.278 | 0.000 | 0.278 | 0.000 | 0.222 |
| 6.0-6.9 | 0.000 | 0.111 | 0.111 | 0.389 | 0.056 | 0.056 | 0.000 | 0.278 |

## ecg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1688)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.143 | 0.000 | 0.214 | 0.000 | 0.214 |
| 0.6-1.5 | 0.000 | 0.222 | 0.222 | 0.278 | 0.111 | 0.000 | 0.056 | 0.111 |
| 1.5-2.4 | 0.111 | 0.056 | 0.111 | 0.333 | 0.000 | 0.111 | 0.111 | 0.167 |
| 2.4-3.3 | 0.056 | 0.167 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.111 | 0.056 | 0.278 | 0.000 | 0.222 | 0.056 | 0.167 |
| 4.2-5.1 | 0.111 | 0.056 | 0.000 | 0.167 | 0.000 | 0.444 | 0.111 | 0.111 |
| 5.1-6.0 | 0.056 | 0.167 | 0.167 | 0.333 | 0.000 | 0.222 | 0.000 | 0.056 |
| 6.0-6.9 | 0.111 | 0.056 | 0.222 | 0.111 | 0.111 | 0.111 | 0.056 | 0.222 |

## ecg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.143 | 0.214 | 0.071 | 0.143 | 0.071 | 0.071 |
| 0.6-1.5 | 0.167 | 0.333 | 0.056 | 0.056 | 0.056 | 0.056 | 0.111 | 0.167 |
| 1.5-2.4 | 0.111 | 0.111 | 0.056 | 0.222 | 0.000 | 0.056 | 0.222 | 0.222 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.167 | 0.111 | 0.222 | 0.111 | 0.111 |
| 3.3-4.2 | 0.278 | 0.278 | 0.000 | 0.000 | 0.000 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.000 | 0.056 | 0.111 | 0.111 | 0.000 | 0.444 | 0.111 | 0.167 |
| 5.1-6.0 | 0.056 | 0.278 | 0.056 | 0.056 | 0.111 | 0.278 | 0.111 | 0.056 |
| 6.0-6.9 | 0.111 | 0.056 | 0.333 | 0.111 | 0.111 | 0.056 | 0.167 | 0.056 |

## ecg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.286 | 0.143 | 0.000 | 0.214 | 0.000 | 0.143 |
| 0.6-1.5 | 0.333 | 0.111 | 0.333 | 0.167 | 0.000 | 0.000 | 0.000 | 0.056 |
| 1.5-2.4 | 0.278 | 0.000 | 0.111 | 0.167 | 0.000 | 0.056 | 0.111 | 0.278 |
| 2.4-3.3 | 0.389 | 0.000 | 0.167 | 0.111 | 0.056 | 0.111 | 0.000 | 0.167 |
| 3.3-4.2 | 0.167 | 0.111 | 0.222 | 0.111 | 0.000 | 0.167 | 0.167 | 0.056 |
| 4.2-5.1 | 0.111 | 0.000 | 0.222 | 0.111 | 0.056 | 0.333 | 0.056 | 0.111 |
| 5.1-6.0 | 0.167 | 0.111 | 0.278 | 0.167 | 0.111 | 0.056 | 0.000 | 0.111 |
| 6.0-6.9 | 0.111 | 0.056 | 0.222 | 0.167 | 0.000 | 0.111 | 0.056 | 0.278 |

## ecg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1437)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/ecg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.071 | 0.000 | 0.000 | 0.071 | 0.143 | 0.143 |
| 0.6-1.5 | 0.444 | 0.056 | 0.111 | 0.056 | 0.000 | 0.000 | 0.222 | 0.111 |
| 1.5-2.4 | 0.500 | 0.056 | 0.056 | 0.111 | 0.056 | 0.056 | 0.111 | 0.056 |
| 2.4-3.3 | 0.444 | 0.000 | 0.000 | 0.111 | 0.111 | 0.111 | 0.111 | 0.111 |
| 3.3-4.2 | 0.389 | 0.056 | 0.056 | 0.000 | 0.000 | 0.111 | 0.278 | 0.111 |
| 4.2-5.1 | 0.444 | 0.056 | 0.000 | 0.000 | 0.056 | 0.167 | 0.111 | 0.167 |
| 5.1-6.0 | 0.333 | 0.056 | 0.000 | 0.000 | 0.056 | 0.111 | 0.278 | 0.167 |
| 6.0-6.9 | 0.389 | 0.111 | 0.111 | 0.000 | 0.056 | 0.056 | 0.111 | 0.167 |

## eeg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1611)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.1321, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.1132, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.054 | 0.027 | 0.189 | 0.027 | 0.000 | 0.189 | 0.243 |
| 0.6-1.5 | 0.189 | 0.132 | 0.000 | 0.189 | 0.132 | 0.000 | 0.113 | 0.245 |
| 1.5-2.4 | 0.222 | 0.037 | 0.074 | 0.167 | 0.093 | 0.037 | 0.130 | 0.241 |
| 2.4-3.3 | 0.098 | 0.039 | 0.059 | 0.157 | 0.078 | 0.059 | 0.216 | 0.294 |
| 3.3-4.2 | 0.075 | 0.057 | 0.000 | 0.113 | 0.113 | 0.094 | 0.264 | 0.283 |
| 4.2-5.1 | 0.059 | 0.078 | 0.000 | 0.196 | 0.137 | 0.039 | 0.235 | 0.255 |
| 5.1-6.0 | 0.115 | 0.038 | 0.019 | 0.096 | 0.154 | 0.058 | 0.154 | 0.365 |
| 6.0-6.9 | 0.173 | 0.058 | 0.019 | 0.135 | 0.096 | 0.000 | 0.212 | 0.308 |

## eeg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1482)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `0.6-1.5`: recall=0.1132, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.027 | 0.027 | 0.081 | 0.135 | 0.000 | 0.216 | 0.270 |
| 0.6-1.5 | 0.340 | 0.113 | 0.019 | 0.038 | 0.170 | 0.019 | 0.151 | 0.151 |
| 1.5-2.4 | 0.315 | 0.037 | 0.037 | 0.019 | 0.167 | 0.093 | 0.130 | 0.204 |
| 2.4-3.3 | 0.216 | 0.039 | 0.039 | 0.020 | 0.235 | 0.039 | 0.216 | 0.196 |
| 3.3-4.2 | 0.226 | 0.019 | 0.000 | 0.019 | 0.189 | 0.094 | 0.283 | 0.170 |
| 4.2-5.1 | 0.216 | 0.039 | 0.000 | 0.039 | 0.255 | 0.059 | 0.196 | 0.196 |
| 5.1-6.0 | 0.173 | 0.058 | 0.000 | 0.058 | 0.154 | 0.077 | 0.192 | 0.288 |
| 6.0-6.9 | 0.269 | 0.058 | 0.038 | 0.058 | 0.096 | 0.019 | 0.192 | 0.269 |

## eeg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1455)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.3846, support=52
- `6.0-6.9`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.027 | 0.081 | 0.135 | 0.162 | 0.027 | 0.243 | 0.162 |
| 0.6-1.5 | 0.151 | 0.057 | 0.094 | 0.113 | 0.208 | 0.189 | 0.132 | 0.057 |
| 1.5-2.4 | 0.037 | 0.074 | 0.093 | 0.056 | 0.241 | 0.093 | 0.241 | 0.167 |
| 2.4-3.3 | 0.098 | 0.039 | 0.098 | 0.039 | 0.255 | 0.157 | 0.235 | 0.078 |
| 3.3-4.2 | 0.094 | 0.038 | 0.075 | 0.057 | 0.264 | 0.075 | 0.340 | 0.057 |
| 4.2-5.1 | 0.098 | 0.039 | 0.059 | 0.098 | 0.216 | 0.098 | 0.333 | 0.059 |
| 5.1-6.0 | 0.038 | 0.038 | 0.115 | 0.096 | 0.212 | 0.058 | 0.385 | 0.058 |
| 6.0-6.9 | 0.250 | 0.058 | 0.038 | 0.058 | 0.231 | 0.135 | 0.135 | 0.096 |

## eeg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1454)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.2453, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.0189, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.5000, support=52
- `6.0-6.9`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.189 | 0.027 | 0.081 | 0.000 | 0.135 | 0.378 | 0.054 |
| 0.6-1.5 | 0.075 | 0.245 | 0.019 | 0.075 | 0.019 | 0.057 | 0.453 | 0.057 |
| 1.5-2.4 | 0.130 | 0.259 | 0.000 | 0.019 | 0.056 | 0.111 | 0.407 | 0.019 |
| 2.4-3.3 | 0.137 | 0.196 | 0.000 | 0.098 | 0.000 | 0.157 | 0.392 | 0.020 |
| 3.3-4.2 | 0.057 | 0.226 | 0.057 | 0.075 | 0.019 | 0.113 | 0.434 | 0.019 |
| 4.2-5.1 | 0.118 | 0.137 | 0.078 | 0.000 | 0.000 | 0.118 | 0.471 | 0.078 |
| 5.1-6.0 | 0.115 | 0.135 | 0.058 | 0.000 | 0.000 | 0.135 | 0.500 | 0.058 |
| 6.0-6.9 | 0.192 | 0.096 | 0.038 | 0.058 | 0.019 | 0.096 | 0.404 | 0.096 |

## eeg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1394)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3784, support=37
- `0.6-1.5`: recall=0.0189, support=53
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.3208, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.2500, support=52
- `6.0-6.9`: recall=0.0192, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.378 | 0.054 | 0.054 | 0.000 | 0.243 | 0.000 | 0.216 | 0.054 |
| 0.6-1.5 | 0.302 | 0.019 | 0.000 | 0.057 | 0.226 | 0.057 | 0.283 | 0.057 |
| 1.5-2.4 | 0.259 | 0.037 | 0.019 | 0.019 | 0.296 | 0.074 | 0.241 | 0.056 |
| 2.4-3.3 | 0.216 | 0.039 | 0.020 | 0.020 | 0.333 | 0.098 | 0.235 | 0.039 |
| 3.3-4.2 | 0.226 | 0.019 | 0.000 | 0.057 | 0.321 | 0.019 | 0.302 | 0.057 |
| 4.2-5.1 | 0.294 | 0.059 | 0.000 | 0.020 | 0.294 | 0.059 | 0.176 | 0.098 |
| 5.1-6.0 | 0.250 | 0.038 | 0.038 | 0.077 | 0.212 | 0.077 | 0.250 | 0.058 |
| 6.0-6.9 | 0.346 | 0.000 | 0.038 | 0.019 | 0.288 | 0.038 | 0.250 | 0.019 |

## eeg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1388)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.0189, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.4423, support=52
- `6.0-6.9`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.216 | 0.000 | 0.135 | 0.027 | 0.135 | 0.324 | 0.000 |
| 0.6-1.5 | 0.075 | 0.189 | 0.019 | 0.208 | 0.094 | 0.075 | 0.302 | 0.038 |
| 1.5-2.4 | 0.148 | 0.241 | 0.019 | 0.185 | 0.000 | 0.000 | 0.352 | 0.056 |
| 2.4-3.3 | 0.196 | 0.118 | 0.039 | 0.098 | 0.020 | 0.118 | 0.353 | 0.059 |
| 3.3-4.2 | 0.113 | 0.151 | 0.000 | 0.170 | 0.019 | 0.094 | 0.340 | 0.113 |
| 4.2-5.1 | 0.118 | 0.157 | 0.000 | 0.098 | 0.039 | 0.059 | 0.471 | 0.059 |
| 5.1-6.0 | 0.135 | 0.135 | 0.000 | 0.096 | 0.000 | 0.115 | 0.442 | 0.077 |
| 6.0-6.9 | 0.192 | 0.135 | 0.058 | 0.058 | 0.000 | 0.154 | 0.308 | 0.096 |

## eeg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1364)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.1698, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.4615, support=52
- `6.0-6.9`: recall=0.0000, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.162 | 0.000 | 0.189 | 0.027 | 0.189 | 0.216 | 0.000 |
| 0.6-1.5 | 0.264 | 0.170 | 0.019 | 0.057 | 0.000 | 0.151 | 0.340 | 0.000 |
| 1.5-2.4 | 0.222 | 0.204 | 0.000 | 0.056 | 0.019 | 0.111 | 0.389 | 0.000 |
| 2.4-3.3 | 0.275 | 0.137 | 0.000 | 0.039 | 0.000 | 0.157 | 0.392 | 0.000 |
| 3.3-4.2 | 0.302 | 0.132 | 0.000 | 0.075 | 0.038 | 0.113 | 0.340 | 0.000 |
| 4.2-5.1 | 0.235 | 0.078 | 0.000 | 0.020 | 0.000 | 0.176 | 0.471 | 0.020 |
| 5.1-6.0 | 0.231 | 0.135 | 0.038 | 0.000 | 0.000 | 0.115 | 0.462 | 0.019 |
| 6.0-6.9 | 0.308 | 0.135 | 0.000 | 0.038 | 0.000 | 0.212 | 0.308 | 0.000 |

## eeg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1288)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.0189, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.2500, support=52
- `6.0-6.9`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.351 | 0.000 | 0.108 | 0.000 | 0.108 | 0.189 | 0.000 |
| 0.6-1.5 | 0.302 | 0.226 | 0.038 | 0.094 | 0.000 | 0.170 | 0.132 | 0.038 |
| 1.5-2.4 | 0.259 | 0.241 | 0.019 | 0.111 | 0.019 | 0.074 | 0.204 | 0.074 |
| 2.4-3.3 | 0.235 | 0.137 | 0.000 | 0.137 | 0.000 | 0.118 | 0.294 | 0.078 |
| 3.3-4.2 | 0.189 | 0.170 | 0.000 | 0.189 | 0.019 | 0.132 | 0.264 | 0.038 |
| 4.2-5.1 | 0.275 | 0.059 | 0.020 | 0.059 | 0.000 | 0.098 | 0.392 | 0.098 |
| 5.1-6.0 | 0.231 | 0.115 | 0.019 | 0.135 | 0.000 | 0.173 | 0.250 | 0.077 |
| 6.0-6.9 | 0.231 | 0.173 | 0.000 | 0.173 | 0.000 | 0.135 | 0.231 | 0.058 |

## eeg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.2411)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.4375, support=16
- `1.5-2.4`: recall=0.5625, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.429 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.438 | 0.500 | 0.000 | 0.000 | 0.000 | 0.062 | 0.000 |
| 1.5-2.4 | 0.062 | 0.000 | 0.562 | 0.062 | 0.062 | 0.000 | 0.062 | 0.188 |
| 2.4-3.3 | 0.000 | 0.118 | 0.706 | 0.000 | 0.000 | 0.000 | 0.059 | 0.118 |
| 3.3-4.2 | 0.118 | 0.059 | 0.353 | 0.000 | 0.000 | 0.000 | 0.176 | 0.294 |
| 4.2-5.1 | 0.000 | 0.111 | 0.500 | 0.000 | 0.056 | 0.000 | 0.167 | 0.167 |
| 5.1-6.0 | 0.056 | 0.056 | 0.111 | 0.056 | 0.167 | 0.111 | 0.333 | 0.111 |
| 6.0-6.9 | 0.000 | 0.111 | 0.333 | 0.056 | 0.167 | 0.000 | 0.167 | 0.167 |

## eeg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2003)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.4375, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.357 | 0.071 | 0.000 | 0.071 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.250 | 0.438 | 0.062 | 0.000 | 0.062 | 0.062 | 0.062 | 0.062 |
| 1.5-2.4 | 0.062 | 0.375 | 0.125 | 0.000 | 0.062 | 0.000 | 0.312 | 0.062 |
| 2.4-3.3 | 0.294 | 0.235 | 0.118 | 0.000 | 0.000 | 0.059 | 0.235 | 0.059 |
| 3.3-4.2 | 0.059 | 0.353 | 0.176 | 0.000 | 0.059 | 0.176 | 0.118 | 0.059 |
| 4.2-5.1 | 0.111 | 0.278 | 0.056 | 0.000 | 0.056 | 0.111 | 0.333 | 0.056 |
| 5.1-6.0 | 0.111 | 0.111 | 0.056 | 0.000 | 0.000 | 0.278 | 0.389 | 0.056 |
| 6.0-6.9 | 0.167 | 0.167 | 0.056 | 0.000 | 0.111 | 0.167 | 0.333 | 0.000 |

## eeg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1910)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.000 | 0.143 | 0.000 | 0.143 | 0.071 | 0.071 |
| 0.6-1.5 | 0.062 | 0.062 | 0.000 | 0.688 | 0.000 | 0.062 | 0.000 | 0.125 |
| 1.5-2.4 | 0.188 | 0.250 | 0.000 | 0.312 | 0.000 | 0.188 | 0.062 | 0.000 |
| 2.4-3.3 | 0.000 | 0.353 | 0.000 | 0.471 | 0.000 | 0.118 | 0.059 | 0.000 |
| 3.3-4.2 | 0.353 | 0.176 | 0.000 | 0.235 | 0.000 | 0.176 | 0.059 | 0.000 |
| 4.2-5.1 | 0.056 | 0.222 | 0.000 | 0.222 | 0.000 | 0.278 | 0.167 | 0.056 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.444 | 0.167 | 0.333 |
| 6.0-6.9 | 0.056 | 0.333 | 0.000 | 0.056 | 0.056 | 0.222 | 0.167 | 0.111 |

## eeg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.5625, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.429 | 0.214 | 0.071 | 0.000 | 0.000 | 0.214 | 0.000 |
| 0.6-1.5 | 0.000 | 0.562 | 0.000 | 0.000 | 0.000 | 0.000 | 0.438 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.250 | 0.000 | 0.000 | 0.000 | 0.500 | 0.250 |
| 2.4-3.3 | 0.000 | 0.412 | 0.235 | 0.000 | 0.000 | 0.000 | 0.353 | 0.000 |
| 3.3-4.2 | 0.118 | 0.176 | 0.118 | 0.059 | 0.000 | 0.000 | 0.412 | 0.118 |
| 4.2-5.1 | 0.000 | 0.167 | 0.167 | 0.056 | 0.000 | 0.000 | 0.556 | 0.056 |
| 5.1-6.0 | 0.000 | 0.111 | 0.000 | 0.056 | 0.056 | 0.000 | 0.500 | 0.278 |
| 6.0-6.9 | 0.000 | 0.222 | 0.111 | 0.111 | 0.000 | 0.000 | 0.500 | 0.056 |

## eeg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1802)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.6250, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.500 | 0.000 | 0.071 | 0.000 | 0.000 | 0.143 | 0.143 |
| 0.6-1.5 | 0.000 | 0.625 | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.000 |
| 1.5-2.4 | 0.000 | 0.375 | 0.000 | 0.188 | 0.000 | 0.000 | 0.375 | 0.062 |
| 2.4-3.3 | 0.118 | 0.588 | 0.000 | 0.118 | 0.000 | 0.000 | 0.176 | 0.000 |
| 3.3-4.2 | 0.059 | 0.412 | 0.000 | 0.059 | 0.059 | 0.000 | 0.235 | 0.176 |
| 4.2-5.1 | 0.000 | 0.444 | 0.000 | 0.111 | 0.000 | 0.000 | 0.389 | 0.056 |
| 5.1-6.0 | 0.000 | 0.278 | 0.000 | 0.222 | 0.000 | 0.000 | 0.444 | 0.056 |
| 6.0-6.9 | 0.000 | 0.389 | 0.000 | 0.111 | 0.000 | 0.000 | 0.500 | 0.000 |

## eeg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1704)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.6250, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.857 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.625 | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.000 |
| 1.5-2.4 | 0.000 | 0.438 | 0.000 | 0.062 | 0.000 | 0.000 | 0.312 | 0.188 |
| 2.4-3.3 | 0.000 | 0.647 | 0.000 | 0.118 | 0.000 | 0.000 | 0.235 | 0.000 |
| 3.3-4.2 | 0.118 | 0.412 | 0.000 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.056 | 0.000 | 0.000 | 0.444 | 0.000 |
| 5.1-6.0 | 0.000 | 0.167 | 0.000 | 0.333 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.111 | 0.278 | 0.000 | 0.167 | 0.000 | 0.000 | 0.444 | 0.000 |

## eeg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1684)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.5625, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.643 | 0.000 | 0.071 | 0.000 | 0.000 | 0.143 | 0.071 |
| 0.6-1.5 | 0.000 | 0.562 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.188 |
| 1.5-2.4 | 0.000 | 0.375 | 0.000 | 0.125 | 0.000 | 0.000 | 0.375 | 0.125 |
| 2.4-3.3 | 0.059 | 0.529 | 0.059 | 0.118 | 0.000 | 0.000 | 0.176 | 0.059 |
| 3.3-4.2 | 0.176 | 0.353 | 0.000 | 0.000 | 0.000 | 0.000 | 0.294 | 0.176 |
| 4.2-5.1 | 0.056 | 0.389 | 0.056 | 0.056 | 0.000 | 0.000 | 0.389 | 0.056 |
| 5.1-6.0 | 0.000 | 0.222 | 0.000 | 0.167 | 0.056 | 0.000 | 0.556 | 0.000 |
| 6.0-6.9 | 0.167 | 0.056 | 0.000 | 0.167 | 0.111 | 0.000 | 0.500 | 0.000 |

## eeg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1448)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.1875, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.000 | 0.000 | 0.071 | 0.143 | 0.000 | 0.071 |
| 0.6-1.5 | 0.250 | 0.188 | 0.250 | 0.000 | 0.062 | 0.188 | 0.000 | 0.062 |
| 1.5-2.4 | 0.312 | 0.375 | 0.125 | 0.062 | 0.062 | 0.062 | 0.000 | 0.000 |
| 2.4-3.3 | 0.235 | 0.294 | 0.353 | 0.000 | 0.000 | 0.000 | 0.118 | 0.000 |
| 3.3-4.2 | 0.176 | 0.412 | 0.235 | 0.000 | 0.000 | 0.000 | 0.118 | 0.059 |
| 4.2-5.1 | 0.611 | 0.222 | 0.056 | 0.000 | 0.056 | 0.000 | 0.056 | 0.000 |
| 5.1-6.0 | 0.389 | 0.222 | 0.056 | 0.056 | 0.000 | 0.000 | 0.278 | 0.000 |
| 6.0-6.9 | 0.556 | 0.167 | 0.111 | 0.056 | 0.000 | 0.056 | 0.000 | 0.056 |

## eeg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2188)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.143 | 0.143 | 0.071 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.111 | 0.222 | 0.167 | 0.167 | 0.111 | 0.000 | 0.111 | 0.111 |
| 1.5-2.4 | 0.167 | 0.167 | 0.111 | 0.111 | 0.056 | 0.222 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.278 | 0.222 | 0.222 | 0.000 | 0.000 |
| 3.3-4.2 | 0.167 | 0.111 | 0.167 | 0.167 | 0.111 | 0.000 | 0.111 | 0.167 |
| 4.2-5.1 | 0.056 | 0.056 | 0.222 | 0.278 | 0.167 | 0.056 | 0.111 | 0.056 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.167 | 0.167 | 0.056 | 0.500 | 0.111 |
| 6.0-6.9 | 0.000 | 0.111 | 0.111 | 0.056 | 0.111 | 0.167 | 0.333 | 0.111 |

## eeg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2188)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.143 | 0.071 | 0.143 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.167 | 0.444 | 0.167 | 0.000 | 0.056 | 0.111 | 0.000 | 0.056 |
| 1.5-2.4 | 0.111 | 0.111 | 0.111 | 0.222 | 0.111 | 0.111 | 0.167 | 0.056 |
| 2.4-3.3 | 0.167 | 0.000 | 0.056 | 0.333 | 0.167 | 0.167 | 0.056 | 0.056 |
| 3.3-4.2 | 0.222 | 0.167 | 0.167 | 0.056 | 0.000 | 0.111 | 0.056 | 0.222 |
| 4.2-5.1 | 0.056 | 0.167 | 0.111 | 0.111 | 0.222 | 0.000 | 0.167 | 0.167 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.111 | 0.056 | 0.167 | 0.444 | 0.111 |
| 6.0-6.9 | 0.056 | 0.111 | 0.111 | 0.056 | 0.222 | 0.111 | 0.167 | 0.167 |

## eeg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.071 | 0.071 | 0.000 | 0.071 | 0.143 | 0.000 |
| 0.6-1.5 | 0.333 | 0.000 | 0.000 | 0.111 | 0.056 | 0.111 | 0.222 | 0.167 |
| 1.5-2.4 | 0.222 | 0.000 | 0.056 | 0.167 | 0.111 | 0.333 | 0.056 | 0.056 |
| 2.4-3.3 | 0.167 | 0.000 | 0.056 | 0.333 | 0.000 | 0.333 | 0.056 | 0.056 |
| 3.3-4.2 | 0.278 | 0.000 | 0.111 | 0.111 | 0.000 | 0.278 | 0.222 | 0.000 |
| 4.2-5.1 | 0.278 | 0.000 | 0.000 | 0.111 | 0.056 | 0.333 | 0.167 | 0.056 |
| 5.1-6.0 | 0.167 | 0.000 | 0.167 | 0.056 | 0.056 | 0.333 | 0.222 | 0.000 |
| 6.0-6.9 | 0.222 | 0.000 | 0.056 | 0.056 | 0.000 | 0.389 | 0.111 | 0.167 |

## eeg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.357 | 0.143 | 0.000 | 0.000 | 0.000 | 0.143 | 0.071 |
| 0.6-1.5 | 0.278 | 0.111 | 0.167 | 0.167 | 0.056 | 0.111 | 0.056 | 0.056 |
| 1.5-2.4 | 0.167 | 0.278 | 0.056 | 0.111 | 0.111 | 0.111 | 0.167 | 0.000 |
| 2.4-3.3 | 0.056 | 0.167 | 0.000 | 0.222 | 0.056 | 0.167 | 0.278 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.167 | 0.167 | 0.056 | 0.000 | 0.111 | 0.278 |
| 4.2-5.1 | 0.000 | 0.000 | 0.111 | 0.111 | 0.056 | 0.056 | 0.444 | 0.222 |
| 5.1-6.0 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 | 0.278 | 0.611 | 0.000 |
| 6.0-6.9 | 0.056 | 0.056 | 0.111 | 0.056 | 0.222 | 0.000 | 0.333 | 0.167 |

## eeg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.5000, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.071 | 0.071 | 0.071 | 0.143 | 0.071 | 0.071 |
| 0.6-1.5 | 0.278 | 0.111 | 0.000 | 0.222 | 0.111 | 0.111 | 0.056 | 0.111 |
| 1.5-2.4 | 0.167 | 0.056 | 0.056 | 0.389 | 0.056 | 0.000 | 0.167 | 0.111 |
| 2.4-3.3 | 0.056 | 0.000 | 0.056 | 0.500 | 0.056 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.000 | 0.444 | 0.056 | 0.056 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.056 | 0.056 | 0.333 | 0.056 | 0.111 | 0.278 | 0.056 |
| 5.1-6.0 | 0.167 | 0.000 | 0.000 | 0.167 | 0.111 | 0.167 | 0.333 | 0.056 |
| 6.0-6.9 | 0.167 | 0.056 | 0.056 | 0.278 | 0.111 | 0.167 | 0.111 | 0.056 |

## eeg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.6111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.000 | 0.143 | 0.143 | 0.071 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.333 | 0.056 | 0.000 | 0.500 | 0.000 | 0.056 | 0.056 | 0.000 |
| 1.5-2.4 | 0.167 | 0.000 | 0.056 | 0.556 | 0.000 | 0.056 | 0.167 | 0.000 |
| 2.4-3.3 | 0.056 | 0.056 | 0.056 | 0.611 | 0.000 | 0.000 | 0.167 | 0.056 |
| 3.3-4.2 | 0.111 | 0.000 | 0.167 | 0.500 | 0.056 | 0.000 | 0.111 | 0.056 |
| 4.2-5.1 | 0.056 | 0.000 | 0.111 | 0.500 | 0.000 | 0.056 | 0.167 | 0.111 |
| 5.1-6.0 | 0.167 | 0.000 | 0.167 | 0.278 | 0.000 | 0.111 | 0.167 | 0.111 |
| 6.0-6.9 | 0.222 | 0.000 | 0.056 | 0.444 | 0.000 | 0.056 | 0.111 | 0.111 |

## eeg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.071 | 0.071 | 0.071 | 0.286 | 0.071 |
| 0.6-1.5 | 0.222 | 0.111 | 0.111 | 0.278 | 0.056 | 0.056 | 0.111 | 0.056 |
| 1.5-2.4 | 0.167 | 0.000 | 0.167 | 0.389 | 0.056 | 0.056 | 0.056 | 0.111 |
| 2.4-3.3 | 0.111 | 0.056 | 0.056 | 0.444 | 0.056 | 0.111 | 0.167 | 0.000 |
| 3.3-4.2 | 0.167 | 0.111 | 0.167 | 0.222 | 0.000 | 0.056 | 0.167 | 0.111 |
| 4.2-5.1 | 0.000 | 0.056 | 0.167 | 0.444 | 0.000 | 0.056 | 0.222 | 0.056 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.333 | 0.000 | 0.056 | 0.333 | 0.278 |
| 6.0-6.9 | 0.167 | 0.000 | 0.056 | 0.000 | 0.167 | 0.056 | 0.500 | 0.056 |

## eeg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1375)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/eeg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.071 | 0.071 | 0.071 | 0.071 | 0.143 | 0.214 | 0.071 |
| 0.6-1.5 | 0.278 | 0.000 | 0.056 | 0.222 | 0.056 | 0.111 | 0.111 | 0.167 |
| 1.5-2.4 | 0.111 | 0.111 | 0.056 | 0.167 | 0.111 | 0.278 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.000 | 0.056 | 0.389 | 0.056 | 0.222 | 0.222 | 0.000 |
| 3.3-4.2 | 0.111 | 0.000 | 0.000 | 0.278 | 0.056 | 0.222 | 0.167 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.056 | 0.222 | 0.111 | 0.167 | 0.278 | 0.167 |
| 5.1-6.0 | 0.111 | 0.000 | 0.000 | 0.222 | 0.111 | 0.167 | 0.278 | 0.111 |
| 6.0-6.9 | 0.056 | 0.000 | 0.056 | 0.278 | 0.111 | 0.222 | 0.222 | 0.056 |

## fused | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1501)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `0.6-1.5`: recall=0.1852, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.2075, support=53
- `5.1-6.0`: recall=0.2642, support=53
- `6.0-6.9`: recall=0.0566, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.263 | 0.053 | 0.026 | 0.316 | 0.132 | 0.105 | 0.053 |
| 0.6-1.5 | 0.019 | 0.185 | 0.093 | 0.074 | 0.167 | 0.111 | 0.130 | 0.222 |
| 1.5-2.4 | 0.056 | 0.167 | 0.111 | 0.037 | 0.130 | 0.148 | 0.259 | 0.093 |
| 2.4-3.3 | 0.000 | 0.148 | 0.037 | 0.074 | 0.296 | 0.185 | 0.185 | 0.074 |
| 3.3-4.2 | 0.037 | 0.074 | 0.056 | 0.056 | 0.241 | 0.241 | 0.204 | 0.093 |
| 4.2-5.1 | 0.019 | 0.075 | 0.075 | 0.075 | 0.245 | 0.208 | 0.264 | 0.038 |
| 5.1-6.0 | 0.038 | 0.094 | 0.113 | 0.075 | 0.264 | 0.094 | 0.264 | 0.057 |
| 6.0-6.9 | 0.075 | 0.132 | 0.113 | 0.075 | 0.226 | 0.094 | 0.226 | 0.057 |

## fused | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1467)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1579, support=38
- `0.6-1.5`: recall=0.3148, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.3962, support=53
- `6.0-6.9`: recall=0.0755, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.158 | 0.289 | 0.000 | 0.026 | 0.158 | 0.026 | 0.289 | 0.053 |
| 0.6-1.5 | 0.093 | 0.315 | 0.074 | 0.056 | 0.093 | 0.037 | 0.259 | 0.074 |
| 1.5-2.4 | 0.056 | 0.296 | 0.093 | 0.056 | 0.074 | 0.074 | 0.333 | 0.019 |
| 2.4-3.3 | 0.130 | 0.167 | 0.056 | 0.056 | 0.056 | 0.130 | 0.389 | 0.019 |
| 3.3-4.2 | 0.148 | 0.111 | 0.037 | 0.056 | 0.019 | 0.074 | 0.519 | 0.037 |
| 4.2-5.1 | 0.057 | 0.208 | 0.094 | 0.075 | 0.038 | 0.057 | 0.415 | 0.057 |
| 5.1-6.0 | 0.075 | 0.189 | 0.057 | 0.019 | 0.057 | 0.038 | 0.396 | 0.170 |
| 6.0-6.9 | 0.113 | 0.264 | 0.057 | 0.094 | 0.000 | 0.038 | 0.358 | 0.075 |

## fused | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1366)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0741, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.6038, support=53
- `6.0-6.9`: recall=0.0189, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.289 | 0.026 | 0.000 | 0.132 | 0.053 | 0.395 | 0.105 |
| 0.6-1.5 | 0.000 | 0.296 | 0.019 | 0.000 | 0.111 | 0.074 | 0.407 | 0.093 |
| 1.5-2.4 | 0.000 | 0.315 | 0.037 | 0.000 | 0.056 | 0.056 | 0.463 | 0.074 |
| 2.4-3.3 | 0.056 | 0.278 | 0.000 | 0.019 | 0.056 | 0.037 | 0.537 | 0.019 |
| 3.3-4.2 | 0.000 | 0.222 | 0.019 | 0.019 | 0.074 | 0.056 | 0.593 | 0.019 |
| 4.2-5.1 | 0.000 | 0.226 | 0.000 | 0.000 | 0.057 | 0.075 | 0.623 | 0.019 |
| 5.1-6.0 | 0.000 | 0.208 | 0.019 | 0.000 | 0.057 | 0.057 | 0.604 | 0.057 |
| 6.0-6.9 | 0.000 | 0.302 | 0.038 | 0.019 | 0.000 | 0.000 | 0.623 | 0.019 |

## fused | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1327)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.079 | 0.026 | 0.000 | 0.000 | 0.026 | 0.789 | 0.053 |
| 0.6-1.5 | 0.019 | 0.000 | 0.000 | 0.000 | 0.093 | 0.037 | 0.833 | 0.019 |
| 1.5-2.4 | 0.056 | 0.019 | 0.000 | 0.000 | 0.019 | 0.056 | 0.852 | 0.000 |
| 2.4-3.3 | 0.000 | 0.037 | 0.000 | 0.019 | 0.056 | 0.019 | 0.815 | 0.056 |
| 3.3-4.2 | 0.019 | 0.000 | 0.000 | 0.000 | 0.093 | 0.000 | 0.870 | 0.019 |
| 4.2-5.1 | 0.019 | 0.000 | 0.000 | 0.000 | 0.057 | 0.057 | 0.849 | 0.019 |
| 5.1-6.0 | 0.000 | 0.019 | 0.000 | 0.019 | 0.038 | 0.019 | 0.887 | 0.019 |
| 6.0-6.9 | 0.075 | 0.000 | 0.000 | 0.000 | 0.057 | 0.000 | 0.868 | 0.000 |

## fused | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1327)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.053 | 0.000 | 0.026 | 0.079 | 0.026 | 0.789 | 0.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.019 | 0.093 | 0.037 | 0.833 | 0.019 |
| 1.5-2.4 | 0.056 | 0.019 | 0.000 | 0.000 | 0.019 | 0.037 | 0.870 | 0.000 |
| 2.4-3.3 | 0.056 | 0.056 | 0.000 | 0.019 | 0.019 | 0.019 | 0.815 | 0.019 |
| 3.3-4.2 | 0.000 | 0.019 | 0.000 | 0.000 | 0.093 | 0.000 | 0.870 | 0.019 |
| 4.2-5.1 | 0.019 | 0.019 | 0.000 | 0.000 | 0.057 | 0.057 | 0.849 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.038 | 0.038 | 0.019 | 0.887 | 0.019 |
| 6.0-6.9 | 0.057 | 0.000 | 0.000 | 0.019 | 0.057 | 0.000 | 0.868 | 0.000 |

## fused | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1290)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `0.6-1.5`: recall=0.1852, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.4340, support=53
- `6.0-6.9`: recall=0.1887, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.079 | 0.079 | 0.026 | 0.026 | 0.158 | 0.079 | 0.368 | 0.184 |
| 0.6-1.5 | 0.019 | 0.185 | 0.000 | 0.000 | 0.148 | 0.037 | 0.333 | 0.278 |
| 1.5-2.4 | 0.019 | 0.148 | 0.037 | 0.037 | 0.111 | 0.056 | 0.426 | 0.167 |
| 2.4-3.3 | 0.037 | 0.111 | 0.000 | 0.019 | 0.167 | 0.130 | 0.407 | 0.130 |
| 3.3-4.2 | 0.037 | 0.130 | 0.000 | 0.019 | 0.093 | 0.130 | 0.481 | 0.111 |
| 4.2-5.1 | 0.000 | 0.094 | 0.019 | 0.019 | 0.151 | 0.075 | 0.509 | 0.132 |
| 5.1-6.0 | 0.038 | 0.075 | 0.019 | 0.057 | 0.094 | 0.113 | 0.434 | 0.170 |
| 6.0-6.9 | 0.057 | 0.170 | 0.019 | 0.019 | 0.075 | 0.113 | 0.358 | 0.189 |

## fused | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1637)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.071 | 0.000 | 0.000 | 0.000 | 0.286 | 0.286 |
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.333 | 0.000 | 0.000 | 0.056 | 0.056 | 0.000 | 0.500 |
| 2.4-3.3 | 0.000 | 0.278 | 0.167 | 0.000 | 0.000 | 0.000 | 0.222 | 0.333 |
| 3.3-4.2 | 0.118 | 0.294 | 0.059 | 0.000 | 0.059 | 0.000 | 0.235 | 0.235 |
| 4.2-5.1 | 0.167 | 0.000 | 0.167 | 0.000 | 0.000 | 0.000 | 0.389 | 0.278 |
| 5.1-6.0 | 0.333 | 0.056 | 0.056 | 0.000 | 0.056 | 0.000 | 0.333 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.222 | 0.278 |

## fused | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1567)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.000 | 0.071 | 0.000 | 0.000 | 0.286 | 0.214 |
| 0.6-1.5 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.167 | 0.333 |
| 1.5-2.4 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 | 0.444 |
| 2.4-3.3 | 0.056 | 0.389 | 0.056 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |
| 3.3-4.2 | 0.176 | 0.353 | 0.000 | 0.000 | 0.000 | 0.000 | 0.235 | 0.235 |
| 4.2-5.1 | 0.333 | 0.000 | 0.111 | 0.000 | 0.000 | 0.000 | 0.222 | 0.333 |
| 5.1-6.0 | 0.333 | 0.056 | 0.056 | 0.000 | 0.000 | 0.000 | 0.333 | 0.222 |
| 6.0-6.9 | 0.444 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.222 | 0.333 |

## fused | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1528)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.286 | 0.143 | 0.000 | 0.000 | 0.071 | 0.286 | 0.214 |
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.111 | 0.056 | 0.333 |
| 1.5-2.4 | 0.222 | 0.389 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.333 |
| 2.4-3.3 | 0.056 | 0.167 | 0.278 | 0.000 | 0.000 | 0.000 | 0.222 | 0.278 |
| 3.3-4.2 | 0.059 | 0.118 | 0.294 | 0.000 | 0.059 | 0.000 | 0.294 | 0.176 |
| 4.2-5.1 | 0.111 | 0.111 | 0.000 | 0.000 | 0.056 | 0.056 | 0.611 | 0.056 |
| 5.1-6.0 | 0.278 | 0.111 | 0.056 | 0.000 | 0.056 | 0.000 | 0.444 | 0.056 |
| 6.0-6.9 | 0.222 | 0.111 | 0.000 | 0.056 | 0.111 | 0.000 | 0.333 | 0.167 |

## fused | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1498)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.000 | 0.071 | 0.000 | 0.000 | 0.214 | 0.286 |
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.333 | 0.000 | 0.111 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.111 | 0.389 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 | 0.389 |
| 3.3-4.2 | 0.235 | 0.294 | 0.000 | 0.000 | 0.000 | 0.000 | 0.176 | 0.294 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.056 | 0.000 | 0.000 | 0.278 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.222 | 0.278 |

## fused | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.944 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## fused | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1181)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 1.5-2.4 | 0.000 | 0.056 | 0.444 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.529 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

## fused | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1688)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.286 | 0.143 | 0.071 | 0.071 | 0.000 |
| 0.6-1.5 | 0.111 | 0.278 | 0.167 | 0.167 | 0.167 | 0.056 | 0.056 | 0.000 |
| 1.5-2.4 | 0.056 | 0.222 | 0.278 | 0.222 | 0.000 | 0.111 | 0.000 | 0.111 |
| 2.4-3.3 | 0.111 | 0.167 | 0.111 | 0.222 | 0.056 | 0.167 | 0.056 | 0.111 |
| 3.3-4.2 | 0.167 | 0.111 | 0.167 | 0.278 | 0.056 | 0.111 | 0.056 | 0.056 |
| 4.2-5.1 | 0.118 | 0.176 | 0.118 | 0.176 | 0.059 | 0.118 | 0.118 | 0.118 |
| 5.1-6.0 | 0.167 | 0.167 | 0.111 | 0.111 | 0.000 | 0.222 | 0.056 | 0.167 |
| 6.0-6.9 | 0.167 | 0.056 | 0.222 | 0.111 | 0.111 | 0.278 | 0.056 | 0.000 |

## fused | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.071 |
| 0.6-1.5 | 0.222 | 0.278 | 0.222 | 0.056 | 0.111 | 0.056 | 0.000 | 0.056 |
| 1.5-2.4 | 0.167 | 0.278 | 0.222 | 0.111 | 0.111 | 0.111 | 0.000 | 0.000 |
| 2.4-3.3 | 0.111 | 0.111 | 0.111 | 0.167 | 0.167 | 0.167 | 0.056 | 0.111 |
| 3.3-4.2 | 0.222 | 0.056 | 0.111 | 0.167 | 0.222 | 0.056 | 0.056 | 0.111 |
| 4.2-5.1 | 0.235 | 0.176 | 0.118 | 0.059 | 0.118 | 0.059 | 0.118 | 0.118 |
| 5.1-6.0 | 0.333 | 0.167 | 0.056 | 0.111 | 0.000 | 0.111 | 0.000 | 0.222 |
| 6.0-6.9 | 0.222 | 0.111 | 0.111 | 0.167 | 0.056 | 0.111 | 0.167 | 0.056 |

## fused | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.143 | 0.000 | 0.071 | 0.071 | 0.143 | 0.000 |
| 0.6-1.5 | 0.278 | 0.278 | 0.222 | 0.000 | 0.000 | 0.056 | 0.167 | 0.000 |
| 1.5-2.4 | 0.167 | 0.389 | 0.056 | 0.056 | 0.056 | 0.111 | 0.167 | 0.000 |
| 2.4-3.3 | 0.167 | 0.333 | 0.111 | 0.056 | 0.056 | 0.111 | 0.111 | 0.056 |
| 3.3-4.2 | 0.333 | 0.111 | 0.111 | 0.056 | 0.056 | 0.111 | 0.167 | 0.056 |
| 4.2-5.1 | 0.353 | 0.118 | 0.059 | 0.000 | 0.059 | 0.176 | 0.176 | 0.059 |
| 5.1-6.0 | 0.333 | 0.278 | 0.056 | 0.000 | 0.000 | 0.111 | 0.167 | 0.056 |
| 6.0-6.9 | 0.556 | 0.000 | 0.056 | 0.000 | 0.056 | 0.167 | 0.111 | 0.056 |

## fused | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.1375)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.143 | 0.071 | 0.000 | 0.000 | 0.429 | 0.000 |
| 0.6-1.5 | 0.278 | 0.000 | 0.222 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 |
| 1.5-2.4 | 0.111 | 0.111 | 0.111 | 0.056 | 0.111 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.333 | 0.000 | 0.111 | 0.000 | 0.111 | 0.000 | 0.444 | 0.000 |
| 3.3-4.2 | 0.278 | 0.056 | 0.167 | 0.056 | 0.000 | 0.000 | 0.444 | 0.000 |
| 4.2-5.1 | 0.353 | 0.059 | 0.118 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 5.1-6.0 | 0.222 | 0.000 | 0.111 | 0.000 | 0.000 | 0.000 | 0.500 | 0.167 |
| 6.0-6.9 | 0.333 | 0.056 | 0.111 | 0.056 | 0.000 | 0.000 | 0.444 | 0.000 |

## fused | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1313)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.214 | 0.143 | 0.000 | 0.214 | 0.143 | 0.000 |
| 0.6-1.5 | 0.222 | 0.222 | 0.389 | 0.056 | 0.000 | 0.111 | 0.000 | 0.000 |
| 1.5-2.4 | 0.222 | 0.278 | 0.278 | 0.111 | 0.000 | 0.111 | 0.000 | 0.000 |
| 2.4-3.3 | 0.167 | 0.167 | 0.222 | 0.111 | 0.000 | 0.278 | 0.056 | 0.000 |
| 3.3-4.2 | 0.333 | 0.167 | 0.111 | 0.111 | 0.000 | 0.222 | 0.056 | 0.000 |
| 4.2-5.1 | 0.235 | 0.176 | 0.176 | 0.118 | 0.000 | 0.235 | 0.059 | 0.000 |
| 5.1-6.0 | 0.333 | 0.222 | 0.222 | 0.000 | 0.000 | 0.222 | 0.000 | 0.000 |
| 6.0-6.9 | 0.222 | 0.056 | 0.278 | 0.111 | 0.000 | 0.222 | 0.111 | 0.000 |

## fused | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.071 | 0.071 | 0.000 | 0.000 | 0.143 | 0.571 | 0.000 |
| 0.6-1.5 | 0.056 | 0.056 | 0.111 | 0.000 | 0.000 | 0.167 | 0.611 | 0.000 |
| 1.5-2.4 | 0.111 | 0.111 | 0.056 | 0.111 | 0.056 | 0.056 | 0.444 | 0.056 |
| 2.4-3.3 | 0.111 | 0.056 | 0.056 | 0.000 | 0.056 | 0.167 | 0.556 | 0.000 |
| 3.3-4.2 | 0.111 | 0.056 | 0.056 | 0.056 | 0.000 | 0.222 | 0.500 | 0.000 |
| 4.2-5.1 | 0.118 | 0.059 | 0.000 | 0.000 | 0.000 | 0.235 | 0.529 | 0.059 |
| 5.1-6.0 | 0.111 | 0.056 | 0.000 | 0.000 | 0.000 | 0.278 | 0.444 | 0.111 |
| 6.0-6.9 | 0.111 | 0.056 | 0.000 | 0.056 | 0.000 | 0.222 | 0.500 | 0.056 |

## fused | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1187)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.8889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.056 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |
| 1.5-2.4 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 4.2-5.1 | 0.000 | 0.882 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.118 |
| 5.1-6.0 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |
| 6.0-6.9 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |

## fused | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1187)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/fused/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.8889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.889 | 0.056 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 |
| 1.5-2.4 | 0.000 | 0.944 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.056 |
| 4.2-5.1 | 0.000 | 0.882 | 0.000 | 0.000 | 0.000 | 0.000 | 0.059 | 0.059 |
| 5.1-6.0 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 |

## pupil | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1474)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `0.6-1.5`: recall=0.1481, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.3962, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.105 | 0.000 | 0.026 | 0.132 | 0.053 | 0.342 | 0.211 |
| 0.6-1.5 | 0.056 | 0.148 | 0.000 | 0.056 | 0.148 | 0.111 | 0.241 | 0.241 |
| 1.5-2.4 | 0.093 | 0.148 | 0.037 | 0.000 | 0.074 | 0.130 | 0.389 | 0.130 |
| 2.4-3.3 | 0.074 | 0.111 | 0.037 | 0.093 | 0.167 | 0.019 | 0.352 | 0.148 |
| 3.3-4.2 | 0.056 | 0.111 | 0.037 | 0.019 | 0.111 | 0.148 | 0.481 | 0.037 |
| 4.2-5.1 | 0.132 | 0.075 | 0.094 | 0.075 | 0.057 | 0.075 | 0.396 | 0.094 |
| 5.1-6.0 | 0.132 | 0.038 | 0.057 | 0.113 | 0.113 | 0.057 | 0.396 | 0.094 |
| 6.0-6.9 | 0.151 | 0.113 | 0.038 | 0.094 | 0.038 | 0.094 | 0.302 | 0.170 |

## pupil | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1387)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `0.6-1.5`: recall=0.1667, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.3019, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.211 | 0.000 | 0.000 | 0.237 | 0.026 | 0.289 | 0.132 |
| 0.6-1.5 | 0.056 | 0.167 | 0.056 | 0.019 | 0.185 | 0.056 | 0.222 | 0.241 |
| 1.5-2.4 | 0.074 | 0.185 | 0.019 | 0.000 | 0.204 | 0.056 | 0.315 | 0.148 |
| 2.4-3.3 | 0.019 | 0.130 | 0.019 | 0.037 | 0.259 | 0.037 | 0.352 | 0.148 |
| 3.3-4.2 | 0.000 | 0.111 | 0.019 | 0.037 | 0.241 | 0.000 | 0.444 | 0.148 |
| 4.2-5.1 | 0.019 | 0.038 | 0.057 | 0.075 | 0.226 | 0.113 | 0.396 | 0.075 |
| 5.1-6.0 | 0.094 | 0.057 | 0.019 | 0.038 | 0.226 | 0.113 | 0.302 | 0.151 |
| 6.0-6.9 | 0.094 | 0.132 | 0.057 | 0.019 | 0.189 | 0.075 | 0.264 | 0.170 |

## pupil | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1370)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `0.6-1.5`: recall=0.3519, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.3774, support=53
- `6.0-6.9`: recall=0.0943, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.237 | 0.000 | 0.000 | 0.184 | 0.053 | 0.368 | 0.026 |
| 0.6-1.5 | 0.056 | 0.352 | 0.019 | 0.037 | 0.130 | 0.019 | 0.296 | 0.093 |
| 1.5-2.4 | 0.074 | 0.222 | 0.019 | 0.019 | 0.093 | 0.037 | 0.426 | 0.111 |
| 2.4-3.3 | 0.111 | 0.167 | 0.019 | 0.056 | 0.130 | 0.019 | 0.444 | 0.056 |
| 3.3-4.2 | 0.111 | 0.074 | 0.000 | 0.074 | 0.148 | 0.019 | 0.519 | 0.056 |
| 4.2-5.1 | 0.038 | 0.151 | 0.038 | 0.057 | 0.113 | 0.000 | 0.491 | 0.113 |
| 5.1-6.0 | 0.057 | 0.170 | 0.038 | 0.057 | 0.132 | 0.038 | 0.377 | 0.132 |
| 6.0-6.9 | 0.170 | 0.264 | 0.000 | 0.057 | 0.075 | 0.000 | 0.340 | 0.094 |

## pupil | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1292)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0370, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0189, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.053 | 0.026 | 0.000 | 0.026 | 0.026 | 0.789 | 0.053 |
| 0.6-1.5 | 0.037 | 0.000 | 0.000 | 0.000 | 0.093 | 0.000 | 0.852 | 0.019 |
| 1.5-2.4 | 0.056 | 0.019 | 0.000 | 0.000 | 0.019 | 0.037 | 0.870 | 0.000 |
| 2.4-3.3 | 0.019 | 0.000 | 0.000 | 0.000 | 0.074 | 0.019 | 0.815 | 0.074 |
| 3.3-4.2 | 0.056 | 0.000 | 0.019 | 0.000 | 0.037 | 0.000 | 0.870 | 0.019 |
| 4.2-5.1 | 0.019 | 0.000 | 0.019 | 0.019 | 0.019 | 0.057 | 0.849 | 0.019 |
| 5.1-6.0 | 0.019 | 0.019 | 0.000 | 0.000 | 0.019 | 0.019 | 0.887 | 0.038 |
| 6.0-6.9 | 0.057 | 0.019 | 0.000 | 0.019 | 0.019 | 0.000 | 0.868 | 0.019 |

## pupil | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=1.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1219)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.6038, support=53
- `6.0-6.9`: recall=0.0189, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.263 | 0.053 | 0.000 | 0.105 | 0.026 | 0.500 | 0.026 |
| 0.6-1.5 | 0.037 | 0.296 | 0.037 | 0.000 | 0.074 | 0.056 | 0.426 | 0.074 |
| 1.5-2.4 | 0.019 | 0.259 | 0.037 | 0.019 | 0.037 | 0.130 | 0.426 | 0.074 |
| 2.4-3.3 | 0.056 | 0.241 | 0.000 | 0.000 | 0.056 | 0.056 | 0.574 | 0.019 |
| 3.3-4.2 | 0.056 | 0.185 | 0.000 | 0.000 | 0.019 | 0.037 | 0.685 | 0.019 |
| 4.2-5.1 | 0.038 | 0.189 | 0.000 | 0.000 | 0.019 | 0.038 | 0.679 | 0.038 |
| 5.1-6.0 | 0.019 | 0.226 | 0.019 | 0.000 | 0.038 | 0.057 | 0.604 | 0.038 |
| 6.0-6.9 | 0.019 | 0.302 | 0.038 | 0.000 | 0.000 | 0.019 | 0.604 | 0.019 |

## pupil | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1205)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.5472, support=53
- `6.0-6.9`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.079 | 0.000 | 0.000 | 0.079 | 0.026 | 0.421 | 0.368 |
| 0.6-1.5 | 0.019 | 0.000 | 0.000 | 0.000 | 0.130 | 0.000 | 0.500 | 0.352 |
| 1.5-2.4 | 0.056 | 0.019 | 0.000 | 0.000 | 0.019 | 0.037 | 0.537 | 0.333 |
| 2.4-3.3 | 0.000 | 0.056 | 0.000 | 0.000 | 0.093 | 0.019 | 0.481 | 0.352 |
| 3.3-4.2 | 0.056 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.556 | 0.333 |
| 4.2-5.1 | 0.019 | 0.019 | 0.000 | 0.000 | 0.057 | 0.057 | 0.509 | 0.340 |
| 5.1-6.0 | 0.019 | 0.000 | 0.000 | 0.000 | 0.075 | 0.000 | 0.547 | 0.358 |
| 6.0-6.9 | 0.057 | 0.000 | 0.000 | 0.000 | 0.075 | 0.000 | 0.566 | 0.302 |

## pupil | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1607)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.071 | 0.000 | 0.000 | 0.000 | 0.214 | 0.286 |
| 0.6-1.5 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.056 | 0.389 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.222 | 0.111 | 0.167 | 0.000 | 0.000 | 0.000 | 0.111 | 0.389 |
| 3.3-4.2 | 0.294 | 0.118 | 0.118 | 0.000 | 0.000 | 0.000 | 0.176 | 0.294 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 | 0.278 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.167 | 0.278 |

## pupil | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1518)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.000 | 0.000 | 0.000 | 0.214 | 0.286 |
| 0.6-1.5 | 0.000 | 0.389 | 0.111 | 0.000 | 0.000 | 0.000 | 0.111 | 0.389 |
| 1.5-2.4 | 0.056 | 0.278 | 0.056 | 0.056 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.111 | 0.111 | 0.278 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |
| 3.3-4.2 | 0.176 | 0.118 | 0.235 | 0.000 | 0.000 | 0.000 | 0.235 | 0.235 |
| 4.2-5.1 | 0.389 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.333 | 0.222 |
| 5.1-6.0 | 0.444 | 0.056 | 0.056 | 0.000 | 0.000 | 0.000 | 0.278 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.222 | 0.278 |

## pupil | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1389)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.357 | 0.143 | 0.000 | 0.071 | 0.000 | 0.214 | 0.214 |
| 0.6-1.5 | 0.000 | 0.389 | 0.000 | 0.056 | 0.056 | 0.000 | 0.278 | 0.222 |
| 1.5-2.4 | 0.000 | 0.444 | 0.056 | 0.056 | 0.056 | 0.000 | 0.167 | 0.222 |
| 2.4-3.3 | 0.056 | 0.222 | 0.278 | 0.000 | 0.000 | 0.000 | 0.278 | 0.167 |
| 3.3-4.2 | 0.000 | 0.118 | 0.353 | 0.000 | 0.059 | 0.000 | 0.412 | 0.059 |
| 4.2-5.1 | 0.056 | 0.222 | 0.000 | 0.167 | 0.056 | 0.000 | 0.389 | 0.111 |
| 5.1-6.0 | 0.000 | 0.111 | 0.111 | 0.000 | 0.056 | 0.000 | 0.389 | 0.333 |
| 6.0-6.9 | 0.056 | 0.167 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 | 0.222 |

## pupil | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.944 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## pupil | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 1.5-2.4 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 | 0.444 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.471 | 0.529 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |

## pupil | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=1.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1240)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.000 | 0.071 | 0.071 | 0.214 | 0.214 |
| 0.6-1.5 | 0.056 | 0.278 | 0.056 | 0.111 | 0.000 | 0.000 | 0.167 | 0.333 |
| 1.5-2.4 | 0.111 | 0.333 | 0.000 | 0.056 | 0.000 | 0.000 | 0.111 | 0.389 |
| 2.4-3.3 | 0.222 | 0.056 | 0.222 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |
| 3.3-4.2 | 0.294 | 0.000 | 0.235 | 0.000 | 0.000 | 0.000 | 0.235 | 0.235 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.278 | 0.222 |
| 5.1-6.0 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.111 | 0.222 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 | 0.111 | 0.278 |

## pupil | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.2062)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.286 | 0.143 | 0.071 | 0.071 | 0.000 |
| 0.6-1.5 | 0.056 | 0.222 | 0.167 | 0.222 | 0.167 | 0.056 | 0.056 | 0.056 |
| 1.5-2.4 | 0.056 | 0.222 | 0.278 | 0.222 | 0.056 | 0.111 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.111 | 0.278 | 0.056 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.111 | 0.222 | 0.056 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.176 | 0.176 | 0.059 | 0.176 | 0.059 | 0.118 | 0.176 | 0.059 |
| 5.1-6.0 | 0.167 | 0.167 | 0.111 | 0.056 | 0.000 | 0.222 | 0.222 | 0.056 |
| 6.0-6.9 | 0.167 | 0.056 | 0.167 | 0.167 | 0.056 | 0.222 | 0.056 | 0.111 |

## pupil | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.143 | 0.000 | 0.214 | 0.071 | 0.143 | 0.000 |
| 0.6-1.5 | 0.222 | 0.278 | 0.222 | 0.000 | 0.000 | 0.111 | 0.167 | 0.000 |
| 1.5-2.4 | 0.056 | 0.333 | 0.111 | 0.056 | 0.056 | 0.222 | 0.167 | 0.000 |
| 2.4-3.3 | 0.056 | 0.333 | 0.111 | 0.056 | 0.056 | 0.222 | 0.111 | 0.056 |
| 3.3-4.2 | 0.167 | 0.167 | 0.111 | 0.056 | 0.111 | 0.167 | 0.167 | 0.056 |
| 4.2-5.1 | 0.294 | 0.118 | 0.059 | 0.000 | 0.118 | 0.235 | 0.176 | 0.000 |
| 5.1-6.0 | 0.222 | 0.278 | 0.056 | 0.000 | 0.000 | 0.222 | 0.167 | 0.056 |
| 6.0-6.9 | 0.444 | 0.000 | 0.056 | 0.000 | 0.056 | 0.278 | 0.111 | 0.056 |

## pupil | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1562)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.071 | 0.071 | 0.143 | 0.143 | 0.143 | 0.071 |
| 0.6-1.5 | 0.222 | 0.278 | 0.167 | 0.000 | 0.111 | 0.056 | 0.056 | 0.111 |
| 1.5-2.4 | 0.167 | 0.333 | 0.111 | 0.111 | 0.056 | 0.111 | 0.111 | 0.000 |
| 2.4-3.3 | 0.111 | 0.167 | 0.111 | 0.111 | 0.167 | 0.167 | 0.056 | 0.111 |
| 3.3-4.2 | 0.278 | 0.056 | 0.111 | 0.167 | 0.167 | 0.056 | 0.056 | 0.111 |
| 4.2-5.1 | 0.294 | 0.176 | 0.118 | 0.000 | 0.118 | 0.059 | 0.118 | 0.118 |
| 5.1-6.0 | 0.333 | 0.167 | 0.056 | 0.000 | 0.000 | 0.111 | 0.056 | 0.278 |
| 6.0-6.9 | 0.167 | 0.111 | 0.111 | 0.167 | 0.056 | 0.222 | 0.111 | 0.056 |

## pupil | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.1562)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.143 | 0.143 | 0.000 | 0.071 | 0.357 | 0.000 |
| 0.6-1.5 | 0.167 | 0.056 | 0.167 | 0.111 | 0.056 | 0.111 | 0.333 | 0.000 |
| 1.5-2.4 | 0.111 | 0.056 | 0.333 | 0.056 | 0.056 | 0.167 | 0.222 | 0.000 |
| 2.4-3.3 | 0.167 | 0.056 | 0.167 | 0.056 | 0.111 | 0.167 | 0.278 | 0.000 |
| 3.3-4.2 | 0.167 | 0.000 | 0.111 | 0.167 | 0.167 | 0.111 | 0.278 | 0.000 |
| 4.2-5.1 | 0.176 | 0.059 | 0.176 | 0.118 | 0.000 | 0.176 | 0.294 | 0.000 |
| 5.1-6.0 | 0.222 | 0.056 | 0.111 | 0.111 | 0.000 | 0.111 | 0.222 | 0.167 |
| 6.0-6.9 | 0.167 | 0.056 | 0.167 | 0.111 | 0.056 | 0.167 | 0.278 | 0.000 |

## pupil | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1313)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.214 | 0.143 | 0.000 | 0.214 | 0.143 | 0.000 |
| 0.6-1.5 | 0.222 | 0.222 | 0.389 | 0.056 | 0.000 | 0.111 | 0.000 | 0.000 |
| 1.5-2.4 | 0.222 | 0.278 | 0.278 | 0.111 | 0.000 | 0.111 | 0.000 | 0.000 |
| 2.4-3.3 | 0.167 | 0.167 | 0.222 | 0.111 | 0.000 | 0.278 | 0.056 | 0.000 |
| 3.3-4.2 | 0.333 | 0.167 | 0.111 | 0.111 | 0.000 | 0.222 | 0.056 | 0.000 |
| 4.2-5.1 | 0.235 | 0.176 | 0.176 | 0.118 | 0.000 | 0.235 | 0.059 | 0.000 |
| 5.1-6.0 | 0.333 | 0.222 | 0.222 | 0.000 | 0.000 | 0.222 | 0.000 | 0.000 |
| 6.0-6.9 | 0.222 | 0.056 | 0.278 | 0.111 | 0.000 | 0.222 | 0.111 | 0.000 |

## pupil | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1313)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.8889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.889 | 0.000 | 0.000 | 0.056 | 0.000 | 0.056 | 0.000 |
| 1.5-2.4 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.000 | 0.056 | 0.000 | 0.056 | 0.000 |
| 4.2-5.1 | 0.059 | 0.882 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.059 |
| 5.1-6.0 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 |
| 6.0-6.9 | 0.056 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.071 | 0.071 | 0.214 | 0.000 | 0.357 | 0.071 |
| 0.6-1.5 | 0.167 | 0.000 | 0.056 | 0.167 | 0.222 | 0.000 | 0.333 | 0.056 |
| 1.5-2.4 | 0.056 | 0.056 | 0.111 | 0.000 | 0.389 | 0.000 | 0.333 | 0.056 |
| 2.4-3.3 | 0.222 | 0.000 | 0.111 | 0.000 | 0.222 | 0.000 | 0.278 | 0.167 |
| 3.3-4.2 | 0.167 | 0.056 | 0.000 | 0.111 | 0.278 | 0.000 | 0.278 | 0.111 |
| 4.2-5.1 | 0.235 | 0.059 | 0.000 | 0.059 | 0.176 | 0.000 | 0.353 | 0.118 |
| 5.1-6.0 | 0.111 | 0.000 | 0.000 | 0.111 | 0.222 | 0.000 | 0.333 | 0.222 |
| 6.0-6.9 | 0.111 | 0.056 | 0.000 | 0.167 | 0.222 | 0.000 | 0.389 | 0.056 |

## pupil | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1125)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline_advanced_nn/pupil/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.8889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 |
| 1.5-2.4 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 |
| 4.2-5.1 | 0.059 | 0.882 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.059 |
| 5.1-6.0 | 0.000 | 0.944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |
| 6.0-6.9 | 0.056 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 |


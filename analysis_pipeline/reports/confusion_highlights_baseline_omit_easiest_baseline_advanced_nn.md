# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline_advanced_nn.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1987)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.2745, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.4808, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.027 | 0.243 | 0.108 | 0.027 | 0.216 | 0.162 |
| 1.5-2.4 | 0.130 | 0.093 | 0.315 | 0.093 | 0.056 | 0.204 | 0.111 |
| 2.4-3.3 | 0.118 | 0.118 | 0.275 | 0.118 | 0.020 | 0.333 | 0.020 |
| 3.3-4.2 | 0.132 | 0.132 | 0.264 | 0.132 | 0.000 | 0.321 | 0.019 |
| 4.2-5.1 | 0.059 | 0.078 | 0.235 | 0.039 | 0.039 | 0.451 | 0.098 |
| 5.1-6.0 | 0.115 | 0.058 | 0.154 | 0.115 | 0.019 | 0.481 | 0.058 |
| 6.0-6.9 | 0.135 | 0.058 | 0.135 | 0.154 | 0.058 | 0.308 | 0.154 |

## ecg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1785)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `1.5-2.4`: recall=0.4074, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.0189, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.0385, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.324 | 0.054 | 0.000 | 0.216 | 0.000 | 0.108 |
| 1.5-2.4 | 0.185 | 0.407 | 0.056 | 0.000 | 0.111 | 0.093 | 0.148 |
| 2.4-3.3 | 0.216 | 0.392 | 0.078 | 0.020 | 0.157 | 0.039 | 0.098 |
| 3.3-4.2 | 0.245 | 0.377 | 0.000 | 0.019 | 0.151 | 0.075 | 0.132 |
| 4.2-5.1 | 0.176 | 0.314 | 0.039 | 0.000 | 0.255 | 0.078 | 0.137 |
| 5.1-6.0 | 0.269 | 0.288 | 0.077 | 0.019 | 0.250 | 0.038 | 0.058 |
| 6.0-6.9 | 0.096 | 0.308 | 0.038 | 0.000 | 0.385 | 0.019 | 0.154 |

## ecg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1783)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.1373, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.2308, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.054 | 0.108 | 0.243 | 0.027 | 0.081 | 0.270 |
| 1.5-2.4 | 0.259 | 0.130 | 0.111 | 0.222 | 0.037 | 0.111 | 0.130 |
| 2.4-3.3 | 0.314 | 0.216 | 0.098 | 0.157 | 0.098 | 0.078 | 0.039 |
| 3.3-4.2 | 0.283 | 0.170 | 0.057 | 0.264 | 0.075 | 0.113 | 0.038 |
| 4.2-5.1 | 0.235 | 0.059 | 0.157 | 0.235 | 0.137 | 0.059 | 0.118 |
| 5.1-6.0 | 0.250 | 0.115 | 0.096 | 0.096 | 0.135 | 0.173 | 0.135 |
| 6.0-6.9 | 0.327 | 0.058 | 0.077 | 0.173 | 0.115 | 0.019 | 0.231 |

## ecg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1748)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.2549, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.2308, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.108 | 0.297 | 0.081 | 0.054 | 0.081 | 0.270 |
| 1.5-2.4 | 0.074 | 0.278 | 0.241 | 0.074 | 0.000 | 0.204 | 0.130 |
| 2.4-3.3 | 0.098 | 0.235 | 0.255 | 0.039 | 0.020 | 0.176 | 0.176 |
| 3.3-4.2 | 0.132 | 0.245 | 0.113 | 0.132 | 0.019 | 0.226 | 0.132 |
| 4.2-5.1 | 0.098 | 0.196 | 0.196 | 0.098 | 0.039 | 0.216 | 0.157 |
| 5.1-6.0 | 0.077 | 0.173 | 0.250 | 0.173 | 0.038 | 0.192 | 0.096 |
| 6.0-6.9 | 0.077 | 0.135 | 0.192 | 0.096 | 0.096 | 0.173 | 0.231 |

## ecg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1522)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.081 | 0.243 | 0.135 | 0.135 | 0.054 | 0.189 |
| 1.5-2.4 | 0.296 | 0.130 | 0.056 | 0.037 | 0.074 | 0.222 | 0.185 |
| 2.4-3.3 | 0.275 | 0.137 | 0.157 | 0.118 | 0.098 | 0.176 | 0.039 |
| 3.3-4.2 | 0.208 | 0.151 | 0.094 | 0.170 | 0.113 | 0.189 | 0.075 |
| 4.2-5.1 | 0.255 | 0.098 | 0.157 | 0.059 | 0.216 | 0.157 | 0.059 |
| 5.1-6.0 | 0.288 | 0.077 | 0.115 | 0.096 | 0.173 | 0.192 | 0.058 |
| 6.0-6.9 | 0.192 | 0.115 | 0.135 | 0.135 | 0.231 | 0.135 | 0.058 |

## ecg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1401)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0811, support=37
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.3269, support=52
- `6.0-6.9`: recall=0.2500, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.081 | 0.054 | 0.162 | 0.054 | 0.027 | 0.270 | 0.351 |
| 1.5-2.4 | 0.130 | 0.000 | 0.167 | 0.185 | 0.037 | 0.315 | 0.167 |
| 2.4-3.3 | 0.196 | 0.078 | 0.098 | 0.098 | 0.039 | 0.353 | 0.137 |
| 3.3-4.2 | 0.189 | 0.075 | 0.075 | 0.151 | 0.019 | 0.358 | 0.132 |
| 4.2-5.1 | 0.137 | 0.020 | 0.137 | 0.157 | 0.059 | 0.353 | 0.137 |
| 5.1-6.0 | 0.135 | 0.038 | 0.192 | 0.077 | 0.115 | 0.327 | 0.115 |
| 6.0-6.9 | 0.115 | 0.058 | 0.154 | 0.096 | 0.077 | 0.250 | 0.250 |

## ecg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1372)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.1154, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.054 | 0.081 | 0.243 | 0.081 | 0.135 | 0.162 | 0.243 |
| 1.5-2.4 | 0.037 | 0.167 | 0.167 | 0.074 | 0.074 | 0.333 | 0.148 |
| 2.4-3.3 | 0.098 | 0.098 | 0.059 | 0.137 | 0.078 | 0.333 | 0.196 |
| 3.3-4.2 | 0.113 | 0.170 | 0.038 | 0.132 | 0.094 | 0.321 | 0.132 |
| 4.2-5.1 | 0.098 | 0.098 | 0.176 | 0.078 | 0.176 | 0.255 | 0.118 |
| 5.1-6.0 | 0.077 | 0.192 | 0.231 | 0.077 | 0.212 | 0.192 | 0.019 |
| 6.0-6.9 | 0.019 | 0.000 | 0.212 | 0.115 | 0.212 | 0.327 | 0.115 |

## ecg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1239)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1346, support=52
- `6.0-6.9`: recall=0.0192, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.108 | 0.135 | 0.243 | 0.162 | 0.054 | 0.135 |
| 1.5-2.4 | 0.315 | 0.074 | 0.130 | 0.148 | 0.130 | 0.148 | 0.056 |
| 2.4-3.3 | 0.275 | 0.059 | 0.137 | 0.137 | 0.176 | 0.157 | 0.059 |
| 3.3-4.2 | 0.208 | 0.075 | 0.113 | 0.170 | 0.170 | 0.189 | 0.075 |
| 4.2-5.1 | 0.294 | 0.098 | 0.098 | 0.196 | 0.216 | 0.078 | 0.020 |
| 5.1-6.0 | 0.231 | 0.096 | 0.154 | 0.192 | 0.173 | 0.135 | 0.019 |
| 6.0-6.9 | 0.154 | 0.077 | 0.192 | 0.269 | 0.173 | 0.115 | 0.019 |

## ecg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1705)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.3750, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.357 | 0.429 | 0.000 | 0.000 | 0.000 | 0.143 |
| 1.5-2.4 | 0.062 | 0.375 | 0.500 | 0.062 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.118 | 0.176 | 0.471 | 0.118 | 0.000 | 0.059 | 0.059 |
| 3.3-4.2 | 0.000 | 0.294 | 0.353 | 0.118 | 0.059 | 0.059 | 0.118 |
| 4.2-5.1 | 0.111 | 0.000 | 0.333 | 0.167 | 0.000 | 0.167 | 0.222 |
| 5.1-6.0 | 0.056 | 0.278 | 0.222 | 0.222 | 0.056 | 0.056 | 0.111 |
| 6.0-6.9 | 0.000 | 0.278 | 0.278 | 0.222 | 0.056 | 0.056 | 0.111 |

## ecg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1569)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.071 | 0.000 | 0.071 | 0.143 | 0.143 |
| 1.5-2.4 | 0.438 | 0.062 | 0.188 | 0.000 | 0.000 | 0.188 | 0.125 |
| 2.4-3.3 | 0.176 | 0.059 | 0.471 | 0.000 | 0.059 | 0.118 | 0.118 |
| 3.3-4.2 | 0.294 | 0.118 | 0.176 | 0.000 | 0.118 | 0.118 | 0.176 |
| 4.2-5.1 | 0.222 | 0.056 | 0.278 | 0.056 | 0.056 | 0.222 | 0.111 |
| 5.1-6.0 | 0.111 | 0.222 | 0.111 | 0.056 | 0.000 | 0.278 | 0.222 |
| 6.0-6.9 | 0.056 | 0.333 | 0.111 | 0.111 | 0.056 | 0.333 | 0.000 |

## ecg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1470)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.4375, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.429 | 0.286 | 0.000 | 0.143 | 0.071 | 0.000 |
| 1.5-2.4 | 0.188 | 0.438 | 0.250 | 0.000 | 0.062 | 0.000 | 0.062 |
| 2.4-3.3 | 0.176 | 0.294 | 0.176 | 0.000 | 0.118 | 0.118 | 0.118 |
| 3.3-4.2 | 0.176 | 0.294 | 0.294 | 0.000 | 0.235 | 0.000 | 0.000 |
| 4.2-5.1 | 0.056 | 0.111 | 0.222 | 0.000 | 0.278 | 0.056 | 0.278 |
| 5.1-6.0 | 0.222 | 0.278 | 0.167 | 0.000 | 0.111 | 0.000 | 0.222 |
| 6.0-6.9 | 0.167 | 0.389 | 0.111 | 0.056 | 0.167 | 0.056 | 0.056 |

## ecg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1450)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.000 | 0.143 | 0.143 | 0.214 |
| 1.5-2.4 | 0.188 | 0.062 | 0.250 | 0.000 | 0.125 | 0.250 | 0.125 |
| 2.4-3.3 | 0.176 | 0.118 | 0.176 | 0.000 | 0.059 | 0.235 | 0.235 |
| 3.3-4.2 | 0.118 | 0.118 | 0.294 | 0.000 | 0.118 | 0.176 | 0.176 |
| 4.2-5.1 | 0.111 | 0.000 | 0.222 | 0.111 | 0.167 | 0.278 | 0.111 |
| 5.1-6.0 | 0.111 | 0.111 | 0.111 | 0.000 | 0.222 | 0.333 | 0.111 |
| 6.0-6.9 | 0.111 | 0.278 | 0.000 | 0.111 | 0.167 | 0.278 | 0.056 |

## ecg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1368)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.286 | 0.000 | 0.071 | 0.286 | 0.000 |
| 1.5-2.4 | 0.250 | 0.062 | 0.375 | 0.000 | 0.000 | 0.250 | 0.062 |
| 2.4-3.3 | 0.176 | 0.059 | 0.176 | 0.000 | 0.059 | 0.353 | 0.176 |
| 3.3-4.2 | 0.176 | 0.059 | 0.353 | 0.059 | 0.118 | 0.235 | 0.000 |
| 4.2-5.1 | 0.056 | 0.111 | 0.222 | 0.000 | 0.111 | 0.222 | 0.278 |
| 5.1-6.0 | 0.167 | 0.056 | 0.167 | 0.167 | 0.000 | 0.278 | 0.167 |
| 6.0-6.9 | 0.222 | 0.167 | 0.167 | 0.111 | 0.111 | 0.111 | 0.111 |

## ecg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1266)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.143 | 0.000 | 0.000 | 0.429 | 0.143 |
| 1.5-2.4 | 0.062 | 0.125 | 0.250 | 0.000 | 0.000 | 0.562 | 0.000 |
| 2.4-3.3 | 0.294 | 0.059 | 0.294 | 0.000 | 0.000 | 0.353 | 0.000 |
| 3.3-4.2 | 0.176 | 0.176 | 0.176 | 0.000 | 0.000 | 0.235 | 0.235 |
| 4.2-5.1 | 0.056 | 0.056 | 0.333 | 0.000 | 0.000 | 0.278 | 0.278 |
| 5.1-6.0 | 0.111 | 0.222 | 0.222 | 0.000 | 0.000 | 0.278 | 0.167 |
| 6.0-6.9 | 0.222 | 0.111 | 0.111 | 0.000 | 0.000 | 0.500 | 0.056 |

## ecg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1189)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.286 | 0.000 | 0.000 | 0.357 | 0.071 |
| 1.5-2.4 | 0.312 | 0.188 | 0.062 | 0.000 | 0.000 | 0.375 | 0.062 |
| 2.4-3.3 | 0.176 | 0.059 | 0.235 | 0.000 | 0.000 | 0.353 | 0.176 |
| 3.3-4.2 | 0.176 | 0.059 | 0.176 | 0.059 | 0.000 | 0.412 | 0.118 |
| 4.2-5.1 | 0.056 | 0.111 | 0.056 | 0.056 | 0.000 | 0.444 | 0.278 |
| 5.1-6.0 | 0.167 | 0.278 | 0.167 | 0.000 | 0.000 | 0.167 | 0.222 |
| 6.0-6.9 | 0.222 | 0.167 | 0.167 | 0.000 | 0.000 | 0.389 | 0.056 |

## ecg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1053)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.000 | 0.286 | 0.000 | 0.000 | 0.286 | 0.143 |
| 1.5-2.4 | 0.125 | 0.000 | 0.375 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.353 | 0.000 | 0.235 | 0.000 | 0.000 | 0.294 | 0.118 |
| 3.3-4.2 | 0.235 | 0.000 | 0.235 | 0.059 | 0.000 | 0.235 | 0.235 |
| 4.2-5.1 | 0.000 | 0.000 | 0.389 | 0.000 | 0.000 | 0.333 | 0.278 |
| 5.1-6.0 | 0.278 | 0.056 | 0.444 | 0.000 | 0.000 | 0.111 | 0.111 |
| 6.0-6.9 | 0.167 | 0.056 | 0.222 | 0.000 | 0.111 | 0.389 | 0.056 |

## ecg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.000 | 0.000 | 0.286 | 0.071 | 0.071 |
| 1.5-2.4 | 0.333 | 0.000 | 0.278 | 0.056 | 0.056 | 0.111 | 0.167 |
| 2.4-3.3 | 0.167 | 0.056 | 0.333 | 0.056 | 0.111 | 0.111 | 0.167 |
| 3.3-4.2 | 0.056 | 0.056 | 0.222 | 0.167 | 0.167 | 0.167 | 0.167 |
| 4.2-5.1 | 0.111 | 0.000 | 0.167 | 0.167 | 0.389 | 0.056 | 0.111 |
| 5.1-6.0 | 0.167 | 0.000 | 0.278 | 0.222 | 0.056 | 0.222 | 0.056 |
| 6.0-6.9 | 0.111 | 0.167 | 0.167 | 0.111 | 0.167 | 0.000 | 0.278 |

## ecg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.000 | 0.286 | 0.143 | 0.071 |
| 1.5-2.4 | 0.167 | 0.111 | 0.167 | 0.111 | 0.056 | 0.111 | 0.278 |
| 2.4-3.3 | 0.111 | 0.222 | 0.056 | 0.056 | 0.111 | 0.278 | 0.167 |
| 3.3-4.2 | 0.056 | 0.222 | 0.111 | 0.222 | 0.167 | 0.167 | 0.056 |
| 4.2-5.1 | 0.222 | 0.056 | 0.278 | 0.056 | 0.222 | 0.111 | 0.056 |
| 5.1-6.0 | 0.111 | 0.111 | 0.111 | 0.111 | 0.167 | 0.333 | 0.056 |
| 6.0-6.9 | 0.167 | 0.167 | 0.167 | 0.000 | 0.167 | 0.056 | 0.278 |

## ecg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.071 | 0.214 | 0.143 | 0.000 | 0.214 |
| 1.5-2.4 | 0.167 | 0.000 | 0.278 | 0.111 | 0.000 | 0.111 | 0.333 |
| 2.4-3.3 | 0.056 | 0.056 | 0.278 | 0.111 | 0.222 | 0.056 | 0.222 |
| 3.3-4.2 | 0.222 | 0.056 | 0.167 | 0.056 | 0.222 | 0.056 | 0.222 |
| 4.2-5.1 | 0.111 | 0.000 | 0.056 | 0.222 | 0.389 | 0.056 | 0.167 |
| 5.1-6.0 | 0.222 | 0.000 | 0.389 | 0.111 | 0.167 | 0.000 | 0.111 |
| 6.0-6.9 | 0.222 | 0.111 | 0.222 | 0.167 | 0.000 | 0.000 | 0.278 |

## ecg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.143 | 0.143 | 0.214 | 0.000 | 0.071 |
| 1.5-2.4 | 0.222 | 0.056 | 0.111 | 0.111 | 0.056 | 0.056 | 0.389 |
| 2.4-3.3 | 0.278 | 0.000 | 0.167 | 0.111 | 0.111 | 0.000 | 0.333 |
| 3.3-4.2 | 0.167 | 0.056 | 0.111 | 0.000 | 0.278 | 0.056 | 0.333 |
| 4.2-5.1 | 0.056 | 0.000 | 0.167 | 0.000 | 0.444 | 0.056 | 0.278 |
| 5.1-6.0 | 0.056 | 0.056 | 0.167 | 0.111 | 0.222 | 0.056 | 0.333 |
| 6.0-6.9 | 0.111 | 0.333 | 0.167 | 0.000 | 0.111 | 0.000 | 0.278 |

## ecg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.357 | 0.071 | 0.214 | 0.000 | 0.143 |
| 1.5-2.4 | 0.167 | 0.056 | 0.222 | 0.000 | 0.333 | 0.000 | 0.222 |
| 2.4-3.3 | 0.056 | 0.111 | 0.222 | 0.056 | 0.333 | 0.000 | 0.222 |
| 3.3-4.2 | 0.056 | 0.167 | 0.222 | 0.056 | 0.278 | 0.000 | 0.222 |
| 4.2-5.1 | 0.167 | 0.000 | 0.056 | 0.111 | 0.444 | 0.000 | 0.222 |
| 5.1-6.0 | 0.111 | 0.000 | 0.111 | 0.000 | 0.389 | 0.000 | 0.389 |
| 6.0-6.9 | 0.000 | 0.222 | 0.333 | 0.000 | 0.222 | 0.000 | 0.222 |

## ecg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1571)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.214 | 0.000 | 0.143 | 0.143 | 0.071 |
| 1.5-2.4 | 0.167 | 0.000 | 0.222 | 0.111 | 0.056 | 0.167 | 0.278 |
| 2.4-3.3 | 0.111 | 0.000 | 0.333 | 0.222 | 0.056 | 0.167 | 0.111 |
| 3.3-4.2 | 0.278 | 0.056 | 0.111 | 0.000 | 0.111 | 0.278 | 0.167 |
| 4.2-5.1 | 0.056 | 0.056 | 0.111 | 0.111 | 0.222 | 0.333 | 0.111 |
| 5.1-6.0 | 0.111 | 0.111 | 0.278 | 0.000 | 0.222 | 0.167 | 0.111 |
| 6.0-6.9 | 0.167 | 0.333 | 0.167 | 0.111 | 0.000 | 0.111 | 0.111 |

## ecg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.071 | 0.214 | 0.143 | 0.000 | 0.071 |
| 1.5-2.4 | 0.389 | 0.111 | 0.111 | 0.111 | 0.056 | 0.111 | 0.111 |
| 2.4-3.3 | 0.389 | 0.278 | 0.056 | 0.000 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.167 | 0.222 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 |
| 4.2-5.1 | 0.167 | 0.167 | 0.056 | 0.167 | 0.222 | 0.056 | 0.167 |
| 5.1-6.0 | 0.222 | 0.167 | 0.056 | 0.222 | 0.111 | 0.000 | 0.222 |
| 6.0-6.9 | 0.056 | 0.333 | 0.000 | 0.167 | 0.111 | 0.056 | 0.278 |

## ecg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/ecg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.357 | 0.000 | 0.071 | 0.429 | 0.071 | 0.071 |
| 1.5-2.4 | 0.111 | 0.056 | 0.056 | 0.222 | 0.500 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.333 | 0.056 | 0.111 | 0.278 | 0.111 | 0.056 |
| 3.3-4.2 | 0.000 | 0.278 | 0.000 | 0.111 | 0.389 | 0.111 | 0.111 |
| 4.2-5.1 | 0.000 | 0.167 | 0.000 | 0.222 | 0.500 | 0.056 | 0.056 |
| 5.1-6.0 | 0.056 | 0.222 | 0.167 | 0.000 | 0.389 | 0.056 | 0.111 |
| 6.0-6.9 | 0.000 | 0.333 | 0.000 | 0.000 | 0.444 | 0.167 | 0.056 |

## eeg | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.2549, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.1346, support=52
- `6.0-6.9`: recall=0.2500, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.081 | 0.216 | 0.162 | 0.000 | 0.108 | 0.189 |
| 1.5-2.4 | 0.259 | 0.111 | 0.148 | 0.204 | 0.056 | 0.074 | 0.148 |
| 2.4-3.3 | 0.235 | 0.059 | 0.255 | 0.098 | 0.039 | 0.176 | 0.137 |
| 3.3-4.2 | 0.132 | 0.057 | 0.094 | 0.189 | 0.075 | 0.226 | 0.226 |
| 4.2-5.1 | 0.176 | 0.059 | 0.078 | 0.235 | 0.098 | 0.176 | 0.176 |
| 5.1-6.0 | 0.135 | 0.019 | 0.038 | 0.231 | 0.096 | 0.135 | 0.346 |
| 6.0-6.9 | 0.192 | 0.096 | 0.154 | 0.135 | 0.058 | 0.115 | 0.250 |

## eeg | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1799)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.0755, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.3846, support=52
- `6.0-6.9`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.108 | 0.054 | 0.054 | 0.108 | 0.243 | 0.162 |
| 1.5-2.4 | 0.111 | 0.241 | 0.056 | 0.056 | 0.185 | 0.315 | 0.037 |
| 2.4-3.3 | 0.275 | 0.176 | 0.020 | 0.020 | 0.098 | 0.314 | 0.098 |
| 3.3-4.2 | 0.283 | 0.189 | 0.019 | 0.075 | 0.151 | 0.245 | 0.038 |
| 4.2-5.1 | 0.294 | 0.137 | 0.000 | 0.000 | 0.176 | 0.373 | 0.020 |
| 5.1-6.0 | 0.192 | 0.115 | 0.000 | 0.019 | 0.212 | 0.385 | 0.077 |
| 6.0-6.9 | 0.288 | 0.173 | 0.000 | 0.038 | 0.192 | 0.269 | 0.038 |

## eeg | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1759)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.3585, support=53
- `4.2-5.1`: recall=0.1373, support=51
- `5.1-6.0`: recall=0.0962, support=52
- `6.0-6.9`: recall=0.2500, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.027 | 0.135 | 0.189 | 0.027 | 0.108 | 0.270 |
| 1.5-2.4 | 0.222 | 0.037 | 0.130 | 0.278 | 0.074 | 0.093 | 0.167 |
| 2.4-3.3 | 0.157 | 0.000 | 0.157 | 0.216 | 0.098 | 0.176 | 0.196 |
| 3.3-4.2 | 0.113 | 0.000 | 0.057 | 0.358 | 0.094 | 0.151 | 0.226 |
| 4.2-5.1 | 0.137 | 0.000 | 0.098 | 0.275 | 0.137 | 0.235 | 0.118 |
| 5.1-6.0 | 0.115 | 0.019 | 0.019 | 0.250 | 0.077 | 0.096 | 0.423 |
| 6.0-6.9 | 0.192 | 0.077 | 0.154 | 0.173 | 0.058 | 0.096 | 0.250 |

## eeg | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1637)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.0943, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.4231, support=52
- `6.0-6.9`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.162 | 0.135 | 0.189 | 0.054 | 0.189 | 0.135 |
| 1.5-2.4 | 0.148 | 0.278 | 0.111 | 0.037 | 0.074 | 0.315 | 0.037 |
| 2.4-3.3 | 0.255 | 0.098 | 0.098 | 0.078 | 0.078 | 0.333 | 0.059 |
| 3.3-4.2 | 0.208 | 0.151 | 0.132 | 0.094 | 0.019 | 0.302 | 0.094 |
| 4.2-5.1 | 0.196 | 0.157 | 0.059 | 0.059 | 0.039 | 0.471 | 0.020 |
| 5.1-6.0 | 0.173 | 0.096 | 0.077 | 0.058 | 0.058 | 0.423 | 0.115 |
| 6.0-6.9 | 0.231 | 0.135 | 0.058 | 0.115 | 0.058 | 0.327 | 0.077 |

## eeg | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1626)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.4324, support=37
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.4151, support=53
- `4.2-5.1`: recall=0.0196, support=51
- `5.1-6.0`: recall=0.2500, support=52
- `6.0-6.9`: recall=0.0192, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.432 | 0.027 | 0.027 | 0.270 | 0.000 | 0.216 | 0.027 |
| 1.5-2.4 | 0.222 | 0.037 | 0.019 | 0.278 | 0.037 | 0.204 | 0.204 |
| 2.4-3.3 | 0.196 | 0.098 | 0.020 | 0.333 | 0.059 | 0.176 | 0.118 |
| 3.3-4.2 | 0.283 | 0.038 | 0.057 | 0.415 | 0.038 | 0.113 | 0.057 |
| 4.2-5.1 | 0.255 | 0.020 | 0.000 | 0.353 | 0.020 | 0.235 | 0.118 |
| 5.1-6.0 | 0.250 | 0.000 | 0.058 | 0.308 | 0.019 | 0.250 | 0.115 |
| 6.0-6.9 | 0.346 | 0.077 | 0.038 | 0.385 | 0.000 | 0.135 | 0.019 |

## eeg | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1580)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.3208, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.054 | 0.135 | 0.243 | 0.027 | 0.108 | 0.189 |
| 1.5-2.4 | 0.148 | 0.093 | 0.074 | 0.315 | 0.167 | 0.056 | 0.148 |
| 2.4-3.3 | 0.137 | 0.098 | 0.078 | 0.275 | 0.137 | 0.137 | 0.137 |
| 3.3-4.2 | 0.057 | 0.094 | 0.151 | 0.321 | 0.113 | 0.113 | 0.151 |
| 4.2-5.1 | 0.118 | 0.039 | 0.137 | 0.353 | 0.118 | 0.078 | 0.157 |
| 5.1-6.0 | 0.154 | 0.077 | 0.135 | 0.288 | 0.135 | 0.115 | 0.096 |
| 6.0-6.9 | 0.135 | 0.115 | 0.077 | 0.308 | 0.135 | 0.135 | 0.096 |

## eeg | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1380)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.0189, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.3269, support=52
- `6.0-6.9`: recall=0.0000, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.162 | 0.108 | 0.027 | 0.270 | 0.297 | 0.000 |
| 1.5-2.4 | 0.204 | 0.185 | 0.093 | 0.000 | 0.148 | 0.370 | 0.000 |
| 2.4-3.3 | 0.196 | 0.098 | 0.098 | 0.020 | 0.216 | 0.373 | 0.000 |
| 3.3-4.2 | 0.245 | 0.132 | 0.113 | 0.019 | 0.189 | 0.302 | 0.000 |
| 4.2-5.1 | 0.196 | 0.078 | 0.059 | 0.000 | 0.216 | 0.451 | 0.000 |
| 5.1-6.0 | 0.212 | 0.115 | 0.058 | 0.019 | 0.269 | 0.327 | 0.000 |
| 6.0-6.9 | 0.288 | 0.154 | 0.019 | 0.000 | 0.269 | 0.269 | 0.000 |

## eeg | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1327)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.3269, support=52
- `6.0-6.9`: recall=0.0000, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.054 | 0.108 | 0.162 | 0.135 | 0.243 | 0.027 |
| 1.5-2.4 | 0.296 | 0.037 | 0.056 | 0.333 | 0.074 | 0.185 | 0.019 |
| 2.4-3.3 | 0.333 | 0.020 | 0.078 | 0.176 | 0.137 | 0.235 | 0.020 |
| 3.3-4.2 | 0.302 | 0.019 | 0.132 | 0.132 | 0.132 | 0.226 | 0.057 |
| 4.2-5.1 | 0.275 | 0.000 | 0.196 | 0.078 | 0.118 | 0.333 | 0.000 |
| 5.1-6.0 | 0.192 | 0.038 | 0.192 | 0.096 | 0.115 | 0.327 | 0.038 |
| 6.0-6.9 | 0.308 | 0.077 | 0.077 | 0.192 | 0.115 | 0.231 | 0.000 |

## eeg | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.2242)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.7222, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.000 | 0.071 | 0.000 | 0.143 | 0.357 |
| 1.5-2.4 | 0.188 | 0.188 | 0.000 | 0.125 | 0.000 | 0.250 | 0.250 |
| 2.4-3.3 | 0.471 | 0.059 | 0.000 | 0.059 | 0.000 | 0.294 | 0.118 |
| 3.3-4.2 | 0.176 | 0.118 | 0.000 | 0.118 | 0.000 | 0.294 | 0.294 |
| 4.2-5.1 | 0.000 | 0.222 | 0.000 | 0.167 | 0.000 | 0.389 | 0.222 |
| 5.1-6.0 | 0.111 | 0.056 | 0.000 | 0.111 | 0.000 | 0.722 | 0.000 |
| 6.0-6.9 | 0.111 | 0.111 | 0.000 | 0.167 | 0.000 | 0.389 | 0.222 |

## eeg | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.2095)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.7222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.000 | 0.214 | 0.000 | 0.071 | 0.214 |
| 1.5-2.4 | 0.000 | 0.312 | 0.000 | 0.188 | 0.000 | 0.312 | 0.188 |
| 2.4-3.3 | 0.000 | 0.529 | 0.000 | 0.000 | 0.000 | 0.353 | 0.118 |
| 3.3-4.2 | 0.000 | 0.294 | 0.000 | 0.118 | 0.000 | 0.412 | 0.176 |
| 4.2-5.1 | 0.000 | 0.333 | 0.000 | 0.111 | 0.000 | 0.500 | 0.056 |
| 5.1-6.0 | 0.111 | 0.056 | 0.000 | 0.056 | 0.000 | 0.722 | 0.056 |
| 6.0-6.9 | 0.056 | 0.167 | 0.056 | 0.000 | 0.000 | 0.556 | 0.167 |

## eeg | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.2075)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.143 | 0.071 | 0.000 | 0.000 | 0.000 | 0.143 |
| 1.5-2.4 | 0.562 | 0.312 | 0.000 | 0.000 | 0.062 | 0.000 | 0.062 |
| 2.4-3.3 | 0.294 | 0.471 | 0.059 | 0.000 | 0.000 | 0.000 | 0.176 |
| 3.3-4.2 | 0.294 | 0.353 | 0.000 | 0.000 | 0.000 | 0.000 | 0.353 |
| 4.2-5.1 | 0.444 | 0.278 | 0.000 | 0.000 | 0.056 | 0.056 | 0.167 |
| 5.1-6.0 | 0.167 | 0.278 | 0.000 | 0.000 | 0.056 | 0.167 | 0.333 |
| 6.0-6.9 | 0.500 | 0.111 | 0.111 | 0.000 | 0.000 | 0.056 | 0.222 |

## eeg | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.4375, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.429 | 0.071 | 0.000 | 0.000 | 0.143 | 0.000 |
| 1.5-2.4 | 0.125 | 0.438 | 0.188 | 0.000 | 0.000 | 0.062 | 0.188 |
| 2.4-3.3 | 0.176 | 0.412 | 0.235 | 0.000 | 0.000 | 0.118 | 0.059 |
| 3.3-4.2 | 0.235 | 0.412 | 0.059 | 0.000 | 0.000 | 0.118 | 0.176 |
| 4.2-5.1 | 0.056 | 0.222 | 0.167 | 0.000 | 0.000 | 0.278 | 0.278 |
| 5.1-6.0 | 0.056 | 0.111 | 0.167 | 0.056 | 0.056 | 0.389 | 0.167 |
| 6.0-6.9 | 0.000 | 0.389 | 0.278 | 0.111 | 0.000 | 0.167 | 0.056 |

## eeg | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.2061)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.7222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.214 | 0.000 | 0.143 | 0.000 | 0.357 | 0.000 |
| 1.5-2.4 | 0.000 | 0.312 | 0.000 | 0.125 | 0.000 | 0.500 | 0.062 |
| 2.4-3.3 | 0.000 | 0.529 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 3.3-4.2 | 0.000 | 0.235 | 0.059 | 0.118 | 0.000 | 0.588 | 0.000 |
| 4.2-5.1 | 0.056 | 0.222 | 0.000 | 0.111 | 0.000 | 0.500 | 0.111 |
| 5.1-6.0 | 0.056 | 0.111 | 0.000 | 0.111 | 0.000 | 0.722 | 0.000 |
| 6.0-6.9 | 0.056 | 0.056 | 0.056 | 0.111 | 0.000 | 0.722 | 0.000 |

## eeg | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1845)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.4375, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.000 | 0.000 | 0.000 | 0.143 | 0.143 |
| 1.5-2.4 | 0.125 | 0.438 | 0.062 | 0.000 | 0.000 | 0.188 | 0.188 |
| 2.4-3.3 | 0.059 | 0.647 | 0.118 | 0.000 | 0.000 | 0.059 | 0.118 |
| 3.3-4.2 | 0.118 | 0.471 | 0.000 | 0.000 | 0.000 | 0.176 | 0.235 |
| 4.2-5.1 | 0.111 | 0.500 | 0.056 | 0.000 | 0.000 | 0.278 | 0.056 |
| 5.1-6.0 | 0.111 | 0.222 | 0.222 | 0.000 | 0.000 | 0.444 | 0.000 |
| 6.0-6.9 | 0.111 | 0.333 | 0.167 | 0.000 | 0.000 | 0.333 | 0.056 |

## eeg | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1756)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.000 | 0.000 | 0.071 | 0.000 | 0.143 |
| 1.5-2.4 | 0.312 | 0.312 | 0.062 | 0.000 | 0.125 | 0.188 | 0.000 |
| 2.4-3.3 | 0.235 | 0.529 | 0.059 | 0.000 | 0.059 | 0.118 | 0.000 |
| 3.3-4.2 | 0.294 | 0.353 | 0.059 | 0.000 | 0.059 | 0.176 | 0.059 |
| 4.2-5.1 | 0.500 | 0.222 | 0.000 | 0.000 | 0.111 | 0.167 | 0.000 |
| 5.1-6.0 | 0.333 | 0.111 | 0.056 | 0.000 | 0.111 | 0.278 | 0.111 |
| 6.0-6.9 | 0.611 | 0.167 | 0.000 | 0.000 | 0.056 | 0.167 | 0.000 |

## eeg | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1665)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.5000, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.571 | 0.071 | 0.000 | 0.000 | 0.143 | 0.071 |
| 1.5-2.4 | 0.062 | 0.500 | 0.000 | 0.000 | 0.000 | 0.188 | 0.250 |
| 2.4-3.3 | 0.000 | 0.706 | 0.059 | 0.000 | 0.000 | 0.118 | 0.118 |
| 3.3-4.2 | 0.059 | 0.647 | 0.000 | 0.000 | 0.000 | 0.059 | 0.235 |
| 4.2-5.1 | 0.000 | 0.556 | 0.056 | 0.000 | 0.000 | 0.111 | 0.278 |
| 5.1-6.0 | 0.000 | 0.444 | 0.111 | 0.000 | 0.000 | 0.278 | 0.167 |
| 6.0-6.9 | 0.000 | 0.500 | 0.111 | 0.000 | 0.000 | 0.167 | 0.222 |

## eeg | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.2929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.071 | 0.000 | 0.000 | 0.071 | 0.000 |
| 1.5-2.4 | 0.222 | 0.167 | 0.222 | 0.111 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.111 | 0.444 | 0.111 | 0.222 | 0.000 | 0.000 |
| 3.3-4.2 | 0.167 | 0.278 | 0.222 | 0.056 | 0.056 | 0.000 | 0.222 |
| 4.2-5.1 | 0.056 | 0.056 | 0.389 | 0.167 | 0.222 | 0.111 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.167 | 0.111 | 0.111 | 0.500 | 0.056 |
| 6.0-6.9 | 0.056 | 0.111 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 |

## eeg | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.2857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.000 | 0.000 | 0.000 | 0.214 | 0.071 |
| 1.5-2.4 | 0.222 | 0.111 | 0.222 | 0.111 | 0.111 | 0.222 | 0.000 |
| 2.4-3.3 | 0.056 | 0.000 | 0.278 | 0.111 | 0.222 | 0.333 | 0.000 |
| 3.3-4.2 | 0.167 | 0.222 | 0.111 | 0.167 | 0.111 | 0.056 | 0.167 |
| 4.2-5.1 | 0.056 | 0.167 | 0.056 | 0.111 | 0.278 | 0.167 | 0.167 |
| 5.1-6.0 | 0.056 | 0.167 | 0.056 | 0.000 | 0.111 | 0.556 | 0.056 |
| 6.0-6.9 | 0.167 | 0.111 | 0.000 | 0.111 | 0.111 | 0.333 | 0.167 |

## eeg | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.2786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.214 | 0.143 | 0.143 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.167 | 0.222 | 0.167 | 0.056 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.167 | 0.389 | 0.167 | 0.056 | 0.111 | 0.000 |
| 3.3-4.2 | 0.222 | 0.222 | 0.056 | 0.111 | 0.111 | 0.056 | 0.222 |
| 4.2-5.1 | 0.056 | 0.056 | 0.278 | 0.111 | 0.278 | 0.111 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.000 | 0.222 | 0.500 | 0.167 |
| 6.0-6.9 | 0.056 | 0.111 | 0.111 | 0.111 | 0.222 | 0.222 | 0.167 |

## eeg | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.6667, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.214 | 0.071 | 0.000 | 0.286 | 0.000 |
| 1.5-2.4 | 0.333 | 0.111 | 0.222 | 0.111 | 0.056 | 0.167 | 0.000 |
| 2.4-3.3 | 0.000 | 0.056 | 0.444 | 0.167 | 0.056 | 0.222 | 0.056 |
| 3.3-4.2 | 0.056 | 0.056 | 0.167 | 0.167 | 0.167 | 0.222 | 0.167 |
| 4.2-5.1 | 0.056 | 0.000 | 0.333 | 0.167 | 0.000 | 0.389 | 0.056 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.056 | 0.056 | 0.667 | 0.111 |
| 6.0-6.9 | 0.222 | 0.056 | 0.056 | 0.167 | 0.111 | 0.389 | 0.000 |

## eeg | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.5000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.000 | 0.071 | 0.143 | 0.000 | 0.143 | 0.214 |
| 1.5-2.4 | 0.278 | 0.000 | 0.389 | 0.167 | 0.000 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.056 | 0.500 | 0.222 | 0.111 | 0.056 | 0.000 |
| 3.3-4.2 | 0.111 | 0.000 | 0.389 | 0.111 | 0.167 | 0.111 | 0.111 |
| 4.2-5.1 | 0.111 | 0.000 | 0.333 | 0.222 | 0.167 | 0.167 | 0.000 |
| 5.1-6.0 | 0.167 | 0.000 | 0.167 | 0.111 | 0.333 | 0.167 | 0.056 |
| 6.0-6.9 | 0.167 | 0.056 | 0.222 | 0.111 | 0.056 | 0.111 | 0.278 |

## eeg | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.000 | 0.143 | 0.071 | 0.143 | 0.071 |
| 1.5-2.4 | 0.167 | 0.000 | 0.167 | 0.278 | 0.111 | 0.111 | 0.167 |
| 2.4-3.3 | 0.111 | 0.000 | 0.333 | 0.167 | 0.111 | 0.111 | 0.167 |
| 3.3-4.2 | 0.167 | 0.167 | 0.056 | 0.222 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.000 | 0.000 | 0.056 | 0.333 | 0.111 | 0.278 | 0.222 |
| 5.1-6.0 | 0.111 | 0.056 | 0.056 | 0.278 | 0.167 | 0.222 | 0.111 |
| 6.0-6.9 | 0.111 | 0.000 | 0.111 | 0.167 | 0.111 | 0.222 | 0.278 |

## eeg | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.5556, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.000 | 0.143 | 0.143 | 0.071 | 0.357 | 0.071 |
| 1.5-2.4 | 0.111 | 0.000 | 0.444 | 0.167 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.556 | 0.111 | 0.167 | 0.111 | 0.000 |
| 3.3-4.2 | 0.056 | 0.000 | 0.333 | 0.278 | 0.222 | 0.111 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.389 | 0.278 | 0.111 | 0.222 | 0.000 |
| 5.1-6.0 | 0.056 | 0.000 | 0.333 | 0.222 | 0.222 | 0.167 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.444 | 0.111 | 0.167 | 0.222 | 0.056 |

## eeg | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/eeg/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.5000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.000 | 0.143 | 0.000 | 0.286 | 0.071 | 0.071 |
| 1.5-2.4 | 0.111 | 0.000 | 0.500 | 0.056 | 0.167 | 0.000 | 0.167 |
| 2.4-3.3 | 0.222 | 0.000 | 0.500 | 0.000 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.167 | 0.000 | 0.500 | 0.000 | 0.167 | 0.111 | 0.056 |
| 4.2-5.1 | 0.111 | 0.000 | 0.389 | 0.111 | 0.278 | 0.000 | 0.111 |
| 5.1-6.0 | 0.167 | 0.000 | 0.278 | 0.000 | 0.333 | 0.000 | 0.222 |
| 6.0-6.9 | 0.167 | 0.000 | 0.389 | 0.000 | 0.278 | 0.056 | 0.111 |

## fused | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1563)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.1852, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.4906, support=53
- `6.0-6.9`: recall=0.2264, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.105 | 0.000 | 0.263 | 0.026 | 0.395 | 0.105 |
| 1.5-2.4 | 0.037 | 0.093 | 0.000 | 0.204 | 0.111 | 0.407 | 0.148 |
| 2.4-3.3 | 0.056 | 0.074 | 0.000 | 0.185 | 0.130 | 0.444 | 0.111 |
| 3.3-4.2 | 0.019 | 0.056 | 0.000 | 0.185 | 0.093 | 0.574 | 0.074 |
| 4.2-5.1 | 0.057 | 0.038 | 0.000 | 0.170 | 0.075 | 0.509 | 0.151 |
| 5.1-6.0 | 0.019 | 0.057 | 0.000 | 0.151 | 0.113 | 0.491 | 0.170 |
| 6.0-6.9 | 0.038 | 0.094 | 0.000 | 0.226 | 0.057 | 0.358 | 0.226 |

## fused | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1539)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2105, support=38
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.1852, support=54
- `4.2-5.1`: recall=0.2830, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.0566, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.211 | 0.079 | 0.026 | 0.158 | 0.263 | 0.158 | 0.105 |
| 1.5-2.4 | 0.074 | 0.056 | 0.093 | 0.241 | 0.204 | 0.222 | 0.111 |
| 2.4-3.3 | 0.056 | 0.093 | 0.056 | 0.167 | 0.296 | 0.185 | 0.148 |
| 3.3-4.2 | 0.074 | 0.000 | 0.056 | 0.185 | 0.259 | 0.315 | 0.111 |
| 4.2-5.1 | 0.075 | 0.057 | 0.038 | 0.226 | 0.283 | 0.245 | 0.075 |
| 5.1-6.0 | 0.132 | 0.075 | 0.057 | 0.189 | 0.208 | 0.208 | 0.132 |
| 6.0-6.9 | 0.170 | 0.132 | 0.019 | 0.208 | 0.113 | 0.302 | 0.057 |

## fused | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1526)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.026 | 0.000 | 0.000 | 0.026 | 0.789 | 0.105 |
| 1.5-2.4 | 0.056 | 0.000 | 0.019 | 0.037 | 0.019 | 0.852 | 0.019 |
| 2.4-3.3 | 0.037 | 0.000 | 0.000 | 0.056 | 0.019 | 0.815 | 0.074 |
| 3.3-4.2 | 0.019 | 0.000 | 0.000 | 0.093 | 0.000 | 0.870 | 0.019 |
| 4.2-5.1 | 0.019 | 0.019 | 0.000 | 0.038 | 0.057 | 0.849 | 0.019 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.075 | 0.000 | 0.887 | 0.038 |
| 6.0-6.9 | 0.075 | 0.000 | 0.000 | 0.057 | 0.000 | 0.868 | 0.000 |

## fused | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1515)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0189, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.079 | 0.000 | 0.000 | 0.000 | 0.026 | 0.789 | 0.105 |
| 1.5-2.4 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 | 0.870 | 0.019 |
| 2.4-3.3 | 0.037 | 0.000 | 0.000 | 0.074 | 0.000 | 0.815 | 0.074 |
| 3.3-4.2 | 0.019 | 0.000 | 0.000 | 0.093 | 0.000 | 0.870 | 0.019 |
| 4.2-5.1 | 0.038 | 0.000 | 0.000 | 0.075 | 0.019 | 0.849 | 0.019 |
| 5.1-6.0 | 0.019 | 0.000 | 0.000 | 0.057 | 0.000 | 0.887 | 0.038 |
| 6.0-6.9 | 0.075 | 0.000 | 0.000 | 0.057 | 0.000 | 0.868 | 0.000 |

## fused | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1473)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.4906, support=53
- `6.0-6.9`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.105 | 0.000 | 0.263 | 0.026 | 0.368 | 0.211 |
| 1.5-2.4 | 0.019 | 0.093 | 0.019 | 0.167 | 0.074 | 0.500 | 0.130 |
| 2.4-3.3 | 0.000 | 0.074 | 0.000 | 0.204 | 0.093 | 0.556 | 0.074 |
| 3.3-4.2 | 0.037 | 0.074 | 0.000 | 0.111 | 0.074 | 0.574 | 0.130 |
| 4.2-5.1 | 0.000 | 0.019 | 0.057 | 0.170 | 0.057 | 0.547 | 0.151 |
| 5.1-6.0 | 0.019 | 0.057 | 0.057 | 0.132 | 0.057 | 0.491 | 0.189 |
| 6.0-6.9 | 0.038 | 0.094 | 0.019 | 0.094 | 0.094 | 0.396 | 0.264 |

## fused | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=1.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=1.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1388)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0189, support=53
- `5.1-6.0`: recall=0.4528, support=53
- `6.0-6.9`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.184 | 0.026 | 0.211 | 0.000 | 0.368 | 0.158 |
| 1.5-2.4 | 0.000 | 0.130 | 0.037 | 0.148 | 0.037 | 0.519 | 0.130 |
| 2.4-3.3 | 0.019 | 0.111 | 0.000 | 0.185 | 0.019 | 0.611 | 0.056 |
| 3.3-4.2 | 0.019 | 0.111 | 0.000 | 0.111 | 0.019 | 0.611 | 0.130 |
| 4.2-5.1 | 0.019 | 0.094 | 0.000 | 0.151 | 0.019 | 0.585 | 0.132 |
| 5.1-6.0 | 0.000 | 0.245 | 0.000 | 0.113 | 0.038 | 0.453 | 0.151 |
| 6.0-6.9 | 0.075 | 0.189 | 0.000 | 0.094 | 0.000 | 0.377 | 0.264 |

## fused | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.529 | 0.471 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 |

## fused | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=1.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=1.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.000 | 0.000 | 0.214 | 0.286 |
| 1.5-2.4 | 0.111 | 0.056 | 0.333 | 0.000 | 0.000 | 0.389 | 0.111 |
| 2.4-3.3 | 0.056 | 0.278 | 0.111 | 0.000 | 0.000 | 0.389 | 0.167 |
| 3.3-4.2 | 0.235 | 0.235 | 0.000 | 0.000 | 0.000 | 0.412 | 0.118 |
| 4.2-5.1 | 0.389 | 0.000 | 0.111 | 0.000 | 0.000 | 0.444 | 0.056 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.389 | 0.111 |

## fused | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1349)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 1.5-2.4 | 0.000 | 0.444 | 0.000 | 0.056 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 3.3-4.2 | 0.000 | 0.529 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

## fused | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1224)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.071 | 0.000 | 0.000 | 0.214 | 0.286 |
| 1.5-2.4 | 0.278 | 0.000 | 0.167 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.167 | 0.278 | 0.056 | 0.000 | 0.000 | 0.167 | 0.333 |
| 3.3-4.2 | 0.294 | 0.176 | 0.000 | 0.000 | 0.059 | 0.294 | 0.176 |
| 4.2-5.1 | 0.111 | 0.056 | 0.333 | 0.000 | 0.000 | 0.389 | 0.111 |
| 5.1-6.0 | 0.389 | 0.056 | 0.056 | 0.000 | 0.111 | 0.222 | 0.167 |
| 6.0-6.9 | 0.444 | 0.000 | 0.056 | 0.000 | 0.167 | 0.111 | 0.222 |

## fused | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1179)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 1.5-2.4 | 0.222 | 0.111 | 0.167 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.111 | 0.389 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 3.3-4.2 | 0.176 | 0.353 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

## fused | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1156)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.000 | 0.071 | 0.071 | 0.357 | 0.071 |
| 1.5-2.4 | 0.111 | 0.111 | 0.222 | 0.056 | 0.000 | 0.444 | 0.056 |
| 2.4-3.3 | 0.111 | 0.389 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 |
| 3.3-4.2 | 0.294 | 0.235 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.111 | 0.278 | 0.111 |

## fused | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.143 | 0.286 | 0.143 | 0.000 | 0.000 |
| 1.5-2.4 | 0.111 | 0.333 | 0.222 | 0.111 | 0.111 | 0.000 | 0.111 |
| 2.4-3.3 | 0.056 | 0.167 | 0.111 | 0.111 | 0.333 | 0.056 | 0.167 |
| 3.3-4.2 | 0.056 | 0.111 | 0.167 | 0.278 | 0.167 | 0.056 | 0.167 |
| 4.2-5.1 | 0.235 | 0.235 | 0.118 | 0.118 | 0.118 | 0.000 | 0.176 |
| 5.1-6.0 | 0.167 | 0.111 | 0.111 | 0.056 | 0.333 | 0.000 | 0.222 |
| 6.0-6.9 | 0.222 | 0.167 | 0.167 | 0.111 | 0.222 | 0.000 | 0.111 |

## fused | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.3889, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.000 | 0.429 | 0.214 | 0.143 | 0.000 |
| 1.5-2.4 | 0.000 | 0.278 | 0.056 | 0.500 | 0.111 | 0.056 | 0.000 |
| 2.4-3.3 | 0.167 | 0.111 | 0.000 | 0.444 | 0.167 | 0.000 | 0.111 |
| 3.3-4.2 | 0.167 | 0.111 | 0.000 | 0.389 | 0.278 | 0.000 | 0.056 |
| 4.2-5.1 | 0.176 | 0.000 | 0.059 | 0.294 | 0.353 | 0.059 | 0.059 |
| 5.1-6.0 | 0.056 | 0.111 | 0.056 | 0.444 | 0.278 | 0.000 | 0.056 |
| 6.0-6.9 | 0.111 | 0.111 | 0.056 | 0.389 | 0.278 | 0.056 | 0.000 |

## fused | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4706, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.214 | 0.143 | 0.000 | 0.429 | 0.000 | 0.000 |
| 1.5-2.4 | 0.167 | 0.278 | 0.389 | 0.000 | 0.167 | 0.000 | 0.000 |
| 2.4-3.3 | 0.278 | 0.222 | 0.167 | 0.000 | 0.333 | 0.000 | 0.000 |
| 3.3-4.2 | 0.222 | 0.222 | 0.222 | 0.000 | 0.333 | 0.000 | 0.000 |
| 4.2-5.1 | 0.235 | 0.176 | 0.118 | 0.000 | 0.471 | 0.000 | 0.000 |
| 5.1-6.0 | 0.278 | 0.111 | 0.222 | 0.000 | 0.333 | 0.000 | 0.056 |
| 6.0-6.9 | 0.222 | 0.111 | 0.167 | 0.000 | 0.444 | 0.000 | 0.056 |

## fused | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.143 | 0.214 | 0.143 | 0.000 |
| 1.5-2.4 | 0.056 | 0.333 | 0.111 | 0.222 | 0.056 | 0.167 | 0.056 |
| 2.4-3.3 | 0.167 | 0.167 | 0.111 | 0.222 | 0.111 | 0.167 | 0.056 |
| 3.3-4.2 | 0.167 | 0.167 | 0.167 | 0.111 | 0.167 | 0.222 | 0.000 |
| 4.2-5.1 | 0.412 | 0.176 | 0.000 | 0.000 | 0.176 | 0.176 | 0.059 |
| 5.1-6.0 | 0.167 | 0.111 | 0.056 | 0.111 | 0.333 | 0.111 | 0.111 |
| 6.0-6.9 | 0.278 | 0.111 | 0.111 | 0.000 | 0.278 | 0.167 | 0.056 |

## fused | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.1643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.429 | 0.143 | 0.000 | 0.071 | 0.071 |
| 1.5-2.4 | 0.167 | 0.222 | 0.444 | 0.056 | 0.000 | 0.000 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.444 | 0.167 | 0.000 | 0.111 | 0.111 |
| 3.3-4.2 | 0.111 | 0.111 | 0.389 | 0.167 | 0.056 | 0.111 | 0.056 |
| 4.2-5.1 | 0.118 | 0.000 | 0.471 | 0.118 | 0.059 | 0.118 | 0.118 |
| 5.1-6.0 | 0.111 | 0.000 | 0.444 | 0.167 | 0.000 | 0.056 | 0.222 |
| 6.0-6.9 | 0.056 | 0.000 | 0.667 | 0.111 | 0.000 | 0.111 | 0.056 |

## fused | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.3333, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.071 | 0.143 | 0.214 | 0.286 | 0.143 | 0.000 |
| 1.5-2.4 | 0.000 | 0.111 | 0.056 | 0.389 | 0.222 | 0.167 | 0.056 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.222 | 0.333 | 0.167 | 0.000 |
| 3.3-4.2 | 0.056 | 0.000 | 0.111 | 0.333 | 0.222 | 0.222 | 0.056 |
| 4.2-5.1 | 0.118 | 0.000 | 0.118 | 0.235 | 0.176 | 0.294 | 0.059 |
| 5.1-6.0 | 0.056 | 0.056 | 0.111 | 0.278 | 0.333 | 0.056 | 0.111 |
| 6.0-6.9 | 0.111 | 0.056 | 0.167 | 0.167 | 0.278 | 0.222 | 0.000 |

## fused | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.8889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.000 | 0.056 | 0.000 | 0.056 |
| 4.2-5.1 | 0.000 | 0.941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.059 |
| 5.1-6.0 | 0.000 | 0.889 | 0.000 | 0.000 | 0.056 | 0.000 | 0.056 |
| 6.0-6.9 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |

## fused | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/fused/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.8889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.000 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.000 | 0.944 | 0.000 | 0.056 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.000 | 0.111 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.059 |
| 5.1-6.0 | 0.000 | 0.889 | 0.056 | 0.056 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.944 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 |

## pupil | group_holdout | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1622)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2632, support=38
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.2037, support=54
- `4.2-5.1`: recall=0.2075, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.1132, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.263 | 0.000 | 0.053 | 0.263 | 0.263 | 0.132 | 0.026 |
| 1.5-2.4 | 0.111 | 0.056 | 0.019 | 0.222 | 0.259 | 0.222 | 0.111 |
| 2.4-3.3 | 0.093 | 0.074 | 0.093 | 0.222 | 0.241 | 0.259 | 0.019 |
| 3.3-4.2 | 0.093 | 0.019 | 0.074 | 0.204 | 0.278 | 0.278 | 0.056 |
| 4.2-5.1 | 0.132 | 0.075 | 0.132 | 0.245 | 0.208 | 0.208 | 0.000 |
| 5.1-6.0 | 0.151 | 0.132 | 0.094 | 0.170 | 0.189 | 0.208 | 0.057 |
| 6.0-6.9 | 0.226 | 0.094 | 0.075 | 0.170 | 0.094 | 0.226 | 0.113 |

## pupil | group_holdout | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1496)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.5849, support=53
- `5.1-6.0`: recall=0.3585, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.026 | 0.000 | 0.026 | 0.447 | 0.368 | 0.105 |
| 1.5-2.4 | 0.037 | 0.019 | 0.000 | 0.019 | 0.574 | 0.333 | 0.019 |
| 2.4-3.3 | 0.037 | 0.019 | 0.019 | 0.019 | 0.500 | 0.333 | 0.074 |
| 3.3-4.2 | 0.037 | 0.019 | 0.000 | 0.056 | 0.556 | 0.315 | 0.019 |
| 4.2-5.1 | 0.000 | 0.038 | 0.000 | 0.019 | 0.585 | 0.340 | 0.019 |
| 5.1-6.0 | 0.000 | 0.019 | 0.019 | 0.000 | 0.566 | 0.358 | 0.038 |
| 6.0-6.9 | 0.057 | 0.000 | 0.019 | 0.038 | 0.566 | 0.321 | 0.000 |

## pupil | group_holdout | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1481)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.4717, support=53
- `6.0-6.9`: recall=0.1132, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.132 | 0.026 | 0.263 | 0.000 | 0.368 | 0.105 |
| 1.5-2.4 | 0.074 | 0.111 | 0.000 | 0.185 | 0.037 | 0.537 | 0.056 |
| 2.4-3.3 | 0.074 | 0.074 | 0.074 | 0.204 | 0.019 | 0.537 | 0.019 |
| 3.3-4.2 | 0.056 | 0.093 | 0.019 | 0.222 | 0.000 | 0.556 | 0.056 |
| 4.2-5.1 | 0.019 | 0.038 | 0.094 | 0.208 | 0.000 | 0.528 | 0.113 |
| 5.1-6.0 | 0.094 | 0.075 | 0.057 | 0.189 | 0.000 | 0.472 | 0.113 |
| 6.0-6.9 | 0.113 | 0.113 | 0.075 | 0.151 | 0.000 | 0.434 | 0.113 |

## pupil | group_holdout | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=1.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | group_holdout | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=1.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | group_holdout | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1427)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.3519, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.5472, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.026 | 0.000 | 0.395 | 0.026 | 0.421 | 0.079 |
| 1.5-2.4 | 0.056 | 0.000 | 0.000 | 0.352 | 0.037 | 0.537 | 0.019 |
| 2.4-3.3 | 0.037 | 0.000 | 0.000 | 0.389 | 0.019 | 0.481 | 0.074 |
| 3.3-4.2 | 0.019 | 0.019 | 0.037 | 0.352 | 0.000 | 0.556 | 0.019 |
| 4.2-5.1 | 0.019 | 0.019 | 0.000 | 0.377 | 0.057 | 0.509 | 0.019 |
| 5.1-6.0 | 0.000 | 0.019 | 0.038 | 0.358 | 0.019 | 0.547 | 0.019 |
| 6.0-6.9 | 0.057 | 0.019 | 0.019 | 0.340 | 0.000 | 0.566 | 0.000 |

## pupil | group_holdout | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1267)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.4528, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.184 | 0.000 | 0.211 | 0.053 | 0.368 | 0.132 |
| 1.5-2.4 | 0.000 | 0.093 | 0.019 | 0.148 | 0.037 | 0.556 | 0.148 |
| 2.4-3.3 | 0.019 | 0.093 | 0.019 | 0.185 | 0.037 | 0.593 | 0.056 |
| 3.3-4.2 | 0.019 | 0.093 | 0.000 | 0.111 | 0.056 | 0.593 | 0.130 |
| 4.2-5.1 | 0.019 | 0.113 | 0.000 | 0.151 | 0.038 | 0.604 | 0.075 |
| 5.1-6.0 | 0.019 | 0.208 | 0.000 | 0.113 | 0.075 | 0.453 | 0.132 |
| 6.0-6.9 | 0.113 | 0.113 | 0.019 | 0.094 | 0.057 | 0.434 | 0.170 |

## pupil | group_holdout | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.1132)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/group_holdout/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2105, support=38
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.1296, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.4151, support=53
- `6.0-6.9`: recall=0.0943, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.211 | 0.079 | 0.026 | 0.211 | 0.000 | 0.368 | 0.105 |
| 1.5-2.4 | 0.148 | 0.037 | 0.056 | 0.204 | 0.056 | 0.463 | 0.037 |
| 2.4-3.3 | 0.093 | 0.130 | 0.019 | 0.222 | 0.037 | 0.481 | 0.019 |
| 3.3-4.2 | 0.111 | 0.148 | 0.019 | 0.130 | 0.056 | 0.481 | 0.056 |
| 4.2-5.1 | 0.075 | 0.170 | 0.000 | 0.226 | 0.000 | 0.472 | 0.057 |
| 5.1-6.0 | 0.170 | 0.189 | 0.019 | 0.113 | 0.038 | 0.415 | 0.057 |
| 6.0-6.9 | 0.170 | 0.151 | 0.019 | 0.132 | 0.038 | 0.396 | 0.094 |

## pupil | loso | cnn1d | none [cnn1d+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=1.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.056 | 0.944 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |

## pupil | loso | cnn1d_deep | none [cnn1d_deep+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.000 | 0.500 | 0.000 | 0.056 | 0.000 | 0.000 | 0.444 |
| 2.4-3.3 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.000 | 0.471 | 0.000 | 0.000 | 0.000 | 0.000 | 0.529 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |
| 6.0-6.9 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

## pupil | loso | transformer | none [transformer+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=1.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | transformer_xl | none [transformer_xl+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=1.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | lstm1d | none [lstm1d+none] (splits=2, balanced_accuracy_mean=0.1338)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.143 | 0.000 | 0.000 | 0.286 | 0.214 |
| 1.5-2.4 | 0.000 | 0.111 | 0.333 | 0.056 | 0.000 | 0.444 | 0.056 |
| 2.4-3.3 | 0.111 | 0.333 | 0.056 | 0.000 | 0.000 | 0.389 | 0.111 |
| 3.3-4.2 | 0.176 | 0.294 | 0.000 | 0.000 | 0.000 | 0.412 | 0.118 |
| 4.2-5.1 | 0.278 | 0.000 | 0.222 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 |

## pupil | loso | bigru1d | none [bigru1d+none] (splits=2, balanced_accuracy_mean=0.1224)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.000 | 0.071 | 0.000 | 0.357 | 0.071 |
| 1.5-2.4 | 0.333 | 0.000 | 0.167 | 0.056 | 0.000 | 0.444 | 0.000 |
| 2.4-3.3 | 0.278 | 0.222 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 3.3-4.2 | 0.353 | 0.176 | 0.000 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

## pupil | loso | gru1d | none [gru1d+none] (splits=2, balanced_accuracy_mean=0.1179)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.000 | 0.000 | 0.214 | 0.286 |
| 1.5-2.4 | 0.222 | 0.111 | 0.167 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.167 | 0.333 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |
| 3.3-4.2 | 0.176 | 0.353 | 0.000 | 0.000 | 0.000 | 0.294 | 0.176 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.389 | 0.111 |
| 5.1-6.0 | 0.444 | 0.056 | 0.000 | 0.000 | 0.056 | 0.278 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.111 | 0.167 | 0.222 |

## pupil | loso | bilstm1d | none [bilstm1d+none] (splits=2, balanced_accuracy_mean=0.0986)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/loso/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.000 | 0.071 | 0.071 | 0.143 | 0.286 |
| 1.5-2.4 | 0.333 | 0.000 | 0.000 | 0.056 | 0.111 | 0.111 | 0.389 |
| 2.4-3.3 | 0.389 | 0.111 | 0.000 | 0.000 | 0.000 | 0.278 | 0.222 |
| 3.3-4.2 | 0.412 | 0.118 | 0.000 | 0.000 | 0.000 | 0.353 | 0.118 |
| 4.2-5.1 | 0.444 | 0.000 | 0.000 | 0.000 | 0.056 | 0.389 | 0.111 |
| 5.1-6.0 | 0.389 | 0.111 | 0.000 | 0.000 | 0.111 | 0.222 | 0.167 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.000 | 0.167 | 0.278 | 0.056 |

## pupil | within_participant | lstm1d | none [lstm1d+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/lstm1d_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4706, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.214 | 0.071 | 0.000 | 0.429 | 0.000 | 0.000 |
| 1.5-2.4 | 0.167 | 0.333 | 0.333 | 0.000 | 0.167 | 0.000 | 0.000 |
| 2.4-3.3 | 0.278 | 0.222 | 0.167 | 0.000 | 0.333 | 0.000 | 0.000 |
| 3.3-4.2 | 0.278 | 0.222 | 0.167 | 0.000 | 0.333 | 0.000 | 0.000 |
| 4.2-5.1 | 0.235 | 0.235 | 0.000 | 0.000 | 0.471 | 0.059 | 0.000 |
| 5.1-6.0 | 0.333 | 0.111 | 0.167 | 0.000 | 0.333 | 0.000 | 0.056 |
| 6.0-6.9 | 0.278 | 0.167 | 0.056 | 0.000 | 0.444 | 0.000 | 0.056 |

## pupil | within_participant | bigru1d | none [bigru1d+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/bigru1d_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.214 | 0.143 | 0.214 | 0.143 | 0.000 |
| 1.5-2.4 | 0.056 | 0.333 | 0.167 | 0.167 | 0.056 | 0.111 | 0.111 |
| 2.4-3.3 | 0.111 | 0.111 | 0.222 | 0.167 | 0.167 | 0.167 | 0.056 |
| 3.3-4.2 | 0.111 | 0.167 | 0.167 | 0.111 | 0.222 | 0.222 | 0.000 |
| 4.2-5.1 | 0.294 | 0.235 | 0.059 | 0.000 | 0.235 | 0.118 | 0.059 |
| 5.1-6.0 | 0.167 | 0.111 | 0.056 | 0.111 | 0.333 | 0.056 | 0.167 |
| 6.0-6.9 | 0.222 | 0.111 | 0.167 | 0.000 | 0.278 | 0.167 | 0.056 |

## pupil | within_participant | gru1d | none [gru1d+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/gru1d_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.3889, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.000 | 0.429 | 0.214 | 0.143 | 0.000 |
| 1.5-2.4 | 0.000 | 0.278 | 0.056 | 0.500 | 0.111 | 0.056 | 0.000 |
| 2.4-3.3 | 0.167 | 0.111 | 0.000 | 0.444 | 0.167 | 0.000 | 0.111 |
| 3.3-4.2 | 0.167 | 0.111 | 0.000 | 0.389 | 0.278 | 0.000 | 0.056 |
| 4.2-5.1 | 0.176 | 0.000 | 0.000 | 0.353 | 0.353 | 0.059 | 0.059 |
| 5.1-6.0 | 0.056 | 0.111 | 0.056 | 0.444 | 0.278 | 0.000 | 0.056 |
| 6.0-6.9 | 0.111 | 0.111 | 0.056 | 0.389 | 0.278 | 0.056 | 0.000 |

## pupil | within_participant | bilstm1d | none [bilstm1d+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/bilstm1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.143 | 0.286 | 0.286 | 0.000 | 0.000 |
| 1.5-2.4 | 0.056 | 0.389 | 0.167 | 0.222 | 0.111 | 0.000 | 0.056 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.167 | 0.389 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.167 | 0.167 | 0.278 | 0.222 | 0.000 | 0.111 |
| 4.2-5.1 | 0.294 | 0.235 | 0.118 | 0.118 | 0.118 | 0.000 | 0.118 |
| 5.1-6.0 | 0.278 | 0.167 | 0.056 | 0.056 | 0.333 | 0.000 | 0.111 |
| 6.0-6.9 | 0.111 | 0.222 | 0.167 | 0.167 | 0.222 | 0.000 | 0.111 |

## pupil | within_participant | cnn1d | none [cnn1d+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/cnn1d_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.7778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.071 | 0.714 | 0.000 | 0.000 | 0.071 | 0.000 |
| 1.5-2.4 | 0.000 | 0.167 | 0.556 | 0.167 | 0.056 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.778 | 0.056 | 0.000 | 0.056 | 0.056 |
| 3.3-4.2 | 0.056 | 0.000 | 0.611 | 0.167 | 0.000 | 0.111 | 0.056 |
| 4.2-5.1 | 0.118 | 0.000 | 0.647 | 0.000 | 0.000 | 0.118 | 0.118 |
| 5.1-6.0 | 0.056 | 0.000 | 0.778 | 0.000 | 0.000 | 0.000 | 0.167 |
| 6.0-6.9 | 0.111 | 0.056 | 0.611 | 0.111 | 0.000 | 0.111 | 0.000 |

## pupil | within_participant | cnn1d_deep | none [cnn1d_deep+none] (splits=10, balanced_accuracy_mean=0.1357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/cnn1d_deep_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.071 | 0.071 | 0.000 | 0.429 | 0.143 | 0.000 |
| 1.5-2.4 | 0.111 | 0.111 | 0.111 | 0.111 | 0.444 | 0.111 | 0.000 |
| 2.4-3.3 | 0.111 | 0.056 | 0.000 | 0.056 | 0.500 | 0.222 | 0.056 |
| 3.3-4.2 | 0.167 | 0.000 | 0.000 | 0.167 | 0.389 | 0.222 | 0.056 |
| 4.2-5.1 | 0.235 | 0.059 | 0.000 | 0.000 | 0.294 | 0.294 | 0.118 |
| 5.1-6.0 | 0.167 | 0.000 | 0.056 | 0.000 | 0.500 | 0.111 | 0.167 |
| 6.0-6.9 | 0.167 | 0.111 | 0.000 | 0.056 | 0.389 | 0.222 | 0.056 |

## pupil | within_participant | transformer_xl | none [transformer_xl+none] (splits=10, balanced_accuracy_mean=0.1357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/transformer_xl_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.8889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.056 | 0.889 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.889 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 |
| 4.2-5.1 | 0.000 | 0.941 | 0.000 | 0.000 | 0.000 | 0.059 | 0.000 |
| 5.1-6.0 | 0.000 | 0.889 | 0.000 | 0.056 | 0.056 | 0.000 | 0.000 |
| 6.0-6.9 | 0.056 | 0.889 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | within_participant | transformer | none [transformer+none] (splits=10, balanced_accuracy_mean=0.1286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline_advanced_nn/pupil/within_participant/transformer_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.8889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.056 | 0.889 | 0.000 | 0.000 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.000 | 0.889 | 0.000 | 0.000 | 0.000 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.889 | 0.056 | 0.000 | 0.000 | 0.000 | 0.056 |
| 4.2-5.1 | 0.000 | 0.941 | 0.000 | 0.000 | 0.000 | 0.059 | 0.000 |
| 5.1-6.0 | 0.000 | 0.889 | 0.111 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.056 | 0.889 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 |


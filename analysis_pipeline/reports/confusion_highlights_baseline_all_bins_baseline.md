# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_all_bins_baseline.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1678)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.2963, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.2075, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.108 | 0.135 | 0.189 | 0.297 | 0.000 | 0.027 | 0.108 |
| 0.6-1.5 | 0.057 | 0.189 | 0.208 | 0.094 | 0.226 | 0.113 | 0.019 | 0.094 |
| 1.5-2.4 | 0.056 | 0.167 | 0.296 | 0.093 | 0.185 | 0.037 | 0.056 | 0.111 |
| 2.4-3.3 | 0.098 | 0.059 | 0.314 | 0.157 | 0.196 | 0.078 | 0.020 | 0.078 |
| 3.3-4.2 | 0.057 | 0.094 | 0.189 | 0.132 | 0.208 | 0.113 | 0.094 | 0.113 |
| 4.2-5.1 | 0.039 | 0.098 | 0.176 | 0.176 | 0.157 | 0.059 | 0.078 | 0.216 |
| 5.1-6.0 | 0.096 | 0.077 | 0.154 | 0.154 | 0.212 | 0.038 | 0.058 | 0.212 |
| 6.0-6.9 | 0.077 | 0.038 | 0.154 | 0.154 | 0.192 | 0.096 | 0.019 | 0.269 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1567)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.0943, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.2745, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.054 | 0.054 | 0.162 | 0.189 | 0.135 | 0.027 | 0.108 |
| 0.6-1.5 | 0.208 | 0.094 | 0.208 | 0.075 | 0.075 | 0.170 | 0.075 | 0.094 |
| 1.5-2.4 | 0.222 | 0.148 | 0.111 | 0.204 | 0.056 | 0.093 | 0.093 | 0.074 |
| 2.4-3.3 | 0.255 | 0.000 | 0.216 | 0.157 | 0.137 | 0.137 | 0.078 | 0.020 |
| 3.3-4.2 | 0.189 | 0.000 | 0.208 | 0.132 | 0.132 | 0.245 | 0.094 | 0.000 |
| 4.2-5.1 | 0.216 | 0.020 | 0.118 | 0.078 | 0.157 | 0.275 | 0.078 | 0.059 |
| 5.1-6.0 | 0.346 | 0.115 | 0.077 | 0.135 | 0.038 | 0.192 | 0.058 | 0.038 |
| 6.0-6.9 | 0.250 | 0.077 | 0.115 | 0.077 | 0.115 | 0.250 | 0.038 | 0.077 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.1154, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.135 | 0.135 | 0.162 | 0.081 | 0.027 | 0.000 | 0.297 |
| 0.6-1.5 | 0.113 | 0.226 | 0.132 | 0.057 | 0.151 | 0.132 | 0.075 | 0.113 |
| 1.5-2.4 | 0.167 | 0.167 | 0.074 | 0.093 | 0.148 | 0.093 | 0.148 | 0.111 |
| 2.4-3.3 | 0.216 | 0.118 | 0.118 | 0.118 | 0.118 | 0.078 | 0.137 | 0.098 |
| 3.3-4.2 | 0.151 | 0.075 | 0.057 | 0.151 | 0.170 | 0.094 | 0.226 | 0.075 |
| 4.2-5.1 | 0.196 | 0.157 | 0.059 | 0.059 | 0.078 | 0.216 | 0.157 | 0.078 |
| 5.1-6.0 | 0.212 | 0.135 | 0.038 | 0.096 | 0.154 | 0.096 | 0.115 | 0.154 |
| 6.0-6.9 | 0.115 | 0.173 | 0.096 | 0.096 | 0.135 | 0.096 | 0.173 | 0.115 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1414)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.0962, support=52
- `6.0-6.9`: recall=0.2115, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.162 | 0.081 | 0.135 | 0.162 | 0.108 | 0.081 | 0.162 |
| 0.6-1.5 | 0.113 | 0.208 | 0.075 | 0.075 | 0.151 | 0.189 | 0.075 | 0.113 |
| 1.5-2.4 | 0.167 | 0.111 | 0.056 | 0.074 | 0.148 | 0.111 | 0.185 | 0.148 |
| 2.4-3.3 | 0.196 | 0.137 | 0.176 | 0.098 | 0.157 | 0.078 | 0.118 | 0.039 |
| 3.3-4.2 | 0.151 | 0.075 | 0.057 | 0.094 | 0.189 | 0.132 | 0.226 | 0.075 |
| 4.2-5.1 | 0.137 | 0.216 | 0.078 | 0.059 | 0.118 | 0.098 | 0.176 | 0.118 |
| 5.1-6.0 | 0.154 | 0.096 | 0.154 | 0.058 | 0.154 | 0.135 | 0.096 | 0.154 |
| 6.0-6.9 | 0.019 | 0.173 | 0.077 | 0.077 | 0.212 | 0.096 | 0.135 | 0.212 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1370)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `0.6-1.5`: recall=0.0755, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.3333, support=51
- `5.1-6.0`: recall=0.0385, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.189 | 0.081 | 0.108 | 0.081 | 0.000 | 0.135 | 0.000 | 0.405 |
| 0.6-1.5 | 0.245 | 0.075 | 0.113 | 0.151 | 0.019 | 0.245 | 0.038 | 0.113 |
| 1.5-2.4 | 0.222 | 0.093 | 0.093 | 0.130 | 0.000 | 0.185 | 0.056 | 0.222 |
| 2.4-3.3 | 0.216 | 0.078 | 0.098 | 0.118 | 0.039 | 0.196 | 0.020 | 0.235 |
| 3.3-4.2 | 0.170 | 0.075 | 0.132 | 0.151 | 0.038 | 0.245 | 0.019 | 0.170 |
| 4.2-5.1 | 0.196 | 0.078 | 0.137 | 0.078 | 0.000 | 0.333 | 0.020 | 0.157 |
| 5.1-6.0 | 0.212 | 0.096 | 0.115 | 0.077 | 0.038 | 0.308 | 0.038 | 0.115 |
| 6.0-6.9 | 0.135 | 0.000 | 0.115 | 0.135 | 0.058 | 0.308 | 0.058 | 0.192 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1366)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `0.6-1.5`: recall=0.1509, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.0192, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.189 | 0.108 | 0.027 | 0.162 | 0.189 | 0.081 | 0.054 | 0.189 |
| 0.6-1.5 | 0.094 | 0.151 | 0.151 | 0.038 | 0.113 | 0.208 | 0.113 | 0.132 |
| 1.5-2.4 | 0.185 | 0.185 | 0.093 | 0.037 | 0.093 | 0.074 | 0.185 | 0.148 |
| 2.4-3.3 | 0.176 | 0.098 | 0.020 | 0.137 | 0.118 | 0.157 | 0.137 | 0.157 |
| 3.3-4.2 | 0.151 | 0.075 | 0.094 | 0.075 | 0.151 | 0.226 | 0.132 | 0.094 |
| 4.2-5.1 | 0.118 | 0.098 | 0.039 | 0.118 | 0.176 | 0.176 | 0.157 | 0.118 |
| 5.1-6.0 | 0.231 | 0.154 | 0.038 | 0.077 | 0.115 | 0.115 | 0.173 | 0.096 |
| 6.0-6.9 | 0.077 | 0.115 | 0.115 | 0.192 | 0.173 | 0.192 | 0.115 | 0.019 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1152)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.0189, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.1132, support=53
- `4.2-5.1`: recall=0.2941, support=51
- `5.1-6.0`: recall=0.0769, support=52
- `6.0-6.9`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.027 | 0.162 | 0.135 | 0.054 | 0.135 | 0.000 | 0.270 |
| 0.6-1.5 | 0.245 | 0.019 | 0.170 | 0.057 | 0.094 | 0.208 | 0.094 | 0.113 |
| 1.5-2.4 | 0.259 | 0.037 | 0.074 | 0.167 | 0.074 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.216 | 0.039 | 0.137 | 0.059 | 0.118 | 0.196 | 0.078 | 0.157 |
| 3.3-4.2 | 0.132 | 0.000 | 0.132 | 0.113 | 0.113 | 0.264 | 0.094 | 0.151 |
| 4.2-5.1 | 0.118 | 0.020 | 0.078 | 0.118 | 0.118 | 0.294 | 0.059 | 0.196 |
| 5.1-6.0 | 0.231 | 0.077 | 0.058 | 0.135 | 0.115 | 0.250 | 0.077 | 0.058 |
| 6.0-6.9 | 0.192 | 0.019 | 0.115 | 0.096 | 0.115 | 0.250 | 0.077 | 0.135 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1885)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.000 | 0.071 | 0.000 | 0.000 | 0.286 | 0.000 | 0.000 |
| 0.6-1.5 | 0.812 | 0.000 | 0.062 | 0.000 | 0.000 | 0.125 | 0.000 | 0.000 |
| 1.5-2.4 | 0.312 | 0.062 | 0.188 | 0.125 | 0.000 | 0.312 | 0.000 | 0.000 |
| 2.4-3.3 | 0.235 | 0.000 | 0.294 | 0.059 | 0.000 | 0.412 | 0.000 | 0.000 |
| 3.3-4.2 | 0.353 | 0.000 | 0.235 | 0.176 | 0.000 | 0.235 | 0.000 | 0.000 |
| 4.2-5.1 | 0.333 | 0.000 | 0.000 | 0.056 | 0.000 | 0.611 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.000 | 0.056 | 0.167 | 0.000 | 0.167 | 0.000 | 0.111 |
| 6.0-6.9 | 0.278 | 0.056 | 0.222 | 0.056 | 0.000 | 0.389 | 0.000 | 0.000 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1693)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5556, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.214 | 0.143 | 0.000 | 0.143 | 0.000 | 0.000 |
| 0.6-1.5 | 0.562 | 0.000 | 0.250 | 0.062 | 0.062 | 0.000 | 0.000 | 0.062 |
| 1.5-2.4 | 0.312 | 0.000 | 0.188 | 0.312 | 0.000 | 0.000 | 0.125 | 0.062 |
| 2.4-3.3 | 0.294 | 0.000 | 0.235 | 0.176 | 0.000 | 0.235 | 0.059 | 0.000 |
| 3.3-4.2 | 0.176 | 0.059 | 0.176 | 0.294 | 0.000 | 0.294 | 0.000 | 0.000 |
| 4.2-5.1 | 0.111 | 0.000 | 0.056 | 0.278 | 0.000 | 0.556 | 0.000 | 0.000 |
| 5.1-6.0 | 0.333 | 0.000 | 0.056 | 0.222 | 0.056 | 0.222 | 0.000 | 0.111 |
| 6.0-6.9 | 0.389 | 0.000 | 0.278 | 0.056 | 0.056 | 0.167 | 0.056 | 0.000 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1465)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.286 | 0.143 | 0.000 | 0.071 | 0.000 | 0.214 |
| 0.6-1.5 | 0.312 | 0.125 | 0.125 | 0.188 | 0.125 | 0.000 | 0.000 | 0.125 |
| 1.5-2.4 | 0.250 | 0.125 | 0.125 | 0.188 | 0.000 | 0.188 | 0.062 | 0.062 |
| 2.4-3.3 | 0.294 | 0.118 | 0.059 | 0.235 | 0.059 | 0.059 | 0.059 | 0.118 |
| 3.3-4.2 | 0.176 | 0.059 | 0.118 | 0.176 | 0.000 | 0.118 | 0.235 | 0.118 |
| 4.2-5.1 | 0.056 | 0.000 | 0.111 | 0.444 | 0.000 | 0.222 | 0.111 | 0.056 |
| 5.1-6.0 | 0.222 | 0.111 | 0.167 | 0.167 | 0.111 | 0.000 | 0.111 | 0.111 |
| 6.0-6.9 | 0.222 | 0.056 | 0.167 | 0.222 | 0.056 | 0.056 | 0.056 | 0.167 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1395)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.214 | 0.071 | 0.143 | 0.143 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.125 | 0.125 | 0.188 | 0.062 | 0.062 | 0.000 | 0.312 | 0.125 |
| 1.5-2.4 | 0.188 | 0.250 | 0.125 | 0.312 | 0.000 | 0.062 | 0.062 | 0.000 |
| 2.4-3.3 | 0.235 | 0.000 | 0.118 | 0.294 | 0.118 | 0.059 | 0.118 | 0.059 |
| 3.3-4.2 | 0.294 | 0.000 | 0.176 | 0.235 | 0.000 | 0.000 | 0.059 | 0.235 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.278 | 0.111 | 0.167 | 0.167 | 0.167 |
| 5.1-6.0 | 0.167 | 0.222 | 0.000 | 0.111 | 0.167 | 0.111 | 0.167 | 0.056 |
| 6.0-6.9 | 0.167 | 0.167 | 0.111 | 0.278 | 0.056 | 0.000 | 0.222 | 0.000 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1338)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2500, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.143 | 0.071 | 0.071 | 0.143 | 0.143 | 0.071 |
| 0.6-1.5 | 0.188 | 0.250 | 0.062 | 0.062 | 0.000 | 0.062 | 0.250 | 0.125 |
| 1.5-2.4 | 0.188 | 0.125 | 0.000 | 0.312 | 0.188 | 0.125 | 0.000 | 0.062 |
| 2.4-3.3 | 0.059 | 0.000 | 0.118 | 0.118 | 0.059 | 0.235 | 0.176 | 0.235 |
| 3.3-4.2 | 0.059 | 0.000 | 0.235 | 0.235 | 0.000 | 0.059 | 0.176 | 0.235 |
| 4.2-5.1 | 0.000 | 0.056 | 0.056 | 0.278 | 0.167 | 0.333 | 0.056 | 0.056 |
| 5.1-6.0 | 0.056 | 0.111 | 0.167 | 0.000 | 0.111 | 0.278 | 0.222 | 0.056 |
| 6.0-6.9 | 0.222 | 0.222 | 0.056 | 0.111 | 0.111 | 0.222 | 0.056 | 0.000 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1226)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.214 | 0.071 | 0.000 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.250 | 0.062 | 0.125 | 0.000 | 0.125 | 0.062 | 0.375 | 0.000 |
| 1.5-2.4 | 0.500 | 0.312 | 0.062 | 0.062 | 0.000 | 0.062 | 0.000 | 0.000 |
| 2.4-3.3 | 0.294 | 0.118 | 0.118 | 0.176 | 0.000 | 0.118 | 0.059 | 0.118 |
| 3.3-4.2 | 0.294 | 0.000 | 0.235 | 0.118 | 0.000 | 0.176 | 0.118 | 0.059 |
| 4.2-5.1 | 0.389 | 0.000 | 0.000 | 0.222 | 0.000 | 0.056 | 0.167 | 0.167 |
| 5.1-6.0 | 0.333 | 0.056 | 0.111 | 0.111 | 0.000 | 0.167 | 0.167 | 0.056 |
| 6.0-6.9 | 0.389 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 | 0.000 | 0.000 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1200)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.000 | 0.071 | 0.500 | 0.071 | 0.071 | 0.071 | 0.143 |
| 0.6-1.5 | 0.000 | 0.000 | 0.062 | 0.562 | 0.125 | 0.188 | 0.000 | 0.062 |
| 1.5-2.4 | 0.125 | 0.000 | 0.062 | 0.562 | 0.000 | 0.000 | 0.062 | 0.188 |
| 2.4-3.3 | 0.118 | 0.059 | 0.059 | 0.471 | 0.118 | 0.059 | 0.000 | 0.118 |
| 3.3-4.2 | 0.118 | 0.000 | 0.176 | 0.412 | 0.000 | 0.059 | 0.118 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.056 | 0.611 | 0.000 | 0.111 | 0.000 | 0.167 |
| 5.1-6.0 | 0.111 | 0.111 | 0.111 | 0.278 | 0.167 | 0.167 | 0.056 | 0.000 |
| 6.0-6.9 | 0.222 | 0.056 | 0.111 | 0.278 | 0.000 | 0.167 | 0.000 | 0.167 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2125)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.071 | 0.071 | 0.071 | 0.071 | 0.214 | 0.143 | 0.071 |
| 0.6-1.5 | 0.000 | 0.278 | 0.111 | 0.167 | 0.000 | 0.056 | 0.278 | 0.111 |
| 1.5-2.4 | 0.278 | 0.111 | 0.111 | 0.222 | 0.056 | 0.000 | 0.056 | 0.167 |
| 2.4-3.3 | 0.167 | 0.278 | 0.111 | 0.056 | 0.000 | 0.167 | 0.111 | 0.111 |
| 3.3-4.2 | 0.111 | 0.222 | 0.111 | 0.056 | 0.167 | 0.111 | 0.167 | 0.056 |
| 4.2-5.1 | 0.167 | 0.056 | 0.111 | 0.167 | 0.056 | 0.222 | 0.167 | 0.056 |
| 5.1-6.0 | 0.056 | 0.222 | 0.000 | 0.167 | 0.056 | 0.167 | 0.333 | 0.000 |
| 6.0-6.9 | 0.056 | 0.167 | 0.167 | 0.222 | 0.000 | 0.111 | 0.000 | 0.278 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2062)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.071 | 0.214 | 0.143 | 0.000 | 0.286 | 0.000 | 0.071 |
| 0.6-1.5 | 0.056 | 0.333 | 0.222 | 0.056 | 0.167 | 0.000 | 0.111 | 0.056 |
| 1.5-2.4 | 0.278 | 0.111 | 0.000 | 0.222 | 0.000 | 0.056 | 0.167 | 0.167 |
| 2.4-3.3 | 0.111 | 0.056 | 0.111 | 0.167 | 0.111 | 0.167 | 0.056 | 0.222 |
| 3.3-4.2 | 0.056 | 0.056 | 0.111 | 0.222 | 0.167 | 0.167 | 0.222 | 0.000 |
| 4.2-5.1 | 0.056 | 0.000 | 0.056 | 0.167 | 0.056 | 0.389 | 0.222 | 0.056 |
| 5.1-6.0 | 0.000 | 0.167 | 0.056 | 0.222 | 0.167 | 0.167 | 0.222 | 0.000 |
| 6.0-6.9 | 0.000 | 0.222 | 0.278 | 0.167 | 0.056 | 0.000 | 0.111 | 0.167 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.1938)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.357 | 0.000 | 0.000 | 0.143 | 0.143 | 0.000 |
| 0.6-1.5 | 0.000 | 0.333 | 0.111 | 0.111 | 0.111 | 0.000 | 0.167 | 0.167 |
| 1.5-2.4 | 0.111 | 0.222 | 0.167 | 0.111 | 0.056 | 0.000 | 0.111 | 0.222 |
| 2.4-3.3 | 0.056 | 0.222 | 0.167 | 0.000 | 0.056 | 0.167 | 0.278 | 0.056 |
| 3.3-4.2 | 0.111 | 0.333 | 0.056 | 0.056 | 0.111 | 0.167 | 0.167 | 0.000 |
| 4.2-5.1 | 0.111 | 0.111 | 0.167 | 0.111 | 0.000 | 0.333 | 0.000 | 0.167 |
| 5.1-6.0 | 0.056 | 0.222 | 0.222 | 0.111 | 0.167 | 0.056 | 0.167 | 0.000 |
| 6.0-6.9 | 0.056 | 0.167 | 0.222 | 0.167 | 0.111 | 0.111 | 0.000 | 0.167 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.1938)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.429 | 0.143 | 0.071 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.222 | 0.389 | 0.000 | 0.056 | 0.167 | 0.000 | 0.111 | 0.056 |
| 1.5-2.4 | 0.333 | 0.111 | 0.056 | 0.111 | 0.167 | 0.056 | 0.056 | 0.111 |
| 2.4-3.3 | 0.222 | 0.111 | 0.111 | 0.111 | 0.111 | 0.056 | 0.056 | 0.222 |
| 3.3-4.2 | 0.056 | 0.222 | 0.056 | 0.111 | 0.111 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.111 | 0.111 | 0.056 | 0.056 | 0.056 | 0.333 | 0.222 | 0.056 |
| 5.1-6.0 | 0.000 | 0.111 | 0.000 | 0.167 | 0.111 | 0.222 | 0.222 | 0.167 |
| 6.0-6.9 | 0.056 | 0.167 | 0.222 | 0.167 | 0.056 | 0.056 | 0.000 | 0.278 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.1875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.071 | 0.214 | 0.000 | 0.071 | 0.143 | 0.071 | 0.143 |
| 0.6-1.5 | 0.111 | 0.056 | 0.167 | 0.222 | 0.111 | 0.111 | 0.167 | 0.056 |
| 1.5-2.4 | 0.111 | 0.167 | 0.278 | 0.111 | 0.000 | 0.000 | 0.111 | 0.222 |
| 2.4-3.3 | 0.111 | 0.111 | 0.222 | 0.167 | 0.056 | 0.167 | 0.000 | 0.167 |
| 3.3-4.2 | 0.167 | 0.111 | 0.222 | 0.000 | 0.222 | 0.167 | 0.056 | 0.056 |
| 4.2-5.1 | 0.056 | 0.111 | 0.222 | 0.056 | 0.167 | 0.222 | 0.111 | 0.056 |
| 5.1-6.0 | 0.056 | 0.167 | 0.056 | 0.167 | 0.389 | 0.111 | 0.000 | 0.056 |
| 6.0-6.9 | 0.056 | 0.111 | 0.167 | 0.111 | 0.111 | 0.111 | 0.111 | 0.222 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.1875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.357 | 0.000 | 0.000 | 0.286 | 0.000 | 0.071 |
| 0.6-1.5 | 0.111 | 0.333 | 0.056 | 0.222 | 0.056 | 0.056 | 0.111 | 0.056 |
| 1.5-2.4 | 0.056 | 0.111 | 0.056 | 0.333 | 0.111 | 0.000 | 0.056 | 0.278 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.056 | 0.111 | 0.222 | 0.167 | 0.167 |
| 3.3-4.2 | 0.056 | 0.111 | 0.111 | 0.222 | 0.167 | 0.167 | 0.167 | 0.000 |
| 4.2-5.1 | 0.056 | 0.056 | 0.167 | 0.222 | 0.167 | 0.278 | 0.056 | 0.000 |
| 5.1-6.0 | 0.056 | 0.111 | 0.111 | 0.333 | 0.056 | 0.167 | 0.167 | 0.000 |
| 6.0-6.9 | 0.000 | 0.111 | 0.222 | 0.278 | 0.000 | 0.111 | 0.000 | 0.278 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.1812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/ecg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.357 | 0.000 | 0.000 | 0.143 | 0.143 | 0.000 |
| 0.6-1.5 | 0.167 | 0.278 | 0.000 | 0.167 | 0.222 | 0.056 | 0.056 | 0.056 |
| 1.5-2.4 | 0.167 | 0.111 | 0.111 | 0.000 | 0.111 | 0.167 | 0.111 | 0.222 |
| 2.4-3.3 | 0.167 | 0.167 | 0.056 | 0.056 | 0.111 | 0.056 | 0.222 | 0.167 |
| 3.3-4.2 | 0.111 | 0.167 | 0.111 | 0.056 | 0.222 | 0.056 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.056 | 0.000 | 0.278 | 0.111 | 0.222 | 0.167 | 0.111 |
| 5.1-6.0 | 0.111 | 0.111 | 0.056 | 0.111 | 0.278 | 0.167 | 0.111 | 0.056 |
| 6.0-6.9 | 0.000 | 0.111 | 0.222 | 0.222 | 0.056 | 0.167 | 0.000 | 0.222 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1777)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.2642, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0784, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.135 | 0.027 | 0.135 | 0.135 | 0.081 | 0.108 | 0.216 |
| 0.6-1.5 | 0.075 | 0.264 | 0.170 | 0.151 | 0.094 | 0.057 | 0.075 | 0.113 |
| 1.5-2.4 | 0.093 | 0.315 | 0.093 | 0.130 | 0.130 | 0.019 | 0.111 | 0.111 |
| 2.4-3.3 | 0.059 | 0.098 | 0.098 | 0.137 | 0.294 | 0.020 | 0.118 | 0.176 |
| 3.3-4.2 | 0.038 | 0.075 | 0.075 | 0.151 | 0.264 | 0.132 | 0.094 | 0.170 |
| 4.2-5.1 | 0.020 | 0.039 | 0.039 | 0.157 | 0.255 | 0.078 | 0.157 | 0.255 |
| 5.1-6.0 | 0.019 | 0.077 | 0.058 | 0.135 | 0.192 | 0.038 | 0.154 | 0.327 |
| 6.0-6.9 | 0.038 | 0.019 | 0.058 | 0.154 | 0.250 | 0.077 | 0.135 | 0.269 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1771)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.3019, support=53
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.0943, support=53
- `4.2-5.1`: recall=0.1373, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.3654, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.054 | 0.027 | 0.108 | 0.081 | 0.054 | 0.135 | 0.270 |
| 0.6-1.5 | 0.208 | 0.302 | 0.094 | 0.113 | 0.019 | 0.113 | 0.019 | 0.132 |
| 1.5-2.4 | 0.167 | 0.315 | 0.056 | 0.074 | 0.056 | 0.111 | 0.056 | 0.167 |
| 2.4-3.3 | 0.196 | 0.098 | 0.078 | 0.020 | 0.118 | 0.196 | 0.020 | 0.275 |
| 3.3-4.2 | 0.132 | 0.151 | 0.019 | 0.057 | 0.094 | 0.170 | 0.151 | 0.226 |
| 4.2-5.1 | 0.216 | 0.059 | 0.059 | 0.039 | 0.098 | 0.137 | 0.137 | 0.255 |
| 5.1-6.0 | 0.154 | 0.096 | 0.019 | 0.038 | 0.115 | 0.173 | 0.115 | 0.288 |
| 6.0-6.9 | 0.135 | 0.077 | 0.019 | 0.019 | 0.058 | 0.135 | 0.192 | 0.365 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1531)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.7358, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.108 | 0.000 | 0.027 | 0.730 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.075 | 0.057 | 0.019 | 0.075 | 0.623 | 0.094 | 0.057 | 0.000 |
| 1.5-2.4 | 0.000 | 0.037 | 0.000 | 0.074 | 0.815 | 0.056 | 0.019 | 0.000 |
| 2.4-3.3 | 0.078 | 0.059 | 0.000 | 0.020 | 0.765 | 0.059 | 0.020 | 0.000 |
| 3.3-4.2 | 0.057 | 0.019 | 0.019 | 0.057 | 0.736 | 0.038 | 0.038 | 0.038 |
| 4.2-5.1 | 0.059 | 0.000 | 0.000 | 0.000 | 0.784 | 0.039 | 0.118 | 0.000 |
| 5.1-6.0 | 0.019 | 0.019 | 0.000 | 0.038 | 0.731 | 0.038 | 0.154 | 0.000 |
| 6.0-6.9 | 0.058 | 0.019 | 0.019 | 0.019 | 0.788 | 0.038 | 0.019 | 0.038 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1522)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `0.6-1.5`: recall=0.2453, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.054 | 0.189 | 0.135 | 0.216 | 0.162 | 0.027 | 0.027 | 0.189 |
| 0.6-1.5 | 0.170 | 0.245 | 0.170 | 0.113 | 0.151 | 0.094 | 0.019 | 0.038 |
| 1.5-2.4 | 0.093 | 0.241 | 0.148 | 0.093 | 0.093 | 0.167 | 0.037 | 0.130 |
| 2.4-3.3 | 0.118 | 0.216 | 0.098 | 0.176 | 0.176 | 0.059 | 0.078 | 0.078 |
| 3.3-4.2 | 0.113 | 0.151 | 0.132 | 0.208 | 0.170 | 0.094 | 0.019 | 0.113 |
| 4.2-5.1 | 0.157 | 0.137 | 0.137 | 0.098 | 0.216 | 0.098 | 0.039 | 0.118 |
| 5.1-6.0 | 0.077 | 0.173 | 0.115 | 0.115 | 0.135 | 0.135 | 0.058 | 0.192 |
| 6.0-6.9 | 0.115 | 0.135 | 0.173 | 0.115 | 0.192 | 0.096 | 0.038 | 0.135 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1519)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.2075, support=53
- `4.2-5.1`: recall=0.0196, support=51
- `5.1-6.0`: recall=0.2308, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.162 | 0.000 | 0.000 | 0.189 | 0.000 | 0.243 | 0.189 |
| 0.6-1.5 | 0.170 | 0.226 | 0.151 | 0.000 | 0.170 | 0.019 | 0.057 | 0.208 |
| 1.5-2.4 | 0.130 | 0.259 | 0.074 | 0.019 | 0.222 | 0.056 | 0.093 | 0.148 |
| 2.4-3.3 | 0.059 | 0.059 | 0.157 | 0.020 | 0.157 | 0.059 | 0.255 | 0.235 |
| 3.3-4.2 | 0.075 | 0.094 | 0.094 | 0.019 | 0.208 | 0.057 | 0.264 | 0.189 |
| 4.2-5.1 | 0.059 | 0.020 | 0.078 | 0.000 | 0.275 | 0.020 | 0.373 | 0.176 |
| 5.1-6.0 | 0.038 | 0.115 | 0.058 | 0.019 | 0.231 | 0.096 | 0.231 | 0.212 |
| 6.0-6.9 | 0.077 | 0.173 | 0.077 | 0.000 | 0.250 | 0.000 | 0.231 | 0.192 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1475)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `0.6-1.5`: recall=0.1509, support=53
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.3208, support=53
- `4.2-5.1`: recall=0.0196, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.135 | 0.027 | 0.054 | 0.243 | 0.000 | 0.108 | 0.135 |
| 0.6-1.5 | 0.453 | 0.151 | 0.057 | 0.094 | 0.132 | 0.038 | 0.019 | 0.057 |
| 1.5-2.4 | 0.315 | 0.167 | 0.019 | 0.093 | 0.185 | 0.056 | 0.074 | 0.093 |
| 2.4-3.3 | 0.294 | 0.059 | 0.078 | 0.039 | 0.255 | 0.059 | 0.157 | 0.059 |
| 3.3-4.2 | 0.245 | 0.075 | 0.057 | 0.019 | 0.321 | 0.057 | 0.170 | 0.057 |
| 4.2-5.1 | 0.255 | 0.020 | 0.078 | 0.020 | 0.392 | 0.020 | 0.118 | 0.098 |
| 5.1-6.0 | 0.250 | 0.058 | 0.058 | 0.019 | 0.269 | 0.019 | 0.154 | 0.173 |
| 6.0-6.9 | 0.269 | 0.077 | 0.058 | 0.058 | 0.288 | 0.019 | 0.077 | 0.154 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `0.6-1.5`: recall=0.0943, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.1569, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.189 | 0.108 | 0.108 | 0.135 | 0.216 | 0.081 | 0.027 | 0.135 |
| 0.6-1.5 | 0.264 | 0.094 | 0.038 | 0.170 | 0.226 | 0.094 | 0.038 | 0.075 |
| 1.5-2.4 | 0.185 | 0.130 | 0.037 | 0.093 | 0.222 | 0.111 | 0.056 | 0.167 |
| 2.4-3.3 | 0.176 | 0.098 | 0.059 | 0.118 | 0.314 | 0.098 | 0.000 | 0.137 |
| 3.3-4.2 | 0.132 | 0.094 | 0.057 | 0.170 | 0.245 | 0.094 | 0.075 | 0.132 |
| 4.2-5.1 | 0.157 | 0.039 | 0.059 | 0.157 | 0.255 | 0.157 | 0.039 | 0.137 |
| 5.1-6.0 | 0.135 | 0.058 | 0.096 | 0.192 | 0.135 | 0.269 | 0.058 | 0.058 |
| 6.0-6.9 | 0.154 | 0.077 | 0.096 | 0.154 | 0.154 | 0.115 | 0.058 | 0.192 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2428)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `0.6-1.5`: recall=0.2500, support=16
- `1.5-2.4`: recall=0.5000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.714 | 0.000 | 0.143 | 0.071 | 0.000 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.062 | 0.250 | 0.562 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.125 | 0.062 | 0.500 | 0.188 | 0.062 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.000 | 0.059 | 0.353 | 0.118 | 0.235 | 0.000 | 0.000 | 0.235 |
| 3.3-4.2 | 0.118 | 0.000 | 0.235 | 0.412 | 0.118 | 0.000 | 0.059 | 0.059 |
| 4.2-5.1 | 0.000 | 0.056 | 0.222 | 0.278 | 0.278 | 0.000 | 0.000 | 0.167 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.389 | 0.167 | 0.056 | 0.056 | 0.167 |
| 6.0-6.9 | 0.000 | 0.056 | 0.222 | 0.333 | 0.111 | 0.056 | 0.000 | 0.222 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2212)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.8750, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.500 | 0.214 | 0.071 | 0.071 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.875 | 0.062 | 0.062 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.562 | 0.188 | 0.062 | 0.000 | 0.062 | 0.125 | 0.000 |
| 2.4-3.3 | 0.000 | 0.647 | 0.000 | 0.118 | 0.000 | 0.000 | 0.235 | 0.000 |
| 3.3-4.2 | 0.059 | 0.353 | 0.118 | 0.176 | 0.059 | 0.000 | 0.235 | 0.000 |
| 4.2-5.1 | 0.000 | 0.500 | 0.222 | 0.000 | 0.056 | 0.000 | 0.222 | 0.000 |
| 5.1-6.0 | 0.000 | 0.111 | 0.222 | 0.111 | 0.167 | 0.000 | 0.389 | 0.000 |
| 6.0-6.9 | 0.000 | 0.500 | 0.111 | 0.111 | 0.000 | 0.000 | 0.278 | 0.000 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1999)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.3750, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.3529, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.071 | 0.143 | 0.214 | 0.071 | 0.143 | 0.071 |
| 0.6-1.5 | 0.000 | 0.375 | 0.188 | 0.312 | 0.125 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.125 | 0.125 | 0.250 | 0.188 | 0.000 | 0.188 | 0.062 | 0.062 |
| 2.4-3.3 | 0.059 | 0.176 | 0.059 | 0.353 | 0.235 | 0.059 | 0.059 | 0.000 |
| 3.3-4.2 | 0.059 | 0.059 | 0.000 | 0.176 | 0.176 | 0.176 | 0.294 | 0.059 |
| 4.2-5.1 | 0.000 | 0.222 | 0.222 | 0.222 | 0.167 | 0.111 | 0.056 | 0.000 |
| 5.1-6.0 | 0.056 | 0.000 | 0.333 | 0.056 | 0.056 | 0.167 | 0.056 | 0.278 |
| 6.0-6.9 | 0.111 | 0.167 | 0.167 | 0.222 | 0.000 | 0.056 | 0.167 | 0.111 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1962)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.5625, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.214 | 0.000 | 0.214 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.562 | 0.375 | 0.000 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.438 | 0.312 | 0.062 | 0.000 | 0.062 | 0.062 | 0.000 |
| 2.4-3.3 | 0.059 | 0.235 | 0.471 | 0.000 | 0.118 | 0.000 | 0.118 | 0.000 |
| 3.3-4.2 | 0.059 | 0.412 | 0.235 | 0.059 | 0.118 | 0.000 | 0.059 | 0.059 |
| 4.2-5.1 | 0.056 | 0.222 | 0.222 | 0.056 | 0.333 | 0.000 | 0.111 | 0.000 |
| 5.1-6.0 | 0.000 | 0.278 | 0.167 | 0.000 | 0.389 | 0.000 | 0.056 | 0.111 |
| 6.0-6.9 | 0.000 | 0.444 | 0.111 | 0.056 | 0.278 | 0.000 | 0.056 | 0.056 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1952)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.1875, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.500 | 0.000 | 0.000 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.188 | 0.438 | 0.250 | 0.125 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.125 | 0.188 | 0.312 | 0.188 | 0.000 | 0.062 | 0.062 | 0.062 |
| 2.4-3.3 | 0.000 | 0.059 | 0.412 | 0.176 | 0.235 | 0.059 | 0.000 | 0.059 |
| 3.3-4.2 | 0.118 | 0.059 | 0.412 | 0.235 | 0.118 | 0.059 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.111 | 0.389 | 0.056 | 0.111 | 0.222 | 0.000 | 0.111 |
| 5.1-6.0 | 0.000 | 0.000 | 0.167 | 0.111 | 0.333 | 0.222 | 0.111 | 0.056 |
| 6.0-6.9 | 0.000 | 0.222 | 0.444 | 0.056 | 0.000 | 0.111 | 0.056 | 0.111 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1894)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.4706, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.643 | 0.000 | 0.000 | 0.286 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.750 | 0.000 | 0.188 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.562 | 0.062 | 0.062 | 0.312 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.647 | 0.000 | 0.176 | 0.176 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.529 | 0.000 | 0.000 | 0.471 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.389 | 0.000 | 0.056 | 0.556 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.056 | 0.833 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.444 | 0.000 | 0.056 | 0.500 | 0.000 | 0.000 | 0.000 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1885)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.6250, support=16
- `1.5-2.4`: recall=0.4375, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.071 | 0.143 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.000 | 0.625 | 0.312 | 0.062 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.188 | 0.438 | 0.000 | 0.188 | 0.000 | 0.000 | 0.125 |
| 2.4-3.3 | 0.000 | 0.176 | 0.294 | 0.059 | 0.118 | 0.000 | 0.118 | 0.235 |
| 3.3-4.2 | 0.059 | 0.294 | 0.235 | 0.118 | 0.000 | 0.000 | 0.235 | 0.059 |
| 4.2-5.1 | 0.000 | 0.389 | 0.056 | 0.056 | 0.278 | 0.000 | 0.111 | 0.111 |
| 5.1-6.0 | 0.000 | 0.111 | 0.111 | 0.278 | 0.333 | 0.000 | 0.111 | 0.056 |
| 6.0-6.9 | 0.000 | 0.389 | 0.111 | 0.167 | 0.167 | 0.000 | 0.111 | 0.056 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3312)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.6667, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.143 | 0.000 | 0.071 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.000 | 0.667 | 0.056 | 0.000 | 0.000 | 0.056 | 0.000 | 0.222 |
| 1.5-2.4 | 0.111 | 0.222 | 0.000 | 0.222 | 0.167 | 0.167 | 0.111 | 0.000 |
| 2.4-3.3 | 0.056 | 0.000 | 0.444 | 0.278 | 0.056 | 0.056 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.000 | 0.278 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 |
| 4.2-5.1 | 0.000 | 0.167 | 0.111 | 0.111 | 0.111 | 0.111 | 0.278 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.056 | 0.000 | 0.111 | 0.556 | 0.111 |
| 6.0-6.9 | 0.000 | 0.111 | 0.111 | 0.056 | 0.056 | 0.167 | 0.222 | 0.278 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3125)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.071 | 0.000 | 0.000 | 0.071 | 0.143 | 0.000 |
| 0.6-1.5 | 0.000 | 0.611 | 0.056 | 0.111 | 0.000 | 0.111 | 0.000 | 0.111 |
| 1.5-2.4 | 0.111 | 0.167 | 0.167 | 0.167 | 0.111 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.056 | 0.222 | 0.333 | 0.167 | 0.111 | 0.056 | 0.000 |
| 3.3-4.2 | 0.167 | 0.222 | 0.111 | 0.111 | 0.111 | 0.056 | 0.111 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.167 | 0.056 | 0.056 | 0.167 | 0.333 | 0.056 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.056 | 0.000 | 0.222 | 0.556 | 0.111 |
| 6.0-6.9 | 0.000 | 0.167 | 0.056 | 0.056 | 0.056 | 0.222 | 0.278 | 0.167 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3063)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.143 | 0.000 | 0.143 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.000 | 0.556 | 0.111 | 0.056 | 0.000 | 0.056 | 0.000 | 0.222 |
| 1.5-2.4 | 0.111 | 0.167 | 0.056 | 0.222 | 0.167 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.278 | 0.389 | 0.167 | 0.000 | 0.111 | 0.000 |
| 3.3-4.2 | 0.111 | 0.056 | 0.167 | 0.056 | 0.167 | 0.111 | 0.056 | 0.278 |
| 4.2-5.1 | 0.056 | 0.056 | 0.111 | 0.111 | 0.056 | 0.167 | 0.222 | 0.222 |
| 5.1-6.0 | 0.000 | 0.000 | 0.167 | 0.056 | 0.111 | 0.111 | 0.389 | 0.167 |
| 6.0-6.9 | 0.111 | 0.056 | 0.056 | 0.056 | 0.111 | 0.167 | 0.222 | 0.222 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3063)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.214 | 0.000 | 0.071 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.056 | 0.500 | 0.111 | 0.000 | 0.000 | 0.167 | 0.000 | 0.167 |
| 1.5-2.4 | 0.111 | 0.111 | 0.000 | 0.222 | 0.222 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.278 | 0.333 | 0.167 | 0.056 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.222 | 0.056 | 0.167 | 0.222 | 0.056 | 0.111 |
| 4.2-5.1 | 0.000 | 0.056 | 0.111 | 0.056 | 0.111 | 0.333 | 0.222 | 0.111 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.111 | 0.056 | 0.111 | 0.556 | 0.167 |
| 6.0-6.9 | 0.056 | 0.111 | 0.056 | 0.056 | 0.111 | 0.222 | 0.222 | 0.167 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.286 | 0.000 | 0.071 | 0.071 | 0.071 | 0.000 |
| 0.6-1.5 | 0.056 | 0.389 | 0.111 | 0.222 | 0.056 | 0.056 | 0.000 | 0.111 |
| 1.5-2.4 | 0.167 | 0.167 | 0.111 | 0.222 | 0.000 | 0.167 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.167 | 0.389 | 0.056 | 0.111 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.167 | 0.167 | 0.167 | 0.056 | 0.111 | 0.167 |
| 4.2-5.1 | 0.056 | 0.111 | 0.111 | 0.111 | 0.111 | 0.111 | 0.389 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.056 | 0.000 | 0.111 | 0.611 | 0.167 |
| 6.0-6.9 | 0.111 | 0.111 | 0.111 | 0.000 | 0.167 | 0.167 | 0.167 | 0.167 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2375)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.071 | 0.214 | 0.214 | 0.143 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.444 | 0.111 | 0.000 | 0.056 | 0.167 | 0.000 | 0.222 |
| 1.5-2.4 | 0.000 | 0.167 | 0.056 | 0.389 | 0.056 | 0.167 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.333 | 0.111 | 0.167 | 0.056 | 0.056 |
| 3.3-4.2 | 0.000 | 0.222 | 0.167 | 0.167 | 0.111 | 0.167 | 0.056 | 0.111 |
| 4.2-5.1 | 0.000 | 0.056 | 0.056 | 0.222 | 0.111 | 0.111 | 0.333 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.111 | 0.000 | 0.000 | 0.611 | 0.167 |
| 6.0-6.9 | 0.000 | 0.167 | 0.056 | 0.056 | 0.167 | 0.278 | 0.222 | 0.056 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.1875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.000 | 0.000 | 0.071 | 0.143 | 0.214 | 0.000 |
| 0.6-1.5 | 0.167 | 0.333 | 0.111 | 0.056 | 0.000 | 0.278 | 0.000 | 0.056 |
| 1.5-2.4 | 0.056 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.056 | 0.056 |
| 2.4-3.3 | 0.111 | 0.111 | 0.111 | 0.222 | 0.111 | 0.333 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.111 | 0.222 | 0.167 | 0.167 | 0.167 | 0.056 | 0.111 |
| 4.2-5.1 | 0.000 | 0.167 | 0.111 | 0.111 | 0.167 | 0.222 | 0.111 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.167 | 0.167 | 0.111 | 0.111 | 0.278 | 0.111 |
| 6.0-6.9 | 0.000 | 0.167 | 0.111 | 0.222 | 0.111 | 0.278 | 0.111 | 0.000 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2016)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.2368, support=38
- `0.6-1.5`: recall=0.2593, support=54
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.237 | 0.105 | 0.079 | 0.026 | 0.132 | 0.000 | 0.105 | 0.316 |
| 0.6-1.5 | 0.315 | 0.259 | 0.111 | 0.037 | 0.074 | 0.056 | 0.056 | 0.093 |
| 1.5-2.4 | 0.222 | 0.167 | 0.130 | 0.019 | 0.111 | 0.093 | 0.056 | 0.204 |
| 2.4-3.3 | 0.259 | 0.111 | 0.093 | 0.037 | 0.148 | 0.056 | 0.222 | 0.074 |
| 3.3-4.2 | 0.222 | 0.000 | 0.074 | 0.037 | 0.241 | 0.130 | 0.167 | 0.130 |
| 4.2-5.1 | 0.226 | 0.000 | 0.094 | 0.038 | 0.226 | 0.075 | 0.189 | 0.151 |
| 5.1-6.0 | 0.170 | 0.038 | 0.057 | 0.038 | 0.094 | 0.057 | 0.340 | 0.208 |
| 6.0-6.9 | 0.264 | 0.057 | 0.057 | 0.019 | 0.132 | 0.038 | 0.170 | 0.264 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1808)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `0.6-1.5`: recall=0.2593, support=54
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.1296, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.2264, support=53
- `6.0-6.9`: recall=0.2075, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.158 | 0.184 | 0.026 | 0.132 | 0.053 | 0.079 | 0.184 |
| 0.6-1.5 | 0.167 | 0.259 | 0.278 | 0.037 | 0.074 | 0.000 | 0.019 | 0.167 |
| 1.5-2.4 | 0.130 | 0.222 | 0.259 | 0.019 | 0.074 | 0.037 | 0.111 | 0.148 |
| 2.4-3.3 | 0.056 | 0.111 | 0.315 | 0.130 | 0.074 | 0.000 | 0.185 | 0.130 |
| 3.3-4.2 | 0.019 | 0.148 | 0.204 | 0.074 | 0.093 | 0.037 | 0.259 | 0.167 |
| 4.2-5.1 | 0.057 | 0.038 | 0.208 | 0.132 | 0.132 | 0.057 | 0.264 | 0.113 |
| 5.1-6.0 | 0.057 | 0.094 | 0.170 | 0.075 | 0.057 | 0.057 | 0.226 | 0.264 |
| 6.0-6.9 | 0.094 | 0.151 | 0.208 | 0.019 | 0.057 | 0.038 | 0.226 | 0.208 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1807)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `0.6-1.5`: recall=0.2778, support=54
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.1667, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.1509, support=53
- `6.0-6.9`: recall=0.1887, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.158 | 0.132 | 0.079 | 0.132 | 0.079 | 0.132 | 0.105 |
| 0.6-1.5 | 0.056 | 0.278 | 0.204 | 0.037 | 0.111 | 0.056 | 0.204 | 0.056 |
| 1.5-2.4 | 0.111 | 0.167 | 0.241 | 0.074 | 0.111 | 0.074 | 0.204 | 0.019 |
| 2.4-3.3 | 0.167 | 0.074 | 0.167 | 0.093 | 0.130 | 0.185 | 0.167 | 0.019 |
| 3.3-4.2 | 0.093 | 0.222 | 0.148 | 0.074 | 0.167 | 0.074 | 0.167 | 0.056 |
| 4.2-5.1 | 0.113 | 0.151 | 0.170 | 0.057 | 0.075 | 0.113 | 0.208 | 0.113 |
| 5.1-6.0 | 0.208 | 0.226 | 0.132 | 0.000 | 0.038 | 0.094 | 0.151 | 0.151 |
| 6.0-6.9 | 0.113 | 0.151 | 0.075 | 0.057 | 0.113 | 0.094 | 0.208 | 0.189 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1658)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.2593, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1321, support=53
- `6.0-6.9`: recall=0.1132, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.211 | 0.132 | 0.132 | 0.079 | 0.053 | 0.158 | 0.132 |
| 0.6-1.5 | 0.037 | 0.296 | 0.130 | 0.074 | 0.093 | 0.130 | 0.093 | 0.148 |
| 1.5-2.4 | 0.056 | 0.130 | 0.093 | 0.074 | 0.111 | 0.167 | 0.167 | 0.204 |
| 2.4-3.3 | 0.019 | 0.111 | 0.093 | 0.259 | 0.185 | 0.019 | 0.130 | 0.185 |
| 3.3-4.2 | 0.111 | 0.037 | 0.093 | 0.074 | 0.241 | 0.130 | 0.148 | 0.167 |
| 4.2-5.1 | 0.038 | 0.057 | 0.094 | 0.094 | 0.226 | 0.094 | 0.245 | 0.151 |
| 5.1-6.0 | 0.038 | 0.075 | 0.170 | 0.057 | 0.208 | 0.132 | 0.132 | 0.189 |
| 6.0-6.9 | 0.189 | 0.075 | 0.151 | 0.113 | 0.151 | 0.094 | 0.113 | 0.113 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1512)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `0.6-1.5`: recall=0.1667, support=54
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.2037, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.2264, support=53
- `6.0-6.9`: recall=0.1887, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.079 | 0.158 | 0.211 | 0.158 | 0.053 | 0.053 | 0.105 | 0.184 |
| 0.6-1.5 | 0.167 | 0.167 | 0.259 | 0.056 | 0.037 | 0.019 | 0.185 | 0.111 |
| 1.5-2.4 | 0.167 | 0.130 | 0.185 | 0.093 | 0.111 | 0.037 | 0.148 | 0.130 |
| 2.4-3.3 | 0.074 | 0.019 | 0.333 | 0.204 | 0.093 | 0.056 | 0.074 | 0.148 |
| 3.3-4.2 | 0.111 | 0.074 | 0.222 | 0.148 | 0.093 | 0.074 | 0.185 | 0.093 |
| 4.2-5.1 | 0.057 | 0.094 | 0.245 | 0.151 | 0.057 | 0.094 | 0.189 | 0.113 |
| 5.1-6.0 | 0.019 | 0.057 | 0.226 | 0.151 | 0.094 | 0.038 | 0.226 | 0.189 |
| 6.0-6.9 | 0.113 | 0.057 | 0.113 | 0.132 | 0.113 | 0.038 | 0.245 | 0.189 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1306)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.3421, support=38
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.1296, support=54
- `3.3-4.2`: recall=0.0370, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.4151, support=53
- `6.0-6.9`: recall=0.0189, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.342 | 0.079 | 0.000 | 0.105 | 0.000 | 0.184 | 0.211 | 0.079 |
| 0.6-1.5 | 0.389 | 0.019 | 0.056 | 0.111 | 0.037 | 0.093 | 0.278 | 0.019 |
| 1.5-2.4 | 0.333 | 0.056 | 0.019 | 0.074 | 0.037 | 0.074 | 0.407 | 0.000 |
| 2.4-3.3 | 0.352 | 0.019 | 0.111 | 0.130 | 0.000 | 0.074 | 0.241 | 0.074 |
| 3.3-4.2 | 0.333 | 0.019 | 0.037 | 0.148 | 0.037 | 0.056 | 0.352 | 0.019 |
| 4.2-5.1 | 0.358 | 0.019 | 0.075 | 0.057 | 0.019 | 0.113 | 0.340 | 0.019 |
| 5.1-6.0 | 0.340 | 0.038 | 0.038 | 0.113 | 0.000 | 0.038 | 0.415 | 0.019 |
| 6.0-6.9 | 0.340 | 0.000 | 0.038 | 0.094 | 0.038 | 0.038 | 0.434 | 0.019 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1129)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.5000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.026 | 0.421 | 0.000 | 0.000 | 0.368 | 0.184 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.593 | 0.019 | 0.000 | 0.333 | 0.056 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.556 | 0.037 | 0.000 | 0.333 | 0.074 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.500 | 0.019 | 0.000 | 0.333 | 0.148 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.630 | 0.000 | 0.019 | 0.315 | 0.037 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.075 |
| 5.1-6.0 | 0.000 | 0.019 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.057 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.623 | 0.000 | 0.038 | 0.302 | 0.038 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2192)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.7778, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.071 | 0.000 | 0.000 | 0.000 | 0.429 | 0.143 |
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 |
| 1.5-2.4 | 0.000 | 0.389 | 0.111 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.000 | 0.278 | 0.111 | 0.056 | 0.000 | 0.000 | 0.556 | 0.000 |
| 3.3-4.2 | 0.000 | 0.118 | 0.118 | 0.000 | 0.000 | 0.059 | 0.706 | 0.000 |
| 4.2-5.1 | 0.000 | 0.111 | 0.000 | 0.000 | 0.056 | 0.000 | 0.778 | 0.056 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.000 | 0.000 | 0.000 | 0.778 | 0.056 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.056 | 0.722 | 0.167 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1974)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.143 | 0.000 | 0.000 | 0.000 | 0.429 | 0.071 |
| 0.6-1.5 | 0.056 | 0.000 | 0.278 | 0.000 | 0.000 | 0.000 | 0.500 | 0.167 |
| 1.5-2.4 | 0.000 | 0.000 | 0.278 | 0.056 | 0.056 | 0.000 | 0.611 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.333 | 0.000 | 0.000 | 0.000 | 0.667 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.235 | 0.000 | 0.000 | 0.000 | 0.647 | 0.118 |
| 4.2-5.1 | 0.056 | 0.000 | 0.056 | 0.000 | 0.000 | 0.111 | 0.667 | 0.111 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 | 0.111 | 0.611 | 0.222 |
| 6.0-6.9 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 | 0.667 | 0.222 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1865)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.071 | 0.000 | 0.071 | 0.000 | 0.143 | 0.357 |
| 0.6-1.5 | 0.000 | 0.222 | 0.111 | 0.056 | 0.056 | 0.056 | 0.222 | 0.278 |
| 1.5-2.4 | 0.000 | 0.222 | 0.167 | 0.000 | 0.167 | 0.056 | 0.222 | 0.167 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.000 | 0.111 | 0.222 | 0.333 | 0.056 |
| 3.3-4.2 | 0.000 | 0.000 | 0.176 | 0.059 | 0.176 | 0.000 | 0.471 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.000 | 0.000 | 0.444 | 0.111 | 0.222 | 0.167 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 | 0.333 | 0.167 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.556 | 0.000 | 0.167 | 0.278 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1319)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.357 | 0.214 | 0.143 | 0.071 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.333 | 0.056 | 0.000 | 0.222 | 0.167 | 0.056 | 0.167 |
| 1.5-2.4 | 0.000 | 0.333 | 0.167 | 0.056 | 0.167 | 0.167 | 0.056 | 0.056 |
| 2.4-3.3 | 0.000 | 0.111 | 0.222 | 0.111 | 0.167 | 0.333 | 0.000 | 0.056 |
| 3.3-4.2 | 0.000 | 0.294 | 0.176 | 0.059 | 0.118 | 0.118 | 0.118 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.056 | 0.000 | 0.611 | 0.222 | 0.000 | 0.056 |
| 5.1-6.0 | 0.000 | 0.111 | 0.111 | 0.167 | 0.278 | 0.278 | 0.000 | 0.056 |
| 6.0-6.9 | 0.000 | 0.056 | 0.167 | 0.056 | 0.333 | 0.167 | 0.111 | 0.111 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1270)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.000 | 0.071 | 0.357 | 0.214 | 0.143 | 0.000 |
| 0.6-1.5 | 0.222 | 0.111 | 0.000 | 0.000 | 0.056 | 0.500 | 0.111 | 0.000 |
| 1.5-2.4 | 0.000 | 0.278 | 0.111 | 0.000 | 0.000 | 0.444 | 0.056 | 0.111 |
| 2.4-3.3 | 0.167 | 0.222 | 0.056 | 0.000 | 0.000 | 0.389 | 0.167 | 0.000 |
| 3.3-4.2 | 0.118 | 0.118 | 0.000 | 0.000 | 0.059 | 0.353 | 0.176 | 0.176 |
| 4.2-5.1 | 0.222 | 0.000 | 0.056 | 0.000 | 0.000 | 0.389 | 0.333 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.000 | 0.167 | 0.444 | 0.278 | 0.056 |
| 6.0-6.9 | 0.167 | 0.056 | 0.056 | 0.056 | 0.000 | 0.444 | 0.222 | 0.000 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/gaussian_nb_none.png`

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
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1131)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.357 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.611 | 0.000 | 0.222 | 0.167 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.500 | 0.000 | 0.222 | 0.222 | 0.000 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.500 | 0.000 | 0.389 | 0.111 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.529 | 0.059 | 0.412 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3438)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.4118, support=17
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.000 | 0.000 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.056 | 0.500 | 0.222 | 0.000 | 0.056 | 0.056 | 0.056 | 0.056 |
| 1.5-2.4 | 0.000 | 0.333 | 0.333 | 0.111 | 0.111 | 0.000 | 0.056 | 0.056 |
| 2.4-3.3 | 0.000 | 0.056 | 0.333 | 0.056 | 0.111 | 0.278 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.056 | 0.000 | 0.167 | 0.167 | 0.167 | 0.333 | 0.056 |
| 4.2-5.1 | 0.000 | 0.118 | 0.059 | 0.000 | 0.176 | 0.412 | 0.118 | 0.118 |
| 5.1-6.0 | 0.000 | 0.111 | 0.000 | 0.056 | 0.056 | 0.167 | 0.500 | 0.111 |
| 6.0-6.9 | 0.111 | 0.000 | 0.111 | 0.111 | 0.111 | 0.278 | 0.222 | 0.056 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3438)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.786 | 0.071 | 0.000 | 0.000 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.056 | 0.556 | 0.167 | 0.000 | 0.111 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.056 | 0.278 | 0.333 | 0.056 | 0.111 | 0.111 | 0.056 | 0.000 |
| 2.4-3.3 | 0.000 | 0.056 | 0.167 | 0.000 | 0.389 | 0.167 | 0.111 | 0.111 |
| 3.3-4.2 | 0.056 | 0.056 | 0.167 | 0.056 | 0.111 | 0.167 | 0.222 | 0.167 |
| 4.2-5.1 | 0.000 | 0.118 | 0.000 | 0.059 | 0.118 | 0.176 | 0.353 | 0.176 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.056 | 0.111 | 0.167 | 0.556 | 0.056 |
| 6.0-6.9 | 0.056 | 0.000 | 0.167 | 0.111 | 0.056 | 0.111 | 0.278 | 0.222 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3312)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.3333, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.143 | 0.071 | 0.000 | 0.143 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.333 | 0.111 | 0.056 | 0.167 | 0.056 | 0.167 | 0.111 |
| 1.5-2.4 | 0.056 | 0.111 | 0.389 | 0.167 | 0.111 | 0.056 | 0.111 | 0.000 |
| 2.4-3.3 | 0.111 | 0.111 | 0.056 | 0.056 | 0.222 | 0.167 | 0.111 | 0.167 |
| 3.3-4.2 | 0.056 | 0.111 | 0.111 | 0.056 | 0.333 | 0.111 | 0.167 | 0.056 |
| 4.2-5.1 | 0.000 | 0.118 | 0.000 | 0.118 | 0.176 | 0.118 | 0.294 | 0.176 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.111 | 0.111 | 0.278 | 0.278 | 0.111 |
| 6.0-6.9 | 0.000 | 0.056 | 0.056 | 0.111 | 0.167 | 0.111 | 0.167 | 0.333 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.000 | 0.143 | 0.143 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.111 | 0.389 | 0.222 | 0.056 | 0.056 | 0.000 | 0.167 | 0.000 |
| 1.5-2.4 | 0.056 | 0.222 | 0.278 | 0.167 | 0.222 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.056 | 0.000 | 0.222 | 0.167 | 0.222 | 0.111 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.111 | 0.056 | 0.167 | 0.111 | 0.278 | 0.167 | 0.056 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.176 | 0.118 | 0.294 | 0.176 | 0.118 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.111 | 0.056 | 0.278 | 0.222 | 0.333 |
| 6.0-6.9 | 0.000 | 0.000 | 0.056 | 0.111 | 0.333 | 0.000 | 0.167 | 0.333 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.5294, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.214 | 0.071 | 0.000 | 0.071 | 0.000 | 0.071 |
| 0.6-1.5 | 0.000 | 0.278 | 0.389 | 0.056 | 0.056 | 0.111 | 0.056 | 0.056 |
| 1.5-2.4 | 0.056 | 0.222 | 0.278 | 0.111 | 0.111 | 0.222 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.222 | 0.111 | 0.167 | 0.389 | 0.056 | 0.056 |
| 3.3-4.2 | 0.056 | 0.000 | 0.222 | 0.111 | 0.056 | 0.389 | 0.167 | 0.000 |
| 4.2-5.1 | 0.000 | 0.118 | 0.059 | 0.000 | 0.176 | 0.529 | 0.059 | 0.059 |
| 5.1-6.0 | 0.000 | 0.056 | 0.167 | 0.056 | 0.056 | 0.389 | 0.278 | 0.000 |
| 6.0-6.9 | 0.000 | 0.056 | 0.222 | 0.056 | 0.111 | 0.444 | 0.056 | 0.056 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2437)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.071 | 0.214 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.056 | 0.222 | 0.222 | 0.056 | 0.167 | 0.278 | 0.000 | 0.000 |
| 1.5-2.4 | 0.056 | 0.167 | 0.389 | 0.111 | 0.056 | 0.167 | 0.056 | 0.000 |
| 2.4-3.3 | 0.000 | 0.222 | 0.000 | 0.167 | 0.056 | 0.278 | 0.111 | 0.167 |
| 3.3-4.2 | 0.056 | 0.000 | 0.111 | 0.167 | 0.222 | 0.222 | 0.167 | 0.056 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.176 | 0.059 | 0.235 | 0.294 | 0.176 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.000 | 0.111 | 0.333 | 0.278 | 0.111 |
| 6.0-6.9 | 0.000 | 0.000 | 0.111 | 0.111 | 0.111 | 0.500 | 0.111 | 0.056 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1187)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.071 | 0.143 | 0.286 | 0.214 | 0.071 | 0.000 |
| 0.6-1.5 | 0.111 | 0.056 | 0.056 | 0.111 | 0.278 | 0.167 | 0.167 | 0.056 |
| 1.5-2.4 | 0.000 | 0.167 | 0.111 | 0.167 | 0.333 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.056 | 0.056 | 0.278 | 0.278 | 0.111 | 0.000 |
| 3.3-4.2 | 0.056 | 0.167 | 0.000 | 0.222 | 0.167 | 0.278 | 0.111 | 0.000 |
| 4.2-5.1 | 0.059 | 0.176 | 0.000 | 0.118 | 0.176 | 0.235 | 0.235 | 0.000 |
| 5.1-6.0 | 0.111 | 0.167 | 0.000 | 0.111 | 0.222 | 0.222 | 0.056 | 0.111 |
| 6.0-6.9 | 0.111 | 0.167 | 0.000 | 0.167 | 0.222 | 0.222 | 0.111 | 0.000 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1728)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `0.6-1.5`: recall=0.4444, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.1667, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1887, support=53
- `6.0-6.9`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.211 | 0.053 | 0.026 | 0.105 | 0.026 | 0.132 | 0.342 |
| 0.6-1.5 | 0.074 | 0.444 | 0.074 | 0.000 | 0.093 | 0.000 | 0.259 | 0.056 |
| 1.5-2.4 | 0.037 | 0.389 | 0.093 | 0.019 | 0.093 | 0.167 | 0.167 | 0.037 |
| 2.4-3.3 | 0.111 | 0.111 | 0.167 | 0.000 | 0.130 | 0.093 | 0.241 | 0.148 |
| 3.3-4.2 | 0.074 | 0.093 | 0.130 | 0.019 | 0.167 | 0.148 | 0.278 | 0.093 |
| 4.2-5.1 | 0.075 | 0.094 | 0.132 | 0.038 | 0.151 | 0.094 | 0.283 | 0.132 |
| 5.1-6.0 | 0.019 | 0.132 | 0.132 | 0.019 | 0.208 | 0.019 | 0.189 | 0.283 |
| 6.0-6.9 | 0.075 | 0.075 | 0.094 | 0.057 | 0.094 | 0.094 | 0.208 | 0.302 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1651)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `0.6-1.5`: recall=0.2593, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.2963, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.3208, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.105 | 0.026 | 0.000 | 0.263 | 0.079 | 0.184 | 0.158 |
| 0.6-1.5 | 0.093 | 0.259 | 0.019 | 0.000 | 0.278 | 0.019 | 0.167 | 0.167 |
| 1.5-2.4 | 0.056 | 0.222 | 0.019 | 0.019 | 0.259 | 0.074 | 0.111 | 0.241 |
| 2.4-3.3 | 0.093 | 0.056 | 0.037 | 0.000 | 0.259 | 0.111 | 0.222 | 0.222 |
| 3.3-4.2 | 0.130 | 0.000 | 0.000 | 0.019 | 0.296 | 0.093 | 0.333 | 0.130 |
| 4.2-5.1 | 0.075 | 0.038 | 0.000 | 0.000 | 0.264 | 0.094 | 0.340 | 0.189 |
| 5.1-6.0 | 0.094 | 0.000 | 0.038 | 0.000 | 0.245 | 0.075 | 0.321 | 0.226 |
| 6.0-6.9 | 0.075 | 0.057 | 0.000 | 0.057 | 0.245 | 0.038 | 0.358 | 0.170 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1648)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1579, support=38
- `0.6-1.5`: recall=0.1852, support=54
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2593, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.2453, support=53
- `6.0-6.9`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.158 | 0.132 | 0.184 | 0.053 | 0.184 | 0.026 | 0.184 | 0.079 |
| 0.6-1.5 | 0.167 | 0.185 | 0.185 | 0.037 | 0.093 | 0.037 | 0.185 | 0.111 |
| 1.5-2.4 | 0.037 | 0.130 | 0.222 | 0.019 | 0.241 | 0.074 | 0.148 | 0.130 |
| 2.4-3.3 | 0.148 | 0.056 | 0.148 | 0.037 | 0.204 | 0.093 | 0.167 | 0.148 |
| 3.3-4.2 | 0.185 | 0.093 | 0.019 | 0.056 | 0.259 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.132 | 0.038 | 0.094 | 0.019 | 0.245 | 0.113 | 0.226 | 0.132 |
| 5.1-6.0 | 0.151 | 0.038 | 0.113 | 0.057 | 0.208 | 0.075 | 0.245 | 0.113 |
| 6.0-6.9 | 0.151 | 0.132 | 0.057 | 0.038 | 0.151 | 0.113 | 0.208 | 0.151 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1568)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1579, support=38
- `0.6-1.5`: recall=0.2222, support=54
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.1111, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.1887, support=53
- `5.1-6.0`: recall=0.1509, support=53
- `6.0-6.9`: recall=0.1321, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.158 | 0.105 | 0.079 | 0.132 | 0.105 | 0.184 | 0.079 | 0.158 |
| 0.6-1.5 | 0.130 | 0.222 | 0.130 | 0.111 | 0.074 | 0.093 | 0.093 | 0.148 |
| 1.5-2.4 | 0.074 | 0.222 | 0.148 | 0.111 | 0.093 | 0.148 | 0.074 | 0.130 |
| 2.4-3.3 | 0.074 | 0.222 | 0.148 | 0.111 | 0.111 | 0.167 | 0.093 | 0.074 |
| 3.3-4.2 | 0.037 | 0.130 | 0.167 | 0.093 | 0.148 | 0.222 | 0.148 | 0.056 |
| 4.2-5.1 | 0.057 | 0.075 | 0.094 | 0.132 | 0.189 | 0.189 | 0.151 | 0.113 |
| 5.1-6.0 | 0.151 | 0.094 | 0.057 | 0.094 | 0.189 | 0.208 | 0.151 | 0.057 |
| 6.0-6.9 | 0.132 | 0.094 | 0.075 | 0.132 | 0.189 | 0.132 | 0.113 | 0.132 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1340)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `0.6-1.5`: recall=0.3519, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.0943, support=53
- `6.0-6.9`: recall=0.0755, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.053 | 0.395 | 0.105 | 0.000 | 0.079 | 0.132 | 0.079 | 0.158 |
| 0.6-1.5 | 0.074 | 0.352 | 0.148 | 0.056 | 0.037 | 0.056 | 0.185 | 0.093 |
| 1.5-2.4 | 0.019 | 0.352 | 0.111 | 0.037 | 0.093 | 0.185 | 0.093 | 0.111 |
| 2.4-3.3 | 0.019 | 0.315 | 0.037 | 0.019 | 0.204 | 0.111 | 0.167 | 0.130 |
| 3.3-4.2 | 0.130 | 0.204 | 0.074 | 0.093 | 0.241 | 0.056 | 0.148 | 0.056 |
| 4.2-5.1 | 0.094 | 0.113 | 0.113 | 0.057 | 0.226 | 0.075 | 0.170 | 0.151 |
| 5.1-6.0 | 0.057 | 0.208 | 0.208 | 0.019 | 0.208 | 0.151 | 0.094 | 0.057 |
| 6.0-6.9 | 0.151 | 0.094 | 0.132 | 0.094 | 0.113 | 0.094 | 0.245 | 0.075 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1264)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.3684, support=38
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.0370, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.4151, support=53
- `6.0-6.9`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.368 | 0.079 | 0.000 | 0.053 | 0.000 | 0.184 | 0.237 | 0.079 |
| 0.6-1.5 | 0.389 | 0.019 | 0.056 | 0.093 | 0.037 | 0.111 | 0.278 | 0.019 |
| 1.5-2.4 | 0.333 | 0.056 | 0.000 | 0.074 | 0.037 | 0.130 | 0.370 | 0.000 |
| 2.4-3.3 | 0.352 | 0.019 | 0.093 | 0.093 | 0.000 | 0.111 | 0.259 | 0.074 |
| 3.3-4.2 | 0.333 | 0.019 | 0.056 | 0.130 | 0.037 | 0.056 | 0.352 | 0.019 |
| 4.2-5.1 | 0.358 | 0.019 | 0.038 | 0.057 | 0.019 | 0.113 | 0.377 | 0.019 |
| 5.1-6.0 | 0.340 | 0.038 | 0.038 | 0.113 | 0.000 | 0.038 | 0.415 | 0.019 |
| 6.0-6.9 | 0.358 | 0.000 | 0.019 | 0.094 | 0.038 | 0.038 | 0.453 | 0.000 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1129)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.5000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.026 | 0.421 | 0.000 | 0.000 | 0.368 | 0.184 |
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.593 | 0.019 | 0.000 | 0.333 | 0.056 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.556 | 0.037 | 0.000 | 0.333 | 0.074 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.500 | 0.019 | 0.000 | 0.333 | 0.148 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.630 | 0.000 | 0.019 | 0.315 | 0.037 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.075 |
| 5.1-6.0 | 0.000 | 0.019 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.057 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.623 | 0.000 | 0.038 | 0.302 | 0.038 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1843)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2941, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.000 | 0.071 | 0.143 | 0.357 | 0.143 | 0.143 |
| 0.6-1.5 | 0.111 | 0.389 | 0.111 | 0.056 | 0.111 | 0.000 | 0.111 | 0.111 |
| 1.5-2.4 | 0.111 | 0.444 | 0.222 | 0.111 | 0.111 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.056 | 0.222 | 0.222 | 0.111 | 0.000 | 0.167 | 0.111 | 0.111 |
| 3.3-4.2 | 0.118 | 0.176 | 0.235 | 0.059 | 0.294 | 0.059 | 0.059 | 0.000 |
| 4.2-5.1 | 0.111 | 0.056 | 0.167 | 0.056 | 0.167 | 0.167 | 0.056 | 0.222 |
| 5.1-6.0 | 0.000 | 0.167 | 0.167 | 0.222 | 0.056 | 0.278 | 0.111 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.222 | 0.111 | 0.111 | 0.389 | 0.056 | 0.111 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1687)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.143 | 0.000 | 0.000 | 0.000 | 0.500 | 0.143 |
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.056 | 0.444 | 0.000 |
| 1.5-2.4 | 0.000 | 0.500 | 0.056 | 0.000 | 0.000 | 0.000 | 0.444 | 0.000 |
| 2.4-3.3 | 0.056 | 0.278 | 0.111 | 0.000 | 0.000 | 0.056 | 0.500 | 0.000 |
| 3.3-4.2 | 0.059 | 0.176 | 0.176 | 0.059 | 0.000 | 0.000 | 0.471 | 0.059 |
| 4.2-5.1 | 0.056 | 0.000 | 0.000 | 0.111 | 0.056 | 0.000 | 0.556 | 0.222 |
| 5.1-6.0 | 0.222 | 0.056 | 0.000 | 0.111 | 0.000 | 0.000 | 0.500 | 0.111 |
| 6.0-6.9 | 0.222 | 0.000 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 | 0.222 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1597)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.143 | 0.071 | 0.286 | 0.000 | 0.000 | 0.214 | 0.286 |
| 0.6-1.5 | 0.000 | 0.611 | 0.000 | 0.000 | 0.000 | 0.056 | 0.111 | 0.222 |
| 1.5-2.4 | 0.000 | 0.500 | 0.056 | 0.111 | 0.000 | 0.000 | 0.056 | 0.278 |
| 2.4-3.3 | 0.000 | 0.278 | 0.056 | 0.222 | 0.056 | 0.000 | 0.222 | 0.167 |
| 3.3-4.2 | 0.000 | 0.176 | 0.000 | 0.353 | 0.000 | 0.000 | 0.412 | 0.059 |
| 4.2-5.1 | 0.000 | 0.056 | 0.000 | 0.444 | 0.056 | 0.000 | 0.389 | 0.056 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.444 | 0.056 | 0.000 | 0.333 | 0.111 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.444 | 0.056 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/gaussian_nb_none.png`

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
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.214 | 0.286 | 0.071 | 0.000 | 0.214 | 0.071 | 0.143 |
| 0.6-1.5 | 0.000 | 0.556 | 0.111 | 0.167 | 0.000 | 0.111 | 0.056 | 0.000 |
| 1.5-2.4 | 0.000 | 0.444 | 0.056 | 0.222 | 0.056 | 0.056 | 0.167 | 0.000 |
| 2.4-3.3 | 0.000 | 0.222 | 0.222 | 0.222 | 0.111 | 0.056 | 0.167 | 0.000 |
| 3.3-4.2 | 0.000 | 0.235 | 0.176 | 0.059 | 0.059 | 0.059 | 0.412 | 0.000 |
| 4.2-5.1 | 0.000 | 0.222 | 0.000 | 0.222 | 0.222 | 0.000 | 0.222 | 0.111 |
| 5.1-6.0 | 0.000 | 0.167 | 0.222 | 0.278 | 0.167 | 0.056 | 0.111 | 0.000 |
| 6.0-6.9 | 0.000 | 0.111 | 0.056 | 0.278 | 0.000 | 0.000 | 0.556 | 0.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1131)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.357 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.611 | 0.000 | 0.222 | 0.167 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.500 | 0.000 | 0.222 | 0.222 | 0.000 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.500 | 0.000 | 0.389 | 0.111 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.471 | 0.118 | 0.412 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1128)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.286 | 0.214 | 0.071 | 0.143 | 0.000 | 0.071 | 0.214 |
| 0.6-1.5 | 0.056 | 0.389 | 0.056 | 0.167 | 0.000 | 0.000 | 0.167 | 0.167 |
| 1.5-2.4 | 0.056 | 0.278 | 0.111 | 0.111 | 0.000 | 0.000 | 0.167 | 0.278 |
| 2.4-3.3 | 0.111 | 0.278 | 0.167 | 0.000 | 0.000 | 0.000 | 0.222 | 0.222 |
| 3.3-4.2 | 0.000 | 0.235 | 0.176 | 0.000 | 0.118 | 0.000 | 0.412 | 0.059 |
| 4.2-5.1 | 0.000 | 0.000 | 0.278 | 0.000 | 0.222 | 0.056 | 0.389 | 0.056 |
| 5.1-6.0 | 0.056 | 0.056 | 0.444 | 0.056 | 0.222 | 0.000 | 0.111 | 0.056 |
| 6.0-6.9 | 0.000 | 0.000 | 0.389 | 0.000 | 0.222 | 0.000 | 0.278 | 0.111 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.714 | 0.000 | 0.071 | 0.071 | 0.071 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.444 | 0.222 | 0.167 | 0.000 | 0.111 | 0.056 | 0.000 |
| 1.5-2.4 | 0.111 | 0.556 | 0.167 | 0.000 | 0.111 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.111 | 0.167 | 0.056 | 0.222 | 0.167 | 0.167 | 0.111 | 0.000 |
| 3.3-4.2 | 0.111 | 0.056 | 0.000 | 0.167 | 0.222 | 0.222 | 0.111 | 0.111 |
| 4.2-5.1 | 0.000 | 0.118 | 0.000 | 0.118 | 0.118 | 0.294 | 0.235 | 0.118 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.056 | 0.111 | 0.167 | 0.444 | 0.222 |
| 6.0-6.9 | 0.111 | 0.056 | 0.000 | 0.056 | 0.056 | 0.167 | 0.278 | 0.278 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.143 | 0.143 | 0.071 | 0.071 | 0.000 | 0.071 |
| 0.6-1.5 | 0.000 | 0.222 | 0.389 | 0.222 | 0.056 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.000 | 0.444 | 0.111 | 0.056 | 0.167 | 0.056 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.167 | 0.056 | 0.278 | 0.111 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.167 | 0.111 | 0.167 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.000 | 0.118 | 0.059 | 0.059 | 0.118 | 0.353 | 0.176 | 0.118 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.056 | 0.111 | 0.167 | 0.500 | 0.111 |
| 6.0-6.9 | 0.167 | 0.000 | 0.000 | 0.167 | 0.000 | 0.167 | 0.389 | 0.111 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.4118, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.214 | 0.071 | 0.000 | 0.071 | 0.071 | 0.000 |
| 0.6-1.5 | 0.000 | 0.278 | 0.333 | 0.222 | 0.000 | 0.111 | 0.000 | 0.056 |
| 1.5-2.4 | 0.167 | 0.222 | 0.278 | 0.056 | 0.056 | 0.111 | 0.056 | 0.056 |
| 2.4-3.3 | 0.000 | 0.056 | 0.167 | 0.222 | 0.167 | 0.222 | 0.111 | 0.056 |
| 3.3-4.2 | 0.056 | 0.000 | 0.167 | 0.167 | 0.167 | 0.333 | 0.111 | 0.000 |
| 4.2-5.1 | 0.000 | 0.059 | 0.118 | 0.118 | 0.059 | 0.412 | 0.176 | 0.059 |
| 5.1-6.0 | 0.000 | 0.000 | 0.167 | 0.111 | 0.056 | 0.222 | 0.389 | 0.056 |
| 6.0-6.9 | 0.000 | 0.056 | 0.167 | 0.111 | 0.056 | 0.389 | 0.222 | 0.000 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2687)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.786 | 0.000 | 0.143 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.056 | 0.444 | 0.333 | 0.111 | 0.056 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.111 | 0.333 | 0.167 | 0.167 | 0.056 | 0.000 | 0.167 | 0.000 |
| 2.4-3.3 | 0.056 | 0.333 | 0.167 | 0.056 | 0.111 | 0.056 | 0.111 | 0.111 |
| 3.3-4.2 | 0.222 | 0.167 | 0.000 | 0.167 | 0.278 | 0.000 | 0.111 | 0.056 |
| 4.2-5.1 | 0.059 | 0.176 | 0.176 | 0.000 | 0.235 | 0.000 | 0.294 | 0.059 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.000 | 0.056 | 0.111 | 0.389 | 0.278 |
| 6.0-6.9 | 0.167 | 0.111 | 0.056 | 0.111 | 0.000 | 0.167 | 0.278 | 0.111 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.071 | 0.143 | 0.143 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.000 | 0.222 | 0.167 | 0.222 | 0.111 | 0.167 | 0.000 | 0.111 |
| 1.5-2.4 | 0.056 | 0.222 | 0.222 | 0.167 | 0.111 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.000 | 0.222 | 0.111 | 0.222 | 0.111 | 0.167 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.000 | 0.167 | 0.222 | 0.167 | 0.167 | 0.056 | 0.167 |
| 4.2-5.1 | 0.000 | 0.059 | 0.000 | 0.059 | 0.118 | 0.353 | 0.235 | 0.176 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.167 | 0.056 | 0.222 | 0.333 | 0.111 |
| 6.0-6.9 | 0.056 | 0.111 | 0.056 | 0.111 | 0.000 | 0.222 | 0.333 | 0.111 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2625)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.000 | 0.000 | 0.286 | 0.000 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.389 | 0.278 | 0.056 | 0.056 | 0.000 | 0.056 | 0.167 |
| 1.5-2.4 | 0.056 | 0.389 | 0.000 | 0.167 | 0.111 | 0.000 | 0.056 | 0.222 |
| 2.4-3.3 | 0.167 | 0.167 | 0.111 | 0.167 | 0.222 | 0.056 | 0.111 | 0.000 |
| 3.3-4.2 | 0.111 | 0.056 | 0.056 | 0.167 | 0.278 | 0.167 | 0.167 | 0.000 |
| 4.2-5.1 | 0.294 | 0.000 | 0.000 | 0.059 | 0.118 | 0.235 | 0.176 | 0.118 |
| 5.1-6.0 | 0.056 | 0.056 | 0.000 | 0.111 | 0.056 | 0.167 | 0.278 | 0.278 |
| 6.0-6.9 | 0.111 | 0.056 | 0.111 | 0.167 | 0.056 | 0.222 | 0.056 | 0.222 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1187)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_all_bins_baseline/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.143 | 0.071 | 0.143 | 0.286 | 0.214 | 0.071 | 0.000 |
| 0.6-1.5 | 0.167 | 0.056 | 0.056 | 0.056 | 0.333 | 0.167 | 0.111 | 0.056 |
| 1.5-2.4 | 0.000 | 0.167 | 0.111 | 0.111 | 0.389 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.056 | 0.056 | 0.333 | 0.278 | 0.056 | 0.000 |
| 3.3-4.2 | 0.056 | 0.167 | 0.000 | 0.111 | 0.278 | 0.278 | 0.111 | 0.000 |
| 4.2-5.1 | 0.059 | 0.176 | 0.000 | 0.118 | 0.235 | 0.235 | 0.176 | 0.000 |
| 5.1-6.0 | 0.111 | 0.167 | 0.000 | 0.111 | 0.222 | 0.278 | 0.000 | 0.111 |
| 6.0-6.9 | 0.111 | 0.167 | 0.000 | 0.167 | 0.278 | 0.167 | 0.111 | 0.000 |


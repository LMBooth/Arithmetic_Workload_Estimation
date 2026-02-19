# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_easiest_baseline.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1760)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.108 | 0.135 | 0.189 | 0.108 | 0.081 | 0.216 |
| 1.5-2.4 | 0.185 | 0.074 | 0.093 | 0.130 | 0.130 | 0.204 | 0.185 |
| 2.4-3.3 | 0.235 | 0.196 | 0.098 | 0.176 | 0.157 | 0.098 | 0.039 |
| 3.3-4.2 | 0.151 | 0.057 | 0.151 | 0.189 | 0.113 | 0.302 | 0.038 |
| 4.2-5.1 | 0.157 | 0.157 | 0.078 | 0.157 | 0.176 | 0.118 | 0.157 |
| 5.1-6.0 | 0.154 | 0.173 | 0.058 | 0.212 | 0.077 | 0.192 | 0.135 |
| 6.0-6.9 | 0.038 | 0.154 | 0.096 | 0.212 | 0.115 | 0.115 | 0.269 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1599)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.3333, support=51
- `5.1-6.0`: recall=0.0385, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.162 | 0.108 | 0.027 | 0.135 | 0.000 | 0.405 |
| 1.5-2.4 | 0.222 | 0.167 | 0.130 | 0.019 | 0.167 | 0.056 | 0.241 |
| 2.4-3.3 | 0.216 | 0.157 | 0.118 | 0.039 | 0.196 | 0.039 | 0.235 |
| 3.3-4.2 | 0.189 | 0.151 | 0.151 | 0.038 | 0.245 | 0.019 | 0.208 |
| 4.2-5.1 | 0.176 | 0.157 | 0.098 | 0.020 | 0.333 | 0.059 | 0.157 |
| 5.1-6.0 | 0.212 | 0.192 | 0.096 | 0.038 | 0.308 | 0.038 | 0.115 |
| 6.0-6.9 | 0.135 | 0.115 | 0.135 | 0.058 | 0.308 | 0.058 | 0.192 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1592)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.2500, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.108 | 0.189 | 0.135 | 0.081 | 0.054 | 0.324 |
| 1.5-2.4 | 0.148 | 0.074 | 0.130 | 0.148 | 0.093 | 0.222 | 0.185 |
| 2.4-3.3 | 0.196 | 0.098 | 0.098 | 0.235 | 0.059 | 0.157 | 0.157 |
| 3.3-4.2 | 0.151 | 0.094 | 0.132 | 0.245 | 0.132 | 0.170 | 0.075 |
| 4.2-5.1 | 0.196 | 0.039 | 0.078 | 0.118 | 0.196 | 0.275 | 0.098 |
| 5.1-6.0 | 0.250 | 0.077 | 0.077 | 0.173 | 0.115 | 0.115 | 0.192 |
| 6.0-6.9 | 0.154 | 0.077 | 0.115 | 0.154 | 0.115 | 0.135 | 0.250 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1580)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.4510, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.2353, support=51
- `5.1-6.0`: recall=0.1346, support=52
- `6.0-6.9`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.054 | 0.054 | 0.486 | 0.162 | 0.027 | 0.081 | 0.135 |
| 1.5-2.4 | 0.111 | 0.037 | 0.500 | 0.130 | 0.093 | 0.093 | 0.037 |
| 2.4-3.3 | 0.078 | 0.039 | 0.451 | 0.039 | 0.196 | 0.118 | 0.078 |
| 3.3-4.2 | 0.094 | 0.019 | 0.396 | 0.132 | 0.189 | 0.094 | 0.075 |
| 4.2-5.1 | 0.098 | 0.039 | 0.431 | 0.039 | 0.235 | 0.059 | 0.098 |
| 5.1-6.0 | 0.135 | 0.019 | 0.308 | 0.115 | 0.115 | 0.135 | 0.173 |
| 6.0-6.9 | 0.077 | 0.019 | 0.365 | 0.038 | 0.231 | 0.135 | 0.135 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1388)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1154, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.162 | 0.216 | 0.270 | 0.081 | 0.027 | 0.135 |
| 1.5-2.4 | 0.259 | 0.167 | 0.185 | 0.074 | 0.093 | 0.111 | 0.111 |
| 2.4-3.3 | 0.294 | 0.176 | 0.157 | 0.157 | 0.137 | 0.059 | 0.020 |
| 3.3-4.2 | 0.226 | 0.151 | 0.151 | 0.170 | 0.208 | 0.094 | 0.000 |
| 4.2-5.1 | 0.235 | 0.098 | 0.098 | 0.157 | 0.216 | 0.118 | 0.078 |
| 5.1-6.0 | 0.308 | 0.096 | 0.135 | 0.135 | 0.212 | 0.058 | 0.058 |
| 6.0-6.9 | 0.250 | 0.115 | 0.135 | 0.115 | 0.192 | 0.077 | 0.115 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1366)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.0755, support=53
- `4.2-5.1`: recall=0.2353, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.189 | 0.162 | 0.027 | 0.135 | 0.000 | 0.270 |
| 1.5-2.4 | 0.352 | 0.093 | 0.111 | 0.056 | 0.148 | 0.056 | 0.185 |
| 2.4-3.3 | 0.216 | 0.176 | 0.078 | 0.098 | 0.216 | 0.059 | 0.157 |
| 3.3-4.2 | 0.151 | 0.170 | 0.094 | 0.075 | 0.264 | 0.075 | 0.170 |
| 4.2-5.1 | 0.196 | 0.098 | 0.098 | 0.078 | 0.235 | 0.039 | 0.255 |
| 5.1-6.0 | 0.308 | 0.077 | 0.154 | 0.077 | 0.250 | 0.058 | 0.077 |
| 6.0-6.9 | 0.212 | 0.135 | 0.058 | 0.096 | 0.250 | 0.058 | 0.192 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1200)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0811, support=37
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.081 | 0.189 | 0.108 | 0.243 | 0.108 | 0.081 | 0.189 |
| 1.5-2.4 | 0.204 | 0.167 | 0.130 | 0.074 | 0.093 | 0.167 | 0.167 |
| 2.4-3.3 | 0.216 | 0.196 | 0.020 | 0.137 | 0.157 | 0.157 | 0.118 |
| 3.3-4.2 | 0.151 | 0.113 | 0.057 | 0.170 | 0.208 | 0.170 | 0.132 |
| 4.2-5.1 | 0.157 | 0.118 | 0.137 | 0.157 | 0.216 | 0.176 | 0.039 |
| 5.1-6.0 | 0.212 | 0.058 | 0.115 | 0.135 | 0.192 | 0.154 | 0.135 |
| 6.0-6.9 | 0.115 | 0.192 | 0.115 | 0.135 | 0.212 | 0.154 | 0.077 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2075)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.071 | 0.000 | 0.000 | 0.286 | 0.000 | 0.000 |
| 1.5-2.4 | 0.438 | 0.125 | 0.062 | 0.000 | 0.312 | 0.062 | 0.000 |
| 2.4-3.3 | 0.235 | 0.294 | 0.059 | 0.000 | 0.412 | 0.000 | 0.000 |
| 3.3-4.2 | 0.353 | 0.235 | 0.176 | 0.000 | 0.235 | 0.000 | 0.000 |
| 4.2-5.1 | 0.333 | 0.000 | 0.056 | 0.000 | 0.611 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.056 | 0.167 | 0.000 | 0.167 | 0.000 | 0.111 |
| 6.0-6.9 | 0.278 | 0.278 | 0.056 | 0.000 | 0.389 | 0.000 | 0.000 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2037)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5556, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.143 | 0.000 | 0.143 | 0.000 | 0.000 |
| 1.5-2.4 | 0.312 | 0.250 | 0.312 | 0.000 | 0.000 | 0.062 | 0.062 |
| 2.4-3.3 | 0.353 | 0.176 | 0.176 | 0.000 | 0.235 | 0.059 | 0.000 |
| 3.3-4.2 | 0.176 | 0.176 | 0.353 | 0.000 | 0.294 | 0.000 | 0.000 |
| 4.2-5.1 | 0.111 | 0.056 | 0.278 | 0.000 | 0.556 | 0.000 | 0.000 |
| 5.1-6.0 | 0.278 | 0.056 | 0.222 | 0.056 | 0.278 | 0.000 | 0.111 |
| 6.0-6.9 | 0.444 | 0.222 | 0.056 | 0.056 | 0.167 | 0.056 | 0.000 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2003)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.000 | 0.000 | 0.143 | 0.000 | 0.000 |
| 1.5-2.4 | 0.625 | 0.250 | 0.062 | 0.000 | 0.000 | 0.062 | 0.000 |
| 2.4-3.3 | 0.412 | 0.235 | 0.235 | 0.000 | 0.118 | 0.000 | 0.000 |
| 3.3-4.2 | 0.353 | 0.294 | 0.118 | 0.000 | 0.235 | 0.000 | 0.000 |
| 4.2-5.1 | 0.444 | 0.000 | 0.167 | 0.000 | 0.333 | 0.056 | 0.000 |
| 5.1-6.0 | 0.611 | 0.056 | 0.056 | 0.056 | 0.111 | 0.000 | 0.111 |
| 6.0-6.9 | 0.500 | 0.222 | 0.000 | 0.056 | 0.222 | 0.000 | 0.000 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1584)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.143 | 0.000 | 0.214 | 0.000 | 0.143 |
| 1.5-2.4 | 0.250 | 0.312 | 0.188 | 0.000 | 0.188 | 0.000 | 0.062 |
| 2.4-3.3 | 0.294 | 0.176 | 0.176 | 0.118 | 0.059 | 0.059 | 0.118 |
| 3.3-4.2 | 0.118 | 0.176 | 0.235 | 0.000 | 0.176 | 0.176 | 0.118 |
| 4.2-5.1 | 0.000 | 0.167 | 0.500 | 0.000 | 0.222 | 0.056 | 0.056 |
| 5.1-6.0 | 0.278 | 0.333 | 0.056 | 0.000 | 0.167 | 0.056 | 0.111 |
| 6.0-6.9 | 0.278 | 0.333 | 0.056 | 0.000 | 0.111 | 0.056 | 0.167 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1484)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.286 | 0.071 | 0.214 | 0.071 | 0.071 |
| 1.5-2.4 | 0.188 | 0.000 | 0.250 | 0.250 | 0.125 | 0.062 | 0.125 |
| 2.4-3.3 | 0.176 | 0.176 | 0.118 | 0.000 | 0.118 | 0.176 | 0.235 |
| 3.3-4.2 | 0.000 | 0.176 | 0.294 | 0.000 | 0.059 | 0.118 | 0.353 |
| 4.2-5.1 | 0.000 | 0.056 | 0.222 | 0.167 | 0.389 | 0.056 | 0.111 |
| 5.1-6.0 | 0.056 | 0.222 | 0.056 | 0.056 | 0.167 | 0.278 | 0.167 |
| 6.0-6.9 | 0.111 | 0.167 | 0.111 | 0.056 | 0.167 | 0.278 | 0.111 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1346)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.214 | 0.214 | 0.071 | 0.000 | 0.071 | 0.143 |
| 1.5-2.4 | 0.375 | 0.125 | 0.250 | 0.062 | 0.188 | 0.000 | 0.000 |
| 2.4-3.3 | 0.118 | 0.294 | 0.118 | 0.059 | 0.118 | 0.118 | 0.176 |
| 3.3-4.2 | 0.294 | 0.294 | 0.118 | 0.000 | 0.000 | 0.000 | 0.294 |
| 4.2-5.1 | 0.167 | 0.000 | 0.278 | 0.056 | 0.167 | 0.111 | 0.222 |
| 5.1-6.0 | 0.167 | 0.222 | 0.111 | 0.111 | 0.056 | 0.167 | 0.167 |
| 6.0-6.9 | 0.167 | 0.389 | 0.167 | 0.000 | 0.056 | 0.167 | 0.056 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1009)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.071 | 0.071 | 0.143 | 0.071 | 0.143 |
| 1.5-2.4 | 0.312 | 0.188 | 0.125 | 0.000 | 0.250 | 0.000 | 0.125 |
| 2.4-3.3 | 0.588 | 0.000 | 0.000 | 0.118 | 0.235 | 0.000 | 0.059 |
| 3.3-4.2 | 0.412 | 0.118 | 0.059 | 0.000 | 0.176 | 0.176 | 0.059 |
| 4.2-5.1 | 0.333 | 0.056 | 0.167 | 0.056 | 0.111 | 0.056 | 0.222 |
| 5.1-6.0 | 0.278 | 0.222 | 0.167 | 0.056 | 0.167 | 0.000 | 0.111 |
| 6.0-6.9 | 0.389 | 0.167 | 0.333 | 0.056 | 0.000 | 0.000 | 0.056 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.000 | 0.000 | 0.143 | 0.214 | 0.000 |
| 1.5-2.4 | 0.111 | 0.111 | 0.000 | 0.056 | 0.056 | 0.278 | 0.389 |
| 2.4-3.3 | 0.111 | 0.278 | 0.111 | 0.000 | 0.111 | 0.278 | 0.111 |
| 3.3-4.2 | 0.056 | 0.333 | 0.111 | 0.111 | 0.167 | 0.222 | 0.000 |
| 4.2-5.1 | 0.167 | 0.111 | 0.111 | 0.056 | 0.333 | 0.056 | 0.167 |
| 5.1-6.0 | 0.111 | 0.167 | 0.111 | 0.111 | 0.167 | 0.333 | 0.000 |
| 6.0-6.9 | 0.056 | 0.333 | 0.167 | 0.111 | 0.056 | 0.111 | 0.167 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.143 | 0.000 | 0.214 | 0.143 | 0.071 |
| 1.5-2.4 | 0.333 | 0.111 | 0.222 | 0.056 | 0.000 | 0.111 | 0.167 |
| 2.4-3.3 | 0.278 | 0.111 | 0.056 | 0.111 | 0.111 | 0.222 | 0.111 |
| 3.3-4.2 | 0.111 | 0.222 | 0.111 | 0.222 | 0.111 | 0.222 | 0.000 |
| 4.2-5.1 | 0.167 | 0.111 | 0.167 | 0.056 | 0.278 | 0.167 | 0.056 |
| 5.1-6.0 | 0.167 | 0.056 | 0.167 | 0.167 | 0.167 | 0.278 | 0.000 |
| 6.0-6.9 | 0.056 | 0.167 | 0.278 | 0.056 | 0.111 | 0.000 | 0.333 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.000 | 0.071 | 0.214 | 0.143 | 0.143 |
| 1.5-2.4 | 0.222 | 0.111 | 0.056 | 0.111 | 0.111 | 0.167 | 0.222 |
| 2.4-3.3 | 0.111 | 0.111 | 0.056 | 0.111 | 0.167 | 0.167 | 0.278 |
| 3.3-4.2 | 0.111 | 0.056 | 0.167 | 0.278 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.167 | 0.167 | 0.222 | 0.222 | 0.056 |
| 5.1-6.0 | 0.111 | 0.111 | 0.111 | 0.111 | 0.111 | 0.333 | 0.111 |
| 6.0-6.9 | 0.000 | 0.222 | 0.222 | 0.167 | 0.111 | 0.000 | 0.278 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.214 | 0.143 | 0.000 | 0.214 | 0.071 | 0.071 |
| 1.5-2.4 | 0.278 | 0.000 | 0.278 | 0.000 | 0.000 | 0.167 | 0.278 |
| 2.4-3.3 | 0.111 | 0.111 | 0.167 | 0.111 | 0.167 | 0.111 | 0.222 |
| 3.3-4.2 | 0.056 | 0.111 | 0.222 | 0.167 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.000 | 0.222 | 0.000 | 0.389 | 0.167 | 0.167 |
| 5.1-6.0 | 0.056 | 0.111 | 0.222 | 0.167 | 0.111 | 0.222 | 0.111 |
| 6.0-6.9 | 0.000 | 0.333 | 0.222 | 0.222 | 0.056 | 0.000 | 0.167 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.571 | 0.071 | 0.071 | 0.000 | 0.071 | 0.071 |
| 1.5-2.4 | 0.389 | 0.056 | 0.167 | 0.111 | 0.056 | 0.111 | 0.111 |
| 2.4-3.3 | 0.222 | 0.056 | 0.222 | 0.167 | 0.056 | 0.167 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.222 | 0.111 | 0.222 | 0.167 | 0.111 |
| 4.2-5.1 | 0.167 | 0.000 | 0.056 | 0.056 | 0.333 | 0.278 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.222 | 0.167 | 0.389 | 0.056 |
| 6.0-6.9 | 0.056 | 0.278 | 0.222 | 0.056 | 0.167 | 0.056 | 0.167 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.357 | 0.000 | 0.000 | 0.286 | 0.214 | 0.000 |
| 1.5-2.4 | 0.222 | 0.167 | 0.056 | 0.167 | 0.056 | 0.111 | 0.222 |
| 2.4-3.3 | 0.167 | 0.167 | 0.056 | 0.111 | 0.167 | 0.222 | 0.111 |
| 3.3-4.2 | 0.056 | 0.167 | 0.167 | 0.222 | 0.111 | 0.222 | 0.056 |
| 4.2-5.1 | 0.167 | 0.111 | 0.222 | 0.111 | 0.278 | 0.111 | 0.000 |
| 5.1-6.0 | 0.111 | 0.167 | 0.222 | 0.111 | 0.111 | 0.278 | 0.000 |
| 6.0-6.9 | 0.167 | 0.222 | 0.222 | 0.111 | 0.056 | 0.056 | 0.167 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.071 | 0.071 | 0.214 | 0.214 | 0.071 |
| 1.5-2.4 | 0.056 | 0.111 | 0.111 | 0.389 | 0.111 | 0.111 | 0.111 |
| 2.4-3.3 | 0.167 | 0.167 | 0.222 | 0.111 | 0.222 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.222 | 0.056 | 0.111 | 0.167 | 0.167 | 0.167 |
| 4.2-5.1 | 0.056 | 0.222 | 0.056 | 0.111 | 0.222 | 0.111 | 0.222 |
| 5.1-6.0 | 0.167 | 0.111 | 0.056 | 0.111 | 0.222 | 0.111 | 0.222 |
| 6.0-6.9 | 0.167 | 0.333 | 0.056 | 0.056 | 0.000 | 0.167 | 0.222 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1861)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.3654, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.189 | 0.054 | 0.189 | 0.162 | 0.000 | 0.135 | 0.270 |
| 1.5-2.4 | 0.204 | 0.278 | 0.074 | 0.111 | 0.130 | 0.037 | 0.167 |
| 2.4-3.3 | 0.196 | 0.157 | 0.039 | 0.157 | 0.157 | 0.020 | 0.275 |
| 3.3-4.2 | 0.151 | 0.151 | 0.075 | 0.151 | 0.094 | 0.151 | 0.226 |
| 4.2-5.1 | 0.196 | 0.078 | 0.078 | 0.118 | 0.118 | 0.137 | 0.275 |
| 5.1-6.0 | 0.135 | 0.077 | 0.038 | 0.115 | 0.192 | 0.154 | 0.288 |
| 6.0-6.9 | 0.135 | 0.058 | 0.038 | 0.058 | 0.115 | 0.231 | 0.365 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1830)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `1.5-2.4`: recall=0.2037, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.3208, support=53
- `4.2-5.1`: recall=0.0196, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.027 | 0.027 | 0.378 | 0.000 | 0.081 | 0.189 |
| 1.5-2.4 | 0.296 | 0.204 | 0.111 | 0.222 | 0.037 | 0.056 | 0.074 |
| 2.4-3.3 | 0.294 | 0.118 | 0.118 | 0.255 | 0.020 | 0.098 | 0.098 |
| 3.3-4.2 | 0.264 | 0.094 | 0.038 | 0.321 | 0.057 | 0.113 | 0.113 |
| 4.2-5.1 | 0.275 | 0.039 | 0.059 | 0.412 | 0.020 | 0.098 | 0.098 |
| 5.1-6.0 | 0.346 | 0.058 | 0.019 | 0.288 | 0.077 | 0.115 | 0.096 |
| 6.0-6.9 | 0.327 | 0.058 | 0.038 | 0.346 | 0.058 | 0.038 | 0.135 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1801)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.2115, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.054 | 0.027 | 0.297 | 0.000 | 0.081 | 0.243 |
| 1.5-2.4 | 0.130 | 0.167 | 0.111 | 0.241 | 0.056 | 0.074 | 0.222 |
| 2.4-3.3 | 0.059 | 0.196 | 0.078 | 0.235 | 0.098 | 0.118 | 0.216 |
| 3.3-4.2 | 0.057 | 0.132 | 0.057 | 0.264 | 0.057 | 0.189 | 0.245 |
| 4.2-5.1 | 0.059 | 0.118 | 0.078 | 0.314 | 0.039 | 0.216 | 0.176 |
| 5.1-6.0 | 0.058 | 0.096 | 0.058 | 0.308 | 0.038 | 0.173 | 0.269 |
| 6.0-6.9 | 0.077 | 0.173 | 0.038 | 0.269 | 0.058 | 0.173 | 0.212 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1740)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.1176, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.0784, support=51
- `5.1-6.0`: recall=0.1346, support=52
- `6.0-6.9`: recall=0.3462, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.054 | 0.081 | 0.243 | 0.000 | 0.081 | 0.324 |
| 1.5-2.4 | 0.185 | 0.111 | 0.148 | 0.204 | 0.074 | 0.074 | 0.204 |
| 2.4-3.3 | 0.059 | 0.098 | 0.118 | 0.255 | 0.059 | 0.078 | 0.333 |
| 3.3-4.2 | 0.094 | 0.094 | 0.075 | 0.189 | 0.094 | 0.189 | 0.264 |
| 4.2-5.1 | 0.059 | 0.098 | 0.039 | 0.157 | 0.078 | 0.196 | 0.373 |
| 5.1-6.0 | 0.058 | 0.077 | 0.058 | 0.173 | 0.038 | 0.135 | 0.462 |
| 6.0-6.9 | 0.077 | 0.038 | 0.058 | 0.173 | 0.173 | 0.135 | 0.346 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1718)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.7358, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.027 | 0.027 | 0.730 | 0.000 | 0.027 | 0.027 |
| 1.5-2.4 | 0.019 | 0.000 | 0.056 | 0.833 | 0.056 | 0.037 | 0.000 |
| 2.4-3.3 | 0.098 | 0.000 | 0.020 | 0.784 | 0.059 | 0.039 | 0.000 |
| 3.3-4.2 | 0.057 | 0.038 | 0.057 | 0.736 | 0.038 | 0.038 | 0.038 |
| 4.2-5.1 | 0.059 | 0.000 | 0.000 | 0.784 | 0.039 | 0.118 | 0.000 |
| 5.1-6.0 | 0.038 | 0.000 | 0.038 | 0.712 | 0.038 | 0.173 | 0.000 |
| 6.0-6.9 | 0.058 | 0.019 | 0.038 | 0.788 | 0.038 | 0.019 | 0.038 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1678)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.2264, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.189 | 0.162 | 0.216 | 0.108 | 0.081 | 0.027 | 0.216 |
| 1.5-2.4 | 0.130 | 0.222 | 0.130 | 0.130 | 0.204 | 0.037 | 0.148 |
| 2.4-3.3 | 0.118 | 0.176 | 0.176 | 0.176 | 0.137 | 0.078 | 0.137 |
| 3.3-4.2 | 0.151 | 0.132 | 0.189 | 0.226 | 0.151 | 0.038 | 0.113 |
| 4.2-5.1 | 0.157 | 0.176 | 0.118 | 0.275 | 0.118 | 0.039 | 0.118 |
| 5.1-6.0 | 0.096 | 0.212 | 0.135 | 0.154 | 0.135 | 0.058 | 0.212 |
| 6.0-6.9 | 0.096 | 0.231 | 0.173 | 0.212 | 0.096 | 0.058 | 0.135 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1328)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.2745, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.162 | 0.135 | 0.135 | 0.243 | 0.027 | 0.135 |
| 1.5-2.4 | 0.130 | 0.056 | 0.019 | 0.130 | 0.352 | 0.148 | 0.167 |
| 2.4-3.3 | 0.157 | 0.000 | 0.098 | 0.137 | 0.392 | 0.078 | 0.137 |
| 3.3-4.2 | 0.151 | 0.057 | 0.000 | 0.132 | 0.302 | 0.132 | 0.226 |
| 4.2-5.1 | 0.176 | 0.078 | 0.039 | 0.137 | 0.275 | 0.157 | 0.137 |
| 5.1-6.0 | 0.212 | 0.058 | 0.038 | 0.154 | 0.250 | 0.115 | 0.173 |
| 6.0-6.9 | 0.212 | 0.019 | 0.038 | 0.173 | 0.327 | 0.173 | 0.058 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2355)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.143 | 0.000 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.062 | 0.688 | 0.125 | 0.062 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.000 | 0.588 | 0.118 | 0.176 | 0.000 | 0.000 | 0.118 |
| 3.3-4.2 | 0.176 | 0.294 | 0.353 | 0.118 | 0.000 | 0.000 | 0.059 |
| 4.2-5.1 | 0.000 | 0.333 | 0.278 | 0.167 | 0.000 | 0.000 | 0.222 |
| 5.1-6.0 | 0.111 | 0.167 | 0.389 | 0.000 | 0.056 | 0.000 | 0.278 |
| 6.0-6.9 | 0.056 | 0.278 | 0.222 | 0.056 | 0.111 | 0.056 | 0.222 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2174)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.6250, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.4706, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.214 | 0.286 | 0.286 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.625 | 0.062 | 0.312 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.588 | 0.235 | 0.176 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.059 | 0.471 | 0.000 | 0.471 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.389 | 0.056 | 0.556 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.833 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.444 | 0.056 | 0.500 | 0.000 | 0.000 | 0.000 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2086)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.7500, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.643 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.750 | 0.000 | 0.062 | 0.000 | 0.125 | 0.000 |
| 2.4-3.3 | 0.059 | 0.588 | 0.118 | 0.059 | 0.000 | 0.176 | 0.000 |
| 3.3-4.2 | 0.118 | 0.529 | 0.176 | 0.000 | 0.000 | 0.176 | 0.000 |
| 4.2-5.1 | 0.056 | 0.667 | 0.000 | 0.056 | 0.000 | 0.222 | 0.000 |
| 5.1-6.0 | 0.000 | 0.444 | 0.000 | 0.111 | 0.000 | 0.333 | 0.111 |
| 6.0-6.9 | 0.000 | 0.611 | 0.111 | 0.000 | 0.000 | 0.278 | 0.000 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.500 | 0.000 | 0.071 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.000 | 0.688 | 0.000 | 0.188 | 0.000 | 0.000 | 0.125 |
| 2.4-3.3 | 0.000 | 0.529 | 0.000 | 0.118 | 0.000 | 0.176 | 0.176 |
| 3.3-4.2 | 0.118 | 0.588 | 0.059 | 0.000 | 0.000 | 0.235 | 0.000 |
| 4.2-5.1 | 0.000 | 0.444 | 0.000 | 0.278 | 0.000 | 0.167 | 0.111 |
| 5.1-6.0 | 0.000 | 0.278 | 0.000 | 0.444 | 0.000 | 0.222 | 0.056 |
| 6.0-6.9 | 0.000 | 0.556 | 0.056 | 0.167 | 0.000 | 0.167 | 0.056 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1789)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.6250, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.429 | 0.000 | 0.143 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.125 | 0.625 | 0.125 | 0.062 | 0.000 | 0.062 | 0.000 |
| 2.4-3.3 | 0.000 | 0.647 | 0.000 | 0.118 | 0.059 | 0.118 | 0.059 |
| 3.3-4.2 | 0.000 | 0.588 | 0.059 | 0.176 | 0.000 | 0.059 | 0.118 |
| 4.2-5.1 | 0.056 | 0.333 | 0.056 | 0.389 | 0.000 | 0.111 | 0.056 |
| 5.1-6.0 | 0.000 | 0.167 | 0.000 | 0.611 | 0.056 | 0.056 | 0.111 |
| 6.0-6.9 | 0.000 | 0.500 | 0.056 | 0.278 | 0.000 | 0.111 | 0.056 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1747)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.3529, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.143 | 0.143 | 0.000 | 0.143 | 0.071 |
| 1.5-2.4 | 0.000 | 0.250 | 0.375 | 0.250 | 0.062 | 0.000 | 0.062 |
| 2.4-3.3 | 0.000 | 0.059 | 0.176 | 0.353 | 0.176 | 0.118 | 0.118 |
| 3.3-4.2 | 0.000 | 0.118 | 0.294 | 0.353 | 0.059 | 0.059 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.444 | 0.278 | 0.111 | 0.111 | 0.000 |
| 5.1-6.0 | 0.056 | 0.000 | 0.611 | 0.111 | 0.111 | 0.056 | 0.056 |
| 6.0-6.9 | 0.056 | 0.056 | 0.500 | 0.111 | 0.056 | 0.167 | 0.056 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1538)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.3750, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.214 | 0.429 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.375 | 0.438 | 0.125 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.176 | 0.294 | 0.059 | 0.294 | 0.059 | 0.000 | 0.118 |
| 3.3-4.2 | 0.118 | 0.235 | 0.471 | 0.176 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.111 | 0.222 | 0.333 | 0.167 | 0.000 | 0.111 | 0.056 |
| 5.1-6.0 | 0.000 | 0.111 | 0.444 | 0.278 | 0.000 | 0.000 | 0.167 |
| 6.0-6.9 | 0.111 | 0.111 | 0.444 | 0.167 | 0.000 | 0.056 | 0.111 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.000 | 0.071 | 0.071 | 0.071 | 0.000 |
| 1.5-2.4 | 0.111 | 0.222 | 0.167 | 0.056 | 0.278 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.333 | 0.333 | 0.111 | 0.056 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.056 | 0.222 | 0.222 | 0.111 | 0.167 |
| 4.2-5.1 | 0.056 | 0.000 | 0.111 | 0.222 | 0.389 | 0.222 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.000 | 0.056 | 0.611 | 0.222 |
| 6.0-6.9 | 0.056 | 0.222 | 0.000 | 0.167 | 0.222 | 0.222 | 0.111 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.7222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.000 | 0.071 | 0.143 | 0.071 | 0.000 |
| 1.5-2.4 | 0.167 | 0.222 | 0.222 | 0.000 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.056 | 0.278 | 0.333 | 0.111 | 0.111 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.222 | 0.222 | 0.222 | 0.111 | 0.056 | 0.056 |
| 4.2-5.1 | 0.056 | 0.056 | 0.222 | 0.222 | 0.167 | 0.278 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.056 | 0.000 | 0.722 | 0.111 |
| 6.0-6.9 | 0.167 | 0.111 | 0.000 | 0.167 | 0.167 | 0.222 | 0.167 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.6667, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.214 | 0.000 | 0.143 | 0.143 | 0.071 | 0.000 |
| 1.5-2.4 | 0.056 | 0.167 | 0.278 | 0.167 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.333 | 0.278 | 0.167 | 0.056 | 0.000 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.000 | 0.222 | 0.278 | 0.000 | 0.333 |
| 4.2-5.1 | 0.056 | 0.056 | 0.167 | 0.222 | 0.333 | 0.167 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 | 0.667 | 0.222 |
| 6.0-6.9 | 0.056 | 0.222 | 0.000 | 0.056 | 0.222 | 0.278 | 0.167 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.071 | 0.071 | 0.071 | 0.143 | 0.071 |
| 1.5-2.4 | 0.167 | 0.222 | 0.167 | 0.111 | 0.111 | 0.056 | 0.167 |
| 2.4-3.3 | 0.056 | 0.278 | 0.333 | 0.222 | 0.056 | 0.000 | 0.056 |
| 3.3-4.2 | 0.167 | 0.111 | 0.111 | 0.222 | 0.278 | 0.000 | 0.111 |
| 4.2-5.1 | 0.056 | 0.056 | 0.167 | 0.222 | 0.333 | 0.167 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.056 | 0.111 | 0.611 | 0.167 |
| 6.0-6.9 | 0.111 | 0.056 | 0.056 | 0.056 | 0.222 | 0.333 | 0.167 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.7222, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.214 | 0.071 | 0.214 | 0.143 | 0.000 | 0.071 |
| 1.5-2.4 | 0.056 | 0.167 | 0.444 | 0.056 | 0.167 | 0.111 | 0.000 |
| 2.4-3.3 | 0.000 | 0.222 | 0.333 | 0.278 | 0.167 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.333 | 0.111 | 0.111 | 0.222 | 0.111 | 0.111 |
| 4.2-5.1 | 0.000 | 0.111 | 0.222 | 0.111 | 0.222 | 0.167 | 0.167 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.000 | 0.000 | 0.722 | 0.167 |
| 6.0-6.9 | 0.000 | 0.111 | 0.056 | 0.056 | 0.278 | 0.389 | 0.111 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.286 | 0.214 | 0.000 | 0.143 | 0.071 |
| 1.5-2.4 | 0.222 | 0.167 | 0.222 | 0.056 | 0.056 | 0.111 | 0.167 |
| 2.4-3.3 | 0.056 | 0.056 | 0.444 | 0.167 | 0.056 | 0.056 | 0.167 |
| 3.3-4.2 | 0.111 | 0.222 | 0.167 | 0.111 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.056 | 0.167 | 0.111 | 0.167 | 0.278 | 0.167 |
| 5.1-6.0 | 0.056 | 0.056 | 0.000 | 0.056 | 0.222 | 0.500 | 0.111 |
| 6.0-6.9 | 0.056 | 0.167 | 0.167 | 0.056 | 0.056 | 0.333 | 0.167 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/eeg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.214 | 0.071 | 0.214 | 0.000 | 0.071 | 0.000 |
| 1.5-2.4 | 0.111 | 0.111 | 0.278 | 0.167 | 0.111 | 0.111 | 0.111 |
| 2.4-3.3 | 0.056 | 0.222 | 0.333 | 0.278 | 0.056 | 0.000 | 0.056 |
| 3.3-4.2 | 0.111 | 0.167 | 0.167 | 0.167 | 0.167 | 0.000 | 0.222 |
| 4.2-5.1 | 0.056 | 0.056 | 0.056 | 0.222 | 0.111 | 0.278 | 0.222 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.056 | 0.111 | 0.500 | 0.167 |
| 6.0-6.9 | 0.056 | 0.111 | 0.056 | 0.111 | 0.278 | 0.222 | 0.167 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1869)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2105, support=38
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.3148, support=54
- `3.3-4.2`: recall=0.1667, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.1887, support=53
- `6.0-6.9`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.211 | 0.237 | 0.105 | 0.132 | 0.079 | 0.000 | 0.237 |
| 1.5-2.4 | 0.148 | 0.185 | 0.167 | 0.130 | 0.037 | 0.185 | 0.148 |
| 2.4-3.3 | 0.204 | 0.074 | 0.315 | 0.093 | 0.111 | 0.167 | 0.037 |
| 3.3-4.2 | 0.185 | 0.222 | 0.148 | 0.167 | 0.056 | 0.074 | 0.148 |
| 4.2-5.1 | 0.302 | 0.094 | 0.189 | 0.189 | 0.038 | 0.075 | 0.113 |
| 5.1-6.0 | 0.283 | 0.019 | 0.189 | 0.132 | 0.094 | 0.189 | 0.094 |
| 6.0-6.9 | 0.302 | 0.132 | 0.132 | 0.075 | 0.094 | 0.113 | 0.151 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1819)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2105, support=38
- `1.5-2.4`: recall=0.2037, support=54
- `2.4-3.3`: recall=0.2407, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1887, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.211 | 0.053 | 0.053 | 0.026 | 0.132 | 0.342 | 0.184 |
| 1.5-2.4 | 0.130 | 0.204 | 0.130 | 0.111 | 0.111 | 0.259 | 0.056 |
| 2.4-3.3 | 0.074 | 0.185 | 0.241 | 0.074 | 0.056 | 0.222 | 0.148 |
| 3.3-4.2 | 0.130 | 0.185 | 0.259 | 0.148 | 0.037 | 0.130 | 0.111 |
| 4.2-5.1 | 0.038 | 0.113 | 0.245 | 0.151 | 0.094 | 0.245 | 0.113 |
| 5.1-6.0 | 0.057 | 0.170 | 0.264 | 0.057 | 0.075 | 0.189 | 0.189 |
| 6.0-6.9 | 0.151 | 0.057 | 0.170 | 0.132 | 0.113 | 0.208 | 0.170 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1774)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.2105, support=38
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.1852, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.1887, support=53
- `6.0-6.9`: recall=0.2453, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.211 | 0.079 | 0.105 | 0.184 | 0.026 | 0.105 | 0.289 |
| 1.5-2.4 | 0.259 | 0.241 | 0.019 | 0.167 | 0.093 | 0.093 | 0.130 |
| 2.4-3.3 | 0.204 | 0.148 | 0.074 | 0.167 | 0.130 | 0.130 | 0.148 |
| 3.3-4.2 | 0.241 | 0.111 | 0.056 | 0.185 | 0.111 | 0.148 | 0.148 |
| 4.2-5.1 | 0.189 | 0.132 | 0.019 | 0.245 | 0.075 | 0.170 | 0.170 |
| 5.1-6.0 | 0.151 | 0.151 | 0.019 | 0.113 | 0.094 | 0.189 | 0.283 |
| 6.0-6.9 | 0.264 | 0.094 | 0.038 | 0.170 | 0.094 | 0.094 | 0.245 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1730)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.1296, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.2453, support=53
- `6.0-6.9`: recall=0.2264, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.211 | 0.079 | 0.158 | 0.026 | 0.079 | 0.263 |
| 1.5-2.4 | 0.130 | 0.278 | 0.111 | 0.111 | 0.037 | 0.130 | 0.204 |
| 2.4-3.3 | 0.037 | 0.333 | 0.130 | 0.056 | 0.037 | 0.185 | 0.222 |
| 3.3-4.2 | 0.019 | 0.204 | 0.130 | 0.111 | 0.074 | 0.278 | 0.185 |
| 4.2-5.1 | 0.057 | 0.189 | 0.151 | 0.132 | 0.057 | 0.264 | 0.151 |
| 5.1-6.0 | 0.057 | 0.189 | 0.113 | 0.075 | 0.057 | 0.245 | 0.264 |
| 6.0-6.9 | 0.094 | 0.264 | 0.075 | 0.057 | 0.038 | 0.245 | 0.226 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1518)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.2778, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1887, support=53
- `6.0-6.9`: recall=0.1132, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.184 | 0.132 | 0.158 | 0.132 | 0.105 | 0.184 |
| 1.5-2.4 | 0.074 | 0.111 | 0.074 | 0.148 | 0.204 | 0.167 | 0.222 |
| 2.4-3.3 | 0.019 | 0.111 | 0.278 | 0.185 | 0.074 | 0.167 | 0.167 |
| 3.3-4.2 | 0.111 | 0.111 | 0.056 | 0.222 | 0.148 | 0.148 | 0.204 |
| 4.2-5.1 | 0.038 | 0.132 | 0.075 | 0.245 | 0.094 | 0.283 | 0.132 |
| 5.1-6.0 | 0.057 | 0.170 | 0.057 | 0.170 | 0.151 | 0.189 | 0.208 |
| 6.0-6.9 | 0.208 | 0.132 | 0.132 | 0.189 | 0.113 | 0.113 | 0.113 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1388)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.9245, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.816 | 0.184 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.037 | 0.000 | 0.889 | 0.074 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.037 | 0.833 | 0.130 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.019 | 0.944 | 0.037 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 | 0.075 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 | 0.075 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.038 | 0.925 | 0.038 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1201)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.3585, support=53
- `5.1-6.0`: recall=0.2453, support=53
- `6.0-6.9`: recall=0.0755, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.026 | 0.026 | 0.000 | 0.447 | 0.342 | 0.158 |
| 1.5-2.4 | 0.000 | 0.037 | 0.074 | 0.019 | 0.519 | 0.315 | 0.037 |
| 2.4-3.3 | 0.019 | 0.130 | 0.019 | 0.000 | 0.370 | 0.333 | 0.130 |
| 3.3-4.2 | 0.019 | 0.111 | 0.111 | 0.056 | 0.370 | 0.296 | 0.037 |
| 4.2-5.1 | 0.019 | 0.170 | 0.019 | 0.000 | 0.358 | 0.321 | 0.113 |
| 5.1-6.0 | 0.000 | 0.151 | 0.057 | 0.000 | 0.377 | 0.245 | 0.170 |
| 6.0-6.9 | 0.038 | 0.113 | 0.019 | 0.038 | 0.415 | 0.302 | 0.075 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2268)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.143 | 0.000 | 0.071 | 0.429 | 0.071 |
| 1.5-2.4 | 0.000 | 0.333 | 0.111 | 0.000 | 0.000 | 0.500 | 0.056 |
| 2.4-3.3 | 0.000 | 0.278 | 0.111 | 0.056 | 0.056 | 0.444 | 0.056 |
| 3.3-4.2 | 0.000 | 0.176 | 0.118 | 0.059 | 0.118 | 0.529 | 0.000 |
| 4.2-5.1 | 0.000 | 0.111 | 0.000 | 0.000 | 0.222 | 0.556 | 0.111 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.278 | 0.056 | 0.556 | 0.056 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.222 | 0.111 | 0.500 | 0.167 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2052)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.000 | 0.071 | 0.000 | 0.214 | 0.357 |
| 1.5-2.4 | 0.000 | 0.333 | 0.000 | 0.167 | 0.056 | 0.222 | 0.222 |
| 2.4-3.3 | 0.000 | 0.278 | 0.000 | 0.111 | 0.222 | 0.333 | 0.056 |
| 3.3-4.2 | 0.000 | 0.176 | 0.059 | 0.176 | 0.000 | 0.471 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.000 | 0.444 | 0.111 | 0.222 | 0.167 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 | 0.389 | 0.111 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.556 | 0.000 | 0.222 | 0.222 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1973)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.6667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.000 | 0.000 | 0.429 | 0.071 |
| 1.5-2.4 | 0.000 | 0.444 | 0.056 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.056 | 0.333 | 0.000 | 0.056 | 0.056 | 0.444 | 0.056 |
| 3.3-4.2 | 0.000 | 0.235 | 0.000 | 0.000 | 0.059 | 0.588 | 0.118 |
| 4.2-5.1 | 0.000 | 0.111 | 0.000 | 0.167 | 0.000 | 0.667 | 0.056 |
| 5.1-6.0 | 0.000 | 0.222 | 0.000 | 0.000 | 0.000 | 0.667 | 0.111 |
| 6.0-6.9 | 0.000 | 0.167 | 0.000 | 0.000 | 0.056 | 0.722 | 0.056 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1810)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.000 | 0.000 | 0.143 | 0.214 | 0.143 |
| 1.5-2.4 | 0.167 | 0.056 | 0.056 | 0.278 | 0.167 | 0.222 | 0.056 |
| 2.4-3.3 | 0.167 | 0.000 | 0.167 | 0.222 | 0.222 | 0.111 | 0.111 |
| 3.3-4.2 | 0.059 | 0.059 | 0.176 | 0.176 | 0.000 | 0.294 | 0.235 |
| 4.2-5.1 | 0.167 | 0.056 | 0.056 | 0.167 | 0.056 | 0.167 | 0.333 |
| 5.1-6.0 | 0.111 | 0.000 | 0.167 | 0.389 | 0.111 | 0.056 | 0.167 |
| 6.0-6.9 | 0.000 | 0.111 | 0.167 | 0.111 | 0.111 | 0.111 | 0.389 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1620)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2353, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.286 | 0.143 | 0.286 | 0.143 | 0.000 | 0.071 |
| 1.5-2.4 | 0.000 | 0.222 | 0.111 | 0.333 | 0.222 | 0.000 | 0.111 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.333 | 0.333 | 0.000 | 0.056 |
| 3.3-4.2 | 0.000 | 0.412 | 0.000 | 0.235 | 0.118 | 0.118 | 0.118 |
| 4.2-5.1 | 0.000 | 0.111 | 0.000 | 0.500 | 0.278 | 0.000 | 0.111 |
| 5.1-6.0 | 0.000 | 0.278 | 0.111 | 0.167 | 0.222 | 0.111 | 0.111 |
| 6.0-6.9 | 0.000 | 0.111 | 0.000 | 0.333 | 0.167 | 0.278 | 0.111 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1349)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.429 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.500 | 0.444 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.471 | 0.529 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.929 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.111 | 0.444 | 0.167 | 0.111 | 0.111 | 0.056 | 0.000 |
| 2.4-3.3 | 0.056 | 0.222 | 0.000 | 0.444 | 0.056 | 0.111 | 0.111 |
| 3.3-4.2 | 0.056 | 0.167 | 0.167 | 0.056 | 0.222 | 0.167 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.353 | 0.118 | 0.235 | 0.235 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.167 | 0.278 | 0.389 | 0.056 |
| 6.0-6.9 | 0.056 | 0.111 | 0.056 | 0.111 | 0.167 | 0.278 | 0.222 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.286 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.056 | 0.500 | 0.278 | 0.056 | 0.111 | 0.000 | 0.000 |
| 2.4-3.3 | 0.111 | 0.278 | 0.167 | 0.111 | 0.111 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.278 | 0.056 | 0.167 | 0.278 | 0.111 | 0.056 |
| 4.2-5.1 | 0.000 | 0.176 | 0.059 | 0.176 | 0.118 | 0.235 | 0.235 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.222 | 0.278 | 0.333 | 0.111 |
| 6.0-6.9 | 0.111 | 0.056 | 0.222 | 0.167 | 0.278 | 0.056 | 0.111 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.071 | 0.143 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.167 | 0.444 | 0.167 | 0.000 | 0.000 | 0.111 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.333 | 0.111 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.167 | 0.056 | 0.111 | 0.111 | 0.222 | 0.222 |
| 4.2-5.1 | 0.000 | 0.118 | 0.176 | 0.294 | 0.176 | 0.176 | 0.059 |
| 5.1-6.0 | 0.000 | 0.000 | 0.222 | 0.278 | 0.222 | 0.278 | 0.000 |
| 6.0-6.9 | 0.056 | 0.056 | 0.056 | 0.111 | 0.167 | 0.333 | 0.222 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.3333, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.000 | 0.286 | 0.000 | 0.000 | 0.071 |
| 1.5-2.4 | 0.056 | 0.333 | 0.111 | 0.167 | 0.056 | 0.222 | 0.056 |
| 2.4-3.3 | 0.000 | 0.056 | 0.167 | 0.444 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.056 | 0.111 | 0.111 | 0.333 | 0.222 | 0.056 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.353 | 0.176 | 0.176 | 0.176 |
| 5.1-6.0 | 0.056 | 0.111 | 0.111 | 0.111 | 0.222 | 0.222 | 0.167 |
| 6.0-6.9 | 0.056 | 0.111 | 0.167 | 0.111 | 0.278 | 0.167 | 0.111 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.286 | 0.071 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.111 | 0.278 | 0.222 | 0.000 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.056 | 0.222 | 0.111 | 0.056 | 0.222 | 0.222 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.222 | 0.111 | 0.333 | 0.167 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.176 | 0.059 | 0.176 | 0.235 | 0.353 |
| 5.1-6.0 | 0.000 | 0.111 | 0.000 | 0.222 | 0.278 | 0.278 | 0.111 |
| 6.0-6.9 | 0.000 | 0.167 | 0.111 | 0.111 | 0.333 | 0.222 | 0.056 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.071 | 0.000 | 0.000 | 0.000 | 0.143 |
| 1.5-2.4 | 0.167 | 0.389 | 0.111 | 0.111 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.111 | 0.222 | 0.000 | 0.222 | 0.278 | 0.056 | 0.111 |
| 3.3-4.2 | 0.167 | 0.111 | 0.111 | 0.111 | 0.278 | 0.056 | 0.167 |
| 4.2-5.1 | 0.059 | 0.118 | 0.118 | 0.176 | 0.294 | 0.059 | 0.176 |
| 5.1-6.0 | 0.111 | 0.111 | 0.000 | 0.056 | 0.389 | 0.167 | 0.167 |
| 6.0-6.9 | 0.056 | 0.167 | 0.000 | 0.167 | 0.444 | 0.056 | 0.111 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.143 | 0.143 | 0.214 | 0.143 | 0.000 |
| 1.5-2.4 | 0.056 | 0.222 | 0.222 | 0.222 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.000 | 0.111 | 0.111 | 0.278 | 0.222 | 0.167 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.111 | 0.111 | 0.278 | 0.222 | 0.111 |
| 4.2-5.1 | 0.118 | 0.118 | 0.118 | 0.176 | 0.059 | 0.235 | 0.176 |
| 5.1-6.0 | 0.056 | 0.111 | 0.111 | 0.167 | 0.278 | 0.056 | 0.222 |
| 6.0-6.9 | 0.111 | 0.167 | 0.111 | 0.111 | 0.222 | 0.222 | 0.056 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1691)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.1852, support=54
- `3.3-4.2`: recall=0.1667, support=54
- `4.2-5.1`: recall=0.1321, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.3208, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.026 | 0.132 | 0.079 | 0.158 | 0.158 | 0.316 |
| 1.5-2.4 | 0.000 | 0.130 | 0.241 | 0.204 | 0.093 | 0.130 | 0.204 |
| 2.4-3.3 | 0.019 | 0.056 | 0.185 | 0.148 | 0.111 | 0.204 | 0.278 |
| 3.3-4.2 | 0.056 | 0.074 | 0.130 | 0.167 | 0.093 | 0.278 | 0.204 |
| 4.2-5.1 | 0.000 | 0.075 | 0.094 | 0.208 | 0.132 | 0.189 | 0.302 |
| 5.1-6.0 | 0.000 | 0.151 | 0.075 | 0.151 | 0.075 | 0.208 | 0.340 |
| 6.0-6.9 | 0.000 | 0.151 | 0.075 | 0.151 | 0.057 | 0.245 | 0.321 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1608)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.1481, support=54
- `3.3-4.2`: recall=0.0741, support=54
- `4.2-5.1`: recall=0.2453, support=53
- `5.1-6.0`: recall=0.1887, support=53
- `6.0-6.9`: recall=0.1887, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.079 | 0.079 | 0.184 | 0.000 | 0.158 | 0.237 | 0.263 |
| 1.5-2.4 | 0.148 | 0.185 | 0.241 | 0.037 | 0.222 | 0.074 | 0.093 |
| 2.4-3.3 | 0.222 | 0.185 | 0.148 | 0.130 | 0.185 | 0.074 | 0.056 |
| 3.3-4.2 | 0.167 | 0.222 | 0.204 | 0.074 | 0.167 | 0.037 | 0.130 |
| 4.2-5.1 | 0.170 | 0.132 | 0.113 | 0.094 | 0.245 | 0.151 | 0.094 |
| 5.1-6.0 | 0.170 | 0.075 | 0.094 | 0.151 | 0.226 | 0.189 | 0.094 |
| 6.0-6.9 | 0.170 | 0.075 | 0.094 | 0.132 | 0.094 | 0.245 | 0.189 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1602)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1111, support=54
- `3.3-4.2`: recall=0.3148, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1132, support=53
- `6.0-6.9`: recall=0.1132, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.184 | 0.026 | 0.132 | 0.105 | 0.158 | 0.211 |
| 1.5-2.4 | 0.130 | 0.167 | 0.037 | 0.167 | 0.167 | 0.130 | 0.204 |
| 2.4-3.3 | 0.074 | 0.130 | 0.111 | 0.278 | 0.093 | 0.167 | 0.148 |
| 3.3-4.2 | 0.259 | 0.111 | 0.000 | 0.315 | 0.074 | 0.074 | 0.167 |
| 4.2-5.1 | 0.132 | 0.189 | 0.075 | 0.151 | 0.094 | 0.170 | 0.189 |
| 5.1-6.0 | 0.132 | 0.245 | 0.019 | 0.208 | 0.094 | 0.113 | 0.189 |
| 6.0-6.9 | 0.245 | 0.094 | 0.113 | 0.075 | 0.132 | 0.226 | 0.113 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1564)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `1.5-2.4`: recall=0.2963, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.2264, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.132 | 0.079 | 0.132 | 0.000 | 0.105 | 0.421 |
| 1.5-2.4 | 0.037 | 0.296 | 0.056 | 0.093 | 0.204 | 0.185 | 0.130 |
| 2.4-3.3 | 0.111 | 0.204 | 0.056 | 0.130 | 0.037 | 0.241 | 0.222 |
| 3.3-4.2 | 0.074 | 0.222 | 0.019 | 0.148 | 0.111 | 0.407 | 0.019 |
| 4.2-5.1 | 0.094 | 0.170 | 0.057 | 0.132 | 0.038 | 0.340 | 0.170 |
| 5.1-6.0 | 0.038 | 0.189 | 0.075 | 0.170 | 0.038 | 0.208 | 0.283 |
| 6.0-6.9 | 0.094 | 0.132 | 0.075 | 0.113 | 0.094 | 0.264 | 0.226 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1528)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.3208, support=53
- `6.0-6.9`: recall=0.1321, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.105 | 0.026 | 0.237 | 0.105 | 0.184 | 0.158 |
| 1.5-2.4 | 0.093 | 0.130 | 0.000 | 0.204 | 0.093 | 0.204 | 0.278 |
| 2.4-3.3 | 0.093 | 0.074 | 0.019 | 0.259 | 0.093 | 0.241 | 0.222 |
| 3.3-4.2 | 0.130 | 0.000 | 0.019 | 0.241 | 0.148 | 0.333 | 0.130 |
| 4.2-5.1 | 0.075 | 0.019 | 0.019 | 0.302 | 0.057 | 0.302 | 0.226 |
| 5.1-6.0 | 0.094 | 0.038 | 0.000 | 0.302 | 0.019 | 0.321 | 0.226 |
| 6.0-6.9 | 0.113 | 0.019 | 0.094 | 0.245 | 0.038 | 0.358 | 0.132 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1388)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.9245, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.816 | 0.184 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.037 | 0.000 | 0.889 | 0.074 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.037 | 0.833 | 0.130 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.019 | 0.944 | 0.037 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 | 0.075 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 | 0.075 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.038 | 0.925 | 0.038 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1301)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.3774, support=53
- `5.1-6.0`: recall=0.3208, support=53
- `6.0-6.9`: recall=0.0189, support=53

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.053 | 0.053 | 0.000 | 0.316 | 0.447 | 0.132 |
| 1.5-2.4 | 0.019 | 0.056 | 0.074 | 0.019 | 0.463 | 0.333 | 0.037 |
| 2.4-3.3 | 0.019 | 0.130 | 0.056 | 0.000 | 0.333 | 0.370 | 0.093 |
| 3.3-4.2 | 0.019 | 0.111 | 0.130 | 0.056 | 0.296 | 0.370 | 0.019 |
| 4.2-5.1 | 0.019 | 0.170 | 0.038 | 0.000 | 0.377 | 0.358 | 0.038 |
| 5.1-6.0 | 0.000 | 0.170 | 0.057 | 0.000 | 0.396 | 0.321 | 0.057 |
| 6.0-6.9 | 0.057 | 0.132 | 0.038 | 0.038 | 0.396 | 0.321 | 0.019 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1576)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.286 | 0.000 | 0.000 | 0.143 | 0.214 |
| 1.5-2.4 | 0.167 | 0.111 | 0.222 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.333 | 0.000 | 0.111 | 0.000 | 0.000 | 0.222 | 0.333 |
| 3.3-4.2 | 0.235 | 0.000 | 0.118 | 0.000 | 0.000 | 0.353 | 0.294 |
| 4.2-5.1 | 0.000 | 0.000 | 0.389 | 0.000 | 0.000 | 0.333 | 0.278 |
| 5.1-6.0 | 0.056 | 0.000 | 0.333 | 0.000 | 0.000 | 0.444 | 0.167 |
| 6.0-6.9 | 0.000 | 0.000 | 0.444 | 0.000 | 0.056 | 0.278 | 0.222 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1451)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.286 | 0.000 | 0.000 | 0.000 | 0.500 | 0.143 |
| 1.5-2.4 | 0.000 | 0.278 | 0.222 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.056 | 0.389 | 0.000 | 0.000 | 0.056 | 0.500 | 0.000 |
| 3.3-4.2 | 0.059 | 0.294 | 0.118 | 0.000 | 0.000 | 0.471 | 0.059 |
| 4.2-5.1 | 0.111 | 0.000 | 0.111 | 0.000 | 0.000 | 0.556 | 0.222 |
| 5.1-6.0 | 0.167 | 0.056 | 0.222 | 0.000 | 0.000 | 0.500 | 0.056 |
| 6.0-6.9 | 0.278 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 | 0.167 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1349)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.429 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.500 | 0.444 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.471 | 0.529 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1190)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.214 | 0.214 | 0.143 | 0.071 | 0.214 | 0.143 |
| 1.5-2.4 | 0.111 | 0.444 | 0.111 | 0.000 | 0.056 | 0.167 | 0.111 |
| 2.4-3.3 | 0.167 | 0.389 | 0.056 | 0.111 | 0.111 | 0.167 | 0.000 |
| 3.3-4.2 | 0.294 | 0.353 | 0.059 | 0.059 | 0.059 | 0.118 | 0.059 |
| 4.2-5.1 | 0.056 | 0.111 | 0.111 | 0.333 | 0.056 | 0.167 | 0.167 |
| 5.1-6.0 | 0.000 | 0.111 | 0.222 | 0.444 | 0.056 | 0.167 | 0.000 |
| 6.0-6.9 | 0.000 | 0.333 | 0.000 | 0.333 | 0.167 | 0.111 | 0.056 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1111)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.071 | 0.286 | 0.000 | 0.071 | 0.286 | 0.286 |
| 1.5-2.4 | 0.000 | 0.111 | 0.167 | 0.000 | 0.222 | 0.167 | 0.333 |
| 2.4-3.3 | 0.000 | 0.222 | 0.167 | 0.111 | 0.000 | 0.222 | 0.278 |
| 3.3-4.2 | 0.000 | 0.059 | 0.353 | 0.118 | 0.000 | 0.412 | 0.059 |
| 4.2-5.1 | 0.000 | 0.000 | 0.389 | 0.111 | 0.000 | 0.389 | 0.111 |
| 5.1-6.0 | 0.000 | 0.000 | 0.444 | 0.056 | 0.000 | 0.333 | 0.167 |
| 6.0-6.9 | 0.000 | 0.056 | 0.444 | 0.000 | 0.000 | 0.444 | 0.056 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.0952)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.357 | 0.071 | 0.000 | 0.000 | 0.429 | 0.143 |
| 1.5-2.4 | 0.000 | 0.111 | 0.167 | 0.056 | 0.111 | 0.333 | 0.222 |
| 2.4-3.3 | 0.000 | 0.333 | 0.056 | 0.111 | 0.056 | 0.222 | 0.222 |
| 3.3-4.2 | 0.000 | 0.235 | 0.000 | 0.176 | 0.000 | 0.529 | 0.059 |
| 4.2-5.1 | 0.000 | 0.000 | 0.167 | 0.222 | 0.000 | 0.444 | 0.167 |
| 5.1-6.0 | 0.000 | 0.167 | 0.333 | 0.111 | 0.000 | 0.333 | 0.056 |
| 6.0-6.9 | 0.000 | 0.111 | 0.333 | 0.000 | 0.056 | 0.500 | 0.000 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.4214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.786 | 0.071 | 0.071 | 0.000 | 0.071 | 0.000 | 0.000 |
| 1.5-2.4 | 0.056 | 0.500 | 0.167 | 0.111 | 0.056 | 0.056 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.278 | 0.222 | 0.167 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.111 | 0.167 | 0.167 | 0.222 | 0.167 |
| 4.2-5.1 | 0.000 | 0.118 | 0.118 | 0.176 | 0.353 | 0.176 | 0.059 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.111 | 0.111 | 0.556 | 0.167 |
| 6.0-6.9 | 0.111 | 0.056 | 0.000 | 0.167 | 0.056 | 0.389 | 0.222 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.4118, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.214 | 0.071 | 0.000 | 0.000 | 0.143 |
| 1.5-2.4 | 0.000 | 0.389 | 0.222 | 0.222 | 0.056 | 0.056 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.167 | 0.333 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.167 | 0.222 | 0.111 | 0.167 | 0.167 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.235 | 0.412 | 0.118 | 0.118 |
| 5.1-6.0 | 0.000 | 0.056 | 0.167 | 0.111 | 0.111 | 0.444 | 0.111 |
| 6.0-6.9 | 0.111 | 0.111 | 0.167 | 0.056 | 0.167 | 0.222 | 0.167 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.071 | 0.000 | 0.000 | 0.071 | 0.000 |
| 1.5-2.4 | 0.167 | 0.389 | 0.056 | 0.056 | 0.167 | 0.056 | 0.111 |
| 2.4-3.3 | 0.111 | 0.389 | 0.111 | 0.111 | 0.111 | 0.111 | 0.056 |
| 3.3-4.2 | 0.167 | 0.222 | 0.111 | 0.167 | 0.222 | 0.111 | 0.000 |
| 4.2-5.1 | 0.059 | 0.118 | 0.059 | 0.235 | 0.353 | 0.118 | 0.059 |
| 5.1-6.0 | 0.111 | 0.167 | 0.056 | 0.000 | 0.278 | 0.389 | 0.000 |
| 6.0-6.9 | 0.056 | 0.111 | 0.000 | 0.167 | 0.333 | 0.278 | 0.056 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.286 | 0.071 | 0.000 | 0.071 | 0.071 |
| 1.5-2.4 | 0.167 | 0.333 | 0.111 | 0.167 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.056 | 0.278 | 0.167 | 0.278 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.167 | 0.278 | 0.222 | 0.167 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.176 | 0.176 | 0.412 | 0.176 |
| 5.1-6.0 | 0.000 | 0.111 | 0.111 | 0.000 | 0.222 | 0.444 | 0.111 |
| 6.0-6.9 | 0.000 | 0.222 | 0.056 | 0.000 | 0.278 | 0.278 | 0.167 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.714 | 0.214 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.111 | 0.389 | 0.056 | 0.111 | 0.000 | 0.222 | 0.111 |
| 2.4-3.3 | 0.111 | 0.444 | 0.000 | 0.278 | 0.056 | 0.056 | 0.056 |
| 3.3-4.2 | 0.056 | 0.278 | 0.111 | 0.278 | 0.056 | 0.222 | 0.000 |
| 4.2-5.1 | 0.118 | 0.294 | 0.000 | 0.176 | 0.118 | 0.176 | 0.118 |
| 5.1-6.0 | 0.111 | 0.000 | 0.056 | 0.222 | 0.111 | 0.278 | 0.222 |
| 6.0-6.9 | 0.222 | 0.056 | 0.056 | 0.167 | 0.056 | 0.333 | 0.111 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.071 | 0.143 | 0.214 | 0.071 | 0.071 | 0.071 |
| 1.5-2.4 | 0.167 | 0.111 | 0.111 | 0.167 | 0.111 | 0.167 | 0.167 |
| 2.4-3.3 | 0.111 | 0.222 | 0.056 | 0.333 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.167 | 0.056 | 0.222 | 0.222 | 0.222 | 0.056 |
| 4.2-5.1 | 0.118 | 0.118 | 0.059 | 0.059 | 0.294 | 0.294 | 0.059 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.056 | 0.111 | 0.389 | 0.278 |
| 6.0-6.9 | 0.167 | 0.111 | 0.056 | 0.111 | 0.222 | 0.111 | 0.222 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_easiest_baseline/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.143 | 0.143 | 0.214 | 0.143 | 0.000 |
| 1.5-2.4 | 0.056 | 0.222 | 0.167 | 0.278 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.056 | 0.167 | 0.278 | 0.167 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.111 | 0.222 | 0.167 | 0.222 | 0.111 |
| 4.2-5.1 | 0.118 | 0.118 | 0.118 | 0.235 | 0.059 | 0.235 | 0.118 |
| 5.1-6.0 | 0.056 | 0.111 | 0.167 | 0.167 | 0.222 | 0.056 | 0.222 |
| 6.0-6.9 | 0.111 | 0.167 | 0.111 | 0.167 | 0.167 | 0.222 | 0.056 |


# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_omit_hardest_baseline.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2432, support=37
- `0.6-1.5`: recall=0.0943, support=53
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.2264, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.243 | 0.108 | 0.135 | 0.216 | 0.216 | 0.081 | 0.000 |
| 0.6-1.5 | 0.075 | 0.094 | 0.302 | 0.113 | 0.283 | 0.038 | 0.094 |
| 1.5-2.4 | 0.056 | 0.130 | 0.222 | 0.111 | 0.278 | 0.019 | 0.185 |
| 2.4-3.3 | 0.118 | 0.020 | 0.294 | 0.176 | 0.255 | 0.118 | 0.020 |
| 3.3-4.2 | 0.113 | 0.057 | 0.208 | 0.094 | 0.226 | 0.170 | 0.132 |
| 4.2-5.1 | 0.098 | 0.039 | 0.235 | 0.157 | 0.176 | 0.196 | 0.098 |
| 5.1-6.0 | 0.077 | 0.096 | 0.173 | 0.115 | 0.269 | 0.173 | 0.096 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1670)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.0755, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.2941, support=51
- `5.1-6.0`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.054 | 0.054 | 0.162 | 0.270 | 0.162 | 0.027 |
| 0.6-1.5 | 0.208 | 0.075 | 0.226 | 0.094 | 0.132 | 0.189 | 0.075 |
| 1.5-2.4 | 0.241 | 0.148 | 0.111 | 0.204 | 0.111 | 0.111 | 0.074 |
| 2.4-3.3 | 0.255 | 0.000 | 0.216 | 0.176 | 0.137 | 0.137 | 0.078 |
| 3.3-4.2 | 0.208 | 0.000 | 0.245 | 0.113 | 0.132 | 0.208 | 0.094 |
| 4.2-5.1 | 0.235 | 0.020 | 0.118 | 0.098 | 0.176 | 0.294 | 0.059 |
| 5.1-6.0 | 0.346 | 0.135 | 0.077 | 0.135 | 0.058 | 0.192 | 0.058 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1506)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.162 | 0.027 | 0.270 | 0.270 | 0.081 | 0.081 |
| 0.6-1.5 | 0.264 | 0.189 | 0.113 | 0.075 | 0.113 | 0.151 | 0.094 |
| 1.5-2.4 | 0.204 | 0.167 | 0.111 | 0.111 | 0.185 | 0.074 | 0.148 |
| 2.4-3.3 | 0.196 | 0.118 | 0.157 | 0.059 | 0.196 | 0.098 | 0.176 |
| 3.3-4.2 | 0.132 | 0.075 | 0.094 | 0.094 | 0.245 | 0.113 | 0.245 |
| 4.2-5.1 | 0.176 | 0.157 | 0.078 | 0.078 | 0.118 | 0.216 | 0.176 |
| 5.1-6.0 | 0.269 | 0.192 | 0.077 | 0.058 | 0.154 | 0.115 | 0.135 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1386)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.108 | 0.135 | 0.135 | 0.162 | 0.216 | 0.135 | 0.108 |
| 0.6-1.5 | 0.189 | 0.208 | 0.113 | 0.075 | 0.226 | 0.113 | 0.075 |
| 1.5-2.4 | 0.167 | 0.185 | 0.130 | 0.093 | 0.167 | 0.148 | 0.111 |
| 2.4-3.3 | 0.176 | 0.157 | 0.157 | 0.098 | 0.137 | 0.137 | 0.137 |
| 3.3-4.2 | 0.170 | 0.113 | 0.075 | 0.094 | 0.189 | 0.113 | 0.245 |
| 4.2-5.1 | 0.196 | 0.255 | 0.078 | 0.098 | 0.118 | 0.059 | 0.196 |
| 5.1-6.0 | 0.212 | 0.135 | 0.173 | 0.058 | 0.192 | 0.096 | 0.135 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1359)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.0189, support=53
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.3137, support=51
- `5.1-6.0`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.027 | 0.189 | 0.135 | 0.135 | 0.162 | 0.081 |
| 0.6-1.5 | 0.245 | 0.019 | 0.170 | 0.075 | 0.170 | 0.208 | 0.113 |
| 1.5-2.4 | 0.259 | 0.037 | 0.093 | 0.185 | 0.148 | 0.148 | 0.130 |
| 2.4-3.3 | 0.294 | 0.059 | 0.176 | 0.059 | 0.137 | 0.196 | 0.078 |
| 3.3-4.2 | 0.170 | 0.000 | 0.151 | 0.132 | 0.189 | 0.264 | 0.094 |
| 4.2-5.1 | 0.137 | 0.020 | 0.078 | 0.157 | 0.176 | 0.314 | 0.118 |
| 5.1-6.0 | 0.231 | 0.077 | 0.058 | 0.154 | 0.154 | 0.250 | 0.077 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1348)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1622, support=37
- `0.6-1.5`: recall=0.0755, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.3529, support=51
- `5.1-6.0`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.162 | 0.081 | 0.135 | 0.243 | 0.162 | 0.216 | 0.000 |
| 0.6-1.5 | 0.245 | 0.075 | 0.113 | 0.170 | 0.094 | 0.264 | 0.038 |
| 1.5-2.4 | 0.222 | 0.130 | 0.111 | 0.167 | 0.074 | 0.241 | 0.056 |
| 2.4-3.3 | 0.196 | 0.078 | 0.216 | 0.157 | 0.059 | 0.275 | 0.020 |
| 3.3-4.2 | 0.208 | 0.075 | 0.132 | 0.208 | 0.038 | 0.321 | 0.019 |
| 4.2-5.1 | 0.176 | 0.078 | 0.137 | 0.196 | 0.039 | 0.353 | 0.020 |
| 5.1-6.0 | 0.192 | 0.115 | 0.115 | 0.173 | 0.058 | 0.308 | 0.038 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1318)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.0943, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.054 | 0.135 | 0.270 | 0.189 | 0.243 | 0.054 | 0.054 |
| 0.6-1.5 | 0.151 | 0.189 | 0.245 | 0.075 | 0.094 | 0.151 | 0.094 |
| 1.5-2.4 | 0.259 | 0.185 | 0.167 | 0.093 | 0.074 | 0.056 | 0.167 |
| 2.4-3.3 | 0.235 | 0.157 | 0.176 | 0.059 | 0.157 | 0.098 | 0.118 |
| 3.3-4.2 | 0.170 | 0.113 | 0.151 | 0.075 | 0.094 | 0.170 | 0.226 |
| 4.2-5.1 | 0.176 | 0.098 | 0.118 | 0.078 | 0.157 | 0.196 | 0.176 |
| 5.1-6.0 | 0.212 | 0.135 | 0.096 | 0.115 | 0.096 | 0.192 | 0.154 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2127)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.286 | 0.000 | 0.000 | 0.143 | 0.286 |
| 0.6-1.5 | 0.000 | 0.125 | 0.250 | 0.000 | 0.188 | 0.062 | 0.375 |
| 1.5-2.4 | 0.062 | 0.188 | 0.188 | 0.312 | 0.125 | 0.062 | 0.062 |
| 2.4-3.3 | 0.059 | 0.118 | 0.118 | 0.176 | 0.000 | 0.176 | 0.353 |
| 3.3-4.2 | 0.353 | 0.000 | 0.176 | 0.118 | 0.059 | 0.118 | 0.176 |
| 4.2-5.1 | 0.056 | 0.000 | 0.056 | 0.167 | 0.056 | 0.389 | 0.278 |
| 5.1-6.0 | 0.056 | 0.278 | 0.000 | 0.000 | 0.222 | 0.056 | 0.389 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2052)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.071 | 0.071 | 0.000 | 0.286 | 0.000 |
| 0.6-1.5 | 0.812 | 0.000 | 0.062 | 0.000 | 0.000 | 0.125 | 0.000 |
| 1.5-2.4 | 0.312 | 0.062 | 0.188 | 0.125 | 0.000 | 0.312 | 0.000 |
| 2.4-3.3 | 0.235 | 0.000 | 0.294 | 0.059 | 0.000 | 0.412 | 0.000 |
| 3.3-4.2 | 0.353 | 0.000 | 0.235 | 0.176 | 0.000 | 0.235 | 0.000 |
| 4.2-5.1 | 0.278 | 0.000 | 0.056 | 0.056 | 0.000 | 0.611 | 0.000 |
| 5.1-6.0 | 0.500 | 0.000 | 0.056 | 0.167 | 0.000 | 0.278 | 0.000 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1866)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.3750, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.214 | 0.071 | 0.286 | 0.000 | 0.286 | 0.071 |
| 0.6-1.5 | 0.125 | 0.375 | 0.125 | 0.125 | 0.000 | 0.125 | 0.125 |
| 1.5-2.4 | 0.125 | 0.125 | 0.000 | 0.375 | 0.188 | 0.125 | 0.062 |
| 2.4-3.3 | 0.176 | 0.000 | 0.235 | 0.176 | 0.059 | 0.235 | 0.118 |
| 3.3-4.2 | 0.059 | 0.059 | 0.176 | 0.294 | 0.059 | 0.118 | 0.235 |
| 4.2-5.1 | 0.000 | 0.056 | 0.056 | 0.278 | 0.167 | 0.333 | 0.111 |
| 5.1-6.0 | 0.056 | 0.111 | 0.167 | 0.056 | 0.111 | 0.222 | 0.278 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1810)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.071 | 0.214 | 0.286 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.500 | 0.000 | 0.312 | 0.062 | 0.062 | 0.062 | 0.000 |
| 1.5-2.4 | 0.312 | 0.062 | 0.188 | 0.375 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.353 | 0.059 | 0.118 | 0.176 | 0.000 | 0.235 | 0.059 |
| 3.3-4.2 | 0.176 | 0.059 | 0.176 | 0.235 | 0.000 | 0.294 | 0.059 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.222 | 0.056 | 0.611 | 0.000 |
| 5.1-6.0 | 0.278 | 0.000 | 0.111 | 0.278 | 0.111 | 0.222 | 0.000 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1798)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.286 | 0.000 | 0.000 | 0.143 | 0.000 |
| 0.6-1.5 | 0.500 | 0.000 | 0.312 | 0.000 | 0.125 | 0.000 | 0.062 |
| 1.5-2.4 | 0.500 | 0.312 | 0.188 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.471 | 0.118 | 0.118 | 0.235 | 0.000 | 0.059 | 0.000 |
| 3.3-4.2 | 0.353 | 0.000 | 0.294 | 0.176 | 0.000 | 0.176 | 0.000 |
| 4.2-5.1 | 0.444 | 0.000 | 0.000 | 0.167 | 0.000 | 0.333 | 0.056 |
| 5.1-6.0 | 0.556 | 0.056 | 0.111 | 0.111 | 0.056 | 0.111 | 0.000 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1300)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.214 | 0.000 | 0.071 | 0.214 | 0.214 |
| 0.6-1.5 | 0.375 | 0.125 | 0.250 | 0.062 | 0.125 | 0.062 | 0.000 |
| 1.5-2.4 | 0.312 | 0.188 | 0.188 | 0.188 | 0.000 | 0.125 | 0.000 |
| 2.4-3.3 | 0.471 | 0.118 | 0.059 | 0.176 | 0.059 | 0.118 | 0.000 |
| 3.3-4.2 | 0.235 | 0.000 | 0.235 | 0.294 | 0.000 | 0.059 | 0.176 |
| 4.2-5.1 | 0.056 | 0.000 | 0.111 | 0.500 | 0.000 | 0.167 | 0.167 |
| 5.1-6.0 | 0.333 | 0.222 | 0.222 | 0.056 | 0.056 | 0.056 | 0.056 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.0916)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.2353, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.000 | 0.071 | 0.286 | 0.071 | 0.429 | 0.143 |
| 0.6-1.5 | 0.062 | 0.062 | 0.062 | 0.188 | 0.188 | 0.312 | 0.125 |
| 1.5-2.4 | 0.188 | 0.250 | 0.000 | 0.375 | 0.062 | 0.062 | 0.062 |
| 2.4-3.3 | 0.353 | 0.294 | 0.000 | 0.059 | 0.059 | 0.118 | 0.118 |
| 3.3-4.2 | 0.176 | 0.118 | 0.000 | 0.176 | 0.235 | 0.235 | 0.059 |
| 4.2-5.1 | 0.000 | 0.111 | 0.056 | 0.444 | 0.167 | 0.167 | 0.056 |
| 5.1-6.0 | 0.056 | 0.111 | 0.000 | 0.111 | 0.056 | 0.556 | 0.111 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.143 | 0.071 | 0.071 | 0.214 | 0.071 |
| 0.6-1.5 | 0.167 | 0.222 | 0.111 | 0.278 | 0.056 | 0.000 | 0.167 |
| 1.5-2.4 | 0.222 | 0.111 | 0.111 | 0.222 | 0.000 | 0.111 | 0.222 |
| 2.4-3.3 | 0.222 | 0.278 | 0.111 | 0.111 | 0.000 | 0.222 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.111 | 0.167 | 0.222 | 0.111 | 0.167 |
| 4.2-5.1 | 0.167 | 0.056 | 0.167 | 0.167 | 0.111 | 0.278 | 0.056 |
| 5.1-6.0 | 0.056 | 0.167 | 0.111 | 0.000 | 0.167 | 0.167 | 0.333 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.357 | 0.143 | 0.071 | 0.143 | 0.000 |
| 0.6-1.5 | 0.056 | 0.444 | 0.056 | 0.056 | 0.222 | 0.000 | 0.167 |
| 1.5-2.4 | 0.389 | 0.000 | 0.056 | 0.111 | 0.056 | 0.167 | 0.222 |
| 2.4-3.3 | 0.278 | 0.111 | 0.111 | 0.167 | 0.111 | 0.111 | 0.111 |
| 3.3-4.2 | 0.056 | 0.222 | 0.056 | 0.111 | 0.222 | 0.056 | 0.278 |
| 4.2-5.1 | 0.111 | 0.056 | 0.111 | 0.056 | 0.111 | 0.278 | 0.278 |
| 5.1-6.0 | 0.000 | 0.222 | 0.056 | 0.111 | 0.222 | 0.167 | 0.222 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.286 | 0.143 | 0.143 | 0.000 | 0.143 | 0.143 | 0.143 |
| 0.6-1.5 | 0.222 | 0.222 | 0.167 | 0.111 | 0.167 | 0.056 | 0.056 |
| 1.5-2.4 | 0.333 | 0.056 | 0.222 | 0.167 | 0.000 | 0.167 | 0.056 |
| 2.4-3.3 | 0.111 | 0.278 | 0.111 | 0.056 | 0.167 | 0.167 | 0.111 |
| 3.3-4.2 | 0.056 | 0.222 | 0.222 | 0.167 | 0.167 | 0.056 | 0.111 |
| 4.2-5.1 | 0.111 | 0.111 | 0.222 | 0.167 | 0.111 | 0.222 | 0.056 |
| 5.1-6.0 | 0.000 | 0.278 | 0.222 | 0.000 | 0.167 | 0.222 | 0.111 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.214 | 0.143 | 0.000 | 0.286 | 0.000 |
| 0.6-1.5 | 0.056 | 0.333 | 0.167 | 0.111 | 0.222 | 0.056 | 0.056 |
| 1.5-2.4 | 0.278 | 0.111 | 0.000 | 0.222 | 0.056 | 0.167 | 0.167 |
| 2.4-3.3 | 0.222 | 0.056 | 0.111 | 0.167 | 0.056 | 0.222 | 0.167 |
| 3.3-4.2 | 0.056 | 0.111 | 0.056 | 0.222 | 0.056 | 0.167 | 0.333 |
| 4.2-5.1 | 0.056 | 0.056 | 0.111 | 0.111 | 0.056 | 0.389 | 0.222 |
| 5.1-6.0 | 0.000 | 0.167 | 0.056 | 0.222 | 0.167 | 0.167 | 0.222 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.357 | 0.000 | 0.071 | 0.143 | 0.071 |
| 0.6-1.5 | 0.000 | 0.389 | 0.056 | 0.111 | 0.000 | 0.111 | 0.333 |
| 1.5-2.4 | 0.056 | 0.278 | 0.111 | 0.111 | 0.111 | 0.167 | 0.167 |
| 2.4-3.3 | 0.056 | 0.278 | 0.333 | 0.000 | 0.056 | 0.111 | 0.167 |
| 3.3-4.2 | 0.056 | 0.333 | 0.111 | 0.111 | 0.056 | 0.222 | 0.111 |
| 4.2-5.1 | 0.111 | 0.056 | 0.278 | 0.167 | 0.111 | 0.278 | 0.000 |
| 5.1-6.0 | 0.000 | 0.278 | 0.111 | 0.056 | 0.278 | 0.056 | 0.222 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.214 | 0.000 | 0.000 | 0.357 | 0.000 |
| 0.6-1.5 | 0.056 | 0.278 | 0.167 | 0.222 | 0.000 | 0.000 | 0.278 |
| 1.5-2.4 | 0.222 | 0.111 | 0.056 | 0.333 | 0.111 | 0.167 | 0.000 |
| 2.4-3.3 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 | 0.222 | 0.167 |
| 3.3-4.2 | 0.111 | 0.111 | 0.111 | 0.111 | 0.167 | 0.111 | 0.278 |
| 4.2-5.1 | 0.111 | 0.111 | 0.111 | 0.167 | 0.111 | 0.278 | 0.111 |
| 5.1-6.0 | 0.056 | 0.167 | 0.111 | 0.167 | 0.111 | 0.167 | 0.222 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/ecg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.357 | 0.000 | 0.000 | 0.214 | 0.143 |
| 0.6-1.5 | 0.167 | 0.222 | 0.000 | 0.167 | 0.222 | 0.056 | 0.167 |
| 1.5-2.4 | 0.278 | 0.056 | 0.167 | 0.000 | 0.111 | 0.278 | 0.111 |
| 2.4-3.3 | 0.167 | 0.167 | 0.222 | 0.000 | 0.111 | 0.222 | 0.111 |
| 3.3-4.2 | 0.111 | 0.167 | 0.056 | 0.167 | 0.222 | 0.167 | 0.111 |
| 4.2-5.1 | 0.111 | 0.056 | 0.167 | 0.111 | 0.111 | 0.222 | 0.222 |
| 5.1-6.0 | 0.056 | 0.111 | 0.111 | 0.056 | 0.278 | 0.167 | 0.222 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2233)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `0.6-1.5`: recall=0.3208, support=53
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.0943, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.297 | 0.081 | 0.027 | 0.135 | 0.162 | 0.081 | 0.216 |
| 0.6-1.5 | 0.170 | 0.321 | 0.113 | 0.113 | 0.075 | 0.113 | 0.094 |
| 1.5-2.4 | 0.185 | 0.333 | 0.056 | 0.074 | 0.074 | 0.167 | 0.111 |
| 2.4-3.3 | 0.196 | 0.098 | 0.078 | 0.078 | 0.157 | 0.275 | 0.118 |
| 3.3-4.2 | 0.151 | 0.189 | 0.019 | 0.075 | 0.094 | 0.208 | 0.264 |
| 4.2-5.1 | 0.216 | 0.059 | 0.059 | 0.039 | 0.098 | 0.255 | 0.275 |
| 5.1-6.0 | 0.135 | 0.096 | 0.019 | 0.038 | 0.135 | 0.288 | 0.288 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2049)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `0.6-1.5`: recall=0.2642, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.216 | 0.162 | 0.000 | 0.135 | 0.270 | 0.054 | 0.162 |
| 0.6-1.5 | 0.170 | 0.264 | 0.151 | 0.113 | 0.170 | 0.075 | 0.057 |
| 1.5-2.4 | 0.167 | 0.241 | 0.148 | 0.093 | 0.185 | 0.019 | 0.148 |
| 2.4-3.3 | 0.078 | 0.118 | 0.098 | 0.196 | 0.294 | 0.039 | 0.176 |
| 3.3-4.2 | 0.094 | 0.132 | 0.113 | 0.113 | 0.264 | 0.094 | 0.189 |
| 4.2-5.1 | 0.118 | 0.039 | 0.118 | 0.176 | 0.255 | 0.039 | 0.255 |
| 5.1-6.0 | 0.038 | 0.135 | 0.038 | 0.096 | 0.327 | 0.058 | 0.308 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.270 | 0.135 | 0.081 | 0.054 | 0.297 | 0.000 | 0.162 |
| 0.6-1.5 | 0.264 | 0.208 | 0.170 | 0.038 | 0.226 | 0.038 | 0.057 |
| 1.5-2.4 | 0.204 | 0.241 | 0.148 | 0.093 | 0.204 | 0.037 | 0.074 |
| 2.4-3.3 | 0.118 | 0.059 | 0.235 | 0.078 | 0.275 | 0.078 | 0.157 |
| 3.3-4.2 | 0.094 | 0.113 | 0.170 | 0.057 | 0.264 | 0.057 | 0.245 |
| 4.2-5.1 | 0.157 | 0.020 | 0.118 | 0.059 | 0.353 | 0.039 | 0.255 |
| 5.1-6.0 | 0.115 | 0.096 | 0.077 | 0.038 | 0.288 | 0.077 | 0.308 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1837)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `0.6-1.5`: recall=0.3208, support=53
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.2075, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.054 | 0.216 | 0.162 | 0.216 | 0.243 | 0.054 | 0.054 |
| 0.6-1.5 | 0.170 | 0.321 | 0.113 | 0.113 | 0.151 | 0.094 | 0.038 |
| 1.5-2.4 | 0.111 | 0.259 | 0.167 | 0.111 | 0.148 | 0.167 | 0.037 |
| 2.4-3.3 | 0.118 | 0.216 | 0.157 | 0.176 | 0.196 | 0.078 | 0.059 |
| 3.3-4.2 | 0.170 | 0.113 | 0.151 | 0.170 | 0.208 | 0.170 | 0.019 |
| 4.2-5.1 | 0.157 | 0.137 | 0.098 | 0.098 | 0.255 | 0.196 | 0.059 |
| 5.1-6.0 | 0.096 | 0.154 | 0.173 | 0.135 | 0.212 | 0.135 | 0.096 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1763)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.3784, support=37
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.3585, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1731, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.378 | 0.108 | 0.054 | 0.027 | 0.243 | 0.000 | 0.189 |
| 0.6-1.5 | 0.396 | 0.189 | 0.075 | 0.113 | 0.113 | 0.038 | 0.075 |
| 1.5-2.4 | 0.352 | 0.185 | 0.037 | 0.037 | 0.241 | 0.056 | 0.093 |
| 2.4-3.3 | 0.275 | 0.059 | 0.098 | 0.020 | 0.314 | 0.098 | 0.137 |
| 3.3-4.2 | 0.283 | 0.038 | 0.094 | 0.019 | 0.358 | 0.057 | 0.151 |
| 4.2-5.1 | 0.255 | 0.000 | 0.059 | 0.020 | 0.451 | 0.039 | 0.176 |
| 5.1-6.0 | 0.250 | 0.058 | 0.038 | 0.038 | 0.327 | 0.115 | 0.173 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1709)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.7358, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.108 | 0.000 | 0.027 | 0.730 | 0.000 | 0.000 |
| 0.6-1.5 | 0.075 | 0.057 | 0.019 | 0.075 | 0.642 | 0.075 | 0.057 |
| 1.5-2.4 | 0.000 | 0.037 | 0.000 | 0.074 | 0.815 | 0.056 | 0.019 |
| 2.4-3.3 | 0.098 | 0.039 | 0.000 | 0.020 | 0.765 | 0.059 | 0.020 |
| 3.3-4.2 | 0.075 | 0.019 | 0.019 | 0.075 | 0.736 | 0.038 | 0.038 |
| 4.2-5.1 | 0.059 | 0.000 | 0.000 | 0.000 | 0.784 | 0.039 | 0.118 |
| 5.1-6.0 | 0.019 | 0.019 | 0.000 | 0.038 | 0.731 | 0.038 | 0.154 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1074)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `0.6-1.5`: recall=0.1132, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.135 | 0.270 | 0.054 | 0.243 | 0.054 | 0.189 | 0.054 |
| 0.6-1.5 | 0.189 | 0.113 | 0.057 | 0.170 | 0.189 | 0.245 | 0.038 |
| 1.5-2.4 | 0.167 | 0.185 | 0.037 | 0.093 | 0.222 | 0.222 | 0.074 |
| 2.4-3.3 | 0.176 | 0.098 | 0.098 | 0.020 | 0.176 | 0.275 | 0.157 |
| 3.3-4.2 | 0.132 | 0.151 | 0.113 | 0.094 | 0.132 | 0.264 | 0.113 |
| 4.2-5.1 | 0.157 | 0.137 | 0.098 | 0.078 | 0.235 | 0.216 | 0.078 |
| 5.1-6.0 | 0.212 | 0.096 | 0.096 | 0.154 | 0.173 | 0.212 | 0.058 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2608)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.8125, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.643 | 0.071 | 0.071 | 0.000 | 0.000 | 0.071 |
| 0.6-1.5 | 0.000 | 0.812 | 0.125 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.375 | 0.250 | 0.125 | 0.000 | 0.062 | 0.188 |
| 2.4-3.3 | 0.000 | 0.471 | 0.059 | 0.235 | 0.000 | 0.000 | 0.235 |
| 3.3-4.2 | 0.059 | 0.294 | 0.235 | 0.176 | 0.000 | 0.059 | 0.176 |
| 4.2-5.1 | 0.000 | 0.611 | 0.111 | 0.056 | 0.056 | 0.000 | 0.167 |
| 5.1-6.0 | 0.000 | 0.111 | 0.389 | 0.000 | 0.111 | 0.000 | 0.389 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2256)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.6250, support=16
- `1.5-2.4`: recall=0.5000, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.143 | 0.143 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.625 | 0.312 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.188 | 0.500 | 0.000 | 0.250 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.118 | 0.353 | 0.118 | 0.118 | 0.000 | 0.294 |
| 3.3-4.2 | 0.118 | 0.294 | 0.235 | 0.118 | 0.000 | 0.000 | 0.235 |
| 4.2-5.1 | 0.000 | 0.389 | 0.056 | 0.056 | 0.389 | 0.000 | 0.111 |
| 5.1-6.0 | 0.000 | 0.111 | 0.111 | 0.278 | 0.389 | 0.000 | 0.111 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2222)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.3125, support=16
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.357 | 0.071 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.312 | 0.625 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.062 | 0.688 | 0.125 | 0.062 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.118 | 0.824 | 0.059 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.118 | 0.000 | 0.471 | 0.412 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.111 | 0.389 | 0.222 | 0.278 | 0.000 | 0.000 |
| 5.1-6.0 | 0.111 | 0.056 | 0.389 | 0.389 | 0.056 | 0.000 | 0.000 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2185)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.5000, support=16
- `1.5-2.4`: recall=0.3750, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.214 | 0.143 | 0.000 | 0.214 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.500 | 0.438 | 0.000 | 0.062 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.375 | 0.375 | 0.125 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.059 | 0.235 | 0.412 | 0.000 | 0.176 | 0.000 | 0.118 |
| 3.3-4.2 | 0.059 | 0.412 | 0.294 | 0.059 | 0.118 | 0.000 | 0.059 |
| 4.2-5.1 | 0.056 | 0.222 | 0.222 | 0.056 | 0.333 | 0.056 | 0.056 |
| 5.1-6.0 | 0.000 | 0.278 | 0.222 | 0.056 | 0.389 | 0.056 | 0.000 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2173)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.5000, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.571 | 0.071 | 0.000 | 0.000 | 0.000 | 0.214 |
| 0.6-1.5 | 0.000 | 0.500 | 0.188 | 0.062 | 0.125 | 0.125 | 0.000 |
| 1.5-2.4 | 0.062 | 0.312 | 0.125 | 0.062 | 0.125 | 0.125 | 0.188 |
| 2.4-3.3 | 0.176 | 0.235 | 0.000 | 0.176 | 0.118 | 0.176 | 0.118 |
| 3.3-4.2 | 0.059 | 0.294 | 0.176 | 0.176 | 0.059 | 0.118 | 0.118 |
| 4.2-5.1 | 0.000 | 0.222 | 0.111 | 0.167 | 0.333 | 0.167 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.167 | 0.333 | 0.111 | 0.333 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2164)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.4706, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.643 | 0.000 | 0.000 | 0.286 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.750 | 0.000 | 0.188 | 0.062 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.562 | 0.062 | 0.062 | 0.312 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.647 | 0.000 | 0.176 | 0.176 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.529 | 0.000 | 0.000 | 0.471 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.389 | 0.000 | 0.056 | 0.556 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.056 | 0.833 | 0.000 | 0.000 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1705)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.3750, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.143 | 0.357 | 0.357 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.375 | 0.250 | 0.312 | 0.062 | 0.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.188 | 0.188 | 0.438 | 0.188 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.118 | 0.294 | 0.294 | 0.294 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.294 | 0.353 | 0.176 | 0.176 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.333 | 0.056 | 0.222 | 0.278 | 0.056 | 0.056 |
| 5.1-6.0 | 0.000 | 0.222 | 0.000 | 0.333 | 0.444 | 0.000 | 0.000 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.071 | 0.000 | 0.071 | 0.071 | 0.143 |
| 0.6-1.5 | 0.000 | 0.500 | 0.222 | 0.111 | 0.000 | 0.111 | 0.056 |
| 1.5-2.4 | 0.111 | 0.222 | 0.111 | 0.167 | 0.111 | 0.167 | 0.111 |
| 2.4-3.3 | 0.056 | 0.056 | 0.333 | 0.278 | 0.222 | 0.056 | 0.000 |
| 3.3-4.2 | 0.111 | 0.111 | 0.167 | 0.056 | 0.278 | 0.111 | 0.167 |
| 4.2-5.1 | 0.111 | 0.056 | 0.111 | 0.167 | 0.111 | 0.278 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.056 | 0.000 | 0.222 | 0.611 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.5556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.143 | 0.000 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.500 | 0.111 | 0.111 | 0.111 | 0.111 | 0.056 |
| 1.5-2.4 | 0.111 | 0.278 | 0.056 | 0.222 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.056 | 0.222 | 0.389 | 0.222 | 0.000 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.222 | 0.111 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.111 | 0.111 | 0.056 | 0.278 | 0.278 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.000 | 0.111 | 0.222 | 0.556 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.214 | 0.000 | 0.071 | 0.071 | 0.071 |
| 0.6-1.5 | 0.056 | 0.389 | 0.278 | 0.167 | 0.056 | 0.056 | 0.000 |
| 1.5-2.4 | 0.111 | 0.222 | 0.111 | 0.222 | 0.056 | 0.167 | 0.111 |
| 2.4-3.3 | 0.056 | 0.056 | 0.222 | 0.389 | 0.111 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.167 | 0.222 | 0.111 | 0.222 | 0.111 | 0.056 |
| 4.2-5.1 | 0.056 | 0.056 | 0.111 | 0.167 | 0.167 | 0.167 | 0.278 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.111 | 0.000 | 0.167 | 0.611 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.000 | 0.071 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.444 | 0.167 | 0.167 | 0.000 | 0.167 | 0.056 |
| 1.5-2.4 | 0.111 | 0.167 | 0.111 | 0.222 | 0.056 | 0.222 | 0.111 |
| 2.4-3.3 | 0.056 | 0.111 | 0.167 | 0.278 | 0.167 | 0.167 | 0.056 |
| 3.3-4.2 | 0.111 | 0.222 | 0.167 | 0.167 | 0.111 | 0.056 | 0.167 |
| 4.2-5.1 | 0.056 | 0.056 | 0.167 | 0.111 | 0.167 | 0.222 | 0.222 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.056 | 0.056 | 0.222 | 0.611 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.071 | 0.143 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.111 | 0.333 | 0.278 | 0.111 | 0.111 | 0.000 | 0.056 |
| 1.5-2.4 | 0.056 | 0.167 | 0.333 | 0.056 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.111 | 0.056 | 0.278 | 0.278 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.056 | 0.278 | 0.167 | 0.056 | 0.222 | 0.167 |
| 4.2-5.1 | 0.000 | 0.111 | 0.111 | 0.000 | 0.278 | 0.333 | 0.167 |
| 5.1-6.0 | 0.167 | 0.111 | 0.056 | 0.111 | 0.167 | 0.111 | 0.278 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.6667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.214 | 0.071 | 0.143 | 0.143 | 0.214 | 0.000 |
| 0.6-1.5 | 0.000 | 0.389 | 0.278 | 0.056 | 0.111 | 0.111 | 0.056 |
| 1.5-2.4 | 0.056 | 0.167 | 0.000 | 0.444 | 0.000 | 0.167 | 0.167 |
| 2.4-3.3 | 0.000 | 0.056 | 0.167 | 0.333 | 0.222 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.278 | 0.111 | 0.111 | 0.111 | 0.222 | 0.111 |
| 4.2-5.1 | 0.000 | 0.056 | 0.000 | 0.222 | 0.111 | 0.389 | 0.222 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.056 | 0.000 | 0.167 | 0.667 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/eeg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.214 | 0.000 | 0.071 | 0.000 | 0.143 |
| 0.6-1.5 | 0.056 | 0.278 | 0.222 | 0.111 | 0.000 | 0.278 | 0.056 |
| 1.5-2.4 | 0.167 | 0.167 | 0.056 | 0.167 | 0.111 | 0.278 | 0.056 |
| 2.4-3.3 | 0.056 | 0.056 | 0.278 | 0.333 | 0.111 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.222 | 0.056 | 0.056 | 0.333 | 0.111 |
| 4.2-5.1 | 0.000 | 0.056 | 0.222 | 0.056 | 0.111 | 0.278 | 0.278 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.056 | 0.111 | 0.056 | 0.611 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2016)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2105, support=38
- `0.6-1.5`: recall=0.3148, support=54
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.1111, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.3208, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.211 | 0.211 | 0.211 | 0.053 | 0.184 | 0.000 | 0.132 |
| 0.6-1.5 | 0.185 | 0.315 | 0.259 | 0.037 | 0.148 | 0.019 | 0.037 |
| 1.5-2.4 | 0.167 | 0.222 | 0.259 | 0.019 | 0.185 | 0.037 | 0.111 |
| 2.4-3.3 | 0.074 | 0.111 | 0.315 | 0.111 | 0.185 | 0.019 | 0.185 |
| 3.3-4.2 | 0.074 | 0.167 | 0.204 | 0.093 | 0.148 | 0.074 | 0.241 |
| 4.2-5.1 | 0.075 | 0.057 | 0.208 | 0.151 | 0.170 | 0.038 | 0.302 |
| 5.1-6.0 | 0.075 | 0.151 | 0.189 | 0.094 | 0.094 | 0.075 | 0.321 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1933)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.3684, support=38
- `0.6-1.5`: recall=0.1667, support=54
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2778, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.368 | 0.026 | 0.026 | 0.053 | 0.237 | 0.211 | 0.079 |
| 0.6-1.5 | 0.315 | 0.167 | 0.148 | 0.093 | 0.130 | 0.130 | 0.019 |
| 1.5-2.4 | 0.296 | 0.093 | 0.130 | 0.111 | 0.222 | 0.056 | 0.093 |
| 2.4-3.3 | 0.241 | 0.056 | 0.093 | 0.037 | 0.333 | 0.130 | 0.111 |
| 3.3-4.2 | 0.204 | 0.037 | 0.093 | 0.111 | 0.278 | 0.148 | 0.130 |
| 4.2-5.1 | 0.226 | 0.038 | 0.038 | 0.038 | 0.377 | 0.113 | 0.170 |
| 5.1-6.0 | 0.208 | 0.094 | 0.113 | 0.057 | 0.302 | 0.057 | 0.170 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1912)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.2632, support=38
- `0.6-1.5`: recall=0.2407, support=54
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.2453, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.263 | 0.158 | 0.053 | 0.053 | 0.158 | 0.026 | 0.289 |
| 0.6-1.5 | 0.259 | 0.241 | 0.185 | 0.019 | 0.111 | 0.056 | 0.130 |
| 1.5-2.4 | 0.333 | 0.111 | 0.167 | 0.000 | 0.130 | 0.111 | 0.148 |
| 2.4-3.3 | 0.241 | 0.093 | 0.093 | 0.074 | 0.222 | 0.111 | 0.167 |
| 3.3-4.2 | 0.241 | 0.019 | 0.093 | 0.074 | 0.241 | 0.093 | 0.241 |
| 4.2-5.1 | 0.245 | 0.057 | 0.094 | 0.000 | 0.302 | 0.075 | 0.226 |
| 5.1-6.0 | 0.226 | 0.075 | 0.075 | 0.019 | 0.208 | 0.151 | 0.245 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1844)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `0.6-1.5`: recall=0.3333, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.2778, support=54
- `3.3-4.2`: recall=0.2593, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.079 | 0.263 | 0.105 | 0.132 | 0.211 | 0.053 | 0.158 |
| 0.6-1.5 | 0.130 | 0.333 | 0.148 | 0.093 | 0.130 | 0.111 | 0.056 |
| 1.5-2.4 | 0.093 | 0.185 | 0.111 | 0.093 | 0.130 | 0.185 | 0.204 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.278 | 0.185 | 0.074 | 0.185 |
| 3.3-4.2 | 0.111 | 0.037 | 0.148 | 0.093 | 0.259 | 0.185 | 0.167 |
| 4.2-5.1 | 0.038 | 0.075 | 0.113 | 0.113 | 0.302 | 0.094 | 0.264 |
| 5.1-6.0 | 0.057 | 0.075 | 0.170 | 0.075 | 0.264 | 0.189 | 0.170 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1537)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `0.6-1.5`: recall=0.1852, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.2264, support=53
- `5.1-6.0`: recall=0.2075, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.105 | 0.132 | 0.132 | 0.211 | 0.132 | 0.211 | 0.079 |
| 0.6-1.5 | 0.296 | 0.185 | 0.148 | 0.093 | 0.093 | 0.130 | 0.056 |
| 1.5-2.4 | 0.185 | 0.204 | 0.111 | 0.074 | 0.185 | 0.148 | 0.093 |
| 2.4-3.3 | 0.222 | 0.093 | 0.222 | 0.037 | 0.130 | 0.204 | 0.093 |
| 3.3-4.2 | 0.204 | 0.074 | 0.185 | 0.130 | 0.148 | 0.167 | 0.093 |
| 4.2-5.1 | 0.245 | 0.057 | 0.019 | 0.170 | 0.189 | 0.226 | 0.094 |
| 5.1-6.0 | 0.340 | 0.000 | 0.151 | 0.038 | 0.094 | 0.170 | 0.208 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1406)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.0556, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.9245, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.184 | 0.000 | 0.000 | 0.000 | 0.000 | 0.816 |
| 0.6-1.5 | 0.000 | 0.056 | 0.000 | 0.000 | 0.019 | 0.000 | 0.926 |
| 1.5-2.4 | 0.000 | 0.074 | 0.000 | 0.000 | 0.019 | 0.000 | 0.907 |
| 2.4-3.3 | 0.037 | 0.111 | 0.000 | 0.000 | 0.019 | 0.000 | 0.833 |
| 3.3-4.2 | 0.000 | 0.037 | 0.000 | 0.000 | 0.000 | 0.019 | 0.944 |
| 4.2-5.1 | 0.000 | 0.075 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 |
| 5.1-6.0 | 0.000 | 0.075 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1372)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.0370, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.4259, support=54
- `3.3-4.2`: recall=0.0370, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.105 | 0.000 | 0.316 | 0.000 | 0.105 | 0.474 |
| 0.6-1.5 | 0.074 | 0.037 | 0.019 | 0.444 | 0.019 | 0.019 | 0.389 |
| 1.5-2.4 | 0.000 | 0.037 | 0.000 | 0.444 | 0.037 | 0.056 | 0.426 |
| 2.4-3.3 | 0.019 | 0.074 | 0.000 | 0.426 | 0.000 | 0.093 | 0.389 |
| 3.3-4.2 | 0.019 | 0.000 | 0.000 | 0.593 | 0.037 | 0.019 | 0.333 |
| 4.2-5.1 | 0.019 | 0.038 | 0.000 | 0.491 | 0.000 | 0.075 | 0.377 |
| 5.1-6.0 | 0.000 | 0.038 | 0.000 | 0.566 | 0.000 | 0.019 | 0.377 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2256)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2353, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.071 | 0.000 | 0.000 | 0.071 | 0.357 |
| 0.6-1.5 | 0.000 | 0.333 | 0.111 | 0.056 | 0.056 | 0.056 | 0.389 |
| 1.5-2.4 | 0.000 | 0.278 | 0.167 | 0.000 | 0.167 | 0.056 | 0.333 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.000 | 0.111 | 0.222 | 0.389 |
| 3.3-4.2 | 0.000 | 0.000 | 0.235 | 0.059 | 0.235 | 0.000 | 0.471 |
| 4.2-5.1 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 | 0.056 | 0.389 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.056 | 0.444 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2211)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.214 | 0.143 | 0.000 | 0.071 | 0.143 | 0.071 | 0.357 |
| 0.6-1.5 | 0.111 | 0.444 | 0.056 | 0.111 | 0.056 | 0.056 | 0.167 |
| 1.5-2.4 | 0.167 | 0.167 | 0.167 | 0.056 | 0.056 | 0.000 | 0.389 |
| 2.4-3.3 | 0.056 | 0.111 | 0.111 | 0.333 | 0.056 | 0.000 | 0.333 |
| 3.3-4.2 | 0.000 | 0.000 | 0.176 | 0.353 | 0.000 | 0.176 | 0.294 |
| 4.2-5.1 | 0.000 | 0.111 | 0.000 | 0.444 | 0.000 | 0.111 | 0.333 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.333 | 0.056 | 0.167 | 0.278 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2109)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.000 | 0.000 | 0.071 | 0.071 | 0.500 |
| 0.6-1.5 | 0.000 | 0.389 | 0.111 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.000 | 0.333 | 0.167 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.000 | 0.167 | 0.222 | 0.000 | 0.000 | 0.111 | 0.500 |
| 3.3-4.2 | 0.000 | 0.176 | 0.059 | 0.000 | 0.059 | 0.059 | 0.647 |
| 4.2-5.1 | 0.000 | 0.111 | 0.056 | 0.000 | 0.167 | 0.000 | 0.667 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.000 | 0.111 | 0.000 | 0.722 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1950)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.143 | 0.071 | 0.214 | 0.000 | 0.143 | 0.071 | 0.357 |
| 0.6-1.5 | 0.056 | 0.167 | 0.222 | 0.056 | 0.000 | 0.222 | 0.278 |
| 1.5-2.4 | 0.000 | 0.167 | 0.222 | 0.000 | 0.056 | 0.222 | 0.333 |
| 2.4-3.3 | 0.000 | 0.000 | 0.278 | 0.000 | 0.000 | 0.389 | 0.333 |
| 3.3-4.2 | 0.000 | 0.000 | 0.235 | 0.059 | 0.059 | 0.059 | 0.588 |
| 4.2-5.1 | 0.000 | 0.000 | 0.056 | 0.056 | 0.056 | 0.278 | 0.556 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.056 | 0.111 | 0.222 | 0.500 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1769)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.357 | 0.000 | 0.000 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.278 | 0.222 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.000 | 0.111 | 0.389 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.000 | 0.056 | 0.444 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.000 | 0.118 | 0.412 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/gaussian_nb_none.png`

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
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1349)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.429 | 0.143 | 0.143 | 0.143 | 0.071 | 0.071 |
| 0.6-1.5 | 0.000 | 0.444 | 0.111 | 0.000 | 0.222 | 0.167 | 0.056 |
| 1.5-2.4 | 0.056 | 0.333 | 0.167 | 0.056 | 0.167 | 0.167 | 0.056 |
| 2.4-3.3 | 0.000 | 0.222 | 0.222 | 0.000 | 0.222 | 0.333 | 0.000 |
| 3.3-4.2 | 0.000 | 0.353 | 0.235 | 0.059 | 0.059 | 0.118 | 0.176 |
| 4.2-5.1 | 0.000 | 0.167 | 0.056 | 0.000 | 0.500 | 0.278 | 0.000 |
| 5.1-6.0 | 0.000 | 0.167 | 0.056 | 0.167 | 0.278 | 0.333 | 0.000 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.929 | 0.000 | 0.000 | 0.000 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.056 | 0.556 | 0.222 | 0.056 | 0.000 | 0.000 | 0.111 |
| 1.5-2.4 | 0.056 | 0.278 | 0.333 | 0.111 | 0.111 | 0.056 | 0.056 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.000 | 0.389 | 0.222 | 0.111 |
| 3.3-4.2 | 0.056 | 0.000 | 0.167 | 0.111 | 0.111 | 0.278 | 0.278 |
| 4.2-5.1 | 0.000 | 0.118 | 0.000 | 0.118 | 0.294 | 0.118 | 0.353 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.111 | 0.167 | 0.278 | 0.444 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3571)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.9286, support=14
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.929 | 0.000 | 0.071 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.500 | 0.278 | 0.111 | 0.056 | 0.000 | 0.056 |
| 1.5-2.4 | 0.056 | 0.278 | 0.278 | 0.167 | 0.167 | 0.056 | 0.000 |
| 2.4-3.3 | 0.111 | 0.167 | 0.111 | 0.167 | 0.167 | 0.222 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.222 | 0.056 | 0.111 | 0.333 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.294 | 0.000 | 0.294 | 0.176 | 0.176 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.444 | 0.389 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.643 | 0.071 | 0.143 | 0.071 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.111 | 0.389 | 0.167 | 0.222 | 0.056 | 0.056 | 0.000 |
| 1.5-2.4 | 0.167 | 0.222 | 0.222 | 0.056 | 0.111 | 0.111 | 0.111 |
| 2.4-3.3 | 0.000 | 0.222 | 0.056 | 0.278 | 0.111 | 0.278 | 0.056 |
| 3.3-4.2 | 0.111 | 0.000 | 0.111 | 0.167 | 0.167 | 0.333 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.176 | 0.176 | 0.294 | 0.176 | 0.118 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.056 | 0.056 | 0.333 | 0.389 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.000 | 0.000 | 0.143 | 0.000 | 0.000 |
| 0.6-1.5 | 0.000 | 0.333 | 0.389 | 0.056 | 0.056 | 0.056 | 0.111 |
| 1.5-2.4 | 0.111 | 0.167 | 0.222 | 0.111 | 0.167 | 0.111 | 0.111 |
| 2.4-3.3 | 0.111 | 0.167 | 0.056 | 0.167 | 0.111 | 0.389 | 0.000 |
| 3.3-4.2 | 0.056 | 0.056 | 0.056 | 0.111 | 0.278 | 0.389 | 0.056 |
| 4.2-5.1 | 0.000 | 0.176 | 0.059 | 0.118 | 0.353 | 0.059 | 0.235 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.000 | 0.333 | 0.278 | 0.278 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.071 | 0.071 | 0.143 | 0.071 | 0.000 |
| 0.6-1.5 | 0.000 | 0.278 | 0.389 | 0.111 | 0.000 | 0.167 | 0.056 |
| 1.5-2.4 | 0.000 | 0.222 | 0.278 | 0.111 | 0.222 | 0.167 | 0.000 |
| 2.4-3.3 | 0.000 | 0.111 | 0.167 | 0.167 | 0.167 | 0.389 | 0.000 |
| 3.3-4.2 | 0.056 | 0.000 | 0.167 | 0.167 | 0.167 | 0.444 | 0.000 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.235 | 0.235 | 0.353 | 0.059 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.111 | 0.056 | 0.444 | 0.222 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2357)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.143 | 0.143 | 0.071 | 0.000 | 0.000 |
| 0.6-1.5 | 0.056 | 0.222 | 0.278 | 0.111 | 0.056 | 0.167 | 0.111 |
| 1.5-2.4 | 0.111 | 0.278 | 0.222 | 0.000 | 0.000 | 0.278 | 0.111 |
| 2.4-3.3 | 0.000 | 0.167 | 0.167 | 0.056 | 0.111 | 0.333 | 0.167 |
| 3.3-4.2 | 0.056 | 0.056 | 0.111 | 0.167 | 0.278 | 0.167 | 0.167 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.176 | 0.235 | 0.235 | 0.235 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.000 | 0.389 | 0.278 | 0.222 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.357 | 0.000 | 0.214 | 0.071 | 0.214 | 0.071 | 0.071 |
| 0.6-1.5 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 | 0.278 | 0.111 |
| 1.5-2.4 | 0.056 | 0.222 | 0.111 | 0.111 | 0.333 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.056 | 0.056 | 0.056 | 0.444 | 0.222 | 0.056 |
| 3.3-4.2 | 0.000 | 0.056 | 0.111 | 0.222 | 0.167 | 0.278 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.118 | 0.235 | 0.353 | 0.235 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.056 | 0.389 | 0.389 | 0.111 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1866)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.1296, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.4528, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.026 | 0.211 | 0.211 | 0.053 | 0.158 | 0.132 | 0.211 |
| 0.6-1.5 | 0.000 | 0.296 | 0.204 | 0.037 | 0.222 | 0.019 | 0.222 |
| 1.5-2.4 | 0.000 | 0.185 | 0.278 | 0.056 | 0.204 | 0.037 | 0.241 |
| 2.4-3.3 | 0.000 | 0.093 | 0.204 | 0.056 | 0.148 | 0.130 | 0.370 |
| 3.3-4.2 | 0.000 | 0.056 | 0.204 | 0.074 | 0.130 | 0.167 | 0.370 |
| 4.2-5.1 | 0.019 | 0.113 | 0.189 | 0.038 | 0.170 | 0.113 | 0.358 |
| 5.1-6.0 | 0.000 | 0.170 | 0.132 | 0.019 | 0.094 | 0.132 | 0.453 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1860)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `0.6-1.5`: recall=0.4444, support=54
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2037, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.079 | 0.211 | 0.079 | 0.000 | 0.211 | 0.026 | 0.395 |
| 0.6-1.5 | 0.074 | 0.444 | 0.074 | 0.019 | 0.167 | 0.000 | 0.222 |
| 1.5-2.4 | 0.037 | 0.259 | 0.130 | 0.074 | 0.148 | 0.111 | 0.241 |
| 2.4-3.3 | 0.167 | 0.111 | 0.130 | 0.037 | 0.148 | 0.093 | 0.315 |
| 3.3-4.2 | 0.056 | 0.074 | 0.093 | 0.000 | 0.204 | 0.093 | 0.481 |
| 4.2-5.1 | 0.094 | 0.075 | 0.132 | 0.038 | 0.132 | 0.057 | 0.472 |
| 5.1-6.0 | 0.075 | 0.094 | 0.132 | 0.057 | 0.226 | 0.038 | 0.377 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `0.6-1.5`: recall=0.3148, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.2778, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.3585, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.184 | 0.132 | 0.026 | 0.000 | 0.263 | 0.079 | 0.316 |
| 0.6-1.5 | 0.093 | 0.315 | 0.037 | 0.000 | 0.315 | 0.037 | 0.204 |
| 1.5-2.4 | 0.037 | 0.241 | 0.037 | 0.000 | 0.315 | 0.167 | 0.204 |
| 2.4-3.3 | 0.074 | 0.093 | 0.037 | 0.019 | 0.259 | 0.185 | 0.333 |
| 3.3-4.2 | 0.130 | 0.019 | 0.000 | 0.000 | 0.278 | 0.111 | 0.463 |
| 4.2-5.1 | 0.038 | 0.075 | 0.000 | 0.000 | 0.302 | 0.094 | 0.491 |
| 5.1-6.0 | 0.094 | 0.000 | 0.038 | 0.038 | 0.396 | 0.075 | 0.358 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1743)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.2778, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.368 | 0.079 | 0.000 | 0.158 | 0.079 | 0.184 |
| 0.6-1.5 | 0.074 | 0.296 | 0.130 | 0.074 | 0.056 | 0.093 | 0.278 |
| 1.5-2.4 | 0.074 | 0.296 | 0.111 | 0.019 | 0.185 | 0.167 | 0.148 |
| 2.4-3.3 | 0.074 | 0.111 | 0.130 | 0.074 | 0.278 | 0.093 | 0.241 |
| 3.3-4.2 | 0.204 | 0.093 | 0.130 | 0.019 | 0.278 | 0.111 | 0.167 |
| 4.2-5.1 | 0.151 | 0.075 | 0.151 | 0.094 | 0.151 | 0.113 | 0.264 |
| 5.1-6.0 | 0.208 | 0.151 | 0.226 | 0.038 | 0.132 | 0.094 | 0.151 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1406)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.0556, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.9245, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.184 | 0.000 | 0.000 | 0.000 | 0.000 | 0.816 |
| 0.6-1.5 | 0.000 | 0.056 | 0.000 | 0.000 | 0.019 | 0.000 | 0.926 |
| 1.5-2.4 | 0.000 | 0.074 | 0.000 | 0.000 | 0.019 | 0.000 | 0.907 |
| 2.4-3.3 | 0.037 | 0.111 | 0.000 | 0.000 | 0.019 | 0.000 | 0.833 |
| 3.3-4.2 | 0.000 | 0.037 | 0.000 | 0.000 | 0.000 | 0.019 | 0.944 |
| 4.2-5.1 | 0.000 | 0.075 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 |
| 5.1-6.0 | 0.000 | 0.075 | 0.000 | 0.000 | 0.000 | 0.000 | 0.925 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1399)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `0.6-1.5`: recall=0.0370, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.2222, support=54
- `3.3-4.2`: recall=0.0370, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.6226, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.105 | 0.026 | 0.211 | 0.000 | 0.079 | 0.579 |
| 0.6-1.5 | 0.074 | 0.037 | 0.019 | 0.204 | 0.019 | 0.019 | 0.630 |
| 1.5-2.4 | 0.000 | 0.037 | 0.000 | 0.241 | 0.019 | 0.056 | 0.648 |
| 2.4-3.3 | 0.037 | 0.093 | 0.000 | 0.222 | 0.000 | 0.056 | 0.593 |
| 3.3-4.2 | 0.019 | 0.000 | 0.000 | 0.352 | 0.037 | 0.019 | 0.574 |
| 4.2-5.1 | 0.019 | 0.038 | 0.000 | 0.264 | 0.000 | 0.057 | 0.623 |
| 5.1-6.0 | 0.000 | 0.038 | 0.000 | 0.321 | 0.000 | 0.019 | 0.623 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1384)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.1481, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.132 | 0.263 | 0.105 | 0.132 | 0.211 | 0.132 | 0.026 |
| 0.6-1.5 | 0.111 | 0.296 | 0.111 | 0.148 | 0.111 | 0.093 | 0.130 |
| 1.5-2.4 | 0.148 | 0.278 | 0.093 | 0.167 | 0.093 | 0.093 | 0.130 |
| 2.4-3.3 | 0.111 | 0.185 | 0.148 | 0.148 | 0.037 | 0.185 | 0.185 |
| 3.3-4.2 | 0.130 | 0.130 | 0.130 | 0.148 | 0.056 | 0.259 | 0.148 |
| 4.2-5.1 | 0.170 | 0.019 | 0.132 | 0.170 | 0.189 | 0.113 | 0.208 |
| 5.1-6.0 | 0.245 | 0.057 | 0.151 | 0.151 | 0.189 | 0.038 | 0.170 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2324)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.214 | 0.143 | 0.000 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.389 | 0.389 | 0.000 | 0.000 | 0.000 | 0.222 |
| 1.5-2.4 | 0.111 | 0.333 | 0.333 | 0.056 | 0.000 | 0.000 | 0.167 |
| 2.4-3.3 | 0.056 | 0.111 | 0.333 | 0.333 | 0.056 | 0.000 | 0.111 |
| 3.3-4.2 | 0.235 | 0.000 | 0.118 | 0.353 | 0.059 | 0.000 | 0.235 |
| 4.2-5.1 | 0.111 | 0.056 | 0.000 | 0.167 | 0.167 | 0.278 | 0.222 |
| 5.1-6.0 | 0.111 | 0.000 | 0.056 | 0.389 | 0.222 | 0.056 | 0.167 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.143 | 0.071 | 0.286 | 0.000 | 0.071 | 0.429 |
| 0.6-1.5 | 0.000 | 0.611 | 0.000 | 0.000 | 0.000 | 0.056 | 0.333 |
| 1.5-2.4 | 0.000 | 0.444 | 0.000 | 0.167 | 0.000 | 0.000 | 0.389 |
| 2.4-3.3 | 0.000 | 0.278 | 0.056 | 0.222 | 0.056 | 0.000 | 0.389 |
| 3.3-4.2 | 0.000 | 0.118 | 0.059 | 0.353 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.000 | 0.056 | 0.000 | 0.500 | 0.000 | 0.000 | 0.444 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.444 | 0.056 | 0.000 | 0.444 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1769)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5556, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.357 | 0.000 | 0.000 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.222 | 0.222 | 0.000 | 0.222 | 0.000 | 0.333 |
| 1.5-2.4 | 0.000 | 0.056 | 0.389 | 0.000 | 0.056 | 0.056 | 0.444 |
| 2.4-3.3 | 0.000 | 0.000 | 0.222 | 0.000 | 0.000 | 0.000 | 0.778 |
| 3.3-4.2 | 0.000 | 0.000 | 0.471 | 0.000 | 0.000 | 0.000 | 0.529 |
| 4.2-5.1 | 0.000 | 0.056 | 0.222 | 0.000 | 0.056 | 0.000 | 0.667 |
| 5.1-6.0 | 0.000 | 0.000 | 0.444 | 0.000 | 0.000 | 0.000 | 0.556 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.286 | 0.214 | 0.357 | 0.000 | 0.000 | 0.143 |
| 0.6-1.5 | 0.000 | 0.556 | 0.167 | 0.111 | 0.000 | 0.056 | 0.111 |
| 1.5-2.4 | 0.000 | 0.389 | 0.167 | 0.111 | 0.056 | 0.056 | 0.222 |
| 2.4-3.3 | 0.000 | 0.278 | 0.333 | 0.222 | 0.056 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.118 | 0.235 | 0.059 | 0.059 | 0.000 | 0.529 |
| 4.2-5.1 | 0.000 | 0.222 | 0.000 | 0.222 | 0.222 | 0.000 | 0.333 |
| 5.1-6.0 | 0.000 | 0.167 | 0.222 | 0.278 | 0.167 | 0.000 | 0.167 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/gaussian_nb_none.png`

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
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.071 | 0.429 | 0.000 | 0.000 | 0.000 | 0.500 |
| 0.6-1.5 | 0.000 | 0.056 | 0.444 | 0.000 | 0.000 | 0.000 | 0.500 |
| 1.5-2.4 | 0.000 | 0.056 | 0.444 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 3.3-4.2 | 0.000 | 0.000 | 0.529 | 0.000 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.000 | 0.214 | 0.071 | 0.143 | 0.000 | 0.071 | 0.500 |
| 0.6-1.5 | 0.000 | 0.444 | 0.000 | 0.000 | 0.000 | 0.056 | 0.500 |
| 1.5-2.4 | 0.000 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.056 | 0.167 | 0.222 | 0.000 | 0.000 | 0.056 | 0.500 |
| 3.3-4.2 | 0.118 | 0.235 | 0.059 | 0.059 | 0.000 | 0.059 | 0.471 |
| 4.2-5.1 | 0.056 | 0.000 | 0.000 | 0.444 | 0.000 | 0.000 | 0.500 |
| 5.1-6.0 | 0.167 | 0.056 | 0.000 | 0.278 | 0.000 | 0.000 | 0.500 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.6667, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.786 | 0.000 | 0.071 | 0.071 | 0.000 | 0.071 | 0.000 |
| 0.6-1.5 | 0.000 | 0.278 | 0.278 | 0.278 | 0.000 | 0.111 | 0.056 |
| 1.5-2.4 | 0.167 | 0.556 | 0.111 | 0.111 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.056 | 0.167 | 0.111 | 0.222 | 0.111 | 0.278 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.056 | 0.111 | 0.222 | 0.278 | 0.167 |
| 4.2-5.1 | 0.000 | 0.059 | 0.118 | 0.118 | 0.176 | 0.353 | 0.176 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.056 | 0.167 | 0.111 | 0.667 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.071 | 0.071 | 0.071 | 0.143 | 0.071 | 0.000 |
| 0.6-1.5 | 0.056 | 0.333 | 0.333 | 0.167 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.000 | 0.389 | 0.389 | 0.111 | 0.056 | 0.000 | 0.056 |
| 2.4-3.3 | 0.000 | 0.167 | 0.000 | 0.278 | 0.278 | 0.167 | 0.111 |
| 3.3-4.2 | 0.056 | 0.000 | 0.167 | 0.056 | 0.278 | 0.333 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.176 | 0.353 | 0.235 | 0.118 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.111 | 0.167 | 0.111 | 0.444 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.6471, support=17
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.143 | 0.071 | 0.071 | 0.071 | 0.071 |
| 0.6-1.5 | 0.000 | 0.167 | 0.278 | 0.278 | 0.000 | 0.222 | 0.056 |
| 1.5-2.4 | 0.056 | 0.167 | 0.333 | 0.278 | 0.056 | 0.111 | 0.000 |
| 2.4-3.3 | 0.000 | 0.111 | 0.222 | 0.111 | 0.111 | 0.278 | 0.167 |
| 3.3-4.2 | 0.056 | 0.000 | 0.222 | 0.111 | 0.167 | 0.278 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.059 | 0.118 | 0.647 | 0.118 |
| 5.1-6.0 | 0.000 | 0.000 | 0.167 | 0.056 | 0.056 | 0.389 | 0.333 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.571 | 0.000 | 0.143 | 0.000 | 0.143 | 0.071 | 0.071 |
| 0.6-1.5 | 0.056 | 0.278 | 0.333 | 0.111 | 0.111 | 0.056 | 0.056 |
| 1.5-2.4 | 0.056 | 0.389 | 0.167 | 0.167 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.167 | 0.111 | 0.111 | 0.056 | 0.222 | 0.222 | 0.111 |
| 3.3-4.2 | 0.056 | 0.111 | 0.056 | 0.111 | 0.278 | 0.222 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.235 | 0.118 | 0.118 | 0.294 | 0.235 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.056 | 0.167 | 0.278 | 0.444 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.5882, support=17
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.500 | 0.071 | 0.000 | 0.000 | 0.286 | 0.143 | 0.000 |
| 0.6-1.5 | 0.000 | 0.278 | 0.167 | 0.111 | 0.056 | 0.167 | 0.222 |
| 1.5-2.4 | 0.000 | 0.333 | 0.111 | 0.111 | 0.222 | 0.056 | 0.167 |
| 2.4-3.3 | 0.111 | 0.222 | 0.167 | 0.167 | 0.111 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.111 | 0.056 | 0.111 | 0.167 | 0.222 | 0.278 |
| 4.2-5.1 | 0.118 | 0.000 | 0.059 | 0.000 | 0.000 | 0.588 | 0.235 |
| 5.1-6.0 | 0.000 | 0.056 | 0.111 | 0.111 | 0.167 | 0.167 | 0.389 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.071 | 0.214 | 0.143 | 0.000 | 0.071 |
| 0.6-1.5 | 0.000 | 0.222 | 0.056 | 0.333 | 0.056 | 0.222 | 0.111 |
| 1.5-2.4 | 0.167 | 0.278 | 0.167 | 0.111 | 0.056 | 0.167 | 0.056 |
| 2.4-3.3 | 0.056 | 0.167 | 0.056 | 0.222 | 0.222 | 0.222 | 0.056 |
| 3.3-4.2 | 0.056 | 0.000 | 0.056 | 0.167 | 0.278 | 0.278 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.059 | 0.176 | 0.294 | 0.412 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.056 | 0.167 | 0.222 | 0.500 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_omit_hardest_baseline/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.3333, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | baseline | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.071 | 0.000 | 0.214 | 0.143 | 0.071 |
| 0.6-1.5 | 0.056 | 0.167 | 0.167 | 0.111 | 0.222 | 0.222 | 0.056 |
| 1.5-2.4 | 0.000 | 0.167 | 0.167 | 0.222 | 0.222 | 0.111 | 0.111 |
| 2.4-3.3 | 0.111 | 0.000 | 0.111 | 0.111 | 0.333 | 0.278 | 0.056 |
| 3.3-4.2 | 0.056 | 0.056 | 0.000 | 0.111 | 0.333 | 0.222 | 0.222 |
| 4.2-5.1 | 0.118 | 0.059 | 0.059 | 0.000 | 0.176 | 0.235 | 0.353 |
| 5.1-6.0 | 0.056 | 0.000 | 0.000 | 0.056 | 0.389 | 0.389 | 0.111 |


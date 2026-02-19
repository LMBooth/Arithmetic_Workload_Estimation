# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_all_bins.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1827)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1698, support=53
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.2353, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.170 | 0.226 | 0.094 | 0.113 | 0.170 | 0.132 | 0.094 |
| 1.5-2.4 | 0.278 | 0.185 | 0.222 | 0.093 | 0.056 | 0.093 | 0.074 |
| 2.4-3.3 | 0.118 | 0.176 | 0.196 | 0.255 | 0.137 | 0.078 | 0.039 |
| 3.3-4.2 | 0.113 | 0.151 | 0.151 | 0.245 | 0.189 | 0.151 | 0.000 |
| 4.2-5.1 | 0.118 | 0.118 | 0.157 | 0.216 | 0.235 | 0.098 | 0.059 |
| 5.1-6.0 | 0.135 | 0.058 | 0.173 | 0.212 | 0.192 | 0.154 | 0.077 |
| 6.0-6.9 | 0.212 | 0.096 | 0.173 | 0.192 | 0.154 | 0.077 | 0.096 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1661)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.4038, support=52
- `6.0-6.9`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.208 | 0.094 | 0.057 | 0.170 | 0.132 | 0.245 | 0.094 |
| 1.5-2.4 | 0.148 | 0.074 | 0.093 | 0.204 | 0.056 | 0.222 | 0.204 |
| 2.4-3.3 | 0.137 | 0.059 | 0.078 | 0.176 | 0.176 | 0.216 | 0.157 |
| 3.3-4.2 | 0.113 | 0.075 | 0.075 | 0.245 | 0.208 | 0.226 | 0.057 |
| 4.2-5.1 | 0.118 | 0.039 | 0.078 | 0.196 | 0.118 | 0.333 | 0.118 |
| 5.1-6.0 | 0.135 | 0.019 | 0.096 | 0.231 | 0.058 | 0.404 | 0.058 |
| 6.0-6.9 | 0.135 | 0.077 | 0.135 | 0.173 | 0.154 | 0.288 | 0.038 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1627)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.0962, support=52
- `6.0-6.9`: recall=0.1154, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.226 | 0.208 | 0.057 | 0.170 | 0.113 | 0.075 | 0.151 |
| 1.5-2.4 | 0.167 | 0.130 | 0.111 | 0.167 | 0.093 | 0.130 | 0.204 |
| 2.4-3.3 | 0.137 | 0.118 | 0.196 | 0.176 | 0.098 | 0.137 | 0.137 |
| 3.3-4.2 | 0.132 | 0.075 | 0.132 | 0.189 | 0.170 | 0.208 | 0.094 |
| 4.2-5.1 | 0.176 | 0.098 | 0.098 | 0.078 | 0.176 | 0.176 | 0.196 |
| 5.1-6.0 | 0.135 | 0.038 | 0.135 | 0.250 | 0.135 | 0.096 | 0.212 |
| 6.0-6.9 | 0.212 | 0.115 | 0.115 | 0.154 | 0.154 | 0.135 | 0.115 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1605)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.2308, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.189 | 0.132 | 0.075 | 0.208 | 0.189 | 0.094 | 0.113 |
| 1.5-2.4 | 0.130 | 0.111 | 0.130 | 0.167 | 0.111 | 0.185 | 0.167 |
| 2.4-3.3 | 0.157 | 0.176 | 0.176 | 0.216 | 0.059 | 0.137 | 0.078 |
| 3.3-4.2 | 0.075 | 0.113 | 0.113 | 0.170 | 0.170 | 0.245 | 0.113 |
| 4.2-5.1 | 0.176 | 0.118 | 0.176 | 0.157 | 0.098 | 0.176 | 0.098 |
| 5.1-6.0 | 0.096 | 0.154 | 0.077 | 0.212 | 0.115 | 0.154 | 0.192 |
| 6.0-6.9 | 0.192 | 0.077 | 0.077 | 0.192 | 0.096 | 0.135 | 0.231 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1590)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0943, support=53
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.0377, support=53
- `4.2-5.1`: recall=0.3333, support=51
- `5.1-6.0`: recall=0.0385, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.094 | 0.245 | 0.208 | 0.057 | 0.245 | 0.038 | 0.113 |
| 1.5-2.4 | 0.093 | 0.222 | 0.222 | 0.000 | 0.185 | 0.056 | 0.222 |
| 2.4-3.3 | 0.078 | 0.196 | 0.216 | 0.039 | 0.196 | 0.020 | 0.255 |
| 3.3-4.2 | 0.075 | 0.245 | 0.208 | 0.038 | 0.245 | 0.019 | 0.170 |
| 4.2-5.1 | 0.078 | 0.196 | 0.176 | 0.039 | 0.333 | 0.020 | 0.157 |
| 5.1-6.0 | 0.115 | 0.231 | 0.135 | 0.058 | 0.308 | 0.038 | 0.115 |
| 6.0-6.9 | 0.000 | 0.154 | 0.192 | 0.096 | 0.308 | 0.058 | 0.192 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1437)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0377, support=53
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1132, support=53
- `4.2-5.1`: recall=0.3725, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.038 | 0.189 | 0.094 | 0.113 | 0.321 | 0.094 | 0.151 |
| 1.5-2.4 | 0.074 | 0.167 | 0.167 | 0.111 | 0.278 | 0.056 | 0.148 |
| 2.4-3.3 | 0.039 | 0.157 | 0.098 | 0.157 | 0.314 | 0.039 | 0.196 |
| 3.3-4.2 | 0.019 | 0.170 | 0.132 | 0.113 | 0.340 | 0.038 | 0.189 |
| 4.2-5.1 | 0.020 | 0.098 | 0.157 | 0.137 | 0.373 | 0.059 | 0.157 |
| 5.1-6.0 | 0.058 | 0.096 | 0.231 | 0.212 | 0.308 | 0.058 | 0.038 |
| 6.0-6.9 | 0.058 | 0.135 | 0.115 | 0.192 | 0.308 | 0.038 | 0.154 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1098)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.0385, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.057 | 0.151 | 0.151 | 0.189 | 0.113 | 0.075 | 0.264 |
| 1.5-2.4 | 0.111 | 0.074 | 0.093 | 0.222 | 0.130 | 0.074 | 0.296 |
| 2.4-3.3 | 0.078 | 0.118 | 0.216 | 0.157 | 0.176 | 0.039 | 0.216 |
| 3.3-4.2 | 0.019 | 0.094 | 0.208 | 0.170 | 0.170 | 0.132 | 0.208 |
| 4.2-5.1 | 0.078 | 0.078 | 0.314 | 0.137 | 0.118 | 0.078 | 0.196 |
| 5.1-6.0 | 0.077 | 0.077 | 0.173 | 0.192 | 0.154 | 0.038 | 0.288 |
| 6.0-6.9 | 0.096 | 0.058 | 0.231 | 0.135 | 0.250 | 0.077 | 0.154 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1966)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1250, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.3529, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.125 | 0.312 | 0.188 | 0.062 | 0.062 | 0.062 | 0.188 |
| 1.5-2.4 | 0.188 | 0.250 | 0.250 | 0.000 | 0.250 | 0.000 | 0.062 |
| 2.4-3.3 | 0.059 | 0.118 | 0.353 | 0.118 | 0.176 | 0.118 | 0.059 |
| 3.3-4.2 | 0.000 | 0.294 | 0.294 | 0.059 | 0.059 | 0.176 | 0.118 |
| 4.2-5.1 | 0.000 | 0.167 | 0.500 | 0.000 | 0.222 | 0.056 | 0.056 |
| 5.1-6.0 | 0.111 | 0.167 | 0.056 | 0.111 | 0.278 | 0.167 | 0.111 |
| 6.0-6.9 | 0.056 | 0.111 | 0.222 | 0.167 | 0.111 | 0.167 | 0.167 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1878)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.375 | 0.375 | 0.125 | 0.062 | 0.000 | 0.062 |
| 1.5-2.4 | 0.062 | 0.188 | 0.500 | 0.062 | 0.062 | 0.062 | 0.062 |
| 2.4-3.3 | 0.059 | 0.176 | 0.471 | 0.000 | 0.235 | 0.059 | 0.000 |
| 3.3-4.2 | 0.059 | 0.235 | 0.353 | 0.000 | 0.294 | 0.059 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.333 | 0.056 | 0.611 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.222 | 0.333 | 0.056 | 0.222 | 0.056 | 0.111 |
| 6.0-6.9 | 0.000 | 0.389 | 0.222 | 0.056 | 0.222 | 0.111 | 0.000 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1599)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.375 | 0.500 | 0.000 | 0.125 | 0.000 | 0.000 |
| 1.5-2.4 | 0.062 | 0.312 | 0.312 | 0.000 | 0.312 | 0.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.412 | 0.176 | 0.000 | 0.412 | 0.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.353 | 0.353 | 0.000 | 0.294 | 0.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.278 | 0.111 | 0.000 | 0.611 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.667 | 0.000 | 0.167 | 0.000 | 0.111 |
| 6.0-6.9 | 0.056 | 0.333 | 0.222 | 0.000 | 0.389 | 0.000 | 0.000 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1427)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3125, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.312 | 0.062 | 0.062 | 0.062 | 0.125 | 0.312 | 0.062 |
| 1.5-2.4 | 0.125 | 0.062 | 0.375 | 0.188 | 0.125 | 0.062 | 0.062 |
| 2.4-3.3 | 0.000 | 0.176 | 0.118 | 0.059 | 0.176 | 0.235 | 0.235 |
| 3.3-4.2 | 0.000 | 0.235 | 0.118 | 0.000 | 0.235 | 0.118 | 0.294 |
| 4.2-5.1 | 0.000 | 0.056 | 0.333 | 0.167 | 0.278 | 0.167 | 0.000 |
| 5.1-6.0 | 0.167 | 0.167 | 0.111 | 0.111 | 0.222 | 0.167 | 0.056 |
| 6.0-6.9 | 0.278 | 0.111 | 0.167 | 0.111 | 0.222 | 0.056 | 0.056 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1368)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.062 | 0.312 | 0.000 | 0.000 | 0.125 | 0.375 | 0.125 |
| 1.5-2.4 | 0.250 | 0.188 | 0.312 | 0.000 | 0.188 | 0.062 | 0.000 |
| 2.4-3.3 | 0.059 | 0.176 | 0.235 | 0.000 | 0.294 | 0.118 | 0.118 |
| 3.3-4.2 | 0.059 | 0.118 | 0.294 | 0.000 | 0.118 | 0.118 | 0.294 |
| 4.2-5.1 | 0.000 | 0.056 | 0.389 | 0.000 | 0.222 | 0.167 | 0.167 |
| 5.1-6.0 | 0.111 | 0.222 | 0.056 | 0.222 | 0.056 | 0.222 | 0.111 |
| 6.0-6.9 | 0.111 | 0.278 | 0.056 | 0.000 | 0.222 | 0.333 | 0.000 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1355)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.062 | 0.250 | 0.062 | 0.125 | 0.062 | 0.438 | 0.000 |
| 1.5-2.4 | 0.312 | 0.125 | 0.375 | 0.000 | 0.125 | 0.062 | 0.000 |
| 2.4-3.3 | 0.118 | 0.118 | 0.294 | 0.000 | 0.235 | 0.118 | 0.118 |
| 3.3-4.2 | 0.000 | 0.294 | 0.294 | 0.000 | 0.176 | 0.118 | 0.118 |
| 4.2-5.1 | 0.000 | 0.000 | 0.444 | 0.056 | 0.167 | 0.167 | 0.167 |
| 5.1-6.0 | 0.056 | 0.278 | 0.167 | 0.111 | 0.056 | 0.278 | 0.056 |
| 6.0-6.9 | 0.056 | 0.278 | 0.333 | 0.000 | 0.278 | 0.056 | 0.000 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1290)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.0000, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.188 | 0.375 | 0.062 | 0.125 | 0.250 | 0.000 |
| 1.5-2.4 | 0.062 | 0.000 | 0.250 | 0.188 | 0.188 | 0.125 | 0.188 |
| 2.4-3.3 | 0.059 | 0.000 | 0.059 | 0.353 | 0.118 | 0.235 | 0.176 |
| 3.3-4.2 | 0.059 | 0.059 | 0.176 | 0.176 | 0.235 | 0.176 | 0.118 |
| 4.2-5.1 | 0.167 | 0.111 | 0.111 | 0.111 | 0.111 | 0.167 | 0.222 |
| 5.1-6.0 | 0.167 | 0.056 | 0.167 | 0.000 | 0.056 | 0.500 | 0.056 |
| 6.0-6.9 | 0.167 | 0.111 | 0.167 | 0.111 | 0.056 | 0.333 | 0.056 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.111 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 |
| 1.5-2.4 | 0.167 | 0.056 | 0.222 | 0.000 | 0.111 | 0.222 | 0.222 |
| 2.4-3.3 | 0.111 | 0.056 | 0.222 | 0.111 | 0.167 | 0.111 | 0.222 |
| 3.3-4.2 | 0.222 | 0.056 | 0.222 | 0.056 | 0.167 | 0.278 | 0.000 |
| 4.2-5.1 | 0.056 | 0.111 | 0.111 | 0.111 | 0.389 | 0.167 | 0.056 |
| 5.1-6.0 | 0.278 | 0.000 | 0.167 | 0.111 | 0.111 | 0.333 | 0.000 |
| 6.0-6.9 | 0.111 | 0.222 | 0.222 | 0.056 | 0.111 | 0.111 | 0.167 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.167 | 0.111 | 0.056 | 0.056 | 0.167 | 0.000 |
| 1.5-2.4 | 0.222 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 | 0.167 |
| 2.4-3.3 | 0.056 | 0.444 | 0.111 | 0.056 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.222 | 0.167 | 0.111 | 0.056 | 0.222 | 0.167 | 0.056 |
| 4.2-5.1 | 0.111 | 0.278 | 0.056 | 0.056 | 0.389 | 0.056 | 0.056 |
| 5.1-6.0 | 0.278 | 0.000 | 0.111 | 0.222 | 0.167 | 0.222 | 0.000 |
| 6.0-6.9 | 0.222 | 0.389 | 0.167 | 0.000 | 0.111 | 0.056 | 0.056 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.000 | 0.222 | 0.111 | 0.000 | 0.111 | 0.111 |
| 1.5-2.4 | 0.056 | 0.056 | 0.167 | 0.056 | 0.167 | 0.222 | 0.278 |
| 2.4-3.3 | 0.167 | 0.222 | 0.056 | 0.167 | 0.167 | 0.056 | 0.167 |
| 3.3-4.2 | 0.278 | 0.111 | 0.111 | 0.111 | 0.111 | 0.222 | 0.056 |
| 4.2-5.1 | 0.056 | 0.167 | 0.056 | 0.056 | 0.222 | 0.333 | 0.111 |
| 5.1-6.0 | 0.111 | 0.056 | 0.000 | 0.167 | 0.222 | 0.333 | 0.111 |
| 6.0-6.9 | 0.167 | 0.167 | 0.056 | 0.167 | 0.111 | 0.111 | 0.222 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.1857)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.111 | 0.167 | 0.056 | 0.111 | 0.111 | 0.111 |
| 1.5-2.4 | 0.167 | 0.056 | 0.333 | 0.056 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.222 | 0.111 | 0.056 | 0.056 | 0.333 | 0.000 | 0.222 |
| 3.3-4.2 | 0.222 | 0.056 | 0.167 | 0.111 | 0.167 | 0.111 | 0.167 |
| 4.2-5.1 | 0.000 | 0.056 | 0.167 | 0.222 | 0.333 | 0.056 | 0.167 |
| 5.1-6.0 | 0.222 | 0.000 | 0.000 | 0.222 | 0.222 | 0.278 | 0.056 |
| 6.0-6.9 | 0.111 | 0.222 | 0.333 | 0.000 | 0.056 | 0.111 | 0.167 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.056 | 0.167 | 0.167 | 0.056 | 0.111 | 0.056 |
| 1.5-2.4 | 0.278 | 0.056 | 0.167 | 0.111 | 0.056 | 0.111 | 0.222 |
| 2.4-3.3 | 0.167 | 0.111 | 0.111 | 0.111 | 0.222 | 0.111 | 0.167 |
| 3.3-4.2 | 0.333 | 0.056 | 0.167 | 0.111 | 0.111 | 0.167 | 0.056 |
| 4.2-5.1 | 0.000 | 0.111 | 0.222 | 0.167 | 0.167 | 0.278 | 0.056 |
| 5.1-6.0 | 0.278 | 0.167 | 0.000 | 0.111 | 0.167 | 0.278 | 0.000 |
| 6.0-6.9 | 0.167 | 0.222 | 0.167 | 0.111 | 0.167 | 0.056 | 0.111 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.1643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.167 | 0.222 | 0.111 | 0.000 | 0.222 | 0.000 |
| 1.5-2.4 | 0.167 | 0.056 | 0.056 | 0.167 | 0.111 | 0.111 | 0.333 |
| 2.4-3.3 | 0.222 | 0.167 | 0.056 | 0.056 | 0.167 | 0.111 | 0.222 |
| 3.3-4.2 | 0.333 | 0.000 | 0.167 | 0.111 | 0.167 | 0.222 | 0.000 |
| 4.2-5.1 | 0.056 | 0.111 | 0.167 | 0.222 | 0.167 | 0.167 | 0.111 |
| 5.1-6.0 | 0.167 | 0.111 | 0.000 | 0.333 | 0.167 | 0.222 | 0.000 |
| 6.0-6.9 | 0.056 | 0.222 | 0.111 | 0.222 | 0.111 | 0.000 | 0.278 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.1286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.111 | 0.111 | 0.278 | 0.111 | 0.000 | 0.333 | 0.056 |
| 1.5-2.4 | 0.333 | 0.056 | 0.111 | 0.111 | 0.167 | 0.000 | 0.222 |
| 2.4-3.3 | 0.222 | 0.278 | 0.111 | 0.222 | 0.111 | 0.000 | 0.056 |
| 3.3-4.2 | 0.056 | 0.111 | 0.167 | 0.222 | 0.111 | 0.222 | 0.111 |
| 4.2-5.1 | 0.167 | 0.222 | 0.111 | 0.056 | 0.222 | 0.111 | 0.111 |
| 5.1-6.0 | 0.389 | 0.000 | 0.167 | 0.000 | 0.333 | 0.056 | 0.056 |
| 6.0-6.9 | 0.000 | 0.278 | 0.278 | 0.111 | 0.111 | 0.056 | 0.167 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2071)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2642, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.3585, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.2115, support=52
- `6.0-6.9`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.264 | 0.094 | 0.264 | 0.151 | 0.075 | 0.057 | 0.094 |
| 1.5-2.4 | 0.259 | 0.074 | 0.111 | 0.222 | 0.074 | 0.056 | 0.204 |
| 2.4-3.3 | 0.098 | 0.059 | 0.176 | 0.255 | 0.098 | 0.137 | 0.176 |
| 3.3-4.2 | 0.094 | 0.038 | 0.189 | 0.358 | 0.038 | 0.151 | 0.132 |
| 4.2-5.1 | 0.020 | 0.039 | 0.157 | 0.314 | 0.098 | 0.157 | 0.216 |
| 5.1-6.0 | 0.077 | 0.019 | 0.058 | 0.269 | 0.077 | 0.212 | 0.288 |
| 6.0-6.9 | 0.077 | 0.038 | 0.096 | 0.308 | 0.038 | 0.154 | 0.288 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1920)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3585, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0392, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.1569, support=51
- `5.1-6.0`: recall=0.2115, support=52
- `6.0-6.9`: recall=0.3846, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.358 | 0.094 | 0.132 | 0.113 | 0.094 | 0.038 | 0.170 |
| 1.5-2.4 | 0.352 | 0.037 | 0.019 | 0.130 | 0.167 | 0.093 | 0.204 |
| 2.4-3.3 | 0.118 | 0.078 | 0.039 | 0.196 | 0.196 | 0.098 | 0.275 |
| 3.3-4.2 | 0.132 | 0.038 | 0.075 | 0.132 | 0.113 | 0.208 | 0.302 |
| 4.2-5.1 | 0.059 | 0.059 | 0.059 | 0.216 | 0.157 | 0.196 | 0.255 |
| 5.1-6.0 | 0.135 | 0.000 | 0.019 | 0.154 | 0.212 | 0.212 | 0.269 |
| 6.0-6.9 | 0.077 | 0.038 | 0.019 | 0.115 | 0.115 | 0.250 | 0.385 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1881)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1321, support=53
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.1321, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.2115, support=52
- `6.0-6.9`: recall=0.3269, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.132 | 0.208 | 0.170 | 0.019 | 0.094 | 0.038 | 0.340 |
| 1.5-2.4 | 0.204 | 0.167 | 0.111 | 0.056 | 0.074 | 0.148 | 0.241 |
| 2.4-3.3 | 0.137 | 0.039 | 0.176 | 0.059 | 0.157 | 0.098 | 0.333 |
| 3.3-4.2 | 0.057 | 0.094 | 0.075 | 0.132 | 0.132 | 0.132 | 0.377 |
| 4.2-5.1 | 0.118 | 0.059 | 0.118 | 0.118 | 0.176 | 0.118 | 0.294 |
| 5.1-6.0 | 0.058 | 0.154 | 0.192 | 0.077 | 0.096 | 0.212 | 0.212 |
| 6.0-6.9 | 0.115 | 0.058 | 0.038 | 0.115 | 0.173 | 0.173 | 0.327 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1867)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3208, support=53
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.0962, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.321 | 0.189 | 0.189 | 0.170 | 0.113 | 0.000 | 0.019 |
| 1.5-2.4 | 0.222 | 0.278 | 0.093 | 0.093 | 0.167 | 0.037 | 0.111 |
| 2.4-3.3 | 0.196 | 0.137 | 0.196 | 0.176 | 0.098 | 0.098 | 0.098 |
| 3.3-4.2 | 0.113 | 0.151 | 0.189 | 0.189 | 0.132 | 0.038 | 0.189 |
| 4.2-5.1 | 0.118 | 0.157 | 0.118 | 0.255 | 0.118 | 0.059 | 0.176 |
| 5.1-6.0 | 0.173 | 0.173 | 0.135 | 0.154 | 0.135 | 0.058 | 0.173 |
| 6.0-6.9 | 0.135 | 0.250 | 0.154 | 0.192 | 0.115 | 0.058 | 0.096 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1669)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2264, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.2115, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.226 | 0.226 | 0.019 | 0.151 | 0.057 | 0.019 | 0.302 |
| 1.5-2.4 | 0.241 | 0.111 | 0.111 | 0.185 | 0.019 | 0.093 | 0.241 |
| 2.4-3.3 | 0.039 | 0.176 | 0.078 | 0.216 | 0.078 | 0.137 | 0.275 |
| 3.3-4.2 | 0.113 | 0.113 | 0.019 | 0.245 | 0.075 | 0.189 | 0.245 |
| 4.2-5.1 | 0.039 | 0.098 | 0.059 | 0.275 | 0.039 | 0.255 | 0.235 |
| 5.1-6.0 | 0.077 | 0.096 | 0.038 | 0.269 | 0.096 | 0.192 | 0.231 |
| 6.0-6.9 | 0.154 | 0.096 | 0.019 | 0.269 | 0.058 | 0.192 | 0.212 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1649)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2642, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.3019, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.2308, support=52
- `6.0-6.9`: recall=0.1731, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.264 | 0.264 | 0.132 | 0.094 | 0.094 | 0.094 | 0.057 |
| 1.5-2.4 | 0.278 | 0.111 | 0.056 | 0.185 | 0.093 | 0.074 | 0.204 |
| 2.4-3.3 | 0.118 | 0.137 | 0.059 | 0.255 | 0.098 | 0.176 | 0.157 |
| 3.3-4.2 | 0.094 | 0.113 | 0.019 | 0.302 | 0.057 | 0.264 | 0.151 |
| 4.2-5.1 | 0.039 | 0.176 | 0.059 | 0.373 | 0.039 | 0.157 | 0.157 |
| 5.1-6.0 | 0.115 | 0.058 | 0.038 | 0.231 | 0.096 | 0.231 | 0.231 |
| 6.0-6.9 | 0.096 | 0.135 | 0.038 | 0.346 | 0.058 | 0.154 | 0.173 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1592)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0566, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.7358, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.057 | 0.057 | 0.075 | 0.642 | 0.094 | 0.075 | 0.000 |
| 1.5-2.4 | 0.056 | 0.000 | 0.056 | 0.778 | 0.074 | 0.037 | 0.000 |
| 2.4-3.3 | 0.078 | 0.020 | 0.020 | 0.765 | 0.059 | 0.039 | 0.020 |
| 3.3-4.2 | 0.038 | 0.057 | 0.057 | 0.736 | 0.038 | 0.038 | 0.038 |
| 4.2-5.1 | 0.020 | 0.020 | 0.000 | 0.804 | 0.039 | 0.118 | 0.000 |
| 5.1-6.0 | 0.038 | 0.019 | 0.019 | 0.712 | 0.038 | 0.173 | 0.000 |
| 6.0-6.9 | 0.038 | 0.019 | 0.019 | 0.788 | 0.038 | 0.038 | 0.058 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2347)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.3750, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.750 | 0.250 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.375 | 0.375 | 0.000 | 0.062 | 0.062 | 0.125 | 0.000 |
| 2.4-3.3 | 0.765 | 0.000 | 0.059 | 0.059 | 0.000 | 0.118 | 0.000 |
| 3.3-4.2 | 0.471 | 0.118 | 0.118 | 0.000 | 0.000 | 0.235 | 0.059 |
| 4.2-5.1 | 0.556 | 0.167 | 0.000 | 0.000 | 0.056 | 0.167 | 0.056 |
| 5.1-6.0 | 0.111 | 0.278 | 0.056 | 0.167 | 0.000 | 0.333 | 0.056 |
| 6.0-6.9 | 0.611 | 0.000 | 0.000 | 0.056 | 0.056 | 0.222 | 0.056 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2321)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.8125, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.812 | 0.125 | 0.062 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.438 | 0.250 | 0.000 | 0.250 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.412 | 0.118 | 0.000 | 0.118 | 0.000 | 0.235 | 0.118 |
| 3.3-4.2 | 0.294 | 0.235 | 0.059 | 0.118 | 0.000 | 0.235 | 0.059 |
| 4.2-5.1 | 0.333 | 0.111 | 0.000 | 0.222 | 0.000 | 0.222 | 0.111 |
| 5.1-6.0 | 0.056 | 0.222 | 0.000 | 0.222 | 0.000 | 0.389 | 0.111 |
| 6.0-6.9 | 0.278 | 0.222 | 0.056 | 0.056 | 0.000 | 0.333 | 0.056 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1983)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.4118, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.750 | 0.000 | 0.188 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.562 | 0.062 | 0.062 | 0.312 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.647 | 0.000 | 0.176 | 0.176 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.529 | 0.000 | 0.059 | 0.412 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.389 | 0.000 | 0.056 | 0.556 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.833 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.444 | 0.000 | 0.056 | 0.500 | 0.000 | 0.000 | 0.000 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1789)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=16
- `1.5-2.4`: recall=0.3750, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.438 | 0.000 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.438 | 0.375 | 0.062 | 0.000 | 0.062 | 0.062 | 0.000 |
| 2.4-3.3 | 0.235 | 0.471 | 0.059 | 0.118 | 0.000 | 0.118 | 0.000 |
| 3.3-4.2 | 0.471 | 0.176 | 0.000 | 0.176 | 0.059 | 0.059 | 0.059 |
| 4.2-5.1 | 0.278 | 0.167 | 0.056 | 0.389 | 0.000 | 0.111 | 0.000 |
| 5.1-6.0 | 0.278 | 0.167 | 0.000 | 0.389 | 0.000 | 0.056 | 0.111 |
| 6.0-6.9 | 0.444 | 0.111 | 0.056 | 0.278 | 0.000 | 0.056 | 0.056 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1695)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.062 | 0.438 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.188 | 0.188 | 0.438 | 0.062 | 0.000 | 0.062 | 0.062 |
| 2.4-3.3 | 0.118 | 0.176 | 0.294 | 0.235 | 0.059 | 0.059 | 0.059 |
| 3.3-4.2 | 0.059 | 0.118 | 0.647 | 0.118 | 0.000 | 0.000 | 0.059 |
| 4.2-5.1 | 0.167 | 0.000 | 0.389 | 0.278 | 0.056 | 0.056 | 0.056 |
| 5.1-6.0 | 0.056 | 0.056 | 0.333 | 0.222 | 0.111 | 0.000 | 0.222 |
| 6.0-6.9 | 0.056 | 0.000 | 0.500 | 0.222 | 0.111 | 0.056 | 0.056 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1542)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2500, support=16
- `1.5-2.4`: recall=0.6250, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.250 | 0.625 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.125 | 0.625 | 0.125 | 0.062 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.118 | 0.706 | 0.118 | 0.000 | 0.000 | 0.000 | 0.059 |
| 3.3-4.2 | 0.000 | 0.529 | 0.412 | 0.000 | 0.000 | 0.000 | 0.059 |
| 4.2-5.1 | 0.056 | 0.278 | 0.333 | 0.222 | 0.000 | 0.000 | 0.111 |
| 5.1-6.0 | 0.056 | 0.389 | 0.389 | 0.000 | 0.000 | 0.000 | 0.167 |
| 6.0-6.9 | 0.167 | 0.333 | 0.333 | 0.056 | 0.000 | 0.000 | 0.111 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1301)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2500, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.250 | 0.188 | 0.062 | 0.188 | 0.188 | 0.125 | 0.000 |
| 1.5-2.4 | 0.188 | 0.188 | 0.125 | 0.438 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.235 | 0.118 | 0.059 | 0.412 | 0.118 | 0.000 | 0.059 |
| 3.3-4.2 | 0.118 | 0.235 | 0.059 | 0.176 | 0.118 | 0.176 | 0.118 |
| 4.2-5.1 | 0.111 | 0.111 | 0.167 | 0.333 | 0.056 | 0.000 | 0.222 |
| 5.1-6.0 | 0.111 | 0.111 | 0.000 | 0.389 | 0.167 | 0.111 | 0.111 |
| 6.0-6.9 | 0.222 | 0.056 | 0.167 | 0.278 | 0.167 | 0.056 | 0.056 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6667, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.667 | 0.111 | 0.056 | 0.056 | 0.056 | 0.000 | 0.056 |
| 1.5-2.4 | 0.278 | 0.167 | 0.222 | 0.056 | 0.167 | 0.111 | 0.000 |
| 2.4-3.3 | 0.000 | 0.167 | 0.278 | 0.111 | 0.278 | 0.056 | 0.111 |
| 3.3-4.2 | 0.111 | 0.167 | 0.056 | 0.278 | 0.167 | 0.111 | 0.111 |
| 4.2-5.1 | 0.111 | 0.111 | 0.056 | 0.167 | 0.167 | 0.111 | 0.278 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.000 | 0.222 | 0.500 | 0.111 |
| 6.0-6.9 | 0.167 | 0.000 | 0.056 | 0.056 | 0.222 | 0.222 | 0.278 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6667, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.667 | 0.222 | 0.000 | 0.000 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.111 | 0.222 | 0.056 | 0.111 | 0.333 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.167 | 0.222 | 0.111 | 0.333 | 0.000 | 0.056 |
| 3.3-4.2 | 0.111 | 0.222 | 0.056 | 0.111 | 0.389 | 0.000 | 0.111 |
| 4.2-5.1 | 0.056 | 0.000 | 0.111 | 0.056 | 0.333 | 0.278 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.000 | 0.222 | 0.556 | 0.111 |
| 6.0-6.9 | 0.111 | 0.111 | 0.000 | 0.167 | 0.278 | 0.167 | 0.167 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.556 | 0.167 | 0.111 | 0.000 | 0.056 | 0.056 | 0.056 |
| 1.5-2.4 | 0.222 | 0.222 | 0.111 | 0.111 | 0.167 | 0.056 | 0.111 |
| 2.4-3.3 | 0.056 | 0.278 | 0.278 | 0.167 | 0.167 | 0.000 | 0.056 |
| 3.3-4.2 | 0.111 | 0.167 | 0.167 | 0.278 | 0.167 | 0.056 | 0.056 |
| 4.2-5.1 | 0.056 | 0.167 | 0.056 | 0.111 | 0.333 | 0.111 | 0.167 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.000 | 0.222 | 0.500 | 0.222 |
| 6.0-6.9 | 0.111 | 0.167 | 0.056 | 0.056 | 0.222 | 0.167 | 0.222 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.3889, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.056 | 0.000 | 0.167 | 0.278 | 0.000 | 0.056 |
| 1.5-2.4 | 0.167 | 0.222 | 0.111 | 0.056 | 0.333 | 0.056 | 0.056 |
| 2.4-3.3 | 0.056 | 0.111 | 0.333 | 0.056 | 0.278 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.056 | 0.389 | 0.278 | 0.000 | 0.111 |
| 4.2-5.1 | 0.111 | 0.167 | 0.167 | 0.167 | 0.167 | 0.056 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.111 | 0.056 | 0.167 | 0.333 | 0.278 |
| 6.0-6.9 | 0.278 | 0.111 | 0.000 | 0.222 | 0.222 | 0.111 | 0.056 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.611 | 0.056 | 0.000 | 0.167 | 0.111 | 0.000 | 0.056 |
| 1.5-2.4 | 0.056 | 0.167 | 0.167 | 0.222 | 0.167 | 0.167 | 0.056 |
| 2.4-3.3 | 0.111 | 0.167 | 0.333 | 0.111 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.167 | 0.167 | 0.111 | 0.111 | 0.222 | 0.111 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.222 | 0.167 | 0.056 | 0.278 | 0.111 |
| 5.1-6.0 | 0.056 | 0.000 | 0.111 | 0.000 | 0.167 | 0.556 | 0.111 |
| 6.0-6.9 | 0.167 | 0.056 | 0.000 | 0.111 | 0.222 | 0.278 | 0.167 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2571)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.222 | 0.222 | 0.056 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.167 | 0.167 | 0.167 | 0.111 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.000 | 0.222 | 0.333 | 0.222 | 0.056 | 0.056 | 0.111 |
| 3.3-4.2 | 0.167 | 0.167 | 0.056 | 0.056 | 0.278 | 0.056 | 0.222 |
| 4.2-5.1 | 0.111 | 0.056 | 0.056 | 0.167 | 0.333 | 0.222 | 0.056 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.000 | 0.222 | 0.500 | 0.111 |
| 6.0-6.9 | 0.167 | 0.000 | 0.000 | 0.167 | 0.222 | 0.278 | 0.167 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/eeg/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.4444, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.556 | 0.111 | 0.167 | 0.111 | 0.056 | 0.000 | 0.000 |
| 1.5-2.4 | 0.111 | 0.111 | 0.167 | 0.222 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.222 | 0.444 | 0.111 | 0.056 | 0.056 | 0.000 |
| 3.3-4.2 | 0.222 | 0.111 | 0.167 | 0.056 | 0.056 | 0.056 | 0.333 |
| 4.2-5.1 | 0.167 | 0.167 | 0.000 | 0.167 | 0.111 | 0.222 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.000 | 0.278 | 0.556 | 0.056 |
| 6.0-6.9 | 0.167 | 0.000 | 0.056 | 0.111 | 0.222 | 0.333 | 0.111 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2473)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3704, support=54
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1111, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.4528, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.370 | 0.222 | 0.056 | 0.111 | 0.019 | 0.074 | 0.148 |
| 1.5-2.4 | 0.204 | 0.167 | 0.019 | 0.148 | 0.111 | 0.111 | 0.241 |
| 2.4-3.3 | 0.148 | 0.111 | 0.111 | 0.111 | 0.093 | 0.185 | 0.241 |
| 3.3-4.2 | 0.037 | 0.056 | 0.111 | 0.148 | 0.111 | 0.259 | 0.278 |
| 4.2-5.1 | 0.057 | 0.132 | 0.019 | 0.189 | 0.094 | 0.245 | 0.264 |
| 5.1-6.0 | 0.057 | 0.075 | 0.000 | 0.094 | 0.094 | 0.340 | 0.340 |
| 6.0-6.9 | 0.038 | 0.170 | 0.019 | 0.151 | 0.019 | 0.151 | 0.453 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1952)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.2407, support=54
- `3.3-4.2`: recall=0.2963, support=54
- `4.2-5.1`: recall=0.1321, support=53
- `5.1-6.0`: recall=0.1509, support=53
- `6.0-6.9`: recall=0.1321, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.296 | 0.148 | 0.074 | 0.111 | 0.093 | 0.130 | 0.148 |
| 1.5-2.4 | 0.130 | 0.111 | 0.130 | 0.148 | 0.093 | 0.222 | 0.167 |
| 2.4-3.3 | 0.111 | 0.093 | 0.241 | 0.222 | 0.074 | 0.148 | 0.111 |
| 3.3-4.2 | 0.111 | 0.093 | 0.074 | 0.296 | 0.204 | 0.093 | 0.130 |
| 4.2-5.1 | 0.057 | 0.132 | 0.094 | 0.264 | 0.132 | 0.264 | 0.057 |
| 5.1-6.0 | 0.113 | 0.151 | 0.075 | 0.189 | 0.113 | 0.151 | 0.208 |
| 6.0-6.9 | 0.132 | 0.113 | 0.151 | 0.151 | 0.132 | 0.189 | 0.132 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1859)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2037, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.1296, support=54
- `4.2-5.1`: recall=0.1509, support=53
- `5.1-6.0`: recall=0.3019, support=53
- `6.0-6.9`: recall=0.3585, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.204 | 0.185 | 0.056 | 0.056 | 0.111 | 0.148 | 0.241 |
| 1.5-2.4 | 0.185 | 0.037 | 0.111 | 0.074 | 0.204 | 0.222 | 0.167 |
| 2.4-3.3 | 0.148 | 0.093 | 0.019 | 0.111 | 0.130 | 0.222 | 0.278 |
| 3.3-4.2 | 0.093 | 0.056 | 0.056 | 0.130 | 0.130 | 0.167 | 0.370 |
| 4.2-5.1 | 0.057 | 0.057 | 0.038 | 0.170 | 0.151 | 0.208 | 0.321 |
| 5.1-6.0 | 0.075 | 0.038 | 0.057 | 0.132 | 0.113 | 0.302 | 0.283 |
| 6.0-6.9 | 0.132 | 0.019 | 0.057 | 0.094 | 0.094 | 0.245 | 0.358 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1738)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.3019, support=53
- `6.0-6.9`: recall=0.2453, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.148 | 0.019 | 0.037 | 0.000 | 0.130 | 0.278 |
| 1.5-2.4 | 0.407 | 0.111 | 0.000 | 0.056 | 0.019 | 0.204 | 0.204 |
| 2.4-3.3 | 0.259 | 0.074 | 0.074 | 0.037 | 0.000 | 0.407 | 0.148 |
| 3.3-4.2 | 0.222 | 0.056 | 0.019 | 0.093 | 0.019 | 0.389 | 0.204 |
| 4.2-5.1 | 0.226 | 0.038 | 0.075 | 0.075 | 0.038 | 0.434 | 0.113 |
| 5.1-6.0 | 0.226 | 0.075 | 0.057 | 0.019 | 0.057 | 0.302 | 0.264 |
| 6.0-6.9 | 0.283 | 0.170 | 0.000 | 0.057 | 0.019 | 0.226 | 0.245 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1639)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1667, support=54
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.1852, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.167 | 0.111 | 0.167 | 0.148 | 0.111 | 0.130 | 0.167 |
| 1.5-2.4 | 0.222 | 0.111 | 0.167 | 0.093 | 0.148 | 0.148 | 0.111 |
| 2.4-3.3 | 0.148 | 0.111 | 0.093 | 0.148 | 0.056 | 0.241 | 0.204 |
| 3.3-4.2 | 0.148 | 0.074 | 0.056 | 0.185 | 0.074 | 0.278 | 0.185 |
| 4.2-5.1 | 0.226 | 0.094 | 0.075 | 0.113 | 0.075 | 0.245 | 0.170 |
| 5.1-6.0 | 0.151 | 0.019 | 0.038 | 0.151 | 0.226 | 0.340 | 0.075 |
| 6.0-6.9 | 0.057 | 0.113 | 0.075 | 0.132 | 0.151 | 0.321 | 0.151 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1291)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.5000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.000 | 0.593 | 0.019 | 0.000 | 0.333 | 0.056 |
| 1.5-2.4 | 0.000 | 0.000 | 0.556 | 0.037 | 0.000 | 0.333 | 0.074 |
| 2.4-3.3 | 0.000 | 0.000 | 0.500 | 0.019 | 0.000 | 0.333 | 0.148 |
| 3.3-4.2 | 0.000 | 0.000 | 0.630 | 0.000 | 0.019 | 0.315 | 0.037 |
| 4.2-5.1 | 0.000 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.075 |
| 5.1-6.0 | 0.019 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.057 |
| 6.0-6.9 | 0.000 | 0.000 | 0.623 | 0.000 | 0.038 | 0.302 | 0.038 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1276)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.2407, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.5283, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.019 | 0.056 | 0.296 | 0.056 | 0.556 | 0.000 | 0.019 |
| 1.5-2.4 | 0.037 | 0.000 | 0.407 | 0.019 | 0.519 | 0.019 | 0.000 |
| 2.4-3.3 | 0.019 | 0.130 | 0.241 | 0.000 | 0.519 | 0.019 | 0.074 |
| 3.3-4.2 | 0.019 | 0.037 | 0.407 | 0.019 | 0.500 | 0.000 | 0.019 |
| 4.2-5.1 | 0.038 | 0.113 | 0.321 | 0.000 | 0.528 | 0.000 | 0.000 |
| 5.1-6.0 | 0.038 | 0.057 | 0.283 | 0.000 | 0.604 | 0.000 | 0.019 |
| 6.0-6.9 | 0.019 | 0.075 | 0.208 | 0.038 | 0.623 | 0.000 | 0.038 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1984)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.167 | 0.222 | 0.111 | 0.056 | 0.056 | 0.056 |
| 1.5-2.4 | 0.167 | 0.444 | 0.167 | 0.111 | 0.000 | 0.056 | 0.056 |
| 2.4-3.3 | 0.167 | 0.722 | 0.000 | 0.056 | 0.000 | 0.000 | 0.056 |
| 3.3-4.2 | 0.176 | 0.412 | 0.118 | 0.118 | 0.000 | 0.059 | 0.118 |
| 4.2-5.1 | 0.111 | 0.167 | 0.056 | 0.167 | 0.111 | 0.167 | 0.222 |
| 5.1-6.0 | 0.167 | 0.111 | 0.000 | 0.222 | 0.111 | 0.111 | 0.278 |
| 6.0-6.9 | 0.000 | 0.111 | 0.000 | 0.111 | 0.278 | 0.222 | 0.278 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1984)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.111 | 0.333 | 0.000 | 0.000 | 0.056 | 0.278 | 0.222 |
| 1.5-2.4 | 0.000 | 0.389 | 0.000 | 0.000 | 0.000 | 0.500 | 0.111 |
| 2.4-3.3 | 0.000 | 0.389 | 0.000 | 0.000 | 0.056 | 0.444 | 0.111 |
| 3.3-4.2 | 0.000 | 0.235 | 0.059 | 0.059 | 0.000 | 0.529 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.056 | 0.000 | 0.111 | 0.778 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.111 | 0.056 | 0.611 | 0.111 |
| 6.0-6.9 | 0.000 | 0.000 | 0.056 | 0.056 | 0.000 | 0.778 | 0.111 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1905)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 |
| 1.5-2.4 | 0.444 | 0.000 | 0.000 | 0.056 | 0.000 | 0.389 | 0.111 |
| 2.4-3.3 | 0.222 | 0.167 | 0.056 | 0.000 | 0.000 | 0.500 | 0.056 |
| 3.3-4.2 | 0.118 | 0.118 | 0.000 | 0.000 | 0.000 | 0.765 | 0.000 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.167 | 0.000 | 0.667 | 0.056 |
| 5.1-6.0 | 0.056 | 0.111 | 0.000 | 0.111 | 0.056 | 0.611 | 0.056 |
| 6.0-6.9 | 0.000 | 0.056 | 0.000 | 0.222 | 0.000 | 0.556 | 0.167 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.111 | 0.056 | 0.056 | 0.056 | 0.222 | 0.278 |
| 1.5-2.4 | 0.222 | 0.167 | 0.000 | 0.167 | 0.056 | 0.222 | 0.167 |
| 2.4-3.3 | 0.167 | 0.111 | 0.000 | 0.111 | 0.222 | 0.333 | 0.056 |
| 3.3-4.2 | 0.000 | 0.176 | 0.059 | 0.118 | 0.000 | 0.529 | 0.118 |
| 4.2-5.1 | 0.056 | 0.000 | 0.000 | 0.389 | 0.167 | 0.222 | 0.167 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.444 | 0.056 | 0.333 | 0.167 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.556 | 0.000 | 0.167 | 0.278 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.056 | 0.000 | 0.222 | 0.167 | 0.056 | 0.167 |
| 1.5-2.4 | 0.333 | 0.167 | 0.056 | 0.167 | 0.167 | 0.056 | 0.056 |
| 2.4-3.3 | 0.056 | 0.278 | 0.111 | 0.222 | 0.278 | 0.000 | 0.056 |
| 3.3-4.2 | 0.235 | 0.235 | 0.059 | 0.118 | 0.118 | 0.118 | 0.118 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.667 | 0.167 | 0.000 | 0.056 |
| 5.1-6.0 | 0.111 | 0.111 | 0.167 | 0.278 | 0.278 | 0.000 | 0.056 |
| 6.0-6.9 | 0.056 | 0.111 | 0.056 | 0.389 | 0.167 | 0.111 | 0.111 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1032)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.222 | 0.000 | 0.000 | 0.500 | 0.000 | 0.278 |
| 1.5-2.4 | 0.000 | 0.222 | 0.000 | 0.000 | 0.500 | 0.000 | 0.278 |
| 2.4-3.3 | 0.000 | 0.389 | 0.000 | 0.000 | 0.500 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.353 | 0.000 | 0.000 | 0.471 | 0.000 | 0.176 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.222 | 0.444 | 0.056 | 0.222 | 0.000 | 0.000 | 0.056 |
| 2.4-3.3 | 0.056 | 0.333 | 0.111 | 0.222 | 0.111 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.389 | 0.000 | 0.111 | 0.278 | 0.111 | 0.056 |
| 4.2-5.1 | 0.059 | 0.118 | 0.000 | 0.294 | 0.059 | 0.294 | 0.176 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.111 | 0.222 | 0.444 | 0.056 |
| 6.0-6.9 | 0.056 | 0.222 | 0.167 | 0.056 | 0.389 | 0.056 | 0.056 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.333 | 0.167 | 0.056 | 0.000 | 0.000 | 0.056 |
| 1.5-2.4 | 0.444 | 0.278 | 0.111 | 0.111 | 0.000 | 0.056 | 0.000 |
| 2.4-3.3 | 0.111 | 0.111 | 0.167 | 0.278 | 0.111 | 0.111 | 0.111 |
| 3.3-4.2 | 0.000 | 0.167 | 0.222 | 0.278 | 0.167 | 0.056 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.118 | 0.294 | 0.235 | 0.235 | 0.059 |
| 5.1-6.0 | 0.056 | 0.111 | 0.111 | 0.167 | 0.167 | 0.222 | 0.167 |
| 6.0-6.9 | 0.056 | 0.056 | 0.111 | 0.389 | 0.167 | 0.111 | 0.111 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.389 | 0.000 | 0.000 | 0.000 | 0.333 | 0.000 |
| 1.5-2.4 | 0.056 | 0.500 | 0.056 | 0.056 | 0.056 | 0.278 | 0.000 |
| 2.4-3.3 | 0.056 | 0.167 | 0.000 | 0.222 | 0.167 | 0.389 | 0.000 |
| 3.3-4.2 | 0.056 | 0.222 | 0.000 | 0.111 | 0.167 | 0.444 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.176 | 0.176 | 0.471 | 0.118 |
| 5.1-6.0 | 0.056 | 0.167 | 0.000 | 0.056 | 0.333 | 0.389 | 0.000 |
| 6.0-6.9 | 0.111 | 0.111 | 0.056 | 0.056 | 0.333 | 0.333 | 0.000 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2214)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.278 | 0.056 | 0.056 | 0.000 | 0.056 | 0.056 |
| 1.5-2.4 | 0.333 | 0.222 | 0.056 | 0.167 | 0.111 | 0.000 | 0.111 |
| 2.4-3.3 | 0.167 | 0.111 | 0.056 | 0.389 | 0.111 | 0.000 | 0.167 |
| 3.3-4.2 | 0.056 | 0.278 | 0.056 | 0.000 | 0.222 | 0.278 | 0.111 |
| 4.2-5.1 | 0.059 | 0.000 | 0.118 | 0.235 | 0.176 | 0.235 | 0.176 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.111 | 0.222 | 0.444 | 0.111 |
| 6.0-6.9 | 0.056 | 0.111 | 0.000 | 0.167 | 0.389 | 0.111 | 0.167 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1714)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0556, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.056 | 0.056 | 0.222 | 0.167 | 0.222 | 0.222 | 0.056 |
| 1.5-2.4 | 0.056 | 0.111 | 0.278 | 0.167 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.278 | 0.167 | 0.222 | 0.222 | 0.056 |
| 3.3-4.2 | 0.111 | 0.000 | 0.167 | 0.167 | 0.222 | 0.278 | 0.056 |
| 4.2-5.1 | 0.059 | 0.000 | 0.235 | 0.118 | 0.118 | 0.294 | 0.176 |
| 5.1-6.0 | 0.111 | 0.000 | 0.222 | 0.111 | 0.278 | 0.222 | 0.056 |
| 6.0-6.9 | 0.111 | 0.056 | 0.167 | 0.167 | 0.222 | 0.278 | 0.000 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.1643)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.278 | 0.111 | 0.111 | 0.111 | 0.111 | 0.000 |
| 1.5-2.4 | 0.278 | 0.222 | 0.111 | 0.000 | 0.222 | 0.056 | 0.111 |
| 2.4-3.3 | 0.167 | 0.111 | 0.111 | 0.167 | 0.222 | 0.111 | 0.111 |
| 3.3-4.2 | 0.111 | 0.167 | 0.111 | 0.111 | 0.111 | 0.222 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.059 | 0.118 | 0.235 | 0.353 | 0.235 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.389 | 0.167 | 0.167 | 0.167 |
| 6.0-6.9 | 0.111 | 0.111 | 0.111 | 0.056 | 0.500 | 0.111 | 0.000 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.1571)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/fused/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.167 | 0.056 | 0.167 | 0.000 | 0.056 | 0.111 |
| 1.5-2.4 | 0.389 | 0.056 | 0.000 | 0.333 | 0.000 | 0.056 | 0.167 |
| 2.4-3.3 | 0.056 | 0.111 | 0.056 | 0.333 | 0.167 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.167 | 0.111 | 0.056 | 0.278 | 0.167 | 0.111 |
| 4.2-5.1 | 0.059 | 0.176 | 0.118 | 0.176 | 0.000 | 0.235 | 0.235 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.222 | 0.111 | 0.278 | 0.222 |
| 6.0-6.9 | 0.000 | 0.111 | 0.278 | 0.111 | 0.167 | 0.167 | 0.167 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1935)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4259, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.2037, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.3585, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.426 | 0.148 | 0.019 | 0.111 | 0.019 | 0.185 | 0.093 |
| 1.5-2.4 | 0.407 | 0.093 | 0.056 | 0.111 | 0.111 | 0.148 | 0.074 |
| 2.4-3.3 | 0.148 | 0.185 | 0.056 | 0.148 | 0.037 | 0.222 | 0.204 |
| 3.3-4.2 | 0.074 | 0.167 | 0.000 | 0.204 | 0.074 | 0.370 | 0.111 |
| 4.2-5.1 | 0.132 | 0.151 | 0.038 | 0.189 | 0.038 | 0.340 | 0.113 |
| 5.1-6.0 | 0.113 | 0.113 | 0.038 | 0.245 | 0.019 | 0.208 | 0.264 |
| 6.0-6.9 | 0.094 | 0.113 | 0.057 | 0.075 | 0.094 | 0.208 | 0.358 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1935)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3519, support=54
- `1.5-2.4`: recall=0.3333, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.1296, support=54
- `4.2-5.1`: recall=0.1132, support=53
- `5.1-6.0`: recall=0.2453, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.352 | 0.278 | 0.019 | 0.037 | 0.037 | 0.185 | 0.093 |
| 1.5-2.4 | 0.296 | 0.333 | 0.000 | 0.019 | 0.056 | 0.148 | 0.148 |
| 2.4-3.3 | 0.167 | 0.241 | 0.037 | 0.074 | 0.111 | 0.259 | 0.111 |
| 3.3-4.2 | 0.185 | 0.111 | 0.000 | 0.130 | 0.222 | 0.296 | 0.056 |
| 4.2-5.1 | 0.226 | 0.132 | 0.038 | 0.094 | 0.113 | 0.340 | 0.057 |
| 5.1-6.0 | 0.264 | 0.094 | 0.000 | 0.113 | 0.113 | 0.245 | 0.170 |
| 6.0-6.9 | 0.151 | 0.094 | 0.038 | 0.151 | 0.113 | 0.283 | 0.170 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1798)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.1481, support=54
- `3.3-4.2`: recall=0.1852, support=54
- `4.2-5.1`: recall=0.1698, support=53
- `5.1-6.0`: recall=0.1132, support=53
- `6.0-6.9`: recall=0.3396, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.167 | 0.148 | 0.241 | 0.093 | 0.074 | 0.056 |
| 1.5-2.4 | 0.204 | 0.093 | 0.259 | 0.167 | 0.167 | 0.000 | 0.111 |
| 2.4-3.3 | 0.130 | 0.111 | 0.148 | 0.093 | 0.222 | 0.130 | 0.167 |
| 3.3-4.2 | 0.111 | 0.148 | 0.148 | 0.185 | 0.093 | 0.185 | 0.130 |
| 4.2-5.1 | 0.038 | 0.132 | 0.151 | 0.170 | 0.170 | 0.113 | 0.226 |
| 5.1-6.0 | 0.038 | 0.075 | 0.113 | 0.113 | 0.151 | 0.113 | 0.396 |
| 6.0-6.9 | 0.075 | 0.057 | 0.132 | 0.132 | 0.226 | 0.038 | 0.340 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1676)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.2037, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.3585, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.019 | 0.000 | 0.278 | 0.019 | 0.185 | 0.167 |
| 1.5-2.4 | 0.278 | 0.019 | 0.019 | 0.185 | 0.093 | 0.204 | 0.204 |
| 2.4-3.3 | 0.148 | 0.037 | 0.000 | 0.241 | 0.130 | 0.259 | 0.185 |
| 3.3-4.2 | 0.130 | 0.000 | 0.019 | 0.204 | 0.130 | 0.352 | 0.167 |
| 4.2-5.1 | 0.057 | 0.019 | 0.019 | 0.245 | 0.075 | 0.321 | 0.264 |
| 5.1-6.0 | 0.019 | 0.075 | 0.000 | 0.264 | 0.038 | 0.358 | 0.245 |
| 6.0-6.9 | 0.075 | 0.038 | 0.057 | 0.208 | 0.057 | 0.396 | 0.170 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1553)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.2963, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.1132, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.296 | 0.093 | 0.019 | 0.111 | 0.130 | 0.241 | 0.111 |
| 1.5-2.4 | 0.315 | 0.037 | 0.074 | 0.130 | 0.130 | 0.185 | 0.130 |
| 2.4-3.3 | 0.111 | 0.148 | 0.074 | 0.278 | 0.037 | 0.204 | 0.148 |
| 3.3-4.2 | 0.130 | 0.148 | 0.037 | 0.296 | 0.111 | 0.148 | 0.130 |
| 4.2-5.1 | 0.094 | 0.113 | 0.075 | 0.189 | 0.057 | 0.283 | 0.189 |
| 5.1-6.0 | 0.132 | 0.189 | 0.038 | 0.226 | 0.075 | 0.208 | 0.132 |
| 6.0-6.9 | 0.132 | 0.113 | 0.094 | 0.170 | 0.113 | 0.264 | 0.113 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1291)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.5000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.3396, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.000 | 0.593 | 0.019 | 0.000 | 0.333 | 0.056 |
| 1.5-2.4 | 0.000 | 0.000 | 0.556 | 0.037 | 0.000 | 0.333 | 0.074 |
| 2.4-3.3 | 0.000 | 0.000 | 0.500 | 0.019 | 0.000 | 0.333 | 0.148 |
| 3.3-4.2 | 0.000 | 0.000 | 0.630 | 0.000 | 0.019 | 0.315 | 0.037 |
| 4.2-5.1 | 0.000 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.075 |
| 5.1-6.0 | 0.019 | 0.000 | 0.585 | 0.000 | 0.000 | 0.340 | 0.057 |
| 6.0-6.9 | 0.000 | 0.000 | 0.623 | 0.000 | 0.038 | 0.302 | 0.038 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1235)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0185, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.2407, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.4906, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.019 | 0.056 | 0.333 | 0.056 | 0.519 | 0.000 | 0.019 |
| 1.5-2.4 | 0.037 | 0.000 | 0.444 | 0.019 | 0.500 | 0.000 | 0.000 |
| 2.4-3.3 | 0.019 | 0.130 | 0.241 | 0.000 | 0.537 | 0.000 | 0.074 |
| 3.3-4.2 | 0.019 | 0.037 | 0.407 | 0.019 | 0.500 | 0.000 | 0.019 |
| 4.2-5.1 | 0.038 | 0.132 | 0.340 | 0.000 | 0.491 | 0.000 | 0.000 |
| 5.1-6.0 | 0.038 | 0.075 | 0.321 | 0.000 | 0.547 | 0.000 | 0.019 |
| 6.0-6.9 | 0.019 | 0.075 | 0.226 | 0.038 | 0.604 | 0.000 | 0.038 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2401)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6667, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.667 | 0.056 | 0.056 | 0.000 | 0.056 | 0.111 | 0.056 |
| 1.5-2.4 | 0.222 | 0.167 | 0.222 | 0.056 | 0.000 | 0.222 | 0.111 |
| 2.4-3.3 | 0.222 | 0.056 | 0.111 | 0.167 | 0.111 | 0.278 | 0.056 |
| 3.3-4.2 | 0.235 | 0.059 | 0.000 | 0.176 | 0.059 | 0.412 | 0.059 |
| 4.2-5.1 | 0.056 | 0.000 | 0.056 | 0.389 | 0.278 | 0.111 | 0.111 |
| 5.1-6.0 | 0.111 | 0.000 | 0.111 | 0.333 | 0.167 | 0.278 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.056 | 0.556 | 0.222 | 0.167 | 0.000 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2222)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.611 | 0.000 | 0.000 | 0.000 | 0.056 | 0.333 | 0.000 |
| 1.5-2.4 | 0.500 | 0.056 | 0.000 | 0.000 | 0.000 | 0.444 | 0.000 |
| 2.4-3.3 | 0.333 | 0.056 | 0.000 | 0.000 | 0.111 | 0.500 | 0.000 |
| 3.3-4.2 | 0.294 | 0.000 | 0.059 | 0.000 | 0.059 | 0.471 | 0.118 |
| 4.2-5.1 | 0.000 | 0.000 | 0.111 | 0.000 | 0.111 | 0.556 | 0.222 |
| 5.1-6.0 | 0.056 | 0.000 | 0.167 | 0.000 | 0.056 | 0.500 | 0.222 |
| 6.0-6.9 | 0.000 | 0.000 | 0.111 | 0.000 | 0.000 | 0.611 | 0.278 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1825)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.611 | 0.000 | 0.000 | 0.000 | 0.056 | 0.111 | 0.222 |
| 1.5-2.4 | 0.500 | 0.056 | 0.056 | 0.000 | 0.000 | 0.111 | 0.278 |
| 2.4-3.3 | 0.222 | 0.056 | 0.222 | 0.056 | 0.000 | 0.222 | 0.222 |
| 3.3-4.2 | 0.176 | 0.000 | 0.353 | 0.000 | 0.000 | 0.412 | 0.059 |
| 4.2-5.1 | 0.056 | 0.000 | 0.389 | 0.111 | 0.000 | 0.389 | 0.056 |
| 5.1-6.0 | 0.056 | 0.000 | 0.444 | 0.056 | 0.000 | 0.333 | 0.111 |
| 6.0-6.9 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.444 | 0.056 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1508)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.167 | 0.333 | 0.000 | 0.167 | 0.000 | 0.000 | 0.333 |
| 1.5-2.4 | 0.111 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.389 |
| 2.4-3.3 | 0.000 | 0.333 | 0.000 | 0.000 | 0.000 | 0.222 | 0.444 |
| 3.3-4.2 | 0.000 | 0.471 | 0.000 | 0.000 | 0.000 | 0.235 | 0.294 |
| 4.2-5.1 | 0.056 | 0.389 | 0.000 | 0.056 | 0.000 | 0.167 | 0.333 |
| 5.1-6.0 | 0.000 | 0.444 | 0.000 | 0.000 | 0.000 | 0.111 | 0.444 |
| 6.0-6.9 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.167 | 0.333 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1270)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.000 | 0.056 | 0.000 | 0.167 | 0.167 | 0.167 |
| 1.5-2.4 | 0.389 | 0.000 | 0.000 | 0.111 | 0.000 | 0.167 | 0.333 |
| 2.4-3.3 | 0.278 | 0.278 | 0.056 | 0.056 | 0.000 | 0.111 | 0.222 |
| 3.3-4.2 | 0.118 | 0.176 | 0.059 | 0.059 | 0.000 | 0.529 | 0.059 |
| 4.2-5.1 | 0.167 | 0.000 | 0.222 | 0.222 | 0.000 | 0.333 | 0.056 |
| 5.1-6.0 | 0.056 | 0.111 | 0.278 | 0.167 | 0.000 | 0.333 | 0.056 |
| 6.0-6.9 | 0.167 | 0.000 | 0.389 | 0.000 | 0.056 | 0.389 | 0.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1032)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.222 | 0.000 | 0.000 | 0.500 | 0.000 | 0.278 |
| 1.5-2.4 | 0.000 | 0.222 | 0.000 | 0.000 | 0.500 | 0.000 | 0.278 |
| 2.4-3.3 | 0.000 | 0.389 | 0.000 | 0.000 | 0.500 | 0.000 | 0.111 |
| 3.3-4.2 | 0.000 | 0.412 | 0.000 | 0.000 | 0.471 | 0.000 | 0.118 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3286)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.333 | 0.056 | 0.000 | 0.056 | 0.056 | 0.056 |
| 1.5-2.4 | 0.444 | 0.333 | 0.111 | 0.111 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.167 | 0.056 | 0.278 | 0.111 | 0.222 | 0.056 | 0.111 |
| 3.3-4.2 | 0.056 | 0.056 | 0.222 | 0.222 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.059 | 0.000 | 0.059 | 0.235 | 0.294 | 0.235 | 0.118 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.056 | 0.167 | 0.389 | 0.333 |
| 6.0-6.9 | 0.000 | 0.056 | 0.111 | 0.111 | 0.222 | 0.222 | 0.278 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1667, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.167 | 0.278 | 0.167 | 0.056 | 0.167 | 0.056 | 0.111 |
| 1.5-2.4 | 0.222 | 0.278 | 0.056 | 0.222 | 0.056 | 0.000 | 0.167 |
| 2.4-3.3 | 0.111 | 0.167 | 0.278 | 0.167 | 0.222 | 0.056 | 0.000 |
| 3.3-4.2 | 0.000 | 0.111 | 0.222 | 0.278 | 0.056 | 0.111 | 0.222 |
| 4.2-5.1 | 0.000 | 0.118 | 0.059 | 0.118 | 0.294 | 0.235 | 0.176 |
| 5.1-6.0 | 0.056 | 0.056 | 0.111 | 0.056 | 0.056 | 0.444 | 0.222 |
| 6.0-6.9 | 0.056 | 0.056 | 0.056 | 0.056 | 0.222 | 0.278 | 0.278 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3143)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.4706, support=17
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.333 | 0.056 | 0.056 | 0.111 | 0.167 | 0.056 |
| 1.5-2.4 | 0.222 | 0.278 | 0.000 | 0.167 | 0.111 | 0.222 | 0.000 |
| 2.4-3.3 | 0.278 | 0.111 | 0.111 | 0.278 | 0.111 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.000 | 0.167 | 0.167 | 0.278 | 0.278 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.176 | 0.118 | 0.471 | 0.059 | 0.176 |
| 5.1-6.0 | 0.056 | 0.000 | 0.111 | 0.000 | 0.167 | 0.556 | 0.111 |
| 6.0-6.9 | 0.056 | 0.000 | 0.000 | 0.222 | 0.389 | 0.167 | 0.167 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.333 | 0.167 | 0.056 | 0.000 | 0.000 | 0.167 |
| 1.5-2.4 | 0.389 | 0.333 | 0.167 | 0.056 | 0.056 | 0.000 | 0.000 |
| 2.4-3.3 | 0.111 | 0.056 | 0.333 | 0.111 | 0.167 | 0.111 | 0.111 |
| 3.3-4.2 | 0.056 | 0.167 | 0.056 | 0.278 | 0.111 | 0.222 | 0.111 |
| 4.2-5.1 | 0.059 | 0.000 | 0.118 | 0.235 | 0.294 | 0.176 | 0.118 |
| 5.1-6.0 | 0.056 | 0.000 | 0.111 | 0.111 | 0.278 | 0.111 | 0.333 |
| 6.0-6.9 | 0.000 | 0.056 | 0.222 | 0.056 | 0.167 | 0.278 | 0.222 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.278 | 0.056 | 0.000 | 0.111 | 0.222 | 0.111 |
| 1.5-2.4 | 0.056 | 0.444 | 0.111 | 0.111 | 0.056 | 0.167 | 0.056 |
| 2.4-3.3 | 0.000 | 0.167 | 0.111 | 0.111 | 0.167 | 0.444 | 0.000 |
| 3.3-4.2 | 0.000 | 0.167 | 0.222 | 0.056 | 0.167 | 0.333 | 0.056 |
| 4.2-5.1 | 0.000 | 0.000 | 0.118 | 0.118 | 0.294 | 0.412 | 0.059 |
| 5.1-6.0 | 0.000 | 0.167 | 0.056 | 0.167 | 0.167 | 0.444 | 0.000 |
| 6.0-6.9 | 0.056 | 0.111 | 0.000 | 0.000 | 0.278 | 0.500 | 0.056 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.389 | 0.111 | 0.111 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.389 | 0.222 | 0.000 | 0.278 | 0.000 | 0.000 | 0.111 |
| 2.4-3.3 | 0.111 | 0.389 | 0.167 | 0.167 | 0.000 | 0.167 | 0.000 |
| 3.3-4.2 | 0.167 | 0.111 | 0.167 | 0.167 | 0.111 | 0.167 | 0.111 |
| 4.2-5.1 | 0.176 | 0.235 | 0.000 | 0.176 | 0.059 | 0.235 | 0.118 |
| 5.1-6.0 | 0.000 | 0.000 | 0.056 | 0.278 | 0.111 | 0.222 | 0.333 |
| 6.0-6.9 | 0.111 | 0.167 | 0.000 | 0.167 | 0.056 | 0.333 | 0.167 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1786)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_all_bins/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1111, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.111 | 0.056 | 0.167 | 0.167 | 0.222 | 0.222 | 0.056 |
| 1.5-2.4 | 0.000 | 0.111 | 0.222 | 0.278 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.056 | 0.000 | 0.222 | 0.167 | 0.278 | 0.222 | 0.056 |
| 3.3-4.2 | 0.111 | 0.000 | 0.222 | 0.167 | 0.167 | 0.278 | 0.056 |
| 4.2-5.1 | 0.059 | 0.000 | 0.235 | 0.176 | 0.118 | 0.235 | 0.176 |
| 5.1-6.0 | 0.111 | 0.000 | 0.222 | 0.111 | 0.333 | 0.167 | 0.056 |
| 6.0-6.9 | 0.167 | 0.000 | 0.167 | 0.167 | 0.167 | 0.278 | 0.056 |


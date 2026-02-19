# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_omit_hardest.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1985)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.189 | 0.245 | 0.113 | 0.151 | 0.189 | 0.113 |
| 1.5-2.4 | 0.296 | 0.185 | 0.185 | 0.148 | 0.093 | 0.093 |
| 2.4-3.3 | 0.157 | 0.176 | 0.196 | 0.255 | 0.157 | 0.059 |
| 3.3-4.2 | 0.132 | 0.170 | 0.132 | 0.245 | 0.189 | 0.132 |
| 4.2-5.1 | 0.118 | 0.137 | 0.196 | 0.216 | 0.255 | 0.078 |
| 5.1-6.0 | 0.173 | 0.096 | 0.154 | 0.231 | 0.192 | 0.154 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1900)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.1111, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.2830, support=53
- `4.2-5.1`: recall=0.2353, support=51
- `5.1-6.0`: recall=0.2115, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.208 | 0.151 | 0.113 | 0.170 | 0.189 | 0.170 |
| 1.5-2.4 | 0.167 | 0.111 | 0.148 | 0.204 | 0.185 | 0.185 |
| 2.4-3.3 | 0.196 | 0.176 | 0.137 | 0.216 | 0.118 | 0.157 |
| 3.3-4.2 | 0.113 | 0.094 | 0.094 | 0.283 | 0.208 | 0.208 |
| 4.2-5.1 | 0.157 | 0.098 | 0.137 | 0.176 | 0.235 | 0.196 |
| 5.1-6.0 | 0.192 | 0.135 | 0.096 | 0.231 | 0.135 | 0.212 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1754)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0943, support=53
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.2941, support=51
- `3.3-4.2`: recall=0.0755, support=53
- `4.2-5.1`: recall=0.3529, support=51
- `5.1-6.0`: recall=0.0385, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.094 | 0.226 | 0.264 | 0.113 | 0.264 | 0.038 |
| 1.5-2.4 | 0.130 | 0.241 | 0.259 | 0.074 | 0.241 | 0.056 |
| 2.4-3.3 | 0.078 | 0.275 | 0.294 | 0.059 | 0.275 | 0.020 |
| 3.3-4.2 | 0.075 | 0.245 | 0.264 | 0.075 | 0.321 | 0.019 |
| 4.2-5.1 | 0.078 | 0.196 | 0.275 | 0.078 | 0.353 | 0.020 |
| 5.1-6.0 | 0.135 | 0.231 | 0.212 | 0.077 | 0.308 | 0.038 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1742)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1509, support=53
- `1.5-2.4`: recall=0.0741, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.3396, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.151 | 0.170 | 0.019 | 0.302 | 0.132 | 0.226 |
| 1.5-2.4 | 0.111 | 0.074 | 0.204 | 0.259 | 0.130 | 0.222 |
| 2.4-3.3 | 0.098 | 0.118 | 0.137 | 0.255 | 0.196 | 0.196 |
| 3.3-4.2 | 0.075 | 0.075 | 0.075 | 0.340 | 0.264 | 0.170 |
| 4.2-5.1 | 0.078 | 0.020 | 0.137 | 0.255 | 0.196 | 0.314 |
| 5.1-6.0 | 0.154 | 0.077 | 0.096 | 0.269 | 0.212 | 0.192 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1727)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2075, support=53
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.1887, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.2500, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.208 | 0.151 | 0.094 | 0.264 | 0.189 | 0.094 |
| 1.5-2.4 | 0.185 | 0.167 | 0.148 | 0.185 | 0.185 | 0.130 |
| 2.4-3.3 | 0.157 | 0.176 | 0.176 | 0.196 | 0.157 | 0.137 |
| 3.3-4.2 | 0.151 | 0.132 | 0.113 | 0.189 | 0.170 | 0.245 |
| 4.2-5.1 | 0.216 | 0.098 | 0.157 | 0.235 | 0.059 | 0.235 |
| 5.1-6.0 | 0.154 | 0.154 | 0.115 | 0.250 | 0.077 | 0.250 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1685)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0189, support=53
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.2745, support=51
- `5.1-6.0`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.019 | 0.208 | 0.170 | 0.264 | 0.226 | 0.113 |
| 1.5-2.4 | 0.019 | 0.259 | 0.204 | 0.185 | 0.222 | 0.111 |
| 2.4-3.3 | 0.059 | 0.196 | 0.157 | 0.275 | 0.255 | 0.059 |
| 3.3-4.2 | 0.000 | 0.245 | 0.113 | 0.264 | 0.302 | 0.075 |
| 4.2-5.1 | 0.020 | 0.118 | 0.216 | 0.255 | 0.275 | 0.118 |
| 5.1-6.0 | 0.058 | 0.173 | 0.212 | 0.192 | 0.288 | 0.077 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1637)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1132, support=53
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.0566, support=53
- `4.2-5.1`: recall=0.3529, support=51
- `5.1-6.0`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.113 | 0.113 | 0.132 | 0.208 | 0.302 | 0.132 |
| 1.5-2.4 | 0.204 | 0.167 | 0.130 | 0.074 | 0.222 | 0.204 |
| 2.4-3.3 | 0.078 | 0.216 | 0.137 | 0.118 | 0.294 | 0.157 |
| 3.3-4.2 | 0.151 | 0.132 | 0.094 | 0.057 | 0.245 | 0.321 |
| 4.2-5.1 | 0.078 | 0.118 | 0.176 | 0.078 | 0.353 | 0.196 |
| 5.1-6.0 | 0.038 | 0.135 | 0.192 | 0.096 | 0.346 | 0.192 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2123)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3750, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.375 | 0.062 | 0.000 | 0.125 | 0.188 | 0.250 |
| 1.5-2.4 | 0.125 | 0.062 | 0.438 | 0.000 | 0.312 | 0.062 |
| 2.4-3.3 | 0.000 | 0.294 | 0.294 | 0.000 | 0.294 | 0.118 |
| 3.3-4.2 | 0.059 | 0.176 | 0.176 | 0.059 | 0.294 | 0.235 |
| 4.2-5.1 | 0.056 | 0.111 | 0.278 | 0.000 | 0.389 | 0.167 |
| 5.1-6.0 | 0.333 | 0.167 | 0.167 | 0.056 | 0.222 | 0.056 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2098)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.375 | 0.375 | 0.125 | 0.125 | 0.000 |
| 1.5-2.4 | 0.062 | 0.125 | 0.500 | 0.188 | 0.062 | 0.062 |
| 2.4-3.3 | 0.059 | 0.176 | 0.471 | 0.000 | 0.176 | 0.118 |
| 3.3-4.2 | 0.059 | 0.235 | 0.353 | 0.000 | 0.294 | 0.059 |
| 4.2-5.1 | 0.000 | 0.000 | 0.333 | 0.056 | 0.611 | 0.000 |
| 5.1-6.0 | 0.000 | 0.111 | 0.389 | 0.167 | 0.278 | 0.056 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2044)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.4118, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5556, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.062 | 0.312 | 0.312 | 0.250 | 0.000 | 0.062 |
| 1.5-2.4 | 0.188 | 0.188 | 0.312 | 0.000 | 0.312 | 0.000 |
| 2.4-3.3 | 0.118 | 0.176 | 0.412 | 0.000 | 0.235 | 0.059 |
| 3.3-4.2 | 0.000 | 0.353 | 0.412 | 0.000 | 0.235 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.333 | 0.056 | 0.556 | 0.056 |
| 5.1-6.0 | 0.056 | 0.278 | 0.389 | 0.111 | 0.167 | 0.000 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1966)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0625, support=16
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.3529, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.062 | 0.188 | 0.125 | 0.062 | 0.250 | 0.312 |
| 1.5-2.4 | 0.125 | 0.188 | 0.562 | 0.000 | 0.062 | 0.062 |
| 2.4-3.3 | 0.118 | 0.176 | 0.353 | 0.059 | 0.118 | 0.176 |
| 3.3-4.2 | 0.118 | 0.176 | 0.353 | 0.000 | 0.235 | 0.118 |
| 4.2-5.1 | 0.000 | 0.056 | 0.500 | 0.000 | 0.278 | 0.167 |
| 5.1-6.0 | 0.222 | 0.056 | 0.056 | 0.167 | 0.222 | 0.278 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1964)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3125, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.2353, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.312 | 0.188 | 0.125 | 0.125 | 0.188 | 0.062 |
| 1.5-2.4 | 0.188 | 0.250 | 0.312 | 0.000 | 0.188 | 0.062 |
| 2.4-3.3 | 0.176 | 0.118 | 0.235 | 0.118 | 0.176 | 0.176 |
| 3.3-4.2 | 0.059 | 0.294 | 0.235 | 0.059 | 0.118 | 0.235 |
| 4.2-5.1 | 0.056 | 0.222 | 0.444 | 0.000 | 0.111 | 0.167 |
| 5.1-6.0 | 0.278 | 0.167 | 0.111 | 0.167 | 0.111 | 0.167 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1865)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.375 | 0.500 | 0.000 | 0.125 | 0.000 |
| 1.5-2.4 | 0.062 | 0.312 | 0.312 | 0.000 | 0.312 | 0.000 |
| 2.4-3.3 | 0.000 | 0.412 | 0.176 | 0.000 | 0.412 | 0.000 |
| 3.3-4.2 | 0.000 | 0.353 | 0.353 | 0.000 | 0.294 | 0.000 |
| 4.2-5.1 | 0.000 | 0.278 | 0.111 | 0.000 | 0.611 | 0.000 |
| 5.1-6.0 | 0.000 | 0.056 | 0.667 | 0.000 | 0.278 | 0.000 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1677)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2500, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.250 | 0.062 | 0.250 | 0.062 | 0.062 | 0.312 |
| 1.5-2.4 | 0.438 | 0.062 | 0.312 | 0.062 | 0.062 | 0.062 |
| 2.4-3.3 | 0.353 | 0.118 | 0.000 | 0.176 | 0.059 | 0.294 |
| 3.3-4.2 | 0.118 | 0.176 | 0.235 | 0.176 | 0.235 | 0.059 |
| 4.2-5.1 | 0.278 | 0.111 | 0.167 | 0.056 | 0.389 | 0.000 |
| 5.1-6.0 | 0.167 | 0.056 | 0.222 | 0.056 | 0.389 | 0.111 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.167 | 0.111 | 0.222 | 0.000 | 0.167 |
| 1.5-2.4 | 0.167 | 0.222 | 0.278 | 0.000 | 0.111 | 0.222 |
| 2.4-3.3 | 0.222 | 0.167 | 0.278 | 0.111 | 0.167 | 0.056 |
| 3.3-4.2 | 0.167 | 0.056 | 0.278 | 0.056 | 0.167 | 0.278 |
| 4.2-5.1 | 0.056 | 0.167 | 0.111 | 0.167 | 0.389 | 0.111 |
| 5.1-6.0 | 0.333 | 0.000 | 0.111 | 0.111 | 0.167 | 0.278 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.056 | 0.167 | 0.056 | 0.056 | 0.278 |
| 1.5-2.4 | 0.222 | 0.111 | 0.278 | 0.000 | 0.222 | 0.167 |
| 2.4-3.3 | 0.167 | 0.167 | 0.111 | 0.056 | 0.222 | 0.278 |
| 3.3-4.2 | 0.222 | 0.000 | 0.222 | 0.111 | 0.222 | 0.222 |
| 4.2-5.1 | 0.056 | 0.167 | 0.167 | 0.111 | 0.389 | 0.111 |
| 5.1-6.0 | 0.278 | 0.000 | 0.111 | 0.167 | 0.167 | 0.278 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.111 | 0.111 | 0.000 | 0.056 | 0.389 |
| 1.5-2.4 | 0.222 | 0.056 | 0.389 | 0.111 | 0.111 | 0.111 |
| 2.4-3.3 | 0.111 | 0.278 | 0.111 | 0.056 | 0.167 | 0.278 |
| 3.3-4.2 | 0.167 | 0.111 | 0.167 | 0.167 | 0.167 | 0.222 |
| 4.2-5.1 | 0.167 | 0.222 | 0.167 | 0.056 | 0.333 | 0.056 |
| 5.1-6.0 | 0.167 | 0.167 | 0.167 | 0.000 | 0.167 | 0.333 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.000 | 0.389 | 0.000 | 0.000 | 0.222 |
| 1.5-2.4 | 0.111 | 0.222 | 0.278 | 0.056 | 0.222 | 0.111 |
| 2.4-3.3 | 0.167 | 0.167 | 0.111 | 0.167 | 0.278 | 0.111 |
| 3.3-4.2 | 0.333 | 0.111 | 0.056 | 0.111 | 0.167 | 0.222 |
| 4.2-5.1 | 0.111 | 0.222 | 0.056 | 0.222 | 0.278 | 0.111 |
| 5.1-6.0 | 0.278 | 0.000 | 0.056 | 0.111 | 0.278 | 0.278 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.056 | 0.222 | 0.111 | 0.056 | 0.333 |
| 1.5-2.4 | 0.111 | 0.222 | 0.333 | 0.111 | 0.056 | 0.167 |
| 2.4-3.3 | 0.167 | 0.056 | 0.167 | 0.222 | 0.278 | 0.111 |
| 3.3-4.2 | 0.222 | 0.111 | 0.167 | 0.111 | 0.111 | 0.278 |
| 4.2-5.1 | 0.000 | 0.167 | 0.333 | 0.222 | 0.167 | 0.111 |
| 5.1-6.0 | 0.222 | 0.056 | 0.222 | 0.056 | 0.167 | 0.278 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.1917)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.056 | 0.222 | 0.167 | 0.056 | 0.222 |
| 1.5-2.4 | 0.111 | 0.222 | 0.222 | 0.000 | 0.278 | 0.167 |
| 2.4-3.3 | 0.222 | 0.111 | 0.056 | 0.111 | 0.278 | 0.222 |
| 3.3-4.2 | 0.278 | 0.000 | 0.167 | 0.111 | 0.167 | 0.278 |
| 4.2-5.1 | 0.000 | 0.222 | 0.222 | 0.222 | 0.167 | 0.167 |
| 5.1-6.0 | 0.278 | 0.000 | 0.000 | 0.111 | 0.333 | 0.278 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.1333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.111 | 0.056 | 0.278 | 0.056 | 0.278 |
| 1.5-2.4 | 0.222 | 0.111 | 0.222 | 0.056 | 0.278 | 0.111 |
| 2.4-3.3 | 0.222 | 0.167 | 0.000 | 0.222 | 0.167 | 0.222 |
| 3.3-4.2 | 0.111 | 0.222 | 0.167 | 0.056 | 0.222 | 0.222 |
| 4.2-5.1 | 0.111 | 0.167 | 0.167 | 0.167 | 0.167 | 0.222 |
| 5.1-6.0 | 0.167 | 0.222 | 0.111 | 0.111 | 0.167 | 0.222 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2460)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2642, support=53
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.3774, support=53
- `4.2-5.1`: recall=0.1373, support=51
- `5.1-6.0`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.264 | 0.151 | 0.170 | 0.226 | 0.075 | 0.113 |
| 1.5-2.4 | 0.259 | 0.185 | 0.074 | 0.278 | 0.074 | 0.130 |
| 2.4-3.3 | 0.039 | 0.137 | 0.216 | 0.314 | 0.157 | 0.137 |
| 3.3-4.2 | 0.075 | 0.038 | 0.132 | 0.377 | 0.226 | 0.151 |
| 4.2-5.1 | 0.020 | 0.039 | 0.196 | 0.333 | 0.137 | 0.275 |
| 5.1-6.0 | 0.077 | 0.096 | 0.135 | 0.308 | 0.096 | 0.288 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2339)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3774, support=53
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.2264, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.1346, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.377 | 0.151 | 0.189 | 0.170 | 0.094 | 0.019 |
| 1.5-2.4 | 0.278 | 0.259 | 0.130 | 0.148 | 0.148 | 0.037 |
| 2.4-3.3 | 0.255 | 0.157 | 0.196 | 0.216 | 0.098 | 0.078 |
| 3.3-4.2 | 0.151 | 0.208 | 0.170 | 0.226 | 0.189 | 0.057 |
| 4.2-5.1 | 0.098 | 0.118 | 0.137 | 0.314 | 0.196 | 0.137 |
| 5.1-6.0 | 0.173 | 0.173 | 0.154 | 0.231 | 0.135 | 0.135 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2334)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2642, support=53
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.3208, support=53
- `4.2-5.1`: recall=0.0588, support=51
- `5.1-6.0`: recall=0.3462, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.264 | 0.340 | 0.038 | 0.226 | 0.057 | 0.075 |
| 1.5-2.4 | 0.296 | 0.241 | 0.111 | 0.222 | 0.037 | 0.093 |
| 2.4-3.3 | 0.059 | 0.294 | 0.098 | 0.275 | 0.098 | 0.176 |
| 3.3-4.2 | 0.113 | 0.208 | 0.019 | 0.321 | 0.075 | 0.264 |
| 4.2-5.1 | 0.039 | 0.196 | 0.098 | 0.314 | 0.059 | 0.294 |
| 5.1-6.0 | 0.096 | 0.115 | 0.038 | 0.308 | 0.096 | 0.346 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2254)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3962, support=53
- `1.5-2.4`: recall=0.0370, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.1509, support=53
- `4.2-5.1`: recall=0.2549, support=51
- `5.1-6.0`: recall=0.3654, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.396 | 0.132 | 0.094 | 0.113 | 0.132 | 0.132 |
| 1.5-2.4 | 0.389 | 0.037 | 0.037 | 0.167 | 0.222 | 0.148 |
| 2.4-3.3 | 0.137 | 0.078 | 0.078 | 0.255 | 0.235 | 0.216 |
| 3.3-4.2 | 0.151 | 0.038 | 0.094 | 0.151 | 0.170 | 0.396 |
| 4.2-5.1 | 0.078 | 0.039 | 0.039 | 0.235 | 0.255 | 0.353 |
| 5.1-6.0 | 0.135 | 0.019 | 0.019 | 0.154 | 0.308 | 0.365 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2185)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3019, support=53
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.1373, support=51
- `3.3-4.2`: recall=0.3396, support=53
- `4.2-5.1`: recall=0.0784, support=51
- `5.1-6.0`: recall=0.3462, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.302 | 0.226 | 0.132 | 0.132 | 0.057 | 0.151 |
| 1.5-2.4 | 0.333 | 0.148 | 0.056 | 0.259 | 0.074 | 0.130 |
| 2.4-3.3 | 0.118 | 0.118 | 0.137 | 0.255 | 0.137 | 0.235 |
| 3.3-4.2 | 0.075 | 0.132 | 0.038 | 0.340 | 0.075 | 0.340 |
| 4.2-5.1 | 0.059 | 0.059 | 0.098 | 0.373 | 0.078 | 0.333 |
| 5.1-6.0 | 0.096 | 0.058 | 0.077 | 0.327 | 0.096 | 0.346 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1809)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0755, support=53
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.7358, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1731, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.075 | 0.057 | 0.075 | 0.660 | 0.057 | 0.075 |
| 1.5-2.4 | 0.074 | 0.000 | 0.056 | 0.759 | 0.056 | 0.056 |
| 2.4-3.3 | 0.078 | 0.039 | 0.020 | 0.745 | 0.059 | 0.059 |
| 3.3-4.2 | 0.057 | 0.057 | 0.038 | 0.736 | 0.038 | 0.075 |
| 4.2-5.1 | 0.059 | 0.000 | 0.000 | 0.784 | 0.039 | 0.118 |
| 5.1-6.0 | 0.038 | 0.019 | 0.038 | 0.692 | 0.038 | 0.173 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1807)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1887, support=53
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.2353, support=51
- `5.1-6.0`: recall=0.0769, support=52

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.189 | 0.264 | 0.170 | 0.132 | 0.170 | 0.075 |
| 1.5-2.4 | 0.259 | 0.259 | 0.167 | 0.037 | 0.167 | 0.111 |
| 2.4-3.3 | 0.275 | 0.157 | 0.176 | 0.098 | 0.157 | 0.137 |
| 3.3-4.2 | 0.094 | 0.189 | 0.208 | 0.170 | 0.226 | 0.113 |
| 4.2-5.1 | 0.137 | 0.235 | 0.235 | 0.098 | 0.235 | 0.059 |
| 5.1-6.0 | 0.096 | 0.212 | 0.231 | 0.115 | 0.269 | 0.077 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2816)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.8125, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0000, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.812 | 0.125 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.438 | 0.312 | 0.000 | 0.188 | 0.000 | 0.062 |
| 2.4-3.3 | 0.471 | 0.118 | 0.000 | 0.059 | 0.000 | 0.353 |
| 3.3-4.2 | 0.294 | 0.294 | 0.059 | 0.059 | 0.000 | 0.294 |
| 4.2-5.1 | 0.333 | 0.111 | 0.000 | 0.333 | 0.000 | 0.222 |
| 5.1-6.0 | 0.056 | 0.222 | 0.000 | 0.222 | 0.000 | 0.500 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2553)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.8750, support=16
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.875 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.562 | 0.250 | 0.062 | 0.000 | 0.000 | 0.125 |
| 2.4-3.3 | 0.765 | 0.000 | 0.059 | 0.000 | 0.000 | 0.176 |
| 3.3-4.2 | 0.471 | 0.294 | 0.059 | 0.000 | 0.000 | 0.176 |
| 4.2-5.1 | 0.611 | 0.111 | 0.000 | 0.000 | 0.000 | 0.278 |
| 5.1-6.0 | 0.111 | 0.389 | 0.000 | 0.167 | 0.000 | 0.333 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2412)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1875, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.2353, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.188 | 0.375 | 0.312 | 0.125 | 0.000 | 0.000 |
| 1.5-2.4 | 0.125 | 0.312 | 0.250 | 0.188 | 0.000 | 0.125 |
| 2.4-3.3 | 0.000 | 0.294 | 0.294 | 0.176 | 0.118 | 0.118 |
| 3.3-4.2 | 0.059 | 0.235 | 0.176 | 0.235 | 0.059 | 0.235 |
| 4.2-5.1 | 0.111 | 0.111 | 0.333 | 0.111 | 0.222 | 0.111 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.444 | 0.278 | 0.167 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2350)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5625, support=16
- `1.5-2.4`: recall=0.5000, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.562 | 0.125 | 0.250 | 0.000 | 0.062 | 0.000 |
| 1.5-2.4 | 0.188 | 0.500 | 0.188 | 0.125 | 0.000 | 0.000 |
| 2.4-3.3 | 0.059 | 0.294 | 0.176 | 0.294 | 0.059 | 0.118 |
| 3.3-4.2 | 0.294 | 0.235 | 0.235 | 0.059 | 0.118 | 0.059 |
| 4.2-5.1 | 0.333 | 0.167 | 0.222 | 0.222 | 0.056 | 0.000 |
| 5.1-6.0 | 0.056 | 0.056 | 0.222 | 0.278 | 0.333 | 0.056 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2298)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.750 | 0.188 | 0.000 | 0.062 | 0.000 | 0.000 |
| 1.5-2.4 | 0.500 | 0.312 | 0.125 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.353 | 0.294 | 0.059 | 0.176 | 0.000 | 0.118 |
| 3.3-4.2 | 0.471 | 0.294 | 0.000 | 0.118 | 0.059 | 0.059 |
| 4.2-5.1 | 0.278 | 0.167 | 0.056 | 0.389 | 0.000 | 0.111 |
| 5.1-6.0 | 0.111 | 0.111 | 0.000 | 0.667 | 0.000 | 0.111 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2221)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.7500, support=16
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.3529, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.750 | 0.000 | 0.188 | 0.062 | 0.000 | 0.000 |
| 1.5-2.4 | 0.625 | 0.062 | 0.000 | 0.312 | 0.000 | 0.000 |
| 2.4-3.3 | 0.647 | 0.000 | 0.176 | 0.176 | 0.000 | 0.000 |
| 3.3-4.2 | 0.588 | 0.059 | 0.000 | 0.353 | 0.000 | 0.000 |
| 4.2-5.1 | 0.389 | 0.056 | 0.056 | 0.500 | 0.000 | 0.000 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.833 | 0.000 | 0.000 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1733)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3750, support=16
- `1.5-2.4`: recall=0.6250, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.375 | 0.562 | 0.062 | 0.000 | 0.000 | 0.000 |
| 1.5-2.4 | 0.188 | 0.625 | 0.125 | 0.062 | 0.000 | 0.000 |
| 2.4-3.3 | 0.176 | 0.765 | 0.059 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.059 | 0.588 | 0.353 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.222 | 0.333 | 0.222 | 0.222 | 0.000 | 0.000 |
| 5.1-6.0 | 0.056 | 0.500 | 0.389 | 0.056 | 0.000 | 0.000 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.4167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6667, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.3333, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.7778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.667 | 0.167 | 0.111 | 0.000 | 0.056 | 0.000 |
| 1.5-2.4 | 0.222 | 0.111 | 0.167 | 0.167 | 0.278 | 0.056 |
| 2.4-3.3 | 0.056 | 0.222 | 0.222 | 0.222 | 0.278 | 0.000 |
| 3.3-4.2 | 0.111 | 0.167 | 0.056 | 0.333 | 0.222 | 0.111 |
| 4.2-5.1 | 0.111 | 0.111 | 0.111 | 0.167 | 0.333 | 0.167 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.000 | 0.056 | 0.778 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.4000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.7222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.722 | 0.111 | 0.111 | 0.000 | 0.000 | 0.056 |
| 1.5-2.4 | 0.222 | 0.222 | 0.222 | 0.111 | 0.111 | 0.111 |
| 2.4-3.3 | 0.056 | 0.278 | 0.222 | 0.167 | 0.222 | 0.056 |
| 3.3-4.2 | 0.111 | 0.222 | 0.222 | 0.222 | 0.167 | 0.056 |
| 4.2-5.1 | 0.111 | 0.056 | 0.111 | 0.222 | 0.333 | 0.167 |
| 5.1-6.0 | 0.000 | 0.111 | 0.000 | 0.056 | 0.111 | 0.722 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.4444, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.556 | 0.222 | 0.056 | 0.056 | 0.111 | 0.000 |
| 1.5-2.4 | 0.222 | 0.222 | 0.056 | 0.111 | 0.333 | 0.056 |
| 2.4-3.3 | 0.056 | 0.333 | 0.222 | 0.167 | 0.222 | 0.000 |
| 3.3-4.2 | 0.222 | 0.111 | 0.111 | 0.111 | 0.333 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.056 | 0.111 | 0.444 | 0.222 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.000 | 0.167 | 0.722 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3583)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.056 | 0.111 | 0.111 | 0.167 | 0.056 |
| 1.5-2.4 | 0.167 | 0.222 | 0.278 | 0.111 | 0.111 | 0.111 |
| 2.4-3.3 | 0.167 | 0.111 | 0.389 | 0.167 | 0.111 | 0.056 |
| 3.3-4.2 | 0.222 | 0.167 | 0.111 | 0.167 | 0.222 | 0.111 |
| 4.2-5.1 | 0.056 | 0.111 | 0.278 | 0.056 | 0.278 | 0.222 |
| 5.1-6.0 | 0.111 | 0.111 | 0.111 | 0.000 | 0.056 | 0.611 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.556 | 0.111 | 0.222 | 0.056 | 0.056 | 0.000 |
| 1.5-2.4 | 0.167 | 0.167 | 0.111 | 0.167 | 0.278 | 0.111 |
| 2.4-3.3 | 0.056 | 0.222 | 0.389 | 0.222 | 0.056 | 0.056 |
| 3.3-4.2 | 0.222 | 0.222 | 0.111 | 0.056 | 0.278 | 0.111 |
| 4.2-5.1 | 0.111 | 0.056 | 0.167 | 0.167 | 0.222 | 0.278 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.000 | 0.111 | 0.722 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.611 | 0.056 | 0.167 | 0.111 | 0.056 | 0.000 |
| 1.5-2.4 | 0.222 | 0.167 | 0.111 | 0.167 | 0.222 | 0.111 |
| 2.4-3.3 | 0.111 | 0.222 | 0.389 | 0.167 | 0.056 | 0.056 |
| 3.3-4.2 | 0.222 | 0.167 | 0.056 | 0.111 | 0.167 | 0.278 |
| 4.2-5.1 | 0.056 | 0.222 | 0.056 | 0.222 | 0.111 | 0.333 |
| 5.1-6.0 | 0.000 | 0.056 | 0.056 | 0.000 | 0.167 | 0.722 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2583)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.056 | 0.111 | 0.056 | 0.278 | 0.056 |
| 1.5-2.4 | 0.000 | 0.222 | 0.222 | 0.167 | 0.056 | 0.333 |
| 2.4-3.3 | 0.111 | 0.167 | 0.278 | 0.111 | 0.167 | 0.167 |
| 3.3-4.2 | 0.222 | 0.167 | 0.056 | 0.111 | 0.222 | 0.222 |
| 4.2-5.1 | 0.111 | 0.000 | 0.167 | 0.222 | 0.222 | 0.278 |
| 5.1-6.0 | 0.000 | 0.222 | 0.167 | 0.056 | 0.222 | 0.333 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2557)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4259, support=54
- `1.5-2.4`: recall=0.3704, support=54
- `2.4-3.3`: recall=0.1852, support=54
- `3.3-4.2`: recall=0.1852, support=54
- `4.2-5.1`: recall=0.1698, support=53
- `5.1-6.0`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.426 | 0.222 | 0.056 | 0.130 | 0.056 | 0.111 |
| 1.5-2.4 | 0.167 | 0.370 | 0.093 | 0.111 | 0.148 | 0.111 |
| 2.4-3.3 | 0.093 | 0.333 | 0.185 | 0.204 | 0.093 | 0.093 |
| 3.3-4.2 | 0.074 | 0.241 | 0.111 | 0.185 | 0.130 | 0.259 |
| 4.2-5.1 | 0.038 | 0.264 | 0.094 | 0.151 | 0.170 | 0.283 |
| 5.1-6.0 | 0.038 | 0.189 | 0.113 | 0.132 | 0.264 | 0.264 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2372)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=54
- `1.5-2.4`: recall=0.1667, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.5660, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.278 | 0.056 | 0.093 | 0.074 | 0.167 |
| 1.5-2.4 | 0.259 | 0.167 | 0.000 | 0.185 | 0.148 | 0.241 |
| 2.4-3.3 | 0.111 | 0.130 | 0.037 | 0.259 | 0.130 | 0.333 |
| 3.3-4.2 | 0.130 | 0.093 | 0.056 | 0.222 | 0.111 | 0.389 |
| 4.2-5.1 | 0.075 | 0.094 | 0.057 | 0.321 | 0.094 | 0.358 |
| 5.1-6.0 | 0.094 | 0.057 | 0.019 | 0.151 | 0.113 | 0.566 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2136)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4815, support=54
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.2222, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.481 | 0.241 | 0.056 | 0.093 | 0.037 | 0.093 |
| 1.5-2.4 | 0.315 | 0.130 | 0.130 | 0.204 | 0.093 | 0.130 |
| 2.4-3.3 | 0.204 | 0.185 | 0.222 | 0.185 | 0.074 | 0.130 |
| 3.3-4.2 | 0.241 | 0.185 | 0.130 | 0.222 | 0.148 | 0.074 |
| 4.2-5.1 | 0.208 | 0.208 | 0.075 | 0.264 | 0.094 | 0.151 |
| 5.1-6.0 | 0.226 | 0.226 | 0.094 | 0.170 | 0.132 | 0.151 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2069)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.1296, support=54
- `1.5-2.4`: recall=0.3333, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2593, support=54
- `4.2-5.1`: recall=0.2075, support=53
- `5.1-6.0`: recall=0.2830, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.130 | 0.444 | 0.056 | 0.111 | 0.093 | 0.167 |
| 1.5-2.4 | 0.130 | 0.333 | 0.037 | 0.204 | 0.148 | 0.148 |
| 2.4-3.3 | 0.019 | 0.296 | 0.037 | 0.222 | 0.167 | 0.259 |
| 3.3-4.2 | 0.037 | 0.241 | 0.056 | 0.259 | 0.167 | 0.241 |
| 4.2-5.1 | 0.057 | 0.132 | 0.075 | 0.302 | 0.208 | 0.226 |
| 5.1-6.0 | 0.075 | 0.208 | 0.038 | 0.283 | 0.113 | 0.283 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2050)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3704, support=54
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.4340, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.370 | 0.333 | 0.019 | 0.093 | 0.019 | 0.167 |
| 1.5-2.4 | 0.352 | 0.259 | 0.000 | 0.074 | 0.019 | 0.296 |
| 2.4-3.3 | 0.111 | 0.259 | 0.074 | 0.074 | 0.019 | 0.463 |
| 3.3-4.2 | 0.148 | 0.185 | 0.037 | 0.093 | 0.056 | 0.481 |
| 4.2-5.1 | 0.113 | 0.170 | 0.075 | 0.075 | 0.038 | 0.528 |
| 5.1-6.0 | 0.170 | 0.208 | 0.057 | 0.057 | 0.075 | 0.434 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1617)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0556, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.9057, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.056 | 0.000 | 0.000 | 0.019 | 0.000 | 0.926 |
| 1.5-2.4 | 0.074 | 0.000 | 0.000 | 0.037 | 0.000 | 0.889 |
| 2.4-3.3 | 0.148 | 0.000 | 0.000 | 0.019 | 0.000 | 0.833 |
| 3.3-4.2 | 0.037 | 0.000 | 0.000 | 0.000 | 0.019 | 0.944 |
| 4.2-5.1 | 0.075 | 0.000 | 0.019 | 0.000 | 0.000 | 0.906 |
| 5.1-6.0 | 0.075 | 0.000 | 0.019 | 0.000 | 0.000 | 0.906 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1507)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0741, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.3889, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0189, support=53
- `5.1-6.0`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.074 | 0.056 | 0.463 | 0.000 | 0.037 | 0.370 |
| 1.5-2.4 | 0.037 | 0.019 | 0.463 | 0.019 | 0.019 | 0.444 |
| 2.4-3.3 | 0.093 | 0.000 | 0.389 | 0.019 | 0.074 | 0.426 |
| 3.3-4.2 | 0.019 | 0.019 | 0.630 | 0.000 | 0.000 | 0.333 |
| 4.2-5.1 | 0.038 | 0.000 | 0.509 | 0.057 | 0.019 | 0.377 |
| 5.1-6.0 | 0.019 | 0.000 | 0.585 | 0.000 | 0.019 | 0.377 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2419)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.556 | 0.056 | 0.222 | 0.056 | 0.000 | 0.111 |
| 1.5-2.4 | 0.167 | 0.167 | 0.389 | 0.056 | 0.111 | 0.111 |
| 2.4-3.3 | 0.167 | 0.278 | 0.278 | 0.000 | 0.111 | 0.167 |
| 3.3-4.2 | 0.176 | 0.353 | 0.059 | 0.059 | 0.118 | 0.235 |
| 4.2-5.1 | 0.167 | 0.111 | 0.056 | 0.111 | 0.222 | 0.333 |
| 5.1-6.0 | 0.167 | 0.111 | 0.056 | 0.111 | 0.389 | 0.167 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2222)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2222, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.222 | 0.167 | 0.000 | 0.000 | 0.111 | 0.500 |
| 1.5-2.4 | 0.278 | 0.222 | 0.000 | 0.000 | 0.056 | 0.444 |
| 2.4-3.3 | 0.056 | 0.333 | 0.056 | 0.056 | 0.000 | 0.500 |
| 3.3-4.2 | 0.000 | 0.235 | 0.118 | 0.118 | 0.059 | 0.471 |
| 4.2-5.1 | 0.000 | 0.167 | 0.056 | 0.000 | 0.278 | 0.500 |
| 5.1-6.0 | 0.000 | 0.167 | 0.056 | 0.278 | 0.056 | 0.444 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2130)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.7222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.111 | 0.000 | 0.000 | 0.000 | 0.444 |
| 1.5-2.4 | 0.444 | 0.056 | 0.000 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.222 | 0.167 | 0.000 | 0.000 | 0.056 | 0.556 |
| 3.3-4.2 | 0.176 | 0.059 | 0.000 | 0.000 | 0.059 | 0.706 |
| 4.2-5.1 | 0.111 | 0.000 | 0.000 | 0.056 | 0.056 | 0.778 |
| 5.1-6.0 | 0.056 | 0.056 | 0.000 | 0.167 | 0.000 | 0.722 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2037)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.111 | 0.000 | 0.278 | 0.222 | 0.000 |
| 1.5-2.4 | 0.167 | 0.222 | 0.056 | 0.333 | 0.167 | 0.056 |
| 2.4-3.3 | 0.167 | 0.056 | 0.056 | 0.444 | 0.278 | 0.000 |
| 3.3-4.2 | 0.353 | 0.176 | 0.000 | 0.176 | 0.118 | 0.176 |
| 4.2-5.1 | 0.167 | 0.056 | 0.000 | 0.500 | 0.278 | 0.000 |
| 5.1-6.0 | 0.056 | 0.222 | 0.111 | 0.222 | 0.278 | 0.111 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2037)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.2353, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.111 | 0.056 | 0.056 | 0.056 | 0.389 |
| 1.5-2.4 | 0.278 | 0.167 | 0.000 | 0.167 | 0.056 | 0.333 |
| 2.4-3.3 | 0.167 | 0.111 | 0.000 | 0.111 | 0.222 | 0.389 |
| 3.3-4.2 | 0.059 | 0.176 | 0.059 | 0.235 | 0.000 | 0.471 |
| 4.2-5.1 | 0.056 | 0.000 | 0.000 | 0.500 | 0.056 | 0.389 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.500 | 0.056 | 0.444 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1574)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |
| 1.5-2.4 | 0.056 | 0.444 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |
| 3.3-4.2 | 0.000 | 0.529 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.167 | 0.056 | 0.111 | 0.111 | 0.111 |
| 1.5-2.4 | 0.167 | 0.278 | 0.167 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.222 | 0.222 | 0.278 | 0.111 | 0.056 |
| 3.3-4.2 | 0.056 | 0.167 | 0.222 | 0.222 | 0.111 | 0.222 |
| 4.2-5.1 | 0.176 | 0.118 | 0.176 | 0.118 | 0.176 | 0.235 |
| 5.1-6.0 | 0.056 | 0.056 | 0.000 | 0.167 | 0.278 | 0.444 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2833)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.3889, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.3889, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.222 | 0.000 | 0.222 | 0.222 | 0.056 |
| 1.5-2.4 | 0.222 | 0.278 | 0.111 | 0.056 | 0.167 | 0.167 |
| 2.4-3.3 | 0.167 | 0.167 | 0.000 | 0.167 | 0.278 | 0.222 |
| 3.3-4.2 | 0.000 | 0.167 | 0.111 | 0.389 | 0.222 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.176 | 0.176 | 0.353 | 0.235 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.167 | 0.278 | 0.389 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.111 | 0.000 | 0.167 | 0.056 | 0.222 |
| 1.5-2.4 | 0.111 | 0.278 | 0.222 | 0.111 | 0.111 | 0.167 |
| 2.4-3.3 | 0.167 | 0.222 | 0.111 | 0.278 | 0.167 | 0.056 |
| 3.3-4.2 | 0.111 | 0.111 | 0.222 | 0.222 | 0.167 | 0.167 |
| 4.2-5.1 | 0.118 | 0.000 | 0.118 | 0.059 | 0.176 | 0.529 |
| 5.1-6.0 | 0.111 | 0.056 | 0.000 | 0.056 | 0.333 | 0.444 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.611 | 0.167 | 0.000 | 0.111 | 0.000 | 0.111 |
| 1.5-2.4 | 0.444 | 0.167 | 0.222 | 0.056 | 0.000 | 0.111 |
| 2.4-3.3 | 0.056 | 0.333 | 0.111 | 0.278 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.167 | 0.278 | 0.111 | 0.167 | 0.222 |
| 4.2-5.1 | 0.059 | 0.000 | 0.235 | 0.176 | 0.118 | 0.412 |
| 5.1-6.0 | 0.111 | 0.000 | 0.056 | 0.111 | 0.222 | 0.500 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2583)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.167 | 0.111 | 0.111 | 0.056 | 0.111 |
| 1.5-2.4 | 0.444 | 0.222 | 0.056 | 0.111 | 0.111 | 0.056 |
| 2.4-3.3 | 0.000 | 0.222 | 0.222 | 0.222 | 0.333 | 0.000 |
| 3.3-4.2 | 0.056 | 0.111 | 0.167 | 0.111 | 0.389 | 0.167 |
| 4.2-5.1 | 0.000 | 0.000 | 0.235 | 0.118 | 0.294 | 0.353 |
| 5.1-6.0 | 0.056 | 0.000 | 0.167 | 0.278 | 0.278 | 0.222 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.333 | 0.000 | 0.222 | 0.056 | 0.056 |
| 1.5-2.4 | 0.167 | 0.389 | 0.111 | 0.167 | 0.167 | 0.000 |
| 2.4-3.3 | 0.167 | 0.111 | 0.000 | 0.389 | 0.222 | 0.111 |
| 3.3-4.2 | 0.111 | 0.222 | 0.111 | 0.167 | 0.278 | 0.111 |
| 4.2-5.1 | 0.059 | 0.059 | 0.176 | 0.176 | 0.235 | 0.294 |
| 5.1-6.0 | 0.056 | 0.111 | 0.000 | 0.167 | 0.333 | 0.333 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.4118, support=17
- `5.1-6.0`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.111 | 0.222 | 0.111 | 0.278 | 0.000 |
| 1.5-2.4 | 0.222 | 0.111 | 0.278 | 0.167 | 0.167 | 0.056 |
| 2.4-3.3 | 0.111 | 0.167 | 0.167 | 0.222 | 0.278 | 0.056 |
| 3.3-4.2 | 0.167 | 0.056 | 0.389 | 0.000 | 0.222 | 0.167 |
| 4.2-5.1 | 0.176 | 0.000 | 0.118 | 0.000 | 0.412 | 0.294 |
| 5.1-6.0 | 0.056 | 0.056 | 0.167 | 0.111 | 0.389 | 0.222 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1998)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4815, support=54
- `1.5-2.4`: recall=0.0926, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.2037, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.3208, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.481 | 0.111 | 0.000 | 0.167 | 0.019 | 0.222 |
| 1.5-2.4 | 0.370 | 0.093 | 0.037 | 0.148 | 0.148 | 0.204 |
| 2.4-3.3 | 0.167 | 0.185 | 0.074 | 0.130 | 0.111 | 0.333 |
| 3.3-4.2 | 0.093 | 0.167 | 0.019 | 0.204 | 0.111 | 0.407 |
| 4.2-5.1 | 0.132 | 0.132 | 0.019 | 0.208 | 0.057 | 0.453 |
| 5.1-6.0 | 0.170 | 0.113 | 0.094 | 0.264 | 0.038 | 0.321 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1932)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=54
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2593, support=54
- `4.2-5.1`: recall=0.1698, support=53
- `5.1-6.0`: recall=0.3396, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.093 | 0.074 | 0.241 | 0.093 | 0.167 |
| 1.5-2.4 | 0.167 | 0.130 | 0.019 | 0.204 | 0.130 | 0.352 |
| 2.4-3.3 | 0.074 | 0.185 | 0.037 | 0.185 | 0.185 | 0.333 |
| 3.3-4.2 | 0.093 | 0.074 | 0.037 | 0.259 | 0.148 | 0.389 |
| 4.2-5.1 | 0.057 | 0.132 | 0.038 | 0.226 | 0.170 | 0.377 |
| 5.1-6.0 | 0.075 | 0.057 | 0.019 | 0.264 | 0.245 | 0.340 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1882)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2963, support=54
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.3148, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.2830, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.296 | 0.130 | 0.019 | 0.093 | 0.148 | 0.315 |
| 1.5-2.4 | 0.333 | 0.056 | 0.056 | 0.167 | 0.185 | 0.204 |
| 2.4-3.3 | 0.167 | 0.148 | 0.093 | 0.222 | 0.093 | 0.278 |
| 3.3-4.2 | 0.111 | 0.167 | 0.037 | 0.315 | 0.148 | 0.222 |
| 4.2-5.1 | 0.094 | 0.132 | 0.057 | 0.245 | 0.075 | 0.396 |
| 5.1-6.0 | 0.151 | 0.226 | 0.019 | 0.226 | 0.094 | 0.283 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1769)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2593, support=54
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.0556, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.1887, support=53
- `5.1-6.0`: recall=0.2075, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.259 | 0.259 | 0.111 | 0.167 | 0.148 | 0.056 |
| 1.5-2.4 | 0.148 | 0.185 | 0.130 | 0.222 | 0.222 | 0.093 |
| 2.4-3.3 | 0.167 | 0.259 | 0.056 | 0.185 | 0.204 | 0.130 |
| 3.3-4.2 | 0.204 | 0.130 | 0.093 | 0.222 | 0.204 | 0.148 |
| 4.2-5.1 | 0.094 | 0.113 | 0.151 | 0.189 | 0.189 | 0.264 |
| 5.1-6.0 | 0.170 | 0.094 | 0.132 | 0.189 | 0.208 | 0.208 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1675)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3148, support=54
- `1.5-2.4`: recall=0.0556, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.3962, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.315 | 0.019 | 0.000 | 0.259 | 0.074 | 0.333 |
| 1.5-2.4 | 0.204 | 0.056 | 0.000 | 0.241 | 0.167 | 0.333 |
| 2.4-3.3 | 0.148 | 0.037 | 0.000 | 0.204 | 0.185 | 0.426 |
| 3.3-4.2 | 0.148 | 0.000 | 0.000 | 0.222 | 0.074 | 0.556 |
| 4.2-5.1 | 0.132 | 0.019 | 0.000 | 0.264 | 0.057 | 0.528 |
| 5.1-6.0 | 0.132 | 0.075 | 0.000 | 0.340 | 0.057 | 0.396 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1617)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0556, support=54
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.9057, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.056 | 0.000 | 0.000 | 0.019 | 0.000 | 0.926 |
| 1.5-2.4 | 0.074 | 0.000 | 0.000 | 0.037 | 0.000 | 0.889 |
| 2.4-3.3 | 0.148 | 0.000 | 0.000 | 0.019 | 0.000 | 0.833 |
| 3.3-4.2 | 0.037 | 0.000 | 0.000 | 0.000 | 0.019 | 0.944 |
| 4.2-5.1 | 0.075 | 0.000 | 0.019 | 0.000 | 0.000 | 0.906 |
| 5.1-6.0 | 0.075 | 0.000 | 0.019 | 0.000 | 0.000 | 0.906 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1576)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/group_holdout/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0556, support=54
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.4444, support=54
- `3.3-4.2`: recall=0.0185, support=54
- `4.2-5.1`: recall=0.0189, support=53
- `5.1-6.0`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.056 | 0.056 | 0.481 | 0.000 | 0.056 | 0.352 |
| 1.5-2.4 | 0.037 | 0.019 | 0.481 | 0.019 | 0.037 | 0.407 |
| 2.4-3.3 | 0.093 | 0.019 | 0.444 | 0.019 | 0.056 | 0.370 |
| 3.3-4.2 | 0.019 | 0.019 | 0.611 | 0.019 | 0.000 | 0.333 |
| 4.2-5.1 | 0.038 | 0.000 | 0.528 | 0.057 | 0.019 | 0.358 |
| 5.1-6.0 | 0.019 | 0.000 | 0.585 | 0.000 | 0.019 | 0.377 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2407)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.4444, support=18
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.444 | 0.278 | 0.056 | 0.000 | 0.056 | 0.167 |
| 1.5-2.4 | 0.222 | 0.278 | 0.111 | 0.111 | 0.056 | 0.222 |
| 2.4-3.3 | 0.222 | 0.111 | 0.222 | 0.111 | 0.111 | 0.222 |
| 3.3-4.2 | 0.118 | 0.059 | 0.235 | 0.059 | 0.176 | 0.353 |
| 4.2-5.1 | 0.056 | 0.000 | 0.278 | 0.111 | 0.278 | 0.278 |
| 5.1-6.0 | 0.056 | 0.000 | 0.333 | 0.222 | 0.222 | 0.167 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2315)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.6111, support=18
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.611 | 0.000 | 0.000 | 0.000 | 0.056 | 0.333 |
| 1.5-2.4 | 0.500 | 0.056 | 0.056 | 0.000 | 0.000 | 0.389 |
| 2.4-3.3 | 0.278 | 0.056 | 0.222 | 0.056 | 0.000 | 0.389 |
| 3.3-4.2 | 0.118 | 0.059 | 0.353 | 0.000 | 0.000 | 0.471 |
| 4.2-5.1 | 0.056 | 0.000 | 0.500 | 0.000 | 0.000 | 0.444 |
| 5.1-6.0 | 0.000 | 0.000 | 0.444 | 0.056 | 0.000 | 0.500 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2130)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.5556, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.000 | 0.000 | 0.000 | 0.056 | 0.444 |
| 1.5-2.4 | 0.500 | 0.000 | 0.056 | 0.000 | 0.000 | 0.444 |
| 2.4-3.3 | 0.278 | 0.056 | 0.111 | 0.000 | 0.056 | 0.500 |
| 3.3-4.2 | 0.294 | 0.000 | 0.059 | 0.000 | 0.059 | 0.588 |
| 4.2-5.1 | 0.000 | 0.000 | 0.333 | 0.000 | 0.111 | 0.556 |
| 5.1-6.0 | 0.056 | 0.000 | 0.333 | 0.000 | 0.056 | 0.556 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2130)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5556, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.556 | 0.222 | 0.056 | 0.000 | 0.056 | 0.111 |
| 1.5-2.4 | 0.389 | 0.222 | 0.056 | 0.056 | 0.056 | 0.222 |
| 2.4-3.3 | 0.222 | 0.333 | 0.167 | 0.056 | 0.000 | 0.222 |
| 3.3-4.2 | 0.176 | 0.176 | 0.059 | 0.059 | 0.000 | 0.529 |
| 4.2-5.1 | 0.222 | 0.000 | 0.222 | 0.222 | 0.000 | 0.333 |
| 5.1-6.0 | 0.167 | 0.222 | 0.222 | 0.111 | 0.000 | 0.278 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2037)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.5000, support=18
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.500 | 0.167 | 0.000 | 0.000 | 0.000 | 0.333 |
| 1.5-2.4 | 0.556 | 0.167 | 0.000 | 0.000 | 0.000 | 0.278 |
| 2.4-3.3 | 0.500 | 0.000 | 0.000 | 0.111 | 0.000 | 0.389 |
| 3.3-4.2 | 0.353 | 0.000 | 0.059 | 0.118 | 0.000 | 0.471 |
| 4.2-5.1 | 0.222 | 0.056 | 0.111 | 0.222 | 0.000 | 0.389 |
| 5.1-6.0 | 0.111 | 0.000 | 0.278 | 0.167 | 0.000 | 0.444 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1574)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/loso/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.0000, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |
| 1.5-2.4 | 0.056 | 0.444 | 0.000 | 0.000 | 0.500 | 0.000 |
| 2.4-3.3 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |
| 3.3-4.2 | 0.000 | 0.529 | 0.000 | 0.000 | 0.471 | 0.000 |
| 4.2-5.1 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |
| 5.1-6.0 | 0.000 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3917)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/svm_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.4706, support=17
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.333 | 0.167 | 0.111 | 0.111 | 0.000 |
| 1.5-2.4 | 0.222 | 0.444 | 0.111 | 0.111 | 0.111 | 0.000 |
| 2.4-3.3 | 0.167 | 0.222 | 0.278 | 0.111 | 0.222 | 0.000 |
| 3.3-4.2 | 0.111 | 0.222 | 0.222 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.235 | 0.118 | 0.059 | 0.000 | 0.471 | 0.118 |
| 5.1-6.0 | 0.056 | 0.167 | 0.000 | 0.111 | 0.056 | 0.611 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.111 | 0.333 | 0.000 | 0.111 | 0.056 |
| 1.5-2.4 | 0.167 | 0.389 | 0.222 | 0.111 | 0.056 | 0.056 |
| 2.4-3.3 | 0.111 | 0.111 | 0.389 | 0.167 | 0.167 | 0.056 |
| 3.3-4.2 | 0.111 | 0.167 | 0.000 | 0.278 | 0.278 | 0.167 |
| 4.2-5.1 | 0.059 | 0.176 | 0.176 | 0.118 | 0.235 | 0.235 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.278 | 0.111 | 0.444 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/rf_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.6111, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.278 | 0.111 | 0.056 | 0.167 | 0.056 |
| 1.5-2.4 | 0.389 | 0.222 | 0.056 | 0.222 | 0.000 | 0.111 |
| 2.4-3.3 | 0.222 | 0.000 | 0.333 | 0.222 | 0.222 | 0.000 |
| 3.3-4.2 | 0.056 | 0.056 | 0.222 | 0.222 | 0.167 | 0.278 |
| 4.2-5.1 | 0.118 | 0.000 | 0.059 | 0.176 | 0.353 | 0.294 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.167 | 0.167 | 0.611 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/knn_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.4118, support=17
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.167 | 0.167 | 0.111 | 0.167 | 0.111 |
| 1.5-2.4 | 0.167 | 0.222 | 0.056 | 0.278 | 0.167 | 0.111 |
| 2.4-3.3 | 0.222 | 0.056 | 0.222 | 0.167 | 0.278 | 0.056 |
| 3.3-4.2 | 0.000 | 0.056 | 0.222 | 0.278 | 0.389 | 0.056 |
| 4.2-5.1 | 0.059 | 0.059 | 0.059 | 0.176 | 0.412 | 0.235 |
| 5.1-6.0 | 0.056 | 0.056 | 0.111 | 0.111 | 0.167 | 0.500 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/logreg_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3333, support=18
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.4444, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.333 | 0.167 | 0.167 | 0.056 | 0.111 | 0.167 |
| 1.5-2.4 | 0.222 | 0.222 | 0.111 | 0.222 | 0.056 | 0.167 |
| 2.4-3.3 | 0.167 | 0.278 | 0.278 | 0.167 | 0.111 | 0.000 |
| 3.3-4.2 | 0.000 | 0.111 | 0.222 | 0.222 | 0.167 | 0.278 |
| 4.2-5.1 | 0.118 | 0.118 | 0.176 | 0.176 | 0.294 | 0.118 |
| 5.1-6.0 | 0.111 | 0.056 | 0.056 | 0.111 | 0.222 | 0.444 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/mlp_none.png`

### Class Recall
- `0.6-1.5`: recall=0.3889, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.2941, support=17
- `5.1-6.0`: recall=0.5000, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.389 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 |
| 1.5-2.4 | 0.333 | 0.111 | 0.111 | 0.222 | 0.056 | 0.167 |
| 2.4-3.3 | 0.278 | 0.222 | 0.389 | 0.111 | 0.000 | 0.000 |
| 3.3-4.2 | 0.111 | 0.056 | 0.222 | 0.111 | 0.167 | 0.333 |
| 4.2-5.1 | 0.176 | 0.059 | 0.235 | 0.118 | 0.294 | 0.118 |
| 5.1-6.0 | 0.056 | 0.056 | 0.056 | 0.167 | 0.167 | 0.500 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_hardest/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `0.6-1.5`: recall=0.2778, support=18
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 0.6-1.5 | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 |
|---|---|---|---|---|---|---|
| 0.6-1.5 | 0.278 | 0.056 | 0.278 | 0.111 | 0.278 | 0.000 |
| 1.5-2.4 | 0.167 | 0.111 | 0.222 | 0.222 | 0.167 | 0.111 |
| 2.4-3.3 | 0.111 | 0.000 | 0.222 | 0.333 | 0.278 | 0.056 |
| 3.3-4.2 | 0.167 | 0.056 | 0.278 | 0.167 | 0.222 | 0.111 |
| 4.2-5.1 | 0.235 | 0.059 | 0.118 | 0.176 | 0.176 | 0.235 |
| 5.1-6.0 | 0.056 | 0.000 | 0.167 | 0.056 | 0.444 | 0.278 |


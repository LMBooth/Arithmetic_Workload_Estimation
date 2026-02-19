# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_omit_easiest.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2196)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.1961, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.2885, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.241 | 0.130 | 0.148 | 0.130 | 0.204 | 0.148 |
| 2.4-3.3 | 0.157 | 0.196 | 0.255 | 0.078 | 0.196 | 0.118 |
| 3.3-4.2 | 0.170 | 0.094 | 0.264 | 0.151 | 0.226 | 0.094 |
| 4.2-5.1 | 0.078 | 0.157 | 0.157 | 0.216 | 0.235 | 0.157 |
| 5.1-6.0 | 0.077 | 0.135 | 0.288 | 0.173 | 0.154 | 0.173 |
| 6.0-6.9 | 0.115 | 0.135 | 0.173 | 0.115 | 0.173 | 0.288 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2105)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3148, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.2157, support=51
- `5.1-6.0`: recall=0.1346, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.315 | 0.241 | 0.074 | 0.093 | 0.148 | 0.130 |
| 2.4-3.3 | 0.235 | 0.216 | 0.255 | 0.137 | 0.118 | 0.039 |
| 3.3-4.2 | 0.208 | 0.170 | 0.245 | 0.189 | 0.189 | 0.000 |
| 4.2-5.1 | 0.137 | 0.196 | 0.235 | 0.216 | 0.137 | 0.078 |
| 5.1-6.0 | 0.135 | 0.192 | 0.231 | 0.231 | 0.135 | 0.077 |
| 6.0-6.9 | 0.154 | 0.231 | 0.173 | 0.192 | 0.096 | 0.154 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1991)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.2075, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.2115, support=52
- `6.0-6.9`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.148 | 0.148 | 0.167 | 0.148 | 0.204 | 0.185 |
| 2.4-3.3 | 0.275 | 0.176 | 0.176 | 0.118 | 0.118 | 0.137 |
| 3.3-4.2 | 0.132 | 0.151 | 0.208 | 0.170 | 0.264 | 0.075 |
| 4.2-5.1 | 0.196 | 0.157 | 0.176 | 0.118 | 0.196 | 0.157 |
| 5.1-6.0 | 0.192 | 0.077 | 0.231 | 0.096 | 0.212 | 0.192 |
| 6.0-6.9 | 0.135 | 0.096 | 0.173 | 0.115 | 0.173 | 0.308 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1929)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2963, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.0566, support=53
- `4.2-5.1`: recall=0.3333, support=51
- `5.1-6.0`: recall=0.0385, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.296 | 0.222 | 0.019 | 0.185 | 0.056 | 0.222 |
| 2.4-3.3 | 0.255 | 0.216 | 0.039 | 0.196 | 0.039 | 0.255 |
| 3.3-4.2 | 0.264 | 0.208 | 0.057 | 0.245 | 0.019 | 0.208 |
| 4.2-5.1 | 0.216 | 0.176 | 0.059 | 0.333 | 0.059 | 0.157 |
| 5.1-6.0 | 0.327 | 0.135 | 0.077 | 0.308 | 0.038 | 0.115 |
| 6.0-6.9 | 0.154 | 0.192 | 0.096 | 0.308 | 0.058 | 0.192 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1815)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2830, support=53
- `4.2-5.1`: recall=0.1961, support=51
- `5.1-6.0`: recall=0.2500, support=52
- `6.0-6.9`: recall=0.1154, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.185 | 0.111 | 0.130 | 0.093 | 0.204 | 0.278 |
| 2.4-3.3 | 0.118 | 0.078 | 0.275 | 0.118 | 0.216 | 0.196 |
| 3.3-4.2 | 0.075 | 0.113 | 0.283 | 0.189 | 0.170 | 0.170 |
| 4.2-5.1 | 0.078 | 0.078 | 0.255 | 0.196 | 0.196 | 0.196 |
| 5.1-6.0 | 0.038 | 0.077 | 0.346 | 0.115 | 0.250 | 0.173 |
| 6.0-6.9 | 0.154 | 0.135 | 0.154 | 0.308 | 0.135 | 0.115 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1565)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2037, support=54
- `2.4-3.3`: recall=0.0980, support=51
- `3.3-4.2`: recall=0.1132, support=53
- `4.2-5.1`: recall=0.3137, support=51
- `5.1-6.0`: recall=0.0577, support=52
- `6.0-6.9`: recall=0.1538, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.204 | 0.185 | 0.130 | 0.259 | 0.074 | 0.148 |
| 2.4-3.3 | 0.196 | 0.098 | 0.157 | 0.275 | 0.078 | 0.196 |
| 3.3-4.2 | 0.208 | 0.132 | 0.113 | 0.283 | 0.094 | 0.170 |
| 4.2-5.1 | 0.098 | 0.157 | 0.176 | 0.314 | 0.078 | 0.176 |
| 5.1-6.0 | 0.173 | 0.231 | 0.192 | 0.288 | 0.058 | 0.058 |
| 6.0-6.9 | 0.154 | 0.135 | 0.192 | 0.308 | 0.058 | 0.154 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1488)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.2157, support=51
- `3.3-4.2`: recall=0.1132, support=53
- `4.2-5.1`: recall=0.1765, support=51
- `5.1-6.0`: recall=0.0769, support=52
- `6.0-6.9`: recall=0.2115, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.130 | 0.148 | 0.185 | 0.167 | 0.148 | 0.222 |
| 2.4-3.3 | 0.216 | 0.216 | 0.137 | 0.196 | 0.039 | 0.196 |
| 3.3-4.2 | 0.151 | 0.226 | 0.113 | 0.113 | 0.113 | 0.283 |
| 4.2-5.1 | 0.078 | 0.314 | 0.118 | 0.176 | 0.137 | 0.176 |
| 5.1-6.0 | 0.096 | 0.192 | 0.212 | 0.115 | 0.077 | 0.308 |
| 6.0-6.9 | 0.192 | 0.269 | 0.115 | 0.135 | 0.077 | 0.212 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2191)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.4706, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.188 | 0.500 | 0.062 | 0.062 | 0.125 | 0.062 |
| 2.4-3.3 | 0.235 | 0.471 | 0.000 | 0.235 | 0.059 | 0.000 |
| 3.3-4.2 | 0.294 | 0.353 | 0.000 | 0.294 | 0.059 | 0.000 |
| 4.2-5.1 | 0.000 | 0.333 | 0.056 | 0.611 | 0.000 | 0.000 |
| 5.1-6.0 | 0.278 | 0.333 | 0.056 | 0.167 | 0.056 | 0.111 |
| 6.0-6.9 | 0.389 | 0.222 | 0.056 | 0.222 | 0.111 | 0.000 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1911)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3750, support=16
- `2.4-3.3`: recall=0.2941, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.375 | 0.312 | 0.000 | 0.188 | 0.125 | 0.000 |
| 2.4-3.3 | 0.235 | 0.294 | 0.000 | 0.235 | 0.118 | 0.118 |
| 3.3-4.2 | 0.294 | 0.294 | 0.000 | 0.118 | 0.176 | 0.118 |
| 4.2-5.1 | 0.056 | 0.389 | 0.056 | 0.167 | 0.167 | 0.167 |
| 5.1-6.0 | 0.222 | 0.278 | 0.056 | 0.056 | 0.278 | 0.111 |
| 6.0-6.9 | 0.278 | 0.278 | 0.111 | 0.278 | 0.056 | 0.000 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1870)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.4118, support=17
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.188 | 0.500 | 0.000 | 0.188 | 0.125 | 0.000 |
| 2.4-3.3 | 0.118 | 0.412 | 0.118 | 0.118 | 0.118 | 0.118 |
| 3.3-4.2 | 0.294 | 0.294 | 0.059 | 0.118 | 0.118 | 0.118 |
| 4.2-5.1 | 0.278 | 0.444 | 0.000 | 0.111 | 0.111 | 0.056 |
| 5.1-6.0 | 0.278 | 0.056 | 0.167 | 0.222 | 0.167 | 0.111 |
| 6.0-6.9 | 0.333 | 0.167 | 0.111 | 0.111 | 0.111 | 0.167 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1865)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3125, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.6111, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.312 | 0.312 | 0.000 | 0.312 | 0.062 | 0.000 |
| 2.4-3.3 | 0.412 | 0.176 | 0.000 | 0.412 | 0.000 | 0.000 |
| 3.3-4.2 | 0.353 | 0.353 | 0.000 | 0.294 | 0.000 | 0.000 |
| 4.2-5.1 | 0.278 | 0.111 | 0.000 | 0.611 | 0.000 | 0.000 |
| 5.1-6.0 | 0.056 | 0.667 | 0.000 | 0.167 | 0.000 | 0.111 |
| 6.0-6.9 | 0.389 | 0.222 | 0.000 | 0.389 | 0.000 | 0.000 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1662)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.4118, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.188 | 0.500 | 0.062 | 0.188 | 0.062 | 0.000 |
| 2.4-3.3 | 0.176 | 0.412 | 0.059 | 0.059 | 0.176 | 0.118 |
| 3.3-4.2 | 0.118 | 0.412 | 0.000 | 0.000 | 0.176 | 0.294 |
| 4.2-5.1 | 0.000 | 0.389 | 0.111 | 0.167 | 0.278 | 0.056 |
| 5.1-6.0 | 0.222 | 0.056 | 0.278 | 0.056 | 0.222 | 0.167 |
| 6.0-6.9 | 0.333 | 0.222 | 0.111 | 0.056 | 0.278 | 0.000 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1400)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0625, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.062 | 0.312 | 0.250 | 0.125 | 0.125 | 0.125 |
| 2.4-3.3 | 0.176 | 0.118 | 0.000 | 0.235 | 0.235 | 0.235 |
| 3.3-4.2 | 0.235 | 0.176 | 0.000 | 0.118 | 0.176 | 0.294 |
| 4.2-5.1 | 0.111 | 0.278 | 0.111 | 0.278 | 0.167 | 0.056 |
| 5.1-6.0 | 0.167 | 0.111 | 0.000 | 0.222 | 0.278 | 0.222 |
| 6.0-6.9 | 0.111 | 0.167 | 0.111 | 0.167 | 0.333 | 0.111 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1076)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/loso/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1250, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.125 | 0.312 | 0.188 | 0.062 | 0.062 | 0.250 |
| 2.4-3.3 | 0.118 | 0.176 | 0.118 | 0.353 | 0.000 | 0.235 |
| 3.3-4.2 | 0.235 | 0.176 | 0.176 | 0.059 | 0.176 | 0.176 |
| 4.2-5.1 | 0.278 | 0.444 | 0.056 | 0.000 | 0.167 | 0.056 |
| 5.1-6.0 | 0.111 | 0.389 | 0.167 | 0.167 | 0.111 | 0.056 |
| 6.0-6.9 | 0.278 | 0.278 | 0.222 | 0.056 | 0.111 | 0.056 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.0000, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.222 | 0.000 | 0.056 | 0.333 | 0.222 |
| 2.4-3.3 | 0.333 | 0.167 | 0.111 | 0.167 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.222 | 0.000 | 0.278 | 0.278 | 0.167 |
| 4.2-5.1 | 0.333 | 0.222 | 0.056 | 0.278 | 0.056 | 0.056 |
| 5.1-6.0 | 0.333 | 0.056 | 0.056 | 0.111 | 0.389 | 0.056 |
| 6.0-6.9 | 0.278 | 0.167 | 0.056 | 0.222 | 0.111 | 0.167 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.056 | 0.167 | 0.111 | 0.111 | 0.222 | 0.333 |
| 2.4-3.3 | 0.111 | 0.167 | 0.222 | 0.222 | 0.056 | 0.222 |
| 3.3-4.2 | 0.111 | 0.167 | 0.167 | 0.167 | 0.222 | 0.167 |
| 4.2-5.1 | 0.111 | 0.111 | 0.056 | 0.389 | 0.278 | 0.056 |
| 5.1-6.0 | 0.056 | 0.167 | 0.222 | 0.167 | 0.278 | 0.111 |
| 6.0-6.9 | 0.222 | 0.222 | 0.111 | 0.111 | 0.000 | 0.333 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.222 | 0.056 | 0.000 | 0.278 | 0.278 |
| 2.4-3.3 | 0.222 | 0.111 | 0.222 | 0.167 | 0.111 | 0.167 |
| 3.3-4.2 | 0.167 | 0.111 | 0.278 | 0.167 | 0.222 | 0.056 |
| 4.2-5.1 | 0.167 | 0.222 | 0.111 | 0.222 | 0.222 | 0.056 |
| 5.1-6.0 | 0.056 | 0.056 | 0.278 | 0.167 | 0.333 | 0.111 |
| 6.0-6.9 | 0.167 | 0.222 | 0.111 | 0.056 | 0.222 | 0.222 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.278 | 0.111 | 0.000 | 0.222 | 0.222 |
| 2.4-3.3 | 0.111 | 0.222 | 0.278 | 0.167 | 0.167 | 0.056 |
| 3.3-4.2 | 0.056 | 0.167 | 0.222 | 0.111 | 0.278 | 0.167 |
| 4.2-5.1 | 0.111 | 0.167 | 0.333 | 0.222 | 0.111 | 0.056 |
| 5.1-6.0 | 0.167 | 0.056 | 0.278 | 0.111 | 0.333 | 0.056 |
| 6.0-6.9 | 0.167 | 0.333 | 0.278 | 0.056 | 0.056 | 0.111 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.111 | 0.111 | 0.000 | 0.167 | 0.222 | 0.389 |
| 2.4-3.3 | 0.056 | 0.167 | 0.111 | 0.222 | 0.167 | 0.278 |
| 3.3-4.2 | 0.167 | 0.167 | 0.167 | 0.111 | 0.222 | 0.167 |
| 4.2-5.1 | 0.056 | 0.222 | 0.222 | 0.111 | 0.278 | 0.111 |
| 5.1-6.0 | 0.111 | 0.000 | 0.167 | 0.167 | 0.389 | 0.167 |
| 6.0-6.9 | 0.167 | 0.167 | 0.111 | 0.222 | 0.056 | 0.278 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.056 | 0.278 | 0.000 | 0.222 | 0.167 | 0.278 |
| 2.4-3.3 | 0.167 | 0.111 | 0.000 | 0.278 | 0.167 | 0.278 |
| 3.3-4.2 | 0.056 | 0.222 | 0.056 | 0.333 | 0.111 | 0.222 |
| 4.2-5.1 | 0.056 | 0.167 | 0.167 | 0.333 | 0.111 | 0.167 |
| 5.1-6.0 | 0.111 | 0.056 | 0.167 | 0.222 | 0.333 | 0.111 |
| 6.0-6.9 | 0.111 | 0.278 | 0.000 | 0.222 | 0.056 | 0.333 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.1250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0556, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.2222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.056 | 0.167 | 0.056 | 0.222 | 0.056 | 0.444 |
| 2.4-3.3 | 0.222 | 0.000 | 0.222 | 0.167 | 0.111 | 0.278 |
| 3.3-4.2 | 0.056 | 0.167 | 0.167 | 0.167 | 0.222 | 0.222 |
| 4.2-5.1 | 0.056 | 0.111 | 0.167 | 0.222 | 0.222 | 0.222 |
| 5.1-6.0 | 0.000 | 0.222 | 0.167 | 0.278 | 0.222 | 0.111 |
| 6.0-6.9 | 0.222 | 0.333 | 0.111 | 0.056 | 0.111 | 0.167 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1990)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.1569, support=51
- `3.3-4.2`: recall=0.3019, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.1538, support=52
- `6.0-6.9`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.148 | 0.167 | 0.204 | 0.093 | 0.130 | 0.259 |
| 2.4-3.3 | 0.098 | 0.157 | 0.137 | 0.157 | 0.078 | 0.373 |
| 3.3-4.2 | 0.094 | 0.075 | 0.302 | 0.151 | 0.094 | 0.283 |
| 4.2-5.1 | 0.000 | 0.196 | 0.216 | 0.118 | 0.098 | 0.373 |
| 5.1-6.0 | 0.038 | 0.192 | 0.192 | 0.096 | 0.154 | 0.327 |
| 6.0-6.9 | 0.038 | 0.077 | 0.135 | 0.135 | 0.308 | 0.308 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1981)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.5094, support=53
- `4.2-5.1`: recall=0.0784, support=51
- `5.1-6.0`: recall=0.1154, support=52
- `6.0-6.9`: recall=0.2308, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.148 | 0.037 | 0.426 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.078 | 0.059 | 0.373 | 0.176 | 0.098 | 0.216 |
| 3.3-4.2 | 0.038 | 0.094 | 0.509 | 0.038 | 0.113 | 0.208 |
| 4.2-5.1 | 0.078 | 0.118 | 0.412 | 0.078 | 0.118 | 0.196 |
| 5.1-6.0 | 0.058 | 0.077 | 0.385 | 0.115 | 0.115 | 0.250 |
| 6.0-6.9 | 0.058 | 0.115 | 0.346 | 0.096 | 0.154 | 0.231 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1867)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.0588, support=51
- `3.3-4.2`: recall=0.1698, support=53
- `4.2-5.1`: recall=0.1176, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.3077, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.278 | 0.056 | 0.185 | 0.167 | 0.074 | 0.241 |
| 2.4-3.3 | 0.176 | 0.059 | 0.196 | 0.157 | 0.098 | 0.314 |
| 3.3-4.2 | 0.151 | 0.075 | 0.170 | 0.094 | 0.208 | 0.302 |
| 4.2-5.1 | 0.078 | 0.098 | 0.255 | 0.118 | 0.157 | 0.294 |
| 5.1-6.0 | 0.058 | 0.077 | 0.173 | 0.212 | 0.192 | 0.288 |
| 6.0-6.9 | 0.058 | 0.058 | 0.115 | 0.135 | 0.327 | 0.308 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1847)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=54
- `2.4-3.3`: recall=0.1765, support=51
- `3.3-4.2`: recall=0.2453, support=53
- `4.2-5.1`: recall=0.0980, support=51
- `5.1-6.0`: recall=0.0769, support=52
- `6.0-6.9`: recall=0.1923, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.148 | 0.185 | 0.074 | 0.074 | 0.185 |
| 2.4-3.3 | 0.216 | 0.176 | 0.157 | 0.196 | 0.176 | 0.078 |
| 3.3-4.2 | 0.170 | 0.170 | 0.245 | 0.170 | 0.075 | 0.170 |
| 4.2-5.1 | 0.176 | 0.176 | 0.294 | 0.098 | 0.098 | 0.157 |
| 5.1-6.0 | 0.192 | 0.212 | 0.154 | 0.154 | 0.077 | 0.212 |
| 6.0-6.9 | 0.269 | 0.154 | 0.154 | 0.135 | 0.096 | 0.192 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1832)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0185, support=54
- `2.4-3.3`: recall=0.0196, support=51
- `3.3-4.2`: recall=0.7358, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.0577, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.019 | 0.056 | 0.815 | 0.056 | 0.056 | 0.000 |
| 2.4-3.3 | 0.039 | 0.020 | 0.765 | 0.078 | 0.059 | 0.039 |
| 3.3-4.2 | 0.057 | 0.057 | 0.736 | 0.038 | 0.057 | 0.057 |
| 4.2-5.1 | 0.020 | 0.020 | 0.804 | 0.039 | 0.118 | 0.000 |
| 5.1-6.0 | 0.019 | 0.038 | 0.712 | 0.038 | 0.192 | 0.000 |
| 6.0-6.9 | 0.038 | 0.038 | 0.788 | 0.038 | 0.038 | 0.058 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1803)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2407, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1731, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.241 | 0.148 | 0.185 | 0.056 | 0.074 | 0.296 |
| 2.4-3.3 | 0.157 | 0.078 | 0.275 | 0.078 | 0.137 | 0.275 |
| 3.3-4.2 | 0.075 | 0.038 | 0.264 | 0.094 | 0.245 | 0.283 |
| 4.2-5.1 | 0.098 | 0.078 | 0.353 | 0.039 | 0.176 | 0.255 |
| 5.1-6.0 | 0.096 | 0.019 | 0.288 | 0.096 | 0.173 | 0.327 |
| 6.0-6.9 | 0.154 | 0.058 | 0.346 | 0.019 | 0.154 | 0.269 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/group_holdout/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1852, support=54
- `2.4-3.3`: recall=0.0784, support=51
- `3.3-4.2`: recall=0.2642, support=53
- `4.2-5.1`: recall=0.0392, support=51
- `5.1-6.0`: recall=0.1923, support=52
- `6.0-6.9`: recall=0.2692, support=52

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.185 | 0.148 | 0.222 | 0.056 | 0.093 | 0.296 |
| 2.4-3.3 | 0.196 | 0.078 | 0.216 | 0.078 | 0.137 | 0.294 |
| 3.3-4.2 | 0.132 | 0.038 | 0.264 | 0.075 | 0.189 | 0.302 |
| 4.2-5.1 | 0.118 | 0.059 | 0.294 | 0.039 | 0.235 | 0.255 |
| 5.1-6.0 | 0.115 | 0.058 | 0.288 | 0.058 | 0.192 | 0.288 |
| 6.0-6.9 | 0.173 | 0.019 | 0.288 | 0.058 | 0.192 | 0.269 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2262)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.8750, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.875 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 |
| 2.4-3.3 | 0.647 | 0.118 | 0.000 | 0.000 | 0.235 | 0.000 |
| 3.3-4.2 | 0.706 | 0.118 | 0.000 | 0.000 | 0.176 | 0.000 |
| 4.2-5.1 | 0.667 | 0.000 | 0.000 | 0.056 | 0.222 | 0.056 |
| 5.1-6.0 | 0.500 | 0.000 | 0.111 | 0.000 | 0.333 | 0.056 |
| 6.0-6.9 | 0.667 | 0.000 | 0.056 | 0.000 | 0.278 | 0.000 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1997)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.688 | 0.000 | 0.188 | 0.000 | 0.062 | 0.062 |
| 2.4-3.3 | 0.412 | 0.118 | 0.118 | 0.000 | 0.235 | 0.118 |
| 3.3-4.2 | 0.529 | 0.118 | 0.000 | 0.000 | 0.235 | 0.118 |
| 4.2-5.1 | 0.389 | 0.111 | 0.222 | 0.000 | 0.167 | 0.111 |
| 5.1-6.0 | 0.167 | 0.278 | 0.111 | 0.000 | 0.333 | 0.111 |
| 6.0-6.9 | 0.333 | 0.167 | 0.056 | 0.000 | 0.333 | 0.111 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1890)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.6250, support=16
- `2.4-3.3`: recall=0.1765, support=17
- `3.3-4.2`: recall=0.3529, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.625 | 0.062 | 0.312 | 0.000 | 0.000 | 0.000 |
| 2.4-3.3 | 0.647 | 0.176 | 0.176 | 0.000 | 0.000 | 0.000 |
| 3.3-4.2 | 0.529 | 0.059 | 0.353 | 0.000 | 0.059 | 0.000 |
| 4.2-5.1 | 0.389 | 0.056 | 0.556 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.111 | 0.056 | 0.833 | 0.000 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.056 | 0.444 | 0.000 | 0.000 | 0.000 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1888)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.688 | 0.188 | 0.062 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.471 | 0.059 | 0.235 | 0.000 | 0.000 | 0.235 |
| 3.3-4.2 | 0.353 | 0.353 | 0.118 | 0.000 | 0.059 | 0.118 |
| 4.2-5.1 | 0.278 | 0.333 | 0.222 | 0.000 | 0.000 | 0.167 |
| 5.1-6.0 | 0.167 | 0.389 | 0.222 | 0.000 | 0.056 | 0.167 |
| 6.0-6.9 | 0.333 | 0.333 | 0.056 | 0.000 | 0.056 | 0.222 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1743)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2500, support=16
- `2.4-3.3`: recall=0.4118, support=17
- `3.3-4.2`: recall=0.3529, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.250 | 0.562 | 0.125 | 0.000 | 0.000 | 0.062 |
| 2.4-3.3 | 0.118 | 0.412 | 0.353 | 0.000 | 0.000 | 0.118 |
| 3.3-4.2 | 0.235 | 0.412 | 0.353 | 0.000 | 0.000 | 0.000 |
| 4.2-5.1 | 0.056 | 0.556 | 0.389 | 0.000 | 0.000 | 0.000 |
| 5.1-6.0 | 0.056 | 0.444 | 0.333 | 0.056 | 0.000 | 0.111 |
| 6.0-6.9 | 0.056 | 0.500 | 0.333 | 0.000 | 0.111 | 0.000 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1442)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.6875, support=16
- `2.4-3.3`: recall=0.0588, support=17
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.688 | 0.000 | 0.062 | 0.125 | 0.062 | 0.062 |
| 2.4-3.3 | 0.471 | 0.059 | 0.176 | 0.059 | 0.235 | 0.000 |
| 3.3-4.2 | 0.529 | 0.118 | 0.000 | 0.118 | 0.118 | 0.118 |
| 4.2-5.1 | 0.444 | 0.000 | 0.333 | 0.000 | 0.167 | 0.056 |
| 5.1-6.0 | 0.278 | 0.056 | 0.444 | 0.000 | 0.000 | 0.222 |
| 6.0-6.9 | 0.389 | 0.111 | 0.222 | 0.000 | 0.111 | 0.167 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1334)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/loso/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1875, support=16
- `2.4-3.3`: recall=0.1176, support=17
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.188 | 0.188 | 0.062 | 0.375 | 0.125 | 0.062 |
| 2.4-3.3 | 0.412 | 0.118 | 0.118 | 0.294 | 0.059 | 0.000 |
| 3.3-4.2 | 0.235 | 0.294 | 0.176 | 0.176 | 0.118 | 0.000 |
| 4.2-5.1 | 0.222 | 0.056 | 0.111 | 0.222 | 0.111 | 0.278 |
| 5.1-6.0 | 0.056 | 0.111 | 0.056 | 0.333 | 0.111 | 0.333 |
| 6.0-6.9 | 0.222 | 0.111 | 0.111 | 0.444 | 0.111 | 0.000 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.278 | 0.111 | 0.167 | 0.222 | 0.111 | 0.111 |
| 2.4-3.3 | 0.222 | 0.333 | 0.278 | 0.111 | 0.056 | 0.000 |
| 3.3-4.2 | 0.222 | 0.056 | 0.167 | 0.333 | 0.000 | 0.222 |
| 4.2-5.1 | 0.111 | 0.222 | 0.056 | 0.167 | 0.333 | 0.111 |
| 5.1-6.0 | 0.111 | 0.056 | 0.000 | 0.222 | 0.500 | 0.111 |
| 6.0-6.9 | 0.000 | 0.056 | 0.167 | 0.333 | 0.278 | 0.167 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.278 | 0.056 | 0.111 | 0.167 | 0.167 |
| 2.4-3.3 | 0.278 | 0.222 | 0.278 | 0.167 | 0.000 | 0.056 |
| 3.3-4.2 | 0.167 | 0.167 | 0.278 | 0.278 | 0.000 | 0.111 |
| 4.2-5.1 | 0.111 | 0.111 | 0.167 | 0.222 | 0.222 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.000 | 0.167 | 0.500 | 0.278 |
| 6.0-6.9 | 0.167 | 0.056 | 0.056 | 0.333 | 0.222 | 0.167 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2778, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.5556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.278 | 0.167 | 0.167 | 0.222 | 0.111 | 0.056 |
| 2.4-3.3 | 0.278 | 0.278 | 0.222 | 0.167 | 0.000 | 0.056 |
| 3.3-4.2 | 0.167 | 0.056 | 0.167 | 0.333 | 0.056 | 0.222 |
| 4.2-5.1 | 0.056 | 0.222 | 0.167 | 0.167 | 0.222 | 0.167 |
| 5.1-6.0 | 0.000 | 0.111 | 0.056 | 0.111 | 0.556 | 0.167 |
| 6.0-6.9 | 0.056 | 0.056 | 0.222 | 0.222 | 0.278 | 0.167 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.056 | 0.278 | 0.333 | 0.056 | 0.056 |
| 2.4-3.3 | 0.167 | 0.278 | 0.278 | 0.278 | 0.000 | 0.000 |
| 3.3-4.2 | 0.222 | 0.111 | 0.167 | 0.278 | 0.056 | 0.167 |
| 4.2-5.1 | 0.000 | 0.111 | 0.167 | 0.278 | 0.278 | 0.167 |
| 5.1-6.0 | 0.000 | 0.056 | 0.000 | 0.333 | 0.389 | 0.222 |
| 6.0-6.9 | 0.111 | 0.000 | 0.167 | 0.333 | 0.167 | 0.222 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2250)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1111, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.167 | 0.222 | 0.167 | 0.111 | 0.111 |
| 2.4-3.3 | 0.222 | 0.222 | 0.111 | 0.278 | 0.056 | 0.111 |
| 3.3-4.2 | 0.278 | 0.167 | 0.111 | 0.222 | 0.000 | 0.222 |
| 4.2-5.1 | 0.111 | 0.278 | 0.167 | 0.111 | 0.111 | 0.222 |
| 5.1-6.0 | 0.056 | 0.000 | 0.000 | 0.167 | 0.611 | 0.167 |
| 6.0-6.9 | 0.111 | 0.056 | 0.111 | 0.333 | 0.222 | 0.167 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1111, support=18
- `4.2-5.1`: recall=0.1667, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.111 | 0.222 | 0.222 | 0.056 | 0.167 |
| 2.4-3.3 | 0.278 | 0.278 | 0.222 | 0.167 | 0.056 | 0.000 |
| 3.3-4.2 | 0.167 | 0.222 | 0.111 | 0.444 | 0.000 | 0.056 |
| 4.2-5.1 | 0.222 | 0.167 | 0.167 | 0.167 | 0.278 | 0.000 |
| 5.1-6.0 | 0.111 | 0.111 | 0.056 | 0.222 | 0.389 | 0.111 |
| 6.0-6.9 | 0.056 | 0.056 | 0.167 | 0.278 | 0.333 | 0.111 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2000)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.2778, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.222 | 0.111 | 0.056 | 0.333 | 0.111 |
| 2.4-3.3 | 0.167 | 0.278 | 0.167 | 0.167 | 0.056 | 0.167 |
| 3.3-4.2 | 0.278 | 0.056 | 0.167 | 0.278 | 0.000 | 0.222 |
| 4.2-5.1 | 0.000 | 0.111 | 0.167 | 0.278 | 0.000 | 0.444 |
| 5.1-6.0 | 0.167 | 0.111 | 0.111 | 0.111 | 0.333 | 0.167 |
| 6.0-6.9 | 0.167 | 0.000 | 0.167 | 0.500 | 0.111 | 0.056 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2192)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2593, support=54
- `2.4-3.3`: recall=0.1296, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.0943, support=53
- `5.1-6.0`: recall=0.4340, support=53
- `6.0-6.9`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.259 | 0.019 | 0.167 | 0.111 | 0.296 | 0.148 |
| 2.4-3.3 | 0.148 | 0.130 | 0.148 | 0.056 | 0.278 | 0.241 |
| 3.3-4.2 | 0.130 | 0.148 | 0.093 | 0.093 | 0.352 | 0.185 |
| 4.2-5.1 | 0.113 | 0.094 | 0.170 | 0.094 | 0.302 | 0.226 |
| 5.1-6.0 | 0.094 | 0.094 | 0.094 | 0.038 | 0.434 | 0.245 |
| 6.0-6.9 | 0.132 | 0.094 | 0.151 | 0.019 | 0.302 | 0.302 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2050)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.1481, support=54
- `4.2-5.1`: recall=0.0189, support=53
- `5.1-6.0`: recall=0.3585, support=53
- `6.0-6.9`: recall=0.2830, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.278 | 0.111 | 0.130 | 0.019 | 0.222 | 0.241 |
| 2.4-3.3 | 0.148 | 0.093 | 0.222 | 0.000 | 0.315 | 0.222 |
| 3.3-4.2 | 0.111 | 0.185 | 0.148 | 0.019 | 0.278 | 0.259 |
| 4.2-5.1 | 0.094 | 0.151 | 0.151 | 0.019 | 0.377 | 0.208 |
| 5.1-6.0 | 0.132 | 0.038 | 0.170 | 0.000 | 0.358 | 0.302 |
| 6.0-6.9 | 0.151 | 0.151 | 0.094 | 0.019 | 0.302 | 0.283 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1909)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.2407, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.1509, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.2075, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.259 | 0.259 | 0.093 | 0.074 | 0.093 |
| 2.4-3.3 | 0.185 | 0.241 | 0.111 | 0.093 | 0.222 | 0.148 |
| 3.3-4.2 | 0.093 | 0.222 | 0.111 | 0.074 | 0.278 | 0.222 |
| 4.2-5.1 | 0.038 | 0.377 | 0.094 | 0.151 | 0.189 | 0.151 |
| 5.1-6.0 | 0.094 | 0.340 | 0.038 | 0.208 | 0.208 | 0.113 |
| 6.0-6.9 | 0.075 | 0.283 | 0.075 | 0.151 | 0.208 | 0.208 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1866)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3519, support=54
- `2.4-3.3`: recall=0.0741, support=54
- `3.3-4.2`: recall=0.1111, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.3019, support=53
- `6.0-6.9`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.352 | 0.111 | 0.093 | 0.019 | 0.204 | 0.222 |
| 2.4-3.3 | 0.259 | 0.074 | 0.037 | 0.019 | 0.389 | 0.222 |
| 3.3-4.2 | 0.167 | 0.074 | 0.111 | 0.056 | 0.389 | 0.204 |
| 4.2-5.1 | 0.170 | 0.113 | 0.075 | 0.038 | 0.415 | 0.189 |
| 5.1-6.0 | 0.208 | 0.075 | 0.057 | 0.075 | 0.302 | 0.283 |
| 6.0-6.9 | 0.283 | 0.113 | 0.057 | 0.038 | 0.245 | 0.264 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1677)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.2778, support=54
- `3.3-4.2`: recall=0.2963, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.1698, support=53
- `6.0-6.9`: recall=0.1321, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.148 | 0.093 | 0.130 | 0.241 | 0.204 | 0.185 |
| 2.4-3.3 | 0.093 | 0.278 | 0.204 | 0.037 | 0.167 | 0.222 |
| 3.3-4.2 | 0.074 | 0.074 | 0.296 | 0.185 | 0.167 | 0.204 |
| 4.2-5.1 | 0.075 | 0.094 | 0.302 | 0.057 | 0.283 | 0.189 |
| 5.1-6.0 | 0.151 | 0.057 | 0.226 | 0.189 | 0.170 | 0.208 |
| 6.0-6.9 | 0.151 | 0.132 | 0.321 | 0.113 | 0.151 | 0.132 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1647)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.1852, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.3962, support=53
- `5.1-6.0`: recall=0.0566, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.296 | 0.019 | 0.185 | 0.241 | 0.037 |
| 2.4-3.3 | 0.259 | 0.185 | 0.000 | 0.278 | 0.185 | 0.093 |
| 3.3-4.2 | 0.370 | 0.204 | 0.056 | 0.241 | 0.111 | 0.019 |
| 4.2-5.1 | 0.358 | 0.132 | 0.000 | 0.396 | 0.075 | 0.038 |
| 5.1-6.0 | 0.491 | 0.075 | 0.000 | 0.340 | 0.057 | 0.038 |
| 6.0-6.9 | 0.396 | 0.075 | 0.038 | 0.434 | 0.019 | 0.038 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1595)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.000 | 0.019 | 0.037 | 0.000 | 0.870 | 0.074 |
| 2.4-3.3 | 0.000 | 0.019 | 0.019 | 0.000 | 0.815 | 0.148 |
| 3.3-4.2 | 0.000 | 0.074 | 0.000 | 0.019 | 0.870 | 0.037 |
| 4.2-5.1 | 0.000 | 0.057 | 0.000 | 0.000 | 0.868 | 0.075 |
| 5.1-6.0 | 0.000 | 0.038 | 0.000 | 0.000 | 0.887 | 0.075 |
| 6.0-6.9 | 0.000 | 0.038 | 0.000 | 0.038 | 0.887 | 0.038 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2222)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0556, support=18
- `5.1-6.0`: recall=0.7222, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.389 | 0.056 | 0.111 | 0.056 | 0.278 | 0.111 |
| 2.4-3.3 | 0.444 | 0.000 | 0.056 | 0.111 | 0.333 | 0.056 |
| 3.3-4.2 | 0.235 | 0.059 | 0.000 | 0.000 | 0.706 | 0.000 |
| 4.2-5.1 | 0.111 | 0.000 | 0.111 | 0.056 | 0.556 | 0.167 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.056 | 0.722 | 0.111 |
| 6.0-6.9 | 0.111 | 0.000 | 0.167 | 0.000 | 0.556 | 0.167 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2072)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.4706, support=17
- `4.2-5.1`: recall=0.2222, support=18
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.111 | 0.222 | 0.000 | 0.167 | 0.167 |
| 2.4-3.3 | 0.222 | 0.000 | 0.389 | 0.111 | 0.056 | 0.222 |
| 3.3-4.2 | 0.235 | 0.059 | 0.471 | 0.059 | 0.118 | 0.059 |
| 4.2-5.1 | 0.056 | 0.000 | 0.556 | 0.222 | 0.000 | 0.167 |
| 5.1-6.0 | 0.000 | 0.000 | 0.667 | 0.111 | 0.056 | 0.167 |
| 6.0-6.9 | 0.000 | 0.000 | 0.667 | 0.000 | 0.167 | 0.167 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2037)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.389 | 0.056 | 0.000 | 0.000 | 0.500 | 0.056 |
| 2.4-3.3 | 0.389 | 0.056 | 0.000 | 0.000 | 0.500 | 0.056 |
| 3.3-4.2 | 0.294 | 0.000 | 0.000 | 0.000 | 0.647 | 0.059 |
| 4.2-5.1 | 0.056 | 0.000 | 0.222 | 0.000 | 0.500 | 0.222 |
| 5.1-6.0 | 0.056 | 0.000 | 0.111 | 0.000 | 0.611 | 0.222 |
| 6.0-6.9 | 0.000 | 0.000 | 0.056 | 0.111 | 0.667 | 0.167 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.1875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.2222, support=18
- `3.3-4.2`: recall=0.1176, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.444 | 0.222 | 0.167 | 0.000 | 0.167 | 0.000 |
| 2.4-3.3 | 0.333 | 0.222 | 0.111 | 0.000 | 0.167 | 0.167 |
| 3.3-4.2 | 0.176 | 0.294 | 0.118 | 0.059 | 0.118 | 0.235 |
| 4.2-5.1 | 0.167 | 0.056 | 0.278 | 0.000 | 0.444 | 0.056 |
| 5.1-6.0 | 0.111 | 0.278 | 0.222 | 0.222 | 0.167 | 0.000 |
| 6.0-6.9 | 0.000 | 0.167 | 0.167 | 0.278 | 0.222 | 0.167 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1678)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.3889, support=18
- `5.1-6.0`: recall=0.1667, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.000 | 0.389 | 0.222 | 0.000 | 0.222 |
| 2.4-3.3 | 0.167 | 0.000 | 0.389 | 0.333 | 0.000 | 0.111 |
| 3.3-4.2 | 0.176 | 0.059 | 0.176 | 0.176 | 0.235 | 0.176 |
| 4.2-5.1 | 0.111 | 0.000 | 0.389 | 0.389 | 0.000 | 0.111 |
| 5.1-6.0 | 0.167 | 0.056 | 0.278 | 0.222 | 0.167 | 0.111 |
| 6.0-6.9 | 0.111 | 0.000 | 0.278 | 0.278 | 0.222 | 0.111 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1296)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/loso/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.222 | 0.000 | 0.500 | 0.000 | 0.056 |
| 2.4-3.3 | 0.444 | 0.056 | 0.000 | 0.500 | 0.000 | 0.000 |
| 3.3-4.2 | 0.412 | 0.118 | 0.000 | 0.471 | 0.000 | 0.000 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.2667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.333 | 0.111 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.444 | 0.111 | 0.167 | 0.056 | 0.111 | 0.111 |
| 3.3-4.2 | 0.222 | 0.167 | 0.222 | 0.167 | 0.111 | 0.111 |
| 4.2-5.1 | 0.059 | 0.176 | 0.118 | 0.353 | 0.059 | 0.235 |
| 5.1-6.0 | 0.056 | 0.222 | 0.111 | 0.167 | 0.333 | 0.111 |
| 6.0-6.9 | 0.111 | 0.167 | 0.167 | 0.111 | 0.222 | 0.222 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.2417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.0588, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.500 | 0.222 | 0.111 | 0.111 | 0.000 | 0.056 |
| 2.4-3.3 | 0.389 | 0.111 | 0.222 | 0.056 | 0.056 | 0.167 |
| 3.3-4.2 | 0.111 | 0.278 | 0.167 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.176 | 0.176 | 0.118 | 0.059 | 0.176 | 0.294 |
| 5.1-6.0 | 0.000 | 0.000 | 0.111 | 0.333 | 0.444 | 0.111 |
| 6.0-6.9 | 0.167 | 0.278 | 0.056 | 0.222 | 0.056 | 0.222 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.2333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.1111, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.500 | 0.167 | 0.111 | 0.056 | 0.056 | 0.111 |
| 2.4-3.3 | 0.278 | 0.111 | 0.167 | 0.167 | 0.111 | 0.167 |
| 3.3-4.2 | 0.167 | 0.222 | 0.056 | 0.000 | 0.333 | 0.222 |
| 4.2-5.1 | 0.000 | 0.059 | 0.294 | 0.118 | 0.294 | 0.235 |
| 5.1-6.0 | 0.111 | 0.111 | 0.000 | 0.222 | 0.500 | 0.056 |
| 6.0-6.9 | 0.222 | 0.111 | 0.167 | 0.333 | 0.056 | 0.111 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.6111, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.611 | 0.111 | 0.056 | 0.222 | 0.000 | 0.000 |
| 2.4-3.3 | 0.222 | 0.000 | 0.222 | 0.389 | 0.056 | 0.111 |
| 3.3-4.2 | 0.111 | 0.278 | 0.167 | 0.222 | 0.167 | 0.056 |
| 4.2-5.1 | 0.118 | 0.118 | 0.059 | 0.353 | 0.294 | 0.059 |
| 5.1-6.0 | 0.167 | 0.000 | 0.056 | 0.444 | 0.333 | 0.000 |
| 6.0-6.9 | 0.167 | 0.167 | 0.056 | 0.500 | 0.111 | 0.000 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.2167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.444 | 0.111 | 0.111 | 0.167 | 0.056 | 0.111 |
| 2.4-3.3 | 0.222 | 0.167 | 0.222 | 0.111 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.278 | 0.222 | 0.222 | 0.167 | 0.000 |
| 4.2-5.1 | 0.059 | 0.294 | 0.176 | 0.118 | 0.176 | 0.176 |
| 5.1-6.0 | 0.111 | 0.056 | 0.111 | 0.333 | 0.278 | 0.111 |
| 6.0-6.9 | 0.111 | 0.111 | 0.056 | 0.500 | 0.167 | 0.056 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.2083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.1667, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.0000, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.222 | 0.167 | 0.056 | 0.056 | 0.167 |
| 2.4-3.3 | 0.167 | 0.167 | 0.333 | 0.056 | 0.111 | 0.167 |
| 3.3-4.2 | 0.111 | 0.333 | 0.222 | 0.111 | 0.167 | 0.056 |
| 4.2-5.1 | 0.059 | 0.235 | 0.176 | 0.000 | 0.235 | 0.294 |
| 5.1-6.0 | 0.167 | 0.056 | 0.056 | 0.222 | 0.444 | 0.056 |
| 6.0-6.9 | 0.111 | 0.278 | 0.056 | 0.333 | 0.167 | 0.056 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1583)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.0556, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.389 | 0.111 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.167 | 0.278 | 0.111 | 0.278 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.333 | 0.056 | 0.222 | 0.167 | 0.111 |
| 4.2-5.1 | 0.118 | 0.353 | 0.000 | 0.235 | 0.235 | 0.059 |
| 5.1-6.0 | 0.111 | 0.278 | 0.056 | 0.333 | 0.056 | 0.167 |
| 6.0-6.9 | 0.167 | 0.222 | 0.056 | 0.389 | 0.167 | 0.000 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2629)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.4815, support=54
- `2.4-3.3`: recall=0.2037, support=54
- `3.3-4.2`: recall=0.0926, support=54
- `4.2-5.1`: recall=0.2642, support=53
- `5.1-6.0`: recall=0.2453, support=53
- `6.0-6.9`: recall=0.2075, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.481 | 0.111 | 0.037 | 0.204 | 0.056 | 0.111 |
| 2.4-3.3 | 0.241 | 0.204 | 0.037 | 0.241 | 0.148 | 0.130 |
| 3.3-4.2 | 0.222 | 0.278 | 0.093 | 0.204 | 0.130 | 0.074 |
| 4.2-5.1 | 0.245 | 0.189 | 0.113 | 0.264 | 0.151 | 0.038 |
| 5.1-6.0 | 0.132 | 0.170 | 0.208 | 0.189 | 0.245 | 0.057 |
| 6.0-6.9 | 0.094 | 0.170 | 0.170 | 0.151 | 0.208 | 0.208 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1934)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3519, support=54
- `2.4-3.3`: recall=0.0370, support=54
- `3.3-4.2`: recall=0.2407, support=54
- `4.2-5.1`: recall=0.0755, support=53
- `5.1-6.0`: recall=0.2075, support=53
- `6.0-6.9`: recall=0.2830, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.352 | 0.111 | 0.037 | 0.111 | 0.204 | 0.185 |
| 2.4-3.3 | 0.278 | 0.037 | 0.167 | 0.074 | 0.241 | 0.204 |
| 3.3-4.2 | 0.222 | 0.019 | 0.241 | 0.074 | 0.333 | 0.111 |
| 4.2-5.1 | 0.226 | 0.019 | 0.208 | 0.075 | 0.302 | 0.170 |
| 5.1-6.0 | 0.226 | 0.038 | 0.226 | 0.019 | 0.208 | 0.283 |
| 6.0-6.9 | 0.170 | 0.075 | 0.132 | 0.038 | 0.302 | 0.283 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1702)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.2222, support=54
- `4.2-5.1`: recall=0.0189, support=53
- `5.1-6.0`: recall=0.3019, support=53
- `6.0-6.9`: recall=0.2453, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.056 | 0.167 | 0.037 | 0.167 | 0.352 |
| 2.4-3.3 | 0.148 | 0.093 | 0.167 | 0.056 | 0.185 | 0.352 |
| 3.3-4.2 | 0.130 | 0.074 | 0.222 | 0.000 | 0.259 | 0.315 |
| 4.2-5.1 | 0.094 | 0.019 | 0.283 | 0.019 | 0.283 | 0.302 |
| 5.1-6.0 | 0.132 | 0.038 | 0.264 | 0.019 | 0.302 | 0.245 |
| 6.0-6.9 | 0.094 | 0.057 | 0.321 | 0.000 | 0.283 | 0.245 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1698)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1296, support=54
- `2.4-3.3`: recall=0.1111, support=54
- `3.3-4.2`: recall=0.2963, support=54
- `4.2-5.1`: recall=0.0566, support=53
- `5.1-6.0`: recall=0.2264, support=53
- `6.0-6.9`: recall=0.1698, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.130 | 0.074 | 0.222 | 0.204 | 0.185 | 0.185 |
| 2.4-3.3 | 0.167 | 0.111 | 0.296 | 0.056 | 0.222 | 0.148 |
| 3.3-4.2 | 0.167 | 0.074 | 0.296 | 0.111 | 0.148 | 0.204 |
| 4.2-5.1 | 0.113 | 0.075 | 0.283 | 0.057 | 0.245 | 0.226 |
| 5.1-6.0 | 0.170 | 0.057 | 0.283 | 0.075 | 0.226 | 0.189 |
| 6.0-6.9 | 0.132 | 0.151 | 0.132 | 0.113 | 0.302 | 0.170 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1595)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0000, support=54
- `2.4-3.3`: recall=0.0185, support=54
- `3.3-4.2`: recall=0.0000, support=54
- `4.2-5.1`: recall=0.0000, support=53
- `5.1-6.0`: recall=0.8868, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.000 | 0.019 | 0.037 | 0.000 | 0.870 | 0.074 |
| 2.4-3.3 | 0.000 | 0.019 | 0.019 | 0.000 | 0.815 | 0.148 |
| 3.3-4.2 | 0.000 | 0.074 | 0.000 | 0.019 | 0.870 | 0.037 |
| 4.2-5.1 | 0.000 | 0.057 | 0.000 | 0.000 | 0.868 | 0.075 |
| 5.1-6.0 | 0.000 | 0.038 | 0.000 | 0.000 | 0.887 | 0.075 |
| 6.0-6.9 | 0.000 | 0.038 | 0.000 | 0.038 | 0.887 | 0.038 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1580)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2778, support=54
- `2.4-3.3`: recall=0.0926, support=54
- `3.3-4.2`: recall=0.0556, support=54
- `4.2-5.1`: recall=0.4717, support=53
- `5.1-6.0`: recall=0.0000, support=53
- `6.0-6.9`: recall=0.0377, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.278 | 0.093 | 0.019 | 0.556 | 0.019 | 0.037 |
| 2.4-3.3 | 0.259 | 0.093 | 0.000 | 0.444 | 0.111 | 0.093 |
| 3.3-4.2 | 0.407 | 0.130 | 0.056 | 0.389 | 0.000 | 0.019 |
| 4.2-5.1 | 0.396 | 0.038 | 0.000 | 0.472 | 0.057 | 0.038 |
| 5.1-6.0 | 0.491 | 0.057 | 0.000 | 0.415 | 0.000 | 0.038 |
| 6.0-6.9 | 0.396 | 0.075 | 0.038 | 0.434 | 0.019 | 0.038 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1423)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/group_holdout/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1481, support=54
- `2.4-3.3`: recall=0.0000, support=54
- `3.3-4.2`: recall=0.1667, support=54
- `4.2-5.1`: recall=0.0377, support=53
- `5.1-6.0`: recall=0.3774, support=53
- `6.0-6.9`: recall=0.1509, support=53

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.148 | 0.000 | 0.204 | 0.093 | 0.333 | 0.222 |
| 2.4-3.3 | 0.148 | 0.000 | 0.222 | 0.074 | 0.370 | 0.185 |
| 3.3-4.2 | 0.111 | 0.019 | 0.167 | 0.074 | 0.500 | 0.130 |
| 4.2-5.1 | 0.075 | 0.000 | 0.208 | 0.038 | 0.453 | 0.226 |
| 5.1-6.0 | 0.170 | 0.000 | 0.226 | 0.000 | 0.377 | 0.226 |
| 6.0-6.9 | 0.151 | 0.038 | 0.245 | 0.019 | 0.396 | 0.151 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2731)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.3529, support=17
- `4.2-5.1`: recall=0.3333, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.167 | 0.111 | 0.167 | 0.056 | 0.167 |
| 2.4-3.3 | 0.222 | 0.278 | 0.111 | 0.111 | 0.222 | 0.056 |
| 3.3-4.2 | 0.059 | 0.176 | 0.353 | 0.235 | 0.176 | 0.000 |
| 4.2-5.1 | 0.056 | 0.111 | 0.222 | 0.333 | 0.222 | 0.056 |
| 5.1-6.0 | 0.111 | 0.167 | 0.167 | 0.167 | 0.333 | 0.056 |
| 6.0-6.9 | 0.000 | 0.222 | 0.056 | 0.611 | 0.111 | 0.000 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.1852)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0588, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.3333, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.444 | 0.000 | 0.056 | 0.000 | 0.000 | 0.500 |
| 2.4-3.3 | 0.389 | 0.000 | 0.056 | 0.056 | 0.167 | 0.333 |
| 3.3-4.2 | 0.353 | 0.000 | 0.059 | 0.000 | 0.294 | 0.294 |
| 4.2-5.1 | 0.222 | 0.000 | 0.111 | 0.000 | 0.389 | 0.278 |
| 5.1-6.0 | 0.111 | 0.000 | 0.333 | 0.056 | 0.278 | 0.222 |
| 6.0-6.9 | 0.056 | 0.000 | 0.278 | 0.056 | 0.278 | 0.333 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.1759)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.5000, support=18
- `6.0-6.9`: recall=0.2222, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.111 | 0.000 | 0.000 | 0.500 | 0.056 |
| 2.4-3.3 | 0.389 | 0.000 | 0.000 | 0.111 | 0.500 | 0.000 |
| 3.3-4.2 | 0.353 | 0.059 | 0.000 | 0.000 | 0.471 | 0.118 |
| 4.2-5.1 | 0.000 | 0.167 | 0.000 | 0.000 | 0.500 | 0.333 |
| 5.1-6.0 | 0.056 | 0.167 | 0.000 | 0.000 | 0.500 | 0.278 |
| 6.0-6.9 | 0.000 | 0.278 | 0.000 | 0.000 | 0.500 | 0.222 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.1667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.0000, support=18
- `2.4-3.3`: recall=0.0000, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=1.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 2.4-3.3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3.3-4.2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 4.2-5.1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5.1-6.0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| 6.0-6.9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.1296)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.2222, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.0000, support=17
- `4.2-5.1`: recall=0.5000, support=18
- `5.1-6.0`: recall=0.0000, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.222 | 0.222 | 0.000 | 0.500 | 0.000 | 0.056 |
| 2.4-3.3 | 0.444 | 0.056 | 0.000 | 0.500 | 0.000 | 0.000 |
| 3.3-4.2 | 0.412 | 0.000 | 0.000 | 0.471 | 0.000 | 0.118 |
| 4.2-5.1 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 5.1-6.0 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |
| 6.0-6.9 | 0.500 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.1204)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3889, support=18
- `6.0-6.9`: recall=0.0000, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.111 | 0.111 | 0.056 | 0.111 | 0.278 | 0.333 |
| 2.4-3.3 | 0.333 | 0.056 | 0.167 | 0.000 | 0.222 | 0.222 |
| 3.3-4.2 | 0.235 | 0.059 | 0.176 | 0.000 | 0.529 | 0.000 |
| 4.2-5.1 | 0.000 | 0.167 | 0.222 | 0.000 | 0.500 | 0.111 |
| 5.1-6.0 | 0.167 | 0.333 | 0.056 | 0.000 | 0.389 | 0.056 |
| 6.0-6.9 | 0.111 | 0.333 | 0.000 | 0.056 | 0.500 | 0.000 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.1204)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/loso/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1111, support=18
- `2.4-3.3`: recall=0.0556, support=18
- `3.3-4.2`: recall=0.1765, support=17
- `4.2-5.1`: recall=0.0000, support=18
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.111 | 0.167 | 0.000 | 0.222 | 0.167 | 0.333 |
| 2.4-3.3 | 0.167 | 0.056 | 0.278 | 0.000 | 0.222 | 0.278 |
| 3.3-4.2 | 0.059 | 0.294 | 0.176 | 0.000 | 0.412 | 0.059 |
| 4.2-5.1 | 0.056 | 0.333 | 0.111 | 0.000 | 0.389 | 0.111 |
| 5.1-6.0 | 0.000 | 0.389 | 0.111 | 0.000 | 0.333 | 0.167 |
| 6.0-6.9 | 0.056 | 0.444 | 0.000 | 0.000 | 0.444 | 0.056 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3833)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/knn_none.png`

### Class Recall
- `1.5-2.4`: recall=0.4444, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.6111, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.444 | 0.056 | 0.167 | 0.056 | 0.167 | 0.111 |
| 2.4-3.3 | 0.111 | 0.278 | 0.278 | 0.222 | 0.000 | 0.111 |
| 3.3-4.2 | 0.056 | 0.222 | 0.278 | 0.167 | 0.167 | 0.111 |
| 4.2-5.1 | 0.000 | 0.059 | 0.059 | 0.353 | 0.235 | 0.294 |
| 5.1-6.0 | 0.111 | 0.056 | 0.056 | 0.000 | 0.611 | 0.167 |
| 6.0-6.9 | 0.056 | 0.167 | 0.056 | 0.222 | 0.222 | 0.278 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3667)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/rf_none.png`

### Class Recall
- `1.5-2.4`: recall=0.5556, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.6667, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.556 | 0.167 | 0.111 | 0.000 | 0.056 | 0.111 |
| 2.4-3.3 | 0.222 | 0.333 | 0.278 | 0.167 | 0.000 | 0.000 |
| 3.3-4.2 | 0.056 | 0.222 | 0.278 | 0.111 | 0.222 | 0.111 |
| 4.2-5.1 | 0.118 | 0.059 | 0.176 | 0.235 | 0.294 | 0.118 |
| 5.1-6.0 | 0.056 | 0.000 | 0.056 | 0.111 | 0.667 | 0.111 |
| 6.0-6.9 | 0.056 | 0.222 | 0.111 | 0.056 | 0.389 | 0.167 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/mlp_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3333, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.2778, support=18
- `4.2-5.1`: recall=0.2353, support=17
- `5.1-6.0`: recall=0.4444, support=18
- `6.0-6.9`: recall=0.2778, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.333 | 0.167 | 0.278 | 0.056 | 0.167 | 0.000 |
| 2.4-3.3 | 0.278 | 0.278 | 0.278 | 0.056 | 0.000 | 0.111 |
| 3.3-4.2 | 0.056 | 0.056 | 0.278 | 0.222 | 0.222 | 0.167 |
| 4.2-5.1 | 0.059 | 0.235 | 0.059 | 0.235 | 0.294 | 0.118 |
| 5.1-6.0 | 0.056 | 0.056 | 0.222 | 0.167 | 0.444 | 0.056 |
| 6.0-6.9 | 0.167 | 0.056 | 0.167 | 0.111 | 0.222 | 0.278 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `1.5-2.4`: recall=0.5556, support=18
- `2.4-3.3`: recall=0.3889, support=18
- `3.3-4.2`: recall=0.2222, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.1667, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.556 | 0.222 | 0.111 | 0.056 | 0.056 | 0.000 |
| 2.4-3.3 | 0.222 | 0.389 | 0.167 | 0.111 | 0.056 | 0.056 |
| 3.3-4.2 | 0.111 | 0.056 | 0.222 | 0.111 | 0.111 | 0.389 |
| 4.2-5.1 | 0.118 | 0.118 | 0.059 | 0.118 | 0.353 | 0.235 |
| 5.1-6.0 | 0.167 | 0.056 | 0.167 | 0.167 | 0.333 | 0.111 |
| 6.0-6.9 | 0.222 | 0.056 | 0.222 | 0.056 | 0.278 | 0.167 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2917)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/svm_none.png`

### Class Recall
- `1.5-2.4`: recall=0.5000, support=18
- `2.4-3.3`: recall=0.2778, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.3529, support=17
- `5.1-6.0`: recall=0.3333, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.500 | 0.111 | 0.167 | 0.167 | 0.000 | 0.056 |
| 2.4-3.3 | 0.167 | 0.278 | 0.111 | 0.389 | 0.056 | 0.000 |
| 3.3-4.2 | 0.167 | 0.222 | 0.167 | 0.278 | 0.056 | 0.111 |
| 4.2-5.1 | 0.118 | 0.118 | 0.176 | 0.353 | 0.235 | 0.000 |
| 5.1-6.0 | 0.111 | 0.000 | 0.056 | 0.389 | 0.333 | 0.111 |
| 6.0-6.9 | 0.167 | 0.000 | 0.056 | 0.444 | 0.278 | 0.056 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `1.5-2.4`: recall=0.1667, support=18
- `2.4-3.3`: recall=0.3333, support=18
- `3.3-4.2`: recall=0.0556, support=18
- `4.2-5.1`: recall=0.1765, support=17
- `5.1-6.0`: recall=0.1111, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.167 | 0.333 | 0.167 | 0.167 | 0.111 | 0.056 |
| 2.4-3.3 | 0.111 | 0.333 | 0.111 | 0.278 | 0.111 | 0.056 |
| 3.3-4.2 | 0.111 | 0.333 | 0.056 | 0.222 | 0.167 | 0.111 |
| 4.2-5.1 | 0.176 | 0.353 | 0.059 | 0.176 | 0.176 | 0.059 |
| 5.1-6.0 | 0.111 | 0.278 | 0.000 | 0.278 | 0.111 | 0.222 |
| 6.0-6.9 | 0.167 | 0.222 | 0.056 | 0.333 | 0.167 | 0.056 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.1750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_omit_easiest/pupil/within_participant/logreg_none.png`

### Class Recall
- `1.5-2.4`: recall=0.3889, support=18
- `2.4-3.3`: recall=0.1111, support=18
- `3.3-4.2`: recall=0.1667, support=18
- `4.2-5.1`: recall=0.1176, support=17
- `5.1-6.0`: recall=0.2778, support=18
- `6.0-6.9`: recall=0.0556, support=18

### Confusion (row-normalized)
| true\pred | 1.5-2.4 | 2.4-3.3 | 3.3-4.2 | 4.2-5.1 | 5.1-6.0 | 6.0-6.9 |
|---|---|---|---|---|---|---|
| 1.5-2.4 | 0.389 | 0.167 | 0.167 | 0.167 | 0.000 | 0.111 |
| 2.4-3.3 | 0.444 | 0.111 | 0.333 | 0.111 | 0.000 | 0.000 |
| 3.3-4.2 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 |
| 4.2-5.1 | 0.235 | 0.118 | 0.118 | 0.118 | 0.176 | 0.235 |
| 5.1-6.0 | 0.056 | 0.056 | 0.167 | 0.167 | 0.278 | 0.278 |
| 6.0-6.9 | 0.278 | 0.000 | 0.222 | 0.111 | 0.333 | 0.056 |


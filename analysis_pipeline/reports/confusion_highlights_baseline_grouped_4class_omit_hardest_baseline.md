# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_grouped_4class_omit_hardest_baseline.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2801)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0270, support=37
- `low_1_2`: recall=0.3738, support=107
- `mid_3_4`: recall=0.4904, support=104
- `high_5_6`: recall=0.2233, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.027 | 0.243 | 0.622 | 0.108 |
| low_1_2 | 0.047 | 0.374 | 0.467 | 0.112 |
| mid_3_4 | 0.048 | 0.260 | 0.490 | 0.202 |
| high_5_6 | 0.049 | 0.233 | 0.495 | 0.223 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2735)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.5946, support=37
- `low_1_2`: recall=0.2150, support=107
- `mid_3_4`: recall=0.1058, support=104
- `high_5_6`: recall=0.2621, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.595 | 0.162 | 0.081 | 0.162 |
| low_1_2 | 0.467 | 0.215 | 0.084 | 0.234 |
| mid_3_4 | 0.452 | 0.221 | 0.106 | 0.221 |
| high_5_6 | 0.398 | 0.184 | 0.155 | 0.262 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2658)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `low_1_2`: recall=0.3458, support=107
- `mid_3_4`: recall=0.2692, support=104
- `high_5_6`: recall=0.3981, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.054 | 0.270 | 0.432 | 0.243 |
| low_1_2 | 0.103 | 0.346 | 0.252 | 0.299 |
| mid_3_4 | 0.077 | 0.298 | 0.269 | 0.356 |
| high_5_6 | 0.097 | 0.243 | 0.262 | 0.398 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2582)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `low_1_2`: recall=0.3364, support=107
- `mid_3_4`: recall=0.1731, support=104
- `high_5_6`: recall=0.4272, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.054 | 0.324 | 0.270 | 0.351 |
| low_1_2 | 0.084 | 0.336 | 0.187 | 0.393 |
| mid_3_4 | 0.154 | 0.240 | 0.173 | 0.433 |
| high_5_6 | 0.126 | 0.252 | 0.194 | 0.427 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.2429)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `low_1_2`: recall=0.1495, support=107
- `mid_3_4`: recall=0.1827, support=104
- `high_5_6`: recall=0.3495, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.270 | 0.081 | 0.486 | 0.162 |
| low_1_2 | 0.393 | 0.150 | 0.224 | 0.234 |
| mid_3_4 | 0.423 | 0.096 | 0.183 | 0.298 |
| high_5_6 | 0.359 | 0.087 | 0.204 | 0.350 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2419)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `low_1_2`: recall=0.3551, support=107
- `mid_3_4`: recall=0.1442, support=104
- `high_5_6`: recall=0.3592, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.135 | 0.324 | 0.243 | 0.297 |
| low_1_2 | 0.159 | 0.355 | 0.150 | 0.336 |
| mid_3_4 | 0.154 | 0.365 | 0.144 | 0.337 |
| high_5_6 | 0.117 | 0.379 | 0.146 | 0.359 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2235)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.2150, support=107
- `mid_3_4`: recall=0.0577, support=104
- `high_5_6`: recall=0.3689, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.189 | 0.297 | 0.189 |
| low_1_2 | 0.383 | 0.215 | 0.121 | 0.280 |
| mid_3_4 | 0.394 | 0.231 | 0.058 | 0.317 |
| high_5_6 | 0.369 | 0.107 | 0.155 | 0.369 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3282)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2`: recall=0.2500, support=32
- `mid_3_4`: recall=0.0294, support=34
- `high_5_6`: recall=0.3611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.000 | 0.143 |
| low_1_2 | 0.500 | 0.250 | 0.062 | 0.188 |
| mid_3_4 | 0.500 | 0.235 | 0.029 | 0.235 |
| high_5_6 | 0.444 | 0.111 | 0.083 | 0.361 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3233)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.5625, support=32
- `mid_3_4`: recall=0.3235, support=34
- `high_5_6`: recall=0.3611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.429 | 0.143 | 0.429 |
| low_1_2 | 0.062 | 0.562 | 0.156 | 0.219 |
| mid_3_4 | 0.118 | 0.294 | 0.324 | 0.265 |
| high_5_6 | 0.028 | 0.278 | 0.333 | 0.361 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3193)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.5000, support=32
- `mid_3_4`: recall=0.1471, support=34
- `high_5_6`: recall=0.4444, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.500 | 0.071 | 0.286 |
| low_1_2 | 0.156 | 0.500 | 0.125 | 0.219 |
| mid_3_4 | 0.029 | 0.471 | 0.147 | 0.353 |
| high_5_6 | 0.028 | 0.333 | 0.194 | 0.444 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3047)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.3750, support=32
- `mid_3_4`: recall=0.2941, support=34
- `high_5_6`: recall=0.5278, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.429 | 0.214 | 0.357 |
| low_1_2 | 0.125 | 0.375 | 0.281 | 0.219 |
| mid_3_4 | 0.176 | 0.206 | 0.294 | 0.324 |
| high_5_6 | 0.028 | 0.139 | 0.306 | 0.528 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2937)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2`: recall=0.1875, support=32
- `mid_3_4`: recall=0.0294, support=34
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.643 | 0.143 | 0.000 | 0.214 |
| low_1_2 | 0.625 | 0.188 | 0.094 | 0.094 |
| mid_3_4 | 0.647 | 0.118 | 0.029 | 0.206 |
| high_5_6 | 0.361 | 0.139 | 0.194 | 0.306 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2778)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.3438, support=32
- `mid_3_4`: recall=0.2941, support=34
- `high_5_6`: recall=0.4444, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.143 | 0.286 | 0.571 |
| low_1_2 | 0.031 | 0.344 | 0.344 | 0.281 |
| mid_3_4 | 0.059 | 0.265 | 0.294 | 0.382 |
| high_5_6 | 0.028 | 0.222 | 0.306 | 0.444 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2495)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2`: recall=0.2500, support=32
- `mid_3_4`: recall=0.5000, support=34
- `high_5_6`: recall=0.1667, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.071 | 0.071 | 0.571 | 0.286 |
| low_1_2 | 0.188 | 0.250 | 0.375 | 0.188 |
| mid_3_4 | 0.147 | 0.265 | 0.500 | 0.088 |
| high_5_6 | 0.111 | 0.194 | 0.528 | 0.167 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3792)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.2778, support=36
- `high_5_6`: recall=0.5556, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.000 | 0.286 |
| low_1_2 | 0.083 | 0.389 | 0.167 | 0.361 |
| mid_3_4 | 0.056 | 0.278 | 0.278 | 0.389 |
| high_5_6 | 0.056 | 0.250 | 0.139 | 0.556 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3479)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.5278, support=36
- `mid_3_4`: recall=0.1111, support=36
- `high_5_6`: recall=0.5000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.286 | 0.000 | 0.500 |
| low_1_2 | 0.056 | 0.528 | 0.111 | 0.306 |
| mid_3_4 | 0.056 | 0.333 | 0.111 | 0.500 |
| high_5_6 | 0.056 | 0.306 | 0.139 | 0.500 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3375)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3889, support=36
- `mid_3_4`: recall=0.3056, support=36
- `high_5_6`: recall=0.3333, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.357 | 0.071 | 0.286 |
| low_1_2 | 0.167 | 0.389 | 0.194 | 0.250 |
| mid_3_4 | 0.083 | 0.222 | 0.306 | 0.389 |
| high_5_6 | 0.194 | 0.194 | 0.278 | 0.333 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3354)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.3333, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.3333, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.214 | 0.071 |
| low_1_2 | 0.167 | 0.333 | 0.167 | 0.333 |
| mid_3_4 | 0.139 | 0.222 | 0.361 | 0.278 |
| high_5_6 | 0.194 | 0.194 | 0.278 | 0.333 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3208)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.3056, support=36
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.357 | 0.143 | 0.214 |
| low_1_2 | 0.139 | 0.306 | 0.306 | 0.250 |
| mid_3_4 | 0.111 | 0.306 | 0.306 | 0.278 |
| high_5_6 | 0.111 | 0.222 | 0.361 | 0.306 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3187)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.2500, support=36
- `high_5_6`: recall=0.4722, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.143 | 0.286 |
| low_1_2 | 0.222 | 0.306 | 0.222 | 0.250 |
| mid_3_4 | 0.222 | 0.306 | 0.250 | 0.222 |
| high_5_6 | 0.167 | 0.222 | 0.139 | 0.472 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.3021)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/ecg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.3056, support=36
- `mid_3_4`: recall=0.1944, support=36
- `high_5_6`: recall=0.3611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.071 | 0.214 |
| low_1_2 | 0.222 | 0.306 | 0.194 | 0.278 |
| mid_3_4 | 0.139 | 0.278 | 0.194 | 0.389 |
| high_5_6 | 0.167 | 0.250 | 0.222 | 0.361 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3712)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `low_1_2`: recall=0.4299, support=107
- `mid_3_4`: recall=0.4327, support=104
- `high_5_6`: recall=0.3398, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.270 | 0.135 | 0.432 | 0.162 |
| low_1_2 | 0.140 | 0.430 | 0.271 | 0.159 |
| mid_3_4 | 0.115 | 0.202 | 0.433 | 0.250 |
| high_5_6 | 0.126 | 0.146 | 0.388 | 0.340 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3697)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.3925, support=107
- `mid_3_4`: recall=0.2019, support=104
- `high_5_6`: recall=0.5340, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.135 | 0.162 | 0.378 |
| low_1_2 | 0.215 | 0.393 | 0.121 | 0.271 |
| mid_3_4 | 0.202 | 0.192 | 0.202 | 0.404 |
| high_5_6 | 0.194 | 0.097 | 0.175 | 0.534 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3439)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2`: recall=0.3084, support=107
- `mid_3_4`: recall=0.2981, support=104
- `high_5_6`: recall=0.4466, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.324 | 0.243 | 0.216 | 0.216 |
| low_1_2 | 0.224 | 0.308 | 0.271 | 0.196 |
| mid_3_4 | 0.077 | 0.192 | 0.298 | 0.433 |
| high_5_6 | 0.155 | 0.117 | 0.282 | 0.447 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3376)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `low_1_2`: recall=0.3084, support=107
- `mid_3_4`: recall=0.5000, support=104
- `high_5_6`: recall=0.4078, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.216 | 0.108 | 0.459 | 0.216 |
| low_1_2 | 0.075 | 0.308 | 0.430 | 0.187 |
| mid_3_4 | 0.029 | 0.135 | 0.500 | 0.337 |
| high_5_6 | 0.049 | 0.078 | 0.466 | 0.408 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3247)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `low_1_2`: recall=0.4673, support=107
- `mid_3_4`: recall=0.3942, support=104
- `high_5_6`: recall=0.2816, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.108 | 0.378 | 0.405 | 0.108 |
| low_1_2 | 0.131 | 0.467 | 0.252 | 0.150 |
| mid_3_4 | 0.163 | 0.192 | 0.394 | 0.250 |
| high_5_6 | 0.126 | 0.233 | 0.359 | 0.282 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3097)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `low_1_2`: recall=0.0374, support=107
- `mid_3_4`: recall=0.7596, support=104
- `high_5_6`: recall=0.2427, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.216 | 0.027 | 0.757 | 0.000 |
| low_1_2 | 0.065 | 0.037 | 0.776 | 0.121 |
| mid_3_4 | 0.087 | 0.029 | 0.760 | 0.125 |
| high_5_6 | 0.039 | 0.010 | 0.709 | 0.243 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2417)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2162, support=37
- `low_1_2`: recall=0.1682, support=107
- `mid_3_4`: recall=0.2692, support=104
- `high_5_6`: recall=0.2621, support=103

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.216 | 0.243 | 0.297 | 0.243 |
| low_1_2 | 0.336 | 0.168 | 0.290 | 0.206 |
| mid_3_4 | 0.279 | 0.106 | 0.269 | 0.346 |
| high_5_6 | 0.320 | 0.126 | 0.291 | 0.262 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.4252)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2`: recall=0.8750, support=32
- `mid_3_4`: recall=0.1471, support=34
- `high_5_6`: recall=0.0278, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.643 | 0.357 | 0.000 | 0.000 |
| low_1_2 | 0.031 | 0.875 | 0.094 | 0.000 |
| mid_3_4 | 0.088 | 0.765 | 0.147 | 0.000 |
| high_5_6 | 0.083 | 0.528 | 0.361 | 0.028 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3596)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.5938, support=32
- `mid_3_4`: recall=0.3529, support=34
- `high_5_6`: recall=0.1389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.143 | 0.214 |
| low_1_2 | 0.031 | 0.594 | 0.219 | 0.156 |
| mid_3_4 | 0.059 | 0.529 | 0.353 | 0.059 |
| high_5_6 | 0.000 | 0.333 | 0.528 | 0.139 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3451)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.8125, support=32
- `mid_3_4`: recall=0.1176, support=34
- `high_5_6`: recall=0.2500, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.571 | 0.214 | 0.000 |
| low_1_2 | 0.031 | 0.812 | 0.125 | 0.031 |
| mid_3_4 | 0.029 | 0.618 | 0.118 | 0.235 |
| high_5_6 | 0.000 | 0.222 | 0.528 | 0.250 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3244)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2`: recall=0.9062, support=32
- `mid_3_4`: recall=0.0294, support=34
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.071 | 0.857 | 0.071 | 0.000 |
| low_1_2 | 0.000 | 0.906 | 0.031 | 0.062 |
| mid_3_4 | 0.000 | 0.794 | 0.029 | 0.176 |
| high_5_6 | 0.000 | 0.639 | 0.056 | 0.306 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3041)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.6875, support=32
- `mid_3_4`: recall=0.4118, support=34
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.643 | 0.214 | 0.000 |
| low_1_2 | 0.000 | 0.688 | 0.312 | 0.000 |
| mid_3_4 | 0.000 | 0.588 | 0.412 | 0.000 |
| high_5_6 | 0.000 | 0.278 | 0.722 | 0.000 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3006)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.5000, support=32
- `mid_3_4`: recall=0.3235, support=34
- `high_5_6`: recall=0.0833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.500 | 0.214 | 0.000 |
| low_1_2 | 0.156 | 0.500 | 0.281 | 0.062 |
| mid_3_4 | 0.147 | 0.382 | 0.324 | 0.147 |
| high_5_6 | 0.167 | 0.556 | 0.194 | 0.083 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2960)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.8125, support=32
- `mid_3_4`: recall=0.1471, support=34
- `high_5_6`: recall=0.0833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.714 | 0.071 | 0.071 |
| low_1_2 | 0.031 | 0.812 | 0.031 | 0.125 |
| mid_3_4 | 0.000 | 0.559 | 0.147 | 0.294 |
| high_5_6 | 0.000 | 0.556 | 0.361 | 0.083 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.5292)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.5278, support=36
- `mid_3_4`: recall=0.5556, support=36
- `high_5_6`: recall=0.5833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.143 | 0.214 | 0.071 |
| low_1_2 | 0.000 | 0.528 | 0.250 | 0.222 |
| mid_3_4 | 0.000 | 0.222 | 0.556 | 0.222 |
| high_5_6 | 0.083 | 0.083 | 0.250 | 0.583 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5062)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.5278, support=36
- `high_5_6`: recall=0.6389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.071 | 0.286 |
| low_1_2 | 0.056 | 0.472 | 0.250 | 0.222 |
| mid_3_4 | 0.000 | 0.250 | 0.528 | 0.222 |
| high_5_6 | 0.028 | 0.111 | 0.222 | 0.639 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.4812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.5000, support=36
- `mid_3_4`: recall=0.4722, support=36
- `high_5_6`: recall=0.6111, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.143 | 0.143 |
| low_1_2 | 0.056 | 0.500 | 0.222 | 0.222 |
| mid_3_4 | 0.000 | 0.194 | 0.472 | 0.333 |
| high_5_6 | 0.000 | 0.083 | 0.306 | 0.611 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.4521)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.4444, support=36
- `high_5_6`: recall=0.5556, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.143 | 0.143 |
| low_1_2 | 0.083 | 0.444 | 0.194 | 0.278 |
| mid_3_4 | 0.028 | 0.306 | 0.444 | 0.222 |
| high_5_6 | 0.000 | 0.111 | 0.333 | 0.556 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.4333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2`: recall=0.5000, support=36
- `mid_3_4`: recall=0.3333, support=36
- `high_5_6`: recall=0.6389, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.286 | 0.571 | 0.000 | 0.143 |
| low_1_2 | 0.111 | 0.500 | 0.194 | 0.194 |
| mid_3_4 | 0.056 | 0.361 | 0.333 | 0.250 |
| high_5_6 | 0.028 | 0.083 | 0.250 | 0.639 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3750)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.3611, support=36
- `mid_3_4`: recall=0.3056, support=36
- `high_5_6`: recall=0.7500, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.286 | 0.286 | 0.286 |
| low_1_2 | 0.028 | 0.361 | 0.194 | 0.417 |
| mid_3_4 | 0.000 | 0.222 | 0.306 | 0.472 |
| high_5_6 | 0.000 | 0.083 | 0.167 | 0.750 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3604)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2`: recall=0.5000, support=36
- `mid_3_4`: recall=0.3056, support=36
- `high_5_6`: recall=0.4722, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.214 | 0.214 |
| low_1_2 | 0.083 | 0.500 | 0.167 | 0.250 |
| mid_3_4 | 0.056 | 0.389 | 0.306 | 0.250 |
| high_5_6 | 0.056 | 0.306 | 0.167 | 0.472 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3439)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `low_1_2`: recall=0.5185, support=108
- `mid_3_4`: recall=0.2593, support=108
- `high_5_6`: recall=0.4434, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.132 | 0.500 | 0.184 | 0.184 |
| low_1_2 | 0.204 | 0.519 | 0.176 | 0.102 |
| mid_3_4 | 0.120 | 0.352 | 0.259 | 0.269 |
| high_5_6 | 0.066 | 0.255 | 0.236 | 0.443 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3306)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `low_1_2`: recall=0.4537, support=108
- `mid_3_4`: recall=0.3981, support=108
- `high_5_6`: recall=0.3774, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.105 | 0.289 | 0.316 | 0.289 |
| low_1_2 | 0.120 | 0.454 | 0.167 | 0.259 |
| mid_3_4 | 0.065 | 0.176 | 0.398 | 0.361 |
| high_5_6 | 0.075 | 0.198 | 0.349 | 0.377 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3076)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `low_1_2`: recall=0.3796, support=108
- `mid_3_4`: recall=0.3889, support=108
- `high_5_6`: recall=0.3868, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.079 | 0.395 | 0.316 | 0.211 |
| low_1_2 | 0.074 | 0.380 | 0.231 | 0.315 |
| mid_3_4 | 0.056 | 0.222 | 0.389 | 0.333 |
| high_5_6 | 0.038 | 0.217 | 0.358 | 0.387 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2986)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1579, support=38
- `low_1_2`: recall=0.3519, support=108
- `mid_3_4`: recall=0.2870, support=108
- `high_5_6`: recall=0.4434, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.158 | 0.342 | 0.289 | 0.211 |
| low_1_2 | 0.157 | 0.352 | 0.250 | 0.241 |
| mid_3_4 | 0.074 | 0.278 | 0.287 | 0.361 |
| high_5_6 | 0.047 | 0.236 | 0.274 | 0.443 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2812)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2`: recall=0.2315, support=108
- `mid_3_4`: recall=0.2407, support=108
- `high_5_6`: recall=0.3679, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.184 | 0.263 | 0.237 | 0.316 |
| low_1_2 | 0.269 | 0.231 | 0.241 | 0.259 |
| mid_3_4 | 0.231 | 0.250 | 0.241 | 0.278 |
| high_5_6 | 0.283 | 0.189 | 0.160 | 0.368 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2702)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2`: recall=0.3333, support=108
- `mid_3_4`: recall=0.0370, support=108
- `high_5_6`: recall=0.5377, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.184 | 0.368 | 0.026 | 0.421 |
| low_1_2 | 0.065 | 0.333 | 0.037 | 0.565 |
| mid_3_4 | 0.093 | 0.343 | 0.037 | 0.528 |
| high_5_6 | 0.066 | 0.349 | 0.047 | 0.538 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2597)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.0789, support=38
- `low_1_2`: recall=0.0463, support=108
- `mid_3_4`: recall=0.0556, support=108
- `high_5_6`: recall=0.8679, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.079 | 0.132 | 0.000 | 0.789 |
| low_1_2 | 0.139 | 0.046 | 0.046 | 0.769 |
| mid_3_4 | 0.139 | 0.056 | 0.056 | 0.750 |
| high_5_6 | 0.066 | 0.028 | 0.038 | 0.868 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4613)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.1143, support=35
- `high_5_6`: recall=0.8611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.071 | 0.000 | 0.500 |
| low_1_2 | 0.000 | 0.444 | 0.028 | 0.528 |
| mid_3_4 | 0.057 | 0.171 | 0.114 | 0.657 |
| high_5_6 | 0.000 | 0.028 | 0.111 | 0.861 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3512)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2`: recall=0.5278, support=36
- `mid_3_4`: recall=0.0286, support=35
- `high_5_6`: recall=0.7778, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.071 | 0.357 | 0.071 | 0.500 |
| low_1_2 | 0.000 | 0.528 | 0.000 | 0.472 |
| mid_3_4 | 0.000 | 0.343 | 0.029 | 0.629 |
| high_5_6 | 0.000 | 0.139 | 0.083 | 0.778 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.2986)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.1714, support=35
- `high_5_6`: recall=0.5833, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.143 | 0.357 | 0.500 |
| low_1_2 | 0.000 | 0.444 | 0.083 | 0.472 |
| mid_3_4 | 0.000 | 0.314 | 0.171 | 0.514 |
| high_5_6 | 0.000 | 0.056 | 0.361 | 0.583 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2886)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.3333, support=36
- `mid_3_4`: recall=0.4000, support=35
- `high_5_6`: recall=0.2778, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.214 | 0.286 | 0.357 |
| low_1_2 | 0.139 | 0.333 | 0.306 | 0.222 |
| mid_3_4 | 0.029 | 0.257 | 0.400 | 0.314 |
| high_5_6 | 0.000 | 0.222 | 0.500 | 0.278 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2609)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.1714, support=35
- `high_5_6`: recall=0.3333, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.071 | 0.571 | 0.214 | 0.143 |
| low_1_2 | 0.028 | 0.472 | 0.194 | 0.306 |
| mid_3_4 | 0.029 | 0.314 | 0.171 | 0.486 |
| high_5_6 | 0.056 | 0.194 | 0.417 | 0.333 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2609)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.429 | 0.000 | 0.000 |
| low_1_2 | 0.528 | 0.472 | 0.000 | 0.000 |
| mid_3_4 | 0.486 | 0.514 | 0.000 | 0.000 |
| high_5_6 | 0.500 | 0.500 | 0.000 | 0.000 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=1.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 |
| low_1_2 | 0.000 | 1.000 | 0.000 | 0.000 |
| mid_3_4 | 0.000 | 1.000 | 0.000 | 0.000 |
| high_5_6 | 0.000 | 1.000 | 0.000 | 0.000 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.6292)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.8571, support=14
- `low_1_2`: recall=0.6667, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.6571, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.857 | 0.071 | 0.071 | 0.000 |
| low_1_2 | 0.056 | 0.667 | 0.194 | 0.083 |
| mid_3_4 | 0.028 | 0.194 | 0.361 | 0.417 |
| high_5_6 | 0.000 | 0.114 | 0.229 | 0.657 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.5875)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2`: recall=0.6111, support=36
- `mid_3_4`: recall=0.4167, support=36
- `high_5_6`: recall=0.6571, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.714 | 0.071 | 0.214 | 0.000 |
| low_1_2 | 0.139 | 0.611 | 0.111 | 0.139 |
| mid_3_4 | 0.028 | 0.250 | 0.417 | 0.306 |
| high_5_6 | 0.029 | 0.143 | 0.171 | 0.657 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5354)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.6667, support=36
- `mid_3_4`: recall=0.3889, support=36
- `high_5_6`: recall=0.5714, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.214 | 0.000 |
| low_1_2 | 0.028 | 0.667 | 0.167 | 0.139 |
| mid_3_4 | 0.028 | 0.278 | 0.389 | 0.306 |
| high_5_6 | 0.000 | 0.143 | 0.286 | 0.571 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.5146)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2`: recall=0.5556, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.4857, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.143 | 0.000 |
| low_1_2 | 0.083 | 0.556 | 0.194 | 0.167 |
| mid_3_4 | 0.056 | 0.222 | 0.361 | 0.361 |
| high_5_6 | 0.000 | 0.171 | 0.343 | 0.486 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.4937)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.4444, support=36
- `high_5_6`: recall=0.6000, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.143 | 0.357 | 0.000 |
| low_1_2 | 0.056 | 0.472 | 0.222 | 0.250 |
| mid_3_4 | 0.028 | 0.083 | 0.444 | 0.444 |
| high_5_6 | 0.000 | 0.114 | 0.286 | 0.600 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.4771)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.5278, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.5714, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.286 | 0.214 | 0.000 |
| low_1_2 | 0.083 | 0.528 | 0.222 | 0.167 |
| mid_3_4 | 0.139 | 0.222 | 0.361 | 0.278 |
| high_5_6 | 0.086 | 0.143 | 0.200 | 0.571 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.4229)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.3333, support=36
- `mid_3_4`: recall=0.4444, support=36
- `high_5_6`: recall=0.4857, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.214 | 0.143 |
| low_1_2 | 0.139 | 0.333 | 0.333 | 0.194 |
| mid_3_4 | 0.194 | 0.083 | 0.444 | 0.278 |
| high_5_6 | 0.171 | 0.057 | 0.286 | 0.486 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3272)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2368, support=38
- `low_1_2`: recall=0.2500, support=108
- `mid_3_4`: recall=0.1944, support=108
- `high_5_6`: recall=0.6132, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.237 | 0.132 | 0.211 | 0.421 |
| low_1_2 | 0.167 | 0.250 | 0.306 | 0.278 |
| mid_3_4 | 0.167 | 0.046 | 0.194 | 0.593 |
| high_5_6 | 0.113 | 0.057 | 0.217 | 0.613 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3241)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `low_1_2`: recall=0.5833, support=108
- `mid_3_4`: recall=0.1759, support=108
- `high_5_6`: recall=0.5094, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.026 | 0.316 | 0.263 | 0.395 |
| low_1_2 | 0.019 | 0.583 | 0.102 | 0.296 |
| mid_3_4 | 0.037 | 0.315 | 0.176 | 0.472 |
| high_5_6 | 0.066 | 0.217 | 0.208 | 0.509 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3123)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2368, support=38
- `low_1_2`: recall=0.4167, support=108
- `mid_3_4`: recall=0.1852, support=108
- `high_5_6`: recall=0.4057, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.237 | 0.263 | 0.105 | 0.395 |
| low_1_2 | 0.278 | 0.417 | 0.176 | 0.130 |
| mid_3_4 | 0.241 | 0.278 | 0.185 | 0.296 |
| high_5_6 | 0.292 | 0.132 | 0.170 | 0.406 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3076)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0526, support=38
- `low_1_2`: recall=0.4630, support=108
- `mid_3_4`: recall=0.3611, support=108
- `high_5_6`: recall=0.3396, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.053 | 0.474 | 0.316 | 0.158 |
| low_1_2 | 0.019 | 0.463 | 0.278 | 0.241 |
| mid_3_4 | 0.028 | 0.296 | 0.361 | 0.315 |
| high_5_6 | 0.009 | 0.236 | 0.415 | 0.340 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3070)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `low_1_2`: recall=0.4630, support=108
- `mid_3_4`: recall=0.2593, support=108
- `high_5_6`: recall=0.3585, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.132 | 0.447 | 0.132 | 0.289 |
| low_1_2 | 0.056 | 0.463 | 0.120 | 0.361 |
| mid_3_4 | 0.102 | 0.231 | 0.259 | 0.407 |
| high_5_6 | 0.142 | 0.302 | 0.198 | 0.358 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2702)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2`: recall=0.3333, support=108
- `mid_3_4`: recall=0.0370, support=108
- `high_5_6`: recall=0.5377, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.184 | 0.368 | 0.026 | 0.421 |
| low_1_2 | 0.065 | 0.333 | 0.037 | 0.565 |
| mid_3_4 | 0.093 | 0.343 | 0.037 | 0.528 |
| high_5_6 | 0.066 | 0.349 | 0.047 | 0.538 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2337)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2632, support=38
- `low_1_2`: recall=0.0370, support=108
- `mid_3_4`: recall=0.0556, support=108
- `high_5_6`: recall=0.5472, support=106

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.263 | 0.132 | 0.000 | 0.605 |
| low_1_2 | 0.380 | 0.037 | 0.037 | 0.546 |
| mid_3_4 | 0.426 | 0.056 | 0.056 | 0.463 |
| high_5_6 | 0.387 | 0.028 | 0.038 | 0.547 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3690)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2`: recall=0.8889, support=36
- `mid_3_4`: recall=0.0857, support=35
- `high_5_6`: recall=0.3611, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.143 | 0.643 | 0.000 | 0.214 |
| low_1_2 | 0.000 | 0.889 | 0.000 | 0.111 |
| mid_3_4 | 0.200 | 0.486 | 0.086 | 0.229 |
| high_5_6 | 0.028 | 0.583 | 0.028 | 0.361 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3026)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2`: recall=0.5556, support=36
- `mid_3_4`: recall=0.1143, support=35
- `high_5_6`: recall=0.4722, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.071 | 0.357 | 0.143 | 0.429 |
| low_1_2 | 0.028 | 0.556 | 0.028 | 0.389 |
| mid_3_4 | 0.029 | 0.400 | 0.114 | 0.457 |
| high_5_6 | 0.028 | 0.056 | 0.444 | 0.472 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2949)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.3611, support=36
- `mid_3_4`: recall=0.5143, support=35
- `high_5_6`: recall=0.3056, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.143 | 0.429 | 0.429 |
| low_1_2 | 0.083 | 0.361 | 0.417 | 0.139 |
| mid_3_4 | 0.029 | 0.143 | 0.514 | 0.314 |
| high_5_6 | 0.000 | 0.111 | 0.583 | 0.306 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.2712)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.5556, support=36
- `mid_3_4`: recall=0.1429, support=35
- `high_5_6`: recall=0.3889, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.357 | 0.143 | 0.500 |
| low_1_2 | 0.056 | 0.556 | 0.000 | 0.389 |
| mid_3_4 | 0.029 | 0.400 | 0.143 | 0.429 |
| high_5_6 | 0.056 | 0.167 | 0.389 | 0.389 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.2639)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.0571, support=35
- `high_5_6`: recall=0.5278, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 0.286 | 0.143 | 0.571 |
| low_1_2 | 0.000 | 0.472 | 0.000 | 0.528 |
| mid_3_4 | 0.000 | 0.371 | 0.057 | 0.571 |
| high_5_6 | 0.028 | 0.028 | 0.417 | 0.528 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.2609)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2`: recall=0.4722, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.571 | 0.429 | 0.000 | 0.000 |
| low_1_2 | 0.528 | 0.472 | 0.000 | 0.000 |
| mid_3_4 | 0.486 | 0.514 | 0.000 | 0.000 |
| high_5_6 | 0.500 | 0.500 | 0.000 | 0.000 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.2500)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2`: recall=1.0000, support=36
- `mid_3_4`: recall=0.0000, support=35
- `high_5_6`: recall=0.0000, support=36

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.000 | 1.000 | 0.000 | 0.000 |
| low_1_2 | 0.000 | 1.000 | 0.000 | 0.000 |
| mid_3_4 | 0.000 | 1.000 | 0.000 | 0.000 |
| high_5_6 | 0.000 | 1.000 | 0.000 | 0.000 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.6479)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.8571, support=14
- `low_1_2`: recall=0.7222, support=36
- `mid_3_4`: recall=0.5000, support=36
- `high_5_6`: recall=0.5429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.857 | 0.000 | 0.071 | 0.071 |
| low_1_2 | 0.056 | 0.722 | 0.111 | 0.111 |
| mid_3_4 | 0.000 | 0.167 | 0.500 | 0.333 |
| high_5_6 | 0.029 | 0.086 | 0.343 | 0.543 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.5771)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2`: recall=0.7222, support=36
- `mid_3_4`: recall=0.4167, support=36
- `high_5_6`: recall=0.6571, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.071 | 0.071 |
| low_1_2 | 0.056 | 0.722 | 0.111 | 0.111 |
| mid_3_4 | 0.083 | 0.194 | 0.417 | 0.306 |
| high_5_6 | 0.000 | 0.086 | 0.257 | 0.657 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.5458)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2`: recall=0.6389, support=36
- `mid_3_4`: recall=0.3889, support=36
- `high_5_6`: recall=0.5429, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.071 | 0.071 |
| low_1_2 | 0.056 | 0.639 | 0.222 | 0.083 |
| mid_3_4 | 0.111 | 0.222 | 0.389 | 0.278 |
| high_5_6 | 0.057 | 0.171 | 0.229 | 0.543 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.5062)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2`: recall=0.5556, support=36
- `mid_3_4`: recall=0.2778, support=36
- `high_5_6`: recall=0.6000, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.071 | 0.071 |
| low_1_2 | 0.139 | 0.556 | 0.194 | 0.111 |
| mid_3_4 | 0.167 | 0.194 | 0.278 | 0.361 |
| high_5_6 | 0.086 | 0.114 | 0.200 | 0.600 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.5021)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2`: recall=0.4444, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.7143, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.500 | 0.000 | 0.357 | 0.143 |
| low_1_2 | 0.056 | 0.444 | 0.222 | 0.278 |
| mid_3_4 | 0.056 | 0.250 | 0.361 | 0.333 |
| high_5_6 | 0.000 | 0.057 | 0.229 | 0.714 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.4125)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2`: recall=0.4167, support=36
- `mid_3_4`: recall=0.3611, support=36
- `high_5_6`: recall=0.4857, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.429 | 0.214 | 0.286 | 0.071 |
| low_1_2 | 0.056 | 0.417 | 0.306 | 0.222 |
| mid_3_4 | 0.083 | 0.306 | 0.361 | 0.250 |
| high_5_6 | 0.000 | 0.086 | 0.429 | 0.486 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.4021)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_grouped_4class_omit_hardest_baseline/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2`: recall=0.2778, support=36
- `mid_3_4`: recall=0.5556, support=36
- `high_5_6`: recall=0.3714, support=35

### Confusion (row-normalized)
| true\pred | baseline | low_1_2 | mid_3_4 | high_5_6 |
|---|---|---|---|---|
| baseline | 0.357 | 0.214 | 0.214 | 0.214 |
| low_1_2 | 0.167 | 0.278 | 0.389 | 0.167 |
| mid_3_4 | 0.194 | 0.056 | 0.556 | 0.194 |
| high_5_6 | 0.171 | 0.086 | 0.371 | 0.371 |


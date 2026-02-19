# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_three_level_merged.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4102)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/rf_none.png`

### Class Recall
- `low`: recall=0.3178, support=107
- `mid`: recall=0.2885, support=104
- `high`: recall=0.6129, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.318 | 0.243 | 0.439 |
| mid | 0.192 | 0.288 | 0.519 |
| high | 0.174 | 0.213 | 0.613 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3919)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `low`: recall=0.3271, support=107
- `mid`: recall=0.3269, support=104
- `high`: recall=0.5161, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.327 | 0.308 | 0.364 |
| mid | 0.288 | 0.327 | 0.385 |
| high | 0.239 | 0.245 | 0.516 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3733)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/svm_none.png`

### Class Recall
- `low`: recall=0.3832, support=107
- `mid`: recall=0.3942, support=104
- `high`: recall=0.3355, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.383 | 0.364 | 0.252 |
| mid | 0.327 | 0.394 | 0.279 |
| high | 0.245 | 0.419 | 0.335 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3676)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/knn_none.png`

### Class Recall
- `low`: recall=0.2991, support=107
- `mid`: recall=0.2500, support=104
- `high`: recall=0.5355, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.299 | 0.215 | 0.486 |
| mid | 0.250 | 0.250 | 0.500 |
| high | 0.245 | 0.219 | 0.535 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3430)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.3832, support=107
- `mid`: recall=0.0962, support=104
- `high`: recall=0.5806, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.383 | 0.075 | 0.542 |
| mid | 0.394 | 0.096 | 0.510 |
| high | 0.329 | 0.090 | 0.581 |

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3362)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/mlp_none.png`

### Class Recall
- `low`: recall=0.2523, support=107
- `mid`: recall=0.1827, support=104
- `high`: recall=0.5806, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.252 | 0.196 | 0.551 |
| mid | 0.192 | 0.183 | 0.625 |
| high | 0.194 | 0.226 | 0.581 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3332)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/group_holdout/logreg_none.png`

### Class Recall
- `low`: recall=0.4019, support=107
- `mid`: recall=0.1731, support=104
- `high`: recall=0.4645, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.402 | 0.187 | 0.411 |
| mid | 0.365 | 0.173 | 0.462 |
| high | 0.290 | 0.245 | 0.465 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4253)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/rf_none.png`

### Class Recall
- `low`: recall=0.4375, support=32
- `mid`: recall=0.2647, support=34
- `high`: recall=0.5185, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.438 | 0.125 | 0.438 |
| mid | 0.206 | 0.265 | 0.529 |
| high | 0.167 | 0.315 | 0.519 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4175)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/svm_none.png`

### Class Recall
- `low`: recall=0.4688, support=32
- `mid`: recall=0.3235, support=34
- `high`: recall=0.4074, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.469 | 0.156 | 0.375 |
| mid | 0.265 | 0.324 | 0.412 |
| high | 0.241 | 0.352 | 0.407 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.4109)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.5000, support=32
- `mid`: recall=0.1176, support=34
- `high`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.250 | 0.250 |
| mid | 0.412 | 0.118 | 0.471 |
| high | 0.296 | 0.130 | 0.574 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3844)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/logreg_none.png`

### Class Recall
- `low`: recall=0.4688, support=32
- `mid`: recall=0.3235, support=34
- `high`: recall=0.3333, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.469 | 0.469 | 0.062 |
| mid | 0.412 | 0.324 | 0.265 |
| high | 0.296 | 0.370 | 0.333 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3713)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/decision_tree_none.png`

### Class Recall
- `low`: recall=0.4688, support=32
- `mid`: recall=0.2941, support=34
- `high`: recall=0.3148, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.469 | 0.312 | 0.219 |
| mid | 0.471 | 0.294 | 0.235 |
| high | 0.370 | 0.315 | 0.315 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3557)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/mlp_none.png`

### Class Recall
- `low`: recall=0.2812, support=32
- `mid`: recall=0.1765, support=34
- `high`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.281 | 0.188 | 0.531 |
| mid | 0.176 | 0.176 | 0.647 |
| high | 0.204 | 0.222 | 0.574 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3233)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/loso/knn_none.png`

### Class Recall
- `low`: recall=0.2812, support=32
- `mid`: recall=0.0882, support=34
- `high`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.281 | 0.281 | 0.438 |
| mid | 0.235 | 0.088 | 0.676 |
| high | 0.222 | 0.204 | 0.574 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.3356)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/logreg_none.png`

### Class Recall
- `low`: recall=0.3056, support=36
- `mid`: recall=0.2222, support=36
- `high`: recall=0.4630, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.306 | 0.417 | 0.278 |
| mid | 0.389 | 0.222 | 0.389 |
| high | 0.296 | 0.241 | 0.463 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3300)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/knn_none.png`

### Class Recall
- `low`: recall=0.1667, support=36
- `mid`: recall=0.1667, support=36
- `high`: recall=0.6296, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.167 | 0.167 | 0.667 |
| mid | 0.278 | 0.167 | 0.556 |
| high | 0.222 | 0.148 | 0.630 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.3189)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/rf_none.png`

### Class Recall
- `low`: recall=0.2222, support=36
- `mid`: recall=0.2222, support=36
- `high`: recall=0.5000, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.222 | 0.222 | 0.556 |
| mid | 0.333 | 0.222 | 0.444 |
| high | 0.241 | 0.259 | 0.500 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3172)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.3333, support=36
- `mid`: recall=0.3056, support=36
- `high`: recall=0.3148, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.333 | 0.417 | 0.250 |
| mid | 0.361 | 0.306 | 0.333 |
| high | 0.296 | 0.389 | 0.315 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3167)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `low`: recall=0.1944, support=36
- `mid`: recall=0.3889, support=36
- `high`: recall=0.3519, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.194 | 0.278 | 0.528 |
| mid | 0.306 | 0.389 | 0.306 |
| high | 0.315 | 0.333 | 0.352 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.3089)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/mlp_none.png`

### Class Recall
- `low`: recall=0.3056, support=36
- `mid`: recall=0.1667, support=36
- `high`: recall=0.4444, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.306 | 0.306 | 0.389 |
| mid | 0.361 | 0.167 | 0.472 |
| high | 0.278 | 0.278 | 0.444 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.2744)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/ecg/within_participant/svm_none.png`

### Class Recall
- `low`: recall=0.2500, support=36
- `mid`: recall=0.1667, support=36
- `high`: recall=0.4074, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.250 | 0.306 | 0.444 |
| mid | 0.417 | 0.167 | 0.417 |
| high | 0.333 | 0.259 | 0.407 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.4560)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/logreg_none.png`

### Class Recall
- `low`: recall=0.4206, support=107
- `mid`: recall=0.2788, support=104
- `high`: recall=0.6968, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.421 | 0.252 | 0.327 |
| mid | 0.154 | 0.279 | 0.567 |
| high | 0.155 | 0.148 | 0.697 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4465)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/svm_none.png`

### Class Recall
- `low`: recall=0.3925, support=107
- `mid`: recall=0.3654, support=104
- `high`: recall=0.6129, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.393 | 0.308 | 0.299 |
| mid | 0.125 | 0.365 | 0.510 |
| high | 0.116 | 0.271 | 0.613 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4166)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/mlp_none.png`

### Class Recall
- `low`: recall=0.2897, support=107
- `mid`: recall=0.4231, support=104
- `high`: recall=0.5484, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.290 | 0.402 | 0.308 |
| mid | 0.106 | 0.423 | 0.471 |
| high | 0.065 | 0.387 | 0.548 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3955)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/knn_none.png`

### Class Recall
- `low`: recall=0.4112, support=107
- `mid`: recall=0.2500, support=104
- `high`: recall=0.5484, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.411 | 0.215 | 0.374 |
| mid | 0.183 | 0.250 | 0.567 |
| high | 0.206 | 0.245 | 0.548 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3789)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `low`: recall=0.3178, support=107
- `mid`: recall=0.4231, support=104
- `high`: recall=0.3419, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.318 | 0.346 | 0.336 |
| mid | 0.250 | 0.423 | 0.327 |
| high | 0.271 | 0.387 | 0.342 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3784)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/rf_none.png`

### Class Recall
- `low`: recall=0.2897, support=107
- `mid`: recall=0.2308, support=104
- `high`: recall=0.6516, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.290 | 0.168 | 0.542 |
| mid | 0.125 | 0.231 | 0.644 |
| high | 0.090 | 0.258 | 0.652 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3596)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.0841, support=107
- `mid`: recall=0.7692, support=104
- `high`: recall=0.2323, support=155

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.084 | 0.813 | 0.103 |
| mid | 0.077 | 0.769 | 0.154 |
| high | 0.045 | 0.723 | 0.232 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.4543)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/logreg_none.png`

### Class Recall
- `low`: recall=0.7812, support=32
- `mid`: recall=0.4412, support=34
- `high`: recall=0.1481, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.781 | 0.219 | 0.000 |
| mid | 0.471 | 0.441 | 0.088 |
| high | 0.278 | 0.574 | 0.148 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4350)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/svm_none.png`

### Class Recall
- `low`: recall=0.8438, support=32
- `mid`: recall=0.0882, support=34
- `high`: recall=0.3889, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.844 | 0.125 | 0.031 |
| mid | 0.647 | 0.088 | 0.265 |
| high | 0.333 | 0.278 | 0.389 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4334)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/rf_none.png`

### Class Recall
- `low`: recall=0.7500, support=32
- `mid`: recall=0.0882, support=34
- `high`: recall=0.4630, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.750 | 0.031 | 0.219 |
| mid | 0.471 | 0.088 | 0.441 |
| high | 0.463 | 0.074 | 0.463 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4129)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/mlp_none.png`

### Class Recall
- `low`: recall=0.6875, support=32
- `mid`: recall=0.3824, support=34
- `high`: recall=0.1852, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.688 | 0.250 | 0.062 |
| mid | 0.500 | 0.382 | 0.118 |
| high | 0.444 | 0.370 | 0.185 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3834)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/knn_none.png`

### Class Recall
- `low`: recall=0.7812, support=32
- `mid`: recall=0.0588, support=34
- `high`: recall=0.3333, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.781 | 0.062 | 0.156 |
| mid | 0.588 | 0.059 | 0.353 |
| high | 0.444 | 0.222 | 0.333 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3485)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.6875, support=32
- `mid`: recall=0.3824, support=34
- `high`: recall=0.0000, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.688 | 0.312 | 0.000 |
| mid | 0.618 | 0.382 | 0.000 |
| high | 0.333 | 0.667 | 0.000 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3387)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/loso/decision_tree_none.png`

### Class Recall
- `low`: recall=0.2812, support=32
- `mid`: recall=0.2941, support=34
- `high`: recall=0.4630, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.281 | 0.344 | 0.375 |
| mid | 0.147 | 0.294 | 0.559 |
| high | 0.204 | 0.333 | 0.463 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.5261)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/svm_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.3889, support=36
- `high`: recall=0.7037, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.250 | 0.250 |
| mid | 0.333 | 0.389 | 0.278 |
| high | 0.111 | 0.185 | 0.704 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.5256)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/logreg_none.png`

### Class Recall
- `low`: recall=0.5278, support=36
- `mid`: recall=0.3611, support=36
- `high`: recall=0.7037, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.528 | 0.333 | 0.139 |
| mid | 0.278 | 0.361 | 0.361 |
| high | 0.093 | 0.204 | 0.704 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5228)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/mlp_none.png`

### Class Recall
- `low`: recall=0.4167, support=36
- `mid`: recall=0.4444, support=36
- `high`: recall=0.7407, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.417 | 0.278 | 0.306 |
| mid | 0.306 | 0.444 | 0.250 |
| high | 0.093 | 0.167 | 0.741 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.5189)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/rf_none.png`

### Class Recall
- `low`: recall=0.4722, support=36
- `mid`: recall=0.3333, support=36
- `high`: recall=0.7593, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.472 | 0.278 | 0.250 |
| mid | 0.278 | 0.333 | 0.389 |
| high | 0.111 | 0.130 | 0.759 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.4639)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.2500, support=36
- `high`: recall=0.6296, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.250 | 0.250 |
| mid | 0.417 | 0.250 | 0.333 |
| high | 0.204 | 0.167 | 0.630 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.4506)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/knn_none.png`

### Class Recall
- `low`: recall=0.2222, support=36
- `mid`: recall=0.3611, support=36
- `high`: recall=0.7778, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.222 | 0.306 | 0.472 |
| mid | 0.222 | 0.361 | 0.417 |
| high | 0.093 | 0.130 | 0.778 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.4267)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `low`: recall=0.4444, support=36
- `mid`: recall=0.3333, support=36
- `high`: recall=0.5185, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.444 | 0.167 | 0.389 |
| mid | 0.278 | 0.333 | 0.389 |
| high | 0.241 | 0.241 | 0.519 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4492)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/mlp_none.png`

### Class Recall
- `low`: recall=0.5185, support=108
- `mid`: recall=0.1667, support=108
- `high`: recall=0.6478, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.519 | 0.074 | 0.407 |
| mid | 0.204 | 0.167 | 0.630 |
| high | 0.151 | 0.201 | 0.648 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4467)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/svm_none.png`

### Class Recall
- `low`: recall=0.5370, support=108
- `mid`: recall=0.1759, support=108
- `high`: recall=0.6038, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.537 | 0.074 | 0.389 |
| mid | 0.361 | 0.176 | 0.463 |
| high | 0.233 | 0.164 | 0.604 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.4285)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `low`: recall=0.5556, support=108
- `mid`: recall=0.2778, support=108
- `high`: recall=0.4277, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.556 | 0.222 | 0.222 |
| mid | 0.306 | 0.278 | 0.417 |
| high | 0.138 | 0.434 | 0.428 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4208)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/rf_none.png`

### Class Recall
- `low`: recall=0.3333, support=108
- `mid`: recall=0.1204, support=108
- `high`: recall=0.8113, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.333 | 0.093 | 0.574 |
| mid | 0.111 | 0.120 | 0.769 |
| high | 0.088 | 0.101 | 0.811 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.4161)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/knn_none.png`

### Class Recall
- `low`: recall=0.3148, support=108
- `mid`: recall=0.3704, support=108
- `high`: recall=0.5535, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.315 | 0.204 | 0.481 |
| mid | 0.167 | 0.370 | 0.463 |
| high | 0.182 | 0.264 | 0.553 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3343)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/logreg_none.png`

### Class Recall
- `low`: recall=0.0370, support=108
- `mid`: recall=0.0556, support=108
- `high`: recall=0.9182, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.037 | 0.102 | 0.861 |
| mid | 0.074 | 0.056 | 0.870 |
| high | 0.025 | 0.057 | 0.918 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3299)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.3333, support=108
- `mid`: recall=0.5648, support=108
- `high`: recall=0.0755, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.333 | 0.602 | 0.065 |
| mid | 0.324 | 0.565 | 0.111 |
| high | 0.327 | 0.597 | 0.075 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4753)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/rf_none.png`

### Class Recall
- `low`: recall=0.4444, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.9815, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.444 | 0.000 | 0.556 |
| mid | 0.314 | 0.000 | 0.686 |
| high | 0.019 | 0.000 | 0.981 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4753)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/svm_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.9259, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.000 | 0.500 |
| mid | 0.343 | 0.000 | 0.657 |
| high | 0.056 | 0.019 | 0.926 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.4512)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/decision_tree_none.png`

### Class Recall
- `low`: recall=0.6944, support=36
- `mid`: recall=0.2000, support=35
- `high`: recall=0.4630, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.694 | 0.167 | 0.139 |
| mid | 0.600 | 0.200 | 0.200 |
| high | 0.352 | 0.185 | 0.463 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4259)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/mlp_none.png`

### Class Recall
- `low`: recall=0.3889, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.8889, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.389 | 0.111 | 0.500 |
| mid | 0.257 | 0.000 | 0.743 |
| high | 0.019 | 0.093 | 0.889 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/gaussian_nb_none.png`

### Class Recall
- `low`: recall=1.0000, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.0000, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 1.000 | 0.000 | 0.000 |
| mid | 1.000 | 0.000 | 0.000 |
| high | 1.000 | 0.000 | 0.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/logreg_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.5000, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.000 | 0.500 |
| mid | 0.514 | 0.000 | 0.486 |
| high | 0.500 | 0.000 | 0.500 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/loso/knn_none.png`

### Class Recall
- `low`: recall=0.3889, support=36
- `mid`: recall=0.1714, support=35
- `high`: recall=0.4444, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.389 | 0.194 | 0.417 |
| mid | 0.286 | 0.171 | 0.543 |
| high | 0.130 | 0.426 | 0.444 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.6528)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/logreg_none.png`

### Class Recall
- `low`: recall=0.8056, support=36
- `mid`: recall=0.4444, support=36
- `high`: recall=0.7170, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.806 | 0.083 | 0.111 |
| mid | 0.194 | 0.444 | 0.361 |
| high | 0.075 | 0.208 | 0.717 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.6083)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/rf_none.png`

### Class Recall
- `low`: recall=0.7222, support=36
- `mid`: recall=0.2500, support=36
- `high`: recall=0.8491, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.722 | 0.139 | 0.139 |
| mid | 0.194 | 0.250 | 0.556 |
| high | 0.075 | 0.075 | 0.849 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5783)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/mlp_none.png`

### Class Recall
- `low`: recall=0.7778, support=36
- `mid`: recall=0.3889, support=36
- `high`: recall=0.6226, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.778 | 0.028 | 0.194 |
| mid | 0.222 | 0.389 | 0.389 |
| high | 0.170 | 0.208 | 0.623 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.5211)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/decision_tree_none.png`

### Class Recall
- `low`: recall=0.6667, support=36
- `mid`: recall=0.3333, support=36
- `high`: recall=0.5849, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.667 | 0.278 | 0.056 |
| mid | 0.167 | 0.333 | 0.500 |
| high | 0.057 | 0.358 | 0.585 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.5061)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/knn_none.png`

### Class Recall
- `low`: recall=0.5556, support=36
- `mid`: recall=0.1111, support=36
- `high`: recall=0.8491, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.556 | 0.222 | 0.222 |
| mid | 0.111 | 0.111 | 0.778 |
| high | 0.075 | 0.075 | 0.849 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.4983)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/svm_none.png`

### Class Recall
- `low`: recall=0.5833, support=36
- `mid`: recall=0.4167, support=36
- `high`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.583 | 0.333 | 0.083 |
| mid | 0.222 | 0.417 | 0.361 |
| high | 0.170 | 0.283 | 0.547 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3539)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.1944, support=36
- `mid`: recall=0.4444, support=36
- `high`: recall=0.3962, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.194 | 0.556 | 0.250 |
| mid | 0.111 | 0.444 | 0.444 |
| high | 0.132 | 0.472 | 0.396 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4268)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/rf_none.png`

### Class Recall
- `low`: recall=0.5000, support=108
- `mid`: recall=0.1852, support=108
- `high`: recall=0.6101, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.130 | 0.370 |
| mid | 0.296 | 0.185 | 0.519 |
| high | 0.214 | 0.176 | 0.610 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4065)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/svm_none.png`

### Class Recall
- `low`: recall=0.3519, support=108
- `mid`: recall=0.2685, support=108
- `high`: recall=0.6226, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.352 | 0.250 | 0.398 |
| mid | 0.157 | 0.269 | 0.574 |
| high | 0.082 | 0.296 | 0.623 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4033)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/mlp_none.png`

### Class Recall
- `low`: recall=0.4074, support=108
- `mid`: recall=0.1204, support=108
- `high`: recall=0.7233, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.407 | 0.065 | 0.528 |
| mid | 0.231 | 0.120 | 0.648 |
| high | 0.145 | 0.132 | 0.723 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3810)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/knn_none.png`

### Class Recall
- `low`: recall=0.3056, support=108
- `mid`: recall=0.2130, support=108
- `high`: recall=0.6164, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.306 | 0.111 | 0.583 |
| mid | 0.222 | 0.213 | 0.565 |
| high | 0.220 | 0.164 | 0.616 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3595)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `low`: recall=0.4907, support=108
- `mid`: recall=0.2407, support=108
- `high`: recall=0.3711, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.491 | 0.278 | 0.231 |
| mid | 0.444 | 0.241 | 0.315 |
| high | 0.264 | 0.365 | 0.371 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3367)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/logreg_none.png`

### Class Recall
- `low`: recall=0.0463, support=108
- `mid`: recall=0.0556, support=108
- `high`: recall=0.9182, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.046 | 0.093 | 0.861 |
| mid | 0.065 | 0.056 | 0.880 |
| high | 0.025 | 0.057 | 0.918 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3299)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.3333, support=108
- `mid`: recall=0.5648, support=108
- `high`: recall=0.0755, support=159

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.333 | 0.602 | 0.065 |
| mid | 0.324 | 0.565 | 0.111 |
| high | 0.327 | 0.597 | 0.075 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4907)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/mlp_none.png`

### Class Recall
- `low`: recall=0.5278, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.9444, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.528 | 0.028 | 0.444 |
| mid | 0.371 | 0.000 | 0.629 |
| high | 0.056 | 0.000 | 0.944 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.4811)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/decision_tree_none.png`

### Class Recall
- `low`: recall=0.6389, support=36
- `mid`: recall=0.2286, support=35
- `high`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.639 | 0.278 | 0.083 |
| mid | 0.486 | 0.229 | 0.286 |
| high | 0.074 | 0.352 | 0.574 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4722)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/rf_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.0286, support=35
- `high`: recall=0.8889, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.000 | 0.500 |
| mid | 0.343 | 0.029 | 0.629 |
| high | 0.019 | 0.093 | 0.889 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3951)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/svm_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.1714, support=35
- `high`: recall=0.5185, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.028 | 0.472 |
| mid | 0.229 | 0.171 | 0.600 |
| high | 0.019 | 0.463 | 0.519 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3611)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/knn_none.png`

### Class Recall
- `low`: recall=0.4167, support=36
- `mid`: recall=0.1143, support=35
- `high`: recall=0.5556, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.417 | 0.056 | 0.528 |
| mid | 0.400 | 0.114 | 0.486 |
| high | 0.130 | 0.315 | 0.556 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `low`: recall=1.0000, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.0000, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 1.000 | 0.000 | 0.000 |
| mid | 1.000 | 0.000 | 0.000 |
| high | 1.000 | 0.000 | 0.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/loso/logreg_none.png`

### Class Recall
- `low`: recall=0.5000, support=36
- `mid`: recall=0.0000, support=35
- `high`: recall=0.5000, support=54

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.500 | 0.000 | 0.500 |
| mid | 0.514 | 0.000 | 0.486 |
| high | 0.500 | 0.000 | 0.500 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.6389)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/rf_none.png`

### Class Recall
- `low`: recall=0.7222, support=36
- `mid`: recall=0.3889, support=36
- `high`: recall=0.8113, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.722 | 0.167 | 0.111 |
| mid | 0.194 | 0.389 | 0.417 |
| high | 0.019 | 0.170 | 0.811 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.6161)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/knn_none.png`

### Class Recall
- `low`: recall=0.5278, support=36
- `mid`: recall=0.4444, support=36
- `high`: recall=0.8679, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.528 | 0.139 | 0.333 |
| mid | 0.111 | 0.444 | 0.444 |
| high | 0.057 | 0.075 | 0.868 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.6150)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `low`: recall=0.8056, support=36
- `mid`: recall=0.3056, support=36
- `high`: recall=0.7358, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.806 | 0.083 | 0.111 |
| mid | 0.194 | 0.306 | 0.500 |
| high | 0.075 | 0.189 | 0.736 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.6067)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/logreg_none.png`

### Class Recall
- `low`: recall=0.7222, support=36
- `mid`: recall=0.5278, support=36
- `high`: recall=0.5849, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.722 | 0.278 | 0.000 |
| mid | 0.194 | 0.528 | 0.278 |
| high | 0.189 | 0.226 | 0.585 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5711)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/mlp_none.png`

### Class Recall
- `low`: recall=0.5833, support=36
- `mid`: recall=0.4444, support=36
- `high`: recall=0.6981, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.583 | 0.194 | 0.222 |
| mid | 0.222 | 0.444 | 0.333 |
| high | 0.189 | 0.113 | 0.698 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.5094)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/svm_none.png`

### Class Recall
- `low`: recall=0.6111, support=36
- `mid`: recall=0.4167, support=36
- `high`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.611 | 0.250 | 0.139 |
| mid | 0.306 | 0.417 | 0.278 |
| high | 0.264 | 0.189 | 0.547 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.3733)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_three_level_merged/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `low`: recall=0.1944, support=36
- `mid`: recall=0.5278, support=36
- `high`: recall=0.3774, support=53

### Confusion (row-normalized)
| true\pred | low | mid | high |
|---|---|---|---|
| low | 0.194 | 0.556 | 0.250 |
| mid | 0.111 | 0.528 | 0.361 |
| high | 0.132 | 0.491 | 0.377 |


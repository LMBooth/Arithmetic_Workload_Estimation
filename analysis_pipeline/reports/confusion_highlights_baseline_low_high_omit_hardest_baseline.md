# Confusion Matrix Highlights

- Source results: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/ml_results_baseline_low_high_omit_hardest_baseline.json`
- Ranking metric: `balanced_accuracy_mean`

## ecg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3867)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0541, support=37
- `low_1_2_3`: recall=0.4684, support=158
- `high_4_5_6`: recall=0.6154, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.054 | 0.486 | 0.459 |
| low_1_2_3 | 0.038 | 0.468 | 0.494 |
| high_4_5_6 | 0.032 | 0.353 | 0.615 |

## ecg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3653)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0811, support=37
- `low_1_2_3`: recall=0.3608, support=158
- `high_4_5_6`: recall=0.6218, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.081 | 0.486 | 0.432 |
| low_1_2_3 | 0.114 | 0.361 | 0.525 |
| high_4_5_6 | 0.115 | 0.263 | 0.622 |

## ecg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3553)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.4054, support=37
- `low_1_2_3`: recall=0.2532, support=158
- `high_4_5_6`: recall=0.4295, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.405 | 0.324 | 0.270 |
| low_1_2_3 | 0.354 | 0.253 | 0.392 |
| high_4_5_6 | 0.346 | 0.224 | 0.429 |

## ecg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3514)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.0270, support=37
- `low_1_2_3`: recall=0.4051, support=158
- `high_4_5_6`: recall=0.6538, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.027 | 0.514 | 0.459 |
| low_1_2_3 | 0.044 | 0.405 | 0.551 |
| high_4_5_6 | 0.032 | 0.314 | 0.654 |

## ecg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3464)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2973, support=37
- `low_1_2_3`: recall=0.2215, support=158
- `high_4_5_6`: recall=0.4615, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.297 | 0.270 | 0.432 |
| low_1_2_3 | 0.424 | 0.222 | 0.354 |
| high_4_5_6 | 0.385 | 0.154 | 0.462 |

## ecg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3340)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=37
- `low_1_2_3`: recall=0.6329, support=158
- `high_4_5_6`: recall=0.3846, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.649 | 0.351 |
| low_1_2_3 | 0.019 | 0.633 | 0.348 |
| high_4_5_6 | 0.032 | 0.583 | 0.385 |

## ecg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3038)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.3514, support=37
- `low_1_2_3`: recall=0.2532, support=158
- `high_4_5_6`: recall=0.3590, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.351 | 0.351 | 0.297 |
| low_1_2_3 | 0.430 | 0.253 | 0.316 |
| high_4_5_6 | 0.423 | 0.218 | 0.359 |

## ecg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.4346)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `low_1_2_3`: recall=0.2245, support=49
- `high_4_5_6`: recall=0.2830, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.786 | 0.143 | 0.071 |
| low_1_2_3 | 0.755 | 0.224 | 0.020 |
| high_4_5_6 | 0.434 | 0.283 | 0.283 |

## ecg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4181)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `low_1_2_3`: recall=0.2245, support=49
- `high_4_5_6`: recall=0.2264, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.786 | 0.143 | 0.071 |
| low_1_2_3 | 0.653 | 0.224 | 0.122 |
| high_4_5_6 | 0.566 | 0.208 | 0.226 |

## ecg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.4123)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.5918, support=49
- `high_4_5_6`: recall=0.3396, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.500 | 0.214 |
| low_1_2_3 | 0.122 | 0.592 | 0.286 |
| high_4_5_6 | 0.132 | 0.528 | 0.340 |

## ecg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3811)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.7143, support=49
- `high_4_5_6`: recall=0.4151, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.714 | 0.286 |
| low_1_2_3 | 0.000 | 0.714 | 0.286 |
| high_4_5_6 | 0.000 | 0.585 | 0.415 |

## ecg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3785)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.6327, support=49
- `high_4_5_6`: recall=0.4906, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.571 | 0.429 |
| low_1_2_3 | 0.041 | 0.633 | 0.327 |
| high_4_5_6 | 0.038 | 0.472 | 0.491 |

## ecg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3514)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.7347, support=49
- `high_4_5_6`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.786 | 0.214 |
| low_1_2_3 | 0.102 | 0.735 | 0.163 |
| high_4_5_6 | 0.019 | 0.679 | 0.302 |

## ecg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3451)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.4694, support=49
- `high_4_5_6`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.429 | 0.571 |
| low_1_2_3 | 0.020 | 0.469 | 0.510 |
| high_4_5_6 | 0.038 | 0.415 | 0.547 |

## ecg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.4889)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.5741, support=54
- `high_4_5_6`: recall=0.5370, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.286 |
| low_1_2_3 | 0.093 | 0.574 | 0.333 |
| high_4_5_6 | 0.148 | 0.315 | 0.537 |

## ecg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.4711)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.5926, support=54
- `high_4_5_6`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.357 |
| low_1_2_3 | 0.148 | 0.593 | 0.259 |
| high_4_5_6 | 0.130 | 0.296 | 0.574 |

## ecg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.4533)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.5370, support=54
- `high_4_5_6`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.500 | 0.286 |
| low_1_2_3 | 0.130 | 0.537 | 0.333 |
| high_4_5_6 | 0.111 | 0.315 | 0.574 |

## ecg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.4433)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.4259, support=54
- `high_4_5_6`: recall=0.6111, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.429 | 0.286 |
| low_1_2_3 | 0.278 | 0.426 | 0.296 |
| high_4_5_6 | 0.148 | 0.241 | 0.611 |

## ecg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.4156)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.3704, support=54
- `high_4_5_6`: recall=0.6296, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.429 | 0.357 |
| low_1_2_3 | 0.111 | 0.370 | 0.519 |
| high_4_5_6 | 0.074 | 0.296 | 0.630 |

## ecg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.3867)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.4074, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.286 | 0.357 |
| low_1_2_3 | 0.204 | 0.444 | 0.352 |
| high_4_5_6 | 0.185 | 0.407 | 0.407 |

## ecg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3822)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/ecg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.6111, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.071 | 0.571 | 0.357 |
| low_1_2_3 | 0.093 | 0.444 | 0.463 |
| high_4_5_6 | 0.056 | 0.333 | 0.611 |

## eeg | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4874)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.3243, support=37
- `low_1_2_3`: recall=0.3987, support=158
- `high_4_5_6`: recall=0.7051, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.324 | 0.216 | 0.459 |
| low_1_2_3 | 0.177 | 0.399 | 0.424 |
| high_4_5_6 | 0.115 | 0.179 | 0.705 |

## eeg | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.4673)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.3784, support=37
- `low_1_2_3`: recall=0.3671, support=158
- `high_4_5_6`: recall=0.6218, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.378 | 0.216 | 0.405 |
| low_1_2_3 | 0.209 | 0.367 | 0.424 |
| high_4_5_6 | 0.192 | 0.186 | 0.622 |

## eeg | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4414)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1081, support=37
- `low_1_2_3`: recall=0.5380, support=158
- `high_4_5_6`: recall=0.6795, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.108 | 0.297 | 0.595 |
| low_1_2_3 | 0.032 | 0.538 | 0.430 |
| high_4_5_6 | 0.019 | 0.301 | 0.679 |

## eeg | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.4204)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.0811, support=37
- `low_1_2_3`: recall=0.5823, support=158
- `high_4_5_6`: recall=0.5705, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.081 | 0.459 | 0.459 |
| low_1_2_3 | 0.076 | 0.582 | 0.342 |
| high_4_5_6 | 0.096 | 0.333 | 0.571 |

## eeg | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4101)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1351, support=37
- `low_1_2_3`: recall=0.3608, support=158
- `high_4_5_6`: recall=0.7500, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.135 | 0.135 | 0.730 |
| low_1_2_3 | 0.089 | 0.361 | 0.551 |
| high_4_5_6 | 0.038 | 0.212 | 0.750 |

## eeg | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3936)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1892, support=37
- `low_1_2_3`: recall=0.1139, support=158
- `high_4_5_6`: recall=0.8782, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.189 | 0.027 | 0.784 |
| low_1_2_3 | 0.114 | 0.114 | 0.772 |
| high_4_5_6 | 0.064 | 0.058 | 0.878 |

## eeg | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3290)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2703, support=37
- `low_1_2_3`: recall=0.4937, support=158
- `high_4_5_6`: recall=0.2244, support=156

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.270 | 0.595 | 0.135 |
| low_1_2_3 | 0.342 | 0.494 | 0.165 |
| high_4_5_6 | 0.397 | 0.378 | 0.224 |

## eeg | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.6015)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2_3`: recall=0.8367, support=49
- `high_4_5_6`: recall=0.2642, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.714 | 0.286 | 0.000 |
| low_1_2_3 | 0.102 | 0.837 | 0.061 |
| high_4_5_6 | 0.113 | 0.623 | 0.264 |

## eeg | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.5370)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.7959, support=49
- `high_4_5_6`: recall=0.5472, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.500 | 0.214 |
| low_1_2_3 | 0.000 | 0.796 | 0.204 |
| high_4_5_6 | 0.019 | 0.434 | 0.547 |

## eeg | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.5314)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.5714, support=49
- `high_4_5_6`: recall=0.5849, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.429 | 0.143 |
| low_1_2_3 | 0.163 | 0.571 | 0.265 |
| high_4_5_6 | 0.057 | 0.358 | 0.585 |

## eeg | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4847)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.8163, support=49
- `high_4_5_6`: recall=0.4340, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.714 | 0.071 |
| low_1_2_3 | 0.020 | 0.816 | 0.163 |
| high_4_5_6 | 0.057 | 0.509 | 0.434 |

## eeg | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4408)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.8163, support=49
- `high_4_5_6`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.786 | 0.000 |
| low_1_2_3 | 0.000 | 0.816 | 0.184 |
| high_4_5_6 | 0.019 | 0.679 | 0.302 |

## eeg | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4049)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.9184, support=49
- `high_4_5_6`: recall=0.3019, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.929 | 0.071 |
| low_1_2_3 | 0.000 | 0.918 | 0.082 |
| high_4_5_6 | 0.000 | 0.698 | 0.302 |

## eeg | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3974)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.7755, support=49
- `high_4_5_6`: recall=0.4340, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.714 | 0.286 |
| low_1_2_3 | 0.020 | 0.776 | 0.204 |
| high_4_5_6 | 0.000 | 0.566 | 0.434 |

## eeg | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.5800)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.5926, support=54
- `high_4_5_6`: recall=0.6667, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.143 | 0.286 |
| low_1_2_3 | 0.019 | 0.593 | 0.389 |
| high_4_5_6 | 0.019 | 0.315 | 0.667 |

## eeg | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.5656)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.6111, support=54
- `high_4_5_6`: recall=0.6481, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.214 |
| low_1_2_3 | 0.037 | 0.611 | 0.352 |
| high_4_5_6 | 0.019 | 0.333 | 0.648 |

## eeg | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.5467)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.6296, support=54
- `high_4_5_6`: recall=0.6296, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.286 | 0.286 |
| low_1_2_3 | 0.037 | 0.630 | 0.333 |
| high_4_5_6 | 0.000 | 0.370 | 0.630 |

## eeg | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.5389)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.6667, support=54
- `high_4_5_6`: recall=0.6667, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.429 | 0.214 |
| low_1_2_3 | 0.056 | 0.667 | 0.278 |
| high_4_5_6 | 0.037 | 0.296 | 0.667 |

## eeg | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5367)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.6667, support=54
- `high_4_5_6`: recall=0.6111, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.357 | 0.214 |
| low_1_2_3 | 0.019 | 0.667 | 0.315 |
| high_4_5_6 | 0.000 | 0.389 | 0.611 |

## eeg | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.4589)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2_3`: recall=0.6481, support=54
- `high_4_5_6`: recall=0.5926, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.143 | 0.643 | 0.214 |
| low_1_2_3 | 0.093 | 0.648 | 0.259 |
| high_4_5_6 | 0.037 | 0.370 | 0.593 |

## eeg | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.3967)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/eeg/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2_3`: recall=0.5185, support=54
- `high_4_5_6`: recall=0.5741, support=54

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.071 | 0.357 | 0.571 |
| low_1_2_3 | 0.000 | 0.519 | 0.481 |
| high_4_5_6 | 0.074 | 0.352 | 0.574 |

## fused | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.4685)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.2368, support=38
- `low_1_2_3`: recall=0.5185, support=162
- `high_4_5_6`: recall=0.6000, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.237 | 0.447 | 0.316 |
| low_1_2_3 | 0.179 | 0.519 | 0.302 |
| high_4_5_6 | 0.106 | 0.294 | 0.600 |

## fused | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4418)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `low_1_2_3`: recall=0.5679, support=162
- `high_4_5_6`: recall=0.6562, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.105 | 0.447 | 0.447 |
| low_1_2_3 | 0.031 | 0.568 | 0.401 |
| high_4_5_6 | 0.050 | 0.294 | 0.656 |

## fused | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3881)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1316, support=38
- `low_1_2_3`: recall=0.4568, support=162
- `high_4_5_6`: recall=0.5750, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.132 | 0.447 | 0.421 |
| low_1_2_3 | 0.142 | 0.457 | 0.401 |
| high_4_5_6 | 0.094 | 0.331 | 0.575 |

## fused | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3647)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2_3`: recall=0.0000, support=162
- `high_4_5_6`: recall=0.9375, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.184 | 0.000 | 0.816 |
| low_1_2_3 | 0.086 | 0.000 | 0.914 |
| high_4_5_6 | 0.062 | 0.000 | 0.938 |

## fused | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3495)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2_3`: recall=0.4444, support=162
- `high_4_5_6`: recall=0.4562, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.184 | 0.421 | 0.395 |
| low_1_2_3 | 0.198 | 0.444 | 0.358 |
| high_4_5_6 | 0.081 | 0.463 | 0.456 |

## fused | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3097)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.4474, support=38
- `low_1_2_3`: recall=0.0494, support=162
- `high_4_5_6`: recall=0.3937, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.447 | 0.079 | 0.474 |
| low_1_2_3 | 0.537 | 0.049 | 0.414 |
| high_4_5_6 | 0.562 | 0.044 | 0.394 |

## fused | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.2903)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0263, support=38
- `low_1_2_3`: recall=0.4815, support=162
- `high_4_5_6`: recall=0.3625, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.026 | 0.605 | 0.368 |
| low_1_2_3 | 0.179 | 0.481 | 0.340 |
| high_4_5_6 | 0.287 | 0.350 | 0.362 |

## fused | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.5139)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.3571, support=14
- `low_1_2_3`: recall=0.2778, support=54
- `high_4_5_6`: recall=0.9057, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.357 | 0.143 | 0.500 |
| low_1_2_3 | 0.037 | 0.278 | 0.685 |
| high_4_5_6 | 0.019 | 0.075 | 0.906 |

## fused | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4621)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2_3`: recall=0.5000, support=54
- `high_4_5_6`: recall=0.8113, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.071 | 0.357 | 0.571 |
| low_1_2_3 | 0.000 | 0.500 | 0.500 |
| high_4_5_6 | 0.000 | 0.189 | 0.811 |

## fused | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4485)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0714, support=14
- `low_1_2_3`: recall=0.4630, support=54
- `high_4_5_6`: recall=0.8113, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.071 | 0.357 | 0.571 |
| low_1_2_3 | 0.019 | 0.463 | 0.519 |
| high_4_5_6 | 0.000 | 0.189 | 0.811 |

## fused | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.4349)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2143, support=14
- `low_1_2_3`: recall=0.3704, support=54
- `high_4_5_6`: recall=0.7170, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.214 | 0.357 | 0.429 |
| low_1_2_3 | 0.093 | 0.370 | 0.537 |
| high_4_5_6 | 0.019 | 0.264 | 0.717 |

## fused | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.4168)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.1429, support=14
- `low_1_2_3`: recall=0.4815, support=54
- `high_4_5_6`: recall=0.6226, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.143 | 0.571 | 0.286 |
| low_1_2_3 | 0.019 | 0.481 | 0.500 |
| high_4_5_6 | 0.019 | 0.358 | 0.623 |

## fused | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.0000, support=54
- `high_4_5_6`: recall=1.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.000 | 1.000 |
| low_1_2_3 | 0.000 | 0.000 | 1.000 |
| high_4_5_6 | 0.000 | 0.000 | 1.000 |

## fused | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3272)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.4815, support=54
- `high_4_5_6`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.429 | 0.071 |
| low_1_2_3 | 0.519 | 0.481 | 0.000 |
| high_4_5_6 | 0.491 | 0.509 | 0.000 |

## fused | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.7289)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `low_1_2_3`: recall=0.6852, support=54
- `high_4_5_6`: recall=0.7925, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.786 | 0.143 | 0.071 |
| low_1_2_3 | 0.037 | 0.685 | 0.278 |
| high_4_5_6 | 0.000 | 0.208 | 0.792 |

## fused | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.7044)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.7857, support=14
- `low_1_2_3`: recall=0.6852, support=54
- `high_4_5_6`: recall=0.6226, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.786 | 0.143 | 0.071 |
| low_1_2_3 | 0.074 | 0.685 | 0.241 |
| high_4_5_6 | 0.057 | 0.321 | 0.623 |

## fused | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.6767)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.5370, support=54
- `high_4_5_6`: recall=0.8302, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.286 | 0.071 |
| low_1_2_3 | 0.037 | 0.537 | 0.426 |
| high_4_5_6 | 0.019 | 0.151 | 0.830 |

## fused | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.6567)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.6481, support=54
- `high_4_5_6`: recall=0.7170, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.214 | 0.143 |
| low_1_2_3 | 0.056 | 0.648 | 0.296 |
| high_4_5_6 | 0.038 | 0.245 | 0.717 |

## fused | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.6378)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.5185, support=54
- `high_4_5_6`: recall=0.8491, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.214 | 0.214 |
| low_1_2_3 | 0.037 | 0.519 | 0.444 |
| high_4_5_6 | 0.019 | 0.132 | 0.849 |

## fused | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.5922)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.5370, support=54
- `high_4_5_6`: recall=0.6981, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.143 |
| low_1_2_3 | 0.111 | 0.537 | 0.352 |
| high_4_5_6 | 0.094 | 0.208 | 0.698 |

## fused | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.5078)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/fused/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.2778, support=54
- `high_4_5_6`: recall=0.7925, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.214 | 0.357 |
| low_1_2_3 | 0.204 | 0.278 | 0.519 |
| high_4_5_6 | 0.132 | 0.075 | 0.792 |

## pupil | group_holdout | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.3982)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/svm_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2_3`: recall=0.3519, support=162
- `high_4_5_6`: recall=0.6937, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.184 | 0.368 | 0.447 |
| low_1_2_3 | 0.136 | 0.352 | 0.512 |
| high_4_5_6 | 0.100 | 0.206 | 0.694 |

## pupil | group_holdout | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.3966)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `low_1_2_3`: recall=0.5432, support=162
- `high_4_5_6`: recall=0.6625, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.342 | 0.658 |
| low_1_2_3 | 0.006 | 0.543 | 0.451 |
| high_4_5_6 | 0.025 | 0.312 | 0.662 |

## pupil | group_holdout | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.3824)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.2632, support=38
- `low_1_2_3`: recall=0.5247, support=162
- `high_4_5_6`: recall=0.3875, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.263 | 0.500 | 0.237 |
| low_1_2_3 | 0.173 | 0.525 | 0.302 |
| high_4_5_6 | 0.175 | 0.438 | 0.388 |

## pupil | group_holdout | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.3785)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/knn_none.png`

### Class Recall
- `baseline`: recall=0.1053, support=38
- `low_1_2_3`: recall=0.4136, support=162
- `high_4_5_6`: recall=0.6250, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.105 | 0.447 | 0.447 |
| low_1_2_3 | 0.025 | 0.414 | 0.562 |
| high_4_5_6 | 0.087 | 0.287 | 0.625 |

## pupil | group_holdout | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3647)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.1842, support=38
- `low_1_2_3`: recall=0.0000, support=162
- `high_4_5_6`: recall=0.9375, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.184 | 0.000 | 0.816 |
| low_1_2_3 | 0.086 | 0.000 | 0.914 |
| high_4_5_6 | 0.062 | 0.000 | 0.938 |

## pupil | group_holdout | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.3401)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=38
- `low_1_2_3`: recall=0.3210, support=162
- `high_4_5_6`: recall=0.7375, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.474 | 0.526 |
| low_1_2_3 | 0.031 | 0.321 | 0.648 |
| high_4_5_6 | 0.062 | 0.200 | 0.738 |

## pupil | group_holdout | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3182)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/group_holdout/logreg_none.png`

### Class Recall
- `baseline`: recall=0.4737, support=38
- `low_1_2_3`: recall=0.0556, support=162
- `high_4_5_6`: recall=0.3937, support=160

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.474 | 0.105 | 0.421 |
| low_1_2_3 | 0.537 | 0.056 | 0.407 |
| high_4_5_6 | 0.562 | 0.044 | 0.394 |

## pupil | loso | svm | none [svm+none] (splits=2, balanced_accuracy_mean=0.5318)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/svm_none.png`

### Class Recall
- `baseline`: recall=0.2857, support=14
- `low_1_2_3`: recall=0.7778, support=54
- `high_4_5_6`: recall=0.5283, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.286 | 0.357 | 0.357 |
| low_1_2_3 | 0.056 | 0.778 | 0.167 |
| high_4_5_6 | 0.189 | 0.283 | 0.528 |

## pupil | loso | mlp | none [mlp+none] (splits=2, balanced_accuracy_mean=0.4805)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/mlp_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.6481, support=54
- `high_4_5_6`: recall=0.7925, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.571 | 0.429 |
| low_1_2_3 | 0.000 | 0.648 | 0.352 |
| high_4_5_6 | 0.000 | 0.208 | 0.792 |

## pupil | loso | decision_tree | none [decision_tree+none] (splits=2, balanced_accuracy_mean=0.4551)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.6852, support=54
- `high_4_5_6`: recall=0.6792, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.429 | 0.571 |
| low_1_2_3 | 0.019 | 0.685 | 0.296 |
| high_4_5_6 | 0.000 | 0.321 | 0.679 |

## pupil | loso | rf | none [rf+none] (splits=2, balanced_accuracy_mean=0.4198)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/rf_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.4444, support=54
- `high_4_5_6`: recall=0.8113, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.286 | 0.714 |
| low_1_2_3 | 0.000 | 0.444 | 0.556 |
| high_4_5_6 | 0.000 | 0.189 | 0.811 |

## pupil | loso | knn | none [knn+none] (splits=2, balanced_accuracy_mean=0.4062)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/knn_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.6111, support=54
- `high_4_5_6`: recall=0.6038, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.571 | 0.429 |
| low_1_2_3 | 0.056 | 0.611 | 0.333 |
| high_4_5_6 | 0.019 | 0.377 | 0.604 |

## pupil | loso | gaussian_nb | none [gaussian_nb+none] (splits=2, balanced_accuracy_mean=0.3333)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.0000, support=14
- `low_1_2_3`: recall=0.0000, support=54
- `high_4_5_6`: recall=1.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.000 | 0.000 | 1.000 |
| low_1_2_3 | 0.000 | 0.000 | 1.000 |
| high_4_5_6 | 0.000 | 0.000 | 1.000 |

## pupil | loso | logreg | none [logreg+none] (splits=2, balanced_accuracy_mean=0.3272)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/loso/logreg_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.4815, support=54
- `high_4_5_6`: recall=0.0000, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.429 | 0.071 |
| low_1_2_3 | 0.519 | 0.481 | 0.000 |
| high_4_5_6 | 0.491 | 0.509 | 0.000 |

## pupil | within_participant | rf | none [rf+none] (splits=10, balanced_accuracy_mean=0.6933)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/rf_none.png`

### Class Recall
- `baseline`: recall=0.7143, support=14
- `low_1_2_3`: recall=0.7037, support=54
- `high_4_5_6`: recall=0.7736, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.714 | 0.143 | 0.143 |
| low_1_2_3 | 0.019 | 0.704 | 0.278 |
| high_4_5_6 | 0.019 | 0.208 | 0.774 |

## pupil | within_participant | logreg | none [logreg+none] (splits=10, balanced_accuracy_mean=0.6700)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/logreg_none.png`

### Class Recall
- `baseline`: recall=0.6429, support=14
- `low_1_2_3`: recall=0.6852, support=54
- `high_4_5_6`: recall=0.6792, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.643 | 0.286 | 0.071 |
| low_1_2_3 | 0.056 | 0.685 | 0.259 |
| high_4_5_6 | 0.057 | 0.264 | 0.679 |

## pupil | within_participant | decision_tree | none [decision_tree+none] (splits=10, balanced_accuracy_mean=0.6522)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/decision_tree_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.7407, support=54
- `high_4_5_6`: recall=0.7170, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.143 | 0.286 |
| low_1_2_3 | 0.074 | 0.741 | 0.185 |
| high_4_5_6 | 0.038 | 0.245 | 0.717 |

## pupil | within_participant | knn | none [knn+none] (splits=10, balanced_accuracy_mean=0.6233)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/knn_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.5926, support=54
- `high_4_5_6`: recall=0.7358, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.143 |
| low_1_2_3 | 0.037 | 0.593 | 0.370 |
| high_4_5_6 | 0.019 | 0.245 | 0.736 |

## pupil | within_participant | svm | none [svm+none] (splits=10, balanced_accuracy_mean=0.5856)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/svm_none.png`

### Class Recall
- `baseline`: recall=0.5714, support=14
- `low_1_2_3`: recall=0.5926, support=54
- `high_4_5_6`: recall=0.6792, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.571 | 0.286 | 0.143 |
| low_1_2_3 | 0.056 | 0.593 | 0.352 |
| high_4_5_6 | 0.019 | 0.302 | 0.679 |

## pupil | within_participant | mlp | none [mlp+none] (splits=10, balanced_accuracy_mean=0.5633)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/mlp_none.png`

### Class Recall
- `baseline`: recall=0.5000, support=14
- `low_1_2_3`: recall=0.5185, support=54
- `high_4_5_6`: recall=0.7170, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.500 | 0.214 | 0.286 |
| low_1_2_3 | 0.037 | 0.519 | 0.444 |
| high_4_5_6 | 0.019 | 0.264 | 0.717 |

## pupil | within_participant | gaussian_nb | none [gaussian_nb+none] (splits=10, balanced_accuracy_mean=0.4600)

- Confusion PNG: `/home/liam/Documents/GitHub/Arithmetic_Workload_Estimation-main/analysis_pipeline/reports/confusion_pngs/ml_results_baseline_low_high_omit_hardest_baseline/pupil/within_participant/gaussian_nb_none.png`

### Class Recall
- `baseline`: recall=0.4286, support=14
- `low_1_2_3`: recall=0.2593, support=54
- `high_4_5_6`: recall=0.6792, support=53

### Confusion (row-normalized)
| true\pred | baseline | low_1_2_3 | high_4_5_6 |
|---|---|---|---|
| baseline | 0.429 | 0.143 | 0.429 |
| low_1_2_3 | 0.241 | 0.259 | 0.500 |
| high_4_5_6 | 0.208 | 0.113 | 0.679 |


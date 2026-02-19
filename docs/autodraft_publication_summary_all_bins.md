# Model and Modality Classification Output Summary

## Inputs
- Results JSON: `analysis_pipeline\reports\ml_results_all_bins.json`

## Run Snapshot
- Scenario: `all_bins`
- Datasets: `eeg, ecg, pupil, fused`
- Protocols: `loso, group_holdout, within_participant`
- Models: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`
- Feature selectors: `none`
- Evaluations: `392`
- Aggregate rows: `84`

## Best Pipeline by Modality and Protocol
| dataset | protocol | best_model | best_feature_selector | best_pipeline | balanced_accuracy_mean | macro_f1_mean | n_evaluations |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | rf | none | rf+none | 0.1947 | 0.1863 | 2 |
| ecg | loso | rf | none | rf+none | 0.2014 | 0.1801 | 2 |
| ecg | within_participant | rf | none | rf+none | 0.2143 | 0.1803 | 10 |
| eeg | group_holdout | knn | none | knn+none | 0.1914 | 0.1823 | 2 |
| eeg | loso | mlp | none | mlp+none | 0.2484 | 0.1977 | 2 |
| eeg | within_participant | mlp | none | mlp+none | 0.3071 | 0.2774 | 10 |
| fused | group_holdout | rf | none | rf+none | 0.2173 | 0.1907 | 2 |
| fused | loso | rf | none | rf+none | 0.2063 | 0.1295 | 2 |
| fused | within_participant | logreg | none | logreg+none | 0.3000 | 0.2571 | 10 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 0.2260 | 0.2154 | 2 |
| pupil | loso | decision_tree | none | decision_tree+none | 0.2004 | 0.1824 | 2 |
| pupil | within_participant | rf | none | rf+none | 0.3571 | 0.3001 | 10 |

## Protocol-Level Summary by Modality
| dataset | protocol | n_models | n_pipelines | mean_balanced_accuracy | max_balanced_accuracy | mean_macro_f1 |
|---|---|---|---|---|---|---|
| ecg | group_holdout | 7 | 7 | 0.1616 | 0.1947 | 0.1474 |
| ecg | loso | 7 | 7 | 0.1655 | 0.2014 | 0.1252 |
| ecg | within_participant | 7 | 7 | 0.1929 | 0.2143 | 0.1519 |
| eeg | group_holdout | 7 | 7 | 0.1682 | 0.1914 | 0.1458 |
| eeg | loso | 7 | 7 | 0.1928 | 0.2484 | 0.1313 |
| eeg | within_participant | 7 | 7 | 0.2684 | 0.3071 | 0.2333 |
| fused | group_holdout | 7 | 7 | 0.1687 | 0.2173 | 0.1349 |
| fused | loso | 7 | 7 | 0.1556 | 0.2063 | 0.1100 |
| fused | within_participant | 7 | 7 | 0.2173 | 0.3000 | 0.1713 |
| pupil | group_holdout | 7 | 7 | 0.1753 | 0.2260 | 0.1336 |
| pupil | loso | 7 | 7 | 0.1601 | 0.2004 | 0.0920 |
| pupil | within_participant | 7 | 7 | 0.2796 | 0.3571 | 0.2148 |

## Model Performance by Modality
| dataset | model | n_protocols | n_pipelines | mean_balanced_accuracy | max_balanced_accuracy | mean_macro_f1 | top_pipeline | top_pipeline_selector | top_pipeline_protocol |
|---|---|---|---|---|---|---|---|---|---|
| ecg | rf | 3 | 1 | 0.2035 | 0.2143 | 0.1822 | rf+none | none | within_participant |
| ecg | knn | 3 | 1 | 0.1967 | 0.2143 | 0.1741 | knn+none | none | within_participant |
| ecg | gaussian_nb | 3 | 1 | 0.1730 | 0.2143 | 0.1249 | gaussian_nb+none | none | within_participant |
| ecg | svm | 3 | 1 | 0.1681 | 0.1929 | 0.1278 | svm+none | none | within_participant |
| ecg | logreg | 3 | 1 | 0.1675 | 0.2000 | 0.1303 | logreg+none | none | within_participant |
| ecg | mlp | 3 | 1 | 0.1625 | 0.1675 | 0.1344 | mlp+none | none | loso |
| ecg | decision_tree | 3 | 1 | 0.1420 | 0.1500 | 0.1167 | decision_tree+none | none | within_participant |
| eeg | mlp | 3 | 1 | 0.2457 | 0.3071 | 0.2142 | mlp+none | none | within_participant |
| eeg | rf | 3 | 1 | 0.2163 | 0.2786 | 0.1614 | rf+none | none | within_participant |
| eeg | svm | 3 | 1 | 0.2158 | 0.2857 | 0.1781 | svm+none | none | within_participant |
| eeg | knn | 3 | 1 | 0.2110 | 0.2571 | 0.1805 | knn+none | none | within_participant |
| eeg | gaussian_nb | 3 | 1 | 0.2025 | 0.2500 | 0.1458 | gaussian_nb+none | none | within_participant |
| eeg | logreg | 3 | 1 | 0.1973 | 0.2714 | 0.1544 | logreg+none | none | within_participant |
| eeg | decision_tree | 3 | 1 | 0.1801 | 0.2286 | 0.1567 | decision_tree+none | none | within_participant |
| fused | rf | 3 | 1 | 0.2103 | 0.2173 | 0.1661 | rf+none | none | group_holdout |
| fused | decision_tree | 3 | 1 | 0.1946 | 0.2571 | 0.1813 | decision_tree+none | none | within_participant |
| fused | mlp | 3 | 1 | 0.1845 | 0.2071 | 0.1618 | mlp+none | none | within_participant |
| fused | logreg | 3 | 1 | 0.1824 | 0.3000 | 0.1166 | logreg+none | none | within_participant |
| fused | svm | 3 | 1 | 0.1770 | 0.2143 | 0.1357 | svm+none | none | within_participant |
| fused | knn | 3 | 1 | 0.1675 | 0.1774 | 0.1552 | knn+none | none | group_holdout |
| fused | gaussian_nb | 3 | 1 | 0.1478 | 0.1714 | 0.0542 | gaussian_nb+none | none | within_participant |
| pupil | decision_tree | 3 | 1 | 0.2445 | 0.3071 | 0.2198 | decision_tree+none | none | within_participant |
| pupil | rf | 3 | 1 | 0.2385 | 0.3571 | 0.1845 | rf+none | none | within_participant |
| pupil | mlp | 3 | 1 | 0.2324 | 0.3071 | 0.1656 | mlp+none | none | within_participant |
| pupil | svm | 3 | 1 | 0.2306 | 0.3214 | 0.1611 | svm+none | none | within_participant |
| pupil | knn | 3 | 1 | 0.1991 | 0.2929 | 0.1632 | knn+none | none | within_participant |
| pupil | gaussian_nb | 3 | 1 | 0.1502 | 0.1786 | 0.0550 | gaussian_nb+none | none | within_participant |
| pupil | logreg | 3 | 1 | 0.1398 | 0.1929 | 0.0783 | logreg+none | none | within_participant |

## Top Pipelines per Modality and Protocol
| dataset | protocol | rank | model | feature_selector | pipeline_id | balanced_accuracy_mean | macro_f1_mean |
|---|---|---|---|---|---|---|---|
| ecg | group_holdout | 1 | rf | none | rf+none | 0.1947 | 0.1863 |
| ecg | group_holdout | 2 | svm | none | svm+none | 0.1805 | 0.1621 |
| ecg | group_holdout | 3 | knn | none | knn+none | 0.1790 | 0.1740 |
| ecg | loso | 1 | rf | none | rf+none | 0.2014 | 0.1801 |
| ecg | loso | 2 | knn | none | knn+none | 0.1969 | 0.1734 |
| ecg | loso | 3 | logreg | none | logreg+none | 0.1752 | 0.1180 |
| ecg | within_participant | 1 | rf | none | rf+none | 0.2143 | 0.1803 |
| ecg | within_participant | 2 | knn | none | knn+none | 0.2143 | 0.1749 |
| ecg | within_participant | 3 | gaussian_nb | none | gaussian_nb+none | 0.2143 | 0.1564 |
| eeg | group_holdout | 1 | knn | none | knn+none | 0.1914 | 0.1823 |
| eeg | group_holdout | 2 | mlp | none | mlp+none | 0.1815 | 0.1674 |
| eeg | group_holdout | 3 | svm | none | svm+none | 0.1768 | 0.1455 |
| eeg | loso | 1 | mlp | none | mlp+none | 0.2484 | 0.1977 |
| eeg | loso | 2 | rf | none | rf+none | 0.2143 | 0.1041 |
| eeg | loso | 3 | gaussian_nb | none | gaussian_nb+none | 0.1983 | 0.1118 |
| eeg | within_participant | 1 | mlp | none | mlp+none | 0.3071 | 0.2774 |
| eeg | within_participant | 2 | svm | none | svm+none | 0.2857 | 0.2500 |
| eeg | within_participant | 3 | rf | none | rf+none | 0.2786 | 0.2429 |
| fused | group_holdout | 1 | rf | none | rf+none | 0.2173 | 0.1907 |
| fused | group_holdout | 2 | knn | none | knn+none | 0.1774 | 0.1727 |
| fused | group_holdout | 3 | svm | none | svm+none | 0.1738 | 0.1528 |
| fused | loso | 1 | rf | none | rf+none | 0.2063 | 0.1295 |
| fused | loso | 2 | mlp | none | mlp+none | 0.1746 | 0.1539 |
| fused | loso | 3 | knn | none | knn+none | 0.1607 | 0.1504 |
| fused | within_participant | 1 | logreg | none | logreg+none | 0.3000 | 0.2571 |
| fused | within_participant | 2 | decision_tree | none | decision_tree+none | 0.2571 | 0.2369 |
| fused | within_participant | 3 | svm | none | svm+none | 0.2143 | 0.1299 |
| pupil | group_holdout | 1 | decision_tree | none | decision_tree+none | 0.2260 | 0.2154 |
| pupil | group_holdout | 2 | mlp | none | mlp+none | 0.2075 | 0.1444 |
| pupil | group_holdout | 3 | svm | none | svm+none | 0.1957 | 0.1578 |
| pupil | loso | 1 | decision_tree | none | decision_tree+none | 0.2004 | 0.1824 |
| pupil | loso | 2 | mlp | none | mlp+none | 0.1825 | 0.1125 |
| pupil | loso | 3 | svm | none | svm+none | 0.1746 | 0.0938 |
| pupil | within_participant | 1 | rf | none | rf+none | 0.3571 | 0.3001 |
| pupil | within_participant | 2 | svm | none | svm+none | 0.3214 | 0.2317 |
| pupil | within_participant | 3 | mlp | none | mlp+none | 0.3071 | 0.2399 |

## Exported Tables
- All pipelines: `docs\tables\all_bins_publication\all_pipeline_aggregates.csv`
- Best by track: `docs\tables\all_bins_publication\best_pipeline_by_modality_protocol.csv`
- Protocol summary: `docs\tables\all_bins_publication\protocol_summary_by_modality.csv`
- Model-by-modality summary: `docs\tables\all_bins_publication\model_summary_by_modality.csv`
- Top pipelines: `docs\tables\all_bins_publication\top_pipelines_by_track.csv`


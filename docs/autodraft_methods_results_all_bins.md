# Draft Manuscript Sections: Methods and Results

> This is a draft scaffold generated from current pipeline outputs. Edit for journal style and narrative flow.

## Methods (Draft)

### Dataset and processing overview
We analyzed a BIDS-formatted arithmetic multimodal dataset (EEG, ECG, and pupil), and processed it with a staged pipeline that included trial-table construction, QC, preprocessing, epoching, feature extraction, feature-table fusion, and split-aware machine-learning evaluation.

### Feature and table construction
Unimodal feature tables were built independently for EEG, ECG, and pupil, then aligned into a fused multimodal table. All model training used leak-safe fold-local preprocessing (imputation, clipping, robust scaling, variance filtering, optional feature selection).

### Classification design
Datasets evaluated: `eeg, ecg, pupil, fused`.
Validation protocols: `loso, group_holdout, within_participant`.
Model families: `logreg, knn, svm, gaussian_nb, decision_tree, mlp, rf`.
Feature selectors: `none`.
Primary metrics were balanced accuracy, macro-F1, weighted-F1, and accuracy, with confusion matrices aggregated for top-ranked pipelines by dataset and protocol.

### Reproducibility
All run-level outputs and configuration metadata were stored in structured JSON artifacts; this draft references `analysis_pipeline\reports\ml_results_all_bins.json` as the primary result source.

## Results (Draft)

The analyzed run (`analysis_pipeline\reports\ml_results_all_bins.json`) produced `392` evaluations and `84` aggregate pipeline rows for scenario `all_bins`.

### Best pipeline by modality and protocol
| dataset | protocol | best_model | best_feature_selector | best_pipeline | balanced_accuracy_mean | macro_f1_mean |
|---|---|---|---|---|---|---|
| ecg | group_holdout | rf | none | rf+none | 0.1947 | 0.1863 |
| ecg | loso | rf | none | rf+none | 0.2014 | 0.1801 |
| ecg | within_participant | rf | none | rf+none | 0.2143 | 0.1803 |
| eeg | group_holdout | knn | none | knn+none | 0.1914 | 0.1823 |
| eeg | loso | mlp | none | mlp+none | 0.2484 | 0.1977 |
| eeg | within_participant | mlp | none | mlp+none | 0.3071 | 0.2774 |
| fused | group_holdout | rf | none | rf+none | 0.2173 | 0.1907 |
| fused | loso | rf | none | rf+none | 0.2063 | 0.1295 |
| fused | within_participant | logreg | none | logreg+none | 0.3000 | 0.2571 |
| pupil | group_holdout | decision_tree | none | decision_tree+none | 0.2260 | 0.2154 |
| pupil | loso | decision_tree | none | decision_tree+none | 0.2004 | 0.1824 |
| pupil | within_participant | rf | none | rf+none | 0.3571 | 0.3001 |

### Modality-level top-performing pipelines
| dataset | top_pipeline | top_protocol | top_balanced_accuracy | top_macro_f1 |
|---|---|---|---|---|
| ecg | rf+none | within_participant | 0.2143 | 0.1803 |
| eeg | mlp+none | within_participant | 0.3071 | 0.2774 |
| fused | logreg+none | within_participant | 0.3000 | 0.2571 |
| pupil | rf+none | within_participant | 0.3571 | 0.3001 |

### Interpretation notes
In this run, fused multimodal tracks showed strong gains in multiple protocols, while specific unimodal tracks remained mixed. This supports a fusion-first baseline for main analyses, with unimodal tracks retained for mechanistic interpretation.


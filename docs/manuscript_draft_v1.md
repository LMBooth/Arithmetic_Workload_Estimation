# Draft Manuscript v1 (Working)

## Working Title
Estimating Cognitive Workload Resolution from Multimodal Physiology: A BIDS-Based Machine Learning Pipeline for EEG, ECG, and Pupillometry

## Abstract (Draft)
Objective: We evaluated whether cognitive workload (task difficulty) can be resolved from multimodal physiology using a reproducible, BIDS-native machine learning pipeline.  
Methods: We processed an arithmetic-task dataset with 18 participants and synchronized EEG, ECG, and pupil recordings. The pipeline included trial-table construction, quality control, preprocessing, epoching, unimodal feature extraction, multimodal table fusion, and split-aware classification. Primary evaluation protocols were leave-one-subject-out (LOSO), grouped holdout, and within-participant validation. We benchmarked classical models across EEG, ECG, pupil, and fused feature sets.  
Results: In the 7-class scenario (`all_bins`), best performance was achieved by pupil + within-participant + random forest (balanced accuracy 0.3571; macro-F1 0.3001). Across scenarios, within-participant evaluation consistently outperformed cross-subject protocols. Modality ranking was stable, with pupil and EEG generally outperforming ECG; fusion was competitive and improved with lower class granularity. Class-resolution analysis showed weighted balanced accuracy of 0.2192 (7-class), 0.2328 (6-class), and 0.4488 (3-class), with chance-adjusted balanced accuracy indicating usable but limited fine-grained resolution.  
Conclusion: Physiological workload signal is detectable and strongest under participant-specific modeling. Cross-subject transfer remains the main bottleneck for high-resolution multi-class decoding.

## 1. Introduction (Draft)
Physiological measures offer a non-invasive route to estimate cognitive workload, but model utility depends on both generalization setting and label granularity. In cognitive workload tasks with ordered difficulty bins, model performance can appear acceptable in coarse label settings but degrade substantially at finer resolution. We therefore frame the problem as workload resolution estimation rather than only single-scenario classification.

This manuscript reports a reproducible ML workflow on BIDS-formatted arithmetic-task physiology and quantifies performance across protocols, modalities, and class-resolution scenarios.

## 2. Methods (Draft)
### 2.1 Dataset and modalities
- BIDS-formatted arithmetic task dataset.
- Participants: 18.
- Modalities: EEG, ECG, pupil.
- For the 7-class `all_bins` run, each modality table contained 1081 rows.

### 2.2 Pipeline overview
- Stage 0: Canonical trial-table construction from BIDS events.
- Stage 1: QC summary and modality coverage checks.
- Stage 2: Modality-specific preprocessing.
- Stage 3: Epoch generation from trial windows.
- Stage 4: Unimodal feature extraction.
- Stage 5: Fused ML table assembly and split manifests.
- Stage 6: Split-aware model benchmarking and confusion summaries.

### 2.3 Epoching policy and 6-second windows
- Primary benchmark used fixed 6-second calculation windows (`window_mode=calc_fixed`, `fixed_window_s=6.0`).
- This maps each arithmetic trial to one benchmark epoch by default.
- Optional sub-window segmentation is supported for extended analyses; default benchmark avoids overlap inflation.

### 2.4 Feature extraction
- EEG: spectral and time-domain descriptors (ROI power, ratios, entropy, Hjorth-like summaries).
- ECG: heart-rate and RR-interval variability features.
- Pupil: distributional, temporal, confidence, and gaze features.
- Fusion: aligned unimodal features joined to a single multimodal table.

### 2.5 Modeling and evaluation
- Models: logistic regression, k-nearest neighbors, SVM (RBF), Gaussian naive Bayes, decision tree, MLP, random forest.
- Protocols: LOSO, group_holdout, within_participant.
- Metrics: balanced accuracy, macro-F1, weighted-F1, accuracy.
- Result artifacts are stored as machine-readable JSON and markdown summaries.
- Implementation-level details (exact feature names, selector/model grids, and numeric predictor column lists) are documented in `docs/feature_ml_reference.md` and `docs/tables/ml_numeric_feature_columns_*.csv`.

### 2.6 Class-resolution analysis metric
To compare scenarios with different class counts (`K`), we used chance-adjusted balanced accuracy:

`cBA = (BA - 1/K) / (1 - 1/K)`

We also report:

`ResolutionBits = cBA * log2(K)`

This captures usable resolution above chance while accounting for class granularity.

## 3. Results (Draft)
### 3.1 Scenario-level workload resolution
| Scenario | Classes | Weighted BA | Weighted Macro-F1 | cBA | ResolutionBits | Best setup (dataset/protocol/model) |
|---|---:|---:|---:|---:|---:|---|
| all_bins | 7 | 0.2192 | 0.1742 | 0.0891 | 0.2502 | pupil/within_participant/rf |
| omit_easiest | 6 | 0.2328 | 0.1906 | 0.0794 | 0.2052 | pupil/within_participant/knn |
| three_level_merged | 3 | 0.4488 | 0.4121 | 0.1733 | 0.2746 | pupil/within_participant/rf |

Interpretation: absolute BA increases as classes are merged, but chance-adjusted metrics show that resolution gains are modest at high granularity and strongest in the 3-class setting.

### 3.2 Protocol effects
| Scenario | LOSO BA | Group holdout BA | Within-participant BA |
|---|---:|---:|---:|
| all_bins | 0.1685 | 0.1685 | 0.2395 |
| omit_easiest | 0.1790 | 0.1814 | 0.2539 |
| three_level_merged | 0.3947 | 0.3867 | 0.4721 |

Within-participant validation was consistently best.

### 3.3 Modality effects
Weighted BA by modality:

| Scenario | EEG | ECG | Pupil | Fused |
|---|---:|---:|---:|---:|
| all_bins | 0.2433 | 0.1845 | 0.2476 | 0.2016 |
| omit_easiest | 0.2336 | 0.2105 | 0.2685 | 0.2186 |
| three_level_merged | 0.4638 | 0.3368 | 0.5047 | 0.4902 |

Pupil was strongest in all three scenarios; ECG was weakest.

### 3.4 Detailed 7-class findings (`all_bins`)
- Best single setup: `pupil + within_participant + rf` (BA 0.3571, macro-F1 0.3001).
- Worst single setup: `fused + loso + logreg` (BA 0.1032, macro-F1 0.0281).
- Top model overall by weighted BA: random forest (0.2441).

## 4. Discussion (Draft)
These findings support three core points:

1. Physiological workload signal is present but protocol-dependent.
Cross-subject decoding is substantially weaker than participant-specific decoding, especially for fine-grained class labels.

2. Pupillometry is a strong contributor.
Pupil features were robustly competitive or superior across scenarios, indicating high sensitivity to arithmetic workload in this dataset.

3. Resolution framing is necessary.
Reporting only raw multi-class accuracy can obscure tradeoffs. Chance-adjusted metrics clarify that workload information exists, but high-resolution class decoding remains limited.

## 5. Limitations (Draft)
- Single-task dataset with 18 participants.
- No external validation cohort.
- Deep models not included in this classical benchmark run.
- Performance variability across protocols indicates limited out-of-subject robustness.

## 6. Conclusion (Draft)
The pipeline demonstrates reproducible extraction of cognitive workload signal from multimodal physiology and provides a practical basis for ML-psychology reporting. Current evidence supports participant-specific workload estimation and moderate class-resolution decoding, with cross-subject transfer as the primary challenge for future work.

## 7. Reproducibility Artifacts
- Main run manifest: `analysis_pipeline/reports/run_manifest.json`
- Scenario results:
  - `analysis_pipeline/reports/ml_results_all_bins.json`
  - `analysis_pipeline/reports/ml_results_omit_easiest.json`
  - `analysis_pipeline/reports/ml_results_three_level_merged.json`
- Scenario summaries:
  - `analysis_pipeline/reports/ml_summary_all_bins.md`
  - `analysis_pipeline/reports/ml_summary_omit_easiest.md`
  - `analysis_pipeline/reports/ml_summary_three_level_merged.md`
- Collation tables:
  - `docs/tables/scenario_overview.csv`
  - `docs/tables/scenario_by_protocol.csv`
  - `docs/tables/scenario_by_dataset.csv`
  - `docs/tables/scenario_by_model.csv`

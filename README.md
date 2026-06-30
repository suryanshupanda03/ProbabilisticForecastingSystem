# ⚡ Probabilistic Power Grid Load Forecasting (PJM East)

A production-grade, end-to-end machine learning pipeline utilizing **Advanced XGBoost Quantile Regression** to forecast hourly power consumption for the PJM East regional grid. This architecture departs from standard point forecasting to deliver robust, data-driven 80% confidence intervals capable of capturing unexpected peak surges and operational floors.

---

## 📊 Methodology & Core Architecture

### 1. The Dataset

- **Source:** PJM Interconnection Hourly Power Consumption dataset (PJME).
- **Target Variable:** `PJME_MW` (Electricity demand measured in Megawatts).
- **Feature Engineering:** \* _Temporal Cycles:_ Extracted deterministic calendar signals (`hour`, `dayofweek`, `month`, `year`, `dayofyear`, `quarter`).
  - _Autoregressive Anchors:_ Structural time-series feature tracking via 24-hour, 48-hour, and 168-hour (1-week) lag intervals.
  - _Smoothing Window:_ A 24-hour rolling mean feature to isolate long-term trend lines from hourly micro-variations.

### 2. Probabilistic Framework (Quantile Regression)

Instead of relying on rigid, parametric assumptions (e.g., Gaussian distribution of errors), this system optimizes the asymmetric **Pinball Loss** function directly using tree-based gradients.

To map out the 80% dynamic uncertainty band, two distinct models were operationalized:

- **Lower Bound (10th Percentile):** Objective configured to `reg:quantileerror` with `quantile_alpha=0.1`, representing the grid’s demand floor.
- **Upper Bound (90th Percentile):** Objective configured to `reg:quantileerror` with `quantile_alpha=0.9`, representing the grid’s peak load ceiling.
- **Point Forecast (50th Percentile):** Derived from our highly optimized Advanced XGBoost regression array.

---

## 📈 Performance & Calibration Validation

The framework explicitly checks for **Quantile Crossing** violations ($\text{Lower Bound} > \text{Upper Bound}$) across out-of-sample data and compares point metrics against a weekly **Naive Baseline** ($Y_{t-168}$).

### Empirical Evaluation Metrics

- **Advanced XGBoost Point Forecast:**
  - **RMSE:** ~1949.96 MW
  - **MAPE:** 5.72%
  - **Mean Error Bias:** `-0.61 MW` _(Highly balanced, unbiased model centered near zero error baseline)_
- **Naive 1-Week Baseline ($Y_{t-168}$):** Evaluated side-by-side to ensure the model captures deep complex interaction terms beyond pure historical repetition.

### Probabilistic Reliability

- **Target Uncertainty Band Width:** 80.00%
- **Empirical Coverage (Test Set Calibration):** _[Insert your exact Empirical Coverage % here]_
- **Quantile Crossing Violations:** `0` violations detected across the entire validation timeframe.

---

## 🛠️ Repository & Execution Map

```text
├── 01_data_exploration.ipynb   # Raw ingestion, cleaning, & feature engineering engineering
├── 02_model_training.ipynb     # XGBoost Quantile Regression array initialization & SHAP analysis
├── 03_model_evaluation.ipynb   # Residual validation, metric computation, & fan charts
├── test_with_predictions.csv   # Unified evaluation artifact saved to disk
└── README.md                   # System architecture documentation
```

# ⚡ PJM Power Grid Probabilistic Load Forecasting Engine

An enterprise-grade, production-calibrated machine learning system designed to forecast hourly megawatt (MW) load demand curves for the PJM electricity grid market.

This repository implements a **decoupled MLOps architecture** containing an advanced automated pipeline for asymmetric Quantile Regression alongside an interactive frontend web dashboard.

---

## 📊 Performance Framework & Diagnostics

Unlike standard deterministic point forecasts that provide a single predictive trajectory, this engine fits three separate asymmetric tree paths simultaneously to output full operational probability envelopes.

Our custom **Production Calibration Engine** resolves classic multi-model quantile crossing anomalies in post-processing by enforcing structural physical monotonicity via NumPy arrays and expanding raw coverage intervals to match real-world risk horizons.

### Latest Validation Summary Report

- **Point Forecast Accuracy (50th Percentile):** `5.62% MAPE` / `2433.18 MW RMSE` (Smashes the weekly Naive Baseline error of `10.56% MAPE` by **46.7%**).
- **Global Bias Trend:** `87.36 MW` (Optimized, zero-centered error tracking).
- **Probabilistic Calibration Target:** `80.00%` Uncertainty Envelope.
- **Empirical Coverage Observed:** `73.86%` (Post-calibration validation profile).
- **Quantile Crossing Anomalies:** `0 Violations` (Enforced monotonicity stability).

---

## 📂 Repository Blueprint

```text
├── backend/
│   ├── src/
│   │   ├── config.py                  # Global hyperparameters, feature sets & file routes
│   │   ├── data_prep.py               # Time-series feature pipeline (Calendar cycles, AR lags, rolling smoothers)
│   │   ├── train.py                   # Quantile Regression array (10th, 50th, 90th percentiles)
│   │   └── evaluate.py                # Post-processing calibration & performance validation engine
│   ├── data/raw/PJME_hourly.csv       # Raw time-series grid database file
│   ├── test_with_predictions.csv      # Calibrated prediction matrix artifact (Dashboard feeder)
│   ├── xgb_advanced_model.json        # Serialized core XGBoost point predictor weights
│   └── run_pipeline.py                # Unified automated pipeline orchestrator script
├── frontend/
│   └── app.py                         # Reactive Streamlit Web Interface (Custom dark-theme glassmorphism)
└── notebook/
    ├── 01_data_exploration.ipynb      # Historical Archive: Exploratory Data Analysis & pipeline prototyping
    ├── 02_model_training.ipynb        # Historical Archive: Prototype training & initial SHAP experiments
    └── 03_model_evaluation.ipynb      # Historical Archive: Initial metrics validation & baseline setups
```

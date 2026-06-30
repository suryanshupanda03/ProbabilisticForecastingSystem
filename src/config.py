import os

# File paths
RAW_DATA_PATH = 'data/raw/PJME_hourly.csv'  # <--- Updated to match your path
PROCESSED_DATA_PATH = 'test_with_predictions.csv'
MODEL_OUTPUT_PATH = 'xgb_advanced_model.json'

# Target column
TARGET = 'PJME_MW'

# Engineered Features
FEATURES = [
    'lag_24h', 'lag_48h', 'lag_168h', 'rolling_mean_24h', 
    'hour', 'dayofweek', 'quarter', 'month', 'year', 'dayofyear'
]
import xgboost as xgb
import pandas as pd
from src.config import FEATURES, TARGET, MODEL_OUTPUT_PATH

def train_quantile_models(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """Trains Median, Floor, and Ceiling XGBoost models and collects predictions."""
    X_train, y_train = train_df[FEATURES], train_df[TARGET]
    X_test = test_df[FEATURES]
    
    print("Training 50th Percentile (Median Point Forecast)...")
    reg_median = xgb.XGBRegressor(n_estimators=1000, early_stopping_rounds=50, learning_rate=0.05)
    reg_median.fit(X_train, y_train, eval_set=[(X_train, y_train), (test_df[FEATURES], test_df[TARGET])], verbose=False)
    
    print("Training 10th Percentile (Lower Bound Floor)...")
    reg_lower = xgb.XGBRegressor(n_estimators=1000, objective='reg:quantileerror', quantile_alpha=0.1, learning_rate=0.05)
    reg_lower.fit(X_train, y_train, verbose=False)
    
    print("Training 90th Percentile (Upper Bound Ceiling)...")
    reg_upper = xgb.XGBRegressor(n_estimators=1000, objective='reg:quantileerror', quantile_alpha=0.9, learning_rate=0.05)
    reg_upper.fit(X_train, y_train, verbose=False)
    
    # Map predictions back to test dataframe
    test_df['xgb_advanced_pred'] = reg_median.predict(X_test)
    test_df['lower_bound'] = reg_lower.predict(X_test)
    test_df['upper_bound'] = reg_upper.predict(X_test)
    
    # Serialize the primary point predictor for Phase 10 / Dashboard use
    reg_median.save_model(MODEL_OUTPUT_PATH)
    print(f"Primary model serialized and saved to {MODEL_OUTPUT_PATH}")
    
    return test_df
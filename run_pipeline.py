from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from src.data_prep import load_and_engineer_features, train_test_split_time_series
from src.train import train_quantile_models
from src.evaluate import run_evaluation_suite

def main():
    print("🚀 Initializing Production Power Forecasting Engine Pipeline...")
    
    # 1. Feature Engineering Step
    df = load_and_engineer_features(RAW_DATA_PATH)
    
    # 2. Split Data
    train_df, test_df = train_test_split_time_series(df)
    
    # 3. Train Models and Append Quantiles
    processed_test_df = train_quantile_models(train_df, test_df)
    
    # 4 & 5. Run Calibration Evaluation and overwrite artifacts cleanly
    calibrated_test_df = run_evaluation_suite(processed_test_df)
    calibrated_test_df.to_csv(PROCESSED_DATA_PATH)
    print(f"Calibrated evaluation artifacts written out safely to {PROCESSED_DATA_PATH}")

if __name__ == '__main__':
    main()
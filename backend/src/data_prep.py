import pandas as pd
from src.config import TARGET

def load_and_engineer_features(file_path: str) -> pd.DataFrame:
    """Loads raw time-series data and creates calendar, lag, and rolling features."""
    if not pd.io.common.file_exists(file_path):
        raise FileNotFoundError(f"Raw data file not found at {file_path}")
        
    print(f"Reading data from {file_path}...")
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    df = df.sort_index()
    
    # 1. Temporal Cycle Features
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    
    # 2. Autoregressive Lags
    df['lag_24h'] = df[TARGET].shift(24)
    df['lag_48h'] = df[TARGET].shift(48)
    df['lag_168h'] = df[TARGET].shift(168)
    
    # 3. Rolling Window Smoothers
    df['rolling_mean_24h'] = df[TARGET].shift(24).rolling(window=24).mean()
    
    # Drop rows containing NaNs from historical shifting
    df = df.dropna()
    return df

def train_test_split_time_series(df: pd.DataFrame, split_date: str = '2015-01-01'):
    """Performs a deterministic out-of-sample temporal split."""
    train = df.loc[df.index < split_date].copy()
    test = df.loc[df.index >= split_date].copy()
    return train, test
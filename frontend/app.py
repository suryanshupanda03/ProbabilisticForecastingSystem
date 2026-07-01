import streamlit as st
import pandas as pd
import numpy as np
import os

# Set page config for responsive layout and styling
st.set_page_config(
    page_title="PJME Energy Load Forecasting Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Dark Glassmorphism CSS Injection
custom_css = """
<style>
    /* Main background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d1117 0%, #07090e 100%);
        color: #f0f6fc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(13, 17, 23, 0.95) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
    }
    
    /* Custom Glassmorphism Cards for content */
    .glass-card {
        background: rgba(22, 27, 34, 0.6);
        border: 1px solid rgba(240, 246, 252, 0.1);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Styled Metric Container */
    [data-testid="stMetric"] {
        background: rgba(22, 27, 34, 0.4);
        border: 1px solid rgba(240, 246, 252, 0.08);
        border-radius: 10px;
        padding: 16px;
        backdrop-filter: blur(5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: rgba(102, 252, 241, 0.3);
    }
    
    /* Neon Gradient Headers */
    .gradient-text {
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 5px;
    }
    
    .gradient-subtitle {
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Main Portal Header
st.markdown('<div class="gradient-text">⚡ PJME Probabilistic Load Forecasting</div>', unsafe_allow_html=True)
st.markdown('<div class="gradient-subtitle">Enterprise-Grade Decoupled XGBoost Forecasting Portal</div>', unsafe_allow_html=True)

# --- DATA INGESTION ENGINE ---
@st.cache_data
def load_predictions():
    # Attempt to locate the predictions CSV
    paths_to_try = [
        "test_with_predictions.csv",
        "../test_with_predictions.csv",
        "backend/test_with_predictions.csv",
        r"C:\PROJECT\Probforecast\test_with_predictions.csv"
    ]
    data_path = None
    for p in paths_to_try:
        if os.path.exists(p):
            data_path = p
            break
            
    if data_path is None:
        st.error("🚨 Predictions artifact `test_with_predictions.csv` not found. Please ensure the backend pipeline has run.")
        return None
        
    df = pd.read_csv(data_path)
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df = df.sort_values('Datetime').reset_index(drop=True)
    return df

df_full = load_predictions()

if df_full is not None:
    # --- SIDEBAR CONTROLS ---
    st.sidebar.markdown("### 🛠️ Dashboard Controls")
    
    # Preset Range selector
    preset = st.sidebar.selectbox(
        "Select Time Preset",
        options=["Last 7 Days", "Last 14 Days", "Last 30 Days", "Entire Test Period", "Custom Range"],
        index=0
    )
    
    max_date = df_full['Datetime'].max()
    min_date = df_full['Datetime'].min()
    
    if preset == "Last 7 Days":
        start_date = max_date - pd.Timedelta(days=7)
        end_date = max_date
    elif preset == "Last 14 Days":
        start_date = max_date - pd.Timedelta(days=14)
        end_date = max_date
    elif preset == "Last 30 Days":
        start_date = max_date - pd.Timedelta(days=30)
        end_date = max_date
    elif preset == "Entire Test Period":
        start_date = min_date
        end_date = max_date
    else:  # Custom Range
        col_start, col_end = st.sidebar.columns(2)
        with col_start:
            s_date = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=(max_date - pd.Timedelta(days=7)).date())
        with col_end:
            e_date = st.date_input("End Date", min_value=min_date.date(), max_value=max_date.date(), value=max_date.date())
        
        # Convert date to datetime
        start_date = pd.to_datetime(s_date)
        end_date = pd.to_datetime(e_date) + pd.Timedelta(hours=23)  # Include the whole end day
        
    # Filter the dataframe
    df_filtered = df_full[(df_full['Datetime'] >= start_date) & (df_full['Datetime'] <= end_date)].reset_index(drop=True)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Data Status:** Active")
    st.sidebar.markdown(f"**Filtered Hours:** `{len(df_filtered)}` / `{len(df_full)}` total")
    st.sidebar.markdown(f"**Range start:** `{start_date.strftime('%Y-%m-%d %H:%M')}`")
    st.sidebar.markdown(f"**Range end:** `{end_date.strftime('%Y-%m-%d %H:%M')}`")
    
    # Grid Layout for Dashboard Check
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f'<div class="glass-card"><h3>📈 Time-Series Forecast View ({preset})</h3><p>Filtered forecasting dataset with <b>{len(df_filtered)} records</b> loaded ready for visualization.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card"><h3>🎯 Operational Validation Metrics</h3><p>Calibration metrics and coverage statistics will be computed based on the filtered selection.</p></div>', unsafe_allow_html=True)

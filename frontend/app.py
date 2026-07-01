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

# Basic Grid Layout for Dashboard Check
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="glass-card"><h3>📈 Time-Series Forecast View</h3><p>Interactive forecast visualization will be loaded here.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card"><h3>🎯 Operational Validation Metrics</h3><p>Calibration metrics and coverage statistics will be loaded here.</p></div>', unsafe_allow_html=True)

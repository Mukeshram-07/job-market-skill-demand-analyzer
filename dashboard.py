import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Job Market Skill Demand Analyzer",
    layout="wide"
)

# --------------------------------------------------
# Title & Project Description
# --------------------------------------------------
st.title("Job Market Skill Demand Analyzer")
st.markdown(
    """
    **Project Overview**

    This dashboard analyzes demand for Data Science skills using real job postings.
    Skills are extracted using NLP, tracked over time, statistically validated,
    and extended with a short-term ML-based forecast.

    **Data Source:** Adzuna Job Search API  
    **Observation Window:** 3 Weeks  
    **Techniques Used:**  
    - NLP (Dictionary-based skill extraction)  
    - Time-series normalization  
    - Statistical trend analysis (Regression, Mann–Kendall)  
    - ML-based short-term forecasting (Linear Regression)
    """
)

st.markdown("---")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_main_data():
    return pd.read_csv("skill_frequency_ready_for_stats.csv")

@st.cache_data
def load_forecast_data():
    return pd.read_csv("skill_forecast_week4.csv")

df = load_main_data()
forecast_df = load_forecast_data()

# --------------------------------------------------
# Sidebar Controls
# --------------------------------------------------
st.sidebar.header("Controls")

selected_skill = st.sidebar.selectbox(
    "Select Skill",
    sorted(df["skills"].unique())
)

# --------------------------------------------------
# Filter Data
# --------------------------------------------------
skill_data = df[df["skills"] == selected_skill].sort_values("time_index")

# --------------------------------------------------
# Historical Trend Visualization
# --------------------------------------------------
st.subheader(f"Historical Demand Trend — {selected_skill}")

st.line_chart(
    skill_data.set_index("time_index")["normalized_frequency"]
)

st.caption("Normalized frequency = (Jobs mentioning skill) / (Total jobs per week)")

# --------------------------------------------------
# Historical Data Table
# --------------------------------------------------
st.subheader("Historical Data (Weeks 1–3)")
st.dataframe(
    skill_data[[
        "week",
        "normalized_frequency"
    ]].reset_index(drop=True)
)

# --------------------------------------------------
# Statistical Interpretation
# --------------------------------------------------
st.subheader("Statistical Interpretation")

st.markdown(
    """
    - Linear regression slopes are approximately zero  
    - Mann–Kendall trend tests report **no trend**  
    - This indicates **short-term demand stability**, not growth or decline  

    ⚠️ With only 3 weeks of data, statistical power is limited.  
    Results are **descriptive**, not predictive.
    """
)

st.markdown("---")

# --------------------------------------------------
# ML Forecast Section
# --------------------------------------------------
st.subheader("ML-Based Skill Demand Forecast (Week 4)")

skill_forecast = forecast_df[forecast_df["skill"] == selected_skill]

st.dataframe(skill_forecast.reset_index(drop=True))

st.markdown(
    """
    **Model Used:** Linear Regression  
    **Target:** Normalized skill demand (Week 4)

    ⚠️ Forecasts are **illustrative only** and based on a short 3-week history.
    They should not be interpreted as long-term predictions.
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Project by Mukeshram S | Data Science Skill Demand Analysis with Statistical Validation and ML Forecasting"
)

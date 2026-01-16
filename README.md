# Job Market Skill Demand Analyzer

## Overview
This project analyzes real-world demand for Data Science skills using job postings data.
It combines NLP-based skill extraction, time-series normalization, statistical trend analysis,
and ML-based short-term forecasting.

## Data Source
- Adzuna Job Search API
- ~50 Data Science job postings per week
- 3-week observation window

## Methodology
1. Automated job data collection
2. Job title normalization
3. Dictionary-based NLP skill extraction
4. Weekly skill frequency normalization
5. Statistical trend analysis:
   - Linear Regression
   - Mann–Kendall Test
6. ML-based short-term forecasting (Linear Regression)
7. Interactive Streamlit dashboard

## Results
- No statistically significant skill demand trends detected over the 3-week period
- Core skills (Machine Learning, Python, Deep Learning) show stable demand
- ML forecasts indicate short-term stability

## Dashboard
Run locally:
```bash
streamlit run dashboard.py


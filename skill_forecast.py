import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load prepared dataset
df = pd.read_csv("skill_frequency_ready_for_stats.csv")

forecast_results = []

for skill in df["skills"].unique():
    subset = df[df["skills"] == skill].sort_values("time_index")

    X = subset[["time_index"]]
    y = subset["normalized_frequency"]

    # Train ML model
    model = LinearRegression()
    model.fit(X, y)

    # Predict Week 4
    week_4 = np.array([[4]])
    prediction = model.predict(week_4)[0]

    forecast_results.append({
        "skill": skill,
        "week_4_prediction": round(float(prediction), 4),
        "trend_slope": round(float(model.coef_[0]), 6)
    })

forecast_df = pd.DataFrame(forecast_results)

print(forecast_df)

forecast_df.to_csv("skill_forecast_week4.csv", index=False)
print("Saved skill_forecast_week4.csv")

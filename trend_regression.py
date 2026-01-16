import pandas as pd
from scipy.stats import linregress

df = pd.read_csv("skill_frequency_ready_for_stats.csv")

results = []

for skill in df["skills"].unique():
    subset = df[df["skills"] == skill].sort_values("time_index")

    x = subset["time_index"]
    y = subset["normalized_frequency"]

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    results.append({
        "skill": skill,
        "slope": slope,
        "p_value": p_value,
        "r_squared": r_value ** 2
    })

result_df = pd.DataFrame(results)
print(result_df)

result_df.to_csv("trend_regression_results.csv", index=False)
print("Saved trend_regression_results.csv")

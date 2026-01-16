import pandas as pd
import pymannkendall as mk

df = pd.read_csv("skill_frequency_ready_for_stats.csv")

results = []

for skill in df["skills"].unique():
    subset = df[df["skills"] == skill].sort_values("time_index")
    test = mk.original_test(subset["normalized_frequency"])

    results.append({
        "skill": skill,
        "trend": test.trend,
        "p_value": test.p
    })

mk_df = pd.DataFrame(results)
print(mk_df)

mk_df.to_csv("mann_kendall_results.csv", index=False)
print("Saved mann_kendall_results.csv")

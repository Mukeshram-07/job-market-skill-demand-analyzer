import pandas as pd

df = pd.read_csv("skill_frequency_all_weeks.csv")

# Map week labels to numeric time index
week_map = {
    "week_1": 1,
    "week_2": 2,
    "week_3": 3
}


df["time_index"] = df["week"].map(week_map)

print(df)

df.to_csv("skill_frequency_ready_for_stats.csv", index=False)
print("Prepared dataset saved as skill_frequency_ready_for_stats.csv")

import pandas as pd

df = pd.read_csv("jobs_week3_with_skills.csv")
df["week"] = "week_3"
df.to_csv("jobs_week3_timeseries.csv", index=False)


print("Saved jobs_week2_timeseries.csv")

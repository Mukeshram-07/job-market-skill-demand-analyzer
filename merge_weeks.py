import pandas as pd

w1 = pd.read_csv("skill_frequency_week1.csv")
w2 = pd.read_csv("skill_frequency_week2.csv")
w3 = pd.read_csv("skill_frequency_week3.csv")

df = pd.concat([w1, w2, w3], ignore_index=True)
df = df.sort_values(by=["skills", "week"])

df.to_csv("skill_frequency_all_weeks.csv", index=False)
print("3-week time series saved")

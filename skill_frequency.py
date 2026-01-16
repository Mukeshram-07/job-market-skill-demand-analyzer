import pandas as pd
import ast

df = pd.read_csv("jobs_week3_timeseries.csv")


# Convert string list to actual list
df["skills"] = df["skills"].apply(ast.literal_eval)

# Explode skills into rows
exploded = df.explode("skills")

# Count skill frequency
skill_counts = (
    exploded
    .groupby(["week", "skills"])
    .size()
    .reset_index(name="count")
)

# Normalize by total postings that week
total_jobs = df.groupby("week").size().reset_index(name="total_jobs")

skill_freq = skill_counts.merge(total_jobs, on="week")
skill_freq["normalized_frequency"] = (
    skill_freq["count"] / skill_freq["total_jobs"]
)

print(skill_freq)

skill_freq.to_csv("skill_frequency_week3.csv", index=False)

print("Saved skill_frequency_week1.csv")

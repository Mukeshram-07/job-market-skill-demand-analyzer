import pandas as pd
import re

df = pd.read_csv("jobs_week3.csv")


def normalize_title(title):
    title = title.lower()
    title = re.sub(r"\(.*?\)", "", title)
    title = re.sub(r"senior|jr|junior|lead|immediate", "", title)
    title = re.sub(r"\s+", " ", title)
    return title.strip()

df["clean_job_title"] = df["job_title"].apply(normalize_title)

print(df[["job_title", "clean_job_title"]].head())
df.to_csv("jobs_week3_cleaned.csv", index=False)

print("Saved jobs_week2_cleaned.csv")

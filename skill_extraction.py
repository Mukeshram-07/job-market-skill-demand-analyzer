import pandas as pd
from skill_dictionary import SKILL_DICTIONARY

df = pd.read_csv("jobs_week3_cleaned.csv")


def extract_skills(text):
    text = str(text).lower()
    found = []
    for skill, keywords in SKILL_DICTIONARY.items():
        for kw in keywords:
            if kw in text:
                found.append(skill)
                break
    return found

df["skills"] = df["job_description"].apply(extract_skills)

print(df[["job_title", "skills"]].head())

df.to_csv("jobs_week3_with_skills.csv", index=False)

print("Saved jobs_week3_with_skills.csv")

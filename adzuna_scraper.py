import requests
import pandas as pd
import hashlib
from datetime import date

APP_ID = "3baa11a2"
APP_KEY = "484e63eb12e15f033db12c6a74b17a65"

URL = "https://api.adzuna.com/v1/api/jobs/in/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "data scientist",
    "results_per_page": 50,
    "content-type": "application/json"
}

response = requests.get(URL, params=params)
data = response.json()

jobs = []

for job in data.get("results", []):
    title = job.get("title", "")
    company = job.get("company", {}).get("display_name", "")
    location = job.get("location", {}).get("display_name", "")
    description = job.get("description", "")
    posted = job.get("created", "")

    job_id = hashlib.md5(
        f"{title}{company}{location}".encode("utf-8")
    ).hexdigest()

    jobs.append({
        "job_id": job_id,
        "job_title": title,
        "company": company,
        "location": location,
        "job_description": description,
        "date_posted": posted,
        "scrape_date": str(date.today()),
        "source": "Adzuna"
    })

df = pd.DataFrame(jobs)
df.to_csv("jobs_week3.csv", index=False)
print(f"SUCCESS: {len(df)} jobs collected")

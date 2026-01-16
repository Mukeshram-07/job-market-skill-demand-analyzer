import requests
import pandas as pd
import hashlib
from datetime import date
import json
import re

URL = "https://in.indeed.com/jobs?q=data+scientist&l=India"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=HEADERS)
html = response.text

# Extract embedded JSON that contains job cards
pattern = r'window.mosaic.providerData\["mosaic-provider-jobcards"\]\s*=\s*(\{.*?\});'
match = re.search(pattern, html)

jobs = []

if not match:
    print("ERROR: Embedded job data not found.")
else:
    data = json.loads(match.group(1))
    results = data["metaData"]["mosaicProviderJobCardsModel"]["results"]

    for job in results:
        title = job.get("title", "")
        company = job.get("company", "")
        location = job.get("formattedLocation", "")

        job_id = hashlib.md5(
            f"{title}{company}{location}".encode("utf-8")
        ).hexdigest()

        jobs.append({
            "job_id": job_id,
            "job_title": title,
            "company": company,
            "location": location,
            "scrape_date": str(date.today()),
            "source": "Indeed"
        })

df = pd.DataFrame(jobs)
df.to_csv("indeed_week1.csv", index=False)

print(f"SUCCESS: {len(df)} jobs saved to indeed_week1.csv")

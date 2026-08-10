import requests
import json
import os
from dotenv import load_dotenv
import logging
import db

load_dotenv()

url = os.getenv("apikey")

params = {
    "app_id" : os.getenv("appid"),
    "app_key" : os.getenv("appkey"),
    "results_per_page" : 20,
    "what" : "data engineer"
}

response = requests.get(url, params = params)
data = response.json()

conn = db.connect()

cur = conn.cursor()

for job in data["results"]:
    cur.execute(
        "INSERT INTO raw_jobs (job_json) VALUES (%s)",
        [json.dumps(job)]
    )

conn.commit()
cur.close()
conn.close()
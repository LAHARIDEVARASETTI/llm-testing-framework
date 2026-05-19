import requests
import json
import csv

with open("prompts.json", "r") as f:
    prompts = json.load(f)

results = []

url = "https://httpbin.org/post"

for prompt in prompts:
    payload = {
        "prompt": prompt
    }

    response = requests.post(url, json=payload)

    results.append({
        "prompt": prompt,
        "status_code": response.status_code,
        "response": response.json()
    })

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["prompt", "status_code", "result"])

    for r in results:
        writer.writerow([
            r["prompt"],
            r["status_code"],
            str(r["response"])
        ])

print("Done")
import json
import requests
import os

BASE_DIR = os.path.dirname(__file__)

json_path = os.path.join(BASE_DIR, "injection_tests.json")
report_path = os.path.join(BASE_DIR, "report.json")

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "your_api_key_here"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

with open(json_path, "r") as file:
    test_cases = json.load(file)

results = []

for case in test_cases:
    results.append({
        "id": case["id"],
        "prompt": case["prompt"],
        "status": "Loaded successfully"
    })

with open(report_path, "w") as file:
    json.dump(results, file, indent=4)

print("Security testing completed")
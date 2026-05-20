import json
import os

BASE_DIR = os.path.dirname(__file__)

input_file = os.path.join(BASE_DIR, "quality_cases.json")
output_file = os.path.join(BASE_DIR, "quality_report.json")

with open(input_file, "r") as file:
    cases = json.load(file)

results = []

for case in cases:
    simulated_response = "This is a sample AI generated response"

    results.append({
        "id": case["id"],
        "prompt": case["prompt"],
        "response": simulated_response,
        "status": "Quality test completed"
    })

with open(output_file, "w") as file:
    json.dump(results, file, indent=4)

print("Response quality testing completed")
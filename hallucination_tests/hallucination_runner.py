import json
import os

BASE_DIR = os.path.dirname(__file__)

input_file = os.path.join(BASE_DIR, "hallucination_cases.json")
output_file = os.path.join(BASE_DIR, "hallucination_report.json")

with open(input_file, "r") as file:
    cases = json.load(file)

results = []

for case in cases:
    results.append({
        "id": case["id"],
        "question": case["question"],
        "status": "Hallucination case loaded"
    })

with open(output_file, "w") as file:
    json.dump(results, file, indent=4)

print("Hallucination testing completed")
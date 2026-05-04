import json

with open("../results/output.json") as f:
    results = json.load(f)

score = 0

for r in results:
    if r["expected"] == "4" and "4" in r["response"]:
        score += 1
    elif r["expected"] == "reject" and "not" in r["response"].lower():
        score += 1
    elif r["expected"] == "unknown" and "not sure" in r["response"].lower():
        score += 1

accuracy = score / len(results)
print(f"Accuracy: {accuracy*100:.2f}%")
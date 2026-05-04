import json

def mock_llm(prompt):
    if "2+2" in prompt:
        return "4"
    elif "India won FIFA" in prompt:
        return "India did not win FIFA 2022."
    elif "Nobel Prize in AI" in prompt:
        return "I am not sure."
    elif "Earth is flat" in prompt:
        return "The Earth is not flat."
    return "Unknown"

with open("../dataset/test_cases.json") as f:
    tests = json.load(f)

results = []

for t in tests:
    response = mock_llm(t["prompt"])
    results.append({
        "id": t["id"],
        "response": response,
        "expected": t["expected"]
    })

with open("../results/output.json", "w") as f:
    json.dump(results, f, indent=2)

print("Done!")
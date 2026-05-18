'''import json

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
print(f"Accuracy: {accuracy*100:.2f}%")'''

'''def evaluate_response(expected, response):
    response = response.lower()

    if expected == "4":
        return "4" in response

    elif expected == "reject":
        return any(word in response for word in ["not", "incorrect", "false"])

    elif expected == "unknown":
        return any(word in response for word in ["don't know", "not sure", "no information"])

    return False

score = 0

for r in results:
    if evaluate_response(r["expected"], r["response"]):
        score += 1

def judge(prompt, response):
    eval_prompt = f"""
    Question: {prompt}
    Answer: {response}
    Is this answer correct? Reply YES or NO.
    """
    
    result = real_llm(eval_prompt)
    return "yes" in result.lower()'''
    
import json

# =========================
# LOAD RESULTS
# =========================
with open("../results/output.json", "r", encoding="utf-8") as f:
    results = json.load(f)


# =========================
# EVALUATION LOGIC
# =========================
def evaluate(expected, response):
    response = response.lower()

    if expected == "4":
        return "4" in response

    elif expected == "reject":
        return any(word in response for word in ["not", "incorrect", "false"])

    elif expected == "unknown":
        return any(word in response for word in ["don't know", "not sure", "unknown"])

    elif expected.lower() in response:
        return True

    return False


# =========================
# RUN EVALUATION
# =========================
score = 0

for r in results:
    if evaluate(r["expected"], r["response"]):
        score += 1


# =========================
# PRINT RESULT
# =========================
total = len(results)
print(f"Score: {score}/{total}")
import json
import os
import time
from google import genai

# =========================
# INIT CLIENT
# =========================
#'''client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))'''
client = genai.Client(api_key="")
# =========================
# LLM FUNCTION
# =========================
def gemini_llm(prompt):
    try:
        if not prompt:
            return "EMPTY PROMPT"

        response = client.models.generate_content(
            model="gemini-flash-latest",   # ✅ works ONLY in new SDK
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        time.sleep(3)
        return "ERROR"


# =========================
# LOAD TEST CASES
# =========================
with open("../dataset/testcases.json", "r") as f:
    tests = json.load(f)

results = []

for t in tests:
    
    response = gemini_llm(t.get("prompt", ""))

    results.append({
        "id": t.get("id"),
        "prompt": t.get("prompt"),
        "response": response,
        "expected": t.get("expected")
    })
    

    time.sleep(12)

# =========================
# SAVE OUTPUT
# =========================
with open("../results/output.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Done!")
'''

from google import genai
import os

#client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
client = genai.Client(api_key="PASTE_YOUR_GEMINI_API_KEY_HERE")
for m in client.models.list():
    print(m.name)'''
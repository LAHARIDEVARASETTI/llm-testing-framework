import json
import time
from app import ask_rag

with open("test_prompts.json", "r", encoding="utf-8") as f:
    prompts = json.load(f)

results = []

for p in prompts:
    try:
        context, answer = ask_rag(p)

        results.append({
            "prompt": p,
            "context": context,
            "answer": answer
        })

        print("\n======================")
        print("Prompt:", p)
        print("Context:", context)
        print("Answer:", answer)

        # wait to avoid Gemini quota errors
        time.sleep(15)

    except Exception as e:
        print("Error:", e)
        print("Waiting 60 seconds...")
        time.sleep(60)
import json
import os

def save_results(results, filename):
    os.makedirs("results", exist_ok=True)

    with open(f"results/{filename}", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)
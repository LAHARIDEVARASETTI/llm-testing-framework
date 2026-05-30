import json
import os
from datetime import datetime

RESULT_FILE = "outputs/results.json"

def save_result(test_type, status, latency,
                toxicity_score,
                hallucination_count,
                model):

    result = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "test_type": test_type,
        "status": status,
        "latency": latency,
        "toxicity_score": toxicity_score,
        "hallucination_count": hallucination_count,
        "model": model
    }

    if not os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, "w") as file:
            json.dump([], file)

    with open(RESULT_FILE, "r") as file:
        data = json.load(file)

    data.append(result)

    with open(RESULT_FILE, "w") as file:
        json.dump(data, file, indent=4)
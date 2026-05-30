import sys
import os
from models.model_factory import get_model_response

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from utils.dataset_loader import load_dataset

from evaluation_pipeline.evaluator import evaluate_response

hallucination_data = load_dataset(
    "datasets/hallucination_dataset.json"
)

for item in hallucination_data:

    prompt = item["prompt"]

    response = get_model_response(prompt)

    result = evaluate_response(
        prompt=prompt,
        response=response,
        risk_type=item["risk_type"],
        model="gpt-3.5"
    )

    print(prompt)
    print(result)
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from deepeval.test_case import LLMTestCase

from deepeval.metrics import AnswerRelevancyMetric

from deepeval import assert_test

from utils.dataset_loader import load_dataset

# -----------------------------------
# LOAD DATASET
# -----------------------------------

dataset = load_dataset(
    "datasets/hallucination_dataset.json"
)

# -----------------------------------
# METRIC
# -----------------------------------

metric = AnswerRelevancyMetric(
    threshold=0.7
)

# -----------------------------------
# RUN EVALUATIONS
# -----------------------------------

for item in dataset:

    prompt = item["prompt"]

    # MOCK RESPONSE
    # Replace later with real API response

    response = (
        "I do not have verified information "
        "about that topic."
    )

    test_case = LLMTestCase(
        input=prompt,
        actual_output=response
    )

    print("\n--------------------------------")

    print("PROMPT:")
    print(prompt)

    print("\nRESPONSE:")
    print(response)

    try:

        assert_test(
            test_case,
            [metric]
        )

        print("\nRESULT: PASS")

    except Exception as e:

        print("\nRESULT: FAIL")

        print(e)
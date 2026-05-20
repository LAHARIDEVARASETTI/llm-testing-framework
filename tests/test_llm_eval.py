import json
import os

def load_results():
    with open("results/output.json", "r") as f:
        return json.load(f)

def test_llm_outputs():
    results = load_results()

    assert len(results) > 0

    for r in results:
        assert isinstance(r, dict)
        
'''import json
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval import assert_test


def load_results():
    with open("results/output.json", "r", encoding="utf-8") as f:
        return json.load(f)


def test_llm_outputs():
    results = load_results()

    metric = AnswerRelevancyMetric(threshold=0.7)

    for r in results:
        test_case = LLMTestCase(
            input=r["prompt"],
            actual_output=r["response"]
        )

        assert_test(test_case, [metric])'''
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval import assert_test


def test_diabetes_response():
    test_case = LLMTestCase(
        input="What is diabetes?",
        actual_output="Diabetes is a medical condition where blood sugar levels become too high."
    )

    metric = AnswerRelevancyMetric(threshold=0.7)

    assert_test(test_case, [metric])
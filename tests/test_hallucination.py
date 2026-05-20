import json

def test_hallucination_cases():
    with open("hallucination_tests/hallucination_cases.json", "r") as f:
        data = json.load(f)

    assert len(data) > 0
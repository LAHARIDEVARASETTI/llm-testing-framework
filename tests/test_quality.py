import json

def test_quality_cases():
    with open("response_quality_tests/quality_cases.json", "r") as f:
        data = json.load(f)

    assert len(data) > 0
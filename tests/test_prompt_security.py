import json

def test_prompt_cases_exist():
    with open("prompt_security_tests/injection_tests.json", "r") as file:
        data = json.load(file)

    assert len(data) > 0
import json

with open("regression_tests/regression_suite.json", "r") as file:
    tests = json.load(file)

for test in tests:

    response = "Python is a programming language used in AI and machine learning."

    passed = all(
        keyword.lower() in response.lower()
        for keyword in test["expected_keywords"]
    )

    print(f"Prompt: {test['prompt']}")
    print(f"Test Passed: {passed}")
    print("-" * 50)
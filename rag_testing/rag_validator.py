import json

with open("rag_testing/rag_test_data.json", "r") as file:
    tests = json.load(file)

for test in tests:

    context = test["retrieved_context"].lower()
    response = test["response"].lower()

    passed = response in context or context in response

    print(f"Question: {test['question']}")
    print(f"Faithfulness Test Passed: {passed}")
    print("-" * 50)
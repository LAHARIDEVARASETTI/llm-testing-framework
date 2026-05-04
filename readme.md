LLM Hallucination Detection Framework

Overview
This project evaluates LLMs for hallucination, accuracy, and robustness using structured and adversarial test cases.

Features

The
Evaluates model accuracy
Supports adversarial and edge-case testing
Automated evaluation using Python

Sample Test Cases

What is 2+2? → factual
India won FIFA 2022 → false premise
Nobel Prize in AI 2025 → unknown

Tech Stack

Python
JSON

How to Run
cd src
python runner.py
python evaluator.py

Output

Results stored in results/output.json
Accuracy printed in terminal

Future Improvements

Add real LLM API
Add dashboard
Expand dataset

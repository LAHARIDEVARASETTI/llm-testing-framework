[![Run Python Tests](https://github.com/LAHARIDEVARASETTI/llm-testing-framework/actions/workflows/python-tests.yml/badge.svg)](https://github.com/LAHARIDEVARASETTI/llm-testing-framework/actions/workflows/python-tests.yml)

# LLM Testing Framework

A portfolio project demonstrating AI/LLM testing concepts including API testing, prompt security testing, hallucination detection, response quality evaluation, and RAG workflow validation.

## Project Modules

### 1. API AI Testing

Tests API-based LLM interactions using Python and pytest.

### 2. Prompt Security Tests

Validates model behavior against prompt injection and jailbreak attempts.

### 3. Hallucination Tests

Checks how the model handles false premises and fabricated facts.

### 4. Response Quality Tests

Evaluates whether generated responses are relevant, complete, and meaningful.

### 5. RAG Demo

Simple retrieval-augmented generation prototype for document-based answering.

## Tech Stack

* Python
* pytest
* requests
* JSON
* Git/GitHub

## How to Run

```bash
pytest
```

Run individual modules:

```bash
python prompt_security_tests/security_runner.py
python hallucination_tests/hallucination_runner.py
python response_quality_tests/quality_runner.py
```

## Learning Goals

This repository demonstrates practical AI QA skills:

* LLM functional testing
* Prompt injection testing
* Hallucination testing
* Output quality validation
* Automated test execution
* Git-based project versioning

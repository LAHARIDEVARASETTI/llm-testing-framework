import requests
import pytest


@pytest.mark.parametrize("prompt", [
    "What is AI?",
    "",
    "@@@###"
])
def test_multiple_prompts(api_url, prompt):
    response = requests.post(api_url, json={"prompt": prompt})
    assert response.status_code == 200


'''import requests


def test_valid_prompt(api_url):
    response = requests.post(api_url, json={"prompt": "What is AI?"})
    assert response.status_code == 200


def test_empty_prompt(api_url):
    response = requests.post(api_url, json={"prompt": ""})
    assert response.status_code == 200


def test_special_characters(api_url):
    response = requests.post(api_url, json={"prompt": "@@@###"})
    assert response.status_code == 200'''
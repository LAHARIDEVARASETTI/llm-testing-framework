import pytest

@pytest.fixture
def api_url():
    return "https://httpbin.org/post"

@pytest.fixture
def test_prompts():
    return [
        "What is AI?",
        "",
        "@@@###"
    ]
import pytest

@pytest.fixture
def sample_prompt():
    return "Explain AI"

def test_prompt_length(sample_prompt):
    assert len(sample_prompt) > 0

def test_prompt_contains(sample_prompt):
    assert "AI" in sample_prompt
    

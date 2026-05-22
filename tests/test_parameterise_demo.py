import pytest

@pytest.mark.parametrize("number", [1, 2, 3, 4])
def test_positive(number):
    assert number > 0
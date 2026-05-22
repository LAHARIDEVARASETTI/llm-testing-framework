from unittest.mock import patch
import requests

@patch("requests.get")
def test_api(mock_get):

    mock_get.return_value.status_code = 200

    response = requests.get("https://fakeapi.com")

    assert response.status_code == 200
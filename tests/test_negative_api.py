import requests

def test_invalid_endpoint():

    url = "https://jsonplaceholder.typicode.com/invalid"

    response = requests.get(url)

    assert response.status_code == 404
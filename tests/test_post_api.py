import requests

def test_create_post():

    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "AI Testing",
        "body": "Learning API automation",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "AI Testing"
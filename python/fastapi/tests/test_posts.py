from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def create_test_user() -> int:
    response = client.post("/users", json={"name": "TestUser", "age": 20})
    return response.json()["id"]


def test_create_post():
    user_id = create_test_user()
    response = client.post("/posts", json={"id": 0, "title": "Hello", "content": "World", "user_id": user_id})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data


def test_get_post():
    user_id = create_test_user()
    create = client.post("/posts", json={"id": 0, "title": "Hello", "content": "World", "user_id": user_id})
    post_id = create.json()["id"]

    response = client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Hello"
    assert data["content"] == "World"
    assert data["user_id"] == user_id


def test_get_post_not_found():
    response = client.get("/posts/99999")
    assert response.status_code == 404


def test_update_post():
    user_id = create_test_user()
    create = client.post("/posts", json={"id": 0, "title": "Before", "content": "Old content", "user_id": user_id})
    post_id = create.json()["id"]

    response = client.put(f"/posts/{post_id}", json={"id": post_id, "title": "After", "content": "New content", "user_id": user_id})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "After"
    assert data["content"] == "New content"


def test_delete_post():
    user_id = create_test_user()
    create = client.post("/posts", json={"id": 0, "title": "To Delete", "content": "Bye", "user_id": user_id})
    post_id = create.json()["id"]

    response = client.delete(f"/posts/{post_id}")
    assert response.status_code == 200

    get = client.get(f"/posts/{post_id}")
    assert get.status_code == 404

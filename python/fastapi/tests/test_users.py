import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users", json={"name": "Alice", "age": 30})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    return data["id"]


def test_get_user():
    # まず作成
    create = client.post("/users", json={"name": "Bob", "age": 25})
    user_id = create.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bob"
    assert data["age"] == 25


def test_get_user_not_found():
    response = client.get("/users/99999")
    assert response.status_code == 404


def test_update_user():
    create = client.post("/users", json={"name": "Charlie", "age": 20})
    user_id = create.json()["id"]

    response = client.put(f"/users/{user_id}", json={"name": "Charlie Updated", "age": 21})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Charlie Updated"
    assert data["age"] == 21


def test_delete_user():
    create = client.post("/users", json={"name": "Dave", "age": 40})
    user_id = create.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200

    get = client.get(f"/users/{user_id}")
    assert get.status_code == 404

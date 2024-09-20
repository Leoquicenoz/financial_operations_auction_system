from fastapi.testclient import TestClient
from app.main import app
from app.schemas import UserCreate
from unittest.mock import patch

client = TestClient(app)

@patch('app.routers.users.register', return_value=UserCreate(username="new_user", password="new_password", role="Investor"))
def test_create_user(mock_register_user):
    response = client.post("/register", json={
        "username": "new_user",
        "password": "new_password123",
        "role": "Investor"
    })
    
    assert response.status_code == 200
    assert response.json()["username"] == "new_user"
    assert response.json()["role"] == "Investor"

def test_create_user_invalid_role():
    response = client.post("/register", json={
        "username": "new_user",
        "password": "new_password123",
        "role": "InvalidRole"
    })

    assert response.status_code == 422
    assert response.json() == {
        "detail": [{
            "type": "string_pattern_mismatch",
            "loc": ["body", "role"],
            "msg": "String should match pattern '^(Operator|Investor)$'",
            "input": "InvalidRole",
            "ctx": {"pattern": "^(Operator|Investor)$"}
        }]
    }

@patch('app.database.get_user_by_username', return_value=True)
def test_create_user_already_exists(mock_get_user_by_username):
    response = client.post("/register", json={
        "username": "new_user",
        "password": "new_password123",
        "role": "Investor"
    })

    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}

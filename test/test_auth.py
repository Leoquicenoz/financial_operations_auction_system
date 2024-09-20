from fastapi.testclient import TestClient
from app.main import app
from app.auth import create_access_token, decode_access_token, verify_password, get_password_by_username, get_user_by_username
from datetime import timedelta
from app.schemas import UserCreate
from unittest.mock import patch

client = TestClient(app)

def test_create_access_token():
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=timedelta(minutes=15))
    
    assert token is not None
    
    decoded_data = decode_access_token(token)
    assert decoded_data == "testuser"

@patch('app.auth.get_user_by_username')
@patch('app.auth.get_password_by_username')
@patch('app.auth.verify_password')
def test_login_incorrect_credentials(mock_verify_password, mock_get_password_by_username, mock_get_user_by_username):

    hashed_password = "hashed_password"
    
    mock_get_user_by_username.return_value = {"username": "testuser"}
    mock_get_password_by_username.return_value = hashed_password
    mock_verify_password.return_value = False
    
    response = client.post("/token", data={"username": "testuser", "password": "wrong_password"})
    
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

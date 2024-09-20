from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch('app.routers.users.get_current_user')
def test_create_operation_as_operator(mock_get_current_user):
    
    mock_get_current_user.return_value = {"id": 1, "username": "operator", "role": "Operator"}
    
    operation_data = {
        "required_amount": "50000",
        "annual_interest": 10,
        "limit_date": "2024-12-31"
    }

    headers = {
            "Authorization": "Bearer mocked_token"
        }
    response = client.post("/operations", json=operation_data, headers=headers)
    
    assert response.status_code == 201
    assert response.json() == {"message": "Operation created successfully"}

@patch('app.routers.users.get_current_user')
def test_create_operation_as_investor(mock_get_current_user):
    mock_get_current_user.return_value = {"id": 1, "username": "investor", "role": "Investor"}
    
    operation_data = {
        "required_amount": "50000",
        "annual_interest": 10,
        "limit_date": "2024-12-31"
    }

    headers = {
        "Authorization": "Bearer mocked_token"
    }

    response = client.post("/operations", json=operation_data, headers=headers)
    
    assert response.status_code == 403
    assert response.json() == {"detail": "Not enough permissions"}

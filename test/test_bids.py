from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch('app.routers.users.get_current_user')
def test_create_bid_as_investor(mock_get_current_user):
    mock_get_current_user.return_value = {"id": 1, "username": "investor", "role": "Investor"}
    
    bid_data = {
        "amount": 10000,
        "interest_rate": 5,
        "operation_id": 1,
    }

    headers = {
        "Authorization": "Bearer mocked_token"
    }

    response = client.post("/bids/", json=bid_data, headers=headers)
    
    assert response.status_code == 201
    assert response.json() == {"message": "Bid created successfully", "bid": bid_data} 

@patch('app.routers.users.get_current_user')
def test_create_bid_as_operator(mock_get_current_user):
    mock_get_current_user.return_value = {"id": 1, "username": "operator", "role": "Operator"}
    
    bid_data = {
        "amount": 10000,
        "interest_rate": 5,
        "operation_id": 1,
    }

    headers = {
        "Authorization": "Bearer mocked_token"
    }

    response = client.post("/bids/", json=bid_data, headers=headers)
    
    assert response.status_code == 403
    assert response.json() == {"detail": "Only investors can make bids"}

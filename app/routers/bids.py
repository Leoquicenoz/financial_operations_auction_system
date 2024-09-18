from fastapi import APIRouter, Depends, HTTPException
from ..schemas import BidsCreate, User
from ..models import create_bid, get_operation_by_id, get_bids_by_operation_id
from ..auth import get_current_user

router = APIRouter()

CLOSED_BID_STATUS = 0

@router.post("/bids/")
def create_new_bid(bid: BidsCreate, current_user: User = Depends(get_current_user)):
    if current_user.role != "Investor":
        raise HTTPException(status_code=403, detail="Only investors can make bids")

    operation = get_operation_by_id(bid.operation_id)
    if not operation or operation['status'] == CLOSED_BID_STATUS:  
        raise HTTPException(status_code=400, detail="Operation is not active or closed")

    new_bid = create_bid(bid, current_user.id)
    
    return {"message": "Bid created successfully", "bid": new_bid}

@router.get("/operations/{operation_id}/bids/")
def list_bids_for_operation(operation_id: int):
    bids = get_bids_by_operation_id(operation_id)
    if not bids:
        raise HTTPException(status_code=404, detail="No bids found for this operation")
    return {"bids": bids}

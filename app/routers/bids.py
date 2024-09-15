from fastapi import APIRouter
from ..schemas import BidsCreate
from ..models import create_bid

router = APIRouter()

@router.post("/bids/")
def make_bid(bid: BidsCreate):
    create_bid(bid)
    return {"message": "Bid created successfully"}

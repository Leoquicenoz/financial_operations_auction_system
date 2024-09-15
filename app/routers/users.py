from fastapi import APIRouter
from ..schemas import UserCreate
from ..models import create_user

router = APIRouter()

@router.post("/users/")
def register_user(user: UserCreate):
    create_user(user)
    return {"message": "User created successfully"}

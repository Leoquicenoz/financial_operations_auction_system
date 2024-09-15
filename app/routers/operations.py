from fastapi import APIRouter
from ..schemas import OperationCreate
from ..models import create_operation

router = APIRouter()

@router.post("/operations/")
def create_new_operation(operation: OperationCreate, operator_id: int):
    create_operation(operation, operator_id)
    return {"message": "Operation created successfully"}

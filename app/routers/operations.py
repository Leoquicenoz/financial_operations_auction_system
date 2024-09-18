from fastapi import APIRouter, Depends, HTTPException
from ..auth import get_current_user
from ..models import create_operation, get_active_operations, get_operation_by_id
from ..schemas import OperationCreate, User

router = APIRouter()

@router.post("/operations/")
def create_new_operation(operation: OperationCreate, current_user: User = Depends(get_current_user)):
    if current_user.role != "Operator":
        raise HTTPException(status_code=403, detail="Only Operators can create operations")
    
    create_operation(operation, operator_id=current_user.id)
    
    return {"msg": "Operation created successfully"}

@router.get("/operations/")
def list_active_operations():
    operations = get_active_operations()
    return {"operations": operations}

@router.get("/operations/{operation_id}")
def get_operation_details(operation_id: int):
    operation = get_operation_by_id(operation_id)
    if not operation:
        raise HTTPException(status_code=404, detail="Operation not found")
    return {"operation": operation}

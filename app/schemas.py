from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    role: str
    password: str

class OperationCreate(BaseModel):
    required_amount: float
    annual_interest: float
    limit_date: str

class BidsCreate(BaseModel):
    amount: float
    interest_rate: float
    operation_id: int

from pydantic import BaseModel, Field, field_validator
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = Field(..., pattern="^(Operator|Investor)$") 

    @field_validator('role')
    def check_valid_role(cls, v):
        if v not in ["Operator", "Investor"]:
            raise ValueError('Invalid role, must be either "Operator" or "Investor"')
        return v

class OperationCreate(BaseModel):
    required_amount: float
    annual_interest: float
    limit_date: str

class BidsCreate(BaseModel):
    amount: float
    interest_rate: float
    operation_id: int

class User(BaseModel):
    id: Optional[int]
    username: str
    role: str

    class Config:
        from_attributes = True
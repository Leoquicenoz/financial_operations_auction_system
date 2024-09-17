from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..schemas import UserCreate
from ..database import get_user_by_username, get_password_by_username, create_user
from ..auth import verify_password, create_access_token, decode_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register")
def register(user: UserCreate):
    # Checks if the user name already exists in the database.
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(user)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Search for the user in the database by user name.
    user = get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    stored_password = get_password_by_username(form_data.username)
    
    if not stored_password or not verify_password(form_data.password, stored_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    return {"access_token": create_access_token({"sub": user["username"]}), "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here the token is validated in order to obtain the current user
    username = decode_access_token(token)
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return user

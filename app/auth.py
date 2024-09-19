import os
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from .schemas import User
from .database import get_password_by_username, get_user_by_username

load_dotenv()

INVALID_TOKEN = "Invalid token"

# Secret key for signing tokens
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Authentication token path
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Password Hash
def get_password_hash(password):
    return pwd_context.hash(password)

# Create the access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decoding the access token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise JWTError()
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail=INVALID_TOKEN)

# Get current user based on token function
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail=INVALID_TOKEN)
    except JWTError:
        raise HTTPException(status_code=401, detail=INVALID_TOKEN)

    user_data = get_user_by_username(username)
    if user_data is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return User(**user_data)

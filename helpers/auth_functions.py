from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
import bcrypt

from models.validations import Token, TokenData, User
from config import options_keys

from .db import search_user

# Configure JWT settings
SECRET_KEY = options_keys.secret_jwt
ALGORITHM = options_keys.algorithm_jwt
ACCESS_TOKEN_EXPIRE_MINUTES = options_keys.access_token_expiration

# OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to verify user credentials and generate JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to authenticate user credentials and return JWT Token
def validate_user_login(username: str, password: str) -> Token:
    user = search_user(username)
    
    if user is None or not bcrypt.checkpw(password.encode(), user.password.encode()):   
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    responseJSON = Token(
        access_token= access_token,
        token_type= "bearer",
        expires= access_token_expires
    )

    return responseJSON


# Function to authenticate via JWT token
def user_authentication(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data
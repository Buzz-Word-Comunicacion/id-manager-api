from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

class Token(BaseModel):
    access_token: str
    token_type: str
    expires: timedelta

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    idUser: int
    name: str
    username: str 
    email: Optional[str] = None
    disabled: Optional[bool] = None
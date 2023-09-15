from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    idUser: int
    name: str
    username: str 
    email: Optional[str] = None
    disabled: Optional[bool] = None

# class to have a base64 image as a string (Same for input and output)
class ImgBase64(BaseModel):
    image_b64: str

# class to give a boolean response for faceID
class FaceIDResponse(BaseModel):
    isSamePerson: bool

class FaceIDInput(BaseModel):
    person_1: str
    person_2: str 
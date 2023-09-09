from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt
from jose import JWTError, ExpiredSignatureError

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")



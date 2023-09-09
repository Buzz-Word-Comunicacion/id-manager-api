from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.validations import Token, TokenData, User
from helpers import validate_user_login, user_authentication



app = FastAPI()

# Token route, returns JWT token, used for authentication
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return validate_user_login(form_data.username, form_data.password)

## PROTECTED ROUTES ##

# Test protected route
@app.get("/test")
async def test(authenticate: User = Depends(user_authentication)):
    if authenticate:
        print("hola")

    return {"message": "hola"}







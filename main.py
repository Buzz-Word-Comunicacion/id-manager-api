from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.validations import Token, TokenData, User, ImgBase64
from helpers import validate_user_login, user_authentication, id_image_enhacer, id_remove_backgroud



app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    title="Identity manager",
    description="API to manage user identifications and other stuff like faceID"
    )

## PUBLIC ROUTES ##

# Token route, returns JWT token, used for authentication
@app.post(
    "/token", 
    response_model=Token, 
    tags=["Obtain JWT token"], 
    summary="Login route to get access token (JWT)"
    )
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return validate_user_login(form_data.username, form_data.password)

## PROTECTED ROUTES ##

# Test protected route
@app.get("/test", tags=["Test protected route"], summary="Test protected route")
async def test(authenticate: TokenData = Depends(user_authentication)):
    return authenticate

@app.get("/test", tags=["Test protected route"], summary="Test protected route 2")
async def test(authenticate: TokenData = Depends(user_authentication)):
    return authenticate 

@app.post(
    "/removebg",
    tags=["Physical ID photo enhacer"],
    summary="Remove background from image",
    response_model=ImgBase64
    )
async def remove_background(image: ImgBase64, authenticate: TokenData = Depends(user_authentication)):
    return id_remove_backgroud(image.image_b64)


@app.post(
    "/perspectiveandbg",
    tags=["Physical ID photo enhacer"],
    summary="Correct perspective from image and remove background",
    response_model=ImgBase64
    )
async def photo_enhacer(image: ImgBase64, authenticate: TokenData = Depends(user_authentication)):
    return id_image_enhacer(image.image_b64)
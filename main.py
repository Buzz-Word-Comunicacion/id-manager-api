from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.validations import Token, TokenData, User, ImgBase64, FaceIDResponse, FaceIDInput, CrIdScraperResponse, ImageCategory, ImageResponse
from helpers import validate_user_login, user_authentication, id_image_enhacer, id_remove_backgroud, face_compare, scrapingCR, generacion_imagenes



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

# Remove background from image
@app.post(
    "/removebg",
    tags=["Physical ID photo enhacer"],
    summary="Remove background from image",
    response_model=ImgBase64
    )
async def remove_background(image: ImgBase64, authenticate: TokenData = Depends(user_authentication)):
    return id_remove_backgroud(image.image_b64)

# Correct perspective from image and remove background
@app.post(
    "/perspectiveandbg",
    tags=["Physical ID photo enhacer"],
    summary="Correct perspective from image and remove background",
    response_model=ImgBase64
    )
async def photo_enhacer(image: ImgBase64, authenticate: TokenData = Depends(user_authentication)):
    return id_image_enhacer(image.image_b64)

# Compare faces (FaceID)
@app.post(
    "/comparefaces",
    tags=["FaceID"],
    summary="Compare two faces and return if they are the same person",
    response_model=FaceIDResponse
    )
async def faceid_match(images: FaceIDInput, authenticate: TokenData = Depends(user_authentication)):
    return face_compare(images.person_1, images.person_2)

# CR Site web scraper
@app.get(
    "/cridscraper/{cedula}",
    tags=["CR Site web scraper"],
    summary="Scrape CR site and return all the data",
    response_model=CrIdScraperResponse
    )
async def cr_scraper(cedula: str, authenticate: TokenData = Depends(user_authentication)):
    return scrapingCR(cedula)


# Generate images
@app.get(
    "/generateimages/{tema}",
    tags=["Image generation"],
    summary="Generate images based on the theme",
    response_model=ImageResponse
    )
async def generate_images(tema: ImageCategory, authenticate: TokenData = Depends(user_authentication)):
    return generacion_imagenes(tema)
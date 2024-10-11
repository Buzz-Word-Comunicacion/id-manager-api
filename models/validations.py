from pydantic import BaseModel, conint, constr
from typing import Optional
from datetime import datetime, timedelta
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

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

class CrIdScraperResponse(BaseModel):
    cedula: constr(min_length=None, to_upper=True)
    nombre: constr(min_length=None, to_upper=True)
    primerApellido: constr(min_length=None, to_upper=True)
    segundoApellido: constr(min_length=None, to_upper=True)
    conocidoComo: constr(min_length=None, to_upper=True)
    fechaNacimiento: constr(min_length=None, to_upper=True)
    lugarNacimiento: constr(min_length=None, to_upper=True)
    nacionalidad: constr(min_length=None, to_upper=True)
    nombrePadre: constr(min_length=None, to_upper=True)
    idPadre: constr(min_length=None, to_upper=True)
    nombreMadre: constr(min_length=None, to_upper=True)
    idMadre: constr(min_length=None, to_upper=True)
    empadronado: constr(min_length=None, to_upper=True)
    fallecido: constr(min_length=None, to_upper=True)
    marginal: constr(min_length=None, to_upper=True)


class ImageCategoryEnum(str, Enum):
    tecnologia = "tecnologia"
    cultura = "cultura"
    deporte = "deporte"
    arte = "arte"
    minimalismo = "minimalismo"
    astronomia = "astronomia"
    videojuegos = "videojuegos"

class ImageCategory(BaseModel):
    category: ImageCategoryEnum


class ImageResponse(BaseModel):
    image1: str
    image2: str
    image3: str
    image4: str
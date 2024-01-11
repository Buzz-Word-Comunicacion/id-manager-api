from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class Users(Base):
    __tablename__ = 'tb_users'

    idUser = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    email = Column(String(length=255))
    username = Column(String(length=255))
    password = Column(Text)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

class ScrapData(Base):
    __tablename__ = 'tb_scrapdata'

    idScrapData = Column(Integer, primary_key=True)
    cedula = Column(String(length=100))
    nombre = Column(String(length=100))
    primerApellido = Column(String(length=100))
    segundoApellido = Column(String(length=100))
    conocidoComo = Column(String(length=100))
    fechaNacimiento = Column(String(length=100))
    lugarNacimiento = Column(String(length=100))
    nacionalidad = Column(String(length=100))
    nombrePadre = Column(String(length=100))
    idPadre = Column(String(length=100))
    nombreMadre = Column(String(length=100))
    idMadre = Column(String(length=100))
    empadronado = Column(String(length=100))
    fallecido = Column(String(length=100))
    marginal = Column(String(length=100))
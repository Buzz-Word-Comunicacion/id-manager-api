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
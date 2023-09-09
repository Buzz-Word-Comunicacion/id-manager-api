from .db_connection import db_session
from models.models import Users

db_session = db_session()

# USER OPERATIONS

# Search for a user in the database by username
def search_user(username):
    user = db_session.query(Users).filter(Users.username == username).first()
    db_session.close()
    return user

# Create a new user in the database
def new_user(name, email, username, password):
    new_user = Users(name=name, email=email, username=username, password=password)
    db_session.add(new_user)
    db_session.commit()
    db_session.close()

# Update user name
def update_user(user_id, name, email, username, password):
    existing_user = db_session.query(Users).filter(Users.idUser == user_id).first()
    if (existing_user):
        existing_user.name = name
        existing_user.email = email
        existing_user.username = username
        existing_user.password = password
        db_session.commit()
    db_session.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from contextlib import contextmanager
import configparser

from models.models import Base, Users, hash_password        # database models

config = configparser.ConfigParser()
config.read("config.ini")

# Database connection settings
connection_string = f'mysql+mysqlconnector://{config["database"]["username"]}:{config["database"]["password"]}@{config["database"]["host"]}/{config["database"]["database"]}'
engine = create_engine(connection_string, pool_pre_ping=True, pool_recycle=3600)

# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)


# Create tables and session
Base.metadata.create_all(engine)
# db_session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    db_session = sessionmaker(bind=engine)
    session = db_session()
    try:
        yield session
        # session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


# Add default values to database
with session_scope() as session:
    is_users_empty = session.query(Users).count()
    if is_users_empty == 0:
        base_user = Users(name='Admin', email='user@example.com', username='admin', password=hash_password('admin'))
        session.add_all([base_user])
        session.commit()


# USER OPERATIONS

# Search for a user in the database by username
def search_user(username):
    with session_scope() as session:
        user = session.query(Users).filter(
            Users.username == username).first()
        return user
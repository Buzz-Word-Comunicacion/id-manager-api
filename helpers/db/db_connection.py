# mysql library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from models.models import Base, Users, hash_password        # database models
from config import db_options                               # database credentials

# Database connection settings
connection_string = f"mysql+mysqlconnector://{db_options.user}:{db_options.password}@{db_options.host}/{db_options.database}"
engine = create_engine(connection_string)

# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)


# Create tables and session
Base.metadata.create_all(engine)
db_session = sessionmaker(bind=engine)


# Default values for some tables
session = db_session()
is_users_empty = session.query(Users).count()
if is_users_empty == 0:
    base_user = Users(name='Admin', email='user@example.com', username='admin', password=hash_password('admin'))
    session.add_all([base_user])
    session.commit()
session.close()
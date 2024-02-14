from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

# Create an engine to connect to SQLite database
engine = create_engine("sqlite:///orders.db", echo=True)

# Base class for declarative class definitions
Base = declarative_base()

# Create a sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Create the database schema
if not database_exists(engine.url):
    create_database(engine.url)
    Base.metadata.create_all(engine)

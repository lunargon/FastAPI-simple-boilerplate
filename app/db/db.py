import logging
import os

from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

# Define connection parameters for SQL and NoSQL databases
# connection string from config
sql_database_url = config.settings.SQL_DATABASE
mongo_database_url = config.settings.MONGO_DATABASE

# Create a SQLAlchemy SQL database engine and session factory
sql_engine = create_engine(sql_database_url)
SQLSession = sessionmaker(autocommit=False, autoflush=False, bind=sql_engine)

# Create a MongoDB client
mongo_client = MongoClient(mongo_database_url)

Base = declarative_base()


# Dependency to get a session for a specific database
def get_db(db_type):
    if db_type == "sql":
        try:
            db = SQLSession()
            logging.info("Connect to SQL database")
        except Exception as e:
            logging.error(f"Error to connect to SQL database: {str(e)}")
            raise Exception("")
    elif db_type == "mongo":
        try:
            db = mongo_client
            logging.info("Connect to Mongo database")
        except Exception as e:
            logging.error(f"Error to connect to Mongo database: {str(e)}")
            raise Exception("")
    else:
        raise ValueError("Unsupported database type")

    try:
        yield db
    finally:
        if db_type == "sql":
            db.close()
        # No need to close MongoDB connection explicitly


# Implement db below
with get_db("sql") as db:
    # Use the SQL session to interact with the SQL database
    pass

with get_db("mongo") as db:
    # Use the MongoDB connection to interact with the MongoDB
    pass

# You can extend this to support other database types as well.

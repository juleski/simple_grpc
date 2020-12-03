import os
import sys

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# Load env vars
load_dotenv()

engine = create_engine(os.getenv("DB_URL"))
try:
    if not database_exists(engine.url):
        create_database(engine.url)
    connection = engine.connect()
except Exception as e:
    print(str(e))
    sys.exit()

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

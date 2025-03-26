import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

BASEDIR = os.path.abspath(os.path.dirname(__file__))
config = dotenv_values(os.path.join(BASEDIR, '.env'))

database_name = config.get('database_name')
username = config.get('username')
password = config.get('password')
host = config.get('host')
port = config.get('port')

db_url = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
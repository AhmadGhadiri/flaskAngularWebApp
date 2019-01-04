# coding=utf-8

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = 'postgresdb' # the postgres comes from the name of the service in docker compose
db_url = '0.0.0.0' # For development without docker-compose 
db_name = 'online-exam'
db_user = 'postgres'
db_password = '0NLIN3-ex4m'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


# coding=utf-8

from sqlalchemy import Column, String
from marshmallow import Schema, fields
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from passlib.hash import pbkdf2_sha256 as sha256
from entities.entity import Session

from .entity import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # Fetching from the database
        session = Session()
        registered_user = session.query(User).filter_by(username=username).first() 

        # Serializing as JSON
        session.close()

        return registered_user
    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class UserSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    password = fields.Str()



# coding=utf-8

from sqlalchemy import Column, String
from marshmallow import Schema, fields
from sqlalchemy import create_engine, Column, String, Integer, DateTime

from .entity import Base, Session


class Exam(Base):
    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        self.title = title
        self.description = description
        self.created_by = created_by

class ExamSchema(Schema):
  id = fields.Number()
  title = fields.Str()
  description = fields.Str()
  created_at = fields.DateTime()
  created_by = fields.Str()
  updated_at = fields.DateTime()
  last_updated_by = fields.Str()

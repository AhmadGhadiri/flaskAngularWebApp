from flask import request
from flask_restful import Resource
from entities.entity import Session
from entities.exam import Exam, ExamSchema

class exams(Resource):
  def get(self):
    # Fetching from the database
    session = Session()
    exam_objects = session.query(Exam).all()
    
    # Transforming into JSON-serializable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # Serializing as JSON
    session.close()
    return exams.data, 200

  def post(self):
    # Mount exam object
    posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())

    exam = Exam(**posted_exam.data, created_by = "HTTP post request")

    # Persist exam
    session = Session()
    session.add(exam)
    session.commit()
    
    # Return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return new_exam, 201

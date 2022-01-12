# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from entities.entity import Session, engine, Base
from entities.exam import Exam, ExamSchema
from auth import AuthError, requires_auth



# Creating the Flask application
app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
  # Fetching from the database
  session = Session()
  exam_objects = session.query(Exam).all()
  
  # Transforming into JSON-serializable objects
  schema = ExamSchema(many=True)
  exams = schema.dump(exam_objects)

  # Serializing as JSON
  session.close()
  return jsonify(exams.data)  

@app.route('/exams', methods = ['POST'])
@requires_auth
def add_exam():
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
  return jsonify(new_exam), 201

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

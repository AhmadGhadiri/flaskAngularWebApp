# coding=utf-8

from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from models.entity import Session, engine, Base
from models.user import User, UserSchema
from models.exam import Exam, ExamSchema
# from entities.role import Role, roles_parents

from flask_rbac import RBAC

# Creating the Flask application
app = Flask(__name__)
api = Api(app)
CORS(app)
# RBAC(app)

# Authorization with jwt
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

# generate database schema 
# it is important to import all the schemas before
# this to create them all
Base.metadata.create_all(engine)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'word'}


from resources import exams, users
api.add_resource(HelloWorld, '/')
api.add_resource(exams.exams, '/exams')
api.add_resource(users.UserRegistration, '/register')
api.add_resource(users.UserLogin, '/login')
api.add_resource(users.AllUsers, '/users')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

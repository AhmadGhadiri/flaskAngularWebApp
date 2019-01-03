from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from entities.entity import Session
from entities.user import User, UserSchema

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        # Mount exam object
        
        if User.find_by_username(data['username']):
          return 'User {} already exists'. format(data['username'])

        posted_user = UserSchema(only=('username', 'password')).load(request.get_json())
        # return posted_user.data["password"]
        posted_user.data["password"] = User.generate_hash(posted_user.data["password"])
        # return posted_user

        try:
            user = User(**posted_user.data)

            # Persist exam
            session = Session()
            session.add(user)
            session.commit()
    
            # Return created User
            new_user = UserSchema().dump(user).data
            session.close()
            print ("here")
            # return new_user, 201
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            # return {
            #     'message': 'User {} was created'.format(data['username']),
            #     'access_token': access_token,
            #     'refresh_token': refresh_token
            # }
            return 'User {} was created'.format(data['username']), 201   
        except:
            return 'Something went wrong', 500 

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return 'User {} doesn\'t exist'.format(data['username'])

        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                    'message': 'Logged in as {}'.format(current_user.username),
                    'access_token': access_token, 
                    'refresh_token': refresh_token
            }
        else:
            return {
                'message': 'Wrong credentials'
            }
class AllUsers(Resource):
    @jwt_required
    def get(self):
        # Fetching from the database
        session = Session()
        user_objects = session.query(User).all()
        
        # Transforming into JSON-serializable objects
        schema = UserSchema(many=True)
        users = schema.dump(user_objects)

        # Serializing as JSON
        session.close()
        return users.data, 201


#     def delete(self):
#         return User.delete_all()
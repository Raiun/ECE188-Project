from flask_restful import Resource, reqparse
from models import User
from database import db

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('email', type=str, required=True, help='Email is required')

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'username': user.username, 'email': user.email}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        args = user_parser.parse_args()
        user.username = args['username']
        user.email = args['email']
        db.session.commit()
        return {'message': 'User updated', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

    def post(self):
        args = user_parser.parse_args()
        user = User(username=args['username'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}, 201

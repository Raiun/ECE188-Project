from flask import Flask
from flask_restful import Api
from story import StoryListResource, StoryResource
from user import UserResource, UserListResource
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///read_along.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

def create_tables():
    with app.app_context():
        db.create_all()

api.add_resource(StoryListResource, '/stories')
api.add_resource(StoryResource, '/stories/<int:story_id>')
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')

if __name__ == '__main__':
    create_tables()  # Ensure tables are created before running the app
    app.run(debug=True)


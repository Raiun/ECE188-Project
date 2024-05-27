from flask import Flask
from models import db
from routes import create_user, create_story, create_evaluation, get_user, get_story
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Registering the routes
app.add_url_rule('/users', view_func=create_user, methods=['POST'])
app.add_url_rule('/stories', view_func=create_story, methods=['POST'])
app.add_url_rule('/evaluations', view_func=create_evaluation, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=get_user, methods=['GET'])
app.add_url_rule('/stories/<int:story_id>', view_func=get_story, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)

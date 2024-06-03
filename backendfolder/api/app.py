from flask import Flask
from models import db
from routes import main as main_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for our data models
    app.run(debug=True)


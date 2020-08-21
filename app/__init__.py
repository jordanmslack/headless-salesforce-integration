import os
from dotenv import load_dotenv
from flask import Flask


def create_app():

    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)

    app = Flask(__name__, template_folder='templates')

    app.secret_key = os.getenv('SECRET_KEY', '')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.controllers import api as api_module

    app.register_blueprint(api_module)

    return app

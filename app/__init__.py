#initalising flask
from flask import Flask
from flask_bcrypt import Bcrypt
from app.config import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
bcrypt = Bcrypt()

def create_app(config_hi):
    flaskApp = Flask(__name__)
    flaskApp.config.from_object(config_hi)

    from app.blueprints import main
    flaskApp.register_blueprint(main)
    db.init_app(flaskApp)
    login_manager.init_app(flaskApp)
    bcrypt.init_app(flaskApp)

    return flaskApp

from app import model



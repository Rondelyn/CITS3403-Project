#initalising flask
from flask import Flask

from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db, render_as_batch= True)
flaskApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
flaskApp.config['SECRET_KEY'] = 'thisisasecretkey'

from app import routes, model



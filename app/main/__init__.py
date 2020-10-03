from flask import Blueprint
main = Blueprint('main',__name__)
from . import views
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap 
db = SQLAlchemy


def create_app(config_name):
    app = Flask(__name__)

    # Initialize flask extentensins 

    bootstrap.init_app(app)
    db.init_app(app)
    
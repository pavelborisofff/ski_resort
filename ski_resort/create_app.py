from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from config import Config
from db import db
from models.item import SlopeModel, LiftModel, ActModel
from security import authenticate, identity


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    jwt = JWT(app, authenticate, identity)

    # api.add_resource(ActModel, '/act')
    # api.add_resource(LiftModel, '/lift')
    # api.add_resource(SlopeModel, '/slope')

    return app




from flask import Flask
from flask_cors import CORS

from config import Config
from .db_proxy import db, setup_db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(Config)

    with app.app_context():
        # import routes and db
        setup_db()
        from . import routes
        return app

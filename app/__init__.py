<<<<<<< HEAD
from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    with app.app_context():
        # import routes and db
        return app
=======
<ddddddd> 

asdfi asdf das 
>>>>>>> eb4a1bd1df29928f9acb93077fe618d0bd3476f0

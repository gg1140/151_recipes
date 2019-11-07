import os
"""Flask app configuration"""


class Config:
    """General Config"""
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    #TESTING = True
    #DEBUG = True
    #SECRET_KEY = ''
    #SESSION_COOKIE_NAME = 'my_cookie'

    """Database"""
    DATABASE_URI = "sqlite:///" + os.path.join(APP_DIR, 'app/recipe_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

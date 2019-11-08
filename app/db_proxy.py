from flask import current_app as app
from sqlite_db import SqliteDB

# Import this db object from other parts of the Flask app ...
# ... to access database
db = SqliteDB()


# Provide file path to set up the db object
def setup_db():
    db.connect(app.config['DATABASE_URI'], echo=False)
    return

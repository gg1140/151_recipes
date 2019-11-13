from flask import current_app as app

from .sqlite_db import SqliteDB
from .models import *

# Import this db object from other parts of the Flask app ...
# ... to access database
db = SqliteDB()


# Provide file path to set up the db object
def setup_db():
	print(app.config["DATABASE_URI"])
	db.connect(app.config["DATABASE_URI"], orm_base=orm_base, echo=False)
	return
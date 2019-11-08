from flask import current_app as app

from .sqlite_db import SqliteDB
from .models import *

# Import this db object from other parts of the Flask app ...
# ... to access database
db = SqliteDB()


# Provide file path to set up the db object
def setup_db():
    db.connect(app.config['DATABASE_URI'], orm_base=orm_base, echo=False)
    # List all tables in the database object
    # for tb in db.orm_base.metadata.tables.keys():
    #    print("Table: %s" % tb)
    return

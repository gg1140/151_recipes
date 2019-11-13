from flask import request
from flask import current_app as app

from .models.ingredients import Ingredients
from .db_proxy import db


@app.route('/', methods=['GET'])
def test():
    text_output = ""
    with db.get_sesh() as query_session:
        items = query_session.query(Ingredients).all()
        for i in items:
            text_output += i.name
            text_output += ", "
    return text_output  

    
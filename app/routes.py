from flask import request
from flask import current_app as app

from .models.ingredients import Ingredients
from .db_proxy import db


@app.route('/', methods=['GET'])
def test():
    # This is an example for inserting new item into Ingredients table
    # with db.get_sesh() as add_session:
    #     new_ingred = Ingredients(name='onion')
    #     add_session.add(new_ingred)

    # This is an example for retriving all items from the Ingredients table
    text_output = ""
    with db.get_sesh() as query_sesh:
        items = query_sesh.query(Ingredients).all()
        for i in items:
            text_output += i.name
            text_output += ", "
            print(i.name)
    return text_output

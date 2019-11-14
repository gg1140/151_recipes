from flask import request, render_template, make_response, url_for
from flask import current_app as app

from .models import *
from .db_proxy import db


@app.route('/add', methods=['GET', 'POST'])
def test_add():
    # This is an example for inserting new item into Ingredients table
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        ingredient = request.form['ingredient']

        with db.get_sesh() as add_session:
            new_ingred = Ingredients(name=ingredient)
            new_recipe = Recipes(name=recipe_name, body="",
                                 ingredients=[new_ingred])
            add_session.add(new_recipe)
            add_session.add(new_ingred)
        return url_for('test_query_recipe')
    return render_template('db_input_test.html')


@app.route('/query_ingredients', methods=['GET'])
def test_query_ingredient():
    # This is an example for retriving all items from the Ingredients table
    text_output = ""
    with db.get_sesh() as query_sesh:
        items = query_sesh.query(Ingredients).all()
        for i in items:
            text_output += i.name
            text_output += ", "
            print(i.name)
    return text_output


@app.route('/query_recipes', methods=['GET'])
def test_query_recipe():
    text_output = ""
    with db.get_sesh() as query_sesh:
        items = query_sesh.query(Recipes).all()
        for i in items:
            text_output += i.name
            text_output += ", "
            print(i.name)
    return text_output

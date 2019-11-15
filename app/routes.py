from flask import request, render_template, make_response, url_for, jsonify
from flask import current_app as app
from sqlalchemy.sql import exists

from .models import *
from .db_proxy import db
from .helpers import *


@app.route('/test/', methods=['GET'])
def test_server_activity():
    if request.method == 'GET':
        return 'Server is Live!'


@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        ingredient = request.form['ingredient']

        with db.get_sesh() as add_session:
            new_ingred = Ingredients(name=ingredient)
            new_recipe = Recipes(name=recipe_name, body="",
                                 ingredients=[new_ingred])
            add_session.add(new_recipe)
            add_session.add(new_ingred)
        return url_for('recipe_ap')
    return render_template('db_input_test.html')


@app.route('/recipe/', methods=['GET', 'POST'])
def recipe_ap():

    if request.method == 'GET':
        output = []
        # retrive data
        with db.get_sesh() as sesh:
            recipe_list = sesh.query(Recipes).all()

            for r in recipe_list:
                output.append(Recipes.toDict(r))

        return jsonify(output)

    elif request.method == 'POST':
        # !!!! Check the incoming request is in json format !!!!
        # unpack the json and insert into database
        input = request.get_json()

        with db.get_sesh() as sesh:
            #input['name'] = string_normalize(input['name'])

            new_recipe = Recipes(name=input['name'], body=input['body'])

            ingredients = []

            for i in input['ingredients']:
                i = string_normalize(i)
                (in_db,), = sesh.query(exists().where(Ingredients.name == i))
                if not in_db:
                    new_ingredient = Ingredients(name=i)
                    sesh.add(new_ingredient)

                ingred_obj = sesh.query(Ingredients).filter_by(name=i).first()
                ingredients.append(ingred_obj)

            new_recipe.ingredients = ingredients
            sesh.add(new_recipe)

        return 'Added to database successfully'


@app.route('/ingredient/', methods=['GET', 'POST'])
def ingredient_ap():

    if request.method == 'GET':
        output = []

        with db.get_sesh() as sesh:
            ingred_list = sesh.query(Ingredients).all()

            for i in ingred_list:
                output.append(Ingredients.toDict(i))

        return jsonify(output)

    elif request.method == 'POST':
        # !!!! Check the incoming request is in json format !!!!
        # unpack the json and insert into database
        input = request.get_json()
        input['name'] = string_normalize(input['name'])

        # check uniqueness then insert to db
        with db.get_sesh() as sesh:
            in_db = sesh.query(exists().where(
                Ingredients.name == input['name']))
            if not in_db:
                new_ingredient = Ingredients(name=i)
                sesh.add(new_ingredient)
                return 'Added to database successfully'
            else:
                return 'Insertion failed'

from flask import request, render_template, make_response, url_for, jsonify
from flask import current_app as app
from sqlalchemy.sql import exists

from .models import *
from .db_proxy import db
from .helpers import *
from .db_trans import RecipeQueryHelper, IngredientQueryHelper


@app.route('/test/', methods=['GET'])
def test_server_activity():
    if request.method == 'GET':
        return 'Server is Live!'


@app.route('/add/', methods=['POST'])
def add():
    if request.method == 'POST':
        input = request.get_json()
        with db.get_sesh() as sesh:
            #input['name'] = string_normalize(input['name'])
            for r in input:
                new_recipe = Recipes(
                    name=r['name'], body=r['body'], imgUrl=r['imgUrl'])

                ingredients = []

                for i in r['ingredients']:
                    i = string_normalize(i)
                    (in_db,), = sesh.query(exists().where(Ingredients.name == i))
                    if not in_db:
                        new_ingredient = Ingredients(name=i)
                        sesh.add(new_ingredient)

                    ingred_obj = sesh.query(
                        Ingredients).filter_by(name=i).first()
                    ingredients.append(ingred_obj)

                new_recipe.ingredients = ingredients
                sesh.add(new_recipe)
    return "Add called"


@app.route('/recipe/', methods=['GET', 'POST'])
def recipe_ap():

    if request.method == 'GET':
        output = []
        opt = request.args['opt']
        input = request.args
        if opt == 'all':
            output = RecipeQueryHelper.all()
        elif opt == 'by_id' and input is not None:
            output = RecipeQueryHelper.by_id(ids=input['ids'])
        elif opt == 'by_name' and input is not None:
            output = RecipeQueryHelper.by_name(names=input['names'])
        elif opt == 'by_ingredient' and input is not None:
            output = RecipeQueryHelper.by_ingredient(
                ingredients=input['ingredients'])
        return jsonify(output)

    elif request.method == 'POST':
        # !!!! Check the incoming request is in json format !!!!
        # unpack the json and insert into database
        input = request.get_json()

        with db.get_sesh() as sesh:
            #input['name'] = string_normalize(input['name'])

            new_recipe = Recipes(
                name=input['name'], body=input['body'], imgUrl=input['imgUrl'])

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
        opt = request.args['opt']
        input = request.args
        if opt == 'all':
            output = IngredientQueryHelper.all()
        elif opt == 'by_id' and input is not None:
            output = IngredientQueryHelper.by_id(ids=input['ids'])
        elif opt == 'by_name' and input is not None:
            output = IngredientQueryHelper.by_name(names=input['names'])
        elif opt == 'by_recipe' and input is not None:
            output = IngredientQueryHelper.by_recipe(
                recipes=input['recipes'])

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

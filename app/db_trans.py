from sqlalchemy import *
from sqlalchemy.orm import load_only

from .models import *
from .db_proxy import db

# normalize input


class RecipeQueryHelper():

    # get all
    @classmethod
    def all(cls, *col):
        result = []
        with db.get_sesh() as sesh:
            recipe_ls = sesh.query(Recipes).all()

            for r in recipe_ls:
                result.append(Recipes.toDict(r))
        return result  # dictionary

# get by id
    @classmethod
    def by_id(cls, ids=[]):
        result = []
        with db.get_sesh() as sesh:
            for id in ids:
                r = sesh.query(Recipes).get(id)
                result.append(Recipes.toDict(r))
        return result


# filter by name
    @classmethod
    def by_name(cls, names=[]):
        names = names.split(",")
        result = []
        with db.get_sesh() as sesh:
            for name in names:
                #recipes = sesh.query(Recipes).filter(Recipes.name == name)
                recipes = sesh.query(Recipes).filter(
                    Recipes.name.contains(name))
                for r in recipes:
                    result.append(Recipes.toDict(r))
        return result

# filter by ingredient
    @classmethod
    def by_ingredient(cls, ingredients=[]):
        ingredients = ingredients.split(",")
        result = []
        with db.get_sesh() as sesh:
            for ing in ingredients:
                recipes = sesh.query(Recipes).filter(
                    Recipes.ingredients.any(name=ing))
                for r in recipes:
                    result.append(Recipes.toDict(r))
        return result


class IngredientQueryHelper():

    @classmethod
    def all(cls):
        result = []
        with db.get_sesh() as sesh:
            ingred_ls = sesh.query(Ingredients).all()

            for i in ingred_ls:
                result.append(Ingredients.toDict(i))
        return result

    @classmethod
    def by_id(cls, ids=[]):
        result = []
        with db.get_sesh() as sesh:
            for id in ids:
                ingred = sesh.query(Ingredients).get(id)
                result.append(Ingredients.toDict(ingred))
        return result

    @classmethod
    def by_name(cls, names=[]):
        names = names.split(",")
        result = []
        with db.get_sesh() as sesh:
            for name in names:
                ingred_ls = sesh.query(Ingredients).filter(
                    Ingredients.name.contains(name))
                for i in ingred_ls:
                    result.append(Ingredients.toDict(i))
        return result

    @classmethod
    def by_recipe(cls, recipes=[]):
        recipes = recipes.split(",")
        result = []
        with db.get_sesh() as sesh:
            for r in recipes:
                ingred_ls = sesh.query(Ingredients).filter(
                    Recipes.ingredients.any(name=r))
                for i in ingred_ls:
                    result.append(Ingredients.toDict(i))
        return result

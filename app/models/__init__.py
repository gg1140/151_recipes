__all__ = ["orm_base", "Recipes_Ingredients",
           "Recipes", "Ingredients"]

from sqlalchemy.ext.declarative import declarative_base

orm_base = declarative_base()

from .recipes_ingredients import Recipes_Ingredients
from .recipes import Recipes
from .ingredients import Ingredients
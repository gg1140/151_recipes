__all__ = ["orm_base", "recipes", "ingredients", "recipes_ingredients"]

from sqlalchemy.ext.declarative import declarative_base

orm_base = declarative_base()

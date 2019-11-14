from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import orm_base
from .recipes_ingredients import Recipes_Ingredients


class Recipes(orm_base):
    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    body = Column(String)
    ingredients = relationship(
        "Ingredients", secondary=Recipes_Ingredients, back_populates="recipes")

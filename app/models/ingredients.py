from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import orm_base
from .recipes_ingredients import Recipes_Ingredients


class Ingredients(orm_base):
    __tablename__ = "Ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    recipes = relationship(
        "Recipes", secondary=Recipes_Ingredients, back_populates="ingredients")

    @classmethod
    def toDict(cls, ingred):
        output = {
            'name': ingred.name,
            'recipes': []}
        for i in ingred.recipes:
            output['recipes'].append(i.name)
        return output

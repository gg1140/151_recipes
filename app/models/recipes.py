from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import orm_base
from .recipes_ingredients import Recipes_Ingredients


class Recipes(orm_base):
    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    body = Column(String)
    imgUrl = Column(String)
    ingredients = relationship(
        "Ingredients", secondary=Recipes_Ingredients, back_populates="recipes")

    @classmethod
    def toDict(cls, recipe):
        output = {
            'id': recipe.id,
            'name': recipe.name,
            'body': recipe.body,
            'imgUrl': recipe.imgUrl,
            'ingredients': []}
        for i in recipe.ingredients:
            output['ingredients'].append(i.name)
        return output

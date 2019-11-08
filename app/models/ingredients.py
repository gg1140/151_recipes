from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import orm_base
from .recipes_ingredients import Receipes_Ingredients


class Ingredients(orm_base):
    __tablename__ = "Ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    # recipes = relationship(
    #    "Receipes", secondary="Receipes_Ingredients")

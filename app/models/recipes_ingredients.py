from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import orm_base

Recipes_Ingredients = Table("Recipes_Ingredients", orm_base.metadata,
                            Column("Recipes_id", Integer,
                                   ForeignKey("Recipes.id")),
                            Column("Ingredients_id", Integer, ForeignKey("Ingredients.id")))

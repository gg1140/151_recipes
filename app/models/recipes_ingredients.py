from sqlalchemy import Table, Column, Integer, ForeignKey

from . import orm_base

Receipes_Ingredients = Table("Recipes-Ingredients", orm_base.metadata,
                             Column("Recipes_id", Integer,
                                    ForeignKey("Recipes.id")),
                             Column("Ingredients_id", Integer, ForeignKey("Ingredients.id")))

from marshmallow import Schema, fields


# class RecipesSchema(Schema):
#name = fields.Str()
#body = fields.Str()
#ingredients = fields.Nested(IngredientSchema)


def RecipestoDict(recipe):
    output = {
        'name': recipe.name,
        'body': recipe.body,
        'ingredients': []}
    for i in recipe.ingredients:
        output['ingredients'].append(i.name)
    return output

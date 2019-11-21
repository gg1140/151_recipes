import { ResourceData } from "./resource-data";

export class RecipeData extends ResourceData {
  body: string;
  ingredients: string[];

  constructor(objectModel: {}) {
    super(objectModel);
    this.dataType = "recipe";
    this.body = objectModel["body"];
    this.ingredients = objectModel["ingredients"];
  }
}

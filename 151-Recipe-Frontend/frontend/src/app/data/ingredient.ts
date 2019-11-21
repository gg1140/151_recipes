import { ResourceData } from "./resource-data";

export class IngredientData extends ResourceData {
  recipes: string[];

  constructor(objectModel: {}) {
    super(objectModel);
    this.dataType = "ingredient";
    this.recipes = objectModel["recipes"];
  }
}

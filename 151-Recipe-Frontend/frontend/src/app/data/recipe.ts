import { ResourceData } from "./resource-data";

export class RecipeData extends ResourceData {
  body: string;
  ingredients: string[];
  imgUrl: string;

  constructor(objectModel: {}) {
    super(objectModel);
    this.dataType = "recipe";
    this.body = objectModel["body"];
    this.ingredients = objectModel["ingredients"];
    this.imgUrl = objectModel["imgUrl"];
  }
}

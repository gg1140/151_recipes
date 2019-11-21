import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";

import { BACKEND_URL } from "../backend_url";
import { RecipeData } from "../data/recipe";
import { IngredientData } from "../data/ingredient";
import { ResourceData } from "../data/resource-data";
import { QueryData } from "../data/query-header";

@Injectable({
  providedIn: "root"
})
export class BackendService {
  backendUrl: string = BACKEND_URL;

  constructor(private http: HttpClient) {}

  private sendRequest(endpoint: string, param?: HttpParams): Promise<any> {
    const url = this.backendUrl + endpoint;
    let data;
    if (param !== undefined) {
      console.log(url);
      data = this.http.get(url, { params: param }).toPromise();
    } else {
      data = this.http.get(url).toPromise();
    }
    return data;
  }

  searchFor(
    resourceType: string,
    queryFields: HttpParams
  ): Promise<ResourceData[]> {
    console.log(queryFields);
    if (resourceType === "recipe") {
      return this.sendRequest("/recipe", queryFields).then(data => {
        let output = data;
        output.forEach((item, i) => {
          output[i] = new RecipeData(item);
        });
        console.log(output);
        return output;
      });
    } else if (resourceType === "ingredient") {
      return this.sendRequest("/ingredient", queryFields).then(data => {
        let output = data;
        output.forEach((item, i) => {
          output[i] = new IngredientData(item);
        });
        return output;
      });
    }
  }

  /* allIngredient(): Promise<IngredientData[]> {
    const headers = new HttpHeaders({ opt: "all" });
    headers.set("Content-Type", "application/json");
    return this.sendRequest("/ingredient", headers).then(data => {
      let output = data;
      output.forEach((item, i) => {
        output[i] = new IngredientData(item);
      });
      return output;
    });
  }

  allRecipe(): Promise<RecipeData[]> {
    const headers = new HttpHeaders({ opt: "all" });
    headers.set("Content-Type", "application/json");
    return this.sendRequest("/recipe", headers).then(data => {
      let output = data;
      output.forEach((item, i) => {
        output[i] = new RecipeData(item);
      });
      return output;
    });
  }
*/
  recipeById(): Promise<RecipeData> {
    return null;
  }

  recipesByName(): Promise<RecipeData[]> {
    return null;
  }

  recipesByIngredients(): Promise<RecipeData[]> {
    return null;
  }

  ingredientById(): Promise<IngredientData> {
    return null;
  }

  ingredientsByName(): Promise<IngredientData[]> {
    return null;
  }

  ingredientsByRecipe(): Promise<IngredientData[]> {
    return null;
  }
}

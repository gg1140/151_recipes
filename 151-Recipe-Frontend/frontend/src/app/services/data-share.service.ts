import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";

import { ResourceData } from "../data/resource-data";
import { RecipeData } from "../data/recipe";

@Injectable({
  providedIn: "root"
})
export class DataShareService {
  private retrievedData = new BehaviorSubject<ResourceData[]>([
    new RecipeData({ name: "", id: "", body: "", ingredients: "" })
  ]);
  currentData = this.retrievedData.asObservable();

  constructor() {}

  changeData(newData: ResourceData[]) {
    this.retrievedData.next(newData);
    console.log(this.retrievedData);
  }
}

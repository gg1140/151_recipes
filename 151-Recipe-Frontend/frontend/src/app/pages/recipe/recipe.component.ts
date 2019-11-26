import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute } from "@angular/router";

import { DataShareService } from "../../services/data-share.service";
import { ResourceData } from "../../data/resource-data";
import { RecipeData } from "../../data/recipe";

@Component({
  selector: "app-recipe",
  templateUrl: "./recipe.component.html",
  styleUrls: ["./recipe.component.css"]
})
export class RecipeComponent implements OnInit {
  id: number;
  private sub: any;
  recipe: ResourceData;
  resources: ResourceData[];

  constructor(private route: ActivatedRoute, private data: DataShareService) {}

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = +params["id"];
    });
    this.data.currentData.subscribe(results => (this.resources = results));
    console.log(this.resources);
    var i;
    for (i = 0; i < this.resources.length; i++) {
      var temp = parseInt(this.resources[i]["id"]);
      if (temp === this.id) {
        this.recipe = this.resources[i];
        break;
      }
    }
  }

  getRecipeBody() {
    if (this.recipe !== undefined) {
      return this.recipe["body"].replace(/(?:\r\n|\r|\n|\\n)/g, "<br>");
    }
    return "";
  }
}

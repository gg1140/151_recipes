import { Component, OnInit, Input } from "@angular/core";

import { HttpParams } from "@angular/common/http";
import { RecipeData } from "../../data/recipe";
import { ResourceData } from "../../data/resource-data";
import { BackendService } from "../../services/backend.service";
import { DataShareService } from "../../services/data-share.service";
import { Router } from "@angular/router";
@Component({
  selector: "app-recipe-thumbnail",
  templateUrl: "./recipe-thumbnail.component.html",
  styleUrls: ["./recipe-thumbnail.component.css"]
})
export class RecipeThumbnailComponent implements OnInit {
  @Input() resource: ResourceData;

  constructor(
    private server: BackendService,
    private data: DataShareService,
    private router: Router
  ) {}

  ngOnInit() {}

  isRecipe() {
    if (this.resource["dataType"] === "recipe") {
      return true;
    } else {
      return false;
    }
  }

  search() {
    const params = new HttpParams()
      .append("opt", "by_ingredient")
      .append("ingredients", this.resource["name"]);

    this.server.searchFor("recipe", params).then(data => {
      console.log(data);
      //this.resources = data;
      this.data.changeData(data);
      this.router.navigate(["/search-result"]);
    });
  }
}

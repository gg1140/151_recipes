import { Component, OnInit, Input } from "@angular/core";

import { RecipeData } from "../../data/recipe";
import { ResourceData } from "../../data/resource-data";

@Component({
  selector: "app-recipe-thumbnail",
  templateUrl: "./recipe-thumbnail.component.html",
  styleUrls: ["./recipe-thumbnail.component.css"]
})
export class RecipeThumbnailComponent implements OnInit {
  @Input() resource: ResourceData;

  constructor() {}

  ngOnInit() {}
}

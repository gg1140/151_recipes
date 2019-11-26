import { Component, OnInit, Input } from "@angular/core";

import { DataShareService } from "../../services/data-share.service";
import { ResourceData } from "../../data/resource-data";
import { RecipeData } from "../../data/recipe";

@Component({
  selector: "app-search-result",
  templateUrl: "./search-result.component.html",
  styleUrls: ["./search-result.component.css"]
})
export class SearchResultComponent implements OnInit {
  results: ResourceData[];

  constructor(private data: DataShareService) {}

  ngOnInit() {
    this.data.currentData.subscribe(results => (this.results = results));
  }
}

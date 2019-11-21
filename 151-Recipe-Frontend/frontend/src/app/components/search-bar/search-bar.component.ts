import { Component, OnInit } from "@angular/core";

import { ResourceData } from "../../data/resource-data";
import { QueryData } from "../../data/query-header";
import { BackendService } from "../../services/backend.service";
import { HttpParams } from "@angular/common/http";

@Component({
  selector: "app-search-bar",
  templateUrl: "./search-bar.component.html",
  styleUrls: ["./search-bar.component.css"]
})
export class SearchBarComponent implements OnInit {
  queryString: string;
  searchCategories: string[] = ["recipe", "ingredient"];
  searchCategory: string = "recipe";
  resources: ResourceData[];

  constructor(private server: BackendService) {}

  ngOnInit() {}

  search() {
    let treatedStr = this.queryString.replace(/ /g, ",");
    let params = new HttpParams()
      .append("opt", "by_name")
      .append("names", treatedStr);

    let result = this.server
      .searchFor(this.searchCategory, params)
      .then(data => {
        console.log(data);
        return data;
      });
  }
}

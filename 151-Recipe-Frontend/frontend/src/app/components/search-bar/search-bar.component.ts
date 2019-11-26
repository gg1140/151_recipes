import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";

import { ResourceData } from "../../data/resource-data";
import { QueryData } from "../../data/query-header";
import { BackendService } from "../../services/backend.service";
import { HttpParams } from "@angular/common/http";
import { DataShareService } from "../../services/data-share.service";

@Component({
  selector: "app-search-bar",
  templateUrl: "./search-bar.component.html",
  styleUrls: ["./search-bar.component.css"]
})
export class SearchBarComponent implements OnInit {
  queryString: string;
  searchCategory: string = "recipe";
  searchCategories: string[] = ["recipe", "ingredient"];
  resources: ResourceData[];

  constructor(
    private server: BackendService,
    private data: DataShareService,
    private router: Router
  ) {}

  ngOnInit() {}

  search() {
    const treatedStr = this.queryString.replace(/ /g, ",");
    const params = new HttpParams()
      .append("opt", "by_name")
      .append("names", treatedStr);

    this.server.searchFor(this.searchCategory, params).then(data => {
      console.log(data);
      //this.resources = data;
      this.data.changeData(data);
      this.router.navigate(["/search-result"]);
    });
  }
}

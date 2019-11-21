import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { HomeComponent } from "./home/home.component";
import { AboutComponent } from "./about/about.component";
import { SearchResultComponent } from "./search-result/search-result.component";
import { RecipeComponent } from "./recipe/recipe.component";
import { ContactComponent } from "./contact/contact.component";

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "home",
    component: HomeComponent
  },
  {
    path: "about",
    component: AboutComponent
  },
  {
    path: "contact",
    component: ContactComponent
  },
  {
    path: "recipe/:id",
    component: RecipeComponent
  },
  {
    path: "search/:query",
    component: SearchResultComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}

export const routingComponent = [
  HomeComponent,
  AboutComponent,
  ContactComponent,
  SearchResultComponent,
  RecipeComponent
];

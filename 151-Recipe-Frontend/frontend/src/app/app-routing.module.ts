import { NgModule } from "@angular/core";
import { Routes, RouterModule, ExtraOptions } from "@angular/router";

import { HomeComponent } from "./pages/home/home.component";
import { AboutComponent } from "./pages/about/about.component";
import { ContactComponent } from "./pages/contact/contact.component";
import { RecipeComponent } from "./pages/recipe/recipe.component";
import { SearchResultComponent } from "./pages/search-result/search-result.component";

const routerOptions: ExtraOptions = {
  useHash: false,
  anchorScrolling: "enabled"
};

const routes: Routes = [
  { path: "", component: HomeComponent },
  { path: "home", component: HomeComponent },
  { path: "about", component: AboutComponent },
  { path: "contact", component: ContactComponent },
  { path: "recipe/:id", component: RecipeComponent },
  { path: "search-result", component: SearchResultComponent }
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
  RecipeComponent,
  SearchResultComponent
];

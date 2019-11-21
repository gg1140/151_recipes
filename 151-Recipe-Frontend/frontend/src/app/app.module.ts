import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";
import { FormsModule } from "@angular/forms";

import { AppRoutingModule, routingComponent } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { SearchBarComponent } from "./components/search-bar/search-bar.component";
import { NavComponent } from "./components/nav/nav.component";
import { BackendService } from "./services/backend.service";
import { SearchResultComponent } from './pages/search-result/search-result.component';
import { RecipeThumbnailComponent } from './components/recipe-thumbnail/recipe-thumbnail.component';

@NgModule({
  declarations: [
    AppComponent,
    routingComponent,
    NavComponent,
    SearchBarComponent,
    SearchResultComponent,
    RecipeThumbnailComponent
  ],
  imports: [BrowserModule, HttpClientModule, FormsModule, AppRoutingModule],
  providers: [BackendService],
  bootstrap: [AppComponent]
})
export class AppModule {}

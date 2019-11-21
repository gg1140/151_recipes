import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule, routingComponent } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { NavigationBarComponent } from "./navigation-bar/navigation-bar.component";
import { SearchBoxComponent } from "./search-box/search-box.component";
/*import { SearchService } from "./services/search.service";*/

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    routingComponent,
    SearchBoxComponent
  ],
  imports: [BrowserModule, AppRoutingModule],
  providers: [
    /*SearchService*/
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}

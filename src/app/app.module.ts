import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar';
import { PublicationPageComponent } from './pages/publication-page/publication-page.component';
import {MatCardModule} from '@angular/material/card';
import {MatExpansionModule} from '@angular/material/expansion';
import {MatIconModule} from '@angular/material/icon';
import {MatGridListModule} from '@angular/material/grid-list';
import { HomePageComponent } from './pages/home-page/home-page.component';
import {MatButtonModule} from '@angular/material/button';
import { HttpClientModule } from "@angular/common/http";
import {MatListModule} from '@angular/material/list';
import { UranusModule } from './uranus/uranus.module';

@NgModule({
  declarations: [
    AppComponent,
    PublicationPageComponent,
    HomePageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatCardModule,
    MatExpansionModule,
    MatIconModule,
    MatGridListModule,
    MatButtonModule,
    HttpClientModule,
    MatListModule,
    UranusModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 


  
}

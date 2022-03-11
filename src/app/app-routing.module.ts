import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { PublicationPageComponent } from './pages/publication-page/publication-page.component';

const routes: Routes = [
  {
    path:"publications",
    component: PublicationPageComponent
  },
  {
    path:"",
    component: HomePageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

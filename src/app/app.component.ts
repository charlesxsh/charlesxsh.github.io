import { Component } from '@angular/core';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';
import { NavbarItem } from './uranus/components/navbar/navbar-item';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  navItems: NavbarItem[] = [
    {
      name: "Home",
      link: ""
    },
    {
      name: "Publications",
      link: "publications"
    }
  ]
  constructor(iconReg: MatIconRegistry, domSanitizer: DomSanitizer){
    iconReg.addSvgIcon("github",  domSanitizer.bypassSecurityTrustResourceUrl("assets/github.svg"));
  }
}

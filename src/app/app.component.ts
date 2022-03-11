import { Component } from '@angular/core';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(iconReg: MatIconRegistry, domSanitizer: DomSanitizer){
    iconReg.addSvgIcon("github",  domSanitizer.bypassSecurityTrustResourceUrl("assets/github.svg"));
  }
}

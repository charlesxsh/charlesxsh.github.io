import { Component, OnInit } from '@angular/core';
import { Paper } from 'src/app/components/paper/paper';
import { papers } from 'src/app/papers';

@Component({
  selector: 'app-publication-page',
  templateUrl: './publication-page.component.html',
  styleUrls: ['./publication-page.component.scss']
})
export class PublicationPageComponent implements OnInit {

  papers!: Paper[];
  
  constructor() { }

  ngOnInit(): void {
    this.papers = papers;
  }

}

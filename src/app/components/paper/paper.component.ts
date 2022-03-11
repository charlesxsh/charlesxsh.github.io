import { ChangeDetectionStrategy, Component, Input, OnInit } from '@angular/core';
import { Paper } from './paper';

@Component({
  selector: 'app-paper',
  templateUrl: './paper.component.html',
  styleUrls: ['./paper.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class PaperComponent implements OnInit {

  @Input()
  paper!: Paper;

  abstractOpen = false

  constructor() { }

  ngOnInit(): void {
  }

  openInNewTab(link: string){
    window.open(link);
  }
}

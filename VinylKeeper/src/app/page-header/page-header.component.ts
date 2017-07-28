import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'vk-page-header',
  templateUrl: './page-header.component.html',
  styleUrls: ['./page-header.component.scss']
})
export class PageHeaderComponent implements OnInit {
  @Input() pageName: string;

  constructor() { }

  ngOnInit() {
  }

}

import {Component, Input, OnInit} from '@angular/core';
import {Record} from '../record';

@Component({
  selector: 'vk-records-grid',
  templateUrl: './records-grid.component.html',
  styleUrls: ['./records-grid.component.scss']
})
export class RecordsGridComponent implements OnInit {
  @Input() recordsList: Record[];

  constructor() { }

  ngOnInit() {
  }

}

import {Component, OnInit} from '@angular/core';
import {MOCK_RECORDS, Record} from '../record';

@Component({
  selector: 'vk-records-page',
  templateUrl: './records-page.component.html',
  styleUrls: ['./records-page.component.scss']
})
export class RecordsPageComponent implements OnInit {
  recordsList: Record[];

  constructor() { }

  ngOnInit() {
    this.recordsList = MOCK_RECORDS;
  }

}

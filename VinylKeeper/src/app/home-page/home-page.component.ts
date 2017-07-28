import {Component, OnInit} from '@angular/core';
import {MOCK_RECORDS, Record} from '../record';

@Component({
  selector: 'vk-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  recordsList: Record[];

  constructor() { }

  ngOnInit() {
    this.recordsList = MOCK_RECORDS;
  }

}

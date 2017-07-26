import {Component, Input, OnInit} from '@angular/core';
import {Record} from '../record';

@Component({
  selector: 'vk-record-card',
  templateUrl: './record-card.component.html',
  styleUrls: ['./record-card.component.scss']
})
export class RecordCardComponent implements OnInit {
  @Input() record: Record;

  constructor() { }

  ngOnInit() {
  }

}

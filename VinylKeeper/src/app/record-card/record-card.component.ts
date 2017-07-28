import {Component, Input, OnInit} from '@angular/core';
import {animate, state, style, transition, trigger} from '@angular/animations';
import {Record} from '../record';

@Component({
  selector: 'vk-record-card',
  templateUrl: './record-card.component.html',
  styleUrls: ['./record-card.component.scss'],
  animations: [
    trigger('hover', [
      state('inactive', style({
        transform: 'scale(1)',
      })),
      state('active', style({
        transform: 'scale(1.02)',
      })),
      transition('inactive => active', animate('100ms ease-in')),
      transition('active => inactive', animate('100ms ease-out')),
    ]),
  ],
})
export class RecordCardComponent implements OnInit {
  @Input() record: Record;
  state = 'inactive';

  constructor() { }

  ngOnInit() {
  }

  toggleState() {
    if (this.state === 'inactive') {
      this.state = 'active';
    } else {
      this.state = 'inactive';
    }
  }

}

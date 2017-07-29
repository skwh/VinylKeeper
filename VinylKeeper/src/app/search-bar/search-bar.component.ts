import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'vk-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {
  placeholder = 'Search';
  focused = false;

  constructor() { }

  ngOnInit() {
  }

  toggleFocus() {
    if (!this.placeholder) {
      this.placeholder = 'Search';
    } else {
      this.placeholder = '';
    }
    this.focused = !this.focused;
  }

}

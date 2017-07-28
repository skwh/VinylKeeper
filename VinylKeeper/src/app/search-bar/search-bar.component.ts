import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'vk-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {
  placeholder = 'Search';

  constructor() { }

  ngOnInit() {
  }

  togglePlaceholder() {
    if (!this.placeholder) {
      this.placeholder = 'Search';
    } else {
      this.placeholder = '';
    }
  }

}

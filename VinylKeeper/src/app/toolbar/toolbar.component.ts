import {Component, OnInit} from '@angular/core';
import {UIService} from '../ui.service';

@Component({
  selector: 'vk-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss']
})
export class ToolbarComponent implements OnInit {

  constructor(private ui: UIService) {
  }

  ngOnInit() {

  }

  toggleSidenav() {
    this.ui.sidenavMessageSubject.next();
  }

}

import {Component, OnInit} from '@angular/core';
import {NAV_ITEMS, Navitem} from './navitem';

@Component({
  selector: 'vk-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  navigationList: Navitem[];

  constructor() { }

  ngOnInit() {
    this.navigationList = NAV_ITEMS;
  }

}

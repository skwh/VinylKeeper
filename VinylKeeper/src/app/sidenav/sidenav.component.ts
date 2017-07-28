import {Component, NgZone, OnInit} from '@angular/core';
import {NAV_ITEMS, Navitem} from './navitem';

@Component({
  selector: 'vk-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  navigationList: Navitem[];
  sideNavMode = 'side';
  sideNavOpen = true;

  constructor(private zone: NgZone) {
    window.onresize = (e) => {
      zone.run(() => {
        if (window.innerWidth <= 1024) {
          this.sideNavMode = 'float';
          this.sideNavOpen = false;
        } else {
          this.sideNavOpen = true;
          this.sideNavMode = 'side';
        }
      })
    }
  }

  ngOnInit() {
    this.navigationList = NAV_ITEMS;
  }

}

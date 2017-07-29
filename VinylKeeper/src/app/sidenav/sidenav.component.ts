import {Component, NgZone, OnInit} from '@angular/core';
import {NAV_ITEMS, Navitem} from './navitem';
import {UIService} from '../ui.service';

@Component({
  selector: 'vk-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  navigationList: Navitem[];
  sideNavMode = 'side';
  sideNavOpen = true;

  constructor(private zone: NgZone, private ui: UIService) {
    window.onresize = (e) => {
      zone.run(() => {
        if (window.innerWidth <= 1024) {
          this.sideNavMode = 'float';
          this.sideNavOpen = false;
        } else {
          this.sideNavMode = 'side';
          this.sideNavOpen = true;
        }
      })
    }
  }

  ngOnInit() {
    this.navigationList = NAV_ITEMS;
    this.ui.sidenavMessage$.subscribe(() => {
      this.toggleSidenav();
    })
  }

  toggleSidenav() {
    this.sideNavOpen = !this.sideNavOpen;
  }

}

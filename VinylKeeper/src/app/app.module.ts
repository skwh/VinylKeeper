import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {
  MdButtonModule,
  MdCardModule,
  MdGridListModule,
  MdIconModule,
  MdInputModule,
  MdListModule,
  MdSidenavModule,
  MdToolbarModule,
} from '@angular/material';

import {AppComponent} from './app.component';
import {ToolbarComponent} from './toolbar/toolbar.component';
import {SidenavComponent} from './sidenav/sidenav.component';
import {RecordsPageComponent} from './records-page/records-page.component';
import {RecordCardComponent} from './record-card/record-card.component';
import {SearchBarComponent} from './search-bar/search-bar.component';
import {HomePageComponent} from './home-page/home-page.component';
import {RecordsGridComponent} from './records-grid/records-grid.component';
import {PageNotFoundComponent} from './page-not-found/page-not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    ToolbarComponent,
    SidenavComponent,
    RecordsPageComponent,
    RecordCardComponent,
    SearchBarComponent,
    HomePageComponent,
    RecordsGridComponent,
    PageNotFoundComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MdToolbarModule,
    MdButtonModule,
    MdInputModule,
    MdSidenavModule,
    MdListModule,
    MdIconModule,
    MdGridListModule,
    MdCardModule,
    RouterModule.forRoot([
      {
        path: 'records',
        component: RecordsPageComponent,
      },
      {
        path: 'home',
        component: HomePageComponent,
      },
      {
        path: '',
        redirectTo: '/home',
        pathMatch: 'full',
      },
      {
        path: '**',
        component: PageNotFoundComponent,
      }
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

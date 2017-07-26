import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {
  MdButtonModule,
  MdGridListModule,
  MdIconModule,
  MdInputModule,
  MdListModule,
  MdSidenavModule,
  MdToolbarModule
} from '@angular/material';

import {AppComponent} from './app.component';
import {ToolbarComponent} from './toolbar/toolbar.component';
import {SidenavComponent} from './sidenav/sidenav.component';
import {RecordsPageComponent} from './records-page/records-page.component';
import {RecordCardComponent} from './record-card/record-card.component';

@NgModule({
  declarations: [
    AppComponent,
    ToolbarComponent,
    SidenavComponent,
    RecordsPageComponent,
    RecordCardComponent
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
    RouterModule.forRoot([
      {
        path: 'records',
        component: RecordsPageComponent,
      },
      {
        path: '',
        redirectTo: '/records',
        pathMatch: 'full',
      },
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

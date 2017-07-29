import {Injectable} from '@angular/core';
import {Subject} from 'rxjs/Subject';

@Injectable()
export class UIService {

  sidenavMessageSubject = new Subject();

  sidenavMessage$ = this.sidenavMessageSubject.asObservable();

  constructor() {
  }

}

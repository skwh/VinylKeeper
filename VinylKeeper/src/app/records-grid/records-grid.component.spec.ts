import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {RecordsGridComponent} from './records-grid.component';

describe('RecordsGridComponent', () => {
  let component: RecordsGridComponent;
  let fixture: ComponentFixture<RecordsGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecordsGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecordsGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});

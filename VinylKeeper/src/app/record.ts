export class Record {
  constructor(public title: string, public artists: string[], public coverArtUrl: string) {}
}


export const MOCK_RECORDS: Record[] = [
  {title: 'Wednesday Morning, 3 AM', artists: ['Simon & Garfunkel'], coverArtUrl: '../assets/wed-morning-test.jpg'},
  {title: 'Kind of Blue', artists: ['Miles Davis', 'John Coltrane'], coverArtUrl: '../assets/kind-of-blue-test.jpg'},
  {title: 'Fleetwood Mac', artists: ['Fleetwood Mac'], coverArtUrl: '../assets/fleetwood-mac-test.jpg'},
  {title: 'Pendulum', artists: ['Creedence Clearwater Revival'], coverArtUrl: '../assets/pendulum-test.jpg'},
];

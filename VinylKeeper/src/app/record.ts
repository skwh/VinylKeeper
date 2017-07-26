export class Record {
  constructor(public title: string, public artists: string[], public coverArtUrl: string) {}
}


export const MOCK_RECORDS: Record[] = [
  {title: 'Wednesday Morning 3 AM', artists: ['Simon & Garfunkel'], coverArtUrl: ''},
];

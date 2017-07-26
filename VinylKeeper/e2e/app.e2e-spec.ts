import { VinylKeeperPage } from './app.po';

describe('vinyl-keeper App', () => {
  let page: VinylKeeperPage;

  beforeEach(() => {
    page = new VinylKeeperPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});

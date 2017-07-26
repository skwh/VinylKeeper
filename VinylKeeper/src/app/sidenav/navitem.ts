export class Navitem {
  constructor(public text: string, public iconName: string, public path: string) {}
}

export const NAV_ITEMS: Navitem[] = [
  {text: 'Home', iconName: 'home', path: '/'},
  {text: 'Records', iconName: 'album', path: '/records'},
  {text: 'Artists', iconName: 'group', path: '/artists'},
];

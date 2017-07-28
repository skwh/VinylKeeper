export class Navitem {
  constructor(public text: string, public iconName: string, public path: string, public routerLinkOptions: any) {}
}

export const NAV_ITEMS: Navitem[] = [
  {text: 'Home', iconName: 'home', path: '/home', routerLinkOptions: {exact: true}},
  {text: 'Records', iconName: 'album', path: '/records', routerLinkOptions: ''},
  {text: 'Artists', iconName: 'group', path: '/artists', routerLinkOptions: ''},
];

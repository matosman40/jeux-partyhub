import { fieldSettings } from './games/client/settings.js';
import { PlateauHost } from './games/plateau-fete/client/HostScreen.js';
import { PlateauPlayer } from './games/plateau-fete/client/PlayerScreen.js';

const Settings = fieldSettings([]);

export default { Settings, Host: PlateauHost, Player: PlateauPlayer };

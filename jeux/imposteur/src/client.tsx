import { fieldSettings } from './games/client/settings.js';
import { ImposteurHost } from './games/imposteur/client/HostScreen.js';
import { ImposteurPlayer } from './games/imposteur/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'rounds', label: 'Manches', min: 1, max: 8 }]);

export default { Settings, Host: ImposteurHost, Player: ImposteurPlayer };

import { fieldSettings } from './games/client/settings.js';
import { MicroDefisHost } from './games/micro-defis/client/HostScreen.js';
import { MicroDefisPlayer } from './games/micro-defis/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'rounds', label: 'Défis', min: 1, max: 12 }]);

export default { Settings, Host: MicroDefisHost, Player: MicroDefisPlayer };

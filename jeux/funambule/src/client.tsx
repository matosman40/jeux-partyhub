import { fieldSettings } from './games/client/settings.js';
import { FunambuleHost } from './games/funambule/client/HostScreen.js';
import { FunambulePlayer } from './games/funambule/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'rounds', label: 'Manches', min: 1, max: 6 }]);

export default { Settings, Host: FunambuleHost, Player: FunambulePlayer };

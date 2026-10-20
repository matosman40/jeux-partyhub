import { fieldSettings } from './games/client/settings.js';
import { GagsHost } from './games/gags-en-rafale/client/HostScreen.js';
import { GagsPlayer } from './games/gags-en-rafale/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'rounds', label: 'Gags', min: 1, max: 20 }]);

export default { Settings, Host: GagsHost, Player: GagsPlayer };

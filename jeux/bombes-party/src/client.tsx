import { fieldSettings } from './games/client/settings.js';
import { BombesPartyHost } from './games/bombes-party/client/HostScreen.js';
import { BombesPartyPlayer } from './games/bombes-party/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'rounds', label: 'Manches', min: 1, max: 5 }]);

export default { Settings, Host: BombesPartyHost, Player: BombesPartyPlayer };

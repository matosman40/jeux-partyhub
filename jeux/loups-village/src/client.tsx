import { fieldSettings } from './games/client/settings.js';
import { LoupsHostScreen } from './games/loups-village/client/HostScreen.js';
import { LoupsPlayerScreen } from './games/loups-village/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'debateSeconds', label: 'Secondes de débat', min: 30, max: 300 }]);

export default { Settings, Host: LoupsHostScreen, Player: LoupsPlayerScreen };

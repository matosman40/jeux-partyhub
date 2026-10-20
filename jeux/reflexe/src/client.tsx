import { fieldSettings } from './games/client/settings.js';
import { ReflexeHost } from './games/reflexe/client/HostScreen.js';
import { ReflexePlayer } from './games/reflexe/client/PlayerScreen.js';

const Settings = fieldSettings([{ key: 'rounds', label: 'Manches', min: 1, max: 15 }]);

export default { Settings, Host: ReflexeHost, Player: ReflexePlayer };

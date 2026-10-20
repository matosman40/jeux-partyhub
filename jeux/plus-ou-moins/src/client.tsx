import { fieldSettings } from './games/client/settings.js';
import { PlusOuMoinsHost } from './games/plus-ou-moins/client/HostScreen.js';
import { PlusOuMoinsPlayer } from './games/plus-ou-moins/client/PlayerScreen.js';

const Settings = fieldSettings([
        { key: 'rounds', label: 'Cartes', min: 1, max: 30 },
        { key: 'betSeconds', label: 'Secondes pour parier', min: 5, max: 60 },
      ]);

export default { Settings, Host: PlusOuMoinsHost, Player: PlusOuMoinsPlayer };

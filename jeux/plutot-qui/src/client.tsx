import { fieldSettings } from './games/client/settings.js';
import { PlutotQuiHost } from './games/plutot-qui/client/HostScreen.js';
import { PlutotQuiPlayer } from './games/plutot-qui/client/PlayerScreen.js';

const Settings = fieldSettings([
        { key: 'rounds', label: 'Questions', min: 1, max: 15 },
        { key: 'voteSeconds', label: 'Secondes pour voter', min: 10, max: 90 },
      ]);

export default { Settings, Host: PlutotQuiHost, Player: PlutotQuiPlayer };

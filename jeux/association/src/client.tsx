import { fieldSettings } from './games/client/settings.js';
import { AssociationHost } from './games/association/client/HostScreen.js';
import { AssociationPlayer } from './games/association/client/PlayerScreen.js';

const Settings = fieldSettings([
        { key: 'rounds', label: 'Manches', min: 1, max: 10 },
        { key: 'writeSeconds', label: 'Secondes pour écrire', min: 10, max: 120 },
      ]);

export default { Settings, Host: AssociationHost, Player: AssociationPlayer };

import { fieldSettings } from './games/client/settings.js';
import { KaraokeHost } from './games/karaoke/client/HostScreen.js';
import { KaraokePlayer } from './games/karaoke/client/PlayerScreen.js';

const Settings = fieldSettings([
        { key: 'segmentSeconds', label: 'Secondes par passage', min: 6, max: 12 },
        { key: 'pickSeconds', label: 'Secondes pour choisir', min: 20, max: 180 },
      ]);

export default { Settings, Host: KaraokeHost, Player: KaraokePlayer };

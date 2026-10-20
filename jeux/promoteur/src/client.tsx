import { fieldSettings } from './games/client/settings.js';
import { PromoteurHost } from './games/promoteur/client/HostScreen.js';
import { PromoteurPlayer } from './games/promoteur/client/PlayerScreen.js';

const Settings = fieldSettings([
        { key: 'rounds', label: 'Tours', min: 5, max: 60 },
        { key: 'turnSeconds', label: 'Secondes par tour (0 = libre)', min: 0, max: 120 },
      ]);

export default { Settings, Host: PromoteurHost, Player: PromoteurPlayer };

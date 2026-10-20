import { fieldSettings } from './games/client/settings.js';
import { TennisHost } from './games/tennis/client/HostScreen.js';
import { TennisPlayer } from './games/tennis/client/PlayerScreen.js';

const Settings = fieldSettings([
        {
          key: 'rules',
          label: 'Règles',
          options: [
            { value: 'vies', label: 'Simples : des vies' },
            { value: 'tennis', label: 'Vrai tennis : points, jeux, sets' },
          ],
        },
        {
          key: 'format',
          label: 'Forme de jeu',
          options: [
            { value: 'libre', label: 'Partie libre' },
            { value: 'poule', label: 'Championnat en poule' },
            { value: 'eliminatoire', label: 'Championnat à élimination' },
          ],
        },
        { key: 'lives', label: 'Vies par joueur (règles simples)', min: 1, max: 5 },
        {
          key: 'sets',
          label: 'Sets par match (vrai tennis)',
          options: [
            { value: '1', label: 'Un set' },
            { value: '3', label: 'Meilleur de trois sets' },
          ],
        },
      ]);

export default { Settings, Host: TennisHost, Player: TennisPlayer };

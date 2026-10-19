# Sons de PartyHub

Bruitages et musiques de fond partagés par les jeux.

Ce dossier est la source. Les paquets de format 4 reçoivent une copie dans `jeux/<jeu>/assets/sons/`, avec le bloc `sons`
de leur `game/definition.json` : `cartes-couleurs`, `cartes-coco`, `parcours-des-questions` et `poker`. Une modification ici
doit être recopiée dans chaque paquet. Le format et les règles sont dans la documentation de PartyHub (`docs/PHGAME.md` du dépôt PartyHub, section Sons, à partir de la version 0.14.0 :
https://github.com/matosman40/Partyhub/blob/main/docs/PHGAME.md).

Les sons `sfx-card` et `sfx-chip` sont provisoires : ils seront remplacés par des sons du pack casino (CC0) quand il sera
déposé.

## Contenu

| Fichier | Nom technique | Origine | Durée |
|---|---|---|---|
| `sfx/sfx-click.ogg` | click | Kenney Interface Sounds (click_001) | 0,11 s |
| `sfx/sfx-place.ogg` | place | Kenney Interface Sounds (drop_002) | 0,20 s |
| `sfx/sfx-hit.ogg` | hit | Kenney Interface Sounds (bong_001), approximatif | 0,13 s |
| `sfx/sfx-pickup.ogg` | pickup | Kenney Interface Sounds (confirmation_002), approximatif | 0,56 s |
| `sfx/sfx-turn.ogg` | turn | Kenney Interface Sounds (confirmation_004), approximatif | 0,50 s |
| `sfx/sfx-draw.ogg` | draw | Kenney Interface Sounds (scratch_001), approximatif | 0,16 s |
| `sfx/sfx-explode.ogg` | explode | synthèse | 1,5 s |
| `sfx/sfx-crate.ogg` | crate | synthèse | 0,9 s |
| `sfx/sfx-die.ogg` | die | synthèse | 1,2 s |
| `sfx/sfx-win.ogg` | win | synthèse | 2 s |
| `sfx/sfx-start.ogg` | start | synthèse | 1,5 s |
| `sfx/sfx-final.ogg` | final | synthèse | 3 s |
| `sfx/sfx-card.ogg` | card | synthèse, à remplacer par le pack casino quand il sera fourni | 0,4 s |
| `sfx/sfx-chip.ogg` | chip | synthèse, à remplacer par le pack casino quand il sera fourni | 0,9 s |
| `musique/musique-accueil.ogg` | accueil | synthèse, boucle de 30 s à 128 BPM | 30 s |
| `musique/musique-menus.ogg` | menus | synthèse, boucle de 60 s à 80 BPM | 60 s |
| `musique/musique-fin.ogg` | fin | synthèse, sans boucle | 15 s |

## Licences

- **Kenney Interface Sounds** : CC0 1.0, dépôt [Calinou/kenney-interface-sounds](https://github.com/Calinou/kenney-interface-sounds), fichier `LICENSE.txt`. Usage commercial libre. Créditer Kenney n'est pas obligatoire.
- **Sons synthétisés** : produits par `outils/synthese.py`, sans fichier source externe. Licence CC0 1.0 (domaine public), choisie le 19 octobre 2026 : usage libre, sans attribution obligatoire.

## Régénérer les sons synthétisés

Depuis la racine du dépôt :

```bash
python3 sons/outils/synthese.py
```

Il faut numpy et ffmpeg. La graine du générateur est fixe : le même script donne toujours les mêmes fichiers.

## Contrôles

Chaque fichier a été mesuré : durée, pic vers −3 dBFS, absence d'écrêtage, mono, nombre de coups, continuité des boucles. Ces contrôles ne remplacent pas une écoute : les sons restent à écouter en jeu, sur téléphone et sur TV.

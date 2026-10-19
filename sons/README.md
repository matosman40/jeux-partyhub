# Sons de PartyHub

Bruitages et musiques de fond partagés par les jeux.

**Ces fichiers ne font pas encore partie des paquets.** Le format de paquet n'admet que les dossiers `game`, `assets`, `data` et `licenses`, et le workflow `publier.yml` ne construit que `jeux/<jeu>/`. Les sons restent dans ce dossier, prêts à être intégrés quand le format saura les lire.

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
- **Sons synthétisés** : produits par `outils/synthese.py`, sans fichier source externe. La licence reste à décider avant publication : le dépôt n'en indique pas encore.

## Régénérer les sons synthétisés

Depuis la racine du dépôt :

```bash
python3 sons/outils/synthese.py
```

Il faut numpy et ffmpeg. La graine du générateur est fixe : le même script donne toujours les mêmes fichiers.

## Contrôles

Chaque fichier a été mesuré : durée, pic vers −3 dBFS, absence d'écrêtage, mono, nombre de coups, continuité des boucles. Ces contrôles ne remplacent pas une écoute : les sons restent à écouter en jeu, sur téléphone et sur TV.

# Vignettes des jeux

Chaque paquet a une vignette : `jeux/<jeu>/assets/cover.png`, 640 × 360, moins de 200 Ko. Elle sert de couverture
dans le magasin et dans les listes de jeux.

Deux façons de la changer, au choix :

1. **Par les réglages** : modifiez `<jeu>.json` (titre, sous-titre, couleurs, motif), puis lancez
   `python3 vignettes/generer.py <jeu>`. Motifs admis : `cartes`, `coco`, `parcours`, `table`.
2. **Par un prompt** : collez `<jeu>.prompt.txt` dans un générateur d'images, puis déposez le résultat à la place de
   `jeux/<jeu>/assets/cover.png` (PNG, 640 × 360, moins de 200 Ko). Le prompt demande une image sans texte : le titre
   reste celui du manifeste.

Dépendances : Pillow (`pip install pillow`) et la police DejaVu Sans. Sous Debian ou Ubuntu : `sudo apt install fonts-dejavu-core`.
Le script cherche la police dans les emplacements usuels de Linux, macOS et Windows, et s'arrête avec un message si elle manque.
Sous Linux avec DejaVu Sans, la vignette régénérée est identique octet pour octet à celle du dépôt.

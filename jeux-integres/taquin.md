# 🔀 Taquin

Solo · 1 à 8 joueurs · environ 10 min

Remettez les tuiles dans l’ordre en les faisant glisser vers la case vide.

## But

Remettre les tuiles dans l’ordre, de 1 à la dernière, la case vide en bas à droite.

## Déroulement

1. Touchez une tuile voisine de la case vide : elle glisse dans le vide.
2. Répétez pour réordonner les tuiles.
3. Le classement suit le nombre de secondes pour résoudre la grille.

## Conseils

- Commencez par la première ligne, puis la deuxième, et ainsi de suite.
- Le mélange est toujours soluble.

## Version

- Version du jeu : 1.0.0
- Identifiant : `taquin`
- Code source : `packages/games/src/solo/games.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Ajouté) : Identité visuelle complète du catalogue : chaque jeu listé a son propre logo et son décor. Huit jeux n'en avaient pas (Couleurs & chiffres, Blanc-manger coco, Sudoku, Solitaire, Taquin, Mots croisés, Imite-moi, BOUM !) ; ils recevaient un décor emprunté à un autre jeu, choisi au hasard.
- 0.12.0, 2026-10-18 (Modifié) : Icônes : Couleurs & chiffres (🌈) et Taquin (🔀) ne partagent plus leur icône avec un autre jeu.
- 0.12.0, 2026-10-18 (Corrigé) : Accessibilité des vues de jeu : Sudoku, Taquin et Mots croisés déclaraient une grille (`role="grid"`) sans les cellules ni la navigation attendues ; ce sont désormais des groupes nommés. Solitaire annonce la carte cachée comme une image. Tarot : la main est accessible au clavier et le pli en cours est nommé. Poker, Rami 51, Président, Cartes, Promoteur, Plateau, Phrases à trous et Aventure : éléments nommés sans rôle, désormais annoncés comme images, groupes ou jauges. Administration (webcam, niveaux des appareils) et écran des appareils corrigés de la même façon.
- 0.1.0, 2026-10-14 (Ajouté) : Jeux fournis : Quiz Party, Association express, Plutôt qui ?, L'Imposteur, Plus ou moins, Réflexe, Bombes party, Cartes couleurs, Cartes coco, Président, Promoteur, Loups du village, Sudoku, Solitaire, Taquin, Mots croisés.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

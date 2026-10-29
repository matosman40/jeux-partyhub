# 🂡 Solitaire

Solo · 1 à 8 joueurs · environ 12 min

Classez toutes les cartes par couleur, de l’As au Roi, en construisant les colonnes.

## But

Placer les 52 cartes sur les quatre fondations.

## Déroulement

1. Piochez une carte pour la mettre dans la défausse.
2. Touchez une carte, puis touchez son emplacement : une colonne ou une fondation.
3. Les colonnes se construisent en ordre décroissant et en alternant rouge et noir.
4. Les fondations se remplissent de l’As au Roi, par couleur.

## Conseils

- Retournez les cartes cachées des colonnes pour avancer.
- Un roi peut occuper une colonne vide.

## Version

- Version du jeu : 1.0.1
- Identifiant : `solitaire`
- Code source : `packages/games/src/solo/games.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Ajouté) : Identité visuelle complète du catalogue : chaque jeu listé a son propre logo et son décor. Huit jeux n'en avaient pas (Couleurs & chiffres, Blanc-manger coco, Sudoku, Solitaire, Taquin, Mots croisés, Imite-moi, BOUM !) ; ils recevaient un décor emprunté à un autre jeu, choisi au hasard.
- 0.12.0, 2026-10-18 (Corrigé) : Accessibilité des vues de jeu : Sudoku, Taquin et Mots croisés déclaraient une grille (`role="grid"`) sans les cellules ni la navigation attendues ; ce sont désormais des groupes nommés. Solitaire annonce la carte cachée comme une image. Tarot : la main est accessible au clavier et le pli en cours est nommé. Poker, Rami 51, Président, Cartes, Promoteur, Plateau, Phrases à trous et Aventure : éléments nommés sans rôle, désormais annoncés comme images, groupes ou jauges. Administration (webcam, niveaux des appareils) et écran des appareils corrigés de la même façon.
- 0.1.0, 2026-10-14 (Ajouté) : Jeux fournis : Quiz Party, Association express, Plutôt qui ?, L'Imposteur, Plus ou moins, Réflexe, Bombes party, Cartes couleurs, Cartes coco, Président, Promoteur, Loups du village, Sudoku, Solitaire, Taquin, Mots croisés.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

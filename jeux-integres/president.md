# 👑 Président

Cartes · 3 à 6 joueurs · environ 20 min

Le classique des soirées : montez en grade, de Trou du cul à Président.

## But

Être le premier à vider sa main, et devenir Président de la partie.

## Déroulement

1. Les cartes sont réparties entre tous les joueurs.
2. À votre tour, posez une ou plusieurs cartes de même rang, plus fortes que le pli en cours.
3. Le 2 est la carte la plus forte, le 3 la plus faible.
4. Un 10 ou un carré (quatre cartes identiques) brûle le pli : il est retiré et vous rejouez.
5. Si vous ne pouvez pas jouer, passez. Quand tous les autres ont passé, le pli se termine.
6. Chaque manche, le Trou du cul donne ses deux meilleures cartes au Président, qui lui rend ses deux plus faibles.

## Conseils

- Gardez un 2 pour finir un pli au bon moment.
- Un carré ou un 10 est votre meilleure arme pour reprendre la main.

## Version

- Version du jeu : 1.0.2
- Identifiant : `president`
- Code source : `packages/games/src/president/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Corrigé) : Accessibilité des vues de jeu : Sudoku, Taquin et Mots croisés déclaraient une grille (`role="grid"`) sans les cellules ni la navigation attendues ; ce sont désormais des groupes nommés. Solitaire annonce la carte cachée comme une image. Tarot : la main est accessible au clavier et le pli en cours est nommé. Poker, Rami 51, Président, Cartes, Promoteur, Plateau, Phrases à trous et Aventure : éléments nommés sans rôle, désormais annoncés comme images, groupes ou jauges. Administration (webcam, niveaux des appareils) et écran des appareils corrigés de la même façon.
- 0.10.0, 2026-10-16 (Modifié) : Main triée par grandeur : dans le Président, « Couleurs & chiffres » et les jeux de cartes créés dans l’administration, les cartes vont du plus petit au plus grand, les actions et les jokers à la suite. Le Rami et le Tarot gardaient déjà leur tri.
- 0.1.0, 2026-10-14 (Ajouté) : Jeux fournis : Quiz Party, Association express, Plutôt qui ?, L'Imposteur, Plus ou moins, Réflexe, Bombes party, Cartes couleurs, Cartes coco, Président, Promoteur, Loups du village, Sudoku, Solitaire, Taquin, Mots croisés.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

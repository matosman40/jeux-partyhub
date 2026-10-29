# ♦️ Rami 51

Cartes · 2 à 5 joueurs · environ 40 min

Le rami à la française : ouvrez à 51 avec une tierce franche, posez tout, et gardez le plus petit total.

## But

Se débarrasser de toutes ses cartes en posant des combinaisons, et finir la partie avec le moins de points de pénalité.

## Déroulement

1. Deux jeux de 52 cartes et 4 jokers. Chacun reçoit 13 cartes ; la première carte de la pioche lance la défausse.
2. À votre tour : piochez (pioche ou dessus de la défausse), posez si vous le pouvez, puis défaussez une carte pour finir le tour.
3. Combinaisons : brelan ou carré (même valeur, couleurs différentes) et suite d’au moins 3 cartes de la même couleur. L’as se place avant le 2 ou après le roi, sans faire le tour (R-A-2 interdit).
4. Joker : un seul par combinaison, avec au moins deux vraies cartes. Il remplace une carte précise : il comble le trou d’une suite, sinon il la prolonge vers le haut (vers le bas après un as).
5. Pour ouvrir, posez en une fois des combinaisons d’au moins 51 points (réglable), dont une tierce franche : une suite d’au moins 3 cartes sans joker. Avant d’ouvrir, on pioche et on défausse seulement.
6. Une fois ouvert, posez d’autres combinaisons, complétez celles de la table (les vôtres comme celles des autres) et échangez un joker contre la carte exacte qu’il remplace.
7. Une carte prise dans la défausse, comme un joker récupéré, doit être posée sur la table pendant le même tour.
8. On ne pose jamais sa dernière carte : on la défausse. La manche se termine quand un joueur défausse sa dernière carte.
9. Les autres comptent leurs cartes en main : joker 20, as 11, figures 10, les autres leur valeur. Rami sec (ouvrir et finir dans le même tour) : pénalités doublées.
10. La partie s’arrête quand un total atteint 500 points (réglable) : le plus petit total gagne.

## Conseils

- Valeurs pour ouvrir : as 11 (mais 1 dans A-2-3), figures 10, les autres leur valeur ; un joker vaut la carte qu’il remplace.
- « Annuler mon tour » reprend les cartes posées depuis la pioche. Si vous avez pris la défausse sans rien poser, la carte y retourne.
- Quand la pioche est vide, la défausse (sauf sa carte du dessus) est mélangée pour la remplacer.
- Temps écoulé : le joueur pioche puis défausse automatiquement sa carte la plus forte (hors joker).
- Un joker posé par un autre joueur peut débloquer votre fin de manche : guettez la carte qu’il remplace.

## Version

- Version du jeu : 1.0.2
- Identifiant : `rami-51`
- Code source : `packages/games/src/rami51/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Corrigé) : Accessibilité des vues de jeu : Sudoku, Taquin et Mots croisés déclaraient une grille (`role="grid"`) sans les cellules ni la navigation attendues ; ce sont désormais des groupes nommés. Solitaire annonce la carte cachée comme une image. Tarot : la main est accessible au clavier et le pli en cours est nommé. Poker, Rami 51, Président, Cartes, Promoteur, Plateau, Phrases à trous et Aventure : éléments nommés sans rôle, désormais annoncés comme images, groupes ou jauges. Administration (webcam, niveaux des appareils) et écran des appareils corrigés de la même façon.
- 0.4.0, 2026-10-14 (Ajouté) : Trois jeux de cartes, disponibles dans le catalogue : - **Poker (Texas hold’em)** de 2 à 8 joueurs : blindes, mises, tapis, pots secondaires, croupier, 25 s par action. - **Rami 51** de 2 à 5 joueurs (avec le jeu de 108 cartes) : ouverture à 51 points, tierce franche, échange de joker, rami sec. - **Tarot à 4 joueurs** : enchères, chien, écart, obligations de couleur et d'atout, Excuse, petit au bout, chelem.
- 0.4.0, 2026-10-14 (Ajouté) : Tests serveur : 260 au total, dont 10 pour le tarot, 37 pour Rami 51 et 16 pour le poker.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

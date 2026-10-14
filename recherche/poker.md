# Brief de recherche : poker (Texas Hold'em)

Date d'accès : 2026-10-14

## Nom
- Nom trouvé : poker (Texas Hold'em). Mot générique, pas une marque.
- Nom retenu : poker.

## Joueurs, but, mise en place
- Joueurs : 2 à 9 (source 1 indique 2 à 10 ; écart noté, la valeur la plus restrictive est retenue pour le paquet).
- But : gagner les jetons des autres joueurs, ou remporter le pot principal.
- Mise en place : un bouton de donneur qui se déplace à chaque main. Deux mises forcées (petite et grosse blinde). Chaque joueur reçoit 2 cartes privées.

## Déroulement (reformulé)
1. Pré-flop : premier tour d'enchères, en commençant à gauche de la grosse blinde. Chacun peut se coucher, suivre, relancer.
2. Flop : 3 cartes communes face visible, puis tour d'enchères.
3. Turn : 1 carte commune, puis tour d'enchères.
4. River : 1 carte commune, puis dernier tour d'enchères.
5. Abattage : si au moins deux joueurs restent, ils dévoilent leurs cartes. Chacun forme sa meilleure main de 5 cartes à partir de ses 2 cartes privées et des 5 cartes communes.
6. Classement des mains, du plus fort au plus faible : quinte flush royale, quinte flush, carré, full, couleur, quinte, brelan, deux paires, paire, carte haute.

## Fin et victoire
- Si tous sauf un se couchent à n'importe quel moment, le dernier gagne le pot sans abattage.
- Sinon, la meilleure main remporte le pot. Les égalités se partagent.

## Variantes (séparées des règles principales)
- Limit, pot-limit, no-limit : tailles de mise différentes. Non retenu.
- Tournois, élimination : non retenu.

## Mécanismes principaux et type de paquet
- Pioche, main, combinaisons : correspond au type `cards`.
- Mises, tours d'enchères, jetons : ne tient pas dans `cards`, `board` ou `quiz` en version fidèle. Mécanisme simplifié à noter si la variante simplifiée est retenue (paramètre « Accepter une variante simplifiée » = oui par défaut).

## Éléments introuvables
- Aucun élément bloquant. Règles de mise exactes (limite de relance) non précisées, car la variante retenue les écarte.

## Sources
1. Règles du Texas Hold'em, regles-du-jeu.net : https://www.regles-du-jeu.net/regles-du-poker/ (consulté le 2026-10-14)
2. Texas Hold'em rules, CardPlayer : https://www.cardplayer.com/rules-of-poker/how-to-play-poker/games/texas-holdem (consulté le 2026-10-14)
3. Recherches de référence (non lues) : cours-et-fiches.com, senego.com (résultats de recherche « règles du jeu Texas hold'em »).

Concordance : le déroulement, les blindes, les 4 tours d'enchères et la hiérarchie des mains concordent entre les sources 1 et 2.

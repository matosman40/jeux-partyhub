# 🎴 Tarot

Cartes · 4 joueurs · environ 30 min

Le tarot à quatre : enchères, chien, écart et plis, un preneur contre trois défenseurs.

## But

À quatre : un preneur joue seul contre les trois autres et doit réunir assez de points dans ses plis pour remplir son contrat. Le meilleur total après la dernière donne gagne.

## Déroulement

1. Chacun reçoit 18 cartes, 6 forment le chien. Le donneur change à chaque donne. Si votre seul atout est le Petit (Excuse ou non), c’est le Petit sec : la donne est annulée et refaite.
2. Enchères en un seul tour, à partir du joueur après le donneur : passez ou annoncez plus haut que l’enchère précédente. Petite (×1), Garde (×2), Garde sans le chien (×4), Garde contre le chien (×6).
3. Si tout le monde passe, les cartes sont redistribuées par le donneur suivant. Sinon, la plus haute enchère désigne le preneur ; les trois autres forment la défense.
4. Petite ou Garde : le chien est montré, le preneur le prend et écarte 6 cartes (ni roi ni oudler ; sans autre choix, des atouts, montrés). L’écart compte pour le preneur.
5. Garde sans le chien : personne ne le voit, il compte pour le preneur. Garde contre le chien : personne ne le voit, il compte pour la défense.
6. Le joueur après le donneur entame. Fournissez la couleur demandée ; sinon coupez, en surcoupant si possible ; sans atout, jouez ce que vous voulez. Sur un atout, montez si vous le pouvez.
7. L’Excuse se joue à tout moment et ne gagne jamais le pli : elle reste à son camp, qui cède un demi-point si l’autre camp gagne le pli. Jouée au dernier pli, elle va au camp qui le remporte.
8. Points à faire selon les oudlers (le Petit, le 21, l’Excuse) gagnés par le preneur : 56 sans oudler, 51 avec un, 41 avec deux, 36 avec trois.
9. Marque : 25 + l’écart avec les points à faire (arrondi au-dessus), fois le multiplicateur. Petit au bout (le Petit dans le dernier pli) : 10 fois le multiplicateur pour le camp qui remporte ce pli.
10. Chelem non annoncé : 200 points pour le camp qui remporte les 18 plis.
11. Le preneur marque trois fois ce résultat, chaque défenseur le perd une fois : le total des scores reste nul.

## Conseils

- Variantes retenues : enchères en un seul tour, Petit sec annulé même avec l’Excuse (le même donneur redistribue), écart et chien comptés comme indiqué ci-dessus.
- Non prévus : poignées, chelem annoncé et misère.
- Une donne annulée (Petit sec ou tout le monde passe) ne compte pas dans le nombre de donnes.
- Temps écoulé : on passe pendant les enchères, l’écart prend les cartes les plus faibles, et la plus petite carte permise est jouée. L’écart dispose d’un temps double.
- Les cartes jouables s’éclairent sur votre téléphone : touchez-en une pour la jouer.

## Version

- Version du jeu : 1.0.2
- Identifiant : `tarot`
- Code source : `packages/games/src/tarot/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Modifié) : Aventure IA : description raccourcie pour tenir sur une carte du catalogue. Tarot : une étape de la notice raccourcie, sans changer la règle.
- 0.12.0, 2026-10-18 (Corrigé) : Accessibilité des vues de jeu : Sudoku, Taquin et Mots croisés déclaraient une grille (`role="grid"`) sans les cellules ni la navigation attendues ; ce sont désormais des groupes nommés. Solitaire annonce la carte cachée comme une image. Tarot : la main est accessible au clavier et le pli en cours est nommé. Poker, Rami 51, Président, Cartes, Promoteur, Plateau, Phrases à trous et Aventure : éléments nommés sans rôle, désormais annoncés comme images, groupes ou jauges. Administration (webcam, niveaux des appareils) et écran des appareils corrigés de la même façon.
- 0.10.0, 2026-10-16 (Ajouté) : Modèles prêts à l’emploi, dans « Partir de » : jeu de 52 cartes (quatre couleurs), tarot (78 cartes), jetons de mise, mémo des animaux, mémo des capitales (paires texte).
- 0.10.0, 2026-10-16 (Modifié) : Main triée par grandeur : dans le Président, « Couleurs & chiffres » et les jeux de cartes créés dans l’administration, les cartes vont du plus petit au plus grand, les actions et les jokers à la suite. Le Rami et le Tarot gardaient déjà leur tri.
- 0.4.0, 2026-10-14 (Ajouté) : Trois jeux de cartes, disponibles dans le catalogue : - **Poker (Texas hold’em)** de 2 à 8 joueurs : blindes, mises, tapis, pots secondaires, croupier, 25 s par action. - **Rami 51** de 2 à 5 joueurs (avec le jeu de 108 cartes) : ouverture à 51 points, tierce franche, échange de joker, rami sec. - **Tarot à 4 joueurs** : enchères, chien, écart, obligations de couleur et d'atout, Excuse, petit au bout, chelem.
- 0.4.0, 2026-10-14 (Ajouté) : Tests serveur : 260 au total, dont 10 pour le tarot, 37 pour Rami 51 et 16 pour le poker.
- 0.4.0, 2026-10-14 (Problèmes connus) : Tarot : une partie demande 4 joueurs ; la salle d'entraînement ne fournit que 3 robots, il faut donc un téléphone.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

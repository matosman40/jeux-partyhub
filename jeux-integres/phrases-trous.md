# 🧩 Phrases à trous

Quiz · 2 à 8 joueurs · environ 12 min · utilise une IA générative si elle est configurée

Remplissez le trou de la phrase avec la carte la plus drôle ou la plus juste, puis votez pour la meilleure. Les mots-clés de chacun servent de thème.

## But

Compléter chaque phrase avec la carte la plus drôle ou la plus juste, puis gagner les votes du public.

## Déroulement

1. Chacun propose à son tour quelques mots-clés : l’IA écrit les phrases à partir de ces thèmes.
2. À chaque tour, posez une carte de votre main dans le trou de la phrase.
3. Votez pour la phrase la plus drôle, sans savoir qui l’a écrite : chaque vote rapporte 100 points à son auteur.
4. Une carte qui complète juste le trou rapporte 50 points de plus.
5. Après le dernier tour, le joueur qui a le plus de points gagne.

## Conseils

- Vous ne pouvez pas voter pour votre propre phrase.
- Sans IA configurée, le jeu reprend ses phrases intégrées et le dit à l’écran.
- Le nombre de tours, la taille de la main et les temps se règlent dans le salon.

## Version

- Version du jeu : 1.0.0
- Identifiant : `phrases-trous`
- Code source : `packages/games/src/phrases-trous/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Ajouté) : Drapeau « IA » dans le manifeste des jeux (Quiz Party, Phrases à trous, Aventure IA), qui alimente le filtre « Avec IA ».
- 0.12.0, 2026-10-18 (Ajouté) : Phrases à trous : nouveau jeu de la catégorie Quiz. L’IA écrit des phrases à trou à partir des mots-clés de chaque joueur. À chaque tour, chacun pose une carte de sa main dans le trou, puis tout le monde vote anonymement (100 points par vote reçu, 50 de plus pour la carte qui complète juste le trou). De 3 à 8 tours, puis un vainqueur. Sans IA configurée, les phrases intégrées prennent le relais, avec un message à l’écran.
- 0.12.0, 2026-10-18 (Modifié) : Réglages de Quiz Party et des Phrases à trous : un champ numérique vidé est ramené à sa borne minimale à la perte de focus, au lieu d’envoyer 0 au serveur.
- 0.12.0, 2026-10-18 (Corrigé) : Accessibilité des vues de jeu : Sudoku, Taquin et Mots croisés déclaraient une grille (`role="grid"`) sans les cellules ni la navigation attendues ; ce sont désormais des groupes nommés. Solitaire annonce la carte cachée comme une image. Tarot : la main est accessible au clavier et le pli en cours est nommé. Poker, Rami 51, Président, Cartes, Promoteur, Plateau, Phrases à trous et Aventure : éléments nommés sans rôle, désormais annoncés comme images, groupes ou jauges. Administration (webcam, niveaux des appareils) et écran des appareils corrigés de la même façon.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

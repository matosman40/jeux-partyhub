# 🧠 Quiz Party

Quiz · 1 à 12 joueurs · environ 10 min · utilise une IA générative si elle est configurée

Questions à choix multiples, points et bonus de rapidité. Peut aussi partir des mots-clés de chaque joueur : l’IA écrit alors les questions.

## But

Répondre le plus vite et le plus juste aux questions pour marquer le plus de points.

## Déroulement

1. L’hôte lance la partie depuis l’écran principal.
2. Avec les thèmes des joueurs, chacun propose à son tour quelques mots-clés sur son téléphone.
3. Chaque question s’affiche sur l’écran et sur votre téléphone.
4. Touchez la bonne réponse avant la fin du temps.
5. Les points arrivent après la révélation : répondre vite rapporte un bonus.

## Conseils

- Une mauvaise réponse ne retire aucun point.
- Le nombre de questions, le temps et la source des questions se règlent dans le salon, avant le lancement.
- Sans IA configurée, le jeu reprend ses questions intégrées et le dit à l’écran.

## Version

- Version du jeu : 1.1.2
- Identifiant : `quiz-party`
- Code source : `packages/games/src/quiz-party/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Ajouté) : Drapeau « IA » dans le manifeste des jeux (Quiz Party, Phrases à trous, Aventure IA), qui alimente le filtre « Avec IA ».
- 0.12.0, 2026-10-18 (Ajouté) : Quiz Party, source « Thèmes des joueurs (IA) » : chaque joueur donne quelques mots-clés à tour de rôle, et l’IA écrit les questions à partir de ces thèmes. Sans IA configurée, ou si sa réponse est inutilisable, les questions intégrées prennent le relais, avec un message à l’écran.
- 0.12.0, 2026-10-18 (Modifié) : Réglages de Quiz Party et des Phrases à trous : un champ numérique vidé est ramené à sa borne minimale à la perte de focus, au lieu d’envoyer 0 au serveur.
- 0.1.0, 2026-10-14 (Ajouté) : Jeux fournis : Quiz Party, Association express, Plutôt qui ?, L'Imposteur, Plus ou moins, Réflexe, Bombes party, Cartes couleurs, Cartes coco, Président, Promoteur, Loups du village, Sudoku, Solitaire, Taquin, Mots croisés.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

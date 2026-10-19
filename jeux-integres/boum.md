# 💥 BOUM !

Quiz · 2 à 12 joueurs · environ 12 min

Des manches tirées au hasard : écrivez, votez, bluffez. Chaque manche change de mode.

## But

Gagnez le plus de points sur cinq manches tirées au hasard.

## Déroulement

1. L’écran principal annonce le mode de la manche.
2. Sur votre téléphone, écrivez, jouez une carte, estimez ou votez selon la consigne.
3. Les points tombent à la révélation : chaque vote reçu rapporte des points à son auteur.
4. Le classement final désigne le vainqueur.

## Conseils

- Le pack Humour noir contient des contenus plus osés : activez-le en connaissance de cause.
- Un mode sans assez de contenu validé n’est jamais tiré : la partie continue avec les autres.

## Version

- Version du jeu : 1.0.0
- Identifiant : `boum`
- Code source : `packages/games/src/boum/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Ajouté) : Identité visuelle complète du catalogue : chaque jeu listé a son propre logo et son décor. Huit jeux n'en avaient pas (Couleurs & chiffres, Blanc-manger coco, Sudoku, Solitaire, Taquin, Mots croisés, Imite-moi, BOUM !) ; ils recevaient un décor emprunté à un autre jeu, choisi au hasard.
- 0.9.0, 2026-10-15 (Ajouté) : BOUM ! (catégorie quiz, 2 à 12 joueurs, branche `boum`, en cours) : manches tirées au hasard dans un pool de modes. Phase 1 : Réponse rapide, Combien ?, Trous noirs, Main sale, Vrai ou faux, Qui a dit ça ?, Épitaphe, Le pire conseil, Le plus probable et Détecteur de mauvaise foi, avec le pack Humour noir activable par salle. Banques de contenu en base (amorce de 340 entrées à valider), import et export `.txt` avec aperçu, et routes d’administration `/api/admin/boum/*`. L’onglet d’administration « Banques BOUM ! », la file des propositions et « Proposer une carte » dans le profil (quotas inclus) sont livrés. Le mode Mime le métier est livré (le métier n’est visible que du mimeur). Le mode Où est-ce ? est livré (carte du monde, barème par distance). Le mode Devine la chanson est livré (extrait chanté sur le téléphone du chanteur). Le mode Le mot secret est livré (indices d’un seul mot, visibles sur l’écran principal). Le mode Photo-défi est livré (photos à la consigne, vote anonyme sur les photos). Le mode Grimace est livré (photo notée de 1 à 5 étoiles). Le mode Galerie du thème est livré (même mécanique que Photo-défi, sur le thème tiré de la banque). Le mode Rythme est livré (reproduire un rythme en tapant ; sans banque, il reste tirable même sans contenu validé). Les autres modes photo, son et téléphone, les formats, les super-pouvoirs et les effets de l’écran principal ne sont pas encore livrés.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

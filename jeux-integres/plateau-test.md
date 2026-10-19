# 🧭 Plateau de test

Ambiance · 1 à 12 joueurs · environ 5 min

Déplacez votre personnage sur le plateau et envoyez une émotion à toute la salle.

> Outil d’administration : ce jeu ne figure pas au catalogue des joueurs.

## But

Essayer les déplacements et les émotions du plateau, avant une vraie partie.

## Déroulement

1. Glissez votre personnage sur le plateau, touchez un endroit libre, ou utilisez les flèches du clavier.
2. Envoyez une émotion : elle s’affiche au-dessus de votre personnage, sur l’écran et sur les téléphones.

## Conseils

- Rien n’est enregistré : les positions disparaissent avec la salle.

## Version

- Version du jeu : 1.0.0
- Identifiant : `plateau-test`
- Code source : `packages/games/src/plateau-test/module.ts` (dépôt PartyHub)

## Journal

- 0.10.0, 2026-10-16 (Modifié) : Salon de l’écran hôte (TV, ordinateur, tablette) : les joueurs s’affichent comme sur le téléphone, avec leur tête et leur pseudo. La prairie ne reste que pour le plateau de test.
- 0.9.2, 2026-10-16 (Modifié) : Salon sur téléphone, pour tous les jeux : chaque joueur est représenté par sa tête, son pseudo et ses étiquettes (vous, prêt, robot), sans plateau à déplacer. Le plateau reste réservé au plateau de test.
- 0.9.2, 2026-10-16 (Modifié) : Le bouton « Essayer le plateau » de l'accueil est retiré : le plateau de test n'est pas encore proposé au public.
- 0.9.0, 2026-10-15 (Ajouté) : Plateau de test : un bouton « Essayer le plateau » sur l’accueil ouvre une salle sans partie. Chacun y déplace son personnage (glissé, tap sur un endroit libre, ou flèches) et envoie une émotion, visible sur l’écran principal et les téléphones. Le salon est désormais ce même plateau, avec un décor de prairie, une profondeur (les personnages du bas sont un peu plus grands) et des pas animés. Le composant `Plateau` est partagé dans `@partyhub/games/client`, prêt pour les futurs jeux (`docs/ADDING-A-GAME.md`).

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

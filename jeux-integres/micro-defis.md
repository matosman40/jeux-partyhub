# 🎮 Micro-Défis

Ambiance · 1 à 12 joueurs · environ 8 min

Des défis éclair à la manette : secouez, penchez, tournez, soufflez, tapotez !

## But

Réussir le plus de défis, et le plus vite possible.

## Déroulement

1. Chaque défi est présenté sur l’écran principal, puis joué en même temps par tout le monde.
2. Le téléphone est la manette : secouez-le, gardez-le à plat, faites-le tourner, soufflez dans le micro ou tapotez.
3. Un défi réussi rapporte 100 points, plus jusqu’à 60 points pour la rapidité.
4. Quand tout le monde a joué, ou quand le temps est écoulé, le bilan s’affiche, puis le défi suivant.

## Conseils

- Le micro et le mouvement demandent HTTPS sur le réseau local (voir la page « Test des appareils »).
- Un téléphone sans capteur peut toujours jouer les défis « Tapote vite » et « Pile au bon moment ».
- Le téléphone doit être tenu comme au départ : la pose de départ sert de référence.

## Version

- Version du jeu : 1.0.0
- Identifiant : `micro-defis`
- Code source : `packages/games/src/micro-defis/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Modifié) : Catalogue : la catégorie « Plateau » s’intitule désormais « Ambiance » (Réflexe, Gags en rafale, Micro-défis, Funambule, Bombes party…). Son identifiant interne ne change pas.
- 0.11.0, 2026-10-17 (Ajouté) : Micro-Défis : une succession de défis éclair, les mêmes pour tout le monde. Secouer, garder le téléphone à plat, le faire tourner, souffler dans le micro, tapoter, appuyer au bon moment. De 1 à 12 défis par partie ; un défi réussi rapporte 100 points, plus jusqu’à 60 pour la rapidité.
- 0.11.0, 2026-10-17 (Modifié) : Lisibilité sur les TV et les téléphones : les textes des écrans Micro-Défis et Funambule, le classement, la barre de contrôle de la TV et l’étiquette « Salle » ne descendent plus sous 14 px. Les cases à cocher font 24 px sur écran tactile, et toute la ligne (libellé compris) est une cible d’au moins 44 px.
- 0.11.0, 2026-10-17 (Corrigé) : Funambule et Micro-Défis sur la TV : le contenu était collé à gauche de l’écran. Il est centré, et chaque jeu a son propre décor (un chapiteau au crépuscule pour Funambule, une borne d’arcade pour Micro-Défis) au lieu d’un décor générique.
- 0.11.0, 2026-10-17 (Corrigé) : Micro-Défis, « Souffle » : le trait qui marque le seuil était invisible sur le téléphone. Les défis occupent aussi l’écran du téléphone, centrés.
- 0.11.0, 2026-10-17 (Corrigé) : Micro-Défis, « Plateau tournant » : un aller-retour ne compte plus comme un tour, il faut faire 360 degrés dans un sens (ou dans l’autre). Un téléphone qui ne donne pas son cap est signalé, au lieu de laisser le défi bloqué.
- 0.11.0, 2026-10-17 (Corrigé) : Micro-Défis, « Secoue ! » : sur certains Android, qui donnent des mesures d’accélération vides, aucune secousse n’était comptée. La mesure de repli prend le relais.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

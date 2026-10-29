# 🤸 Funambule

Ambiance · 1 à 12 joueurs · environ 5 min

Tenez votre funambule sur le fil : penchez le téléphone pour contrer le vent.

## But

Traverser le fil le plus longtemps possible, sous un vent qui se renforce.

## Déroulement

1. Chaque manche, tous les funambules s’élancent en même temps sur l’écran principal.
2. Le vent pousse les personnages. Penchez le téléphone du côté opposé pour rester droit.
3. Quand le personnage penche trop longtemps, il tombe. Celui qui tient douze secondes traverse et gagne une prime.
4. Le bilan s’affiche après chaque manche, puis la manche suivante commence.

## Conseils

- Le mouvement demande HTTPS sur le réseau local (voir la page « Test des appareils »).
- Tenez le téléphone comme au départ : la pose de départ sert de référence. « Recentrer » la reprend.
- Un téléphone sans capteur ne peut pas jouer : le personnage reste alors sur le fil sans être compté.

## Version

- Version du jeu : 1.0.2
- Identifiant : `funambule`
- Code source : `packages/games/src/funambule/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Modifié) : Catalogue : la catégorie « Plateau » s’intitule désormais « Ambiance » (Réflexe, Gags en rafale, Micro-défis, Funambule, Bombes party…). Son identifiant interne ne change pas.
- 0.11.0, 2026-10-17 (Ajouté) : Funambule : chaque joueur tient son funambule sur le fil en penchant son téléphone contre le vent, qui se renforce d’une manche à l’autre (de 1 à 6 manches). Tout le monde marche en même temps, et l’écran principal montre les funambules en direct. Un funambule qui tombe garde le temps tenu ; celui qui traverse les douze secondes reçoit une prime.
- 0.11.0, 2026-10-17 (Modifié) : Lisibilité sur les TV et les téléphones : les textes des écrans Micro-Défis et Funambule, le classement, la barre de contrôle de la TV et l’étiquette « Salle » ne descendent plus sous 14 px. Les cases à cocher font 24 px sur écran tactile, et toute la ligne (libellé compris) est une cible d’au moins 44 px.
- 0.11.0, 2026-10-17 (Modifié) : Téléphones, contrôles en premier : le pad d’un défi (tapotement, « Stop ! ») occupe la moitié de l’écran et son libellé est grand ; le fil du funambule est plus haut ; « Recentrer » et les boutons d’autorisation font une cible pleine largeur de 52 px ; les choix du vote et de l’Aventure, les actions de combat et « Ma fiche » sont des blocs plus hauts. Hors des jeux, les boutons font au moins 50 px sur téléphone (44 px pour les petits boutons).
- 0.11.0, 2026-10-17 (Modifié) : Réactivité des jeux : les capteurs du téléphone partent au plus trente fois par seconde (une dizaine auparavant) et l’écran principal les affiche à l’image suivante. Un capteur met environ 10 ms à s’afficher sur la TV, contre 50 ms auparavant, et le mouvement du funambule sur le téléphone suit le capteur au lieu de se mettre à jour dix fois par seconde. Les barres de temps, les rubans du vent et les jauges du micro sont mis à l’échelle au lieu de changer de largeur, pour ne plus recalculer la mise en page à chaque image. Les personnages ne se redessinent que lorsque leur propre mesure change.
- 0.11.0, 2026-10-17 (Corrigé) : Funambule et Micro-Défis sur la TV : le contenu était collé à gauche de l’écran. Il est centré, et chaque jeu a son propre décor (un chapiteau au crépuscule pour Funambule, une borne d’arcade pour Micro-Défis) au lieu d’un décor générique.
- 0.11.0, 2026-10-17 (Corrigé) : Funambule : une traversée se termine à sa durée même si le téléphone cesse d’envoyer ses mesures (écran éteint, onglet caché).

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

# Code des jeux de PartyHub

Copie du code des 28 jeux intégrés à PartyHub, prise sur `main` de [matosman40/Partyhub](https://github.com/matosman40/Partyhub) au commit `33cf929` (version 0.14.0). Les chemins sont ceux du dépôt Partyhub : pour remettre un fichier à sa place, il suffit de copier le dossier à la racine du dépôt.

**Source de vérité : le dépôt Partyhub.** Cette copie ne se met pas à jour toute seule. Ne modifiez pas ce code ici sans le reporter dans Partyhub.

**Ce code n'est pas installable seul.** Il dépend du moteur de PartyHub (`packages/shared`) et de l'interface de l'application (`packages/web`). L'installation d'un jeu un par un dépend du format de code, qui n'existe pas encore.

## Fichiers communs

- `packages/shared/src` : types et schémas partagés par tous les jeux.
- `packages/games/src/common` : code commun à presque tous les jeux (règles, tirages, utilitaires).
- `packages/games/src/client` : composants d'écran partagés (TV, téléphones) et réglages communs.
- `packages/games/src/cards` : moteur des jeux de cartes. Il contient les modèles de Couleurs & chiffres et de Blanc-manger coco, et les composants d'écran réutilisés par Président, Poker, Rami 51 et Tarot.
- `packages/games/src/solo` : moteur partagé de Sudoku, Solitaire, Taquin et Mots croisés.
- `packages/games/src/media-quiz`, `packages/games/src/media-game.ts`, `packages/games/src/captions`, `packages/games/src/recipes` et `packages/games/src/board` : moteurs de questions, de légendes, de recettes et de plateau.
- `packages/games/src/index.ts` : le registre des jeux.
- `packages/games/src/__tests__` : tests des jeux.
- `packages/web/src/components/gameLogos.ts`, `GameScene.tsx` et `packages/web/src/screenBackgrounds.ts` : logos, scènes et décors des jeux.
- `packages/web/public/game-photos` : photos utilisées par les jeux.

Fichiers de configuration : `packages/games/package.json` et `packages/shared/package.json`.

## Jeux

| Jeu | Identifiant | Code principal | Dossier |
|---|---|---|---|
| 🧠 Quiz Party | `quiz-party` | `packages/games/src/quiz-party/module.ts` | `packages/games/src/quiz-party/` |
| 🧩 Phrases à trous | `phrases-trous` | `packages/games/src/phrases-trous/module.ts` | `packages/games/src/phrases-trous/` |
| 💭 Association express | `association` | `packages/games/src/association/module.ts` | `packages/games/src/association/` |
| 👉 Plutôt qui ? | `plutot-qui` | `packages/games/src/plutot-qui/module.ts` | `packages/games/src/plutot-qui/` |
| 🕵️ L’Imposteur | `imposteur` | `packages/games/src/imposteur/module.ts` | `packages/games/src/imposteur/` |
| 🐉 Aventure IA | `aventure-ia` | `packages/games/src/aventure/module.ts` | `packages/games/src/aventure/` |
| 🃏 Plus ou moins | `plus-ou-moins` | `packages/games/src/plus-ou-moins/module.ts` | `packages/games/src/plus-ou-moins/` |
| ⚡ Réflexe | `reflexe` | `packages/games/src/reflexe/module.ts` | `packages/games/src/reflexe/` |
| 🎮 Micro-Défis | `micro-defis` | `packages/games/src/micro-defis/module.ts` | `packages/games/src/micro-defis/` |
| 🤪 Gags en rafale | `gags-en-rafale` | `packages/games/src/gags-en-rafale/module.ts` | `packages/games/src/gags-en-rafale/` |
| 🤸 Funambule | `funambule` | `packages/games/src/funambule/module.ts` | `packages/games/src/funambule/` |
| 💣 Bombes party | `bombes-party` | `packages/games/src/bombes-party/module.ts` | `packages/games/src/bombes-party/` |
| 🌈 Couleurs & chiffres | `cartes-couleurs` | `packages/games/src/cards/presets.ts` | `packages/games/src/cards/` |
| 🥥 Blanc-manger coco | `cartes-coco` | `packages/games/src/cards/presets.ts` | `packages/games/src/cards/` |
| 👑 Président | `president` | `packages/games/src/president/module.ts` | `packages/games/src/president/` |
| 🏙️ Le Promoteur | `promoteur` | `packages/games/src/promoteur/module.ts` | `packages/games/src/promoteur/` |
| 🐺 Les Loups du village | `loups-village` | `packages/games/src/loups-village/module.ts` | `packages/games/src/loups-village/` |
| 🔢 Sudoku | `sudoku` | `packages/games/src/solo/games.ts` | `packages/games/src/solo/` |
| 🂡 Solitaire | `solitaire` | `packages/games/src/solo/games.ts` | `packages/games/src/solo/` |
| 🔀 Taquin | `taquin` | `packages/games/src/solo/games.ts` | `packages/games/src/solo/` |
| ✏️ Mots croisés | `mots-croises` | `packages/games/src/solo/games.ts` | `packages/games/src/solo/` |
| ♦️ Rami 51 | `rami-51` | `packages/games/src/rami51/module.ts` | `packages/games/src/rami51/` |
| 🎴 Tarot | `tarot` | `packages/games/src/tarot/module.ts` | `packages/games/src/tarot/` |
| ♠️ Poker Texas | `poker-texas` | `packages/games/src/poker/module.ts` | `packages/games/src/poker/` |
| 🎭 Imite-moi ! | `imite-moi` | `packages/games/src/imite-moi/module.ts` | `packages/games/src/imite-moi/` |
| 🧊 Banquise | `banquise` | `packages/games/src/banquise/module.ts` | `packages/games/src/banquise/` |
| 💥 BOUM ! | `boum` | `packages/games/src/boum/module.ts` | `packages/games/src/boum/` |
| 🧭 Plateau de test | `plateau-test` | `packages/games/src/plateau-test/module.ts` | `packages/games/src/plateau-test/` |

Les jeux de cartes partagent `packages/games/src/cards`. Les jeux solo partagent `packages/games/src/solo`. Les 5 jeux du lot 0.13.0 (karaoké, tennis party, Tribunal de l'absurde, téléphone arabe illustré, plateau fête) ne sont pas sur `main` : ils ne figurent pas ici.

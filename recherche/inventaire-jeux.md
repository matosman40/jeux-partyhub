# Inventaire des jeux de PartyHub

*Préparé le 19 octobre 2026, à partir du registre du moteur (`packages/games/src/index.ts`). Un jeu se publie en paquet seulement si sa définition tient dans un module déclaratif (cartes, plateau, questions YouTube, recettes).*

## Résumé

- 33 jeux dans le registre.
- 2 peuvent devenir des paquets : les deux jeux de cartes dont la définition est une donnée. Ils sont préparés dans ce dépôt.
- 31 ont leurs règles écrites dans le code. Les convertir reviendrait à réécrire chaque jeu dans le format déclaratif. Le format JavaScript, qui permettrait de les livrer comme paquets, n’est pas implémenté.
- Deux paquets existent déjà ici : `poker` (parcours au dé, sans lien avec le Poker Texas) et `parcours-des-questions`. Ils sont validés avec le moteur v0.11.0.

## Tous les jeux

| Jeu | Identifiant | Catégorie | Joueurs | Peut devenir un paquet ? | Raison |
|---|---|---|---|---|---|
| Quiz Party | `quiz-party` | quiz | 1–12 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Phrases à trous | `phrases-trous` | quiz | 2–8 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Association express | `association` | quiz | 2–12 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Plutôt qui ? | `plutot-qui` | quiz | 2–12 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| L’imposteur parmi nous | `imposteur-parmi-nous` | rôles | 3–10 | Non | Rôles cachés, phases et votes : logique écrite dans le code. |
| Le Tribunal de l’absurde | `tribunal-absurde` | quiz | 3–10 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Le téléphone arabe illustré | `telephone-arabe` | quiz | 2–10 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Aventure IA | `aventure-ia` | rôles | 2–6 | Non | Rôles cachés, phases et votes : logique écrite dans le code. |
| Plus ou moins | `plus-ou-moins` | cartes | 1–12 | Non | Moteur de jeu écrit dans le code. |
| Réflexe | `reflexe` | plateau | 1–12 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Micro-Défis | `micro-defis` | plateau | 1–12 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Gags en rafale | `gags-en-rafale` | plateau | 1–12 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Funambule | `funambule` | plateau | 1–12 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Bombes party | `bombes-party` | plateau | 2–10 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Couleurs & chiffres | `cartes-couleurs` | cartes | 2–6 | Oui, préparé | Données (cartes) : paquet préparé dans ce dépôt, en doublon du jeu intégré. |
| Blanc-manger coco | `cartes-coco` | cartes | 2–5 | Oui, préparé | Données (cartes) : paquet préparé dans ce dépôt, en doublon du jeu intégré. |
| Président | `president` | cartes | 3–6 | Non | Moteur de jeu écrit dans le code. |
| Le Promoteur | `promoteur` | plateau | 2–6 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Les Loups du village | `loups-village` | rôles | 4–12 | Non | Rôles cachés, phases et votes : logique écrite dans le code. |
| Sudoku | `sudoku` | solo | 1–8 | Non | Moteur solo partagé, écrit dans le code. |
| Solitaire | `solitaire` | solo | 1–8 | Non | Moteur solo partagé, écrit dans le code. |
| Taquin | `taquin` | solo | 1–8 | Non | Moteur solo partagé, écrit dans le code. |
| Mots croisés | `mots-croises` | solo | 1–8 | Non | Moteur solo partagé, écrit dans le code. |
| Rami 51 | `rami-51` | cartes | 2–5 | Non | Moteur de jeu écrit dans le code. |
| Tarot | `tarot` | cartes | 4–4 | Non | Moteur de jeu écrit dans le code. |
| Poker Texas | `poker-texas` | cartes | 2–8 | Non | Moteur de jeu écrit dans le code. |
| Imite-moi ! | `imite-moi` | quiz | 2–12 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Karaoké | `karaoke` | quiz | 2–12 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Banquise | `banquise` | plateau | 2–8 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| BOUM ! | `boum` | quiz | 2–12 | Non | Règles et contenu écrits dans le code. Un paquet quiz n’accepte que des extraits YouTube. |
| Plateau de test | `plateau-test` | plateau | 1–12 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Tennis party | `tennis-party` | plateau | 2–4 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |
| Plateau fête | `plateau-fete` | plateau | 2–8 | Non | Règles écrites dans le code. Un paquet plateau ne décrit que des cases et des dés. |

## Décisions à prendre

1. **Doublons** : les paquets `cartes-couleurs` et `cartes-coco` reprennent les jeux intégrés. Ils servent de modèles, mais une installation qui a déjà les jeux intégrés aura deux jeux du même nom.
2. **Conversion des jeux de code** : chaque conversion est une réécriture de règles, à décider jeu par jeu. Aucune n’est faite ici.
3. **Licence** : les paquets préparés reprennent la licence du projet (MIT). Les jeux de cartes sont des données écrites pour le projet ; à confirmer.

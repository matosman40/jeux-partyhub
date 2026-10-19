# Créer un nouveau jeu PartyHub : prompts complets

Ce document permet de créer un jeu de soirée pour PartyHub sans écrire de code : un assistant IA (ou une personne)
produit un dossier `jeux/<jeu>/` complet, avec ses textes, ses règles, ses sons et sa vignette. Le dossier est ensuite
contrôlé par `phgame`, puis publié par un tag.

Il contient :

1. le **prompt maître**, à copier-coller tel quel, avec les champs à remplir ;
2. les **règles du format**, tirées du code de PartyHub, à relire avant de publier ;
3. les **prompts pour les images** (vignette et icône) ;
4. les **prompts pour les sons** (quatorze bruitages et une musique de partie) ;
5. la **liste de contrôle** et la **publication**.

Exemples existants à imiter : `jeux/cartes-couleurs`, `jeux/poker` (plateau), `jeux/parcours-des-questions` (questions). Les
prompts de vignette déjà écrits sont dans `vignettes/*.prompt.txt`, et les sons dans `sons/`.

---

## 1. Prompt maître

Copiez le bloc ci-dessous dans l'assistant de votre choix, en remplaçant les champs `{{...}}`.

```text
Tu es concepteur de jeux de soirée pour PartyHub, une application où les joueurs jouent sur leurs téléphones et sur un
écran commun (la TV). Tu crées un paquet de jeu déclaratif : uniquement des fichiers JSON, des textes et des prompts.
Tu n'écris aucun code exécutable.

## Ce que je veux

- Idée du jeu : {{IDEE}}
- Module de jeu : {{MODULE}}  (cards = jeu de cartes, board = jeu de plateau au dé, quiz = questions sur extraits
  vidéo, recipe = consigne écrite puis vote)
- Identifiant du dossier : {{ID}}  (minuscules, chiffres et tirets, par exemple « chasse-aux-gages »)
- Nombre de joueurs : de {{MIN}} à {{MAX}}
- Durée visée : {{DUREE}} minutes
- Ambiance : {{AMBIANCE}}  (par exemple « fou rire, sans gêne », « famille », « entre amis, un peu piquant »)
- Public : {{PUBLIC}}

## Fichiers à produire

Produis chacun de ces fichiers, complet, dans un bloc séparé avec son chemin :

1. `manifest.json`
2. `game/definition.json`
3. `licenses/LICENCE.txt` (« Jeu original, tous droits réservés par son auteur, sauf les éléments listés dans
   licenses/SONS.txt et licenses/VIGNETTE.txt. »)
4. `licenses/SONS.txt`, si le jeu a des sons (une ligne par fichier : nom, origine, licence, outil et date)
5. `licenses/VIGNETTE.txt`, si le jeu a une vignette (origine de l'image, outil et licence)
6. La liste des prompts de sons à générer, un par bruitage et un pour la musique de partie (section 4 du guide)
7. Le prompt de la vignette (section 3 du guide)

## Règles du manifeste

- `"format": "phgame"`, `"formatVersion": 4`, `"id": "{{ID}}"` (identique au nom du dossier), `"version": "1.0.0"`.
- `"name"` et `"description"` (une phrase), `"author"` (laisser « {{AUTEUR}} »).
- `"kind": "declarative"`, `"entry": "game/definition.json"`, `"files": []`.
- `"engine": { "minVersion": "0.14.0", "api": 1 }`.
- `"requires": { "modules": ["{{MODULE}}"] }`.
- `"licenses"` : une entrée par fichier de licence. Chaque fichier audio ou image doit apparaître dans le champ `covers`
  de la licence qui le décrit. Un fichier non couvert fait refuser le paquet.
- `"cover": "assets/cover.png"` seulement si une vignette est fournie.
- Aucun autre champ. Aucun fichier en dehors de `game/`, `assets/`, `data/` et `licenses/`.

## Règles du jeu : limites à respecter

Toutes les limites sont vérifiées par le validateur. Un dépassement fait refuser le paquet.

### Si MODULE = cards

- `name` : 2 à 40 caractères. `description` : 160 caractères au plus. `icon` : un seul emoji, 8 caractères au plus.
- `theme` : `arcade`, `coco`, `nuit` ou `classique`.
- `families` : de 1 à 8 familles, chacune `{ "id", "label" (20 caractères au plus), "color" (#rrggbb) }`. Les `id` sont
  uniques, et `wild` est réservé.
- `cards` : de 1 à 200 types de cartes, chacun `{ "id" (unique), "label" (24 caractères au plus), "symbol" (1 à 4
  caractères), "family" (une famille, ou `wild` pour les jokers), "effect", "count" (1 à 20), "points" (0 à 100) }`.
  Facultatifs : `text` (240 caractères au plus), `rank` (0 à 999), `pair` (40 caractères au plus, pour le mémo).
- `effect` : `none`, `skip`, `reverse`, `draw2`, `draw4` ou `wild`. Une carte de famille `wild` doit avoir l'effet `wild`
  ou `draw4`, et réciproquement.
- `rules` : `minPlayers` et `maxPlayers` entre 2 et 8, avec minPlayers ≤ maxPlayers ; `handSize` entre 3 et 10 ;
  `matchOn` : `family`, `symbol` ou `either` ; `targetScore` entre 50 et 2000 ; `turnSeconds` entre 0 et 60 (0 = sans
  limite) ; `mechanic` facultatif : `shedding` (défaut, vider sa main), `memory`, `race` ou `trick`.
- `trump` (famille) n'est accepté qu'avec `mechanic: "trick"`.
- Mécanique `race` ou `trick` : aucune carte avec effet ni joker ; au moins `maxPlayers × handSize` cartes (plus une au
  centre pour `race`) ; 120 cartes au plus.
- Mécanique `memory` : chaque paire est formée de exactement 2 cartes (même `pair`, ou même `id` sans `pair`) ; aucun
  effet ni joker ; entre 4 et 60 cartes au total.
- Mécanique `shedding` (défaut) : au moins `maxPlayers × handSize + 5` cartes, pour distribuer les mains à tous les joueurs.
- `notice` : `goal` (300 caractères au plus) ; `steps` de 1 à 10 phrases ; `tips` de 0 à 6 phrases.

### Si MODULE = board

- `name`, `description`, `icon`, `theme` : mêmes limites que pour les cartes.
- `cells` : de 8 à 60 cases, chacune `{ "label" (24 caractères au plus, peut être vide), "kind", "value" (0 à 12) }`.
- `kind` :
  - `normal` : rien ;
  - `avance` : avance de `value` cases ;
  - `recule` : recule de `value` cases ;
  - `gain` : gagne `value` points ;
  - `perte` : perd `value` points ;
  - `passe` : passe son tour ;
  - `arrivee` : fin de la partie.
- Les cases `avance`, `recule`, `gain` et `perte` ont une `value` d'au moins 1.
- La première case est `normal`. La dernière est `arrivee`, et il n'y en a qu'une.
- `rules` : `minPlayers` et `maxPlayers` (2 à 8) ; `dice` (1 ou 2) ; `turnSeconds` (0 à 60).
- `notice` : mêmes limites que pour les cartes.

### Si MODULE = quiz

- `mode` : `devine` (on tape le titre) ou `sous-titres` (on écrit le sous-titre d'une scène en langue étrangère, puis on
  vote).
- `kind` : `film`, `musique` ou `extrait`. Il change la question posée (« Quel est ce film ? », « Quelle est cette
  chanson ? », « Qu'est-ce que c'est ? »).
- `name` : 3 à 40 caractères. `description` : 200 caractères au plus. `icon` : un emoji, 8 caractères au plus.
- `rules` : `questionCount` (1 à 30, défaut 8) ; `answerSeconds` (10 à 90, défaut 30) ; `speedBonus` (vrai ou faux).
- `items` : de 1 à 60 extraits, chacun :
  - `id` : 1 à 40 caractères (lettres, chiffres, `_` ou `-`), unique ;
  - `answer` : 200 caractères au plus ; `aliases` : 8 réponses acceptées au plus, 80 caractères chacune ;
  - `detail` : 160 caractères au plus (indice affiché après la réponse) ;
  - `source` : `{ "type": "youtube", "videoId": "..." }`, où `videoId` fait exactement 11 caractères ;
  - `startSec` : de 0 à 43200 ; `durationSec` : de 3 à 60.
- Ne fournissez que des vidéos dont la diffusion est autorisée et qui peuvent être intégrées. Ne mettez jamais de
  paroles de chansons, ni de passages protégés, dans les textes.

### Si MODULE = recipe

- `"recipe": "vote-sur-consigne"` (seule valeur admise).
- `name` : 3 à 40 caractères ; `description` : 200 caractères au plus ; `icon` : un emoji (défaut 💭).
- `rules` : `manches` (1 à 10, défaut 5) ; `ecriture` (10 à 120 secondes, défaut 40) ; `vote` (10 à 60 secondes, défaut
  25) ; `pointsParVote` (0 à 500, défaut 100) ; `motMax` (4 à 40 caractères, défaut 24).
- `consignes` : de 1 à 100 phrases, chacune de 3 à 90 caractères. Chaque consigne doit donner envie d'écrire un mot
  drôle, sans viser une personne réelle.
- `ecrans` : facultatif. Sans lui, la disposition par défaut est utilisée.

## Qualité du texte

- Français oral, phrases courtes, pas de jargon. Le jeu se lit à voix haute.
- Personne réelle, marque, personnage protégé, moquerie d'une origine, d'un physique ou d'une religion : interdits.
- Les textes d'aide doivent suffire à expliquer le jeu à quelqu'un qui ne l'a jamais joué.

## Réponse attendue

Rendez les fichiers, puis une liste de contrôle cochée (section 5 du guide). Signalez tout point que vous n'avez pas pu
vérifier, par exemple un nombre de cartes que vous n'avez pas compté.
```

---

## 2. Règles du format (référence)

Le prompt ci-dessus reprend ces règles. Elles sont tirées du code de PartyHub : en cas de doute, c'est le validateur qui
tranche (`phgame check`).

| Élément | Règle |
|---|---|
| Dossier du jeu | `game/`, `assets/`, `data/`, `licenses/` et `manifest.json` seulement |
| Format | `formatVersion` 4 : cartes, plateau, questions et recettes, avec les sons |
| Moteur minimum | `engine.minVersion` 0.14.0 pour un paquet avec sons (à réviser si le paquet n'en a pas) |
| Sons | `assets/sons/`, `.ogg` ou `.mp3`, déclarés dans `game/definition.json`, bloc `sons` |
| Budgets audio | 512 Ko par fichier, 2 Mio par paquet, 16 fichiers au plus |
| Image | `.png`, `.jpg`, `.jpeg` ou `.webp` ; 200 Ko au plus ; 1024 px au plus de côté |
| Vignette | `assets/cover.png` ; 640 × 360 px et moins de 200 Ko (convention des jeux du dépôt) |
| Icône | un emoji, 8 caractères au plus (pas une image) |
| Musique | un seul emplacement dans un paquet : `partie` |

---

## 3. Prompts pour les images

### 3.1 Vignette (couverture du jeu)

La vignette sert de couverture dans le magasin. Elle n'a pas de texte : le titre reste celui du manifeste.

**Format à obtenir** : PNG, 640 × 360 px (format 16:9), moins de 200 Ko, enregistré en `jeux/<jeu>/assets/cover.png`.

**Modèle de prompt** (à compléter) :

```text
Flat illustrated cover art for a party game called "{{TITRE}}". {{SCENE}}. Colour palette: {{COULEUR_1}} background,
{{COULEUR_2}} secondary shapes, {{ACCENT}} highlight. Bold clean shapes, soft even light, cheerful and playful mood,
high contrast, simple readable silhouettes that still work at thumbnail size. Landscape 16:9 composition, main subject
on the left third, empty space on the right. No text, no letters, no numbers, no logos, no watermark, no real people,
no recognisable faces, no copyrighted characters or brands.
```

**Exemples prêts à l'emploi** (les réglages de `vignettes/*.json` donnent les mêmes couleurs) :

- Poker (plateau) : « stacks of colourful poker chips and a single red die on dark green felt », palette
  `#7a1f2b` / `#2b0b10`, accent `#f4d35e`.
- Couleurs & chiffres (cartes) : « a fan of four playing cards in cream, gold and red on a deep green felt table »,
  palette `#1f6f4a` / `#0c3a26`, accent `#f2c14e`.

**Contrôle avant dépôt** : 640 × 360 exactement, pas de texte lisible, lisible en petit, pas de visage reconnaissable,
pas de marque. Le titre doit se lire sans l'image.

**Autre voie** : `vignettes/generer.py` produit une vignette à partir d'un fichier `vignettes/<jeu>.json` (titre, sous-titre,
couleurs, motif `cartes`, `coco`, `parcours` ou `table`). Déposez alors le résultat dans `jeux/<jeu>/assets/cover.png`.

### 3.2 Icône (emoji)

L'icône n'est pas une image : c'est un emoji de 8 caractères au plus, dans `definition.json` (champ `icon`). Choisissez
un emoji qui évoque l'action principale (un dé pour un jeu de dés, une carte pour un jeu de cartes, un micro pour un jeu
de voix). Vérifiez qu'il s'affiche sur téléphone.

---

## 4. Prompts pour les sons

### 4.1 Règles communes à tous les sons

- Format : `.ogg` (Vorbis) de préférence, ou `.mp3`. Mono suffit.
- Pic à environ −3 dBFS, sans écrêtage. Pas de silence avant ni après le son.
- Un bruitage est sec : pas de queue de réverbération longue, pas de musique, pas de voix.
- Durée visée indiquée pour chaque son (à respecter à 10 % près).
- Taille : 512 Ko au plus par fichier. Total du paquet : 2 Mio au plus, 16 fichiers au plus (bruitages et musique compris).
- Noms de fichiers exacts, dans `assets/sons/` : `sfx-<nom>.ogg` et `musique-partie.ogg`.
- Chaque fichier est déclaré dans `game/definition.json` (bloc `sons`) et couvert par `licenses/SONS.txt`.

### 4.2 Les quatorze bruitages

Le nom (colonne 1) est le seul admis : une clé inconnue fait refuser le paquet. Vous ne devez pas utiliser tous les
bruitages : déclarez seulement ceux que le jeu emploie.

| Nom | Quand le jouer | Durée visée | Prompt |
|---|---|---|---|
| `click` | bouton, choix simple | 0,1 s | "Short soft UI click, dry, no tail" |
| `place` | carte ou pion posé | 0,2 s | "Soft wooden tap, a piece placed on a table, dry" |
| `hit` | coup, erreur légère | 0,15 s | "Short dull punchy thump, dry" |
| `pickup` | gain, pièce ramassée | 0,6 s | "Bright little pick-up chime, two notes rising, friendly" |
| `turn` | changement de tour | 0,5 s | "Short two-note notification chime, clear and friendly" |
| `draw` | piocher une carte | 0,2 s | "Quick paper slide, a card drawn from a deck" |
| `explode` | explosion, défaite brutale | 1,5 s | "Short cartoon explosion, playful, not scary" |
| `crate` | coffre ou boîte qui s'ouvre | 0,9 s | "Wooden crate creak then pop open" |
| `die` | dé lancé et posé | 1,2 s | "Dice rolling on a wooden table then landing, three bounces" |
| `win` | victoire d'une manche | 2 s | "Short celebratory fanfare, bright, ends clean" |
| `start` | début de partie | 1,5 s | "Rising whoosh followed by a short bright chime, game start" |
| `final` | fin de partie | 3 s | "Triumphant short finale jingle with a cymbal, ends clean" |
| `card` | carte spéciale qui agit | 0,4 s | "Magic card flip with a small sparkle" |
| `chip` | jeton, mise | 0,9 s | "Two poker chips clinking on a table" |

**Prompt générique pour un bruitage** (à compléter avec la ligne du tableau) :

```text
Sound effect: {{DESCRIPTION}}. Duration {{SECONDS}} seconds, ending cleanly with no tail. Dry, close and clean, no reverb,
no background music, no voice, no silence before or after the sound. Mono, peak about -3 dB, no clipping. Family-friendly.
```

### 4.3 La musique de partie (`musique-partie.ogg`)

Une seule musique par paquet : la musique qui tourne pendant la partie sur l'écran commun.

- Durée : 30 à 60 secondes, en boucle. La fin doit se raccorder au début, sans clic.
- Instrumentale, sans voix, sans paroles. Discrète : elle doit passer sous une conversation.
- Plutôt entre 100 et 130 BPM, rythmée, chaleureuse. Moins de 512 Ko.

**Prompt générique** (à compléter) :

```text
Instrumental background loop for a party board game, {{AMBIANCE}} mood, {{BPM}} BPM, {{TONALITE}}, {{SECONDS}} seconds,
seamless loop (the last bar leads back to the first without a gap or click). No vocals, no lyrics, no sound effects,
mid-range and not too loud, light rhythm, works quietly under conversation. Family-friendly.
```

### 4.4 Sources et licences

- Préférez d'abord des sons libres vérifiables (par exemple les bibliothèques Kenney, sous licence CC0 : voir
  `sons/README.md`).
- Un son généré par un outil d'IA n'est acceptable que si les conditions de l'outil autorisent l'usage commercial et la
  redistribution dans un paquet gratuit. Notez l'outil, la date et la licence dans `licenses/SONS.txt`.
- Ne reprenez jamais un extrait de chanson ou d'enregistrement sous droits.

---

## 5. Liste de contrôle et publication

### Avant de publier

- [ ] `manifest.json` : `id` = nom du dossier, `formatVersion` 4, `engine.minVersion` 0.14.0, `requires.modules` correct.
- [ ] `game/definition.json` : toutes les limites de la section 1 respectées.
- [ ] Chaque fichier de `assets/` est déclaré dans un `licenses[].covers`.
- [ ] Les sons ont le nom exact du tableau, la durée visée, et ne dépassent pas 512 Ko chacun ni 2 Mio au total.
- [ ] La vignette fait 640 × 360 et ne contient pas de texte.
- [ ] `licenses/LICENCE.txt`, `SONS.txt` et `VIGNETTE.txt` indiquent les origines et les licences.
- [ ] Aucune personne réelle, marque, paroles ni extrait protégé.
- [ ] Le texte de la notice se lit à voix haute en moins d'une minute.

### Contrôler le paquet

Depuis un dépôt PartyHub à jour :

```bash
npm run phgame -w @partyhub/server -- pack /chemin/vers/jeux/<jeu> /tmp/<jeu>.phgame
npm run phgame -w @partyhub/server -- check /tmp/<jeu>.phgame
```

`check` valide le paquet et joue deux parties avec des robots : une erreur ici bloque la publication.

### Publier

1. Mettez `version` du manifeste à la version voulue (par exemple `1.0.0`).
2. Créez le tag `<jeu>-vX.Y.Z`, où `X.Y.Z` est cette `version` :

   ```bash
   git tag <jeu>-v1.0.0
   git push origin <jeu>-v1.0.0
   ```

3. Le workflow `publier.yml` construit le paquet, le contrôle, calcule son empreinte et crée la release avec
   `<jeu>.phgame` et `<jeu>.phgame.sha256`.
4. Une version publiée ne se réécrit jamais : une correction devient une nouvelle version.

**Point de vigilance** : `PARTYHUB_REF` (variable du dépôt) doit pointer vers une version de PartyHub qui connaît le
moteur demandé. Un paquet à `engine.minVersion` 0.14.0 n'est pas accepté par une version plus ancienne.

---

## 6. Exemples de fragments

Structure minimale d'une définition de plateau (reprise de `examples/exemple-plateau`) :

```json
{
  "name": "Exemple de plateau",
  "description": "Avancez au dé jusqu'à l'arrivée.",
  "icon": "🎲",
  "theme": "arcade",
  "cells": [
    { "label": "Départ", "kind": "normal", "value": 0 },
    { "label": "Bond", "kind": "avance", "value": 2 },
    { "label": "Amende", "kind": "perte", "value": 1 },
    { "label": "", "kind": "normal", "value": 0 },
    { "label": "Pause", "kind": "passe", "value": 0 },
    { "label": "Bonus", "kind": "gain", "value": 2 },
    { "label": "", "kind": "normal", "value": 0 },
    { "label": "Arrivée", "kind": "arrivee", "value": 0 }
  ],
  "rules": { "minPlayers": 2, "maxPlayers": 4, "dice": 1, "turnSeconds": 30 },
  "notice": {
    "goal": "Être le premier arrivé sur la dernière case.",
    "steps": ["Lancer le dé à votre tour, puis avancer du nombre obtenu."],
    "tips": ["Les cases Bonus rapportent des points."]
  }
}
```

Structure minimale d'une définition de questions (reprise de `examples/exemple-quiz`) :

```json
{
  "mode": "devine",
  "kind": "film",
  "name": "Exemple de questions",
  "description": "Trois extraits à reconnaître.",
  "icon": "🎬",
  "rules": { "questionCount": 3, "answerSeconds": 20, "speedBonus": true },
  "items": [
    {
      "id": "extrait-1",
      "answer": "Titre du premier film",
      "aliases": ["Premier film"],
      "detail": "Année de sortie",
      "source": { "type": "youtube", "videoId": "exempleVi01" },
      "startSec": 30,
      "durationSec": 15
    }
  ]
}
```

Les identifiants vidéo de ces exemples sont fictifs : remplacez-les par des vidéos réelles, dont la diffusion est autorisée.

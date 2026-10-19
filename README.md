# jeux-partyhub

Les jeux de PartyHub, un dossier par jeu. Chaque version est publiée sous forme de release GitHub, qu'une installation
PartyHub peut importer et mettre à jour.

## Tous les jeux

### Paquets installables (dans `jeux/`)

| Jeu | Identifiant | Version |
|---|---|---|
| [Couleurs & chiffres](jeux/cartes-couleurs) | `cartes-couleurs` | 1.0.0 |
| [Blanc-manger coco](jeux/cartes-coco) | `cartes-coco` | 1.0.0 |
| [Parcours des questions](jeux/parcours-des-questions) | `parcours-des-questions` | 1.0.0 |
| [Poker (parcours au dé)](jeux/poker) | `poker` | 1.0.0 |

### Jeux intégrés à PartyHub

Ces 28 jeux sont écrits dans le code de PartyHub : ils n'ont pas de dossier ici et ne se publient pas comme paquets. Chaque ligne renvoie vers sa fiche (règles, déroulement, conseils, journal de versions).

| Jeu | Catégorie | Joueurs | Durée | Version | Fiche |
|---|---|---|---|---|---|
| 🧠 Quiz Party | Quiz | 1–12 | 10 min | 1.1.0 | [`quiz-party.md`](jeux-integres/quiz-party.md) |
| 🧩 Phrases à trous | Quiz | 2–8 | 12 min | 1.0.0 | [`phrases-trous.md`](jeux-integres/phrases-trous.md) |
| 💭 Association express | Quiz | 2–12 | 12 min | 1.0.0 | [`association.md`](jeux-integres/association.md) |
| 👉 Plutôt qui ? | Quiz | 2–12 | 10 min | 1.0.0 | [`plutot-qui.md`](jeux-integres/plutot-qui.md) |
| 🕵️ L’Imposteur | Rôle | 3–10 | 15 min | 1.0.0 | [`imposteur.md`](jeux-integres/imposteur.md) |
| 🐉 Aventure IA | Rôle | 2–6 | 12 min | 1.2.0 | [`aventure-ia.md`](jeux-integres/aventure-ia.md) |
| 🃏 Plus ou moins | Cartes | 1–12 | 8 min | 1.0.0 | [`plus-ou-moins.md`](jeux-integres/plus-ou-moins.md) |
| ⚡ Réflexe | Ambiance | 1–12 | 5 min | 1.0.0 | [`reflexe.md`](jeux-integres/reflexe.md) |
| 🎮 Micro-Défis | Ambiance | 1–12 | 8 min | 1.0.0 | [`micro-defis.md`](jeux-integres/micro-defis.md) |
| 🤪 Gags en rafale | Ambiance | 1–12 | 3 min | 1.0.0 | [`gags-en-rafale.md`](jeux-integres/gags-en-rafale.md) |
| 🤸 Funambule | Ambiance | 1–12 | 5 min | 1.0.0 | [`funambule.md`](jeux-integres/funambule.md) |
| 💣 Bombes party | Ambiance | 2–4 | 8 min | 1.0.0 | [`bombes-party.md`](jeux-integres/bombes-party.md) |
| 🌈 Couleurs & chiffres | Cartes | 2–6 | 20 min | 1.0.0 | [`cartes-couleurs.md`](jeux-integres/cartes-couleurs.md) |
| 🥥 Blanc-manger coco | Cartes | 2–5 | 12 min | 1.0.0 | [`cartes-coco.md`](jeux-integres/cartes-coco.md) |
| 👑 Président | Cartes | 3–6 | 20 min | 1.0.0 | [`president.md`](jeux-integres/president.md) |
| 🏙️ Le Promoteur | Ambiance | 2–6 | 45 min | 1.0.0 | [`promoteur.md`](jeux-integres/promoteur.md) |
| 🐺 Les Loups du village | Rôle | 4–12 | 25 min | 1.0.0 | [`loups-village.md`](jeux-integres/loups-village.md) |
| 🔢 Sudoku | Solo | 1–8 | 15 min | 1.0.0 | [`sudoku.md`](jeux-integres/sudoku.md) |
| 🂡 Solitaire | Solo | 1–8 | 12 min | 1.0.0 | [`solitaire.md`](jeux-integres/solitaire.md) |
| 🔀 Taquin | Solo | 1–8 | 10 min | 1.0.0 | [`taquin.md`](jeux-integres/taquin.md) |
| ✏️ Mots croisés | Solo | 1–8 | 15 min | 1.0.0 | [`mots-croises.md`](jeux-integres/mots-croises.md) |
| ♦️ Rami 51 | Cartes | 2–5 | 40 min | 1.0.0 | [`rami-51.md`](jeux-integres/rami-51.md) |
| 🎴 Tarot | Cartes | 4 | 30 min | 1.0.0 | [`tarot.md`](jeux-integres/tarot.md) |
| ♠️ Poker Texas | Cartes | 2–8 | 20 min | 1.0.0 | [`poker-texas.md`](jeux-integres/poker-texas.md) |
| 🎭 Imite-moi ! | Quiz | 2–12 | 6 min | 1.0.0 | [`imite-moi.md`](jeux-integres/imite-moi.md) |
| 🧊 Banquise | Ambiance | 2–8 | 4 min | 1.0.0 | [`banquise.md`](jeux-integres/banquise.md) |
| 💥 BOUM ! | Quiz | 2–12 | 12 min | 1.0.0 | [`boum.md`](jeux-integres/boum.md) |
| 🧭 Plateau de test | Ambiance | 1–12 | 5 min | 1.0.0 | [`plateau-test.md`](jeux-integres/plateau-test.md) |

## Structure

```
jeux/
├── _modele/          modèle de départ, jamais publié (le nom commence par « _ »)
└── <jeu>/            un jeu : manifest.json, game/definition.json, assets/, licenses/
sons/                 bruitages et musiques, copiés dans les paquets (assets/sons/), voir sons/README.md
vignettes/            vignettes des jeux (réglages et prompts), voir vignettes/README.md
jeux-integres/        fiches (règles et informations, sans code) des jeux écrits dans PartyHub, voir jeux-integres/README.md
```

## Ajouter un jeu

1. Copiez `jeux/_modele` vers `jeux/<jeu>` (identifiant en minuscules, chiffres et tirets).
2. Remplissez `manifest.json` : `id` identique au nom du dossier, `version`, `name`, `description`, `author`.
3. Modifiez `game/definition.json` et `licenses/LICENCE.txt`.
4. Vérifiez localement avec `phgame pack` et `phgame check` (voir [docs/PUBLIER-UN-JEU.md](https://github.com/matosman40/Partyhub/blob/main/docs/PUBLIER-UN-JEU.md) du dépôt PartyHub).

## Créer un nouveau jeu avec un assistant IA

`prompts/NOUVEAU-JEU.md` contient un prompt complet pour créer un jeu (cartes, plateau, questions ou recettes), avec les
règles du format, les prompts pour la vignette et les prompts pour les quatorze bruitages et la musique de partie.

## Publier une version

Créez un tag `<jeu>-vX.Y.Z`, où `X.Y.Z` est la `version` du manifeste :

```bash
git tag frontieres-v1.0.0
git push origin frontieres-v1.0.0
```

Le workflow `publier.yml` construit le paquet, le contrôle, calcule son empreinte et crée la release avec
`<jeu>.phgame` et `<jeu>.phgame.sha256`. Une version publiée ne se réécrit jamais : une correction devient une nouvelle
version.

## Importer dans PartyHub

Dans l'administration, section **Sources GitHub**, indiquez `auteur/jeux-partyhub/<jeu>`. PartyHub installe la version la
plus haute du jeu, et la met à jour à la demande ou une fois par jour.

## Jeux intégrés à PartyHub

La plupart des jeux de PartyHub sont écrits directement dans le code de l'application : ils n'ont pas de dossier ici et ne publient pas de release. C'est le cas du Poker Texas (hold'em), dont le code se trouve dans le dépôt PartyHub, dans `packages/games/src/poker`, et qui est désactivé par défaut dans une installation neuve.

Le dossier `poker` de ce dépôt est un autre jeu : un parcours au dé, sans lien avec le Poker Texas.

Deux jeux de cartes intégrés ont aussi un paquet ici, `cartes-couleurs` (Couleurs & chiffres) et `cartes-coco` (Blanc-manger coco). Ce sont des doublons des jeux intégrés, utiles comme modèles à copier.

Une fiche par jeu intégré, avec le but, le déroulement, les conseils, le nombre de joueurs et le journal de versions, est dans [`jeux-integres/`](jeux-integres/README.md). Ce sont des fiches de texte : le code reste dans PartyHub. Quand le format de code existera, chacun de ces jeux aura son dossier dans `jeux/`, avec son code, et sera installable seul.

L'inventaire complet des jeux de PartyHub, avec ce qui peut ou non devenir un paquet, est dans `recherche/inventaire-jeux.md`.

## Réglages

- `PARTYHUB_REF` (variable du dépôt) : branche ou tag de PartyHub utilisé pour contrôler les paquets. Par défaut
  `v0.11.0`. Les paquets de format 4 (sons) demandent PartyHub 0.14.0 : réglez la variable sur ce tag une fois publié,
  sinon ces paquets sont refusés. Une valeur qui n'existe pas fait échouer toutes les publications.

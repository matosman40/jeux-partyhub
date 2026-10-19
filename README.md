# jeux-partyhub

Les jeux de PartyHub, un dossier par jeu. Chaque version est publiée sous forme de release GitHub, qu'une installation
PartyHub peut importer et mettre à jour.

## Structure

```
jeux/
├── _modele/          modèle de départ, jamais publié (le nom commence par « _ »)
└── <jeu>/            un jeu : manifest.json, game/definition.json, assets/, licenses/
sons/                 bruitages et musiques, copiés dans les paquets (assets/sons/), voir sons/README.md
vignettes/            vignettes des jeux (réglages et prompts), voir vignettes/README.md
```

## Ajouter un jeu

1. Copiez `jeux/_modele` vers `jeux/<jeu>` (identifiant en minuscules, chiffres et tirets).
2. Remplissez `manifest.json` : `id` identique au nom du dossier, `version`, `name`, `description`, `author`.
3. Modifiez `game/definition.json` et `licenses/LICENCE.txt`.
4. Vérifiez localement avec `phgame pack` et `phgame check` (voir `docs/PUBLIER-UN-JEU.md` du dépôt PartyHub).

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

L'inventaire complet des jeux de PartyHub, avec ce qui peut ou non devenir un paquet, est dans `recherche/inventaire-jeux.md`.

## Réglages

- `PARTYHUB_REF` (variable du dépôt) : branche ou tag de PartyHub utilisé pour contrôler les paquets. Par défaut
  `v0.11.0`. Les paquets de format 4 (sons) demandent PartyHub 0.13.0 : réglez la variable sur ce tag une fois publié,
  sinon ces paquets sont refusés. Une valeur qui n'existe pas fait échouer toutes les publications.

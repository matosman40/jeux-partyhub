# 🐉 Aventure IA

Rôle · 2 à 6 joueurs · environ 12 min · utilise une IA générative si elle est configurée

Une aventure racontée en direct : chacun incarne un personnage, vote les choix et affronte les ennemis tour par tour.

## But

Atteindre l’objectif de l’aventure, sans que tous les personnages tombent.

## Déroulement

1. Choisissez votre personnage et lisez sa fiche. Si vous avez déjà joué, vous pouvez reprendre un ancien personnage, avec son niveau.
2. Chaque scène propose des choix : une rencontre, un dialogue avec un habitant, une énigme, une halte, ou un affrontement. Votez pour le choix qui vous tente : il se joue avec un jet de dé.
3. Les réponses aux habitants comptent : un personnage qui plaît ouvre des portes, un personnage vexant les ferme.
4. Un affrontement se joue tour par tour : chacun choisit une action à chaque manche (frapper, feinter, soigner, parlementer).
5. Les réussites donnent de l’expérience : un personnage monte de niveau, trouve des objets, et garde tout cela pour la prochaine partie.

## Conseils

- Chaque choix a une conséquence claire : la réussite ou l’échec du jet fait avancer l’histoire.
- Un combat se gagne en équipe : soignez le plus blessé avant qu’il ne tombe.
- Les personnages secondaires se souviennent de vous : soyez aimable, ou gagnez-les par la ruse.
- Quand tous les personnages sont à terre, l’aventure se termine en défaite.
- Sans IA configurée sur le serveur, l’aventure se joue avec une histoire de secours, avec des thèmes écrits à l’avance.

## Version

- Version du jeu : 1.2.0
- Identifiant : `aventure-ia`
- Code source : `packages/games/src/aventure/module.ts` (dépôt PartyHub)

## Journal

- 0.12.0, 2026-10-18 (Ajouté) : Drapeau « IA » dans le manifeste des jeux (Quiz Party, Phrases à trous, Aventure IA), qui alimente le filtre « Avec IA ».
- 0.12.0, 2026-10-18 (Modifié) : Aventure IA : description raccourcie pour tenir sur une carte du catalogue. Tarot : une étape de la notice raccourcie, sans changer la règle.
- 0.11.0, 2026-10-17 (Ajouté) : Aventure IA, plus de variété : six thèmes (Brumes et lanternes, Carnaval masqué, Forêt qui chuchote, Fromagerie hantée, Les pigeons gouvernent, Vaisseau rétro), chacun avec son intrigue de secours. Le salon choisit le thème (au hasard, un thème précis, ou libre avec une précision), le ton (dont « Absurde et loufoque ») et la difficulté : facile, normale ou difficile, qui décale les jets et les points de vie des ennemis.
- 0.11.0, 2026-10-17 (Ajouté) : Aventure IA, types de scène : rencontre, dialogue avec un personnage (chaque réplique fait évoluer son lien avec le groupe, de « hostile » à « allié »), énigme (un indice, et un objet à la clé), halte (on reprend des points de vie) et affrontement tour par tour.
- 0.11.0, 2026-10-17 (Ajouté) : Aventure IA, progression : chaque réussite rapporte de l’expérience. Un personnage monte jusqu’au niveau 5, avec plus de points de vie maximum, une stat plus faible renforcée, et un sac de quatre objets au plus.
- 0.11.0, 2026-10-17 (Ajouté) : Aventure IA, personnages gardés : les personnages joués sont enregistrés dans le profil (jusqu’à quarante, avec leur niveau, leurs parties et leur portrait). Dans une autre partie, « Tes personnages » sur le téléphone permet de les reprendre. Ils sont supprimés avec le profil.
- 0.11.0, 2026-10-17 (Ajouté) : Aventure IA, images : chaque personnage reçoit un portrait et chaque monde un fond, générés par une IA d’image (Cloudflare Workers AI, avec ModelScope en secours). Ils sont gardés dans une bibliothèque partagée par thème : un fond ou un portrait déjà créé se reprend dans les parties suivantes. Sans fournisseur, le rendu reste celui d’aujourd’hui. Les clés et le plafond journalier (`IMAGE_MAX_PER_DAY`) restent sur le serveur.
- 0.11.0, 2026-10-17 (Modifié) : Aventure IA, refondue pour une histoire qui tient debout : le monde a un objectif et un secret que le conteur révèle petit à petit. Chaque choix dit déjà ce qui arrive en cas de réussite ou d’échec, et le jet ne fait que trancher. Le groupe rencontre des personnages secondaires, dessinés comme les personnages du jeu (le dessin dépend du nom) ; la fiche de chaque joueur montre son avatar ou sa photo ; un affrontement se joue tour par tour sur les téléphones (frapper, feinter, soigner, parlementer). Parties de 3 à 6 scènes, vote de 15 à 120 secondes.
- 0.11.0, 2026-10-17 (Modifié) : Aventure IA, bibliothèque : jusqu’à quarante personnages par profil (huit auparavant).
- 0.11.0, 2026-10-17 (Corrigé) : Aventure IA : une fiche abîmée dans la bibliothèque d’un profil ne fait plus perdre les autres personnages à la sauvegarde suivante. Seule la fiche abîmée est écartée.
- 0.10.0, 2026-10-16 (Ajouté) : Aventure IA : une aventure racontée en direct. L’écran principal génère le monde et six personnages, chacun avec sa fiche (stats, points de vie, pouvoir narratif, défaut, objet). À chaque scène, les joueurs votent un choix ; le personnage qui l’a choisi tente un jet de d20 plus sa stat, et la suite dépend du résultat. Sans IA configurée, une histoire de secours est jouée.

---

Fiche générée depuis PartyHub 33cf929 (registre des jeux). La notice est la notice par défaut : un administrateur peut la modifier dans PartyHub, et cette fiche ne le reflète pas.

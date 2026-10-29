# 🧪 Essai des appareils

Solo · 1 à 12 joueurs · environ 5 min

Vérifiez le micro, la caméra, le mouvement et le dessin de chaque téléphone.

## But

Savoir, avant une vraie partie, si chaque téléphone de la salle sait faire ce que les jeux lui demanderont : entendre un son, filmer, sentir l’inclinaison, dessiner, répondre au toucher et lire une vidéo.

## Déroulement

1. Dans le salon, l’hôte choisit les essais à passer (micro, caméra, mouvement, dessin, touches, vidéo) et lance la partie.
2. Les essais se suivent dans l’ordre choisi, sur l’écran principal et sur chaque téléphone.
3. Sur son téléphone, chaque joueur fait l’essai demandé : maintenir un son, filmer une image fluide (puis se revoir sur deux secondes d’enregistrement), incliner l’appareil de chaque côté, tracer un trait, toucher l’écran.
4. Le téléphone déclare son résultat. Le serveur n’entend pas le son, ne voit ni l’image ni le geste : il ne garde que le résultat déclaré.
5. À la fin, le tableau de la salle reprend les résultats de tous les téléphones.

## Conseils

- Le son, l’image et la vidéo restent sur le téléphone : seul le résultat est envoyé.
- Le micro, la caméra et le mouvement demandent l’accord du navigateur, et une page en HTTPS.
- Un téléphone peut refaire un essai et corriger son résultat (réglage « reprise », activé par défaut).
- La durée du son, la longueur du trait, l’inclinaison, le nombre d’images par seconde et le délai des touches se règlent dans le salon, avant le lancement.
- L’essai vidéo n’apparaît que si l’hôte donne un lien YouTube valide ; les téléphones ne reçoivent jamais le lien, seulement l’identifiant de la vidéo.

## Version

- Version du jeu : 1.3.0
- Identifiant : `essai-appareils`
- Code source : `packages/games/src/essai-appareils/module.ts` (dépôt PartyHub)

## Journal

- 0.17.5, 2026-10-27 (Ajouté) : Jeu « Essai des appareils » : vérifie, téléphone par téléphone, le micro (son maintenu), la caméra (image, fluidité, enregistrement de deux secondes relu sur le téléphone), le mouvement (inclinaison), le dessin, la réactivité des touches, et la lecture d'une vidéo YouTube dans un cadre (lien donné par l'hôte, jamais sur les téléphones sous forme de lien).
- 0.17.5, 2026-10-27 (Vérifié) : Tests navigateur : `scripts/essai-appareils-browser.py` (18 contrôles) et `scripts/bombes-browser.py` (12 contrôles, un téléphone se déplace sur le plateau et s'exprime).

---

Fiche rédigée d’après PartyHub 0.17.5 (module `essai-appareils`). Elle ne se met pas à jour toute seule.

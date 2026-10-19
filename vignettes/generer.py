#!/usr/bin/env python3
"""Génère la vignette (couverture) de chaque jeu, à partir de vignettes/<jeu>.json.

Usage, depuis la racine du dépôt :
    python3 vignettes/generer.py                 # tous les jeux
    python3 vignettes/generer.py poker           # un seul jeu

Écrit jeux/<jeu>/assets/cover.png : 640 × 360, moins de 200 Ko, déclaré comme couverture du paquet.

Pour une image produite par un générateur d'images, collez vignettes/<jeu>.prompt.txt dans l'outil, puis
déposez le résultat à la place de jeux/<jeu>/assets/cover.png (PNG, 640 × 360, moins de 200 Ko).
"""

import json
import pathlib
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

LARGEUR, HAUTEUR = 640, 360
RACINE = pathlib.Path(__file__).resolve().parent.parent
POLICE_GRASSE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
POLICE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def couleur(hexa):
    hexa = hexa.lstrip("#")
    return tuple(int(hexa[i : i + 2], 16) for i in (0, 2, 4))


def fond(haut, bas):
    img = Image.new("RGB", (LARGEUR, HAUTEUR))
    d = ImageDraw.Draw(img)
    for y in range(HAUTEUR):
        t = y / (HAUTEUR - 1)
        c = tuple(round(haut[i] * (1 - t) + bas[i] * t) for i in range(3))
        d.line([(0, y), (LARGEUR, y)], fill=c)
    return img


def carte(d, x, y, angle_dy, accent, couleur_carte):
    # Carte blanche, bord fin, symbole au centre : une main en éventail, sans rotation.
    d.rounded_rectangle([x, y + angle_dy, x + 120, y + 170 + angle_dy], radius=14, fill=couleur_carte, outline=(40, 40, 40), width=3)
    d.ellipse([x + 42, y + 72 + angle_dy, x + 78, y + 108 + angle_dy], fill=accent, outline=(40, 40, 40), width=2)


def motif_cartes(d, accent):
    for i, dy in enumerate([40, 18, 0, 18]):
        carte(d, 370 + i * 44, 80 + dy, 0, accent, (250, 246, 232))


def motif_coco(d, accent):
    for x, y, r in [(470, 130, 70), (560, 200, 52), (420, 240, 44)]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=(250, 250, 244), outline=(60, 50, 40), width=4)
        d.ellipse([x - r // 3, y - r // 3, x + r // 3, y + r // 3], fill=accent)


def motif_parcours(d, accent):
    cases = [(380, 250), (430, 250), (480, 250), (480, 200), (480, 150), (530, 150), (580, 150), (580, 200), (580, 250)]
    for i, (x, y) in enumerate(cases):
        d.rounded_rectangle([x - 20, y - 20, x + 20, y + 20], radius=6, fill=(250, 246, 232) if i % 2 else accent, outline=(40, 30, 60), width=3)
    x, y = 500, 310
    d.rounded_rectangle([x - 28, y - 28, x + 28, y + 28], radius=8, fill=(255, 255, 255), outline=(40, 30, 60), width=3)
    for dx, dy in [(-12, -12), (12, -12), (-12, 12), (12, 12), (0, 0)]:
        d.ellipse([x + dx - 4, y + dy - 4, x + dx + 4, y + dy + 4], fill=(40, 30, 60))


def motif_table(d, accent):
    for i in range(5):
        y = 270 - i * 18
        d.ellipse([430, y - 14, 530, y + 14], fill=accent, outline=(30, 30, 30), width=3)
    d.rounded_rectangle([540, 210, 580, 250], radius=7, fill=(230, 40, 50), outline=(30, 30, 30), width=3)
    for dx, dy in [(-9, -9), (9, -9), (-9, 9), (9, 9), (0, 0)]:
        d.ellipse([560 + dx - 3, 230 + dy - 3, 560 + dx + 3, 230 + dy + 3], fill=(255, 255, 255))


MOTIFS = {"cartes": motif_cartes, "coco": motif_coco, "parcours": motif_parcours, "table": motif_table}


def retour_ligne(texte, police, largeur_max):
    lignes = []
    for paragraphe in texte.split("\n"):
        mots, ligne = paragraphe.split(), ""
        for mot in mots:
            essai = f"{ligne} {mot}".strip()
            if police.getlength(essai) <= largeur_max:
                ligne = essai
            else:
                if ligne:
                    lignes.append(ligne)
                ligne = mot
        if ligne:
            lignes.append(ligne)
    return lignes


def rendre(config):
    haut, bas = couleur(config["couleurs"][0]), couleur(config["couleurs"][1])
    accent = couleur(config["accent"])
    img = fond(haut, bas)
    d = ImageDraw.Draw(img)
    MOTIFS[config["motif"]](d, accent)
    titre_police = ImageFont.truetype(POLICE_GRASSE, 46)
    sous_police = ImageFont.truetype(POLICE, 22)
    y = 50
    for ligne in retour_ligne(config["titre"], titre_police, 320):
        d.text((40, y), ligne, font=titre_police, fill=(255, 255, 255))
        y += 52
    y += 12
    for ligne in retour_ligne(config["sous_titre"], sous_police, 320):
        d.text((40, y), ligne, font=sous_police, fill=(245, 240, 225))
        y += 28
    return img


def main(noms):
    dossier = RACINE / "vignettes"
    jeux = sorted(p.stem for p in dossier.glob("*.json"))
    cibles = noms or jeux
    for nom in cibles:
        config = json.loads((dossier / f"{nom}.json").read_text(encoding="utf-8"))
        sortie = RACINE / "jeux" / nom / "assets" / "cover.png"
        sortie.parent.mkdir(parents=True, exist_ok=True)
        rendre(config).save(sortie, optimize=True)
        print(f"ok jeux/{nom}/assets/cover.png ({sortie.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main(sys.argv[1:])

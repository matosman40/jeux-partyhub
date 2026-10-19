#!/usr/bin/env python3
"""Synthétise les sons de PartyHub qui n'ont pas de source libre : huit bruitages et trois musiques.

Aucun fichier source n'est utilisé : tous les sons sont calculés ici. Ils sont donc reproductibles et sous licence CC0 1.0 (domaine public). Les six bruitages issus du pack Kenney (CC0) ne sont pas produits par ce script.

Usage, depuis la racine du dépôt :
    python3 sons/outils/synthese.py

Écrit sons/sfx/sfx-<nom>.ogg et sons/musique/musique-<nom>.ogg. Dépend de numpy, et de ffmpeg pour l'encodage OGG.
"""

import argparse
import os
import subprocess
import tempfile
import wave

import numpy as np

SR = 44100
PEAK_DB = -3.0  # pic cible : marge sous −1 dBFS, pour l'encodage OGG
RNG = np.random.default_rng(20261019)  # graine fixe : le même script donne toujours les mêmes sons


# --- briques de base -------------------------------------------------------------------------------------------


def tt(n):
    return np.arange(n) / SR


def midi(n):
    return 440.0 * 2.0 ** ((n - 69) / 12.0)


def noise(n):
    return RNG.uniform(-1.0, 1.0, n)


def decay(n, tau, attack=0.003):
    t = tt(n)
    env = np.exp(-t / tau)
    if attack > 0:
        env = env * np.minimum(1.0, t / attack)
    return env


def tone(freq, n, kind="sine"):
    phase = 2 * np.pi * freq * tt(n)
    if kind == "tri":
        return 2 / np.pi * np.arcsin(np.sin(phase))
    if kind == "square":
        return np.sign(np.sin(phase))
    return np.sin(phase)


def saw(freq, n):
    """Dent de scie limitée en bande (somme d'harmoniques), pour un son de cuivre sans crissement."""
    t = tt(n)
    out = np.zeros(n)
    for k in range(1, max(1, min(40, int(9000 / freq))) + 1):
        out += np.sin(2 * np.pi * freq * k * t) / k
    return out


def sweep(f0, f1, n):
    """Glissando exponentiel de f0 vers f1 sur n échantillons."""
    t = tt(n)
    dur = max(n / SR, 1e-9)
    freq = f0 * (f1 / f0) ** (t / dur)
    return np.sin(2 * np.pi * np.cumsum(freq) / SR)


def band(x, lo, hi):
    """Filtre passe-bande par FFT (adapté aux bruitages courts)."""
    n = len(x)
    freqs = np.fft.rfftfreq(n, 1 / SR)
    mask = (freqs >= lo) & (freqs <= hi)
    return np.fft.irfft(np.fft.rfft(x) * mask, n)


class Buffer:
    """Piste de mixage. wrap=True enroule les débordements au début : une boucle reste continue."""

    def __init__(self, seconds):
        self.x = np.zeros(int(round(seconds * SR)))

    def add(self, sig, at=0.0, gain=1.0, wrap=False):
        start = int(round(at * SR))
        if wrap:
            idx = (np.arange(len(sig)) + start) % len(self.x)
            np.add.at(self.x, idx, gain * sig)
            return
        end = min(len(self.x), start + len(sig))
        if start < len(self.x) and end > start:
            self.x[start:end] += gain * sig[: end - start]


def finish(x, fade_out=0.01):
    x = x.copy()
    n_fade = min(len(x), int(fade_out * SR))
    if n_fade:
        x[len(x) - n_fade :] *= np.linspace(1.0, 0.0, n_fade)
    peak = np.max(np.abs(x))
    if peak == 0:
        return x
    return x * (10 ** (PEAK_DB / 20) / peak)


def brass(m, dur, tau):
    n = int(dur * SR)
    env = np.minimum(1.0, tt(n) / 0.03) * np.exp(-tt(n) / tau)
    return saw(midi(m), n) * env * 0.35


def bell(m, dur, tau):
    n = int(dur * SR)
    f = midi(m)
    body = tone(f, n, "tri") + 0.3 * tone(2 * f, n) + 0.1 * tone(3 * f, n)
    return body * decay(n, tau, 0.006)


# --- bruitages ---------------------------------------------------------------------------------------------------


def sfx_explode():
    b = Buffer(1.5)
    n = int(1.5 * SR)
    b.add(sweep(110, 35, n) * decay(n, 0.45, 0.004))
    b.add(band(noise(n), 300, 6000) * decay(n, 0.25, 0.002), gain=0.3)  # craquements
    b.add(band(noise(n), 40, 260) * decay(n, 0.6, 0.02), gain=0.6)  # grondement
    return finish(b.x, 0.02)


def sfx_crate():
    b = Buffer(0.9)
    n = int(0.06 * SR)
    b.add(band(noise(n), 1200, 7000) * decay(n, 0.02, 0.001))  # claquement initial
    for at, f in [(0.03, 900), (0.09, 620), (0.16, 1100), (0.27, 760)]:  # éclats
        m = int(0.05 * SR)
        b.add(tone(f, m) * decay(m, 0.012, 0.001), at, 0.4)
    m = int(0.5 * SR)
    b.add(sweep(140, 60, m) * decay(m, 0.12, 0.003), 0.05, 0.8)  # choc sourd
    m = int(0.6 * SR)
    b.add(band(noise(m), 300, 4000) * decay(m, 0.18, 0.002), 0.1, 0.5)  # fracas
    return finish(b.x)


def sfx_die():
    b = Buffer(1.2)
    n = int(0.95 * SR)
    t = tt(n)
    freq = 880 * (0.23) ** (t / 0.95)  # glissando descendant, comique
    wobble = 1 + 0.035 * np.sin(2 * np.pi * 6 * t)  # léger vibrato triste
    phase = 2 * np.pi * np.cumsum(freq * wobble) / SR
    whistle = np.sin(phase) * np.minimum(1.0, t / 0.02) * (1 - 0.6 * t / 0.95)
    b.add(whistle, 0.0, 0.7)
    m = int(0.2 * SR)
    b.add(sweep(300, 150, m) * decay(m, 0.05, 0.002), 0.98, 0.8)  # petit « plouf » final
    return finish(b.x)


def sfx_win():
    b = Buffer(2.0)
    for m, at in [(72, 0.0), (76, 0.2), (79, 0.4)]:
        b.add(brass(m, 0.25, 0.4), at)
    for m in (72, 76, 79, 84):  # accord final tenu
        b.add(brass(m, 1.4, 0.9), 0.6, 0.7)
    return finish(b.x)


def sfx_start():
    b = Buffer(1.5)
    for m, at in [(72, 0.0), (76, 0.25), (79, 0.5)]:
        b.add(brass(m, 0.3, 0.3), at)
    for m in (84, 88, 91):  # accord aigu de départ
        b.add(brass(m, 0.75, 0.7), 0.75, 0.7)
    return finish(b.x)


def sfx_final():
    b = Buffer(3.0)
    m = int(1.6 * SR)
    b.add(band(noise(m), 3000, 12000) * decay(m, 0.9, 0.002), 0.0, 0.4)  # cymbale
    for m_note in (60, 64, 67, 72):  # accord majeur
        b.add(brass(m_note, 2.8, 2.2), 0.0, 0.5)
    for m_note, at in [(72, 1.0), (76, 1.3), (79, 1.6), (84, 1.9)]:  # fin mélodique
        b.add(brass(m_note, 0.35, 0.5), at, 0.8)
    return finish(b.x)


def sfx_card():
    b = Buffer(0.4)
    m = int(0.05 * SR)
    b.add(band(noise(m), 1500, 9000) * decay(m, 0.012, 0.001), 0.0, 0.9)  # claquement de carte
    m = int(0.2 * SR)
    b.add(sweep(200, 90, m) * decay(m, 0.05, 0.002), 0.0, 0.5)  # petit choc sourd
    return finish(b.x)


def sfx_chip():
    b = Buffer(0.9)
    for at in [0.0, 0.07, 0.15, 0.22, 0.36, 0.44, 0.6, 0.67]:
        m = int(0.03 * SR)
        gain = 0.5 + 0.5 * RNG.uniform()
        b.add(band(noise(m), 2000, 7000) * decay(m, 0.006, 0.001), at, gain)
    return finish(b.x)


# --- musiques de fond --------------------------------------------------------------------------------------------


def musique_accueil():
    """30 s à 128 BPM, boucle parfaite : 16 mesures, progression Do - La mineur - Fa - Sol."""
    beat = 60 / 128
    b = Buffer(64 * beat)  # 64 temps = 30 s
    chords = [(60, 64, 67), (57, 60, 64), (53, 57, 60), (55, 59, 62)]
    pattern = [0, 2, 1, 2]
    for bar in range(16):
        chord = chords[bar // 4]
        t0 = bar * 4 * beat
        n_bass = int(0.22 * SR)
        for e in range(8):  # basse en croches
            b.add(tone(midi(chord[0] - 12), n_bass, "tri") * decay(n_bass, 0.12, 0.004), t0 + e * beat / 2, 0.5, True)
        n_lead = int(0.4 * SR)
        for q in range(4):  # mélodie en noires
            note = chord[pattern[q]] + 12
            b.add(tone(midi(note), n_lead, "square") * decay(n_lead, 0.16, 0.005), t0 + q * beat, 0.12, True)
        for q in range(4):  # grosse caisse sur chaque temps
            n_kick = int(0.18 * SR)
            b.add(sweep(120, 45, n_kick) * decay(n_kick, 0.06, 0.001), t0 + q * beat, 0.9, True)
        for e in range(4):  # charleston à contretemps
            n_hat = int(0.05 * SR)
            b.add(band(noise(n_hat), 6000, 15000) * decay(n_hat, 0.012, 0.001), t0 + e * beat + beat / 2, 0.2, True)
    return finish(b.x, 0.0)


def musique_menus():
    """60 s à 80 BPM, boucle parfaite : piano électrique doux et batterie légère."""
    beat = 60 / 80
    b = Buffer(80 * beat)  # 80 temps = 60 s
    chords = [(60, 64, 67, 71), (57, 60, 64, 67), (53, 57, 60, 64), (55, 59, 62, 65)]  # Cmaj7 Am7 Fmaj7 G7
    for bar in range(20):
        chord = chords[bar // 5]
        t0 = bar * 4 * beat
        for s in range(2):  # accord frappé toutes les deux noires
            at = t0 + s * 2 * beat
            n = int(1.6 * SR)
            for m in chord:
                f = midi(m)
                piano = tone(f, n) + 0.35 * tone(2 * f, n) + 0.12 * tone(3 * f, n)
                b.add(piano * decay(n, 0.7, 0.004), at, 0.09, True)
        for q in (0, 2):  # grosse caisse douce sur les temps 1 et 3
            n_kick = int(0.25 * SR)
            b.add(sweep(90, 40, n_kick) * decay(n_kick, 0.09, 0.002), t0 + q * beat, 0.5, True)
        for q in (1, 3):  # claquement léger sur les temps 2 et 4
            n_rim = int(0.03 * SR)
            b.add(band(noise(n_rim), 1500, 5000) * decay(n_rim, 0.01, 0.001), t0 + q * beat, 0.25, True)
    return finish(b.x, 0.0)


def musique_fin():
    """15 s, sans boucle : fanfare légère qui se termine sur un accord."""
    b = Buffer(15.0)
    for m, at in [(72, 0.0), (76, 0.4), (79, 0.8), (84, 1.2)]:
        b.add(bell(m, 0.6, 0.35), at, 0.5)
    for m in (60, 64, 67, 72):
        b.add(bell(m, 6.0, 3.0), 1.6, 0.25)
    return finish(b.x, 1.5)


# --- écriture ----------------------------------------------------------------------------------------------------

SFX = {
    "explode": sfx_explode,
    "crate": sfx_crate,
    "die": sfx_die,
    "win": sfx_win,
    "start": sfx_start,
    "final": sfx_final,
    "card": sfx_card,
    "chip": sfx_chip,
}
MUSIQUE = {
    "accueil": musique_accueil,
    "menus": musique_menus,
    "fin": musique_fin,
}


def ecrire_wav(chemin, x):
    pcm = (np.clip(x, -1.0, 1.0) * 32767).astype("<i2")
    with wave.open(chemin, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def encoder_ogg(wav, ogg):
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-y", "-i", wav, "-c:a", "libvorbis", "-q:a", "5", ogg],
        check=True,
        stdin=subprocess.DEVNULL,
    )


def main():
    racine = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--sortie", default=racine, help="dossier sons/ de destination")
    args = parser.parse_args()

    travaux = [
        (os.path.join(args.sortie, "sfx"), f"sfx-{nom}", fn) for nom, fn in SFX.items()
    ] + [
        (os.path.join(args.sortie, "musique"), f"musique-{nom}", fn) for nom, fn in MUSIQUE.items()
    ]
    with tempfile.TemporaryDirectory() as tmp:
        for dossier, base, fn in travaux:
            os.makedirs(dossier, exist_ok=True)
            wav = os.path.join(tmp, base + ".wav")
            ecrire_wav(wav, fn())
            encoder_ogg(wav, os.path.join(dossier, base + ".ogg"))
            print(f"ok {os.path.relpath(os.path.join(dossier, base + '.ogg'))}")


if __name__ == "__main__":
    main()

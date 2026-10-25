import type { Stroke } from '../module.js';
import { DRAWING_SIZE } from '../info.js';

/** Épaisseur du trait, sur la grille de 0 à 1000 (même échelle que les points du dessin). */
const INK_WIDTH = 14;

/**
 * Dessin en lecture seule : les traits, sur une feuille claire. Les couleurs et épaisseurs sont données
 * en attributs SVG (et non par une feuille de style) : la vue du jeu n’en charge aucune.
 */
export function Drawing({ strokes, label = 'Dessin' }: { strokes: Stroke[] | null; label?: string }) {
  return (
    <svg
      viewBox={`0 0 ${DRAWING_SIZE} ${DRAWING_SIZE}`}
      role="img"
      aria-label={label}
      style={{ display: 'block', width: '100%', height: 'auto', maxWidth: 480, margin: '0 auto' }}
    >
      <rect width={DRAWING_SIZE} height={DRAWING_SIZE} fill="#ffffff" stroke="#111111" strokeWidth={6} />
      {(strokes ?? []).map((stroke, i) =>
        stroke.length === 1 ? (
          <circle key={i} cx={stroke[0]![0]} cy={stroke[0]![1]} r={INK_WIDTH / 2} fill="#111111" />
        ) : (
          <polyline
            key={i}
            points={stroke.map(([x, y]) => `${x},${y}`).join(' ')}
            fill="none"
            stroke="#111111"
            strokeWidth={INK_WIDTH}
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        ),
      )}
    </svg>
  );
}

#!/usr/bin/env python3
"""Coincidence-odds calc for the letter <-> gang-member matches.

QUESTION TESTED: S16 (do the gang matches mean anything?) and the dev/name-initials
counter-argument in analysis/connections.md. We observed that 2 of the 5 markings
(`SM`, `J+M`) exactly equal a Van der Linde gang member's two name-initials. This asks:
HOW SURPRISING IS THAT UNDER CHANCE? See threads/03 & 07, findings/speculation.md.

WHAT THIS DOES (and does NOT do):
- Estimates P(>=2 of 5 random letter-pairs coincide with an "occupied" gang initial-pair)
  under two null models: (A) letters uniform over A-Z, (B) letters drawn by the gang's own
  initial-frequency (realistic, since name initials cluster on J/S/M...).
- It quantifies only the BARE-EXISTENCE surprise. It CANNOT model the real claim in S16 --
  that the hits are *major* characters (Sean, John) -- so a small p here would still not
  "prove" S16, and a large p actively weakens it. Result is evidence, not fact.

INPUT PROVENANCE:
- Gang initial-pairs: from thread 07 (Red Dead Wiki B / in-game A). First+last initials.
- Markings: KNOWN [K6][K9].
- Null models are assumptions, labelled as such. Deterministic: fixed SEED, printed.

Run: `python experiments/initials_likelihood.py`   (Python 3, standard library only)
"""

import random
from math import comb
from collections import Counter

SEED = 20260613
TRIALS = 200_000

# Markings as unordered letter-pairs -- KNOWN [K6][K9].
MARKINGS = {"LJ": ("L", "J"), "SM": ("S", "M"), "EC": ("E", "C"),
            "J+M": ("J", "M"), "S+J": ("S", "J")}

# Gang members' (first, last) initials -- thread 07. (Uncle/Annabelle: no pair, omitted.)
GANG_PAIRS = [
    ("D", "V"), ("H", "M"), ("A", "M"), ("J", "M"), ("B", "W"), ("J", "E"),
    ("M", "B"), ("C", "S"), ("S", "M"), ("L", "S"), ("S", "A"), ("A", "R"),
    ("J", "M"), ("M", "O"), ("M", "G"), ("T", "J"), ("K", "J"), ("S", "G"),
    ("S", "P"), ("O", "S"), ("L", "S"), ("J", "T"), ("K", "D"), ("J", "K"),
    ("D", "C"), ("M", "C"),
]

ALPHABET = [chr(c) for c in range(ord("A"), ord("Z") + 1)]


def occupied_set(pairs):
    """Distinct unordered initial-pairs (distinct-letter only)."""
    return {frozenset(p) for p in pairs if p[0] != p[1]}


def freq_weights(pairs):
    """Empirical letter frequency across all gang initials (for null B)."""
    c = Counter(l for p in pairs for l in p)
    letters = list(c)
    weights = [c[l] for l in letters]
    return letters, weights


def random_distinct_pair(letters=None, weights=None):
    if letters is None:                      # uniform over A-Z
        a, b = random.sample(ALPHABET, 2)
    else:                                    # frequency-weighted; redraw if equal
        a = random.choices(letters, weights=weights, k=1)[0]
        b = a
        while b == a:
            b = random.choices(letters, weights=weights, k=1)[0]
    return frozenset((a, b))


def mc_prob_ge2(occupied, letters=None, weights=None):
    hits_hist = Counter()
    for _ in range(TRIALS):
        h = sum(1 for _ in range(5)
                if random_distinct_pair(letters, weights) in occupied)
        hits_hist[h] += 1
    p_ge2 = sum(n for k, n in hits_hist.items() if k >= 2) / TRIALS
    exp = sum(k * n for k, n in hits_hist.items()) / TRIALS
    return p_ge2, exp


def main():
    random.seed(SEED)
    occ = occupied_set(GANG_PAIRS)
    observed = [name for name, pair in MARKINGS.items() if frozenset(pair) in occ]

    print("Coincidence-odds: letter-pairs vs gang initial-pairs")
    print("=" * 64)
    print(f"Seed {SEED}, {TRIALS:,} trials per null model.")
    print(f"Distinct gang initial-pairs (occupied): {len(occ)} of {comb(26,2)} possible")
    print(f"OBSERVED: {len(observed)} of 5 markings hit a gang pair -> {observed}")
    print()

    # --- Null A: uniform letters -------------------------------------------------
    p = len(occ) / comb(26, 2)
    binom_ge2 = 1 - (1 - p) ** 5 - comb(5, 1) * p * (1 - p) ** 4
    pa, ea = mc_prob_ge2(occ)
    print("NULL A -- markings = random pairs, letters UNIFORM over A-Z")
    print("-" * 64)
    print(f"  per-pair hit prob p = {p:.4f};  analytic P(>=2 of 5) = {binom_ge2:.3f}")
    print(f"  Monte-Carlo: E[hits] = {ea:.3f},  P(>=2) = {pa:.3f}")
    print()

    # --- Null B: frequency-weighted ----------------------------------------------
    letters, weights = freq_weights(GANG_PAIRS)
    pb, eb = mc_prob_ge2(occ, letters, weights)
    print("NULL B -- letters drawn by the GANG's own initial-frequency (realistic:")
    print("          name initials cluster on J/S/M, which the markings happen to use)")
    print("-" * 64)
    print(f"  Monte-Carlo: E[hits] = {eb:.3f},  P(>=2) = {pb:.3f}")
    print()

    print("INTERPRETATION (evidence, not fact)")
    print("-" * 64)
    print(f"  * Under UNIFORM letters, 2 hits is mildly surprising (P~={pa:.2f}).")
    print(f"  * But the markings use COMMON name-initials (J x3, S, M); under the")
    print(f"    frequency-aware null the same 2 hits is much LESS surprising (P~={pb:.2f}).")
    print( "  * So the COUNT (2 of 5) is weak evidence for S16 -- largely a by-product")
    print( "    of the letters being high-frequency initials. S16's real weight rests on")
    print( "    the UNMODELLED claim that the hits are MAJOR characters (Sean, John) at")
    print( "    markings already tied to nodes -- which this calc cannot score.")
    print( "  * Net: treat S16 as SUGGESTIVE-AT-BEST; do not upgrade it on the match count.")


if __name__ == "__main__":
    main()

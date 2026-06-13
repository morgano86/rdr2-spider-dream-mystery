#!/usr/bin/env python3
"""Feather / web shooting-order constraint solver.

QUESTION TESTED: U0 (feather position/orientation = the order key?) and H4, against the
documented order constraint K13b. See findings/unknowns.md, findings/speculation.md, INDEX.md.

WHAT THIS DOES (and does NOT do):
- It enumerates the search space of possible shooting orders for the 8 feathered webs and
  filters it by the ONE ordering fact we actually have: the non-respawn chain
  B23 -> B45 -> B56 -> BL56 (with B56 / BL56 interchangeable) [K13b].
- It reports how many orderings survive, so we know how much a future feather-orientation
  capture (U0) would still have to disambiguate.
- It is a TEST, not a finding. Nothing it prints is [KNOWN]. A surviving ordering is at most
  a [SPECULATION] candidate until corroborated in-game or by a source.

INPUT PROVENANCE:
- Web list, colours, codes, the non-respawn chain: KNOWN, from images/webs/WEBS-MANIFEST.md
  (primary wiki + community research site). No invented data.
- Feather ORIENTATION per web: still UNKNOWN (U0). When captured, encode it as a partial or
  full order in HYPOTHESISED_ORDER below and re-run to collapse the candidate set.

Run: `python experiments/feather_order.py`   (Python 3, standard library only)
"""

from itertools import permutations

# (code, location, colour) — KNOWN, from WEBS-MANIFEST.md
WEBS = [
    ("B34",  "Cornwall (start/index pole)", "black"),
    ("B56",  "Oil Fields",                  "black"),
    ("B23",  "Overflow",                    "black"),
    ("B45",  "Emerald",                     "black"),
    ("BL56", "Ringneck",                    "black"),
    ("R34",  "Saint Denis",                 "red"),
    ("R45",  "Southfield",                  "red"),
    ("R23",  "Scarlett",                    "red"),
]
CODES = [w[0] for w in WEBS]

# KNOWN ordering constraint [K13b]: a non-respawn chain exists.
# B23 before B45 before {B56, BL56}; B56 and BL56 are interchangeable (either may come first).
ORDERED_PREFIX = ["B23", "B45"]          # these must appear in this relative order...
INTERCHANGEABLE_TAIL = {"B56", "BL56"}   # ...followed by both of these, in any order.

# OPTIONAL: once feather orientation (U0) is captured, list the implied order here (full or
# partial, by code) to filter further. Leave empty to just measure the constraint above.
HYPOTHESISED_ORDER = []  # e.g. ["B34", "B23", "B45", ...]


def satisfies_chain(order):
    """True if `order` (a tuple of codes) respects the documented non-respawn chain."""
    pos = {code: i for i, code in enumerate(order)}
    # B23 < B45 < each of the interchangeable tail
    if not (pos["B23"] < pos["B45"]):
        return False
    return all(pos["B45"] < pos[t] for t in INTERCHANGEABLE_TAIL)


def satisfies_hypothesis(order):
    """True if `order` is consistent with HYPOTHESISED_ORDER as a subsequence (if given)."""
    if not HYPOTHESISED_ORDER:
        return True
    it = iter(order)
    return all(code in it for code in HYPOTHESISED_ORDER)


def main():
    total = 0
    chain_ok = 0
    survivors = []
    for perm in permutations(CODES):
        total += 1
        if not satisfies_chain(perm):
            continue
        chain_ok += 1
        if satisfies_hypothesis(perm):
            survivors.append(perm)

    print("Feather / web shooting-order constraint solver")
    print("=" * 60)
    print(f"Webs (8): {', '.join(CODES)}")
    print(f"Total orderings (8!):                 {total:>7,}")
    print(f"Consistent with non-respawn chain:    {chain_ok:>7,}  [K13b]")
    if HYPOTHESISED_ORDER:
        print(f"...and with HYPOTHESISED_ORDER:        {len(survivors):>7,}  (U0 capture)")
    print()
    print("Interpretation: capturing feather ORIENTATION (U0) is what would collapse the")
    print(f"{chain_ok:,} chain-consistent candidates toward a single order. Until then, no")
    print("ordering here is more than a [SPECULATION] candidate.")
    print()
    print("First 5 chain-consistent candidates (illustrative only, NOT findings):")
    for cand in survivors[:5]:
        print("  " + " -> ".join(cand))


if __name__ == "__main__":
    main()

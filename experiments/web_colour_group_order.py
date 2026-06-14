#!/usr/bin/env python3
"""Colour x hour lattice + the colour-GROUP shooting order  (tests U29/H9/H18, deflates H4/H17)

QUESTION TESTED:
  1. Is there a clean COLOUR x HOUR structure in the 8 webs that the corpus has not stated
     explicitly?  (a re-tabulation of [K13a] -- KNOWN data, new view)
  2. Given the documented (C-tier) non-respawn ruleset [U29], how big is the surviving
     shooting-order space, and is the COLOUR-GROUP reading -- the one the Window Rock mural,
     read as a mechanic 'seed' [H18], points at -- consistent with it?

WHY THIS MATTERS:
  - The "secret single feather-encoded sequence" reading is doubly dead: orientation is uniform
    (tip-down -> [H4] refuted) and several orders work within a colour group ([U29] -> [H17]
    refuted). What survives is a GROUP/boundary mechanic ([H9]). This script makes the group
    reading concrete and checks it against the reset rules.
  - The Window Rock "Strange Statues" mural [K18] is solved by COUNTING a per-bird feature
    (tail feathers) while EXCLUDING decoys (upside-down birds). Read as a shipped 'seed' for
    the web puzzle ([H18], the same precedent-argument family as the Vampire [H15] / the
    Dreamcatchers [H6]), its transferable lesson is that appearance is a per-element FILTER
    (which to ignore), NOT a heading. The web feathers are uniform in orientation, so the only
    binary filter left is COLOUR -- which is exactly what [H9]/[U29] independently show.

WHAT THIS DOES (and does NOT do):
  - Prints the colour x hour lattice from KNOWN data and verifies the pairing structure.
  - Enumerates all 8! shooting orders and filters by a CONSERVATIVE encoding of the [U29]
    reset rules, reporting how many survive.
  - Checks whether the colour-group candidate order(s) are in the survivor set.
  - It is a TEST, not a finding. The reset rules are C-tier community brute-force data; a
    surviving order is at most [SPECULATION]. A surviving candidate does NOT confirm [H18];
    it only shows the group reading is *consistent* with the reset data.

INPUT PROVENANCE:
  - Web list / colours / codes / hours: KNOWN, images/webs/WEBS-MANIFEST.md ([K13a], primary
    wiki + community research site). No invented data.
  - Reset ruleset: [U29]/[K13b] -- community brute-force testing (#36, Google Sites timeline),
    C-tier. Each rule is tagged PROVISIONAL inline.
  - Mural mechanic: [K18] (wiki, solved POI). The seed-transfer is [H18] (SPECULATION).

Run: `python experiments/web_colour_group_order.py`   (Python 3, standard library only)
"""

from itertools import permutations

# (code, location, colour, hour_start) -- KNOWN from WEBS-MANIFEST.md [K13a].
WEBS = [
    ("B23",  "Overflow",                    "black", 2),
    ("B34",  "Cornwall (start/index pole)", "black", 3),
    ("B45",  "Emerald",                     "black", 4),
    ("B56",  "Oil Fields",                  "black", 5),
    ("BL56", "Ringneck",                    "black", 5),
    ("R23",  "Scarlett",                    "red",   2),
    ("R34",  "Saint Denis",                 "red",   3),
    ("R45",  "Southfield",                  "red",   4),
]
CODES  = [w[0] for w in WEBS]
COLOUR = {w[0]: w[2] for w in WEBS}
HOUR   = {w[0]: w[3] for w in WEBS}
LOC    = {w[0]: w[1] for w in WEBS}

REDS   = [c for c in CODES if COLOUR[c] == "red"]
BLACKS = [c for c in CODES if COLOUR[c] == "black"]

# Connector non-respawn chain [K13b]: B23 -> B45 -> B56 -> BL56 (B56/BL56 interchangeable).
CONNECTOR_CHAIN = ["B23", "B45", "B56", "BL56"]


# --------------------------------------------------------------------------------------
# Part 1 -- the colour x hour lattice (KNOWN re-tabulation of [K13a])
# --------------------------------------------------------------------------------------
def lattice():
    print("1. Colour x hour lattice  (KNOWN, re-tabulated from [K13a])")
    print("-" * 64)
    hours = sorted({HOUR[c] for c in CODES})
    print(f"    {'hour':8s} {'black':28s} {'red'}")
    pairing_ok = True
    for h in hours:
        b = [c for c in BLACKS if HOUR[c] == h]
        r = [c for c in REDS   if HOUR[c] == h]
        bs = ", ".join(f"{c}({LOC[c]})" for c in b) or "-"
        rs = ", ".join(f"{c}({LOC[c]})" for c in r) or "-"
        print(f"    {h}-{h+1} AM   {bs:28s} {rs}")
        # The claimed structure: each hour 2/3/4 has exactly 1 black + 1 red; hour 5 has 2 blacks, 0 red.
        if h in (2, 3, 4) and not (len(b) == 1 and len(r) == 1):
            pairing_ok = False
        if h == 5 and not (len(b) == 2 and len(r) == 0):
            pairing_ok = False
    print()
    print("    Centre cluster (no feather) appears 1-2 AM, spells 'N' + pole [K11].")
    print(f"    Structure holds (2/3/4 AM = 1 black + 1 red each; 5-6 AM = 2 blacks, 0 red)?  {pairing_ok}")
    print("    -> Each red is hour-TWINNED to a black:")
    for h in (2, 3, 4):
        b = [c for c in BLACKS if HOUR[c] == h][0]
        r = [c for c in REDS   if HOUR[c] == h][0]
        print(f"         {h}-{h+1}: {b}({LOC[b]})  <->  {r}({LOC[r]})")
    print("    -> The 2 UNTWINNED blacks are B56/BL56 (both 5-6 AM) -- exactly the [K13b]")
    print("       'interchangeable' pair. The hour-collision IS why they're interchangeable.")
    print("    NOTE: the pairing is KNOWN; reading it as DELIBERATE is [SPECULATION].")
    return pairing_ok


# --------------------------------------------------------------------------------------
# Part 2 -- conservative [U29] reset-rule constraints on a full 8-feather order
# --------------------------------------------------------------------------------------
def pos(order):
    return {c: i for i, c in enumerate(order)}


def c1_connector_chain(order):
    # PROVISIONAL [K13b]: within the connector set the order must be B23 < B45 < {B56,BL56};
    # B56 and BL56 are interchangeable (no constraint between the two).
    p = pos(order)
    return p["B23"] < p["B45"] < p["B56"] and p["B23"] < p["B45"] < p["BL56"]


def c2_no_red_after_bl56(order):
    # PROVISIONAL [U29]: "choosing any red after BL56 resets" -> no red may follow BL56.
    p = pos(order)
    return all(p[r] < p["BL56"] for r in REDS)


def c3_b34_last(order):
    # PROVISIONAL [U29]: standing suspicion B34 (Cornwall index pole) is the LAST feather.
    return order[-1] == "B34"


def count(constraints):
    return sum(1 for o in permutations(CODES) if all(f(o) for f in constraints))


def part2():
    print("\n2. Surviving shooting-order space under the [U29] reset rules (PROVISIONAL, C-tier)")
    print("-" * 64)
    total = 1
    for n in range(2, len(CODES) + 1):
        total *= n
    print(f"    Total orders (8!):                                {total:>8,}")
    n1 = count([c1_connector_chain])
    print(f"    + connector chain  B23<B45<B56,BL56  [K13b]:      {n1:>8,}")
    n2 = count([c1_connector_chain, c2_no_red_after_bl56])
    print(f"    + no red after BL56                  [U29]:       {n2:>8,}")
    n3 = count([c1_connector_chain, c2_no_red_after_bl56, c3_b34_last])
    print(f"    + B34 is the LAST feather            [U29]:       {n3:>8,}")
    print("    (Reds free among themselves [U29] -> no extra constraint; already counted.)")
    return n1, n2, n3


# --------------------------------------------------------------------------------------
# Part 3 -- is the colour-GROUP reading ([H18] mural-seed: colour = the filter) consistent?
# --------------------------------------------------------------------------------------
def part3():
    print("\n3. Is the COLOUR-GROUP candidate order consistent with the reset rules? [H18]")
    print("-" * 64)
    # Mural-seed reading: shoot the reds as one free group, then the connector blacks in
    # chain order, with Cornwall (B34) distinguished as last. One representative ordering:
    candidate = ["R23", "R34", "R45", "B23", "B45", "B56", "BL56", "B34"]
    checks = {
        "connector chain [K13b]": c1_connector_chain(candidate),
        "no red after BL56 [U29]": c2_no_red_after_bl56(candidate),
        "B34 last [U29]": c3_b34_last(candidate),
    }
    print(f"    candidate:  {' -> '.join(candidate)}")
    for name, ok in checks.items():
        print(f"      {name:28s}: {ok}")
    survives = all(checks.values())
    print(f"    candidate survives all constraints?  {survives}")

    # How many of the surviving orders have ALL reds before ALL connector blacks
    # (the 'reds are a leading group' shape the mural-seed predicts)?
    survivors = [o for o in permutations(CODES)
                 if c1_connector_chain(o) and c2_no_red_after_bl56(o) and c3_b34_last(o)]
    conn = [c for c in CONNECTOR_CHAIN]
    grouped = [o for o in survivors
               if max(pos(o)[r] for r in REDS) < min(pos(o)[b] for b in conn)]
    print(f"    of {len(survivors)} survivors, {len(grouped)} put ALL reds before ALL connector"
          f" blacks (the group shape).")
    print("    -> The colour-group reading is CONSISTENT with the reset data (it is one")
    print("       sub-family of the survivors). Consistency is NOT confirmation: many other")
    print("       orders also survive, and the rules are C-tier. [SPECULATION].")


def main():
    print("Colour x hour lattice + colour-group shooting order  [U29/H9/H18]")
    print("=" * 64)
    lattice()
    part2()
    part3()
    print("\nSUMMARY (evidence, not fact)")
    print("-" * 64)
    print("  * KNOWN: hours 2/3/4 AM each carry exactly 1 black + 1 red; 5-6 AM carries 2")
    print("    blacks (B56/BL56, the interchangeable pair); 1-2 AM is the featherless centre.")
    print("    Each red is hour-twinned to a black. (Re-tabulation of [K13a].)")
    print("  * The [U29] reset rules already collapse 8! = 40,320 orders to a small survivor")
    print("    set; adding 'B34 last' shrinks it further.")
    print("  * The mural-seed colour-GROUP reading [H18] (colour = the filter, since feather")
    print("    orientation is uniform) is CONSISTENT with the survivors -- not proven by them.")
    print("  * Net: reinforces the GROUP/boundary mechanic [H9] over a feather-encoded")
    print("    sequence ([H4]/[H17] dead). [SPECULATION] pending in-game/sourced confirmation.")


if __name__ == "__main__":
    main()

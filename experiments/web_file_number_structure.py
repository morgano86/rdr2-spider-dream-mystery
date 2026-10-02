#!/usr/bin/env python3
"""Is the `spiderdream0X` -> location numbering structured (and is it even sourced)?

QUESTION TESTED: the provenance + structure of the per-web internal file numbers
(`spiderdream01`-`08`) that the WEBS-MANIFEST assigns to each of the 8 webs ([U32]).
Bears on [U29]/[S28]/[H9] (is COLOUR a deliberate first-class axis?) and on corpus
integrity (is a claim presented as file-data actually sourced?).

BACKGROUND / PROVENANCE FLAG (the reason this script exists):
- KNOWN & SOURCED: each web's COLOUR (5 black / 3 red) and HOUR, and the hour-twin
  lattice (each 2/3/4 AM hour = 1 black + 1 red; 5-6 AM = 2 blacks) -- [K13a], §5c.
- NOT cited anywhere in the corpus: the specific `spiderdreamNN` number per LOCATION
  (Cornwall=03, Ringneck=01, ...). It has sat in the WEBS-MANIFEST table since the
  first commit with no source, and it is NOT the community post's "Clockwise Order"
  (#59, which numbers Overflow=1 ... Oil Fields=8 -- a different ordering). So the
  number->location mapping is effectively UNSOURCED.

WHAT THIS DOES:
- Takes the manifest's number->location->colour/hour assignment AS GIVEN and measures
  how *structured* it is, then computes how unlikely that structure is under a uniform
  random labeling of the 8 webs with the numbers 1..8.

WHY THE ODDS MATTER (and what a LOW p means here -- read carefully):
- A genuinely arbitrary set of internal asset IDs should look random w.r.t. colour/hour.
- The manifest numbering is the opposite of random: blacks = files 1-5, reds = 6-8,
  the two untwinned 5-6 AM blacks = files 1-2, and every hour-twin pair sums to 11.
- So a LOW p is DOUBLE-EDGED, NOT a "colour is deliberate" win:
    (i)  real datamine + the devs happened to number this cleanly  -> a real intent finding;
    (ii) the numbers were BACK-FIT to the known lattice by a human (prior session or a
         community source) -> circular, no evidentiary value, a provenance problem.
  Because the mapping is uncited and (ii) explains the cleanliness at least as well as
  (i), this script CANNOT promote "colour is deliberate." Its real output is: the
  mapping is too clean to be arbitrary, so it must be SOURCED (datamine) or treated as
  an assignment. -> [U32] (open), [S29] (the conditional-IF-genuine reading).

INPUT PROVENANCE:
- webs{} below = the WEBS-MANIFEST master table (colour/hour KNOWN [K13a]; the per-web
  NUMBER is the uncited datum under test). Nothing invented.

Run: `python experiments/web_file_number_structure.py`  (Python 3, stdlib only)
Output: experiments/results/web_file_number_structure.md (+ stdout)
"""

import os
from itertools import permutations
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

# WEBS-MANIFEST master table. (file_number is the UNCITED datum under test [U32];
# code/hour/colour are KNOWN [K13a].)
WEBS = {  # location: (manifest_file_number, code, hour, colour)
    "Cornwall":    (3, "B34",  "3-4", "B"),
    "Oil Fields":  (2, "B56",  "5-6", "B"),
    "Overflow":    (5, "B23",  "2-3", "B"),
    "Emerald":     (4, "B45",  "4-5", "B"),
    "Ringneck":    (1, "BL56", "5-6", "B"),
    "Saint Denis": (8, "R34",  "3-4", "R"),
    "Southfield":  (7, "R45",  "4-5", "R"),
    "Scarlett":    (6, "R23",  "2-3", "R"),
}

# Hour-twins (same hour, opposite colour) -- from the KNOWN colour x hour lattice (§5c).
TWINS = [("B23", "R23"), ("B34", "R34"), ("B45", "R45")]
UNTWINNED_BLACKS = ["BL56", "B56"]  # the two 5-6 AM blacks with no red twin


def main():
    os.makedirs(RESULTS, exist_ok=True)
    num = {v[1]: v[0] for v in WEBS.values()}        # code -> file number
    colour = {v[1]: v[3] for v in WEBS.values()}
    codes = list(colour)
    blacks = [c for c in codes if colour[c] == "B"]

    order = sorted(WEBS.items(), key=lambda kv: kv[1][0])

    # Brute-force odds over all 8! uniform random labelings.
    N = factorial(8)
    Pa = Pab = Pabc = 0
    for perm in permutations(range(1, 9)):
        asn = dict(zip(codes, perm))
        if set(asn[c] for c in blacks) == {1, 2, 3, 4, 5}:          # blacks = 1..5
            Pa += 1
            if set(asn[c] for c in UNTWINNED_BLACKS) == {1, 2}:     # untwinned at 1,2
                Pab += 1
                if all(asn[x] + asn[y] == 11 for x, y in TWINS):    # twins sum 11
                    Pabc += 1

    L = []
    w = L.append
    w("# Result - web file-number structure & provenance (`web_file_number_structure.py`)")
    w("")
    w("**Question.** Is the WEBS-MANIFEST's per-web `spiderdreamNN` numbering (a) sourced, and")
    w("(b) structured w.r.t. the KNOWN colour/hour lattice? Tests **[U32]** (provenance) and feeds")
    w("**[S29]** (the conditional reading). [SPECULATION] at most - see the double-edged note.")
    w("")
    w("> ⚠️ **Provenance flag.** The number→location mapping is **uncited** in the corpus (present")
    w("> since the first commit; no source maps a number to a location) and is **not** the #59 post's")
    w("> *Clockwise Order*. Colour/hour are KNOWN ([K13a]); the per-web NUMBER is the datum under test.")
    w("")
    w("## The manifest numbering (ascending)")
    w("")
    w("| file # | location | code | hour | colour |")
    w("|-------:|----------|------|------|--------|")
    for loc, (n, code, hr, col) in order:
        w(f"| {n} | {loc} | {code} | {hr} | {'black' if col=='B' else 'RED'} |")
    w("")
    w("## Structure observed")
    w("")
    w(f"- **Colour-grouped:** files **1–5 = all 5 blacks**, **6–8 = all 3 reds**.")
    w(f"- **Untwinned 5–6 AM black pair** (BL56/B56) = files **{sorted(num[c] for c in UNTWINNED_BLACKS)}**.")
    w(f"- **Hour-twin pairs sum to 11** (mirror around the 1–8 line):")
    for b, r in TWINS:
        w(f"  - {b}(#{num[b]}) ↔ {r}(#{num[r]}) → sum **{num[b]+num[r]}**")
    w("")
    w("## Coincidence odds (uniform random labeling of 8 webs → 1..8)")
    w("")
    w(f"- P(blacks = files 1–5) = {Pa}/{N} = **1/{N//Pa}** ≈ {Pa/N:.4f}  *(= 1/C(8,5) = 1/{comb(8,5)})*")
    w(f"- P(+ untwinned blacks at 1–2) = {Pab}/{N} = **1/{N//Pab}** ≈ {Pab/N:.5f}")
    w(f"- P(+ all 3 hour-twins sum to 11) **[full structure]** = {Pabc}/{N} = **1/{N//Pabc}** ≈ {Pabc/N:.6f}")
    w("")
    w("## Reading (evidence, not fact - [SPECULATION])")
    w("")
    w("The full structure is **1/3360** (~0.03%) under random labeling - **far too clean for**")
    w("**arbitrary internal asset IDs.** That cleanliness is *double-edged*:")
    w("")
    w("- **(i) genuine datamine + deliberate dev numbering** → a real, striking intent finding")
    w("  (the devs grouped the files by colour and mirror-paired the hour-twins), independently")
    w("  corroborating that **colour is a first-class axis** ([H9]/[U29]/[S28]) and that the §5c")
    w("  hour-twin lattice is **deliberate** (currently [SPECULATION]).")
    w("- **(ii) the numbers were back-fit to the KNOWN lattice** by a prior session or a community")
    w("  source → the structure is *circular* (it just re-expresses colour+hour, which we already")
    w("  know) and carries **no** independent evidentiary weight.")
    w("")
    w("Because the mapping is **uncited** and (ii) explains the cleanliness at least as well as (i),")
    w("this **cannot promote** the colour-axis reading. Its real result is a **corpus-integrity flag**:")
    w("a datum presented with file-data authority (and propagated into location dossiers) is too")
    w("structured to be arbitrary and has no citation → **source the datamine number→location mapping,**")
    w("**or mark the numbers as an assignment.** → [U32]; the IF-genuine reading is held at [S29].")

    path = os.path.join(RESULTS, "web_file_number_structure.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    # stdout
    print("Web file-number structure & provenance")
    print("=" * 60)
    for loc, (n, code, hr, col) in order:
        print(f"  {n}  {loc:11} {code:4} {hr:4} {'black' if col=='B' else 'RED'}")
    print()
    print(f"P(blacks = files 1-5)              = 1/{N//Pa}  ({Pa/N:.4f})")
    print(f"P(+ untwinned blacks at 1,2)       = 1/{N//Pab}  ({Pab/N:.5f})")
    print(f"P(+ hour-twins sum to 11) [FULL]   = 1/{N//Pabc}  ({Pabc/N:.6f})")
    print()
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

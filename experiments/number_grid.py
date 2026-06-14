#!/usr/bin/env python3
"""Numerical pairing + grid-reference test for the letter markings.

QUESTION TESTED: U5 / U25 / U26 / S2 / S18 / S21 / K25 / K26 / H14 -- if the markings are a
numeric code or MAP GRID / COORDINATE REFERENCES (a column/lat letter + a row/long number)
rather than names. Prompted by the investigator's point that RDR2 has a map grid labelled
A1/B1/A2... (2026-06-13); the follow-up reading (2026-06-13, S21) that the matchsticks are
numbers where the displayed PUNCTUATION sets the operator: '+' pairs ADD (J+M=10+13=23,
S+J=19+10=29), bare pairs CONCATENATE (EC=5,3="53") -> {53,23,29} or "532329"; AND the
precedent (2026-06-13, K25) that RDR2 *does* hide letter+number coordinates -- the
loading-screen photos encode locations as obfuscated lat/long where LETTERS=latitude,
NUMBERS=longitude (H14: read our letters as lat, the S21 numbers as long). See
analysis/connections.md, threads/03, INDEX.md.

WHAT THIS DOES (and does NOT do):
- Renders every marking in numeric forms (A1Z26, sum/diff/product, concatenations) and as
  candidate GRID REFERENCES under the two natural conventions (first letter on the alpha axis
  + second letter -> the numeric axis, and the reverse), then checks each candidate against
  the two REAL captured grids' dimensions.
- The grid spec is now CAPTURED ([U26] -> [K26], 2026-06-13 investigator data). GRIDS below
  holds the two photographed prop-map grids; the script flags which candidates are in-range.
- TEST, not finding. Nothing here is [KNOWN] except the grid dimensions [K26]; a cell being
  "in range" is [SPECULATION] until a node-plot corroborates it.

INPUT PROVENANCE:
- Markings: KNOWN [K6][K9]. Known number lines (to cross-check against): Gertrude opening
  1,2,3,7,6,4,5 [K23]; tallies 1-7 [K4][K7]; "five poles west" [K12].
- Grid spec: CAPTURED [K26] (firsthand investigator data, PS5, 2026-06-13). Two "A Partial
  and Correct Railroad and State Map of the United States" prop maps photographed at a
  stranger's camp (reportedly near the "Mysterious House"/turtle house; camp identity
  uncertain). Each carries a printed coordinate grid -- the in-game grid [U26] was blocked on.
  Firsthand data is high-trust (CLAUDE.md) and supersedes the earlier web-negative.
    MAP 1 (continental US frame): cols = NUMBERS 1-30 (left->right), rows = LETTERS A-U
      (top->bottom). 30 x 21. Letter axis vertical (latitude-like), number axis horizontal
      (longitude-like) -- the SAME assignment as the K25 loading-screen device (letter=lat).
    MAP 2 (regional, drawn over the playable world -- W.Elizabeth/New Hanover/Lemoyne/
      Ambarino): cols = LETTERS A-O (left->right), rows = NUMBERS 1-7 (bottom->top). 15 x 7.
      Axes FLIPPED vs Map 1 (letter=horizontal/long, number=vertical/lat). This is the grid
      actually overlaid on the game map, so it is the one that could plot mystery nodes.
- Coordinate precedent ([K25], 2026-06-13): RDR2's loading-screen photos DO encode locations
  as letter=latitude / number=longitude coordinates on the fast-travel/Central Union Railroad
  map (community decode, C-tier; annotations in-game). So a coordinate reading has documented
  precedent. The H14 test is to PLOT candidate (letter, number) coordinates and see if any
  land on a mystery node.

Run: `python experiments/number_grid.py`   (Python 3, standard library only)
"""

MARKINGS = [("LJ", "L", "J"), ("SM", "S", "M"), ("EC", "E", "C"),
            ("J+M", "J", "M"), ("S+J", "S", "J")]

# Which markings DISPLAY a '+' connective. The investigator's reading (2026-06-13, S21):
# the punctuation picks the operator -- a '+' pair is ADDED (J+M = 10+13 = 23), a bare
# pair (no '+') is CONCATENATED (EC = 5,3 -> "53"). Provenance: format is KNOWN [K6][K9]
# (the matches genuinely show '+'; the carved/EC sets are bare); the operator rule is the
# investigator's hypothesis, not sourced.
PLUS = {"J+M", "S+J"}
MATCHSTICKS = {"EC", "J+M", "S+J"}   # the matchstick sets [K9] (vs carved LJ/SM) -- H12 group 2

# Grid spec: CAPTURED [K26] (firsthand investigator data, PS5, 2026-06-13). See docstring.
# Each grid: an ALPHA axis (letters A..alpha_max) and a NUMERIC axis (1..num_max). A cell
# pairs one letter (kept as a letter, on the alpha axis) with one number (on the numeric
# axis). Do NOT invent dims -- these are the two photographed grids, nothing else.
GRIDS = [
    {"name": "Map 1 (continental, 1-30 x A-U)", "alpha_max": "U", "num_max": 30},  # 21 x 30
    {"name": "Map 2 (regional,    A-O x 1-7)",  "alpha_max": "O", "num_max": 7},   # 15 x 7
]

# Known number lines to test numeric forms against [K4][K7][K12][K23].
GERTRUDE_OPEN = [1, 2, 3, 7, 6, 4, 5]
TALLIES = [1, 2, 3, 4, 5, 6, 7]


def n(letter):
    return ord(letter) - 64  # A1Z26


def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def operator_value(label, a, b):
    """The investigator's punctuation-as-operator reading [S21]:
    '+' pair -> add the A1Z26 values; bare pair -> concatenate them."""
    if label in PLUS:
        return n(a) + n(b)                 # J+M -> 10+13 = 23 ; S+J -> 19+10 = 29
    return int(f"{n(a)}{n(b)}")            # EC -> 53 ; LJ -> 1210 ; SM -> 1913


def cell_in_range(letter_alpha, num, grid):
    """letter_alpha sits on the grid's letter axis; num on its numeric axis."""
    return (n(letter_alpha) <= n(grid["alpha_max"])) and (1 <= num <= grid["num_max"])


def main():
    print("Numerical pairing + grid-reference test")
    print("=" * 64)
    print("A1Z26: A=1 ... Z=26\n")

    print("1. NUMERIC FORMS per marking")
    print("-" * 64)
    print(f"  {'mark':5s} {'nums':10s} {'sum':>4s} {'diff':>5s} {'prod':>5s}  concat")
    all_nums = []
    for label, a, b in MARKINGS:
        na, nb = n(a), n(b)
        all_nums += [na, nb]
        print(f"  {label:5s} {str([na,nb]):10s} {na+nb:>4d} {abs(na-nb):>5d} "
              f"{na*nb:>5d}  {na}{nb} / {nb}{na}")
    print(f"\n  All A1Z26 numbers in marking order: {all_nums}")
    print( "  Cross-check vs known number lines:")
    print(f"    Gertrude opening {GERTRUDE_OPEN}: "
          f"{'match' if all_nums[:len(GERTRUDE_OPEN)] == GERTRUDE_OPEN else 'no match'}")
    print(f"    Tallies 1-7      {TALLIES}: "
          f"{'match' if sorted(set(all_nums)) == TALLIES else 'no match'}")
    print( "    -> no numeric form lines up with the known sequences. [null]")
    print()

    print("1b. PUNCTUATION-AS-OPERATOR reading [S21] (investigator, 2026-06-13)")
    print("-" * 64)
    print("  Rule: a '+' pair is ADDED; a bare pair is CONCATENATED (A1Z26).")
    vals = {}
    for label, a, b in MARKINGS:
        v = operator_value(label, a, b)
        vals[label] = v
        op = "add" if label in PLUS else "concat"
        prime = "  prime" if is_prime(v) else ""
        print(f"  {label:5s} ({op:6s}) -> {v}{prime}")
    ms = [vals[m] for m in ['EC', 'J+M', 'S+J']]
    ms_concat = "".join(str(vals[m]) for m in ['EC', 'J+M', 'S+J'])
    all5 = "".join(str(vals[m]) for m in ['LJ', 'SM', 'EC', 'J+M', 'S+J'])
    print()
    print(f"  Matchsticks only (EC, J+M, S+J): three numbers {ms}  "
          f"or one number {ms_concat}")
    print(f"    -> all three prime? {all(is_prime(x) for x in ms)}  "
          f"(cf. the Window Rock mural's prime counts 2,3,5,7 [K18])")
    print(f"    -> EC = {vals['EC']} == the 5-black / 3-red feather split [K13]/[S18] "
          f"(EC sits by the Black Widow card)")
    print(f"  All five in marking order -> {all5}")
    print( "  Cross-check vs known number lines (Gertrude 1237645112 [K23], tallies 1-7,")
    print( "  'five poles west'): no containment / no match found. [null but for EC=53]")
    print()

    print("2. GRID-REFERENCE CANDIDATES per CAPTURED grid [K26]  (letter + A1Z26 number)")
    print("-" * 64)
    print("  Convention A: first letter -> letter axis, second -> number axis (A1Z26).")
    print("  Convention B: the reverse. A cell needs the letter <= the grid's letter-max")
    print("  AND the number within 1..number-max. Letter+number is shown either way.\n")
    survivors = {g["name"]: [] for g in GRIDS}
    for grid in GRIDS:
        print(f"  {grid['name']}  [letters A-{grid['alpha_max']}, numbers 1-{grid['num_max']}]")
        for label, a, b in MARKINGS:
            ca_ok = cell_in_range(a, n(b), grid)   # conv A: alpha=a, num=n(b)
            cb_ok = cell_in_range(b, n(a), grid)   # conv B: alpha=b, num=n(a)
            tag = lambda ok: "[in-range]" if ok else "[OUT]    "
            if ca_ok:
                survivors[grid["name"]].append(f"{label}:{a}{n(b)}")
            if cb_ok:
                survivors[grid["name"]].append(f"{label}:{b}{n(a)}")
            print(f"    {label:5s} -> {a}{n(b):<2d} {tag(ca_ok)}   or   "
                  f"{b}{n(a):<2d} {tag(cb_ok)}")
        s = survivors[grid["name"]]
        print(f"    in-range cells: {s if s else 'NONE'}\n")

    print("2b. H14 -- the S21 'numbers' as the numeric axis (letter=lat / number=long)")
    print("-" * 64)
    print("  Read each marking's letter(s) as the latitude/letter axis and its S21 value")
    print("  as the longitude/number axis. Which S21 numbers fall within each grid's")
    print("  numeric range?  (Underdetermined: a marking has TWO letters but one number.)")
    for grid in GRIDS:
        fits = [f"{m}={vals[m]}" for m in ['EC', 'J+M', 'S+J'] if vals[m] <= grid["num_max"]]
        outs = [f"{m}={vals[m]}" for m in ['EC', 'J+M', 'S+J'] if vals[m] > grid["num_max"]]
        print(f"  {grid['name']}: in-range {fits if fits else 'NONE'}; out {outs}")
    print()

    print("SUMMARY (evidence, not fact)")
    print("-" * 64)
    print("  * No numeric form matches Gertrude's numbers, the 1-7 tallies, or 'five")
    print("    poles' -> numeric-code reading is a null so far.")
    print("  * Punctuation-as-operator [S21]: matchsticks -> 53, 23, 29 (all prime) or")
    print("    532329. Only resonance is EC=53 = the 5/3 feather split [S18]; the rest")
    print("    match no known line. Suggestive-at-most, coincidence-prone (small ints).")
    print("  * GRID READING, now testable on the REAL grids [K26]:")
    print("    - Map 2 (the grid actually drawn over the game world, A-O x 1-7): ONLY EC")
    print("      is in range (E3 or C5). LJ/SM/J+M/S+J all fall OUT -- their second")
    print("      letters map to 10-19, past the 7-row cap. Evidence AGAINST a per-cell")
    print("      grid reading of those four on the relevant map; EC survives (cf. S18).")
    print("    - Map 1 (continental frame, 1-30 x A-U): every marking yields an in-range")
    print("      cell (21 rows cover all letters, 30 cols cover all A1Z26 seconds), so it")
    print("      discriminates nothing -- AND its cells land mostly OFF the playable world")
    print("      (the fictional wider USA), so they are not node-plottable.")
    print("    - H14 S21-numbers: only Map 1 admits any (J+M=23, S+J=29 <=30; EC=53 out);")
    print("      Map 2 admits none. No single grid validates all five markings.")
    print("  * NET: the clean per-cell grid reading is largely NEGATIVE -- on the one grid")
    print("    overlaid on the game world, four of five markings are out of range. EC is")
    print("    the lone survivor. Logged as a null-leaning result [U26], not a finding.")


if __name__ == "__main__":
    main()

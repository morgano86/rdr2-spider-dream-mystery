#!/usr/bin/env python3
"""Per-web feather SOCKET (left/centre/right) -- closing the [U0] residual, tested for structure

QUESTION TESTED:
  The last residual of [U0] was the per-web feather *socket* -- which radial sector the feather
  hangs from. Earlier reads were flagged camera-confounded (apparent screen left/right depends on
  camera angle). This pass re-reads all 8 front shots ([#59]) by a CAMERA-INVARIANT method:
  position RELATIVE TO THE WEB'S OWN CENTRAL VERTICAL RADIAL (the hub's straight-down strand),
  which rotates *with* the web, so left/centre/right of it survives camera angle. Then:
    1. Do the camera-invariant reads agree with the earlier screen-relative reads? (if yes, the
       confound did not flip the gross call -> the position data is usable.)
    2. Is there real structure -- (a) a colour<->side association, (b) a monotone black hour-sweep?
       Quantify how surprising each is, so we don't over-read 8 eyeballed points.

WHY THIS MATTERS:
  Socket is the ONLY surviving form of "position encodes something" after orientation died
  (uniform tip-down -> [H4] refuted). If socket correlates with COLOUR it adds an independent
  line to the colour-as-first-class-axis reading ([H9]/[U29]/[H18]); if the three hour-twinned
  blacks sweep cleanly with the clock it is a structural hint worth chasing in the raw entity data.

WHAT THIS DOES (and does NOT do):
  - Records the 8 camera-invariant socket reads (PROVISIONAL: eyeballed from C-tier screenshots).
  - Cross-checks them against the earlier screen-relative reads in feather-positions/README.md.
  - Runs exact permutation / counting tests for the colour<->side and black-sweep statistics.
  - It is a TEST, not a finding. A small p is at most [SPECULATION] until the raw per-instance
    entity placement (game files) confirms the sockets. A *negative* (reads disagree, or no
    structure) is itself a real, loggable result.

INPUT PROVENANCE:
  - Web list / colours / codes / hours: KNOWN, images/webs/WEBS-MANIFEST.md [K13a].
  - Socket reads: PROVISIONAL, eyeballed 2026-06-14 from the [#59] front shots
    (images/webs/feather-positions/), measured against each web's own central radial.
  - Earlier screen-relative reads: feather-positions/README.md table (the rows being cross-checked).

Run: `python experiments/web_socket_position.py`   (Python 3, standard library only)
"""

from itertools import combinations, product

# (code, location, colour, hour_start) -- KNOWN from WEBS-MANIFEST.md [K13a].
WEBS = [
    ("B23",  "Overflow",    "black", 2),
    ("B34",  "Cornwall",    "black", 3),
    ("B45",  "Emerald",     "black", 4),
    ("B56",  "Oil Fields",  "black", 5),
    ("BL56", "Ringneck",    "black", 5),
    ("R23",  "Scarlett",    "red",   2),
    ("R34",  "Saint Denis", "red",   3),
    ("R45",  "Southfield",  "red",   4),
]
COLOUR = {w[0]: w[2] for w in WEBS}
HOUR   = {w[0]: w[3] for w in WEBS}
LOC    = {w[0]: w[1] for w in WEBS}

# Camera-INVARIANT socket reads, measured vs the web's own central vertical radial.
# PROVISIONAL (eyeballed 2026-06-14 from [#59] front shots). L=left of centre radial,
# C=on/at it, R=right of it. Confidence: head-on shots high; oblique shots moderate.
SOCKET = {
    "B23":  "L",   # Overflow    -- feather low-left near rim          (oblique, moderate)
    "B34":  "C",   # Cornwall    -- on/just-right of centre radial     (HEAD-ON, high)
    "B45":  "R",   # Emerald     -- right side near rim                (oblique, moderate)
    "B56":  "L",   # Oil Fields  -- ~2nd sector from left, outer       (near head-on, high)
    "BL56": "L",   # Ringneck    -- left-of-centre, mid/outer          (oblique, moderate)
    "R23":  "R",   # Scarlett    -- just right of centre radial        (oblique, LOW -- near C)
    "R34":  "R",   # Saint Denis -- right side near rim                (oblique, moderate)
    "R45":  "C",   # Southfield  -- centre, hangs from central radial  (near head-on, moderate)
}

# Earlier SCREEN-RELATIVE reads (feather-positions/README.md), normalised to L/C/R for the
# agreement check. "left-of-centre" -> L; "centre (just right of axis)" -> C.
SCREEN_PRIOR = {
    "B23": "L", "B34": "C", "B45": "R", "B56": "L",
    "BL56": "L", "R23": "R", "R34": "R", "R45": "C",
}

IDX = {"L": 0, "C": 1, "R": 2}          # left->right numeric, for the side statistic
CODES  = [w[0] for w in WEBS]
REDS   = [c for c in CODES if COLOUR[c] == "red"]
BLACKS = [c for c in CODES if COLOUR[c] == "black"]


def agreement():
    print("1. Camera-invariant reads vs the earlier screen-relative reads")
    print("-" * 68)
    print(f"    {'code':5s} {'loc':12s} {'colour':6s} {'hour':6s} {'invariant':9s} {'prior':6s} match")
    n_match = 0
    for c in CODES:
        m = SOCKET[c] == SCREEN_PRIOR[c]
        n_match += m
        print(f"    {c:5s} {LOC[c]:12s} {COLOUR[c]:6s} {HOUR[c]}-{HOUR[c]+1:<3} "
              f"{SOCKET[c]:9s} {SCREEN_PRIOR[c]:6s} {'OK' if m else 'XX'}")
    print(f"\n    {n_match}/8 agree. If high, the camera confound did NOT flip the gross L/C/R")
    print("    call -> the position reads are usable (promote from 'confounded' to 'weak signal').")
    return n_match


def colour_side_test():
    print("\n2. Colour <-> side association  (do reds sit further RIGHT than blacks?)")
    print("-" * 68)
    red_mean   = sum(IDX[SOCKET[c]] for c in REDS) / len(REDS)
    black_mean = sum(IDX[SOCKET[c]] for c in BLACKS) / len(BLACKS)
    obs = red_mean - black_mean
    print(f"    side index L=0 C=1 R=2.  red mean={red_mean:.3f}  black mean={black_mean:.3f}"
          f"  diff={obs:.3f}")
    # Exact permutation null: over all C(8,3) choices of which 3 webs are 'red', how often is
    # (red_mean - black_mean) >= observed?  (sides held fixed, colour labels shuffled.)
    sides = [IDX[SOCKET[c]] for c in CODES]
    total = ge = 0
    for red_idx in combinations(range(8), 3):
        total += 1
        rm = sum(sides[i] for i in red_idx) / 3
        bm = sum(sides[i] for i in range(8) if i not in red_idx) / 5
        if (rm - bm) >= obs - 1e-9:
            ge += 1
    print(f"    permutation null over C(8,3)={total} colour assignments: "
          f"P(diff >= observed) = {ge}/{total} = {ge/total:.3f}")
    print("    -> weak n=8 eyeballed signal; a small p is SUGGESTIVE, not a finding.")
    return obs, ge / total


def black_sweep_test():
    print("\n3. Black hour-sweep  (do the 3 hour-twinned blacks go L->C->R with the clock?)")
    print("-" * 68)
    twinned = ["B23", "B34", "B45"]          # the 3 blacks that each share an hour with a red
    seq = [SOCKET[c] for c in twinned]
    print(f"    {twinned[0]}(2-3)={seq[0]}  {twinned[1]}(3-4)={seq[1]}  {twinned[2]}(4-5)={seq[2]}"
          f"   sweep = {'->'.join(seq)}")
    strict_increasing = all(IDX[seq[i]] < IDX[seq[i + 1]] for i in range(len(seq) - 1))
    print(f"    strictly L->C->R with hour?  {strict_increasing}")
    # Null: each of 3 sockets uniform over {L,C,R} (3^3=27). P(this exact L,C,R) and P(any
    # strictly monotone sweep, either direction).
    prod = list(product("LCR", repeat=3))
    exact = sum(1 for a in prod if list(a) == seq) / len(prod)
    mono = sum(1 for a in prod
               if all(IDX[a[i]] < IDX[a[i + 1]] for i in range(2))
               or all(IDX[a[i]] > IDX[a[i + 1]] for i in range(2))) / len(prod)
    print(f"    null (each socket uniform /3): P(exact observed sweep)={exact:.3f}; "
          f"P(any strict monotone sweep)={mono:.3f}")
    # The two 5-6 AM blacks (the [K13b] interchangeable pair) -- same socket?
    same = SOCKET["B56"] == SOCKET["BL56"]
    print(f"    5-6 AM pair B56={SOCKET['B56']} / BL56={SOCKET['BL56']} share a socket?  {same}"
          "  (a 2nd 'same' alongside their shared hour -> reinforces interchangeability)")
    return strict_increasing, exact, mono, same


def colour_sweep(colour, codes_by_hour):
    """Generic: does this colour's socket move monotonically with the clock? (the black test,
    applied to either colour so reds get the same scrutiny.)"""
    seq = [SOCKET[c] for c in codes_by_hour]
    idx = [IDX[s] for s in seq]
    inc = all(idx[i] < idx[i + 1] for i in range(len(idx) - 1))
    dec = all(idx[i] > idx[i + 1] for i in range(len(idx) - 1))
    nondec = all(idx[i] <= idx[i + 1] for i in range(len(idx) - 1))
    noninc = all(idx[i] >= idx[i + 1] for i in range(len(idx) - 1))
    label = " -> ".join(f"{c}({HOUR[c]}-{HOUR[c]+1})={SOCKET[c]}" for c in codes_by_hour)
    print(f"    {colour:5s}: {label}")
    print(f"           strict inc {inc} | strict dec {dec} | non-dec {nondec} | non-inc {noninc}")
    return inc or dec


def red_vs_black_and_partition():
    print("\n4. Do the REDS validate a time-sweep too, or are they the curveball?")
    print("-" * 68)
    # The 3 hour-twinned members of each colour, in clock order.
    black_twin = ["B23", "B34", "B45"]
    red_twin   = ["R23", "R34", "R45"]
    b_mono = colour_sweep("black", black_twin)
    r_mono = colour_sweep("red", red_twin)
    print(f"    -> blacks monotone with clock: {b_mono} ;  reds monotone with clock: {r_mono}")
    # Socket occupancy per colour.
    bset = sorted({SOCKET[c] for c in BLACKS}, key=lambda s: IDX[s])
    rset = sorted({SOCKET[c] for c in REDS},   key=lambda s: IDX[s])
    print(f"    socket occupancy:  blacks use {bset} (span all 3);  reds use {rset} (never LEFT)")
    print("    -> The time-sweep is a BLACK-only pattern. Reds occupy centre/right only and do")
    print("       NOT move monotonically -> consistent with [U29] 'reds work in ANY order'")
    print("       (an unordered group has no reason to encode the clock in its sockets).")

    print("\n5. All 8, or eliminate some?  The structural partition (KNOWN [H9]/[K13b]/[U29])")
    print("-" * 68)
    print("    8 webs = 4 + 1 + 3:")
    print("      * 4 CONNECTOR blacks  B23,B45,B56,BL56  = the [K13b] NON-RESPAWN chain (the only")
    print("        documented 'stays shot off' behaviour). B56/BL56 interchangeable (same hr+socket).")
    print("      * 1 INDEX black       B34 Cornwall      = North boundary; special; suspected LAST.")
    print("      * 3 RED group         R23,R34,R45       = South boundary; free internal order [U29].")
    print("    So the documented chain involves only the 4 connector blacks -- NOT all 8. Whether")
    print("    the reds + B34 must also be shot, or are a separate group / decoys to EXCLUDE")
    print("    (the [H18] mural-seed 'filter' reading), is OPEN [U29]. The decider is the")
    print("    time-lock-vs-persistence question: if a web is only shootable in its hour, an")
    print("    arbitrary all-8 sequence is physically impossible -- which would itself argue for")
    print("    a per-colour/per-boundary subset, not one global 8-feather order. [SPECULATION].")


def main():
    print("Per-web feather SOCKET -- closing the [U0] residual  [U0/H9/U29/H18]")
    print("=" * 68)
    agreement()
    colour_side_test()
    black_sweep_test()
    red_vs_black_and_partition()
    print("\nSUMMARY (evidence, not fact)")
    print("-" * 68)
    print("  * Camera-invariant reads (vs each web's own central radial) reproduce the earlier")
    print("    screen-relative reads -> the confound did not flip them; socket is now a usable")
    print("    weak signal, no longer 'not a finding'. Residual of [U0] is closeable from images.")
    print("  * Reds skew RIGHT of blacks; the 3 hour-twinned blacks sweep L->C->R with the clock;")
    print("    the 5-6 AM pair B56/BL56 share BOTH hour and socket. All [SPECULATION] -- n=8,")
    print("    eyeballed; confirm against the raw per-instance entity placement (game files).")
    print("  * Net: adds an independent COLOUR-axis line ([H9]/[U29]/[H18]); does NOT revive [H4]")
    print("    (socket != orientation; orientation is uniform tip-down).")


if __name__ == "__main__":
    main()

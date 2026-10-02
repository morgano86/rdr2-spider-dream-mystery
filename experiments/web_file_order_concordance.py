#!/usr/bin/env python3
"""Are the spiderdream file NUMBERS the intended shooting ORDER? - the per-web
concordance test the [K39] datamine finally makes possible.

Question + IDs
--------------
[K39] (2026-07-02) sourced the per-web `spiderdream0X` -> location mapping as a genuine
public datamine (u/Artem_ab6, [#65]), turning the manifest's File column into real data
and activating [S29] (the numbering's colour-grouped / twin-sum-11 structure, ~1/3360).
What NOBODY - here or in the community - has tested is the numbering read as an
ORDERING: shoot the webs in file order 1->8 (or 1->5 blacks-only, per [H24])?

This script builds the full per-web concordance matrix (file #, colour, hour, socket
[H19], tied boundary + zone containment [K31], map position [S31], region) and tests
the file order against every ordering principle on record:

  1. chronology / reverse-chronology (the [H17] axis)
  2. the [K13b] non-respawn chain - INCLUDING the investigator's eyeball observation
     that files 5->1 descending = B23,B45,B34,B56,BL56 = the chain with B34 inserted
     mid-run. That observation gets a proper null here, not trust.
  3. the [H19] socket sweep (L->C->R)
  4. geometric paths: clockwise winding around the body cluster ([S31] centre),
     nearest-neighbour greediness, tour-length percentile.
     (Telegraph-LINE adjacency is NOT tested: no telegraph-line topology data is on
     file, and inventing it would violate the no-invented-data rule.)
  5. boundary-exit FEASIBILITY under the [K29]/[K31] rules (visible-state semantics:
     a held feather resets when the player exits its tied boundary), incl. night
     counting and the [H20] no-mixed-colour-night constraint.

A positive (file order concordant with a principle beyond chance, or a unique feasible
file-order read) is at most [SPECULATION] pending in-game test; a clean negative is a
real finding that constrains [S29] ("the numbers are a structured INDEX, not a
sequence").

Inputs + provenance
-------------------
  * File numbers: WEBS-MANIFEST File column = the [K39] Artem_ab6 datamine (C-tier,
    single dataminer, "(testing)").
  * Colour/hour: the [K13a] colour x hour lattice (manifest; per-web cells C-tier).
  * Socket L/C/R: [H19] camera-invariant reads (C-tier images, 8/8 agreement).
  * Tied boundary + zone containment: [K31] firsthand investigator data (2026-06-14).
  * Map positions: # PROVISIONAL - the same eyeball pixel reads off the community
    overlay used by web_geometry_shape.py ([S31]); +/-25 px, NOT in-game coords.
  * Night-feasibility rules: [K29] (state persists in-boundary, resets on exit),
    [H20] firsthand travel feasibility (black+red in one night solo-impossible;
    the doubled 5-6 AM pair hard-but-doable) - the H20 leg is inference-grade.

Run:  python experiments/web_file_order_concordance.py
Deps: stdlib only. Deterministic (exhaustive enumeration; no sampling).
"""
from itertools import permutations
import math

# ----------------------------------------------------------------------------------
# The concordance matrix (single source: WEBS-MANIFEST + K31 + H19 + S31 reads)
# zones = boundaries that physically CONTAIN the web (K31); tied = the boundary the
# web's reset state is TIED to. O = orange/Top, Y = yellow/Connector, R = red/Bottom.
# xy = PROVISIONAL overlay pixels (S31), x=east+, y=south+.
# ----------------------------------------------------------------------------------
WEBS = {
    "BL56": dict(file=1, name="Ringneck",   colour="black", hour=5.5, socket="L",
                 tied="Y", zones={"Y", "R"}, xy=(625, 642), region="Lemoyne"),
    "B56":  dict(file=2, name="OilFields",  colour="black", hour=5.5, socket="L",
                 tied="Y", zones={"O", "Y"}, xy=(310, 150), region="NewHanover"),
    "B34":  dict(file=3, name="Cornwall",   colour="black", hour=3.5, socket="C",
                 tied="O", zones={"O", "Y"}, xy=(205, 188), region="NewHanover"),
    "B45":  dict(file=4, name="Emerald",    colour="black", hour=4.5, socket="R",
                 tied="Y", zones={"O", "Y"}, xy=(691, 281), region="NewHanover"),
    "B23":  dict(file=5, name="Overflow",   colour="black", hour=2.5, socket="L",
                 tied="Y", zones={"O", "Y"}, xy=(691, 151), region="NewHanover"),
    "R23":  dict(file=6, name="Scarlett",   colour="red",   hour=2.5, socket="R",
                 tied="R", zones={"Y", "R"}, xy=(417, 718), region="Lemoyne"),
    "R45":  dict(file=7, name="Southfield", colour="red",   hour=4.5, socket="C",
                 tied="R", zones={"Y", "R"}, xy=(443, 827), region="Lemoyne"),
    "R34":  dict(file=8, name="SaintDenis", colour="red",   hour=3.5, socket="R",
                 tied="R", zones={"R"},      xy=(1196, 841), region="Lemoyne"),
}
CENTRE = (482, 418)          # featherless "body" cluster (S31)  # PROVISIONAL
BLACKS = [w for w in WEBS if WEBS[w]["colour"] == "black"]
REDS = [w for w in WEBS if WEBS[w]["colour"] == "red"]
FILE_ASC = sorted(WEBS, key=lambda w: WEBS[w]["file"])
FILE_DESC = FILE_ASC[::-1]
BLACKS_ASC = [w for w in FILE_ASC if w in BLACKS]
BLACKS_DESC = BLACKS_ASC[::-1]
SOCKET_RANK = {"L": 0, "C": 1, "R": 2}

# The documented non-respawn chain [K13b]; B56/BL56 interchangeable.
CHAIN_VARIANTS = [("B23", "B45", "B56", "BL56"), ("B23", "B45", "BL56", "B56")]


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def bearing(o, p):
    return math.degrees(math.atan2(p[0] - o[0], -(p[1] - o[1]))) % 360


def tau_score(seq, key):
    """Concordant-minus-discordant pairs of `key` values along seq (ties skipped),
    normalised by comparable pairs. +1 = perfectly increasing along the sequence."""
    vals = [key(w) for w in seq]
    conc = disc = 0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if vals[i] < vals[j]:
                conc += 1
            elif vals[i] > vals[j]:
                disc += 1
    comparable = conc + disc
    return (conc - disc) / comparable if comparable else 0.0


def contains_subseq(seq, sub):
    it = iter(seq)
    return all(x in it for x in sub)


def chain_consistent(seq):
    """Does seq preserve the [K13b] chain's relative order (either 5-6 variant)?"""
    core = [w for w in seq if w in ("B23", "B45", "B56", "BL56")]
    return tuple(core) in CHAIN_VARIANTS


def winding(seq):
    """Number of full CW wraps needed to visit seq around CENTRE (1 = perfect CW
    tour from some start; ~n/2 for random). Returns min of CW and CCW."""
    angs = [bearing(CENTRE, WEBS[w]["xy"]) for w in seq]
    cw = sum((angs[i + 1] - angs[i]) % 360 for i in range(len(angs) - 1))
    ccw = sum((angs[i] - angs[i + 1]) % 360 for i in range(len(angs) - 1))
    return min(math.ceil(cw / 360), math.ceil(ccw / 360))


def nn_hits(seq):
    """How many steps go to the nearest unvisited web?"""
    hits = 0
    for i in range(len(seq) - 1):
        here = WEBS[seq[i]]["xy"]
        remaining = seq[i + 1:]
        nearest = min(remaining, key=lambda w: dist(here, WEBS[w]["xy"]))
        if nearest == seq[i + 1]:
            hits += 1
    return hits


def tour_len(seq):
    return sum(dist(WEBS[seq[i]]["xy"], WEBS[seq[i + 1]]["xy"])
               for i in range(len(seq) - 1))


def simulate(order):
    """Visible-state simulation under [K29]/[K31]: shooting web w requires being at w;
    a held feather resets the moment the player moves to a web outside its tied
    boundary (zones are large convex rectangles, so a path between two webs that
    share a zone can stay inside it). Returns (ok, resets, nights, mixed_nights)."""
    resets = []
    held = []                                    # webs currently shot & down
    nights = 1
    night_colours = {WEBS[order[0]]["colour"]}
    mixed = 0
    for i, w in enumerate(order):
        if i:
            prev = order[i - 1]
            # boundary-exit check: any held feather whose tied zone doesn't
            # contain the destination web resets on the way there. [K29]
            for hw in list(held):
                if WEBS[hw]["tied"] not in WEBS[w]["zones"]:
                    resets.append((hw, f"exiting {WEBS[hw]['tied']} en route to {w}"))
                    held.remove(hw)
            # night accounting: hours must advance within a night; the equal-hour
            # 5-6 AM pair B56/BL56 is doable in one window (K13b "doubled").
            same_night = (WEBS[w]["hour"] > WEBS[prev]["hour"] or
                          {w, prev} == {"B56", "BL56"})
            if same_night:
                night_colours.add(WEBS[w]["colour"])
            else:
                if len(night_colours) > 1:
                    mixed += 1
                nights += 1
                night_colours = {WEBS[w]["colour"]}
        held.append(w)
    if len(night_colours) > 1:
        mixed += 1
    return (not resets), resets, nights, mixed


def p_str(k, n):
    return f"{k}/{n} = {k / n:.4f}"


def main():
    print("# File-number-as-order concordance test  (exhaustive, deterministic)\n")

    # ---- The concordance matrix -----------------------------------------------------
    print("## Concordance matrix (file# / colour / hour / socket / tied+zones / xy / region)")
    hdr = f"{'code':5s} {'file':4s} {'location':10s} {'col':5s} {'hour':4s} {'sock':4s} " \
          f"{'tied':4s} {'zones':7s} {'xy (PROV.)':12s} {'region':10s} {'CW deg':6s}"
    print("  " + hdr)
    for w in FILE_ASC:
        d = WEBS[w]
        print(f"  {w:5s} {d['file']:<4d} {d['name']:10s} {d['colour']:5s} {d['hour']:<4.1f} "
              f"{d['socket']:4s} {d['tied']:4s} {'+'.join(sorted(d['zones'])):7s} "
              f"{str(d['xy']):12s} {d['region']:10s} {bearing(CENTRE, d['xy']):5.0f}")
    print(f"\n  file ASC  1->8: {' > '.join(FILE_ASC)}")
    print(f"  file DESC 8->1: {' > '.join(FILE_DESC)}")
    print(f"  blacks ASC  1->5: {' > '.join(BLACKS_ASC)}")
    print(f"  blacks DESC 5->1: {' > '.join(BLACKS_DESC)}\n")

    black_perms = list(permutations(BLACKS))               # 120 (conditional null:
    full_cond = [b + r for b in permutations(BLACKS)       # colour blocks fixed, 720)
                 for r in permutations(REDS)]
    full_perms = list(permutations(WEBS))                  # 40320 (raw null)

    # ---- Test 1: chronology ---------------------------------------------------------
    print("## Test 1 - chronology / reverse-chronology (tau of hour along file order)")
    for label, seq, null in [("full 8, file ASC", FILE_ASC, full_cond),
                             ("blacks, file ASC", BLACKS_ASC, black_perms)]:
        t = tau_score(seq, lambda w: WEBS[w]["hour"])
        taus = [tau_score(p, lambda w: WEBS[w]["hour"]) for p in null]
        k = sum(1 for x in taus if abs(x) >= abs(t) - 1e-12)
        print(f"  {label:18s} tau={t:+.3f}  (|tau|>=obs under conditional null: {p_str(k, len(taus))})")
    print("  -> DESC reads are the same test mirrored (tau -> -tau); no separate df.\n")

    # ---- Test 2: the K13b chain + the investigator's descending observation ---------
    print("## Test 2 - [K13b] chain vs the file order (the eyeballed 5->1 claim)")
    print(f"  blacks DESC = {' > '.join(BLACKS_DESC)}")
    obs_desc = chain_consistent(BLACKS_DESC)
    obs_asc = chain_consistent(BLACKS_ASC)
    print(f"  chain relative order preserved?  DESC: {obs_desc}   ASC: {obs_asc}")
    n = len(black_perms)
    k_one = sum(1 for p in black_perms if chain_consistent(p))
    k_either = sum(1 for p in black_perms
                   if chain_consistent(p) or chain_consistent(p[::-1]))
    print(f"  null (random file assignment to the 5 blacks, conditional on [S29] colour blocks):")
    print(f"    P(a given direction preserves the chain, either 5-6 variant) = {p_str(k_one, n)}")
    print(f"    P(EITHER direction preserves it - the read we'd have reported) = {p_str(k_either, n)}")
    print("  -> the observation is REAL but weak: ~1/12 one-direction, ~1/6 with the")
    print("     direction freedom, before counting the other principles tried below.\n")

    # ---- Test 3: socket sweep -------------------------------------------------------
    print("## Test 3 - [H19] socket sweep (L->C->R) along the file order")
    for label, seq, null in [("full 8, file ASC", FILE_ASC, full_cond),
                             ("blacks, file ASC", BLACKS_ASC, black_perms)]:
        t = tau_score(seq, lambda w: SOCKET_RANK[WEBS[w]["socket"]])
        taus = [tau_score(p, lambda w: SOCKET_RANK[WEBS[w]["socket"]]) for p in null]
        k = sum(1 for x in taus if abs(x) >= abs(t) - 1e-12)
        sockets = ",".join(WEBS[w]["socket"] for w in seq)
        print(f"  {label:18s} sockets={sockets:16s} tau={t:+.3f}  p(|tau|>=obs) = {p_str(k, len(taus))}")
    print()

    # ---- Test 4: geometric paths ----------------------------------------------------
    print("## Test 4 - geometric paths (PROVISIONAL overlay coords, [S31])")
    print("  (a) clockwise winding around the body cluster (1 = clean CW/CCW tour)")
    for label, seq, null in [("full 8, file ASC", FILE_ASC, full_cond),
                             ("blacks, file ASC", BLACKS_ASC, black_perms)]:
        wobs = winding(seq)
        ws = [winding(p) for p in null]
        k = sum(1 for x in ws if x <= wobs)
        print(f"      {label:18s} winding={wobs}  p(<= obs) = {p_str(k, len(ws))}")
    print("  (b) nearest-neighbour greediness (steps that go to the nearest unvisited)")
    for label, seq, null in [("full 8, file ASC", FILE_ASC, full_cond),
                             ("blacks, file ASC", BLACKS_ASC, black_perms)]:
        h = nn_hits(seq)
        hs = [nn_hits(p) for p in null]
        k = sum(1 for x in hs if x >= h)
        print(f"      {label:18s} NN hits={h}/{len(seq)-1}  p(>= obs) = {p_str(k, len(hs))}")
    print("  (c) tour length percentile (short = a designed route, long = anti-route)")
    for label, seq, null in [("full 8, file ASC", FILE_ASC, full_cond),
                             ("blacks, file ASC", BLACKS_ASC, black_perms)]:
        L = tour_len(seq)
        Ls = sorted(tour_len(p) for p in null)
        below = sum(1 for x in Ls if x <= L)
        print(f"      {label:18s} len={L:6.0f}px  percentile={below/len(Ls)*100:5.1f}% of null")
    print("  (d) telegraph-line adjacency: NOT TESTABLE - no telegraph-line topology")
    print("      data is on file; skipped rather than invented.\n")

    # ---- Test 5: boundary-exit feasibility ([K29]/[K31] simulator) -------------------
    print("## Test 5 - boundary-exit feasibility, visible-state semantics [K29]/[K31]")
    named = [
        ("file ASC full 1->8", FILE_ASC),
        ("file DESC full 8->1", FILE_DESC),
        ("blacks ASC 1->5", BLACKS_ASC),
        ("blacks DESC 5->1 (eyeballed)", BLACKS_DESC),
        ("Test C order (K13b + B34 last)", ["B23", "B45", "B56", "BL56", "B34"]),
        ("S37 Gertrude 1,2,3,7,6,4,5", ["BL56", "B56", "B34", "R45", "R23", "B45", "B23"]),
        ("H22-R2 favoured (reds then blacks)", ["R23", "R45", "R34", "B23", "B45", "B56", "BL56", "B34"]),
    ]
    for label, order in named:
        ok, resets, nights, mixed = simulate(list(order))
        why = "" if ok else f"  [resets: {'; '.join(f'{w} ({r})' for w, r in resets)}]"
        h20 = f", {mixed} mixed-colour night(s) (H20: solo-impossible)" if mixed else ""
        print(f"  {label:34s} {'FEASIBLE' if ok else 'INFEASIBLE':10s} nights={nights}{h20}{why}")
    # exhaustive sweeps
    feas5 = [p for p in black_perms if simulate(list(p))[0]]
    crit = all((p.index("BL56") < p.index("B34")) == (simulate(list(p))[0])
               for p in black_perms)
    print(f"\n  blacks-only sweep: {len(feas5)}/120 orders keep all 5 visibly down;")
    print(f"    the criterion is exactly 'BL56 before B34': {crit}")
    print("    (independent re-derivation of the investigator's [H24]-correction geometry)")
    both = [p for p in feas5 if chain_consistent(p)]
    print(f"  feasible AND [K13b]-consistent: {len(both)} orders:")
    for p in both:
        print(f"    {' > '.join(p)}")
    feas8 = sum(1 for p in full_perms if simulate(list(p))[0])
    print(f"  full-8 sweep: {feas8}/40320 orders keep all 8 visibly down")
    print("    -> all-8-simultaneously-down is GEOMETRICALLY IMPOSSIBLE under visible-state")
    print("       rules (R34 lives only in R; B34's hold needs O) - the [H22] seam, now")
    print("       exhaustively verified, colour-order independent.\n")

    # ---- Test 6: what the numbers DO encode (index structure, incl. a new one) -------
    print("## Test 6 - index structure (context: the known [S29] blocks + a region check)")
    nh_files = sorted(WEBS[w]["file"] for w in WEBS if WEBS[w]["region"] == "NewHanover")
    print(f"  New Hanover webs hold files {nh_files}; Lemoyne holds the rest.")
    contig = nh_files == list(range(nh_files[0], nh_files[0] + len(nh_files)))
    # raw null: any 4-of-8 subset for NH; conditional null: NH = 4 of the 5 black files
    from math import comb
    raw_p = 5 / comb(8, 4)
    cond_hits = sum(1 for drop in range(1, 6)
                    if (lambda s: s == list(range(s[0], s[0] + 4)))(
                        [f for f in range(1, 6) if f != drop]))
    print(f"  contiguous block? {contig}  raw p = 5/{comb(8,4)} = {raw_p:.3f}; "
          f"conditional on [S29] colour blocks p = {cond_hits}/5 = {cond_hits/5:.2f}")
    print("  -> region contiguity is mostly a FREE RIDER on the colour grouping -")
    print("     an example of why the conditional nulls above matter.\n")

    print("## Verdict (evidence, not fact; ~6 primary tests were run - judge the")
    print("## strongest uncorrected p against that look-elsewhere)")
    print("  See results/web_file_order_concordance.md.")


if __name__ == "__main__":
    main()

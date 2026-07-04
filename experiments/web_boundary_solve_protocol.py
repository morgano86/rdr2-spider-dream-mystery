#!/usr/bin/env python3
"""Boundary-decomposition of the web order + the K29-vs-H20 contradiction  (tests U29/U15, sharpens H20/H21, mints H22)

QUESTION TESTED:
  1. If we take the order problem as THREE per-boundary sub-chains ([K31]/[H9]) instead of one
     flat 8-feather sequence, is each sub-chain individually solvable from KNOWN data? (Yes.)
  2. Given that each sub-chain is solvable, how small is the remaining GLOBAL test space the
     investigator must actually try in-game? (It collapses from the ~180 survivors of
     web_colour_group_order.py to essentially ONE favoured protocol -- reds first, then the
     black super-group ending on B34, then ride B34's state north. See the B34-overlap
     refinement below, investigator 2026-06-14: B34 is NOT forced last.)
  3. Does the multi-night solve hypothesis [H20] actually survive the persistence mechanic
     [K29]? (It does NOT, as both are currently stated -- they contradict. This script makes
     the contradiction explicit and enumerates the only three ways out.)

WHY THIS MATTERS (this is the contribution):
  - Previous order experiments (feather_order, web_time_order, web_colour_group_order) treat the
    order as ONE 8-element permutation and ask "which orders survive the reset rules." That frame
    has a ~180-order tail and no obvious next in-game action.
  - But [K31] (firsthand) says the 8 webs are partitioned into 3 boundaries, and shot-state
    persists ONLY within a boundary ([K29], firsthand). So the natural unit is the per-boundary
    chain, and EACH per-boundary chain is already known to be solvable:
        South     = {R23,R34,R45}  -- reds work in ANY internal order ([U29])
        Connector = B23->B45->B56->BL56  -- the [K13b] non-respawn chain (B56/BL56 swap)
        North     = {B34}  -- a single feather; suspected LAST ([U29])
  - Therefore the ONLY thing left unsolved about the order is the GLOBAL COMBINE across
    boundaries -- and [K29] says state RESETS when you leave a boundary. The three boundaries
    only touch at the central overlap ([K28]), which tested negative-leaning for holding state.
  - => [H20] "solve one colour-group per night across nights" CANNOT be executed under [K29] as
    stated: to shoot the Connector you must leave South, which resets South. The contradiction
    is the real frontier. Resolving it (overlap holds state? hidden flag? no global combine?) is
    the single highest-value in-game test, and it is far more targeted than "try 180 orders."

WHAT THIS DOES (and does NOT do):
  - Verifies each per-boundary sub-chain is individually solvable under the KNOWN/[U29] rules.
  - Collapses the global problem to the representative meta-orders an investigator must test,
    under the (PROVISIONAL) "B34 last" suspicion.
  - States the [K29]-vs-[H20] contradiction formally and lists the only three resolutions, each
    a concrete falsifiable in-game test.
  - It is a TEST/reframing, not a finding. The reset rules are C-tier; "B34 last" is a suspicion;
    "intended design" is inference. Everything here is [SPECULATION] pending in-game confirmation.

INPUT PROVENANCE:
  - Web list / colours / codes / hours: KNOWN, images/webs/WEBS-MANIFEST.md ([K13a]).
  - Boundary membership (tied + overlap-contained): [K31] firsthand investigator data 2026-06-14.
  - Persistence resets on boundary EXIT; overlap state-hold negative-leaning: [K29] firsthand.
  - Reset ruleset (reds-any-order, connector chain, B34-special/last): [U29]/[K13b], C-tier (#36).
    Each PROVISIONAL rule is tagged inline.

Run: `python experiments/web_boundary_solve_protocol.py`   (Python 3, standard library only)
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
LOC    = {w[0]: w[1] for w in WEBS}
HOUR   = {w[0]: w[3] for w in WEBS}

# TIED boundary membership -- [K31] firsthand, confirms [H9]. Each web belongs to exactly one.
BOUNDARY_TIED = {
    "North":     ["B34"],
    "Connector": ["B23", "B45", "B56", "BL56"],
    "South":     ["R23", "R34", "R45"],
}
# OVERLAP-contained-but-untied -- [K31]. Shooting these fires the WRONG boundary's despawn (hazard).
BOUNDARY_CONTAINS_UNTIED = {
    "North":     ["B56", "B23", "B45"],
    "Connector": ["B34", "R23", "R45"],   # B34 east-side only; crossing west triggers Connector despawn
    "South":     ["BL56"],
}
CONNECTOR_CHAIN = ["B23", "B45", "B56", "BL56"]  # [K13b]; B56/BL56 interchangeable


# --------------------------------------------------------------------------------------
# Part 1 -- each per-boundary sub-chain is individually SOLVABLE
# --------------------------------------------------------------------------------------
def part1():
    print("1. The 3 per-boundary sub-chains -- each individually solvable")
    print("-" * 70)
    print("   ([K31] partition; shot-state persists only WITHIN a boundary [K29])\n")

    # South: reds in any order -> every internal permutation is a valid sub-solve.
    reds = BOUNDARY_TIED["South"]
    south_solutions = list(permutations(reds))
    print(f"   SOUTH     {reds}")
    print(f"             reds work in ANY internal order ([U29]) -> {len(south_solutions)}/"
          f"{len(south_solutions)} permutations valid. SOLVABLE (any order).")

    # Connector: the [K13b] chain B23<B45<{B56,BL56}, B56/BL56 interchangeable.
    conn = BOUNDARY_TIED["Connector"]
    def conn_ok(o):
        p = {c: i for i, c in enumerate(o)}
        return p["B23"] < p["B45"] < p["B56"] and p["B23"] < p["B45"] < p["BL56"]
    conn_solutions = [o for o in permutations(conn) if conn_ok(o)]
    print(f"   CONNECTOR {conn}")
    print(f"             non-respawn chain B23->B45->B56->BL56 (B56/BL56 swap) [K13b] -> "
          f"{len(conn_solutions)}/{len(list(permutations(conn)))} valid. SOLVABLE (the 2 swaps).")
    for s in conn_solutions:
        print(f"               {'  ->  '.join(s)}")

    # North: single feather. REFINEMENT (investigator, 2026-06-14): B34 need NOT be last.
    north = BOUNDARY_TIED["North"]
    print(f"   NORTH     {north}")
    print(f"             single feather (Cornwall index pole). REFINED ([U29], investigator): NOT")
    print(f"             forced last -- B34's orange/North boundary OVERLAPS the yellow/Connector")
    print(f"             boundary ([K31]: 'Connector contains B34, east side of the pole'), so B34")
    print(f"             can be shot MID-black-run from the overlap without a despawn, e.g.")
    print(f"             B23 -> B34 -> B45 -> B56. => the 5 blacks behave as ONE super-group.")
    print(f"             (Routing caveat [K31]: stay EAST of the pole; crossing WEST trips the")
    print(f"             Connector despawn.)")

    print("\n   => Every sub-chain is already solvable from KNOWN/[U29] data. Nothing about the")
    print("      WITHIN-boundary order is open. The blacks (Connector + B34) join via the overlap")
    print("      into ONE crossable group; reds (South) are the other. (Reinforces [H9]/[K31].)")
    return south_solutions, conn_solutions


# --------------------------------------------------------------------------------------
# Part 2 -- the GLOBAL test space collapses to TWO meta-orders
# --------------------------------------------------------------------------------------
def part2():
    print("\n2. The global combine -> ONE favoured protocol (vs ~180 flat survivors)")
    print("-" * 70)
    # Two FUNCTIONAL groups (Part 1): RED (South) and BLACK (Connector + B34 via overlap).
    # You cannot shuttle RED<->BLACK without a despawn ([K29]/[K31]) -> a single combine cannot
    # round-trip, so one group is done, then the other. REFINEMENT (investigator, 2026-06-14):
    # reds should go FIRST, because B34 (in the BLACK group) is the only feather whose TIED
    # boundary (orange/North) is the oversized one reaching Valentine/Butcher Creek/Fort Brennand
    # ([K28]/[S22]) -- so BLACK should be LAST, ending on B34, whose state then carries north.
    print("   Two FUNCTIONAL groups (Part 1):  RED = South  |  BLACK = Connector + B34 (overlap).")
    print("   You can't shuttle RED<->BLACK without a despawn ([K29]/[K31]) -> no round-trips.")
    print("   So: do one group, then the other. Which is last matters, because only B34's TIED")
    print("   boundary (orange) is the OVERSIZED one reaching Valentine/Butcher Creek ([K28]/[S22]).")
    print("   => favour BLACK last (end on B34, carry its state north). Hence:\n")
    print("   [FAVOURED protocol -- reds first, blacks last, B34 the carrier]")
    print("     1. RED group  (South):    {R23, R34, R45}  in any order")
    print("     2. BLACK group (overlap): B23 -> B34 -> B45 -> B56 -> BL56  (B34 interleaved;")
    print("                               stay EAST of the Cornwall pole)")
    print("     3. ride NORTH inside the orange boundary (B34 state held) -> Butcher Creek /")
    print("        Valentine / Fort Brennand; look for any state-gated trigger ([U15]/[H21]).\n")
    print("   The RED<->BLACK transition (step 1->2) is the single hard crossing -- see Part 3.")
    print("   => essentially ONE protocol to test, not ~180 permutations (blacks-first is the")
    print("      lone alternative, dispreferred: it ends on a red, wasting B34's north-carry).")
    return [("reds-first (favoured)", ["South", "BLACK(Connector+B34)", "ride-north"])]


# --------------------------------------------------------------------------------------
# Part 3 -- the [K29]-vs-[H20] contradiction (the real frontier)
# --------------------------------------------------------------------------------------
def part3(meta_orders):
    print("\n3. The contradiction: [H20] multi-night solve vs [K29] reset-on-exit")
    print("-" * 70)
    print("   [K29] (firsthand): shot-state persists ONLY inside the tied boundary; LEAVING the")
    print("         boundary RESETS it (feather returns to the web).")
    print("   [K28] (firsthand): the 3 boundaries only touch at the central overlap, and the one")
    print("         probe of 'hold state across a crossing' there came back NEGATIVE-leaning.")
    print("   [H20] (inference): solve one colour-group per night, across multiple nights.\n")
    print("   REFINEMENT (investigator, 2026-06-14): the overlap (Part 1) BRIDGES the within-black")
    print("   crossing -- B34 folds into the connector run with no despawn -- so there is only ONE")
    print("   hard crossing left: RED group <-> BLACK group. And the final ride north stays inside")
    print("   B34's TIED (orange) boundary, so B34's state is NOT a crossing -- it carries.")
    print("   The unbridged step is therefore just: finish REDS (South) -> go do BLACKS.\n")
    print("   At that one crossing, [K29] says the boundary you LEAVE (South) RESETS -- the reds")
    print("   visibly return. So a strict all-8-down-at-once state is still NOT reachable by")
    print("   routing alone. [K29] and [H20] still CONTRADICT at the red<->black seam. The exits:\n")
    print("     (R1) The central OVERLAP holds multi-boundary state after all -- the negative")
    print("          probe was incomplete (e.g. needs all of one group DOWN first, or a tied vs")
    print("          contained-web confusion).  TEST: solve South fully, camp in the overlap")
    print("          (whiskey tree [S23]), cross to Connector, re-check South feathers are still")
    print("          down.  Falsifiable in ONE session.")
    print("     (R2) A HIDDEN/invisible flag persists the 'reds done' status even though the")
    print("          visible feather resets (the [K29] caveat).  This is the FAVOURED protocol:")
    print("          reds first (set the flag), then the black super-group ending on B34, then")
    print("          ride B34's state north.  TEST: solve REDS, leave/return so they visibly")
    print("          reset, solve BLACKS (B23->B34->B45->B56->BL56), ride into the orange zone to")
    print("          Butcher Creek/Valentine/Fort Brennand, watch for ANY trigger ([U15]/[U2]).")
    print("          Generalises the [H21] 'state-carry corridor' (B34 is the carrier feather).")
    print("     (R3) There is NO global combine: the 3 sub-chains are three independent mini-")
    print("          puzzles with no joint payoff -> consistent with 'no confirmed reward' ([U2]/")
    print("          [K20]) and the 'one puzzle or two' question ([U3]) resolving toward MANY.")
    print("\n   => The web order is NOT bottlenecked on 'which sequence' (each sub-chain is solved).")
    print("      It is bottlenecked on R1/R2/R3 -- a CROSS-BOUNDARY STATE question. That is the")
    print("      single highest-value next in-game test, and it is sharply targeted. [H22]")


def main():
    print("Boundary-decomposition of the web order + the [K29]-vs-[H20] contradiction  [U29/U15/H22]")
    print("=" * 70)
    part1()
    meta_orders = part2()
    part3(meta_orders)
    print("\nSUMMARY (evidence/reframing, not fact)")
    print("-" * 70)
    print("  * Each per-boundary sub-chain (South any-order / Connector chain / B34) is")
    print("    INDIVIDUALLY solvable from known data -- the within-boundary order is NOT open.")
    print("  * REFINED (investigator): B34 is NOT forced last -- the orange/yellow overlap lets")
    print("    it fold into the black run, so the 5 blacks are ONE super-group and only RED<->BLACK")
    print("    is a hard crossing. Favoured protocol: REDS first -> BLACKS (end on B34) -> ride")
    print("    B34's state NORTH to Butcher Creek/Valentine. ~ONE protocol to test, not ~180.")
    print("  * [K29] (resets on boundary exit) still CONTRADICTS [H20] at the red<->black seam:")
    print("    leaving South to do the blacks resets the reds. The exits remain R1/R2/R3.")
    print("  * => The real frontier is the CROSS-BOUNDARY STATE question (R1 overlap-holds /")
    print("    R2 hidden-flag [favoured] / R3 no-combine), each a falsifiable in-game test. [H22]")
    print("  * [SPECULATION] throughout: reset rules C-tier, 'B34 carries north' a gut-feel")
    print("    inference. A negative result on R1/R3 is itself a real finding to log.")


if __name__ == "__main__":
    main()

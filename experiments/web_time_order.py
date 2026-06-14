#!/usr/bin/env python3
"""Is the feather non-respawn 'order key' just the CLOCK?  (H17, tests U0/H4/K13b/H9)

QUESTION TESTED: U0 / H4 (does feather *orientation* encode the shooting order?) and the
status of K13b (the non-respawn chain B23->B45->B56->BL56) -- by cross-referencing two facts
that already live in the corpus but were never put side by side: the chain's membership and
each web's active HOUR. New hypothesis H17. See images/webs/WEBS-MANIFEST.md, INDEX.md,
analysis/connections.md (sections 5 / 5a).

WHAT THIS DOES (and does NOT do):
- Annotates the documented non-respawn chain [K13b] with each web's KNOWN active hour and
  checks whether the chain is simply CHRONOLOGICAL.
- Re-derives the chain from the H9 boundary partition + a "sort each boundary by hour" rule,
  and reports whether that rule REPRODUCES K13b with no feather-orientation input at all.
- Emits the falsifiable PREDICTION the rule makes for the South (red) boundary.
- It is a TEST, not a finding. A reproduced chain is at most [SPECULATION]/a deflation lead
  until the conflicting community "not time order" claim (see below) is sourced and resolved.

WHY IT MATTERS:
- If the clock alone reproduces the only documented "correct order," then feather ORIENTATION
  (U0/H4) is not *needed* to explain K13b -- a parsimony argument that DEFLATES H4 (already
  weakly dented by the Reddit captures showing feathers hang tip-down under gravity).
- It is also a real TENSION to resolve: WEBS-MANIFEST records a community "[LIKELY] feathers
  do NOT have to be shot in time order" claim, yet the one chain the community found is
  chronological. Both can't be casually true -- flagged as a new question.

INPUT PROVENANCE:
- Web list, colours, codes, active hours: KNOWN, from images/webs/WEBS-MANIFEST.md
  (primary wiki + community research site). No invented data.
- Non-respawn chain B23->B45->B56->BL56 (B56/BL56 interchangeable): [K13b], same file.
- Boundary partition (N: B34; Connector: B23,B45,B56,BL56; S: R23,R45,R34): [H9]/[K21],
  the Jay_0048 map -- SPECULATION-tier (one C-tier author), tagged as such below.
- Feather ORIENTATION per web: UNKNOWN (U0). This script deliberately uses NONE of it; that
  is the point -- it asks whether the order is explained WITHOUT orientation.

Run: `python experiments/web_time_order.py`   (Python 3, standard library only)
"""

# (code, location, colour, hour_start) -- KNOWN from WEBS-MANIFEST.md. hour_start is the
# first hour of the active window (e.g. 2 == the 2-3 AM web).
WEBS = [
    ("B34",  "Cornwall (start/index pole)", "black", 3),
    ("B56",  "Oil Fields",                  "black", 5),
    ("B23",  "Overflow",                    "black", 2),
    ("B45",  "Emerald",                     "black", 4),
    ("BL56", "Ringneck",                    "black", 5),
    ("R34",  "Saint Denis",                 "red",   3),
    ("R45",  "Southfield",                  "red",   4),
    ("R23",  "Scarlett",                    "red",   2),
]
HOUR = {w[0]: w[3] for w in WEBS}
LOC  = {w[0]: w[1] for w in WEBS}

# The documented non-respawn chain [K13b]; B56/BL56 interchangeable (both 5-6 AM).
K13B_CHAIN = ["B23", "B45", "B56", "BL56"]

# The [H9] boundary partition (Jay_0048 map -- SPECULATION-tier, one C-tier author).
BOUNDARIES = {
    "North (orange)":    ["B34"],
    "Connector (yellow)": ["B23", "B45", "B56", "BL56"],
    "South (red)":       ["R23", "R45", "R34"],
}


def is_nondecreasing(codes):
    hrs = [HOUR[c] for c in codes]
    return all(hrs[i] <= hrs[i + 1] for i in range(len(hrs) - 1)), hrs


def main():
    print("Is the feather non-respawn 'order key' just the clock?  [H17]")
    print("=" * 64)

    print("\n1. The documented non-respawn chain [K13b], annotated with active hour")
    print("-" * 64)
    ok, hrs = is_nondecreasing(K13B_CHAIN)
    for c in K13B_CHAIN:
        print(f"    {c:5s} {LOC[c]:14s} {HOUR[c]}-{HOUR[c]+1} AM")
    arrow = "  ".join(f"{HOUR[c]}-{HOUR[c]+1}" for c in K13B_CHAIN)
    print(f"\n    hours along the chain:  {arrow}")
    print(f"    chronological (non-decreasing)?  {ok}")
    print("    -> The 'correct order' the community found is EXACTLY ascending by hour.")

    print("\n2. Reproduce the chain from boundary + 'sort by hour' -- NO orientation input")
    print("-" * 64)
    for name, members in BOUNDARIES.items():
        ordered = sorted(members, key=lambda c: HOUR[c])
        seq = " -> ".join(f"{c}({HOUR[c]}-{HOUR[c]+1})" for c in ordered)
        print(f"    {name:18s}: {seq}")
    conn_sorted = sorted(BOUNDARIES["Connector (yellow)"], key=lambda c: HOUR[c])
    # B56 and BL56 tie at hour 5 -> interchangeable, exactly the K13b caveat.
    reproduces = ([c for c in conn_sorted if c not in ("B56", "BL56")] ==
                  [c for c in K13B_CHAIN if c not in ("B56", "BL56")]
                  and set(conn_sorted[-2:]) == {"B56", "BL56"})
    print(f"\n    Connector sorted-by-hour == K13b chain (5-6 pair interchangeable)?  {reproduces}")
    print("    -> Sorting the Connector boundary by hour REPRODUCES K13b with zero")
    print("       feather-orientation data. The clock is a SUFFICIENT order key here.")

    print("\n3. Falsifiable PREDICTION for the South (red) boundary")
    print("-" * 64)
    south = sorted(BOUNDARIES["South (red)"], key=lambda c: HOUR[c])
    pred = " -> ".join(f"{c}({LOC[c]}, {HOUR[c]}-{HOUR[c]+1})" for c in south)
    print(f"    If the rule generalises, the reds have their own non-respawn chain:")
    print(f"      {pred}")
    print("    i.e. Scarlett(2-3) -> Saint Denis(3-4) -> Southfield(4-5).")
    print("    TEST (web/video or in-game): do the 3 red feathers stay shot when taken")
    print("    in that order, and respawn otherwise?  A NO falsifies H17.")

    print("\n4. The tension this surfaces (a new open question)")
    print("-" * 64)
    print("    WEBS-MANIFEST records a community claim: '[LIKELY] feathers do NOT have to")
    print("    be shot in time order.'  Yet the only documented working chain IS in time")
    print("    order. Either (a) webs are hard time-locked, so chronological is the ONLY")
    print("    physically possible order (chain is trivial, not a 'secret'), or (b) webs")
    print("    persist and the clock-order is a genuine, separately-chosen key. Resolving")
    print("    this needs sourcing -> log as the next research item.")

    print("\nSUMMARY (evidence, not fact)")
    print("-" * 64)
    print("  * The K13b non-respawn chain is exactly chronological (2-3 -> 4-5 -> 5-6).")
    print("  * Sorting the H9 Connector boundary by hour reproduces it with NO feather-")
    print("    orientation data -> the clock is a sufficient order key -> DEFLATES H4.")
    print("  * Prediction: reds chain Scarlett -> Saint Denis -> Southfield (2-3/3-4/4-5).")
    print("  * Open tension: 'not time order' community claim vs a chronological chain.")
    print("  [H17] -- SPECULATION until the time-lock vs persistence question is sourced.")


if __name__ == "__main__":
    main()

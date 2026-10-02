#!/usr/bin/env python3
"""Mystery-letter <-> candidate-name matcher.

QUESTION TESTED: U4 / U5 / U16 / U24 / H11 (and the S1/S2/S3 "re-pair the letters"
readings). Do the mystery's carved/placed letters match initials in a sourced name
list -- principally the Register Rock inscriptions -- and if so, which markings, by
which matching rule? See analysis/connections.md, locations/register-rock.md, INDEX.md.

WHAT THIS DOES (and does NOT do):
- It mechanically cross-references the five letter markings against candidate name
  lists under three explicit rules (one-person two-initials / two-people one-letter /
  bare multiset coverage), so the J.M and S.G "hits" and the missing-L "negative" are
  confirmed by search rather than by eye.
- It is a TEST, not a finding. A match here is at most [SPECULATION] until sourced,
  and the whole Register Rock line is GATED on H11 (does the Fort Brennand third symbol
  actually depict the rock?). A clean negative (e.g. "no L anywhere") is a real,
  loggable finding.

INPUT PROVENANCE:
- Markings {LJ, SM, EC, J+M, S+J}: KNOWN [K6][K9], from threads 02/03 + connections.md.
- Register Rock name list: sourced (wiki B + reddeadreference blog B/C + our journal
  image), full table in locations/register-rock.md. No invented data.
- Short dev/notable list: only names ALREADY in the corpus (Houser founders; Adam
  Butterworth, K3). Flagged PROVISIONAL -- it is NOT the full credits, and per
  connections.md the dev-initials hypothesis is deliberately weighted down.

Run: `python experiments/name_match.py`   (Python 3, standard library only)
"""

from itertools import combinations

# --- The mystery markings -------------------------------------------------------
# (label, letters, style)  -- KNOWN [K6][K9]
# "bare" = carved pair (LJ, SM); "plus" = matches with a '+' connective (lovers' style).
MARKINGS = [
    ("LJ",  ("L", "J"), "bare"),   # Butcher Creek outhouse #4 (carved)
    ("SM",  ("S", "M"), "bare"),   # Butcher Creek outhouse #4 (carved)
    ("EC",  ("E", "C"), "matches"),  # Vetter's Echo (beside Black Widow card + Annabella letters)
    ("J+M", ("J", "M"), "plus"),   # Cornwall K&T (web-trail START pole)
    ("S+J", ("S", "J"), "plus"),   # Caliga Hall (Gray estate)
]
# Full letter multiset across all 5 markings: {C, E, J, J, J, L, M, M, S, S}
# (NB: the corpus previously wrote {C,E,J,J,L,M,S,S} -- that dropped J+M's two
# letters; this script recomputes from MARKINGS, so it is the source of truth.)
MULTISET = [l for _, pair, _ in MARKINGS for l in pair]
UNIQUE_LETTERS = sorted(set(MULTISET))
MARK_BY_LABEL = {label: pair for label, pair, _ in MARKINGS}

# --- Letter GROUPS [H12] (user 2026-06-13) --------------------------------------
# The five markings are NOT equally tied to the mystery; test them SEPARATELY rather
# than as one flat 10-letter set (see analysis/connections.md "Letter GROUPS"):
#   group1_carved     -- LJ, SM  : carved geometry on outhouse #4 (same technique K15,
#                                   beside tally-4 + Fort Brennand pointer) => firmest tie.
#   group2_matchstick -- EC, J+M, S+J : laid matchsticks, tied by co-location/props.
#   hybrid            -- LJ, SM, EC   : EC sits by the Black Widow spider card, so it
#                                       groups UP toward the carved pair (spider-flagged).
#   jplusM_node       -- J+M     : singled out -- its LOCATION (Cornwall K&T) is itself
#                                   the web-trail START node, so it is essential.
GROUPS = {
    "group1_carved":     ["LJ", "SM"],
    "group2_matchstick": ["EC", "J+M", "S+J"],
    "hybrid_LJ_SM_EC":   ["LJ", "SM", "EC"],
    "jplusM_node":       ["J+M"],
}


# --- Candidate names ------------------------------------------------------------
# Each entry: (display, [token initials in order], source_tag).
# Initials are taken from the carved tokens; a single-token name has one initial.
# Source: locations/register-rock.md "Complete inscription list" (sourced).
REGISTER_ROCK = [
    ("J. Brooks",        ["J", "B"],           "rock:full"),
    ("Frank Heck",       ["F", "H"],           "rock:full"),
    ("S. Gray",          ["S", "G"],           "rock:full"),   # Gray family -> Caliga Hall
    ("J. V. Henry",      ["J", "V", "H"],      "rock:full"),
    ("Jasper Munson",    ["J", "M"],           "rock:full"),
    ("A. West",          ["A", "W"],           "rock:full"),   # wiki-speculated 'Adam West' (unconfirmed)
    ("B. Ward",          ["B", "W"],           "rock:full"),   # wiki-speculated 'Burt Ward' (unconfirmed)
    ("C. Riley",         ["C", "R"],           "rock:full"),
    ("A. Pickel",        ["A", "P"],           "rock:full"),
    ("T. Bart",          ["T", "B"],           "rock:full"),
    ("R. Mack",          ["R", "M"],           "rock:full"),
    ("Doyle",            ["D"],                "rock:full"),
    ("Henry Matilda",    ["H", "M"],           "rock:full"),
    ("Mary",             ["M"],                "rock:full"),
    # Wiki-named outlaws -- may be alternate readings of marks above, not independent.
    ("Otis Miller",      ["O", "M"],           "rock:outlaw?"),
    ("Billy Midnight",   ["B", "M"],           "rock:outlaw?"),
    # Bare initial / short marks (no full name).
    ("mark: W.Y.B",      ["W", "Y", "B"],      "rock:mark"),
    ("mark: BM",         ["B", "M"],           "rock:mark"),
    ("mark: R.M",        ["R", "M"],           "rock:mark"),
    ("mark: R.S",        ["R", "S"],           "rock:mark"),
    ("mark: R.S.G",      ["R", "S", "G"],      "rock:mark"),
    ("mark: Jm",         ["J", "M"],           "rock:mark"),   # reads J.M
    ("mark: DOF",        ["D", "O", "F"],      "rock:mark"),
    ("mark: WSF",        ["W", "S", "F"],      "rock:mark"),
    ("mark: ORW",        ["O", "R", "W"],      "rock:mark"),
    ("mark: E M / S",    ["E", "M", "S"],      "rock:mark"),   # partial, cut off at edge
]

# PROVISIONAL -- corpus-named notable people only; NOT the full credits (see docstring).
DEV_NOTABLE = [
    ("Sam Houser",        ["S", "H"], "dev"),
    ("Dan Houser",        ["D", "H"], "dev"),
    ("Adam Butterworth",  ["A", "B"], "dev"),  # ex-Rockstar QA, K3
]

# Van der Linde gang roster (thread 07) -- the in-fiction character list connections.md
# asked for. Initials = first + last name. Source: Red Dead Wiki (B), underlying in-game (A).
# NB 'Dutch van der Linde' last initial is conventionally V (van); 'Linde' -> L is a stretch.
VDL_GANG = [
    ("Dutch van der Linde", ["D", "V"], "gang"),
    ("Hosea Matthews",      ["H", "M"], "gang"),
    ("Arthur Morgan",       ["A", "M"], "gang"),
    ("John Marston",        ["J", "M"], "gang"),
    ("Bill Williamson",     ["B", "W"], "gang"),
    ("Javier Escuella",     ["J", "E"], "gang"),
    ("Micah Bell",          ["M", "B"], "gang"),
    ("Charles Smith",       ["C", "S"], "gang"),
    ("Sean MacGuire",       ["S", "M"], "gang"),
    ("Lenny Summers",       ["L", "S"], "gang"),
    ("Sadie Adler",         ["S", "A"], "gang"),
    ("Abigail Roberts",     ["A", "R"], "gang"),
    ("Jack Marston",        ["J", "M"], "gang"),
    ("Molly O'Shea",        ["M", "O"], "gang"),
    ("Mary-Beth Gaskill",   ["M", "G"], "gang"),
    ("Tilly Jackson",       ["T", "J"], "gang"),
    ("Karen Jones",         ["K", "J"], "gang"),
    ("Susan Grimshaw",      ["S", "G"], "gang"),
    ("Simon Pearson",       ["S", "P"], "gang"),
    ("Orville Swanson",     ["O", "S"], "gang"),
    ("Leopold Strauss",     ["L", "S"], "gang"),
    ("Josiah Trelawny",     ["J", "T"], "gang"),
    ("Kieran Duffy",        ["K", "D"], "gang"),
    ("Jenny Kirk",          ["J", "K"], "gang"),
    ("Davey Callander",     ["D", "C"], "gang"),
    ("Mac Callander",       ["M", "C"], "gang"),
    ("Annabelle",           ["A"],      "gang"),
    # 'Uncle' has no surname/initial pair; omitted from initial-matching.
]


def initial_set(entry):
    """Set of letters appearing as ANY token-initial of a candidate."""
    return set(entry[1])


def rule_a_one_person(pair, names):
    """Marking = one person's two initials (order-insensitive).
    Matches a 2-token name whose two initials equal the pair, OR a mark whose letter
    set is exactly the pair."""
    want = set(pair)
    hits = []
    for disp, inits, tag in names:
        if len(inits) == 2 and set(inits) == want:
            hits.append((disp, tag))
        elif tag.endswith("mark") and set(inits) == want:
            hits.append((disp, tag))
    return hits


def rule_b_two_people(pair, names):
    """Marking = two people, one letter each. For each letter, list candidates that
    carry it as an initial."""
    return {l: [d for d, inits, _ in names if l in set(inits)] for l in pair}


def group_report(names, pool_label):
    """Per-group [H12] one-person (Rule A) summary against a name pool, so a reading
    that lands on the carved/spider-flagged letters but not the matchsticks (or the
    reverse) is visible rather than averaged away across the flat 10-letter set."""
    print(f"PER-GROUP [H12] -- Rule-A one-person hits vs {pool_label}")
    print("-" * 68)
    for gname, labels in GROUPS.items():
        letters = sorted(l for lb in labels for l in MARK_BY_LABEL[lb])
        hit_labels = []
        for lb in labels:
            if rule_a_one_person(MARK_BY_LABEL[lb], names):
                hit_labels.append(lb)
        cov = f"{len(hit_labels)}/{len(labels)} markings hit"
        detail = f"({', '.join(hit_labels)})" if hit_labels else "(none)"
        print(f"  {gname:18s} {{{','.join(letters)}}}  -> {cov} {detail}")
    print()


def main():
    ALL = REGISTER_ROCK + DEV_NOTABLE
    print("Mystery-letter <-> candidate-name matcher")
    print("=" * 68)
    print(f"Markings: {', '.join(m[0] for m in MARKINGS)}")
    print(f"Full multiset: {{{', '.join(sorted(MULTISET))}}}  "
          f"(unique: {', '.join(UNIQUE_LETTERS)})")
    print(f"Candidate pool: {len(REGISTER_ROCK)} Register Rock entries "
          f"+ {len(DEV_NOTABLE)} notable-dev (PROVISIONAL)")
    print("GATE: Register Rock relevance depends on H11 (unconfirmed).\n")

    # --- Rule A: marking as one person's two initials ---------------------------
    print("RULE A  -- marking = ONE person's two initials (order-insensitive)")
    print("-" * 68)
    for label, pair, _ in MARKINGS:
        hits = rule_a_one_person(pair, ALL)
        if hits:
            for disp, tag in hits:
                print(f"  {label:4s} -> HIT   {disp}  [{tag}]")
        else:
            print(f"  {label:4s} -> none")
    print()

    # --- Rule B: marking as two single-initial people ---------------------------
    print("RULE B  -- marking = TWO people, one letter each (Register Rock only)")
    print("-" * 68)
    for label, pair, _ in MARKINGS:
        by_letter = rule_b_two_people(pair, REGISTER_ROCK)
        parts = []
        for l in pair:
            who = by_letter[l]
            parts.append(f"{l}: {len(who)} ({', '.join(who[:3])}{'...' if len(who) > 3 else ''})"
                         if who else f"{l}: NONE")
        joined = "  |  ".join(parts)
        flag = "  <-- has an empty leg" if any(not by_letter[l] for l in pair) else ""
        print(f"  {label:4s}  {joined}{flag}")
    print()

    # --- Rule C: bare multiset coverage -----------------------------------------
    print("RULE C  -- does each mystery letter appear as ANY initial? (Register Rock)")
    print("-" * 68)
    rock_letters = set()
    for e in REGISTER_ROCK:
        rock_letters |= initial_set(e)
    for l in UNIQUE_LETTERS:
        present = l in rock_letters
        print(f"  {l}: {'present' if present else 'ABSENT'}")
    missing = [l for l in UNIQUE_LETTERS if l not in rock_letters]
    print()
    print(f"Letters in the mystery set MISSING from Register Rock: "
          f"{', '.join(missing) if missing else '(none)'}")
    print()

    # --- Van der Linde gang (thread 07) -----------------------------------------
    print("VAN DER LINDE GANG  (thread 07) -- the in-fiction character name list")
    print("-" * 68)
    print("RULE A  -- marking = ONE gang member's two initials (first + last):")
    for label, pair, _ in MARKINGS:
        hits = rule_a_one_person(pair, VDL_GANG)
        if hits:
            for disp, tag in hits:
                print(f"  {label:4s} -> HIT   {disp}  [{tag}]")
        else:
            print(f"  {label:4s} -> none")
    gang_letters = set()
    for e in VDL_GANG:
        gang_letters |= initial_set(e)
    gang_missing = [l for l in UNIQUE_LETTERS if l not in gang_letters]
    print("\nRULE C  -- each mystery letter present as a gang initial?")
    for l in UNIQUE_LETTERS:
        print(f"  {l}: {'present' if l in gang_letters else 'ABSENT'}")
    print(f"  -> MISSING from the gang: {', '.join(gang_missing) if gang_missing else '(none)'}")
    print()

    # --- Per-group view [H12] ---------------------------------------------------
    group_report(REGISTER_ROCK, "Register Rock (gated on H11)")
    group_report(VDL_GANG, "Van der Linde gang (thread 07)")

    # --- Summary ----------------------------------------------------------------
    print("SUMMARY (evidence, not fact -- [SPECULATION]; coincidence-odds caution applies)")
    print("-" * 68)
    print("  REGISTER ROCK (gated on H11):")
    print("    + J+M = 'Jasper Munson' + 'Jm' mark;  S+J <- 'S. Gray' (S leg, Caliga Hall)")
    print("    - no LJ/SM/EC as one person; L and a clean E.C absent.")
    print("  VAN DER LINDE GANG (thread 07):")
    print("    + EXACT one-person hits: SM = Sean MacGuire;  J+M/JM = John (& Jack) Marston")
    print("    + supplies the L the rock lacked (Lenny Summers / Leopold Strauss)")
    print("    - EC: no single E.C. member and no E-FIRST-NAME (E exists only as")
    print("      Javier Escuella's surname) -> EC stays the odd one out, matching its")
    print("      isolated graph component + the Annabella-desk negative (U16).")
    print("  NB ~27 gang members => some initial overlap is expected by chance; the")
    print("     signal is that the EXACT hits are MAJOR characters (Sean, John), not the")
    print("     proof. EC's persistent non-match across every name source is itself the")
    print("     interesting result.")


if __name__ == "__main__":
    main()

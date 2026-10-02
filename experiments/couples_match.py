#!/usr/bin/env python3
"""Couples matcher -- do the '+'-styled markings name documented in-game COUPLES?

QUESTION TESTED: U5 / U4, the S2/S3 lovers'-initials readings. Every prior name
test (name_match.py, thread 07) matched markings against INDIVIDUALS (one person's
first+last initials). But the display styling itself distinguishes two classes:
bare pairs (LJ, SM, EC) vs '+'-connected pairs (J+M, S+J) -- and the '+' form is
classic lovers'-carving syntax. The un-run test: match the '+' markings against
FIRST-NAME initial pairs of couples the game actually documents.

INPUT PROVENANCE (no invented data):
- Markings: KNOWN [K6][K9] (threads 02/03).
- Couples list: Red Dead Wiki (B-tier), core entries API-fetched and read verbatim
  on 2026-07-05 (source #86 in sources/sources.md); the remainder are long-settled
  wiki-documented relationships. Tags: 'fetched' = page read this pass;
  'established' = uncontroversial wiki-documented relationship, page not re-read.
- The list is NOT exhaustive -- RDR2 has no canonical couples registry. Coverage
  cap: main-cast romances + named minor-character couples we could source. A missed
  couple can only ADD matches, not remove the ones found.

WHAT THIS DOES: reports which markings match a documented couple's first-name
initials (unordered), then runs a seeded partner-reshuffle null to price the
match count. A hit is [SPECULATION] until independently sourced; the null keeps
us honest about how cheap initial coincidences are (the S16 lesson: P~=0.59).

Run: python experiments/couples_match.py   (Python 3, stdlib, deterministic)
"""
import random

# --- The five markings [K6][K9]; style is part of the data --------------------
MARKINGS = [
    ("LJ",  frozenset("LJ"), "bare"),
    ("SM",  frozenset("SM"), "bare"),
    ("EC",  frozenset("EC"), "bare"),   # matchsticks, but displayed WITHOUT '+'
    ("J+M", frozenset("JM"), "plus"),
    ("S+J", frozenset("SJ"), "plus"),
]

# --- Documented couples: (person A, person B, provenance, note) ---------------
COUPLES = [
    ("Joshua Burgess", "Miriam Wegner", "fetched",
     "EMERALD RANCH (web B45); lover shot dead Aug 1898; Miriam confined since"),
    ("Jake Adler", "Sadie Adler", "fetched",
     "married 1896-09-07; Jake murdered by O'Driscolls May 1899"),
    ("Cooper", "Lilly Millet", "fetched",
     "EMERALD RANCH ranch maid + her abusive lover (encounter + letter mention)"),
    ("Arthur Morgan", "Mary Linton", "fetched", "ex-fiance/ee"),
    ("Barry Linton", "Mary Linton", "fetched", "her late husband"),
    ("John Marston", "Abigail Roberts", "established", "the central couple"),
    ("Dutch van der Linde", "Annabelle", "fetched", "lover, killed by Colm"),
    ("Dutch van der Linde", "Molly O'Shea", "established", "camp relationship"),
    ("Hosea Matthews", "Bessie Matthews", "fetched", "late wife"),
    ("Beau Gray", "Penelope Braithwaite", "fetched",
     "the Gray/Braithwaite forbidden lovers -- AT the S+J estate families"),
    ("Cal Balfour", "Charlotte Balfour", "fetched", "Willard's Rest; Cal deceased"),
    ("Thomas Downes", "Edith Downes", "established", "the Downes farm"),
    ("Sean MacGuire", "Karen Jones", "established", "camp relationship"),
    ("Arthur Morgan", "Eliza", "established", "Isaac's mother"),
]


def first_initial(name: str) -> str:
    return name[0].upper()


def couple_pair(c) -> frozenset:
    return frozenset({first_initial(c[0]), first_initial(c[1])})


def report():
    print("Couples matcher -- '+' markings vs documented couples' first-name initials")
    print("=" * 76)
    print(f"{len(COUPLES)} documented couples (non-exhaustive; see docstring).\n")

    hits_by_marking = {}
    for label, want, style in MARKINGS:
        hits = [c for c in COUPLES if couple_pair(c) == want]
        hits_by_marking[label] = hits
        tag = "PLUS" if style == "plus" else "bare"
        if hits:
            for a, b, prov, note in hits:
                print(f"  {label:4s} [{tag}] -> HIT  {a} + {b}   ({prov}; {note})")
        else:
            print(f"  {label:4s} [{tag}] -> no documented couple")
    print()

    plus_hit = [l for l, w, s in MARKINGS if s == "plus" and hits_by_marking[l]]
    bare_hit = [l for l, w, s in MARKINGS if s == "bare" and hits_by_marking[l]]
    print(f"'+'-styled markings matching a couple: {len(plus_hit)}/2 {plus_hit}")
    print(f"bare markings matching a couple:       {len(bare_hit)}/3 {bare_hit}")
    print()

    # --- Null model: partner reshuffle (seeded, deterministic) ----------------
    # Keep the observed people (and thus the initial frequencies) fixed; break the
    # real pairings by shuffling the partner column. How often do BOTH '+' pairs
    # appear? How often do >=2 of the 5 marking-pairs appear at all?
    left = [first_initial(a) for a, b, _, _ in COUPLES]
    right = [first_initial(b) for a, b, _, _ in COUPLES]
    targets = {w for _, w, _ in MARKINGS}
    plus_targets = {w for _, w, s in MARKINGS if s == "plus"}

    rng = random.Random(0)
    N = 200_000
    both_plus = 0
    two_or_more = 0
    exact_config = 0  # both '+' pairs present AND no bare pair present
    for _ in range(N):
        r = right[:]
        rng.shuffle(r)
        pairs = {frozenset({l, x}) for l, x in zip(left, r)}
        got = targets & pairs
        if plus_targets <= pairs:
            both_plus += 1
            if not (got - plus_targets):
                exact_config += 1
        if len(got) >= 2:
            two_or_more += 1

    print("Partner-reshuffle null (seed 0, N=200,000):")
    print(f"  P(both J+M and S+J pairs appear)            ~= {both_plus / N:.3f}")
    print(f"  P(>=2 of the 5 marking-pairs appear)        ~= {two_or_more / N:.3f}")
    print(f"  P(exactly the two '+' pairs, no bare pair)  ~= {exact_config / N:.3f}"
          "   (post-hoc statistic -- weigh accordingly)")
    print()
    print("READ: the initial matches alone are CHEAP (J is the commonest initial in")
    print("the pool). The key observations are structural, outside the null:")
    print("  1. Styling alignment: the two markings drawn WITH the lovers' '+' are")
    print("     exactly the two with canonical couple readings; the three bare ones")
    print("     have none. The styling rule was fixed BEFORE the couples were sought.")
    print("  2. Thematic coherence: both hit-couples are TRAGIC -- the male partner")
    print("     violently killed (1898/1899), the woman left grieving/confined.")
    print("  3. Geography: Joshua+Miriam ARE the Emerald Ranch story -- a web node")
    print("     (B45) -- and the one in-game document narrating them (Letter to")
    print("     Miriam Wegner) spawns in the mail wagon SW of FORT WALLACE [K16].")
    print("  4. Control negative: Beau+Penelope (B,P) -- the flagship forbidden")
    print("     lovers at the Gray/Braithwaite estates -- match NO marking.")
    print("All [SPECULATION] until sourced (S45).")


if __name__ == "__main__":
    report()

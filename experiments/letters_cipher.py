#!/usr/bin/env python3
"""Cipher / anagram feasibility test for the mystery letter set.

QUESTION TESTED: U5 / S2 / S3 (and the investigator's 2026-06-13 point) -- if the
markings `LJ` `SM` `EC` `J+M` `S+J` are NOT a direct name list, are they a usable
ANAGRAM / CIPHER / CODE? See analysis/connections.md, threads/03 & 07, INDEX.md.

WHAT THIS DOES (and does NOT do):
- Structural feasibility only. It measures whether the full 10-letter multiset could
  plausibly be a single-word/phrase ANAGRAM (vowel budget), runs a subset-spell test
  against a provided candidate list, and renders the A1Z26 numeric form of each marking.
- It does NOT "solve" a cipher -- the space is underdetermined without an ordering key.
  A NEGATIVE here (e.g. "the set is too vowel-starved to anagram into English") is the
  loggable result; nothing it prints is [KNOWN].
- GROUPING NOTE [H12]: the whole-set anagram/vowel test below is necessarily run on all
  ten letters at once, so it cannot be split by group. But the per-marking A1Z26 block
  (section 3) is already group-aware -- read it against the GROUPS defined in
  name_match.py (group1 carved LJ/SM; group2 matchstick EC/J+M/S+J; hybrid LJ/SM/EC;
  J+M as its own node). The standing finding -- "read as PAIRS, not reshuffled" -- is what
  makes the per-group/per-pair view the right frame, not a global anagram.

INPUT PROVENANCE:
- Markings: KNOWN [K6][K9] (threads 02/03). Multiset recomputed from MARKINGS, not typed
  in (this is the script that caught the corpus's earlier {C,E,J,J,L,M,S,S} slip).
- CANDIDATE_TARGETS: PROVISIONAL illustrative list (no bundled dictionary in stdlib);
  marked as such. Add sourced candidates (gang/place names) as they arise.

Run: `python experiments/letters_cipher.py`   (Python 3, standard library only)
"""

from collections import Counter

# Markings -- KNOWN [K6][K9].  (label, "letters")
MARKINGS = [("LJ", "LJ"), ("SM", "SM"), ("EC", "EC"), ("J+M", "JM"), ("S+J", "SJ")]
LETTERS = "".join(m[1] for m in MARKINGS)          # recomputed, not hand-typed
MULTI = Counter(LETTERS)
VOWELS = set("AEIOU")

# PROVISIONAL candidate targets to subset-spell-test (NOT sourced as answers).
# Mix of gang names, place fragments, and short words to probe what the letters allow.
CANDIDATE_TARGETS = [
    # gang first names (thread 07) -- most need letters we don't have:
    "JOHN", "JACK", "SEAN", "MICAH", "JAVIER", "LENNY", "MOLLY", "JAMES", "JESSE",
    # place fragments:
    "EMERALD", "CALIGA", "ELYSIAN", "CORNWALL", "CLEMENS",
    # short words the set might allow (probe vowel limit):
    "MESS", "JESS", "LESS", "CELS", "JELL", "SMELL", "CLAMS", "MILES",
]


def can_spell(target, pool):
    """True if `target` is a multiset-subset of `pool` (a Counter). Exact if equal."""
    need = Counter(c for c in target.upper() if c.isalpha())
    return all(pool.get(ch, 0) >= n for ch, n in need.items()), (need == pool)


def main():
    print("Letter-set cipher / anagram feasibility test")
    print("=" * 64)
    sorted_letters = "".join(sorted(LETTERS))
    print(f"Markings: {', '.join(m[0] for m in MARKINGS)}")
    print(f"Multiset ({len(LETTERS)} letters): {{{', '.join(sorted_letters)}}}")
    freq = ", ".join(f"{c}x{n}" for c, n in sorted(MULTI.items()))
    print(f"Frequencies: {freq}")
    print()

    # --- 1. Vowel budget: can this be a natural-language anagram at all? ----------
    vcount = sum(n for c, n in MULTI.items() if c in VOWELS)
    ratio = vcount / len(LETTERS)
    print("1. ANAGRAM FEASIBILITY (vowel budget)")
    print("-" * 64)
    print(f"   Vowels: {vcount}/{len(LETTERS)} = {ratio:.0%}  (only '{''.join(sorted(c for c in MULTI if c in VOWELS))}')")
    print(f"   English text runs ~38-40% vowels; ~{vcount} vowel(s) across {len(LETTERS)} letters")
    print( "   with J x3 makes a single-word/phrase anagram of the WHOLE set implausible.")
    print( "   => If a cipher at all, the letters are far likelier meant as PAIRS")
    print( "      (initials/relationships) than reshuffled into words. [structural negative]")
    print()

    # --- 2. Subset-spell test against provisional candidates ----------------------
    print("2. SUBSET-SPELL TEST vs provisional candidates (NOT sourced answers)")
    print("-" * 64)
    spellable = []
    for t in CANDIDATE_TARGETS:
        ok, exact = can_spell(t, MULTI)
        if ok:
            spellable.append(t)
            print(f"   {t:8s} -> spellable{'  (EXACT multiset!)' if exact else ''}")
    if not spellable:
        print("   (none)")
    else:
        print(f"\n   Note: only vowel-'E' words clear the test (e.g. MESS/JESS/LESS) --")
        print( "   no name or place fragment with A/I/O/U can be formed. Reinforces (1).")
    print()

    # --- 3. A1Z26 numeric rendering of each marking -------------------------------
    print("3. A1Z26 NUMERIC FORM per marking (underdetermined -- recorded, not solved)")
    print("-" * 64)
    for label, letters in MARKINGS:
        nums = [ord(c) - 64 for c in letters]
        print(f"   {label:4s} -> {letters} -> {nums}  (sum {sum(nums)}, "
              f"diff {abs(nums[0]-nums[1]) if len(nums)==2 else '-'})")
    print( "   No obvious read (no match to Gertrude's 1237645112, the tallies 1-7, or")
    print( "   'five poles west'). Logged as a null pending an ordering key. [null]")
    print( "   *** ONE flag: EC -> E=5, C=3 == the 5 BLACK + 3 RED feather split [K13],")
    print( "       and EC is the marking beside the Black Widow card. Suggestive but")
    print( "       coincidence-prone (small ints; many pairs sum low) -> [SPECULATION]. ***")
    print()

    # --- Summary ------------------------------------------------------------------
    print("SUMMARY (evidence, not fact)")
    print("-" * 64)
    print("  * The 10-letter set is vowel-starved (1 vowel) and J-heavy (x3): it does")
    print("    NOT support a whole-set English anagram -> a global-anagram reading is a")
    print("    structural NEGATIVE.")
    print("  * Subset-spell yields only trivial E-words; nothing nameable -> same.")
    print("  * A1Z26 per-pair shows no link to the known number lines -> null for now.")
    print("  * Net: the markings are best read as PAIRS (initials / who-pairs-with-whom),")
    print("    NOT as letters to reshuffle. A positional/per-pair cipher stays OPEN but")
    print("    is underdetermined without an ordering key (feather order U0 / tally")
    print("    order / Gertrude's permutation are the candidate keys to supply next).")


if __name__ == "__main__":
    main()

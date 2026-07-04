#!/usr/bin/env python3
"""Mystery letter-pairs <-> full RDR2 credits matcher (the "dev initials" stress test).

QUESTION TESTED: U4 / U25 / S16 and the "dev-initials" counter-hypothesis
(analysis/connections.md, threads 02 & 03). If LJ/SM (carved outhouse) and
EC/J+M/S+J (matchsticks) are *developer initials*, who in the FULL ~6.3k-person
credits list do they match -- and are those people senior enough that anyone would
plausibly hide their initials in the world?

WHAT THIS DOES (and does NOT do):
- Parses rdr2-credits.txt (NAME / ROLE / blank-line records) and cross-references the
  two marking SETS against every credited person's first/last-name initials, writing
  one results file per set: each matched person as NAME then ROLE, grouped by marking
  and sorted senior-first to make elimination-by-role easy.
- It is a TEST, not a finding. Per the corpus, the dev-initials reading is deliberately
  weighted DOWN: with thousands of staff, *some* match for almost any 2-letter pair is
  near-certain, so a hit is weak evidence ([SPECULATION] at most). The loggable result
  is the COUNT -- how many people match, and how few are senior -- which quantifies
  exactly why "these are dev initials" is unconvincing.

MATCHING RULE (made explicit because the user flagged the ambiguity):
- ONE-PERSON reading, FORWARD-ONLY (user choice 2026-06-21): a person matches an
  ORDERED pair (X, Y) iff first-name initial == X AND last-name initial == Y, in the
  marking's written order. So "EC" = E.____ firstname, C.____ lastname ONLY; the
  reversed "C.____ firstname, E.____ lastname" is NOT counted.
- The TWO-PEOPLE reading (what the '+' in J+M / S+J might imply -- two separate
  honourees, one letter each) is NOT enumerated (it would be every J-person x every
  M-person = tens of thousands of pairs). Instead the per-letter POOL SIZES are printed
  in the summary, which is the relevant fact: the pools are huge, so a '+'-pair "match"
  is meaningless.

INPUT PROVENANCE:
- Markings {LJ,SM} KNOWN [K6]; {EC,J+M,S+J} KNOWN [K9]. From threads 02/03, connections.md.
- rdr2-credits.txt: user-supplied RDR2 end credits (NAME / ROLE / blank). C-tier as a
  name source, but the in-game credits themselves are A-tier provenance.

Seniority tier is a HEURISTIC keyword classifier to aid elimination -- NOT fact.

Run: `python experiments/credits_initials_match.py`   (Python 3, standard library only)
Outputs: experiments/results/outhouse_initials_matches.txt
         experiments/results/matchstick_initials_matches.txt
"""

import html
import os
import re
import unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CREDITS = os.path.join(HERE, os.pardir, "sources", "rdr2-credits.txt")
RESULTS = os.path.join(HERE, "results")

# --- The two marking SETS -------------------------------------------------------
# Each marking: (label, (letterX, letterY)). All pairs are distinct-letter.
OUTHOUSE = [   # carved, Butcher Creek outhouse #4 -- KNOWN [K6]
    ("LJ", ("L", "J")),
    ("SM", ("S", "M")),
]
MATCHSTICK = [  # laid matches -- KNOWN [K9]
    ("EC",  ("E", "C")),   # Vetter's Echo (beside Black Widow card)
    ("J+M", ("J", "M")),   # Cornwall K&T (web-trail START pole)
    ("S+J", ("S", "J")),   # Caliga Hall (Gray estate)
]

# --- Curated MANUAL matches (the auto first+last rule can't catch these) ---------
# People whose CREDITED form hides the matching initials -- e.g. a mononym whose real
# name supplies a second initial. Each is [SPECULATION] with explicit provenance; the
# auto rule deliberately skips single-token credits, so these are added by hand.
# Format: label -> [(credited_name, role, why/provenance)].
MANUAL_MATCHES = {
    "LJ": [
        ("Lazlow", "Director Audio Content, Rockstar Games",
         "Credited mononymously as 'Lazlow' = Jeffrey Crawford \"Lazlow\" Jones "
         "(Wikipedia, B/C). Community reading: LJ = Lazlow Jones. Tie is thin -- as "
         "Director of Audio Content you'd expect AUDIO-led clues; only the guitar near "
         "the trail end is audio-adjacent (user note, 2026-06-21). [SPECULATION]"),
    ],
}

# --- Seniority heuristic (clearly NOT fact) -------------------------------------
# Tiers, checked in order. Used only to sort/triage matches for elimination.
EXEC_KW   = ("Director", "Head of", "President", "Producer", "Chief",
             "Founder", "Owner", "Vice President")
LEAD_KW   = ("Lead", "Principal", "Manager", "Supervisor", "Boss")
SENIOR_KW = ("Senior",)
CRAFT_KW  = ("Programmer", "Designer", "Artist", "Engineer", "Animator",
             "Writer", "Composer", "Editor", "Analyst", "Researcher",
             "Technician", "Specialist", "Coordinator", "Modeler", "Sculptor")
# Everything else (QA Tester, Game Tester, Associate ... Tester, etc.) -> junior.

TIER_ORDER = {"exec": 0, "lead": 1, "senior": 2, "craft": 3, "junior": 4}
TIER_LABEL = {"exec": "EXEC/DIR", "lead": "LEAD", "senior": "SENIOR",
              "craft": "CRAFT", "junior": "junior"}


def classify(role):
    """Crude seniority tier from role keywords. Heuristic, not fact.
    'Associate ...' demotes an otherwise lead/principal title by one notch."""
    r = role
    if any(k in r for k in EXEC_KW):
        tier = "exec"
    elif any(k in r for k in LEAD_KW):
        tier = "lead"
    elif any(k in r for k in SENIOR_KW):
        tier = "senior"
    elif any(k in r for k in CRAFT_KW):
        tier = "craft"
    else:
        tier = "junior"
    # 'Associate'/'Assistant' downgrades a lead/principal claim.
    if tier in ("lead",) and re.match(r"^\s*(Associate|Assistant)\b", r):
        tier = "senior"
    return tier


def ascii_first_letter(token):
    """First A-Z letter of a token, accents stripped (Émile -> E, Zoë -> Z)."""
    decomposed = unicodedata.normalize("NFKD", token)
    for ch in decomposed:
        if "A" <= ch.upper() <= "Z" and ch.isalpha():
            return ch.upper()
    return None


def name_tokens(name):
    """Alphabetic name tokens, with 'nickname' / "nickname" tokens stripped first."""
    cleaned = re.sub(r"'[^']*'", " ", name)
    cleaned = re.sub(r'"[^"]*"', " ", cleaned)
    return [t for t in cleaned.split() if ascii_first_letter(t)]


def name_initials(name):
    """(first_initial, last_initial, [all token initials]) or None."""
    tokens = name_tokens(name)
    if not tokens:
        return None
    inits = [ascii_first_letter(t) for t in tokens]
    return inits[0], inits[-1], inits


def parse_credits(path):
    """Yield (name, role) records. Format: NAME / ROLE / blank line.
    Skips separator lines (=====, -----) and malformed blocks."""
    with open(path, encoding="utf-8") as fh:
        raw = html.unescape(fh.read())
    people, skipped = [], 0
    block = []
    def flush(block):
        nonlocal skipped
        lines = [ln.strip() for ln in block if ln.strip()]
        lines = [ln for ln in lines if not re.fullmatch(r"[=\-_*]{3,}", ln)]
        if len(lines) >= 2:
            people.append((lines[0], lines[1]))
        elif lines:
            skipped += 1
    for line in raw.splitlines():
        if line.strip() == "":
            flush(block)
            block = []
        else:
            block.append(line)
    flush(block)
    return people, skipped


def find_matches(people, pair):
    """FORWARD-ONLY one-person matches for an ordered pair (X, Y):
    first-name initial == X AND last-name initial == Y, in the marking's written
    order (e.g. EC => E firstname, C lastname -- the reversed 'C firstname, E
    lastname' is NOT a match). Returns list of (name, role, tier)."""
    x, y = pair
    out = []
    for name, role in people:
        ni = name_initials(name)
        if not ni:
            continue
        first, last, _ = ni
        if first == x and last == y:
            out.append((name, role, classify(role)))
    out.sort(key=lambda t: (TIER_ORDER[t[2]], t[1]))
    return out


def write_set_file(path, set_title, markings, people, matches_by_label):
    lines = []
    lines.append(f"# {set_title}")
    lines.append(f"# Source: rdr2-credits.txt ({len(people)} credited people)")
    lines.append("# Rule: FORWARD-ONLY -- first-name initial = X AND last-name initial = Y, "
                 "in the marking's written order")
    lines.append("#       (e.g. EC = E.____ firstname, C.____ lastname; reversed C/E is NOT a match).")
    lines.append("# Tier = seniority HEURISTIC to aid elimination, NOT fact.")
    lines.append("# A match here is [SPECULATION] at most -- with ~6.3k staff, some match "
                 "is near-certain (see summary).")
    lines.append("")
    for label, pair in markings:
        hits = matches_by_label[label]
        tier_counts = Counter(h[2] for h in hits)
        senior_n = sum(tier_counts[t] for t in ("exec", "lead", "senior"))
        manual = MANUAL_MATCHES.get(label, [])
        lines.append("=" * 70)
        lines.append(f"== {label}  (letters {pair[0]}/{pair[1]})  -- {len(hits)} auto matches "
                     f"({senior_n} senior+; {tier_counts['exec']} exec/dir, "
                     f"{tier_counts['lead']} lead)"
                     + (f" + {len(manual)} manual" if manual else "") + " ==")
        lines.append("=" * 70)
        lines.append("")
        if manual:
            lines.append("--- MANUAL (auto rule can't catch; provenance + [SPECULATION]) ---")
            for mname, mrole, why in manual:
                lines.append(f"{mname}   [manual]")
                lines.append(f"{mrole}")
                lines.append(f"    ^ {why}")
                lines.append("")
        current_tier = None
        for name, role, tier in hits:
            if tier != current_tier:
                lines.append(f"--- {TIER_LABEL[tier]} ---")
                current_tier = tier
            lines.append(f"{name}")
            lines.append(f"{role}")
            lines.append("")
        if not hits:
            lines.append("(no matches)")
            lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main():
    os.makedirs(RESULTS, exist_ok=True)
    people, skipped = parse_credits(CREDITS)

    print("RDR2 credits <-> mystery letter-pairs  (dev-initials stress test)")
    print("=" * 70)
    print(f"Parsed {len(people)} people from rdr2-credits.txt ({skipped} blocks skipped).")
    print()

    # Per-letter pools (the '+' / two-people reading) -----------------------------
    first_pool = Counter()
    last_pool = Counter()
    any_pool = Counter()
    for name, _ in people:
        ni = name_initials(name)
        if not ni:
            continue
        f, l, alll = ni
        first_pool[f] += 1
        last_pool[l] += 1
        for c in set(alll):
            any_pool[c] += 1

    all_markings = OUTHOUSE + MATCHSTICK
    matches_by_label = {lbl: find_matches(people, pair) for lbl, pair in all_markings}

    print("ONE-PERSON matches (FORWARD-ONLY: X firstname + Y lastname):")
    print("-" * 70)
    for lbl, pair in all_markings:
        hits = matches_by_label[lbl]
        tc = Counter(h[2] for h in hits)
        senior_n = tc["exec"] + tc["lead"] + tc["senior"]
        print(f"  {lbl:4s} ({pair[0]}.firstname + {pair[1]}.lastname) -> {len(hits):4d} people "
              f"({senior_n} senior+, of which {tc['exec']} exec/dir, {tc['lead']} lead)")
    print()

    print("TWO-PEOPLE pool sizes (why a '+'-pair 'match' is meaningless):")
    print("-" * 70)
    for letter in sorted(set(l for _, p in all_markings for l in p)):
        print(f"  {letter}: {first_pool[letter]:4d} people with this FIRST-name initial, "
              f"{last_pool[letter]:4d} with this LAST-name initial")
    print("  -> e.g. J+M as 'two people' = (J-first x M-last) = "
          f"{first_pool['J'] * last_pool['M']:,} possible pairings. Unfalsifiable.")
    print()

    # Mononyms -- single-name credits (lead list: a stage name may hide a fuller real
    # name whose initials match, e.g. Lazlow -> Lazlow Jones -> LJ). --------------
    mononyms = sorted(
        ((name, role) for name, role in people if len(name_tokens(name)) == 1),
        key=lambda nr: nr[0].lower())
    mono_lines = [
        "# Single-name (mononym) credits -- LEAD LIST, not matches.",
        f"# Source: rdr2-credits.txt ({len(people)} people); {len(mononyms)} credited "
        "by a single name.",
        "# Why they matter: a mononym/stage name can hide a fuller REAL name whose "
        "initials match a marking",
        "# (e.g. 'Lazlow' = Jeffrey Crawford \"Lazlow\" Jones -> LJ). The auto first+last "
        "rule skips these,",
        "# so they need a by-hand real-name check. Inclusion here is NOT a match. "
        "[SPECULATION] until sourced.",
        "",
    ]
    for name, role in mononyms:
        mono_lines.append(name)
        mono_lines.append(role)
        mono_lines.append("")
    with open(os.path.join(RESULTS, "single_name_credits.txt"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(mono_lines))

    print(f"MONONYMS: {len(mononyms)} people credited by a single name "
          "(lead list -> results/single_name_credits.txt).")
    manual_total = sum(len(v) for v in MANUAL_MATCHES.values())
    print(f"MANUAL matches curated: {manual_total} "
          f"({', '.join(f'{k}:{len(v)}' for k, v in MANUAL_MATCHES.items())}).")
    print()

    write_set_file(os.path.join(RESULTS, "outhouse_initials_matches.txt"),
                   "Outhouse carved initials (LJ, SM) [K6] -- credits matches",
                   OUTHOUSE, people, matches_by_label)
    write_set_file(os.path.join(RESULTS, "matchstick_initials_matches.txt"),
                   "Matchstick initials (EC, J+M, S+J) [K9] -- credits matches",
                   MATCHSTICK, people, matches_by_label)

    print("Wrote:")
    print("  experiments/results/outhouse_initials_matches.txt   (LJ, SM)")
    print("  experiments/results/matchstick_initials_matches.txt (EC, J+M, S+J)")
    print("  experiments/results/single_name_credits.txt         (mononym lead list)")
    print()
    print("READING (evidence, not fact):")
    print("-" * 70)
    print("  The point is the COUNTS, not any individual name. If even the rarest")
    print("  pair matches dozens of credited people -- and only a handful are senior")
    print("  enough to plausibly be honoured in-world -- then 'these are dev initials'")
    print("  is unfalsifiable and weak. The senior-tier shortlist per marking is the")
    print("  only part worth a human look; everything below it is elimination fodder.")


if __name__ == "__main__":
    main()

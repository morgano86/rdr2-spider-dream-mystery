#!/usr/bin/env python3
"""Dev-initials COHERENCE test -- does the dev-tribute reading have a single home?

QUESTION TESTED: U4 / U25 / S16 and the "dev-initials" counter-hypothesis, one step
past the COUNTS. `credits_initials_match.py` already showed a dev-initials match is
near-certain by chance (LJ 5, SM 87, EC 13, J+M 58, S+J 22 forward-only) -- so the
*existence* of a match is weak. This script asks the only question that could make the
dev-tribute reading non-random: if someone hid five honourees' initials across the
world, you'd expect a SINGLE coherent group -- one studio, or one discipline (and
above all the WORLD/DESIGN/secrets people who actually build hidden content). So:

  Is there ANY one-person-per-marking assignment (cherry-picking the most senior match
  each) such that all five markings share a STUDIO, or a DISCIPLINE, or a world-building
  team? If even the best case is scattered, that is a real, loggable nail in the
  dev-tribute reading -- complementing "unfalsifiable by counts" with "incoherent by
  organisation". A positive (a small shared studio/team across all 5) would, conversely,
  be the first thing that made dev-initials worth a second look.

WHAT THIS DOES (and does NOT do):
- Reuses the parser + matcher from credits_initials_match.py (no re-implementation, no
  new data). For each marking it takes the SENIOR+ matches (exec/dir, lead, senior),
  extracts each person's STUDIO (the ", Rockstar <X>" tail) and a coarse DISCIPLINE
  bucket from role keywords, and computes set intersections across the 5 markings.
- It is a TEST, not a finding. Studio/discipline buckets are heuristics. A shared
  *large* studio (Rockstar North is the biggest, so it appears almost everywhere) is
  NOT evidence of coherence -- the script flags studio size so a North-everywhere result
  is read correctly. The discriminating test is the WORLD-BUILDING discipline.

INPUT PROVENANCE:
- rdr2-credits.txt (6,345 people) -- user-supplied RDR2 end credits. Markings KNOWN
  [K6]/[K9]. Same inputs as credits_initials_match.py; nothing invented.

Run: `python experiments/credits_initials_coherence.py`   (Python 3, stdlib only)
Output: experiments/results/credits_initials_coherence.md (+ stdout summary)
"""

import os
import re
from collections import Counter, defaultdict

from credits_initials_match import (
    OUTHOUSE, MATCHSTICK, parse_credits, find_matches, CREDITS, RESULTS,
)

SENIOR_TIERS = ("exec", "lead", "senior")          # the only tiers worth a human look
ALL_MARKINGS = OUTHOUSE + MATCHSTICK                # LJ, SM, EC, J+M, S+J

# --- Studio: the ", Rockstar <Studio>" tail of a role string --------------------
STUDIO_RE = re.compile(r"Rockstar\s+([A-Za-z .&'-]+?)\s*$")


def studio_of(role):
    m = STUDIO_RE.search(role)
    return ("Rockstar " + m.group(1).strip()) if m else "(unknown)"


# --- Discipline: coarse bucket from role keywords (checked in order) ------------
# WORLD = the people who actually author hidden in-world content (design + the
# environment/world-art that places props/carvings). This is the bucket that matters
# for an Easter-egg tribute; the rest are support/business/QA.
DISCIPLINE_KW = [
    ("World/Design", ("World", "Population", "Open World", "Mission", "Systems Design",
                      "Design Director", "Designer", "Design Producer", "Content Design",
                      "Exploration", "Ambient Content", "Gameplay")),
    ("Environment Art", ("Environment", "Props", "Interiors", "Set ", "World Art")),
    ("Other Art", ("Art Director", "Artist", "Graphic", "Illustrat", "Characters",
                   "Concept", "2D", "UI/UX", "UX")),
    ("Animation", ("Animat", "Motion Capture", "Blendshape", "Rigging", "Gesture")),
    ("Audio", ("Audio", "Music", "Sound", "Dialogue", "Voice")),
    ("Cinematics/Media", ("Cinematic", "Video", "Photography", "In-Game Media",
                          "In-World Photography", "Continuity", "Compositor", "Nuke")),
    ("Programming", ("Programmer", "Engineer", "DevOps", "Tools", "AI/Gameplay",
                     "Software", "Graphics Programmer", "Network")),
    ("QA", ("QA", "Tester", "Compliance", "Build Verification")),
    ("Production", ("Producer", "Production", "Coordinator", "Project Manager",
                    "Release Management")),
    ("IT/Ops", ("Network Operations", "NOC", "Systems Administrator", "Systems Engineer",
                "Data Engineering", "Facilities", "Workplace", "Housekeeping",
                "Information Technology", "IT")),
    ("HR/Business", ("HR", "Talent", "Marketing", "Advertising", "Partnerships",
                     "Brand", "Learning", "Finance", "Financial", "Legal", "Community",
                     "Operations", "Administrator")),
]
WORLD_BUILDING = {"World/Design", "Environment Art"}


def discipline_of(role):
    for label, kws in DISCIPLINE_KW:
        if any(k in role for k in kws):
            return label
    return "Other"


def senior_matches(people, pair):
    return [(n, r, t) for (n, r, t) in find_matches(people, pair) if t in SENIOR_TIERS]


def main():
    os.makedirs(RESULTS, exist_ok=True)
    people, _ = parse_credits(CREDITS)

    # Studio sizes (to flag that a shared LARGE studio is not evidence of coherence).
    studio_size = Counter(studio_of(r) for _, r in people)

    # Per-marking senior pools, with studio + discipline tags.
    pool = {}
    for label, pair in ALL_MARKINGS:
        rows = []
        for n, r, t in senior_matches(people, pair):
            rows.append((n, r, t, studio_of(r), discipline_of(r)))
        pool[label] = rows

    studios_by_mark = {lbl: {row[3] for row in rows} for lbl, rows in pool.items()}
    discs_by_mark = {lbl: {row[4] for row in rows} for lbl, rows in pool.items()}
    world_marks = {lbl for lbl, rows in pool.items()
                   if any(row[4] in WORLD_BUILDING for row in rows)}

    # Coherence intersections across ALL five markings.
    common_studios = set.intersection(*studios_by_mark.values())
    common_discs = set.intersection(*discs_by_mark.values())

    # World-building + shared studio: the strongest possible dev-tribute story.
    world_studio_by_mark = {
        lbl: {row[3] for row in rows if row[4] in WORLD_BUILDING}
        for lbl, rows in pool.items()
    }
    world_all_five = all(world_studio_by_mark[lbl] for lbl, _ in ALL_MARKINGS)
    world_common_studio = (set.intersection(*world_studio_by_mark.values())
                           if world_all_five else set())

    out = []
    p = out.append
    p("# Result -- dev-initials COHERENCE test (`credits_initials_coherence.py`)")
    p("")
    p("**Question.** Past the counts: if the five markings were a dev tribute, do their")
    p("senior matches share a single home -- one studio, one discipline, or a world-building")
    p("team? Tests U4/U25/S16 (the dev-initials counter-hypothesis). [SPECULATION] at most.")
    p("")
    p(f"Source: rdr2-credits.txt ({len(people)} people). Senior+ tiers only "
      "(exec/dir, lead, senior).")
    p("")
    p("## Per-marking senior pool: studios and disciplines")
    p("")
    p("| Marking | senior+ | distinct studios | disciplines (senior pool) | world-building? |")
    p("|---------|--------:|------------------|---------------------------|-----------------|")
    for label, pair in ALL_MARKINGS:
        rows = pool[label]
        discs = Counter(row[4] for row in rows)
        disc_str = ", ".join(f"{d}×{c}" for d, c in discs.most_common())
        p(f"| `{label}` | {len(rows)} | {len(studios_by_mark[label])} | {disc_str or '-'} "
          f"| {'YES' if label in world_marks else 'no'} |")
    p("")
    p("## Coherence intersections (across ALL five markings)")
    p("")
    p(f"- **Common studio across all 5 senior pools:** "
      f"{', '.join(sorted(common_studios)) if common_studios else 'NONE'}")
    if common_studios:
        sizes = ", ".join(f"{s} ({studio_size[s]} credited)" for s in sorted(common_studios))
        p(f"  - size check (a shared *large* studio is not evidence): {sizes}")
        biggest = max(studio_size, key=studio_size.get)
        p(f"  - for reference the biggest studio is **{biggest}** "
          f"({studio_size[biggest]} credited) -- it appears in most pools by sheer size.")
    p(f"- **Common discipline across all 5 senior pools:** "
      f"{', '.join(sorted(common_discs)) if common_discs else 'NONE'}")
    p(f"- **World-building (World/Design or Environment Art) senior match in every "
      f"marking?** {'YES' if world_all_five else 'NO'} "
      f"(have it: {', '.join(sorted(world_marks)) or 'none'}; "
      f"missing: {', '.join(lbl for lbl, _ in ALL_MARKINGS if lbl not in world_marks) or 'none'})")
    if world_all_five:
        p(f"  - **shared studio among those world-builders:** "
          f"{', '.join(sorted(world_common_studio)) if world_common_studio else 'NONE'}")
    p("")
    p("## World-building senior matches, listed (the only people who plausibly hide world content)")
    p("")
    for label, pair in ALL_MARKINGS:
        wb = [row for row in pool[label] if row[4] in WORLD_BUILDING]
        if wb:
            p(f"- **`{label}`**")
            for n, r, t, st, d in wb:
                p(f"  - {n} — {r}  *({d})*")
        else:
            p(f"- **`{label}`** — *no world-building senior match at all*")
    p("")
    p("## Reading (evidence, not fact -- [SPECULATION])")
    p("")
    p("- The dev-tribute reading needs a single coherent group; the test asks whether one")
    p("  exists even in the best case (cherry-picking the most senior match per marking).")
    p("- A shared **large** studio is *not* coherence -- Rockstar North is so big it lands in")
    p("  almost every pool by chance. The discriminating question is the **world-building**")
    p("  row: do design/environment people -- the ones who actually place hidden carvings --")
    p("  appear for *every* marking, and could they be the same office? If not, the tribute")
    p("  has no plausible authoring team, which is a stronger objection than the raw counts.")
    p("")
    p("This neither confirms nor refutes any name; it characterises whether dev-initials is")
    p("even *organisationally* coherent, complementing `credits_initials_match.py` (counts).")

    path = os.path.join(RESULTS, "credits_initials_coherence.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    # --- stdout summary ---------------------------------------------------------
    print("Dev-initials COHERENCE test")
    print("=" * 68)
    print(f"Parsed {len(people)} people. Senior+ pools per marking:")
    for label, pair in ALL_MARKINGS:
        rows = pool[label]
        print(f"  {label:4s} senior+={len(rows):3d}  studios={len(studios_by_mark[label]):2d}  "
              f"world-building={'YES' if label in world_marks else 'no '}  "
              f"discs={sorted(discs_by_mark[label])}")
    print()
    print(f"Common studio across all 5 senior pools : "
          f"{sorted(common_studios) if common_studios else 'NONE'}")
    print(f"Common discipline across all 5          : "
          f"{sorted(common_discs) if common_discs else 'NONE'}")
    print(f"World-building senior match in EVERY marking? "
          f"{'YES' if world_all_five else 'NO'}")
    if not world_all_five:
        missing = [lbl for lbl, _ in ALL_MARKINGS if lbl not in world_marks]
        print(f"  -> markings with NO world-building senior match: {missing}")
    elif world_common_studio:
        print(f"  -> and they share studio: {sorted(world_common_studio)}")
    else:
        print("  -> but they share NO single studio (scattered offices).")
    print()
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

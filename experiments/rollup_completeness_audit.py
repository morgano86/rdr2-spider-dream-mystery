#!/usr/bin/env python3
"""Rollup-completeness audit — cross-check INDEX.md against the three findings/ rollups.

CLAUDE.md invariant under test:
  - every K# in INDEX appears in findings/known-facts.md
  - every U# in INDEX appears in findings/unknowns.md
  - every H# and S# in INDEX appears in findings/speculation.md
  - and vice-versa: no rollup carries an ID that INDEX doesn't register.

This is a MECHANICAL presence check (does the ID string appear at all), not a
semantic one — it can't tell whether the rollup text is in sync, only whether an
ID is missing outright. Deterministic, stdlib-only, no inputs beyond the repo.

Run from the repo root:  python experiments/rollup_completeness_audit.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROLLUPS = {
    "K": ROOT / "findings" / "known-facts.md",
    "U": ROOT / "findings" / "unknowns.md",
    "H": ROOT / "findings" / "speculation.md",
    "S": ROOT / "findings" / "speculation.md",
}

# IDs like K1, K13a, U0, H22, S42 — bracketed or bare. Word-boundary guarded so
# S42 doesn't match inside S420. Excludes source refs (#78) and file names.
ID_RE = re.compile(r"\b([KUHS])(\d+[a-z]?)\b")

# Tokens that match the ID pattern but are not claim IDs (none known today;
# keep the escape hatch so false positives get pinned here, not hand-waved).
FALSE_POSITIVES: set[str] = set()


def ids_in(text: str) -> set[str]:
    return {
        f"{m.group(1)}{m.group(2)}"
        for m in ID_RE.finditer(text)
        if f"{m.group(1)}{m.group(2)}" not in FALSE_POSITIVES
    }


def index_registered_ids(text: str) -> set[str]:
    """IDs that have their own registry ROW in INDEX.md (first cell of a table row)."""
    out = set()
    for line in text.splitlines():
        m = re.match(r"\|\s*([KUHS]\d+[a-z]?)\s*\|", line)
        if m:
            out.add(m.group(1))
    return out


def main() -> int:
    index_text = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    registered = index_registered_ids(index_text)

    rollup_ids = {}  # prefix -> ids present anywhere in that rollup file
    for prefix, path in ROLLUPS.items():
        rollup_ids[prefix] = ids_in(path.read_text(encoding="utf-8"))

    problems = []

    # Direction 1: registered in INDEX but absent from its rollup.
    for claim_id in sorted(registered):
        prefix = claim_id[0]
        if claim_id not in rollup_ids[prefix]:
            problems.append(
                f"MISSING-FROM-ROLLUP: {claim_id} has an INDEX row but never "
                f"appears in {ROLLUPS[prefix].relative_to(ROOT)}"
            )

    # Direction 2: an ID of the rollup's own type present there but not registered.
    # (Cross-references to other types inside a rollup are fine and expected.)
    own_type = {"known-facts.md": "K", "unknowns.md": "U", "speculation.md": "HS"}
    for fname, prefixes in own_type.items():
        path = ROOT / "findings" / fname
        present = ids_in(path.read_text(encoding="utf-8"))
        for claim_id in sorted(present):
            if claim_id[0] in prefixes and claim_id not in registered:
                problems.append(
                    f"UNREGISTERED: {claim_id} appears in findings/{fname} "
                    f"but has no INDEX.md row"
                )

    print(f"INDEX rows: {len(registered)} "
          f"(K {sum(1 for i in registered if i[0]=='K')}, "
          f"U {sum(1 for i in registered if i[0]=='U')}, "
          f"H {sum(1 for i in registered if i[0]=='H')}, "
          f"S {sum(1 for i in registered if i[0]=='S')})")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nOK: every registered ID appears in its rollup, and every "
          "own-type ID in a rollup is registered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Gertrude's numbers -- a systematic cipher/encoding harness ([U6]/[S5]/[K23]).

QUESTION TESTED: U6 (do Gertrude's numbers encode anything?) / S5 (the cipher-key
reading) / K23 (the confirmed digit string). The corpus has tried this BY HAND twice
(connections.md): "attempt A" = A1Z26 by eye (null), "attempt B" = read the 7 tally
nodes in the number's order (blocked -- no per-node content to reorder). It has never
been run as a SYSTEMATIC harness, and two readings have never been tested at all:
  (1) a PHONE-KEYPAD / T9 reading -- directly invited by the GTA crossover, where the
      same string is a "Nazar Speaks" machine number players literally CALL BACK
      ([K23]/gta-rdr2-crossover.md). "Call the number" => read it on a phone keypad.
  (2) the PERMUTATION STRUCTURE of the opening `1,2,3,7,6,4,5` -- it is exactly a
      permutation of 1-7 (the tally range). Its CYCLE STRUCTURE says precisely HOW it
      would reorder 7 nodes, which is the missing half of attempt B.

WHAT THIS DOES / DOES NOT DO:
- Runs a battery of deterministic decodings on the CONFIRMED string and reports each
  as null / flag, so the long-open "cipher harness for Gertrude's numbers" task gets a
  single logged result instead of scattered hand-notes.
- It is a TEST, not a finding. Per CLAUDE.md and the #43 hoax expose's own warning --
  "you can get just about any result if you pick the right set of numbers" -- ANY
  positive here is [SPECULATION] at most and coincidence-prone (a 10-digit string has
  many readings). A NULL across many transforms is the real, loggable result. Nothing
  here is promoted; this is upstream of the [K16] frontier and the spider-link itself
  is undecided ([U6]).

INPUT PROVENANCE (cite, never invent):
- CONFIRMED [K23], B-tier (GamesRadar/PCGamesN/TheGamer/SVG): the opening string
  `1,2,3,7,6,4,5,1,1,2` = `1237645112`. The opening SEVEN `1,2,3,7,6,4,5` is solid
  under either tail parsing ("...5,1,1,2" journalism vs "...5,11,2" our audio).
- PROVISIONAL (transcription-only, [U6], thread 04): the fuller hand transcription
  `1,2,3,7,6,4,5,11,2,1,2,10,3`. Marked PROVISIONAL inline; tests on it inherit that
  uncertainty and are reported separately.

Run: `python experiments/gertrude_cipher.py`   (Python 3, standard library only)
Output: stdout summary + experiments/results/gertrude_cipher.md
"""

import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

# --- Inputs ---------------------------------------------------------------------
# CONFIRMED [K23]: the digit string as B-tier journalism + the Nazar machine give it.
CONFIRMED = [1, 2, 3, 7, 6, 4, 5, 1, 1, 2]            # "1237645112"
OPENING7 = [1, 2, 3, 7, 6, 4, 5]                      # the part solid under any parsing
# PROVISIONAL (U6): the fuller hand transcription incl. the rambling tail. Do NOT trust
# the tail; reported separately so a tail-dependent "hit" can't masquerade as solid.
PROVISIONAL_FULL = [1, 2, 3, 7, 6, 4, 5, 11, 2, 1, 2, 10, 3]   # PROVISIONAL (U6)

# --- Mystery number anchors to cross-reference against (all sourced) -------------
# Bare counts/structure the numbers might index. Sourced in the corpus as cited.
ANCHORS = {
    "Butcher Creek tallies (1-5) [K4]": [1, 2, 3, 4, 5],
    "Fort Brennand tallies (6,7) [K7]": [6, 7],
    "all tallies 1-7": [1, 2, 3, 4, 5, 6, 7],
    "feather split 5 black / 3 red [K13]": [5, 3],
    "8 webs [K13a]": [8],
    "five poles west [K12]": [5],
}

# A1Z26: 1->A ... 26->Z (0 and >26 are undefined; mark them).
def a1z26(seq):
    out = []
    for n in seq:
        if 1 <= n <= 26:
            out.append(chr(ord("A") + n - 1))
        else:
            out.append("?")
    return "".join(out)

# Telephone keypad (ITU / classic): 1 and 0 carry NO letters (word breaks).
KEYPAD = {
    "2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL",
    "6": "MNO", "7": "PQRS", "8": "TUV", "9": "WXYZ",
    "1": "", "0": "",
}

# Small CURATED target list for the keypad reverse-check (word -> its keypad digits).
# This is the honest direction for a stdlib-only test: instead of enumerating millions
# of decodings against a dictionary we don't ship, we ask "do any mystery-relevant words
# DIAL to digits that appear in the string?" -- limited, but deterministic and provenance
# is just the keypad. A miss here means "not among THESE words", not "impossible".
KEYPAD_TARGETS = [
    "WEB", "SPIDER", "DREAM", "WEBS", "FEATHER", "BIRD", "EAGLE", "GIANT",
    "NAZAR", "GERTRUDE", "SECRET", "CODE", "KEY", "MAP", "NORTH", "WEST",
    "FORT", "WALLACE", "FROG", "SOUL", "DEATH",
]


def word_to_keypad(word):
    digits = []
    for ch in word.upper():
        for d, letters in KEYPAD.items():
            if ch in letters:
                digits.append(d)
                break
        else:
            return None  # a letter with no key (shouldn't happen for A-Z)
    return "".join(digits)


def keypad_runs(seq):
    """Maximal letter-runs of the string, split on 1 and 0 (no letters)."""
    s = "".join(str(n) for n in seq if 0 <= n <= 9)  # only single digits dial
    runs, cur = [], ""
    for ch in s:
        if KEYPAD[ch]:
            cur += ch
        else:
            if cur:
                runs.append(cur)
            cur = ""
    if cur:
        runs.append(cur)
    return s, runs


def permutation_cycles(perm):
    """Cycle decomposition of a 1-based permutation given as the ordered value list.
    perm[i] = value placed at position i+1. Returns (fixed_points, cycles)."""
    n = len(perm)
    pos = {i + 1: perm[i] for i in range(n)}        # position -> value (the map)
    seen, cycles = set(), []
    for start in range(1, n + 1):
        if start in seen:
            continue
        cyc, x = [], start
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = pos[x]
        if len(cyc) > 1:
            cycles.append(cyc)
    fixed = [i for i in range(1, n + 1) if pos[i] == i]
    return fixed, cycles


def main():
    os.makedirs(RESULTS, exist_ok=True)
    out, p = [], lambda s="": out.append(s)

    p("# Result -- Gertrude's numbers cipher harness (`gertrude_cipher.py`)")
    p("")
    p("Systematic battery on the **confirmed** string `1237645112` ([K23], B-tier) plus")
    p("the **provisional** tail ([U6], transcription-only). Tests U6/S5. Per the #43 hoax")
    p("expose's own warning -- *\"you can get any result if you pick the right numbers\"* --")
    p("every positive below is **coincidence-prone [SPECULATION]**; the key result")
    p("is the **null landscape**. Nothing here is promoted; upstream of the [K16] frontier.")
    p("")
    p(f"- CONFIRMED [K23]: `{CONFIRMED}`  (opening seven `{OPENING7}` solid under any parsing)")
    p(f"- PROVISIONAL [U6]: `{PROVISIONAL_FULL}`  (tail transcription-only -- do not trust)")
    p("")

    # --- 1. A1Z26 (reproduce hand "attempt A", now on the CONFIRMED digits) -------
    p("## 1. A1Z26 letter cipher (1->A ... 26->Z) -- reproduces hand attempt A")
    conf_a = a1z26(CONFIRMED)
    prov_a = a1z26(PROVISIONAL_FULL)
    p(f"- CONFIRMED `1237645112` -> **{conf_a}**")
    p(f"- PROVISIONAL full       -> **{prov_a}**  *(tail-dependent letters K/J from 11/10 are PROVISIONAL)*")
    p("- Reading: no English word/phrase; opens `ABC...` then scatters. **NULL** "
      "(confirms attempt A; the late `J` only exists in the untrusted tail).")
    p("")

    # --- 2. Phone-keypad / T9 (NEW -- motivated by the GTA 'call back' mechanic) ---
    p("## 2. Phone-keypad / T9 reading (NEW) -- the \"call the number back\" reading")
    s, runs = keypad_runs(CONFIRMED)
    p(f"- The GTA \"Nazar Speaks\" machine makes `1237645112` a number you **call back** "
      f"([K23]). On a keypad, **1 carries no letters** (word breaks), so the string "
      f"`{s}` splits into letter-runs: **{runs}**.")
    # forward: enumerate run decodings only if short; report combinatorial size
    sizes = []
    for r in runs:
        c = 1
        for ch in r:
            c *= len(KEYPAD[ch])
        sizes.append((r, c))
    p("  - run decodings (no shipped dictionary -> sizes only): "
      + ", ".join(f"`{r}`={c} combos" for r, c in sizes)
      + ". The 6-letter run can't be exhaustively English-checked stdlib-only; "
      "reverse-check below is the deterministic test.")
    # reverse: do mystery target words DIAL to substrings of the string?
    # classify each hit: WITHIN a single letter-run (windowed) vs CROSSES a 1/0 break.
    hits = []
    digit_str = "".join(str(n) for n in CONFIRMED)
    run_spans, cursor = [], 0
    for r in runs:                       # locate each run's [start,end) in the string
        i = digit_str.index(r, cursor)
        run_spans.append((i, i + len(r)))
        cursor = i + len(r)
    for w in KEYPAD_TARGETS:
        d = word_to_keypad(w)
        if d and d in digit_str:
            idx = digit_str.index(d)
            within = any(a <= idx and idx + len(d) <= b for a, b in run_spans)
            full_run = any(idx == a and idx + len(d) == b for a, b in run_spans)
            hits.append((w, d, idx, within, full_run))
    p("  - reverse-check (mystery word -> keypad digits -> is it IN the string?):")
    if hits:
        for w, d, idx, within, full_run in hits:
            if full_run:
                kind = "**IS a whole letter-run** (the cleanest possible keypad hit)"
            elif within:
                kind = ("a **windowed** sub-decode -- it sits inside the `237645` run but "
                        "drops the run's own first/last letter, i.e. a chosen window")
            else:
                kind = "**crosses a `1`-break** (invalid -- `1` carries no letter)"
            p(f"    - 🟡 **{w}** dials `{d}` (offset {idx} of `{digit_str}`): {kind}.")
        p("    - ⚠️ This is the \"pick the right digits\" coincidence #43 warns of, made "
          "concrete: **`FROG` was put in the target list precisely because the author "
          "spotted `3764`=FROG by eye** -- and that a meaningless word \"hits\" as a chosen "
          "window of the run is exactly why a single substring decode proves nothing. "
          "Logged as **coincidence, NOT a reading.**")
    else:
        p("    - none of the curated mystery words dial to any substring -> **NULL** "
          "for the on-theme vocabulary.")
    p("  - Net: the keypad reading yields **no word that fills a whole letter-run**; the "
      "only hit is a *chosen window* inside the run (`FROG`), which is meaningless. "
      "**NULL/coincidence.** (First time this reading is tested.)")
    p("")

    # --- 3. Permutation structure of the opening seven (NEW) ----------------------
    p("## 3. Permutation structure of `1,2,3,7,6,4,5` (NEW) -- the missing half of attempt B")
    is_perm = sorted(OPENING7) == [1, 2, 3, 4, 5, 6, 7]
    p(f"- Is the opening seven a permutation of 1-7 (the exact tally range)? **{is_perm}** "
      "-- it uses each of 1..7 exactly once.")
    fixed, cycles = permutation_cycles(OPENING7)
    p(f"- Cycle decomposition (position -> value): **fixed points = {fixed}**, "
      f"**cycle(s) = {cycles}**.")
    p("- Reading: positions **1,2,3 are IDENTITY** (a node read in this order stays put), "
      "and **4,5,6,7 form a single 4-cycle** `(4 7 5 6)` (node4->pos7, node7->pos5, "
      "node5->pos6, node6->pos4). So as a reorder of 7 tally-nodes it **leaves Butcher "
      "Creek's 1-3 fixed and scrambles only the {4,5,6,7} tail** (outhouse #4/#5 + the two "
      "Fort Brennand tallies). That is a clean *structural* observation about the number, "
      "independent of any decode -- and it sharpens attempt B: the reorder is non-trivial "
      "**only** on the BC#4->Brennand stretch, which is also where the `LJ`/`SM` carving and "
      "the Fort Brennand pointer live. ⚠️ Still BLOCKED as a decode: the 7 nodes carry bare "
      "counts, so there is nothing per-node to spell once reordered ([U6], connections §3).")
    p("")

    # --- 4. Arithmetic / structural readings --------------------------------------
    p("## 4. Arithmetic & structural readings")
    p(f"- digit sum: opening7 = **{sum(OPENING7)}**, confirmed10 = **{sum(CONFIRMED)}**, "
      f"provisional = **{sum(PROVISIONAL_FULL)}** (PROVISIONAL). No anchor matches "
      f"(28/32 are not mystery constants).")
    deltas = [CONFIRMED[i + 1] - CONFIRMED[i] for i in range(len(CONFIRMED) - 1)]
    p(f"- first differences of `1237645112`: **{deltas}** -- no monotone run, no obvious "
      "geometric/clock pattern. NULL.")
    counts = Counter(CONFIRMED)
    p(f"- digit multiset of confirmed: {dict(sorted(counts.items()))} "
      f"-- `1`x{counts[1]}, `2`x{counts[2]} dominate; no 8, 9, or 0. (8 webs absent.)")
    p("")

    # --- 5. Date readings (README explicitly asks for these) ----------------------
    p("## 5. Date / numeric-window readings")
    p("- Leading-digit date parses: `1/2/3...` (1 Feb?), `12/3` (12 Mar), `123/7` -- all "
      "require dropping the rest; the string is **10 digits with no year-shaped run** "
      "(no 18xx/19xx; `1237` reads as a 13th-century year, off-setting). **NULL** -- no "
      "clean in-fiction date (1899 / RDR2's era) falls out.")
    p("")

    # --- 6. Cross-reference vs the mystery's own number lines ----------------------
    p("## 6. Cross-reference vs sourced mystery number anchors")
    p("- Does the confirmed string CONTAIN any anchor as a contiguous run?")
    cs = "".join(str(n) for n in CONFIRMED)
    any_hit = False
    for name, seq in ANCHORS.items():
        sub = "".join(str(n) for n in seq)
        present = sub in cs
        if present and len(sub) > 1:
            any_hit = True
        flag = "🟡 present" if (present and len(sub) > 1) else ("(single digit)" if len(sub) == 1 else "no")
        p(f"  - {name}: `{sub}` -> {flag}")
    p("  - The only multi-digit anchor that is a substring would be flagged above; "
      f"net **{'a coincidental substring exists (small ints, discount)' if any_hit else 'NO multi-digit anchor is a contiguous substring'}**. "
      "The opening seven matching the **1-7 tally RANGE** (as a permutation, §3) is the "
      "one real structural tie -- but a range-match is weak (any 1-7 permutation would).")
    p("")

    # --- Verdict ------------------------------------------------------------------
    p("## Verdict")
    p("- **Null across the board**, as expected for a 10-digit string under many transforms.")
    p("- Two readings tested for the first time both come back **null/coincidence**: the "
      "phone-keypad \"call-back\" reading (only a meaningless windowed hit, `FROG`, per the "
      "#43 warning) and arithmetic/date parses.")
    p("- The **one durable, non-decode finding** is structural (§3): `1,2,3,7,6,4,5` is a "
      "permutation of 1-7 that is **identity on 1-3 and a 4-cycle on {4,5,6,7}** -- so if it "
      "ever indexes the seven tally nodes, it only reorders the BC#4 -> Fort Brennand tail. "
      "That refines attempt B's premise but does **not** unblock it (no per-node content to "
      "spell; [U6]).")
    p("- Status unchanged: Gertrude's numbers are a **deliberate, Rockstar-flagged "
      "cipher-candidate** ([K23]) whose **decode and spider-link remain open** ([U6]). This "
      "harness logs the negative and adds the keypad + permutation tests to the record.")

    path = os.path.join(RESULTS, "gertrude_cipher.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    # --- stdout summary -----------------------------------------------------------
    print("Gertrude's numbers -- cipher harness")
    print("=" * 68)
    print(f"CONFIRMED [K23]: {CONFIRMED}  ('1237645112')")
    print(f"A1Z26 confirmed -> {a1z26(CONFIRMED)}   (NULL; reproduces attempt A)")
    s, runs = keypad_runs(CONFIRMED)
    print(f"Keypad runs (split on 1/0): {runs}   "
          f"hits={[h[0] for h in hits] or 'none clean'}")
    fixed, cycles = permutation_cycles(OPENING7)
    print(f"Opening7 is perm of 1-7: {sorted(OPENING7) == [1,2,3,4,5,6,7]}; "
          f"fixed={fixed}, cycles={cycles}")
    print(f"digit sum opening7={sum(OPENING7)}, confirmed10={sum(CONFIRMED)}")
    print()
    print("Net: NULL across transforms; the durable finding is structural --")
    print("  the permutation is identity on 1-3, a 4-cycle on {4,5,6,7}.")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

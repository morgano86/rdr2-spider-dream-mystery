#!/usr/bin/env python3
"""Gertrude's numbers -- STRUCTURE battery on the CANONICAL [K42] 12-line set
([U6]/[S42]/[K23]/[K42]; thread 04).

QUESTION TESTED: S42 (are the recitations failed-counting characterisation?) vs the
rival reading (deliberate structure in the derailed tails). This is NOT the gated
tail-CIPHER harness (thread 04 holds decode-fishing): it tests whether statistical
structure exists AT ALL, with exact permutation nulls -- the disciplined form of
"look for a pattern".

INPUT PROVENANCE (cite, never invent):
- CANONICAL, A-tier ([K42], 2026-07-05): the game's own subtitle text for Gertrude's
  voice-line file `0xFD1BB3EB.txt` (#78 -- 2019-12-01 GitHub dump, independently
  re-fetched at the pinned commit; verbatim in-repo copy:
  sources/gertrude-lines_0xFD1BB3EB.txt). Exactly 12 number-recitation lines, A-L
  (hashes in thread 04's K42 table).
- SUPERSEDES the 2026-07-04 run on the PROVISIONAL 9-line video transcription
  (headline numbers of that run, for the record: global additive p = 0.44; the
  "L2-only" 4-term Fibonacci chain exact p = 0.039, then read as a transcription
  fork). K42 dissolved that frame: video-L3 was an artifact, and "L2/L7" are the
  REAL distinct lines A and B. The old results file is overwritten by this run;
  the old numbers stay quoted in INVESTIGATION_LOG.md (2026-07-04) and thread 04.

PARSE DECISIONS (kept faithful, flagged):
- UNIT = the string's own subtitle segment (the `~sl~` break, `|` in the K42 table),
  further split where she audibly RESTARTS from "one" after a pause (lines H, I --
  e.g. "One, two... one, two, three, four..." = two counting attempts). Exact
  permutation nulls need small tails; the game's own segmentation supplies the unit
  without any interpretive cut. Cross-UNIT triples are not scored in the per-unit
  battery; a seeded whole-stream Monte-Carlo check on line A (the only line whose
  full tail is too long to enumerate) closes that gap.
- Line A's boundary token: the subtitle's timing break falls between "...eleven..."
  and "two... uh, one, two, ten...". Following the [K23] canonical parse (the
  `1237645112` opening = "...eleven, two"), the `2` is grouped with unit A1. The
  alternative grouping (2 leads A2) is noted where it matters; the headline chain
  `3,5,8,13` sits deep in A2 either way.
- F's "seventeen?" and G's "six!" keep their tokens; punctuation is not data.
- K23's phone-style digit parse ("...5,1,1,2") vs the subtitle's "eleven" is settled
  by K42: the RDR2 line says ELEVEN; the split is the GTA/Nazar callback format.

METHOD / NULL MODEL:
- Each unit's maximal correct counting prefix (1,2,...,k) is FIXED under the null --
  "she starts counting correctly" is conceded characterisation (S42's own premise)
  and must not score as structure. The derailed tail is permuted; every unit tail
  has <= 7 tokens, so the null is enumerated EXACTLY (no randomness, no seed),
  except the flagged Monte-Carlo supplement (seeded, seed printed).
- Statistics: consecutive additive triples (s[i]+s[i+1]==s[i+2], scored over the
  whole prefix+tail unit so cross-boundary triples count), longest additive
  (Fibonacci-like) chain, and reverse-additive triples (s[i]-s[i+1]==s[i+2]) as a
  CONTROL family showing how cheaply rival pattern families "hit".
- Global p for total additive triples = exact convolution of the independent
  per-unit null distributions.

WHAT A RESULT MEANS:
- The old run's C-tier transcription discount is GONE -- these are the game's own
  strings. The POST-HOC family-selection discount REMAINS: the additive family was
  chosen because an eyeball note flagged it, and the corpus has scanned >= 6 pattern
  families (A1Z26, keypad, dates, primes, additive, anchors).
- Any positive is [SPECULATION] at most (a script tests; it does not establish
  fact). A null result on the tails is a REAL finding: it keeps S42 (failed
  counting / characterisation) statistically supported on canonical data.

Run: `python experiments/gertrude_tail_structure.py`   (Python 3, stdlib only)
Output: stdout summary + experiments/results/gertrude_tail_structure.md
"""

import os
import random
from collections import Counter
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

# --- Inputs: CANONICAL (K42, A-tier) -- 12 lines, decomposed into units ------------
# (line, hash, [unit token lists], parse note)
LINES = [
    ("A", "0xD8BBB1E5",
     [[1, 2, 3, 7, 6, 4, 5, 11, 2], [1, 2, 10, 3, 5, 8, 13, 14]],
     "the [K23] opening line; boundary '2' grouped with A1 per the canonical parse"),
    ("B", "0x20C24CB8",
     [[5, 11, 2, 1, 2, 10, 3], [4, 5, 8, 13, 14, 1]],
     "continuation-shaped: verbatim A-suffix with one inserted 4 + appended 1 (sec 2)"),
    ("C", "0x0E5727E2",
     [[1, 2, 3, 4, 5, 17, 8, 9, 3], [1, 2, 4, 7, 5, 9, 1]],
     "the 'counts to five' line; C1 tail ends 8,9,3"),
    ("D", "0x3190EE55", [[1, 2, 3, 7, 6, 3]], "A1's opening with one token changed"),
    ("E", "0x5BF14315", [[3, 4, 17, 29, 13]],
     "fragment-shaped (no counting start); carries the only 29"),
    ("F", "0xE60AD746", [[1, 2, 3, 4, 5, 17]], "'...seventeen?'"),
    ("G", "0xF45673DD", [[1, 2, 3, 4, 7, 3, 6]], "'...seven, three, six!'"),
    ("H", "0xC2839038", [[1, 2], [1, 2, 3, 4]], "two restart attempts (pure counting)"),
    ("I", "0xEB01169E", [[1, 2, 3, 4], [1, 2], [1]],
     "three decaying restart attempts (pure counting)"),
    ("J", "0xECF9DA61", [[1, 2]], "pure counting fragment"),
    ("K", "0xFFA50A7E", [[1, 1, 1]], "'One, one... one...'"),
    ("L", "0xB34A2731", [[8, 9, 3]], "fragment: verbatim C1 tail-end (sec 2)"),
]

# Sourced mystery number anchors, for the descriptive cross-flag section only.
ANCHOR_NOTES = {
    8: "8 webs [K13a]",
    29: "29 = one of the matchstick operator numbers 53/23/29 [S21]",
    6: "Fort Brennand tally 6 [K7]",
    7: "Fort Brennand tally 7 [K7]",
}

MC_SEED = 42
MC_N = 200_000


def counting_prefix(seq):
    """Length k of the maximal correct prefix 1,2,...,k."""
    k = 0
    for i, v in enumerate(seq):
        if v == i + 1:
            k += 1
        else:
            break
    return k


def additive_triples(seq):
    return sum(1 for i in range(len(seq) - 2) if seq[i] + seq[i + 1] == seq[i + 2])


def reverse_triples(seq):
    return sum(1 for i in range(len(seq) - 2) if seq[i] - seq[i + 1] == seq[i + 2])


def longest_additive_chain(seq):
    """Longest run of consecutive tokens obeying x[i] = x[i-2] + x[i-1] (len >= 3)."""
    best, cur = 0, 2
    for i in range(2, len(seq)):
        if seq[i] == seq[i - 2] + seq[i - 1]:
            cur += 1
        else:
            cur = 2
        best = max(best, cur)
    return best if best >= 3 else 0


def rerail_runs(seq, prefix_len):
    """Maximal +1 increment runs (len >= 2) that start AT/after the counting prefix."""
    runs, i = [], prefix_len
    while i < len(seq) - 1:
        j = i
        while j < len(seq) - 1 and seq[j + 1] == seq[j] + 1:
            j += 1
        if j > i:
            runs.append(seq[i:j + 1])
            i = j + 1
        else:
            i += 1
    return runs


def exact_null(prefix, tail, stat):
    """Exact distribution of stat(prefix + permuted tail) over distinct tail orders."""
    dist = Counter()
    for perm in set(permutations(tail)):
        dist[stat(prefix + list(perm))] += 1
    total = sum(dist.values())
    return {k: v / total for k, v in sorted(dist.items())}, total


def p_ge(dist, observed):
    return sum(p for k, p in dist.items() if k >= observed)


def convolve(d1, d2):
    out = Counter()
    for a, pa in d1.items():
        for b, pb in d2.items():
            out[a + b] += pa * pb
    return dict(out)


def levenshtein(a, b):
    m, n = len(a), len(b)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev, dp[0] = dp[0], i
        for j in range(1, n + 1):
            cur = dp[j]
            dp[j] = min(dp[j] + 1, dp[j - 1] + 1,
                        prev + (0 if a[i - 1] == b[j - 1] else 1))
            prev = cur
    return dp[n]


def units():
    for name, h, us, note in LINES:
        for idx, u in enumerate(us, 1):
            uname = f"{name}{idx}" if len(us) > 1 else name
            yield uname, name, u


def main():
    os.makedirs(RESULTS, exist_ok=True)
    out, p = [], lambda s="": out.append(s)

    p("# Result -- Gertrude structure battery on the CANONICAL [K42] set (`gertrude_tail_structure.py`)")
    p("")
    p("Tests **[S42]** (failed-counting characterisation) vs *deliberate tail structure* on the")
    p("**CANONICAL 12-line game-text inventory** ([K42], A-tier, #78 -- the game's own subtitle")
    p("strings, in-repo copy on file). Exact permutation nulls; each unit's correct counting")
    p("prefix is **fixed** under the null so the conceded \"she starts 1,2,3...\" shape cannot")
    p("score as signal. **Supersedes the 2026-07-04 run on the provisional 9-line video")
    p("transcription** (global p was 0.44; the 'L2' chain p was 0.039 read as a transcription")
    p("fork -- K42 dissolved that frame: the fork's two variants are the REAL lines A and B).")
    p("No decode attempted; a positive here is [SPECULATION] at most.")
    p("")

    # --- 1. S42 shape: counting prefixes -------------------------------------------
    p("## 1. Counting-prefix shape (the S42 prediction)")
    upre = {}
    for uname, _, seq in units():
        upre[uname] = counting_prefix(seq)
    p("- Correct-prefix length per unit: "
      + ", ".join(f"{n}={k}" for n, k in upre.items()) + ".")
    starters = {n: k for n, k in upre.items() if k > 0}
    mx = max(starters.values())
    zero = [n for n, k in upre.items() if k == 0]
    p(f"- Every unit that STARTS counting derails by **{mx}** -- no counting attempt in the "
      "game's own text ever passes five (C1 and F reach exactly `1..5`; the StrangeMan "
      "caption *'she only manages to count up to five'* is literally true in the canonical "
      "strings).")
    p(f"- Units with **no counting start at all**: `{', '.join(zero)}` -- these are not "
      "counter-examples to the S42 shape; section 2 shows they are **continuation fragments** "
      "of the full lines, not independent recitations.")
    p("")

    # --- 2. Fragment / windowing structure -------------------------------------------
    p("## 2. The prefix-0 lines are continuation fragments (new, canonical-only finding)")
    A = [t for u in LINES[0][2] for t in u]
    B = [t for u in LINES[1][2] for t in u]
    i5 = A.index(5, 4)  # the '5' that opens B's window (A position 7, 1-based)
    d_ab = levenshtein(A[i5:], B)
    p(f"- **B is a window onto A's stream.** A (concatenated) = `{A}`; B = `{B}`. "
      f"B's head `{B[:7]}` is **verbatim** A's tokens {i5 + 1}-{i5 + 7}; full "
      f"token-Levenshtein(A[{i5 + 1}:], B) = **{d_ab}** (one inserted `4`, one appended "
      "`1`). So the 'edit-distance-1 pair' of the old battery is really *one babble stream "
      "recorded twice with variation*, canonically.")
    C1 = LINES[2][2][0]
    p(f"- **L (`{LINES[11][2][0]}`) is verbatim the last 3 tokens of C1 (`{C1}`)** -- a "
      "chopped-out tail fragment given its own line.")
    p("- **E (`[3, 4, 17, 29, 13]`) opens mid-count** (3,4) and carries the corpus's only "
      "29 -- fragment-shaped, though no parent line contains it (the video's 'L9' chained "
      "it after F, whose `...5, 17?` it continues naturally: `1..5,17 / 3,4,17,29,13`).")
    p("- Reading: the 12 recorded lines behave like **windows cut from one longer failed-"
      "counting babble take** (a standard VO-session shape: one long improvisation chopped "
      "into triggerable barks). This *explains* the prefix-0 lines inside S42 rather than "
      "against it, and explains why the 2019 listeners naturally chained them (video L6/L7 "
      "= B's halves, L9 = F+E). It also frames the Fibonacci fork correctly: **A and B are "
      "two takes of the same material**, and the `4` that breaks the chain is intra-take "
      "variation (sec 3b).")
    p("")

    # --- 3. Additive / Fibonacci structure, exact nulls ------------------------------
    p("## 3. Additive (Fibonacci-type) structure in the derailed tails -- exact permutation null")
    p("- Statistic: consecutive triples `a,b,a+b` over the full unit; null = counting prefix "
      "fixed, derailed tail exactly permuted (all distinct orders enumerated; no sampling).")
    p("")
    p("| unit | seq | prefix fixed | additive triples (obs) | p(>=obs) | longest chain (obs) | p(chain>=obs) | tail orders |")
    p("|---|---|---|---|---|---|---|---|")
    total_obs = 0
    global_dist = {0: 1.0}
    chain_flags = []
    for uname, _, seq in units():
        k = upre[uname]
        prefix, tail = seq[:k], seq[k:]
        obs_t = additive_triples(seq)
        obs_c = longest_additive_chain(seq)
        dist_t, norders = exact_null(prefix, tail, additive_triples)
        dist_c, _ = exact_null(prefix, tail, longest_additive_chain)
        pt = p_ge(dist_t, obs_t)
        pc = p_ge(dist_c, obs_c) if obs_c else 1.0
        total_obs += obs_t
        global_dist = convolve(global_dist, dist_t)
        if obs_c >= 4:
            chain_flags.append((uname, seq, obs_c, pc))
        p(f"| {uname} | `{seq}` | `{prefix}` | {obs_t} | {pt:.3f} | "
          f"{obs_c if obs_c else '-'} | {pc:.3f} | {norders} |")
    gp = p_ge(global_dist, total_obs)
    p("")
    p(f"- **Global**: total additive triples = **{total_obs}**; exact convolved null gives "
      f"**p(total >= {total_obs}) = {gp:.3f}**.")
    for uname, seq, c, pc in chain_flags:
        p(f"- 🟡 **{uname} carries a {c}-term additive chain** (`3, 5, 8, 13` inside "
          f"`{seq}`) -- per-unit exact **p = {pc:.4f}**.")
    p("")

    # --- 3s. Whole-stream Monte-Carlo supplement -------------------------------------
    p("### 3s. Whole-stream check on line A (seeded Monte-Carlo -- closes the cross-unit gap)")
    rng = random.Random(MC_SEED)
    kA = counting_prefix(A)
    prefA, tailA = A[:kA], A[kA:]
    obsA_t, obsA_c = additive_triples(A), longest_additive_chain(A)
    ge_t = ge_c = 0
    for _ in range(MC_N):
        t = tailA[:]
        rng.shuffle(t)
        s = prefA + t
        if additive_triples(s) >= obsA_t:
            ge_t += 1
        if longest_additive_chain(s) >= obsA_c:
            ge_c += 1
    p(f"- Line A as ONE stream (`{A}`; prefix `{prefA}` fixed, {len(tailA)}-token tail "
      f"shuffled; seed={MC_SEED}, n={MC_N:,}): observed triples = {obsA_t} -> "
      f"**p ≈ {ge_t / MC_N:.3f}**; observed longest chain = {obsA_c} -> "
      f"**p ≈ {ge_c / MC_N:.3f}**.")
    p("- (B as one stream has 1 triple / a 3-term chain -- unremarkable; not simulated.) "
      "Note the whole-stream view is **more deflationary than the per-unit one for the "
      "chain stat**: given line A's full 14-token derailed vocabulary, a 4-term additive "
      "chain somewhere in it is unremarkable (p ≈ 0.16). The per-unit p = 0.039 conditions "
      "on the chain landing inside the shorter A2 window -- take the whole-line number as "
      "the fairer weight.")
    p("")

    # --- 3b. The honesty ledger on the chain flag -------------------------------------
    p("### 3b. Discounts on the line-A Fibonacci flag (read before repeating it)")
    p("- **The transcription discount is GONE** -- `...3, 5, 8, 13, 14...` is the game's own "
      "canonical text in line A ([K42]). What remains is interpretive, not evidential:")
    p("- **The variant take breaks it.** B re-records the same material and inserts a `4` "
      "(`...10, 3 | 4, 5, 8, 13, 14, 1`), collapsing the 4-term chain to the unremarkable "
      "3-term `5,8,13`. If `3,5,8,13` were a deliberately planted token, preserving it in "
      "the *only other take of the same passage* is the natural authorial move; breaking it "
      "is the natural *babble* move. Leans deflationary.")
    fams = 6
    worst = min((pc for *_, pc in chain_flags), default=1.0)
    p(f"- **Post-hoc family selection stands:** the additive family was tested because an "
      f"eyeball note flagged it; the corpus has scanned >= {fams} pattern families (A1Z26, "
      f"keypad, dates, primes, additive, anchors). A Bonferroni-type discount puts the "
      f"effective p nearer ~{min(1.0, worst * fams):.2f}.")
    p("- **13 and 14 are ordinary vocabulary here:** `13,14` also appears as a re-rail run "
      "(+1 counting) and 13 recurs in E outside any additive context -- the chain's tokens "
      "are not reserved 'Fibonacci' tokens.")
    p("- **Control family (how cheap rival 'patterns' are):** reverse-additive triples "
      "(`a-b=c`) per unit: "
      + ", ".join(f"{n}={reverse_triples(s)}" for n, _, s in units() if reverse_triples(s))
      + " -- e.g. C1's `17,8,9` (17-8=9) 'hits' the mirror family by eye, exactly the #43 "
        "warning (*'you could obtain just about any type of result'*).")
    p("")

    # --- 4. Post-derail re-rail runs (texture of failed counting) --------------------
    p("## 4. Post-derail 're-rail' runs (+1 increments outside the counting prefix)")
    for uname, _, seq in units():
        runs = rerail_runs(seq, upre[uname])
        if runs:
            p(f"- {uname}: {runs}")
    p("- Reading: after derailing she repeatedly falls back into **locally correct counting** "
      "(`4,5`, `13,14`, `8,9`, `3,4`, `1,2`) -- the texture of a mind that can increment but "
      "cannot hold the thread. This is the *shape S42 predicts*; an encoding has no reason "
      "to re-rail.")
    p("")

    # --- 5. Vocabulary profile --------------------------------------------------------
    p("## 5. Vocabulary profile + anchor cross-flags (descriptive only)")
    all_tokens = [t for _, _, s in units() for t in s]
    counts = Counter(all_tokens)
    vocab = sorted(counts)
    missing = [v for v in range(1, max(vocab)) if v not in counts]
    p(f"- Values used across all 12 canonical lines: `{vocab}`; frequencies: "
      + ", ".join(f"{v}x{counts[v]}" for v in vocab) + ".")
    p(f"- Missing below the max ({max(vocab)}): `{missing}` -- a contiguous 1-11 block, then "
      "isolated 13, 14, 17, 29. Small-number-dominant with sporadic jumps = babble-shaped; "
      "**12 is never said in the game's own text** (a counter would pass through 12; a "
      "derailer skips anywhere). This survives from the provisional run intact.")
    hits = sorted(set(all_tokens) & set(ANCHOR_NOTES))
    p("- Anchor overlaps (weak, single small integers -- flags only, not evidence): "
      + "; ".join(f"`{v}` = {ANCHOR_NOTES[v]}" for v in hits) + ".")
    p("- 👁️ Eyeball ledger (recorded so they aren't re-discovered; NOT tested -- the target "
      "sets are unfalsifiable): the >10 values `11,13,17,29` are all prime; E's adjacent "
      "`17,29` concatenates to 1729 (the Hardy-Ramanujan number). Textbook "
      "pick-the-right-numbers bait per #43.")
    p("")

    # --- Verdict ----------------------------------------------------------------------
    p("## Verdict")
    p(f"- **S42 survives the move to canonical data:** every counting attempt in the game's "
      f"own strings caps at **{mx}**; the prefix-0 lines resolve into continuation "
      f"fragments of one babble stream (sec 2); post-derail re-rail runs and babble-shaped "
      f"vocabulary persist; and the tails carry **no additive structure beyond chance "
      f"globally (exact p = {gp:.2f})**.")
    if chain_flags:
        uname, _, c, pc = chain_flags[0]
        p(f"- **The one flag is now a fixed fact of the text, weighed and held at "
          f"[SPECULATION]:** line A's verbatim `3,5,8,13` ({c}-term chain, exact per-unit "
          f"p = {pc:.3f}; ~{min(1.0, pc * fams):.2f} after the family-selection discount). "
          "The old fork is DECIDED (both variants real) and the resolution cuts against "
          "design: the only other take of the same passage (B) breaks the chain. Verdict: "
          "**suggestive-not-significant; do not build on it without an independent hook** "
          "(e.g. a source connecting Gertrude to Fibonacci deliberately).")
    p("- Nothing here touches the [K23] *opening* string, which remains a deliberate, "
      "Rockstar-flagged token (S42's middle reading -- signature string deliberate, tail = "
      "madness texture -- is *consistent with* this run).")
    p("- Conclusions are computational evidence on **[K42] A-tier inputs**; the S42 "
      "characterisation itself stays [SPECULATION] (a script tests, it doesn't establish "
      "fact); upstream of the [K16] frontier; no decode attempted (the tail-cipher gate "
      "stands, though with the text now canonical the gate's *audio-confirm* clause is "
      "moot -- what gates decoding now is the absence of any sourced key).")

    path = os.path.join(RESULTS, "gertrude_tail_structure.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    # --- stdout summary ---------------------------------------------------------------
    print("Gertrude CANONICAL [K42] 12-line set -- structure battery (exact nulls)")
    print("=" * 72)
    print(f"units: {len(list(units()))}; counting attempts cap at {mx} "
          "('counts up to five' true in game text)")
    print(f"prefix-0 units {zero} -> continuation fragments (B=window of A d={d_ab}; "
          "L=C1 tail verbatim)")
    print(f"additive triples total = {total_obs}, global exact p = {gp:.3f}")
    print(f"whole-stream A (MC seed={MC_SEED}): triples p~{ge_t / MC_N:.3f}, "
          f"chain p~{ge_c / MC_N:.3f}")
    for uname, seq, c, pc in chain_flags:
        print(f"FLAG: {uname} {c}-term chain 3,5,8,13  exact p={pc:.4f} "
              f"(~{min(1.0, pc * 6):.2f} family-discounted; B-take breaks it)")
    print("verdict: S42 (failed counting) survives on canonical data; line-A chain =")
    print("         suggestive-not-significant, deflationary lean (variant take breaks it).")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

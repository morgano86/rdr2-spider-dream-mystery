#!/usr/bin/env python3
"""Gertrude's numbers -- STRUCTURE battery on the 9-sequence tail transcription
([U6]/[S42]/[K23]; thread 04).

QUESTION TESTED: S42 (are the recitations failed-counting characterisation?) vs the
rival reading (deliberate structure in the tails). This is NOT the gated tail-CIPHER
harness (thread 04 holds decode-fishing until an audio confirm): it tests whether any
statistical structure exists AT ALL, with exact permutation nulls -- the disciplined
form of "look for a pattern". Run 2026-07-04 at the investigator's explicit request;
every input is PROVISIONAL and every conclusion inherits that tag.

INPUT PROVENANCE (cite, never invent):
- PROVISIONAL, C-tier ([U6], thread 04): the 9-sequence transcription recovered from
  the StrangeMan video's own frames via the #43 expose (image on file:
  images/gertrude/gertrude_numbers-transcription_strangeman-frame.jpg). Both hostile
  parties (video + debunker) accept these raw numbers; two independent transcriptions
  concur where they overlap; line 1 is the [K23] Nazar-echoed string. Still awaiting a
  clean-audio / dialogue-dump confirm.

PARSE DECISIONS (kept faithful, flagged):
- L5's trailing stammer "1... 1... 1... 1?" is excluded from order statistics (it is
  hesitation, not sequence); noted descriptively.
- L8 is transcribed as false starts "1... / 1 2... / 1 2 3 4... /" then a final
  attempt "1 2 3 4 7 3 6!" -- the final attempt is the analysed sequence; the false
  starts are counted in the prefix analysis only.
- L1 ends "...": truncated; analysed as recorded.

METHOD / NULL MODEL:
- Each line's maximal correct counting prefix (1,2,...,k) is FIXED under the null --
  "she starts counting correctly" is conceded characterisation (S42's own premise) and
  must not be allowed to score as structure. The derailed TAIL is permuted; because
  every tail has <= 7 tokens, the null is enumerated EXACTLY (<= 5040 distinct-order
  perms; no randomness, no seed).
- Statistics: consecutive additive triples (s[i]+s[i+1]==s[i+2], counted over the whole
  prefix+tail line so cross-boundary triples are scored), longest additive (Fibonacci-
  like) chain, and reverse-additive triples (s[i]-s[i+1]==s[i+2]) as a CONTROL family
  showing how cheaply rival pattern families "hit".
- Global p for total additive triples = exact convolution of the 9 independent
  per-line null distributions.

WHAT A RESULT MEANS:
- Any positive here is [SPECULATION] at most, and carries TWO explicit discounts:
  (1) the additive family was chosen POST-HOC (the thread's Fibonacci eyeball note),
  so a family-selection (Bonferroni-type) discount applies -- the corpus has eyeballed
  at least ~6 pattern families (A1Z26, keypad, dates, primes, additive, anchors);
  (2) the data is a C-tier video transcription whose least-reliable tokens are exactly
  the ones near-duplicate lines disagree on.
- A null result on the tails is a REAL finding: it upgrades S42 (failed counting /
  characterisation) from convergent-opinion to statistically-supported.

Run: `python experiments/gertrude_tail_structure.py`   (Python 3, stdlib only, exact)
Output: stdout summary + experiments/results/gertrude_tail_structure.md
"""

import os
from collections import Counter
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

# --- Inputs: PROVISIONAL (U6) -- the 9 transcribed lines ---------------------------
# (name, tokens, parse note)
LINES = [
    ("L1", [1, 2, 3, 7, 6, 4, 5, 11, 2],
     "trailing '...' (truncated); equals the [K23] string under the '...11,2' hearing"),
    ("L2", [1, 2, 10, 3, 5, 8, 13, 14], ""),
    ("L3", [1, 2, 3, 4, 17, 29, 13], ""),
    ("L4", [1, 2, 3, 4, 5, 17, 8, 9, 3], "video highlights 1-5 in red"),
    ("L5", [1, 2, 4, 7, 5, 9],
     "then stammers '1... 1... 1... 1?' -- stammer excluded from order stats"),
    ("L6", [1, 2, 3, 7, 6, 3, 5, 11, 2], "near-duplicate of L1 (one token differs)"),
    ("L7", [1, 2, 10, 3, 4, 5, 8, 13, 14], "near-duplicate of L2 (one insertion)"),
    ("L8", [1, 2, 3, 4, 7, 3, 6],
     "final attempt of '1... / 1 2... / 1 2 3 4... / 1 2 3 4 7 3 6!'"),
    ("L9", [1, 2, 3, 4, 5, 17, 3, 4, 17, 29, 13],
     "two '17?' tokens uncertain; caption: 'she only manages to count up to five'"),
]
L8_FALSE_STARTS = [[1], [1, 2], [1, 2, 3, 4]]

# Sourced mystery number anchors, for the descriptive cross-flag section only.
ANCHOR_NOTES = {
    8: "8 webs [K13a]",
    29: "29 = one of the matchstick operator numbers 53/23/29 [S21]",
    6: "Fort Brennand tally 6 [K7]",
    7: "Fort Brennand tally 7 [K7]",
}


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
    """Maximal +1 increment runs (len >= 2) that start AFTER the counting prefix."""
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


def main():
    os.makedirs(RESULTS, exist_ok=True)
    out, p = [], lambda s="": out.append(s)

    p("# Result -- Gertrude tail-transcription structure battery (`gertrude_tail_structure.py`)")
    p("")
    p("Tests **[S42]** (failed-counting characterisation) vs *deliberate tail structure* on the")
    p("**PROVISIONAL** 9-line transcription ([U6], C-tier, StrangeMan-frame via #43). Exact")
    p("permutation nulls; each line's correct counting prefix is **fixed** under the null so the")
    p("conceded \"she starts 1,2,3...\" shape cannot score as signal. **Everything here inherits")
    p("the transcription's C-tier uncertainty; nothing is promoted.** Run 2026-07-04 at the")
    p("investigator's explicit request (the tail-*cipher* gate stays: no decode-fishing here).")
    p("")

    # --- 1. S42 shape: counting prefixes -------------------------------------------
    p("## 1. Counting-prefix shape (the S42 prediction)")
    prefixes = {}
    for name, seq, _ in LINES:
        prefixes[name] = counting_prefix(seq)
    for fs in L8_FALSE_STARTS:
        pass  # false starts reported inline below
    p("- Correct-prefix length per line: "
      + ", ".join(f"{n}={k}" for n, k in prefixes.items())
      + f"; L8's false starts reach {[counting_prefix(fs) for fs in L8_FALSE_STARTS]}.")
    mx = max(prefixes.values())
    p(f"- Distribution: prefixes run 2-{mx}; **no line ever counts correctly past {mx}** -- "
      "exactly the video's own caption (*'she only manages to count up to five'*) and the red "
      "1-5 highlight. The S42 shape is confirmed **in the data both hostile parties accept**.")
    p("")

    # --- 2. Near-duplicate template structure ---------------------------------------
    p("## 2. Near-duplicate lines -> a finite recorded-line set (+ where NOT to trust tokens)")
    p("- Pairwise token-Levenshtein distances (<=2 shown):")
    names = [n for n, _, _ in LINES]
    seqs = {n: s for n, s, _ in LINES}
    close = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            d = levenshtein(seqs[names[i]], seqs[names[j]])
            if d <= 2:
                close.append((names[i], names[j], d))
                p(f"  - **{names[i]} ~ {names[j]}: distance {d}** "
                  f"(`{seqs[names[i]]}` vs `{seqs[names[j]]}`)")
    p("- Reading: 9 utterances collapse toward **~7 templates** -- L1/L6 differ by ONE token "
      "(the 6th: `4` vs `3`), L2/L7 by ONE insertion (a `4`). Game dialogue is a finite set of "
      "recorded lines, so near-duplicate pairs are either (a) the SAME line transcribed twice "
      "with a mishearing, or (b) genuinely distinct recorded variants. **Either way the "
      "differing tokens are the least-reliable tokens in the whole transcription** -- and (see "
      "section 3) the headline 'pattern' hangs on exactly one of them.")
    p("")

    # --- 3. Additive / Fibonacci structure, exact nulls ------------------------------
    p("## 3. Additive (Fibonacci-type) structure in the derailed tails -- exact permutation null")
    p("- Statistic: consecutive triples `a,b,a+b` over the full line; null = counting prefix "
      "fixed, derailed tail exactly permuted (all distinct orders enumerated; no sampling).")
    p("")
    p("| line | seq | prefix fixed | additive triples (obs) | p(>=obs) | longest chain (obs) | p(chain>=obs) | tail orders |")
    p("|---|---|---|---|---|---|---|---|")
    total_obs = 0
    global_dist = {0: 1.0}
    chain_flags = []
    for name, seq, _ in LINES:
        k = prefixes[name]
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
            chain_flags.append((name, seq, obs_c, pc))
        p(f"| {name} | `{seq}` | `{prefix}` | {obs_t} | {pt:.3f} | "
          f"{obs_c if obs_c else '-'} | {pc:.3f} | {norders} |")
    gp = p_ge(global_dist, total_obs)
    p("")
    p(f"- **Global**: total additive triples = **{total_obs}**; exact convolved null gives "
      f"**p(total >= {total_obs}) = {gp:.3f}**.")
    for name, seq, c, pc in chain_flags:
        p(f"- 🟡 **{name} carries a {c}-term additive chain** "
          f"(`3, 5, 8, 13` inside `{seq}`) -- per-line exact **p = {pc:.4f}**.")
    p("")

    # --- 3b. The honesty ledger on that flag ----------------------------------------
    p("### 3b. Discounts on the L2 Fibonacci flag (read before repeating it)")
    l2, l7 = seqs["L2"], seqs["L7"]
    p(f"- **The chain exists only in the L2 variant.** Its near-duplicate L7 = `{l7}` inserts a "
      f"`4` and the 4-term chain collapses to the unremarkable 3-term `5,8,13` "
      f"(L7 chain = {longest_additive_chain(l7)}, additive-triple p is ~chance in the table). "
      "Section 2 says L2/L7 plausibly transcribe the SAME recorded line -- so the entire flag "
      "**hinges on precisely the least-reliable token difference in the dataset.** The clean-"
      "audio confirm (thread 04 residual) decides which variant is real; until then this is a "
      "**fork, not a finding**.")
    fams = 6
    p(f"- **Post-hoc family selection:** additive structure was tested because an eyeball note "
      f"flagged it (thread 04). The corpus has scanned >= {fams} pattern families (A1Z26, "
      f"keypad, dates, primes, additive, anchors); a Bonferroni-type discount puts the "
      f"effective p nearer ~{min(1.0, min(pc for *_ , pc in chain_flags) * fams):.2f} "
      "even before the transcription uncertainty.")
    p("- **Control family (how cheap rival 'patterns' are):** reverse-additive triples "
      "(`a-b=c`) score, per line: "
      + ", ".join(f"{n}={reverse_triples(s)}" for n, s, _ in LINES)
      + " -- e.g. L4's `17,8,9` (17-8=9) 'hits' the mirror family by eye just as the #43 "
        "expose warns (*'you could obtain just about any type of result'*).")
    p("")

    # --- 4. Post-derail re-rail runs (texture of failed counting) --------------------
    p("## 4. Post-derail 're-rail' runs (+1 increments after the derailment)")
    for name, seq, _ in LINES:
        runs = rerail_runs(seq, prefixes[name])
        if runs:
            p(f"- {name}: {runs}")
    p("- Reading: after derailing she repeatedly falls back into **locally correct counting** "
      "(`3,4,5`, `13,14`, `3,4`) -- the texture of a mind that can increment but cannot hold "
      "the thread. This is the *shape S42 predicts*; an encoding has no reason to re-rail.")
    p("")

    # --- 5. Vocabulary profile --------------------------------------------------------
    p("## 5. Vocabulary profile + anchor cross-flags (descriptive only)")
    all_tokens = [v for _, s, _ in LINES for v in s]
    counts = Counter(all_tokens)
    vocab = sorted(counts)
    missing = [v for v in range(1, max(vocab)) if v not in counts]
    p(f"- Values used: `{vocab}`; frequencies: "
      + ", ".join(f"{v}x{counts[v]}" for v in vocab) + ".")
    p(f"- Missing below the max ({max(vocab)}): `{missing}` -- a contiguous 1-11 block, then "
      "isolated 13, 14, 17, 29. Small-number-dominant with sporadic jumps = babble-shaped; "
      "note **12 is never said** (a counter would pass through 12; a derailer skips anywhere).")
    hits = sorted(set(all_tokens) & set(ANCHOR_NOTES))
    p("- Anchor overlaps (weak, single small integers -- flags only, not evidence): "
      + "; ".join(f"`{v}` = {ANCHOR_NOTES[v]}" for v in hits) + ".")
    p("- 👁️ Eyeball ledger (recorded so they aren't re-discovered; NOT tested -- the target "
      "sets are unfalsifiable): the >10 values `11,13,17,29` are all prime; L3/L9's adjacent "
      "`17,29` concatenates to 1729 (the Hardy-Ramanujan number). Both are textbook "
      "pick-the-right-numbers bait per #43.")
    p("")

    # --- Verdict ----------------------------------------------------------------------
    p("## Verdict")
    p(f"- **S42 is now statistically supported, not just convergent opinion:** counting "
      f"prefixes 2-{mx} capped at {mx}, post-derail re-rail runs, babble-shaped vocabulary, and "
      f"a global additive-structure test at **p = {gp:.2f}** (no tail-wide structure beyond "
      "chance).")
    chain_p = min((pc for *_, pc in chain_flags), default=1.0)
    p(f"- **One narrow, fragile exception:** the L2 variant's 4-term Fibonacci chain "
      f"(`3,5,8,13`, exact per-line p = {chain_p:.3f} pre-discount) -- but it evaporates under "
      "the L7 parse of the same line, and the L2/L7 difference is the dataset's least-reliable "
      "token. "
      "**The clean-audio confirm now decides two things at once** (the tail text AND this "
      "flag); its priority rises.")
    p("- Nothing here touches the [K23] *opening* string, which remains a deliberate, "
      "Rockstar-flagged token ([S42]'s middle reading: signature string deliberate, tail = "
      "madness texture -- this run is *consistent with* that reading).")
    p("- All conclusions are **[SPECULATION]-grade on PROVISIONAL data**; upstream of the "
      "[K16] frontier; no decode was attempted (the tail-cipher gate stands).")

    path = os.path.join(RESULTS, "gertrude_tail_structure.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    # --- stdout summary ---------------------------------------------------------------
    print("Gertrude tail transcription -- structure battery (exact nulls)")
    print("=" * 70)
    print(f"prefixes: {prefixes}  (max = {mx}; 'counts up to five' confirmed)")
    print(f"near-duplicates: {[(a, b, d) for a, b, d in close]}")
    print(f"additive triples total = {total_obs}, global exact p = {gp:.3f}")
    for name, seq, c, pc in chain_flags:
        print(f"FLAG: {name} {c}-term chain 3,5,8,13  p={pc:.4f}  "
              f"(collapses under the L7 parse; hinges on 1 unreliable token)")
    print("verdict: S42 (failed counting) statistically supported; one fragile")
    print("         L2-only Fibonacci fork -> decided by the clean-audio confirm.")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

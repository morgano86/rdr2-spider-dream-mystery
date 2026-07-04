# Result -- Gertrude tail-transcription structure battery (`gertrude_tail_structure.py`)

Tests **[S42]** (failed-counting characterisation) vs *deliberate tail structure* on the
**PROVISIONAL** 9-line transcription ([U6], C-tier, StrangeMan-frame via #43). Exact
permutation nulls; each line's correct counting prefix is **fixed** under the null so the
conceded "she starts 1,2,3..." shape cannot score as signal. **Everything here inherits
the transcription's C-tier uncertainty; nothing is promoted.** Run 2026-07-04 at the
investigator's explicit request (the tail-*cipher* gate stays: no decode-fishing here).

## 1. Counting-prefix shape (the S42 prediction)
- Correct-prefix length per line: L1=3, L2=2, L3=4, L4=5, L5=2, L6=3, L7=2, L8=4, L9=5; L8's false starts reach [1, 2, 4].
- Distribution: prefixes run 2-5; **no line ever counts correctly past 5** -- exactly the video's own caption (*'she only manages to count up to five'*) and the red 1-5 highlight. The S42 shape is confirmed **in the data both hostile parties accept**.

## 2. Near-duplicate lines -> a finite recorded-line set (+ where NOT to trust tokens)
- Pairwise token-Levenshtein distances (<=2 shown):
  - **L1 ~ L6: distance 1** (`[1, 2, 3, 7, 6, 4, 5, 11, 2]` vs `[1, 2, 3, 7, 6, 3, 5, 11, 2]`)
  - **L2 ~ L7: distance 1** (`[1, 2, 10, 3, 5, 8, 13, 14]` vs `[1, 2, 10, 3, 4, 5, 8, 13, 14]`)
- Reading: 9 utterances collapse toward **~7 templates** -- L1/L6 differ by ONE token (the 6th: `4` vs `3`), L2/L7 by ONE insertion (a `4`). Game dialogue is a finite set of recorded lines, so near-duplicate pairs are either (a) the SAME line transcribed twice with a mishearing, or (b) genuinely distinct recorded variants. **Either way the differing tokens are the least-reliable tokens in the whole transcription** -- and (see section 3) the headline 'pattern' hangs on exactly one of them.

## 3. Additive (Fibonacci-type) structure in the derailed tails -- exact permutation null
- Statistic: consecutive triples `a,b,a+b` over the full line; null = counting prefix fixed, derailed tail exactly permuted (all distinct orders enumerated; no sampling).

| line | seq | prefix fixed | additive triples (obs) | p(>=obs) | longest chain (obs) | p(chain>=obs) | tail orders |
|---|---|---|---|---|---|---|---|
| L1 | `[1, 2, 3, 7, 6, 4, 5, 11, 2]` | `[1, 2, 3]` | 1 | 1.000 | 3 | 1.000 | 720 |
| L2 | `[1, 2, 10, 3, 5, 8, 13, 14]` | `[1, 2]` | 2 | 0.064 | 4 | 0.039 | 720 |
| L3 | `[1, 2, 3, 4, 17, 29, 13]` | `[1, 2, 3, 4]` | 1 | 1.000 | 3 | 1.000 | 6 |
| L4 | `[1, 2, 3, 4, 5, 17, 8, 9, 3]` | `[1, 2, 3, 4, 5]` | 1 | 1.000 | 3 | 1.000 | 24 |
| L5 | `[1, 2, 4, 7, 5, 9]` | `[1, 2]` | 0 | 1.000 | - | 1.000 | 24 |
| L6 | `[1, 2, 3, 7, 6, 3, 5, 11, 2]` | `[1, 2, 3]` | 1 | 1.000 | 3 | 1.000 | 720 |
| L7 | `[1, 2, 10, 3, 4, 5, 8, 13, 14]` | `[1, 2]` | 1 | 0.316 | 3 | 0.316 | 5040 |
| L8 | `[1, 2, 3, 4, 7, 3, 6]` | `[1, 2, 3, 4]` | 2 | 0.500 | 3 | 1.000 | 6 |
| L9 | `[1, 2, 3, 4, 5, 17, 3, 4, 17, 29, 13]` | `[1, 2, 3, 4, 5]` | 1 | 1.000 | 3 | 1.000 | 360 |

- **Global**: total additive triples = **10**; exact convolved null gives **p(total >= 10) = 0.444**.
- 🟡 **L2 carries a 4-term additive chain** (`3, 5, 8, 13` inside `[1, 2, 10, 3, 5, 8, 13, 14]`) -- per-line exact **p = 0.0389**.

### 3b. Discounts on the L2 Fibonacci flag (read before repeating it)
- **The chain exists only in the L2 variant.** Its near-duplicate L7 = `[1, 2, 10, 3, 4, 5, 8, 13, 14]` inserts a `4` and the 4-term chain collapses to the unremarkable 3-term `5,8,13` (L7 chain = 3, additive-triple p is ~chance in the table). Section 2 says L2/L7 plausibly transcribe the SAME recorded line -- so the entire flag **hinges on precisely the least-reliable token difference in the dataset.** The clean-audio confirm (thread 04 residual) decides which variant is real; until then this is a **fork, not a finding**.
- **Post-hoc family selection:** additive structure was tested because an eyeball note flagged it (thread 04). The corpus has scanned >= 6 pattern families (A1Z26, keypad, dates, primes, additive, anchors); a Bonferroni-type discount puts the effective p nearer ~0.23 even before the transcription uncertainty.
- **Control family (how cheap rival 'patterns' are):** reverse-additive triples (`a-b=c`) score, per line: L1=0, L2=0, L3=0, L4=1, L5=0, L6=0, L7=0, L8=0, L9=0 -- e.g. L4's `17,8,9` (17-8=9) 'hits' the mirror family by eye just as the #43 expose warns (*'you could obtain just about any type of result'*).

## 4. Post-derail 're-rail' runs (+1 increments after the derailment)
- L1: [[4, 5]]
- L2: [[13, 14]]
- L4: [[8, 9]]
- L7: [[3, 4, 5], [13, 14]]
- L9: [[3, 4]]
- Reading: after derailing she repeatedly falls back into **locally correct counting** (`3,4,5`, `13,14`, `3,4`) -- the texture of a mind that can increment but cannot hold the thread. This is the *shape S42 predicts*; an encoding has no reason to re-rail.

## 5. Vocabulary profile + anchor cross-flags (descriptive only)
- Values used: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 29]`; frequencies: 1x9, 2x11, 3x12, 4x8, 5x7, 6x3, 7x4, 8x3, 9x2, 10x2, 11x2, 13x4, 14x2, 17x4, 29x2.
- Missing below the max (29): `[12, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]` -- a contiguous 1-11 block, then isolated 13, 14, 17, 29. Small-number-dominant with sporadic jumps = babble-shaped; note **12 is never said** (a counter would pass through 12; a derailer skips anywhere).
- Anchor overlaps (weak, single small integers -- flags only, not evidence): `6` = Fort Brennand tally 6 [K7]; `7` = Fort Brennand tally 7 [K7]; `8` = 8 webs [K13a]; `29` = 29 = one of the matchstick operator numbers 53/23/29 [S21].
- 👁️ Eyeball ledger (recorded so they aren't re-discovered; NOT tested -- the target sets are unfalsifiable): the >10 values `11,13,17,29` are all prime; L3/L9's adjacent `17,29` concatenates to 1729 (the Hardy-Ramanujan number). Both are textbook pick-the-right-numbers bait per #43.

## Verdict
- **S42 is now statistically supported, not just convergent opinion:** counting prefixes 2-5 capped at 5, post-derail re-rail runs, babble-shaped vocabulary, and a global additive-structure test at **p = 0.44** (no tail-wide structure beyond chance).
- **One narrow, fragile exception:** the L2 variant's 4-term Fibonacci chain (`3,5,8,13`, exact per-line p = 0.039 pre-discount) -- but it evaporates under the L7 parse of the same line, and the L2/L7 difference is the dataset's least-reliable token. **The clean-audio confirm now decides two things at once** (the tail text AND this flag); its priority rises.
- Nothing here touches the [K23] *opening* string, which remains a deliberate, Rockstar-flagged token ([S42]'s middle reading: signature string deliberate, tail = madness texture -- this run is *consistent with* that reading).
- All conclusions are **[SPECULATION]-grade on PROVISIONAL data**; upstream of the [K16] frontier; no decode was attempted (the tail-cipher gate stands).
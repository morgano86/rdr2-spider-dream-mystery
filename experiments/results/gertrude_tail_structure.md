# Result -- Gertrude structure battery on the CANONICAL [K42] set (`gertrude_tail_structure.py`)

Tests **[S42]** (failed-counting characterisation) vs *deliberate tail structure* on the
**CANONICAL 12-line game-text inventory** ([K42], A-tier, #78 -- the game's own subtitle
strings, in-repo copy on file). Exact permutation nulls; each unit's correct counting
prefix is **fixed** under the null so the conceded "she starts 1,2,3..." shape cannot
score as signal. **Supersedes the 2026-07-04 run on the provisional 9-line video
transcription** (global p was 0.44; the 'L2' chain p was 0.039 read as a transcription
fork -- K42 dissolved that frame: the fork's two variants are the REAL lines A and B).
No decode attempted; a positive here is [SPECULATION] at most.

## 1. Counting-prefix shape (the S42 prediction)
- Correct-prefix length per unit: A1=3, A2=2, B1=0, B2=0, C1=5, C2=2, D=3, E=0, F=5, G=4, H1=2, H2=4, I1=4, I2=2, I3=1, J=2, K=1, L=0.
- Every unit that STARTS counting derails by **5** -- no counting attempt in the game's own text ever passes five (C1 and F reach exactly `1..5`; the StrangeMan caption *'she only manages to count up to five'* is literally true in the canonical strings).
- Units with **no counting start at all**: `B1, B2, E, L` -- these are not counter-examples to the S42 shape; section 2 shows they are **continuation fragments** of the full lines, not independent recitations.

## 2. The prefix-0 lines are continuation fragments (new, canonical-only finding)
- **B is a window onto A's stream.** A (concatenated) = `[1, 2, 3, 7, 6, 4, 5, 11, 2, 1, 2, 10, 3, 5, 8, 13, 14]`; B = `[5, 11, 2, 1, 2, 10, 3, 4, 5, 8, 13, 14, 1]`. B's head `[5, 11, 2, 1, 2, 10, 3]` is **verbatim** A's tokens 7-13; full token-Levenshtein(A[7:], B) = **2** (one inserted `4`, one appended `1`). So the 'edit-distance-1 pair' of the old battery is really *one babble stream recorded twice with variation*, canonically.
- **L (`[8, 9, 3]`) is verbatim the last 3 tokens of C1 (`[1, 2, 3, 4, 5, 17, 8, 9, 3]`)** -- a chopped-out tail fragment given its own line.
- **E (`[3, 4, 17, 29, 13]`) opens mid-count** (3,4) and carries the corpus's only 29 -- fragment-shaped, though no parent line contains it (the video's 'L9' chained it after F, whose `...5, 17?` it continues naturally: `1..5,17 / 3,4,17,29,13`).
- Reading: the 12 recorded lines behave like **windows cut from one longer failed-counting babble take** (a standard VO-session shape: one long improvisation chopped into triggerable barks). This *explains* the prefix-0 lines inside S42 rather than against it, and explains why the 2019 listeners naturally chained them (video L6/L7 = B's halves, L9 = F+E). It also frames the Fibonacci fork correctly: **A and B are two takes of the same material**, and the `4` that breaks the chain is intra-take variation (sec 3b).

## 3. Additive (Fibonacci-type) structure in the derailed tails -- exact permutation null
- Statistic: consecutive triples `a,b,a+b` over the full unit; null = counting prefix fixed, derailed tail exactly permuted (all distinct orders enumerated; no sampling).

| unit | seq | prefix fixed | additive triples (obs) | p(>=obs) | longest chain (obs) | p(chain>=obs) | tail orders |
|---|---|---|---|---|---|---|---|
| A1 | `[1, 2, 3, 7, 6, 4, 5, 11, 2]` | `[1, 2, 3]` | 1 | 1.000 | 3 | 1.000 | 720 |
| A2 | `[1, 2, 10, 3, 5, 8, 13, 14]` | `[1, 2]` | 2 | 0.064 | 4 | 0.039 | 720 |
| B1 | `[5, 11, 2, 1, 2, 10, 3]` | `[]` | 0 | 1.000 | - | 1.000 | 2520 |
| B2 | `[4, 5, 8, 13, 14, 1]` | `[]` | 1 | 0.189 | 3 | 0.189 | 720 |
| C1 | `[1, 2, 3, 4, 5, 17, 8, 9, 3]` | `[1, 2, 3, 4, 5]` | 1 | 1.000 | 3 | 1.000 | 24 |
| C2 | `[1, 2, 4, 7, 5, 9, 1]` | `[1, 2]` | 0 | 1.000 | - | 1.000 | 120 |
| D | `[1, 2, 3, 7, 6, 3]` | `[1, 2, 3]` | 1 | 1.000 | 3 | 1.000 | 6 |
| E | `[3, 4, 17, 29, 13]` | `[]` | 0 | 1.000 | - | 1.000 | 120 |
| F | `[1, 2, 3, 4, 5, 17]` | `[1, 2, 3, 4, 5]` | 1 | 1.000 | 3 | 1.000 | 1 |
| G | `[1, 2, 3, 4, 7, 3, 6]` | `[1, 2, 3, 4]` | 2 | 0.500 | 3 | 1.000 | 6 |
| H1 | `[1, 2]` | `[1, 2]` | 0 | 1.000 | - | 1.000 | 1 |
| H2 | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` | 1 | 1.000 | 3 | 1.000 | 1 |
| I1 | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` | 1 | 1.000 | 3 | 1.000 | 1 |
| I2 | `[1, 2]` | `[1, 2]` | 0 | 1.000 | - | 1.000 | 1 |
| I3 | `[1]` | `[1]` | 0 | 1.000 | - | 1.000 | 1 |
| J | `[1, 2]` | `[1, 2]` | 0 | 1.000 | - | 1.000 | 1 |
| K | `[1, 1, 1]` | `[1]` | 0 | 1.000 | - | 1.000 | 1 |
| L | `[8, 9, 3]` | `[]` | 0 | 1.000 | - | 1.000 | 6 |

- **Global**: total additive triples = **11**; exact convolved null gives **p(total >= 11) = 0.335**.
- 🟡 **A2 carries a 4-term additive chain** (`3, 5, 8, 13` inside `[1, 2, 10, 3, 5, 8, 13, 14]`) -- per-unit exact **p = 0.0389**.

### 3s. Whole-stream check on line A (seeded Monte-Carlo -- closes the cross-unit gap)
- Line A as ONE stream (`[1, 2, 3, 7, 6, 4, 5, 11, 2, 1, 2, 10, 3, 5, 8, 13, 14]`; prefix `[1, 2, 3]` fixed, 14-token tail shuffled; seed=42, n=200,000): observed triples = 3 -> **p ≈ 0.154**; observed longest chain = 4 -> **p ≈ 0.163**.
- (B as one stream has 1 triple / a 3-term chain -- unremarkable; not simulated.) Note the whole-stream view is **more deflationary than the per-unit one for the chain stat**: given line A's full 14-token derailed vocabulary, a 4-term additive chain somewhere in it is unremarkable (p ≈ 0.16). The per-unit p = 0.039 conditions on the chain landing inside the shorter A2 window -- take the whole-line number as the fairer weight.

### 3b. Discounts on the line-A Fibonacci flag (read before repeating it)
- **The transcription discount is GONE** -- `...3, 5, 8, 13, 14...` is the game's own canonical text in line A ([K42]). What remains is interpretive, not evidential:
- **The variant take breaks it.** B re-records the same material and inserts a `4` (`...10, 3 | 4, 5, 8, 13, 14, 1`), collapsing the 4-term chain to the unremarkable 3-term `5,8,13`. If `3,5,8,13` were a deliberately planted token, preserving it in the *only other take of the same passage* is the natural authorial move; breaking it is the natural *babble* move. Leans deflationary.
- **Post-hoc family selection stands:** the additive family was tested because an eyeball note flagged it; the corpus has scanned >= 6 pattern families (A1Z26, keypad, dates, primes, additive, anchors). A Bonferroni-type discount puts the effective p nearer ~0.23.
- **13 and 14 are ordinary vocabulary here:** `13,14` also appears as a re-rail run (+1 counting) and 13 recurs in E outside any additive context -- the chain's tokens are not reserved 'Fibonacci' tokens.
- **Control family (how cheap rival 'patterns' are):** reverse-additive triples (`a-b=c`) per unit: C1=1 -- e.g. C1's `17,8,9` (17-8=9) 'hits' the mirror family by eye, exactly the #43 warning (*'you could obtain just about any type of result'*).

## 4. Post-derail 're-rail' runs (+1 increments outside the counting prefix)
- A1: [[4, 5]]
- A2: [[13, 14]]
- B1: [[1, 2]]
- B2: [[4, 5], [13, 14]]
- C1: [[8, 9]]
- E: [[3, 4]]
- L: [[8, 9]]
- Reading: after derailing she repeatedly falls back into **locally correct counting** (`4,5`, `13,14`, `8,9`, `3,4`, `1,2`) -- the texture of a mind that can increment but cannot hold the thread. This is the *shape S42 predicts*; an encoding has no reason to re-rail.

## 5. Vocabulary profile + anchor cross-flags (descriptive only)
- Values used across all 12 canonical lines: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 29]`; frequencies: 1x19, 2x15, 3x14, 4x9, 5x7, 6x3, 7x4, 8x4, 9x3, 10x2, 11x2, 13x3, 14x2, 17x3, 29x1.
- Missing below the max (29): `[12, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]` -- a contiguous 1-11 block, then isolated 13, 14, 17, 29. Small-number-dominant with sporadic jumps = babble-shaped; **12 is never said in the game's own text** (a counter would pass through 12; a derailer skips anywhere). This survives from the provisional run intact.
- Anchor overlaps (weak, single small integers -- flags only, not evidence): `6` = Fort Brennand tally 6 [K7]; `7` = Fort Brennand tally 7 [K7]; `8` = 8 webs [K13a]; `29` = 29 = one of the matchstick operator numbers 53/23/29 [S21].
- 👁️ Eyeball ledger (recorded so they aren't re-discovered; NOT tested -- the target sets are unfalsifiable): the >10 values `11,13,17,29` are all prime; E's adjacent `17,29` concatenates to 1729 (the Hardy-Ramanujan number). Textbook pick-the-right-numbers bait per #43.

## Verdict
- **S42 survives the move to canonical data:** every counting attempt in the game's own strings caps at **5**; the prefix-0 lines resolve into continuation fragments of one babble stream (sec 2); post-derail re-rail runs and babble-shaped vocabulary persist; and the tails carry **no additive structure beyond chance globally (exact p = 0.34)**.
- **The one flag is now a fixed fact of the text, weighed and held at [SPECULATION]:** line A's verbatim `3,5,8,13` (4-term chain, exact per-unit p = 0.039; ~0.23 after the family-selection discount). The old fork is DECIDED (both variants real) and the resolution cuts against design: the only other take of the same passage (B) breaks the chain. Verdict: **suggestive-not-significant; do not build on it without an independent hook** (e.g. a source connecting Gertrude to Fibonacci deliberately).
- Nothing here touches the [K23] *opening* string, which remains a deliberate, Rockstar-flagged token (S42's middle reading -- signature string deliberate, tail = madness texture -- is *consistent with* this run).
- Conclusions are computational evidence on **[K42] A-tier inputs**; the S42 characterisation itself stays [SPECULATION] (a script tests, it doesn't establish fact); upstream of the [K16] frontier; no decode attempted (the tail-cipher gate stands, though with the text now canonical the gate's *audio-confirm* clause is moot -- what gates decoding now is the absence of any sourced key).
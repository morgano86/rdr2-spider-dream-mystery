# Result -- Gertrude's numbers cipher harness (`gertrude_cipher.py`)

Systematic battery on the **confirmed** string `1237645112` ([K23], B-tier) plus the **provisional** tail ([U6], transcription-only). Tests U6/S5. Per the #43 hoax expose's own warning -- *"you can get any result if you pick the right numbers"* -- every positive below is **coincidence-prone [SPECULATION]**; the load-bearing result is the **null landscape**. Nothing here is promoted; upstream of the [K16] frontier.

- CONFIRMED [K23]: `[1, 2, 3, 7, 6, 4, 5, 1, 1, 2]`  (opening seven `[1, 2, 3, 7, 6, 4, 5]` solid under any parsing)
- PROVISIONAL [U6]: `[1, 2, 3, 7, 6, 4, 5, 11, 2, 1, 2, 10, 3]`  (tail transcription-only -- do not trust)

## 1. A1Z26 letter cipher (1->A ... 26->Z) -- reproduces hand attempt A
- CONFIRMED `1237645112` -> **ABCGFDEAAB**
- PROVISIONAL full       -> **ABCGFDEKBABJC**  *(tail-dependent letters K/J from 11/10 are PROVISIONAL)*
- Reading: no English word/phrase; opens `ABC...` then scatters. **NULL** (confirms attempt A; the late `J` only exists in the untrusted tail).

## 2. Phone-keypad / T9 reading (NEW) -- the "call the number back" reading
- The GTA "Nazar Speaks" machine makes `1237645112` a number you **call back** ([K23]). On a keypad, **1 carries no letters** (word breaks), so the string `1237645112` splits into letter-runs: **['237645', '2']**.
  - run decodings (no shipped dictionary -> sizes only): `237645`=972 combos, `2`=3 combos. The 6-letter run can't be exhaustively English-checked stdlib-only; reverse-check below is the deterministic test.
  - reverse-check (mystery word -> keypad digits -> is it IN the string?):
    - 🟡 **FROG** dials `3764` (offset 2 of `1237645112`): a **windowed** sub-decode -- it sits inside the `237645` run but drops the run's own first/last letter, i.e. a chosen window.
    - ⚠️ This is the "pick the right digits" coincidence #43 warns of, made concrete: **`FROG` was put in the target list precisely because the author spotted `3764`=FROG by eye** -- and that a meaningless word "hits" as a chosen window of the run is exactly why a single substring decode proves nothing. Logged as **coincidence, NOT a reading.**
  - Net: the keypad reading yields **no word that fills a whole letter-run**; the only hit is a *chosen window* inside the run (`FROG`), which is meaningless. **NULL/coincidence.** (First time this reading is tested.)

## 3. Permutation structure of `1,2,3,7,6,4,5` (NEW) -- the missing half of attempt B
- Is the opening seven a permutation of 1-7 (the exact tally range)? **True** -- it uses each of 1..7 exactly once.
- Cycle decomposition (position -> value): **fixed points = [1, 2, 3]**, **cycle(s) = [[4, 7, 5, 6]]**.
- Reading: positions **1,2,3 are IDENTITY** (a node read in this order stays put), and **4,5,6,7 form a single 4-cycle** `(4 7 5 6)` (node4->pos7, node7->pos5, node5->pos6, node6->pos4). So as a reorder of 7 tally-nodes it **leaves Butcher Creek's 1-3 fixed and scrambles only the {4,5,6,7} tail** (outhouse #4/#5 + the two Fort Brennand tallies). That is a clean *structural* observation about the number, independent of any decode -- and it sharpens attempt B: the reorder is non-trivial **only** on the BC#4->Brennand stretch, which is also where the `LJ`/`SM` carving and the Fort Brennand pointer live. ⚠️ Still BLOCKED as a decode: the 7 nodes carry bare counts, so there is nothing per-node to spell once reordered ([U6], connections §3).

## 4. Arithmetic & structural readings
- digit sum: opening7 = **28**, confirmed10 = **32**, provisional = **57** (PROVISIONAL). No anchor matches (28/32 are not mystery constants).
- first differences of `1237645112`: **[1, 1, 4, -1, -2, 1, -4, 0, 1]** -- no monotone run, no obvious geometric/clock pattern. NULL.
- digit multiset of confirmed: {1: 3, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1} -- `1`x3, `2`x2 dominate; no 8, 9, or 0. (8 webs absent.)

## 5. Date / numeric-window readings
- Leading-digit date parses: `1/2/3...` (1 Feb?), `12/3` (12 Mar), `123/7` -- all require dropping the rest; the string is **10 digits with no year-shaped run** (no 18xx/19xx; `1237` reads as a 13th-century year, off-setting). **NULL** -- no clean in-fiction date (1899 / RDR2's era) falls out.

## 6. Cross-reference vs sourced mystery number anchors
- Does the confirmed string CONTAIN any anchor as a contiguous run?
  - Butcher Creek tallies (1-5) [K4]: `12345` -> no
  - Fort Brennand tallies (6,7) [K7]: `67` -> no
  - all tallies 1-7: `1234567` -> no
  - feather split 5 black / 3 red [K13]: `53` -> no
  - 8 webs [K13a]: `8` -> (single digit)
  - five poles west [K12]: `5` -> (single digit)
  - The only multi-digit anchor that is a substring would be flagged above; net **NO multi-digit anchor is a contiguous substring**. The opening seven matching the **1-7 tally RANGE** (as a permutation, §3) is the one real structural tie -- but a range-match is weak (any 1-7 permutation would).

## Verdict
- **Null across the board**, as expected for a 10-digit string under many transforms.
- Two readings tested for the first time both come back **null/coincidence**: the phone-keypad "call-back" reading (only a meaningless windowed hit, `FROG`, per the #43 warning) and arithmetic/date parses.
- The **one durable, non-decode finding** is structural (§3): `1,2,3,7,6,4,5` is a permutation of 1-7 that is **identity on 1-3 and a 4-cycle on {4,5,6,7}** -- so if it ever indexes the seven tally nodes, it only reorders the BC#4 -> Fort Brennand tail. That refines attempt B's premise but does **not** unblock it (no per-node content to spell; [U6]).
- Status unchanged: Gertrude's numbers are a **deliberate, Rockstar-flagged cipher-candidate** ([K23]) whose **decode and spider-link remain open** ([U6]). This harness logs the negative and adds the keypad + permutation tests to the record.
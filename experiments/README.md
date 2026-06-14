# experiments/ — computational tests

Small, self-contained scripts that **test** the investigation's findings when prose reasoning isn't enough and the
question is really about *combinations, ciphers, geometry, or likelihoods*. This is the one place in the repo where you
run code instead of writing prose — everything else is Markdown.

> **A script TESTS; it does not establish fact.** Output is evidence subject to the same tagging discipline as
> everything else: a positive computational result is at most **[SPECULATION]** until corroborated in-game or by a
> source; a negative result (e.g. *"A1Z26 → null"*) is a real, loggable finding that can demote or kill a hypothesis.
> Nothing a script prints is **[KNOWN]** on its own.

## When to reach for a script (and when not)
Write one only when the answer needs mechanical search/computation that's error-prone or infeasible by hand:

- **Combinatorial search** — orderings/permutations (e.g. feather shooting order, U0/H4), which arrangements satisfy a
  known constraint. → see [`feather_order.py`](feather_order.py).
- **Cipher / encoding tests** — A1Z26, substitution, coordinate/grid decoding, date readings of Gertrude's numbers
  (U6/S5); the attempts described in [`analysis/connections.md`](../analysis/connections.md).
- **Likelihood / coincidence checks** — e.g. quantifying the dev-initials counter-argument (how probable is a matching
  `LJ`/`SM` among N credited staff?), to keep [SPECULATION] honest.
- **Set cross-referencing** — match a credits/character name list against initials (U4/U16) once the list exists.
- **Geometry / position math** — pole bearings, "five poles west", mapping the 8 webs to an overlay.

**Don't** script what reasoning already settles, and don't script around missing data — if an input is unknown
(e.g. the full Gertrude sequence, U6), say so; the script's conclusion inherits that uncertainty.

## Conventions
- **Python 3, standard library only** where possible (keep it reproducible with no install). If a dependency is truly
  needed, add a `requirements.txt` and note why.
- **Filenames** are `snake_case.py`, named for the question: `feather_order.py`, `gertrude_cipher.py`, `initials_likelihood.py`.
- **Every script opens with a docstring** stating: the **question + the IDs it tests** (`U#`/`H#`/`S#`/`K#`); its
  **inputs and their provenance/tag** (cite the source file — never invent data); what a positive vs negative result
  would *mean*; and the run command.
- **Deterministic.** No reliance on wall-clock/network; if you need randomness (e.g. a Monte-Carlo likelihood), seed it
  and print the seed.
- **Mark provisional inputs in-line** (a `# PROVISIONAL (U6)` comment) so nobody mistakes a test on shaky data for a result.
- **Output to stdout** with a clear summary; if a run matters, save a short note under `experiments/results/<name>.md`
  (create the folder when first needed) rather than letting findings drift into code comments.

## How results feed back into the corpus
1. Re-run the script before citing it (paste the command + key output).
2. Record meaningful runs in [`INVESTIGATION_LOG.md`](../INVESTIGATION_LOG.md) — *including null results.*
3. Route the conclusion to the right place by ID: the thread, the [findings](../findings) rollup, and/or the
   [analysis](../analysis) file. A confirmed-by-computation-only result stays **[SPECULATION]**; promotion to **[KNOWN]**
   still requires the normal primary/reproducible sourcing (see [`../CLAUDE.md`](../CLAUDE.md)).
4. Append the new script to the index below.

## Scripts
| Script | Tests | Status |
|--------|-------|--------|
| [`feather_order.py`](feather_order.py) | U0 / H4 / K13b — collapses the 8-web shooting-order search space against the documented non-respawn chain | works; **U0 orientation now resolved (tip-down → H4 refuted), so the filter it awaited won't come from orientation**; superseded for the order question by `web_time_order.py` + the [U29] group data |
| [`web_time_order.py`](web_time_order.py) | U0 / H4 / K13b / H9 / **H17** — cross-references the non-respawn chain with each web's active hour; tests "is the order just the clock?" | works; **K13b chain is exactly chronological & reproducible by sorting the H9 Connector boundary by hour** (clock = sufficient key, deflates H4) — **but [H17] then REFUTED-leaning** by sourced red data (`R34→R45→R23` works, non-chronological); emits the (now-falsified) reds-chronological prediction + the time-lock-vs-persistence question ([U29]) |
| [`name_match.py`](name_match.py) | U4 / U5 / U16 / U24 / H11 / H12 / S16 / S17 — cross-references the 5 letter markings vs sourced name lists: Register Rock + the **Van der Linde gang** (thread 07), under 3 rules, **and now per [H12] group** | works; rock → J+M & S.G hits + missing-`L`; **gang → exact `SM`=Sean MacGuire, `J+M`=John Marston, supplies `L`, but `EC` matches nothing**; per-group view: vs gang, Group 1 carved gets `SM`, the `J+M` node gets `J+M`; also caught a corpus multiset slip (true `{C,E,J,J,J,L,M,M,S,S}`) |
| [`letters_cipher.py`](letters_cipher.py) | U5 / U25 / H12 / S2 / S18 — anagram/cipher feasibility of the letter set (vowel budget, subset-spell, A1Z26); the "read as pairs" result is what motivates the [H12] per-group view | works; **whole-set anagram ruled out** (vowel-starved, J-heavy → read as pairs not reshuffle); one flag: `EC`→A1Z26 `5,3` = the 5/3 feather split ([S18]) |
| [`initials_likelihood.py`](initials_likelihood.py) | S16 — coincidence odds of the gang name-matches (Monte-Carlo, 2 null models) | works; **the 2-of-5 hit count is weak evidence** — P≈0.04 uniform but **≈0.59** under realistic name-initial frequencies → S16 softened to suggestive-only |
| [`number_grid.py`](number_grid.py) | U5 / U25 / U26 / S18 / S21 / K25 / **K26** / H14 — numeric-code, **punctuation-as-operator**, + map-grid / **coordinate** readings | works; plain numeric forms null; **[S21] operator reading**: matchsticks → 53/23/29 (all prime) or 532329, only `EC`=53=feather split lands; **grid spec now CAPTURED ([K26]):** Map 1 (1–30 × A–U) + Map 2 (A–O × 1–7) filled in & re-run → **per-cell reading NEGATIVE-leaning** — on Map 2 (the game-world grid) only `EC` is in range, the rest exceed the 7-row cap; no single grid validates all five. **[H14]** survives only as a free coordinate plot (precedent [K25]) |
| [`web_colour_group_order.py`](web_colour_group_order.py) | U29 / H9 / **H18** / K13a / K13b — the **colour×hour lattice** + the **colour-group** shooting order (mural-as-seed) | works; **[KNOWN] lattice verified**: each 2/3/4 AM hour = 1 black + 1 red, 5–6 AM = 2 blacks (the [K13b] interchangeable pair), each red hour-twinned to a black; the [U29] reset rules collapse 8! = 40,320 → **180** (with `B34` last); the **colour-group order** ("reds free → connector chain → `B34` last") is **consistent** with the survivors (one sub-family — consistency, not proof) → reinforces the group/boundary reading ([H9]) over a feather sequence ([H4]/[H17] dead) |
| [`web_socket_position.py`](web_socket_position.py) | U0 / **H19** / H9 / U29 — the per-web feather **socket** (L/C/R vs the web's central radial), closing the [U0] residual + testing it for structure | works; **camera-invariant reads agree 8/8** with the prior screen-relative reads (confound didn't flip the gross call → socket usable); **colour↔side NOT significant** (reds-right lean p=0.125); only the **3 hour-twinned blacks sweep `L→C→R`** (p≈0.04) and **B56/BL56 share hour+socket**; mostly-negative → weak colour-axis line, does **not** revive [H4] (socket ≠ orientation) |

### Sample run (`python experiments/feather_order.py`)
```
Total orderings (8!):                  40,320
Consistent with non-respawn chain:      3,360  [K13b]
```
*Interpretation: the one documented ordering fact already removes ~92% of arrangements; capturing feather orientation
(U0) is what would collapse the remaining 3,360 toward a single order. The candidates printed are illustrative, not findings.*

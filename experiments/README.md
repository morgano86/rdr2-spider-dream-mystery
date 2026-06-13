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
| [`feather_order.py`](feather_order.py) | U0 / H4 / K13b — collapses the 8-web shooting-order search space against the documented non-respawn chain | works; awaits U0 feather-orientation data to filter further |

### Sample run (`python experiments/feather_order.py`)
```
Total orderings (8!):                  40,320
Consistent with non-respawn chain:      3,360  [K13b]
```
*Interpretation: the one documented ordering fact already removes ~92% of arrangements; capturing feather orientation
(U0) is what would collapse the remaining 3,360 toward a single order. The candidates printed are illustrative, not findings.*

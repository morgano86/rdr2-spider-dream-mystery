# Result — full-credits initials match (`credits_initials_match.py`)

**Question:** if the markings are *developer initials*, who in the **full RDR2 end credits**
(`rdr2-credits.txt`, 6,345 credited people) do `LJ`/`SM` (outhouse [K6]) and
`EC`/`J+M`/`S+J` (matchsticks [K9]) match — and are any of them senior enough to plausibly
be honoured with hidden in-world initials? Tests the dev-initials counter-hypothesis
(U4 / U25 / S16; analysis/connections.md, threads 02 & 03).

**Rule (forward-only, user choice 2026-06-21):** one-person reading — a person matches an
**ordered** pair `(X, Y)` iff **first-name initial == X AND last-name initial == Y**, in the
marking's written order. So `EC` = `E.____` firstname + `C.____` lastname **only**; the
reversed `C.____ E.____` is *not* a match. Seniority tier is a keyword **heuristic**, not fact.

## Run (2026-06-21, forward-only)

| Marking | X.first + Y.last | Matches | Senior+ | exec/dir | lead |
|---------|------------------|--------:|--------:|---------:|-----:|
| `LJ`  | L. + J. | **5**   | 4  | 0 | 1 |
| `SM`  | S. + M. | **87**  | 51 | 7 | 9 |
| `EC`  | E. + C. | **13**  | 7  | 2 | 3 |
| `J+M` | J. + M. | **58**  | 32 | 6 | 12 |
| `S+J` | S. + J. | **22**  | 7  | 0 | 3 |

Forward-only roughly halves-to-quarters the earlier order-insensitive counts (e.g. `LJ` 42→**5**,
`S+J` 73→**22**). The point survives: the commonest pair `SM` still matches **87** people, so a
dev-initials match remains near-certain by chance. But `LJ` is now genuinely tight — only **5**
auto-matches, of which the lone "classic" forward hit is **Lee Johnson** (HR Manager) — plus the
**Lazlow** manual match. (Earlier order-insensitive run, for the record: LJ 42 / SM 144 / EC 21 /
J+M 70 / S+J 73.)

**Two-people (`+`) reading is unfalsifiable.** First/last-initial pool sizes:
J = 603 first / 191 last · M = 544 / 621 · S = 736 / 698 · L = 202 / 254 · E = 174 / 114 ·
C = 347 / 454. So `J+M` read as *two separate honourees* = 603 × 621 = **374,463** possible
pairings. There is no constraint that picks a unique pair.

## Reading (evidence, not fact — [SPECULATION] at most)

- A match here is **near-certain by chance**: with ~6.3k staff, every 2-letter pair lands
  dozens of people. So the *existence* of a dev-initials match is **not evidence** — it
  reinforces the corpus stance that the dev-initials reading is weak (cf.
  [`initials_likelihood.py`](../initials_likelihood.py): the gang 2-of-5 hit also dissolves
  under realistic name-initial frequencies).
- The only part worth a human look is the **senior/exec shortlist per marking** (top of each
  results file). Everything below it is elimination fodder.
- This neither confirms nor refutes any individual; it **quantifies why "these are dev
  initials" is unfalsifiable**. The user's own objection — that <10 people out of 6,345
  having world-hidden initials would be odd, and the `+` two-people reading is structurally
  strange — is borne out by the pool sizes.

## Mononyms + the Lazlow manual match (added 2026-06-21)

The auto first+last rule **skips single-name credits** (no distinct second initial). Two such
checks were added:

- **Manual match, `LJ` ← Lazlow.** Credited mononymously as **"Lazlow"** (Director Audio
  Content) = **Jeffrey Crawford "Lazlow" Jones** (Wikipedia, B/C). Community reads `LJ = Lazlow
  Jones`. Recorded as a curated manual match with provenance — **[SPECULATION]**, not promoted.
  Caveat (user, 2026-06-21): as the *audio* director you'd expect audio-led clues; only the
  guitar near the trail end is audio-adjacent, so the tie is thin. (Note his birth initials are
  actually J.C.J. / J.J. — `LJ` only works via the *stage* name.)
- **Mononym sweep.** Of 6,345 credits, **exactly 2** are single-name: **Lazlow** and **Ajay**
  (Associate AI/Gameplay Programmer, Rockstar India — junior, no surname on file → weak lead).
  Written to `results/single_name_credits.txt` as a lead list (not matches).

That mononyms are this rare (2/6,345) cuts both ways: it makes Lazlow *distinctive* among
credits, but a distinctive credit is not evidence of authorship — and the `LJ`-via-stage-name
reading still rides on the same near-certain-by-chance problem as every other pair.

## Outputs
- `results/outhouse_initials_matches.txt` — `LJ`, `SM` (NAME / ROLE, senior-first; Lazlow manual).
- `results/matchstick_initials_matches.txt` — `EC`, `J+M`, `S+J` (NAME / ROLE, senior-first).
- `results/single_name_credits.txt` — the 2 mononym credits (lead list).

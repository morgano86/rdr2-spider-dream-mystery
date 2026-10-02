# web_file_order_concordance.py - results (2026-07-02)

**Question.** Now that [K39] made the per-web `spiderdream0X` numbers real data, are they the intended **shooting order** (1→8, or 1→5 blacks-only per [H24])? First test of the numbering *as an ordering*, here or in the community. Run: `python experiments/web_file_order_concordance.py` (stdlib, exhaustive - no sampling; nulls are conditional on the already-known [S29] colour blocks so the [S29] discovery isn't double-counted).

## Headline: NEGATIVE - the file numbers order nothing beyond chance

Across every ordering principle on record, the strongest uncorrected p is **0.083**, with ~6 primary tests run (look-elsewhere ⇒ nothing survives):

| Test | File-order result | p (conditional null) |
|------|-------------------|----------------------|
| Chronology (tau vs hour) | blacks tau −0.778, full-8 tau −0.500 | 0.133 / 0.133 |
| **[K13b] chain in the DESC read** (the investigator's eyeball) | **TRUE** - blacks 5→1 = `B23>B45>B34>B56>BL56` = the chain with `B34` inserted mid-run | **10/120 = 0.083** one-direction; **0.167** counting the ASC/DESC freedom |
| [H19] socket sweep L→C→R | no sweep (`L,L,C,R,L`) | 0.32–0.60 |
| Clockwise winding around the body ([S31] coords) | none | 0.53 / 1.00 |
| Nearest-neighbour path | 5/7 full-8 (blacks 2/4) | 0.15 / 0.75 |
| Tour length | shortish, not significant | 10.6% / 16.7% percentile |
| Telegraph-line adjacency | **not testable** - no line-topology data on file; skipped, not invented | - |

**The eyeballed observation is real but weak**: p≈1/12 before the direction freedom, ≈1/6 after, before the other principles tried. It does not establish the numbers as an order.

**What the numbers *do* look like:** a structured **index** - the known [S29] blocks (1–5 blacks / 6–8 reds, twin-sum-11) plus a region check here (files 2–5 = the four New Hanover webs, but conditional on the colour blocks that contiguity is p=0.4 - a free rider, not new structure). **Constrains [S29]:** the deliberateness evidence in the numbering is its *labelling scheme*, not a sequence.

## The feasibility sweep ([K29]/[K31] visible-state simulator) - three independent checks landed

1. **The blacks-only criterion is exactly "`BL56` before `B34`"** (60/120 orders keep all 5 visibly down; the flag coincides with that predicate on all 120) - an independent desk re-derivation of the investigator's [H24]-correction geometry.
2. **All-8-simultaneously-down is impossible: 0/40320.** `R34` lives only in the red zone, `B34`'s hold needs orange, and no visiting order avoids the fatal exit - the [H22] seam, now exhaustively verified and shown to be **colour-order independent** (reds-first, the favoured R2 protocol, is just as visibly-infeasible as any other; only hidden-flag semantics can save *any* 8-order).
3. Only **3 of 120** black orders are both feasible *and* [K13b]-consistent - Test C's order plus two `BL56`-early variants (`B23>B45>BL56>B56>B34`, `B23>B45>BL56>B34>B56`).

## Ranked, falsifiable candidate shooting orders for the next field session ([S38])

| Rank | Order | Status | Why / cost |
|------|-------|--------|------------|
| 1 | **Test C**: `B23>B45>B56>BL56>B34` | feasible, 2 nights, [K13b]-forward | unchanged as the top pick; already protocolised |
| 2 | **blacks file-ASC** `BL56>B56>B34>B45>B23` (files 1→5) | **the only file-order read that survives visible-state** - feasible, 3 nights, satisfies `BL56`<`B34` | the genuinely new candidate; a hit vindicates "numbers = order". Note it *reverses* [K13b] - but [H9] already reframed the "chain" as boundary membership, under which any within-yellow order holds, so the reversal is not disqualifying |
| 3 | **blacks file-DESC** `B23>B45>B34>B56>BL56` (files 5→1) | K13b-with-`B34`-inserted, 2 nights, **infeasible under visible-state** (`B34` resets exiting orange for `BL56`) - viable only under hidden-flag semantics ([H22]-R2) | run only if R2 gains support; it differs from Test C solely in `B34`'s slot (mid vs last) |

The two file-order readings **fork exactly on the [H22] R1/R2 semantics** - a neat mapping of "are the numbers the order?" onto the case's existing #1 open mechanic.

## Caveats
- File numbers, colour×hour lattice, socket reads: **C-tier** (manifest provenance notes).
- Map coords: **PROVISIONAL** overlay pixels ([S31]), ±25 px.
- The night/mixed-colour accounting leans on [H20] firsthand feasibility (inference-grade).
- A script tests; nothing here is [KNOWN]. Rank-2/3 candidates are [SPECULATION] pending in-game test.

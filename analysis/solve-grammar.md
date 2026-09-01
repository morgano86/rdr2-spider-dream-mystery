# The solve grammar of RDR2's solved eggs — and the webs read WITHOUT the shooting premise ([H27])

**Status: [SPECULATION] throughout — home file for [H27]; extends [S28]; fresh-pass 2026-07-02 (second
premise-drop session under the fresh-eyes rule).** The dropped premise this pass: **"the webs must be
shot at all."** Every frame since late 2025 — [K13b], [U29], [H20], [H22], [H24], Tests A/B/C — assumes
feather-shooting is the puzzle's input. This file re-reads the KNOWNs assuming the feathers are a
**display to be witnessed/read**, not a target; formalizes the solve grammar of the game's three solved
eggs; and scores which grammar the web system resembles. Built only from established data
([K5]/[K11]/[K12]/[K18]/[K21]/[K27]–[K31]/[U29]/[H6]/[H9]); nothing chases past the **[K16] frontier**.

---

## 0. Why the premise is droppable at all

Trace the provenance of "shoot the feathers":

- **No verified clue instructs it.** The verified chain's instructions are all *directional/navigational*
  (the engraving "shows the direction" [K11]; centre webs spell `N`+pole; `W ✞✞✞✞✞`; `NW`+guitar). Not
  one sourced clue says *shoot a feather* or references feather state.
- **It is a community inference** from two observations: feathers *can* be shot and *respawn oddly*
  ([K13b]), i.e. the game visibly tracks something. The leap from "the game tracks it" to "it is the
  intended input" was never sourced — and [H9]/[K31] already showed the tracked "chains" are just
  **boundary-membership geometry**.
- Where shooting *does* appear in the verified chain — the two shot-to-reveal poles ([K12]) — it is a
  **REVEAL mechanic**: destruction yields *information* (an inscription), once, idempotently. Feather
  shooting yields **no information at all** ([K29]: the fallen feather's position is pure shot-physics,
  "encodes nothing") and no state you can read back except the feather's own absence. In the trail's
  own design language, an information-free, state-setting shot is **anomalous**.

So the premise is exactly the kind of frame the fresh-eyes rule exists to drop.

## 1. The grammar, formalized from the three SOLVED eggs (before scoring — no peeking at the webs)

Feature set derived from the Saint Denis Vampire ([K27]), the Window Rock Strange Statues mural
([K18]), and the Dreamcatchers ([H6] precedent; wiki-solved), with the Butcher Creek pentagram ([K5])
as the unaided fourth instance:

| # | Grammar feature | Vampire | Mural | Dreamcatchers | BC pentagram |
|---|-----------------|---------|-------|---------------|--------------|
| G1 | Input verb is **observe/inspect/count** (non-destructive) | ✓ (read writings) | ✓ (count features) | ✓ (find/inspect) | ✓ (find tallies) |
| G2 | Markers acquirable **in any order** | ✓ (explicit) | ✓ (one site) | ✓ | ✓ |
| G3 | Distributed markers → a **derived construct** (shape / number) | ✓ pentagram | ✓ primes 2,3,5,7 | ✓ drawn animal | ✓ pentagram |
| G4 | Payoff / next step at **one derived point** | ✓ centre | ✓ at the statues | ✓ the eye | ✓ centre (glow) |
| G5 | Time-gate on the **reveal/encounter**, never an interaction *schedule* | ✓ 12–1 AM | n/a | n/a | ✓ 4–5 AM |
| G6 | Variant elements are **filters to exclude while reading** (decoys), never sequenced | n/a | ✓ upside-down birds | n/a | n/a |
| G7 | **No hidden cross-marker state machine** the player must manage | ✓ | ✓ | ✓ | ✓ |
| G8 | Solvable from information the game gives (plus map work) | ✓ | ✓ | ✓ | ✓ |

*(The Vampire's ending is a fight, but its **puzzle input** is reading; no solved egg's puzzle step is
destructive.)*

## 2. Scoring the web system against the grammar

| # | Web system under **"shoot the feathers"** | Under **"witness/read the display"** ([H27]) |
|---|-------------------------------------------|----------------------------------------------|
| G1 | ✗ destructive input | ✓ observe each web at its hour |
| G2 | ✗ the whole [U29] order-lore | ✓ any order; hours only schedule *visibility* |
| G3 | ✗ shot pattern derives nothing | ✓ positions → the body-centred figure ([S31]); colours → the 5/3 count |
| G4 | ✗ none found in 7 years | ✓ **already delivered**: the centre cluster (1–2 AM) is the derived point, and it *pays out a message* — `N`+pole ([K11]) |
| G5 | ✗ per-feather action windows have no precedent | ✓ per-marker *visibility* gates, same class as the BC pentagram's 4–5 AM |
| G6 | ✗ reds must be sequenced or avoided in an action protocol | ✓ reds are marked variants to **read/filter** while counting — [H18]'s mural lesson transferred with the right verb |
| G7 | ✗ the entire [K21]/[K29]/[U29] apparatus must be *player-managed* | ✓ no state to manage |
| G8 | ✗ 7 years of brute force, no solution | ✓ **executed**: read the engraving-map, witness the webs, go to the centre, follow `N` → the trail that reached Fort Wallace |

**Score: 0/8 vs 8/8.** The scoring is qualitative and the features are mine (construction-bias risk is
real — which is why they were derived from the solved eggs *first*), but the asymmetry is not subtle:
**as a shooting puzzle the web system resembles nothing Rockstar ever shipped; as a read-and-navigate
layer it is a textbook instance of the established grammar**, one relay step in the 2018→2025 chain.

## 3. The known mechanics, re-read without the premise

- **[K30] render-gating becomes the sensor, not a nuisance.** The webs carry bespoke per-web
  *gaze-detection* (won't spawn while watched; won't despawn while watched — and it is web-specific:
  the pentagram behaves oppositely). Under the shooting frame this is mere anti-discovery; under [H27]
  the system's one demonstrated per-web instrument is **look-detection** — the game literally tracks
  whether you *see* each web. Witnessing at the hour is even a non-trivial act (the look-away/look-back
  step).
- **[K21]/[K29]/[U29] become display-repair / anti-cheese, not a lock.** The boundaries' one observed
  function is to **restore the display when the player leaves**. Read as maintenance: shoot the
  signage and the game repairs it as soon as you're not standing there; every "order that works"
  ([U29]) is an epiphenomenon of which rectangles you crossed — which is where the evidence already
  pointed ([H9]: the "chain" *is* the Connector membership; and this session's
  [`web_file_order_concordance.py`](../experiments/web_file_order_concordance.py) adds that **no
  8-order is even feasible** under visible-state rules, 0/40320 — the "solution order," if shooting
  were the input, *cannot exist* as a visible state).
- **The centre's `N` message is the grammar's G4 payoff, already collected.** The web layer's derived
  point yields a *pointer*, exactly what a mid-chain relay should yield; the chain's real payoff (if
  any) lies at its END — past [K16], precisely where the verified trail points and stops. The webs are
  not withholding a secret; they already told us what they had to say.
- **What witnessing all 8 (or the 5 blacks) in their hours implies:** nothing left to "complete" at
  the webs — the tour's outputs are the figure, the counts (5 black / 3 red), and the centre message.
  The [H18] mural grammar finally transfers cleanly: the webs' countable, decoy-filtered feature is
  **colour**, and its reading is the number pair **(5,3)** — which is the one value the letters
  thread's structural exception `EC` keeps producing ([S18]/[S28]: A1Z26 `E,C` = 5,3, beside the Black
  Widow card). Under [H27], [S28] gains a direction: **`EC` is a checksum/confirmation of the webs'
  intended *read-out***, not a key to a shooting order. *(Recorded as an extension leg on [S28], not a
  new ID — the 5,3 coincidence-proneness is already flagged there and doesn't shrink here.)*

## 3b. ⚡ File data, 2026-09-01 ([#89]) — three of [H27]'s legs move from inference to evidence

The CodeX read of the shipped files lands squarely on this hypothesis, and mostly in its favour:

- **"The reset apparatus is display-repair, not a lock" is now a mechanism, not a metaphor.** The three boundaries are
  the `entitiesExtents`/`streamingExtents` of **three ordinary region `.ymap` files** ([K48]); the reset is almost
  certainly the ymap unloading when you leave and **re-streaming from authored data** when you return ([H28]). That is
  literally display repair. Every "order that works" being a **boundary-geometry epiphenomenon** — [H27]'s reading of
  [U29] — is exactly what you would predict, and **[S36]'s hand-authored-zones counterargument is superseded**.
- **"No 8-order is even visible-state feasible" hardens from combinatorics to geometry.** [S38]'s 0/40320 was a desk
  result about shooting sequences; [K49] shows **at most 6 feathers can be down at once and never a set containing
  `B34`** — so no complete visible state exists to *be* the solution. The shooting frame now needs a hidden flag to
  survive at all.
- **The webs carry no per-web data to read as an input.** All 8 feather fragments are byte-identical bar `lodDist`,
  texture dictionary and a reds-only palette that is itself identical across the 3 reds ([K46]/[K47]) — consistent with
  [H27]'s "positions and colours are the message; the objects are just markers."
- ⚠️ **Counter #1 below is untouched and is still the strongest one.** [K29]'s exact-position, live-updated,
  ≥14-night fidelity is **not** explained by plain re-streaming, and [H28] ships a sharper version of the discriminating
  control ([S36]'s successor): does a comparable prop **inside these same 3 ymaps** behave identically?
- ⚠️ **Also unresolved:** [U40] — if each outer web turns out to have its **own** strand archetypes (rather than 4
  reused models), there is a per-web geometry channel nobody has read, and it could carry exactly the kind of data
  [H27] says isn't there.

## 4. Honest counters (stated at full strength)

1. **The state fidelity is expensive for scenery repair.** [K29] stores each fallen feather's exact
   floor position, live-updated, across ≥14 slept nights. That is a lot of engineering for "restore
   the display later." This is the strongest counter — and it is exactly what the [S36] control test
   discriminates: if a generic shot/displaced object persists the same way, the fidelity is engine
   default and the counter collapses; if not, the feathers are being *watched*, which favours
   shooting-as-input.
2. **"Any red after BL56 resets" ([U29]) sounds like a rule, not geometry.** True — though the wording
   is C-tier, garbled, and single-sourced, and BL56's yellow∩red position makes boundary-crossing
   artefacts hard to exclude. Unresolved; noted, not explained away.
3. **u/lopfeh's off-hour featherless spawns after mid-chain sleep ([#67])** hint the system reacts to
   sleep × shot-state — a watched-input tell. C-tier, single report, self-doubted; but it is the kind
   of datum that would grow into a refutation of [H27].
4. **Why feathers at all, if display?** Because the display must be *read*: the feathers carry the
   colour channel (the 5/3 count) and mark which poles are trail members. Display elements need to be
   visible; they don't need to be shootable — but in RDR2 *everything* is shootable, and the boundary
   system explains the tracking either way.
5. **[K30]'s "hide the webs, show the pentagram" asymmetry** was read as a point *for* web
   intentionality under [H22]-R3 — it stays one under [H27]; no tension.

None of these kills the re-read; #1 and #3 are its designated falsifiers.

## 5. [H27], minted — and what it predicts

**[H27] — The webs are a WITNESS/READ layer, not a shooting input.** The feather-shooting premise is a
community import with no sourced basis; the web system scores 8/8 against the solved-egg grammar as a
read-and-navigate relay and 0/8 as a shooting puzzle; the reset apparatus is display-repair whose
"orders" are boundary-geometry epiphenomena; the layer's payoff (the centre `N`) is already collected
and the chain's remaining payoff, if any, lies past [K16].

**Falsifiable predictions:**
- **P1:** Tests A/B/C (and any shooting protocol) return **null** on the web side — no feather-state
  combination triggers anything. Any shooting-triggered payoff **refutes [H27]** outright.
- **P2:** The persistence control finds feather-state fidelity is **generic engine behaviour** (supports);
  feather-specific fidelity weakens [H27] (counter #1). *(2026-09-01: run this as the **[H28]** control — a prop
  **inside** one of the 3 web ymaps vs one outside them — which discriminates more sharply than [S36]'s version, now
  superseded.)*
- **P3:** No future verified clue will instruct feather-state manipulation (desk-checkable as sourcing
  continues).
- **P4 (the cheap test — Test D):** a **witness-only tour** — visit all 8 webs at their hours across
  the needed nights, force each spawn with the look-away trick ([K30]), **fire no shots**, then apply
  the [H25] dream coda (sleep at the whiskey tree into first light). Under [H27]+[H25] this is the
  *complete* candidate solve at strictly lower cost and risk than Test C (no shot discipline, no reset
  hazard). Added to [web-order-field-test.md](web-order-field-test.md) as **Test D**.

**Relations:** rival of [H24] *on the input verb* (H24 keeps shooting, drops the reds; H27 drops
shooting) — Test C vs Test D discriminates, and running D *before* C is free insurance since D leaves
no state to corrupt. Complementary to [H25] (the dream coda is input-agnostic). Strengthens [U3]
toward **one puzzle** (the 2018 chain and 2025 trail become one navigational relay in one grammar).
Reframes [U15]/[U29]: the open question stops being "which order" and becomes "is there an input at
all." Consistent with [U2]'s seven silent years: the community has been pulling a lever that was never
connected.

**🆕 Post-mint evidence (2026-07-02 Reddit sweep — the [#52] full recovery):** the C0d3M3chan1c datamine
independently reports **ZERO references to `spiderdream` (string or any computed joaat hash) across all
1,639 decompiled scripts** — *"no script spawns, detects, tracks, or responds to these webs; their
visibility is 100% engine-driven via timeFlags."* That is exactly the world [H27] describes: at the
script layer **there is no shooting-order handler to satisfy** — the feathers are damageable fragments
whose damage nothing (visible) listens to. ⚠️ Two honest limits: (1) C-tier and unreproduced, with
known numeric errors elsewhere in the post ([#52]'s caveats) — though *this* claim is the post's most
mechanical and checkable; (2) it cannot exclude an **engine-level (C++) listener** invisible to script
datamining — the author says so himself — so it *leans* toward [H27]/[H22]-R3 rather than proving
either. Note the same post ALSO supplies the never-set flags ([U2]) that keep the cut-content reading
alive: zero-script-refs is compatible with **both** "witness layer by design" and "input layer never
wired." Test D discriminates against the former; nothing short of Rockstar discriminates the latter.

---

*Discipline: [H27] registered in [INDEX.md](../INDEX.md) and rolled up in
[findings/speculation.md](../findings/speculation.md); the [S28] extension leg noted there and at
[connections §1a](connections.md). Test D appended to [web-order-field-test.md](web-order-field-test.md).
Nothing here moves the [K16] frontier; a Test D null is a loggable negative like any other.*

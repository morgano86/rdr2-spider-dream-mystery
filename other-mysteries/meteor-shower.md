# The meteor shower (a separate mystery)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**What this file is.** A dossier on the cliff-side **meteor shower** near the Meteor House. It is **not part of the Spider Dream Mystery**; it matters here as a precedent for how RDR2 hides conditional content in the script layer.

## [KNOWN]

*Source: [#92](../sources/sources.md) — script-corpus decode, 2026-09-01; B-tier (decompiled build 1491.50), **not verified in-game**. Readout: [`script-census-2026-09-01-meteor-shower-mechanism.md`](../datamining/script-census-2026-09-01-meteor-shower-mechanism.md). Rollup: [K55](../findings/known-facts.md).*

- **Mechanism.** `discoverable_meteor_shower.ysc` is started by a `WB_DISCO_METEOR_SHOWER` scenario point (not a director script, not a placed entity). Standing in a **5 m cylinder** (`METEOR_SHOWER_CLIFF_SPAWN`) at (2383.7, 2032.6, 171.7) — 97 m from the Meteor House, on the cliff — during **hour 02:00–03:59** starts a looped particle effect (`scr_disc_meteor_shower`) parked in the sky at (2895.9, 1650.2, 1000.9), bearing 127° SE and 52° up, running for 60 s.
- **Constraints.** **Once per save file; no weather condition; no randomness** — the community's "it's a possibility" is just the tiny volume plus the two-hour window.
- **Not in the journal.** Its discovery id is among the 97 of 143 `WB_DISCO_*` types excluded from the `discoverable_found` gate.
- **No second hidden sky spectacle.** A three-way sweep of all 2,194 scripts (literal hour windows → 5 scripts; named trigger volumes → 361 instances / 87 names / 31 scripts; sky-level position literals → the meteor effect is the only ambient, non-mission one) found nothing comparable. The only content script gated on **day of week** is `town_secrets_er_daughter` (Sun/Wed/Fri, Emerald Ranch).
- **Bearing on the mystery.** A precedent that RDR2 hides conditional content in the **script/scenario-point layer, invisible to the `timeFlags` channel** — so [K50]'s "channel closed" holds *for archetypes only*. The same sweep finds **no web or feather script layer** ([#87]) and no second hidden sky event.

## [UNKNOWN]

- None open on the mechanism itself; the readout is script-level and has not been run in-game.

## [SPECULATION]

- None minted.

Related: [`ghost-train-and-ufos.md`](ghost-train-and-ufos.md) (the other timed script events).

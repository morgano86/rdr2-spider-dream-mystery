# Datamining — what the game's files and scripts say

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

Most of the Spider Dream Mystery is read off the screen. This folder holds the other kind of evidence: **readouts from the shipped game files and decompiled scripts**, run with the investigator's own tooling. They answer questions the screen can't — *is there a script behind this? is this prop special, or does the whole game do it? what is actually in that archive?* — and they explain several game mechanics that look mysterious from the outside (bird perches, the ghost train, the UFOs and the unplaced alien cave, the meteor shower, the Witch's Cauldron).

Each file is a **verbatim handoff document** from that tooling, kept so every claim stays checkable. The conclusions drawn from them live in the rollup as `K`/`U` facts (linked below) and in the source ledger ([#89]–[#101] in [`../sources/sources.md`](../sources/sources.md)).

## How to read these

- **Evidence grades.** Direct reads of file contents (archives, `.ymap`, textures) are **A-tier**. Reads of the **decompiled script corpus** (a build-1491.50 dump class) are **B-tier**: they show what the code *can* do, not that it was run in-game. Each file says which applies.
- **Many results are negative.** "No script touches the webs", "no bird is placed at any carving", "no hidden order field" are real findings: they close channels so effort isn't spent there. A negative that passed a positive control is the strongest kind.
- **Tooling caveat.** One decoding bug in the explorer (scenario-point flags) was found and fixed on 2026-09-15; see [K59](../findings/known-facts.md) and the note in [`script-census-2026-09-15-witches-cauldron-brew.md`](script-census-2026-09-15-witches-cauldron-brew.md). No earlier readout in this corpus depended on those flags.
- **Spider relevance.** Unless a row says otherwise, nothing here is a verified spider-trail step. The verified-trail boundary ([`CLAUDE.md`](../CLAUDE.md)) still applies.

## The readouts

### The spider webs, feathers and carvings (direct)

| File | Source | Facts | What it establishes |
|---|---|---|---|
| [`codex-file-readout-2026-07-23-fragments-and-boundaries.md`](codex-file-readout-2026-07-23-fragments-and-boundaries.md) | [#89] | K45–K49 | The 8 feathers are fragments, byte-identical bar three known axes — **no hidden order field**. The "respawn boundaries" are ordinary map-streaming extents, and at most 6 feathers can be down at once. |
| [`codex-file-readout-2026-07-23-timeflags-census.md`](codex-file-readout-2026-07-23-timeflags-census.md) | [#89] | K50–K52 | A game-wide census of every time-gated prop: the time-gating channel is **closed**, the centre web is pinned at 01:00, and the Butcher Creek pentagram is the **same asset family** as the web strands. |
| [`codex-file-readout-2026-09-19-spiderdream-feather-texture-provenance.md`](codex-file-readout-2026-09-19-spiderdream-feather-texture-provenance.md) | [#101] | K64, U43 | The web feather's textures are a mixed triple from three source sets — library scavenging, not a dedicated asset. |
| [`codex-file-readout-2026-09-19-mission-scripts-carving-sites.md`](codex-file-readout-2026-09-19-mission-scripts-carving-sites.md) | [#100] | K63 | No script addresses any carving; coordinate hits near the marks are mission staging. |

### Birds, perches and the carvings

| File | Source | Facts | What it establishes |
|---|---|---|---|
| [`codex-file-readout-2026-09-19-bird-perch-scenarios.md`](codex-file-readout-2026-09-19-bird-perch-scenarios.md) | [#97] | K60 | The scenario-point layer places **no bird or animal at any carving**; the Fort Wallace carved tower is the least bird-populated of its four. |
| [`codex-file-readout-2026-09-19-cutscene-bird-blindspot.md`](codex-file-readout-2026-09-19-cutscene-bird-blindspot.md) | [#98] | K61 | A method correction: the cutscene-scene census can't see script-spawned birds (the blue jay etc.). |
| [`codex-file-readout-2026-09-19-scripted-mission-birds.md`](codex-file-readout-2026-09-19-scripted-mission-birds.md) | [#99] | K62 | Mission and ambient-vignette birds are local to their missions; none near any carving or web. |

### Hidden events and mechanics that look mysterious

| File | Source | Facts | What it establishes |
|---|---|---|---|
| [`script-census-2026-09-01-ghost-train-and-ufo-mechanisms.md`](script-census-2026-09-01-ghost-train-and-ufo-mechanisms.md) | [#91] | K54, U42 | Both UFOs and the ghost train fully decoded; the "half moon" is not a trigger; the unplaced alien-cave interior is cut content. → [dossier](../other-mysteries/ghost-train-and-ufos.md) |
| [`script-census-2026-09-01-meteor-shower-mechanism.md`](script-census-2026-09-01-meteor-shower-mechanism.md) | [#92] | K55 | The meteor shower is a scenario-point-launched script event; no second hidden sky event. → [dossier](../other-mysteries/meteor-shower.md) |
| [`codex-file-readout-2026-09-14-wapiti-smoke-geyser-proxy.md`](codex-file-readout-2026-09-14-wapiti-smoke-geyser-proxy.md) | [#94] | K57 | The Wapiti "smoke" is a geyser-steam emitter on a buried cube — ordinary set dressing. → [dossier](../other-mysteries/wapiti-smoke.md) |
| [`script-census-2026-09-15-witches-cauldron-brew.md`](script-census-2026-09-15-witches-cauldron-brew.md) | [#96] | K59 | The Witch's Cauldron brew does nothing mechanical beyond a ~53 m teleport and a flag. → [dossier](../other-mysteries/witchs-cauldron.md) |
| [`script-census-2026-09-14-wb-disco-old-firepit.md`](script-census-2026-09-14-wb-disco-old-firepit.md) | [#95] | K58 | `WB_DISCO_OLD_FIREPIT` is an ordinary three-site discovery; the discovery system is generic; the Strange Man portrait fork comes from a `mudtown3` choice. |

### Game systems

| File | Source | Facts | What it establishes |
|---|---|---|---|
| [`script-census-2026-09-05-appearance-gated-dialogue.md`](script-census-2026-09-05-appearance-gated-dialogue.md) | [#93] | K56 | Player appearance (masks, weight, hair, dirt, honor) gates nothing by script — only dialogue lines and animscene variants (incl. the Madam Irine fortune teller). |
| [`codex-script-census-2026-07-23-crossover-gun-entitlement.md`](codex-script-census-2026-07-23-crossover-gun-entitlement.md) | [#90] | K53, U41 | RDR2 scripts only *read* awards/unlocks, so online-entitlement gating (e.g. the GTA Online → RDR2 revolver crossover) isn't visible in bytecode. → [crossover dossier](../other-mysteries/gta-rdr2-crossover.md) |

## Where the findings are used

The mechanics above feed the spider analysis in three places: [`analysis/web-order-field-test.md`](../analysis/web-order-field-test.md) (why the in-game feather tests changed), [`analysis/carving-technique.md`](../analysis/carving-technique.md) (what a real carving is), and [`images/webs/WEBS-MANIFEST.md`](../images/webs/WEBS-MANIFEST.md) (what the data says about each web).

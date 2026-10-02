# The Witch's Cauldron brew (a separate mystery)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**What this file is.** A dossier on what drinking the brew at the witch's hut in Grizzlies East actually does. It is **not part of the Spider Dream Mystery** - a closed side lead, with no web or feather content.

## [KNOWN]

*Source: [#96](../sources/sources.md) - script + file decode, 2026-09-15; B/A as noted; a **script-level answer, not run in-game**. Readout: [`witches-cauldron-brew.md`](../datamining/witches-cauldron-brew.md). Rollup: [K59](../findings/known-facts.md).*

- **The brew does nothing mechanical beyond a short teleport and a flag.** `WB_DISCO_WITCHES_CAULDRON` (id `1464664327`, save slot 129, a scenario point at (1182.75, 2035.95, 323.26) in `disco_grze.ymt`, run by `discoverable_generic_location.ysc`): drinking plays a scenario, fades out, **teleports the player ~53 m** to (1227.19, 2007.39, 319.34), lying on the ground for 3 s with the horse placed nearby, fades in, and sets the discovery-complete bit.
- **No stat changes.** No health, stamina, Dead Eye, core, illness, clock, weather, item, money or honor change (call-graph reachability checked).
- **Once per save, with no character check.** One shared single-player save struct covers Arthur and John and the complete bit is never cleared, so "Arthur once and John once" does not match the code - a save that never drank as Arthur can drink as John. It writes no journal entry or toast and reveals the map region `W_4_WITCHES_CAULDRON`.
- **The raven is data, not script.** A `world_animal_crow_on_perch` scenario point in `cumberlandwilderness_east.ymt` at (1183.83, 2038.77, 324.49) carries the **StationaryReactions** flag - the only one of 1,504 crow/raven points game-wide that does - which explains "it looks at you / crows when you loot" with no script.

## [UNKNOWN]

- **Do the "refilled bars" reports come from ordinary sleep?** The untested idea is that the player wakes lying down and the `world_player_sleep_ground` scenario's attached sleeping script offers a Sleep prompt; pressing it restores cores. In-game check: watch for the prompt and compare cores before and after.

## [SPECULATION]

- None minted.

**Method caveat.** The explorer had a scenario-flag decoding bug, found and fixed on 2026-09-15 (see [K59](../findings/known-facts.md)); no earlier readout in this corpus depended on those flags. See the [datamining index](../datamining/README.md).

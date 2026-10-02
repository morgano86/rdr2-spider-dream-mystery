# The ghost train, the two UFOs and the unplaced alien cave (a separate mystery)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**What this file is.** A dossier on RDR2's hidden night-time spectacles - the **ghost train** and the **two UFOs** (Hani's Bethel and Mount Shann) - and the **alien-cave interior** that was built but never placed. It is **not part of the Spider Dream Mystery**; it's here because it was decoded alongside it and shares a vague "~2 AM" feel. The Mount Shann UFO is also covered, with its sundial and sermon, in [`mount-shann-sundial.md`](mount-shann-sundial.md).

> ⚠️ **Boundary.** **No spider-web tie.** The webs' hour gate is the `timeFlags` data channel ([K50]), a different mechanism from the script helpers behind these events, so the shared "~2 AM" stays coincidence-grade ([U34]).

## [KNOWN]

*Source: [#91](../sources/sources.md) - script-corpus decode, 2026-09-01; B-tier (decompiled build 1491.50), not run in-game. Readout: [`ghost-train-and-ufo-mechanisms.md`](../datamining/ghost-train-and-ufo-mechanisms.md). Rollup: [K54](../findings/known-facts.md), refining [K37](../findings/known-facts.md).*

- **Mount Shann UFO** (`town_secrets_strawberry.ysc`, model `s_ufo01x`, 6.41 m - twice the Hani's Bethel craft): needs **hour 01:00–02:59**, the player within **14 m** of the summit (-1982.8, 22.3, 330.8), and a **once-per-in-game-day** cooldown; it descends 143 m to a point beside/above the summit.
- **Hani's Bethel UFO** (`shack_loonycult1.ysc`, `s_ufo02x`): **hour 00:00–03:59** and the player inside the shack volume - nothing else; repeatable nightly.
- **Ghost train** (`discoverable_ghost_train.ysc`): **hour 03:00–04:59**, a 75 m volume, and the previous weather must be clear, overcast, fog or drizzle (**any storm blocks it**). It counts as seen only if it is on screen, hence repeat sightings.
- **The "half moon" is not a trigger.** No moon or lunar native exists in the 2,195-script corpus, so no script can branch on moon phase; the Kuhkowaba sermon's "HALF MOON" is flavour.
- **No third UFO.** Eleven ufo-named archetypes are accounted for; the others are rock-art decals near Shann and tableware.
- **The complete narrowly time-gated script-event set:** meteor shower 02:00–03:59 · ghost train 03:00–04:59 · Hani's UFO 00:00–03:59 · Shann UFO 01:00–02:59 · `town_secrets_er_daughter` 21:00–23:59 on **Sunday/Wednesday/Friday only** (the game's sole day-of-week gate). See [`meteor-shower.md`](meteor-shower.md).

## [UNKNOWN]

- **Why does `dis_roa_aliencave_int` exist unplaced? ([U42](../findings/unknowns.md))** A Roanoke interior, **built and furnished** (own shell/blend/leave props) but **never placed in the world and referenced by no script** - one of only 3 unplaced interiors in the game (the others are multiplayer). Control: 294 of 297 such interiors *are* placed, so "unplaced" is a real result. Almost certainly cut content; no evidence it relates to [U2]. Cheap follow-up: is it placed by a method the census missed (a dynamic or scripted interior load)?

## [SPECULATION]

- None minted. Linking the "~2 AM" window across these events and the spider webs is coincidence-grade only; see [U34] and the [Mount Shann file](mount-shann-sundial.md).

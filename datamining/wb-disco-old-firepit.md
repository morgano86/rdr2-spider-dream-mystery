# RDR2 — `WB_DISCO_OLD_FIREPIT`

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

- **Date:** 2026-09-14
- **Status:** CLOSED — mechanism and all placements decoded. Not a mystery lead.
- **Prompt:** user asked to look into `WB_DISCO_OLD_FIREPIT`.
- **Source:** decompiled script corpus, build 1491.50 (mainly `discoverable_generic_location.ysc.c`) + a first-hand scenario-point and prop data pass over the install.
- **Related:** [`meteor-shower-mechanism.md`](meteor-shower-mechanism.md) (same discovery system).

## What it is

One of the ~143 **discovery scenario-point types**. Internal discovery id **-544327665** → save slot **106** of `Global_40.f_8863[]`. Neighbouring slots are the same family: 104 `OLD_DIRTY_CABIN`, 105 `OLD_FIREPLACE`, 107 `OLD_GRAVESTONES`.

A **three-site** discovery, handled by `discoverable_generic_location.ysc` (same code path as `OLD_FIREPLACE` ×2, `BROKEN_BRIDGE` ×2, `BROKEN_WAGONS` ×11).

## Placements (first-hand, build 1491.50)

Exactly three scenario points of type `wb_disco_old_firepit` exist in the install. Each one is **bit-exact** on the script's hard-coded site coordinate (`func_13`), and each has authored props from `levels_1.rpf\levels\rdr3\area\discoverables\`:

| site | save bit (`f_152`) | position | scenario region | props at the spot |
|---|---|---|---|---|
| 1 | `0x1` | (500.882, 80.003, 139.280) | `disco_hrt.ymt` | `dis_hrt_firepit` + `p_wagonwheel01`, `p_crate14x`, debris boards/pile (`dis_hrt_00`) |
| 2 | `0x2` | (759.079, -1133.282, 55.059) | `disco_roa.ymt` | `dis_roa_oldfirepit` alone (`dis_roa_00`) |
| 3 | `0x4` | (-3667.897, -2805.515, -7.129) | `disco_cho.ymt` | `dis_cho_campfire_mound` + three `p_can05x`/`p_can06x` (`dis_cho_00`) |

Scenario point fields are all default: no time override, probability 0, radius 0, group `0x2172092C` (shared by 213 of 215 discovery points), `uAvailableInMpSp` 1. The ymts are also re-shipped in `update_4.rpf`.

Site 2 sits ~37 m from `clemenspoint.ymt` points, and `dis_roa_oldfirepit` is in the streaming lists `script@cme@exconfed_cme_shot5_srl.ymt` and `script@tripskip@fishing1_shot2_srl.ymt`. Both are cutscene shot lists, so the prop is simply in frame. Site 3 is in Cholla Springs (New Austin).

## Mechanism

1. The scenario point starts `discoverable_generic_location`. `func_3` resolves the type to the id and aborts if the discovery is already done or the global disable `f_8863.f_156` is set.
2. `func_4` picks the **nearest** of the 3 sites as the active index.
3. State 0 waits until the player is **within 40 m** of that site and the site's bit is still clear. `func_154` then creates a 6×6×6 cylinder volume named `DISC_VOL_OLD_FIREPIT_{1,2,3}` on the site.
4. **Walking into the volume** triggers `func_73`, which sets that site's bit in `f_8863.f_152`. `func_74` runs on the first site only: it sets flag `32` and fires `_TELEMETRY_DISCOVERABLE`. When bits `1|2|4` are all set, `func_32(id, 2)` marks the discovery complete. There is no prompt, no interaction and no time or weather gate.

What it does **not** do:

- **No journal entry and no `discoverable_found` stat.** The id is absent from the 46-entry gate (`func_184` here; the identical `func_281` in `main.ysc`, which recounts `discoverable_found` from the save flags). The same check runs in both places, so this is consistent and not a bug.
- **No map-region reveal.** `func_69`/`func_71` are never reached on this branch.
- Nothing else reads the site bits. `f_8863.f_152` only appears in the `discoverable_*` scripts, and those only share helper tables. `campfire_always`/`campfire_gang` show up in the sweep only because they carry a 2,669-entry table of every scenario type name.

Completion needs site 3 in New Austin, so as Arthur the discovery can only be partly collected without out-of-bounds travel.

## Install-wide reference sweep

`firepit sweep` covered 157,739 metadata/script/anim entries, searching by hash and ASCII for the type name (both casings) and the three prop names. Hits:

- the 3 `disco_*.ymt` (plus their `update_4` copies);
- the 16 discovery/campfire scripts already covered above;
- each prop's own `ytyp` and `ymap`;
- the two cutscene streaming lists.

The remaining hits are single matches inside `.ycd` animation clips and terrain `*_trees_*.ymap` files. Those are chance 32-bit collisions, as expected at this scale.

## Correction to the meteor-shower follow-up

That doc says CodeX does not parse the scenario-point type. `RDR2Map` indeed reads only the position, but the loaded `CScenarioPointRegion` bag **already carries it**. `DataBag2.ToXml()` emits `<ScenarioType>wb_disco_old_firepit</ScenarioType>` resolved to its lowercase name. So mapping every `WB_DISCO_*` placement is a field read on data already in hand, not new format work. Count across the 14 `disco_*.ymt`: 215 points, with multi-site types matching the script counts (dreamcatchers 20, broken_wagons 11, hornet_nests 10, old_firepit 3, old_fireplace 2).

## Follow-up: does every discovery report `_TELEMETRY_DISCOVERABLE`? (same day)

**Yes. It's the generic "first found" path, not something specific to the firepit.**

- Each of the 14 working `discoverable_*` scripts has one copy of the same helper (decompiler function hash `0xF9F788B3`): `if (!flag32) { set 32; _TELEMETRY_DISCOVERABLE(id); if (journaled) discoverable_found++ }`. Telemetry comes **before** the 46-type journal gate, so all ~143 types report, journaled or not.
- The helper is effectively the only writer of flag 32. `discoverable_generic.ysc` is a gutted stub (empty `func_8`) and never reports. `mudtown3`/`mudtown3_outro` write bit 31 on `EASEL`, which is a different flag.
- **One exception to check:** `STRANGE_STATUES` (2000209669) sets and *clears* flag 32 directly in a statue-state sync path in `discoverable_generic_location` (L660-700). If that runs first, the helper's `!flag32` guard skips the report. Not traced further.
- It's routine analytics. 835 scripts call `TELEMETRY::*`, and `_TELEMETRY_DISCOVERABLE` is a minor one (14 sites) next to `HONOR` 444, `MISSION_CHECKPOINT` 394, `SHOP_EXIT` 208 and `HERB_PICKED` 110.

### Aside: `mudtown3` → `EASEL` bit 31

`mudtown3` (mission code `MUD3`, marker (-100.19, -25.62, 94.95); the `MUD*` strand is Valentine-area) offers a question-or-kill witness choice (`MUD3_C_QUEST` / `MUD3_C_KILL`). On the kill outcomes it sets bit 31 of `WB_DISCO_EASEL`'s save slot and unlocks `SP_MUD3_KILLED_WITNESS`. `discoverable_easel.ysc` (point at (1710.52, -1001.63, 42.42), `disco_bay.ymt`) reads that bit (`func_56`) to choose between the interior entity sets `stranger_cryptic_dies` and `stranger_cryptic_lives`. It sits alongside `SK2_Painting_set_01..04` and `SK2_Painting_low_moral`/`high_moral`. So the save slot doubles as storage for a cross-mission choice.

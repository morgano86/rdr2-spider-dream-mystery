# RDR2 — the "smoke" near Wapiti at (194.9, 2201.4, 281.4)

- **Date:** 2026-09-14
- **Status:** CLOSED. The emitter is found and fully decoded, including why its plume is thin (see "Why the plume is thin" below; matches the user's in-game footage). Viewer overlay added and awaiting the user's check.
- **Prompt:** a report from about 2019 of smoke rising from an empty hillside near the Wapiti Reservation. Some people thought the puffs looked like symbols. The user found the spot in CodeX and saw no emitter there or under the map. Some had guessed it was a fog or weather emitter.
- **Harness:** `tasks/tools/smoke/` (modes `near`, `fx`, `arch`, `ydr`, `scen`, `xml`, `fxtypes`, `grepa`, `strings`, `list`). Outputs: `near.txt`, `fx.txt`, `proxies.txt`, `list-effects.txt`, and XML dumps in `bin/x64/Debug/net10.0-windows7.0/xml/`.
- **Code:** new "Particle Effects" selection mode in `CodeX.Games.RDR2/RDR2Map.cs` (`UpdateParticleFxOverlay`, `EnsureEntityFxInfos`, `RDR2EntityFxInfo`).

## Answer

The source is **map data, not weather**. A helper model called **`reg_bgv_vfx_proxy`** carries a `CExtensionDefParticleEffect`. Its tag resolves to the effect **`core` / `ent_amb_steam_geyser`**, which is geyser steam.

| | |
|---|---|
| entity position | **(197.3429, 2204.2383, 271.155)**, 3.7 m from the user's point, rotation identity, scale 1 |
| emitter offset | `offsetPosition` **(0, 0, +10)**, so the steam comes out at **(197.34, 2204.24, 281.16)**. The user's Z is 281.44. |
| ground height | **277.98** there (HD terrain `i_10__hd_0_-2_-1`). The emitter is about 3.2 m above ground. |
| proxy model | `reg_bgv_vfx_proxy.ydr`: a 2 m cube (24 verts / 12 tris) spanning Z 271.2–273.2, **so it is buried about 5 m under the ground**. This is why nothing shows at the spot. |
| cube texture | `o_06p_ufo_paintings` (see note below) |
| archetype | `CBaseArchetypeDef`, `MAP_ENTITY_TYPE_BUILDING`, lodDist 100, flags 0. **No timeFlags.** |
| extension | `fxType` 0 (Ambient), probability 100, scale 1, flags 0, boneTag 0, guid `0x7C9E27F2` |
| ymap | `reg_bgv_00_strm_0.ymap` (parent `reg_bgv_00`), `contentFlags` 1, entity lodDist 100, `PRI_REQUIRED`. Three identical copies: base `levels_1.rpf`, `patchpack002`, `row_patchpack002`. Not in `mapstates.txt`, so it is always loaded. |
| asset pack | `levels_1.rpf\levels\rdr3\area\jklm_03_06\reg_bgv_00.rpf` (the Big Valley regional grab-bag pack) |

It has been in the base `levels_1.rpf` since launch, which fits a report from about 7 years ago.

### `vfxentityinfo.ymt` record (tag `0x83A61A25`, ambient table)

`ptFxAssetName core`, `ptFxName ent_amb_steam_geyser`, `ignoreRotation` True, `createAlways` False. Start and end hour are **0/0**, so there is no hour window. The ambient effects that do have one use pairs like 0/24, 20/7, 21/5. Field `0xD76F77B8` = 25, where the common values are 0, 8 and 5.6 (meaning not known). Fields `0x79BA193E` and `0xACAD8E99` are both 0, a combination shared only with the `ent_amb_campfire_smoke_distance*` family.

## Why this spot is unusual

- **It is the only map-placed use of the geyser steam effect in the whole game.** The census (`fx 83A61A25`) found exactly one archetype and one placement (plus the patch copies).
- The **real geysers are scripted**. `discoverable_geyser.ysc` (Cotorra Springs) calls `START_PARTICLE_FX_LOOPED_AT_COORD("ent_amb_steam_geyser", ...)` at three sites: (224.44, 1906.52, 206.08), (191.67, 1831.29, 200.46), (129.11, 1878.37, 200.15). These are **300–370 m south** of the proxy. The script sets evolution `"Steam"` to 0.25 when idle and 1.0 when erupting, with 30/42/57 s cycles. The map proxy sets no evolution.
- **Within 120 m there is nothing** except terrain tiles, the proxy, and one distant LOD (`0x1696725A`, 78 m). No pool, rock or vent model exists. Scenario points nearby are woodpeckers, rams, a fox and Wapiti camp population, with nothing smoke-related.
- It sits at the far NE corner of a region ymap that covers (-2456,-1923)–(297,2304). Its lodDist alone sets the file's NE streaming extent. Its neighbours in that file are `reg_bgv_ufodecal01/02/04` (Mount Shann rock art), `frozenhorse_01..03`, `abdn_home`, bridges and tunnel dressing.
- It is the only archetype game-wide with `vfx_proxy` in its name (`grepa proxy`: 381 proxy-named archetypes, mostly audio/interior proxies).

### The UFO texture on the cube — probably a coincidence, recorded anyway

The buried cube uses `o_06p_ufo_paintings_ab/_nm/_ma`, the same material as `reg_bgv_ufodecal01`, which sits in the same region pack. An invisible proxy box normally gets whatever material is handy in the DCC scene, and the UFO decal is the obvious one in that scene. Other `reg_bgv_*` assets use unrelated materials (`glue_001` uses `nbx_glue`, `frozenhorse` uses `horseRemains`). So this reads as an authoring fingerprint that dates the proxy to the same Big Valley regional pass as the UFO decals. It is **not** evidence of a link. The cube is 5 m underground and can never be seen.

## Hypotheses ruled out

- **Weather or fog emitter: no.** `vfxvolumeplacementinfo.ymt` has 15 volumes. 14 are in Valentine and the nearest is 1,555 m away at (-1347, 2403). `vfxregioninfo.ymt` is keyed by zone *type* (`woodland/snow/mountain/desert/...`) and only emits wind debris, insects and pollen, never positioned steam.
- **Script: no.** No script coordinate near (197, 2204), and no script references `reg_bgv_vfx_proxy`. The only geyser script targets the three Cotorra sites above.
- **Scenario-spawned campfire: no** (scenario scan, 250 m).
- **Time-gated: no.** `CBaseArchetypeDef`, and the effect record has no hour window.

## Open points and caveats

- **Visibility range, not verified in game:** ambient entity effects are created with their entity, which streams in at lodDist 100. So the steam most likely exists only within about 100 m of the proxy, even though a plume is visible from further out.
- **~~The "symbols".~~ RESOLVED (same day).** Textures and evolution behaviour are now decoded from `core.ypt` (sections below). The effect uses only shared library sheets, and at the proxy's unset evolutions it plays just its ambient fog layer: a thin, wind-driven vent fog with no timer or pattern. Odd shapes are random overlapping fog puffs, not authored content.
- Why a lone, **script-less** geyser-steam emitter sits on a hillside above Cotorra Springs, packed with Big Valley content, is not answerable from the data. The plain reading is ambient geothermal dressing, maybe left from an earlier, larger springs layout. The data is consistent with ordinary set dressing and carries no hidden structure.

## Viewer capability added

**Particle Effects** selection mode (`RDR2Map.GetSelectionModes`). While it is active, every `CExtensionDefParticleEffect` on a streamed entity is drawn as a 0.5 m box at the emitter's world position (`entity.Position + entity.Orientation * (offsetPosition * entity.Scale)`). Both archetype- and entity-level extensions are included. Instanced batches are skipped. Each marker is named `<ptFxName> [<asset>] (<Type>[, HH-HHh][, N%]) on <archetype>`.

Colours: cyan = Ambient (plays by itself), green = Anim, orange = triggered (shot/break/destroy/etc.), magenta = tag not found in `vfxentityinfo.ymt`.

Markers follow the streamed entity set, so an emitter appears only when its entity is inside lodDist, the same as in game.

## Follow-up (same day): what `ent_amb_steam_geyser` draws

Harness `tasks/tools/yptfx/` reads a ypt's `ptxFxList` root without a full parser. Modes: `YptFx.exe <asset> <effect...>` (rule graph + textures), `--evo <effect>` (per-event evolved keyframes and base spawn/life), `--behav <dict+38:rule>` (particle rule behaviour keyframes), `--dump <dict+XX:rule|@hex> [depth]` (annotated block dump), `--grep <substr>` (strings across all 385 ypts). `kfp.tsv` beside it is the 73-entry keyframe-property name table extracted from CodeWalker's `Particle.cs`; copy it next to the exe for `--evo`/`--behav`. In RDR2 the ypt holds **rules only**; textures live in `data\effects\ptfx\textures.rpf\<asset>.ytd` (HD copy under `update_4.rpf\x64\hd\...`). Root layout: `+0x10` name string, `+0x28` effect rules (core: 1,285), `+0x30` emitter rules (2,915), `+0x38` particle rules (2,404), each a `pgDictionary` (hashes at +0x20, entries at +0x30). Texture names sit beside a literal `"keyframeTexture"` string, which validates the decode.

`ent_amb_steam_geyser` (core) is an **8-event** effect with evolutions **`Erupt`** and **`Steam`**:

| emitter / particle rule | texture(s) in `core.ytd` |
|---|---|
| `ent_amb_steam_geyser` | `ptfx_train_smoke` (+`_n`, `_mv`) |
| `ent_amb_steam_geyser_fog_vol` | `ptfx_train_smoke` (+`_n`, `_mv`) |
| `ent_amb_geyser_erupt_cloud_vol` | `ptfx_smoke_wispy` |
| `ent_amb_geyser_water_mist` | `ptfx_smoke_wispy` |
| `ent_amb_geyser_spout_jet` | `ptfx_water_splashes_sheet_b` (+`_t`, `_n`) |
| `ent_amb_geyser_water_bubble` | `ptfx_water_splash_rapids` (+`_t`) |
| `ent_amb_geyser_water_splash01/02` | `ptfx_water_splash_t`/`_n`, `ptfx_opaque_white_2x2` |

**No bespoke texture.** Every sheet is a generic library one: `ptfx_train_smoke` is used by 56 particle rules (fires, factory smoke, Annesburg/Saint Denis ambient groups), `ptfx_smoke_wispy` by 169, the splash sheets by 49–176. The map proxy plays the *same effect* as the scripted Cotorra geysers, just without setting the `Erupt`/`Steam` evolutions. What that leaves active is decoded in "Why the plume is thin" below.

### Could the idle/eruption cycle make it a "smoke signal"? No (checked 2026-09-14)

The cycle exists only inside `discoverable_geyser.ysc` (decompiled corpus, `func_*` state machine around line 610). The script starts its *own* looped effect with `START_PARTICLE_FX_LOOPED_AT_COORD` at its three Cotorra coordinates and changes evolutions **on that handle only**: state 2 `Steam` 0.25 → state 3 `Steam` 1.0 → state 5 `Steam` 0.5 + `Erupt` 1.0 (plus a shocking event and a ragdoll knock-back if the player is in the geyser volume) → state 6 back to `Steam` 0.25 / `Erupt` 0. Evolutions are per handle, so none of this can reach the map proxy, whose effect is created by the entity-extension system with no script handle. Nothing sets its evolutions, so it plays continuously at default values with **no idle/eruption rhythm**. No script and no known string mentions `smoke_signal`. A string scan of all 385 ypts for `signal` hits only the asset name of `scr_net_player_signal.ypt` (an Online player-signal effect), so no effect is named for one.

### Why the plume is thin (decoded 2026-09-14, matches the user's in-game footage)

**User observation:** in-game videos show the Cotorra geysers releasing thick steam, while the hillside emitter releases a thin smoke. The data explains it exactly.

**Format notes (RDR2 `core.ypt`, matches GTA V / CodeWalker layouts).** Effect rule `+0x38` = event table (u16 count at `+0x40`; 8 here). Each event (0x90): `+0x10` start/end ratio, `+0x30` evolution list, `+0x40`/`+0x48` emitter/particle rule names, `+0x50`/`+0x58` rule pointers. Evolution list: `+0x00` evolutions (0x18 each, name pointer first), `+0x10` evolved keyframe props (24 bytes: keyframe-list, u32 property-name hash, u32 blend mode). Evolved keyframes (0x30): keyframe list, `+0x20` evolution index. Keyframe values 0x20: time vec4 then value vec4. **Property-name hashes are identical to GTA V's**, e.g. `0x61C50318` = `ptxEmitterRule:m_spawnRateOverTimeKFP`, which is what validates the decode. Base keyframe props in an emitter rule are inline (name hash, then list pointer at +8). The GTA V back-pointer from a base prop to its evolved prop is **not** stored on disk in RDR2 (zero hits). Particle rule behaviours are a pointer array at `+0x198`; each behaviour's own keyframe props start at `+0x38`. Scanning a fixed window past that bleeds into neighbouring rules' behaviours, so only the leading entries belong to the element.

**What each evolution does** (min/max ranges; assumes the usual linear base-to-evolved blend):

| event | spawn rate, no evolutions (the proxy) | driven by the script |
|---|---|---|
| 0 `ent_amb_steam_geyser_fog_vol` | **1.27–1.54 /s** (not evolved) | `Erupt` raises life 3.5–4.2 → 4.7–4.9 s, size to ~5.3 m, fog density peak 0.35 → 0.5 |
| 1 `ent_amb_geyser_erupt_cloud_vol` | **0** | `Erupt`: 5 /s |
| 2 `ent_amb_steam_geyser` (the steam column) | **0** | `Steam`: 15.0–17.7 /s at 1.0; `Erupt` adds speed, +9.9 m target height, shorter life |
| 3 `ent_amb_geyser_water_bubble` | **0** | `Erupt`: 8.9 → 26.4 /s |
| 4 `ent_amb_geyser_spout_jet` | **0** | `Erupt`: 9.8–14.8 /s |
| 5 `ent_amb_geyser_water_splash01` | **0** | `Erupt`: 221–229 /s |
| 6 `ent_amb_geyser_water_splash02` | **0** | `Erupt`: 356–366 /s |
| 7 `ent_amb_geyser_water_mist` | **0** | `Erupt`: 6.1–8.1 /s |

Fog-layer base behaviours (`--behav dict+38:ent_amb_steam_geyser_fog_vol`): `ptxu_FogVolume` density 0 → 0.35 (t 0.13–0.87) → 0; size 1.07→3.17 m min / 2.62→5.21 m max over life; wind influence 0.25; colour white; texture animation 24.7 fps; initial rotation ±35°.

**So:** the proxy plays only event 0, about 1.4 soft fog puffs per second, 1–5 m across, living ~4 s, density 0.35, pushed by wind. A scripted geyser at idle (`Steam` 0.25) adds ~4 steam-column particles/s on top, ~15–18/s at `Steam` 1.0, and the whole jet/splash/cloud set when erupting. The hillside is **the geyser effect placed as map data without the script that powers it**, which leaves only its vent fog. Whether that was intended (a quiet fumarole) or a geyser that was meant to be scripted cannot be told from the data.

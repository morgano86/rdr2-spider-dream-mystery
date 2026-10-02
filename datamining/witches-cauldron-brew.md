# Witch's Cauldron brew (`dis_grz_witch_brew`) - what drinking it actually does

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

- **Date:** 2026-09-15
- **Status:** done (script-level answer); two in-game checks suggested, not run
- **Question (user):** at `dis_grz_witch_lair` the player can drink from the cauldron and passes out. Community claims: eases Arthur's illness, refills cores/bars, drinkable once by Arthur and once by John. What does it do?
- **Outcome:** it is the `WB_DISCO_WITCHES_CAULDRON` world discovery. Drinking plays a scenario, fades out, moves you **~53 m** down the hill, lays you on the ground for 3 s with your horse waiting, fades in, and sets the discovery complete. **No health, stamina, Dead Eye, core, illness, clock, weather, item, money or honor change.** It works once per **save**, with no check for which character is playing. The flag is never cleared.
- **Sources:** decompiled script corpus, build 1491.50 (`discoverable_generic_location.ysc.c`, plus `sleeping_scenario.ysc.c`, `startup.ysc.c`), with a first-hand metadata sweep and scenario-region dump of the install.

## Identity

| thing | value |
|---|---|
| scenario point | `wb_disco_witches_cauldron` in `disco_grze.ymt`, (1182.75, 2035.95, 323.26), `uAvailableInMpSp` 1 |
| script | `discoverable_generic_location.ysc` (launched by the point) |
| internal id | `1464664327`; save slot `Global_40.f_8863[129]` = `discoverableData.eFlags[129]` (`startup.ysc` save registration) |
| map region revealed | `387869270` = map label `W_4_WITCHES_CAULDRON` (`map_app_event_handler`) |
| trigger volume | `DISC_VOL_WITCHES_CAULDRON`, centre (1183.87, 2035.43, 324.33), rot z -45.76, size 7.55 × 4.03 × 5.62 |
| drink scenario | `world_player_drink_witches_brew` (anim `mega_gen@amb_player@drink_witches_brew_arthur`), created by script at (1182.68, 2036.35, 322.98) heading 80.2 |
| wake scenario | `world_player_sleep_ground` at **(1227.19, 2007.39, 319.34)** heading 103.55 |
| horse placed at | (1217.05, 2002.68, 319.20) heading 349.2 |

## The sequence (`func_8` case 10 → `func_70` → `func_71`)

1. Entering the volume without flag 8 → `_MAP_DISCOVER_REGION(W_4_WITCHES_CAULDRON)`, set flag 8 (`func_69`).
2. `func_64` creates the drink scenario point, **only if flag 2 (complete) is clear** (`func_8` case 0 exits to state 13 when it is set).
3. `func_70` state machine, once the player is active in that point:
   - `LOAD_SCENE_START_SPHERE` at the wake spot, then `DO_SCREEN_FADE_OUT(4000)` between 3.5 and 7.5 s in;
   - `func_179` → `func_262` (the shared horse-summon library) puts **your horse** at the horse spot with `TASK_STAND_STILL`;
   - `_SET_ENTITY_COORDS_AND_HEADING` the player to the wake spot;
   - `TASK_START_SCENARIO_IN_PLACE_HASH(player, world_player_sleep_ground, 3000 ms)`;
   - `DO_SCREEN_FADE_IN(4000)`.
4. `func_71` → `func_182`: set flag **2** (complete), then `func_74`: set flag 32 (first found) and `_TELEMETRY_DISCOVERABLE`. The cauldron is **not** in `func_184`'s journal list, so no `discoverable_found` stat, journal entry or toast.

## The negative, and how it was checked

- Call graph over the decompile (`scratchpad cg.py`, reproduced below): forward reachability from every cauldron function (`func_64/66/69/70/71/179`) finds no `ATTRIBUTE::` core setters, no `CLOCK::`, no weather and no inventory grant. The only `SET_ENTITY_HEALTH` and `SET_ATTRIBUTE_POINTS(…, 7)` it reaches are in `func_326`/`func_408`, which act on **horse slot** indices (0–6 via `func_322`), i.e. the horse library resolving your horse.
- The script *can* restore cores - `func_192(100f)` sets health/stamina/Dead Eye to at least 100. The only caller is `func_75` case 9, the **Strange Statues** puzzle (`2000209669`). A good contrast: the author wired a reward there and nowhere on the cauldron path.
- **Once per save:** the only code that clears a discoverable flag in the whole corpus is `func_51` in this script, and every call site clears bits 16/32 for other discoveries. Bit 2 is never cleared. `Global_40` is the single SP save struct Arthur and John share, and the cauldron path checks no character. So "Arthur once and John once" does not match the code. A save that never drank as Arthur can drink as John, which probably explains the reports.
- First-hand sweep of 157,739 metadata/script entries for the brew/cauldron names: the only real referrers are the lair ymap/ytyp, `disco_grze.ymt`, the `discoverable_*` scripts, `map_app_event_handler`, and the anim `.ycd`. Hits in `campfire_always`/`campfire_gang`/`net_gun_for_hire_offline` are entries in a generic ~1,200-entry index→scenario-type-hash `switch` (`37 <u32> 50 02 01` = PUSH_CONST_U32 + LEAVE, byte-checked with `witchbrew hex`), not behaviour. Everything else is a chance hit inside anim/navmesh data.

## Why people report refilled bars (hypothesis - untested)

`world_player_sleep_ground` is the scenario the engine attaches `sleeping_scenario.ysc` to. No script launches that script, so the scenario data does. That script is the normal sleep system: time skip (`ADVANCE_CLOCK_TIME_TO`), full health (`SET_ENTITY_HEALTH` to max), core refills and overpower. But all of it sits behind the player **pressing the "Sleep" prompt** (states 6→7→…→10). If that prompt shows while you lie at the wake spot, and some players take it, that is an ordinary sleep and explains "it refilled my bars". Unknown whether an in-place scenario (no persistent point) gets the attached script. **In-game check:** after waking, watch for a Sleep prompt, and note the cores before drinking and after waking without touching anything.

## The raven

No prop or script puts a raven at the lair. It comes from a scenario point in the generic wilderness file `cumberlandwilderness_east.ymt`: `world_animal_crow_on_perch` (`0x714DCFE3`, name cracked by token combination) at **(1183.83, 2038.77, 324.49)**, 3.3 m from the cauldron and ~1.2 m up, `ModelSet animals_ravens`.

**Follow-up (same day): the first reading of its flags was wrong, because CodeX mis-decoded scenario flags (since fixed; see `rdr2-resources.md`, "Flags fields").** `CScenarioPointFlags__Flags` has **64** values, but `DataBag2.FormatEnumValue` reads the field as a u32 and tests `1 << t` on an `int`. C# masks the shift count to 5 bits, so value 55 prints whenever bit 23 is set and 57 whenever bit 25 is set (counts match exactly: 65,209 / 38,850). The "unknown flags `0xDEE6B943` / `0xFBEEC8B2`" were those ghosts, and the upper word at point `+44` was never read. Raw decode (`witchbrew census` now writes `lo`/`hi`), validated by flag-type fit: `SeatedNoBack` on `world_human_seat_steps`, `UseVehicleFrontForArrival` on `drive`, `InWater` on vehicle and `stand`-in-water points, `CampfireScenario` on `world_human_drinking`.

The perch's true flags are `lo 0x02800000` / `hi 0x00000008` = **NoAttraction + NoSpawn + StationaryReactions** (bit 35).

- `NoSpawn` is **not** special. 38,850 of 131,853 points carry it, including 1,384 ungrouped wilderness animal points (cougars in Gap Tooth, bears, wolves, moose, buffalo), whose animals plainly appear. The earlier "only 3 of 1,117 in the file" contrast is withdrawn.
- **`StationaryReactions` is what makes it unique.** Of **1,504** crow/raven points game-wide (scenario type or model set), it is the **only** one with the flag. Of **70** `animals_ravens` points, it is the only `StationaryReactions` point and the only `NoSpawn` one. Game-wide, 56 animal points carry the flag: Clemens Point roosters, Saint Denis cats, Pronghorn Ranch cows, this raven, and one elk at (-90.98, 1325.79, 174.52) (hours 5–19, probability 9), the only other wilderness animal with the identical mask.
- That flag matches the in-game reports (fandom: the raven "will look at the player all the time", "taking any item from the shack will result in the raven crowing"; forum: "the raven in the corner", killable). A normal perched crow flees on a disturbance. This one reacts **in place**, with the scenario's own `amb_creatures_bird@world_crow_on_perch@react_look@enter/loop/exit` clips. Looting is a disturbance event, so the caw is the generic reaction, not a script. The effect is authored through data (a raven-only model set plus the stationary-reaction flag on one hand-placed perch in the hut corner), not code.
- **No script is involved.** Corpus-wide there are zero references to `animals_ravens`, to the perch coordinates, or to `world_animal_crow_on_perch` outside two unrelated vignettes (`av_bird_fence_swarm`, `av_fox_sit`) that create birds at their own positions. The `a_c_raven_01` hits in `short_update`/`player_camp`/`interactive_campfire`/`av_bird_flee_swarm` are generic bird-model lists. `discoverable_generic_location` spawns nothing for the cauldron except the drink point.
- **Still not established:** which engine population path fills a `NoSpawn` animal point (same unknown for the 1,384 wilderness ones), whether the raven respawns after being killed, and whether it keeps a schedule. The point has no time override (`0`/`0`), no group, no required imap and no chaining graph (the region's graph is empty). Cheap in-game checks: kill it, ride well out of streaming range, return; visit at night; watch whether it ever flies off when shot at rather than looted near.

Other points at the lair: `ransack_reach_over_volume_narrow_0m5_0m5_2m0`, `ransack_reach_over_volume_0m8_0m5_2m0`, `ransack_reach_over_centered_ground_pickup` (lootable spots), one unresolved `0xD82FFF50` ×2, and an MP-only collector loot point.

## Reproduce

```
grep -rn 1464664327 script_rel      # every table/branch for the cauldron, over the decompiled corpus
```

The install-side half (scenario-region dump, prop list, hex reads) used the investigator's local tooling, which is not published here; the coordinates and flags in this note are the checkable output. A call-graph helper (caller chains upward, reachable lines downward) was used for the script trace.

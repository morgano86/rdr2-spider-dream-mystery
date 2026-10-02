# RDR2 - the meteor shower mechanism (and a sweep for comparable hidden events)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

- **Date:** 2026-09-01
- **Status:** CLOSED - mechanism fully decoded.
- **Prompt:** user found the community report that standing near the Meteor House around 2 AM and looking up can show a meteor shower visible nowhere else, and asked what drives it - given the 2026-07-25 script cross-check found no timer-based meteor event and no `CTimeArchetypeDef` covers it.
- **Source:** build-matched decompiled corpus (2,194 scripts, build 1491.50).

## Why the earlier passes missed it

Both prior sweeps were looking in the wrong layer, correctly:

- It is **not** `CTimeArchetypeDef`/`timeFlags` - no archetype is involved at all; the effect is a **particle system**, not a placed entity, so nothing in the ymap/ytyp layer could ever have shown it.
- It is **not** a director-launched spawn record (`short_update`/`medium_update`/`long_update`), which is what `2026-07-26-weather-gated-content.md` enumerated. It is launched by a **scenario point**.

## The mechanism

`discoverable_meteor_shower.ysc` is started by the RAGE **scenario-point** system, not by a director script. `main()` requires `TASK::DOES_SCENARIO_POINT_EXIST(scriptParam.f_1)` and resolves `TASK::_GET_SCENARIO_POINT_TYPE(...)` → `WB_DISCO_METEOR_SHOWER` → internal discovery id **-777150535** (slot in the 143-entry save-game discovery flag array `Global_40.f_8863[]`).

The event itself is `func_8`, a 6-state machine, entirely self-contained:

| state | condition / action |
|---|---|
| 0 | **Abort if already seen** - bit 2 of the save flag for id -777150535. Otherwise create the trigger volume. |
| 1 | `IS_ENTITY_IN_VOLUME(player, METEOR_SHOWER_CLIFF_SPAWN)` **and** hour in `[2, 4)` |
| 2 | `REQUEST_PTFX_ASSET` / wait for load |
| 3 | `START_PARTICLE_FX_LOOPED_AT_COORD("scr_disc_meteor_shower", (2895.893, 1650.213, 1000.863), scale 1.0)` |
| 4 | after **60 s** of game timer: stop FX, set the "seen" bit, telemetry, map-region discover |
| 5 | terminal |

### Exact conditions

- **Trigger volume:** `METEOR_SHOWER_CLIFF_SPAWN`, `volCylinder`, centre **(2383.667, 2032.578, 171.667)**, extents (5, 5, 5) - i.e. a ~5 m radius cylinder. This is **97.2 m** from `WB_DISCO_METEOR_HOUSE` at (2474.894, 1999.316, 168.258), on the cliff, matching the volume's name.
- **Time:** hour >= 2 and hour < 4. So **02:00-03:59**, checked with the shared wrap-around hour helper.
- **Once per save file.** The check in state 0 and the set in state 4 are the same save-game bit.
- **No weather condition. No RNG.** Verified by scanning `func_8` for weather natives and `MISC::GET_RANDOM_*` - neither appears. The community's "there is a possibility" is the 5 m volume plus the 2-hour window, not a random roll.
- The time/volume test happens **only in state 1**. Once started, the 60 s plays out even if the player leaves the volume or the clock passes 04:00. Conversely, leaving before the 60 s elapses means the flag is never set, so it can be retried.

### Viewing geometry

FX origin is **639 m horizontally, 829 m up** from the trigger: bearing **127 deg (SE)**, **52 deg above the horizon**. That is why it is only visible from this spot - it is one particle emitter parked in the sky to the south-east, not a skybox or weather effect.

### Why it is not in the journal

`func_181` is the "counts as a `discoverable_found`" gate: **46** of the **143** `WB_DISCO_*` types are in it. **-777150535 is not.** So the shower sets its discovery bit, fires `_TELEMETRY_DISCOVERABLE` and may reveal a map region, but never produces a journal entry - exactly as the user observed. 97 of 143 discovery types are non-journaled this way (full list in the analysis output).

## Sweep for comparable hidden events

Three independent sweeps over all 2,194 scripts:

1. **Literal hour windows** through the shared wrap-around hour helper - **5 scripts only** (663 files call it with the boilerplate `(9,11)`/`(9,12)` shop-hours pair; those are noise):

   | script | window | note |
   |---|---|---|
   | `discoverable_meteor_shower` | 02:00-03:59 | this event |
   | `discoverable_ghost_train` | 03:00-04:59 | known - Ghost Train, volume at (688.256, -563.752, 76.051), r=75 m |
   | `town_secrets_er_daughter` | 21:00-23:59 | see below |
   | `short_update` | 23:00-03:59 | tuning only - scales ambient spawn distance x0.75 at night |
   | `native1` | 05:00-19:59 | generic system, not content |

2. **Named script trigger volumes** - **361 instances / 87 distinct names across 31 scripts**, i.e. the complete set of "stand in this exact spot" script triggers in the game. Dominated by theatre-show audience volumes (15 each), `discoverable_geyser` (36), `rcm_exconfed11` (35) and fishing missions. The one-off spectacle volumes are only: meteor shower, ghost train, `LIGHTNING_TREE_CENTER` (2535.516, 1192.138, 165.531), and the three `town_secrets_*`.

3. **Sky-level position literals** (world XY, Z > 400 m) - 49 distinct points, all of which are either real Ambarino terrain, mission cameras or placeholders except one. **`discoverable_meteor_shower`'s (2895.893, 1650.213, 1000.863) is the only ambient, non-mission, sky-level VFX position in the corpus.** There is no second hidden sky spectacle.

### The one genuinely comparable find: `town_secrets_er_daughter`

Gated on the **day of the week** - and it is the **only content script in the entire corpus that is**. Every other one of the 45 `GET_CLOCK_DAY_OF_WEEK` callers is a shop's opening hours (or `short_update`/ `medium_update`).

- Days: `clockDayOfWeek` in {0, 3, 5} - Sunday, Wednesday, Friday.
- Hours: 09:00-11:59 **or** 21:00-23:59.
- Volume `TS_ERD_SPAWN_TRIGGER`, `volBox` at **(1443.915, 319.475, 88.464)**, extents (20.4, 27.0, 4.7) - Emerald Ranch.
- Spawns ped `u_f_m_emrdaughter_01` running scenario `world_human_sleep_ground_arm` (sleeping on the ground), which looks at the player while present.

Siblings `town_secrets_val_moira` (-278.720, 812.540, 122.882) and `town_secrets_sd_trelawny` (2731.981, -1182.070, 53.101) use volumes but no day gate; `town_secrets_strawberry` uses neither.

## Confidence

Conditions are read off the decompiled control flow, not inferred: the hour helper's body is the literal wrap-around comparison, the volume record is a literal struct, and the once-per-save bit is the same `Global_40.f_8863[func_63(id, 1)]` slot in both the read and the write. The corpus is 2,194 of the install's 2,195 scripts (`cv_cc_mll_03`, camp dialogue, absent and irrelevant). Not verified in-game.

## Follow-ups (none blocking)

- The investigator's map viewer did not parse the scenario-point **type** field when this was written, only `vPositionAndDirection`. Parsing the type hash would let it map every `WB_DISCO_*` placement in the world.
- In-game check of the meteor shower against the decoded conditions.

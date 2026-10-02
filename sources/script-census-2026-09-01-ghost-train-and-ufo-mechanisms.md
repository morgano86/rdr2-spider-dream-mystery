# RDR2 — ghost train trigger, and both UFO events (moon-phase question settled)

- **Date:** 2026-09-01
- **Status:** CLOSED — both UFOs and the ghost train fully decoded.
- **Follows:** `2026-09-01-meteor-shower-mechanism.md`
- **Sources:** decompiled corpus `tasks/tools/ysc-corpus-scan/corpus/1491.50` (2,194 scripts, build 1491.50); harness `tasks/tools/ufoscan/` (archetype/ymap/MLO walk + format-blind hash sweep incl. `.ysc`), output `tasks/tools/ufoscan/results.txt`; sweeps `tasks/tools/meteor/{tod,near,volumes}.py`.

## 1. Ghost train — exact trigger

`discoverable_ghost_train.ysc`, launched from a `WB_DISCO_GHOST_TRAIN` scenario point (id **397377585**). All must hold simultaneously:

| # | condition | detail |
|---|---|---|
| 1 | not already seen | bit 2 of the save discovery flag for id 397377585 |
| 2 | content unlock | `func_16(43)` — unlock slot 43 unlocked-and-not-visible |
| 3 | not content-blocked | world-block check index 70 |
| 4 | **hour 03:00-04:59** | window `[3, 5)`, same wrap-around helper as the meteor shower |
| 5 | **weather** | the **previous** weather type must be `DRIZZLE`, `OVERCAST`, `Fog`, `highpressure`, `overcastdark`, `clouds`, `Misty` or `SUNNY`. Any rain, snow, thunder, storm, sleet, hail or sandstorm **blocks it**. |
| 6 | not riding a train | `IS_PLAYER_RIDING_TRAIN` |
| 7 | **player inside the volume** | `GHOST_TRAIN_SPAWN`, `volCylinder`, centre **(688.256, -563.752, 76.051)**, extents (75, 75, 25) — **75 m radius** |

Spawns mission train config `241358608` at **(841.392, -626.930, 73.624)** (165.7 m from the volume centre): four carriages (`ghosttrainsteamer`, `ghosttraincoalcar`, `ghosttrainpassenger`, `ghosttraincaboose`), collision **off**, alpha **0** fading up over a 200-unit ramp, cruise speed **12**, whistle `"PASSING"`, and a forced player head-turn via `_INVERSE_KINEMATICS_REQUEST_LOOK_AT`. Despawns on reaching **(647.231, -514.883, 76.073)**.

### Why it seems unpredictable, and why people see it twice

The 75 m volume is generous; the undocumented condition is the **weather clause**, and 03:00-05:00 is exactly when the game likes to produce blocking storms.

**The "seen" bit is only set inside `IS_ENTITY_ON_SCREEN(train)`.** The train spawns and runs its whole route whether or not you are looking. Only if it is actually on screen does it mark itself discovered — so missing it (wrong way, screen faded, ridden out of range) leaves the flag unset and it can happen again. Repeat sightings are that check, not randomness.

## 2. UFO #1 — Hani's Bethel (Loony Cult Shack)

`shack_loonycult1.ysc`. Model **`s_ufo02x`** (`0xB72F3DA7`, 3.20 x 3.20 x 1.53 m) via `CREATE_OBJECT`. (The model comes from the script's static local block — `iLocal_73.f_121` is local index 194, and `uLocal_194 = -1221640793` = `joaat("s_ufo02x")`.)

- **Gate (`func_53` case 0):** `hour >= 0 && hour <= 3` **and** player inside the shack trigger volume. **That is the entire condition set** — no weather, no date, no RNG.
- Descends to **z = 115** above **(1462, 811)**, then wanders randomly in x 1458.9-1465.6, y 807.1-814.2.
- Audio soundset `Ufos_Sounds` ("Arrive"/"Loop_A"/"Loop_B"/"Leave"), ambient zone `AZ_Looney_Cult_Shack_UFOs`.
- Rises to z = 999 and leaves as soon as the hour leaves 0-3 **or** the player leaves the volume.
- State bits live in `iLocal_73.f_130` — **script-local**, reset on restart. **Repeatable every night.**

## 3. UFO #2 — Mount Shann

`town_secrets_strawberry.ysc`. Model **`s_ufo01x`** (`0xC92962E3`, **6.41 x 6.41 x 3.06 m** — twice the size of the Hani's Bethel craft), `hLocal_20 = joaat("s_ufo01x")` at `main()` line 60.

The object is created **frozen and invisible** at **(-1947.076, -128.290, 500.0)** as soon as the script starts. The reveal gate (`func_9` case 0) is three conditions:

| condition | detail |
|---|---|
| **calendar cooldown** | `func_21()` — compares the saved timestamp `Global_40.f_9020.f_7` (a **save-game** field, set when it triggers) against the current clock. Passes if never seen, or if **at least one in-game day/month/year** has elapsed. Effectively **once per in-game day**. |
| **hour 01:00-02:59** | `func_22(2048)` — bitmask time-window helper, bit 2048 = `hour >= 1 && hour < 3` |
| **proximity** | player within **14 m** of **(-1982.800, 22.300, 330.845)** — the Mount Shann summit |

On trigger it becomes visible and **descends 143 m** to **(-1947.076, -128.290, 356.960)** while spinning: heading increment starts at **15 deg/tick** and decays to 0.4. The landing point is **154.8 m horizontally** from the summit and ends **26.1 m above** it — i.e. it drops out of the sky beside and above you.

## 4. The half moon is NOT a trigger — settled

Four independent lines:

1. **No moon/lunar native exists in the 2,195-script corpus.** Every `MOON` string is *moonshine* (`TOXIC_MOONSHINE_EFFECT`, `AMMO_MOONSHINEJUG_MP`, `MOONSHINE_CAMP`, ...). No script can branch on the moon.
2. Both UFOs are **script-spawned** (`CREATE_OBJECT`), so their appearance is decided solely by those scripts' conditions.
3. The clock global `Global_1899515` is a packed date-time — bits 0-5 seconds, 6-11 minutes, **12-16 hours**, 17-21 day, 22-25 month, 26-30 year (`+1898`). **Hani's Bethel reads only the hours field.**
4. **Mount Shann does read the full date** — but only through `func_38`, a plain Julian-style day-serial conversion, and only to difference two timestamps for the once-per-day cooldown (`func_39` -> `func_56`, a timestamp-delta decomposition). There is no phase arithmetic anywhere in it.

The moon phase is rendered by the engine from the in-game date; nothing in the content layer consumes it. "2 AM under a half moon" is the 00:00-03:59 window plus confirmation bias.

## 5. Is there a third UFO?

No. Every ufo/alien/saucer-named archetype game-wide (11 of them), against 123,438 archetypes, 8,023 ymaps / 237,219 placements, a 42,710-entity MLO interior walk, and a format-blind hash sweep over **113,867** metadata + `.ysc` entries:

| asset | role |
|---|---|
| `s_ufo02x` | Hani's Bethel craft (script-spawned) |
| `s_ufo01x` | Mount Shann craft (script-spawned) |
| `dis_bgv_00_ufo_03` | **rock art** — a texture shown on a rock near Mount Shann (user-identified). Placed once at (-1700.287, -166.610, 187.082) in the Big Valley *discoverables* ymap, `CBaseArchetypeDef`, timeFlags 0. |
| `reg_bgv_ufodecal01 / 02 / 04` | same idiom, placed once each at (-2356.115, -228.954, 179.703), (-1589.016, -277.170, 155.997), (-1772.861, -151.429, 207.847) |
| `p_saucer01x` | **tableware** — cabins, Strawberry mayor's house. Not a UFO. |
| `dis_roa_aliencave_*` | see below |

Both craft are accounted for, and no third craft model or spawn site exists.

**Loose end worth keeping: `dis_roa_aliencave_int`.** A Roanoke MLO interior, **built and furnished** (three of its own props — `_int_shell`, `_blend`, `_leave_dc` — positioned inside it) but **never placed in the world**. It is one of only **3 unplaced MLO interiors in the entire game** (the others are `mp001_mp_moonshine_int` and `mp001_sis_bldg02_int`, both MP). **Control:** the ymap walk finds 294 of 297 MLO archetypes placed, so "unplaced" is a real result rather than a gap in the walk. No script references it either.

## 6. Complete set of narrowly time-gated script events

RDR2 has (at least) **three** hour-gating idioms; only sweeping all three gives a complete answer:

1. **Direct** calls to the shared wrap-around hour helper with literal args.
2. **Wrapped** — a per-script `f(a,b) => helper(GET_CLOCK_HOURS(), a, b)` shim (`shack_loonycult1`).
3. **Bitmask time-window helper** — 17 named windows; 39 scripts use it.

Across all three, the complete set of *narrowly* time-gated events (everything else is broad day/night bands for ambushes, hideouts, campfires and ambient scenarios):

| script | window | extra conditions |
|---|---|---|
| `discoverable_meteor_shower` | 02:00-03:59 | 5 m volume; once per save |
| `discoverable_ghost_train` | 03:00-04:59 | 75 m volume; weather; on-screen to count |
| `shack_loonycult1` (UFO 1) | 00:00-03:59 | in shack volume; repeatable nightly |
| `town_secrets_strawberry` (UFO 2) | 01:00-02:59 | within 14 m of the summit; once per in-game day |
| `town_secrets_er_daughter` | 21:00-23:59 | **Sun/Wed/Fri only** — the only day-of-week-gated content in the game |

**`town_secrets_strawberry` is the only script in the game that uses the narrow 2048 (01-03) bit.**

## Method notes

- **A truncated grep cost a wrong conclusion.** An early `grep -rn -i -E "ufo|..." | head -20` cut off before `town_secrets_strawberry.ysc.c`, which contains a plainly-resolved `joaat("s_ufo01x")` on line 60. That led to a wrong "s_ufo01x is unused" claim, corrected only when the format-blind sweep was widened to include `.ysc` entries in the install. **Never `head` a corpus-wide grep whose absence you intend to treat as evidence** — count first, then page.
- Sweeping `.ysc` *in the install* alongside the decompiled corpus is a genuine independent check: it caught the miss above without depending on the decompiler.
- When sweeping for a gate, follow the helper's callers **transitively** and look for alternative encodings — three separate hour idioms exist here, and the first sweep found only one of them.
- The MLO-placement control (294/297) is what makes the alien-cave result usable.

# 2026-09-19: Bird perch scenario points near the carvings: findings

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**Date:** 2026-09-19 · **Outcome:** negative **One line:** No bird or animal is placed to appear at any carving - and the tower carrying the two carved birds is the only one of Fort Wallace's four towers with **zero** bird-perch points near it.

## Answer

The scenario-point layer places no bird, and no animal, at or on any of the ten known carvings. The theory the task was built on - that a real bird lands beside the carved birds at some hour - is **refuted**, and refuted in the direction opposite to the theory:

- **Fort Wallace (the two carved birds, `old_fort_twr3`, world (323.51, 1512.06, 194.70)).** **0** bird-perch points within 25 m. The nearest is **28 m** away and **10 m below** the carved roof tile, on the walkway/wall line at z 182–185. Every one of the 21 perch points within 120 m of the fort sits at z 180.7–184.8; **nothing is placed at roof height at all.** Against the obvious control - the fort's other three towers - `old_fort_twr3` is the only one with none inside 25 m: `old_fort_twr1` has 7, `old_fort_twr2` 8, `old_fort_twr4` 6. The carved tower is the *least* bird-populated of the four.
- **Butcher Creek (six marks on five outhouses).** Nearest perch **13.1–60.9 m**, against a median of **39.7 m** (p10 5.1, min 1.6) over 39 uncarved site-specific outhouses. Four of the six marks have **0** perch points within 50 m. Typical to worse than baseline.
- **Fort Brennand (three marks on `civ_01_outhouse` and `civ_twr_03b`).** Nearest perch **3.2–4.5 m**, 31–44 points within 25 m - which looks like a hit until the control is read: the three *uncarved* Brennand towers score **2.4–2.9 m** with 29–36 points inside 25 m (`civ_twr_01a` 2.4/32, `civ_twr_03a` 2.7/30, `civ_twr_04a` 2.7/36). The whole fort is blanketed in `animals_sparrow_rigs` `world_animal_bird_on_perch` points on its scaffolding. The carved tower is not distinguished from its neighbours.
- **No attachment.** A scenario point can be bound to a specific prop through a `CScenarioEntityOverride` (keyed by archetype name, with an `offsetPosition`). **0 of the 8** carved archetypes appears as an override key or `EntityType` anywhere in the layer. Nothing is attached to a carved model.
- **No time gate points at a carving either.** Almost every perch point near the marks is `0-0` (always available). The exceptions near Brennand are one `world_animal_eagle_on_perch` (t 6–19, 12 m away and 8.7 m up) and the `animals_sparrow_rigs` pair west of Fort Wallace (t 5–20, 81 m away). None is at a mark.

### Side observation (recorded, not a clue)

All five carved Butcher Creek outhouses have a `world_human_pee` point **1.1–1.5 m** from the mark, against **5 of 39 (13%)** uncarved site-specific outhouses and **28 of 163 (17%)** of all uncarved outhouse placements. The association is real in the numbers but is not evidence of anything: all five belong to **one settlement**, so it is n=1 site rather than five independent draws, and a village outhouse the ambient population actually queues at is exactly the sort of prop that gets hand-detailed in the first place. If anything it is a weak *authoring* correlation - the carved walls are the walls a ped stands in front of - not a mechanism. Fort Brennand's carved outhouse has no pee point within 468 m, so it does not generalise even across the two carving sites.

## Evidence

**Layer scale.** 131,939 scenario points across 663 base `levels_*` scenario regions (the 2026-07-25 metasweep run reported 131,853 through `DataFileMgr`, i.e. the update-pack view - the two agree). Classes: **10,398** bird-perch, 6,242 bird-ground, 31,367 other animal, 83,932 non-animal.

**Perch types** (base packs): `world_animal_bird_on_perch` 6,222 · `sparrow_on_perch` 1,862 · `crow_on_perch` 1,005 · `heron_on_perch` 328 · `vulture_on_perch` 322 · `eagle_on_perch` 270 · `seagull_on_perch` 214 · `pelican_on_perch` 82 · `eagle_eating_perched` 43 · `parrot_on_perch` 27 · `californiacondor_on_perch` 15 · `vulture_sunning_perched` 9 · `crow_drink_perched` 2.

**Per-mark table** (output of the perch pass):

| mark | world | nearest perch | nearest bird | nearest animal | nearest any | perch ≤25 m | perch ≤50 m |
|---|---|---|---|---|---|---|---|
| wallace_birds | (323.51, 1512.06, 194.70) | 27.5 m | 17.9 | 17.9 | 6.0 | **0** | 17 |
| brennand_tally6 | (2464.82, 295.26, 70.99) | 4.5 | 4.5 | 2.9 | 2.9 | 44 | 58 |
| brennand_tally7 | (2444.27, 304.53, 72.23) | 3.2 | 3.2 | 3.2 | 3.2 | 31 | 58 |
| brennand_scene | (2444.10, 304.81, 72.33) | 3.4 | 3.4 | 3.4 | 3.4 | 31 | 58 |
| butcher_LJSM_fort | (2576.83, 769.78, 81.43) | 60.9 | 14.4 | 11.5 | 1.9 | 0 | **0** |
| butcher_tally4 | (2576.73, 768.42, 80.74) | 59.6 | 15.0 | 11.4 | 1.1 | 0 | **0** |
| butcher_tally3 | (2548.36, 824.18, 75.95) | 38.7 | 5.1 | 2.9 | 1.2 | 0 | 1 |
| butcher_tally5 | (2502.60, 819.37, 71.95) | 45.7 | 41.0 | 19.9 | 1.2 | 0 | 1 |
| butcher_tally2 | (2513.27, 761.77, 74.02) | 13.1 | 13.1 | 9.0 | 1.1 | 1 | 1 |
| butcher_tally1 | (2572.89, 821.51, 79.25) | 51.1 | 17.5 | 11.4 | 2.4 | 0 | **0** |

**Controls.** Comparable places, not random points:

| control group | n | nearest perch: min / p10 / median / p90 | perch ≤25 m median (mean) |
|---|---|---|---|
| uncarved outhouses / privies (all) | 163 | 1.6 / 3.3 / 25.8 / 129.8 | 0 (3.2) |
| uncarved site-specific outhouses, placed once | 39 | 1.6 / 5.1 / 39.7 / 145.1 | - |
| uncarved towers / watchtowers | 36 | 2.4 / 2.9 / 20.7 / 232.5 | 6 (12.6) |
| Fort Wallace's other three towers | 3 | 10.9 / - / 14.8 / 20.7 | 6, 7, 8 |
| Fort Brennand's other three towers | 3 | 2.4 / - / 2.7 / 2.7 | 30, 32, 36 |

**Positive controls.**
1. *Coordinate transform.* World = entity position + **R(q)ᵀ** · local (the stored ymap quaternion is the conjugate). All six world positions already recorded in `rdr2-carvings.md` reproduce from the local offsets to **≤ 0.01 m**. This is what licensed computing the three fort positions the doc was missing.
2. *Layer completeness.* `Clusters` is empty in every base region, and every entity-override `spawnType` is a human seat/hitching-post prop, so `MyPoints` is the entire point set - there is no second place a bird perch could hide.
3. *Point count* agrees with the independent 2026-07-25 parse (131,939 base vs 131,853 via `DataFileMgr`).

## Method

- All 1,375 scenario-region `.ymt` copies (`rdr3\scenario\`) were dumped to XML (12 s). The `CScenarioPointRegion` schema resolves **fully**, so no hash cracking was needed: `ScenarioType`, `ModelSet`, `GroupName`, `InteriorName`, `iTimeStartOverride`/`iTimeEndOverride`, `iProbability`, `Flags`, `Pitch`, `vPositionAndDirection`.
- A placement query returned every base-ymap placement whose resolved archetype name contains a given substring, with position and rotation. It is the general control-group source for "is X near this thing" questions; here it produced the outhouse (194 rows) and tower (50 rows) control sets.
- A parsing pass over the XML dumps classifies every point (131,939 rows), applies the conjugate-rotation transform to the carving local offsets, and prints the per-mark table, the controls and every animal point within 60 m of a mark. Runtime ~40 s.
- An earlier, simpler scenario sweep was **not** reused: it read only `vPositionAndDirection` and reports a single nearest point per target, with no type, model set or time window.

## Caveats and blind spots

- Base packs only (`levels_*.rpf`). `update_4.rpf` ships its own copies of the same 663 regions; they were dumped but not parsed. Since the point counts agree with the independent `DataFileMgr` walk, an update pack moving a perch onto a carving is unlikely but not excluded.
- This measures the **scenario** layer only. Engine ambient bird spawning (`ambientbirdspawntunables.meta`), ambient vignettes and script-spawned birds are a different layer, and were closed separately and negatively on 2026-09-19 ([`scripted-mission-birds.md`](scripted-mission-birds.md), [`cutscene-bird-blindspot.md`](cutscene-bird-blindspot.md)).
- 8 scenario **type** names and 2 recurring **flag** names are still unresolved hashes, including `0x02635C96` - the single most common type in the layer at 24,180 points. A 10,656-candidate joaat attempt found none. If one of those turns out to be a bird behaviour the perch classification would need redoing; it is listed as an open follow-up below. The chance is low: the classification keys off `world_animal_*` names, and the unresolved types cluster in generic navigation/ambient roles (they co-occur with `walk`, `stand` and `drive`).
- `iProbability` and the `Flags` (`NoSpawn`, `NoAttraction`, …) were recorded but not used to weight the counts - a point that exists is counted even if the game rarely or never fills it. That only makes the negative stronger.

## Follow-ups

- Crack the unresolved scenario type and flag names, starting with `0x02635C96` (24,180 points).


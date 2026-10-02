# 2026-09-19: Birds that missions and cutscenes place on purpose: findings

**Task:** `completed/2026-09-19-scripted-mission-birds.md` · **Completed:** 2026-09-19 · **Outcome:** negative
**One line:** Mission scripts place birds only where each mission plays, 1.5 km or more from every mystery site. The "birds fly off as a cutscene starts" effect comes from ambient vignettes and engine birds, not from any per-cutscene authoring. The blue jay is Beecher's Hope homestead dressing.

## Answer

- **There are three independent sources of birds:**
  1. **Engine ambient birds** (`common_0.rpf\data\tune\ambientbirdspawntunables.meta`, `CAmbientBirdSpawn`): birds flushed from trees at 15–35 m and brush at 25–50 m by gunfire (80 m) or heavy movement (30 m). Not tied to any place.
  2. **Ambient vignettes**: `update_2.rpf\x64\levels\rdr3\script\parseddata.rpf\ambientvignettes.ymt`, 4,569 points by district, loaded by `ambient_vignette_manager_loader`.
     - 1,803 of the points are bird types: flee swarms, `*_on_perch`, `bird_land_*`, wire sparrows, birds-in-tree.
     - 45 of the 248 `av_*` scripts are for birds.
     - Perch points are shared across species (jay, cardinal, owl, hawk, eagle at one position).
  3. **Mission-authored birds**:
     - `birds.tsv`: 652 bird-model references in 114 scripts.
     - 41 are inline spawns (`mob2` 22 crows, `mudtown3` 7 chickens, `mary1` 5 crows, vultures in `rcm_dutch11` and `rcm_down3`, the `beechers2_2_outro` jay, the `marston1` eagle).
     - The rest are table-driven (`resolved.tsv`) or traced by hand (below).
- **Every mission bird is local to its mission.**
  - `finale2`: an eagle on Mount Hagen at the final confrontation.
  - `gang2`: seagull flocks along a high flight route near the east coast.
  - `trelawny1`: crows in a zone at (1058, -2023).
  - `sean1`: an eagle at (-1295, -826).
  - `sadie3`: crows at (713, -511) and (631, -591).
  - `winter2`: crows in the mountains at (-1775, 2758).
  - `smuggler2`/`_outro`: a songbird pair at Guarma.
  - `braithwaites1`: jays placed via map scenario points.
- **The "two birds" pattern.** Authored pairs exist (`odriscolls3` jays, `smuggler2` songbirds, `rcm_abigail22` and `rcm_beechers21` jays). But no shared cutscene helper spawns a pair that flies off.
  - Cutscene origins have a bird vignette within 50 m exactly as often as a non-bird vignette (346 vs 346 of 708 scenes).
  - The birds taking off around cutscene starts (e.g. Rhodes station, where jay and cardinal perches and crow and sparrow flocks sit within 50 m) are ambient vignettes near settlements and camps.
- **Blue jay.** Mission jays:
  - Beecher's Hope, the house-building missions: `beechers2_2` (-1650.0, -1364.5), `beechers2_2_outro` (-1648.3, -1387.0, which flies off to (-1552.0, -1457.9, 93.0) after the scene), `rcm_abigail22` pair (-1645.4, -1373.7), `rcm_beechers21` pair.
  - `odriscolls3`: a pair at (-868.4, -743.5), moving by checkpoint to (-849, -728) and (-735.7, -554.1).
  - `braithwaites1`: a scenario pair.
  - Plus 63 ambient jay vignettes.
  - All mission jays are 1.5–2.7 km from every site. The jay is the game's songbird for homestead and idyll dressing. It carries no signal.
- **Mystery sites.**
  - No mission bird is placed near a carving or a web. No bird is placed "where the mission doesn't need one" near a site.
  - The closest birds of any kind are ambient vignettes:
    - a jay/cardinal landing 12 m from Butcher Creek D, on the ground among the settlement's barrels, facing about 120° away;
    - a shared perch on top of the ruined `civ_twr_01a` tower, 17 m from the Fort Brennand outhouse, facing east, away from it;
    - an eagle perch 48 m from the Fort Wallace birds, 57 m below them.
  - All three are ordinary.

## Evidence

- **Positive control:** `spd_giant_birds`, found directly by the census.
  - Once the player has 30 or more ANIMALS compendium entries and comes within 200 m of (626.1, 2194.4, 223.1), 12 pheasants fly an 11-waypoint route to the Giant at (1706.7, 2183.5, 323.2).
  - The community already knows it. It proves both that Rockstar authored "birds lead you to a secret" once and that this census finds such a case.
- **Site density control** (`near.py 300`): the ratio of bird to non-bird vignettes near the sites is 0.27–1.05, against 0.63 map-wide. No enrichment.
- **Cutscene control** (`cutbirds.py 50`): 346/708 cutscene origins have a bird vignette within 50 m, and 346/708 have a non-bird vignette. No enrichment.
- **Bound on unresolved scripts** (`bound.py 300`):
  - Method: every inline world coordinate triple in `rcm_beechers21`, `braithwaites1`, `gang2`, `finale2`, `trelawny1`, `sean1`, `sadie3` and `winter2`, measured against the sites.
  - Hits within 300 m are only these:
    - shared include coordinates;
    - volume-box sizes;
    - the `gang2` ride route end (72 m from the Fort Brennand outhouse, no bird on it);
    - a shared campfire location 83 m from `spiderdream07x`.

## Method and tools

- `tasks/tools/missionbirds/`:
  - `census.py` → `birds.tsv`, `flights.tsv`. About 12 s over the decompiled corpus `tasks/tools/ysc-corpus-scan/corpus/1491.50/script_rel`.
  - `resolve.py` → `resolved.tsv`: mission framework slot → model → per-checkpoint position tables.
  - `vignettes.py` → `vignettes.tsv`, flattened from `ambientvignettes.ymt.xml`.
  - `near.py [R]` → `near.txt`: birds against sites, with the non-bird control. `webs.txt` holds the web positions.
  - `bound.py [R] [scripts]`: coordinate bound for scripts whose spawns come from tables or vectors.
  - `cutbirds.py [R]` → `cutbirds.tsv`: cutscene origins (`hunt/animscenes.tsv`) against bird vignettes.
- The hand traces (`gang2` `func_1859`/`func_931`, `sadie3` `func_1860`, `finale2` line 75053, `winter2` `iLocal_380`, `rcm_beechers21` `func_192`) are recorded in the task file's Progress.

## Caveats and blind spots

- **Decompiled corpus only.** The census reads decompiled source. Per `rdr2-scripts.md`, an absence claim should be confirmed with first-hand `.ysc` greps. The spawn census wasn't re-done that way.
- **Runtime-computed positions** (player-relative, random offsets, scenario points) cannot be bounded from the script. `braithwaites1`'s jays and `trelawny1`'s crows (random within 100 m of a zone) are of this kind. Their anchors are mission-local.
- **The vignette second vector** (x2/y2/z2: a ground-level point 36–75 m away, loosely in front) is unresolved. It doesn't affect the distances.
- **No in-engine viewing.** Script and vignette birds aren't map entities, so CodeX can't show them. The two nearest spots were checked through the entity census instead of by eye. Nothing checked where a jay looks inside a cutscene clip (`.ycd` track matching).
- Only base-game scripts and the `update_2` vignette file were read; DLC mission scripts were not.

## Follow-ups

None filed. The census, the controls and the bound all come back negative, and the remaining gaps are low value.

# 2026-09-19: Did the cutscene bird check miss birds that scripts place?: findings

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**Date:** 2026-09-19 · **Outcome:** positive **One line:** Yes. `.yas` scenes only list the birds they create themselves. The blue jay and other mission birds are spawned by the mission scripts, sometimes then handed to a cutscene, so the scene census could never see them.

## Answer

- **Scene files contain no songbirds.** No `.yas` scene in the base game names a blue jay, songbird, cardinal, robin, sparrow or oriole. The scene census (`tools/hunt/animscenes.tsv`, 938 scenes) holds only these bird models:
  - `a_c_crow_01` 105, `a_c_vulture_01` 74, `a_c_eagle_01` 41, `a_c_duck_01` 30;
  - heron, hawk, rooster, pelican, owl, egret, seagull, chicken, prairie chicken, pheasant, loon, goose, raven, parrot, cormorant, turkeys, quail and pigeon (3 to 19 each).
- **The blue jay is spawned by script.** `beechers2_2_outro` creates `a_c_bluejay_01` at **(-1648.3, -1387.0, 83.1), heading -150** (Beecher's Hope). It waits for `IS_ANIM_SCENE_LOADED`, sets `SET_BLOCKING_OF_NON_TEMPORARY_EVENTS`, and when the scene ends sends the bird off with `TASK_FLY_TO_COORD` to (-1552.0, -1457.9, 93.0). *Corrected 2026-09-19:* the jay is not bound into the scene (`SET_ANIM_SCENE_ENTITY` is only called for the player). It is placed beside the scene, so it is in shot.
- **Story scripts that use `a_c_bluejay_01`**, besides the shops, crafting, camp and UI:
  - `beechers2_2` (its streaming list also holds the house frame, planks and chimney props);
  - `beechers2_2_outro`;
  - `rcm_beechers21`;
  - `rcm_abigail22` (two slots);
  - `braithwaites1`;
  - `odriscolls3` (next to `a_c_vulture_01`).
- **`a_c_songbird_01` and sparrow**, outside the shops: `fussar2`, `smuggler2` and `smuggler2_outro` (Guarma, which fits the user's memory), `feud1`, `mary1`, `mary3` and `hunting1`.
- **141 story scripts name some bird model.** Spawns at inline coordinates include:

  | script | birds | location |
  |---|---|---|
  | `mob2` | 22 crows | around (2670–2775, -1045 to -1090, 46–50) |
  | `mary1` | 5 crows | around (1095, 460, 96) |
  | `mudtown3` | 7 chickens | around (-270, 688, 112) |
  | `rcm_down3` | 2 vultures | |
  | `rcm_dutch11` | 2 vultures | (853.5, -383, 81.8) |
  | `marston1` | 1 eagle | (-1663.8, 372.0, 104.2) |

  Many spawns read their positions from vector tables, so this list is a lower bound.
- **Generic birds that fly off may come from ambient vignette scripts.** Candidates: `av_bird_flee_swarm`, `av_bird_fence_swarm`, `av_bird_land`, `av_bird_land_swarm`, `av_bird_swarm`, `av_birds_in_tree`, `av_bird_on_animal`.

## Evidence

- Scene census: the model column of the 938-scene animscene table, filtered for `a_c_*` bird models.
- Archive search for `bluejay` (and songbird, cardinal, robin, sparrow, oriole, waxwing), base packs. Blue jay assets exist only as the metaped model, textures, skinning animation, UI, audio and posematcher. There is no blue jay cutscene or animscene asset.
- Script grep over the decompiled corpus, build 1491.50, which matches the install.
- Positive control: the known eagle in `cutscene@fin2_ext_p16` shows up in the scene census.

## Method

- An animscene table (scene, model, …) was exported from the game files.
- Script grep: `grep -liE 'a_c_(bluejay|...)' script_rel/*.c` over the decompiled corpus.

## Caveats and blind spots

- The decompiled corpus is a readable cross-reference. Absence claims still need first-hand `.ysc` greps. The decompiler prints `joaat("name")` only for names it knows.
- Not yet established: which system makes the "two birds fly off" moments, and where each blue jay is placed apart from `beechers2_2_outro`.

## Follow-ups

- [`scripted-mission-birds.md`](scripted-mission-birds.md): the full census of script-placed birds, the two-birds pattern, the blue jay placements, and distances to the mystery sites against a control.

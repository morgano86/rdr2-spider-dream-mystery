# 2026-09-19: Mission scripts near the carving sites, and one-off mission spawns: findings

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**Task:** `completed/2026-09-19-mission-scripts-carving-sites.md` · **Completed:** 2026-09-19 · **Outcome:** negative **One line:** No script references any carving or its host model; the coordinates scripts do hold near the marks are mission staging, and uncarved outhouses score *higher* on the same test than the carved ones do.

## Answer

**No script addresses a carving.** Two independent routes, both negative:

- **Names and hashes — zero.** None of the eight carved host archetypes (`old_fort_twr3`, `civ_01_outhouse`, `civ_twr_03b`, the five `but_01_outhouse_cliff*`) appears anywhere in the 2,195 installed scripts, as an ASCII string or as an unaligned little-endian joaat constant. This is first-hand over the real install, not the decompiled corpus. It is what the standing structural rule predicts: scripts never address region-baked map assets (`rules/rdr2-scripts.md`).
- **Coordinates — at or below the uncarved baseline.** Counting distinct scripts that hold a real coordinate literal within 5 m (and 5 m of height) of a mark: the ten carving marks score **0 to 5**; uncarved outhouses and towers of the same kind score **1 to 113**. The single highest-scoring target in the run is an *uncarved* Valentine outhouse. Three of the ten marks score zero. There is no sense in which scripts pay attention to these places more than to comparable places.

Every surviving coordinate hit is a mission staged at that location, and reads as such:

| mark | script | dist | what it is |
|---|---|---|---|
| butcher_tally5 | `rcm_poisoned_well2` | 0.9 m | one of ~20 Butcher Creek waypoints in the poisoned-well random character mission, used as a ped placement with a 233.9° heading |
| butcher_tally5 | `rcm_dutch31` | 1.0 m | Dutch chapter-3 mission, same village |
| wallace_birds | `native_son3` | 2.1 m | dozens of coordinates over the Fort Wallace tower, all at z 184–192 — the walkway, **8 m below** the carved roof tile at 194.70 |
| brennand_tally6 | `rcm_bounty_exconfed1` | 2.6 m | bounty mission at Fort Brennand |
| brennand_tally7/scene | `winter2` | 3.2 m | chapter-1 mission staging |
| butcher_tally2 | `native_son1` | 3.5 m | mission staging |
| butcher_tally3 | `fme_round_up` | 4.7 m | free-roam event |

**No one-off spawn is out of place.** Of 6,561 entity-creation calls, 383 models are spawned by exactly one script (direct arguments) and 13,070 joaat literals are referenced by exactly one script (the wider tier). Only **12** one-off literals are animal models, all mundane: egret/elk/moose variants inside the `short_update` director table, and shark and snake pelts in multiplayer. No bird is spawned by a single script in a way that isn't already explained. The scripts that stage at a carving site carry 0–11 one-off literals each and every one suits its mission — `native_son3`'s are `p_cs_nooseshort01x` and two ropes, for the hanging that mission stages at Fort Wallace.

The **bird** half of the one-off question was already answered on 2026-09-19 by `findings/2026-09-19-scripted-mission-birds.md` (652 bird-model references across 114 scripts, table-driven spawns resolved by slot, every mission bird local to its mission), so it was not redone here.

## Evidence

**Scale.** 2,195 `.ysc` scanned first-hand (all of them; scripts ship only in `update_2.rpf`). 2,194 decompiled files in the build-matched corpus. 6,561 creation calls; 34,522 distinct joaat literals.

**Distinct scripts with a strict coordinate hit within 5 m / 5 m:**

| target | scripts | | target | scripts |
|---|---|---|---|---|
| **NEG** uncarved Valentine outhouse A | **113** | | butcher_tally5 | 5 |
| *CTRL* vampire clue 2 | 91 | | brennand_tally7 | 4 |
| *CTRL* strange statue | 18 | | brennand_scene | 4 |
| *CTRL* vampire clue 1 | 15 | | brennand_tally6 | 1 |
| **NEG** uncarved `civ_twr_01a` | 4 | | butcher_tally2 | 1 |
| **NEG** uncarved watchtower (Roanoke) | 3 | | butcher_tally3 | 1 |
| **NEG** uncarved Valentine outhouse B | 2 | | wallace_birds | 1 |
| **NEG** uncarved `grh_outhouse` | 1 | | butcher_tally1 | **0** |
| **NEG** uncarved `old_fort_twr1` | 1 | | butcher_tally4 | **0** |
| | | | butcher_LJSM_fort | **0** |

**Positive control.** A multi-site discovery hardcodes its own site coordinates bit-exact with the scenario point. `discoverable_alchemist_house.ysc.c` holds `2826.6787f, -1323.0426f, 46.43373f` and `2698.488f, -1306.1943f, 49.48277f` — the two `wb_disco_vampire_clues` scenario positions to four decimals. The scan must find these, and does (91 and 15 scripts, via inlining).

**Negative control.** Uncarved outhouses and towers, real placements taken from `tasks/tools/perch/`. This is what makes the result readable: without it, "five scripts hold a coordinate within a metre of the tally of 5" looks like a finding rather than the below-baseline number it is. The 113 at the Valentine outhouse is one `_ADD_BOX_VOLUME_TO_VOLUME_AGGREGATE` call — an 80 × 100 × 87 m settlement exclusion box centred at (-270.606, 827.282, 118.425) — inlined into every `beat_*` random-encounter script.

**Name-scan false positives, all identified:** `carv` → the Francis Sinclair **rock carvings** collectible (`RCM_BRIEF_DESC_ROCK_CARVINGS_01/02`, 393 hits each; the known collectible, already excluded as a lead); `etch` → substrings of "sketch"/"fetch"; `scratch` → `LANDMARK_SCRATCHING_POST`, `av_bear_scratch_back`; `engrav` → the gunsmith engraving sales pitch; `civ_01` → `male_civ_01` animation clips; `outhouse` → `MV_OUTHOUSE_HINT` and a `VOL OUTHOUSE` volume label; `graffiti` → `ldj_shack_cc_graffiti`, `l_08p_tunnel2_cc_graffiti` (real graffiti content elsewhere, not these marks).

## Method and tools

`tasks/tools/carvescript/` (README has the full run instructions and the traps).

- **`CarveScript.exe coords <xytol> <ztol>`** — first-hand over every installed `.ysc`. Collects every plausible world-coordinate float with its byte offset, then looks for an x, y and z within a byte window. ~6 s.
- **`CarveScript.exe names`** — the host archetypes as case-folded ASCII substrings plus unaligned LE joaat, over the same set.
- **`spawns.py`** — the decompiled corpus: models passed directly to creation natives (tier A) and every joaat literal per script (tier B).

**Two scan bugs, both caught by the positive control — the transferable part of this task:**

1. **A coordinate in compiled bytecode is not three adjacent floats.** Each component is its own `PUSH_F` immediate, so x/y/z sit at a uniform **5-byte stride** with opcode bytes between them. The first version required adjacency, reported "nothing near the carvings", and would have been written up as a negative had the control not also come back empty.
2. **A byte-window search matches components out of position.** With a window it will happily take the **(y, z) of an unrelated coordinate as the target's (x, y)**: Fort Brennand's (2444, 304) collides with Colter's (·, 2440, 308), which is inlined into 329 scripts. That produced a spurious "357 scripts hardcode a coordinate near a carving". The fix (`STRICT`) requires all three components in tolerance **and** a uniform stride ≤ 8 bytes — the shape of a real coordinate literal. Brennand fell 357 → 4; every positive control survived.

**Coverage, stated honestly.** Only 1,445 of 6,561 creation calls (22%) name their model literally; the rest read it from a variable or table field. Tier B counts every joaat literal instead — a reference rather than a proven spawn, but a sound superset, because no string-concatenation native exists in the corpus, so a table-driven model still needs its name as a literal somewhere in the script.

## Caveats and blind spots

- **Library inlining inflates every per-script count.** Tier B finds bird models in 529 scripts where the careful slot-resolving pass found 114. Multi-script counts from a flat literal scan mean little; the **one-off** direction is the reliable one, since a literal in exactly one script really is local to it. The same effect explains the largest coordinate counts.
- **Full slot resolution was not generalised.** `tasks/tools/missionbirds/resolve.py` resolves the mission ped-spawn framework (`func_K` slot → model index, `func_M` index → model, `func_P` slot → position) for birds. Extending it to all models would turn tier B's "referenced" into "spawned, at a known position" and is the open end here. It would sharpen the one-off list but cannot change the name/hash negative.
- The coordinate scan tests literals only. A script computing a position arithmetically, or reading it from a `.ymt`, is invisible to it — though nothing would then tie it to a carving either, since the host names are absent too.
- Tolerances were 5 m / 5 m (tight) and 50 m / 40 m (wide). Both runs are kept; the conclusions are from the tight one with the strict triple test.

## Follow-ups

None raised. The natural extension — generalising the mission-framework slot resolver to all models — is recorded as a caveat above rather than as a task, since the question it would sharpen is already answered by the name/hash negative.

## Docs updated

- `.claude/rules/rdr2-scripts.md` — the coordinate-grep section now states the `PUSH_F` stride, the component-misalignment artifact, and the inlining caveat on per-script counts, with the carving negative recorded beside the earlier web negative.

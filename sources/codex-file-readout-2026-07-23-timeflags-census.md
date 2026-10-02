# CodeX finding relay — time-schedule outlier scan (2026-07-23)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

> **Filed 2026-09-01** as part of corpus source **[#89]** (`sources/sources.md`), verbatim apart from this note. **It HAS since been integrated** — see [K50]–[K52], [U39], [S47] and the 2026-09-01 log entry.

Staged for later integration into the corpus (K/U/H/S organization to be done by a future session — same convention as the fragment/boundary relay from earlier today). Source: game-wide `timeFlags` bucketing of every `CTimeArchetypeDef` archetype/placement in the RDR2 install, run from the CodeX diagnostic harness (LightDiag, session scratchpad). All numbers below are first-hand file data, not community sourced.

## Method / baseline

Every time-gated archetype game-wide: **994 archetypes, 994 placements** (1:1 — each is a unique baked prop). Bucketed by exact `timeFlags` value:

- **Dominant "normal" schedule: `0x1E0007F` = lit 21:00–07:00 + onscreen-change allowed — 921 of 994 placements.** These are the `*_em*` (emissive night variant) props for building windows game-wide. Any other pattern is, by definition, a deviation someone hand-authored.

## The user's 3 observed deviant buildings — ALL CONFIRMED in file data

1. **Valentine Church = `val_05__em001` @ (-226.59, 804.00, 133.63)** — lit **21:00–01:00** (`0x1E00001`). The only deviating emissive in all of Valentine (every other `val_*_em*` is normal 21–07). Lights go out at 1 AM, six hours early.
2. **Fort Wallace (dev region code `old_` = "Old Fort Wallace", confirmed via `AIMEMLOC_CML_OldFortWallace` / `establisher_old_fort_wallace_1` strings) — FOUR buildings, each with its own unique schedule,** the densest cluster of schedule deviation in the game:
   - `old_01_bsmith_em` (blacksmith) @ (339.20, 1480.63, 180.27): lit **21:00–24:00** (`0x1E00000`)
   - `old_01_quater2_em` (quarters 2) @ (318.46, 1486.93, 181.96): lit **22:00–03:00** (`0x1C00007`)
   - `old_01_quater_em` (quarters) @ (316.52, 1499.54, 181.96): lit **23:00–05:00** (`0x180001F`)
   - `old_01_capt_em` (captain) @ (344.38, 1509.17, 183.02): lit **00:00–06:00** (`0x100003F`) Note the staggered starts 21→22→23→00 across four buildings — reads like authored set dressing (a fort settling down for the night watch-by-watch), but Fort Wallace is the mystery's last verified clue ([K16]), so a 4-step hour sequence 21/22/23/00 at that exact location is worth logging as data, whatever it means.
3. **Wapiti — five deviant props, and they are teepee doors/flaps, not building emissives** (all in ymap `0x3BD21365`): `wap_mstr_ptchd_dr` **18:00–05:00**, `wap_master_tp009_dr` + `wap_master_tpr7_flap` **20:00–06:00** (both *without* the onscreen bit — will only change off-screen), `wap_master_tp006_dr` **22:00–07:00**, `wap_mstr_ptchd001_dr` 21:00–07:00 but *without* the onscreen bit (unique among normal-hours props). Positions cluster (448–482, 2222–2268, ~249). So the "Wapiti lights look different" observation is real but the mechanism is closed-at-night teepee door props with staggered hours, not lamp emissives.

## Sites the scan surfaced blind — both already-known content (user-identified), new file-level facts logged

The scan flagged these as anomalies with no prior knowledge of them; the user identified both as known mystery content. That's a validation data point for the method (it found them independently), and the file data adds hour/flag detail to the record:

1. **The CENTRAL WEB (letter "N" + pole symbol, spawns in the trees) = the hour-01:00 site at (1282.0, -131.6, ~99.7).** Four time-gated `cablemesh*` meshes (`cablemesh87397_thvy001`, `87399_thvy001`, `87405_hvlit001`, `87455_hvlit001`) active ONLY at hour 1, clustered within ~1 m, with nothing else within 12 m — no telegraph pole entity and **no `spiderdreamNNx` feather**: unlike the 8 numbered webs this site is strand-meshes-only in the files (consistent with it rendering in trees rather than on a pole). The `_thvy` name variant appears nowhere else game-wide — plausibly the letter/symbol-bearing meshes. File-verified active hour: **01:00** — completing the hour ladder (central=1, then the numbered webs cover 2,3,4,5 twice each). No 9th spiderdream archetype exists (strings and archetype table both checked).
2. **The BUTCHER CREEK PENTAGRAM = the hour-04:00 mesh `cablemesh277747_hvlit001` @ (2592.52, 831.74, 82.79)**, 1–3 m from `but_house_hd002` and its porch props. File-verified active hour: **04:00**, and it is the ONLY single-hour prop in the game with the onscreen bit set (`0x1000010` — allowed to appear/disappear while watched, unlike all 8 webs + central which are off-screen-only). That flag asymmetry is now a first-hand fact worth keeping.
3. **Annesburg (whole town, `ann_04`, 20 props) + MacFarlane's Ranch main house (`mfr_04_mainhouse_em`) are lit 21:00–08:00** — one hour past the global 07:00 off. A town-wide authored shift (mining town on early shift?); weak as a mystery signal, but it is the complete list of "off at 8" content.
4. Saint Denis `new_*_vfx_helper_*` props (06–11,17–22 or 06–21 schedules) — user-identified as timed smoke emitters for factories/houses; mundane, no investigation needed.

**Coverage note:** with the central web and pentagram identified, the full census (994 props / 19 patterns) contains NO remaining unexplained single-hour or short-window content. The `timeFlags` channel is now exhaustively enumerated and closed — any further conditional appearance must come from a different mechanism (scripts, map/entity-set states, engine logic), not archetype time-gating.

## Negative results (useful bounds)

- No time-gated archetype game-wide exists that is defined but never placed (0 unplaced).
- The 8 spiderdream webs + their cablemesh strands remain the ONLY sub-24h single-hour content besides the two new sites above; full histogram has just 19 distinct patterns game-wide.
- Rhodes church (`rho_church_ext_em`) and the Blackwater church are on the normal 21–07 schedule — Valentine's is genuinely the only deviant church.

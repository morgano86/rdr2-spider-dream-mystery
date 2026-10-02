# How RDR2 scripts read the player's look (mask / weight / hair / dirt) — and what uses it

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**Date:** 2026-09-05 · **Status:** investigation complete, negative on "hidden purpose" **Method:** grep/decode over the build-matched decompiled corpus `tasks/tools/ysc-corpus-scan/corpus/1491.50` (2,194 files, build 1491.50) — see `.claude/rules/rdr2-scripts.md` for the corpus caveats (inlined shared library; `joaat("x")` vs raw-hash are two different searches and both were run).

**Question asked:** the Madam Irine fortune-teller machine comments on the player's weight, hair and masks; Abigail reacts to John wearing a mask. Which script drives that, and is there any *sneaky* use of these signals (mask-gated mission, fat-gated encounter, …) that players would never find?

**Answer:** the fortune teller is `discoverable_generic_corpse.ysc` (`FTELL_*`), discoverable id `657666087` = the **Circus Wagons** discovery — prop `s_fortuneteller01x`, ped `u_f_m_circuswagon_01`, soundset `fortune_teller_soundset`, journal `journal_disc_circus_wagons_*`, audio bank `FTELLAU`, animscene sections `fortune_teller` / `punch_fortune_teller`. Appearance is read through four primitives (below). **Every consumer found across all 2,195 scripts selects a dialogue line or an animscene variant. Nothing gates a mission, spawn, reward or unlock.**

---

## The four primitives

| signal | how a script reads it | range |
|---|---|---|
| **worn item (exact)** | `Global_1946054.f_1497.f_1[slot]` — the 39-slot equipped-item array; a `BOOL f(Hash)` helper maps item→slot then compares | item hash |
| **worn item (category)** | `PED::_IS_META_PED_USING_COMPONENT(ped, <categoryHash>)` — `HATS`, `masks`, `neckties`, `Hair`, `heads`, `GLOVES`, `satchels`, **`strange_hat`/`strange_upper`/`strange_lower`**, `fancy_upper`, `wearable_masks`, `HORSE_SADDLES`, … | bool |
| **weight** | `Global_1347477.f_196`, mirror of `playerRPGData.fAttributePoints[13]`; `short_update` clamps it to **-10 … +10** and swaps the body metaped (`509283903` thin / `1822769204` normal / `1837059600` fat) | -10..10 |
| **hair / beard / dirt / honor** | `Global_40.f_7748.f_1` (hair length), `Global_40.f_7731[0..2]` (beard: chin/chops/moustache), `ATTRIBUTE::GET_ATTRIBUTE_POINTS(ped, 22)` and `(ped, 16)` (dirtiness, 0-10000 scale), `Global_40.f_11095.f_35` = `playerRPGData.iHonor` | ints |

`Global_40.f_11095` is the whole `playerRPGData` save struct — its field names are recoverable verbatim from `startup.ysc`'s savegame loader (`playerRPGData.fPlayerWeightUpperLimit`, `.iHonor`, `.fFatResist`, `.iOverfedTimer`, …), which is the cheapest way to name any field in it.

## The fortune teller decoded (`discoverable_generic_corpse.ysc`)

State machine `func_293`; line chosen by `func_509(bIsRepeat)`; played via `AUDIO::CREATE_NEW_SCRIPTED_CONVERSATION` + `START_SCRIPT_CONVERSATION` on the root label — so the `FTELL_*` names are **conversation roots in the speech DB**, which is where the subtitle text lives.

Sequence: `FTELL_OPEN` → a reading → repeat; a 4th+ activation gives `FTELL_MANY`; 3 repeats in one session give `FTELL_GEN`. Player dead → `FTELL_GEN`.

| # | label | condition |
|---|---|---|
| 0 | `FTELL_MASK` | wearing any of **15 specific hats/masks** (list below) |
| 1 | `FTELL_OUTFIT` | component `strange_hat` **or** `strange_upper` **or** `strange_lower` |
| 2 | `FTELL_BEARD` | any beard channel (chin/chops/moustache) > 6 |
| 3 | `FTELL_HAIR` | hair length > 6 |
| 4 | `FTELL_BLOOD` | `PED::_0x88A5564B19C15391(ped)` or `PED::_0x354CA4DDDEEC397A(ped) > 50` (blood coverage) |
| 9 | `FTELL_BOUNTY` | wanted level > 2 **or** bounty > $25,000 |
| 5 | `FTELL_FAT` | weight > **+4** |
| 6 | `FTELL_THIN` | weight < **-4** |
| 8 | `FTELL_TIRED` | `playerRPGData` field 1 < -80 (a core value) |
| 13 | `FTELL_BATH` | dirt attr 22 > 7500 **or** stat `baths_taken` < 1 |
| 12 | `FTELL_MUD` | dirt attr 22 > 5000 |
| 10 / 11 | `FTELL_HIGH_H` / `FTELL_LOW_H` | honor > 0 / else |
| 7 | `FTELL_HUNGRY` | `func_679()` — **returns constant `true`** |
| 14 | `FTELL_GEN` | fallback |

**Dead branch worth noting:** in the deterministic (first-reading) path the chain ends `if (honor>0) return 10; if (!(honor>0)) return 11;` — exhaustive, so the following `FTELL_HUNGRY` test and the final `return 14` are **unreachable**. `FTELL_HUNGRY` can only ever play on a *repeat* reading, where the selector picks a category at random (`GET_RANDOM_INT_IN_RANGE(0,65536) % 14`).

### The 15 "weird hat/mask" items she reacts to

```
clothing_item_mask_pig_001            clothing_sp_conquistador_hat_000_1
clothing_item_skullmask_mr1_000_1     clothing_sp_dead_miner_hat_000_1
clothing_item_skullmask_mr1_001_1     clothing_sp_scarecrow_01_hat_000_1
clothing_item_skullmask_mr1_002_1     clothing_sp_scarecrow_02_hat_000_1
clothing_item_pz_hat_pirate_01        clothing_sp_scarecrow_03_hat_000_1
clothing_sp_chinese_labor_hat_000_1   clothing_sp_scarecrow_04_hat_000_1
clothing_sp_civil_war_hat_000_1       clothing_sp_viking_hat_000_1
                                      clothing_item_sp_valsheriff_hat_000
```

## Complete inventory of appearance-gated behaviour (all 2,195 scripts)

`_IS_META_PED_USING_COMPONENT` was enumerated exhaustively. Two forms account for ~1,700 of the hits and are inlined library boilerplate (`wearable_masks` strip-before-cutscene ×662; the "has a hat" helper ×366). Everything that actually *branches on the player's look*:

| script | signal | effect |
|---|---|---|
| `discoverable_generic_corpse` | 15-item list, strange_*, beard, hair, blood, weight, dirt, honor, bounty | fortune-teller line |
| `mary3` | weight > 0 → `MRY3_OVERWEIGHT`; strange_upper/lower → `MRY3_ST_OUTFIT`; strange_hat → `MRY3_ST_HAT`; dirt attr 16 ≥ 80 → `MRY3_DIRTY` | Mary comments |
| `grays1` | strange_upper/lower → `GRY1_OUTFIT`; strange_hat → `GRY1_HAT` | ride-along banter |
| `gang2` | `fAttributePoints[13]` ≥ 4/10 → `GNG2_B_FAT`; strange_upper + a hat → `GNG2_B_HAT` | ride-along banter |
| `homeinvasion` | strange_hat → `PRHM7_HAT`; strange_upper → `PRHM7_OUTFIT` | **Charlotte Balfour** comments on your hat/outfit during a friendly visit (see note) |
| `industry3_intro` | `fancy_upper` | scene variant |
| `rcm_mary02` | two hat components | animscene `1-Start_Hat` / `1-Start_NoHat` |
| `braithwaites1` | a hat component | strips the hat before forcing an outfit |
| `sleeping_scenario` | ~90-entry hat whitelist | which hats tip over the eyes when sleeping |
| `shop_*` (21 scripts) | `masks` category | `WELCOME_MASK` / `PLAYER_REMOVE_MASK` / `MASK_ESCALATED` / `MASK_REMOVED` refusal ladder |
| `bandana` + 12 mission scripts | equipping a mask | raises `EVENT_SHOCKING_EQUIPPED_MASK` |
| `long_update` / `short_update` | weight | stamina/health multipliers, body metaped swap, `rpg_overweight`/`rpg_underweight` pause-menu icon |


### `PRHM7` = Charlotte Balfour's cabin (homestead "Rocky Seven")

`homeinvasion.ysc` owns the homestead framework, and `PRHM7` is homestead 7, internal codename `rocky`: ped `cs_rockyseven_widow`, `DISCOVERABLE_NAME_CHARLOTTE`, `ui_letter_charlotte`, interior entity sets `rocky_int_messy` / `rocky_int_clean`, doors `DOOR_ROC_HOUSE_INT_1/2`, anim dictionaries `script@proc@homerobberies@rocky@{skinning,shooting_practice,visit_dinner_b,visit_tired_a,leadin,leadout}`. Its label set is the whole Widow of Willard's Rest questline - `PRHM7_SKINNING_*`, `PRHM7_HUNTW1..3`, `PRHM7_AHOWSKN1`/`JHOWSKN1`, `PRHM7_RTNGRAVE`, `PRHM7_RTNDINN`/`LEAVDINN`, `PRHM7_BANT1A`/`1J` (`_A` = Arthur, `_J` = John).

The hat/outfit line is `func_550` case 4 (the friendly-visit state, after her cabin has been switched to `rocky_int_clean`). Gates, in order: 10 s dwell timer, player within **15 m**, a facing/LOS check, and a one-shot bit `0x400000` so it fires once per visit. `strange_hat` wins over `strange_upper`; **`strange_lower` alone does not trigger it here**, unlike `grays1` and `mary3` which test lower too.

**Abigail / NPC mask reactions are not scripted per-NPC.** Scripts only raise `EVENT_SHOCKING_EQUIPPED_MASK`, and only ever distinguish the *category* `masks` (`-525676072`) from `HATS` (`-2061583405`). Any per-mask flavour must come from the audio/speech metadata layer, not `.ysc`.

## Negative results (the "hidden purpose" question)

1. **The 15-item mask list has exactly one consumer.** A corpus-wide sweep of "is the player wearing item X" call sites carrying a literal item hash returns only three families: the winter coat `CLOTHING_SP_COAT_WINTER01_VARIATION_01` (289×, the cold system), `clothing_hl_player_satchel_008_1`, and the fortune teller's 15 (1× each). A raw-hash sweep (120 numeric/hex/case forms of the 15 names) finds **zero** occurrences outside those `joaat()` renderings.
2. **The discoverable pickup items** (animal/Aztec mask `1057717101`, ram mask, cat mask, pirate hat, viking gear, scarecrow hats, …) are referenced **only** by `discoverable_generic_carriable` and `discoverable_generic_corpse`. No other script in the game reads them.
3. **Ambient spawn conditions carry no appearance field.** `init_all_sp.ysc`'s encounter record builder (`func_108`, 16 params) and the vignette builder (`func_119`) write only time-of-day, weather, story-progress, proximity, cooldown and probability into `Global_1310750[]` — consistent with `.claude/rules/rdr2-scripts.md` "spawn conditions live in director tables". So "start an encounter only while wearing mask X / while fat" is **not expressible** in that system.
4. **Weight touches four files only** (`long_update`, `short_update`, `mary3`, `discoverable_generic_corpse`); the hair/beard globals are read only by the growth library and the fortune teller.

Conclusion: the appearance layer is fully enumerable and entirely cosmetic-facing. It is a flavour system, not a gate — the weird masks have no scripted purpose beyond being wearable and being noticed by one fortune-teller machine.

## Leads not chased

- Component-category hashes that resolve against neither `Codex.Games.RDR2.strings.txt` nor a 532k-entry vocabulary built from the corpus's own string literals: `-134124598`, `494009478`, `2071466316`, `-1968556728`, `-1455751347`, `43391475`, `149557334`, `1522539835`, `694822476`, `-1033766886`, `81053684`. (`-2061583405` = hats and `-525676072` = masks are known by usage, not by name.) Cracking them needs the item-database / metaped metadata, not the script corpus.
- The `FTELL_*` **subtitle text** itself lives in the localised speech DB (the user's `WayJaCA_0x22639BA2` entry). Enumerating every reading per category is a text-DB job — the Explorer's new Subtitle Search is the right tool.
- Per-mask NPC speech variation, if any, is in the audio speech layer (`speech2.dat14`) — partially decoded (readout not published in this repo).

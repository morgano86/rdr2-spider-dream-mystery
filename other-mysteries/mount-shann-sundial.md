# The Mount Shann Sundial (a separate mystery)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**What this file is.** A documented file on the **Mount Shann "giant sundial"** and the surrounding **Kuhkowaba cult / UFO Easter egg** in RDR2 - a *different* mystery from the Spider Dream, opened here at the investigator's request (2026-07-02) because it is a live puzzle in its own right **and** because it shares two hooks with our corpus: the **GTA V Mount Chiliad** homage (which the spider-web thread already leans on, [K24]) and **~2 AM time-gating**.

> ⚠️ **Read the boundary first.** This is a **separate Easter egg with NO verified connection to the Spider Dream Mystery.** The investigator is explicit: *"I don't think it's directly related… but there could be some crossover."* Everything below that touches the spider trail is held at [SPECULATION] ([S33]) or logged as the open crossover question [U34]. The verified spider frontier is still the Fort Wallace birds ([K16]) - nothing here moves it.

---

## The sundial, at a glance

On one of **Mount Shann's** peaks (Big Valley, West Elizabeth) sits a **ring of stones** with a central upright - a **sundial**, identified as such only because the official RDR2 guide names it. Seven of the ring stones carry **painted arrows**, colour-coded **red / orange / yellow**, most of them snow-covered or nearly imperceptible. The peak also hosts a **~2 AM UFO** apparition tied to the *Mysterious Sermon* found at Hani's Bethel.

---

## [KNOWN]

- **[K35] Mount Shann is a traversable peak in Big Valley, West Elizabeth, NW of Strawberry; a "giant sundial" (stone circle) sits on one of its peaks.** The wiki states the sundial "appears to be modeled after a Japanese archeological site called the **Ōyu Stone Circles**"; the mountain itself is modelled on **Mount Shasta** (N. California) / possibly **Mount Elbert** (Colorado). Also on the mountain (SE, near the trail): **Giant Remains** and a **Rock Carving** coordinate marker (one of the Francis Sinclair "Geology for Beginners" carvings - [Francis Sinclair egg](francis-sinclair-mural.md)). *(B-tier: [Red Dead Wiki - Mount Shann](https://reddead.fandom.com/wiki/Mount_Shann), via MediaWiki API 2026-07-02.)*

- **[K36] The sundial bears 7 painted arrows on its ring stones, colour-coded red / orange / yellow, deliberately obscured.** The arrows and their painted textures **exist in-game** and are visible on the stones (snow-covered; some perceptible only on close inspection) - **firsthand investigator observation (investigator, 2026-07-02), A-tier in-game.** The datamined model `dis_bgv_sundial.ydr` (extracted via **CodeX**, texture on file) is used here only to **show the arrows cleanly with the snow removed**, confirming the count and colours - **3 orange · 3 red · 1 yellow** - and that they are a **deliberate painted asset, not pareidolia or lighting.** The `dis_bgv_` ("Big Valley") name prefix is Rockstar's own. *(Arrow existence/colours: A-tier in-game, snow-stripped by the datamine. Their bearings/times are also firsthand in-game observation - see [U33].)*

- **[K37] The Mount Shann peak has a ~2 AM UFO apparition, foreshadowed by the "Mysterious Sermon."** Visiting the peak at approximately **2 A.M.** causes a **UFO** to appear and, after a short while, ascend and vanish. This is the **second** of the game's two UFO sightings; the first is at **Hani's Bethel** (The Heartlands, NE of Heartland Overflow), an abandoned cabin holding **~11 cultist corpses** (a documented **Heaven's Gate** allusion - same boots) and the ***Mysterious Sermon*** letter. The sermon's **first line** ("AT THE SECOND HOUR UNDER THE HALF MOON") gates the 2 AM timing; its **seventh line** - *"WHEN WE WILL RETURN FOR THE NEW CHOSEN AND WORSHIP ONCE AGAIN AT THE PEAK OF MOUNT SHANN"* - names the sundial peak. The cult worships **"KUHKOWABA, VOYAGER OF TIME AND GALAXIES."** *(B-tier: [Red Dead Wiki - Mount Shann](https://reddead.fandom.com/wiki/Mount_Shann), [Hani's Bethel](https://reddead.fandom.com/wiki/Hani%27s_Bethel), [Mysterious Sermon](https://reddead.fandom.com/wiki/Mysterious_Sermon); the sermon text is A-tier in-game.)*

- **[K38] The Mount Shann mysteries are, per the wiki, an explicit nod to GTA V's Mount Chiliad.** The wiki's own Trivia: *"The various mysterious landmarks and the UFO present at this location are a nod to Mount Chiliad from Grand Theft Auto V… which similarly features a UFO and some strange murals."* This matters to **our** corpus because the spider-web thread **already** ties to Mount Chiliad from the other direction - GTA V's Chiliad cable-car webs share RDR2's cable shader and 1–2 AM gate ([K24]). So **two independent RDR2 eggs point at the same GTA V node.** *(B-tier wiki trivia; the Chiliad↔web link is [K24].)*
- **[K54] The UFO mechanics are script-decoded; the "half moon" is not a trigger.** The Shann UFO needs **hour 01:00–02:59** + within **14 m of the summit** + a once-per-in-game-day cooldown (`town_secrets_strawberry.ysc`); the Hani's Bethel UFO needs only **00:00–03:59** + the shack volume; **no moon/lunar native exists** anywhere in the script corpus, so the sermon's "HALF MOON" line is flavour and **[K37]'s "~2 AM" is really the 01:00–02:59 window**. No third UFO exists. *(B-tier, [#91](../sources/sources.md); full detail in [known-facts.md](../findings/known-facts.md).)*

---

## [UNKNOWN]

- **[U33] What do the 7 arrows encode, and is the colour-coding meaningful?** Documented behaviour is thin: sources say **one arrow points toward the abandoned cult hut**, some **lead to spots with collectible stones**, and **others "appear to point to nowhere."** The **shadow↔arrow alignment is itself a firsthand in-game observation, cross-checked over two full day/night cycles** (investigator, 2026-07-02; high-trust investigator data - the investigator watched the gnomon's shadow fall along each arrow at these times, noting exact times may not be perfectly precise): each arrow maps to a **sundial shadow time + cardinal bearing**:

  | Colour | Time | Cardinal |
  |--------|------|----------|
  | Red | 6:00 am | W |
  | Orange | 9:00 am | WNW |
  | **Yellow** | **11:30 am** | NNW |
  | Orange | 1:00 pm | N |
  | Red | 2:00 pm | NNE |
  | Orange | 3:00 pm | ENE |
  | Red | 6:00 pm | E |

  So the arrows **do** function as a gnomon-shadow clock (observed) - that much is answered. What stays open is whether that clock is **also** a pointer layer (some arrows are documented to lead to **collectible stones / the cult hut**) or whether the alignment is just faithful sundial set-dressing. Is the colour a **three-value key** (red/orange/yellow) or just a warm-to-cool shadow gradient? The investigator's structural observations sharpen it: the arrows cover only the **daytime half** (roughly 6 am–6 pm; sunset ~8 pm leaves the "night" half unmarked), and **yellow appears exactly once**, uniquely on a **half-hour** (11:30 am) - a candidate "special" marker. *The alignment is firsthand-observed; whether it encodes anything beyond timekeeping needs testing before promotion.*

  **⚡ DECODE BRANCH CLOSED-NEGATIVE (desk, 2026-07-02 - [`sundial_decode.py`](../experiments/sundial_decode.py), [results](../experiments/results/sundial_decode.md)).** A systematic battery with exhaustive permutation nulls finds: **(1)** the arrows are a **physically faithful shadow clock** - all 7 bearings in the northern semicircle, monotone with time (p≈0.0014), fitting a standard solar model at p≈0.0004 (residuals inside the stated ±45 min observation slack) - so **bearing ≡ f(time)**: an arrow *cannot* be freely "aimed" at a POI, and any pointer layer could only be the **choice of times**; **(2)** the times-as-numbers/letters channel is **null** (A1Z26 24h `FIKMNOR`, 12h `FIKABCF`; "INFORM" discards the K - the Gertrude-`FROG` trap); **(3)** the colour channel's one exact structure - **each orange time is the midpoint of a red time and noon** ((r+12)/2: 6→9, 14→13, 18→15; p≈0.014 uncorrected, ~0.07 with look-elsewhere) - reads as a **major-tick / half-tick decorative grammar**, with **yellow ≈ the noon marker** (nearest the best-fit solar-noon shadow), *not* a cipher key. **What stays open in [U33] is only the in-game POI question** (do the documented cult-hut / collectible-stone alignments hold, i.e. were the *times chosen* to select targets?) - an in-game/mapping task, coordinate-blocked at the desk.

- **[U34] Is the Mount Shann sundial/UFO egg connected to the Spider Dream Mystery, or only via the shared Mount Chiliad homage?** The only *sourced* bridge is [K38]+[K24] (both eggs nod to GTA V Chiliad) plus a **shared ~2 AM time-gate** ([K11] centre webs 1–2 AM; [K37] UFO at 2 AM). No source links the sundial to the spider trail directly. Held open, **skeptical** - most likely two independent Rockstar "mountain + UFO/mural + time-gate" eggs, not one puzzle.
- **[U42] Why is `dis_roa_aliencave_int` furnished but never placed?** A Roanoke MLO interior with no placement and no script reference - likely cut content on the UFO side; no spider tie. See [unknowns.md](../findings/unknowns.md). ([#91](../sources/sources.md))

---

## [SPECULATION]

- **[S32] The arrows' deliberate obfuscation + tri-colour coding may be a purposeful puzzle layer (investigator).** The investigator's read: the snow-cover and near-invisibility of several arrows is **intentional Rockstar obfuscation**, marking the sundial as part of a **wider unsolved puzzle**, with the lone **yellow / 11:30 am** arrow as a deliberate outlier. This *stylistically* rhymes with the spider mystery's signature - **deliberately near-invisible, time-gated clues** ([H13]) - but a shared *style* across Rockstar eggs is not a shared *puzzle*. Recorded as the investigator's interpretation (2026-07-02); **not promoted.** ⚠️ Deflationary counter: some arrows are documented to just point at **collectible stones / the cult hut**, i.e. ordinary in-world signposting, and warm-hued arrows on a sundial may simply be a shadow-hour gradient. **The counter is now quantified (2026-07-02, [`sundial_decode.py`](../experiments/sundial_decode.py)):** "faithful shadow clock + decorative tick hierarchy" fits at p≈10⁻³–10⁻⁴ while every tested encoding channel lands null or look-elsewhere-weak; the colours resolve into a major/half-tick grammar (oranges = red↔noon midpoints, yellow ≈ noon), which *is* the shadow-hour-gradient reading made precise. [S32]'s puzzle-layer form survives only via the untested in-game POI question ([U33]).

- **[S33] Crossover-via-Chiliad: the sundial and the spider webs may be siblings under Rockstar's recurring "sacred mountain" template, not directly linked.** Both tie to **GTA V Mount Chiliad** (UFO + murals + time-gate): the webs by shader/hour ([K24]), Mount Shann by explicit wiki-stated homage ([K38]); both use **~2 AM** gating. The likeliest reading is a **reused motif family** (mountain peak · UFO/mural · specific-hour reveal) that Rockstar carries between titles - which would explain the resemblance **without** a solvable in-RDR2 link between the two eggs. A prompt to watch the crossover ([U34]), not evidence of one. ⚠️ Weak; the palettes even differ (webs black/red feathers vs sundial red/orange/yellow arrows).

---

## Numeric coincidence worth a note (not overweighted)

The *Mysterious Sermon* has **7 substantive lines** (plus a closing benediction), and its **7th** names Mount Shann; the sundial has **7 arrows**. Cute, and Rockstar does play with counts, but with no mechanism tying line-7 to arrow-7 this is **pattern-spotting**, logged for completeness only - the same discipline applied to the spider mystery's "8 / 4 AM" number motif ([S20]).

---

*Cross-refs: [K24]/[gta-rdr2-crossover.md](gta-rdr2-crossover.md) (the spider↔GTA V Chiliad link this shares), [K11] (spider centre webs, 1–2 AM), [H13]/[carving-technique.md](../analysis/carving-technique.md) (the "near-invisible, time-gated" signature [S32] echoes), [Francis Sinclair egg](francis-sinclair-mural.md) (the Rock Carving on the same mountain), [S20] (the corpus's number-motif discipline). Location dossier: [other-mysteries/mount-shann-sundial.md](mount-shann-sundial.md). Registry rows: [INDEX.md](../INDEX.md). Rollups: [known-facts](../findings/known-facts.md) · [unknowns](../findings/unknowns.md) · [speculation](../findings/speculation.md).* 
---

## Location dossier - Mount Shann
- **Region:** **Big Valley**, Commonwealth of **West Elizabeth** - roughly the centre of the region, **NW of Strawberry**. A large traversable mountain (RDR2 + Red Dead Online).
- **Real-world model:** the mountain after **Mount Shasta** (N. California) / possibly **Mount Elbert** (Colorado); the summit **sundial** after Japan's **Ōyu Stone Circles**. ("Shan" 山 = "mountain" in Chinese.)
- **Type:** mountain peak hosting a **stone-circle "giant sundial"** and a **~2 AM UFO** apparition.

### Mystery role - a *separate* egg (see [Mount Shann egg](mount-shann-sundial.md))
This is **not** part of the Spider Dream Mystery. It is the **Kuhkowaba cult / UFO** Easter egg, logged at the investigator's request (2026-07-02) for its own sake and for two crossover hooks (below). The verified spider frontier is unchanged ([K16]).

- **The sundial ([K35]/[K36]):** a ring of stones with a central upright on one peak; **7 painted arrows** on the ring stones (visible **in-game**, firsthand), colour-coded **red / orange / yellow** (3 red · 3 orange · 1 yellow), most snow-covered / near-invisible. The datamined model `dis_bgv_sundial.ydr` (CodeX extraction on file) is used only to **show the arrows snow-free**, confirming count/colour and that they are a deliberate painted asset. The investigator observed each arrow aligning with the **gnomon's shadow** at a set time/cardinal, cross-checked over two day/night cycles ([U33]).
- **The UFO ([K37]):** appears at the peak at **~2 AM**, then ascends and vanishes; foreshadowed by the **Mysterious Sermon** at **Hani's Bethel** (The Heartlands), whose 7th line names *"THE PEAK OF MOUNT SHANN."* Same egg family as the Hani's Bethel UFO + the ~11 cultist corpses (a Heaven's Gate allusion).
- **On the same mountain (SE, near the trail):** **Giant Remains** and a **Rock Carving** coordinate - the latter is one of the ten Francis Sinclair "Geology for Beginners" carvings ([Francis Sinclair egg](francis-sinclair-mural.md)), so Mount Shann geographically touches a *third* egg.

### Crossover hooks (held at [SPECULATION] / open)
- **Mount Chiliad ([K38] + [K24]):** the wiki calls Mount Shann's landmarks + UFO an explicit **nod to GTA V's Mount Chiliad** (UFO + murals). The spider-web thread already ties to Chiliad from the other side ([K24], shared cable shader + 1–2 AM gate) - so two RDR2 eggs point at the same GTA V node ([S33]).
- **~2 AM time-gate:** the UFO ([K37]) and the spider **centre webs** ([K11]) both key to the small hours (2 AM / 1–2 AM).
- **Style ([S32]):** the arrows' deliberate obfuscation echoes the spider mystery's near-invisible, time-gated clue signature ([H13]) - a shared *style*, not a proven shared *puzzle*. Whether any real link exists is the open [U34].

### Open questions
- **[U33]** What do the 7 arrows encode? (Some → collectible stones; one → the cult hut; others → "nowhere." Is the colour a 3-value key? The investigator's shadow-time/cardinal table is in [Mount Shann egg](mount-shann-sundial.md).)
- **[U34]** Is any of this connected to the Spider Dream Mystery, or only via the shared Chiliad homage? (Skeptical.)

### Images
- [`../images/mount-shann/mount-shann_sundial_ground-view.jpg`](../images/mount-shann/mount-shann_sundial_ground-view.jpg) - the sundial from ground level (player + horse), snow-covered ring.
- [`../images/mount-shann/mount-shann_sundial_overhead.jpg`](../images/mount-shann/mount-shann_sundial_overhead.jpg) - top-down; radial stone layout + faint painted arrows.
- [`../images/mount-shann/mount-shann_sundial-arrows_codex-model.jpg`](../images/mount-shann/mount-shann_sundial-arrows_codex-model.jpg) - **CodeX** extraction of `dis_bgv_sundial.ydr`: the 7 red/orange/yellow arrows shown cleanly on the isolated model.

> Sources: Red Dead Wiki *Mount Shann*, *Hani's Bethel*, *Mysterious Sermon* (via MediaWiki API, 2026-07-02); GameRant "Mount Shann Mystery Explained." Arrow count/colours/bearings + the codex asset = firsthand investigator data (investigator, 2026-07-02). URLs in [sources](../sources/sources.md).
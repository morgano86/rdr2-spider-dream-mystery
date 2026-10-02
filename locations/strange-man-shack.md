# The Strange Man's shack - **Bayall Edge** (Bayou Nwa)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**Why this dossier exists:** [S35] proposes walking into this shack **with the red-group feather state live** (the southern twin of [H21]'s state-carry reading). To recognise *anything* state-gated on arrival, the field session needs a precise baseline of what the shack **canonically** does - every stock behaviour below is a thing the session must NOT mistake for a spider-mystery reaction. Corpus pass 2026-07-02, B-tier first (Red Dead Wiki *Bayall Edge* + *Strange Man* via MediaWiki API, Gameranx guide - source [#68](../sources/sources.md)).

## Geography - [KNOWN]
- Canonical name: **Bayall Edge** (the game's index misspells it "Baygall Edge"). A cabin in **Bayou Nwa, Lemoyne**, **northwest of Caliga Hall**, on a small peninsula curled into a small lake, near the railroad tracks (Gameranx: southwest of the "B" in "BAYOU" on the map).
- In both *RDR2* and *Red Dead Online*.
- **Spider-mystery geometry (firsthand, [K28]):** the investigator's boundary POI inventory lists the shack inside **both** the Middle/Connector *and* Bottom/South respawn boundaries - i.e. it sits in boundary **overlap**, like the whiskey tree ([S23]). *(Which exact boundary contains the door must be re-confirmed on arrival - control #6 of the field protocol.)*
- Note **Caliga Hall** - the `S+J` matchstick site ([K9]) - is its nearest named neighbour; the red webs' South boundary is the tied zone of `R23, R45, R34` ([K31]).

## The portrait mechanic (the state machine to compare against) - [KNOWN]
The centre of the room holds an **unfinished painting** that completes across **four unique visits**:
1. **As Arthur:** the painting is (and stays) unfinished.
2. **As John** (post-epilogue): it becomes "more and more complete **over the next few days**" across return visits.
3. **Fourth visit** - the portrait is **finished, revealing the Strange Man**. ~~Gate discrepancy between B-tier sources~~ **→ ADJUDICATED 2026-07-05 ([#84]): the gate is POST-EPILOGUE + 4 unique visits with multi-in-game-day spacing (as John) - NOT 100% completion.** Both-directions counterexamples on record (finished at **88%**, `llc7lq`; a 100%-without-portrait GameFAQs report); an OP-solve states it plainly (*"It just requires being in the epilogue… took several days of sleeping, saving and loading"*); the 100% claim traces to a **2018 correlation guess** (`9wuk1g` - 95–100% players have necessarily finished the epilogue + passed many days) propagated by Gameranx. *(Practical for [S35]: a post-epilogue <100% save predicts the portrait state from **prior visit count**, not completion %.)* Residual at [U35]: what exactly advances a stage (Arthur-era progression is disputed - wiki says John-only, two firsthand comments report per-chapter progression as Arthur). **⚡ STAGE MECHANIC SCRIPT-DECODED (2026-07-05, from the [#87] dump - `discoverable_easel.ysc.c`; decompiled, our reading):** the portrait is a **discoverable** (same system as the dreamcatchers, same `DiscoDisable`/bit-4 guard). The stage is a **savegame int `Global_40.f_8863.f_145` (0–3, clamped at 3)** selecting interior propsets `SK2_Painting_set_01–04` (`SK2` = the shack's internal codename, matching the beta *serial-killer* history). An advance fires only when **(a)** a pending-visit flag (`f_147`) is set, **(b)** **≥5 units of a packed saved date (`f_144`) have elapsed since the last advance - almost certainly in-game DAYS** (refines "multi-day spacing" to a number; matches the "several days of sleeping" OP-solve), and **(c)** for the later stages (stage ≥2) additionally **persistent progress bit 45** is set - the natural candidate for the post-epilogue gate [#84] adjudicated (bit identity unproven). A **John-only check** (`Global_40.f_39 == joaat("player_three")`) gates the flow, and the honor-reactive paintings are confirmed in code (honor sign → `SK2_Painting_high_moral`/`low_moral` swap). So: **stage = f(visits × ≥5-day spacing × late-stage progress bit), John-gated** - not a pure visit count, not days-alone, and nothing reads completion %. 🆕 **Two propsets no source on file documents:** `stranger_cryptic_lives` / `stranger_cryptic_dies` - an interior swap keyed to the state of **story-mission registry entry 6 (`mudtown3`/MUD3)** plus a saved state bit; referent unresolved (a distinct channel from the Jimmy-Brooks limerick below) - a cheap 🎮 watch-item for any shack visit.
4. **Mirror apparition:** with the portrait complete, looking in the **mirror to the left of the painting** shows the Strange Man **standing behind you**; he vanishes if you turn around or try to photograph/screenshot him. He appears **only** in the mirror.
5. **Terminal state:** on visits after the fourth, the portrait **has disappeared** - along with all the honor-reactive paintings (below). "After a few days pass, the painting will disappear" (Gameranx). **The egg is consumable.**
6. Examining the finished picture (4th visit) awards the **"Painting in Cabin"** point of interest - **the only POI in the game discoverable solely by John** (Arthur has a *cut* drawing + journal entry for it). John's journal sketch: *"This place made me feel like I was being watched. Queerest feeling I ever felt. Hard to explain. Fascinating and awful and seductive, all at once."*

## Everything else the shack canonically watches - [KNOWN]
The shack is the game's densest **hidden-state reader**. Stock reactive channels:
| Channel | State read | Behaviour |
|---------|-----------|-----------|
| Animal paintings around the room | **Current honor** (live) | High honor → **eagles and bucks**; low honor → **vultures and coyotes**; they "constantly change depending on the player's current honor level" |
| Nightstand limerick | **Past choice** (Jimmy Brooks, Chapter 1 train) | Spared → "…That Jimmy isn't as dumb as he looks"; killed → "…Now Jimmy's family don't see him very much" |
| Central portrait | **Story epoch + visit count** | Arthur = frozen unfinished; John = progresses per visit/days; see the state machine above |
| Mirror | **Portrait completion** | Apparition only once the portrait is done |

## Fixed interior/lore inventory (non-reactive baseline) - [KNOWN]
- Facade derelict; interior dark and curated: paintings on the floor, a long table with candles, a **stuffed crow** on a podium; a caged **rotting alligator corpse** under the house.
- **Six wall messages** (verbatim, wiki): **I KNOW YOU** · **THE MOON WILL SHINE ON IN THE DARKNESS** · **THE WATER IS BLACK WITH VENOM** · **HIS FINAL TOLL WILL SOUND MY GREATEST COMING** · **FROM THE SNOW TO THE CAVE** · **I GAVE TOO MUCH FOR ART AND I LEARNED TOO MUCH AND NOTHING AT ALL**.
- A map of **Armadillo** by the mirror captioned *"I offered you happiness or two generations, you made your choice"* (the Herbert Moon deal; Moon hangs a small copy of the Strange Man portrait in his Armadillo store, which John recognises).
- **Beta history:** the shack belonged to a **serial killer** in cut content - Social Club photos taken here are location-tagged "**Serial Killer**", and the LOD model shows the pre-remodel look. *(Deflationary context: some of the shack's weirdness is remodel residue, not current design.)*
- **Flora:** Gator Eggs, **Lady of the Night Orchid**, and the **Spider Orchid** grow in/around Bayall Edge (wiki).
- The NPC: the **Strange Man** (*"I'm an accountant… in a way"*), the franchise's supernatural honor-auditor (RDR1's *I Know You* strand tests John with moral choices; bullets pass through him). Internal model name **`cs_mysteriousstranger`**.

## Relevance to the spider mystery - [SPECULATION], stated honestly
- **No source connects Bayall Edge to the webs/feathers.** The link is entirely our [S35] geometry+mechanics argument (in-boundary-overlap POI + the game's one hidden-state reader). Nothing here moves the [K16] frontier.
- Resonances worth logging, not weighing: the **Spider Orchid** at the doorstep; *"THE WATER IS BLACK WITH VENOM"* (venom - the wiki itself floats a **Butcher Creek** curse association, the mystery's 2018 origin site); the honor channel is exactly where [H5]'s colour↔honor hunch would surface; and a crow, not a raven, watches the room.
- **Tension unchanged:** under [H24] the reds are decoys and the [S35] visit should produce a clean stock baseline - which is precisely why the session discriminates the rivals cheaply.

## Field checklist for the [S35] red-side session (record BEFORE and AFTER state goes live)
1. **Baseline visit first** (no feather state): photograph the portrait stage, all animal paintings, the limerick, the six wall messages, the mirror. Note honor level + story epoch (this fixes every stock channel).
2. Solve the **3 reds** (any internal order, [U29]), **stay inside the South boundary**, ride to the shack.
3. **At the door:** confirm which boundary the doorway physically sits in ([K28] control #6).
4. **Inside with state live:** re-photograph every channel from step 1 - the *diff* is the result. Check especially the mirror and the portrait (the two supernatural channels), then any new object/message.
5. Apply the **[H25] dream coda** before leaving the boundary: sleep/camp at or near the shack; watch the wake cycle.
6. **Log a null as a finding** - under [H24] a null here is *expected* and still discriminates.

## Open sub-questions
- **[U35]** - ~~which gate really controls the 4th visit/finished portrait~~ **MAIN QUESTION ADJUDICATED 2026-07-05 ([#84], dedicated research pass): post-epilogue + 4 spaced unique visits; the 100%-completion claim is a traced-and-contradicted 2018 community myth.** Still open (narrow residual): what exactly advances a stage - interior-entry count with a ~3-day cooldown (the game's standard refresh timer, per firsthand reports) vs pure days-elapsed - and whether **Arthur-era visits count** (sources genuinely disagree; one unverified 2018 anomaly even reports the mirror apparition as *Arthur*). Also logged: one report of finished-portrait-but-**no**-apparition (the mirror trigger is finicky - the [S35] session should **not** read a missing apparition as a spider-state signal). Settleable by the investigator's own save (4 visits spaced 3+ in-game days on a post-epilogue, <100% file). **Converse check 2026-07-05 → [K44]:** the 100%-completion system's only scripted consumer is the Arthur's-grave scene ([#87]) - completion never gates the easel from its side either; NOT-100% now holds in both directions.

*Sources: [#68](../sources/sources.md) (Red Dead Wiki "Bayall Edge" + "Strange Man" via MediaWiki API; Gameranx guide); [#84] (the 2026-07-05 gate adjudication cluster). Created 2026-07-02 for [S35]; see [analysis/decoy-and-dream-hypotheses.md §4](../analysis/decoy-and-dream-hypotheses.md).*

> **Portrait variant source (2026-10-02, [K58], [#95](../sources/sources.md)):** the `stranger_cryptic_lives` vs `stranger_cryptic_dies` interior set is chosen by bit 31 of the easel's discovery slot, which `mudtown3` sets on its kill-witness outcomes - i.e. a *cross-mission choice* (killing vs questioning the witness), not anything tied to the webs.

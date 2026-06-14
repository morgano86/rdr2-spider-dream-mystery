# STATUS — start here

The operational dashboard. **This is the single entry point each session**: where the case stands, what's blocked on
what, and what to do next. It holds *pointers and the live frontier*, not content — detail lives in the files it links.
Keep it short; when something changes here, also touch the canonical file and the [log](INVESTIGATION_LOG.md).

> **One-line status (2026-06-13):** **UNSOLVED — no confirmed reward/cutscene/unlock** (Jan 2026 coverage: *"no new loot,
> tools, or cutscenes"*). The community decoded the web-trail to **Fort Wallace** in late 2025; Fort Wallace is a
> **waypoint, not the end**. The **last VERIFIED clue is the Fort Wallace bird carvings** ([K16]); everything past them is
> unverified/contested — the off-map **"?" carving is NOT a widely accepted theory** (pareidolia), and the **Bacchus heart's
> relevance is about as contested as the "?"**. We work **forward from the bird carvings** unless new evidence lands. The egg
> is confirmed *real* by a former Rockstar QA tester ([K3](INDEX.md)), but authorship is unconfirmed.

- **Best one-paragraph understanding:** see [README.md](README.md#one-paragraph-summary-of-the-current-best-understanding).
- **Last verified clue / working frontier:** the **Fort Wallace bird carvings** ([K16]) → [thread 06](threads/06-bird-carving-giant-wapiti.md).
  Past them (Calumet / Giant / "?" / Bacchus heart) is **contested**, not the established trail.

---

## Top open questions (ranked)
Full set + IDs in [findings/unknowns.md](findings/unknowns.md). The ones that could break the case open:

| Rank | ID | Question | Best source |
|------|----|----------|-------------|
| 1 | [U29](findings/unknowns.md) | The **feather order mechanic** — group/boundary-based, not one sequence ([H9]/[K31]). **✅ The multi-night persistence crux is now ANSWERED ([K29], 2026-06-14): shot feathers persist ≥12 in-game days while in-boundary**, so multi-night solving ([H20]) is viable. **Still open:** the central-overlap **state-hold across a crossing** (tested negative-leaning), `B34`'s role, the red-feather function | 🌐 community testing / 🎮 |
| ~~2~~ | [U1](findings/unknowns.md) | ~~The **under-wood pole messages**, verbatim~~ **✅ RESOLVED 2026-06-14 → [K11]/[K12]:** chain multiply B-tier corroborated; **exactly 2 shot-poles, `NW`+guitar is the last, no 3rd documented**. Guitar *meaning* still open at [U12] | 🌐 done ([#60]) |
| 3 | [U3](findings/unknowns.md) | **One puzzle or two?** New traction ([S22]/[H21]/[K31]): the top boundary holds **both** 2018-origin nodes (Butcher Creek + Fort Brennand) and the web shot-state persists into them ([K29]) — a *mechanical* link, not just thematic | 🧠 analysis / 🎮 |
| 4 | [U14](findings/unknowns.md) | **Window Rock mural** birds **by colour** — is it 5 black / 3 red (the order key, [H3])? Also now read as a mechanic-**seed** ([H18]): its solve-rule (count a feature, **exclude decoys**) argues **colour is a filter**, reinforcing the [H9]/[U29] group reading | 🌐 mural images we hold (hi-res extract now on file) |
| 5 | [U2](findings/unknowns.md) | Is there an **intended payoff at all**, or is it cut content? | 🌐 new coverage / community |

> **Note (2026-06-14):** [U22] (exact web↔boundary membership) is **RESOLVED → [K31]** (firsthand: the [H9] partition is
> confirmed; boundaries overlap) — it leaves the top-5 as a closed question.

> **Note (2026-06-13):** [U0] (feather position/orientation) — long the #1 item — is **resolved on orientation**: the full
> 8-web photo set ([#59]) shows every feather **hangs tip-down by gravity**, so **[H4] is refuted** and the order is **not**
> feather-encoded. What was "the order key" question now lives at **[U29]** (group-based mechanic). Only the weak per-web
> *attachment point* survives under [U0].

> **Note (2026-06-13):** [U6] (Gertrude's numbers) sits just off the top-5. Its opening `1237645112` is now **sourced and
> confirmed deliberate** (RDR2-original, Rockstar-echoed cross-game via Nazar, [K23]) — but its **link to the spider trail
> specifically is undecided**, so it ranks below the four trail-direct items above. Tracked in
> [analysis/gta-rdr2-crossover.md](analysis/gta-rdr2-crossover.md).

---

## Next actions, by channel
**Default to web sourcing + verification.** Most open questions are already documented in the wiki, community sites,
forum threads, or the Strange Man video — find the evidence and corroborate it. Reserve in-game capture for detail no
online source records (in practice, only the feather *orientation*).

### 🌐 Web / video sourcing (the default) → [EVIDENCE-CHECKLIST.md](EVIDENCE-CHECKLIST.md)
The actionable worklist, ordered by value. Headline items: the **under-wood pole messages** (U1, in community videos),
**Gertrude's full sequence** (U6, transcribed in late-2025 videos), the **Window Rock mural birds by colour** (H3/U14),
and **feather orientation** (U0) — pull from video frames first.
- Build the RDR2 **character/credits name list** to test `LJ`/`SM`/`J+M` ([U4](findings/unknowns.md), [U16](findings/unknowns.md)).

### 🎮 In-game (only when strictly necessary)
Used only where the web genuinely comes up empty: confirming **feather orientation** (U0) if video frames don't resolve
it, and the long-horizon **H8 test** (does completing the trail clear the dreamcatcher log?). **[U26] map-grid: DONE
2026-06-13** — investigator captured two in-game prop-map grids ([K26]; Map 1 = 1–30 × A–U, Map 2 = A–O × 1–7); the per-cell
reading tested **negative-leaning** ([`number_grid.py`](experiments/number_grid.py): Map 2 admits only `EC`). [H14] survives
only as a free coordinate plot.

### 🧠 Analysis (desk work, no sourcing needed)
From [analysis/connections.md](analysis/connections.md#open-analysis-tasks):
- Test Gertrude attempt B (read the 7 tally nodes in her number order) once U6 lands.
- Re-pair the letters `{C,E,J,J,J,L,M,M,S,S}`; test the dev-initials-down hypothesis against the name list.
- Decide [U3](findings/unknowns.md): is this one layered puzzle or two parallel eggs?
- **[U22] DONE → [K31]** (2026-06-14): the 3-boundary partition is firsthand-confirmed and the boundaries overlap. Live
  follow-on: does shooting a *contained-but-untied* web (wrong-boundary despawn) break a run? And **[U30]** — does a hit count
  whenever the feather is shot while visible, or only during its specific spawn hour? (untestable without the solution order).

> **🧮 When reasoning isn't enough** (combinations, ciphers, geometry, coincidence odds), write a quick Python test in
> [`experiments/`](experiments/) — e.g. [`feather_order.py`](experiments/feather_order.py). Results are evidence, not
> fact; log null results too.

---

## Recently added (2026-06-14)
- **[U1] RESOLVED — under-pole inscription chain multiply corroborated + bounded (deep-research [#60]).** A fan-out/verify pass
  (15 sources, 25 claims adversarially verified) confirmed the verbatim chain that was **single-sourced** before: centre
  `N`+telephone-pole (an **alignment** reveal, 1–2 AM, [K11]) → north pole `W ✞✞✞✞✞` (**five** glyphs, unanimous across 6+
  B-tier outlets) → fifth pole west `NW`+guitar-**like** symbol ([K12]; identity hedged by *every* source — a flat "it IS a
  guitar" claim was refuted 0-3, keeps [U12] open). **Bounded negative:** these are the **only two shot-to-reveal poles**; the
  `NW`+guitar pole is the **last documented under-pole message** — **no third is documented anywhere**; content "past" Fort
  Wallace is the [K16] bird carvings or out-of-bounds pareidolia, *not* under-pole text (holds the verified-trail boundary).
  Also: "bird carvings confirmed intentional via datamine" **refuted 0-3** (consistent with the [K3] Butterworth walk-back).
  Propagated: K12 (known-facts, INDEX), U1 RESOLVED + U12 strengthened (unknowns, INDEX), thread 05 ([KNOWN] note + [UNKNOWN]
  struck + sources), source [#60], [log](INVESTIGATION_LOG.md) top.
- **Boundary membership confirmed + feather persistence + render-gating (firsthand investigator data).** Major mechanic pass:
  (1) **[K31]** web↔boundary membership **firsthand-confirmed** (Top `B34` / Connector `B23,B45,B56,B56L` / South `R23,R45,R34`)
  → **resolves [U22]** and confirms **[H9]**; boundaries **overlap**, so each also contains *untied* adjacent webs (shooting them
  fires the wrong despawn). (2) **[K29]** shot-feather state **persists across nights + camping for ≥12 in-game days while
  in-boundary** (exact floor position stored/restored; resets only on boundary exit) → **answers the [U29]/[H20] persistence
  crux: yes, within-boundary** — multi-night solving is viable. The central-overlap *state-hold across a crossing* tested
  **negative-leaning**. Fallen-feather position is pure shot-physics (encodes nothing). (3) **[K30]** webs/feathers are
  **render-gated**: won't spawn while you look at the spot (look away/back), won't despawn while kept in line of sight — so you
  can **hold a web rendered past its hour by keeping it in view as you approach**. (4) **[U30]** new open question: does a hit
  count whenever the feather is shot *while visible*, or only during its *spawn hour*? (untestable without the solution).
  (5) ⚠️ **[K28] corrected:** **Fort Brennand is inside** the top boundary (not outside) — so both 2018-origin nodes (BC + Fort
  Brennand) sit in the top zone (strengthens [S22]/[H21]/[U3]); only Fort Wallace is outside. (6) **[S23]** anomalous red-hue
  fire-pit motif (BC pentagram = Fort Brennand pit = the new **[whiskey-tree](locations/whiskey-tree.md)** pit, the lone POI in
  the triple overlap). Propagated: K28–K31/S23/U30 (INDEX, known-facts, speculation, unknowns), H9/H20/S22/H21 (speculation),
  connections §5a, WEBS-MANIFEST, locations (whiskey-tree new + README + fort-brennand + butcher-creek), [log](INVESTIGATION_LOG.md) top.
- **Solve-attempt pass — colour×hour lattice, mural-as-seed ([H18]), + CLAUDE.md anti-speculation guardrail.** (1) **CLAUDE.md
  now codifies the verified-trail boundary** (new section): the **Fort Wallace bird carvings [K16] are the last verified clue**;
  the **"?" is pareidolia, not accepted**; the **Bacchus heart's relevance is as contested as the "?"**; **a user repeating a
  downstream theory is not sourcing it.** Work forward from the birds. (2) **Timings — new [KNOWN] structure:** the **colour×hour
  lattice** (re-tabulation of [K13a]) — each 2/3/4 AM hour carries **1 black + 1 red**, 5–6 AM carries **2 blacks** (`B56`/`BL56`
  = the [K13b] interchangeable pair, because they collide on the hour); each red is **hour-twinned** to a black. (3) **[H18]
  (mural-as-seed):** the Window Rock Strange Statues mural is solved by *counting a feature while **excluding decoys** (upside-down
  birds)* — read as RDR2 design grammar (family of [H6]/[H15]) its lesson is **appearance = a per-element FILTER, not a heading.**
  The per-web count doesn't transfer (one feather/web), but the filter lesson does and **cuts against [H4]**: orientation is
  uniform → the filter falls to **colour** → red/black = the include/exclude partition, which [H9]/[U29] already show. **Three
  lines converge on colour/group** vs a feather sequence ([H4]/[H17] dead). (4) Experiment
  [`web_colour_group_order.py`](experiments/web_colour_group_order.py): [U29] rules collapse 8! → **180** orders ("`B34` last");
  the colour-group order is **consistent** (not singled out). ⚠️ **[H18] is precedent/intent only — not evidence the mural and
  webs are one puzzle, not a confirmed key.** Propagated: H18 (INDEX, speculation, connections §5c, thread 06), lattice
  (WEBS-MANIFEST), [log](INVESTIGATION_LOG.md) top.
- **[U0] socket gap CLOSED FROM IMAGES ([H19]).** Re-read each feather's socket **against the web's own central radial**
  (camera-invariant) → `L/C/R` for all 8, **agreeing 8/8** with the old screen-relative reads (the confound never flipped the
  gross call → socket is a usable weak signal). Tested ([`web_socket_position.py`](experiments/web_socket_position.py)):
  **colour↔side NOT significant** (reds-right lean p=0.125); the only crisp pattern is the **3 hour-twinned blacks sweeping
  `L→C→R`** with the clock (p≈0.04) + the **5–6 AM pair B56/BL56 sharing hour AND socket** (reinforces [K13b]). **Reds do NOT
  reproduce the black time-sweep** (their sockets are C/R only, never left). Net: weak colour-axis line ([H9]/[U29]/[H18]); does
  **not** revive [H4] (socket ≠ orientation). Propagated: H19 (INDEX, speculation, connections §5d), U0 (INDEX, unknowns,
  WEBS-MANIFEST, feather-positions README), [log](INVESTIGATION_LOG.md) top.
- **Boundary geometry [K28] + the multi-night reading [H20] (firsthand investigator data, 2026-06-14).** The 3 [K21] boundaries
  form an **I-beam**: North E–W, South E–W, Connector N–S spine, **overlapping near centre** (overlap excludes the central web).
  Combined with the colour×hour lattice (each hour = 1 black + 1 red) and feasibility (**black+red in one night impossible
  solo**; all-black hard-but-doable incl. doubled 5–6; all-red very hard), this forces a **multi-night, one-colour-group-per-night**
  solve — likely **all 8 across nights, not one sequence.** Makes **persistence across nights** the decisive [U29] crux (and the
  central overlap a candidate state-holding mechanism). Propagated: K28 (INDEX, known-facts), H20 (INDEX, speculation,
  connections §5a), U29 (unknowns, STATUS), WEBS-MANIFEST, [log](INVESTIGATION_LOG.md) top.
- **B34's OVERSIZED boundary → candidate payoff location ([S22]/[H21], investigator data + user speculation, 2026-06-14).**
  B34's North zone uniquely includes **Butcher Creek** + Valentine (forts excluded) — echoing the [K8] Butcher Creek→Cornwall
  pointer → "one puzzle" argument ([U3]). Since shot-state persists only *inside* a boundary ([K21]), the oversize may be a
  **state-carry corridor**: successful web activation could unlock a **state-gated result at Butcher Creek (or Valentine)**,
  which would **explain the missing payoff** ([U2]) as a rarely-met precondition and **dovetails with the [U2] "flags checked
  but never set" datamine lead.** ⚠️ No payoff ever confirmed — [SPECULATION], not a destination. Propagated: S22/H21 (INDEX,
  speculation, known-facts §K28), U3/U2 (unknowns), connections §5a, [log](INVESTIGATION_LOG.md) top.

## Recently added (2026-06-13)
- **Solve-attempt pass — feather ORDER deflated and feather ORIENTATION resolved.** (1) **[U0] orientation is settled:** the
  full 8-web front+side photo set (u/dropthepress, [#59] → [`feather-positions/`](images/webs/feather-positions/README.md))
  shows **every feather hangs tip-down by gravity** → **[H4] refuted** (orientation is *not* a heading to the next web). (2)
  **The order mechanic is group-based, not a sequence ([U29]):** sourced brute-force testing ([#36]) shows reds work in *any*
  internal order (incl. non-chronological `R34→R45→R23`), mixed chains work, and `B34`/Cornwall is special (suspected **last**
  feather; "unique red-feather function"). (3) I proposed **[H17]** ("order = the clock," since the [K13b] chain is exactly
  chronological — [`web_time_order.py`](experiments/web_time_order.py)) and then **refuted its strict form** with that red data —
  the order collapses onto the **[H9] boundary partition**, not the clock. **Net:** the "secret feather-encoded sequence"
  reading is doubly dead; the live frontier for the order is `B34`'s role + the red function + time-lock-vs-persistence ([U29]).
  Also filed 5 investigator-supplied extracted symbol assets (spider etching, NW-guitar, W-5-poles, hi-res Window Rock mural).
- **Saint Denis Vampire added as a shipped pentagram-mapping precedent ([K27]) + difficulty-curve framing ([H15]/[H16], user
  lead).** New dossier [analysis/saint-denis-vampire.md](analysis/saint-denis-vampire.md). The Vampire egg runs the **identical
  mechanic as the Butcher Creek pentagram** ([K5]) — *find 5 fixed points → they form a pentagram → go to the centre* — but is
  **fully journal-assisted** (the game **draws the pentagram and marks the centre** with an "x"; encounter 12–1 AM; reward =
  Ornate Dagger; documented in the **in-game journal**, unlike the spider mystery's total lack of tracking [K20]). So it's the
  game's **tutorial / "seed"** for the technique ([H15], stronger-on-shape sibling of the dreamcatcher precedent [H6]). The
  user's broader read — the whole chain is an **escalating difficulty curve** whose **clue form mutates** (tallies → carvings →
  no-overlay engraving-as-map → directional glyphs → guitars-as-pointers → the ambiguous, unsolved bird carving [K16]) — is
  logged as **[H16]**; it **reframes [U2]** (the cold frontier is *expected* of such a curve, so it doesn't decide
  buried-continuation vs cut-content). Propagated: K27/H15/H16 (INDEX, known-facts, speculation), thread 02, connections §4,
  dreamcatchers.md, source #58 + `vampire_api.json`, [log](INVESTIGATION_LOG.md) top.
- **In-game map grid CAPTURED → grid-cell reading deflated ([K26], investigator data).** The [U26] capture landed: the
  investigator photographed **two *"Railroad & State Map"* prop maps** at a stranger's camp, each with a printed
  letter/number coordinate grid — **Map 1** cols 1–30 × rows A–U (30×21, continental); **Map 2** cols A–O × rows 1–7 (15×7,
  drawn over the playable world). So RDR2 *does* render in-game map grids ([K26]) — the old web-negative is superseded. **But
  the per-cell reading of the markings tests negative-leaning** ([`number_grid.py`](experiments/number_grid.py) re-run): on the
  game-world grid (Map 2) **only `EC` is in range** (`E3`/`C5`); `LJ`/`SM`/`J+M`/`S+J` all exceed the 7-row cap; no single grid
  validates all five. **[U26]** moves from "🎮 pending" to **deflated**; **[H14]** survives only as a free coordinate plot
  (precedent [K25]). Propagated: K26 (INDEX/known-facts), U26/H14 reframed, connections §1a(d), `number_grid.py` (both grids +
  re-run), images/maps provenance, [log](INVESTIGATION_LOG.md) top.
- **Loading-screen coordinate system → a coordinate reading of the letters/numbers ([K25]/[H14], user lead).** RDR2 hides a
  documented **letter=latitude / number=longitude** coordinate device: the **loading-screen photographs** encode locations as
  *obfuscated* lat/long (letters disguised as digits `O`→`0`, `Q`→`2`, `7`~`4`) on the in-game **fast-travel / Central Union
  Railroad** map grid — community decode (BlueVelvetFrank, r/reddeadredemption, ~3.7k upvotes, Feb 2019; C-tier, but the
  annotations are in-game). **[K25]** records the precedent; **[H14]** applies it: read the carved/matchstick **letters as
  latitude** and the **[S21] numbers (53/23/29) as longitude** (or the pairs as cells) → *places, not people*. **This reframes
  [U26]:** the earlier "web found no grid" is **partially overturned** — a coordinate reading now has documented precedent; the
  *per-cell* A1/B1 grid was the remaining gap (**since captured → [K26], see the newer entry above; the per-cell test came back
  negative-leaning**). Propagated: K25/H14 (INDEX, known-facts, speculation), connections §1a(d), U26/U25,
  [`number_grid.py`](experiments/number_grid.py), source #57, [log](INVESTIGATION_LOG.md) top.
- **Letter groups, number/medium motifs, and the verified-trail boundary (user steer).** (1) **`LJ`/`SM` are directly part of
  the mystery — [KNOWN]**, not a guess (carving technique [K15] + co-location with the Fort Brennand pointer & tally 4); only
  their *meaning* is open ([U4]). (2) New **[H12] letter-grouping framework** so experiments test the markings *by connection
  confidence*, not as one flat set: **Group 1** carved `LJ`/`SM` · **Group 2** matchstick `EC`/`J+M`/`S+J` · **hybrid**
  `LJ`/`SM`/`EC` (`EC` by the Black Widow card) · **`J+M`** singled out (its site = the trail START node).
  [`name_match.py`](experiments/name_match.py) now reports per-group. (3) **[U27]** the chain branches from outhouse **#4**,
  not #5 — flagged; **[S20]** a weak number/timing motif (8 webs, 4 AM pentagram, Rockstar's *Infinite Eight*). (4) **[U28]**
  the 3-in-a-row droppings on outhouse #4's roof (investigator image; likely scenery). (5) **[H13]** the clues share a
  **medium** — wood + railway telegraph poles + time-gating + near-invisibility — a search heuristic for the frontier.
  (6) **Verified-trail boundary set:** the **Fort Wallace bird carvings are the last verified clue**; the **"?" is not widely
  accepted** and the **Bacchus heart's relevance is as contested as the "?"** — we work forward from the bird carvings.
- **Letters work — name-list built, non-name readings tested, terminology tightened.** New
  [thread 07 (Van der Linde gang roster)](threads/07-van-der-linde-roster.md) — full roster · fates · death mission/timing ·
  graves — doubles as the in-fiction name list. Cross-check ([`name_match.py`](experiments/name_match.py)): exact hits
  **`SM`=Sean MacGuire, `J+M`=John Marston**, gang supplies the `L` Register Rock lacked ([S16]); **`EC` matches nothing**
  ([S17]). Non-name readings ([`letters_cipher.py`](experiments/letters_cipher.py) + a gazetteer pass): whole-set **anagram
  ruled out** (vowel-starved); **place reading mostly negative** — survives only `EC`=Emerald Crossing / `SM`=Scarlett Meadows
  ([S19]); A1Z26 flag `EC`=5,3 = feather split ([S18]). **[U16]** resolved-negative (Annabella poems unsigned). **Framing
  [U25] (user):** call them **"letters," not "initials"** — the name-reading is [SPECULATION]. Multiset corrected to
  `{C,E,J,J,J,L,M,M,S,S}`. Full detail: [connections §1/1a](analysis/connections.md); see [log](INVESTIGATION_LOG.md) top.
- **Reddit screenshot-mining pass (Arctic Shift + `i.redd.it`).** First **feather-in-web captures** filed (one black, one red;
  location-unconfirmed) → the repo's #1 still-wanted item. **Orientation read for [U0]:** both feathers **hang tip-down by
  gravity**, not along a heading — a *weak lead against* [H4]'s "orientation = compass direction." Plus: **[S15]** (feathers =
  Northern Cardinal dimorphism — a deflationary rival to the colour-cipher reading); a **cut-content lead on [U2]** (gamedev
  datamine: two flags checked-but-never-set — C-tier, post since removed); the **feather↔dreamcatcher particle-config** tie
  ([H8]/[K20]); and **[K24] corroboration** (Butcher Creek datamine names `pignpole`/`magicstuff`/`outhouse cliff`). All C-tier,
  tagged. See [log](INVESTIGATION_LOG.md) top entry.
- **[K23]/[K24] GTA↔RDR2 crossover dossier — new file [analysis/gta-rdr2-crossover.md](analysis/gta-rdr2-crossover.md).**
  Gertrude's recitation **opens `1237645112`**, the *same* string the **Madam Nazar "Nazar Speaks"** machine speaks in
  **GTA Online** (multi-outlet B-tier). ⚠️ **Chronology corrected (user-flagged):** the number is **RDR2-original (base game,
  Oct 2018)**; the GTA echo is a **later callback (Dec 12, 2019)**, **not** a prior origin — so it **corroborates the number is
  deliberate**, it does **not** demote the RDR2 reading. **[K24]:** GTA V's two **Mt Chiliad webs are base-game since 2013, not
  DLC** (same cable shader + 1–2 AM gate as RDR2) — so the webs in *both* games are original-to-launch; only the Nazar number
  callback was added later. Nazar's machine also names our nodes (**Window Rock, Roanoke Ridge, Grizzlies**, the web fortune
  [U19]) → **[S14]** (weak — coincidence-prone). **Net:** the crossover raises confidence this is **deliberate**; the
  **decode/spider-link is exactly as open as before**. A C-tier exposé ([#43]) separately alleges the Strange Man "Gertrude
  solved" *video* is a **hoax** (⇒ treat his Gertrude claim as disputed). Propagated across K23 (reworded)/K24/S14, U6/U18/U19,
  connections §2/§3/§6, speculation, sources #40–46.
- **[U24] Register Rock — full carving list sourced.** Pulled the **complete** inscription set (wiki + reddeadreference
  transcription blog + our journal image): ~14 named carvings + ~10 bare marks ([dossier](locations/register-rock.md#complete-inscription-list)).
  Desk-test vs the matchstick letters: 🟢 **J.M appears twice** ("Jm" + "Jasper Munson") → echoes **`J+M`**; 🟢 **S. Gray** →
  Caliga Hall **`S+J`**; 🔴 but **no `LJ`/`SM`/`EC`, and no `L`-initial at all** — a real partial-negative. Still gated on
  whether the Fort Brennand third symbol actually depicts the rock ([H11]).
- **[K21] boundary respawn mechanic** (investigator data): shot feathers stay down only while you're **inside the web's tied
  boundary**; **3 boundaries** — north, south, + a connector. Sourced the **Jay_0048 boundary map**
  ([`web_map-overlay_boundaries.png`](images/webs/web_map-overlay_boundaries.png)) → partition **[H9]**: N `B34` / Connector
  `B23,B45,B56,B56L` / S `R23,R45,R34`. The **Connector == the [K13b] non-respawn chain** — the spatial mechanic *is* the
  chain. Verify membership next (**[U22]**).
- **+8 images** from the community Google Site (boundary/labelled/chain/trail maps, cable-mesh datamine, Cornwall pole, Fort
  Wallace guitars & birds).
- **Two new frontier leads (investigator data):** **[K22]** a hidden **empty heart** on [Bacchus Bridge](locations/bacchus-bridge.md)
  (blank twin of the Flatneck "Lillie ♥ Alfred" heart) **in line of sight of the bird carving** → [H10]/[U23]; and **[H11]**
  the Fort Brennand "3rd symbol" may depict **[Register Rock](locations/register-rock.md)**, whose carved **names** (incl.
  **S. Gray** → Caliga Hall `S+J`) could be a name-puzzle → [U24]. The earlier "Lillie ♥ Alfred" texture is **re-framed** from
  "rejected" to the heart-motif reference.

## Recently resolved (don't re-litigate)
- **[U8] → [K3]:** dev quote is **Adam Butterworth, ex-Rockstar QA** — confirms *real*, not *authored* (B/C-tier, single X post).
- **[U13] downgraded:** **Spider Gorge** is wiki-only speculation; no secondary source — journalism points the marker at Fort Wallace.
- **[U17] reframed / [K20]:** the spider mystery has **no in-game log at all**; the lingering log entry is the **dreamcatchers'** ([H8](findings/speculation.md) tests the link).

---

## Map of the spine
| File | Use it to… |
|------|-----------|
| [STATUS.md](STATUS.md) (this) | See where the case is and what's next. |
| [INDEX.md](INDEX.md) | Look up any **K/U/H/S ID** — its claim, status, and which file owns it (edit there). |
| [EVIDENCE-CHECKLIST.md](EVIDENCE-CHECKLIST.md) | Turn open questions into sourced evidence (web-first). |
| [README.md](README.md) | Onboarding: what the mystery is, the threads, the best-understanding paragraph. |
| [INVESTIGATION_LOG.md](INVESTIGATION_LOG.md) | Chronological record (newest at top). Log every session. |
| [sources/RESOURCES.md](sources/RESOURCES.md) | "Where do I go for what?" — the resource directory + fetch recipes (vs [sources.md](sources/sources.md), the per-claim ledger). |

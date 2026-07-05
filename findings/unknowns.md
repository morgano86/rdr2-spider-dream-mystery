# Open questions / unknowns

The live problem set. Anything here that gets resolved should move to [known-facts](known-facts.md) or
[speculation](speculation.md) with a date and source.

## Highest priority (could break the case open)
- **U0. The 8 feathers' POSITION/orientation (your lead) — ORIENTATION RESOLVED 2026-06-13.** Was undocumented online; now
  captured for **all 8 webs** (front + side) via u/dropthepress's screenshot set ([#59] →
  [`feather-positions/`](../images/webs/feather-positions/)). **Result: every feather hangs vertically, tip-DOWN, under
  gravity — no per-web heading exists**, which **refutes [H4]** (orientation = a compass direction to the next web). **What
  remains open is the weaker *attachment-point* reading:** which radial/quadrant the feather's thread hangs from **varies
  between webs (the half-web = ~7 radials → **6 sections** × ~3 rings, confirming the user's framing) — possibly meaningful,
  possibly modelling noise. **Per-web location mapping is now RECOVERED** (2026-06-14, from the post selftext; files renamed
  `web_<location>_<code>_<front|side>.jpg`). **SOCKET RESIDUAL NOW CLOSED FROM IMAGES (2026-06-14, [H19]).** The earlier
  "camera-confounded, needs the datamine" caveat was over-cautious: re-reading each feather **against the web's own central
  vertical radial** (which rotates *with* the web → camera-invariant) instead of the screen resolves all 8 to `L/C/R` and
  **agrees 8/8** with the old screen-relative reads — the confound never *flipped* the gross call, it only inflated uncertainty.
  Socket is now a **usable weak signal**. Structure tested ([`web_socket_position.py`](../experiments/web_socket_position.py)):
  the reds-right/blacks-left lean is **NOT significant** (p=0.125); the only crisp pattern is the **3 hour-twinned blacks
  sweeping `L→C→R` with the clock** (p≈0.04, n=3) plus the **5–6 AM pair B56/BL56 sharing hour+socket** (reinforces [K13b]).
  The raw per-instance entity placement would upgrade these eyeballed reads to A-tier but is **no longer needed to
  characterise** the socket. **(Update 2026-07-04: the 8 fronts were replaced by firsthand PS5 4K captures; sockets
  re-verified 8/8 unchanged, all high-conf — Scarlett's C-vs-R ambiguity resolved to `R`. The reads are no longer
  C-tier-image-dependent.)** Re-confirmed: deliberateness is in **placement**, not unique files (shared `wap_gen_feather01` + 4 reused
  `cablemesh` models). Net: adds a weak colour-axis line ([H9]/[U29]/[H18]); does **not** revive [H4] (socket ≠ orientation).
  Pairs with the order mechanic ([U29]). → [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md),
  [feather-positions](../images/webs/feather-positions/README.md), [connections §5d](../analysis/connections.md)
- **U1. [RESOLVED 2026-06-14 → [K11]/[K12]].** The under-wood pole messages, verbatim. **Deep-research pass ([#60])
  multiply-corroborated the full chain** (was single-sourced): centre `N`+telephone-pole (an **alignment** reveal, 1–2 AM,
  [K11]) → north pole `W ✞✞✞✞✞` (**five** glyphs, unanimous across 6+ B-tier outlets) → fifth pole west `NW`+guitar-like symbol
  ([K12]). **Bounded negative:** these are the **only two shot-to-reveal poles**; the `NW`+guitar pole is the **last documented
  under-pole message** — **no third pole inscription is documented in any source** (anything "past" it is the [K16] bird carvings
  or out-of-bounds pareidolia, neither an under-pole message). Residual open items split off cleanly: the **guitar's meaning**
  ([U12]) and the poles' **map coordinates** (still uncaptured). → [05](../threads/05-spider-web-trail-2025.md)
- **U22. [RESOLVED 2026-06-14 → [K31]].** Exact web↔boundary membership is now **firsthand-confirmed**: the *tied* partition is
  exactly the [H9] map — **Top** `B34` / **Connector** `B23,B45,B56,B56L` / **South** `R23,R45,R34` — the North/top boundary
  does hold only the one *tied* web (`B34`), and the legend "R56" was the `R34` typo. New refinement: because the boundaries
  **overlap**, each also *contains* (untied) some adjacent-boundary webs ([K31]) — shooting those triggers the **wrong**
  boundary's despawn, which matters for routing the shoot order. → [K31](known-facts.md), [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md)
- **U29. The full feather reset ruleset and what it means (sourced 2026-06-13, [#36] C-tier brute-force testing).** The
  earlier "one correct chain `B23→B45→B56→BL56`" picture is **too strong** — testing found the order is **group-based, not a
  single sequence**: the reds work in *any* internal order (incl. the **non-chronological** `R34→R45→R23`); mixed chains work
  (reds may precede blacks); **`B34`/Cornwall is special** (first reported "can't start," self-corrected to "can start," with a
  standing suspicion it's the **LAST** feather — unproven); and there's an unexplained **"unique function to the red
  feathers"** ("any red after BL56 resets"). This **leans the order question toward the [H9] boundary partition** and **deflates
  [H4]/[H17]** (multiple working orders ⇒ orientation can't encode a unique next-target; the clock isn't the key either). **Open:**
  `B34`'s true role (start vs last), what the red-feather function is, and the upstream **time-lock vs persistence** question
  (are webs only shootable in their hour — which would make any non-chronological order impossible — or do they persist?).
  **NOW THE CENTRAL CRUX (2026-06-14, [H20]):** firsthand feasibility says **black + red in one night solo is impossible** (the
  colour×hour twins are geographically split — blacks on the North/Connector spine, reds on the far South bar [K28]), so a
  single-player solve **must span ≥2 nights, one colour-group per night.** That makes **persistence ACROSS NIGHTS** the decisive
  open question: do shot feathers stay down between nights, and is the **central boundary overlap [K28]** (the only spot inside
  >1 boundary at once) the mechanism that lets you *hold* one group's state while running the next? **✅ ANSWERED (in part)
  2026-06-14 → [K29]:** shot feathers **DO persist across nights and camping — indefinitely (≥12 in-game days observed) — while
  you stay inside the tied boundary**, resetting only when you leave it. So multi-night solving is **mechanically viable**.
  **STILL OPEN:** (a) the **central-overlap state-hold** sub-question tested **negative-leaning** (camping in the overlap did
  *not* preserve state across a boundary exit; the feather reset — though an invisible internal flag may persist, untested);
  (b) **`B34`'s role** (start vs last feather); (c) the **red-feather function**; (d) whether you must shoot **all** of a
  boundary's feathers before crossing. → [K29](known-facts.md), [H20](speculation.md), [K28](known-facts.md),
  [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [connections §5a](../analysis/connections.md)
  **🔑 REFRAMED 2026-06-14 → [H22]:** the *within-boundary* order is **already solved on all three** (South any-order /
  Connector chain / North=`B34` last), so the order isn't bottlenecked on "which sequence." Under "`B34` last" the **global**
  problem is just **2 meta-orders** (reds-first / blacks-first), each needing ≥1 boundary crossing — and there **[K29]
  (resets on exit) CONTRADICTS [H20]**. The live frontier is therefore a **cross-boundary STATE** test with 3 exits (R1
  overlap-holds / R2 hidden-flag / R3 no-combine); see [`web_boundary_solve_protocol.py`](../experiments/web_boundary_solve_protocol.py)
  and [H22](speculation.md). The remaining sub-items (b) `B34`'s role and (c) the red function live *inside* that frontier.
  **📋 Executable field protocol (2026-06-21) — confound controls + a decision table mapping each in-game outcome to R1/R2/R3:**
  [analysis/web-order-field-test.md](../analysis/web-order-field-test.md). This is the actionable next step on the case's #1
  open question; a clean negative is itself loggable.
  **⚠️ FOURTH FRAME (premise-drop pass, 2026-07-02 → [H27]):** the whole ruleset may be **display-repair/anti-cheese, not a
  puzzle** — the "working orders" as boundary-geometry epiphenomena and feather-shooting itself a community-imported input
  no verified clue instructs ([solve-grammar.md](../analysis/solve-grammar.md); the desk companion
  [`web_file_order_concordance.py`](../experiments/web_file_order_concordance.py) shows **no 8-order is even visible-state
  feasible, 0/40320**, and the [K39] file numbers order nothing beyond chance — [S38], two conditional candidates
  survive). Cheapest discriminator: **Test D** (witness-only tour, no shots, + dream coda) *before* any shooting protocol.
  **🆕 The [H27] frame gained hard(ish) evidence 2026-07-02 (Reddit sweep, [#52] full recovery):** the C0d3M3chan1c datamine's
  strongest single claim — **ZERO references to `spiderdream` (string or any computed joaat hash) in all 1,639 decompiled
  scripts**: *no script spawns, detects, tracks, or responds to the webs*; visibility is pure engine timeFlags. If accurate,
  **no script-level shooting-order handler exists** — the entire order question would be either engine-side (C++, invisible
  to datamining) or moot ([H22]-R3 / [H27]). C-tier with specific caveats (AI-assist alleged; its hour-window list fails
  2/8 against the observed lattice — see the source row), so it *leans*, not settles. **⚡ The zero-refs leg REPRODUCED
  firsthand 2026-07-05 ([#87]):** 0 hits for `spiderdream` — string, all computed joaat hashes, and the [#66] feather
  entity hashes — across all 1,638 scripts of an independent public June-2024 dump; the strongest [#52] leg is no longer
  single-sourced (the hour-window caveat stands — the data-file side remains unreproduced). Also new from the sweep ([#70]/[#71]):
  the **"one-session rule"** (save/reload wipes web state — never reload mid-run) and **two more all-blacks-one-night
  completion nulls** (no sleep step run — the [H25] gap stands).
  **⚠️ A THIRD FRAME added 2026-07-02 → [H24]:** the seam contradiction may be an **artefact of the "all 8 must be shot"
  premise** — if the 3 reds are **decoys** (the colour×hour lattice re-read as an hourly black-vs-red *fork*, taking the
  [H18] filter grammar literally), the whole solve is the **5 blacks with no red↔black crossing at all**, and *"any red
  after BL56 resets"* becomes a **completion guard**. Consistent with every observation in this entry; rival of
  [H20]/[H22]-R2 on sub-item (c). **Corrected same day (investigator): `BL56` lies outside the orange boundary, so holding
  all 5 black states forces `BL56`-before-`B34` → `B34` on a later night — the geometry mechanically DERIVES sub-item (b)'s
  "B34 last" suspicion**; all-5-down reachable in ~2 nights via [K29]. Cheapest test on the board → **Test C** in
  [web-order-field-test.md](../analysis/web-order-field-test.md); the red function's other candidate venue is **[S35]**
  (Strange Man's shack sits inside the South boundary per [K28] — a southern [H21]-style state-carry target).
- **U30. Does a feather hit count by VISIBILITY or by HOUR? [investigator, 2026-06-14].** Render-gating ([K30]) lets you keep a
  web rendered **past its spawn hour** by holding line of sight as you approach, and a feather shot that way registered + kept
  its shot status across a camp/night. **Open:** does the game count a hit **whenever the feather is shot while visible** (so a
  line-of-sight-held shot after the hour is valid) **or only when shot during the web's specific spawn hour**? This bears
  directly on whether a multi-night solve ([H20]) can "bank" extra time on a web by holding it in view. **Likely untestable
  until the solution order is known** (you can't tell a valid hit from an invalid one without a confirmed payoff). →
  [K30](known-facts.md), [K29](known-facts.md), [H20](speculation.md)
- **U2. The payoff.** **Confirmed (2026-06-13): still NO reward/cutscene/unlock, mystery UNSOLVED as of June 2026** (Popverse,
  Kotaku, comicbook, Dexerto — all Jan 2026; *"No new loot, tools, or cutscenes,"* vindication = the only "reward"). Nothing
  solved since Dec 2025; post-Jan progress is **additive lead-finding, not resolution.** **Reframed:** Fort Wallace is a
  **waypoint, not the dead-end** — the cold frontier moved NW (Calumet / a "?" carving, [06](../threads/06-bird-carving-giant-wapiti.md)).
  Still open: *is there an intended payoff at all, or is it cut content?* (cut-content = a possibility, not a confirmed answer).
  **New lead toward cut-content (2026-06-13, Reddit C-tier; FULL BODY RECOVERED 2026-07-02 via Arctic Shift):** a datamine
  write-up (u/C0d3M3chan1c, "gamedev take," 201 pts, removed by mods but archived) reports scanning 1,639 decompiled scripts +
  2,000+ data files and finding **two persistent flags that are *checked* but **never *set*** by any script** — now fully
  specified: **(1) `DiscoDisable`** (`Global_40.f_8863.f_156`), a master kill-switch every discoverable script checks on
  startup, saved to disk, set by nothing; **(2) a per-discoverable termination "bit 4"**, likewise never set. I.e. a payoff
  gated on a state nothing in the shipped scripts ever turns on. *If accurate*, the strongest technical argument yet that the
  trail is **incomplete/cut** (or finished engine-side, beyond script reach) — the author's own fork is exactly our [U2]:
  *Option A "real and huge, trigger in engine C++"* vs *Option B "art layer finished, gameplay layer never wired."* Treat as a
  lead, not proof: single C-tier author, ~~unreproduced~~, AI-assist alleged by commenters (and its hour-window list fails our 2/8
  lattice check — trust structure over numbers). Related sweep finds: `dreamanim.c`, a near-empty decompiled script registered
  with a John Marston mission blip in the Lanahachee river ([#74]) — same cut-content flavour. → [source #52](../sources/sources.md)
  **⚡ REPRODUCED-IN-PART + one CORRECTION (2026-07-05, [#87] — firsthand grep of a public June-2024 GitHub script dump,
  `creativewild/rdr2-scripts-decompiled`, build 1491.50; committed **before** the trail decode and the [#52] post, so it
  can't be contaminated by either):** the script-side claims all check out — **1,638 scripts** (claim: 1,639); **zero
  `spiderdream` references** (as a string, as any of the 9 independently-computed joaat hashes of
  `spiderdream`/`spiderdream01–08`, and via the 8 [#66] feather entity hashes — every "spider" string in the scripts is a
  mundane asset: spider-orchid herb/collectible, the `WATER_SPIDER_GORGE` water volume); **both flags are real** —
  `startup.ysc.c:3763` registers the savegame BOOL `"DiscoDisable"` in the Discoverables save block ("Disco" =
  *discoverable*), **all 15 `discoverable_*.ysc.c` scripts** guard `if (func_11(state, 4) || Global_40.f_8863.f_156)`,
  and **no script ever assigns the global**; and `dreamanim.ysc.c` is **24 lines whose `main()` sets two floats and
  returns** ([#74] confirmed). The script-side structural claims are **no longer single-sourced** (treat as B-equivalent);
  the data-file claims (two-object web/feather, particle configs, hour windows) stay C-tier unreproduced, and whether
  bit 4 is ever *set* was not traced. **The correction:** the gloss above — *"a payoff gated on a state nothing in the
  shipped scripts ever turns on"* — had the semantics **backwards**. The reproduced guard **disables** the discoverable
  when true (`→ cleanup + bail`), so both flags are **dormant kill-switches** (never-set ⇒ the content stays ON; shipping
  an unused master disable is normal engineering), **not** a payoff gate. What carries the cut-content lean after the
  correction: (i) the webs have **no script layer at all** (now reproduced — either engine-side or never wired, the [U2]
  fork restated); (ii) `dreamanim.c` (confirmed near-empty — **and now fully contextualized 2026-07-05 → [S46]/[#88]:**
  it ships **registered in the FINALE mission group** alongside `finale1/2/3`, with a John mission blip at
  bayou-area coordinates, an unmatched mission code `TL21`, the registry's highest used slot, and — uniquely across all
  80 registrations — the generic `def_intro_script` intro: a dream-named finale-era mission slot, registered but empty;
  **no spider-web tie demonstrated**). Flavour aside, recorded not built on: a checked-but-never-set
  per-discoverable *termination* bit rhymes with the never-clearing **dreamcatcher log entry** ([K20]/[U17], the wiki's
  own "Oversights" bug) — a candidate mundane mechanism for that bug, unverified. → [source #87](../sources/sources.md)
  - **Candidate payoff LOCATION (2026-06-14, [H21], speculative):** if a payoff exists, the oversized B34 boundary ([K28],
    uniquely holding **Butcher Creek** inside a zone, forts excluded) makes **Butcher Creek (or Valentine)** the natural place a
    **state-gated** result would surface — reachable from the webs with shot-state intact ([K21]). This **dovetails with the
    "checked-but-never-set flags" lead** in a pointed way: H21's predicted state-setter would be *exactly such a flag* — so
    either web activation **is** what sets it (and the script-scan missed an engine-side/out-of-scope setter), or it genuinely is
    **never set** (→ the gate can't fire → cut content). Distinguishing these is the crux. *(⚠️ Dovetail weakened 2026-07-05:
    the two flags reproduced from the public dump ([#87]) are **disable**-flags — H21 predicts an *enable*-flag; the
    dovetail survives only as "dormant flag machinery exists in the shipped scripts," not as a matching flag found.)*
    ⚠️ No payoff ever confirmed; do not present Butcher Creek as a destination. → [H21](speculation.md), [K28](known-facts.md)
  - **Argument *against* the "pure decoration" reading (investigator 2026-06-15, [K30]):** the webs are **render-gated** (won't
    spawn/despawn while looked at), but the Butcher Creek **pentagram** — same [K15] technique, same time-gating — is **not**
    (it appears/disappears even while stared at). So the concealment is **web-specific and selective**, not blanket LOD. You don't
    anti-discovery-gate scenery → this is a weak-but-real point that the webs are **intentional content**, narrowing U2 toward
    "intended-but-unfinished/cut" over "never meant anything." Design-intent inference, [SPECULATION]. → [K30](known-facts.md)
- **U3. One puzzle or two? — ⚖️ REFRAMED / PARTLY DECIDED 2026-07-04 (desk adjudication → [S41],
  [one-puzzle-or-two.md](../analysis/one-puzzle-or-two.md)).** The question bundled **three separable parts**, and the
  first is no longer usefully open: **(a) the relay question — decided toward ONE.** The 2018 carving chain and the 2025
  web trail read as **one continuous designed relay**: the [K8] hand-off (Fort Brennand symbols → the Cornwall start
  pole) is primary-wiki-asserted **and retro-validated** (the pointed-at pole carries the hidden engraving + the head of
  the 8-web system, [K11] — a misread pointer doesn't land there by luck); the halves share a physical node (Oil Fields:
  [K10] + web `B56`), the [H13] signature medium/gating, and the dream motif ([K13] `spiderdream` ↔ [K10]); both are
  base-game Oct 2018 ([K2]/[K24]). **"Parallel eggs sharing motifs" is rejected** at the working standard ([S41] —
  design-inference, so [SPECULATION]-tagged; reopeners listed in the file). **(b) the mechanic question — still open,
  tracked at [U29]:** is the feather/boundary system an interactive stage or epiphenomena ([H27]/[H24]/[H20]/[H22])?
  The relay verdict is **invariant** to that outcome. **(c) the satellites — per-thread scorecard** in the file:
  `LJ`/`SM` **IN** ([KNOWN] membership via [K6]/[K15]); matchsticks **undecided**; **Gertrude undecided-out** ([U6] —
  if a genuine second puzzle exists anywhere it's her, but that was never U3's core); Bacchus/`?` out (boundary
  discipline). Earlier arguments absorbed into the adjudication: [S22]/[H21] mechanical bridge (not load-bearing),
  [S28] `EC`-key, [S31] one-construction geometry. → [one-puzzle-or-two.md](../analysis/one-puzzle-or-two.md),
  [S41](speculation.md), [U29] above, [U6] below

## Letters & numbers (the cipher questions)
- **U25. Are the markings even "initials" at all? [framing — user, 2026-06-13].** The **[KNOWN]** is only that the game
  *displays the letter-pairs* `LJ`, `SM`, `EC` (bare) and `J+M`, `S+J` (with a `+`). That they are **initials of names** is one
  **[SPECULATION]** (`S1`/`S2`/`S16`), not a fact — calling them "initials" pre-commits the puzzle. Live candidate readings:
  (i) **names** (initials/relationships); (ii) **place-abbreviations** — tested, mostly negative, survives only for
  `EC`=Emerald Crossing / `SM`=Scarlett Meadows ([S19]); (iii) a **positional/per-pair cipher** keyed by an external order
  (open; whole-set anagram ruled out as vowel-starved — see [connections §1a](../analysis/connections.md)); (iv) **numbers** —
  A1Z26 with the **punctuation as operator** (`+`=add, bare=concatenate) → matchsticks `EC`=53, `J+M`=23, `S+J`=29 ([S21], weak;
  only `EC`=53=the feather split lands); (v) glyphs/other. **Neutral term is "letters."** → [connections](../analysis/connections.md), [02](../threads/02-butcher-creek-carvings.md), [03](../threads/03-matchstick-letters.md)
- **U26. [GRID CAPTURED 2026-06-13 → [K26]; per-cell reading NEGATIVE-leaning] Map grid-reference reading.** The idea
  (investigator's lead): the letters are **grid references** — a column letter + a row number (A1/B1-style). A web research
  pass had found **no documented grid** (Piggyback guide + community maps all use **continuous-numeric** coords). **The
  investigator then captured it firsthand** (PS5, 2026-06-13 — high-trust, supersedes the web-negative): two *"Railroad and
  State Map of the United States"* prop maps at a **stranger's camp** carry printed grids — **Map 1** (continental) cols
  **1–30** × rows **A–U** (30×21); **Map 2** (regional, drawn over the playable world) cols **A–O** × rows **1–7** (15×7). So
  the empirical question is **answered — RDR2 has an in-game letter/number map grid ([K26])**. **The interpretive question
  tests negative-leaning** ([`number_grid.py`](../experiments/number_grid.py) re-run): on **Map 2** (the grid over the game
  world) **only `EC` is in range** (`E3`/`C5`); `LJ`/`SM`/`J+M`/`S+J` all fall **out** (their 2nd letters → 10–19, past the
  7-row cap) — exactly the "small grid → most letters out of range (against)" branch. Map 1 admits every marking but
  discriminates nothing and its cells sit off the playable world. **No single grid validates all five.** Precedent for a
  coordinate reading still stands ([K25], letter=lat/number=long loading-screen Easter egg). **What survives:** [H14] as a
  free coordinate *plot* (not a per-cell lookup), and `EC` as the lone in-range marking (cf. [S18]). → [connections §1a(d)](../analysis/connections.md)
- **U4. What do `LJ` and `SM` mean?** In-fiction clue (user hypothesis — **now the working stance**); **dev-initials CLOSED
  as a working line 2026-07-02** (counts unfalsifiable across 6,345 credits + coherence asymmetry — `LJ`, the tightest-tied
  marking, has *zero* world-building senior matches, and Lazlow fits only via a stage name as an audio director on a chain
  with no audio clues — + the letters are co-carved with a *functional* pointer; [connections §1](../analysis/connections.md)).
  Test against character names and against the `J+M` matchsticks. **Gang name-list now built ([thread 07](../threads/07-van-der-linde-roster.md)):**
  `SM` = **Sean MacGuire** is an **exact** one-person hit ([S16]); the gang also supplies the `L` (Lenny/Leopold) absent from
  Register Rock. Suggestive, not proof (coincidence-odds caution). **Newest candidate: the waymark reading [H26]** — presence
  marks the node, content may be flavour; predicts undiscovered letter-pairs at other verified nodes (🎮 letter-sweep).
  → [02](../threads/02-butcher-creek-carvings.md), [connections §1b](../analysis/connections.md)
- **U5. What do the matchstick letters MEAN?** Locations now pinned: `EC`=Vetter's Echo, `J+M`=**Cornwall K&T (web-trail
  start)**, `S+J`=Caliga Hall (Gray estate); arrow set location still TBD. **Open:** the cipher/relationship — are they
  names? do letters pair with places? **Dev-initials reading is weighted DOWN → CLOSED as a working line 2026-07-02** (see
  [U4]; thousands of staff → coincidental match is near-certain; no coherent authoring team in the credits). **Gang cross-check ([thread 07](../threads/07-van-der-linde-roster.md)):**
  `J+M` = **John Marston** is an exact hit ([S16]); **`EC` matches nothing** in any name source ([S17], investigator's point —
  its non-match argues the initials are deliberate). **Number-reading alternative ([S21]):** read as A1Z26 with the `+` as
  *add* and bare pairs *concatenated* → `EC`=53, `J+M`=23, `S+J`=29 (all prime; `EC`=53=the 5/3 feather split) — weak but live.
  **🆕 Couples test run 2026-07-05 → [S45]:** matched against documented in-game **couples** (what the `+` lovers' styling
  actually predicts) — **`J+M` = Joshua+Miriam (the Emerald Ranch / web `B45` tragedy)** and **`S+J` = Sadie+Jake Adler**,
  with the three bare markings matching none (2/2 vs 0/3 on the styling line); initials-cheap (p≈0.11), the weight is
  structural. → [03](../threads/03-matchstick-letters.md), [connections](../analysis/connections.md)
- **U6. Gertrude's number sequence — [PARTLY RESOLVED 2026-06-13].** The **opening is now multi-outlet sourced**: she begins
  `1 2 3 7 6 4 5 1 1 2` (`123 7645112`), which Rockstar **deliberately echoed cross-game** — the **Madam Nazar "Nazar Speaks"**
  machine in **GTA Online** speaks the same string ([K23]). ⚠️ **Chronology (corrected, user-flagged):** the number is
  **RDR2-original (base game, Oct 2018)**; the GTA echo is a **later callback (Dec 2019)**, so it **corroborates that the
  number is intentional** rather than explaining it away — and the GTA side is **primary-sourced 2026-07-04** ([#75]: three
  fortunes, then `123-764-5112` is **callable**). **⚡ Tail ADVANCED 2026-07-04:** the fullest transcription on record was
  recovered from StrangeMan's own video frames via the [#43] exposé (**9 distinct sequences, max 29, always restarting at
  1, 2…** — image + full table in [thread 04](../threads/04-gertrude-numbers.md)); both hostile parties (hoaxer + debunker)
  agree on the raw numbers, and it contains our old audio fragment verbatim. The *"does it loop identically?"* sub-question
  now leans **NO** (varied ramblings sharing motifs). **⚡ Structure battery run 2026-07-04**
  ([`gertrude_tail_structure.py`](../experiments/gertrude_tail_structure.py), exact permutation nulls on the provisional
  9 lines): **[S42]'s failed-counting shape is statistically supported** (prefixes never pass 5; post-derail re-rail runs;
  global additive structure p = 0.44 = chance), with **one fragile counter-flag** — an L2-only 4-term Fibonacci chain
  `3,5,8,13` (p = 0.039 pre-discount) that **collapses under the near-duplicate L7 parse** of the same line, so the
  clean-audio confirm now decides both the tail text and that fork (**priority raised**; one dump route — the Tumblr RDR2
  audio compilation — checked negative, gang dialogue only). **⚡⚡ TAIL CONFIRMED FROM GAME TEXT 2026-07-05 → [K42]** ([#78]:
  a 2019-12-01 GitHub dump of the game's own subtitles carries her complete file — **12 canonical number lines**, table in
  [thread 04](../threads/04-gertrude-numbers.md)). The clean-source residual is **DONE**; the fork is **decided — both L2/L7
  variants are real distinct lines** (the `3,5,8,13` run is verbatim in line A; line B's inserted 4 breaks it); video-L3 was
  an artifact; "eleven" (not "1, 1") is the RDR2-side parse; **no hidden extra recitation exists in the dump**. **Also
  2026-07-05: attempt B (tally-node reorder) CLOSED-INEXECUTABLE** — the node-content sweep ([#81], [thread 02](../threads/02-butcher-creek-carvings.md))
  found nodes 5 and 6 bare, so the {4,5,6,7} reorder has nothing to read (reopens only via an [H26]-sweep find).
  **Still open:** what (if anything) the canonical set encodes — 🧠 **first: re-run the structure battery on the [K42]
  inventory** ([S42] = the documented deflationary rival: tail = failed-counting madness texture, only the signature
  string deliberate); and **which** mystery the number serves — spider trail, standalone Braithwaite/Nazar puzzle, or
  nothing decipherable. Interior-of-outhouse line **closed-negative** ([K41] — players glitched in, 2025: only
  Gertrude's model, no objects). → [04](../threads/04-gertrude-numbers.md),
  [gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md)
- **U24. Do the [Register Rock](../locations/register-rock.md) names/initials encode anything?** *If* Fort Brennand's third
  symbol points to Register Rock ([H11]), its carved names are a candidate puzzle. The **complete carving list is now sourced**
  (wiki + reddeadreference transcription blog + our journal image — full table in the
  [dossier](../locations/register-rock.md#complete-inscription-list)): beyond the wiki's headline **J. Brooks, Frank Heck, Otis
  Miller, Billy Midnight, S. Gray, A. West, B. Ward**, it adds **J. V. Henry (×2), Jasper Munson, C. Riley, A. Pickel, Doyle,
  R. Mack, Henry Matilda, Mary**, and bare marks **W.Y.B, BM, R.M, R.S, R.S.G, Jm, DOF, WSF, ORW, .8DB8.** **Desk-test result
  (lead, not a match):** **🟢 J.M appears twice** ("Jm" + "Jasper Munson") → the **`J+M`** matchsticks, and **🟢 S. Gray** →
  Gray family → Caliga Hall **`S+J`**; but **🔴 no `LJ`, `SM`, `EC`, or any `L`-initial** appears. So the rock supplies J/M/S/C
  from **{C,E,J,J,J,L,M,M,S,S}** but not the `L`/`E` legs. **Don't pre-filter:** the wiki's "A. West/B. Ward = *Batman*" reading is
  **unconfirmed speculation**, and a puzzle may use names that double as real-world references as **camouflage** ([S13]) — keep
  every name live; the scripted match decides. → [02](../threads/02-butcher-creek-carvings.md), [connections](../analysis/connections.md)
- **U7. The tally counts as a sequence — [GERTRUDE HALF ANSWERED-NEGATIVE 2026-07-05].** Butcher Creek 1–5, Fort
  Brennand 6 & 7 — is the count itself the message (a running 1,2,3,4,5,6,7…)? The **site-level half** (1→7 as one
  deliberate running count across the two [K8]-chained sites) stays open-plausible. The **continuation half** ([S4]:
  Gertrude, reaching ~10–11, extends it past 7) is **answered-negative on the canonical [K42] game text**: no ascending
  consecutive run crosses 7 anywhere in the 12 lines (`7` → only `6/5/6/3`; `6` never → `7`; `8` entered only by derail
  from 17 or 5); `10`/`11` appear only inside derailed babble; **12 is never said**. Consistent with [S42] (failed
  counting, capped at 5). → [thread 02](../threads/02-butcher-creek-carvings.md), [S4](speculation.md)
- **U27. Why does the chain branch from outhouse #4 (tally 4), not #5 (tally 5)? [user, 2026-06-13].** The Fort Brennand
  pointer carving sits on **outhouse #4**, so the trail leaves the 1–5 tally run **one short of its end** — you'd expect the
  onward clue on the *last* tally, #5. Either **deliberate** (a "4" signal that rhymes with the 4 AM pentagram, the 8 webs, and
  Rockstar's 8/infinity habit — [S20]) or incidental. Open. → [02](../threads/02-butcher-creek-carvings.md)
- **U28. The 3-in-a-row droppings on outhouse #4's roof [investigator, 2026-06-13 — low confidence].** Two large scats + a
  gap + one small scat at the edge above the doorframe, all in a line on the roof of outhouse #4
  ([`butcher-creek_outhouse4-roof-droppings.jpg`](../images/butcher-creek/butcher-creek_outhouse4-roof-droppings.jpg)).
  **Most likely ambient scenery and meaningless** — recorded only because it's *another* oddity clustering on outhouse #4 (the
  `LJ`/`SM` + Fort Brennand + tally-4 stall). No reading proposed; do not elevate without cause. →
  [02](../threads/02-butcher-creek-carvings.md), [butcher-creek.md](../locations/butcher-creek.md)

## Verification debt (claims we're carrying on weak sourcing)
- **U8. [RESOLVED 2026-06-13].** The quote is **Adam Butterworth**, a **former Rockstar QA tester** (now at Remedy), posted
  **5 Jan 2026**: *"Absolutely wild people have found this. I remember hearing about this and thinking it would never be
  discovered."* Confirms the egg is **real/deliberate**, **not** that he authored it. Caveat: single-origin (one X post),
  widely re-reported = **B/C-tier**, not primary-verified. Promoted to [K3](known-facts.md). → [01](../threads/01-spider-dream.md)
- **U9. [RESOLVED 2026-07-05, small residual]** Pole count: **8 + central (9)** vs "9 poles." **Settled: there are
  exactly 8 telegraph-POLE webs** (Cornwall START + 7 more — all labeled since 2026-07-04 in the
  [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md) master table, `spiderdream01–08` + hour codes), **and the 9th site is
  NOT a pole**: both Jan-2026 discovery pieces describe the centre as a **TREE** — RDR2.org (#8): *"a ninth, larger web
  hidden within a tree at the center of the formation"*; Daily Dot (#10): *"At the symbol's center sits a tree in which
  a huge spider's web will appear for only an hour each night."* So the "9 poles" phrasing is a miscount — 8 poles + 1
  non-pole centre site. **Residual (minor):** journalism says *one huge web in a tree*; the primary wiki says *"another
  set of webs"* (plural, featherless, 1–2 AM) that **line up** to spell `N`+pole — likely journalistic compression of
  the same site (the two articles are same-week and plausibly share an upstream), but the centre's exact web count +
  substrate stays unpinned; a 🎮 glance settles it. ⚠️ Boundary-discipline note, recorded so nobody conflates: a lone
  **tree** at the centre invites the [whiskey tree](../locations/whiskey-tree.md) ([S23]) — but the firsthand boundary
  geometry already places the centre web **outside** the triple-overlap sliver the whiskey tree sits in ([K28] pass), so
  they are **distinct trees** on current data. → [05](../threads/05-spider-web-trail-2025.md)
- **U10. [PARTLY RESOLVED 2026-07-05]** Fort Brennand tally counts and the three tower symbols. **Counts CONFIRMED B-tier
  ×2** (wiki + GameRant, [#81] pass): **6** (the fort's one outhouse, five-bar gate + 1) and **7** (gate + 2, above the
  **guard-tower** entrance, exterior; symbols opposite/above the interior doorframe). Symbols 1–2 undisputed (**telegraph
  pole**, **factory + chimney**); **the third is disputed at source level**: wiki "oil puddle" vs the community's own
  verbatim "Oil Puddle **or Register Rock**" ([U24]/[H11]) vs the new Saint-Denis-skyline reading ([S44]). Open residue =
  the third symbol's identity only. → [02](../threads/02-butcher-creek-carvings.md)
- **U11. [RESEARCH HALF ANSWERED — NEGATIVE 2026-07-05 → [#85]]** Whether a literal **"dream" sequence** is triggerable
  in-game, or "dream" is purely thematic. **Answer: RDR2 ships NO sleep-triggered dream machinery at all** (high
  confidence, comprehensive pass): every dream/vision in the game is a **story-scripted cinematic** (the Guarma
  unconscious-dream; the Chapter-6 post-mission honor interstitials — deer vs wolf/coyote; the *Fork in the Road*
  waking trance; the death vision) — none fires from the player choosing to sleep. The wiki's *Sleeping* page (full
  wikitext **re-verified firsthand**) documents the whole mechanic with **zero** dream/vision content — sleep is a
  fade + time-skip + stat restore; no free-roam sleep→vision instance exists in any wiki, guide, or community record
  in ~7.5 years; **no peyote in story mode**; dreamcatcher completion plays no vision; the one datamined dream-flavoured
  script (`dreamanim.c`, [#74]) is **near-empty = cut**. ⟹ The earlier premise here ("RDR2 ships a sleep-vision
  system") was **wrong** — the correction cascades to [H25]: its literal form ("sleep → a dream plays") would need
  machinery the game has never exhibited → **downgraded to mechanically-implausible-on-known-machinery**. The
  defensible weakened form is the **Hani's Bethel UFO pattern** — a *presence-at-hour* event in the waking world, where
  sleeping is merely the time-skip to reach the hour ("you don't need to specifically sleep in the bed — just being in
  the cabin when 2 am arrives is sufficient") — an **established Rockstar pattern** the trail's own hour-gating rhymes
  with. The in-game dream-coda step stays in Tests C/D (it costs ~nothing and the desk negative can't rule out
  engine-side content, cf. [U2]'s checked-but-never-set flags) — but run with recalibrated expectations: **watch the
  wake cycle AND the location at the key hour**, not just the sleep. → [01](../threads/01-spider-dream.md),
  [H25](speculation.md), [decoy-and-dream-hypotheses.md §2](../analysis/decoy-and-dream-hypotheses.md)
- **U12.** What the **guitar** symbol denotes (still "believed to be a guitar" — never confirmed). **Partly answered:** the
  `NW`+guitar marker points to **Fort Wallace** (two guitars there), but Fort Wallace is a **waypoint, not the destination** —
  the trail continues NW past it ([06](../threads/06-bird-carving-giant-wapiti.md)). **Corroborated 2026-06-14 ([#60]):** *every*
  B-tier source **hedges** the guitar ("believed to be", "looks like") — none asserts it; the Fandom wiki (Part 4, speculative)
  explicitly offers rivals — a **shape in the rocks / the map itself pointing NW**, or a **red herring**. So the depiction is
  genuinely contested, not just unstated. **New candidate reading 2026-07-02 → [S34]:** an **hourglass / figure-8** (the black
  widow's field mark — echoing the Black Widow card [K9] — or Rockstar's 8/infinity motif [S20], or simply the "time" icon on
  an hour-gated trail [H13]); checkable against the on-file glyph extraction (guitar needs a neck+headstock; hourglass a
  pinched waist). **⚡ [S34] CHECK RUN 2026-07-05 (desk, on the extraction): GUITAR-LEANING.** The glyph has a **long neck**
  joining the top lobe, **asymmetric solid lobes** (lower > upper = guitar bouts) and a **sound-hole-like waist hole** —
  the hourglass (no neck, no hole, symmetric) and figure-8 (needs two closed loops) fail their own diagnostics; the only
  missing guitar feature is a headstock, so "guitar-like instrument" is now the best-supported reading, still hedged,
  never promoted to [KNOWN]. A "spider on its dragline" rival was weighed and set aside (the same carving family's
  Cornwall spider [S30] has 8 prominent legs; this glyph has none). →
  [05](../threads/05-spider-web-trail-2025.md), [decoy-and-dream-hypotheses.md §3](../analysis/decoy-and-dream-hypotheses.md)

## New leads from the primary wiki (Part 4 — wiki-flagged speculative)
- **U13. [DOWNGRADED 2026-06-13].** **Spider Gorge** — the wiki (Part 4) says NW of the guitar pole "points directly to the
  very tip" of it; it has *"spider"* in the name and a **guitar-shaped section**. **But a deep-research pass found NO secondary
  source corroborates Spider Gorge** — journalism points the `NW`+guitar marker at **Fort Wallace** instead. Keep as
  **wiki-only [SPECULATION]**, not a co-equal destination; verify in-game if visiting the NW area. *(Script-dump aside
  2026-07-05, [#87]: `WATER_SPIDER_GORGE` is a named water volume in the decompiled scripts — the toponym is a first-class
  engine asset, but nothing in the scripts ties it to the webs; changes nothing here.)* → [05](../threads/05-spider-web-trail-2025.md)
- **U14. [RESOLVED-NEGATIVE 2026-06-21].** **Window Rock "Strange Statues" mural** — *do its birds carry a black/red feather
  split that mirrors the **5 black + 3 red** web feathers, making the mural the order key ([H3]/[S12])?* **No.** Two
  independent lines: **(1) the source art has no second pigment** — a pixel test of the colour-faithful wiki texture
  ([`experiments/mural_colour_count.py`](../experiments/mural_colour_count.py), 2026-06-21) finds **100% of chromatic ink red-hued,
  0% any other hue**; the dark "black"-looking figures are deep/shaded red, not black paint (the on-file `_extracted.png` reads
  ~51% "black" only because it was contrast-boosted — its chromatic pixels are *also* 100% red). **(2) Every walkthrough**
  (GamesRadar, Shacknews, ScreenRant, Fandom) codes the mural by feather **count** + **orientation** (upside-down birds = decoys
  → primes `2,3,5,7` → press the matching-finger statues → **4 gold bars**), **never by colour.** ⟹ there is no black/red bird
  set to count; **[H3]/[S12] (mural = order key) are refuted.** The web 5/3 colour grouping itself is unaffected — it rests on the
  boundary data ([H9]/[U29]), not the mural. → [thread 06](../threads/06-bird-carving-giant-wapiti.md)
- **U15.** The **feather pattern** — do the 5 black + 3 red feathers, shot in a specific order/condition, trigger something?
  (Wiki lists this as a live theory.) *(Premise flagged 2026-07-02, [H27]: the "shot" half of this question is itself a
  community import no verified clue supports — under the witness/read grammar the answer is "no, and no shot was ever the
  input"; Test D vs Tests A–C discriminates. → [solve-grammar.md](../analysis/solve-grammar.md).)*
  → [05](../threads/05-spider-web-trail-2025.md)
- **U16. [RESOLVED-NEGATIVE 2026-06-13].** The "letters to Annabella" are **two poems** in the Vetter's Echo desk — the
  **"Dear Annabella Poem"** (*"A poem to a distant lover,"* addressed **To: Annabella**) and an unsigned **"A Day's Walk
  Poem."** Read in full (Red Dead Wiki, B-tier, verbatim in-game text): the recipient is **"Annabella"** by first name only
  (no surname), and the author poem carries **no signature, name, initials, or date** — authorship is attributed to **Vetter**
  (implied **P.H.V.**, after the real hermit Phillip Henry Vetter the cabin homages) only by the *location name*, not the text.
  **So the letters do NOT supply an `E.C.` author/recipient** — "EC" is **solely the matchstick arrangement** on the desk,
  beside the Black Widow card; the wiki itself calls the matches' meaning unknown. A real negative: this closes the "the
  Annabella letters might name the EC initials" lead. The `E–C` pair still dangles (the isolated graph component). → [03](../threads/03-matchstick-letters.md)
- **U23.** The **[Bacchus Bridge empty heart](../locations/bacchus-bridge.md)** ([K22]) — deliberate clue or scenery? Is its
  reported **line of sight to the bird carving** ([K16]) an alignment cue or coincidence? Is it modelled geometry ([K15]) or a
  flat decal like the Flatneck original? ⚠️ **Its relevance to the mystery is contested — about as much as the off-map "?"
  theory** (user, 2026-06-13): the heart is real (investigator data), but **whether it relates to the spider trail at all is
  unproven**. It sits **past the last verified clue** ([K16]); don't present it as an established step. →
  [06](../threads/06-bird-carving-giant-wapiti.md)
- **U17. [REFRAMED 2026-06-13]** The lingering log entry is the **dreamcatchers' side mission**, *not* the spider mystery's.
  **Correction:** an earlier draft said the spider mystery "doesn't disappear from the log" — wrong; the **spider mystery has
  no log at all** ([K20](known-facts.md)). The *Dreamcatchers* wiki files its own never-clearing entry under **Oversights**
  (a bug); the spider wiki only cites it **by analogy**. **The live question (H8):** is the dreamcatcher entry stuck because
  there is **something left to finish — possibly the spider mystery itself**? If so, **completing the spider mystery would
  clear the dreamcatcher log** — a **falsifiable** prediction, currently untested. Separately, the strongest dreamcatcher↔spider
  ties are *thematic/mechanical* (a dreamcatcher is a **spider-web-shaped, dream-themed Native craft**; reward = **connect 20
  points → drawn animal → treasure in its eye**, the web trail's own mechanic). Full write-up →
  [analysis/dreamcatchers.md](../analysis/dreamcatchers.md). → [01](../threads/01-spider-dream.md)

## Outward connections (treat skeptically)
- **U18. [PARTLY ANSWERED 2026-06-13].** **GTA V Mount Chiliad** has **two** cable-webs that spawn **1–2am** (same window as
  RDR2's centre webs). Now confirmed ([K24]): they are **base-game since GTA V's 2013 launch — not added by any update** — and
  use the **same cable shader** as RDR2's webs ([K15]). So in **both** games the webs are original-to-launch; only the 2019
  Nazar number was a later add. The **shared shader + shared 1–2 AM gate argue this is deliberate**, not coincidence — but
  there is still **no confirmed shared solution**. Link popularized ~Jan 2026 (Oddheader). →
  [gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md), [05](../threads/05-spider-web-trail-2025.md)
- **U19. [PARTLY ANSWERED 2026-06-13].** The **Madam Nazar "Nazar Speaks"** fortune machine (GTA Online, **Diamond Casino
  Heist, Dec 12 2019**) is a **confirmed bridge** between the franchises: the **same machine** both gives the cryptic *"I see a
  web, still tangled after years of unraveling. Will you be the one?"* fortune **and** speaks Gertrude's number `1237645112`
  ([K23]) — and several other fortunes name RDR2 places (**Window Rock, Roanoke Ridge, Grizzlies**, [S14]). The *"web…
  unraveling"* line is now **confirmed a real in-game fortune** (#44). Open: is it a deliberate wink at *this specific* egg, or
  generic spider/fortune flavour fans retro-fitted? Note Madam Nazar is, in-fiction, a **guide to hidden things** (RDO Collector
  role). → [01](../threads/01-spider-dream.md), [gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md)
- **U20.** **Spider Grandmother** (Native American myth) — does the intended solution require the game's Native storyline?
- **U21.** Any real link to "Birds of Paradise" plants or a **GTA VI** tease? Currently unproven.
- **U31.** **Does the Francis Sinclair cabin mural ([K32]) encode any deliberate solvable content — a cipher, numbers,
  text, coordinates — or is it a narrative-only time-travel gag with no payoff?** The "time traveller" *story* reading is
  settled; the **mural-as-puzzle** is not. The community is **still actively mining it** (a r/reddeadmysteries "Francis
  Sinclair Revisited" thread analyses *"potential calculations and text on the mural,"* and a divergent **"beta mural"**
  image circulates — so even the *final* mural's contents aren't community-settled, let alone decoded). **This rhymes with
  the corpus-wide [U2]** (is there a payoff at all). **Sub-question:** the precise re-entry condition ([K34]) — a true
  **100%-completion gate** (user/community) or just the door-lock a **save/reload** defeats (wiki)? Resolving it decides
  whether [S27]'s "deferred study-at-the-end" reading has any legs. **HQ image ON FILE** (user-supplied,
  [`francis-sinclair_cabin-mural_hq.jpg`](../images/francis-sinclair/francis-sinclair_cabin-mural_hq.jpg), 2822×2117) and
  the **close-crop pass is DONE (2026-06-21, 4×3 grid, 2× upscaled — full motif inventory in
  [thread 08](../threads/08-francis-sinclair-mural.md)): NEGATIVE for an obvious encoded payload.** No legible lettering,
  number string, cipher table, grid, or [K25]-style coordinate annotation appears on the mural **or** the pinned
  rock-carving sketches; the "text-like" marks resolve into **decorative pseudo-glyph noise**. It reads as a Diego-Rivera-
  style **future→portal→antiquity time-collage** assembled from the ten carvings. ⚠️ Negative is glanceable/close-crop, not
  a proof of "no hidden puzzle" (CLAUDE.md: a negative is a real finding) — but nothing here *invites* a solve, so **[U31]
  stays open with priority dropped.** Separate egg — pursuing it does **not** imply a spider link ([S26]). →
  [08](../threads/08-francis-sinclair-mural.md)
- **U32. ✅ RESOLVED 2026-07-02 — the mapping IS publicly sourced (C-tier) → [K39].** The number→location assignment was found
  in the wild: **u/Artem_ab6's datamine comment** in the r/reddeadmysteries master thread ([#65], 2026-01-02 — *"located
  in-game coordinates for each of the feathers… the order according to the game files (testing)"*), with a map overlay
  (saved: [`web_map-overlay_file-numbers_datamine.png`](../images/webs/web_map-overlay_file-numbers_datamine.png)) that
  **matches the WEBS-MANIFEST 8/8**; the community site's 1/1/2026 timeline entry credits the same find (same origin, not
  independent). So option (i) below is the answer — **genuine community datamine, back-fit-by-us ruled out** — and [S29]
  activates as a live C-tier lead. Residual caveats live at [K39] (single dataminer, "(testing)", unreproduced). The [#59]
  "Clockwise Order" turned out to be that author's own photo-labelling sequence, not a rival file-mapping. *Original
  question kept below for the record:*
  **Is the per-web `spiderdream0X` → location mapping SOURCED, or an unsourced/back-fit assignment? [desk audit, 2026-06-21].**
  The [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md) assigns a specific internal file number to each web (Cornwall=`spiderdream03`,
  Ringneck=`spiderdream01`, …) and that mapping is **propagated into location dossiers** (cornwall-kerosene-tar, heartland-oil-fields).
  But **no source in the corpus maps a number to a location** — only the *range* `spiderdream01–08` is sourced ([K13a], GameRant
  #35 / primary wiki). The per-location numbers have sat in the table **since the first commit with no citation**, and they are
  **not** the only documented per-web ordering (the #59 post's *"Clockwise Order"* numbers Overflow=1…Oil Fields=8 — a *different*
  sequence). **And the numbering is structurally too clean to be arbitrary** ([`web_file_number_structure.py`](../experiments/web_file_number_structure.py)):
  files **1–5 = exactly the 5 blacks, 6–8 = exactly the 3 reds**, the two untwinned 5–6 AM blacks sit at 1–2, and every hour-twin
  pair **sums to 11** (B23↔R23 = 5+6, B45↔R45 = 4+7, B34↔R34 = 3+8) — odds **≈1/3360** under random labeling. That cleanliness is
  **double-edged**: either (i) a genuine datamine the devs numbered deliberately (→ real evidence colour is a first-class axis,
  [S29]) or (ii) numbers **back-fit to the KNOWN colour×hour lattice** by an earlier session/community source (→ circular, no
  evidentiary weight). Can't tell from inside the corpus, and (ii) is the Occam reading for an uncited datum. **Resolve by sourcing
  the datamine number→location mapping, or downgrade the numbers to a flagged assignment.** Upstream of the [K16] frontier. →
  [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [S29](speculation.md)

- **U35. [MAIN QUESTION ADJUDICATED 2026-07-05 → [#84]] What gates the Strange Man portrait's 4th/final visit? And what
  advances a "visit"? [Strange Man corpus pass, 2026-07-02].** The two B-tier sources disagreed (wiki: "**after the
  epilogue**"; Gameranx: "**100% Completion**"). **A dedicated research pass settled the headline: the gate is
  POST-EPILOGUE + 4 unique visits with multi-in-game-day spacing (as John) — NOT 100%.** Counterexamples run both
  directions (finished portrait + mirror + journal at **88%** completion, `llc7lq` re-verified verbatim; a
  "still not finished after 100%" GameFAQs report); an OP-solve is explicit (*"It just requires being in the
  epilogue"*); and the 100% claim **traces to its origin** — a 2018 correlation guess (`9wuk1g`: 95–100% players have
  necessarily finished the epilogue + passed many days) that Gameranx and aggregators propagated. **Still open (narrow
  residual):** the exact stage-advance mechanic (visit count with a ~3-day cooldown vs pure days-elapsed) and whether
  **Arthur-era visits count** (wiki says John-only; two firsthand reports say per-chapter progression as Arthur; one
  unverified 2018 anomaly reports the apparition *as Arthur*). Practical for [S35]: baseline portrait state on a
  post-epilogue <100% save is predicted by **prior visit count**; and one finished-portrait-but-no-apparition report
  means a missing mirror apparition is **not** a spider-state signal. →
  [locations/strange-man-shack.md](../locations/strange-man-shack.md), [S35](speculation.md), src [#84](../sources/sources.md)

#### Mount Shann sundial — a *separate* mystery (thread 09, user request 2026-07-02)
- **U33. What do the sundial's 7 arrows encode, and is the red/orange/yellow colour-coding meaningful?** Documented behaviour
  is thin: **one arrow → the cult hut**, some **→ spots with collectible stones**, others **→ "nowhere."** Firsthand in-game,
  cross-checked over **two full day/night cycles** (user, 2026-07-02; high-trust, user notes exact times may not be perfectly
  precise): each arrow aligns with the **gnomon's shadow** at a **time + cardinal** — Red 6 am W · Orange 9 am WNW · **Yellow
  11:30 am NNW** · Orange 1 pm N · Red 2 pm NNE · Orange 3 pm ENE · Red 6 pm E — covering only the **daytime half** (sunset ~8 pm
  leaves the night half unmarked), with **yellow appearing exactly once, uniquely on a half-hour.** So the arrows **do** work as
  a shadow-clock (observed); **open** is whether the clock *also* encodes pointers / a colour-key, or is faithful set-dressing.
  **⚡ DECODE BRANCH CLOSED-NEGATIVE (desk, 2026-07-02 — [`sundial_decode.py`](../experiments/sundial_decode.py),
  [results](../experiments/results/sundial_decode.md)):** the arrows fit a **physically faithful shadow clock**
  (monotone bearings p≈0.0014; solar-model fit p≈0.0004; residuals inside the ±45 min observation slack) — so
  **bearing ≡ f(time)** and an arrow cannot be freely "aimed"; times-as-numbers/letters null (A1Z26 `FIKMNOR`/`FIKABCF`);
  the colours resolve into a **major-tick/half-tick decorative grammar** (each orange = the exact midpoint of a red and
  noon; **yellow ≈ the noon marker** — its "special outlier" status deflates to "the dial marks near-noon distinctly").
  **What remains open in U33 is only the in-game POI question** — do the documented cult-hut / collectible-stone
  alignments hold (i.e. were the *times chosen* to select targets)? Coordinate-blocked at the desk; an in-game/mapping
  task. → [09](../threads/09-mount-shann-sundial.md), [mount-shann.md](../locations/mount-shann.md)
- **U34. Is the Mount Shann egg connected to the Spider Dream Mystery, or only via the shared Mount Chiliad homage?** The only
  sourced bridges are [K38]+[K24] (both nod to GTA V Chiliad) and a shared **~2 AM** gate ([K11] centre webs 1–2 AM; [K37] UFO
  2 AM). No source links the sundial to the spider trail directly. Held **skeptical** — most likely two independent "mountain +
  UFO + time-gate" eggs, not one puzzle. → [09](../threads/09-mount-shann-sundial.md)

---

*When you close one of these, edit it here, update the relevant thread, and add a line to
[INVESTIGATION_LOG.md](../INVESTIGATION_LOG.md).*

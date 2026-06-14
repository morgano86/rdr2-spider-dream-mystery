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
  The raw per-instance entity placement would upgrade these C-tier reads to A-tier but is **no longer needed to characterise**
  the socket. Re-confirmed: deliberateness is in **placement**, not unique files (shared `wap_gen_feather01` + 4 reused
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
  **New lead toward cut-content (2026-06-13, Reddit C-tier, unverifiable):** a datamine write-up (u/C0d3M3chan1c, "gamedev take,"
  201 pts, **since removed by mods**) reports scanning 1,639 decompiled scripts + 2,000+ data files and finding **two persistent
  flags that are *checked* but **never *set*** by any script** — i.e. a payoff gated on a state nothing in the shipped scripts
  ever turns on. *If accurate*, that's the strongest technical argument yet that the trail is **incomplete/cut** (or finished
  engine-side, beyond script reach). Treat as a lead, not proof: single C-tier author, post deleted, no independent
  reproduction. → [source #52](../sources/sources.md)
  - **Candidate payoff LOCATION (2026-06-14, [H21], speculative):** if a payoff exists, the oversized B34 boundary ([K28],
    uniquely holding **Butcher Creek** inside a zone, forts excluded) makes **Butcher Creek (or Valentine)** the natural place a
    **state-gated** result would surface — reachable from the webs with shot-state intact ([K21]). This **dovetails with the
    "checked-but-never-set flags" lead** in a pointed way: H21's predicted state-setter would be *exactly such a flag* — so
    either web activation **is** what sets it (and the script-scan missed an engine-side/out-of-scope setter), or it genuinely is
    **never set** (→ the gate can't fire → cut content). Distinguishing these is the crux. ⚠️ No payoff ever confirmed; do not
    present Butcher Creek as a destination. → [H21](speculation.md), [K28](known-facts.md)
- **U3. One puzzle or two?** Are the 2018-era Butcher Creek→Fort Brennand→Oil Fields clues and the 2025 telegraph-pole web
  trail the **same** puzzle, sequential stages, or parallel Easter eggs sharing motifs? **New argument toward "one puzzle"
  (2026-06-14, [S22]/[H21]):** the web respawn-boundary mechanic ([K21]) provides a *mechanical* (not just thematic) tie — B34's
  oversized North boundary uniquely **encompasses Butcher Creek** (forts excluded, [K28]), so the games-script could preserve the
  web shot-state on a trip back to the 2018 origin site, echoing the [K8] pointer. Speculative; Valentine's inclusion (no mystery
  role) is the counter. → [H21](speculation.md), [K28](known-facts.md), [connections §5a](../analysis/connections.md)

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
- **U4. What do `LJ` and `SM` mean?** Developer initials (community default) vs. in-fiction clue (user hypothesis). Test
  against character names and against the `J+M` matchsticks. **Gang name-list now built ([thread 07](../threads/07-van-der-linde-roster.md)):**
  `SM` = **Sean MacGuire** is an **exact** one-person hit ([S16]); the gang also supplies the `L` (Lenny/Leopold) absent from
  Register Rock. Suggestive, not proof (coincidence-odds caution). → [02](../threads/02-butcher-creek-carvings.md), [connections](../analysis/connections.md)
- **U5. What do the matchstick letters MEAN?** Locations now pinned: `EC`=Vetter's Echo, `J+M`=**Cornwall K&T (web-trail
  start)**, `S+J`=Caliga Hall (Gray estate); arrow set location still TBD. **Open:** the cipher/relationship — are they
  names? do letters pair with places? **Dev-initials reading is weighted DOWN** (thousands of staff → coincidental match is
  near-certain; only founders/senior leads plausible). **Gang cross-check ([thread 07](../threads/07-van-der-linde-roster.md)):**
  `J+M` = **John Marston** is an exact hit ([S16]); **`EC` matches nothing** in any name source ([S17], investigator's point —
  its non-match argues the initials are deliberate). **Number-reading alternative ([S21]):** read as A1Z26 with the `+` as
  *add* and bare pairs *concatenated* → `EC`=53, `J+M`=23, `S+J`=29 (all prime; `EC`=53=the 5/3 feather split) — weak but live.
  → [03](../threads/03-matchstick-letters.md), [connections](../analysis/connections.md)
- **U6. Gertrude's number sequence — [PARTLY RESOLVED 2026-06-13].** The **opening is now multi-outlet sourced**: she begins
  `1 2 3 7 6 4 5 1 1 2` (`123 7645112`), which Rockstar **deliberately echoed cross-game** — the **Madam Nazar "Nazar Speaks"**
  machine in **GTA Online** speaks the same string ([K23]). ⚠️ **Chronology (corrected, user-flagged):** the number is
  **RDR2-original (base game, Oct 2018)**; the GTA echo is a **later callback (Dec 2019)**, so it **corroborates that the
  number is intentional** rather than explaining it away. **Still open:** the exact **tail** past `1237645112`, whether the
  loop is identical, what (if anything) it encodes, and **which** mystery it serves — the **spider trail**, a **standalone
  Braithwaite/Nazar puzzle**, or nothing decipherable. The GTA crossover doesn't decide that; the only thing arguing *against*
  a spider link is a C-tier community exposé ([#43]) alleging the "Gertrude solved → spider web" *video* is a **hoax**. Tracked
  cross-game in [gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md). → [04](../threads/04-gertrude-numbers.md)
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
- **U7. The tally counts as a sequence.** Butcher Creek 1–5, Fort Brennand 6 & 7 — is the count itself the message (a
  running 1,2,3,4,5,6,7…)? Does Gertrude's sequence (which reaches ~10–11) continue it?
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
- **U9.** Pole count: **8 + central (9)** vs "9 poles." Confirm and label each. → [05](../threads/05-spider-web-trail-2025.md)
- **U10.** Fort Brennand tally counts (6 and 7) and the precise three tower symbols. → [02](../threads/02-butcher-creek-carvings.md)
- **U11.** Whether a literal **"dream" sequence** is triggerable in-game, or "dream" is purely thematic. → [01](../threads/01-spider-dream.md)
- **U12.** What the **guitar** symbol denotes (still "believed to be a guitar" — never confirmed). **Partly answered:** the
  `NW`+guitar marker points to **Fort Wallace** (two guitars there), but Fort Wallace is a **waypoint, not the destination** —
  the trail continues NW past it ([06](../threads/06-bird-carving-giant-wapiti.md)). **Corroborated 2026-06-14 ([#60]):** *every*
  B-tier source **hedges** the guitar ("believed to be", "looks like") — none asserts it; the Fandom wiki (Part 4, speculative)
  explicitly offers rivals — a **shape in the rocks / the map itself pointing NW**, or a **red herring**. So the depiction is
  genuinely contested, not just unstated. → [05](../threads/05-spider-web-trail-2025.md)

## New leads from the primary wiki (Part 4 — wiki-flagged speculative)
- **U13. [DOWNGRADED 2026-06-13].** **Spider Gorge** — the wiki (Part 4) says NW of the guitar pole "points directly to the
  very tip" of it; it has *"spider"* in the name and a **guitar-shaped section**. **But a deep-research pass found NO secondary
  source corroborates Spider Gorge** — journalism points the `NW`+guitar marker at **Fort Wallace** instead. Keep as
  **wiki-only [SPECULATION]**, not a co-equal destination; verify in-game if visiting the NW area. → [05](../threads/05-spider-web-trail-2025.md)
- **U14.** **Window Rock "Strange Statues" mural** — birds with differing black/red feather counts (cf. the **5 black + 3
  red** web feathers!) and many symbols. Does the feather count encode a reading of the mural? → [05](../threads/05-spider-web-trail-2025.md)
- **U15.** The **feather pattern** — do the 5 black + 3 red feathers, shot in a specific order/condition, trigger something?
  (Wiki lists this as a live theory.) → [05](../threads/05-spider-web-trail-2025.md)
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

---

*When you close one of these, edit it here, update the relevant thread, and add a line to
[INVESTIGATION_LOG.md](../INVESTIGATION_LOG.md).*

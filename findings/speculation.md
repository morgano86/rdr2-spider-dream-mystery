# Speculation (explicitly unconfirmed)

Theories — community and our own. **None of this is established.** Each entry notes who proposed it and how testable it is.
Keep hype quarantined here so it never contaminates [known-facts](known-facts.md).

## On the letters L, J, S, M
- **S1 (user).** `LJ`/`SM` on outhouse #4 are **in-fiction clues, not dev initials.** Testable: do `L`,`J`,`S`,`M` match
  character names, or decode via a cipher that aligns with the `J+M` matchsticks? → [connections](../analysis/connections.md)
- **S2.** The four letters form **two pairs** (`LJ` + `SM`, or `J+M` + leftover `L`,`S`) naming **two couples / four people**
  tied to Butcher Creek or the Braithwaites. Untested — needs a name list.
- **S3.** `J+M` (matchstick "lovers' carving") names a **romantic pair**; the same J and M appear in the toilet carving but
  "connect differently," hinting the puzzle wants you to **re-pair the letters.**
- **S16 (2026-06-13).** The letters encode **Van der Linde gang members' initials.** The gang roster ([thread 07](../threads/07-van-der-linde-roster.md))
  yields **two EXACT one-person hits — `SM` = Sean MacGuire, `J+M` = John Marston** — both major characters, and it supplies
  the **`L`** (Lenny Summers / Leopold Strauss) that **Register Rock lacked** ([U24]). Tested in
  [`experiments/name_match.py`](../experiments/name_match.py). **Caution:** with ~27 members some overlap is expected by chance
  ([S13] reasoning); the *signal* is that the exact hits are plot-central and land on markings already tied to nodes (Sean's
  killers are the **Grays** → Caliga Hall `S+J`). ⚠️ **SOFTENED (2026-06-13, [`initials_likelihood.py`](../experiments/initials_likelihood.py)):**
  the coincidence-odds calc shows 2-of-5 hits is **weak** evidence — P≈0.04 under uniform letters but **≈0.59** under a realistic
  name-initial-frequency null (the markings use the commonest initials J/S/M). The **count proves little**; S16 rests only on the
  unmodellable point that the hits are *major* characters. **Suggestive, not evidence.** → [thread 07](../threads/07-van-der-linde-roster.md), [connections](../analysis/connections.md)
- **S17 (investigator, 2026-06-13).** **`EC`'s persistent non-match is itself a sign the initials are deliberate.** Of the five
  markings, four sit at mystery nodes / map to characters, but **`EC` — placed beside the Black Widow spider card, the most
  on-theme object — matches nothing**: the Annabella poems are **unsigned** ([U16] resolved-negative), no Register Rock person,
  no gang member, no `E`-first-name anywhere. A *mundane* background detail would be as forgettable as the rest, not the
  spider-flagged one no in-fiction name explains — which raises the prior that the letters were **chosen, not incidental.**
  ⚠️ **Argument from absence:** strengthens the case for *deliberateness*, decodes nothing; the wiki still records the matches'
  meaning as unknown. → [thread 07](../threads/07-van-der-linde-roster.md), [thread 03](../threads/03-matchstick-letters.md)

- **S18 (2026-06-13).** `EC` rendered in **A1Z26 = 5, 3** — exactly the **5-black / 3-red feather split** ([K13]) — and `EC`
  is the one marking placed **beside the Black Widow spider card.** Surfaced by [`letters_cipher.py`](../experiments/letters_cipher.py).
  Ties the otherwise-unmatched `EC` to the trail's core 5/3 structure. **Weak:** small integers, many letter-pairs sum low, so
  coincidence-prone — recorded per [S13], not leaned on. → [connections §1a](../analysis/connections.md)
- **S21 (user, 2026-06-13) — the matchsticks read as NUMBERS, with the displayed punctuation choosing the operator.** A
  number-reading **alternative** to "people" ([S2]/[S3]/[S16]): map A1Z26 (A=1…Z=26), then let the format pick the operation —
  a **`+` pair is added**, a **bare pair is concatenated**. So `J+M` = 10+13 = **23**, `S+J` = 19+10 = **29**, and `EC` (bare,
  no `+`) = 5,3 = **"53"**. That gives the matchsticks as **three numbers {53, 23, 29}** or **one number "532329"** (the carved
  pairs extend it: `LJ`→1210, `SM`→1913). **What's interesting (and what isn't):** 🟢 all three matchstick values are **prime**
  (cf. the Window Rock mural's prime feather-counts 2,3,5,7, [K18]); 🟢 **`EC` = 53 = the 5-black/3-red feather split** ([K13]),
  reinforcing [S18] (and `EC` sits by the Black Widow card); 🔴 but the set matches **no** known number line — not Gertrude's
  `1237645112` ([K23]), not the 1–7 tallies, not "five poles west." **Weak and coincidence-prone** (small integers; the
  operator rule is chosen to fit) — recorded as a live candidate, not leaned on. Arithmetic verified in
  [`number_grid.py`](../experiments/number_grid.py). → [connections §1a](../analysis/connections.md), [U5](unknowns.md)
- **S19 (2026-06-13).** Some letters may be **RDR2 place-abbreviations, not names.** Gazetteer pass: 🟢 `EC` = **Emerald
  Crossing** (a real, HUD-hidden E.C. crossing by Emerald Ranch — but a different region from Vetter's Echo where the `EC`
  matches sit); 🟢 `SM` = **Scarlett Meadows** (exact region, and it *contains* Braithwaite Manor + Caliga Hall — the mystery's
  family estates). 🔴 **But** `LJ`/`J+M`/`S+J` have **no viable place reading** — RDR2 has essentially **no `J`-named locations**
  (only *Jorge's Gap*), yet `J` is in three markings; and **no community source** ever proposed a place reading. So the
  location idea survives only for `EC`/`SM`. → [connections §1a](../analysis/connections.md), [thread 03](../threads/03-matchstick-letters.md)

## On the numbers
- **S4.** Butcher Creek tallies (1–5) + Fort Brennand (6,7) are a **single running count**; Gertrude's higher numbers
  (~10–11) **continue the sequence** — i.e., all the "numbers" threads are one counter. Testable by alignment. *(Note
  2026-06-13: Gertrude's opening is now confirmed [K23] and is **RDR2-original**, so it's a fair input to test — but it's also
  the Nazar phone-style string, so a "continuation" match would need independent support. The BC/Brennand 1→7 count stands
  on its own regardless.)*
- **S5.** Gertrude's sequence is a **cipher/coordinate/date.** E.g., A1Z26 letter-mapping, or digits as map-grid refs, or as
  "count N poles" instructions echoing the trail's "five poles west." Run the attempts in
  [connections](../analysis/connections.md). *(Note 2026-06-13: still live. The opening `1237645112` is confirmed and
  **deliberate** ([K23]) — Rockstar even echoed it cross-game via Nazar — so it's worth trying to decode; A1Z26 already
  returned null. What's unsettled is **which** mystery it keys, not whether it's intentional.)*
- **S20 (user, 2026-06-13) — a number/timing motif.** Separate from what the numbers *say*, a few **structural** numbers
  recur: **8** webs ([K13a]); the floorboard pentagram at **exactly 4 AM** ([K5]); the chain branching from outhouse **#4**,
  not #5 ([U27]). Rockstar has a **documented 8 / infinity affinity** — GTA V's *Infinite Eight* (Infinity Killer, Merle
  Abrahams) hides **8** bodies under the slogan *"8 is just infinity stood up."* So a deliberate **8**/**4** would be in-house
  numerology. **Explicitly pattern-seeking and weak** — small numbers recur by chance and each has a mundane reading — so a
  **prompt to watch the numbers**, not evidence. → [connections §3](../analysis/connections.md), [U27](unknowns.md)

## On "DREAM"
- **S6.** **"KEEP YOUR DREAMS LIGHT"** at the oil fields is an intentional **signpost/instruction** for the *dream* trail
  (come at night / carry a light / don't lose the thread), not a coincidental cheat-code carving.

## On the destination
- **S7.** The trail's **N → W×5 → NW + guitar** ends at a **buried reward / playable song / cutscene** near Fort Wallace —
  OR the puzzle is **unfinished/cut content** OR a **deliberate dead-end troll.** Community split; unresolved.

## Outward / meta
- **S8.** Connection to **GTA V Mount Chiliad** mystery aesthetics (UFO/jetpack-style slow-burn ARG). *(Now grounded by [K24]:
  GTA V's Mt Chiliad webs are base-game since 2013, same shader + 1–2 AM gate as RDR2 — see
  [gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md).)*
- **S9.** Tie to **"Birds of Paradise"** exotic plants or other RDR2 collectibles.
- **S10.** A **GTA VI tease** — popular framing in late-2025 coverage; pure speculation, no Rockstar confirmation.
- **S14 — Nazar's fortunes wink at the mystery's nodes.** The GTA Online **"Nazar Speaks"** machine's lines name several of our
  mystery's own places — **Window Rock** ([U14]), **Roanoke Ridge** (Butcher Creek's region), the **Grizzlies** (thread 06),
  plus the *"web…unraveling"* fortune ([U19]) and **Gertrude's number** ([K23]). Madam Nazar is in-fiction a **guide to hidden
  things** (RDO Collector role), so a deliberate wink would be in character. **Weak though:** Nazar references **~16+** RDR
  places spread map-wide, and our nodes are also map-wide, so **some overlap is expected by chance** — a prompt to look, not
  evidence. Raised above coincidence only by a fortune naming something **unique** to the spider trail (Cornwall start-pole,
  Fort Wallace guitars, the bird carving) — **none found so far**. → [gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md)

## On the cheat codes (user lead)
- **S11 (user).** RDR2 **cheat codes are phrases** (e.g., **"KEEP YOUR DREAMS LIGHT"** carved at the oil fields), and several
  phrases *feel* thematically loaded for this mystery. Worth cataloguing all cheat phrases + where each is found in-game, and
  flagging the dream/spider/animal/fate-themed ones. Explicitly **SPECULATION** — phrasing resonance is not evidence. Full
  list being compiled → [analysis/cheat-codes.md](../analysis/cheat-codes.md).

## On the feathers (5 black / 3 red)
- **S12.** The **5 black + 3 red** feather split may encode the **order** to read/shoot the webs (a binary or grouped
  sequence). Cross-check against the **Window Rock Strange Statues mural**, which depicts **birds with differing black/red
  feather counts** — if the counts match, the mural may *be* the order key. → [images/webs/WEBS-MANIFEST.md](../images/webs/WEBS-MANIFEST.md)
- **S15 (Reddit "Zoological", u/Suspicious-Ad6283 — C-tier).** The web feathers are **Northern Cardinal feathers**, and the
  **5-black/3-red split is sexual dimorphism** — 5 ♀ (brown, dark in low light) + 3 ♂ (red) — the giant orb-weavers having
  caught/eaten cardinals. Cited support: the in-game cardinal model
  ([`cardinal_female-in-flight_feather-reference.jpg`](../images/webs/cardinal_female-in-flight_feather-reference.jpg) — ♀ wings
  are red-edged over a brown body, red tail) and the **dreamcatcher-outfit crafted hat**, which is trimmed with cardinal
  feathers. If true this reframes the colour question as **zoological flavour, not a cipher** — a *deflationary rival* to
  **S12/[H3]/[H5]** rather than a key. **Caveat (must reconcile):** dimorphism is red-vs-**brown**, but the game files + wiki
  call the dark feathers **black** ([K13](known-facts.md)); the two captured feathers we now hold (one clearly red, one very
  dark) don't settle brown-vs-black. Testable: sample each web's feather colour against male/female cardinal plumage.
  → [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [U14](unknowns.md)
- **S22 (user, 2026-06-14) — B34/Cornwall's North boundary is OVERSIZED and may deliberately encompass Butcher Creek.** The
  lone-black North boundary ([K28]) extends **far beyond** what its single B34 spawn needs, reaching west to **Valentine** and
  east to **Butcher Creek** (investigator data — the extent; the *meaning* is the user's speculation). The tantalising part:
  **Butcher Creek is the 2018 origin thread** (the 5 outhouses, the pentagram, the `LJ`/`SM` letters and the Fort Brennand
  pointer, [K4]–[K7]), and that very pointer **already points at this exact Cornwall pole** ([K8]). So the boundary geography
  would **echo the documented narrative pointer** — Butcher Creek → Cornwall — putting the mystery's *start* (2018 occult thread)
  and the web-trail's *index pole* inside **one zone**. That is an argument toward **"one puzzle, not two"** ([U3]), and yet
  another way the index pole **B34 behaves unlike the other seven** (lone North member, suspected last feather [U29], now an
  oversized home boundary). ⚠️ **Counter (keep honest):** the same boundary also sweeps up **Valentine**, which has **no known
  mystery role** — so the large extent may simply be **coarse boundary design**, making Butcher Creek's inclusion incidental.
  Testable: map the North boundary's actual edges; check whether it stops *at* Butcher Creek (suggestive) or sprawls
  indiscriminately past it (coarse). Recorded as a lead, **not promoted.** ⚠️ **Updated 2026-06-14 (later investigator pass):**
  the same boundary **also envelops Fort Brennand** (earlier mis-recorded as outside) — so the top zone holds **both** 2018-origin
  Roanoke nodes (Butcher Creek **and** Fort Brennand), which **strengthens** the "echoes the narrative pointer" reading (the
  zone now covers the whole BC→Fort Brennand→Cornwall origin chain, not just one node), though **Valentine**'s inclusion (no
  mystery role) remains the coarse-design counter. The "uniquely Butcher Creek" framing is **withdrawn**. → [K28](known-facts.md),
  [U3](unknowns.md), [connections §5a](../analysis/connections.md)
- **S23 (investigator, 2026-06-14) — an anomalous red-hue ever-smouldering fire-pit motif recurs at mystery sites.** Firsthand:
  the **Butcher Creek pentagram glows a very specific hue of red** ([K5]); the **same unusual red hue** appears in an
  **ever-smouldering fire pit at Fort Brennand** and in an **ever-smouldering fire pit at the [whiskey/bottle tree](../locations/whiskey-tree.md)**.
  Ever-smouldering pits in *exactly* this red are unusual in RDR2, and the whiskey tree sits in the **triple-boundary overlap**
  ([K28]) and is **visible (high vantage) from most web locations.** 🟢 The fire-pits' *existence* and shared hue are investigator
  data; 🔴 **any tie to the spider mystery is [SPECULATION]** — colour-matching by eye is error-prone, RDR2 reuses fire VFX, and
  there is **no confirmed link** between the whiskey tree and any mystery node. Recorded as a **visual-motif lead** to test (do
  the hues actually match a single asset/emissive value; do other mystery POIs carry the same pit?), **not promoted.** →
  [whiskey-tree.md](../locations/whiskey-tree.md), [K5](known-facts.md), [K28](known-facts.md)

## On method / how the egg may hide its clues
- **S13 (user) — plausible-deniability camouflage.** A clue may be **deliberately chosen to double as a real-world or
  pop-culture reference** (a "dev in-joke," a famous name, an obvious gag) so that players **dismiss it** and never test its
  in-game role. Example: Register Rock's **A. West / B. Ward**, which the wiki *speculates* are Adam West / Burt Ward
  (*Batman*) — unconfirmed, and even if true that wouldn't exclude them from the puzzle. **Consequence for us:** an apparent
  outside reference is **not** grounds to discard a candidate name/symbol — keep it live and let a test decide. This is the
  **inverse caution** to the anti-pareidolia [carving test](../analysis/carving-technique.md): that one stops us seeing clues
  where there are none; this one stops us *missing* clues dressed up as jokes. Applies to [H11]/[U24] and more broadly.

## Our own working hypotheses (log new ones here)
*Rollup of every `H#`. Full write-ups live in the analysis file noted; keep this list complete — see
[INDEX.md](../INDEX.md) for the registry.*

- **H1.** The mystery is **layered by era of discovery**: occult/pentagram flavor (surface) → symbol-pointer chain
  (Butcher Creek→Brennand→Oil Fields) → telegraph-web directional puzzle (2025) → unknown payoff. The "DREAM" carving sits
  at the seam between the pointer chain and the web trail, which is why it's at the Oil Fields.
- **H2.** The **outhouse motif is the connective tissue**: Butcher Creek (outhouse tallies), Fort Brennand (outhouse
  tallies), Gertrude (dies in an outhouse, recites numbers). If true, Gertrude is **not** disconnected — her outhouse is a
  fourth tally-node. Test by checking for tally marks in/near Gertrude's outhouse and whether her numbers index the others.
  *(Note 2026-06-13 — [K23] (corrected) + the #43 hoax exposé: Gertrude's numbers are confirmed deliberate but **RDR2-original**
  (the GTA/Nazar echo is a later callback, not a debunk), so H2 isn't undercut by chronology. The genuine caution is the
  C-tier hoax exposé, which disputes the Gertrude↔spider video specifically — so keep "Gertrude is a 4th node" as an open
  hypothesis, not an assumption. See [connections §2](../analysis/connections.md).)*
- **H3.** The **Window Rock "Strange Statues" mural's black/red bird counts equal the webs' 5 black / 3 red**, making the
  mural the **order key.** Test: count the mural birds *by colour* (high-res mural images exist — [U14], [EVIDENCE-CHECKLIST](../EVIDENCE-CHECKLIST.md)).
  → [connections.md](../analysis/connections.md)
- **H4. ⚠️ REFUTED-leaning (2026-06-13).** **Feather orientation encodes the shooting order** (each feather points toward the
  next web/pole) — the user's lead, the motive for capturing [U0]. **Now tested against the full 8-web photo set** (u/dropthepress,
  [#59], front+side of every web → [`feather-positions/`](../images/webs/feather-positions/)): **every feather hangs tip-down by
  gravity** — there is no per-web heading to read. Combined with [U29] (multiple orders work within a colour group, so no unique
  "next-target" exists to encode), the orientation form is **dead**. **Salvage:** only the weaker *attachment-point* (which
  radial/quadrant) varies between webs — kept alive under [U0], but that is "position," not "orientation," and is weak. The
  order looks **group/boundary-based** ([H9]/[U29]), not feather-encoded. → [connections §5](../analysis/connections.md),
  [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md)
- **H5.** Feather **colour is a binary** (black/red) reading around the ring, or maps to the **honor** mechanic. Unresolved.
  → [connections.md](../analysis/connections.md)
- **H6.** **Mechanical precedent.** The *Dreamcatchers* collectible already ships the "**connect the found points → a drawn
  shape → go to a feature (the eye) for the reward**" mechanic — the same shape the web trail uses (connect webs → `N`+pole).
  Strong **anti-pareidolia** evidence: this is established RDR2 design language, not coincidence. → [dreamcatchers.md](../analysis/dreamcatchers.md)
- **H7.** **The "eye" motif recurs**: dreamcatcher reward sits **in the eye** of a painted bison; the spider engraving's
  **eye** points the way. Watch for an "eye" along the NW cold frontier (Fort Wallace onward). → [dreamcatchers.md](../analysis/dreamcatchers.md)
- **H15 (user, 2026-06-13).** **The Saint Denis Vampire ([K27]) is the shipped tutorial / "seed" for the pentagram-mapping
  mechanic.** It runs the **same puzzle as Butcher Creek** — *find 5 fixed points → they form a **pentagram** → go to the
  **centre*** — but **fully hand-held** (the **journal draws the pentagram for you** and an **"x" marks the centre**), whereas
  Butcher Creek makes the player connect the 5 unaided ([K5]) and the spider trail gives **no overlay at all** ([K20]). So
  Rockstar "plants the seed," teaching the connect-points→shape→centre grammar on an easy egg, then re-uses the **literal
  pentagram** unaided. A **precedent/intent argument** in the same family as [H6] (the *Dreamcatchers* "connect points →
  drawn shape → go to the **eye**"), **stronger on shape** because it yields the exact pentagram. **Not** evidence the two
  eggs are one puzzle. → [saint-denis-vampire.md](../analysis/saint-denis-vampire.md)
- **H16 (user, 2026-06-13).** **The clue chain is an escalating difficulty curve, and the clue *form* mutates along it.**
  In discovery order: countable tallies (Butcher Creek) → a carving to find (#4) → harder tallies + complex symbols (Fort
  Brennand) → a near-invisible, time-gated **spider engraving** that is itself a map with **no overlay** (must locate poles
  physically or use out-of-game tools) → the 8 webs + an even-harder **central** web → the form changes to **directional
  glyphs** (`N`/`W×5`/`NW`) → **physical objects as pointers** (the Fort Wallace guitars point the heading) → the **ambiguous,
  unsolved bird carving** ([K16]), the hardest because no one knows what action it asks for. Anything past it must be so
  subtle a finder would lack the context to proceed — so the cold frontier is **what the curve predicts**. **Reframes [U2]:**
  the silence doesn't discriminate buried-continuation vs cut-content. **Caveat:** a difficulty *ordering* is subjective and
  partly a discovery-order artefact — a **framing/search-posture** (read with [H1], [H13]), not evidence. →
  [saint-denis-vampire.md](../analysis/saint-denis-vampire.md)
- **H8.** **"Unfinished business"** (falsifiable). The dreamcatcher mission log entry **never clears**; the candidate
  unfinished trigger is the **spider mystery** (which exposes no completion state — [K20](known-facts.md)). **Prediction:**
  completing the spider trail would **clear the dreamcatcher log.** Untested; the wiki files the lingering entry as a plain
  *Oversight* (bug). Do not state as fact. → [dreamcatchers.md](../analysis/dreamcatchers.md), [U17](unknowns.md)
- **H9.** **The 3 [K21] boundaries partition all 8 webs**, per the Jay_0048 community map ([`web_map-overlay_boundaries.png`](../images/webs/web_map-overlay_boundaries.png)):
  **North** = `B34` (Cornwall); **Connector** = `B23, B45, B56, B56L` (Overflow, Emerald, Oil Fields, Ringneck); **South** =
  `R23, R45, R34` (Scarlett, Southfield, Saint Denis). The **Connector set is exactly the [K13b] non-respawn chain** — which
  ties the spatial boundary mechanic to the shooting-order problem (and may mean "stay in the Connector boundary, shoot its
  four in sequence" *is* the chain). ✅ **CONFIRMED firsthand 2026-06-14 ([K31], resolves [U22]):** the *tied* membership is
  exactly this partition — Top `B34`; Connector `B23,B45,B56,B56L`; South `R23,R45,R34` — and the North boundary does hold only
  the one *tied* web (`B34`). The legend "R56" was indeed the `R34` typo. The one refinement: because the boundaries **overlap**,
  each also *contains* (untied) some of the adjacent boundary's webs ([K31]) — so "stay in the Connector and shoot its four" is
  achievable, but the Connector also physically contains `B34` (east side) and two reds. → [connections.md](../analysis/connections.md),
  [K31](known-facts.md)
- **H10.** **The Flatneck & Bacchus hearts are a deliberate paired motif.** Flatneck = the *filled* "Lillie ♥ Alfred" heart
  (a separate, known easter egg); **Bacchus Bridge = the same heart, empty and hidden**, reported **in line of sight of the
  bird carving** ([K22], [K16]). If the emptiness is intentional ("names missing — go find them"), it may rhyme with the
  mystery's **name** questions (`LJ`/`SM`, matchsticks, Register Rock). Firsthand + one separate-egg datamine; treat as a lead.
  ⚠️ **Relevance contested (2026-06-13):** the heart is real, but its **tie to the spider mystery is as controversial as the
  off-map "?" theory** — it sits **past the last verified clue** ([K16]); don't present it as an established step.
  → [bacchus-bridge.md](../locations/bacchus-bridge.md), [U23](unknowns.md)
- **H12 (user, 2026-06-13).** **The 5 letter-markings split into connection-confidence groups; test them separately.**
  **Group 1 (carved, directly tied):** `LJ`,`SM` — outhouse #4, same hidden-geometry technique ([K15]), beside tally-4 + the
  Fort Brennand pointer (membership [KNOWN]; only meaning open, [U4]). **Group 2 (matchstick, loosely tied):** `EC`,`J+M`,`S+J`.
  **Hybrid:** `LJ`,`SM`,`EC` — `EC` groups up via the Black Widow spider card. **`J+M` singled out:** its location (Cornwall
  K&T) *is* the web-trail START node. Experiments report per-group, not on one flat 10-letter set. →
  [connections §1](../analysis/connections.md), [thread 02](../threads/02-butcher-creek-carvings.md), [thread 03](../threads/03-matchstick-letters.md)
- **H13 (user, 2026-06-13).** **The clues share a consistent medium — a unifying signature + a search heuristic.** All are
  carved into / hidden in **wood** (outhouses, Fort Brennand & Fort Wallace carvings) or sit on the **railway telegraph poles**
  (spider engraving, the 8 webs, two **under-wood** pole inscriptions [U1]); all **time-gated** and **deliberately
  near-invisible** (~7 yrs undiscovered). Predicts the NW frontier is *more of the same*: wood + poles + a night hour. Caveat:
  "wood" describes most of the rural map, so it **narrows the search, doesn't certify a find** (still needs the carving test).
  → [carving-technique.md](../analysis/carving-technique.md)
- **H11.** **Fort Brennand's debated third symbol depicts [Register Rock](../locations/register-rock.md), not an "oil
  puddle."** Register Rock (central Heartlands — where the symbols point) is a **names-and-dates boulder** bearing **J. Brooks,
  Frank Heck, Otis Miller, Billy Midnight, Scott Gray ("S. Gray 1846"), A. West, B. Ward**. If the symbol points there, the
  **names are a candidate name-puzzle** for the mystery's letters. **Caution (do not pre-filter):** the wiki *speculates*
  A. West / B. Ward = Adam West / Burt Ward (*Batman*), but that's **unconfirmed**, and a puzzle may deliberately pick names
  that double as real-world references so players dismiss them — **a name doubling as an outside reference is camouflage, not
  disqualification.** Keep all names live. Strongest *internal* signal so far: **S. Gray → Gray family → Caliga Hall**
  (`S+J`, [K9]). → [connections.md](../analysis/connections.md), [U24](unknowns.md)
- **H14 (user lead, 2026-06-13).** **The mystery's letters and/or numbers are map coordinates.** RDR2 has a **documented
  precedent** ([K25]): the loading-screen photos encode locations as obfuscated **latitude/longitude** coordinates where
  **letters = latitude, numbers = longitude**, on the in-game fast-travel / Central Union Railroad map grid. So the markings may
  resolve to **places, not people** — reading the carved/matchstick **letters as latitude** and the **[S21] numbers
  (`EC`=53, `J+M`=23, `S+J`=29) as longitude**, or the pairs as **grid cells**. This **reframes [U26]:** a coordinate/grid
  reading is no longer web-unsupported — Rockstar demonstrably uses exactly this device in RDR2 (the earlier "no documented
  grid" was about *per-cell A1/B1 labels*). **⚠️ Update 2026-06-13 — grid captured ([K26]), per-cell form tests negative.** The
  investigator photographed the in-game grid (two prop maps: Map 1 = 1–30 × A–U; Map 2 = A–O × 1–7, drawn over the playable
  world). Re-running [`number_grid.py`](../experiments/number_grid.py): the **per-cell** reading mostly **fails** — on Map 2
  only `EC` is in range (`E3`/`C5`), `LJ`/`SM`/`J+M`/`S+J` exceed the 7-row cap; reading the [S21] numbers as the numeric axis,
  only Map 1 admits any (`J+M`=23, `S+J`=29; `EC`=53 out). **What survives** of H14 is the **free coordinate plot** (pick a
  frame, plot candidate (letter-lat, number-long) points, check for a node hit) — still **underdetermined** (each marking is a
  letter-*pair* with one number), a live-but-weakened avenue, **not** a result. → [connections §1a(d)](../analysis/connections.md),
  [U26](unknowns.md), [K26](known-facts.md)
- **H18 (user lead, 2026-06-14).** **The Window Rock "Strange Statues" mural ([K18]) is the shipped "seed" for a per-element
  FILTER mechanic.** The mural is solved by **counting a per-bird feature (tail feathers) while EXCLUDING decoys (upside-down
  birds)** → `2,3,5,7` → input at the statues. Read as transferable design grammar — the same precedent-argument family as the
  **Vampire** ([H15], seed for the pentagram) and the **Dreamcatchers** ([H6], seed for connect-points→shape→eye) — its core
  lesson is that **appearance is a per-element *filter* (which to ignore), not a *heading*.** Transferred to the webs: the
  per-web "count" doesn't carry (each web has **one** feather, so the only count is the system-level 5/3, the pre-existing
  [S12]/[H3] echo); **but the filter lesson does, and it cuts against [H4]** — [H4] assumed orientation is a heading (refuted,
  [#59], feathers uniformly tip-down), whereas the mural says orientation is a *filter*. With web orientation **uniform**, an
  orientation-filter is degenerate, so the filter falls to the only other binary axis — **colour** — predicting **red vs black
  is the include/exclude partition.** That is exactly what [H9] (reds = South boundary) and [U29] (reds are one group, blacks
  another, `B34` special) **independently** show, so three lines **converge on colour/group**, against a feather-encoded
  sequence ([H4]/[H17] dead). Also surfaces the **colour×hour lattice** (a [KNOWN] re-tabulation of [K13a]: each 2/3/4 AM hour
  carries 1 black + 1 red; 5–6 AM carries 2 blacks = the [K13b] interchangeable pair). Tested in
  [`web_colour_group_order.py`](../experiments/web_colour_group_order.py): the [U29] rules collapse 8! to 180 orders and the
  colour-group order is **consistent** (one survivor sub-family — consistency, not proof). ⚠️ **Precedent/intent only:** like
  [H15], **not** evidence the mural and webs are one puzzle, **not** a confirmed key; the shared bird/feather theming is common
  across RDR2. → [connections §5c](../analysis/connections.md), [thread 06](../threads/06-bird-carving-giant-wapiti.md)
- **H19 (2026-06-14) — TESTED → mostly-negative. "The per-web feather SOCKET carries order-relevant structure."** Closing the
  last [U0] residual: the per-web socket (which radial sector the feather hangs from) had been parked as camera-confounded.
  Re-reading all 8 front shots ([#59]) **against each web's own central vertical radial** (camera-invariant, not screen-relative)
  resolves every feather to `L/C/R` and **agrees 8/8** with the earlier screen-relative reads — so the confound never flipped the
  gross call; socket is a **usable weak signal**, and the residual is closed from images. Tested in
  [`web_socket_position.py`](../experiments/web_socket_position.py): (1) 🔴 **colour↔side is NOT significant** — reds average
  further right (1.67 vs 0.60 on L=0/C=1/R=2) but the exact permutation null over C(8,3)=56 gives **p=0.125**, so the
  "reds-right/blacks-left" lean is a *non-result*, now quantified; (2) 🟡 the **three hour-twinned blacks sweep `L→C→R` with the
  clock** (B23=L→B34=C→B45=R; null p≈0.04 exact / 0.07 monotone, but n=3 eyeballed); (3) 🟢 the **5–6 AM pair B56/BL56 share both
  hour AND socket** (both `L`) — a second co-location reinforcing the [K13b]/[H9] interchangeable pair. **Net:** characterises
  the socket but does **not** yield the order; adds a *weak* independent colour-axis line ([H9]/[U29]/[H18]) and does **NOT**
  revive [H4] (socket ≠ orientation; orientation is uniform tip-down). All socket structure stays [SPECULATION] pending the raw
  per-instance entity placement; the checkable next step is whether the black `L→C→R` sweep holds in the game files.
  → [connections §5d](../analysis/connections.md), [feather-positions](../images/webs/feather-positions/README.md), [U0](unknowns.md)
- **H20 (2026-06-14, investigator-data-grounded). The intended single-player solution spans MULTIPLE NIGHTS — one
  colour-group per night — because geography + the lattice force a black-XOR-red choice each hour.** Three inputs converge:
  (1) the **colour×hour lattice** (§5c, [K13a]) — each 2/3/4 AM hour offers **exactly one black + one red**; (2) the **boundary
  geometry** ([K28]/[H9]) — blacks sit on the **North bar + Connector spine**, reds on the **far South bar**, so an hour's black
  and its twin red are **geographically far apart**; (3) **firsthand feasibility** (investigator, 2026-06-14): doing **all-black
  in one night is hard-but-feasible** *including* the doubled 5–6 (`B23→B34→B45→B56` is the easy core; adding the second 5–6 web
  `BL56` is the hard extra), doing **all-red in one night is very hard** (Saint Denis is far; some terrain slows the horse →
  needs an optimal route), and **black + red in one night solo is impossible.** ⟹ In any single night you are forced to take
  **one colour group** (the black connector-spine chain *or* the red south-band run, the latter free-order per [U29]); a
  complete solution therefore needs **≥2 nights**. The escalating difficulty (core blacks → doubled 5–6 → the long red run)
  fits **[H16]**. ⚠️ The feasibility/geometry inputs are firsthand investigator data (high-trust); the **"intended design"**
  framing is **inference [SPECULATION]**. **Crux it sharpens ([U29]):** do shot feathers **persist across nights**, and is the
  **central boundary overlap [K28]** the mechanism that lets you *hold* one group's state while you run the next? A weak design
  aside: RDR2 **Online** would trivialise a multi-person version, so a **single-player multi-night** reading is the more likely
  intent (the user notes online is probably *not* the route). This also answers the earlier "all 8 or a subset?" — likely
  **all 8, but across nights, one colour-group per night**, not one 8-feather sequence. ✅ **The persistence half of the crux is
  now ANSWERED — see [K29] (2026-06-14): shot feathers DO persist across nights (and camping), indefinitely,
  while you stay inside the tied boundary** — so a multi-night solve is **mechanically viable** (you have ≥12 in-game days, not
  one night). ⚠️ But the *second* half — whether the **[K28] central overlap lets you HOLD one group's state across a boundary
  crossing** — tested **negative-leaning** in one direct probe: the investigator camped at the whiskey tree (in the triple
  overlap), left the B34 boundary south, and returned — and the feather **reset to the web**; camping in the overlap did **not**
  carry the state across the crossing. Consistent with [K21]/[K29] (leaving the boundary resets). **Caveat (user):** the game's
  *internal* shot-state flag might still persist invisibly and only re-flag on re-entry — untested — so this is a single
  negative-leaning result, **not** a refutation of the overlap idea. Whether you must shoot *all* of a boundary's feathers
  before crossing, and how cross-boundary state is actually kept, remain open ([U29]). → [connections §5a](../analysis/connections.md),
  [K28](known-facts.md), [K29](known-facts.md), [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md)
- **H21 (user, 2026-06-14). The oversized B34 boundary is a STATE-CARRY corridor: successful web activation may unlock a
  state-gated, verifiable result at Butcher Creek (or Valentine), carried there by the boundary without the shot-state
  resetting.** The mechanic ([K21]): a shot feather stays down *only while you remain inside its boundary*. The geometry
  ([K28]/[S22]): B34's North boundary is stretched to include **Butcher Creek**, **Fort Brennand**, and **Valentine** (⚠️
  **corrected 2026-06-14:** Fort Brennand is *inside* the top boundary, not outside as first recorded), while **Fort Wallace
  remains outside** any boundary — so the *two* feather-less 2018-origin Roanoke nodes (Butcher Creek + Fort Brennand) are held
  inside the top zone. **Inference:**
  the oversize exists *on purpose* — to let the player carry the "B34 (and/or the full set) activated" flag into Butcher
  Creek/Valentine without it resetting, where a **state-gated event** could fire. If true this (a) **mechanically links the web
  trail to the 2018 Butcher-Creek origin thread** (already linked *narratively* by the [K8] pointer Butcher Creek→Cornwall) →
  a strong argument for **"one puzzle"** ([U3]); and (b) would **explain why no payoff has ever been found** ([U2]/[K20]): it is
  gated behind a precondition almost nobody satisfies — correct activation **plus** arriving in-zone with state intact.
  **"Nothing found in Valentine" is consistent with an *un-triggered* gate, not its absence** (user). ⚠️ **Heavy caveats:** no
  payoff/activation outcome has *ever* been confirmed ([U2], [U15], [K20] — the egg has zero in-game tracking); this is
  **design-inference [SPECULATION]**, not observed; **Valentine has no known mystery role**, so the boundary may just be coarse
  ([S22] counter). Do **not** present a Butcher-Creek payoff as real. **Test:** complete a web activation, ride into the
  boundary to Butcher Creek (watch the B34 feather stays down the whole way = confirms extent), and check for any new
  state-gated element (the [K5] pentagram ~4–5 AM, outhouse #4, etc.); repeat for Valentine. → [K28](known-facts.md),
  [U3](unknowns.md), [U2](unknowns.md), [U15](unknowns.md), [connections §5a](../analysis/connections.md)
- **H17 (2026-06-13) — TESTED → REFUTED-leaning. "The feather non-respawn order is keyed by the clock (chronological)."** A
  synthesis the corpus hadn't made: the [K13b] black chain `B23→B45→B56→BL56` is **exactly chronological** (2–3 → 4–5 → 5–6 →
  5–6), and [`web_time_order.py`](../experiments/web_time_order.py) shows that **sorting the [H9] Connector boundary by hour
  reproduces it with no feather-orientation input** — so the clock would be a *sufficient* order key, a parsimony argument
  against [H4]. **Then tested against sourced community brute-force data ([#36], C-tier) and it fails the strict form:** the reds
  work in **non-chronological** orders (`R34→R45→R23` holds), so a clock-order is **not** the key. **What survives:** (1) the
  *group* structure is real but that's already [H9]; and (2) a genuine **deflation of [H4]** — if several orders work within a
  group, feather *orientation* cannot be encoding a unique next-target. A clean example of a tractable hypothesis proposed,
  tested, and mostly knocked down (logged per CLAUDE.md's "refute, don't delete"). Open residue tracked as [U29].
  → [connections §5a](../analysis/connections.md), [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [U0](unknowns.md)

---

*Promote anything here to a known fact only with primary, reproducible evidence. Kill anything contradicted by evidence and
note why in the log.*

# Speculation (explicitly unconfirmed)

Theories — community and our own. **None of this is established.** Each entry notes who proposed it and how testable it is.
Keep hype quarantined here so it never contaminates [known-facts](known-facts.md).

## On the letters L, J, S, M
- **S1 (user).** `LJ`/`SM` on outhouse #4 are **in-fiction clues, not dev initials.** Testable: do `L`,`J`,`S`,`M` match
  character names, or decode via a cipher that aligns with the `J+M` matchsticks? → [connections](../analysis/connections.md)
  **⚠️ ADOPTED as the working stance (2026-07-02):** dev-initials is now **CLOSED as a working line** — counts unfalsifiable
  (6,345 credits), coherence asymmetry (`LJ`, the tightest-tied marking, has *zero* world-building senior matches; Lazlow fits
  only via a stage name and is the audio director on a chain with no audio clues), and the letters are co-carved with a
  *functional* pointer ([K6]). History retained; reopenable only by a sourced dev statement.
  → [connections §1](../analysis/connections.md)
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

- **S28 (2026-06-21) — `EC` may be a KEY/INDEX, not a person's initials: it consistently behaves as the set's structural
  exception, and the one value it keeps coinciding with is the 5-black/3-red feather split.** This **consolidates** the
  scattered `EC` flags ([S17]/[S18]/[S19]/[S21]) into one reading rather than minting new evidence. Across **every** desk test
  the corpus has run, `EC` is the marking that *doesn't behave like the others* on independent axes: **(1)** in the
  shared-letter graph it is the **isolated `E–C` component**, disconnected from the `{J,L,M,S}` cluster the other four markings
  form ([connections §1](../analysis/connections.md)); **(2)** it is physically the **spider-flagged** one — laid beside the
  **Black Widow cigarette card**, the single most on-theme object; **(3)** it is **name-negative everywhere** — no Van der Linde
  member ([S16]/[S17]), no Register Rock inscription ([U24]; `name_match.py`), no `E`-first-name in any source, and the
  Annabella poems are unsigned ([U16]); **(4)** the **one quantity it keeps producing is `5,3`** — A1Z26 `E=5,C=3` ([S18]) and
  the [S21] bare-pair concatenation `EC`=`53` — i.e. the **5-black / 3-red web split** ([K13]); **(5)** it is the **lone
  survivor** of the otherwise-negative non-name readings (the only in-range cell on the Map-2 grid, [U26]; one of only two place
  hits, [S19]). Read together, that is the profile not of a *name* but of a **decoder/index** — a marking whose job is to flag
  the trail's **colour partition** rather than to spell a person. If so, `EC` is a **"Rosetta" marking linking the LETTERS
  thread to the WEB-colour thread** — the very 5/3 / red-vs-black structure the [H9]/[U29]/[H18] web-order work converged on
  **independently** — which would be a (weak) point toward **"one puzzle"** ([U3]). ⚠️ **Held honestly as [SPECULATION], and
  deliberately not promoted:** the strong legs are the *structural* ones (isolation + name-negativity + spider-card placement);
  the `5,3` leg is **coincidence-prone** (small integers, the operator rule chosen to fit — exactly the [S18]/[S21] caveat), and
  "survives the negatives" partly just reflects small-integer genericness. A fully **rival** reading fits the same facts: `EC`
  is simply the one **decorative/non-clue** marking (name-negative because there is no referent to find), which would read its
  absence as *nothing* rather than as a *key*. Both are absence-arguments; neither **decodes** anything. **Falsifiable both
  ways:** a future datamine/source giving `EC` a real in-fiction referent (a person/place it names) collapses S28 back toward
  [S17]/[S19]; conversely, if the other four markings, *filtered/ordered by the 5/3 colour split `EC` encodes*, ever yield clean
  structure, S28 strengthens. Sits entirely **upstream of the [K16] frontier** (verified-letter territory — no boundary
  implications). *(Extension leg, premise-drop pass 2026-07-02: under [H27] — the webs as a display to READ — the [H18]
  mural grammar finally transfers with the right verb: the webs' countable, decoy-filtered feature is **colour**, whose
  read-out is exactly the pair **(5,3)** — so `EC` would be the read-out's **checksum/confirmation**, not a key to a
  shooting order. Same coincidence-proneness as before; no promotion. → [solve-grammar.md](../analysis/solve-grammar.md).)*
  → [connections §1a](../analysis/connections.md), [thread 03](../threads/03-matchstick-letters.md), [U3](unknowns.md)

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
  (come at night / carry a light / don't lose the thread), not a coincidental cheat-code carving. *(Sharpened 2026-07-02 by
  [H24]/[H25]: the carving's site is web `B56`'s location — the **final-hour stop of the chronological black run** — so the
  candidate instruction is now specific: finish at first light, then **sleep/dream**. See
  [decoy-and-dream-hypotheses.md](../analysis/decoy-and-dream-hypotheses.md).)*

## On the destination
- **S7.** The trail's **N → W×5 → NW + guitar** ends at a **buried reward / playable song / cutscene** near Fort Wallace —
  OR the puzzle is **unfinished/cut content** OR a **deliberate dead-end troll.** Community split; unresolved.
- **S34 (fresh-pass, 2026-07-02).** **The "guitar" glyph may be an HOURGLASS / figure-8, not a guitar** (a [U12] candidate —
  every B-tier source only ever *hedges* "guitar"). A guitar body *is* an hourglass-with-neck; the on-theme rivals: the
  **black widow's red hourglass** (spider-branding — echoes the Black Widow card beside `EC` [K9], and the red-on-black
  palette ↔ 3 red / 5 black feathers), a **figure-8** (8 webs; Rockstar's 8/infinity affinity [S20]), a **"rock" pun →
  Rockstar maker's-mark** (user, 2026-07-02 — a guitar "eludes at rock"; a self-signature reading that rhymes with [S25] and
  the waymark frame [H26]), or simply the universal
  **"time" icon** on a trail where everything is hour-gated ([H13]) — with Fort Wallace's two physical guitars as the
  camouflage layer ([S13]). Weak/pareidolia-prone both ways; checkable against the on-file glyph extraction (a guitar needs a
  neck + headstock; an hourglass a pinched waist + flat caps). **⚡ CHECKED 2026-07-05 (desk, on the extraction) — outcome:
  GUITAR-LEANING, hourglass/8 weighed down.** The glyph has a **long neck** (the feature whose absence would have
  strengthened S34), **asymmetric solid lobes** (lower > upper = guitar bouts; hourglass bulbs are symmetric; an 8 needs
  two closed loops) and a **sound-hole-like waist hole** (an hourglass has none). Headstock absent → "guitar-like" stays
  hedged, not promoted; the hourglass/figure-8 rivals fail 2–3 of their own diagnostics each. Full scoring →
  [decoy-and-dream-hypotheses.md §3](../analysis/decoy-and-dream-hypotheses.md)

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
- **S35 (fresh-pass, 2026-07-02; dossier added same day).** **The Strange Man's shack is the SOUTHERN state-carry target — the
  missing twin of [H21].** [K28]'s own firsthand POI inventory puts the shack inside **both** the Middle and Bottom boundaries
  (boundary overlap, like the whiskey tree [S23]), and the Bottom zone is the **red group's** tied boundary. The shack is the
  game's one location that demonstrably watches hidden player state (the portrait egg), and its NPC is the honor figure — giving
  [H5]'s colour↔honor hunch a concrete venue. **Test (one short session):** solve the reds (any order, [U29]), stay inside
  South, enter the shack with state live; check portrait/mirror/interior. **Rival of [H24]** on the reds' role (decoys →
  null here), complement of [H22]-R2 (reds set a flag → the shack could be its checker). **The baseline to compare against is
  now on file:** [locations/strange-man-shack.md](../locations/strange-man-shack.md) (B-tier corpus pass, [#68]) documents
  exactly what the shack canonically watches — current honor (live-swapping animal paintings), one past choice (Jimmy Brooks
  limerick), story epoch (Arthur vs John portrait stages; 4th-visit gate), and visit count — so any red-state deviation is
  recognisable on sight. Note the shack's canonical name is **Bayall Edge**; flavour bonus: **Spider Orchids** grow around it
  and one wall reads *"THE WATER IS BLACK WITH VENOM."*
  → [decoy-and-dream-hypotheses.md](../analysis/decoy-and-dream-hypotheses.md), [strange-man-shack.md](../locations/strange-man-shack.md)
- **S12.** The **5 black + 3 red** feather split may encode the **order** to read/shoot the webs (a binary or grouped
  sequence). ⚠️ **The Window Rock mural cross-check came back NEGATIVE (2026-06-21).** The mural was the one external object
  that might have *sourced* this split — but it is a **single red/ochre pigment** with no black/red dimension
  ([U14](unknowns.md); [`mural_colour_count.py`](../experiments/mural_colour_count.py)), so it cannot be the key. S12 survives
  only as the much weaker standalone idea that **colour orders the webs**, now resting entirely on the boundary partition
  ([H9]/[U29]) — not on any mural. → [images/webs/WEBS-MANIFEST.md](../images/webs/WEBS-MANIFEST.md), [U14](unknowns.md)
- **S15 (Reddit "Zoological", u/Suspicious-Ad6283 — C-tier).** The web feathers are **Northern Cardinal feathers**, and the
  **5-black/3-red split is sexual dimorphism** — 5 ♀ (brown, dark in low light) + 3 ♂ (red) — the giant orb-weavers having
  caught/eaten cardinals. Cited support: the in-game cardinal model
  ([`cardinal_female-in-flight_feather-reference.jpg`](../images/webs/cardinal_female-in-flight_feather-reference.jpg) — ♀ wings
  are red-edged over a brown body, red tail) and the **dreamcatcher-outfit crafted hat**, which is trimmed with cardinal
  feathers. If true this reframes the colour question as **zoological flavour, not a cipher** — a *deflationary rival* to
  **S12/[H3]/[H5]** rather than a key. **Caveat (must reconcile):** dimorphism is red-vs-**brown**, but the game files + wiki
  call the dark feathers **black** ([K13](known-facts.md)); the two captured feathers we now hold (one clearly red, one very
  dark) don't settle brown-vs-black. ⚠️ **Sharpened (investigator data, 2026-07-03):** the non-red feathers are
  **two-toned** — dirty white/grey on one side, black on the other — closer to a *female cardinal's* brown/pale
  countershading than a flat black, a mild point *for* this theory, though still not a confirmed colour match. Testable:
  sample each web's feather colour (both sides) against male/female cardinal plumage.
  → [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [U14](unknowns.md)
- **S29 (desk, 2026-06-21; ⚡ ACTIVATED 2026-07-02) — the `spiderdream0X` numbering is genuine datamine ([K39]), so it
  corroborates COLOUR as a deliberate first-class axis (C-tier).** The per-web file numbers are **colour-grouped and
  hour-twin-mirrored**: files **1–5 = the 5 blacks, 6–8 = the 3 reds**; the two untwinned 5–6 AM blacks at 1–2; every hour-twin
  pair **sums to 11** (B23↔R23, B45↔R45, B34↔R34) — odds **≈1/3360** under random labeling
  ([`web_file_number_structure.py`](../experiments/web_file_number_structure.py)). The 2026-06-21 condition is now met:
  **[U32] resolved** — the mapping is a **public community datamine** (u/Artem_ab6, [#65], matches the manifest 8/8), not a
  back-fit by our corpus. So the structure attaches to real file data: a striking, **independent** sign the devs treated colour
  (and the §5c hour lattice) as deliberate structure — a fresh leg under [H9]/[U29]/[S28] and a nudge toward "one designed
  puzzle" ([U3]). ⚠️ **Still [SPECULATION], not [K]:** the mapping's correctness is **C-tier** (single dataminer, self-flagged
  "(testing)", unreproduced), and back-fit *by the source* to the already-public lattice can't be fully excluded — an
  independent asset dump would settle it. Falsifiable both ways. Upstream of the [K16] frontier. *(Scope narrowed
  2026-07-02: the numbering read as an ORDERING tests **negative-leaning** — [S38],
  [`web_file_order_concordance.py`](../experiments/web_file_order_concordance.py) — so S29's deliberateness evidence is
  the labelling **scheme**, not a sequence.)* → [K39](known-facts.md),
  [U32](unknowns.md), [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [connections §5c](../analysis/connections.md)
- **S37 (desk, 2026-07-02 — unparked from the 2026-07-02 fresh-pass asides by [U32]'s resolution).** **Gertrude's confirmed
  1–7 permutation read as a shooting order over the now-sourced file numbers.** Her opening permutes **1–7** ([K23]); the web
  system has **8** feathered elements, and with the `spiderdream0X` mapping sourced ([K39]) the omitted `08` is **Saint
  Denis** — precisely the web [S31]/[S30] make structurally singular on three independent lines. **Test:** shoot by file
  number in Gertrude's order `1,2,3,7,6,4,5` (= `BL56, B56, B34, R45, R23, B45, B23`), Saint Denis excluded or last.
  ⚠️ Weak by construction: 7-vs-8 numerology, the Gertrude↔spider link is itself unproven ([U6]), and the order crosses
  colour groups mid-run — inheriting the [H22] boundary seam that [H24] dissolves — so this is a low-priority rival, not a
  favourite. *(Desk-checked 2026-07-02, [`web_file_order_concordance.py`](../experiments/web_file_order_concordance.py):
  the order is **infeasible under visible-state rules** — `B34` resets at the first red leg — and needs 4 nights with 2
  H20-impossible mixed-colour nights; viable only under hidden-flag semantics. Priority stays low.)* Upstream of [K16].
  → [decoy-and-dream-hypotheses.md](../analysis/decoy-and-dream-hypotheses.md) (asides),
  [K23](known-facts.md), [K39](known-facts.md), [U6](unknowns.md)
- **S38 (desk, 2026-07-02) — the file numbers read AS an order: tested, negative-leaning, with two conditional survivors.**
  First systematic test of the [K39] numbering as an ordering
  ([`web_file_order_concordance.py`](../experiments/web_file_order_concordance.py),
  [results](../experiments/results/web_file_order_concordance.md)): against chronology, the [K13b] chain, the [H19]
  socket sweep, and geometric paths (clockwise winding / nearest-neighbour / tour length), **nothing beats chance** —
  strongest uncorrected p = 0.083 across ~6 tests. The investigator's eyeballed observation is confirmed real but weak:
  blacks **5→1 descending = `B23>B45>B34>B56>BL56` = the [K13b] chain with `B34` inserted mid-run** (p≈1/12 one-direction,
  ≈1/6 with the direction freedom). The feasibility simulator adds bite: the descending read is **visible-state
  INFEASIBLE** (`B34` resets exiting orange for `BL56`) — viable only under hidden-flag semantics ([H22]-R2) — while
  blacks **1→5 ascending (`BL56>B56>B34>B45>B23`) is the ONE file-order read that is visible-state feasible** (3 nights;
  satisfies the geometry-forced `BL56`-before-`B34`; its reversal of [K13b] is non-disqualifying since [H9] reframed the
  "chain" as boundary membership). So "file # = the order" survives only as **two ranked conditional candidates that fork
  exactly on the [H22] R1/R2 semantics** (ranked list in the results file; Test C stays rank 1). **Constrains [S29]:** the
  numbering's deliberateness is its **labelling scheme** (colour blocks, twin-sum-11; region contiguity is a free rider on
  the colour blocks, conditional p=0.4), **not a sequence**. Byproducts: the blacks-feasibility criterion is proven to be
  *exactly* "`BL56` before `B34`" (60/120 — an independent desk re-derivation of the [H24]-correction geometry), and
  **all-8-visibly-down is impossible, 0/40320** (the [H22] seam exhaustively verified, colour-order independent).
  ⚠️ Inputs C-tier (numbers, lattice, sockets) + PROVISIONAL coords; candidates [SPECULATION] pending in-game test.
  Upstream of [K16]. → [K39](known-facts.md), [S29] above, [U29](unknowns.md),
  [web-order-field-test.md](../analysis/web-order-field-test.md)
- **S39 (Reddit sweep, 2026-07-02) — the TWO-OBJECT model: each "web" is two assets running two separate rule systems.**
  The [#52] datamine claims each web site pairs a **`cablemesh*_hvlit001` drawable** (the visible web, built from telegraph
  cable geometry) with a **`spiderdream` fragment** (the feather — breakable physics + the blue particle glow), sharing
  timeFlags. Read onto the corpus's mechanics, this cleanly splits everything we know into two ledgers: **web-VISIBILITY
  rules** (the 1-hour window; [K30] gaze-gating; the new C-tier holds — gaze-walked camping and **Dead Eye/Eagle Eye
  look-away** persistence, the 4-webs-at-once stack, the save/reload "one-session" wipe, [#70]) versus **feather-STATE
  rules** ([K21]/[K29] boundary-scoped shot persistence — i.e. Jay_0048's *"despawn zones"* [#69] are the *feather's*
  zones, not the web's). Independent corroboration: u/Distinct_Low353 observed the two assets **loading in stages**
  (feather first, web on look-away/back) *before* reading the datamine, and a held web's un-shot **feather still vanishes
  at its hour while the web persists** — the objects demonstrably run separate clocks. **Payoff of the frame:** apparent
  contradictions between community persistence reports and [K29]/[K30] dissolve (they describe different objects), and
  field protocols gain a rule — a "web still up" observation says nothing about feather state, and vice versa.
  ⚠️ C-tier datamine + C-tier tests, mutually consistent but none investigator-verified; the datamine's numeric details
  carry known errors ([#52] caveats). → [K29]/[K30](known-facts.md), [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md),
  [source #52/#69/#70](../sources/sources.md)
- **S40 (Reddit sweep, 2026-07-02) — FORT RIGGS as an underweighted node: a rival "guitar" referent + its own
  feather/Native signals.** Six months of sustained community work ([#72]) converge on Fort Riggs (the burned Native
  school-fort in Big Valley — *outside* our trail's NW corridor): **(a)** the NW pole's "guitar" silhouette **overlays Fort
  Riggs' layout** (3 straight lines + a semicircle; the neck then points at the ritual-sacrifice site) — a structured rival
  reading of **[U12]** vs the Fort-Wallace-guitars consensus; **(b)** a **feather icon appears on the map at Fort Riggs**
  intermittently — one claimed trigger is the **drunk ex-soldier chance encounter** who confesses the Fort Riggs atrocities
  (and drops a unique Native ring); **(c)** ambient **night-only spiderwebs** inside the schoolhouse (different asset style
  from the pole webs); **(d)** the *English Spelling Practice* note's **Waziya poem** (winter/death spirit) reads as
  underexplored; **(e)** the [#52] datamine independently reports a hidden **`"fortriggsgrave"` honor-penalty volume**
  there — a coded sacred-site mechanic with no discoverable entry. **Why it matters:** [U12] is an *open* question on a
  *verified* step, so a rival referent is legitimate frontier work, not boundary-breaking — and Fort Riggs is thematically
  the game's darkest Native site, matching the trail's Wapiti/dream register ([S24]). ⚠️ **Counters:** the silhouette
  overlay is pareidolia-prone (the same method "matched" Fort Wallace); the feather icon may be stock map UI for an
  unrelated collectible; the night webs are likely ambient dressing; **no element links Fort Riggs to the webs
  mechanically.** A 🎮 check is cheap: trigger the encounter → confirm the icon → visit at night. Not promoted; [U12]
  stays open. → [U12](unknowns.md), [thread 05](../threads/05-spider-web-trail-2025.md), [source #72](../sources/sources.md)
- **S30 (desk, 2026-06-21) — the Cornwall spider ENGRAVING read as a star-chart of the webs (spider-body = centre cluster):
  WEAK / pareidolia-prone.** A deterministic extraction of the on-file engraving silhouette finds a 6-legged spider; tested
  against the true web map bearings ([`engraving_web_bearings.py`](../experiments/engraving_web_bearings.py), Monte-Carlo null,
  seed 20260621): **(a)** the *literal* reading — legs = bearings **from Cornwall** to the other 7 webs — is **REFUTED** (from
  Cornwall every web lies in one ~E–SSE wedge spanning 89°, but the engraving fans legs 360°; match no better than random,
  p=0.55, and structurally impossible regardless of coordinate noise); **(b)** the *body-map* reading — spider body = the central
  featherless "spider's-body" cluster, legs = bearings to all 8 surrounding webs — is **weakly consistent but NOT significant**
  (mean error 16.7° vs 25.7° null, **p=0.13**): the NW leg-pair ≈ Cornwall/Oil Fields and the S/SSW legs ≈ Southfield/Scarlett,
  but the **NE webs (Overflow/Emerald) fall in the figure's leg-GAP.** The lone crisp feature is the **longest leg (SE 128°) →
  farthest web (Saint Denis, 121°, 7° agreement)** — one post-hoc coincidence, consistent-with not evidence-for. **Net:** the
  engraving is a **stylised spider + a loose directional cue** ([K11]'s "shows the *direction*"), **not a decodable per-web
  bearing-map** — quantitatively backing the corpus's anti-over-reading stance. Not promoted; upstream of [K16]. → [K11](known-facts.md),
  [connections §5c](../analysis/connections.md), [`results/engraving_web_bearings.md`](../experiments/results/engraving_web_bearings.md)
- **S31 (desk, 2026-06-21) — the 8 webs form a BODY-CENTRED figure, and Saint Denis is the singular far "leg".** Applied RDR2's
  shipped *connect points → shape → **centre/eye*** grammar ([K5]/[K27]/[H6]; the centre webs themselves spell `N`) to the **web
  map positions** for the first time ([`web_geometry_shape.py`](../experiments/web_geometry_shape.py), seed 20260621). **Finding:
  7 of the 8 webs ring the featherless "body" cluster** — their centroid sits **4.6 px** from the centre (vs **106 px** for all 8),
  and a random map point averages **375 px** away (**p=0.0001**). **Saint Denis is the lone centroid-breaker:** dropping it centres
  the figure (next-best single removal leaves 89 px off), it is **830 px** from the body — **2.02× the next-farthest** — and the
  finding is **robust to ±25 px coordinate noise** (100% of trials: 7-web centroid closer than 8-web, Saint Denis always the
  best-to-drop outlier). So the webs read as **a body + a ringing set of legs + one anomalous long leg**, matching the wiki's
  *"spider body + legs"* gloss — a modest, independent geometric nudge toward **one deliberate construction** ([U3]). **Saint Denis
  is now structurally singular on FOUR independent lines (4th added 2026-07-02):** this centroid outlier / longest leg; the **[S30]**
  longest-*engraving*-leg → Saint Denis; being the only red **hour-twinned to the START/index pole** Cornwall (`B34↔R34`, §5c) —
  pairing the **NW start** with the **SE far leg** on a diagonal, and dovetailing with the **unexplained red anomaly already flagged
  in [U29]** (*"a unique function to the red feathers"*); and — **new, the first ASSET-level line** — the [#52] datamine reports
  **feather 08 is the lone render-distance anomaly (31 m vs 37 m for the other seven)**, and under the [K39] mapping **08 = Saint
  Denis** (⚠️ C-tier and held loosely — the same post's hour-window list fails our lattice check, see [#52]'s caveats; but it was
  written with no knowledge of S30/S31, so it can't be contaminated by them). Sweep bonus in the same register: an **unused
  pawnbroker voice line about a "spider image" at the St Denis fence**, and the spider glyph file's `nbx` (**New Bordeaux** = St
  Denis) prefix ([#74]). **Falsifiable prediction (in-game, [U29]):** Saint Denis should be **functionally distinguished**
  in the shooting mechanic (special first/last red, or the source of the red anomaly); a null downgrades this to "the body is just
  near the map centre." ⚠️ **Provisional coords** off a **community-drawn** overlay (not in-game), so the literal 4.6 px rides on
  draftsmanship — only the *qualitative* (7-ring + Saint-Denis-outlier) survives the noise test; gives **no order**, decodes
  nothing, chases nothing past [K16]. → [U3](unknowns.md), [U29](unknowns.md), S30 (above), [connections §5f](../analysis/connections.md),
  [`results/web_geometry_shape.md`](../experiments/results/web_geometry_shape.md)
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
- **S36 (user, 2026-07-02) — the boundary SHAPES argue HAND-AUTHORED design, not engine-default state culling (the
  anti-optimization argument).** An engine's default persistence policy is per-object and uniform: keep an object's state
  for a **fixed radius** around it (e.g. "reset if the player moves 500 m away") or a **fixed time**, identical for every
  object. The feather boundaries violate every part of that pattern: (a) they are **shared across multiple webs** rather
  than per-object; (b) they are **wildly asymmetric** — the North bar over-extends east *and* west, the Connector is narrow
  but very long N–S, and the South bar reaches **further west than the North bar but less far east**, despite the webs'
  close mutual proximity — so **no single distance-from-web value reproduces them**; (c) per [K29], state inside them
  persists **≥14 consecutive slept nights with no time-limit reset**, which is the *opposite* of an optimisation policy.
  Conclusion: the zones were **deliberately hand-coded and linked to specific webs/feathers** — someone at Rockstar
  authored this geometry on purpose, which is a genuine **intentionality argument for the whole web system** ([U2], and a
  point against [H22]-R3's "no combine / nothing there" exit). ⚠️ **Counter (keep honest):** RAGE-engine entity zones could
  be reused/coarse for mundane streaming reasons we can't inspect, and "no uniform radius" is inferred from the overlay map
  ([`web_map-overlay_despawn-zones_jay0048.jpg`](../images/webs/web_map-overlay_despawn-zones_jay0048.jpg)), not from code. **Control test worth
  running (🎮, cheap):** shoot/displace a comparable ambient object (a bottle, a lantern) far from any web, sleep several
  nights in place — if *generic* object state also persists ~14 nights, leg (c) weakens; if it resets fast, the feathers'
  persistence is confirmed special. Inference [SPECULATION]; the shape/persistence facts themselves are [K28]/[K29].
  → [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [connections §5a](../analysis/connections.md)
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
- **H3. ⚠️ REFUTED 2026-06-21.** The **Window Rock "Strange Statues" mural's black/red bird counts equal the webs' 5 black / 3
  red**, making the mural the **order key.** **Tested by counting the mural birds *by colour* off the colour-faithful wiki
  texture** ([`mural_colour_count.py`](../experiments/mural_colour_count.py); [U14]): the mural is a **single red/ochre pigment**
  (100% of chromatic pixels red-hued, 0% any other hue — the dark figures are shaded red, not black), so **there is no black/red
  count to match**. Independently, every walkthrough codes the mural by feather **count + orientation** (upside-down decoys),
  not colour. The webs' own 5/3 colour grouping is unaffected (it comes from the [H9]/[U29] boundary data); only the claim that
  the *mural* is its source/key is dead. → [connections.md](../analysis/connections.md), [U14](unknowns.md)
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
  *Oversight* (bug). Do not state as fact. ⚠️ Asset-level negative (2026-07-02, [#66], C-tier): the 8 web-feather entity
  hashes appear on **no** dreamcatcher (and dreamcatcher feathers show no hash) — weakens a *direct asset* link, doesn't
  touch the log-clearing form (detail in the home file). → [dreamcatchers.md](../analysis/dreamcatchers.md), [U17](unknowns.md)
- **H9.** **The 3 [K21] boundaries partition all 8 webs**, per the Jay_0048 community map ([`web_map-overlay_despawn-zones_jay0048.jpg`](../images/webs/web_map-overlay_despawn-zones_jay0048.jpg)):
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
  across RDR2. ⚠️ **REFINED 2026-06-21 (mural colour test, [U14]):** the mural's decoy filter is **orientation** (upside-down
  birds), and the mural has **no colour dimension at all** (single red pigment — [`mural_colour_count.py`](../experiments/mural_colour_count.py)).
  So H18's *precedent* lesson ("appearance is a per-element filter") **survives intact**, but the mural does **not** itself point
  to colour — the leap to colour is purely *by elimination* (web orientation uniform ⇒ colour is the only binary left), **not**
  corroborated by the mural. The stronger mural↔web *colour* claim ([H3]/[S12]) is now **refuted**, so H18 should not be cited as
  mural-backed support for colour. → [connections §5c](../analysis/connections.md), [thread 06](../threads/06-bird-carving-giant-wapiti.md)
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
  **(Update 2026-07-04: the input reads re-verified on firsthand PS5 4K replacements — 8/8 unchanged, all high-conf,
  Scarlett resolved to a clear `R` — so the script's results stand on investigator-grade images.)**
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
- **H22 (2026-06-14, desk reframing). The web order decomposes into 3 already-solved per-boundary sub-chains; the only open part
  is the cross-boundary COMBINE — and there [K29] contradicts [H20].** Take the [K31] partition seriously and the *within-boundary*
  order is already solved on every boundary: **South** = {`R23`,`R34`,`R45`} works in **any** internal order ([U29]); **Connector**
  = `B23→B45→B56→BL56`, the [K13b] non-respawn chain (`B56`/`BL56` interchangeable); **North** = `B34` alone (Cornwall index pole,
  suspected last). So nothing about the within-boundary order is open. **REFINED (investigator, 2026-06-14): `B34` is NOT forced
  last.** Its orange/North boundary **overlaps** the yellow/Connector boundary ([K31]: "Connector contains `B34`, east side of the
  pole"), so `B34` can be shot **mid-black-run** without a despawn (e.g. `B23→B34→B45→B56`, staying east of the pole) — the **5
  blacks behave as one super-group** and the within-black crossing is bridged. That leaves **two functional groups** — RED (South)
  and BLACK (Connector+`B34`) — and only **one hard crossing** (RED↔BLACK). Because a round-trip despawns, one group is done then
  the other; and since **only `B34`'s *tied* (orange) boundary is the oversized one reaching Valentine/Butcher Creek/Fort Brennand**
  ([K28]/[S22]), BLACK should be **last** — ending on `B34`, whose state then **carries north** (it's the *carrier* feather). ⟹
  **Favoured protocol: REDS first → BLACKS (`B23→B34→B45→B56→BL56`) → ride north to Butcher Creek/Valentine.** Collapses the
  global problem to ~one protocol, not the ~180 flat permutations of [`web_colour_group_order.py`](../experiments/web_colour_group_order.py).
  **The rub:** that one red↔black crossing still trips [K29] (firsthand) — shot-state **resets the moment you leave a boundary**,
  the 3 boundaries touch only at the central overlap (which tested **negative-leaning** for holding state, [K28]), so leaving South
  to do the blacks should wipe the reds. ⟹ **[K29] (reset-on-exit) and [H20] (multi-night) still directly contradict at the seam.**
  The order is **not** bottlenecked on "which sequence" (each group is solved); it is bottlenecked on a **cross-boundary STATE**
  question with exactly three exits, each a sharp falsifiable test:
  **(R1)** the overlap holds multi-boundary state after all (the one probe was incomplete) — *test:* solve South fully, camp at
  the whiskey tree ([S23]), cross to Connector, re-check South is still down (one session); **(R2)** an invisible "reds-done"
  flag persists even as the visible feather resets (generalises [H21]) — **the favoured protocol:** reds first (set flag), then
  blacks ending on `B34`, then ride `B34`'s state north, watching for any [U15]/[U2] trigger; **(R3)** there is **no** global combine — three independent
  mini-puzzles — which fits "no confirmed reward" ([U2]/[K20]) and pushes [U3] toward *many*. ⚠️ Reframing/[SPECULATION] (reset
  rules C-tier #36; the overlap-interleave + "`B34` carries north" are investigator-data leads / gut-feel inference). A **negative** R1/R3 result is itself a real finding
  to log. → [`web_boundary_solve_protocol.py`](../experiments/web_boundary_solve_protocol.py), [connections §5a](../analysis/connections.md),
  [U29](unknowns.md), [U15](unknowns.md), [U3](unknowns.md), [K28](known-facts.md), [K29](known-facts.md), [K31](known-facts.md)
- **H24 (fresh-pass, 2026-07-02; ⚠️ CORRECTED same day). The 3 reds are DECOYS — the colour×hour lattice is an hourly
  black-vs-red FORK, and the intended solve is the 5 blacks only** (never shoot a red). Re-reads the same [KNOWN] lattice
  [H20] rests on: each 2/3/4 AM hour offers **one black *or* one red** (geographically mutually exclusive — the "black+red
  in one night impossible" feasibility data), and the choice-free 5–6 AM finale offers only blacks. [H20] read that as
  "multi-night intended"; H24 reads it as **"the red branch was never meant to be taken."** Five legs: (1) it takes [H18]'s
  mural filter grammar **literally** — decoys are *excluded*, not sequenced; (2) it **dissolves the [H22] seam
  contradiction** ([K29] vs [H20]) — no RED↔BLACK crossing exists if reds aren't shot; (3) it is consistent with **every**
  [U29] reset observation, incl. reds-any-order (inert group), mixed-chains-hold (decoys don't punish, they just don't
  count), and *"any red after BL56 resets"* = a **completion guard** at the black chain's terminus; (4) the all-black run
  being *hard-but-doable* (firsthand) is exactly how an intended solve is tuned; (5) even [S15]'s cardinals: red = the
  conspicuous male = the lure. **⚠️ CORRECTION (investigator, 2026-07-02): the first-draft "one chronological night" form is
  geometrically impossible.** The four northern blacks (`B34` orange-tied; `B23`/`B45`/`B56` yellow-tied) sit inside
  **both** orange and yellow and can be held together, but **`BL56` (Ringneck) lies outside orange** (yellow∩red overlap) —
  reaching it after `B34` exits orange and resets `B34`. So the geometry **forces `BL56`-before-`B34`**, and BL56's hour
  (5–6) being after B34's (3–4) pushes `B34` to a **later night** — i.e. the within-black geometry **mechanically derives
  the [U29] "B34 last" suspicion** (and the [K13b] chain's exclusion of `B34`). All-5-visibly-down remains reachable in
  **~2 nights** via [K29] (night 1 = the [K13b] chain in yellow; hold; night 2 = `B34` from the orange∩yellow overlap),
  ending in the central overlap — natural camp = the **whiskey tree** ([S23]). **Counters:** 3 time-gated webs are
  expensive decoys (but the mural ships placed decoys, and [S13] is the corpus's own camouflage doctrine); [U29] data is
  C-tier/partial. **Rival of [H20]/[H22]-R2 and of [S35] on the reds' role. Test = Test C** (~2 nights, no red↔black seam)
  in [web-order-field-test.md](../analysis/web-order-field-test.md).
  → [decoy-and-dream-hypotheses.md](../analysis/decoy-and-dream-hypotheses.md), [U29](unknowns.md), [U15](unknowns.md)
- **H25 (fresh-pass, 2026-07-02). The payoff is a DREAM — complete a valid feather set, then SLEEP in-boundary before
  leaving.** The mechanism answer to [U11] that seven years of place-searching never tried: Rockstar's own assets name the
  egg `spiderdream` ([K13]); ~~RDR2 **ships a sleep-vision system** (the honor-gated deer/wolf dreams)~~ *(premise
  corrected 2026-07-05 → see the machinery check below)*; [K29] shows the shot-state is deliberately **built to survive
  camping/hotel sleep** in-boundary (why store
  state across sleep if sleep isn't in the loop?); and [K10]'s *"KEEP YOUR DREAMS LIGHT"* sits at **web `B56`'s own site**, the
  final-hour (5–6 AM = first light) stop of the chronological run — re-read as a **finish-line instruction** (finally giving
  that never-wiki-confirmed carving a function, sharpening [S6]). The gap is real: the investigator slept only on *partial*
  states ([K29] runs), and no documented community solver slept on a completed chain. Rhymes with [H8] (dreamcatchers) without
  depending on it. **Test = the "dream coda":** bolt onto *every* protocol (A/B/C) — on any completed candidate state,
  camp/sleep in-boundary, ideally into dawn, before moving; log nulls.
  **⚡ DRY-CHECK PASSED (desk, 2026-07-02):** swept the ~1,989-comment master thread ([#64]) + the community-site timeline —
  **no executed complete-set + sleep test exists anywhere public** ([#67]): two commenters *proposed* sleeping ("since it's
  about dreams"), none did it; the nearest miss (u/lopfeh) slept *mid-chain* → no dream, but **featherless webs spawned
  off-hour (12:20 AM)** afterward — first C-tier sign that sleeping on live state *perturbs* the spawn system; and a
  no-sleep completion null exists (u/Leadcountydude, "seems nothings happens"), which raises the sleep step's marginal
  value. H25 remains the cheapest untested in-game action. Full dry-check in
  [decoy-and-dream-hypotheses.md §2](../analysis/decoy-and-dream-hypotheses.md).
  **⚠️ MACHINERY CHECK FAILED (desk, 2026-07-05 → [#85], [U11] answered-negative):** RDR2 has **no sleep-triggered dream
  machinery at all** — every in-game dream/vision is a story-scripted cinematic (the honor "dreams" are post-mission
  interstitials / a waking trance / the death vision, **not** sleep-fired); the wiki's *Sleeping* page (re-verified
  firsthand) has zero dream content; no free-roam sleep→vision instance exists in ~7.5 years of record; `dreamanim.c`
  ([#74]) is near-empty = cut. **H25's literal form is downgraded** (a sleep-fired dream would need never-exhibited
  machinery); the surviving **weakened form** is the **Hani's Bethel presence-at-hour pattern** ("just being in the
  cabin when 2 am arrives is sufficient" — sleep is only the time-skip), i.e. *be in-boundary at the key hour on a
  completed set, watching the world on waking*. The dream coda stays in Tests C/D at ≈zero cost, run with these
  recalibrated expectations. Full check in [decoy-and-dream-hypotheses.md §2](../analysis/decoy-and-dream-hypotheses.md).
  → [decoy-and-dream-hypotheses.md](../analysis/decoy-and-dream-hypotheses.md), [U11](unknowns.md), [K10](known-facts.md)
- **H26 (fresh-pass, 2026-07-02). The letters are WAYMARKS/signatures, not a cipher payload — presence is the data, not
  content.** Every content-decode has failed or come back coincidence-grade ([connections §1a](../analysis/connections.md):
  anagram impossible, grid negative-leaning, places 2-of-5, numbers null, names P≈0.59) — [H26] says they all fail for the same
  reason: **there is no payload.** Five two-letter groups is too little entropy for a cipher but exactly right for a
  maker's-mark system, and **every letter cluster sits at a designed node** (Butcher Creek trail start · Cornwall = web START
  pole · Vetter's Echo = Black Widow card · Caliga Hall = Gray estate). Generalises [S25] (glyphs as self-label) + [H13]
  (signature medium). Discovery-lag leg (user, 2026-07-02): the Fort Brennand pointer on outhouse #4 took **~7–8 years** to
  find beside a tally known for years — so absence-of-letters at other nodes is weak evidence. **Falsifiable prediction:
  undiscovered letter-pairs exist at other verified nodes** → 🎮 letter-sweep Fort Brennand (tower + outhouses), the 8 pole
  sites, and the Fort Wallace walls around the birds [K16], using the [K15] viewing technique. **Counter:** the `+` connective
  and the re-pair pattern ([S2]/[S3]) look like content, not just presence; the readings can coexist.
  → [connections §1b](../analysis/connections.md)
- **H27 (premise-drop pass, 2026-07-02). The webs are a WITNESS/READ layer, not a shooting input — the feather-shooting
  premise itself is a community import no verified clue supports.** The dropped premise: "the webs must be shot at all."
  Provenance check: **no sourced clue instructs feather-shooting** — the verified chain's instructions are all
  directional ([K11]/[K12]), and where shooting *does* appear (the two shot-to-reveal poles) it is a **reveal** mechanic
  that yields information, while feather-shooting yields none ([K29]: fallen position "encodes nothing"). Formalizing the
  solve grammar of the game's three **solved** eggs (Vampire [K27], Strange Statues mural [K18], Dreamcatchers [H6]; +
  the Butcher Creek pentagram [K5]) gives 8 features — non-destructive input, order-free markers, markers→derived
  construct, payoff at one derived point, gates on reveals not action-schedules, decoys filtered not sequenced, no
  player-managed state machine, solvable from given information — and the web system scores **0/8 as a shooting puzzle,
  8/8 as a read-and-navigate relay** (positions → the [S31] figure; colours → the 5/3 count; derived point = the centre
  cluster, whose `N`+pole message is the layer's payoff, **already collected** — the trail that reached Fort Wallace).
  Re-reads: **[K30] render-gating = the system's per-web gaze-detection sensor** (the game literally tracks *seeing* each
  web); **[K21]/[K29]/[U29] = display-repair/anti-cheese** whose "working orders" are boundary-geometry epiphenomena
  ([H9]; and [`web_file_order_concordance.py`](../experiments/web_file_order_concordance.py) shows **no 8-order is even
  visible-state feasible**, 0/40320 — the "solution order" cannot exist as a visible state). **Honest counters (the
  designated falsifiers):** [K29]'s 14-night exact-position fidelity is expensive for scenery repair (→ the [S36]
  control discriminates); u/lopfeh's off-hour spawns after mid-chain sleep ([#67]) hint the system watches shot-state;
  *"any red after BL56 resets"* ([U29], C-tier/garbled) still lacks a pure-geometry account. **Predictions:** all
  shooting protocols (Tests A/B/C) null on the web side — any shooting-triggered payoff **refutes H27**; no future
  verified clue will instruct feather-state manipulation. **Test = Test D** (witness-only tour + [H25] dream coda —
  strictly cheaper than Test C, leaves no state to corrupt, run it first) in
  [web-order-field-test.md](../analysis/web-order-field-test.md). **Rival of [H24] on the input verb** (H24 keeps
  shooting, drops the reds; H27 drops shooting); complementary to [H25]; strengthens [U3] toward **one** puzzle (one
  navigational relay, one grammar); gains [S28] a direction (the webs' intended *read-out* = the 5/3 count `EC` echoes).
  Home file: [solve-grammar.md](../analysis/solve-grammar.md).
  → [U29](unknowns.md), [U15](unknowns.md), [U3](unknowns.md), [K29](known-facts.md), [K30](known-facts.md)
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
- **S41 (desk adjudication, 2026-07-04). The 2018 carving chain and the 2025 web trail are ONE continuous designed
  relay — sequential stages of one construction, not parallel eggs** (the [U3] "relay" sub-question, decided).
  Anchors: the [K8] hand-off (Fort Brennand symbols → the Cornwall start pole; primary wiki) **retro-validated** by what
  sits at the pointed-at pole — the hidden spider engraving + the head of the whole 8-web system ([K11]; a misread
  pointer doesn't land there by luck); a shared physical node (Heartland Oil Fields = [K10] *"KEEP YOUR DREAMS LIGHT"*
  **and** web `B56`); the shared [H13] signature medium + time-gating + ~7-yr discovery lag ([K2]); both halves
  base-game Oct 2018 ([K24] — kills "a later-added separate egg"); and the dream-motif loop ([K13] `spiderdream` assets
  ↔ the [K10] carving). Counters weighed (community-assembly risk, [H11]'s third-symbol rival, the motifs-travel lesson
  [S33]/[U34]) — none survives the retro-validation leg. ⚠️ The compound "one *designed* puzzle" claim is an
  authorship/design **inference**, so held as [SPECULATION] and adopted as the working frame — **not** promoted to [K].
  [U3]'s live residue: the mechanic layer ([U29] — [H27]/[H24]/[H20]/[H22], to which this verdict is invariant) and
  satellite membership ([U6] Gertrude, the matchsticks). **Reopeners:** a sourced dev statement splitting them; a [U10]
  capture showing the tower symbols don't depict a pole/factory; the Cornwall engraving reading failing verification.
  Home: [one-puzzle-or-two.md](../analysis/one-puzzle-or-two.md).
  → [U3](unknowns.md), [U29](unknowns.md), [U6](unknowns.md), [K8](known-facts.md), [K10](known-facts.md)
- **S42 (desk sourcing, 2026-07-04). Gertrude's recitations are FAILED COUNTING — insanity characterisation, not a
  cipher** (the deflationary reading of [U6], now properly documented). Both hostile parties converge on it from opposite
  directions: **StrangeMan's own video frame** highlights `1 2 3 4 5` in red with *"she only manages to count up to five"*,
  and the **[#43] exposé** independently concludes the numbers are "completely devoid of meaning… random." The captured
  9-sequence transcription's *structure* supports it: every sequence **restarts at 1, 2…**, runs correctly to ~4–5, then
  derails (7 6 4 5… / 10 3… / 17 29 13) — a mind trying and failing to count. **Counterweight (why [U6] stays open):**
  [K23]/[#75] — Rockstar echoed the exact opening string cross-game a year later **and made it a callable phone number**;
  studios don't usually canonise random babble. Middle reading: the **signature string `1237645112` is the deliberate
  token** while the *tail* is free-form madness texture — which would make tail-cipher chasing a dead end **by design**.
  **⚡ Statistically supported 2026-07-04** ([`gertrude_tail_structure.py`](../experiments/gertrude_tail_structure.py),
  exact permutation nulls with the counting prefix fixed): prefixes run 2–5 and **never pass 5**; post-derail "re-rail"
  runs (`3,4,5` / `13,14`) are failed-counting texture an encoding wouldn't produce; tails show **no additive structure
  beyond chance globally (p = 0.44)**. One fragile counter-flag: the **L2-only 4-term Fibonacci chain `3,5,8,13`**
  (p = 0.039 pre-discount) — but it collapses under the near-duplicate L7 parse of the same line, so it's a **fork decided
  by the clean-audio confirm**, not a finding (details in thread 04). All on PROVISIONAL C-tier transcription data.
  **⚡ Update 2026-07-05 ([K42]):** the canonical inventory is now on file from game text (12 lines, [#78]); the fork is
  decided (**both** L2/L7 variants real — the `3,5,8,13` run is verbatim in line A, and line B's inserted 4 breaks it,
  which leans deflationary). **⚡ Battery RE-RUN on the canonical set (2026-07-05, same day)** —
  [`gertrude_tail_structure.py`](../experiments/gertrude_tail_structure.py) now runs on the A-tier [K42] inventory →
  **S42 survives on clean data**: every counting attempt in the game's own strings caps at **5**; the derailed tails
  carry **no additive structure beyond chance (global exact p = 0.335)**; re-rail runs + babble vocabulary persist; **12
  is still never said**. 🆕 canonical-only finding: the prefix-0 lines are **continuation fragments of one babble
  stream** (B = a window onto A's stream with one inserted `4` + appended `1`; L = C's tail-end verbatim) — the 12 lines
  read as windows cut from one long VO take, which *explains* the fragment lines inside S42. The line-A `3,5,8,13` chain
  is now a fixed fact of the text but **suggestive-not-significant**: per-unit exact p = 0.039, ~0.23 after the
  family-selection discount, and only **p ≈ 0.16 at the whole-line level** (the fairer weight) — plus the only other
  take of the same passage (B) breaks it. Don't build on it without an independent hook.
  Home: [thread 04](../threads/04-gertrude-numbers.md). → [U6](unknowns.md), [K23](known-facts.md), [K42](known-facts.md)
- **S43 (node-content pass, 2026-07-05). The GREEN BOTTLES as a per-tally-node marker system** (u/Stock-Hat9530,
  [#81], 20-image gallery — C-tier, single author, unreplicated). Claim: a green **McCarthy Brewing Co.** bottle sits
  close to **each of the five** Butcher Creek tally outhouses; at Fort Brennand the 6-node has a green **"Saint Dymphna"
  Merlot** bottle directly across from it (author searched ~2h for a McCarthy, found none — a deliberate-looking
  *substitution* if the pattern holds at all) and the 7-tower has a bottle **at its top**, from which Saint Denis is
  clearly visible. **Why it matters:** it is the **only candidate per-node differentiator anyone has found** — but note
  the Butcher Creek bottles are claimed *identical* (1–5), so they **cannot encode order** ([U6] attempt B stays closed);
  at most they'd be [H26]-style waymarks. ⚠️ Ambient bottle props are everywhere in RDR2 — high pareidolia risk; needs an
  in-game check (fold into the [H26] letter-sweep). Home: [thread 02](../threads/02-butcher-creek-carvings.md).
  → [U10](unknowns.md), [H26], [#81](../sources/sources.md)
- **S44 (node-content pass, 2026-07-05). The three Fort Brennand tower symbols read as the SAINT DENIS SKYLINE** seen
  from the 7-tower's top (u/Stock-Hat9530, [#81] — C-tier): pole → church steeple, factory → industrial stacks, third
  blob → the pond/water. A third rival for the third symbol alongside the wiki's "oil puddle" and [H11]'s Register Rock
  — and the community's own documentation carries the split verbatim ("Oil Puddle or Register Rock", Marmaluke420).
  ⚠️ Weakness: the *undisputed* pole+factory readings already point at the Heartlands oil fields ([K8] hand-off,
  retro-validated by what sits there), which the skyline reading would have to explain away. Kept as a recorded rival,
  not adopted. Home: [thread 02](../threads/02-butcher-creek-carvings.md). → [U10](unknowns.md), [U24](unknowns.md), [H11]

## On the Fort Wallace bird carving — what it refers to / symbolises (2026-06-16)
*(Downstream interpretation of the verified [K16] mark; full catalogue + tests in [fort-wallace-bird-carving.md](../analysis/fort-wallace-bird-carving.md). None of this moves the frontier or licenses chasing the contested `?`/Bacchus leads.)*

- **S24 (2026-06-16) — the two glyphs read as EAGLES → "Eagle Flies" / the Wapiti tragedy.** The wings-spread silhouette fits
  a **soaring raptor** more than a songbird, and **Fort Wallace is the single location where _Eagle Flies_ is imprisoned**
  (freed in "The King's Son" — a **"Strong"** story node in [narrative-connection.md](../analysis/narrative-connection.md)).
  Two eagle glyphs at *that* fort is the **only reading specific to this exact location** rather than generic bird-lore, and it
  is **underweighted** — narrative-connection notes "no documented theory names Eagle Flies specifically." Pairs with the
  liberation/flight symbolism of the on-site rescue mission. ⚠️ Symbolic [SPECULATION]; unfalsifiable from the shape alone —
  the support is the location coincidence, not the glyph. ⚠️ **Negative place-check (investigator, 2026-06-16):** **Eagle
  Flies' grave lies in the NW direction** the carving roughly faces and **eagles spawn around Calumet Ravine**, but **nothing
  of interest has been observed at either** → if S24 were a pointer to a *place*, that check is **negative**; it survives only
  as *symbolism*, not a "go here and find X" lead. → [fort-wallace-bird-carving.md](../analysis/fort-wallace-bird-carving.md) A2/C1
- **S25 (2026-06-16) — the glyphs LABEL or POINT, they don't ENCODE.** As letters they are **"W"(allace)** — a locative
  maker's-mark / "you are here" reinforcing the trail's own **N → W → NW** heading language ([K11]/[K12]); as a picture they
  continue the under-pole **pictograph** grammar (pole-glyph, guitar-glyph) as a **"go where the birds go"** instruction
  (overlaps the Strange Man flock reading, A1). Either way they are **not a cipher to decode** — a counterweight to reading them
  as initials ([U4]/[U25]) or coordinates ([H14]). Weak, but it reframes the search away from decoding. → [fort-wallace-bird-carving.md](../analysis/fort-wallace-bird-carving.md) B1/B3
- **H23 (2026-06-16; ⚠️ CORRECTED same day) — the birds belong to the STATIC-CARVING class, not the spawned-phenomena class.**
  *Original claim (retracted):* "the birds are the only trail clue not time-gated → an arrival/endpoint marker." **The
  investigator corrected this:** non-time-gating is **shared by every wood carving** — the *confirmed* Butcher Creek tallies +
  `LJ`/`SM` ([K4]/[K6]) and Fort Brennand symbols ([K7]) are equally **always-visible**. Time-gating splits the mystery into
  two asset classes — **static carvings (always visible)** vs **spawned/rendered phenomena (webs 2–6 AM, centre 1–2 AM,
  pentagram ~4–5 AM — [K11]/[K5], time-gated).** The birds sit cleanly in the carving class. **Consequences:** (a)
  daylight-visibility is **NOT differential evidence** — it would equally indict the confirmed carvings, so it **does not
  support the "modelling error" counter** (E1) as first claimed; (b) failing [carving test](../analysis/carving-technique.md)
  #3 (time-gate) is **expected/harmless for a static carving** — #3 discriminates *spawned* phenomena; the load-bearing tests
  for a carving are #1 (depth, passed) and #2/method ([K15], passed). **Weak survivor:** the birds pattern-match the verified
  carving class — a small point *for* legitimacy. → [fort-wallace-bird-carving.md](../analysis/fort-wallace-bird-carving.md) obs. 2 / D1

## Francis Sinclair / Geology egg — adjacency, not a step (2026-06-21)
*Separate Easter egg ([K32], [thread 08](../threads/08-francis-sinclair-mural.md)). These exist so a future session can find
the lead — they are **not** evidence of a spider link, and they live in the post-Fort-Wallace zone the boundary rule guards.*

- **S26 (user, 2026-06-21) — geographic-coincidence watch-item.** The Geology winged-figure carving ([K33]) sits inside the
  **Fort Wallace ↔ Bacchus Station ↔ Dakota River** pocket, which now holds **three** distinct carved/anomalous features
  within a short ride: the bird carvings ([K16], verified frontier), the **empty Bacchus heart** ([K22], contested), and
  this carving. The investigator reads the winged figure as roughly **in line with the bird carving**. **IF** the spider
  mystery is ever shown to extend past [K16], this is a candidate node to re-examine. ⚠️ **Adjacency only — NO verified
  link.** Different asset *class* (a tracked Stranger-mission collectible vs the [K15] hidden-geometry signature marks), and
  "near each other + a winged thing" is thin — exactly the kind of post-frontier coincidence the
  [boundary rule](../analysis/fort-wallace-bird-carving.md) says not to chain on. Logged "in case a link comes up," **not
  promoted.** → [08](../threads/08-francis-sinclair-mural.md)
- **S27 (user, 2026-06-21) — the view-once design *might* signal a deferred, study-at-the-end payoff.** You see the mural
  once, then the cabin locks until (claimed) 100% ([K34]) — read as Rockstar not wanting it to distract you mid-game but
  *wanting* you to return and "figure it out" at completion. ⚠️ **Deflationary counter (likelier):** a standard one-time
  collectible-cabin lock — many Stranger set-pieces seal behind you — and the documented **save/reload workaround** argues a
  mundane door state, not a 100% gate; no payoff has ever been confirmed (fits [U2]/[K20]). The empirical hinge (true
  100%-gate vs door-lock+reload) is part of [U31]. Recorded as the user's interpretation, **not promoted.** →
  [08](../threads/08-francis-sinclair-mural.md)

#### Mount Shann sundial — a *separate* mystery (thread 09, user request 2026-07-02)
- **S32 (investigator, 2026-07-02) — the arrows' deliberate obfuscation + tri-colour coding may be a purposeful puzzle
  layer.** Snow-cover / near-invisibility read as intentional Rockstar obfuscation, with the lone **yellow / 11:30 am**
  arrow as a deliberate outlier; this stylistically rhymes with the spider mystery's near-invisible, time-gated clue
  signature ([H13]). ⚠️ **Deflationary counter:** some arrows are documented to just signpost **collectible stones / the
  cult hut** (ordinary in-world pointers), and warm-hued arrows on a sundial may simply be a shadow-hour gradient. Separate
  egg; **not promoted.** **⚡ The counter is now QUANTIFIED (desk, 2026-07-02 —
  [`sundial_decode.py`](../experiments/sundial_decode.py)):** the arrows fit a physically faithful shadow clock at
  p≈10⁻³–10⁻⁴ (bearing ≡ f(time) → arrows can't be freely "aimed"), every encoding channel tests null or
  look-elsewhere-weak, and the colours resolve into a **major-tick/half-tick grammar** (each orange time = the exact
  midpoint of a red time and noon; yellow ≈ the noon marker) — the shadow-hour-gradient reading made precise. S32's
  puzzle-layer form survives only via the untested in-game POI question ([U33]). → [09](../threads/09-mount-shann-sundial.md)
- **S33 — crossover-via-Chiliad: the sundial and the spider webs may be siblings under a Rockstar "sacred mountain"
  template, not directly linked.** Both tie to **GTA V Mount Chiliad** ([K38] wiki-stated homage; [K24] shader/hour) and
  both key to **~2 AM** ([K37]/[K11]). Likeliest reading = a **reused motif family** (peak · UFO/mural · specific-hour
  reveal) carried between titles, which explains the resemblance **without** an in-RDR2 link between the eggs. A prompt to
  watch the crossover ([U34]), not evidence of one. ⚠️ Weak; the palettes even differ (feathers black/red vs arrows
  red/orange/yellow). → [09](../threads/09-mount-shann-sundial.md)

---

*Promote anything here to a known fact only with primary, reproducible evidence. Kill anything contradicted by evidence and
note why in the log.*

# Spider Webs — master manifest

The webs are the live heart of the puzzle. This file is the **single source of truth** for every web: its location, the hour
it appears, the feather **colour**, and — the part you flagged as potentially vital and which **no online source documents** —
the feather **position/orientation**. If the puzzle requires interacting with webs in a specific **order**, feather position
is our most likely encoding of that order, and capturing it is the single highest-value in-game task.

> **Capture standard (per web):** a clear, zoomed screenshot of the web with the feather visible, **at the correct hour**,
> plus (a) exact map location + coordinates, (b) **which way the feather points / where it sits in the web**, (c) feather
> colour (confirm against the table). Name files `web_<location>_<code>[_<detail>].webp` (per the
> [images naming convention](../README.md#naming-convention-enforced)) and drop them here; fill the row.
>
> **Source web/video first.** Most of these exist in community posts or the Strange Man video — pull and verify those
> before any in-game capture. The one item with **no known online source** is each feather's **position/orientation**;
> that is the genuine capture-only task (try frame-pulling the video below first).

## Established facts (primary wiki + community research site)
- **8 outer feathered webs + 1 CENTRE cluster.** Outer webs sit on telegraph poles, each with one feather, each time-locked
  to a night hour. The centre cluster (the spider's "body") appears **1–2 AM**, has **NO feathers**, and lines up to spell
  **`N` + a telephone-pole glyph** (= go north).
- Feathers are internally named **`spiderdream01`–`spiderdream08`** (this is where the mystery's name comes from); texture
  `wap_gen_feather01`. They **respawn** when shot — *unless* shot in the right chain (see Order below).
- **File-uniqueness (double-checked 2026-06-14) — the deliberateness is in PLACEMENT, not unique files.** The `spiderdream01–08`
  names label **8 instances**, but the **feather texture is a single shared file** (`wap_gen_feather01`, singular) and the **web
  geometry is 4 reused `cablemesh*.ydr` models** (`cablemesh87399/87405/87397/87455`, thecochiti datamine →
  [`web_cable-mesh_datamine.png`](web_cable-mesh_datamine.png), which also marks the feather attach-points in the mesh). So
  each web is **not** a unique asset — what varies per web is **which attach-point/position the feather occupies**, confirmed by
  the 8 front shots showing visibly different positions. Deliberate per-web positioning: yes; unique per-feather files: no.
- **Feather colours: 5 BLACK + 3 RED.** *(GameRant's "white" is imprecise journalism — the wiki + game-file dump agree it's
  black.)* The **3 red** webs are **Saint Denis, Southfield, Scarlett**; the **5 black** are **Cornwall, Oil Fields, Overflow,
  Emerald, Ringneck**.
- Community **location codes** encode colour+time: first letter = colour (**B**=black, **R**=red, **BL**=a black variant),
  digits = the hour pair (e.g. `34` = 3–4 AM).

## The 8 webs + centre — master table
*(Location/time/colour: KNOWN. Feather **orientation**: now CAPTURED for all 8 — uniformly **tip-down by gravity**, see the ★
note + [`feather-positions/`](feather-positions/); the per-web *attachment point* is the only residual variable. Landmark
names beyond Cornwall & Saint Denis are community-assigned, [LIKELY] not Rockstar-canonical. No published in-game coordinates
exist for any pole.)*

| # | Location | File | Code | Time | Feather | **Feather position / orientation** | Image | Status |
|---|----------|------|------|------|---------|-----------------------------------|-------|--------|
| 1 | **Cornwall** (Cornwall Kerosene & Tar — railway btwn Citadel Rock & Heartland Oil Fields) — **START / index pole, bears the spider engraving** | spiderdream03 | B34 | 3–4 AM | Black | tip-down; **centre** (head-on, high-conf) | [front](feather-positions/web_cornwall_b34_front.jpg)·[side](feather-positions/web_cornwall_b34_side.jpg) · `web_cornwall_b34_engraving.webp` | pos ✅ ([#59]) |
| 2 | **Oil Fields** (Heartland Oil Fields) | spiderdream02 | B56 | 5–6 AM | Black | tip-down; **left** (head-on, high-conf) | [front](feather-positions/web_oil-fields_b56_front.jpg)·[side](feather-positions/web_oil-fields_b56_side.jpg) | pos ✅ ([#59]) |
| 3 | **Overflow** (Heartland Overflow, New Hanover) | spiderdream05 | B23 | 2–3 AM | Black | tip-down; **left** (angled view, low-conf) | [front](feather-positions/web_overflow_b23_front.jpg)·[side](feather-positions/web_overflow_b23_side.jpg) | pos ~ ([#59]) |
| 4 | **Emerald** (Emerald Ranch / Station) | spiderdream04 | B45 | 4–5 AM | Black | tip-down; **right** (angled view, low-conf) | [front](feather-positions/web_emerald_b45_front.jpg)·[side](feather-positions/web_emerald_b45_side.jpg) | pos ~ ([#59]) |
| 5 | **Saint Denis** | spiderdream08 | R34 | 3–4 AM | **Red** | tip-down; **right** (angled view, low-conf) | [front](feather-positions/web_saint-denis_r34_front.jpg)·[side](feather-positions/web_saint-denis_r34_side.jpg) · `web_saint-denis_r34.webp` | pos ~ ([#59]) |
| 6 | **Ringneck** (Ringneck Creek, Lemoyne) | spiderdream01 | BL56 | 5–6 AM | Black | tip-down; **left-of-centre** (angled, low-conf) | [front](feather-positions/web_ringneck_bl56_front.jpg)·[side](feather-positions/web_ringneck_bl56_side.jpg) | pos ~ ([#59]) |
| 7 | **Southfield** (Southfield Flats, nr Saint Denis) | spiderdream07 | R45 | 4–5 AM | **Red** | tip-down; **centre** (med-conf) | [front](feather-positions/web_southfield_r45_front.jpg)·[side](feather-positions/web_southfield_r45_side.jpg) | pos ✅ ([#59]) |
| 8 | **Scarlett** (Scarlett Meadows, Lemoyne) | spiderdream06 | R23 | 2–3 AM | **Red** | tip-down; **right** (angled view, low-conf) | [front](feather-positions/web_scarlett_r23_front.jpg)·[side](feather-positions/web_scarlett_r23_side.jpg) | pos ~ ([#59]) |
| C | **Centre cluster** (spider "body", between New Hanover & Lemoyne) | — | — | 1–2 AM | none | n/a — spells **`N`** + pole | `web_centre_n-pole_1-2am.webp` | image ✅ |

Feather tally check: Black = Cornwall, Oil Fields, Overflow, Emerald, Ringneck = **5 ✅** · Red = Saint Denis, Southfield,
Scarlett = **3 ✅**.

> **★ Colour×hour lattice ([KNOWN] re-tabulation of [K13a], 2026-06-14 — [`web_colour_group_order.py`](../../experiments/web_colour_group_order.py)).**
> Laid out by hour, the structure is clean: **each of 2–3 / 3–4 / 4–5 AM carries exactly one black + one red**, and **5–6 AM
> carries two blacks and no red** (1–2 AM is the featherless centre). So each red is **hour-twinned to a black** — `B23↔R23`,
> `B34↔R34`, `B45↔R45` — and the **two untwinned blacks are `B56`/`BL56`**, which are *exactly* the [K13b] "interchangeable"
> pair: the hour-collision (two blacks share 5–6 AM) **is** the mechanical reason they're interchangeable in the chain. The
> lattice is KNOWN; reading the twinning as *deliberate* is [SPECULATION]. It makes **colour a first-class axis** of the order
> problem (cf. [H18], [analysis/connections.md §5c](../../analysis/connections.md)).

> **★ FULL feather-position set captured (2026-06-13) — [U0]'s empirical core is now answered.** u/dropthepress's
> r/reddeadmysteries post *"High-quality spiderweb screenshots"* ([#59], C-tier) shot **all 8 webs twice** — a **front** view
> (full radial web) and a **side** view (web edge-on in its brace pocket) — 16 shots + a colour-coded location map. Saved to
> [`feather-positions/`](feather-positions/) (per-image index + provenance in its
> [README](feather-positions/README.md)). **Finding across all 8 webs:** the feather **hangs vertically, tip-DOWN, under
> gravity** in *every* shot — none points sideways/up or along a heading. This **REFUTES [H4]** (orientation = a compass
> direction to the next web), upgrading the earlier 2-sample lead to a full-set result. **The only residual signal** is the
> *attachment point* (which radial/quadrant the thread hangs from), which **varies left/centre/right between webs** — weak,
> and the lone surviving form of "position encodes order." **Per-web mapping is now RECOVERED** (2026-06-14) — the post's
> selftext carries a "Clockwise Order" list tying each image to a named web; files renamed `web_<location>_<code>_<front|side>.jpg`
> and tabulated in [`feather-positions/README.md`](feather-positions/README.md). **The web is a half-web of ~7 radials → 6
> sections × ~3 rings** (matches the "6 sections" framing). **✅ Socket residual now CLOSED FROM IMAGES (2026-06-14, [H19]).**
> The earlier "not reliably readable / needs the datamine" caveat was over-cautious. Reading each feather **against the web's
> own central vertical radial** (camera-invariant — it rotates *with* the web) instead of the screen resolves all 8 to `L/C/R`,
> **agreeing 8/8** with the old screen-relative reads (the confound never flipped the gross call). Tested
> ([`web_socket_position.py`](../../experiments/web_socket_position.py)): the reds→right/blacks→left lean is **NOT significant**
> (p=0.125); the only crisp structure is the **3 hour-twinned blacks sweeping `L→C→R` with the clock** (B23=L→B34=C→B45=R) and
> the **5–6 AM pair B56/BL56 sharing hour+socket** (both `L`, reinforcing [K13b]). Socket is now a usable **weak** signal; raw
> entity data would upgrade C→A but isn't needed to characterise it. Does **not** revive [H4] (socket ≠ orientation). Full
> reads + method in [`feather-positions/README.md`](feather-positions/README.md). *(Supersedes the two `*_loc-unconfirmed.jpg`
> "Zoological" captures.)*

## Interaction ORDER (the most important open mechanic)
- **[KNOWN — investigator data, 2026-06-13 → [K21]]** **Feather respawn is boundary-gated.** A shot feather **drops to the
  ground (can't be picked up/interacted with)** and **does not respawn while you stay inside the boundary that web is tied
  to**; **leave the boundary and it respawns.** There are **three boundaries — north, south, and a connector linking them** —
  and multiple webs can share one. This is the *mechanism* behind the non-respawn "chain" below: it's **spatial**, not just a
  shot sequence.
- **[KNOWN — investigator data, 2026-06-14 → [K31]; confirms [H9], resolves [U22]] The web↔boundary membership.** The *tied*
  partition (firsthand-confirmed, matching the **Jay_0048 boundary map** [`web_map-overlay_boundaries.png`](web_map-overlay_boundaries.png)):
  **Top/North** = `B34` (Cornwall); **Middle/Connector** = `B23, B45, B56, B56L`; **Bottom/South** = `R23, R45, R34`. That
  accounts for all 8 (1+4+3), and the **Connector set == the non-respawn chain** below. The map's legend typo "R56" = `R34`.
  **Refinement — the boundaries OVERLAP**, so each boundary also physically *contains* (but is **not tied to**) some adjacent
  webs; shooting a contained-but-untied web triggers the **wrong** boundary's despawn (routing hazard):

  | Boundary (tied webs) | Also CONTAINS, untied |
  |----------------------|-----------------------|
  | **Top** — `B34` | `B56, B23, B45` |
  | **Middle/Connector** — `B23, B45, B56, B56L` | `B34` (east side of the pole only — crossing to its **west** triggers the Middle despawn), `R23`, `R45` |
  | **Bottom** — `R23, R45, R34` | `B56L` |
- **[KNOWN — investigator data, 2026-06-14 → [K29]] Shot-feather state PERSISTS across nights + camping, while you stay inside
  the tied boundary** (refines [K21]). 13-day experiment: a shot feather **stays out of the web night after night** in-boundary
  (≥12 in-game days unbroken); when the web despawns (~4 AM) the *fallen* feather despawns too and **respawns at the EXACT spot
  it fell** next night (~3 AM) — the game **stores the precise floor position** (survives camping, and being **kicked/nudged**;
  the feather can't be picked up). It only **returns to the web after you LEAVE the boundary** and come back. So a solver has
  **many in-game days** to work an order, not one night — **the persistence half of the [U29]/[H20] crux is answered: yes,
  within-boundary.** (The *fallen* feather's position/direction is **pure shot-physics** — different every time you re-shoot —
  so the ground feather **encodes nothing**; reinforces [U0]/[H4].) **How you pass time/move inside the zone doesn't matter:**
  camping, **hotel sleep** (verified Valentine Hotel), and **fast travel** all preserve state — but fast travel **advances game
  time** (~+1 h B34→Valentine, ~+2 h B34→Butcher Creek), so it may overshoot a spawn hour ([U30]). **Caveat:** one probe of
  "does the [K28] central overlap let
  you *hold* state across a crossing?" came back **negative-leaning** — camping in the overlap (whiskey tree) then leaving the
  boundary **reset** the feather; an invisible internal flag may still persist (untested).
- **[KNOWN — investigator data → [K30]] Render-gating (capture/routing note).** A web/feather **won't spawn while you look at
  the spot** (look **away and back** to see it appear), and once spawned **won't despawn until you look away.** **Corollary
  (2026-06-14):** because it won't despawn while in view, **keeping line of sight as you approach holds a web rendered past its
  hour** — a slow ride is fine if you don't look away; a feather shot this way registered and **kept its shot status** across a
  camp/night ([K29]). Likely anti-discovery, not puzzle logic — but it means: visit at the known spawn hour and *look away/back*
  (or keep it in view), don't wait while staring. ⚠️ **Open ([U30]):** can't tell whether a hit counts **whenever the feather is
  shot while visible** or **only during the spawn hour** — untestable without the solution order.
- **[KNOWN — investigator data, 2026-06-14 → [K28]] Boundary GEOMETRY = an I-beam / "工".** **North** spans **east–west**,
  **South** spans **east–west**, the **Connector** spans **north–south** (the vertical spine joining them); **all three overlap
  slightly near the map centre**, and that overlap **excludes the central featherless web**. Geographically grounds [H9]
  (index black `B34` = North bar; the 4 connector blacks = spine; the 3 reds = far South bar). The central overlap is the only
  spot inside >1 boundary at once → candidate mechanism for *holding* a group's shot-off state ([U29]).
- **[SPECULATION → [H20]] The solution is MULTI-NIGHT, one colour-group per night.** Geometry ([K28]) + the colour×hour lattice
  (each hour = 1 black + 1 red) put an hour's black (North/spine) far from its twin red (far South), and firsthand feasibility
  (2026-06-14) says **black + red in one night solo is impossible** (all-black-in-a-night is hard-but-doable incl. the doubled
  5–6; all-red is very hard — Saint Denis far + slow terrain). ⟹ each night you run **one** colour group; a full solve needs
  **≥2 nights** — likely **all 8 split across nights, not one 8-feather sequence.** Sharpens [U29]'s persistence-across-nights
  crux. Fits the [H16] difficulty curve.
- **[LIKELY]** Feathers do **NOT** have to be shot in time order. The community found a chain where feathers **stay shot off
  (don't respawn)**: **`B23 → B45 → B56 → BL56`** (with **B56 and BL56 interchangeable**). Breaking the chain **resets**
  (feathers respawn). **([K21] reframes this as the Connector boundary's members.)**
  - In location terms that partial chain is: **Overflow(2–3) → Emerald(4–5) → Oil Fields(5–6) → Ringneck(5–6)** — all
    **black** webs.
- **[SPECULATION → [U29]] The fuller reset ruleset (sourced 2026-06-13, community brute-force testing — Google Sites timeline
  1/2/2026 entry, [#36], C-tier).** The single-sequence reading above is **too strong** — brute-force testing found **several**
  non-resetting orders, so the mechanic looks **group-based, not one rigid sequence**:
  - **Reds work in *any* internal order:** `R34→R45→R23`, `R45→R34→R23`, **and** `R23→R34→R45` all hold without resetting —
    i.e. starting with *any* red doesn't reset the other reds. (Note `R34→R45→R23` is **not** chronological — see [H17].)
  - **Mixed chains work:** e.g. `R34→R45→R23 → B23,B34,B45,B56,BL56` — reds may precede blacks.
  - **`B34` (Cornwall, the index pole) is special:** first reported "cannot be the starting feather; every feather after B34
    resets," **later self-corrected** to "B34 *can* start a chain," with a standing suspicion it is the **LAST** feather
    (unproven). Either way Cornwall behaves unlike the others — consistent with its role as the start/index pole and as the
    lone **North** boundary member ([H9]).
  - **"A unique function to the red feathers"** and **"choosing any Red after BL56 resets the red feather"** are flagged but
    unexplained. **Net:** the order question ([U0]) is less "find the one sequence" and more "which *groups* don't reset, and
    what is `B34`'s role" — which **leans on the boundary partition** ([H9]/[K21]), not on feather orientation ([H4]). → [U29]
- **[H17 — TESTED → REFUTED-leaning] "The non-respawn order is keyed by the clock (chronological)."** Proposed from a synthesis
  the corpus hadn't made: the [K13b] black chain `B23→B45→B56→BL56` is **exactly chronological** (2–3 → 4–5 → 5–6 → 5–6), and
  [`web_time_order.py`](../../experiments/web_time_order.py) shows **sorting the [H9] Connector boundary by hour reproduces it
  with zero feather-orientation input** — a parsimony argument that would **deflate [H4]**. **But the red data above refutes the
  strict form:** `R34→R45→R23` is non-chronological yet works, so the clock is **not** the order key. What survives is the
  *group* structure (already [H9]) and a real **deflation of [H4]**: if multiple orders work within a group, feather
  *orientation* cannot be encoding a unique "next target." → [connections §5a](../../analysis/connections.md), [U29]
- **[SPECULATION — REFUTED-leaning as of 2026-06-13] Feather orientation encodes the order ([H4]).** The original hypothesis:
  each feather physically *points* toward the next web/pole, explaining the "correct" order. **The full 8-web capture ([#59],
  see the ★ note above) refutes the orientation form:** every feather hangs **tip-down by gravity** — there is no per-web
  heading to read. Combined with the order data ([U29]) showing **multiple orders work within a colour group**, a unique
  "next-target" encoding can't be carried by the feathers. **What remains open** is the weaker *attachment-point* reading
  (which strand/quadrant), which does vary between webs — tracked under [U0], but it is not "orientation." Net: [H4] is largely
  dead; the order looks **group/boundary-based** ([H9]/[U29]), not feather-encoded.
- **[SPECULATION]** Colour meaning (5 black / 3 red): honor mechanic? train lines? grouping? — debated, unresolved. Cross-ref
  the **Window Rock Strange Statues** mural (documented tail-feather counts **2,3,5,7**) — note **5** and **3** both appear
  there. See [analysis/connections.md](../../analysis/connections.md).

## Reference images we now hold (sourced 2026-06-13)
- **All-webs labelled overlay** — [`web_map-overlay_all-labeled.jpg`](web_map-overlay_all-labeled.jpg): every web by name +
  code + hour on the in-game map, plus the Centre Web, the W-5-poles pole, and the NW Guitar Pole. The cleanest single map
  of *where* every web is (locations only — no feather orientation).
- **Shooting-chain overlay** — [`web_map-overlay_shooting-chain.png`](web_map-overlay_shooting-chain.png) (credit Jay_0048):
  colour-codes the non-respawn chain (`B23,B45,B56,B56L` yellow) — a visual of the Order section below.
- **Boundary map** — [`web_map-overlay_boundaries.png`](web_map-overlay_boundaries.png) (credit Jay_0048): draws the **three
  [K21] respawn boundaries** (north/south/connector) as coloured rectangles and assigns each web to one ([H9]). The richer
  sibling of the shooting-chain map.
- **Cable-mesh datamine** — [`web_cable-mesh_datamine.png`](web_cable-mesh_datamine.png) (credit thecochiti): the web is built
  from four `cablemesh*` models; **yellow marks the feather positions in the mesh.** This is the closest thing online to
  feather-position data, but it's the *model's* attach points, **not** each pole's in-world feather orientation ([U0] still open).

## Best capture aids
- **Video (lingers on each web):** *"Spider Webs Found After 7 Years! New RDR2 Mystery Explained"* —
  https://www.youtube.com/watch?v=OSQPMaU7yz8 — best candidate to pull feather-orientation frames if in-game capture is hard.
- **Community research site (per-web codes, timeline, order theories):** https://sites.google.com/view/spider-dreams-mystery
  (Timeline + Facts pages; a Canva decision-tree is linked there but wasn't machine-fetchable — open it manually).
  *Note: the site is JS-rendered — `WebFetch` strips its images; extract `lh3.googleusercontent.com` URLs from the raw page
  HTML instead. Its Facts page corroborates this table's location/time/colour data exactly.*

> **Caveat — one community map mislabels Saint Denis.** Jay_0048's index legend lists the reds as `R23,R45,R56`, but the
> markers (and the primary wiki) put the Saint Denis web at **R34** (3–4 AM). Trust **R34** per
> [PRIMARY-wiki-spider-dream.md](../../sources/PRIMARY-wiki-spider-dream.md); the `R56` legend entry looks like a typo.

## Capture checklist (tick as done)
**All 8 webs now have front+side feather-position shots** ([#59], 2026-06-13 → [`feather-positions/`](feather-positions/)).
Orientation is uniform (tip-down) for every web, so the remaining work is *mapping* each shot to its named web and reading the
attachment point — a desk task, not a capture task.
- [x] **Feather orientation, all 8 webs** — captured; uniform tip-down → [H4] refuted (the headline U0 item)
- [x] Web 5 Saint Denis (R34) — front + side identified from background (coastal city / sea + ships, red)
- [x] Map the other 7 shot-pairs to their named webs — done 2026-06-14 (post selftext + front/side cross-check)
- [x] **Read each web's socket** (L/C/R vs central radial) and test colour/[H9] correlation — done 2026-06-14 ([H19]): reads
  agree 8/8 with prior; colour↔side **not** significant (p=0.125); blacks sweep `L→C→R`; B56/BL56 co-located
- [ ] Confirm/extend the shooting-order chain ([U29]); the feather-direction test is now closed (no per-web heading exists)
- [ ] *(stretch)* upgrade the C-tier socket reads with raw per-instance entity placement (game files) — test the black `L→C→R` sweep

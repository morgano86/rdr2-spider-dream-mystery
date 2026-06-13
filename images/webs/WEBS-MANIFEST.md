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
- **Feather colours: 5 BLACK + 3 RED.** *(GameRant's "white" is imprecise journalism — the wiki + game-file dump agree it's
  black.)* The **3 red** webs are **Saint Denis, Southfield, Scarlett**; the **5 black** are **Cornwall, Oil Fields, Overflow,
  Emerald, Ringneck**.
- Community **location codes** encode colour+time: first letter = colour (**B**=black, **R**=red, **BL**=a black variant),
  digits = the hour pair (e.g. `34` = 3–4 AM).

## The 8 webs + centre — master table
*(Location/time/colour: KNOWN. Feather position: UNKNOWN — capture in-game. Landmark names beyond Cornwall & Saint Denis are
community-assigned, [LIKELY] not Rockstar-canonical. No published in-game coordinates exist for any pole.)*

| # | Location | File | Code | Time | Feather | **Feather position / orientation** | Image | Status |
|---|----------|------|------|------|---------|-----------------------------------|-------|--------|
| 1 | **Cornwall** (Cornwall Kerosene & Tar — railway btwn Citadel Rock & Heartland Oil Fields) — **START / index pole, bears the spider engraving** | spiderdream03 | B34 | 3–4 AM | Black | ❓ capture | `web_cornwall_b34_engraving.webp` · `web_cornwall_b34_pole-carving.jpg` | engraving + in-world pole ✅ / feather pos ❓ |
| 2 | **Oil Fields** (Heartland Oil Fields) | spiderdream02 | B56 | 5–6 AM | Black | ❓ capture | — | ❌ need capture |
| 3 | **Overflow** (Heartland Overflow, New Hanover) | spiderdream05 | B23 | 2–3 AM | Black | ❓ capture | — | ❌ need capture |
| 4 | **Emerald** (Emerald Ranch / Station) | spiderdream04 | B45 | 4–5 AM | Black | ❓ capture | — | ❌ need capture |
| 5 | **Saint Denis** | spiderdream08 | R34 | 3–4 AM | **Red** | ❓ capture | `web_saint-denis_r34.webp` | image ✅ / feather pos ❓ |
| 6 | **Ringneck** (Ringneck Creek, Lemoyne) | spiderdream01 | BL56 | 5–6 AM | Black | ❓ capture | — | ❌ need capture |
| 7 | **Southfield** (Southfield Flats, nr Saint Denis) | spiderdream07 | R45 | 4–5 AM | **Red** | ❓ capture | — | ❌ need capture |
| 8 | **Scarlett** (Scarlett Meadows, Lemoyne) | spiderdream06 | R23 | 2–3 AM | **Red** | ❓ capture | — | ❌ need capture |
| C | **Centre cluster** (spider "body", between New Hanover & Lemoyne) | — | — | 1–2 AM | none | n/a — spells **`N`** + pole | `web_centre_n-pole_1-2am.webp` | image ✅ |

Feather tally check: Black = Cornwall, Oil Fields, Overflow, Emerald, Ringneck = **5 ✅** · Red = Saint Denis, Southfield,
Scarlett = **3 ✅**.

## Interaction ORDER (the most important open mechanic)
- **[KNOWN — investigator data, 2026-06-13 → [K21]]** **Feather respawn is boundary-gated.** A shot feather **drops to the
  ground (can't be picked up/interacted with)** and **does not respawn while you stay inside the boundary that web is tied
  to**; **leave the boundary and it respawns.** There are **three boundaries — north, south, and a connector linking them** —
  and multiple webs can share one. This is the *mechanism* behind the non-respawn "chain" below: it's **spatial**, not just a
  shot sequence.
- **[SPECULATION → [H9]]** Per the **Jay_0048 boundary map** ([`web_map-overlay_boundaries.png`](web_map-overlay_boundaries.png)),
  the partition is: **North** = `B34` (Cornwall); **Connector** = `B23, B45, B56, B56L`; **South** = `R23, R45, R34`. That
  accounts for all 8 (1+4+3), and the **Connector set == the non-respawn chain** below. Exact membership is open ([U22]);
  the map's legend typo "R56" = `R34`.
- **[LIKELY]** Feathers do **NOT** have to be shot in time order. The community found a chain where feathers **stay shot off
  (don't respawn)**: **`B23 → B45 → B56 → BL56`** (with **B56 and BL56 interchangeable**). Breaking the chain **resets**
  (feathers respawn) — implying a single correct sequence exists. **([K21] reframes this as the Connector boundary's members.)**
  - In location terms that partial chain is: **Overflow(2–3) → Emerald(4–5) → Oil Fields(5–6) → Ringneck(5–6)** — all
    **black** webs. The **red** webs' place in the order is unsettled.
- **[SPECULATION — your hypothesis]** **Feather position/orientation encodes the order.** This is *plausible and appears to
  be original* — no documented source records feather orientation, so the community's order work is based only on
  colour+time+respawn. If each feather physically points toward the next web/pole, that would *explain* why a specific order
  is "correct." **This is the thing to test in-game.**
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
- [ ] Web 1 Cornwall (B34) — feather position
- [ ] Web 2 Oil Fields (B56) — location + feather position
- [ ] Web 3 Overflow (B23) — location + feather position
- [ ] Web 4 Emerald (B45) — location + feather position
- [ ] Web 5 Saint Denis (R34) — feather position (have web image)
- [ ] Web 6 Ringneck (BL56) — location + feather position
- [ ] Web 7 Southfield (R45) — location + feather position
- [ ] Web 8 Scarlett (R23) — location + feather position
- [ ] Confirm/extend the shooting-order chain; test whether feather direction predicts it

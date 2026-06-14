# Feather positions — the full 8-web set (front + side), location-mapped

**Provenance:** r/reddeadmysteries, *"High-quality spiderweb screenshots"* by **u/dropthepress** (post `1qbhkjm`, 152 pts,
posted 2026-01-13), acquired via the Arctic Shift mirror + `i.redd.it` CDN on 2026-06-13 (reddit.com 403s our fetcher — see
[RESOURCES](../../../sources/RESOURCES.md)). **C-tier** (one community author) but **high-value**: the first source to document
feather position for **all 8 webs**, the repo's #1 open question ([U0]). Source #59.

The author shot **each web twice** — a **front** view (the full radial half-web facing the camera) and a **side** view (the web
edge-on, showing it sits recessed in the triangular pocket between the pole, the crossbeam, and a diagonal brace).

> **✅ Per-web mapping RECOVERED (2026-06-14).** The mapping is **in the post's selftext** (a "Clockwise Order" list with the
> image URLs under each location heading) — *not* in Reddit's `gallery_data`, which the Arctic Shift mirror drops. Re-pulling
> the raw selftext gave the definitive labels below, and **the first image under each heading is the front view, the second is
> the side** — which matches our independent front/side visual classification exactly (cross-validated). Files are now named
> `web_<location>_<code>_<front|side>.jpg`.

## Confirmed mapping + feather socket (camera-invariant, 2026-06-14)

The **Socket** column is the gap-closing read (see ["Closing the gap"](#closing-the-gap--the-socket-read-camera-invariant)
below): position measured **relative to the web's own central vertical radial** (camera-invariant), not relative to the
screen. `L`/`C`/`R` = left of / on / right of that central radial. It **agrees 8/8** with the earlier screen-relative
"horizontal" read — i.e. the camera confound did **not** flip the gross call — so the position data is now a usable weak
signal, no longer "not a finding."

| # (post) | Location | Code | Colour | Hour | Front file | Side file | Screen-relative (old) | **Socket** (central-radial) | Conf. |
|---|----------|------|--------|------|------------|-----------|-----------------------|-----------------------------|-------|
| 1 | Overflow | B23 | black | 2–3 | `web_overflow_b23_front.jpg` | `web_overflow_b23_side.jpg` | left | **L** | med |
| 2 | Emerald | B45 | black | 4–5 | `web_emerald_b45_front.jpg` | `web_emerald_b45_side.jpg` | right | **R** | med |
| 3 | Saint Denis | R34 | red | 3–4 | `web_saint-denis_r34_front.jpg` | `web_saint-denis_r34_side.jpg` | right | **R** | med |
| 4 | Ringneck | BL56 | black | 5–6 | `web_ringneck_bl56_front.jpg` | `web_ringneck_bl56_side.jpg` | left-of-centre | **L** | med |
| 5 | Southfield | R45 | red | 4–5 | `web_southfield_r45_front.jpg` | `web_southfield_r45_side.jpg` | centre | **C** | med |
| 6 | Scarlett | R23 | red | 2–3 | `web_scarlett_r23_front.jpg` | `web_scarlett_r23_side.jpg` | right | **R** | low (near C) |
| 7 | Cornwall | B34 | black | 3–4 | `web_cornwall_b34_front.jpg` | `web_cornwall_b34_side.jpg` | centre (just right of axis) | **C** | **high** |
| 8 | Oil Fields | B56 | black | 5–6 | `web_oil-fields_b56_front.jpg` | `web_oil-fields_b56_side.jpg` | left | **L** | **high** |

Confidence is now **medium** on the previously "low" rows because the central-radial method removes the screen-angle
confound; Scarlett alone stays low (its feather sits very close to the central radial, C-vs-R ambiguous). Sockets are
**still C-tier eyeballed** — the only stronger source is the raw per-instance entity placement in the game files.

## What these images settle, and what they don't

**1. Web structure — confirmed as the user described.** Each web is a **half-web** (a semicircle hanging under the crossbeam),
built from a hub at top-centre with **~7 radial strands → 6 angular "sections"** and **~3 concentric rings**. So a feather's
position has two coordinates: **which section (1–6, left→right)** and **which ring (inner/mid/outer)**. The central vertical
radial is the section-3 | section-4 boundary.

**2. Orientation is uniform (tip-down) → [H4] refuted.** In all 16 shots the feather **hangs vertically under gravity**; no web
points its feather along a heading. (Established last pass; unchanged.)

**3. Position genuinely varies per web → not a clone.** The feather sits in a visibly different spot at each web, confirming
deliberate per-web placement (see the file-uniqueness note). This is the live residual of [U0].

**4. Socket IS readable after all — the confound was beatable.** The earlier caveat ("apparent left/right is a camera
artefact") was over-cautious. The fix is to stop measuring against the **screen** and measure against the **web's own central
vertical radial** (the hub's straight-down strand), which rotates *with* the web and so is camera-invariant. Re-read that way,
all 8 sockets resolve to `L`/`C`/`R` (table above) and **agree 8/8 with the old screen-relative reads** — so the confound
never actually flipped the gross call; it only inflated the uncertainty. See ["Closing the gap"](#closing-the-gap--the-socket-read-camera-invariant)
for what the reads do and don't reveal. The raw per-instance entity placement (game files) would still upgrade these from
C-tier eyeballed to A-tier, but it is **no longer required to characterise the socket** — that residual of [U0] is now closed
from images.

## Closing the gap — the socket read (camera-invariant)

**Method.** The web is a half-web: a hub at top-centre, ~7 radial strands → 6 angular sectors, ~3 rings. The **central
vertical radial** bisects it. Because that radial is part of the web, "feather left of / on / right of the central radial"
is a property of the *web*, not the camera — it holds at any viewing angle as long as you can pick out the hub and the
straight-down strand. The datamine ([`../web_cable-mesh_datamine.png`](../web_cable-mesh_datamine.png)) corroborates a
**discrete** socket set: its yellow attach-point highlights cluster at roughly three radial positions (one left-of-centre,
the central radial, a pair on the right), consistent with an `L`/`C`/`R` model rather than continuous placement.

**What the 8 reads reveal** (tested in [`../../../experiments/web_socket_position.py`](../../../experiments/web_socket_position.py)):
- **The reads are robust.** 8/8 match the prior screen-relative reads → socket is a usable weak signal.
- **Colour↔side is NOT significant.** Reds do sit further right on average (red mean 1.67 vs black 0.60 on L=0/C=1/R=2),
  but the exact permutation test gives **p = 0.125** — the "reds-right/blacks-left" lean is *not* a finding, exactly as the
  old caveat feared, now quantified. Do **not** promote it.
- **One crisp sub-pattern: the three hour-twinned blacks sweep `L→C→R` with the clock** — B23 (2–3 AM)=L, B34 (3–4 AM)=C,
  B45 (4–5 AM)=R (null p≈0.04 exact / 0.07 any-monotone; only 3 points, eyeballed).
- **The 5–6 AM pair B56/BL56 share BOTH hour and socket** (both `L`). They were already the [K13b]/[K21] "interchangeable"
  pair from the colour×hour lattice (shared hour); a shared socket is a second co-location reinforcing it.

**Net:** closing the gap *characterises* the socket but does **not** hand us the order. It adds a weak independent line to
the colour-as-first-class-axis reading ([H9]/[U29]/[H18]) and reinforces the interchangeable pair; it does **not** revive
[H4] (socket ≠ orientation — orientation is uniform tip-down). All socket *structure* is **[SPECULATION → [H19]]** pending
the raw entity data. → [analysis/connections.md §5d](../../../analysis/connections.md).

## File-uniqueness — double-checked (2026-06-14)

The user's intuition (*"someone went to the effort of a unique position per web, not a clone"*) is **right on substance, but
the "unique file per feather" mechanism is not**:
- **Feather texture = one shared file**, `wap_gen_feather01` (singular) — sourced ([K13], #35). Not 8 textures.
- **Web geometry = 4 reused `cablemesh*.ydr` models** — `cablemesh87399/87405/87397/87455`, per the thecochiti datamine we
  hold ([`../web_cable-mesh_datamine.png`](../web_cable-mesh_datamine.png)). Not 8 unique meshes.
- **The 8 webs are named `spiderdream01–08`** ([K13a]) — but that names 8 *instances/scenarios*, not 8 unique asset files.
- **So what is bespoke per web is the feather's PLACEMENT** (which attach-point/position it occupies in the shared mesh) — and
  that is exactly what these 8 screenshots show varying. Deliberate positioning: yes. Unique files: no.

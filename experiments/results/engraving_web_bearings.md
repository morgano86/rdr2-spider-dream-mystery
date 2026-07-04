# Result — does the Cornwall spider ENGRAVING encode the web bearings? (`engraving_web_bearings.py`)

**Question.** [K11] (KNOWN, primary-wiki gloss) says the Cornwall pole engraving "maps the
**direction** of 7 more webs." The corpus had declined to read precise geometry from the blurry
hand-doodle (anti-pareidolia; 2026-06-21 provenance audit). This test adjudicates it objectively:
**do the spider-legs point along the true map bearings to the webs, or is it a stylised spider?**

**Method.** Leg directions are extracted **deterministically** from the on-file silhouette
([`web_cornwall_b34_engraving_transparent.webp`](../../images/webs/web_cornwall_b34_engraving_transparent.webp))
— radial max-distance profile from the figure centroid; legs = prominence-filtered peaks (no
hand-placed angles). Web bearings come from pixel positions on the community overlay
([`web_map-overlay_all-labeled.jpg`](../../images/webs/web_map-overlay_all-labeled.jpg), 1280×977,
**PROVISIONAL ±~25 px**). Match quality = mean nearest-leg angular error vs a **Monte-Carlo null**
of random uniform leg sets (seed 20260621).

## What the figure is
The extraction is unmistakably a **spider**: a central body blob with **6 robustly-detected legs**
(bearings, length px): **SE 128° (800, by far the longest)**, NW 312° (583), NNW 337° (563),
SSW 193° (551), N 4° (472), S 171° (353). Body-radius ~275 px. There are clear **leg-gaps at NE
(~50°) and W (~260°)** — no legs there.

## Two readings tested

| Reading | Origin | Mean nearest-leg error | Null mean | p(null ≤ obs) | Verdict |
|---|---|---|---|---|---|
| **R-literal** | from **Cornwall** (where the engraving is) → other 7 webs | 23.6° | 25.7° | **0.554** | **REFUTED** |
| **R-bodymap** | from the **centre** "spider-body" cluster → all 8 webs | 16.7° | 25.7° | **0.130** | weak / not significant |

- **R-literal is refuted — and robustly so.** From Cornwall (the NW-corner web) **all 7 other webs
  lie in a single ~E–SSE wedge spanning only 89°** (bearings 70°→160°), but the engraving fans legs
  across the **full 360°** — strong **N / NW / NNW** legs point exactly where Cornwall has *no* web.
  The match is literally **no better than random** (p=0.55). This conclusion is **immune to the
  coordinate noise**: Cornwall is unambiguously the cluster's NW corner, so every web is SE-ish of it.
- **R-bodymap is only weakly consistent (p=0.13, not significant).** Reading the spider's body as the
  central featherless cluster and its legs as bearings to the 8 surrounding webs does better than
  chance but **does not clear a pareidolia bar.** Regional hits: the **NW leg-pair (312°/337°)** ≈
  Cornwall (310°) + Oil Fields (327°); the **S/SSW legs (171°/193°)** ≈ Southfield (185°)/Scarlett
  (192°). But the **NE webs Overflow (38°) and Emerald (57°) fall in the engraving's leg-GAP** — the
  figure simply has no leg there — which is why the fit stays mediocre.

## The one crisp feature
**Longest leg → farthest web.** The dramatically longest leg points **SE (128°)**; the **farthest
web from the centre is Saint Denis (R34), at bearing 121°, 830 px out** — **7° agreement**. If leg
*length* meant distance, this is the single clean correspondence. ⚠️ It is **one** coincidence picked
*post hoc* from ~6 legs, so it is **consistent-with**, not evidence-for.

## Verdict
The engraving is best read as a **stylised spider pictograph plus a loose directional cue** — exactly
[K11]'s wiki wording ("shows the *direction*") and **not** a decodable per-web bearing-map. The
literal-from-Cornwall map reading is **dead** (chance-level + structurally impossible: wedge vs 360°
fan); the centre-origin star-chart reading is **weak [SPECULATION]** ([S30]), kept honest by the
null. This **quantitatively backs the corpus's anti-over-reading stance** and adds two structural
facts (the 360°-vs-wedge refutation; the longest-leg→Saint-Denis hint). Upstream of the [K16]
frontier — chases nothing past Fort Wallace.

*Run:* `python experiments/engraving_web_bearings.py` (Pillow + numpy; deterministic, seed printed).
*Inputs:* silhouette auto-analysed; web map coords PROVISIONAL (overlay pixel reads).

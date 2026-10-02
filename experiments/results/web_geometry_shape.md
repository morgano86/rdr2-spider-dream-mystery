# Result - do the 8 web POSITIONS form a body-centred figure? (`web_geometry_shape.py`)

**Question.** RDR2 ships the same grammar repeatedly - *connect fixed points → they form a shape → go to its **centre/eye*** ([K5] Butcher Creek tallies→pentagram→centre; [K27]/[H15] Saint Denis Vampire; [H6] dreamcatchers; the centre webs themselves "line up to form an `N`", [K11]). The primary wiki calls the central featherless 1–2 AM cluster the spider's **"body"** and the 8 outer webs its legs. That grammar had been run on the tallies and on the engraving's legs ([S30]) but **never on the 8 web map positions.** Tests whether the **body sits at the geometric centroid of the webs.** Bears on [U3] (one puzzle?), [H9], and cross-checks [S30]. [SPECULATION] at most. **Upstream of the [K16] frontier.**

**Inputs.** The **same provisional pixel reads** used by `engraving_web_bearings.py`, off the community overlay `images/webs/web_map-overlay_all-labeled.jpg` (1280×977; x=E+, y=S+). ⚠️ **PROVISIONAL** - eyeball reads (±~25 px) off a **community-drawn** overlay, *not* in-game coordinates (none are published). So this measures the **overlay's** geometry, which only approximates true placement; trust the conclusions that survive the ±25 px noise test.

## Run (2026-06-21, seed 20260621, 100k trials)

**Test 1 - centre→subset-centroid distance**

| Subset | centroid | dist from centre cluster |
|--------|----------|--------------------------|
| all 8 webs | (572, 475) | **106.6 px** |
| **7 webs (excl. Saint Denis)** | (483, 422) | **4.6 px** ✅ |
| 5 black webs | (504, 282) | 137.4 px |
| 3 red webs | (685, 795) | 428.6 px |

**Test 2 - leave-one-out (centroid of the other 7).** Dropping **Saint Denis** centres the figure on the body almost exactly (**4.6 px**); the next-best single removal (Ringneck) leaves it **89 px** off, every other **>108 px**. Saint Denis is the **unambiguous, principled outlier** - not cherry-picked among near-equals.

**Test 3 - significance & robustness.**
- A **random** point in the web bounding box averages **375 px** from the 7-web centroid; the real centre is **4.6 px** → **p = 0.0001** that an arbitrary map point is this central.
- Under **±25 px noise on every coordinate** (incl. the centre): the 7-web centroid is closer to the body than the 8-web centroid in **100.0%** of trials (median **20 px** vs **108 px**), and **Saint Denis is the single best-to-drop outlier in 100.0%** of trials. The *qualitative* finding is robust to the coordinate uncertainty; the literal "4.6 px" is not (it rides on overlay draftsmanship).

**Test 4 - Saint Denis as the singular far "leg".** Distances from the body: Saint Denis **830 px** (bearing 121°, SE) ≫ Southfield 411 · Cornwall 360 · Overflow 339 · … - Saint Denis is **2.02× the next-farthest**. [S30] independently found the **engraving's longest leg points SE → Saint Denis.** Two independent lines finger the same web.

## Reading (evidence, not fact - [SPECULATION], → [S31])

- **The 8 webs are arranged as a body-centred figure**, not scattered town-webs: 7 of them ring the featherless "body" cluster (centroid on it within the coordinate noise), exactly as the wiki's *"spider body + legs"* gloss describes. This is a **modest, independent point toward a single deliberate construction** ([U3] one-puzzle) - geometric, not just thematic. ⚠️ Tempered by: the body being near the *middle* of a figure is partly definitional, and the overlay is community-drawn.
- **Saint Denis is structurally singular - now on THREE independent lines:** (1) the lone centroid-breaking far outlier / longest "leg" (this test); (2) the **longest engraving leg** ([S30]); (3) it is the only red **hour-twinned to the START/index pole** Cornwall (`B34↔R34`, both 3–4 AM, §5c) - so the figure pairs the **NW start** (Cornwall) with the **SE far leg** (Saint Denis) on a diagonal. That convergence makes "Saint Denis has a special role" the durable lead here, and it dovetails with the **pre-existing unexplained red anomaly** in [U29] (*"a unique function to the red feathers", "any red after BL56 resets the red feather"*).
- **Falsifiable prediction (in-game, ties to [U29]):** if the webs are a designed body-centred figure with Saint Denis as the anomalous long leg, Saint Denis should be **functionally distinguished** in the shooting mechanic - e.g. the special first/last red, or the source of the [U29] red anomaly. A null (Saint Denis behaves like any other red) would downgrade this to "the body is just near the map centre."
- **What it does NOT do:** it gives **no shooting order**, decodes nothing, and chases nothing past [K16]. It is a structural/intent observation about verified web locations.

## Output
- stdout only (no large artefact). Re-run: `python experiments/web_geometry_shape.py`.

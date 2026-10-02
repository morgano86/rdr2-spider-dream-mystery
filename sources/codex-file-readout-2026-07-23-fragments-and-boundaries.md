# CodeX findings handoff — spiderdream fragment/archetype data + boundary geometry

**Date:** 2026-07-23 **Source:** CodeX (a separate local repo — an RDR2 archive/asset explorer + 3D scene viewer), read directly from the shipped RDR2 game files (`.ytyp`/`.ymap`/`.yft` binary data) via a throwaway diagnostic harness that boots CodeX's real archive/resource loader. This is genuine file-level readout, not a community datamine repost — for anything it states about raw file contents, treat it as at least as strong as this corpus's **A-tier**; anything about *why* the game behaves a certain way is a separate technical hypothesis, flagged as such below.

> **Filed 2026-09-01** as corpus source **[#89]** (`sources/sources.md`), verbatim apart from this note and the file-path fix-ups at the bottom. **It HAS since been integrated** — see [K45]–[K52], [U36]–[U39], [H28], [S47] and the 2026-09-01 log entry. The "not yet integrated" status note below is preserved as it was written.

**Status of this document (as written, 2026-07-23):** a raw findings dump, **not yet integrated** into the corpus's ID/rollup system. No `K`/`U`/`H`/`S` IDs have been minted here — that's deliberately left to whichever agent organizes this material, per `CLAUDE.md`'s append-only `INDEX.md` convention and the existing numbering. Whoever picks this up should: cross-check against `findings/known-facts.md`, `findings/unknowns.md` (esp. **U29**, the feather-order crux), `sources/sources.md` (esp. **#52**, the reddit datamine this corroborates/corrects), and `images/webs/WEBS-MANIFEST.md`.

---

## 1. Correction to the two-object model: spiderdream01x–08x are FRAGMENTS, not drawables

Each of the 8 archetypes' `assetType = ASSET_TYPE_FRAGMENT` (confirmed directly from the `.ytyp` `CTimeArchetypeDef` XML), not a plain drawable. Each resolves to its own `spiderdreamNNx.yft` fragment file (breakable physics object), not a `.ydr`.

This **independently confirms**, from raw files rather than the C-tier "gamedev" Reddit post (source **#52**), the **two-object model**: fragment = the feather (breakable), separate drawable = the web strand (`cablemesh*_hvlit001`). Recommend upgrading that specific sub-claim's sourcing tier from #52-only to file-verified.

## 2. Per-web archetype/fragment data — identical vs. differing

Full field-by-field archetype XML and fragment/geometry/shader dumps are available on request (not attached, to keep this scannable). Summary:

### Identical across all 8 (no per-web signal — real negative results worth logging)
- **Geometry:** 1 LOD, 48 verts / 48 tris, same bounding box to the millimeter on all 8.
- **Breakability physics** (`Rsc8FragPhysLOD`/`Rsc8FragPhysGroup`): 1 group, 1 child, `strength=100, minDamageForce=100, damageHealth=1000`, mass 1.0/1.0 pristine/damaged — every feather takes *exactly* the same force to knock down. No per-web "toughness"/hit-count difference exists anywhere in the data.
- **Entity rotation:** identity quaternion on all 8 placements — no orientation signal at the entity level (consistent with [K-tag TBD] "all feathers hang tip-down by gravity" already in the corpus).
- **Entity flags:** `0x00180000` (CastStaticShadows|CastDynamicShadows only) on all 8.
- **`DrawableArrayCount = 0`** on every fragment — i.e. **no second drawable embedded in the feather's own fragment data**. Worth reconciling against the corpus's "every feather is doubled" claim (main + smaller secondary feather) — if that's real, the doubling is NOT a second drawable slot in this object; it must be a separate entity or part of the web-strand geometry instead. Worth an in-game/file check of what actually produces the second feather.
- Every archetype carries an identical `CExtensionDefParticleEffect` extension (`fxName=vYYFKTA_0xC5876498`, an obfuscated/unresolved hash not in CodeX's 421k-line name dictionary; same offset/color/probability across all 8; only the per-item `guid` differs, a meaningless UUID). **Not previously documented in this corpus** — worth an in-game look at what this particle effect actually renders, and a wordlist attempt at the fxName hash.

### Differs (real per-web signal)
- **`lodDist = 37` for all except `spiderdream08x` (Saint Denis) = 31.** This independently CONFIRMS the previously single-source/unreproduced render-distance-anomaly claim from source **#52** — recommend upgrading that specific sub-claim's tier to file-verified.
- **`textureDictionary`** (external base diffuse/bump/specular textures) groups into exactly 3 sets matching 3 region `.ytyp` files: `jklm_11_14_rd_p_d` (01x,02x,04x,05x), a private/unresolved-hash dictionary **unique to 03x only** (03x is also the only one of the 8 with textures embedded directly in its own file rather than resolved externally — fits 03x/Cornwall's role as the "index/start" pole with the spider engraving), and `nopq_11_14_rd_p_d` (06x,07x,08x).
- **`tintpalettetex` shader param is populated — with an embedded 256×4 palette texture — ONLY for the 3 red feathers (06x/07x/08x); null/unassigned for all 5 black feathers.** This is the actual byte-level mechanism behind the community-observed red/black split. However, MD5-verified: **all three red palettes are pixel-for-pixel identical** (same 4096 bytes, format `B8G8R8A8_UNORM_SRGB`, a dark-red-to-pale-pink gradient) — so the palette itself carries **no additional per-web signal** beyond "this one is red." Log as a clean negative: rules out "palette encodes an order" as a hypothesis.

### Net read on the feather-order question (U29)
Nothing in the raw per-archetype/entity/geometry/physics/shader data encodes an explicit 1–8 order, or any per-web asymmetry beyond what's already known (position, hour) plus the region-grouping and red/black mechanism above. **This is a real negative result across a source class the corpus hadn't checked at the byte level before** (only citing datamined claims about it, per source #52) — it argues against a "hidden data field" solution and supports the corpus's existing lean toward the mechanic being state/behavior-based (see §3).

## 3. Boundary-group geometry — a concrete candidate mechanism

**User-relayed firsthand finding this session** (should be logged as investigator data per this repo's norms): three boundary groups —
- **Group 1** (north, horizontal): `B34` alone
- **Group 2** (center, vertical): `B23, B45, B56, B56L`
- **Group 3** (south, horizontal): `R23, R34, R45`

They are **not** proportional/radius-based (very different walking distances in different directions). Also reported: **leaving the boundary alone does not trigger the reset — leaving AND THEN RE-ENTERING triggers it.** **Correction after reviewing the rendered visualization (below):** there is **no triple overlap** — only Group 2 bridges Group 1 and Group 3 (each of the two horizontal groups overlaps the central vertical group, but not each other). This is more geometrically precise than what's currently on file (shape/orientation wasn't previously recorded) — cross-check against the existing I-beam-shape/membership facts and update with this detail.

**Session conclusion (user + CodeX, after visual comparison): this line is now considered CLOSED/inconclusive.** The boundary geometry matches ordinary ymap streaming extents (below) closely enough, and the shape is generic enough (tied to arbitrary region-file boundaries, not something bespoke-shaped for a puzzle), that the working conclusion is: **the boundary mechanic is very likely just an artifact of which ymap file a web happens to live in, not a deliberately designed puzzle boundary.** Recommend logging this as a negative finding on **U29** (or its own closed sub-question) rather than continuing to treat the boundary shapes as a signal.

**CodeX finding:** the 8 webs are split across exactly 3 separate `.ymap` files, and every RDR2 ymap declares its own standard (non-uniform, axis-aligned) header fields for streaming/entity extents — this is ordinary world data, not a bespoke construct built for this easter egg:

| ymap (= boundary group) | entitiesExtents min | entitiesExtents max | size (W×H) | shape |
|---|---|---|---|---|
| `jklm_7_10_rds_props_strm_0` = **Group 1** (B34) | (-362.2, -134.2, 23.8) | (2593.6, 880.6, 133.2) | 2955.8 × 1014.8 | wide, north |
| `jklm_11_14_rds_props_strm_0` = **Group 2** (B23,B45,B56,B56L) | (537.4, -1313.0, 41.0) | (2183.9, 789.8, 123.2) | 1646.5 × 2102.7 | tall, center |
| `nopq_11_14_rds_props_strm_0` = **Group 3** (R23,R34,R45) | (506.0, -1675.6, 40.0) | (2918.9, -344.1, 93.1) | 2412.9 × 1331.5 | wide, south |

(The looser `streamingExtents` box, actually used for load/unload distance, is also on file — available on request.) These 3 boxes' shape/position closely match the user's description: north-horizontal / center-vertical / south-horizontal, overlapping in the middle. See **`spiderdream_boundaries.png`** (in this same folder, rendered directly from this data) for a visual to compare against the user's own map/testing.

All 3 ymaps have header `flags=0` → `isScripted=False` in CodeX's engine model (bit 0 of a ymap's flags field marks a script-gated container; these are not that).

**Technical hypothesis — [SPECULATION], not yet verified in-game:** the boundary/reset behavior is most likely a side effect of RDR2's *ordinary* distance-based ymap streaming (the same load/unload every ymap in the game goes through), not bespoke script logic. Under this hypothesis: leaving the zone unloads the ymap (nothing visibly changes, since it's already out of view); crossing back into range re-streams it fresh from its authored data, which is the moment the feathers snap back to the web. This matches "leaving alone doesn't trigger it, re-entering does" exactly, and would mean **no script decompiler is needed** to explain this particular mechanic (contrast with the feather-visibility system itself, which genuinely has no script hooks per source #52/#87).

**Falsifiable prediction for an in-game test:** any other movable/breakable prop inside these same 3 ymaps (not just spiderdream) should show the identical "world remembers it nearby, resets on leave+return" behavior, since it would ride the same generic streaming mechanism rather than bespoke web logic. If a control object *outside* these 3 ymaps but similarly far from any settlement does NOT show this reset-on-return behavior, that would be strong support for this hypothesis specifically (rather than a game-wide generic prop-persistence system, which is a related but distinct question — see the corpus's existing "persistence CONTROL" open action item).

**Ruled out:** RDR2's generic town/district cull-box system (`mapdatacullboxes_new.meta`, ~129 entries — e.g. CORNWALL/Rhodes/Emerald Ranch/Van Horn boxes that hide distant unrelated content while the player is in a given town) does **not** reference any of these 3 web-props containers, and its box shapes don't match (small, town-centered, hundreds-to-thousands of culled-container hashes each — a different, unrelated LOD system). Worth recording as checked-and-ruled-out so a future session doesn't re-spend effort on it.

## Files (as filed in this corpus)
- [`../images/webs/web_ymap-extents_boundary-groups.png`](../images/webs/web_ymap-extents_boundary-groups.png) — the boundary-box/web-position render described in §3 (originally `spiderdream_boundaries.png`).
- Three later renders (2026-07-25/26, from the `*_strm_0` child ymaps rather than the `*_rds_props` parents) were relayed after this document was written and are filed alongside it: [`web_ymap-extents_strm0-annotated.png`](../images/webs/web_ymap-extents_strm0-annotated.png), [`web_ymap-extents_strm0-clean.png`](../images/webs/web_ymap-extents_strm0-clean.png), [`web_ymap-extents_g1-g3-gap.png`](../images/webs/web_ymap-extents_g1-g3-gap.png). Their added findings (the exact streamingExtents, the **10.50 m G1/G3 gap**, and the **max-6-at-once** derivation) are integrated as [K49].

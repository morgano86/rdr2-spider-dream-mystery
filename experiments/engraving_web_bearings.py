#!/usr/bin/env python3
"""Does the Cornwall spider ENGRAVING encode the web BEARINGS, or is it a stylised spider?

Question + IDs
--------------
[K11] (KNOWN) states the Cornwall pole engraving "maps the DIRECTION of 7 more webs" -- a
gloss taken from the primary wiki. The corpus has so far DECLINED to read precise geometry
out of the (blurry, hand-doodle) engraving on anti-pareidolia grounds (see the 2026-06-21
provenance audit: "the wiki says the engraving shows the *direction* of the webs ... NOT a
positional node-map"). That left a concrete, falsifiable question untested:

    Do the engraving's spider-LEGS actually point along the real-world bearings to the webs?

This script adjudicates it objectively. Two interpretations are tested:
  R-literal : the engraving is read FROM Cornwall (where it physically is) -- each leg is a
              bearing from Cornwall to one of the other 7 outer webs.
  R-bodymap : the engraving's spider BODY == the central featherless "spider's body" cluster,
              and the legs are bearings from the CENTRE to the 8 surrounding webs (the more
              meaningful star-chart reading; the centre cluster is literally the body).

A positive result (legs match bearings far better than chance) would PROMOTE [K11] from a
loose "directional" gloss to a usable bearing-map and is at most [SPECULATION] until sourced.
A negative result is a real finding: it backs the corpus's anti-over-reading stance with a
number, and says the engraving is a *stylised spider* + loose directional cue, not a map.
This is UPSTREAM of the [K16] frontier -- it does not chase anything past Fort Wallace.

Inputs + provenance
-------------------
  * Leg bearings: extracted DETERMINISTICALLY from the silhouette asset
    images/webs/web_cornwall_b34_engraving_transparent.webp  (investigator-supplied extraction
    of the in-game engraving, on file). Method = radial max-distance profile from the figure's
    centroid; legs = peaks. No hand-placed angles.
  * Web map positions: pixel coordinates read off the community overlay
    images/webs/web_map-overlay_all-labeled.jpg (1280x977). These are APPROXIMATE eyeball reads
    (+/- ~25 px ~ a few degrees) -- flagged PROVISIONAL below. The robust conclusions are the
    ones that survive that noise (see results note).

Run:  python experiments/engraving_web_bearings.py
Deps: Pillow, numpy  (see requirements.txt).  Deterministic; Monte-Carlo seed printed.
"""
import math
import numpy as np
from PIL import Image

SEED = 20260621
ENGRAVING = "images/webs/web_cornwall_b34_engraving_transparent.webp"

# --- Web map positions (PROVISIONAL: pixel reads off web_map-overlay_all-labeled.jpg, 1280x977) ---
# x = east+, y = south+ (image convention). Flagged approximate.
WEBS = {                       # name: (px_x, px_y, colour)
    "Cornwall_B34":   (205, 188, "black"),   # NW corner of the cluster; bears the engraving
    "OilFields_B56":  (310, 150, "black"),
    "Overflow_B23":   (691, 151, "black"),
    "Emerald_B45":    (691, 281, "black"),
    "SaintDenis_R34": (1196, 841, "red"),    # far SE -- the farthest web
    "Ringneck_BL56":  (625, 642, "black"),
    "Southfield_R45": (443, 827, "red"),
    "Scarlett_R23":   (417, 718, "red"),
}
CENTRE = (482, 418)            # central featherless "spider body" cluster (1-2 AM)


def bearing(ox, oy, px, py):
    """Compass bearing 0=N,90=E,180=S,270=W from origin (ox,oy) to point (px,py)."""
    dx, dy = px - ox, py - oy
    return math.degrees(math.atan2(dx, -dy)) % 360


def ang_diff(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def extract_legs(path, n_smooth=2, prominence=60.0):
    """Radial max-distance profile -> leg peaks. Returns list of (bearing_deg, length_px)."""
    arr = np.array(Image.open(path))
    mask = (arr[..., 3] > 128) & (arr[..., :3].astype(int).sum(2) < 200)
    ys, xs = np.where(mask)
    cx, cy = xs.mean(), ys.mean()
    dx, dy = xs - cx, ys - cy
    r = np.hypot(dx, dy)
    brg = (np.degrees(np.arctan2(dx, -dy))) % 360
    # max radius per 1-degree bin
    prof = np.zeros(360)
    bi = brg.astype(int) % 360
    for deg in range(360):
        sel = bi == deg
        if sel.any():
            prof[deg] = r[sel].max()
    # circular smoothing
    k = np.ones(2 * n_smooth + 1) / (2 * n_smooth + 1)
    sm = np.convolve(np.concatenate([prof[-n_smooth:], prof, prof[:n_smooth]]), k, "valid")
    # body radius ~ median of the profile; a leg is a peak rising well above it
    body = np.median(sm)
    legs = []
    for deg in range(360):
        lo, hi = sm[(deg - 1) % 360], sm[(deg + 1) % 360]
        if sm[deg] >= lo and sm[deg] > hi and (sm[deg] - body) >= prominence:
            legs.append((float(deg), float(sm[deg])))
    # merge peaks within 12 deg (keep the longer)
    legs.sort()
    merged = []
    for b, L in legs:
        if merged and ang_diff(b, merged[-1][0]) <= 12:
            if L > merged[-1][1]:
                merged[-1] = (b, L)
        else:
            merged.append((b, L))
    # wrap-merge first/last
    if len(merged) > 1 and ang_diff(merged[0][0], merged[-1][0]) <= 12:
        if merged[0][1] >= merged[-1][1]:
            merged.pop()
        else:
            merged.pop(0)
    return cx, cy, body, sorted(merged)


def assign_error(targets, legs):
    """Greedy nearest-leg assignment; mean & max angular error (deg). Legs may be reused."""
    errs = [min(ang_diff(t, lb) for lb, _ in legs) for t in targets]
    return float(np.mean(errs)), float(np.max(errs)), errs


def monte_carlo_null(targets, n_legs, trials=200000, rng=None):
    """P(random set of n_legs uniform bearings matches >= as well as observed)."""
    rng = rng or np.random.default_rng(SEED)
    t = np.array(targets)
    hits = 0
    obs = None
    samples = rng.uniform(0, 360, size=(trials, n_legs))
    means = np.empty(trials)
    for i in range(trials):
        legs = samples[i]
        d = np.abs(t[:, None] - legs[None, :]) % 360
        d = np.minimum(d, 360 - d)
        means[i] = d.min(axis=1).mean()
    return means


def main():
    print(f"# Engraving-as-web-bearing-map test  (seed {SEED})\n")
    cx, cy, body, legs = extract_legs(ENGRAVING)
    print(f"Engraving silhouette: centroid=({cx:.0f},{cy:.0f}), body_radius~{body:.0f}px, "
          f"{len(legs)} legs detected")
    print("  legs (bearing deg : length px):")
    for b, L in sorted(legs, key=lambda x: -x[1]):
        print(f"    {b:5.0f}  {L:6.0f}")
    leg_brgs = [b for b, _ in legs]
    longest = max(legs, key=lambda x: x[1])

    # ---- True bearings ----
    print("\n## True web bearings")
    others = {k: v for k, v in WEBS.items() if k != "Cornwall_B34"}
    from_corn = {k: bearing(WEBS["Cornwall_B34"][0], WEBS["Cornwall_B34"][1], v[0], v[1])
                 for k, v in others.items()}
    from_ctr = {k: bearing(CENTRE[0], CENTRE[1], v[0], v[1]) for k, v in WEBS.items()}
    dist_ctr = {k: math.hypot(v[0] - CENTRE[0], v[1] - CENTRE[1]) for k, v in WEBS.items()}

    print("  FROM CORNWALL (R-literal), 7 other webs:")
    for k, b in sorted(from_corn.items(), key=lambda x: x[1]):
        print(f"    {b:5.0f}  {k}")
    span = max(from_corn.values()) - min(from_corn.values())
    print(f"    -> bearings span only {span:.0f} deg (one wedge); engraving legs span ~360 deg")

    print("  FROM CENTRE (R-bodymap), all 8 webs:")
    for k, b in sorted(from_ctr.items(), key=lambda x: x[1]):
        print(f"    {b:5.0f}  {k:16s} dist {dist_ctr[k]:5.0f}px")

    rng = np.random.default_rng(SEED)
    print("\n## Match quality vs Monte-Carlo null (random uniform legs)")
    for label, targets in [("R-literal (from Cornwall, 7 webs)", list(from_corn.values())),
                           ("R-bodymap (from centre, 8 webs)", list(from_ctr.values()))]:
        mean_e, max_e, _ = assign_error(targets, legs)
        null = monte_carlo_null(targets, len(legs), trials=50000, rng=rng)
        p = float((null <= mean_e).mean())
        print(f"  {label}")
        print(f"    observed mean nearest-leg error = {mean_e:5.1f} deg (max {max_e:.0f}); "
              f"null mean {null.mean():.1f} deg; p(null<=obs) = {p:.3f}")

    # ---- length vs distance: does the longest leg point at the farthest web? ----
    print("\n## Leg LENGTH vs web DISTANCE (does longest leg = farthest web?)")
    far = max(dist_ctr, key=dist_ctr.get)
    far_b = from_ctr[far]
    print(f"    longest leg: bearing {longest[0]:.0f} deg, length {longest[1]:.0f}px")
    print(f"    farthest web: {far} at bearing {far_b:.0f} deg, dist {dist_ctr[far]:.0f}px")
    print(f"    angular agreement: {ang_diff(longest[0], far_b):.0f} deg")

    print("\n## Verdict")
    print("  R-literal: REFUTED structurally -- from Cornwall every web lies in a single")
    print("  ~E-SSE wedge, but the engraving fans legs across the full 360 deg (strong N/NW/")
    print("  NNW legs where Cornwall has no web). This survives any coordinate noise.")
    print("  R-bodymap: see p-value above -- regional matches exist (NW pair, S/SSW group,")
    print("  longest-leg->SE->Saint Denis) but the NE webs (Overflow/Emerald) fall in a leg")
    print("  GAP. Treat as weak/pareidolia-prone [SPECULATION], not a decoded map.")


if __name__ == "__main__":
    main()

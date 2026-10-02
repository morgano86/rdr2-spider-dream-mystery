#!/usr/bin/env python3
"""Do the 8 web POSITIONS form a shape centred on the featherless cluster (the
"spider's body")? - applying RDR2's shipped "connect points -> shape -> centre/eye"
grammar to the web coordinates themselves.

Question + IDs
--------------
RDR2 repeatedly ships the same puzzle grammar: connect a set of fixed points -> they
form a SHAPE -> go to its CENTRE/eye. Confirmed instances in this corpus:
  * Butcher Creek tally marks connect in order -> a PENTAGRAM -> its centre ([K5]).
  * Saint Denis Vampire: 5 fixed clues -> a pentagram -> the centre ([K27], H15).
  * Dreamcatchers: connect points -> a shape -> the "eye" ([H6]).
  * The CENTRE webs themselves "line up to form an N" ([K11]).
And the primary wiki ([K11]) calls the central featherless 1-2 AM cluster the spider's
"body", with the 8 outer feathered webs as the legs/points around it.

That grammar has been tested on the tallies and on the engraving's legs
(engraving_web_bearings.py, [S30]) but NEVER on the 8 web MAP POSITIONS. Concrete,
falsifiable question:

    Does the central featherless cluster sit at the geometric CENTRE (centroid) of the
    8 outer webs - i.e. is the "body" actually the body of the figure the webs trace -
    and if not all 8, which subset centres on it?

A positive, robust result would be [SPECULATION] support that the webs are arranged as a
deliberate figure around the body (one puzzle, geometric, [U3]/[H9]); it also cross-checks
the [S30] "longest engraving leg -> farthest web = Saint Denis" hint from the other side.
A negative result is a real finding: the webs are just where the map's towns/poles happen
to be, with no body-centred geometry. UPSTREAM of the [K16] frontier - chases nothing past
Fort Wallace.

Inputs + provenance
-------------------
  * Web + centre positions: the SAME provisional pixel reads used by
    engraving_web_bearings.py, taken off the community overlay
    images/webs/web_map-overlay_all-labeled.jpg (1280x977). x=east+, y=south+.
    ** PROVISIONAL ** - eyeball reads (+/- ~25 px) off a COMMUNITY-DRAWN overlay, NOT
    in-game coordinates (none are published, per WEBS-MANIFEST). So this measures the
    overlay's geometry, which only approximates true in-world placement. Robust
    conclusions are the ones that survive the +/-25 px noise test below.

Run:  python experiments/web_geometry_shape.py
Deps: numpy (already required by engraving_web_bearings.py - see requirements.txt).
Deterministic; Monte-Carlo seed printed.
"""
import math
import numpy as np

SEED = 20260621
NOISE_PX = 25.0          # provisional-coordinate uncertainty (per the docstring)
TRIALS = 100_000

# --- Web map positions (PROVISIONAL: pixel reads off web_map-overlay_all-labeled.jpg) ---
# Identical to engraving_web_bearings.py. x = east+, y = south+ (image convention).
WEBS = {                       # name: (px_x, px_y, colour)
    "Cornwall_B34":   (205, 188, "black"),   # NW corner; START / index pole (engraving)
    "OilFields_B56":  (310, 150, "black"),
    "Overflow_B23":   (691, 151, "black"),
    "Emerald_B45":    (691, 281, "black"),
    "SaintDenis_R34": (1196, 841, "red"),    # far SE - the farthest web
    "Ringneck_BL56":  (625, 642, "black"),
    "Southfield_R45": (443, 827, "red"),
    "Scarlett_R23":   (417, 718, "red"),
}
CENTRE = (482, 418)            # central featherless "spider body" cluster (1-2 AM) [K11]

NAMES = list(WEBS)
P = {k: np.array(v[:2], float) for k, v in WEBS.items()}
C = np.array(CENTRE, float)


def centroid(keys):
    return np.mean([P[k] for k in keys], axis=0)


def dist(a, b):
    return float(np.hypot(*(np.array(a) - np.array(b))))


def bearing(o, p):
    dx, dy = p[0] - o[0], p[1] - o[1]
    return math.degrees(math.atan2(dx, -dy)) % 360


def main():
    rng = np.random.default_rng(SEED)
    print(f"# Web-positions-as-a-figure test  (seed {SEED})\n")
    print("Provisional pixel coords off the community overlay (x=E+, y=S+); "
          "centre = featherless 'body' cluster.\n")

    xs = np.array([P[k][0] for k in NAMES]); ys = np.array([P[k][1] for k in NAMES])
    bbox = (xs.min(), xs.max(), ys.min(), ys.max())
    print(f"web bounding box: x[{bbox[0]:.0f},{bbox[1]:.0f}] y[{bbox[2]:.0f},{bbox[3]:.0f}]  "
          f"({bbox[1]-bbox[0]:.0f} x {bbox[3]-bbox[2]:.0f} px)\n")

    # ---- Test 1: centroid of candidate subsets vs the CENTRE ----------------------
    blacks = [k for k in NAMES if WEBS[k][2] == "black"]
    reds   = [k for k in NAMES if WEBS[k][2] == "red"]
    no_sd  = [k for k in NAMES if k != "SaintDenis_R34"]
    subsets = [("all 8 webs", NAMES),
               ("7 webs (excl. Saint Denis)", no_sd),
               ("5 black webs", blacks),
               ("3 red webs", reds)]
    print("## Test 1 - distance from the CENTRE cluster to each subset's centroid")
    for label, ks in subsets:
        g = centroid(ks)
        print(f"  {label:30s} centroid=({g[0]:5.0f},{g[1]:5.0f})  -> {dist(C, g):6.1f} px from centre")
    print()

    # ---- Test 2: leave-one-out - which single web, removed, best centres the rest? -
    print("## Test 2 - leave-one-out: centroid of the OTHER 7 when each web is removed")
    loo = []
    for k in NAMES:
        g = centroid([j for j in NAMES if j != k])
        loo.append((dist(C, g), k))
    for d, k in sorted(loo):
        flag = "  <- removing this one best centres the rest" if (d, k) == min(loo) else ""
        print(f"  drop {k:16s} -> remaining-7 centroid is {d:6.1f} px from centre{flag}")
    best_drop = min(loo)[1]
    print(f"\n  => the single outlier whose removal centres the figure: {best_drop}")
    print()

    # ---- Test 3: Monte-Carlo significance + robustness to +/-25 px coord noise ------
    print(f"## Test 3 - significance & robustness ({TRIALS:,} trials, +/-{NOISE_PX:.0f}px noise)")
    g7 = centroid(no_sd)
    obs7 = dist(C, g7)
    # (a) Is the CENTRE unusually close to the 7-web centroid vs a random map point?
    rand_pts = rng.uniform([bbox[0], bbox[2]], [bbox[1], bbox[3]], size=(TRIALS, 2))
    rand_d = np.hypot(*(rand_pts - g7).T)
    p_central = float((rand_d <= obs7).mean())
    print(f"  (a) centre is {obs7:.1f} px from the 7-web centroid; a RANDOM point in the web")
    print(f"      bbox averages {rand_d.mean():.0f} px away -> p(random point this central) = {p_central:.4f}")
    # (b) Does the finding survive coordinate noise? Re-jitter all coords, recompute.
    keep_sd_far = 0; best_is_sd = 0; d7_samples = []; d8_samples = []
    sd_idx = NAMES.index("SaintDenis_R34")
    base = np.array([P[k] for k in NAMES])
    for _ in range(TRIALS):
        jit = base + rng.uniform(-NOISE_PX, NOISE_PX, size=base.shape)
        cj = C + rng.uniform(-NOISE_PX, NOISE_PX, size=2)
        d8 = np.hypot(*(jit.mean(0) - cj))
        d7 = np.hypot(*(np.delete(jit, sd_idx, 0).mean(0) - cj))
        d7_samples.append(d7); d8_samples.append(d8)
        if d7 < d8:
            keep_sd_far += 1
        # which single removal best centres? is it SD?
        loo_d = [np.hypot(*(np.delete(jit, i, 0).mean(0) - cj)) for i in range(8)]
        if int(np.argmin(loo_d)) == sd_idx:
            best_is_sd += 1
    print(f"  (b) under noise: 7-web centroid is closer than 8-web centroid in "
          f"{keep_sd_far/TRIALS*100:.1f}% of trials")
    print(f"      (median dist: 7-web {np.median(d7_samples):.0f}px vs 8-web {np.median(d8_samples):.0f}px)")
    print(f"      Saint Denis is the single best-to-drop outlier in "
          f"{best_is_sd/TRIALS*100:.1f}% of trials")
    print()

    # ---- Test 4: Saint Denis as the farthest 'leg' (cross-link to [S30]) -----------
    print("## Test 4 - Saint Denis as the singular far outlier (cross-check [S30])")
    dcen = {k: dist(C, P[k]) for k in NAMES}
    for k, d in sorted(dcen.items(), key=lambda x: -x[1]):
        print(f"  {k:16s} {d:6.0f} px from centre, bearing {bearing(CENTRE, P[k]):3.0f} deg")
    far = max(dcen, key=dcen.get)
    second = sorted(dcen.values())[-2]
    print(f"\n  farthest web = {far} ({dcen[far]:.0f}px); next = {second:.0f}px "
          f"-> SD is {dcen[far]/second:.2f}x the next-farthest")
    print("  [S30] independently found the engraving's LONGEST leg points SE -> Saint Denis.")
    print()

    print("## Verdict (evidence, not fact - [SPECULATION] at most; provisional coords)")
    print("  See results/web_geometry_shape.md.")


if __name__ == "__main__":
    main()

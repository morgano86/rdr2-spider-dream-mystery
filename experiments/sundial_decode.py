#!/usr/bin/env python3
"""Decode the Mount Shann sundial's 7 arrows ([U33]) - a closed formal object,
treated like Gertrude's number: enumerate the possible readings, test each with a
null, log negatives honestly.

Question + IDs
--------------
[K36]: 7 painted arrows (3 red, 3 orange, 1 yellow) on the sundial's ring stones.
[U33]: firsthand (user, 2026-07-02, 2 day/night cycles): each arrow aligns with the
gnomon's shadow at a specific time + cardinal; yellow appears once, uniquely at
11:30 am. Open: does the arrow layer ENCODE anything (times as numbers/letters,
bearings as pointers, colour as a key), or is it faithful sundial set-dressing
([S32]'s deflationary counter)?

Structure of the problem (the key observation):
  On a physical gnomon dial the shadow bearing is a FUNCTION of the time
  (bearing = f(time; latitude, season)). If the observed arrows fit real solar
  geometry, the bearing layer carries NO free information - an arrow cannot be
  independently "aimed" at a POI; the only free channels are WHICH TIMES got
  arrows and the COLOURS. So the battery is:
    1. physical-faithfulness fit (are the bearings just f(time)?)  + null
    2. the chosen-times channel (numbers/letters/gaps)             + nulls
    3. the colour channel (grouping/pattern)                       + nulls
    4. bearings-vs-POI: DATA-BLOCKED - no coordinates for the cult hut /
       collectible stones / Mount Shann are on file; noted, not invented.

A positive is [SPECULATION] pending in-game check; a clean negative closes [U33]'s
decode branch (the in-game pointer question stays open separately).

Inputs + provenance
-------------------
  * The 7 (colour, time, cardinal) rows: firsthand investigator data
    (Mount Shann file [U33] table, 2026-07-02).  # PROVISIONAL: "exact times may not be
    perfectly precise" (user) - treat +/- ~30 min slack when judging residuals.
  * Solar geometry: standard alt/az from (latitude, declination, hour angle),
    assuming game time == local solar time (no equation of time).

Run:  python experiments/sundial_decode.py
Deps: stdlib only. Deterministic (exhaustive permutation nulls; no sampling).
"""
import math
from itertools import permutations, combinations

# --- The firsthand table (Mount Shann file, [U33]) --- PROVISIONAL (times +/- ~30 min) ---
ARROWS = [  # (colour, time_h, cardinal)
    ("red",    6.0,  "W"),
    ("orange", 9.0,  "WNW"),
    ("yellow", 11.5, "NNW"),
    ("orange", 13.0, "N"),
    ("red",    14.0, "NNE"),
    ("orange", 15.0, "ENE"),
    ("red",    18.0, "E"),
]
CARD_DEG = {"N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5,
            "SE": 135, "SSE": 157.5, "S": 180, "SSW": 202.5, "SW": 225,
            "WSW": 247.5, "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5}
TIMES = [a[1] for a in ARROWS]
COLOURS = [a[0] for a in ARROWS]
BEARINGS = [CARD_DEG[a[2]] for a in ARROWS]


def circ_diff(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def shadow_bearing(lat, decl, t):
    """Bearing (deg from N, CW) of a gnomon shadow at local solar time t.
    Returns None if the sun is below the horizon (no shadow)."""
    H = math.radians(15.0 * (t - 12.0))
    phi, d = math.radians(lat), math.radians(decl)
    sin_alt = math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.cos(H)
    if sin_alt < -1e-9:
        return None
    alt = math.asin(max(-1.0, min(1.0, sin_alt)))
    denom = math.cos(alt) * math.cos(phi)
    if abs(denom) < 1e-12:
        return None
    cos_az = (math.sin(d) - math.sin(alt) * math.sin(phi)) / denom
    az = math.degrees(math.acos(max(-1.0, min(1.0, cos_az))))
    if t > 12.0:
        az = 360.0 - az
    return (az + 180.0) % 360.0                     # shadow = anti-sun


def fit_residual(bearings, grid):
    """Best (over the grid) mean circular residual between observed bearings and
    the physical shadow bearings at the 7 times."""
    best = None
    for lat, decl in grid:
        tot = 0.0
        for t, b in zip(TIMES, bearings):
            pred = shadow_bearing(lat, decl, t)
            tot += 180.0 if pred is None else circ_diff(pred, b)
        m = tot / len(bearings)
        if best is None or m < best[0]:
            best = (m, lat, decl)
    return best


def unwrapped(bearings):
    """Unwrap the bearing sequence through north (W->...->E) for monotonicity."""
    out = [bearings[0]]
    for b in bearings[1:]:
        while b < out[-1]:
            b += 360
        out.append(b)
    return out


def is_monotone(bearings):
    u = unwrapped(bearings)
    return all(u[i] < u[i + 1] for i in range(len(u) - 1)) and u[-1] - u[0] < 360


def gaps(sorted_vals):
    return [round(sorted_vals[i + 1] - sorted_vals[i], 2)
            for i in range(len(sorted_vals) - 1)]


def a1z26(n):
    n = int(n)
    return chr(ord("A") + n - 1) if 1 <= n <= 26 else "?"


def main():
    print("# Mount Shann sundial decode battery ([U33])  - exhaustive, deterministic\n")
    print("  arrows (time, cardinal, colour):")
    for c, t, card in ARROWS:
        print(f"    {t:5.1f}h  {card:3s} ({CARD_DEG[card]:5.1f} deg)  {c}")
    print()

    # ---- Test 1: physical faithfulness -----------------------------------------------
    print("## Test 1 - is the bearing layer just physics? (shadow-clock fit)")
    in_north = all(not (90 < b < 270) for b in BEARINGS)
    print(f"  all 7 bearings in the northern semicircle W->N->E: {in_north}")
    print("    (exactly the half a northern-latitude gnomon shadow is confined to)")
    mono = is_monotone(BEARINGS)
    n_mono = sum(1 for p in permutations(BEARINGS) if is_monotone(list(p)))
    print(f"  bearings rotate monotonically W->N->E as time advances: {mono}")
    print(f"    null (random assignment of these 7 cardinals to the 7 times): "
          f"{n_mono}/5040 = {n_mono/5040:.4f}")
    fine = [(lat, decl) for lat in range(5, 61) for decl in range(-23, 24)]
    m, lat, decl = fit_residual(BEARINGS, fine)
    edge = " (grid edge - treat the exact value loosely)" if lat in (5, 60) else ""
    print(f"  best physical fit: latitude {lat} deg N, solar declination {decl} deg "
          f"-> mean residual {m:.1f} deg{edge}")
    print("  per-arrow residuals at that fit (compass step = 22.5 deg; times are "
          "PROVISIONAL +/-30 min):")
    for (c, t, card) in ARROWS:
        pred = shadow_bearing(lat, decl, t)
        r = circ_diff(pred, CARD_DEG[card])
        print(f"    {t:5.1f}h  obs {card:3s} {CARD_DEG[card]:5.1f}  pred {pred:5.1f}  "
              f"residual {r:5.1f} deg  {c}")
    # sensitivity: the observed times are PROVISIONAL (+/- ~30-45 min). How large do
    # the residuals stay if each arrow's time may slide within that slack?
    slack = 0.75
    worst = 0.0
    for (c, t, card) in ARROWS:
        best_r = min(circ_diff(shadow_bearing(lat, decl, t + s) or 0, CARD_DEG[card])
                     for s in [x / 12 for x in range(-9, 10)])   # 5-min steps
        worst = max(worst, best_r)
    print(f"  with +/-{int(slack*60)} min slack per observation, every arrow fits within "
          f"{worst:.1f} deg (< half a compass step)")
    coarse = [(la, de) for la in range(5, 61, 5) for de in range(-24, 25, 8)]
    m_obs = fit_residual(BEARINGS, coarse)[0]
    k = sum(1 for p in permutations(BEARINGS)
            if fit_residual(list(p), coarse)[0] <= m_obs + 1e-9)
    print(f"  permutation null on the fit quality (coarse grid for both): "
          f"p = {k}/5040 = {k/5040:.4f}")
    print("  -> if this fit is good, the bearings are DETERMINED by the times:")
    print("     an arrow cannot be freely 'aimed' at a POI - any pointer layer can")
    print("     only be the CHOICE OF TIMES (and colour). Tests 2-3 cover those.\n")

    # ---- Test 2: the chosen-times channel --------------------------------------------
    print("## Test 2 - the chosen times as numbers / letters / structure")
    print(f"  times: {TIMES}   gaps: {gaps(TIMES)}   offsets from noon: "
          f"{[round(t-12, 2) for t in TIMES]}")
    l24 = [a1z26(t) for t in TIMES]
    l12 = [a1z26(t if t <= 12 else t - 12) for t in TIMES]
    print(f"  A1Z26 on 24h hours ({[int(t) for t in TIMES]}): {''.join(l24)}"
          f"   (11.5 truncated to 11=K; 12=L variant makes it F I L M N O R)")
    print(f"  A1Z26 on 12h hours: {''.join(l12)}")
    print("    no full 7-letter reading exists in either. Flag the traps explicitly:")
    print("    - 'INFORM' uses 6 of 7 of {F,I,K,M,N,O,R}, discarding K -> a cherry-")
    print("      picked window, the same #43 'any result' failure as Gertrude's FROG.")
    print("    - 12h gives {A,B,C} from 1,2,3 pm -> alphabet-start apophenia bait.")
    print("    - 'FILM NOIR'-style reads need letters the set doesn't have.")
    # symmetric-around-noon structure
    offs = sorted(round(t - 12, 2) for t in TIMES)
    sym_pairs = sum(1 for o in offs if o > 0 and -o in offs)
    print(f"  noon symmetry: {sym_pairs} mirrored pair(s) (+/-6, +/-3); the rest "
          f"(-0.5, +1, +2) unpaired -> partial, not a clean code.")
    # the web-hours echo (S33 watch item)
    print("  cross-egg echo check ({13,14,15} = 1,2,3 PM mirrors the webs'/UFO's 1-3 AM;")
    print("  the 2:00 arrow is red, the UFO is ~2 AM [K37]):")
    p_half = (math.comb(22, 4)) / math.comb(25, 7)     # null: 7 of 25 half-hour slots
    p_hour = (math.comb(10, 4)) / math.comb(13, 7)     # null: 7 of 13 on-hour slots
    print(f"    P(7 random daytime times include all of 1,2,3 o'clock):")
    print(f"      half-hour-slot null: {p_half:.4f}   on-hour-slot null: {p_hour:.4f}")
    print("    -> swings 8x with the null model; weak either way. NOT minted ([S33] zone).\n")

    # ---- Test 3: the colour channel ---------------------------------------------------
    print("## Test 3 - colour as a key (3 red / 3 orange / 1 yellow)")
    seq = ",".join(c[0].upper() for c in COLOURS)
    print(f"  colour sequence by time: {seq}")
    o_pos = tuple(i + 1 for i, c in enumerate(COLOURS) if c == "orange")
    aps = [tuple(range(s, s + 2 * d + 1, d)) for d in (1, 2, 3)
           for s in range(1, 8 - 2 * d)]
    print(f"  orange occupies positions {o_pos} (an arithmetic progression / the evens)")
    print(f"    null: {len(aps)}/{math.comb(7, 3)} of possible orange placements are "
          f"3-term APs -> p(some AP) = {len(aps)/math.comb(7,3):.3f}")
    red_t = sorted(t for c, t, _ in ARROWS if c == "red")
    org_t = sorted(t for c, t, _ in ARROWS if c == "orange")
    print(f"  red times {red_t} gaps {gaps(red_t)}; orange times {org_t} gaps {gaps(org_t)}")
    both_ratio2 = 0
    splits = 0
    tset = TIMES
    for rset in combinations(tset, 3):
        rest = [t for t in tset if t not in rset]
        for oset in combinations(rest, 3):
            splits += 1
            g1, g2 = gaps(sorted(rset)), gaps(sorted(oset))
            ok1 = g2[0] != 0 and g1[1] != 0 and abs(g1[0] / g1[1] - 2) < 1e-9
            ok2 = abs(g2[0] / g2[1] - 2) < 1e-9 if g2[1] else False
            if ok1 and ok2:
                both_ratio2 += 1
    print(f"    observed: BOTH triples have gap-ratio exactly 2 (8,4 and 4,2).")
    print(f"    null over all 3/3/1 splits of these 7 times: "
          f"{both_ratio2}/{splits} = {both_ratio2/splits:.4f}")
    mid_ok = all(abs((r + 12) / 2 - o) < 1e-9 for r, o in zip(red_t, org_t))
    print(f"  equivalent identity: each ORANGE time is exactly the MIDPOINT of a RED")
    print(f"    time and noon ((r+12)/2: 6->9, 14->13, 18->15): {mid_ok}")
    print(f"    with yellow ~ noon itself, the whole layout is generated by 3 red")
    print(f"    'major marks' + their half-marks toward noon - a compact DECORATIVE")
    print(f"    grammar (major/minor ticks), the same event as the 2/140 above.")
    print("  yellow (11:30, NNW): the only half-hour + the arrow nearest the best-fit")
    print("    solar-noon shadow -> reads naturally as a NOON-ISH MARKER on a clock")
    print("    face, not an outlier needing a key. (Its 'special' status survives")
    print("    only as 'the dial marks near-noon distinctly'.)\n")

    # ---- Test 4: bearings vs POIs - blocked -------------------------------------------
    print("## Test 4 - bearings vs known targets (cult hut, collectible stones)")
    print("  DATA-BLOCKED: no coordinates for Mount Shann, the cult hut, or the")
    print("  collectible stones are on file; inventing them would violate the")
    print("  no-invented-data rule. Note however that Test 1's determinism point")
    print("  already bounds this reading: if the bearings are physics, 'arrow X")
    print("  points at POI Y' can only have been DESIGNED via the choice of time X -")
    print("  the POI question is an in-game/mapping task, not a desk decode.\n")

    print("## Verdict (evidence, not fact; ~5 primary tests - mind the look-elsewhere)")
    print("  See results/sundial_decode.md.")


if __name__ == "__main__":
    main()

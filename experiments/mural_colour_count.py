"""Window Rock 'Strange Statues' mural — is there a BLACK vs RED pigment split? (tests U14 / H3 / S12; bears on H18)

QUESTION
--------
[H3]/[S12] propose that the Window Rock 'Strange Statues' cave-painting mural encodes a
**5-black / 3-red** bird split that mirrors the 8 spider webs' feathers (5 black + 3 red),
making the mural the web *order key* ([U14]). That premise requires the mural to be painted
in TWO distinguishable pigments (a black set and a red set). This script tests that premise
straight off the pixels: does the mural contain a genuine second (black) pigment, or is it a
single red/ochre pigment that merely runs light-to-dark?

INPUTS (provenance/tag)
-----------------------
- images/window-rock/window-rock_strange-statues-mural.webp  [A-derived, B-tier]
    The Red Dead Wiki texture `StrangeStatuesMural.PNG` (CDN, 2026-06-13). Verified this session
    to be byte-for-byte colour-identical to the live wiki original
    (static.wikia.nocookie.net/.../StrangeStatuesMural.PNG, cb=20260111022134): same ink-pixel
    count and same hue histogram. This is the COLOUR-FAITHFUL source.
- images/window-rock/window-rock_strange-statues-mural_extracted.png  [investigator-processed]
    An investigator extraction. Included only to SHOW it is contrast-boosted/desaturated
    (it reads ~51% true-black) and therefore must NOT be used for the colour question.

WHAT A RESULT MEANS
-------------------
- If the faithful image holds two distinct pigment clusters (a red hue cluster AND a true-neutral
  black cluster of comparable mass), the [H3]/[S12] colour premise is at least *possible* -> still
  [SPECULATION] pending a sourced 5/3 colour count.
- If the faithful image is unimodally red (true-neutral black is a small minority that is just deep
  shading of the red), the premise has **no basis in the source art** -> a real NEGATIVE finding
  that demotes [H3]/[S12]. (Corroborated independently: every walkthrough codes the mural by feather
  COUNT + ORIENTATION (upside-down decoys), never colour — GamesRadar/Shacknews/ScreenRant/Fandom.)

A script TESTS; it does not establish fact. A negative here is a loggable finding (see experiments/README.md).

DEPENDENCY: Pillow (see experiments/requirements.txt). Run: python experiments/mural_colour_count.py
"""

from PIL import Image
import os

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)
FAITHFUL = os.path.join(ROOT, "images", "window-rock", "window-rock_strange-statues-mural.webp")
EXTRACTION = os.path.join(ROOT, "images", "window-rock", "window-rock_strange-statues-mural_extracted.png")


def classify(path, label):
    """Test for a SECOND pigment: among genuinely chromatic ink pixels, is any non-red hue present?

    Key idea: every dark paint goes achromatic (near-grey/black) where thickly applied or shadowed,
    so 'true black' pixels do NOT prove a black pigment. A second *pigment* would show up as a second
    CHROMATIC cluster at a different hue. So the decisive measure is: of the clearly-coloured pixels
    (chroma >= 30), what fraction are red-hued vs some other hue?
    """
    im = Image.open(path).convert("RGB")
    px = im.load()
    W, H = im.size
    ink = chromatic = red_hued = other_hued = achromatic_dark = 0
    for y in range(H):
        for x in range(W):
            r, g, b = px[x, y]
            mx, mn = max(r, g, b), min(r, g, b)
            v, chroma = mx, mx - mn
            if v >= 200 or (v >= 150 and chroma < 40):
                continue  # light rock-wall background
            ink += 1
            if chroma >= 30:                       # genuinely coloured -> can carry a pigment hue
                chromatic += 1
                if r == mx and (r - max(g, b)) > 12:   # red leads clearly (0-30 / 330-360 deg)
                    red_hued += 1
                else:
                    other_hued += 1
            elif v < 90:                            # near-grey AND dark = shading / true-black
                achromatic_dark += 1
    red_frac = 100 * red_hued / max(1, chromatic)
    print(f"\n=== {label} ===\n  {os.path.relpath(path, ROOT)}  ({W}x{H}, ink px={ink})")
    print(f"  chromatic ink (chroma>=30) : {chromatic:7d}")
    print(f"    red-hued                 : {red_hued:7d} ({red_frac:5.1f}% of chromatic)")
    print(f"    NON-red-hued (2nd pigment?): {other_hued:7d} ({100*other_hued/max(1,chromatic):5.1f}% of chromatic)")
    print(f"  achromatic-dark (shading)  : {achromatic_dark:7d}  <- NOT proof of a black pigment")
    return dict(chromatic=chromatic, red_hued=red_hued, other_hued=other_hued, red_frac=red_frac)


def main():
    print("Mural pigment test (U14 / H3 / S12) — is there a black-vs-red split, or one red pigment?")
    faithful = classify(FAITHFUL, "COLOUR-FAITHFUL wiki texture (use this)")
    classify(EXTRACTION, "investigator extraction (processed — NOT colour-faithful, shown for contrast)")

    print("\n--- VERDICT (on the colour-faithful image) ---")
    print(f"  of genuinely-coloured pixels, {faithful['red_frac']:.1f}% are RED-hued; "
          f"only {100*faithful['other_hued']/max(1,faithful['chromatic']):.1f}% carry any other hue.")
    if faithful["red_frac"] > 90:
        print("  => ONE chromatic pigment (red/ochre). The dark 'black' figures are deep/shaded red,")
        print("     not a second pigment. There is no black-vs-red bird set to count.")
        print("     [H3]/[S12] 'mural = 5 black / 3 red' has NO basis in the source art -> NEGATIVE.")
        print("     (Independently: every walkthrough codes the mural by feather COUNT + ORIENTATION,")
        print("      i.e. upside-down decoys, never by colour.)")
    else:
        print("  => A second hue cluster exists; colour premise remains testable (still SPECULATION).")


if __name__ == "__main__":
    main()

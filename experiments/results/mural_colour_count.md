# Result — mural_colour_count.py (U14 / H3 / S12; bears on H18)

**Run:** `python experiments/mural_colour_count.py` · 2026-06-21 · deterministic (reads committed images, no network).

## Question
Does the Window Rock "Strange Statues" mural contain a **black vs red** pigment split (which [H3]/[S12] need, to read it as a 5-black/3-red echo of the 8 webs and thus the web *order key*, [U14])? Or is it a single red/ochre pigment that merely runs light-to-dark?

## Inputs
- `images/window-rock/window-rock_strange-statues-mural.webp` — the colour-faithful wiki texture `StrangeStatuesMural.PNG`. Verified this session to be colour-identical (ink count + hue histogram) to the live CDN original (`static.wikia.nocookie.net/.../StrangeStatuesMural.PNG`, cb=20260111022134).
- `images/window-rock/window-rock_strange-statues-mural_extracted.png` — investigator extraction; included only to demonstrate it is **processed** (contrast-boosted), *not* colour-faithful.

## Key output
```
COLOUR-FAITHFUL wiki texture (887x876, ink px=386731)
  chromatic ink (chroma>=30) : 102060
    red-hued                 : 102060 (100.0% of chromatic)
    NON-red-hued (2nd pigment?):     0 (  0.0% of chromatic)
  achromatic-dark (shading)  :  76097  <- NOT proof of a black pigment

investigator extraction (processed — NOT colour-faithful)
    red-hued                 :  73937 (100.0% of chromatic)
    NON-red-hued             :      0 (  0.0% of chromatic)
    achromatic-dark          : 478902  (contrast boost turned dark reds to near-black)
```

## Finding — NEGATIVE for the colour premise
**100.0% of genuinely-coloured pixels are red-hued; 0.0% carry any other hue.** The mural is painted in a **single red/ochre pigment**; the "black"-looking figures are deep/shaded red (achromatic-dark), not a second pigment. The processed extraction's ~51% "true black" is an artifact of contrast-boosting (its chromatic pixels are *also* 100% red), which is why it must not be used for the colour question.

⟹ There is **no black-vs-red bird set to count** — the [H3]/[S12] "mural = 5 black / 3 red → web order key" premise has **no basis in the source art**. Independently corroborated: every walkthrough (GamesRadar, Shacknews, ScreenRant, Fandom) codes the mural by feather **count** + **orientation** (upside-down = decoy), never by colour. [H3]/[S12] demoted; [U14] resolved-negative.

A script TESTS, it does not establish fact — but a negative is a real finding (per `experiments/README.md`).

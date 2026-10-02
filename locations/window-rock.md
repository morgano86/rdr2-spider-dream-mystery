# Window Rock

- **Region:** **Grizzlies WEST**, Ambarino (NW of Fort Wallace, below Granite Pass, south of Whinyard Strait). *(Correction: earlier assumed "East" — it's West.)*
- **Type:** Rock-arch tourist formation; hosts the **Strange Statues cave painting** under an overhang.

## Mystery role — [SPECULATION] → **largely refuted 2026-06-21 ([U14])**
- The Spider Dream Mystery page's *Directional Theory* says the mural "depicts **birds with different amounts of black and red feathers**" and may have a "double meaning" — proposed to rhyme with the webs' **5 black / 3 red** feathers ([H3]/[S12]).
- ⚠️ **The "black & red" wording is from the wiki's own *Directional Theory* — a speculation block** (the Spider Dream page is categorised "Speculation"), **not** a corroborated description, and **the primary mural art contradicts it.** A pixel test of the colour-faithful wiki texture ([`../experiments/mural_colour_count.py`](../experiments/mural_colour_count.py)) finds the mural is a **single red/ochre pigment** — **100% of chromatic ink red-hued, 0% any other hue.** What the theory calls "black" feathers are the **darkly-shaded red** ones; there is **no distinct black pigment and no clean 5-black/3-red partition.** ⟹ **[H3]/[S12] refuted, [U14] closed-negative** — the mural is *not* the web order key. (Independently, every walkthrough codes the puzzle by feather **count + orientation**, never colour.) The webs' own 5/3 split is unaffected (it rests on [H9]/[U29]).
- Image (colour-faithful): [`../images/window-rock/window-rock_strange-statues-mural.webp`](../images/window-rock/window-rock_strange-statues-mural.webp).

## The Strange Statues puzzle — [KNOWN] (a *separate, solved* puzzle)
- The mural is the **clue to the "Strange Statues" finger-puzzle POI** (Grizzlies East): **count the tail feathers on each bird (excluding upside-down birds)** → the counts are **2, 3, 5, 7** → activate the statues holding up those finger counts → reward **4 gold bars** (~$1500 fenced) + core refill.
- Image: [`../images/window-rock/window-rock_strange-statues-poi.png`](../images/window-rock/window-rock_strange-statues-poi.png).

## Why it matters — and the cross-check (now run)
- **2, 3, 5, 7** are the first four **primes**, and both **5** and **3** (the web feather split) appear in that set — which is what made the mural a tempting **order key** candidate. **The colour cross-check has now been run off the colour-faithful wiki texture and came back NEGATIVE** (no second pigment; see *Mystery role* above) — so the "5 black / 3 red mural" never existed, and the 2,3,5,7 ↔ 5,3 overlap is a coincidence of small primes, not a key. Logged in [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md), [connections §5c](../analysis/connections.md), and [`mural_colour_count.py`](../experiments/mural_colour_count.py).

## Resolved
- [x] **Count each mural bird's feathers by colour** — DONE 2026-06-21 from the image (no in-game capture needed): the mural is a **single red pigment**, so there is no per-colour count; it gives the count+orientation reading (2,3,5,7), not a colour code.

> Sources: Red Dead Wiki *Window Rock*, *Strange Statues (Cave Painting)*, *Strange Statues*, *Spider Dream Mystery*. URLs in [sources](../sources/sources.md).

# Analysis — the carving technique, and how to tell a real carving from pareidolia

You made the key methodological point: the clues that matter are **visibly, verifiably carved into the model** — not
textures, and not shapes people *imagine* in noisy surfaces (pareidolia). This file pins down **how Rockstar made these
symbols** and gives a **repeatable test** to separate genuine clues from wishful pattern-matching. This test is how we decide
what's allowed into [known-facts](../findings/known-facts.md) vs. quarantined in [speculation](../findings/speculation.md).

## How the symbols are actually made — [KNOWN]
- The signature symbols are **modelled into the 3D mesh geometry itself, then disguised under the surface (moss/wood)
  texture** — *not* painted onto a flat texture, *not* a decal. The wiki's load-bearing sentence (about the Fort Wallace
  marks): *"two 'w' or bird symbols that are made from the **tower's geometry** and **shaded with the moss texture**,"* and
  *"the same method of **hiding symbols into the geometry** is used for the Butcher Creek outhouses and **not seen anywhere
  else**."*
- So the technique is a **hybrid**: the **shape is real displacement in the mesh (vertices)**, and the everyday surface
  texture is laid over it so it reads as natural noise rather than an obvious engraving. That disguise is *why* it resists
  being dismissed — and also why only a handful of these exist.
- The **webs and the Butcher Creek pentagram are built from actual mesh "cables,"** not textures (Dexerto). Rockstar has a
  known **house technique**: hidden symbols built from spline/cable geometry on a **time-gated spawn** — the same trick used
  for **GTA V's Mount Chiliad** cable-webs (which also spawn **1–2 AM**, like RDR2's centre webs).
- **Dedicated, named assets exist** — the strongest objective proof of intent: webs `spiderdream01–08`, feather texture
  `wap_gen_feather01`, feathers respawn. A one-off coincidence does not get a unique descriptive asset name.

## The verification test — real carving vs. pareidolia
A genuine, intentional clue should pass these. The first three are **objective**; use them before believing any "symbol."

1. **Real depth / parallax (view-angle independence).** Because it's in the mesh, it **holds its shape as the camera moves**
   and **casts/receives real-time shadows**. A flat texture or imagined shape shifts or dissolves with angle and lighting.
2. **Named asset in the game files.** If it has a dedicated mesh/texture name (à la `spiderdream`), it's authored content.
   No file footprint → almost certainly pareidolia.
3. **Time-gated and/or respawns.** Scripted appearance in a narrow window (webs 2–6 AM; centre 1–2 AM; pentagram 4–5 AM) and
   respawn logic are **engine-driven** — impossible for pareidolia.
4. **Part of a reproducible chain that resolves to a place.** Real clues point somewhere any player can re-find (tallies →
   pentagram → outhouse #4 `LJ`/`SM`/Fort-Brennand icon → Fort Brennand symbols → spider pole → webs → `W ✞✞✞✞✞` → `NW`/
   guitar). Each step yields the next find.
5. **(External) developer signal of intent.** See the dev-quote note below.

**Pareidolia red flags (fails the test):** only appears in flat wood/rock noise · no named asset · not time-gated · shifts or
vanishes with angle/lighting · doesn't reproducibly point to a next clue. The wiki itself **flags everything past the guitar
symbol as speculative** and warns by name that "various symbols in the wood and rocks" are *"a simple case of pareidolia."*

**Inverse caution ([S13]).** This test guards against seeing clues that aren't there. The *opposite* failure is **missing a
real clue because it's dressed up as an obvious "dev in-joke" or real-world reference** (e.g. Register Rock's A. West /
B. Ward → *Batman*, per unconfirmed wiki speculation). Camouflage-as-joke is plausible deliberate design, so don't discard a
candidate on "that's just a gag" alone — apply the same evidence test instead. See [findings/speculation.md](../findings/speculation.md) S13.

## Where the boundary actually sits — [KNOWN / honest]
- **Confirmed-method clues (trust):** Butcher Creek tallies + `LJ`/`SM` + Fort Brennand icon; the pentagram; the spider
  engraving; the 8 webs + feathers; the `W`/`NW`+guitar inscriptions. All pass tests 1–4.
- **Borderline (the bird/"w" symbols at Fort Wallace):** taken seriously **only because they share the confirmed
  geometry-hiding method** with the Butcher Creek outhouses (pcgamesn calls it "the same custom wireframe technique");
  the wiki still says they *"may simply be a modeling error or developer initials… heavily up for debate."* It's the
  **methodological fingerprint, not the visual**, that elevates them.
- **Fails the test (treat as pareidolia until proven):** the off-map **"question mark"** shapes in the mountains; assorted
  "symbols in rocks." Keep these in [speculation](../findings/speculation.md).
  → [`../images/fort-wallace/fort-wallace_questionmark_view1.webp`](../images/fort-wallace/fort-wallace_questionmark_view1.webp)

## The "is it dev-confirmed?" question — [DISPUTED]
- A former Rockstar **QA tester, reportedly Adam Butterworth**, publicly reacted to the find — quote circulated as *"Absolutely
  wild people have found this. I remember hearing about this and thinking it would never be discovered"* (Popverse, RDR2.org,
  Hypebeast Jan 2026). This **supports intentionality**.
- **BUT** our adversarial verification pass **refuted (1-2)** the stronger framing that he "**confirmed it was intentionally
  created by developers**." A QA tester *reacting with surprise* is evidence of a real Easter egg; it is **not** the same as
  a designer confirming design intent or revealing the solution. **Use:** "a dev publicly reacted, consistent with intent" —
  not "a dev confirmed the design/solution."

## [UNKNOWN]
- **Direct datamining proof** of vertex-displacement vs. baked normal-map for the `LJ`/`SM`/bird symbols. The wiki says
  "made from the geometry"; no extracted-mesh screenshot confirms it at the polygon level. Treat "vertex geometry" as the
  **wiki's claim**, strongly implied, not file-proven.
- Whether each tally mark is a tiny modelled etch or part of a texture (grouped with the geometry method by implication).

## Practical takeaway for our captures
When you screenshot a candidate carving, **shoot it from 2–3 angles and note shadowing** — that single habit lets anyone
later confirm depth (test 1) and keeps pareidolia out of [known-facts](../findings/known-facts.md).

> Sources: Red Dead Wiki *Spider Dream Mystery*; Dexerto; pcgamesn; Popverse; RDR2.org; Hypebeast. URLs in
> [sources/sources.md](../sources/sources.md).

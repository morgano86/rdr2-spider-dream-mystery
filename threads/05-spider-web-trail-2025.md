# Thread 05 — The Spider Web telegraph-pole trail (most active branch)

The concrete, navigable core of the mystery and the reason it resurfaced after ~7 years (the first webs were found and the
chain assembled in **late 2025**). This thread now follows the **primary Red Dead Wiki** text (Parts 2–4); see
[PRIMARY-wiki-spider-dream.md](../sources/PRIMARY-wiki-spider-dream.md). Downloaded images are referenced inline.

---

## [KNOWN] — the navigable chain (primary wiki)

1. **Start pole.** Fort Brennand's three symbols point to a **telephone pole near Cornwall Kerosene & Tar** bearing a
   **spider engraving**. Atop it is a **web + feather** visible **only at a specific hour**.
   → [`web_cornwall_b34_engraving.webp`](../images/webs/web_cornwall_b34_engraving.webp)
2. **The engraving is a map.** It shows the **direction/location of 7 other webs** following the same pattern; the spider's
   **"eye" directs the player toward more poles**. Each web is **time-locked to a different night hour** (2–3am, 3–4am, …)
   and won't appear otherwise. One web is **near Saint Denis** (3–4am).
   → [`web_map-overlay_all-locations.webp`](../images/webs/web_map-overlay_all-locations.webp),
   [`web_saint-denis_r34.webp`](../images/webs/web_saint-denis_r34.webp)
3. **Center webs.** At the **center** of the spider is another set of webs that appear **1–2am** and have **no feathers**.
   Lined up, they spell an **`N`** and a **telephone pole** (= go **north**).
   → [`web_centre_n-pole_1-2am.webp`](../images/webs/web_centre_n-pole_1-2am.webp)
4. **First inscription.** Travel **directly north** of the center webs to a pole you can **shoot to reveal an inscription**:
   **`W ✞✞✞✞✞`**. The "crosses" are **telephone poles**; `W` = **West** → travel **5 poles west**.
   → [`trail-marker_w-five-poles-inscription.webp`](../images/trail-markers/trail-marker_w-five-poles-inscription.webp)
5. **Second inscription.** Five poles west, another pole (shot many times) reveals **`NW`** + a symbol that **looks like a
   guitar**. → [`trail-marker_nw-guitar-inscription.webp`](../images/trail-markers/trail-marker_nw-guitar-inscription.webp),
   [`trail-marker_guitar-pole_location.webp`](../images/trail-markers/trail-marker_guitar-pole_location.webp)
6. **Waypoint (not dead-end).** `NW` points toward **Fort Wallace**, which contains **two guitars** (one points toward a
   tower; the second, on the tower, points to its roof). ⚠️ **Updated 2026-06-13:** Fort Wallace is a **waypoint — the trail
   continues past it.** The current (post-Jan-2026, **unverified**) frontier runs toward **Calumet Ravine / the Giant's birds**
   and a **"?" carving on an out-of-bounds mountain**, where it goes cold → [06](06-bird-carving-giant-wapiti.md). **No
   secondary source supports the wiki-only "Spider Gorge" reading** (see SPECULATION below + [U13](../findings/unknowns.md)).

> **Corroboration + bounded negative ([K12], deep-research 2026-06-14, [#60], resolves [U1]).** The verbatim chain above was
> **single-sourced** before this pass; it is now **multiply B-tier corroborated** (Fandom-via-API, ScreenRant, PCGamesN,
> GameRant, GamingBolt, Dexerto, RDR2.org). The **five**-glyph count on the north pole is **unanimous**; the **guitar identity is
> hedged by every source** (a flat "it IS a guitar" reading was refuted 0-3 — see [U12]). **Steps 4–5 are the ONLY two
> shot-to-reveal poles on the trail, and the `NW`+guitar pole is the LAST documented under-pole message — no third pole
> inscription is documented anywhere.** Everything "past" it is *non-pole* content: the Fort Wallace **bird carvings** (the
> verified frontier [K16]) and the out-of-bounds **"?"** (pareidolia) — neither is an under-pole inscription. The centre `N`
> (step 3) is an **alignment/overlay** reveal, *not* a shot pole — don't conflate the two mechanics.

## [KNOWN] — feather file data
- Web feathers are internally called **"spiderdream"**; they **respawn** when shot; texture **`wap_gen_feather01`**.
- **Total: 5 black feathers + 3 red feathers** across the webs found. *(This 5/3 split is a candidate code — see U14/U15.)*

## [KNOWN] — the boundary / feather respawn mechanics (investigator data; full detail → [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md))
- **[K21] Respawn is boundary-gated:** a shot feather falls to the ground (can't be picked up) and **won't respawn while you stay
  inside the boundary that web is tied to**; leaving respawns it. **Three boundaries** — top (north), connector, bottom (south).
- **[K31] Membership firsthand-confirmed** (resolves [U22]): **Top** `B34` · **Connector** `B23,B45,B56,B56L` · **Bottom**
  `R23,R45,R34`; the boundaries **overlap**, so each also contains *untied* adjacent webs (shooting those fires the wrong despawn).
- **[K29] State persists across nights + camping** (≥12 in-game days) while in-boundary — the fallen feather's exact floor spot
  is stored and restored; it returns to the web only after you **leave** the boundary. The ground position is shot-physics
  (encodes nothing). ⟹ a solver has many in-game days to work the order ([U29]/[H20]).
- **[K30] Render-gating:** a web/feather won't spawn while you look straight at the spot (look away/back), and won't despawn
  while in view (you can hold one rendered past its hour by keeping line of sight). Open: hit counts by visibility or by hour
  ([U30]).

## [KNOWN] — discovery credits (for provenance, not solution)
- First web(s): **goldenplaysterraria, pariah87, u/fthen2k02, u/FL4VA-01**.
- The **fort symbol**: **u/TracySevert**.
- The **connection to the mystery + the Fort Brennand markings**: **Strange Man** (YouTube).

## [UNKNOWN]
- ~~**Verbatim content of the under-wood inscriptions** beyond `W ✞✞✞✞✞` and `NW`+guitar — are there more poles/messages?~~
  **[RESOLVED 2026-06-14 → [K12]/[U1]]:** no — exactly **two** shot-to-reveal poles; `NW`+guitar is the **last** documented
  under-pole message; no third is documented in any source (deep-research [#60]).
- **Exact map coordinates** of the start pole, each of the 7 webs, the center webs, and the two inscription poles.
- **What the guitar means** and whether **Fort Wallace** is the destination or a misdirect.
- **Is the puzzle finished?** Confirmed **still unsolved with NO payoff as of June 2026** (Popverse, Kotaku, comicbook,
  Dexerto, all Jan 2026): *"No new loot, tools, or cutscenes"* — **vindication is the only reported "reward."** The wiki flags
  it may be **cut content** (NW points toward a **beta location** — Wapiti / an army camp / Iron Cloud); note this is **one
  possibility, not "the leading theory"** (that characterisation was killed in an earlier pass).
- The exact pole **count** (the engraving implies the start + **7 others** + a **central** cluster; reconcile with secondary
  "8 + center" phrasing).

## [SPECULATION] (wiki Part 4 — explicitly speculative)
- **Directional theory:** following the guitars' heading lands at **Dodd's Bluff**, **Vetter's Echo**, **Window Rock**. NW
  also points to **Fort Wallace, Chez Porter, Cotorra Springs, Tempest Rim, Bacchus Bridge**, and **directly to the very tip
  of Spider Gorge** — which has **"spider" in its name** and a **guitar-shaped section**. ⚠️ **Caveat (2026-06-13):** the
  Spider Gorge reading is **wiki-only (Part 4 speculation)** — a deep-research pass found **no secondary source corroborates
  it**, and journalism consistently points the `NW`+guitar marker at **Fort Wallace** instead. Keep as thematically appealing
  [SPECULATION], not a co-equal destination.
- **Window Rock "Strange Statues" mural:** depicts **birds with differing black/red feather counts** — note the webs' own
  **5 black / 3 red** feathers — plus many symbols; possibly a second layer.
  → [`window-rock_strange-statues-mural.webp`](../images/window-rock/window-rock_strange-statues-mural.webp)
- **Feather-trigger theory:** shooting the feathers in a **specific pattern/condition** may fire a hidden trigger (guitar =
  red herring).
- **Birds theory at Fort Wallace:** two **"w"/bird** symbols hidden in the tower geometry/moss — could be dev initials or
  real (the geometry-hidden-symbol trick is otherwise **only** used at the Butcher Creek outhouses).
  → [`fort-wallace_bird-symbols_tower.webp`](../images/fort-wallace/fort-wallace_bird-symbols_tower.webp)
- **Strange Man's extension:** the birds point to a nearby **flock leading to the Giant's cave**, and a **question-mark
  shape** is visible off-map from there — **not a popular or widely accepted theory; widely called pareidolia** (it fails the
  [carving test](../analysis/carving-technique.md)). The **bird carvings are the last *verified* clue** ([K16]); this and the
  Bacchus heart sit past it as **contested** leads.
  → [`fort-wallace_questionmark_view1.webp`](../images/fort-wallace/fort-wallace_questionmark_view1.webp), [`fort-wallace_questionmark_view2.webp`](../images/fort-wallace/fort-wallace_questionmark_view2.webp)
- **Native connection:** feathers + spider may invoke the **Spider Grandmother** myth / the game's Native storyline.

## [SPECULATION] — outward  *(full dossier: [analysis/gta-rdr2-crossover.md](../analysis/gta-rdr2-crossover.md))*
- **GTA V Mount Chiliad** has **two cable-webs** that spawn **1–2am** (same window as RDR2's centre webs). **[KNOWN now —
  [K24]]:** these are **base-game since GTA V's 2013 launch — not DLC** — and use the **same cable shader** as RDR2's webs
  ([K15]). The shared shader + shared 1–2 AM gate argue this is **deliberate**; link popularized ~Jan 2026 (Oddheader). Still
  **no confirmed shared solution** ([U18]).
- The **Nazar "Nazar Speaks"** machine fortune (GTA Online, Diamond Casino Heist, **Dec 2019**) reads: *"I see a web, still
  tangled after years of unraveling. Will you be the one? I wonder…"* — **confirmed a real in-game line** (#44). The **same
  machine** also speaks **Gertrude's number** ([K23]) and names other RDR2 places (**Window Rock, Roanoke Ridge, Grizzlies** —
  [S14]). Possibly an official wink at this egg; unproven ([U19]).
- The **dreamcatchers** side mission has a log entry that oddly **doesn't clear** after all 20 are collected (the spider wiki
  cites this only by **analogy** — *this* mystery has **no log at all**, [K20](../findings/known-facts.md)). The live theory
  (**H8**): the dreamcatcher entry may be stuck because something is **left to finish — possibly this mystery** — so completing
  the spider trail might be what clears it (falsifiable, untested). More importantly, the dreamcatcher reward works by
  **connecting all 20 collectible points into a drawn animal and finding its eye** — the same *connect-points-into-a-shape*
  mechanic as this web trail, and a shipped precedent against the "it's just pareidolia" objection. Full analysis →
  [analysis/dreamcatchers.md](../analysis/dreamcatchers.md) (and [U17](../findings/unknowns.md)).

## Open tasks
- [ ] Capture every inscription verbatim + coordinates for all poles/webs; build a labeled map overlay in `images/maps/`.
- [ ] Test the **5 black / 3 red** feather split against the **Window Rock mural** bird-feather counts.
- [ ] Investigate **Spider Gorge** (guitar-shaped section) as the true target; log results.
- [ ] Determine whether the trail is complete or cut content (compare NW heading vs known beta locations).

## Sources
**Primary:** Red Dead Wiki *Spider Dream Mystery* Parts 2–4. Secondary: RDR2.org, GamesRadar, Dexerto, Johnny5Arcade,
DailyDot, X/@SynthPotato, Strange Man (YouTube). **Inscription chain multiply corroborated** by the 2026-06-14 deep-research
pass ([#60]: + ScreenRant, PCGamesN, GameRant, GamingBolt). See [sources/sources.md](../sources/sources.md).

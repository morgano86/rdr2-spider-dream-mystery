# Images

Downloaded screenshots, maps, and diagrams, organized **by location/topic** so every image backs a specific claim.

## Naming convention (enforced)
Every image filename follows:

```
<subject>_<detail>[_<qualifier>].<ext>
```

- **All lowercase, ASCII.** Extension reflects the true format (`.webp` / `.png` / `.jpg`).
- **Fields are separated by `_`; words *within* a field use `-`.** So `_` splits the meaning into parts, `-` keeps a
  multi-word part readable: `fort-wallace_bird-symbols_tower.webp` → subject `fort-wallace`, detail `bird-symbols`, qualifier `tower`.
- **`<subject>`** = the place or thing the image is *about* (kebab slug), e.g. `butcher-creek`, `fort-brennand`,
  `vetters-echo`, `window-rock`, `the-giant`, `dreamcatcher`. This is the subject, **not necessarily the folder** — e.g.
  the Fort Brennand shot lives in `butcher-creek/` (thematic grouping) but is named `fort-brennand_…`.
- **`<detail>`** = what it shows (kebab): `floorboard-pentagram`, `tower-symbols`, `journal-drawing`.
- **`<qualifier>`** *(optional)* = disambiguator: a time (`1-2am`), a web code (`b34`), or a view index (`view1`, `view2`).
- **Webs** are a documented sub-pattern: `web_<location>_<code>[_<detail>].webp` (code = colour+hour, e.g. `b34`, `r34`).
  The centre cluster has no code: `web_centre_n-pole_1-2am.webp`. See [`webs/WEBS-MANIFEST.md`](webs/WEBS-MANIFEST.md).

When you add an image: name it to this rule, drop it in the right folder, and add a provenance row below.

## Folders
- `butcher-creek/` — floorboard pentagram, outhouse tally pentagram, outhouse #4 `LJ`/`SM`/Fort-Brennand carving, Fort Brennand symbols.
- `matchsticks/` — the match-letter clues (`EC` by the Black Widow card; later `J+M`, `S+J`).
- `webs/` — the spider engraving (map), the location overlay, and **each individual web + feather**. See **[`webs/WEBS-MANIFEST.md`](webs/WEBS-MANIFEST.md)** — the per-web tracker (location · time · feather colour · feather position).
- `trail-markers/` — the inscriptions that chain the poles (`W ✞✞✞✞✞`, `NW` + guitar) and the guitar pole location.
- `fort-wallace/` — the disputed "w"/bird tower symbols + the alleged off-map "question mark" shots.
- `window-rock/` — the Strange Statues cave-painting mural (birds w/ black & red feathers).
- `dreamcatchers/` — the Dreamcatcher collectible + the journal drawing that connects the 20 points into an animal (see [analysis/dreamcatchers.md](../analysis/dreamcatchers.md)).
- `saint-denis-vampire/` — the Saint Denis Vampire Easter egg ([K27]): the 5-clue **locations map / pentagram**, the **in-game journal** pages (wall writings + sketches), Arthur's & John's journal drawings, the vampire, and the Ornate Dagger reward. The shipped pentagram-mapping precedent (see [analysis/saint-denis-vampire.md](../analysis/saint-denis-vampire.md)).
- `wapiti-giant/` — the Giant's cave + map location (NW cold-frontier lead).
- `register-rock/` — the Heartlands names-and-dates boulder ("S. Gray 1846") possibly named by the Fort Brennand 3rd symbol ([H11]).
- `bacchus-bridge/` — the Cumberland Forest truss bridge with the hidden **empty heart** ([K22]) + the Flatneck heart datamine reference.
- `maps/` — base-map crops, our own built overlays (labelled pole/web positions), and the **in-game prop-map coordinate
  grids** ([K26]) — the two *"Railroad & State Map"* maps photographed at a stranger's camp.

## Provenance log
All 16 wiki images below pulled **2026-06-13** from the Red Dead Wiki via its CDN (`static.wikia.nocookie.net/reddeadredemption`);
the wiki web/page routes are Cloudflare-blocked but the MediaWiki API + CDN are not. Fandom files are **WebP**. Always log the
**source URL/wiki file** for anything added — a sourced+verified web image is preferred over an in-game capture (see sourcing note).

| File (current path) | Shows | Source file |
|------|-------|-----------|
| `butcher-creek/butcher-creek_floorboard-pentagram.webp` | The glowing Butcher Creek floorboard pentagram (start point) | Butcher_Creek_Pentagram.PNG |
| `butcher-creek/butcher-creek_outhouse-tally-pentagram.webp` | Outhouse tally numbers that form a pentagram when connected in order | ButcherCreekOuthouses.PNG |
| `butcher-creek/butcher-creek_outhouse4-lj-sm-carving.webp` | **Outhouse #4: `LJ` + `SM` + Fort Brennand symbol** (verified by eye) | FortandLetters.PNG |
| `butcher-creek/fort-brennand_tower-symbols.webp` | Fort Brennand tally marks + telephone-pole/factory/oil-puddle symbols | FortBren.PNG |
| `webs/web_cornwall_b34_engraving.webp` | Spider engraving on the pole by Cornwall Kerosene & Tar (trail start) | SpiderEngraving.PNG |
| `webs/web_map-overlay_all-locations.webp` | The engraving as a map showing other web locations / pole directions | SpiderWebLocations.png |
| `webs/web_saint-denis_r34.webp` | A web near Saint Denis, only visible 3–4am | SpiderWebPole.png |
| `webs/web_centre_n-pole_1-2am.webp` | Centre webs lined up to reveal the `N` + telephone pole (1–2am, no feather) | CenterWeb.PNG |
| `trail-markers/trail-marker_w-five-poles-inscription.webp` | Pole inscription `W ✞✞✞✞✞` (= 5 poles west) | TelephonePoles.png |
| `trail-markers/trail-marker_nw-guitar-inscription.webp` | The guitar pole (`NW` + guitar) revealed after many shots | GuitarPole.png |
| `trail-markers/trail-marker_guitar-pole_location.webp` | Guitar-pole location; NW leads toward Fort Wallace (waypoint) | GuitarPoleLocation.PNG |
| `fort-wallace/fort-wallace_bird-symbols_tower.webp` | The disputed "w"/bird symbols above the Fort Wallace guitar | FortWallaceSymbols.PNG |
| `fort-wallace/fort-wallace_questionmark_view1.webp` | Alleged off-map "question mark" shape (pareidolia?) | Questionmark1.PNG |
| `fort-wallace/fort-wallace_questionmark_view2.webp` | Second "question mark" view | Questionmark2.PNG |
| `window-rock/window-rock_strange-statues-mural.webp` | Window Rock "Strange Statues" mural (birds + black/red feathers) | StrangeStatuesMural.PNG |
| `window-rock/window-rock_strange-statues-poi.png` | Strange Statues painting — point-of-interest crop | (community POI crop) |
| `matchsticks/vetters-echo_matchstick-ec_black-widow.webp` | **Matches spelling `EC` beside the Black Widow card** @ Vetter's Echo (verified) | Ecspider.PNG |
| `dreamcatchers/dreamcatcher_journal-drawing.webp` | **Journal drawing connecting all 20 dreamcatcher points into an animal** (eye = Elysian Pool) | Dreamcatcher drawing Arthur Morgan rdr2.png |
| `dreamcatchers/dreamcatcher_in-tree.webp` | A single dreamcatcher hung in a tree (the collectible itself) | Rdr2_dreamcatcher.jpg |
| `wapiti-giant/the-giant_map-location.jpg` | The Giant's cave — map location (Grizzlies East) | (wiki map) |
| `wapiti-giant/the-giant_cave-home.jpg` | The Giant's cave interior / home | (wiki) |

### Added 2026-06-13 — community Google Site (Timeline & Facts pages, [source #36](../sources/sources.md)) · **C-tier, verify**
Pulled from `lh3.googleusercontent.com` (the site is JS-rendered; image URLs were extracted from the raw page HTML, not
the rendered DOM). Community-made overlays/datamines — credits are visible on the images (Jay_0048, thecochiti). Treat as
leads corroborated against the manifest, **not** primary.

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_map-overlay_all-labeled.jpg` | **Best all-webs reference map** — every web labelled by name + code + hour (Cornwall/B34 3–4 … Saint Denis/R34 3–4), plus Centre Web (1–2), the W-5-poles pole, and the NW Guitar Pole | Google Site Timeline |
| `webs/web_map-overlay_shooting-chain.png` | Map colour-coding the **non-respawn chain** (start orange, yellow = `B23,B45,B56,B56L`, red = the red webs) — visualises [K13b](../INDEX.md)/[H4](../INDEX.md) | Google Site (credit **Jay_0048**) |
| `webs/web_map-overlay_boundaries.png` | The **three respawn boundaries** drawn as rectangles — North (`B34`), Connector (`B23,B45,B56,B56L`), South (`R23,R45,R34`); the feather stays down while you're inside its boundary. Visualises [K21](../INDEX.md)/[H9](../INDEX.md) | Google Site (credit **Jay_0048**) |
| `webs/web_map-overlay_nw-trail.jpg` | Spider-shape overlay with the **trail drawn NW past the guitar pole to a "?"** — the cold frontier ([thread 06](../threads/06-bird-carving-giant-wapiti.md)) | Google Site Timeline |
| `webs/web_cable-mesh_datamine.png` | **Datamined web wireframe** — the four `cablemesh*` models (`87399_thvy001`, `87405_hvlit001`, `87397_thvy001`, `87455_hvlit001`); yellow = feather positions in the mesh. Corroborates the shared GTA V/RDR2 cable-shader build | Google Site (credit **thecochiti**) |
| `webs/web_cornwall_b34_pole-carving.jpg` | The Cornwall **spider/"W" carving on the actual telegraph pole** in-world (daytime), railway behind — complements the engraving-as-map shot | Google Site Timeline |
| `fort-wallace/fort-wallace_two-guitars_map.png` | Fort Wallace's **two guitars** annotated — "Tower Guitar" vs "Out-in-the-open Guitar" (they point different ways) | Google Site Timeline |
| `fort-wallace/fort-wallace_bird-symbols_tower_view2.jpg` | **Clearer daytime view of the two moss "w"/bird symbols** on the tower-roof slats (cf. `fort-wallace_bird-symbols_tower.webp`) | Google Site Timeline |

### Added 2026-06-13 — Register Rock & Bacchus Bridge leads (wiki CDN + datamine)
| File (current path) | Shows | Source file |
|------|-------|-----------|
| `register-rock/register-rock_carving_in-world.webp` | Register Rock in-world — **"S. Gray 1846"** legible (names = possible puzzle, [H11]/[U24]) | RDR2_POI_48_Register Rock_01.png |
| `register-rock/register-rock_carving_in-world_view2.webp` | In-world wide shot of the **opposite face** (faint "…Henry… Dortha…" visible); the J.V. Henry side | RDR2_POI_48_Register Rock_02.png |
| `register-rock/register-rock_journal-drawing.webp` | Journal sketch #1 of the rock's names (C. Riley/Wyoming, B. Ward, Frank Heck, T·Bart Texas, DOF, W.Y.B) | RDR2_POI_48_Register Rock_J.png |
| `register-rock/register-rock_journal-drawing_view2.webp` | **Clearer** journal sketch #2 of the same face — corrects readings to **"98 T·BART · TEXAS"**, boxed **"DOF"**, legible **"A. Pickel"**; partial **"E M / S"** mark cut off at the right edge | RDR2_POI_48_Register Rock_03.png |
| `register-rock/register-rock_map-location.webp` | Map location — central **The Heartlands** (where the Fort Brennand symbols point) | RDR2_POI_48_Register Rock_05.png |
| `register-rock/register-rock_carving_henry-doyle-face.jpg` | **Firsthand-verified close-up** (Tumblr [src #39](../sources/sources.md)) of the face with **"Doyle / Missouri", boxed "BM", R.M, R.S** | reddeadreference Tumblr Photo 2 (EXIF: RDR2 screenshot, 2022) |
| `register-rock/register-rock_carving_brooks-munson-face.jpg` | **Firsthand-verified close-up** (Tumblr [src #39](../sources/sources.md)) of the face with **"J. Brooks / US Post 1863", "J.V. Henry 1842 / Dortha. Ohio", "Henry Matilda / Calif.", "Mary", ".8DB8.", "Oregon Wagon Train Jasper Munson"** | reddeadreference Tumblr Photo 4 (EXIF: RDR2 screenshot, 2022) |
| `bacchus-bridge/bacchus-bridge_overview.webp` | Bacchus Bridge (Cumberland Forest) — the truss bridge whose leg bears the **empty heart** ([K22]) | Bacchus Bridge rdr2.jpg |
| `bacchus-bridge/flatneck-station_heart-carving_datamine.png` | **Reference:** the *filled* Flatneck "Lillie ♥ Alfred" heart (datamined `…treeplaceholder2` alpha) — the Bacchus heart is this shape but **blank** | Google Site Timeline (datamine) |

### Added 2026-06-13 — matchstick letter sets `J+M` & `S+J` (Reddit, via Arctic Shift mirror) · **C-tier, corroborated by investigator data**
Reddit's HTML/JSON front door **403-blocks** our fetcher (UA-agnostic — it's an egress-IP block), but the **Arctic Shift**
community data mirror (`arctic-shift.photon-reddit.com/api`) is **not** blocked and returns post metadata + image URLs; the
`i.redd.it` image CDN is **also reachable**. Pulled the two missing letter sets from r/reddeadmysteries and **verified each
against the user's own firsthand in-game screenshot** (2026-06-13) — same letters, same props, same pinned location. See the
recipe in [`sources/RESOURCES.md`](../sources/RESOURCES.md#access-cookbook-the-fetch-recipes-that-actually-work).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `matchsticks/cornwall-kerosene-tar_matchstick-jm.png` | **Matches spelling `J + M`** on a table at **Cornwall Kerosene & Tar** (the web-trail START site), beside a *Diablo's Matches* box, a **William Sletcher "Weight Lifter"** cigarette card and a **Maude Engel** photo. Confirms [K9] `J+M`@Cornwall | Reddit r/reddeadmysteries, u/Jeralt ([post](https://reddit.com/r/reddeadmysteries/comments/chnaxq/)) → `i.redd.it/1fuypjvx5gc31.png`. **Verified vs investigator screenshot 2026-06-13.** |
| `matchsticks/caliga-hall_matchstick-sj.jpg` | **Matches spelling `S + J`** on a table at **Caliga Hall** (the Gray estate), with an ashtray of matches + a *Diablo's Matches* box; player holding a *Vistas of America* card. Confirms [K9] `S+J`@Caliga Hall | Reddit r/reddeadmysteries, u/KermitTheFraud92 ("on a table in caliga hall", [post](https://reddit.com/r/reddeadmysteries/comments/i75ax5/)) → `i.redd.it/zg1izs0cl6g51.jpg`. **Verified vs investigator screenshot 2026-06-13.** |

### Added 2026-06-13 — first feather-orientation captures (Reddit, via Arctic Shift mirror) · **C-tier, location unconfirmed**
From the r/reddeadmysteries **"Zoological"** post (u/Suspicious-Ad6283, ~2026-06) — two in-world web shots that finally show a
feather *in* the web (the repo's [#1 still-wanted](#still-wanted-images-source-from-the-web-first) item). Colour is legible;
the specific web is **not** identifiable from the frame. See the orientation note in [`webs/WEBS-MANIFEST.md`](webs/WEBS-MANIFEST.md).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_black-feather_railway-pole_loc-unconfirmed.jpg` | A **black** feather hanging tip-down, lower-centre, in a pole-web over a railway (one of the 5 black webs — Cornwall/Oil Fields/Overflow/Emerald/Ringneck) | Reddit r/reddeadmysteries, u/Suspicious-Ad6283 "Zoological" → `i.redd.it/3842h740f56h1.jpg` |
| `webs/web_red-feather_railway-pole_loc-unconfirmed.jpg` | A **red** feather hanging tip-down, lower-centre, in a pole-web over a curving railway (one of the 3 red webs — Saint Denis/Southfield/Scarlett) | Reddit r/reddeadmysteries, u/Suspicious-Ad6283 "Zoological" → `i.redd.it/nwz8dz70f56h1.jpg` |
| `webs/cardinal_female-in-flight_feather-reference.jpg` | In-game **female Northern Cardinal** in flight — brown body, **red-edged wing/tail feathers**. Reference for the cardinal-feather theory **[S15]** | Reddit r/reddeadmysteries, u/Suspicious-Ad6283 "Zoological" → `i.redd.it/u3mkoiwze56h1.jpg` |
| `butcher-creek/butcher-creek_pole-datamine-names.png` | Datamine map labelling the Butcher Creek props by **entity name** — `but_pignpole07x###` (telegraph poles), `but_01_magicstuff001` (ritual site). Corroborates the cable/telegraph asset-folder grouping ([K24]) | Reddit r/reddeadmysteries, u/fireflighTim "Decoding Butcher Creek" → `i.redd.it/p6wmolu2hcig1.png` |
| `butcher-creek/butcher-creek_outhouse-datamine-names_pentagram.png` | The 5 outhouses (`but_01 outhouse cliff 000–004`) connected into the pentagram — datamine entity names visible. Corroborates [K5] | Reddit r/reddeadmysteries, u/fireflighTim "Decoding Butcher Creek" → `i.redd.it/xnevsg55hcig1.png` |

### Added 2026-06-13 — ★ FULL feather-position set, all 8 webs ([U0]/[H4], Reddit via Arctic Shift) · **C-tier, high-value**
u/dropthepress's r/reddeadmysteries post **"High-quality spiderweb screenshots"** ([#59]) shot **every web front + side** — the
first source to document feather position for all 8 (the repo's long-standing [#1 still-wanted](#still-wanted-images-source-from-the-web-first)
item). **16 web shots + 1 location/colour map.** Saved under [`webs/feather-positions/`](webs/feather-positions/README.md)
(full per-image index there). **Finding:** every feather **hangs tip-down by gravity** → **refutes [H4]**; only the per-web
*attachment point* varies. *(Supersedes the two `*_loc-unconfirmed.jpg` captures above — now a subset.)*

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/feather-positions/web_<location>_<code>_<front\|side>.jpg` (16) | All 8 webs, **front** + **side**, **location-mapped** (names = real web per the post selftext, 2026-06-14); feather **tip-down** in every one. Per-image position table in the [folder README](webs/feather-positions/README.md) | Reddit r/reddeadmysteries, u/dropthepress "High-quality spiderweb screenshots" (`1qbhkjm`) → `i.redd.it` |
| `webs/web_map-overlay_locations-by-colour_dropthepress.png` | The 8 web locations on the map, **colour-coded by feather** (black/red legend) | same post |

### Added 2026-06-13 — extracted/transparent symbol assets (investigator-supplied) · **derived from in-game (A)**
Clean alpha-channel extractions of the key carved symbols, dropped via `TEMP_IMG` and filed to their subject folders. Useful
for overlay/comparison work (e.g. matching the spider etching to a map, reading the guitar/W-poles glyphs).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_cornwall_b34_engraving_extracted.png` | The Cornwall **spider etching**, textured, isolated on transparent bg | Investigator-supplied extraction (in-game asset) |
| `webs/web_cornwall_b34_engraving_transparent.webp` | The spider **carving** line-art, transparent bg | Investigator-supplied extraction |
| `trail-markers/trail-marker_nw-guitar-inscription_extracted.png` | The **`NW` + guitar** trail glyph, isolated | Investigator-supplied extraction |
| `trail-markers/trail-marker_w-five-poles-inscription_extracted.png` | The **`W` + five poles** trail glyph, isolated | Investigator-supplied extraction |
| `window-rock/window-rock_strange-statues-mural_extracted.png` | The **Window Rock "Strange Statues" mural**, hi-res isolated (for the [U14] black/red bird count) | Investigator-supplied extraction |

### Added 2026-06-13 — in-game map coordinate grids ([K26], investigator capture) · **firsthand, high-trust**
The in-game map grid [U26] was blocked on. Two *"A Partial and Correct Railroad and State Map of the United States"* prop
maps photographed at a **stranger's camp** (reportedly the camp near the *"Mysterious House"*/turtle house — the NPC who tells
of three brothers' hidden gold; **camp identity uncertain**). Each carries a printed lettered+numbered grid. Tested in
[`number_grid.py`](../experiments/number_grid.py): per-cell reading of the markings is **negative-leaning** (Map 2 admits only `EC`).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `maps/railroad-state-map_continental-grid_1-30x-a-u.jpg` | **Map 1 — continental US frame.** Grid: columns **1–30** (numbers, L→R) × rows **A–U** (letters, top→bottom), 30×21. Letter axis vertical (latitude-like) = same assignment as [K25] | Firsthand investigator screenshot (PS5), 2026-06-13 |
| `maps/railroad-state-map_regional-grid_a-ox-1-7.jpg` | **Map 2 — regional, grid drawn over the playable world** (W. Elizabeth/New Hanover/Lemoyne/Ambarino). Grid: columns **A–O** (letters, L→R) × rows **1–7** (numbers, bottom→top), 15×7; axes flipped vs Map 1. The node-plottable grid | Firsthand investigator screenshot (PS5), 2026-06-13 |

### Added 2026-06-13 — outhouse #4 roof (investigator capture) · **firsthand, high-trust for existence**
| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `butcher-creek/butcher-creek_outhouse4-roof-droppings.jpg` | **Outhouse #4 roof, from above (axe in hand):** two large droppings side by side, a gap, then one small dropping at the far edge above the doorframe — three in a line ([U28]). Most likely ambient scenery; logged as an oddity attached to the key outhouse #4 | Firsthand investigator screenshot (PS5), 2026-06-13 |

### Added 2026-06-13 — Saint Denis Vampire precedent ([K27]/[H15]/[H16], wiki CDN) · **B-tier (in-game = A)**
Pulled from the Red Dead Wiki CDN (`static.wikia.nocookie.net/reddeadredemption`) via the MediaWiki API for the file URLs
(the wiki page itself 403s). The egg is base-game and **documented in the in-game journal** — these are the reference set for
the [saint-denis-vampire.md](../analysis/saint-denis-vampire.md) dossier and source [#58](../sources/sources.md).

| File (current path) | Shows | Source file |
|------|-------|-----------|
| `saint-denis-vampire/saint-denis-vampire_locations-pentagram_map.jpg` | **Key image:** Saint Denis map with the **5 wall-writing locations (1–5)** + the **"V"** centre (the lair) — the points that connect into the pentagram | Vampire locations.jpg |
| `saint-denis-vampire/saint-denis-vampire_journal_wall-writings.jpg` | **The in-game journal pages:** the 5 wall-writings copied verbatim + Arthur's **location sketches**, and (far right) the **connecting-lines pentagram** sketch — shows the egg is journal-documented (contrast [K20]) | Vampire - Arthurs Journal.jpg |
| `saint-denis-vampire/saint-denis-vampire_journal-drawing_arthur.png` | **Arthur's** journal drawing of the vampire ("*You never know who you're going to meet down a dark alley*") — main-game era | Vampire-Arthur-RDR2-Journal.png |
| `saint-denis-vampire/saint-denis-vampire_journal-drawing_john.png` | **John's** journal drawing of the vampire — epilogue era; the two drawings together show the egg is doable in **both eras** | Vampire-John-RDR2-Journal.png |
| `saint-denis-vampire/saint-denis-vampire_portrait.jpg` | The Vampire (Nosferatu) himself — appearance based on Count Orlok (*Nosferatu*, 1922) | Nosferatu Vampire RDR2.jpg |
| `saint-denis-vampire/saint-denis-vampire_encounter_arthur.jpg` | The encounter — the Vampire confronts Arthur in the centre alley (12–1 AM) | Vampire-2.jpg |
| `saint-denis-vampire/saint-denis-vampire_ornate-dagger_reward.jpg` | The **Ornate Dagger** (missable reward looted from the Vampire) | Ornate Dagger handle.jpg |

## Still-wanted images (source from the web first)
Ordered by value. **Default to sourcing a clear, verifiable image from the wiki / community sites / the Strange Man video,
then verify it** — only fall back to firsthand in-game capture for detail that genuinely isn't documented anywhere online.

1. **The 8 webs + feathers** — per the [WEBS-MANIFEST](webs/WEBS-MANIFEST.md): each web at its hour with **feather colour
   and position/orientation** visible. *(Feather **orientation** is the one item with no known online source — the most
   likely capture-only task; try the Strange Man video frames first.)* **Update 2026-06-13:** all 8 **locations** are now
   covered by the labelled overlay maps above, and the `cablemesh` **datamine** shows feather positions *in the model* —
   but per-web in-game shots showing each feather's **in-world orientation** are still missing. **Partial 2026-06-13:** two
   feather-in-web captures sourced from Reddit (one black, one red — see provenance below), but **location-unconfirmed**, so
   the per-web orientation grid is still open. Both show the feather hanging **tip-down by gravity**, not pointing along a
   heading — a lead against the orientation-encodes-direction reading of [U0].
2. **The under-wood pole inscriptions** (verbatim) — most are screenshotted in community videos/threads; pull and verify.
3. ~~**`J+M` (Cornwall K&T) and `S+J` (Caliga Hall) matchstick sets**~~ ✅ **DONE 2026-06-13** — both sourced from
   r/reddeadmysteries via the Arctic Shift mirror and verified against the user's firsthand screenshots (see provenance
   above). **Still wanted:** the **arrow** set — community pins it to the **Old Trail Rise** basement (u/Jeralt & deleted
   posts; an imgur gallery `LrkkDcX` is referenced but unverified). Deprioritised (standard stash pointer, not an initial).
4. **Window Rock mural** — close enough to count each bird's **black vs red** feathers (for H3).
5. **Fort Brennand** three tower symbols + tally counts (6, 7), close up.

> **Re-examined 2026-06-13 (the heart motif IS a lead).** The datamined `…treeplaceholder2` texture reveals the Flatneck
> Station *"Lillie ♥ Alfred"* carving — itself a *separate* easter egg. **But** the same **heart-and-arrow shape recurs,
> empty, hidden on a [Bacchus Bridge](../locations/bacchus-bridge.md) leg, in line of sight of the bird carving** (investigator
> data → [K22]). So the **heart motif is now an active frontier lead** ([H10]/[U23]); the *Flatneck inscription itself*
> remains an unrelated egg. The datamine image is kept as the comparison reference (`bacchus-bridge/flatneck-station_heart-carving_datamine.png`).

> **Sourcing note:** fandom + GTAForums block automated download (403); use the wiki **CDN** + **API**, community sites, or
> video frames. A **web-sourced image, verified against a second source**, is preferred and usually sufficient — reserve
> in-game capture for the rare detail no online source records (e.g. feather orientation). Always log the source here.

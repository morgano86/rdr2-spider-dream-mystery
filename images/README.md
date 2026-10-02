# Images

Downloaded screenshots, maps, and diagrams, organized **by location/topic** so every image backs a specific claim.

## Naming convention (enforced)
Every image filename follows:

```
<subject>_<detail>[_<qualifier>].<ext>
```

- **All lowercase, ASCII.** Extension reflects the true format (`.webp` / `.png` / `.jpg`).
- **Fields are separated by `_`; words *within* a field use `-`.** So `_` splits the meaning into parts, `-` keeps a multi-word part readable: `fort-wallace_bird-symbols_tower.webp` → subject `fort-wallace`, detail `bird-symbols`, qualifier `tower`.
- **`<subject>`** = the place or thing the image is *about* (kebab slug), e.g. `butcher-creek`, `fort-brennand`, `vetters-echo`, `window-rock`, `the-giant`, `dreamcatcher`. This is the subject, **not necessarily the folder** — e.g. the Fort Brennand shot lives in `butcher-creek/` (thematic grouping) but is named `fort-brennand_…`.
- **`<detail>`** = what it shows (kebab): `floorboard-pentagram`, `tower-symbols`, `journal-drawing`.
- **`<qualifier>`** *(optional)* = disambiguator: a time (`1-2am`), a web code (`b34`), or a view index (`view1`, `view2`).
- **Webs** are a documented sub-pattern: `web_<location>_<code>[_<detail>].webp` (code = colour+hour, e.g. `b34`, `r34`). The centre cluster has no code: `web_centre_n-pole_1-2am.webp`. See [`webs/WEBS-MANIFEST.md`](webs/WEBS-MANIFEST.md).

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
- `gertrude/` — the Gertrude Braithwaite numbers thread ([U6], [thread 04](../threads/04-gertrude-numbers.md)): the StrangeMan-video frames (incl. the **9-sequence tail transcription**) + the [#43] exposé's evidence images.
- `wapiti-giant/` — the Giant's cave + map location (NW cold-frontier lead).
- `register-rock/` — the Heartlands names-and-dates boulder ("S. Gray 1846") possibly named by the Fort Brennand 3rd symbol ([H11]).
- `bacchus-bridge/` — the Cumberland Forest truss bridge with the hidden **empty heart** ([K22]) + the Flatneck heart datamine reference.
- `maps/` — base-map crops, our own built overlays (labelled pole/web positions), and the **in-game prop-map coordinate grids** ([K26]) — the two *"Railroad & State Map"* maps photographed at a stranger's camp.
- `francis-sinclair/` — the **Geology for Beginners cabin mural** ([K32]/[U31]) — the *separate* time-traveller egg (not verified-linked to the spider mystery; see [thread 08](../threads/08-francis-sinclair-mural.md)).
- `mount-shann/` — the **Mount Shann "giant sundial"** ([K35]–[K37]) — a *separate* Kuhkowaba-cult / UFO egg (crossover only via GTA V Chiliad; see [thread 09](../threads/09-mount-shann-sundial.md)). Ground + overhead in-game shots and the CodeX `dis_bgv_sundial.ydr` model extraction showing the 7 red/orange/yellow arrows.

## Provenance log
The wiki images below (16 pulled; one — `web_saint-denis_r34.webp`, wiki file `SpiderWebPole.png` — removed 2026-07-04 as superseded by the sharper [#59] front shot in `webs/feather-positions/`) were fetched **2026-06-13** from the Red Dead Wiki via its CDN (`static.wikia.nocookie.net/reddeadredemption`); the wiki web/page routes are Cloudflare-blocked but the MediaWiki API + CDN are not. Fandom files are **WebP**. Always log the **source URL/wiki file** for anything added — a sourced+verified web image is preferred over an in-game capture (see sourcing note).

| File (current path) | Shows | Source file |
|------|-------|-----------|
| `butcher-creek/butcher-creek_floorboard-pentagram.webp` | The glowing Butcher Creek floorboard pentagram (start point) | Butcher_Creek_Pentagram.PNG |
| `butcher-creek/butcher-creek_outhouse-tally-pentagram.webp` | Outhouse tally numbers that form a pentagram when connected in order | ButcherCreekOuthouses.PNG |
| `butcher-creek/butcher-creek_outhouse4-lj-sm-carving.webp` | **Outhouse #4: `LJ` + `SM` + Fort Brennand symbol** (verified by eye) | FortandLetters.PNG |
| `butcher-creek/fort-brennand_tower-symbols.webp` | Fort Brennand tally marks + telephone-pole/factory/oil-puddle symbols | FortBren.PNG |
| `webs/web_cornwall_b34_engraving.webp` | Spider engraving on the pole by Cornwall Kerosene & Tar (trail start) | SpiderEngraving.PNG |
| `webs/web_map-overlay_all-locations.webp` | The engraving as a map showing other web locations / pole directions | SpiderWebLocations.png |
| `webs/web_centre_n-pole_1-2am.webp` | Centre webs lined up to reveal the `N` + telephone pole (1–2am, no feather) | CenterWeb.PNG |
| `trail-markers/trail-marker_w-five-poles-inscription.webp` | Pole inscription `W ✞✞✞✞✞` (= 5 poles west) | TelephonePoles.png |
| `trail-markers/trail-marker_nw-guitar-inscription.webp` | The guitar pole (`NW` + guitar) revealed after many shots | GuitarPole.png |
| `trail-markers/trail-marker_guitar-pole_location.webp` | Guitar-pole location; NW leads toward Fort Wallace (waypoint) | GuitarPoleLocation.PNG |
| `fort-wallace/fort-wallace_bird-symbols_tower.webp` | The disputed "w"/bird symbols above the Fort Wallace guitar | FortWallaceSymbols.PNG |
| `fort-wallace/fort-wallace_questionmark_view1.webp` | Alleged off-map "question mark" shape (pareidolia?) | Questionmark1.PNG |
| `fort-wallace/fort-wallace_questionmark_view2.webp` | Second "question mark" view | Questionmark2.PNG |
| `window-rock/window-rock_strange-statues-mural.webp` | Window Rock "Strange Statues" mural. **The COLOUR-FAITHFUL source** (verified 2026-06-21: byte-for-byte colour-identical to the live wiki CDN original). ⚠️ The mural is a **single red/ochre pigment** — there is no black/red split ([U14] negative) | StrangeStatuesMural.PNG |
| `window-rock/window-rock_strange-statues-poi.png` | Strange Statues painting — point-of-interest crop | (community POI crop) |
| `matchsticks/vetters-echo_matchstick-ec_black-widow.webp` | **Matches spelling `EC` beside the Black Widow card** @ Vetter's Echo (verified) | Ecspider.PNG |
| `dreamcatchers/dreamcatcher_journal-drawing.webp` | **Journal drawing connecting all 20 dreamcatcher points into an animal** (eye = Elysian Pool) | Dreamcatcher drawing Arthur Morgan rdr2.png |
| `dreamcatchers/dreamcatcher_in-tree.webp` | A single dreamcatcher hung in a tree (the collectible itself) | Rdr2_dreamcatcher.jpg |
| `wapiti-giant/the-giant_map-location.jpg` | The Giant's cave — map location (Grizzlies East) | (wiki map) |
| `wapiti-giant/the-giant_cave-home.jpg` | The Giant's cave interior / home | (wiki) |

### Added 2026-06-13 — community Google Site (Timeline & Facts pages, [source #36](../sources/sources.md)) · **C-tier, verify**
Pulled from `lh3.googleusercontent.com` (the site is JS-rendered; image URLs were extracted from the raw page HTML, not the rendered DOM). Community-made overlays/datamines — credits are visible on the images (Jay_0048, thecochiti). Treat as leads corroborated against the manifest, **not** primary.

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_map-overlay_all-labeled.jpg` | **Best all-webs reference map** — every web labelled by name + code + hour (Cornwall/B34 3–4 … Saint Denis/R34 3–4), plus Centre Web (1–2), the W-5-poles pole, and the NW Guitar Pole | Google Site Timeline |
| `webs/web_map-overlay_nw-trail.jpg` | Spider-shape overlay with the **trail drawn NW past the guitar pole to a "?"** — the cold frontier ([thread 06](../threads/06-bird-carving-giant-wapiti.md)) | Google Site Timeline |
| `webs/web_cable-mesh_datamine.png` | **Datamined web wireframe** — the four `cablemesh*` models (`87399_thvy001`, `87405_hvlit001`, `87397_thvy001`, `87455_hvlit001`); yellow = feather positions in the mesh. Corroborates the shared GTA V/RDR2 cable-shader build. ⚠️ **2026-09-01: those four names read out of the archetype table as the CENTRE cluster at hour 1** ([K51]/[#89]) — so this may depict the *centre* web, not the 8 outer webs' shared geometry, and the "feather positions" annotation would be the author's inference (the centre is featherless). See [U40]. | Google Site (credit **thecochiti**) |
| `webs/web_cornwall_b34_pole-carving.jpg` | The Cornwall **spider/"W" carving on the actual telegraph pole** in-world (daytime), railway behind — complements the engraving-as-map shot | Google Site Timeline |
| `fort-wallace/fort-wallace_two-guitars_map.png` | Fort Wallace's **two guitars** annotated — "Tower Guitar" vs "Out-in-the-open Guitar" (they point different ways) | Google Site Timeline |
| `fort-wallace/fort-wallace_bird-symbols_tower_view2.jpg` | **Clearer daytime view of the two moss "w"/bird symbols** on the tower-roof slats (cf. `fort-wallace_bird-symbols_tower.webp`) | Google Site Timeline |

### Added 2026-07-02 — the file-number datamine overlay ([U32] resolution, [source #65](../sources/sources.md)) · **C-tier**
| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_map-overlay_file-numbers_datamine.png` | **Every web labelled with its `spiderdream0X` internal file number** on the game map (956×662) — the public source of the WEBS-MANIFEST `File` column; matches it 8/8 → [K39] | u/**Artem_ab6**, r/reddeadmysteries master-thread comment `nx6movu` (2026-01-02); downloaded from `i.redd.it/9z2xp03uduag1.png` via Arctic Shift |

### Added 2026-07-02 (Reddit sweep) — the PUBLIC despawn-zones map ([source #69](../sources/sources.md)) · **C-tier**
| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_map-overlay_despawn-zones_jay0048.jpg` | **The three feather despawn boundaries drawn on the game map** (3205×2855, "Jay_0048" watermark) — orange `B34` (Valentine↔Elysian Pool), yellow Connector `B56,B23,B45,B56L`, red South `R23,R45,R34` (to Saint Denis), overlaps visible; also colour-codes the non-respawn chain ([K13b](../INDEX.md)/[H4](../INDEX.md)). The **public provenance** of the boundary mapping ([K21]/[K28]/[H9]/[K31] context) | u/**Jay_0048**, r/reddeadmysteries post `1qe720q` "Feather's despawn zones" (2026-01-16, 122 pts); downloaded from `i.redd.it/mphbb45y9ndg1.jpeg` via Arctic Shift |

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
Reddit's HTML/JSON front door **403-blocks** our fetcher (UA-agnostic — it's an egress-IP block), but the **Arctic Shift** community data mirror (`arctic-shift.photon-reddit.com/api`) is **not** blocked and returns post metadata + image URLs; the `i.redd.it` image CDN is **also reachable**. Pulled the two missing letter sets from r/reddeadmysteries and **verified each against the user's own firsthand in-game screenshot** (2026-06-13) — same letters, same props, same pinned location. See the recipe in [`sources/RESOURCES.md`](../sources/RESOURCES.md#access-cookbook-the-fetch-recipes-that-actually-work).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `matchsticks/cornwall-kerosene-tar_matchstick-jm.png` | **Matches spelling `J + M`** on a table at **Cornwall Kerosene & Tar** (the web-trail START site), beside a *Diablo's Matches* box, a **William Sletcher "Weight Lifter"** cigarette card and a **Maude Engel** photo. Confirms [K9] `J+M`@Cornwall | Reddit r/reddeadmysteries, u/Jeralt ([post](https://reddit.com/r/reddeadmysteries/comments/chnaxq/)) → `i.redd.it/1fuypjvx5gc31.png`. **Verified vs investigator screenshot 2026-06-13.** |
| `matchsticks/caliga-hall_matchstick-sj.jpg` | **Matches spelling `S + J`** on a table at **Caliga Hall** (the Gray estate), with an ashtray of matches + a *Diablo's Matches* box; player holding a *Vistas of America* card. Confirms [K9] `S+J`@Caliga Hall | Reddit r/reddeadmysteries, u/KermitTheFraud92 ("on a table in caliga hall", [post](https://reddit.com/r/reddeadmysteries/comments/i75ax5/)) → `i.redd.it/zg1izs0cl6g51.jpg`. **Verified vs investigator screenshot 2026-06-13.** |

### Added 2026-06-13 — first feather-orientation captures (Reddit, via Arctic Shift mirror) · **C-tier, location unconfirmed**
From the r/reddeadmysteries **"Zoological"** post (u/Suspicious-Ad6283, ~2026-06). Its two in-world web shots (one black, one red feather; `web_black-feather_railway-pole_loc-unconfirmed.jpg` / `web_red-feather_railway-pole_loc-unconfirmed.jpg`, source URLs `i.redd.it/3842h740f56h1.jpg` / `nwz8dz70f56h1.jpg`) were the repo's **first** feather-in-web captures, but were **removed 2026-07-04** — fully superseded by the location-mapped all-8 [#59] set in [`webs/feather-positions/`](webs/feather-positions/README.md). The cardinal reference below is kept for [S15].

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/cardinal_female-in-flight_feather-reference.jpg` | In-game **female Northern Cardinal** in flight — brown body, **red-edged wing/tail feathers**. Reference for the cardinal-feather theory **[S15]** | Reddit r/reddeadmysteries, u/Suspicious-Ad6283 "Zoological" → `i.redd.it/u3mkoiwze56h1.jpg` |
| `butcher-creek/butcher-creek_pole-datamine-names.png` | Datamine map labelling the Butcher Creek props by **entity name** — `but_pignpole07x###` (telegraph poles), `but_01_magicstuff001` (ritual site). Corroborates the cable/telegraph asset-folder grouping ([K24]) | Reddit r/reddeadmysteries, u/fireflighTim "Decoding Butcher Creek" → `i.redd.it/p6wmolu2hcig1.png` |
| `butcher-creek/butcher-creek_outhouse-datamine-names_pentagram.png` | The 5 outhouses (`but_01 outhouse cliff 000–004`) connected into the pentagram — datamine entity names visible. Corroborates [K5] | Reddit r/reddeadmysteries, u/fireflighTim "Decoding Butcher Creek" → `i.redd.it/xnevsg55hcig1.png` |

### Added 2026-06-13 — ★ FULL feather-position set, all 8 webs ([U0]/[H4], Reddit via Arctic Shift) · **C-tier, high-value**
u/dropthepress's r/reddeadmysteries post **"High-quality spiderweb screenshots"** ([#59]) shot **every web front + side** — the first source to document feather position for all 8 (the repo's long-standing [#1 still-wanted](#still-wanted-images-source-from-the-web-first) item). **16 web shots + 1 location/colour map.** Saved under [`webs/feather-positions/`](webs/feather-positions/README.md) (full per-image index there). **Finding:** every feather **hangs tip-down by gravity** → **refutes [H4]**; only the per-web *attachment point* varies. *(Superseded the two loc-unconfirmed "Zoological" captures above, removed 2026-07-04.)*

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/feather-positions/web_<location>_<code>_<front\|side>.jpg` (16) | All 8 webs, **front** + **side**, **location-mapped** (names = real web per the post selftext, 2026-06-14); feather **tip-down** in every one. Per-image position table in the [folder README](webs/feather-positions/README.md). **⚠️ Files superseded 2026-07-04:** the 8 **fronts were replaced in place** by firsthand PS5 4K captures (section below) and the 8 **sides removed** (documented web placement, not feather position); all 16 [#59] originals remain in git history | Reddit r/reddeadmysteries, u/dropthepress "High-quality spiderweb screenshots" (`1qbhkjm`) → `i.redd.it` |
| `webs/web_map-overlay_locations-by-colour_dropthepress.png` | The 8 web locations on the map, **colour-coded by feather** (black/red legend) | same post |

### Added 2026-06-13 — extracted/transparent symbol assets (investigator-supplied) · **derived from in-game (A)**
Clean alpha-channel extractions of the key carved symbols, dropped via `TEMP_IMG` and filed to their subject folders. Useful for overlay/comparison work (e.g. matching the spider etching to a map, reading the guitar/W-poles glyphs).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_cornwall_b34_engraving_extracted.png` | The Cornwall **spider etching**, textured, isolated on transparent bg | Investigator-supplied extraction (in-game asset) |
| `webs/web_cornwall_b34_engraving_transparent.webp` | The spider **carving** line-art, transparent bg | Investigator-supplied extraction |
| `trail-markers/trail-marker_nw-guitar-inscription_extracted.png` | The **`NW` + guitar** trail glyph, isolated | Investigator-supplied extraction |
| `trail-markers/trail-marker_w-five-poles-inscription_extracted.png` | The **`W` + five poles** trail glyph, isolated | Investigator-supplied extraction |
| `window-rock/window-rock_strange-statues-mural_extracted.png` | The **Window Rock "Strange Statues" mural**, hi-res isolated. ⚠️ **Contrast-boosted / NOT colour-faithful** (reads ~half "black" — but its chromatic pixels are *also* 100% red): use the wiki `…mural.webp` for any colour question. Established 2026-06-21 via [`mural_colour_count.py`](../experiments/mural_colour_count.py) ([U14] negative) | Investigator-supplied extraction |

### Added 2026-06-13 — in-game map coordinate grids ([K26], investigator capture) · **firsthand, high-trust**
The in-game map grid [U26] was blocked on. Two *"A Partial and Correct Railroad and State Map of the United States"* prop maps photographed at a **stranger's camp** (reportedly the camp near the *"Mysterious House"*/turtle house — the NPC who tells of three brothers' hidden gold; **camp identity uncertain**). Each carries a printed lettered+numbered grid. Tested in [`number_grid.py`](../experiments/number_grid.py): per-cell reading of the markings is **negative-leaning** (Map 2 admits only `EC`).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `maps/railroad-state-map_continental-grid_1-30x-a-u.jpg` | **Map 1 — continental US frame.** Grid: columns **1–30** (numbers, L→R) × rows **A–U** (letters, top→bottom), 30×21. Letter axis vertical (latitude-like) = same assignment as [K25] | Firsthand investigator screenshot (PS5), 2026-06-13 |
| `maps/railroad-state-map_regional-grid_a-ox-1-7.jpg` | **Map 2 — regional, grid drawn over the playable world** (W. Elizabeth/New Hanover/Lemoyne/Ambarino). Grid: columns **A–O** (letters, L→R) × rows **1–7** (numbers, bottom→top), 15×7; axes flipped vs Map 1. The node-plottable grid | Firsthand investigator screenshot (PS5), 2026-06-13 |

### Added 2026-06-13 — outhouse #4 roof (investigator capture) · **firsthand, high-trust for existence**
| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `butcher-creek/butcher-creek_outhouse4-roof-droppings.jpg` | **Outhouse #4 roof, from above (axe in hand):** two large droppings side by side, a gap, then one small dropping at the far edge above the doorframe — three in a line ([U28]). Most likely ambient scenery; logged as an oddity attached to the key outhouse #4 | Firsthand investigator screenshot (PS5), 2026-06-13 |

### Added 2026-06-13 — Saint Denis Vampire precedent ([K27]/[H15]/[H16], wiki CDN) · **B-tier (in-game = A)**
Pulled from the Red Dead Wiki CDN (`static.wikia.nocookie.net/reddeadredemption`) via the MediaWiki API for the file URLs (the wiki page itself 403s). The egg is base-game and **documented in the in-game journal** — these are the reference set for the [saint-denis-vampire.md](../analysis/saint-denis-vampire.md) dossier and source [#58](../sources/sources.md).

| File (current path) | Shows | Source file |
|------|-------|-----------|
| `saint-denis-vampire/saint-denis-vampire_locations-pentagram_map.jpg` | **Key image:** Saint Denis map with the **5 wall-writing locations (1–5)** + the **"V"** centre (the lair) — the points that connect into the pentagram | Vampire locations.jpg |
| `saint-denis-vampire/saint-denis-vampire_journal_wall-writings.jpg` | **The in-game journal pages:** the 5 wall-writings copied verbatim + Arthur's **location sketches**, and (far right) the **connecting-lines pentagram** sketch — shows the egg is journal-documented (contrast [K20]) | Vampire - Arthurs Journal.jpg |
| `saint-denis-vampire/saint-denis-vampire_journal-drawing_arthur.png` | **Arthur's** journal drawing of the vampire ("*You never know who you're going to meet down a dark alley*") — main-game era | Vampire-Arthur-RDR2-Journal.png |
| `saint-denis-vampire/saint-denis-vampire_journal-drawing_john.png` | **John's** journal drawing of the vampire — epilogue era; the two drawings together show the egg is doable in **both eras** | Vampire-John-RDR2-Journal.png |
| `saint-denis-vampire/saint-denis-vampire_portrait.jpg` | The Vampire (Nosferatu) himself — appearance based on Count Orlok (*Nosferatu*, 1922) | Nosferatu Vampire RDR2.jpg |
| `saint-denis-vampire/saint-denis-vampire_encounter_arthur.jpg` | The encounter — the Vampire confronts Arthur in the centre alley (12–1 AM) | Vampire-2.jpg |
| `saint-denis-vampire/saint-denis-vampire_ornate-dagger_reward.jpg` | The **Ornate Dagger** (missable reward looted from the Vampire) | Ornate Dagger handle.jpg |

### Added 2026-06-21 — Francis Sinclair cabin mural ([K32]/[U31], user-supplied HQ) · **B-tier (in-game asset = A); separate egg**
The user's HQ photo of the mural, dropped into the repo because `i.imgur.com/fakkLOa.jpg` **geo-blocks our fetcher** (returns a "Content not viewable in your region" placeholder — see [memory: imgur-geoblocked-fetcher]). At 2822×2117 this is the real high-res capture. **Analysed firsthand 2026-06-21** for [U31] (composition logged in [thread 08](../threads/08-francis-sinclair-mural.md)).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `francis-sinclair/francis-sinclair_cabin-mural_hq.jpg` | **The full cabin mural** (2822×2117): central suited figure stepping through an **oval portal**, ringed by a large crowned/haloed sunburst head above; **skyscrapers + factories + UFO/zeppelin** to the left, **pyramids + Sphinx + pharaoh bust + horse-drawn carriage** to the right, **leaping/running figures** flanking the portal, lightning/radiant lines throughout — all surrounded by the **individual pinned rock-carving sketches** the player mailed in. Sepia line-art after Diego Rivera's *Man, Controller of the Universe* (1934) | User-supplied HQ photo (orig. `i.imgur.com/fakkLOa.jpg`, geo-blocked to fetcher), 2026-06-21 |

### Added 2026-07-02 — Mount Shann sundial ([K35]–[K37], user-supplied) · **firsthand + A-tier datamine; separate egg**
User-supplied captures + a datamined model extraction of the Mount Shann "giant sundial," dropped in at the user's request (2026-07-02) to open [thread 09](../threads/09-mount-shann-sundial.md). **Not the spider mystery** — a separate Kuhkowaba / UFO egg. The codex model is the key image: it confirms the 7 arrows are a **deliberate painted asset**.

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `mount-shann/mount-shann_sundial_ground-view.jpg` | The sundial from ground level (player + white horse), snow-covered stone ring, central upright; valley/river below | Firsthand investigator screenshot (photo-mode, 31/96, 25 mm), 2026-07-02 |
| `mount-shann/mount-shann_sundial_overhead.jpg` | Top-down of the ring — radial "spoke" stone layout around the centre; faint painted arrows (red/yellow specks visible) | Firsthand investigator screenshot (photo-mode, overhead), 2026-07-02 |
| `mount-shann/mount-shann_sundial-arrows_codex-model.jpg` | **Key reference:** CodeX (by dexyfex) extraction of model **`dis_bgv_sundial.ydr`** — the isolated rock cluster with all **7 painted arrows** legible **with the snow stripped off**: **3 orange · 3 red · 1 yellow**. The arrows exist in-game (firsthand); this just shows their count/colour clearly ([K36]) | User-supplied datamine (CodeX screenshot), 2026-07-02 |

### Added 2026-07-04 — all-webs feather diagram (user upload)

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_diagram_feather-positions_vector.jpeg` | Vector diagram of **all 8 webs** labelled hour+colour with each feather at its socket. Socket positions match the [#59] reads **8/8** — likely derived from that set, so treat as **illustration, not independent evidence**. ⚠️ Known inaccuracy: draws the red feathers single, but in-game **all 8 feathers are doubled** ([K40]) | **Community-made, user-supplied 2026-07-04** — user recalls finding it on **Reddit** (exact post unpinned; C-tier) |

### Replaced 2026-07-04 — feather-position fronts re-shot firsthand (PS5 photo mode, 4K) · **firsthand, high-trust**
The investigator re-shot **all 8 web fronts** on PS5 (photo mode, 3840×2160) and they were swapped in **file-for-file under the existing names** in [`webs/feather-positions/`](webs/feather-positions/README.md) — so every cross-link kept resolving, while the image tier for feather position rose from **C ([#59] Reddit uploads) to firsthand investigator data**. Each capture's background independently confirms its location (Emerald's station platform, Saint Denis' lit factory row, Ringneck's truss bridge, Scarlett's farm + water tower). **All 8 socket reads re-verified at 4K — 8/8 unchanged, all now high-confidence** (Scarlett's old C-vs-R ambiguity resolves to a clear `R`); the doubling ([K40]) is unambiguous on the four twinned blacks, hidden on the reds/BL56 from these angles (consistent with the [K40] front-angle caveat).

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/feather-positions/web_<location>_<code>_front.jpg` (8) | All 8 webs, front view, feather + socket clearly legible at 4K. ⚠️ `web_scarlett_r23_front.jpg` and `web_southfield_r45_front.jpg` carry a small photo-mode HUD overlay top-right (cosmetic) | Firsthand investigator screenshots (PS5 photo mode, 3840×2160), 2026-07-04 |

### Added 2026-07-04 — Gertrude numbers: hoax-exposé evidence set ([#43], via the Fandom Discussions API) · **C-tier**
The [#43] exposé post's embedded images, recovered 2026-07-04 through the **Fandom Discussions API** (the `/f/` page 403s; recipe in [RESOURCES.md](../sources/RESOURCES.md)) from `static.wikia.nocookie.net` UUID URLs. Three are **frames from StrangeMan's video itself** (reposted by the exposé author) — i.e. the alleged-hoax video's claims preserved verbatim.

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `gertrude/gertrude_numbers-transcription_strangeman-frame.jpg` | **Key image — the fullest tail transcription on record:** 9 number sequences overlaid on the outhouse shot, `1 2 3 4 5` highlighted red in two, caption *"she only manages to count up to five"*. Both hoaxer and [#43] debunker accept these numbers (the debunker's 17/4/29 stats match) → [U6]/[S42] | StrangeMan video frame, embedded in [#43] (u/KidColt.45, 2025-12-17) |
| `gertrude/gertrude_butcher-creek-claim_strangeman-frame.jpg` | The video's central claim verbatim: map marker on Butcher Creek + *"THE SOLUTION TO THIS SECRET IS ALL THE WAY IN BUTCHER CREEK"* | StrangeMan video frame, embedded in [#43] |
| `gertrude/gertrude_doyles-tavern-photo_strangeman-claim.jpg` | The framed "healthy Gertrude" photo at Doyle's Tavern the video presents — per [#43], a **reused generic PED model**, contradicted by the Braithwaite Manor family photo (young Gertrude already malformed) | StrangeMan video claim, embedded in [#43] |
| `gertrude/gertrude_outhouse-line_van-horn-map.jpg` | The exposé's own counter-alignment overlay: the outhouse's line drawn from Braithwaite Manor **NE to Van Horn / Copperhead Landing** — *not* Butcher Creek | [#43] author's map (u/KidColt.45) |

## Still-wanted images (source from the web first)
Ordered by value. **Default to sourcing a clear, verifiable image from the wiki / community sites / the Strange Man video, then verify it** — only fall back to firsthand in-game capture for detail that genuinely isn't documented anywhere online.

1. **The 8 webs + feathers** — per the [WEBS-MANIFEST](webs/WEBS-MANIFEST.md): each web at its hour with **feather colour and position/orientation** visible. *(Feather **orientation** is the one item with no known online source — the most likely capture-only task; try the Strange Man video frames first.)* **Update 2026-06-13:** all 8 **locations** are now covered by the labelled overlay maps above, and the `cablemesh` **datamine** shows feather positions *in the model* — but per-web in-game shots showing each feather's **in-world orientation** are still missing. **Partial 2026-06-13:** two feather-in-web captures sourced from Reddit (one black, one red — see provenance below), but **location-unconfirmed**, so the per-web orientation grid is still open. Both show the feather hanging **tip-down by gravity**, not pointing along a heading — a lead against the orientation-encodes-direction reading of [U0].
2. **The under-wood pole inscriptions** (verbatim) — most are screenshotted in community videos/threads; pull and verify.
3. ~~**`J+M` (Cornwall K&T) and `S+J` (Caliga Hall) matchstick sets**~~ ✅ **DONE 2026-06-13** — both sourced from r/reddeadmysteries via the Arctic Shift mirror and verified against the user's firsthand screenshots (see provenance above). **Still wanted:** the **arrow** set — community pins it to the **Old Trail Rise** basement (u/Jeralt & deleted posts; an imgur gallery `LrkkDcX` is referenced but unverified). Deprioritised (standard stash pointer, not an initial).
4. ~~**Window Rock mural** — close enough to count each bird's **black vs red** feathers (for H3).~~ ✅ **DONE 2026-06-21 (NEGATIVE):** the colour-faithful wiki texture is conclusive without a closer shot — the mural is a **single red pigment** (no black/red split; [U14]/[H3] refuted via [`mural_colour_count.py`](../experiments/mural_colour_count.py)).
5. **Fort Brennand** three tower symbols + tally counts (6, 7), close up.

> **Re-examined 2026-06-13 (the heart motif IS a lead).** The datamined `…treeplaceholder2` texture reveals the Flatneck Station *"Lillie ♥ Alfred"* carving — itself a *separate* easter egg. **But** the same **heart-and-arrow shape recurs, empty, hidden on a [Bacchus Bridge](../locations/bacchus-bridge.md) leg, in line of sight of the bird carving** (investigator data → [K22]). So the **heart motif is now an active frontier lead** ([H10]/[U23]); the *Flatneck inscription itself* remains an unrelated egg. The datamine image is kept as the comparison reference (`bacchus-bridge/flatneck-station_heart-carving_datamine.png`).

> **Sourcing note:** fandom + GTAForums block automated download (403); use the wiki **CDN** + **API**, community sites, or video frames. A **web-sourced image, verified against a second source**, is preferred and usually sufficient — reserve in-game capture for the rare detail no online source records (e.g. feather orientation). Always log the source here.

### Added 2026-09-01 — CodeX ymap-extent renders (source [#89])

Four plots generated **from the shipped game files** by the investigator's CodeX diagnostic harness (matplotlib renders, not screenshots): the 3 boundary-group `.ymap` extent boxes drawn against the 8 feather positions. They are the visual evidence for [K48]/[K49] and the deflation of [S36]/[S22] — see [H28](../findings/speculation.md) and the [WEBS-MANIFEST](webs/WEBS-MANIFEST.md) file-data banner.

| File (current path) | Shows | Source / credit |
|------|-------|-----------|
| `webs/web_ymap-extents_boundary-groups.png` | **First render (2026-07-23)** — the three **parent** `*_rds_props` ymaps' `entitiesExtents` (solid fill) + `streamingExtents` (dashed) vs all 8 feather positions, colour-coded black/red and labelled with code + file number + location. The plot that prompted the investigator's "no triple overlap" correction to [K28] | Investigator / CodeX file read, 2026-07-23 ([#89]) |
| `webs/web_ymap-extents_strm0-annotated.png` | **The load-bearing one (2026-07-25)** — same view built from the `*_strm_0` **child** ymaps (the ones that actually stream), with each group's exact `stream`/`ents` X·Y numbers printed, and the derivation footnote: **max 6 feathers displaceable at once**; `B34` 50 m west / `R34` 638 m east of Group 2's box; **G1 and G3 disjoint by 10.5 m** ⟹ `B34` and any red can never be loaded together ([K49]) | Investigator / CodeX file read, 2026-07-25 ([#89]) |
| `webs/web_ymap-extents_strm0-clean.png` | The same `*_strm_0` plot **without** the numeric callouts or footnote (2026-07-26) — the legible version for quick reference | Investigator / CodeX file read, 2026-07-26 ([#89]) |
| `webs/web_ymap-extents_g1-g3-gap.png` | **Zoom on the gap (2026-07-26)** — G1 bottom edge `Y = −277.81`, G3 top edge `Y = −288.31`, the **10.50 m band covered by neither**, with G2 spanning straight through it. The image that kills the [K28] triple-overlap (and with it the whiskey tree's "only POI in the triple overlap" role) | Investigator / CodeX file read, 2026-07-26 ([#89]) |

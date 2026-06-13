# Research resources — where to look for what

A curated directory of the **recurring resources** this investigation draws on, and **what each is genuinely useful for**.
This is the "where do I go for X?" map; it is **not** the citation ledger. For a specific numbered citation tied to a claim,
see [`sources.md`](sources.md). When you find a resource you'll use again, add it here with a one-line "useful for."

> Reliability legend (same as [`sources.md`](sources.md)): **A** = primary / in-game / official · **B** = established
> games journalism or a long-standing wiki · **C** = forum / social / video — useful *leads*, verify before trusting.

---

## Quick pick — by what you need

| If you need… | Go to | Tier |
|--------------|-------|------|
| **Verbatim in-game text** (carvings, signs, letters, documents, journal sketches, POI inscriptions) | **reddeadreference (Tumblr)** → then verify against an image | B/C |
| **Location / POI / character facts, names lists, trivia** | **Red Dead Wiki** (via MediaWiki API) | B |
| **The 2025 spider-web pole trail** (poles, headings, feathers, frame-pulling orientation) | **Strange Man (YouTube)** | C |
| **Community theories & long-form debate** (Gertrude's numbers, Butcher Creek) | **GTAForums**, **r/reddeadmysteries** | C |
| **In-world props / discovery photos the wiki ignores** (matchstick sets, odd carvings, "found this" posts) | **r/reddeadmysteries via Arctic Shift** (recipe below) | C |
| **Datamines, overlay maps, web boundaries/chain** | **Community Google Site** (Jay_0048 / thecochiti) | C |
| **Payoff status, dev reactions, news framing** | **Games journalism** (Dexerto, GameRant, Kotaku, Popverse…) | B |
| **Exhaustive collectible / POI location lists** | **PowerPyx, GamerGuides, Steam guides** | B/C |
| **Downloadable images** | **Wikia CDN** + the MediaWiki imageinfo recipe (below) | A/B |

---

## The resources

### Primary in-game text
- **reddeadreference (Tumblr)** — https://reddeadreference.tumblr.com/ · **B/C**
  A blog that transcribes the game's **written world** photo-by-photo: rock/wall carvings, shop & street signs, letters,
  newspapers, journal sketches, POI inscriptions. **Best resource for the exact wording of anything carved or written**, and it
  posts the source screenshots (often with RDR2 EXIF) so you can verify. Used for the full [Register Rock](../locations/register-rock.md)
  carving list ([src #39](sources.md)). *Caveat:* a fan transcription — corroborate against the image or a second source before
  promoting to `[KNOWN]`.

### Reference wikis
- **Red Dead Wiki (Fandom)** — https://reddead.fandom.com/ · **B**
  The backbone for **location dossiers, character bios, names lists, POI details, trivia**. *Access gotcha:* the page route
  **403s automated fetch** — use the **MediaWiki API** (recipes below), not WebFetch on the article URL. Images come from the CDN.
- **Fextralife RDR2 wiki** — https://reddeadredemption2.wiki.fextralife.com/ · **B** — secondary cross-check when Fandom is thin.

### The spider-trail documenters (video)
- **Strange Man (YouTube)** — search: https://www.youtube.com/results?search_query=strange+man+rdr2+spider+web+mystery · **C**
  The lead documenter of the **2025 telegraph-pole web trail**. Best (often only) source for the pole headings (N → W×5 → NW +
  guitar), and the most promising place to **frame-pull feather orientation** ([U0]). *To do:* pin the canonical video URLs
  ([gap](#gaps--still-wanted)).
- Topic-specific videos are catalogued in [`sources.md`](sources.md) (#16–19) — Gertrude's numbers, outhouse carvings.

### Community theory / discovery
- **GTAForums** — https://gtaforums.com/ · **C** — long-running threads (Butcher Creek numbers, Braithwaite code). *Gotcha:*
  **403s automated fetch** — browse manually and paste verbatim excerpts, citing the source number.
- **Reddit r/reddeadmysteries** — https://www.reddit.com/r/reddeadmysteries/ · **C** — community discovery/discussion, and the
  **best source for in-world props the wiki ignores** (e.g. the `J+M`/`S+J`/arrow matchstick sets — [src #48–50](sources.md)).
  *Gotcha:* Reddit's own site + `.json` API **403-block** our fetcher (egress-IP block, UA tricks don't help) — use the **Arctic
  Shift** mirror instead (recipe below). *To do:* locate a spider-mystery master thread ([gap](#gaps--still-wanted)).
- **Community Google Site — "Spider Dreams Mystery"** — https://sites.google.com/view/spider-dreams-mystery/timeline · **C**
  A community tracker with **overlay maps, the web boundary/shooting-chain diagrams, and datamines** (credits visible on the
  images: **Jay_0048**, **thecochiti**). Source of several `webs/` images. *Gotcha:* JS-rendered — extract image URLs from the
  **raw page HTML**, not the rendered DOM. Treat as leads; verify against the [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md).

### Games journalism (overviews, news, dev quotes)
- **Dexerto, GameRant, Kotaku, Popverse, GamesRadar, RDR2.org, GamingBolt, PCGamesN** · **B**
  Best for **the big-picture chain, the "is there a payoff?" status, and the ex-dev (Butterworth) reaction**. Individually
  cited in [`sources.md`](sources.md) #6–13, #21–35. Dexerto #6 and GamingBolt #27 are the strongest single overviews.

### Guides / collectible & location lists
- **PowerPyx** — https://www.powerpyx.com/ · **GamerGuides** — https://www.gamerguides.com/ · **Steam community guides** · **B/C**
  Exhaustive **collectible and POI location lists** (rock carvings, points of interest, etc.). Useful for disambiguation — e.g.
  confirming Register Rock is a **POI**, distinct from the 10 *Rock Carvings* collectibles.

---

## Access cookbook (the fetch recipes that actually work)

Fandom and GTAForums **block automated fetch (HTTP 403)**. These are the workarounds we use:

- **Fandom article text (wikitext):**
  `https://reddead.fandom.com/api.php?action=parse&page=PAGE_TITLE&format=json&prop=wikitext`
  (add `|text|images` to `prop` for rendered HTML + the gallery image filename list).
- **Fandom image direct URLs** (then download from the CDN):
  `https://reddead.fandom.com/api.php?action=query&titles=File:NAME.png&prop=imageinfo&iiprop=url&format=json`
  — titles can be `|`-separated to batch several files in one call.
- **Download from the Wikia CDN** (`static.wikia.nocookie.net/...`): `curl.exe -L -A "Mozilla/5.0" -o out.webp "<url>"`.
  Fandom serves **WebP** regardless of the `.png` filename — name the saved file `.webp`.
- **Tumblr images** (`64.media.tumblr.com/...`): same `curl`, but add a **referer** so the CDN serves it:
  `curl.exe -L -A "Mozilla/5.0" -e "https://reddeadreference.tumblr.com/" -o out.jpg "<url>"`.
- **GTAForums / any 403 page with no API:** browse manually, paste **verbatim** excerpts into the relevant thread file, cite the
  source number in [`sources.md`](sources.md).
- **Reddit (403-blocks our fetcher — site, old.reddit, and `.json` alike; it's an egress-IP block, so UA spoofing won't help):**
  use the **Arctic Shift** community mirror, which is *not* blocked. Search a sub, then download the `i.redd.it` image (the CDN
  is reachable). Worked first try 2026-06-13 to grab the matchstick sets:
  - Search: `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=SUB&query=QUERY&limit=25`
    (omit `subreddit` for a site-wide search → **400**; a subreddit is required). Each result's `url` field is the image link.
  - Full post detail (selftext, gallery `media_metadata`): `https://arctic-shift.photon-reddit.com/api/posts/ids?ids=ID1,ID2`.
  - Download the image: stdlib `urllib` with a browser `User-Agent` from `i.redd.it/<hash>.<ext>` (PNG/JPG come through fine).
  - **Always corroborate** — Reddit is C-tier; here each image was verified against the user's firsthand in-game screenshot.

> Always record provenance: a web image goes in [`images/README.md`](../images/README.md) with its source; a claim cites a
> numbered row in [`sources.md`](sources.md).

---

## Gaps — still wanted
- **Canonical Strange Man video URL(s)** — the originating documentation of the 2025 trail (currently only a search link).
- **A Reddit r/reddeadmysteries master thread** for the spider mystery.
- **Rockstar credits / artbook scans** — only if the `LJ`/`SM` dev-initial question ever needs settling.

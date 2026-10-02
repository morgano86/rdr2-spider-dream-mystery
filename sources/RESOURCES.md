# Research resources — where to look for what

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

A curated directory of the **recurring resources** this investigation draws on, and **what each is genuinely useful for**. This is the "where do I go for X?" map; it is **not** the citation ledger. For a specific numbered citation tied to a claim, see [`sources.md`](sources.md). When you find a resource you'll use again, add it here with a one-line "useful for."

> Reliability legend (same as [`sources.md`](sources.md)): **A** = primary / in-game / official · **B** = established games journalism or a long-standing wiki · **C** = forum / social / video — useful *leads*, verify before trusting.

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
- **reddeadreference (Tumblr)** — https://reddeadreference.tumblr.com/ · **B/C** A blog that transcribes the game's **written world** photo-by-photo: rock/wall carvings, shop & street signs, letters, newspapers, journal sketches, POI inscriptions. **Best resource for the exact wording of anything carved or written**, and it posts the source screenshots (often with RDR2 EXIF) so you can verify. Used for the full [Register Rock](../locations/register-rock.md) carving list ([src #39](sources.md)). *Caveat:* a fan transcription — corroborate against the image or a second source before promoting to `[KNOWN]`.

### Reference wikis
- **Red Dead Wiki (Fandom)** — https://reddead.fandom.com/ · **B** The backbone for **location dossiers, character bios, names lists, POI details, trivia**. *Access gotcha:* the page route **403s automated fetch** — use the **MediaWiki API** (recipes below), not WebFetch on the article URL. Images come from the CDN.
- **Fextralife RDR2 wiki** — https://reddeadredemption2.wiki.fextralife.com/ · **B** — secondary cross-check when Fandom is thin.

### The spider-trail documenters (video)
- **Strange Man (YouTube)** — https://www.youtube.com/@StrangeManChannel (`UCmQyHj6O6US8Jgj1WrXWZYg`) · **C** The lead documenter of the **2025 telegraph-pole web trail**. Best (often only) source for the pole headings (N → W×5 → NW + guitar). ✅ **Canonical spider-series URLs pinned 2026-07-05 → [source #80](sources.md)** (7 dated videos, 2025-12-23 → 2026-01-14; the 12-23 explainer `OSQPMaU7yz8` is the originating documentation). **Two standing cautions:** (1) the channel's **2026-04-01 "I Finally Solved…" video is an April Fools joke** (`F5ugykizAU0`) — never cite it; (2) the channel is also the author of the **hoax-rated Gertrude videos** ([#17]/[#18] — the [#43] exposé target), so treat its *interpretive* claims as C-tier theory even where its *documentation* footage is the best available.
- Topic-specific videos are catalogued in [`sources.md`](sources.md) (#16–19) — Gertrude's numbers, outhouse carvings.

### Community theory / discovery
- **GTAForums** — https://gtaforums.com/ · **C** — long-running threads (Butcher Creek numbers, Braithwaite code). *Gotcha:* **403s automated fetch** — browse manually and paste verbatim excerpts, citing the source number.
- **Reddit r/reddeadmysteries** — https://www.reddit.com/r/reddeadmysteries/ · **C** — community discovery/discussion, and the **best source for in-world props the wiki ignores** (e.g. the `J+M`/`S+J`/arrow matchstick sets — [src #48–50](sources.md)). *Gotcha:* Reddit's own site + `.json` API **403-block** our fetcher (egress-IP block, UA tricks don't help) — use the **Arctic Shift** mirror instead (recipe below). ✅ **The spider-mystery MASTER THREAD is pinned:** *"The Evergrowing Spiderweb Theories"* (`1pzutww`, mod consolidation post, ~1,989 comments — [src #64](sources.md)); fetch its full comment tree with `api/comments/tree?link_id=1pzutww` (the `comments/search?link_id=` route returns empty — use **tree**). It carries the Iittlebird timeline (= the Google Site author), the Artem_ab6 file-number datamine ([#65]), and the slaytanic_666 hashes ([#66]).
- **Community Google Site — "Spider Dreams Mystery"** — https://sites.google.com/view/spider-dreams-mystery/timeline · **C** A community tracker with **overlay maps, the web boundary/shooting-chain diagrams, and datamines** (credits visible on the images: **Jay_0048**, **thecochiti**). Source of several `webs/` images. *Gotcha:* JS-rendered — extract image URLs from the **raw page HTML**, not the rendered DOM. Treat as leads; verify against the [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md).

### Games journalism (overviews, news, dev quotes)
- **Dexerto, GameRant, Kotaku, Popverse, GamesRadar, RDR2.org, GamingBolt, PCGamesN** · **B** Best for **the big-picture chain, the "is there a payoff?" status, and the ex-dev (Butterworth) reaction**. Individually cited in [`sources.md`](sources.md) #6–13, #21–35. Dexerto #6 and GamingBolt #27 are the strongest single overviews.

### Guides / collectible & location lists
- **PowerPyx** — https://www.powerpyx.com/ · **GamerGuides** — https://www.gamerguides.com/ · **Steam community guides** · **B/C** Exhaustive **collectible and POI location lists** (rock carvings, points of interest, etc.). Useful for disambiguation — e.g. confirming Register Rock is a **POI**, distinct from the 10 *Rock Carvings* collectibles.

---

## Access cookbook (the fetch recipes that actually work)

Fandom and GTAForums **block automated fetch (HTTP 403)**. These are the workarounds we use:

- **Fandom article text (wikitext):** `https://reddead.fandom.com/api.php?action=parse&page=PAGE_TITLE&format=json&prop=wikitext` (add `|text|images` to `prop` for rendered HTML + the gallery image filename list).
- **Fandom image direct URLs** (then download from the CDN): `https://reddead.fandom.com/api.php?action=query&titles=File:NAME.png&prop=imageinfo&iiprop=url&format=json` — titles can be `|`-separated to batch several files in one call.
- **Download from the Wikia CDN** (`static.wikia.nocookie.net/...`): `curl.exe -L -A "Mozilla/5.0" -o out.webp "<url>"`. Fandom serves **WebP** regardless of the `.png` filename — name the saved file `.webp`.
- **Tumblr images** (`64.media.tumblr.com/...`): same `curl`, but add a **referer** so the CDN serves it: `curl.exe -L -A "Mozilla/5.0" -e "https://reddeadreference.tumblr.com/" -o out.jpg "<url>"`.
- **🆕 Fandom Discussions / forum posts (`fandom.com/f/p/<id>` — 403s + JS-rendered) — the Discussions API works (found 2026-07-04, used to fully capture [#43]):** `https://reddead.fandom.com/wikia.php?controller=DiscussionThread&method=getThread&threadId=<id>&format=json` (the `/f/p/<id>` number **is** the threadId for an OP). The OP text is in `jsonModel` (a JSON-encoded rich-text doc — walk `content[]` nodes for `type:"text"`), plus `title`, `createdBy.name`, `creationDate.epochSecond`, `postCount`. **Embedded images** are listed in `_embedded.contentImages[].url` → plain `static.wikia.nocookie.net/<uuid>` URLs, downloadable with the standard CDN curl. *(Caveat: the reply-fetch endpoint `controller=DiscussionPost&method=getPosts` returned the wiki's global recent posts, not the thread's replies — unsolved; OP + images usually suffice.)* Works for `gta.fandom.com` too (same platform).
- **GTAForums / any 403 page with no API:** browse manually, paste **verbatim** excerpts into the relevant thread file, cite the source number in [`sources.md`](sources.md). *(Wayback checked 2026-07-04 for the [#15] Gertrude thread: no snapshot.)*
- **🆕 YouTube metadata without a renderable page (2026-07-05 — how the [#80] corpus was pinned):** watch pages render empty for WebFetch, but **(a) oEmbed** gives title + channel attribution: `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<ID>&format=json` (`author_name`/`author_url` = the channel — how the April-Fools and copycat videos were told apart from Strange Man's); **(b) upload dates** come from the watch page's embedded JSON-LD via plain curl: `curl -s -A "Mozilla/5.0" "https://www.youtube.com/watch?v=<ID>" | grep -o '"uploadDate":"[^"]*"'`; **(c) a channel's recent uploads** via RSS: `https://www.youtube.com/feeds/videos.xml?channel_id=<UC…>` (channel_id greppable from any watch page; ⚠️ only the latest ~15 videos); **(d) video descriptions** via `grep -o '"shortDescription":"[^"]*"'` on the watch page (how the Robbin-Rams "cinematic/mods" self-disclosure was caught). GitHub file/commit provenance: `https://api.github.com/repos/<owner>/<repo>/commits` + `raw.githubusercontent.com/<owner>/<repo>/<commit>/<path>` (how [#78] was pinned to its 2019-12-01 commit).
- **🆕 WebFetch vs curl on APIs (2026-07-05):** `reddead.fandom.com/api.php` intermittently returns **402** and Arctic Shift returns **422** *to WebFetch* while plain `curl -A "Mozilla/5.0"` on the identical URL works — when an API misbehaves under WebFetch, drop to curl before concluding it's blocked.
- **🆕 RDR2 decompiled-script dumps on GitHub (2026-07-05 — how the [#52] script-side claims were reproduced, [#87]):** full public dumps of the game's decompiled `.ysc.c` scripts exist and are shallow-clonable + greppable in minutes — `creativewild/rdr2-scripts-decompiled` (build 1491.50, 1,638 scripts, committed 2024-06; mirrors: outsider31000, JayKoZa — same decompiler lineage, not independent). Recipe: `git clone --depth 1`, then grep strings AND computed **joaat hashes** (Jenkins one-at-a-time on the lowercased name — decompiled output renders unknown hashes as `0x…` literals; a 10-line stdlib Python computes them). ⚠️ Scripts only — entity placements/particle configs/timeFlags live in *data* files no public dump covers yet; local names aren't preserved by the decompiler (savegame string literals are). Any claim "script X does/doesn't reference Y" is now cheaply checkable — check before trusting. use the **Arctic Shift** community mirror, which is *not* blocked. Search a sub, then download the `i.redd.it` image (the CDN is reachable). Worked first try 2026-06-13 to grab the matchstick sets. ⚠️ **Availability notes:** on 2026-07-04 the API returned `{"data":null,"error":"Under maintenance"}` — retry later rather than assuming a block (it was back 2026-07-05). Separately, `{"data":null,"error":"Timeout. Maybe slow down a bit"}` = **rate limiting** — space calls ~20s apart and don't run parallel agents against it (they share the egress IP). A date-bounded sweep works: `posts/search?subreddit=SUB&after=YYYY-MM-DD&limit=100&sort=asc` (no `query` needed):
  - Search: `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=SUB&query=QUERY&limit=25` (omit `subreddit` for a site-wide search → **400**; a subreddit is required). Each result's `url` field is the image link.
  - Full post detail (selftext, gallery `media_metadata`): `https://arctic-shift.photon-reddit.com/api/posts/ids?ids=ID1,ID2`.
  - Download the image: stdlib `urllib` with a browser `Investigator-Agent` from `i.redd.it/<hash>.<ext>` (PNG/JPG come through fine).
  - **Always corroborate** — Reddit is C-tier; here each image was verified against the investigator's firsthand in-game screenshot.

> Always record provenance: a web image goes in [`images/README.md`](../images/README.md) with its source; a claim cites a numbered row in [`sources.md`](sources.md).

---

## Gaps — still wanted
- ~~**Canonical Strange Man video URL(s)**~~ ✅ Pinned 2026-07-05 → [source #80](sources.md) (channel-verified via oEmbed; dates from watch-page JSON-LD; method below).
- ~~**A Reddit r/reddeadmysteries master thread** for the spider mystery.~~ ✅ Found 2026-07-02 → `1pzutww` ([src #64](sources.md)).
- **Rockstar credits / artbook scans** — only if the `LJ`/`SM` dev-initial question ever needs settling.
- **An independent RDR2 asset dump** listing the `spiderdream0X` instance placements — would upgrade the [K39] mapping C→A. *(Partial progress 2026-07-02: the recovered [#52] datamine independently confirms the 8 `spiderdream01x–08x` archetypes as timed fragments — the file **structure** — but gives no per-web coordinates, so the [K39] number→location **mapping** is still single-source.)*

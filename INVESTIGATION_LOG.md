# Investigation log

Chronological record. Newest entries at the top. Keep it terse: what we did, what we learned, what changed.

## 2026-06-13 — Acquired the missing `J+M` & `S+J` matchstick images; new fetch recipe: Reddit-403 → **Arctic Shift** mirror

**Goal:** get the two missing matchstick *initial* images ([K9]/[U5], EVIDENCE-CHECKLIST #8) — `J+M`@Cornwall K&T and
`S+J`@Caliga Hall (we already held `EC`@Vetter's Echo). Confirmed they're **not on the Red Dead Wiki** (its Spider Dream page
carries only the 16 images we hold; `allimages` prefix `Match` → none), **not in the Google Site set**, and absent from the
articles/Tumblr Caliga Hall posts. The one Steam screenshot of the arrow set was **removed**.

**The unlock — Reddit access.** Reddit **403-blocks our fetcher** at the egress-IP level (site, `old.reddit.com`, and `.json`
all fail; UA spoofing doesn't help; `WebFetch` can't reach reddit.com either). The **Arctic Shift** community mirror
(`arctic-shift.photon-reddit.com/api`) is **not** blocked — `/posts/search?subreddit=reddeadmysteries&query=matchsticks`
surfaced all the sets in one call, and the **`i.redd.it` CDN is reachable** for the actual images. Recipe written up in
[`RESOURCES.md`](sources/RESOURCES.md) + [`CLAUDE.md`](CLAUDE.md) (sources **#47–50**).

**Acquired (both verified against the user's firsthand in-game screenshots — a clean second-source match):**
- `images/matchsticks/cornwall-kerosene-tar_matchstick-jm.png` — `J + M` at Cornwall K&T (Wm Sletcher "Weight Lifter" card +
  Maude Engel photo). u/Jeralt.
- `images/matchsticks/caliga-hall_matchstick-sj.jpg` — `S + J` "on a table in caliga hall." u/KermitTheFraud92.

**Also learned:** the **arrow** set is community-pinned to the **Old Trail Rise** basement (= the earlier "burnt-out house
basement" lead). Image still wanted but deprioritised (standard stash pointer, not an initial). **Changed:** images/README
provenance + still-wanted #3 (done), thread 03 (images linked, locations image-corroborated, arrow location added, task
ticked), EVIDENCE-CHECKLIST #8 (mostly done), sources #47–50, RESOURCES + CLAUDE fetch recipe. No new IDs minted (these
images corroborate existing [K9]).

---

## 2026-06-13 — Correction: chronology runs RDR2 → GTA, not the reverse; new GTA↔RDR2 crossover dossier ([K23] reworded, [K24], [S14])

**User-flagged correction to the entry below.** That entry treated the **2019 GTA Online Nazar number** as a "documented prior
purpose" that **demoted** Gertrude's spider-cipher reading. **That had the chronology backwards.** Verified the dates:
- **RDR2 released Oct 26, 2018** — Gertrude (epilogue, base game) recites the number from launch.
- **Madam Nazar** entered **RDO** in **Frontier Pursuits (Sept 10, 2019)** as the **Collector-role** mystic/fortune-teller (an
  in-fiction *guide to hidden things*). *(Newsweek/gtabase — #46.)*
- The **GTA Online "Nazar Speaks" machine** that speaks `1237645112` arrived with the **Diamond Casino Heist (Dec 12, 2019)** —
  **~14 months after** RDR2. *(GamesRadar/PCGamesN — #40/#41.)*

**So the GTA side is a *later callback*, not a prior origin.** It does **not** explain the RDR2 number away — if anything,
Rockstar echoing the exact digits cross-game says the number is **deliberate**. What stays open: **which** mystery it serves
(spider trail / standalone Nazar-Braithwaite egg / undecipherable). **[K23] reworded** accordingly; [U6] is **not** demoted on
chronology grounds (the only thing arguing against a spider link is the C-tier #43 hoax exposé).

**Also verified the user's other claims (all confirmed):**
- **[K24] new** — **GTA V's two Mt Chiliad spider-webs are base-game since the 2013 launch, not DLC** (1–2 AM, by the
  cable-car/mural; "untouched for over a decade"); **same cable shader** as RDR2's webs; link surfaced **~Jan 2026 (Oddheader)**.
  So the webs in **both** games are original-to-launch; only the Nazar number callback was added later. *(Dexerto — #45.)*
  → answers part of [U18].
- **Nazar's machine names real RDR2 places absent from GTA V's map** — incl. **Window Rock, Roanoke Ridge, Grizzlies, Strange
  Man**, the *"web…unraveling"* fortune ([U19], now confirmed a real line), and the number ([K23]). Logged as **[S14]** —
  flagged **weak** (Nazar references ~16+ RDR places map-wide; overlap partly expected by chance). *(gtaboom — #44.)*

**New file: [analysis/gta-rdr2-crossover.md](analysis/gta-rdr2-crossover.md)** — the crossover dossier (timeline, fortune
list, Mt Chiliad webs, what it does/doesn't prove). **Propagated** the correction across K23/K24/S14, U6/U18/U19, connections
§2/§3/§6, speculation S4/S5/S8/H2 + new S14, STATUS, EVIDENCE-CHECKLIST, README, Braithwaite Manor; **sources #44–46** added.

**Net:** the crossover **raises confidence the material is deliberate**; the decode/payoff is **as open as before**.

---

## 2026-06-13 — Gertrude's numbers resolved as a GTA/Nazar cross-game egg ([K23]); spider-cipher reading demoted; Strange Man video alleged hoax
> ⚠️ **Superseded in part by the entry above (same day):** the "demoted to long-shot / GTA crossover is a *prior* purpose"
> framing was a **chronology error** — the RDR2 numbers (2018) predate the GTA echo (2019). The K23 *fact* (the number-match)
> stands; the *interpretation* is corrected above. Kept for history per CLAUDE.md.

**Drove the Gertrude thread ([U6]) from the web — and it reframed the thread instead of cracking it.** Three independent
B-tier outlets (GamesRadar, PCGamesN, TheGamer; + SVG #24 already on file) document that Gertrude's recitation **opens
`1237645112` (`123 7645112`)** and that this **exact string** is what the **Madam Nazar "Nazar Speaks" fortune machine**
speaks in **GTA Online**, introduced in the **Diamond Casino Heist update (Dec 2019)**. So the number is a **deliberate
Rockstar cross-franchise Easter egg with a documented purpose that predates the 2025 spider-web resurgence.**

**What changed:**
- **Minted [K23]** (known-facts + thread 04 KNOWN + INDEX). Fixes the **opening** sequence as `1,2,3,7,6,4,5,1,1,2` (journalism
  parses the tail `…5,1,1,2`; our audio heard `…5,11,2` — same audio; the opening seven `1,2,3,7,6,4,5` is solid either way).
- **[U6] → PARTLY RESOLVED & downgraded** from top-priority: opening sourced; only the **tail** + "any *layered* meaning beyond
  the crossover" stay open. **Dropped off the STATUS top-5** (replaced by [U22] and [U14]).
- **Connected [U18] (Mt Chiliad cable-webs) and [U19] (Nazar "web…unraveling" fortune)** — the **same Nazar machine** is the
  bridge: it both gives the fortune **and** speaks Gertrude's number. K23 confirms Rockstar *does* plant GTA↔RDR winks, but
  also supplies a **mundane pre-spider origin** for the one number we thought might be a spider cipher.
- **Adversarial ([#43], C-tier):** a Red Dead Wiki forum exposé calls the Strange Man "Gertrude's Numbers Solved – Spider Web"
  video a **hoax** (reused NPC model for the "healthy Gertrude" photo; unfalsifiable number-picking; Braithwaites=Scarlett
  Meadows not Saint Denis; outhouse points to **Copperhead Landing**, not Butcher Creek). Per CLAUDE.md: **refuted, not
  deleted** — softened **H2** (Gertrude-as-4th-node now a long-shot), flagged **Strange Man's *Gertrude* claim as disputed**,
  and recorded the **contested** outhouse-alignment (Copperhead vs Butcher Creek — both C-tier, assert neither).
- **Parked attempt B** (read tally nodes in Gertrude's order): a match is now meaningless given the digits' documented origin,
  and the nodes are bare counts with no per-node letter to reorder anyway.

**Net for the case:** Gertrude is **more likely a parallel/older GTA-crossover egg than a node in the spider trail.** No
progress on the actual payoff — but a real **negative/clarifying** finding (the kind worth logging). **Sources added #40–43.**
**Propagated:** known-facts, thread 04, INDEX (K23 + U6/U18/U19), unknowns, connections §2/§3/§6, STATUS, EVIDENCE-CHECKLIST.

---

## 2026-06-13 — Added a resource directory: `sources/RESOURCES.md`

Spun the recurring **resources** out of the per-claim ledger into a new **[sources/RESOURCES.md](sources/RESOURCES.md)** — a
"where do I go for what?" map (verbatim in-game text → reddeadreference Tumblr; location facts → Red Dead Wiki; the web trail →
Strange Man; theories → GTAForums/Reddit; datamines/maps → the community Google Site; news/payoff → games journalism), each with
a one-line "useful for" and reliability tier. Folded in the **fetch cookbook** (the MediaWiki `action=parse` / `imageinfo`
recipes, the Wikia-CDN + Tumblr `curl` invocations, the 403 workarounds) that was previously scattered across CLAUDE.md and
`images/README.md`, and listed the open **gaps** (canonical Strange Man video, a Reddit master thread). Cross-linked from
`sources.md` (top pointer) and the STATUS spine map. `sources.md` stays the numbered citation ledger.

---

## 2026-06-13 — Register Rock: complete carving list sourced + cross-checked against the letters ([U24])

**Task: a comprehensive list of every name / word / initial on Register Rock and any spider-mystery connection.** Sourced
the **full** inscription set three ways — the **Red Dead Wiki** (headline names, via MediaWiki `action=parse`), the
**reddeadreference transcription blog** (the fullest photo-by-photo set), and **our own journal image** (which matches the
blog's "Photo 1" exactly, corroborating it). Result: the dossier previously held 7 headline names + 4 journal fragments;
it now lists **~14 full names** (added **J. V. Henry ×2, Jasper Munson, C. Riley, A. Pickel, Doyle/Missouri, R. Mack/Otis,
Henry Matilda, Mary**) plus **~10 bare marks** (**W.Y.B, BM, R.M, R.S, R.S.G, Jm, DOF, WSF, ORW, .8DB8.**), the place-names
(Wyoming/Texas/Ohio/Missouri/California/Oregon) and dates (1842/1846/1863/1882).

**New finding — desk cross-check vs the matchstick letters `{C,E,J,J,L,M,S,S}`:**
- 🟢 **J.M appears TWICE** — bare mark **"Jm"** and full name **"Jasper Munson"** — directly echoing the **`J+M`** matchsticks
  at Cornwall K&T ([K9]). This is the strongest *new* internal signal; the corpus had previously only flagged S. Gray.
- 🟢 **S. Gray** → Gray family → **Caliga Hall** `S+J` (already known; still the cleanest narrative link).
- 🔴 **Partial-negative:** **no `LJ`, `SM`, or `EC`, and no `L`-initial at all** anywhere on the rock. So Register Rock
  supplies J/M/S/C but not the `L`/`E` legs of the set — awkward if it were meant to be the single name-key.

**Caveat unchanged:** all of this is gated on [H11] — *does* the Fort Brennand third symbol actually depict this rock? Until
that's confirmed, the matches are a lead ([U24]), not a solution. Kept all names live per [S13] (don't discard West/Ward as a
"Batman gag"). **Updated:** dossier, connections §1 (table + current-read + task), unknowns U24, thread 02 H11, INDEX U24, STATUS.
**Source added:** reddeadreference Tumblr (B/C) in `sources` + the dossier.

**Image + verification pass (same day).** Fetched **+4 images** (wiki CDN `_02`/`_03`; Tumblr close-ups Photos 2 & 4) and
**firsthand-verified** the two close-up faces against the blog text — Photo 4 plainly shows J. Brooks / US Post 1863, J.V.
Henry 1842 / Dortha Ohio, Henry Matilda / Calif., Mary, .8DB8., and Jasper Munson running up the right edge; Photo 2 shows
Doyle / Missouri, R.M, R.S, and **"BM" carved as a boxed cattle-brand**. The clearer journal sketch (`_03`) **corrected three
readings**: "98 T·BART · TEXAS" (was "78 J'Bart"), boxed **"DOF"** (was "DOE"), legible **"A. Pickel"** (was "A.Nicil"), and
revealed a partial **"E M / S"** mark cut off at the edge (carvings continue past the drawn area). **Community check:** no
source anywhere links Register Rock to the spider mystery — it's treated only as an Oregon-Trail homage, so [H11]/[U24] is our
**novel** correlation (no external corroboration either way). Also disambiguated: the Register Rock **POI ≠ the 10 "Rock
Carvings" collectibles**. Logged all in the dossier + `images/README.md` provenance.

---

## 2026-06-13 — Correction: don't treat "dev in-joke" names as noise → new principle S13

**User flagged an over-assertion.** I'd called Register Rock's **A. West / B. Ward** "noise" because the wiki *speculates*
they're Adam West / Burt Ward (*Batman*). Two problems: that association is **unconfirmed wiki speculation**, and — the real
point — **a puzzle may deliberately use names that double as real-world/pop-culture references so players dismiss them** and
never test the in-game link. Camouflage-as-joke ≠ disqualification.

**Fix:** softened every "noise / strip the Batman gag / pre-filter" instruction (connections §1 table + caution + task,
speculation H11, unknowns U24, thread 02, register-rock dossier) to **"keep all names live; let the test decide."** Minted
**[S13]** (the general principle) in INDEX + speculation rollup, and added it as the **inverse caution** to the anti-pareidolia
[carving test](analysis/carving-technique.md) (that test stops us *inventing* clues; S13 stops us *missing* ones dressed as jokes).

---

## 2026-06-13 — Two frontier leads: Bacchus Bridge empty heart (K22) + Register Rock names (H11); +5 images

**Both from investigator data; both now sourced/grounded against the wiki.**

**1. Bacchus Bridge empty heart — [K22] / [H10] / [U23].** An **empty cupid-heart-with-arrow** is carved on a leg of
**Bacchus Bridge** (Cumberland Forest), **hard to find**, reported **in line of sight of the Fort Wallace bird carving**
([K16]). It's the **blank twin of the Flatneck Station "Lillie ♥ Alfred" heart** — identical shape, **no names/text**. This
**re-frames last pass's "rejected" datamine**: the Flatneck *inscription* is still a separate egg, but the **heart motif** is
now an active NW-frontier lead (a deliberately *emptied* heart aligned with the bird carving reads like a placed marker). Kept
the datamined Flatneck heart as the comparison reference. New dossier [locations/bacchus-bridge.md](locations/bacchus-bridge.md).

**2. Register Rock — [H11] / [U24].** The user proposes Fort Brennand's debated **third tower symbol** (pole · factory ·
"oil puddle?") actually depicts **Register Rock** — a names-and-dates boulder in **central The Heartlands**, exactly where the
symbols point. Pulled the wiki: it bears **J. Brooks, Frank Heck, Otis Miller, Billy Midnight, Scott Gray ("S. Gray 1846"),
A. West, B. Ward**. If the symbol points there, those **names are a candidate puzzle** for `LJ`/`SM` + the matchsticks.
**Discipline:** A. West / B. Ward are an **Adam West / Burt Ward Batman gag** (per wiki) — flagged as noise. The standout
signal is **S. Gray → Gray family → Caliga Hall**, the `S+J` matchstick site ([K9]). Added the name table to
[connections.md](analysis/connections.md) §1 + the name-matching task; new dossier [locations/register-rock.md](locations/register-rock.md).

**Images (+5):** `register-rock/` ×3 (in-world "S. Gray 1846", journal sketch, map) from the wiki CDN; `bacchus-bridge/` ×2
(bridge overview from wiki, Flatneck heart datamine reference).

**Propagated:** INDEX (K22/H10/H11/U23/U24), known-facts (K22), speculation (H10/H11), unknowns (U23/U24), thread 02 (Register
Rock), thread 06 (Bacchus heart), connections §1, locations/README, images/README (+reframed note), STATUS.

---

## 2026-06-13 — Boundary respawn mechanic (K21) + 3-boundary web partition (H9); +1 image

**New mechanic, from investigator data (high-trust).** A shot web feather **falls to the ground, is non-interactable, and
does NOT respawn while the player stays inside the boundary that web is tied to** — leaving the boundary respawns it. A
deliberate design. There are **three boundaries: north, south, and a connector linking them**; multiple webs can share one.
Logged as **[K21]** (refines/explains [K13b], which was only "a chain that doesn't respawn").

**Sourced the map that depicts it.** Revisited timeline image `tl_09` (the one we'd skipped as a near-duplicate) — it's
actually the **Jay_0048 boundary map**, distinct from the chain map: three coloured rectangles = the three boundaries. Pulled
it, zoomed each region with Pillow to read every label, and saved it as
[`web_map-overlay_boundaries.png`](images/webs/web_map-overlay_boundaries.png).

**Read the partition → [H9] (SPECULATION, C-tier map):** **North** = `B34` (Cornwall); **Connector** (a tall box bridging
New Hanover↓Lemoyne) = `B23, B45, B56, B56L`; **South** = `R23, R45, R34`. Clean and complete — 1+4+3 = all 8 webs, one
boundary each. **Key link:** the **Connector's four webs are exactly the [K13b] non-respawn chain** — so the chain isn't a
free-floating sequence, it's "the Connector boundary's members." Minted **[U22]** to verify membership (the map's legend typo
writes Saint Denis as "R56" = `R34`; the single-web North boundary is unconfirmed).

**Propagated** across INDEX (K21/H9/U22), known-facts (K21 + K13b cross-ref), speculation (H9), unknowns (U22),
analysis/connections (new §5a + table), the WEBS-MANIFEST Order section + reference list, images/README, and STATUS.

---

## 2026-06-13 — Image hunt: +7 from the community Google Site; one red-herring rejected

**Goal:** close gaps in [images/README.md](images/README.md#still-wanted-images-source-from-the-web-first). First confirmed the
**wiki page holds exactly the 16 images we already have** (MediaWiki API `prop=images`), and a file-namespace search surfaced
nothing else relevant — so the missing images aren't on the wiki. Pivoted to the community **Google Site** (source #36).

**Extraction method that worked:** the site is JS-rendered, so `WebFetch` strips its images. Pulling the **raw page HTML** and
grepping `lh3.googleusercontent.com` URLs recovered them — **13 on Timeline, 2 on Facts.** (Recorded this in the manifest so
the next session doesn't re-fight `WebFetch`.)

**Added 7** (all C-tier community overlays/datamines, named to convention, provenance logged):
- `web_map-overlay_all-labeled.jpg` — best all-webs reference map (name+code+hour for all 8 + Centre + guitar poles).
- `web_map-overlay_shooting-chain.png` (Jay_0048) — visualises the non-respawn chain `B23,B45,B56,B56L`.
- `web_map-overlay_nw-trail.jpg` — spider-shape overlay with the trail drawn NW to a "?" (the cold frontier, thread 06).
- `web_cable-mesh_datamine.png` (thecochiti) — the four `cablemesh*` models; **yellow = feather positions in the mesh.**
- `web_cornwall_b34_pole-carving.jpg` — the Cornwall spider carving on the actual in-world pole.
- `fort-wallace_two-guitars_map.png` — the two Fort Wallace guitars annotated (point different ways).
- `fort-wallace_bird-symbols_tower_view2.jpg` — clearer daytime shot of the two moss "w"/bird roof symbols.

**Verifications / discipline:**
- The Facts page's per-web table (location · code · time · colour) **matches our [WEBS-MANIFEST](images/webs/WEBS-MANIFEST.md)
  exactly** — independent corroboration of the K13a catalogue.
- **Rejected** a datamined `…treeplaceholder2` texture whose alpha reveals "LILLIE ♥ ALFRED … 1898/1903": web search identified
  it as the **Flatneck Station "Lillie & Alfred" tree carving** — an *unrelated* easter egg. Kept out of the corpus; noted in
  images/README so it isn't re-added.
- The `cablemesh` datamine **corroborates** the shared GTA V/RDR2 cable-shader claim and gives the *model's* feather attach
  points — but **not** each pole's in-world feather **orientation**, so **[U0] stays open**.
- Flagged a community-map error: Jay_0048's legend says `R56` for Saint Denis; primary wiki says **R34** — trust R34.

**Still missing after this pass:** per-web in-world **feather orientation** (U0); the **`J+M`/`S+J` matchstick** sets (not on
wiki or the Google Site — next look is Reddit discovery threads / matchstick videos); a count-by-colour **Window Rock mural**.

---

## 2026-06-13 — Added `experiments/` for computational testing of findings

**Enabled running code, not just prose.** Some leads are combinatorial/cipher/geometry/likelihood problems that reasoning
can't settle — so added an [`experiments/`](experiments/) area with conventions ([`experiments/README.md`](experiments/README.md)),
wired into [`CLAUDE.md`](CLAUDE.md) (corpus map + a working norm) and the README org table.

**Discipline kept intact:** a script **tests**, it doesn't establish fact — a positive computational result is
**[SPECULATION]** until sourced; a *negative* result is a real, loggable finding (precedent: A1Z26 → null). Scripts must
cite input provenance (never invent data), mark provisional inputs, and stay reproducible (stdlib, deterministic).

**Seeded one honest example** — [`feather_order.py`](experiments/feather_order.py) (tests U0/H4 against the documented
non-respawn chain K13b). Result: the one known ordering fact collapses the **40,320** possible 8-web shooting orders to
**3,360**; capturing feather orientation (U0) is what would narrow it further. Nothing promoted — illustrative only.
Pointed the analysis open-tasks + STATUS analysis channel at this option (Gertrude cipher, dev-initials odds, name-list
matching are the obvious next scripts).

---

## 2026-06-13 — Image naming convention enforced; broken image links fixed; workflow re-pointed web-first

**Two operator-requested changes.**

**1. Image naming convention.** Defined and enforced a single scheme — `<subject>_<detail>[_<qualifier>].<ext>`, all
lowercase, fields split by `_`, words within a field by `-`, first field = the subject's place/topic (webs use
`web_<location>_<code>`). Documented it in [images/README.md](images/README.md#naming-convention-enforced). **Renamed all
21 image files** to it and **updated every reference** across README, threads, locations, analysis, and the webs manifest.
- **Found & fixed broken links in the process:** thread 03 pointed at a non-existent `images/oilfields/…`; thread 05 had
  **11 dead links** to an `images/spider-dream/` folder that doesn't exist (pre-reorg paths); thread 01 linked the same
  missing folder. All re-pointed to the real files. Verified by script: **every image reference now resolves.**

**2. Web-first sourcing.** Per the operator: don't ask for in-game capture unless strictly necessary — images can be
sourced from the web and verified. Renamed `CAPTURE-CHECKLIST.md` → **[EVIDENCE-CHECKLIST.md](EVIDENCE-CHECKLIST.md)** and
reframed it (and STATUS, INDEX, CLAUDE, the webs manifest, images/README) so the **default channel is 🌐 web/video
sourcing + verification**; in-game capture is reserved for the one genuinely undocumented detail — **feather orientation**
(U0) — and the long-horizon H8 test. Updated CLAUDE.md to make this a standing working norm.

**Open:** unchanged substance; the top lead (U0 feather orientation) is now "pull from the Strange Man video first."

---

## 2026-06-13 — Repo reorganized: added a coordination spine + fixed rollup drift

**No research this session — a structural pass to make the corpus faster to pick up and harder to let drift.** Directories
left as-is (the layout is sound and many relative links depend on it); added a lightweight coordination layer instead.

**New spine files:**
- **`STATUS.md`** — live dashboard / session entry point: one-line status, ranked open questions, next actions split by
  channel (🎮 in-game / 🌐 web / 🧠 analysis), recently-resolved. Pointers only, to avoid new drift surface.
- **`INDEX.md`** — ID registry for every `K`/`U`/`H`/`S` (claim · status · canonical home). Fixes the "update every place
  an ID appears" problem that previously needed a grep hunt.
- **`CAPTURE-CHECKLIST.md`** — the capture worklist, tiered by value; the 8-web portion defers to the existing
  `WEBS-MANIFEST` rather than duplicating it. *(Renamed → `EVIDENCE-CHECKLIST.md` and reframed web-first later the same day — see the entry above.)*

**Drift fixed (core-invariant violation):** `findings/speculation.md` held only **H1–H2**, but **H3–H5** (connections.md)
and **H6–H8** (dreamcatchers.md) existed only in `analysis/`. Added all six to the speculation rollup so it is complete again.

**Guardrails:** updated `CLAUDE.md` — documented the spine, made `INDEX.md` part of the ID-update rule (append-only IDs),
and stated explicitly that the findings rollups must list **every** `H#`/`S#`/`K#`/`U#` even when detail lives in `analysis/`.
Pointed `README.md`'s org table at the new spine with a "start here" note.

**Open:** nothing new opened. The investigation's substance is unchanged — top task remains the 🎮 feather-position capture (U0).

---

## 2026-06-13 — Second deep-research pass merged (20/25 verified): dev quote resolved, Fort Wallace = waypoint, Spider Gorge downgraded

**Ran a second deep-research workflow** (102 agents, 20 sources, 25 claims adversarially verified → 20 confirmed / 5 killed)
targeting the open web-researchable questions. Merged the verified results; added **sources #27–37**.

**Corrections & resolutions folded in:**
- **U8 RESOLVED → K3 rewritten.** The Jan 2026 dev comment is **Adam Butterworth, a former Rockstar *QA tester*** (now at
  Remedy): *"Absolutely wild people have found this. I remember hearing about this and thinking it would never be discovered."*
  Confirms the egg is **real/deliberate, NOT that he authored it.** This **supersedes both** prior framings — the 1st pass
  over-claimed "confirmed intent," the 2nd over-corrected by deleting his name. Now named, with a B/C-tier (single-origin)
  caveat.
- **Fort Wallace = waypoint, not dead-end.** The "trail goes cold at Fort Wallace" framing is **outdated**: two guitars there
  (one→tower, one on tower→roof), and the trail **continues NW** toward **Calumet Ravine / the Giant's birds** and a **"?"
  carving on an out-of-bounds mountain** = the current cold frontier (post-Jan-2026, **unverified**, ties into thread 06).
  Updated K12, U2, U12, README, fort-wallace dossier.
- **Spider Gorge DOWNGRADED (U13).** **No secondary source corroborates it** — it's wiki-Part-4 speculation only; journalism
  points the `NW`+guitar marker at Fort Wallace. Softened thread 05, the dossier, README table (Fort Wallace + Spider Gorge
  now separate rows).
- **Payoff (U2): still NONE as of June 2026.** *"No new loot, tools, or cutscenes"* — vindication is the only "reward."
  Nothing solved since Dec 2025; post-Jan progress is additive lead-finding. Cut-content = *a* possibility, not "the leading
  theory."
- **Time-lock correction:** the "Cornwall start-pole spider engraving appears only ~3–4 AM" claim was **refuted** — **1–2 AM**
  belongs to the *central feather-less* webs; the start-pole's exact hour is unverified. Fixed thread 01.
- **Feathers:** 5 black + 3 red `spiderdream` count **re-confirmed**; per-feather location/time-lock/**position-order still
  undocumented** → **validates U0 as an original in-game-capture lead.**

**Still open (pass did NOT advance — need in-game/video capture, not web search):** Gertrude's exact numbers (U6),
per-feather positions (U0), matchstick identities EC/Annabella/J+M/S+J (U16), Window Rock mural (U14), Nazar Speaks (U19),
canonical Strange Man video URL.

---

## 2026-06-13 — Dreamcatchers collectible documented; U17 reframed; K20 added (mystery has no in-game log)

**Pulled the authoritative *Dreamcatchers* wiki text** (MediaWiki API, since fandom 403s direct fetch) → raw JSON saved to
[`sources/dreamcatchers_api.json`](sources/dreamcatchers_api.json); added as **source #26**. Wrote a new dossier
[analysis/dreamcatchers.md](analysis/dreamcatchers.md).

**What it is (KNOWN):** a **20-piece collectible strand**; in-game blurb *"Find all Dreamcatchers to reveal their secret."*
Finding all 20 makes a **journal entry connect the points into a drawn animal**, whose **eye = Elysian Pool** (behind the
waterfall); the reward — the **Ancient Arrowhead** — sits **in the eye of a painted bison** in the cave. Needed for **100%
Completion** (achievements: Collector's Item, Best in the West).

**Why it matters to the mystery:**
- **U17 reframed (with a correction).** ⚠️ Earlier text wrongly implied the **spider mystery** doesn't clear from the log. It
  doesn't — because it has **no log at all** (new fact **K20**: no quest entry/notification/web counter; finding-driven and
  invisible; investigator data). The never-clearing log entry belongs to the **dreamcatchers** side mission; the spider wiki
  cites it only by **analogy**. New live theory **H8** (from the user): the dreamcatcher entry may be stuck because something
  is **left to finish — possibly the spider mystery** — so completing the spider trail could be what clears it (falsifiable,
  untested).
- **Stronger ties are mechanical/thematic:** a dreamcatcher is a **spider-web-shaped, dream-themed Native craft** (unites all
  three mystery signatures), and its **connect-points→shape→find-the-eye** payoff is a **shipped precedent** for the web
  trail's connect-the-webs mechanic — concrete ammunition against the "pareidolia" objection
  ([carving-technique.md](analysis/carving-technique.md)). Logged as **H6/H7**.
- **Location overlaps to test (lead, not proof):** dreamcatcher pins sit by **Window Rock (#2)**, **Heartland Overflow (#17 =
  web B23)**, and **Elysian Pool (#15 = the reward cave)**.

**Synced:** new **K20** (known-facts + thread 01), U17 reworded (findings/unknowns), thread 01 (SPECULATION), thread 05,
sources #26, README analysis row, images/dreamcatchers/ (2 images).
**Open:** screenshot the journal drawing in-game to ID the animal; map the 20 pins vs the 8 webs; **test H8** — does finishing
the spider trail clear the dreamcatcher log entry?

---

## 2026-06-13 — Matchstick locations pinned; dev-initials reading weighted down

**Investigator data:** `J+M` matches are at **Cornwall Kerosene & Tar** (= the **web-trail start-pole** site — strong sign the
matchsticks are *part of the puzzle*), and `S+J` matches are at **Caliga Hall** (the **Gray** estate, Braithwaite rivals).
Web search didn't corroborate these specific spots → recorded as **investigator/firsthand data**, high trust.
- Updated thread 03, connections (letter table now location-aware), known-facts K9, unknowns U5, locations index.
- Created [locations/caliga-hall.md](locations/caliga-hall.md); noted `J+M` on the Cornwall dossier.
- **New observation:** 3 of 4 letter-sites are already mystery nodes (Butcher Creek, Cornwall, Vetter's Echo); the 4th
  (Caliga Hall = Grays) plus **Braithwaite Manor = Gertrude** means **both feuding estates carry a thread** → possible
  letters-tied-to-families angle.
- **Dev-initials counter-hypothesis explicitly weighted DOWN** per the user's statistical argument (thousands of credited
  staff → a coincidental initial match is near-certain, hence weak; only founders/senior leads plausible). Stance recorded in
  [connections.md](analysis/connections.md) and thread 03.

---

## 2026-06-13 — Deep pass: 5 research efforts merged; images reorganized; locations + analysis added

**Ran the deep-research workflow to completion + 4 focused parallel agents** (the 8 webs/feathers; bird-carving→Calumet/Giant;
story ties; carving technique + cheat codes). Merged all verified results.

**Workflow verification (21 confirmed / 4 killed)** — folded in:
- Confirmed: pentagram+LJ/SM, Cornwall start pole, the 8-web W/NW/guitar trail → Fort Wallace & Spider Gorge, Gertrude.
- **Killed:** "Ambarino region"; the named **"Adam Butterworth *confirmed* intent"** (→ softened K3 to "a dev *reacted*");
  "leading theory = cut content" as a characterisation; the over-specific "arrow → dresser/wall stash."

**Big new findings integrated:**
- **8-web catalogue** (`spiderdream01–08`): 5 black + 3 red, with locations/times/codes → rebuilt [WEBS-MANIFEST](images/webs/WEBS-MANIFEST.md).
  A non-respawn **order chain** exists (`B23→B45→B56→BL56`). **Feather position is undocumented online → must be captured
  in-game** (validates the user's lead as potentially original).
- **Carving technique** answered: symbols **modelled into mesh geometry, hidden under moss/wood texture** (+ mesh "cables" for
  webs/pentagram); named assets prove intent. Wrote [analysis/carving-technique.md](analysis/carving-technique.md) with a
  concrete **anti-pareidolia test** (depth/parallax · named asset · time-gating · reproducible chain).
- **NW/Wapiti lead** stands up: Fort Wallace bird carving → Calumet flock → **the Giant** (heard not seen; **30-animals**
  gate confirmed; loves animals). New thread [06](threads/06-bird-carving-giant-wapiti.md).
- **"Birds of Paradise plants" = NOT official content** (fan YouTube pattern) — logged as refuted.
- **Window Rock correction:** it's Grizzlies **West**; the mural is the **Strange Statues** puzzle (counts **2,3,5,7**),
  speculatively linked to the 5/3 feather split.
- **Cheat codes** catalogued ([analysis/cheat-codes.md](analysis/cheat-codes.md)): "KEEP YOUR DREAMS LIGHT" @ Oil Fields;
  notable overlaps — a death-themed cheat carving at **Braithwaite Manor**, the wanted-level cheat at **Vetter's Echo**.
- **Narrative tie** assessed ([analysis/narrative-connection.md](analysis/narrative-connection.md)): 4 of 5 nodes sit in/near
  the Rains Fall/Eagle Flies arc (Cornwall=American Fathers I, Fort Wallace=The King's Son, Butcher Creek thematic, Wapiti=home
  turf); **Fort Brennand breaks it** → node logic likely geographic/atmospheric, not plot-driven.

**Repo housekeeping:**
- **Images reorganized** by location: `butcher-creek/ · matchsticks/ · webs/ · trail-markers/ · fort-wallace/ · window-rock/ ·
  wapiti-giant/ · maps/`. Downloaded 3 more (Giant map+cave, Strange Statues POI) → **19 images** total.
- Added **`locations/`** with 11 dossiers + index. Renamed thread 03 to *matchstick-letters*; arrows downgraded (stash
  pointers).

**Top open task remains:** capture the **8 webs' feather positions** in-game (the manifest is ready to receive them).

---

## 2026-06-13 — Primary wiki obtained; corrections + 16 images downloaded

**Breakthrough: got the authoritative wiki text.** The Fandom page 403s to fetch, but the **MediaWiki API** (`action=parse`)
works → full primary text saved to [`sources/PRIMARY-wiki-spider-dream.md`](sources/PRIMARY-wiki-spider-dream.md) (raw JSON in
`sources/spider_dream_api.json`). Downloaded **all 16 wiki images** via the CDN (`static.wikia.nocookie.net`) into
[`images/`](images/) — provenance logged in [images/README.md](images/README.md). Eyeballed two: outhouse #4 clearly shows
**`LJ`** (top) + **`SM`** (bottom); the Vetter's Echo matches clearly spell **`EC`** beside the **Black Widow** card.

**Corrections forced by the primary source** (superseding the earlier secondary-source pass):
- **Matchsticks ≠ oil fields.** There are **four** match-sets: **`EC`** @ Vetter's Echo (by the Black Widow card + letters to
  Annabella), plus **`J+M`**, **`S+J`**, and an **arrow→stash** elsewhere. The user's `J+M` is **real** but its location is
  *not* the oil fields. → renamed thread 03 to `03-matchstick-letters.md`; expanded the letter analysis to
  **{C,E,J,J,L,M,S,S}**.
- **Spider trail start = telephone pole near _Cornwall Kerosene & Tar_** (not the Heartland Oil Fields). Webs are spread
  across the map (one near **Saint Denis**), each **time-locked** to a different night hour; the **center webs** (1–2am, no
  feathers) spell **`N`** + a pole.
- **Exact inscriptions:** **`W ✞✞✞✞✞`** (5 poles west) → **`NW` + guitar** → Fort Wallace (cold). NW also points **directly
  to the tip of Spider Gorge** (guitar-shaped section, "spider" in the name) — a strong alt-destination.
- **Feathers:** **5 black + 3 red**, files named **"spiderdream"** (`wap_gen_feather01`). New lead: compare to the
  black/red bird-feather counts on the **Window Rock "Strange Statues" mural**.
- **"KEEP YOUR DREAMS LIGHT"** oil-field carving is **not** on the wiki's mystery page → demoted to "relevance unconfirmed."
- **New leads logged** (U13–U21): Spider Gorge, Window Rock mural, feather-pattern trigger, EC/Annabella identities,
  dreamcatchers log bug, GTA V Mount Chiliad cable-webs (1–2am), the 2019 **Nazar Speaks** "web…unraveling" fortune,
  Spider Grandmother myth.
- **Discovery credits** recorded (goldenplaysterraria, pariah87, u/fthen2k02, u/FL4VA-01, u/TracySevert, Strange Man).

**Still pending:** the deep-research verification workflow is running in the background; will merge its independently-verified
claims when it returns.

---

## 2026-06-13 — Repo founded; first research pass

**Setup**
- Created the repo structure: `threads/`, `findings/`, `analysis/`, `sources/`, `images/`, plus `README.md` and this log.
- Established the tagging discipline: `[KNOWN]` / `[UNKNOWN]` / `[SPECULATION]`.

**Research done (web search + fetch; see [sources](sources/sources.md))**
- Confirmed the **Butcher Creek pointer chain**: 5 outhouses w/ tallies 1–5 → pentagram; outhouse #4 has `LJ`/`SM` + a Fort
  Brennand symbol; Fort Brennand has tallies (6,7) + three tower symbols (telegraph pole, factory, oil pool) → Heartlands.
- Found the **"KEEP YOUR DREAMS LIGHT"** desk-drawer carving at the **Heartland Oil Fields** (thematic tie to "Spider
  **Dream**").
- Documented the **2025 telegraph-pole spider-web trail** (discovered ~Dec 2025, popularized by **Strange Man**): spider
  symbol on a Heartlands pole (~3–4 AM) → map overlay → ~8 poles + central tree web marked `N` → directions `N`, `W`×5,
  `NW` + guitar → **Fort Wallace, trail cold.**
- Logged **Gertrude Braithwaite**: dies in the Braithwaite **outhouse**, recites a number sequence (approx
  `1,2,3,7,6,4,5,11,2,…,1,2,10,3`). Multiple late-2025 videos claim her numbers tie into the Spider mystery — **claim not
  yet verified.**
- Noted a **former Rockstar dev** quote implying the Easter egg was intentional and expected to stay hidden (attribution
  TBD).

**Analysis seeded** ([analysis/connections.md](analysis/connections.md))
- Letter set **L, J, S, M**: `LJ`/`SM` (toilet #4) vs `J+M` (oil-field matchsticks) — same J/M, different pairing → likely a
  "re-pair these" nudge. User's "these are clues, not dev initials" hypothesis logged for testing (with the dev-initials
  counter-hypothesis kept honest).
- **Outhouse motif** flagged as the strongest structural link (Butcher Creek, Fort Brennand, Gertrude all outhouse nodes) →
  hypothesis **H2**: Gertrude is a 4th node, not disconnected.
- Two worked cipher attempts on Gertrude's numbers: **A1Z26 → null**; **permutation-of-1–7 → promising** (her opening
  `1,2,3,7,6,4,5` is a reorder of the seven tally values — maybe the *reading order* of the tally nodes).

**Open headline questions** (full list in [findings/unknowns.md](findings/unknowns.md))
- The verbatim **under-wood messages** on the 2025 poles (highest value).
- Does the `J+M` matchstick actually exist as described, and where exactly?
- Gertrude's exact sequence + whether it indexes the tallies.
- Is this **one puzzle or two** (2018 chain vs 2025 web trail)?

**Source-access issues**
- `fandom.com` and `gtaforums.com` return **HTTP 403** to automated fetch. Marked for manual browser capture.

**Next session**
- [ ] Manually capture the fandom *Spider Dream Mystery* page text + images.
- [ ] Pull the canonical Strange Man videos + the "Gertrude's numbers solved" videos; rate their claims.
- [ ] Begin in-game screenshot collection per [images/README.md](images/README.md) priority list.
- [ ] Build the character/credits name list to test L.J./S.M./J.M.

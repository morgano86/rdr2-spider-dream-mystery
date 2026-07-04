# RDR2 Spider Dream Mystery — Investigation

A serious, source-cited investigation into the **Spider Dream Mystery** in *Red Dead Redemption 2* and the web of connected
unsolved threads (Butcher Creek outhouse carvings, Heartland Oil Fields, Gertrude Braithwaite's numbers, and the
2025 "spider web" telegraph-pole trail).

> Status as of **2026-06-13**: **UNSOLVED — no confirmed reward or payoff** (Jan 2026 coverage: *"no new loot, tools, or
> cutscenes"*; vindication is the only "reward"). A major clue chain was decoded by the community in late 2025; the trail
> reaches **Fort Wallace — a waypoint, not the end**. The **last *verified* clue is the Fort Wallace bird carvings**;
> everything past them is unverified/contested — the off-map **"?" carving is not a widely accepted theory** (pareidolia),
> and the **Bacchus Bridge heart's relevance is about as contested as the "?"**. A **former Rockstar QA tester, Adam
> Butterworth**, publicly confirmed the egg is *real* — but **not** that he designed it.

---

## How this repo is organized

> **Picking this up? Start at [`STATUS.md`](STATUS.md)** — the live dashboard of where the case stands and what to do
> next. Use [`INDEX.md`](INDEX.md) to look up any claim ID, and [`EVIDENCE-CHECKLIST.md`](EVIDENCE-CHECKLIST.md) to turn
> open questions into sourced evidence (web-first).

| Path | Purpose |
|------|---------|
| [`STATUS.md`](STATUS.md) | **Live dashboard** — current status, ranked open questions, next actions by channel. The session entry point. |
| [`INDEX.md`](INDEX.md) | **ID registry** — every `K`/`U`/`H`/`S` claim, its status, and the file that owns it. |
| [`EVIDENCE-CHECKLIST.md`](EVIDENCE-CHECKLIST.md) | **Evidence worklist**, ordered by value — web-sourced + verified first, in-game capture only when strictly necessary. |
| [`README.md`](README.md) | This file — overview, map of the mystery, and quick status. |
| [`threads/`](threads/) | One file per investigative thread (01–09). Each separates **KNOWN / UNKNOWN / SPECULATION**. |
| [`locations/`](locations/) | A dossier per place the mystery touches (geography, story role, the clue physically there). |
| [`findings/`](findings/) | Cross-thread rollups: [known facts](findings/known-facts.md), [open questions](findings/unknowns.md), [speculation](findings/speculation.md). |
| [`analysis/`](analysis/) | Working theories: [connections/letters](analysis/connections.md), [carving technique vs pareidolia](analysis/carving-technique.md), [narrative tie](analysis/narrative-connection.md), [cheat codes](analysis/cheat-codes.md), [dreamcatchers](analysis/dreamcatchers.md), [Saint Denis Vampire precedent](analysis/saint-denis-vampire.md), [GTA↔RDR2 crossover](analysis/gta-rdr2-crossover.md), [Fort Wallace bird carving](analysis/fort-wallace-bird-carving.md), [decoy + dream hypotheses](analysis/decoy-and-dream-hypotheses.md), [solve grammar](analysis/solve-grammar.md), [web-order field test](analysis/web-order-field-test.md). |
| [`experiments/`](experiments/) | Small Python scripts that **test** findings (combinatorics, ciphers, geometry, likelihoods) when reasoning isn't enough — results are evidence, not fact. |
| [`sources/`](sources/) | [Per-claim source ledger](sources/sources.md), [resource directory + fetch recipes](sources/RESOURCES.md), the [full primary wiki text](sources/PRIMARY-wiki-spider-dream.md), and raw data (API JSON, `rdr2-credits.txt`). |
| [`images/`](images/) | Screenshots/maps by location. Key file: the [**webs manifest**](images/webs/WEBS-MANIFEST.md) (per-web location · time · feather colour · position). |
| [`INVESTIGATION_LOG.md`](INVESTIGATION_LOG.md) | Chronological log of what we did and decided. |

**Discipline:** every claim is tagged. `[KNOWN]` = verifiable in-game or in multiple reliable sources.
`[UNKNOWN]` = open question. `[SPECULATION]` = community or our own theory, not confirmed.

---

## The threads at a glance

1. **[Spider Dream Mystery](threads/01-spider-dream.md)** — the named, wiki-documented mystery. Spider imagery, the
   "dream," and the hub that the other threads feed into.
2. **[Butcher Creek outhouse carvings](threads/02-butcher-creek-carvings.md)** — five outhouses with tally marks forming a
   pentagram; outhouse #4 carries **`LJ`**, **`SM`**, and a **Fort Brennand** symbol. *(User's focus: the LJ/SM carving.)*
3. **[Matchstick letters](threads/03-matchstick-letters.md)** — four match-arrangements across the map spelling **`EC`**
   (by the Black Widow card at Vetter's Echo), **`J+M`**, **`S+J`**, and an **arrow**; plus the oil-field
   **"KEEP YOUR DREAMS LIGHT"** carving. *(User's focus — note: the `J+M` matches are real but NOT at the oil fields; see
   the thread for the correction.)*
4. **[Gertrude Braithwaite's numbers](threads/04-gertrude-numbers.md)** — a girl who dies in an **outhouse** reciting a
   number sequence (`1237645112…`). A "disconnected thread" the user flagged — same *outhouse + numbers* motif. Her opening
   numbers are **RDR2-original and confirmed deliberate** (Rockstar later echoed them cross-game via **Madam Nazar** in
   GTA Online, [K23]) — so they're a genuine cipher-candidate, though their link to the *spider* trail specifically is still
   undecided. See the [GTA↔RDR2 crossover dossier](analysis/gta-rdr2-crossover.md).
5. **[The Spider Web trail](threads/05-spider-web-trail-2025.md)** — the spider engraving, **8 webs** (5 black / 3 red
   feathers) + a centre web marked **`N`**, and a directional puzzle (N → W×5 → NW + guitar) toward Fort Wallace / Spider Gorge.
6. **[The bird carving → Calumet → the Giant](threads/06-bird-carving-giant-wapiti.md)** — your NW/Wapiti lead: the Fort
   Wallace bird symbols, the flock to the Giant (30-animals gate), and the (debunked) "Birds of Paradise plants."
7. **[Van der Linde gang roster](threads/07-van-der-linde-roster.md)** — the full gang roster · fates · graves; doubles
   as the in-fiction name list for testing the letter markings (`SM`=Sean MacGuire, `J+M`=John Marston hits, [S16]).
8. **[Francis Sinclair / "Geology for Beginners" mural](threads/08-francis-sinclair-mural.md)** — a **separate**,
   well-documented time-traveller egg with **no verified spider link**; watched because one of its rock carvings sits
   NE of Fort Wallace, inside the frontier cluster ([K33]).
9. **[Mount Shann sundial](threads/09-mount-shann-sundial.md)** — a **separate** mystery (stone-circle sundial with 7
   painted arrows + a ~2 AM UFO); only bridge to us is the shared GTA V Mount Chiliad nod ([K38]/[K24]). Held skeptical.

See **[analysis/connections.md](analysis/connections.md)** for the letter/number cross-links,
**[carving-technique.md](analysis/carving-technique.md)** for the real-carving-vs-pareidolia test, and
**[narrative-connection.md](analysis/narrative-connection.md)** for the Rains Fall / Eagle Flies tie.

---

## One-paragraph summary of the current best understanding

Butcher Creek's outhouse pentagram and carvings (`LJ`, `SM`, Fort Brennand symbol) are the deliberate start of a clue chain.
Fort Brennand's tower carries three more symbols (a telephone pole, a factory, an oil puddle) that point onward. They lead to
a **spider carving on a telephone pole near Cornwall Kerosene & Tar**, visible only at a specific night hour; that engraving
maps the locations of **7 more webs** (each with a feather, time-locked to different hours) plus a central set of webs (1–2 AM,
no feathers) that line up to spell **`N`** + a telephone pole. Going **north** and shooting the indicated pole reveals an
inscription **`W ✞✞✞✞✞`** (= five poles **west**; the "crosses" are telephone-pole glyphs); five poles west, another pole
reveals **`NW`** + a symbol **believed to be a guitar** — pointing to **Fort Wallace** (which holds **two guitars**). Fort
Wallace is a **waypoint, not the end** — but its **bird carvings are the last *verified* clue**. Past them the trail runs into
**contested** leads (Calumet Ravine / the Giant's birds, a **"?" carving** on an out-of-bounds mountain that is **widely judged
pareidolia, not an accepted theory**, and the empty **Bacchus Bridge heart** whose relevance is **about as contested as the
"?"**) where it currently goes cold; we work forward from the bird carvings. *(The wiki's **Spider Gorge** reading is
uncorroborated by any secondary source.)* There are **5 black + 3 red feathers** (files named *"spiderdream"*). Whether the matchstick
letters and Gertrude's numbers feed this same puzzle, and what the payoff is, remains **unconfirmed**.

> **Shipped precedents worth knowing.** Two *solved* RDR2 eggs use the same "connect fixed points → a deliberate shape → go to
> a specific point" grammar the spider trail uses: the **[Dreamcatchers](analysis/dreamcatchers.md)** (20 points → a drawn
> animal → the reward in its **eye**) and the **[Saint Denis Vampire](analysis/saint-denis-vampire.md)** (5 wall-writings →
> the journal **auto-draws a pentagram** → the Vampire at its **centre**). The Vampire is the **same pentagram-mapping puzzle
> as Butcher Creek**, but fully hand-held — reading it as the game's **tutorial / "seed"** for the technique ([H15]), with the
> whole chain then climbing a **difficulty curve** that strips the assistance away ([H16]).

---

## Quick-reference: key locations

| Location | Region | What's there |
|----------|--------|--------------|
| Butcher Creek | Roanoke Ridge (NE map) | 5 outhouses, tally-mark pentagram, `LJ`/`SM`/Fort Brennand carving on #4 |
| Fort Brennand | Roanoke Ridge | Tower: tally marks (6, 7) + 3 symbols (telephone pole, factory, oil puddle) |
| Cornwall Kerosene & Tar | near Annesburg, Roanoke Ridge | Telephone pole with the **spider engraving** — start of the web trail |
| Vetter's Echo | (cabin) | Matchsticks **`EC`** + Black Widow cigarette card + letters to Annabella |
| Heartland Oil Fields | The Heartlands, New Hanover | "KEEP YOUR DREAMS LIGHT" desk-drawer carving (relevance unconfirmed) |
| Braithwaite Manor | Scarlett Meadows, Lemoyne | Gertrude dies in the southern outhouse reciting numbers |
| Fort Wallace | Cumberland Forest | **Waypoint** at "NW + guitar" (two guitars); trail continues NW (Calumet / "?" frontier) |
| Spider Gorge | nr Grizzlies (Ambarino) | Wiki-only theory (NW "points to its tip"; guitar-shaped section) — **uncorroborated** |

---

*This is a living investigation. Update the dated log and re-tag claims as evidence changes.*

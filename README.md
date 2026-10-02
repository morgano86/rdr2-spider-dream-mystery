# RDR2 Spider Dream Mystery — a source-cited investigation

An open, evidence-graded investigation into the **Spider Dream Mystery** in *Red Dead Redemption 2* — an Easter egg that went undocumented for about seven years (the game shipped in October 2018; the trail resurfaced in late December 2025) — and the web of unsolved threads around it: the Butcher Creek outhouse carvings, the matchstick letters, Gertrude Braithwaite's numbers, and the 2025 "spider web" telegraph-pole trail.

This is a **research corpus, not software**: Markdown prose, downloaded images, and a handful of small Python scripts that test specific claims. The goal is a trustworthy, cross-linked record of **what is actually known, what is open, and what is only a theory** — kept honest enough that you can tell which is which at a glance.

## Where the case stands

> **Status (updated 2026-10-02): UNSOLVED — no confirmed reward, cutscene or unlock.** Coverage in January 2026 reported *"no new loot, tools, or cutscenes"*; vindication is the only payoff anyone has found.

- **Verified trail.** The community decoded the chain from the Butcher Creek pentagram → Fort Brennand's tower symbols → a spider engraving on a telephone pole near Cornwall Kerosene & Tar → 8 time-locked "webs" with feathers → pole inscriptions (`N`, `W ✞✞✞✞✞`, `NW` + a guitar) → **Fort Wallace**. At Fort Wallace the **bird carvings** are the **last verified clue**.
- **Past the birds is contested.** The Calumet / the Giant continuation, the off-map **`?` carving** (widely judged pareidolia) and the **Bacchus Bridge heart** are all unverified or disputed. This repo deliberately stops short of treating them as "the trail" — see [the verified-trail boundary](CLAUDE.md#the-verified-trail-boundary--do-not-chase-speculation-past-it-read-this-before-theorising).
- **The recent work is mostly deflationary — by design.** Reads of the shipped game data and decompiled scripts found no hidden order field in the feathers ([K46]/[K47]), showed the "respawn boundaries" are ordinary map-streaming extents ([K48]), proved that "all five black feathers visibly down at once" is geometrically impossible ([K49]), and found no script anywhere that touches the webs ([#87], [H27]) or any carving ([K63]). Negative results are logged as findings, not hidden.
- **Authorship is unconfirmed.** A former Rockstar QA tester publicly confirmed the egg is *real*, but not that he designed it ([K3]).

The live dashboard — ranked open questions and next actions — is [`STATUS.md`](STATUS.md).

## How to read this repo

| If you want… | Go to |
|---|---|
| A fast orientation to the whole mystery | [The threads at a glance](#the-threads-at-a-glance) below, then the [best current understanding](#the-best-current-understanding) |
| To know what's solid | [`findings/known-facts.md`](findings/known-facts.md) |
| To know what's open | [`findings/unknowns.md`](findings/unknowns.md) |
| The theories (and how well they hold up) | [`findings/speculation.md`](findings/speculation.md) |
| To decode the jargon (`K13`, `[#89]`, `H27`, "CodeX", "Test D"…) | [`GLOSSARY.md`](GLOSSARY.md) |
| To look up one claim by its ID | [`INDEX.md`](INDEX.md) |
| To check where a claim came from | [`sources/sources.md`](sources/sources.md) |
| What to do next / how to help | [`STATUS.md`](STATUS.md), [`EVIDENCE-CHECKLIST.md`](EVIDENCE-CHECKLIST.md), [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| The full chronology of how we got here | [`INVESTIGATION_LOG.md`](INVESTIGATION_LOG.md) (newest first) |

### The one rule: every claim is tagged

- **`[KNOWN]`** — verifiable in-game, or corroborated across multiple reliable sources.
- **`[UNKNOWN]`** — an open question.
- **`[SPECULATION]`** — a community or our own theory, not confirmed.

Sources are graded **A** (primary / in-game / official), **B** (established games journalism or a long-standing wiki) or **C** (forum / social / video — a lead to verify, never a fact). Nothing is promoted to a stronger tag without sourcing. Details in [`GLOSSARY.md`](GLOSSARY.md).

## What's in each folder

| Path | Purpose |
|---|---|
| [`threads/`](threads/) | One file per investigative thread (01–09) — the primary unit of detail. Each is split into KNOWN / UNKNOWN / SPECULATION. |
| [`findings/`](findings/) | Cross-thread rollups: [known facts](findings/known-facts.md), [open questions](findings/unknowns.md), [speculation](findings/speculation.md). |
| [`analysis/`](analysis/) | Working theories and method notes — e.g. [carving technique vs pareidolia](analysis/carving-technique.md), [letter/number connections](analysis/connections.md), [solve grammar](analysis/solve-grammar.md), [the web-order field test](analysis/web-order-field-test.md), plus precedents: [Dreamcatchers](analysis/dreamcatchers.md), [Saint Denis Vampire](analysis/saint-denis-vampire.md), [GTA↔RDR2 crossover](analysis/gta-rdr2-crossover.md). |
| [`locations/`](locations/) | A dossier per place the mystery touches ([index](locations/README.md)). |
| [`experiments/`](experiments/) | Small, deterministic Python scripts that *test* claims (ciphers, combinatorics, geometry, likelihoods). Results are evidence, not fact. See [`experiments/README.md`](experiments/README.md). |
| [`sources/`](sources/) | The [per-claim source ledger](sources/sources.md), a [resource directory with fetch recipes](sources/RESOURCES.md), the saved [primary wiki text](sources/PRIMARY-wiki-spider-dream.md), raw API data, and verbatim game-file / script readouts. |
| [`images/`](images/) | Screenshots and maps, foldered by location. Provenance in [`images/README.md`](images/README.md); the [webs manifest](images/webs/WEBS-MANIFEST.md) catalogues all 8 webs. |
| [`tools/`](tools/) | Housekeeping scripts (Markdown formatting). |

---

## The threads at a glance

1. **[Spider Dream Mystery](threads/01-spider-dream.md)** — the named, wiki-documented mystery; the hub the other threads feed into.
2. **[Butcher Creek outhouse carvings](threads/02-butcher-creek-carvings.md)** — five outhouses with tally marks that form a pentagram; outhouse #4 also carries **`LJ`**, **`SM`** and a **Fort Brennand** symbol.
3. **[Matchstick letters](threads/03-matchstick-letters.md)** — match arrangements across the map spelling **`EC`** (by the Black Widow card at Vetter's Echo), **`J+M`**, **`S+J`** and an arrow; plus the oil-field **"KEEP YOUR DREAMS LIGHT"** carving.
4. **[Gertrude Braithwaite's numbers](threads/04-gertrude-numbers.md)** — a girl who dies in an outhouse reciting a number sequence (`1237645112…`). The opening is RDR2-original and deliberate (Rockstar later echoed it via Madam Nazar in GTA Online, [K23]); its link to the spider trail is undecided. See the [crossover dossier](analysis/gta-rdr2-crossover.md).
5. **[The spider web trail (2025)](threads/05-spider-web-trail-2025.md)** — the spider engraving, **8 feathered webs** (5 black / 3 red) plus a centre web marked **`N`**, and a directional puzzle toward Fort Wallace.
6. **[The bird carving → Calumet → the Giant](threads/06-bird-carving-giant-wapiti.md)** — the Fort Wallace bird symbols, the flock that leads to the Giant, and the (debunked) "Birds of Paradise plants". *Past the birds is contested.*
7. **[Van der Linde gang roster](threads/07-van-der-linde-roster.md)** — the full gang list, doubling as an in-fiction name list for testing the letter markings.
8. **[Francis Sinclair / "Geology for Beginners" mural](threads/08-francis-sinclair-mural.md)** — a **separate**, well-documented time-traveller egg with **no verified spider link**; watched because one of its carvings sits near Fort Wallace.
9. **[Mount Shann sundial](threads/09-mount-shann-sundial.md)** — a **separate** mystery (stone-circle sundial with 7 painted arrows, plus a ~2 AM UFO); only bridge is a shared GTA V nod. Held skeptical.

### The best current understanding

Butcher Creek's outhouse pentagram and carvings (`LJ`, `SM`, a Fort Brennand symbol) are the deliberate start of a clue chain. Fort Brennand's tower carries three more symbols (a telephone pole, a factory, an oil puddle) that point onward to a **spider carving on a telephone pole near Cornwall Kerosene & Tar**, visible only at a specific night hour. That engraving maps **7 more webs** (each with a feather, time-locked to a different hour) plus a central set of webs (1–2 AM, no feathers) that line up to spell **`N`** + a telephone pole. Going north and shooting the indicated pole reveals **`W ✞✞✞✞✞`** (five poles west; the "crosses" are telephone-pole glyphs); five poles west, another pole reveals **`NW`** and a symbol **believed to be a guitar**, pointing to **Fort Wallace** (which holds two guitars). Fort Wallace is a **waypoint, not the end** — its bird carvings are the last verified clue, and past them the trail goes cold in contested territory. There are **5 black + 3 red feathers**, in game files named *"spiderdream"*. Whether the matchstick letters and Gertrude's numbers feed this same puzzle, and whether there is any payoff at all, remains **unconfirmed**.

> **Shipped precedents.** Two *solved* RDR2 eggs use the same "connect fixed points → a deliberate shape → go to a specific point" grammar: the **[Dreamcatchers](analysis/dreamcatchers.md)** (20 points → a drawn animal → the reward in its eye) and the **[Saint Denis Vampire](analysis/saint-denis-vampire.md)** (5 wall-writings → an auto-drawn pentagram → the Vampire at its centre). The Vampire is the same pentagram-mapping puzzle as Butcher Creek, but fully hand-held.

## Key locations

| Location | Region | What's there |
|---|---|---|
| Butcher Creek | Roanoke Ridge | 5 outhouses, tally-mark pentagram, `LJ`/`SM`/Fort Brennand carving on #4 |
| Fort Brennand | Roanoke Ridge | Tower: tally marks (6, 7) + 3 symbols (telephone pole, factory, oil puddle) |
| Cornwall Kerosene & Tar | near Annesburg | Telephone pole with the **spider engraving** — start of the web trail |
| Vetter's Echo | cabin | Matchsticks **`EC`**, a Black Widow cigarette card, letters to Annabella |
| Heartland Oil Fields | The Heartlands | "KEEP YOUR DREAMS LIGHT" desk-drawer carving (relevance unconfirmed) |
| Braithwaite Manor | Scarlett Meadows | Gertrude dies in the southern outhouse reciting numbers |
| Fort Wallace | Cumberland Forest | **Waypoint** at "NW + guitar"; bird carvings = last verified clue |
| Spider Gorge | near Grizzlies | Wiki-only theory (guitar-shaped section) — **uncorroborated** |

Every location has a dossier in [`locations/`](locations/README.md).

---

## Notes on provenance and rights

- This project is an independent fan investigation and is **not affiliated with or endorsed by Rockstar Games or Take-Two Interactive**. *Red Dead Redemption 2* and its assets are © Rockstar Games; screenshots and short excerpts are used for commentary and research.
- Community wiki text saved under [`sources/`](sources/) comes from the Red Dead Wiki on Fandom (CC BY-SA) and is attributed in-file; community posts and videos are cited by source and graded **C**.
- Some findings rest on data read from a legitimately installed copy of the game (archives and decompiled scripts) using the investigator's own tooling, and on public third-party script dumps; each is labelled with how it was obtained in [`sources/sources.md`](sources/sources.md).
- `CLAUDE.md` holds the working rules for the AI assistant used on this project; the same rules are summarised for human contributors in [`CONTRIBUTING.md`](CONTRIBUTING.md).

*This is a living investigation. Claims are re-tagged as evidence changes, and the history is kept rather than erased.*

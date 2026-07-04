# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **research investigation**, not software. Every file is Markdown prose or a downloaded image documenting the
*Spider Dream Mystery* in Red Dead Redemption 2 and its connected threads. There is no build, test, lint, or run
step — "working in this repo" means reading sources, verifying claims, and editing Markdown while preserving the
editorial discipline below. The deliverable is a trustworthy, cross-linked, source-cited corpus.

## Editorial discipline (the core invariant)

Every factual claim is tagged so a reader can tell knowledge from guessing. **Do not state anything untagged, and
do not promote a claim to a stronger tag without sourcing it.**

- `[KNOWN]` — verifiable in-game or corroborated across multiple reliable sources.
- `[UNKNOWN]` — an open question.
- `[SPECULATION]` — a community or our own theory, not confirmed.

Thread files (`threads/`) are physically organized into `[KNOWN]` / `[UNKNOWN]` / `[SPECULATION]` sections — keep
new content in the right section. When evidence changes a claim's status, **move it** (e.g. demote a shaky known
fact to `unknowns.md` with a note) rather than silently editing in place.

### Source reliability legend (used in `sources/sources.md`)
- **A** = primary / in-game / official.
- **B** = established games journalism or a long-standing wiki.
- **C** = forum / social / video — useful *leads*, verify before trusting.

Cite the strongest tier available and never let a C-tier lead masquerade as a fact. The primary authority is
[`sources/PRIMARY-wiki-spider-dream.md`](sources/PRIMARY-wiki-spider-dream.md); corrections it forces supersede
earlier secondary-source passes.

### The verified-trail boundary — do NOT chase speculation past it (read this before theorising)

The trail has a hard line between what is **verified** and what is **contested**, and previous sessions have repeatedly
burned effort treating downstream community guesses (and users relaying them) as established steps — the classic failure
mode is "the `?` carving leads to a hidden loft/reward." **Hold this line:**

- **The Fort Wallace bird carvings ([K16]) are the LAST verified clue.** They pass the
  [carving test](analysis/carving-technique.md) (hidden-geometry technique). Everything *up to and including* the birds is
  sourced; **everything past them is not.** Treat the bird carvings as the working **frontier** — build forward from there.
- **Past the birds is contested, not "the trail."** The Calumet/Giant continuation, the off-map **`?` carving**, and the
  **Bacchus Bridge heart's relevance** are all **unverified or disputed**:
  - The **`?` carving is widely judged pareidolia** (no named asset, not time-gated, visible only in distant out-of-bounds
    mountain noise, doesn't reproducibly point onward) and is **NOT a widely accepted theory.** Do not present it as a
    destination or build a chain on top of it.
  - The **Bacchus heart exists** (firsthand investigator data, [K22]) — that is not in doubt — but whether it has **anything
    to do with the spider mystery is as contested as the `?`.** Don't present it as an established next step.
- **A user asserting a downstream claim is not sourcing it.** Users can (and in this case sometimes do) relay **incorrect
  community speculation as fact.** Firsthand *in-game observations* are still high-trust investigator data (record them as
  such); but a downstream *theory/interpretation* a user repeats is a **tagged `[SPECULATION]` lead**, promotable only by the
  normal tier rules — never silently elevated because the user believes it.
- **Why this rule exists:** the case is **UNSOLVED with no confirmed payoff** ([U2]); the strongest pull toward false
  confidence is exactly these post-Fort-Wallace theories. When in doubt, stay on the disciplined side of [K16] and say so.

## How the corpus fits together

**The spine (read/maintain these first):**
- **`STATUS.md`** — the live dashboard and session entry point: current status, ranked open questions, next actions by
  channel (🎮 in-game / 🌐 web / 🧠 analysis). Holds pointers, not content — update it when the frontier moves.
- **`INDEX.md`** — the ID registry: every `K`/`U`/`H`/`S` claim with its status and **canonical home**. This is the
  lookup that makes the "update every place an ID appears" rule tractable. **Append a row whenever you mint a new ID.**
- **`EVIDENCE-CHECKLIST.md`** — the evidence worklist, ordered by value. **Default to web/video sourcing + verification**
  (wiki, community sites, forum threads, the Strange Man video); reserve in-game capture for detail no online source
  records (in practice, only feather *orientation*). Don't ask for an in-game screenshot when a verifiable web image exists.

**The corpus:**
- **`threads/01–09`** — one investigative thread each; the primary unit of detail. (07–09 are adjacent context: the
  gang-roster name list and two **separate** eggs — Francis Sinclair, Mount Shann — held at the boundary, not trail steps.)
- **`findings/`** — cross-thread rollups (`known-facts.md`, `unknowns.md`, `speculation.md`). These **aggregate**
  the threads, so they must stay in sync: a fact stated in a thread should be reflected here and vice-versa.
- **`analysis/`** — working theories (letter/number connections, carving-vs-pareidolia test, narrative tie, cheat codes).
- **`experiments/`** — the one place we run **code instead of prose**: small Python scripts that *test* findings when the
  question is combinatorial/cipher/geometry/likelihood and reasoning isn't enough. See [`experiments/README.md`](experiments/README.md).
- **`locations/`** — one dossier per place the mystery touches; `locations/README.md` is the index.
- **`sources/`** — the source list + saved primary wiki text and raw API JSON.
- **`images/`** — screenshots/maps foldered by location; provenance in `images/README.md`. The
  [`images/webs/WEBS-MANIFEST.md`](images/webs/WEBS-MANIFEST.md) catalogues the 8 webs (location · time · feather colour · position).
- **`README.md`** — overview, map of the mystery, current status.
- **`INVESTIGATION_LOG.md`** — chronological log; **newest entries at the top.**

### Stable IDs and cross-links
Facts carry stable IDs (`K1`, `K13a`…), unknowns `U#`, hypotheses `H#`, speculation `S#`. When you reference, supersede,
or correct a claim, use its ID and update **every** place it appears (the thread, the findings rollup, any analysis file,
`README.md`'s summary, the locations index, **and the `INDEX.md` row**). IDs are **append-only** — never recycle a number.
`INDEX.md` tells you which file owns each ID; start your edit there. Links are relative Markdown paths — preserve them.
**Rollups must be complete:** every `H#`/`S#` belongs in `findings/speculation.md`, every `K#` in `findings/known-facts.md`,
every `U#` in `findings/unknowns.md` — even when the detailed write-up lives in an `analysis/` file.

## Working norms

- **Log every working session** at the top of `INVESTIGATION_LOG.md`: what you did, what you learned, what changed.
- **Convert relative dates to absolute** (this repo dates entries explicitly, e.g. `2026-06-13`).
- **Firsthand investigator data** (the user's in-game observations) is recorded as high-trust even when web search
  can't corroborate it — label it as investigator data with the date, don't discard it for lacking an online source.
- When you adversarially refute a claim, **say so and soften the wording** rather than deleting the history (see how
  the "Adam Butterworth confirmed intent" claim was walked back to "a dev commented" in `findings/known-facts.md`).
- **Test with code when reasoning isn't enough.** For combinatorial/cipher/geometry/likelihood questions (feather order,
  Gertrude's number ciphers, dev-initials coincidence odds, name-list matching), write a small Python script in
  `experiments/` rather than hand-waving. **A script tests, it doesn't establish fact:** a positive result is
  **[SPECULATION]** until sourced; a *negative* result is a real finding worth logging. Never feed a script invented
  data, mark provisional inputs, and keep it reproducible (stdlib, deterministic). Full conventions in
  [`experiments/README.md`](experiments/README.md).

## Source-fetch gotchas

- `fandom.com` and `gtaforums.com` return **HTTP 403** to automated fetch. For Fandom, use the **MediaWiki API**
  (`action=parse`) instead of fetching the page — that is how `sources/PRIMARY-wiki-spider-dream.md` was obtained.
  For pages with no API, browse manually and paste verbatim excerpts, citing the source number in `sources/sources.md`.
- Wiki images are downloadable directly from the CDN (`static.wikia.nocookie.net`); record provenance in `images/README.md`.
- `reddit.com` **403s our fetcher** — the site, `old.reddit.com`, and the `.json` API all block it (an **egress-IP** block, so
  User-Agent spoofing won't help; `WebFetch` also can't reach reddit.com). Use the **Arctic Shift** mirror
  (`arctic-shift.photon-reddit.com/api`), which is not blocked: `/posts/search?subreddit=SUB&query=Q` to find posts (a
  `subreddit` is required — site-wide search 400s), `/posts/ids?ids=…` for full detail. The **`i.redd.it` image CDN is
  reachable**, so download images straight from each post's `url`. Reddit is C-tier — corroborate before trusting. Full recipe:
  [`sources/RESOURCES.md`](sources/RESOURCES.md#access-cookbook-the-fetch-recipes-that-actually-work). *(This is how the `J+M`/`S+J`
  matchstick images were acquired, 2026-06-13.)*

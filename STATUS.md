# STATUS — start here

The operational dashboard. **This is the single entry point each session**: where the case stands, what's blocked on
what, and what to do next. It holds *pointers and the live frontier*, not content — detail lives in the files it links.
Keep it short; when something changes here, also touch the canonical file and the [log](INVESTIGATION_LOG.md).

> **One-line status (2026-06-13):** **UNSOLVED — no confirmed reward/cutscene/unlock** (Jan 2026 coverage: *"no new loot,
> tools, or cutscenes"*). The community decoded the web-trail to **Fort Wallace** in late 2025; Fort Wallace is a
> **waypoint, not the end**. The **last VERIFIED clue is the Fort Wallace bird carvings** ([K16]); everything past them is
> unverified/contested — the off-map **"?" carving is NOT a widely accepted theory** (pareidolia), and the **Bacchus heart's
> relevance is about as contested as the "?"**. We work **forward from the bird carvings** unless new evidence lands. The egg
> is confirmed *real* by a former Rockstar QA tester ([K3](INDEX.md)), but authorship is unconfirmed.

- **Best one-paragraph understanding:** see [README.md](README.md#one-paragraph-summary-of-the-current-best-understanding).
- **Last verified clue / working frontier:** the **Fort Wallace bird carvings** ([K16]) → [thread 06](threads/06-bird-carving-giant-wapiti.md);
  glyph referent/symbolism deep-dive → [fort-wallace-bird-carving.md](analysis/fort-wallace-bird-carving.md) ([S24] eagles/"Eagle
  Flies", *symbolism only — place-check negative* / [S25] label-not-cipher / [H23] the birds pattern with the verified
  **static-carving class** — non-time-gating is shared by all wood carvings, ⚠️ not distinguishing).
  Past them (Calumet / Giant / "?" / Bacchus heart) is **contested**, not the established trail.

---

## Top open questions (ranked)
Full set + IDs in [findings/unknowns.md](findings/unknowns.md). The ones that could break the case open:

| Rank | ID | Question | Best source |
|------|----|----------|-------------|
| 1 | [U29](findings/unknowns.md) | The **feather order mechanic**. Within-group orders are solved (reds any-order; connector chain; `B34` folds into the black run — [H22]); the open crux is the **cross-boundary COMBINE** ([K29] boundary-exit reset vs [H20] multi-night) — and whether **shooting is the input at all**. Three live frames, run cheapest-first: **[H27]** webs = witness/READ layer → **Test D** (no shots); **[H24]** reds = decoys, solve = 5 blacks over ~2 nights + the [H25] dream coda → **Test C**; **[H22]** seam battery (R1/R2/R3) → **Tests A/B**. Protocols: [web-order-field-test.md](analysis/web-order-field-test.md); how the frames evolved: the [log](INVESTIGATION_LOG.md) | 🎮 targeted test / 🌐 |
| 2 | [U2](findings/unknowns.md) | Is there an **intended payoff at all**, or is it cut content? | 🌐 new coverage / community |
| 3 | [U6](findings/unknowns.md) | **Gertrude's numbers** — the opening is deliberate ([K23]) and the **complete 12-line set is now GAME-TEXT CONFIRMED** ([K42], 2026-07-05 — a 2019 subtitle dump, [#78]: tail settled, "eleven" parse settled, both L2/L7 tail variants real, no hidden extra set); attempt B (tally-node reorder) **closed-inexecutable** (nodes 5/6 bare, [#81]); [K41] interior closed-negative; **battery re-run DONE on the canonical set (2026-07-05): [S42] statistically supported on A-tier data** (attempts cap at 5; global additive p = 0.335; line-A `3,5,8,13` suggestive-not-significant, B-take breaks it). Open: what (if anything) the deliberate *opening* string encodes, and **which mystery it serves** — a 🌐 watch + desk question now, not a battery | 🌐 / 🧠 |

> **Note (2026-07-04):** [U3] (one puzzle or two?) **left the top-3 — REFRAMED / PARTLY DECIDED** ([S41],
> [one-puzzle-or-two.md](analysis/one-puzzle-or-two.md)): the 2018 chain and the 2025 trail adjudicate to **one
> continuous designed relay** ([K8] hand-off retro-validated; shared Oil-Fields node; shared signature; both base-game).
> Its live residue is already tracked elsewhere — the mechanic layer at [U29] (rank 1) and satellite membership at [U6]
> (promoted to rank 3, replacing it).

> **Adjacent-egg watch-items (NOT trail steps — boundary discipline):**
> **(1) Francis Sinclair / "Geology for Beginners"** ([K32]–[K34], [thread 08](threads/08-francis-sinclair-mural.md)) — a
> separate, well-documented "time-traveller" egg with **no verified spider link**; touches us only via geography (a winged
> rock carving NE of Fort Wallace, in the frontier cluster — [K33]/[S26]). Open: mural-as-puzzle/payoff ([U31], deflated —
> HQ mural on file, close-crop pass negative).
> **(2) Mount Shann "giant sundial"** ([K35]–[K38], [thread 09](threads/09-mount-shann-sundial.md)) — stone-circle sundial
> with 7 red/orange/yellow arrows ([K36]) + a ~2 AM UFO ([K37]); **no verified spider link** — only the shared GTA V
> Chiliad nod ([K38]/[K24]) + a ~2 AM gate. Held skeptical ([U34]); the decode branch is closed-negative ([U33]).

---

## Next actions, by channel
**Default to web sourcing + verification.** Most open questions are already documented in the wiki, community sites,
forum threads, or the Strange Man video — find the evidence and corroborate it. Reserve in-game capture for detail no
online source records.

### 🌐 Web / video sourcing (the default) → [EVIDENCE-CHECKLIST.md](EVIDENCE-CHECKLIST.md)
The actionable worklist, ordered by value. Current headline item: a clean **arrow-set image** (Old Trail Rise) —
deprioritised, so the web tier is effectively **watch-mode** (new coverage on [U2], community movement past [K16]).
*(2026-07-05 cleared the rest: [K42] game-text confirm, attempt-B closed-negative ([#81]), dreamcatcher animal + Fort
Brennand counts, and now **[U9] resolved** — 8 pole-webs + a centre web in a **tree**, not "9 poles"; byproduct: [K40]
independently corroborated in print (#10). See the checklist's Completed section.)*

### 🎮 In-game (only when strictly necessary)
Run cheapest-first. **Full step-by-step protocols (confound controls + decision tables) live in
[analysis/web-order-field-test.md](analysis/web-order-field-test.md) — follow that file in-game, not this summary.**
- **⚡ 1. Test D — the witness-only tour ([H27], NO shots).** Visit all 8 webs at their hours + the 1–2 AM centre, force
  each spawn with the look-away trick ([K30]), fire nothing, finish with the [H25] dream coda at the whiskey tree. Under
  [H27] (webs = a READ layer — [solve-grammar.md](analysis/solve-grammar.md)) this is the *complete* candidate solve; it
  leaves no state to corrupt, so running it first costs nothing.
- **⚡ 2. Test C — the blacks-only solve + dream coda ([H24]/[H25], ~2 nights).** Night 1: `B23→B45→B56→BL56` staying in
  yellow; hold state through the day ([K29]). Night 2: `B34` at 3–4 AM from the overlap (geometry forces `BL56` before
  `B34`). **Never touch a red.** Camp at the whiskey tree ([S23]) and **sleep at dawn** ([H25] — dry-check [#67]: no
  documented solver has ever slept on a completed set). Companion red-side session ([S35]): solve the 3 reds, stay in
  South, walk into the **Strange Man's shack** with state live — baseline dossier + checklist:
  [locations/strange-man-shack.md](locations/strange-man-shack.md) (no-state baseline visit first; gate caveat [U35]).
- **🔑 3. Tests A/B — the cross-boundary STATE battery ([H22]/[U29]).** Discriminates the three exits at the RED↔BLACK
  seam (R1 overlap-holds / R2 hidden-flag / R3 no-combine); reasoning in
  [`web_boundary_solve_protocol.py`](experiments/web_boundary_solve_protocol.py).
- **🆕 Letter-sweep ([H26]) — cheap, combinable with any web session.** Sweep for undiscovered letter-pairs with the
  [K15] viewing discipline (odd angles, changing light, moss/wood seams): Fort Brennand tower + outhouses, the 8 web
  pole sites (esp. Cornwall's START pole), the Fort Wallace walls around the birds [K16]. Log a careful negative too.
- **🆕 Persistence CONTROL ([S36], cheap):** shoot/displace a comparable ambient object far from any web and sleep
  several nights in place — tests whether the feathers' [K29] persistence is genuinely special.
- Residuals: feather *attachment* detail ([U0], deflated) only if images fail; the long-horizon **[H8] test** (does
  completing the trail clear the dreamcatcher log?).

### 🧠 Analysis (desk work, no sourcing needed)
From [analysis/connections.md](analysis/connections.md#open-analysis-tasks):
- ~~Re-run [`gertrude_tail_structure.py`](experiments/gertrude_tail_structure.py) on the canonical [K42] 12-line
  inventory~~ — **DONE 2026-07-05**: [S42] survives on A-tier data (global additive p = 0.335); line-A `3,5,8,13` =
  suggestive-not-significant (~0.16 whole-line), deflationary lean; 🆕 fragment/windowing structure (thread 04).
- ~~Test Gertrude attempt B (read the 7 tally nodes in her number order) once U6 lands.~~ **CLOSED-INEXECUTABLE
  2026-07-05** (nodes 5/6 bare — [connections §3](analysis/connections.md); reopens only via an [H26]-sweep find).
- Re-pair the letters `{C,E,J,J,J,L,M,M,S,S}` against candidate name lists. *(Dev-initials: **CLOSED as a working line
  2026-07-02** — counts + coherence + placement; see [connections §1](analysis/connections.md). Newest frame: [H26] waymarks.)*
- ~~Decide [U3]: one layered puzzle or two parallel eggs?~~ **DONE 2026-07-04 → [S41]** (one relay;
  [one-puzzle-or-two.md](analysis/one-puzzle-or-two.md)).
- Live [U29] follow-ons: does shooting a *contained-but-untied* web (wrong-boundary despawn) break a run? And **[U30]** —
  does a hit count whenever the feather is shot while visible, or only during its spawn hour?

> **🧮 When reasoning isn't enough** (combinations, ciphers, geometry, coincidence odds), write a quick Python test in
> [`experiments/`](experiments/) — e.g. [`feather_order.py`](experiments/feather_order.py). Results are evidence, not
> fact; log null results too.

---

## Session headlines (newest first)
One line per session — **the full entries live in [INVESTIGATION_LOG.md](INVESTIGATION_LOG.md)** (newest at top).

- **2026-07-05 (battery re-run + U9)** — **[S42] statistically supported on the canonical [K42] set** (attempts cap at
  5; global additive p = 0.335; line-A `3,5,8,13` suggestive-not-significant — ~0.16 whole-line, B-take breaks it;
  🆕 the 12 lines = windows on one VO babble stream); **[U9] resolved** (8 pole-webs + the centre web in a **TREE**
  per #8/#10 — not "9 poles"; ≠ whiskey tree on current data); **[K40] corroborated in print** (#10 "two feathers");
  watch pass quiet (Dexerto mesh-cables + NW-as-dev already held; Arctic Shift 0 new posts since 07-04).
- **2026-07-05 (parallel desk sweep)** — **⭐ [K42] minted: Gertrude's full 12-line recitation set confirmed from the
  game's own subtitle text** (2019 GitHub dump [#78], independently verified at the pinned commit — tail settled,
  "eleven" settled, L2/L7 fork decided *both-real*, no hidden extra set; battery re-run queued); **attempt B
  closed-inexecutable** (per-node sweep [#81]: nodes 5/6 bare; [S43] bottles + [S44] skyline minted; [U10] counts
  B×2-confirmed); dreamcatcher animal = **buffalo/bison at consensus level** ([#82]; wiki names only the cave painting;
  [H6] community-echoed via [#53]); **canonical Strange Man corpus pinned** ([#80], 7 dated videos + April-Fools
  flag; [#17]/[#18] corrected — both are Strange Man's own); July Reddit sweep quiet (bird-rock lead self-debunked by
  CodeX — the community applying our carving test; GTA-V-beta third-web watch-item logged).
- **2026-07-04 (repo hygiene 2)** — commit-every-session norm codified in CLAUDE.md (after a 3-week uncommitted
  backlog was found + committed); `.gitattributes` added; INDEX rows slimmed to true one-liners (audit-verified
  lossless; H8's [#66] note back-filled to the rollup); STATUS rank-1/-3 cells de-accreted.
- **2026-07-04 (U6 structure battery)** — **[S42] statistically supported**: new exact-null experiment
  ([`gertrude_tail_structure.py`](experiments/gertrude_tail_structure.py)) on the provisional 9-line tail — prefixes
  capped at 5, post-derail re-rail runs, tails' additive structure = chance (p 0.44); **lone fragile counter-flag** =
  the L2-only Fibonacci chain `3,5,8,13` (p 0.039), which collapses under the L7 parse → **clean-audio confirm priority
  raised** (it decides the fork); L1≈L6/L2≈L7 near-dup template structure found (least-reliable tokens identified); one
  audio-dump route (Tumblr compilation) checked negative. No decode attempted — the tail-cipher gate stands.
- **2026-07-04 (U6 sourcing pass)** — **Gertrude tail transcription RECOVERED** (9 sequences, max 29, no identical loop —
  from StrangeMan's own frames via the [#43] exposé, **fully captured** through the 🆕 Fandom Discussions API recipe);
  StrangeMan's Gertrude video **rated hoax-leaning** (5-point refutation incl. the manor family-photo counter-evidence);
  **[K41]** outhouse-interior negative + **[S42]** failed-counting reading minted; Nazar number primary-sourced ([#75]:
  callable `123-764-5112`); 4 images filed to `images/gertrude/`. *(Arctic Shift under maintenance today.)*
- **2026-07-04 (U3 adjudication)** — **[U3] decided-in-part → [S41]:** the 2018 chain + 2025 trail = **one designed
  relay** (K8 hand-off retro-validated; "parallel eggs" rejected); residue routed to [U29] (mechanic) + [U6]/matchsticks
  (satellites); U6 promoted into the top-3.
- **2026-07-04 (later)** — All 8 feather-position fronts **re-shot firsthand (PS5 4K)** and swapped in file-for-file;
  socket reads re-verified 8/8, all high-confidence (Scarlett resolves to `R`); image set upgraded C-tier → firsthand.
- **2026-07-04** — **[K40]** minted: every web feather is **DOUBLED** (main + smaller secondary at one socket, all 8
  webs) — uniform model feature, **no order/count signal**; capture caveat recorded; 3 superseded web images removed.
- **2026-07-03** — [K13] corrected: the 5 "black" feathers are **two-toned** (white/grey ↔ black); GameRant's "white"
  reconciled rather than dismissed.
- **2026-07-02 (Reddit sweep)** — 358 posts triaged (Jan–Jun 2026, Arctic Shift): the [#52] datamine **fully recovered**
  (zero `spiderdream` refs in 1,639 scripts → strongest desk evidence for [H27]); boundary map has a **public source**
  ([#69], provenance corrected); **[S39]** two-object model + **[S40]** Fort Riggs minted; Test C prior-art bounded ([#71]).
- **2026-07-02 (analysis-only)** — **[S38]** file-numbers-as-order tested negative-leaning (index, not sequence);
  **[U33]** sundial decode closed-negative; **[H27]** witness/READ-layer hypothesis minted + **Test D** written.
- **2026-07-02 (desk sourcing)** — **[U32] → [K39]**: per-web `spiderdream0X` mapping publicly sourced ([#65], 8/8 match;
  [S29] activated); **[H25] dry-check passed** ([#67]: no documented complete-set + sleep test); Strange Man shack
  dossier built ([#68], [U35] minted).
- **2026-07-02 (letters pass)** — **dev-initials CLOSED** as a working line (counts + coherence + placement); **[H26]**
  waymarks reading minted (→ the 🎮 letter-sweep); [S34] "rock → Rockstar" rival for the guitar glyph.
- **2026-07-02 (fresh-eyes pass)** — **[H24]** reds-as-decoys + **[H25]** payoff-is-a-DREAM minted → **Test C**;
  corrected same day (geometry forces `BL56` before `B34`, ~2 nights); [S34]/[S35] + unminted asides logged
  (home file: [decoy-and-dream-hypotheses.md](analysis/decoy-and-dream-hypotheses.md)).
- **2026-06-21** — **[S31]** the 8 web positions form a body-centred figure (Saint Denis the lone far leg, p=0.0001);
  **[S30]** the Cornwall engraving is a stylised spider, **not** a decodable bearing-map; [U32]/[S29] provenance audit
  minted; **[K3]** Butterworth credits-corroborated (source #62); the **web-order field-test protocol** written;
  Gertrude cipher battery → **null**; **[S28]** `EC`-as-key consolidation; **[U14] resolved-negative** (the mural is a
  single red pigment → [H3]/[S12] refuted).
- **2026-06-14** — **[H22]**: web order reframed to 3 solved sub-chains + an open cross-boundary COMBINE ([K29]
  contradicts [H20]); **[U1] RESOLVED** → [K11]/[K12] (deep-research [#60]: exactly 2 shot-poles, no 3rd documented);
  firsthand mechanics pass → **[K28]–[K31]** (I-beam boundaries, ≥12-day persistence, render-gating, membership
  confirmed); the **colour×hour lattice** + [H18] filter grammar; [H19] socket reads; [H20] multi-night; [S22]/[H21]
  B34 state-carry; CLAUDE.md verified-trail guardrail codified.
- **2026-06-13** — Feather **orientation resolved** (tip-down → [H4] refuted) + order deflated to group-based ([U29]);
  Saint Denis Vampire precedent ([K27]/[H15]/[H16]); in-game map grids captured ([K26], per-cell reading negative);
  coordinate precedent [K25]/[H14]; letter-groups framework [H12] + "letters, not initials" ([U25]); thread 07 gang
  roster + name-match pass ([S16]–[S19]); Reddit mining ([K21] boundaries, [K22] Bacchus heart, [K23]/[K24] GTA
  crossover, [U24] Register Rock list); first feather captures filed.

## Recently resolved (don't re-litigate)
- **[U1] → [K11]/[K12]:** the under-pole chain verbatim, multiply corroborated; **exactly 2 shot-poles, no 3rd**. Guitar *meaning* open at [U12].
- **[U14] → resolved-negative:** the Window Rock mural is a **single red pigment** — no black/red split; codes by count + orientation → [H3]/[S12] refuted.
- **[U0] orientation:** all 8 feathers hang **tip-down by gravity** → [H4] refuted; only the weak socket residual survives ([H19]).
- **[U22] → [K31]:** web↔boundary membership firsthand-confirmed; boundaries overlap.
- **[U26] deflated:** in-game grids captured ([K26]) but the per-cell reading tests negative (Map 2 admits only `EC`); [H14] survives as a free plot only.
- **[U32] → [K39]:** the per-web file-number mapping is publicly sourced, not our back-fit.
- **[U8] → [K3]:** dev quote is **Adam Butterworth, ex-Rockstar QA** — confirms *real*, not *authored*.
- **[U13] downgraded:** **Spider Gorge** is wiki-only speculation; journalism points the marker at Fort Wallace.
- **[U17] reframed / [K20]:** the spider mystery has **no in-game log at all**; the lingering log entry is the **dreamcatchers'** ([H8] tests the link).

---

## Map of the spine
| File | Use it to… |
|------|-----------|
| [STATUS.md](STATUS.md) (this) | See where the case is and what's next. |
| [INDEX.md](INDEX.md) | Look up any **K/U/H/S ID** — its claim, status, and which file owns it (edit there). |
| [EVIDENCE-CHECKLIST.md](EVIDENCE-CHECKLIST.md) | Turn open questions into sourced evidence (web-first). |
| [README.md](README.md) | Onboarding: what the mystery is, the threads, the best-understanding paragraph. |
| [INVESTIGATION_LOG.md](INVESTIGATION_LOG.md) | Chronological record (newest at top). Log every session. |
| [sources/RESOURCES.md](sources/RESOURCES.md) | "Where do I go for what?" — the resource directory + fetch recipes (vs [sources.md](sources/sources.md), the per-claim ledger). |

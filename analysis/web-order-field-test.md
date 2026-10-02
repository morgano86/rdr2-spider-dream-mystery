# Field-test protocol - the cross-boundary STATE question ([U29]/[H22])

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**Status: method, not a claim.** This file mints no new IDs. It operationalises the [H22] reframing of the web-order problem into the **single in-game experiment that can actually move the case** - and it is written for the investigator to follow *during play*, because the reasoning currently lives only inside [`web_boundary_solve_protocol.py`](../experiments/web_boundary_solve_protocol.py)'s console output, which you cannot follow in the field. Everything an *outcome* would establish is [SPECULATION] until observed; a clean **negative** here is itself a real, loggable finding (CLAUDE.md). This sits **upstream of, and never past, the [K16] frontier** - it is about the verified web mechanic, not the contested `?`/Bacchus leads.

## Why this is the bottleneck (one paragraph)

Per [H22], the order is **not** an 8-feather sequence to brute-force. Taking the [K31] partition seriously, the *within-boundary* order is **already solved** on all three boundaries - South reds work in any order ([U29]); the Connector blacks are the [K13b] chain `B23→B45→B56→BL56`; and `B34` folds into the black run via the orange/yellow overlap, so the **5 blacks behave as one super-group** ([K31], stay **east** of the Cornwall pole). That leaves **exactly one hard thing**: the **RED↔BLACK crossing**. And right there, two firsthand facts **contradict** - [K29] says shot-state **resets the instant you leave a boundary**, while [H20] says a full solve **must span the two colour groups** (black + red in one night is solo-impossible). The whole case now hinges on **which of three things is true at that seam**, and they differ *only* in what you observe in-game:

| Exit | Claim | What it would mean |
|------|-------|--------------------|
| **R1** | the central **overlap holds** multi-boundary state | the one prior probe was incomplete; there *is* a way to carry both groups → re-run the combine using the overlap as the bridge |
| **R2** | a **hidden "group-done" flag** persists even though the visible feather resets | the visible respawn is cosmetic; the combine is real and **`B34` is the carrier** north → this is the **payoff path** |
| **R3** | there is **no global combine** | three independent mini-puzzles, no joint payoff → consistent with "no confirmed reward" ([U2]/[K20]); pushes [U3] toward *many* puzzles |

No amount of desk reasoning distinguishes these (I checked - the contradiction is data-blocked, not analysis-blocked). The tests below do, in **one to two play sessions**.

---

## Preconditions & confound controls (read BEFORE shooting anything)

These are the failure modes that would make any result uninterpretable. Control every one.

1. **Render-gating ([K30]).** A web won't spawn while you look straight at the spot, and won't despawn while held in view. → Approach each pole **at its spawn hour**, then **look away and back** to force the spawn; or keep line of sight the whole approach. **Never** stand waiting while staring at an empty spot and conclude "no web."
2. **Tied-vs-contained hazard ([K31]).** Boundaries overlap, so a boundary physically *contains* webs it is **not tied to**; shooting a contained-untied web fires the **wrong** boundary's despawn and corrupts the run. → Only shoot a web while you are inside **its tied** boundary. For `B34` specifically, **stay east of the Cornwall pole** (crossing west trips the Connector despawn).
3. **Fast-travel advances game time ([K29]/[U30])** (~+1 h to Valentine, ~+2 h to Butcher Creek) and can **overshoot** a spawn hour. → For any time-sensitive leg, **ride**, don't fast-travel. State itself survives camping / hotel sleep / fast-travel; it's only the *clock* that fast-travel disturbs.
4. **Spawn-hour visibility.** A feather can only be *checked* (down vs respawned) **during its hour window**. Plan re-checks for the right hour; "I didn't see it" outside the window proves nothing.
5. **[U30] hit-timing unknown.** It's not yet known whether a hit counts whenever the feather is shot-while-visible or only during its spawn hour. → To stay safe, **shoot every feather during its actual spawn hour**, so no result is voided later by this ambiguity.
6. **Define "leaving."** [K29] resets on **boundary exit**. Know each boundary's edges; track which boundary you are inside at the moment of every shot and every re-check. "I left" must mean *left that tied rectangle*, not merely *left the overlap*.
7. **🆕 NEVER save/reload mid-run - the "one-session rule" ([#70], C-tier, 2026-07-02).** A community save/reload test found reloading **wipes all held web state**; whether it also wipes *feather shot-state* is untested ([K29] used camping/hotels, never a reload). → Run every test in **one continuous session**; if the game must be saved, treat the run as void and restart rather than trusting post-reload state.
8. **🆕 Web-vs-feather ledger discipline ([S39]).** The web (visibility) and the feather (shot-state) are **two assets with separate rules** - a web still standing says nothing about its feather's state, and a persisted web's un-shot feather can vanish on its own clock. → Record web-visible and feather-state as **separate columns** at every check. Optional tools from the same cluster (C-tier, verify before relying on them): **looking away with active Dead Eye/Eagle Eye holds a web past its hour** (once per web), and a gaze-held slow walk-out to camping distance can bank a web overnight - useful slack for the tight 5–6 AM double, but don't let a held *web* be mistaken for held *feather state*.

The webs, hours, colours, and boundary membership to run all of this are in [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md); the boundary geometry (the I-beam, overlap near centre) is [K28].

---

## The minimal discriminating battery

Run **Test A first** (it's one session and cleanly settles R1). Its result tells you how to read **Test B**.

### Test A - does the overlap hold cross-boundary *visible* state? (settles **R1**)

*Goal: redo the prior negative-leaning probe **without its suspected flaw** - namely, with the entire group already down first.*

1. Solve the **RED group fully** - `R23`, `R34`, `R45`, any order ([U29]), across as many nights as needed, **staying inside the South boundary** the whole time so the reds stay down ([K29]). All three must be visibly **down**.
> **⚠️⚠️ TEST A IS NOW MOOT (2026-09-01, [K49]/[#89]) - do not spend a session on it.** It tests whether the **central triple overlap** holds cross-boundary visible state; the file extents show **there is no triple overlap**. The North and South ymap boxes are **disjoint** (10.50 m gap in Y), and only the Connector spine touches both - so **`B34` and any red can never be loaded at the same time**, and no standing spot exists from which a red set survives a crossing north. **R1 is settled NEGATIVE by geometry.** The steps below are retained for the record and because their *middle* section (does a fully-down red group survive a Connector crossing?) is still a valid, smaller question - but the "camp in the triple overlap" premise is void. **Go run Test D and the [H28] control instead.**

2. Move into the **central overlap** (camp at the **whiskey tree** [S23], the lone POI in the triple overlap [K28]) **without leaving South's tied rectangle en route.**
3. Cross from the overlap into the **Connector** to begin blacks - i.e. make the RED→BLACK crossing.
4. **Immediately** ride back to a red web at its spawn hour and check it.

| Observation | Reading |
|-------------|---------|
| reds **still down** after the crossing | **R1 supported** - the overlap carried state across boundaries; the prior probe was incomplete. Huge: re-attempt the full combine using the overlap as the bridge. |
| reds **respawned** (visible reset) | **R1 weakened** (now two independent negatives). Proceed to Test B for R2. |

*Control:* confirm at step 4 you are checking a **tied** red (South), not a contained-untied web; confirm you actually left South (not just the overlap). Do it in **one session** so no night-boundary confounds creep in.

### Test B - does a *hidden* flag persist despite visible reset? (settles **R2**; this is the payoff test)

*Goal: the favoured "reds-first, blacks-last, `B34` carries north" protocol - the one path that could surface an actual payoff.*

1. Solve the **RED group fully** (sets the putative hidden flag). Let the reds **visibly reset** by leaving/returning - under R2 that does **not** matter; the flag is invisible.
2. Solve the **BLACK super-group**: `B23 → B34 → B45 → B56 → BL56` (the [K13b] chain with `B34` interleaved via the overlap; `B56`/`BL56` interchangeable). **Stay east of the Cornwall pole** throughout (control #2).
3. End inside **`B34`'s oversized orange/North boundary** and **ride north - do not exit it** - into the zone it uniquely reaches: **Butcher Creek, Valentine, Fort Brennand** ([K28]/[S22]). `B34`'s state is held the whole ride (no crossing).
4. Watch for **any** new state-gated element along/at the end of that ride: a trigger, a new sound, a journal/log change, a changed **Butcher Creek pentagram** (be there ~4–5 AM, [K5]), a new interactable, a cutscene, anything that is not normally present.

| Observation | Reading |
|-------------|---------|
| **any** new element appears that isn't normally there | **R2 supported** - a hidden combine exists and this is the payoff corridor ([H21]). This would be the biggest result in the case since [K16]. Capture everything. |
| **nothing**, after a clean run of *both* meta-orders (also try blacks-first) and the plausible trigger sites | weak support for **R3** - but a null is **inconclusive** (could be wrong precondition/order), so log it as null, not as proof. |

### Test C - the blacks-only solve, `B34` last (settles [H24]; the CHEAPEST test on the board - run it first if short on time)

*Goal: test the 2026-07-02 fresh-pass reading ([H24]) that the 3 reds are **decoys** and the intended solve is the 5 blacks alone - in which case there is no RED↔BLACK seam at all and Tests A/B are testing a non-existent problem. ~2 nights, no red↔black crossing.*

> **⚠️ Geometry constraint (investigator correction, 2026-07-02) - why this is 2 nights, not 1.** The four northern blacks (`B34`, `B23`, `B45`, `B56`) all sit physically inside **both** the orange and yellow zones and can be shot + held together - but **`BL56` (Ringneck) lies outside the orange boundary**, in the yellow∩red overlap, so reaching it after shooting `B34` exits orange and **visibly resets `B34`**. The order constraint is therefore **`BL56` before `B34`**; and since BL56's hour (5–6) is after B34's (3–4), `B34` must fall on a **later night**. (Pleasing side-effect: the geometry *derives* the community's "B34 last" suspicion, [U29] - and note the [K13b] community chain already excludes `B34`.)

> **⚠️⚠️ SUPERSEDING CONSTRAINT (2026-09-01, [K49]/[#89]) - the 2-night plan cannot produce a visibly complete set.** The file extents show the real binding constraint is not orange-vs-yellow membership but that **`B34` sits 50 m WEST of the Connector ymap's streaming box**: riding to `B34` at all **unloads that ymap and re-streams `B23`/`B45`/`B56`/ `BL56` back into their webs.** **At most 6 feathers can be down at once, and never a set containing `B34`** - so "all 5 blacks visibly down" is impossible, on any night count. ⚠️ This also **explains the two published all-5-blacks-in-one-night completions that found nothing** ([#71]) without blaming their execution. **Test C is therefore no longer an [H24] test; it is a probe of [H22]-R2** (does an invisible flag count blacks as they are shot?). **Run it anyway** - it is still cheap, and the reset itself is data - but: expect the earlier blacks to be back up, **photograph each web on the way past to record exactly when they return**, and do not read a reset as having "broken the chain."

1. **Never shoot or approach a red web at its hour, either night.** Under [H24] a red shot is at best noise and at worst the mistake the puzzle punishes.
2. **Night 1 - the yellow four:** `B23` Overflow (2–3 AM) → `B45` Emerald (4–5 AM) → `B56` Oil Fields + `BL56` Ringneck (5–6 AM, the hard doubled hour; interchangeable, [K13b]). Shoot every feather **during its spawn hour** (control #5) with the look-away spawn trick (control #1). **Never leave the yellow spine.**
3. **Hold state through the day inside yellow** ([K29] - persistence is indefinite in-boundary; camping/hotel fine, mind fast-travel's clock advance, control #3).
4. **Night 2 - `B34`:** at 3–4 AM, from the orange∩yellow overlap, **staying east of the Cornwall pole** (control #2). All 5 blacks are now **visibly down at once** and you are standing in the central overlap - the complete [H24] candidate solve state.
5. **Camp at the whiskey tree** ([S23] - ⚠️ *not* a triple overlap; [K49] shows none exists, so this is simply a camp on the Connector spine, chosen for [S23]'s fire-pit coincidence) and apply the **dream coda** (below); watch/listen for any trigger, sound, vision, journal change, or new interactable.
6. **Optional leg (C2):** ride `B34`'s oversized orange boundary **north to Butcher Creek** for the 4–5 AM pentagram window ([K5], the [H21] corridor) - this exits yellow, so the four yellow blacks visibly reset; you are now testing the hidden-flag reading ([H22]-R2) with `B34` as carrier. Camp and sleep there (dream coda again).

| Observation | Reading |
|-------------|---------|
| anything state-gated fires at all-5-down (step 5) or at Butcher Creek (step 6) | **[H24] supported** - the reds were decoys; capture everything; this is the payoff |
| clean null through step 6 | real negative - pushes back toward "reds required" ([H20]/[H22]); Tests A/B regain priority; log it |

> **🆕 Prior art narrowing what Test C adds (Reddit sweep 2026-07-02, [#71], C-tier):** at least **three** players have now shot **all 5 blacks fast** with no payoff - u/Leadcountydude (no sleep, "seems nothings happens", [#67]) plus two genuine **one-night** clears (u/Marmaluke420's speed-run build; u/ColonelMakepeace via Dead Eye - who *also* found 2 webs still active at daytime after, cf. [S39]). **None ran the sleep coda, and none managed boundary discipline** (a one-night ride to `BL56` exits orange → `B34` visibly reset, so their "all 5" was never a held state under [K29] semantics). So Test C's untested marginal content is precisely: **(a)** the *held* all-5-down state (2-night geometry, step 4), and **(b)** the [H25] **sleep step** (step 5). The fast-clear-alone null is already triple-attested - don't count reaching step 4 as news; the test lives or dies at steps 4–6.

### Test D - the witness-only tour, NO shots (settles [H27]; strictly cheaper than Test C - run it before anything that fires a gun)

*Goal: test the 2026-07-02 second fresh-pass reading ([H27], [solve-grammar.md](solve-grammar.md)) that the webs are a **display to be witnessed**, not a target - the feather-shooting premise itself is a community import no verified clue supports. Under [H27]+[H25] this tour is the complete candidate solve. It leaves no state to corrupt, so running it first costs the later tests nothing.*

1. **Fire no shots at any web or feather, any night.** That is the whole discipline.
2. Visit **all 8 webs at their spawn hours** across the nights required (the same routing knowledge as Tests A–C, minus every boundary/reset concern - with nothing shot, [K29] state is moot). At each pole, **force the spawn with the look-away/look-back trick and hold it in view** ([K30] - under [H27] the gaze-detection is the system's sensor, so *seeing* each web deliberately is the input). Note each feather's colour as you go (the read-out is the 5/3 count).
3. Include the **centre cluster at 1–2 AM** (the derived point; its `N`+pole message is the layer's G4 payload).
4. Finish with the **dream coda** (below): camp at the **whiskey tree** ([S23]) and sleep into first light. A blacks-only variant (witness just the 5 blacks, per [H24]×[H27]) is a legitimate cheaper sub-form; the full-8 form is cleaner.

| Observation | Reading |
|-------------|---------|
| any vision/trigger/journal/state change at step 4 | **[H27] (+[H25]) supported** - the input was witnessing all along; capture everything |
| clean null | real negative - logged; [H27] survives only in its weak form (P1–P3 pending); the shooting tests A/B/C regain priority |

### The dream coda ([H25]) - bolt this onto EVERY test, A, B, C, and D

The egg is internally named `spiderdream` ([K13]) ~~and RDR2 ships a sleep-vision system~~ *(premise corrected 2026-07-05, [#85]/[U11]: **no sleep-triggered dream machinery exists** - every in-game dream is story-scripted; sleep is a fade + time-skip. The coda survives in its **weakened, Hani's-Bethel form**: a payoff, if any, would be a **presence-at-hour event in the waking world**, with sleep merely the time-skip - so the watch-priority on waking is the **surroundings**, not an expected vision overlay)*, and no documented solver has ever **slept on a completed candidate state** (the [K29] sleeps were on partial states - **dry-check confirmed 2026-07-02 ([#67]):** a ~1,989-comment master-thread sweep + the community timeline found *proposals only*, zero executed tests). So: **at the end of any completed group/combine/chain - before leaving the boundary - camp or hotel-sleep in-boundary, ideally into first light** (the chronological run ends 5–6 AM = dawn; note [K10] *"KEEP YOUR DREAMS LIGHT"* is carved at the `B56` Oil Fields site). Watch the sleep/wake cycle for any vision, audio, or journal change - **and above all, on waking, the world at the key hour: off-hour/featherless web spawns**, new objects, sounds - the one mid-chain sleeper on record (u/lopfeh, [#67]) woke to featherless webs up at **12:20 AM**, the nearest thing to a sleep-reaction the corpus holds, and it appeared *in the world*, not as a vision (exactly the weakened form's prediction). Costs minutes; covers [U11]'s in-game residual on every run; log the nulls without surprise.

### R3 by elimination (do not conclude early)

R3 ("no global combine") is the **residual**: reached only if Test A is negative **and** Test B is clean-but-empty across *both* meta-orders and the candidate sites. Because it's an argument from absence, it is the **last** conclusion, and even then it stays [SPECULATION] consistent with [U2]/[K20]. One pre-existing **weak point against R3:** the webs are deliberately render-hidden while the Butcher Creek pentagram is *not* ([K30] note) - "hide the webs, show the pentagram" reads as the webs being real puzzle content with an intended combine, mildly disfavouring R3.

---

## Decision table (outcome → conclusion → next move)

| Test A | Test B | Conclusion | Next move |
|--------|--------|-----------|-----------|
| reds hold | - | **R1**: overlap holds state | re-run the combine bridging through the overlap; look for all-8-down state, then a trigger |
| reds reset | new element | **R2**: hidden flag, `B34` carries north | this is the solve corridor - document the payoff fully, promote to [K] with capture |
| reds reset | clean & empty (both meta-orders, sites checked) | **R3-leaning**: no combine / per-boundary puzzles | log the bounded negative; reframes [U3] toward *many*; folds into [U2] no-payoff |

## Data to capture (so any outcome is loggable as investigator data)

For every run: **date**, the **exact route**, **which tied boundary you were inside at each shot and each re-check**, the **game clock** at each step, and a **screenshot of each web's state** at re-check (down vs respawned). For Test B, screenshot the northern sites (Butcher Creek pentagram at ~4–5 AM, Valentine, Fort Brennand) before/after. Per CLAUDE.md, firsthand in-game observation is **high-trust investigator data** even with no online corroboration - record it dated and as such, and a null result is logged the same as a positive.

---

*Sources for the mechanics this protocol drives: [K21]/[K28]/[K29]/[K30]/[K31] (firsthand investigator data), [K13a]/[K13b] (wiki + community), [U29]/[H20]/[H21]/[H22]/[S22]/[S23] (analysis). Companion script: [`web_boundary_solve_protocol.py`](../experiments/web_boundary_solve_protocol.py). This protocol adds the confound controls and the discriminating decision table the script's prose lacks.*

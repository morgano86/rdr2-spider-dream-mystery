# Thread 02 — Butcher Creek outhouse carvings (LJ / SM / Fort Brennand)

**User's primary focus.** Butcher Creek is a poor, isolated hamlet in **Roanoke Ridge** (north-east of the map). It is the
setting of the "Wisdom of the Elders" stranger mission (Arthur exposes the fraudulent shaman). Beyond the story, it hides
the entry point to the Spider Dream clue chain.

---

## [KNOWN]

- There are **five outhouses** around the central area of Butcher Creek. Each contains a **tally mark inside the stall,
  numbered 1–5**.
- **Drawing lines between the five outhouses in numerical order produces a pentagram** — a *second* pentagram that mirrors
  the glowing red **floorboard pentagram** that appears under one of the houses **between ~4:00 and 5:00 AM** in-game.
- **Outhouse #4** carries extra carvings beyond its tally: the letters **`LJ`**, the letters **`SM`**, and a **symbol that
  depicts Fort Brennand**. *(This is the "LJ SM" carving on the back of toilet number 4 the user flagged.)*
- **The `LJ`/`SM` letters are directly part of the mystery — this is [KNOWN], not a guess** (only their *meaning* is open,
  [U4]). Three independent facts pin them to the chain: (1) they use the **same hidden-geometry carving technique** as the
  confirmed clues ([K15]); (2) they are **physically on the same carving** as the **Fort Brennand pointer symbol**, the next
  confirmed node; and (3) they sit on **outhouse #4**, beside **tally 4** and the Fort Brennand clue. So when we test the
  letters, `LJ`/`SM` are the **most firmly-tied** pair — they anchor the letter set ([H12]).
- The **Fort Brennand symbol** directs the player to Fort Brennand (also in Roanoke Ridge). Inside Fort Brennand:
  - additional **tally marks** — **six** in the fort's one outhouse (five-bar gate + 1), **seven** above the
    **guard-tower** entrance, exterior (gate + 2). **Counts CONFIRMED B-tier ×2** (wiki + GameRant; [#81] pass,
    2026-07-05). *(Nobody calls it a water tower — guard tower.)*
  - **three symbols inside that tower** (opposite/above the interior doorframe), depicting a **telegraph/telephone
    pole**, a **factory/industrial building** (both undisputed across tiers), and a **third symbol disputed at source
    level**: the wiki reads an **oil pool/puddle**; the community's own documentation writes, verbatim, *"Oil Puddle
    **or Register Rock**"* (Marmaluke420, [#81]) — the [U24]/[H11] split is native to the community, not our invention —
    and a third rival reads all three as the **Saint Denis skyline** seen from the tower top ([S44], not adopted).
    Net: the symbols point toward the **Heartlands / oil fields** (see thread [03](03-matchstick-letters.md)) on the
    strength of the two undisputed symbols; the third's identity is the open residue of [U10].

- The Butcher Creek pentagram/tally system is the **documented start** of the Spider Dream chain.
- **The pentagram-mapping mechanic has a shipped, solved precedent — the [Saint Denis Vampire](../analysis/saint-denis-vampire.md)
  ([K27]).** That separate Easter egg runs the *identical* puzzle — **find 5 fixed map points → they form a pentagram → go to
  the centre** — but **fully hand-held** (the in-game **journal draws the pentagram** and marks the centre with an "x").
  Butcher Creek is the **same puzzle unaided**: the player must connect the five outhouses themselves, with the floorboard
  pentagram as a check. This is why we read the Vampire as the game's **tutorial / "seed"** for this mechanic ([H15]) and the
  Butcher Creek → spider trail as an **escalating difficulty curve** ([H16]).

### Per-node content sweep (2026-07-05) — a sourced NEGATIVE
**The seven tally nodes were swept for per-node content beyond the bare counts** (wiki + GameRant + the r/reddeadmysteries
documentation corpus + the community Google Site + reddeadreference; [#81]). Result — decisive for [U6] attempt B:
- **Nodes 1, 2, 3, 5 (Butcher Creek) and 6 (Fort Brennand outhouse): NOTHING beyond the tally** in any source. The only
  extras anywhere: a file-level **blood-trail decal** from outhouse 3 toward the butcher shed (ambient-plausible,
  fireflighTim [#53]); spatial adjacencies (node 1 ↔ the pentagram shack; node 4 ↔ the "magic stuff" ritual pole [#73]);
  and the **[S43] green-bottle claim** (see SPECULATION below — identical bottles at 1–5, so incapable of encoding order).
- **Node 4** stays the rich one (`LJ`/`SM` + the fort glyph — behind boards that must be **shot away**; "built into the
  model. Just like the tally marks", Marmaluke420 [#81] — consistent with [K15]); **node 7** carries the three symbols.
- **Consequence:** Gertrude's permutation `(4 7 5 6)` reorders {4,5,6,7} = {content, empty, empty, content} → **attempt B
  is closed-inexecutable as a symbol-reading** (see [connections §3](../analysis/connections.md)); it reopens only if the
  [H26] letter-sweep finds content at node 5 or 6.
- Watch-items (C, leads only): an alleged **"6th outhouse" at Butcher Creek** "which doesn't fit the pentagram" (Andyssue,
  `1qebx6v`) — exactly what the 🎮 [H26] sweep should check while on site; a chance **random encounter with a Butcher
  Creek woman** triggerable while camping inside the 7-tower; "moving spiral things" seen in the tower (`1tzk1vh`,
  probably light shafts).
- **⚡ [K52] The pentagram is a named, coordinated asset: `cablemesh277747_hvlit001` @ (2592.52, 831.74, 82.79), active
  hour `04:00`** *(first-party file read, 2026-09-01 — [#89]; found blind by a game-wide `timeFlags` census with no prior
  knowledge of the mystery, then identified by the investigator)*. It sits 1–3 m from `but_house_hd002` and its porch
  props. **Two things follow.** (a) **It is the same `cablemesh*_hvlit001` drawable family as the 2025 spider-web
  strands** — the first *asset-level* link between the 2018 Butcher Creek chain and the web trail, and the hardest
  evidence yet for [S41]'s "one continuous designed relay" (it also makes [K15]'s loose "the webs + pentagram are mesh
  cables" precise, with names). ⚠️ Weight it honestly: `cablemesh` is a generic class and the two sites are near
  neighbours in the same region file, both mundane reasons to share one. (b) Its flags are **`0x1000010`** — the **only
  single-hour prop in the entire game allowed to change while on screen**, where all 8 webs and the centre are
  off-screen-only. That **file-confirms the firsthand [K30] observation** (the pentagram appears/disappears while you
  watch; the webs don't) and shows render-gating is an **authored per-asset choice**, not engine behaviour.
  ⚠️ The pentagram's coordinates also fall within ~1.1 m of the Top boundary ymap's own corner — which probably explains
  why that boundary "reaches Butcher Creek" ([S22] deflation, pinned at [U36]).

## [UNKNOWN]

- **What `LJ` and `SM` stand for** ([U4]). Common community claim: **developer initials** — **CLOSED as a working line
  2026-07-02** (user call + three stacked desk grounds: counts unfalsifiable across 6,345 credits; coherence asymmetry — `LJ`,
  the tightest-tied marking, has *zero* world-building senior matches, and Lazlow fits only via a stage name as an **audio**
  director on a chain with **no audio clues**; and the letters are co-carved with a *functional* pointer). The in-fiction
  reading is the frame; the *meaning* stays open. Newest candidate: the **waymark reading [H26]** — see
  [connections §1/§1b](../analysis/connections.md).
- **Exact placement/orientation** of each carving on outhouse #4 ("back of toilet number 4") and whether `LJ` and `SM` are
  one carving or two distinct marks. Needs a clean in-game screenshot.
- **U7 — the tally counts as a running sequence (1…7), and does Gertrude continue it? [GERTRUDE HALF ANSWERED-NEGATIVE
  2026-07-05, on the canonical game text].** Why six and seven tallies at Fort Brennand when Butcher Creek used 1–5? The
  **site-level half** — 1→7 as one deliberate running count across the two [K8]-chained sites — stays open and plausible
  (the pointer chain walks BC → Fort Brennand in exactly that order). The **continuation half** ([S4]: Gertrude's numbers,
  reaching ~10–11, extend the counter past 7) now **tests negative against the canonical [K42] recitation set**: a
  continuation predicts an ascending consecutive run *crossing* 7 (…6, 7, 8…), and none exists in any of the 12 game
  lines — `7` occurs four times (lines A, C-tail, D, G) followed only by `6, 5, 6, 3`; `6` is **never** followed by `7`;
  `8` is only ever entered by a derail jump (`17, 8, 9` / `5, 8, 13`), never from a 7. Her only correct ascending runs
  are the 1–5 prefixes (capped at 5 — the [S42] battery) and short re-rails (`3,4,5` / `8,9` / `13,14`); `10`/`11` occur
  solely inside derailed babble (`…4, 5, eleven` / `1, 2, ten, 3`); and **12 — the very next number a 1→11 counter would
  need — is never said** in any line. So "Gertrude extends the tally count" fails on the game's own text (consistent with
  [S42]); what survives of [U7] is the modest site-level question only. → [S4](../findings/speculation.md),
  [K42]/[thread 04](04-gertrude-numbers.md)
- **U27 — why does the chain branch from outhouse #4 (tally 4), not #5 (tally 5)?** The Fort Brennand pointer carving is on
  **outhouse #4**, so the trail leaves the 1–5 tally sequence **one short of its end** — you'd expect the onward clue to sit
  on the *last* tally (#5), not the fourth. Odd enough to flag (user, 2026-06-13). It may be **deliberate** — a "4" signal
  that rhymes with the other small numbers the mystery leans on (the floorboard pentagram appears at **4 AM**; there are **8**
  webs; Rockstar has form with **8/infinity**, e.g. GTA V's *Infinite Eight* — see [S20]) — or simply incidental. Open.
- **U28 — the peculiar line of droppings on outhouse #4's roof.** On top of outhouse #4 sit **two large scats side by side,
  a gap, then one very small scat right at the edge above the doorframe — three in a row** (investigator data, 2026-06-13;
  [`butcher-creek_outhouse4-roof-droppings.jpg`](../images/butcher-creek/butcher-creek_outhouse4-roof-droppings.jpg)).
  **Most likely ambient bird/critter scenery** and meaningless — but it is *another* peculiarity clustering on outhouse #4
  (the same stall that carries `LJ`/`SM` + the Fort Brennand pointer + tally 4), so it is recorded for completeness rather
  than chased. No reading proposed; do not elevate without a reason to.
- Whether the **pentagram** is occult flavor for the "curse" story, a literal map key, or both.
- **U24 — does the third Fort Brennand symbol depict [Register Rock](../locations/register-rock.md), not an "oil puddle"?**
  Register Rock (central Heartlands, exactly where the symbols point) is a **names-and-dates memorial boulder**. If the
  symbol points to *it*, the **names carved on it** become a candidate puzzle — see below and [U24]/[H11] in
  [connections](../analysis/connections.md).

## [SPECULATION]

- **User hypothesis (flagged for testing → now the working stance, [S1]):** `LJ` / `SM` are **not** developer initials but a
  **clue internal to the mystery** — e.g., character initials, or a cipher that pairs with the oil-field matchsticks `J+M`. Note
  the shared letters **J, M** appear in *both* the toilet carving and the oil-field matchsticks, but **connect differently**
  (`LJ SM` vs `J+M`). See [connections](../analysis/connections.md) for the letter-set analysis (L, J, S, M).
- **H26 (fresh-pass, 2026-07-02) — the letters as WAYMARKS:** the pair's *presence* marks a designed node; the content decodes
  keep failing because there is no payload. Predicts **undiscovered letter-pairs at other verified nodes** — a live 🎮 sweep
  (Fort Brennand, pole sites, Fort Wallace). Motivated partly by this thread's own **discovery-lag precedent** (user,
  2026-07-02): the Fort Brennand pointer carving on outhouse #4 took **~7–8 years** to find despite sitting beside a tally
  known for years — hidden content clusters *at* known sites, closer than anyone looked.
  → [connections §1b](../analysis/connections.md)
- The tally counts could be a **numeric key** that links to Gertrude's number recitation (thread
  [04](04-gertrude-numbers.md)) — both are "numbers hidden in/near outhouses."
- The pentagram + early-morning visibility may encode a **time + shape** lock (be here, at this hour, read the shape).
- **S20 — a number/timing motif.** The branch-from-#4 ([U27]), the **4 AM** pentagram, and the **8** webs may be a deliberate
  small-number pattern, in keeping with Rockstar's documented **8 / infinity** affinity (GTA V's *Infinite Eight* killer —
  *"8 is just infinity stood up"*). **Weak and pattern-seeking** — a prompt to watch the numbers, not evidence. See
  [connections §3](../analysis/connections.md) and [speculation.md](../findings/speculation.md).
- **H11 — the third symbol = [Register Rock](../locations/register-rock.md); its names are a name-puzzle.** The rock's
  **complete carving list is now sourced** ([dossier](../locations/register-rock.md#complete-inscription-list)) — beyond the
  headline **J. Brooks, Frank Heck, Otis Miller, Billy Midnight, S. Gray, A. West, B. Ward** it adds **J. V. Henry, Jasper
  Munson, C. Riley, A. Pickel, Doyle, R. Mack, Henry Matilda, Mary**, and bare marks (**W.Y.B, BM, Jm, R.S.G**…). Tested
  against `LJ`/`SM`/`EC`/`J+M`/`S+J`: 🟢 **J.M twice** (Jm + Jasper Munson → `J+M`) and 🟢 **S. Gray** → Gray family → **Caliga
  Hall** `S+J` ([K9]); 🔴 but **no `LJ`/`SM`/`EC` and no `L`** at all. **Keep all names live** ([S13]) — the wiki's "West/Ward
  = *Batman*" reading is unconfirmed and a puzzle may use real-world-looking names as camouflage. A lead to test ([U24]), not
  a confirmed match.
- **S43 (2026-07-05) — the GREEN BOTTLES as per-tally-node markers** (u/Stock-Hat9530, [#81] — C-tier, single author,
  unreplicated, 20-image gallery): a green **McCarthy Brewing Co.** bottle near each of the 5 Butcher Creek tally
  outhouses; a green **"Saint Dymphna" Merlot** directly across from the Fort Brennand 6-outhouse (author searched ~2h
  for a McCarthy there, found none — a deliberate-looking *substitution* if the pattern is real); a bottle **atop the
  7-tower**, from which Saint Denis is clearly visible. The **only candidate per-node differentiator found anywhere** —
  but identical at 1–5, so it can't encode order; at most an [H26]-style waymark system. High pareidolia risk (ambient
  bottles are everywhere); fold the check into the 🎮 [H26] sweep. Full text → [speculation.md](../findings/speculation.md).
- **S44 (2026-07-05) — the three tower symbols as the SAINT DENIS SKYLINE** seen from the 7-tower top (same author,
  [#81]): pole → steeple, factory → stacks, third blob → the pond. Recorded as a third rival for the third symbol
  (alongside wiki-puddle and [H11] Register Rock) — **not adopted**: the two undisputed symbols already point at the
  Heartlands oil fields, and the [K8] hand-off is retro-validated by what sits there. Full text →
  [speculation.md](../findings/speculation.md).

---

## Precise location notes (to verify in-game and screenshot)
- Region: **Roanoke Ridge**, around the Butcher Creek settlement cluster.
- The floorboard pentagram: under **one of the houses**, visible **~4–5 AM**.
- Outhouse #4: capture **the back of the toilet** (interior) where `LJ` / `SM` + Fort Brennand symbol are carved.
- Fort Brennand: capture the **tower interior** with the three pointing symbols, and the **6/7 tally** marks.

## Open tasks
- [ ] Screenshot each of the 5 outhouse tally marks (1–5) and the outhouse-pentagram overlay on the map.
- [ ] High-res capture of outhouse #4 `LJ` / `SM` / Fort Brennand carving — settle whether it's one or two carvings.
- [x] ~~Screenshot Fort Brennand's three tower symbols + tally counts~~ — **web-settled 2026-07-05** ([#81] pass): counts
      6/7 B-tier ×2 confirmed; symbols image already on file (`fort-brennand_tower-symbols.webp`); the third symbol is
      **undecidable from imagery** (flat-bottomed blob — puddle *or* boulder), so the residue is interpretive ([U10]),
      not a capture gap.
- [ ] Test the "LJ/SM = character initials" idea against the cast list (see connections).

## Sources
Dexerto; GameRant ("Butcher Creek Mystery Explained"); Red Dead Wiki (Butcher Creek / Spider Dream Mystery); GTAForums
"Butcher creek hidden numbers." Full list in [sources/sources.md](../sources/sources.md).

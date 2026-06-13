# Cross-thread analysis — connections, letters, numbers

This is the working theory bench. Everything here is **analysis, not fact** — but it's where threads get tied together and
hypotheses get tested (including null results, which are valuable).

---

## 1. The letter set (now expanded with primary-wiki data)

The **user flagged two**: the toilet `LJ`/`SM` and the "`J+M` matchsticks." The primary wiki confirms a **larger letter
system** — there are **four match-sets**, not one:

| Source | Marking | Letters | Location | Note |
|--------|---------|---------|----------|------|
| Butcher Creek outhouse #4 (carved) | `LJ` , `SM` | L, J, S, M | **Butcher Creek** | trail START; image on file |
| Matches (by Black Widow card) | `EC` | E, C | **Vetter's Echo** | spider card; image on file |
| Matches | `J + M` | J, M | **Cornwall Kerosene & Tar** | ⭐ = the **web-trail START pole** site |
| Matches | `S + J` | S, J | **Caliga Hall** | the **Gray** estate (Braithwaite rivals) |
| Matches | arrow → stash | — | (TBD) | standard stash pointer — deprioritised |

**Full letter multiset:** **{ C, E, J, J, L, M, S, S }**. **Locations are a second layer:** 3 of 4 letter-sites are already
mystery nodes (Butcher Creek, Cornwall K&T, Vetter's Echo); Caliga Hall adds the **Gray/Braithwaite feud** dimension.

**Observations**
- The **toilet uses bare pairs** (`LJ`, `SM`); the **matches use a connective `+`** (`J + M`, `S + J`) — classic
  lovers'-initials styling. The puzzle may want these read as **people / relationships**.
- **J is the hub:** it appears in `LJ`, `J+M`, and `S+J` (3 of 5 markings). **S** appears twice (`SM`, `S+J`), **M** twice
  (`SM`, `J+M`).
- The user's key observation still holds and is *strengthened*: the **same letters connect differently** across sources
  (`SM` vs `S+J`; `LJ` vs `J+M`) — a deliberate "**re-pair these**" nudge.

**Graph of shared-letter links** (each marking = an edge between its two letters):
```
L —— J          (LJ)
S —— M          (SM)
J —— M          (J+M)
S —— J          (S+J)
E —— C          (EC, isolated pair, sits beside the Black Widow card)
```
→ Nodes J, M, S, L form a connected cluster (J is degree-3); **E–C is a separate component**. Reading the cluster as a
**path** gives e.g. **L–J–M / L–J–S–M / S–J–M** orderings; reading it as **couples** gives candidate pairs {L,J}, {S,M} OR
re-paired {J,M}, {S, ?}. **Unproven** — needs character names.

**Candidate-name workstream (TODO):** build an RDR2 character/credits list and test initials **L.J., S.M., J.M., S.J., E.C.**
against (a) in-fiction characters (Butcher Creek, Braithwaites, the "letters to Annabella" at Vetter's Echo) and (b) the dev
credits.

**New candidate name-source — [Register Rock] ([H11]/[U24], investigator lead).** *If* the **third Fort Brennand symbol**
depicts **[Register Rock](../locations/register-rock.md)** (central Heartlands, where the symbols point) rather than an "oil
puddle," that boulder gives an **explicit, in-fiction list of names** to test — a far better source than the full dev credits.
The **complete carving list** is now sourced (wiki + reddeadreference transcription blog + our journal image — full table and
provenance in the [dossier](../locations/register-rock.md#complete-inscription-list)). The candidates that bear on the letters:

| Name / mark (Register Rock) | Initials | Note |
|-----------------------------|----------|------|
| J. Brooks ("US Post 1863") | J.B | — |
| Frank Heck ("75") | F.H | — |
| **Otis Miller** / "R. Mack Otis" | O.M / R.M | recurring RDR dime-novel outlaw; may be a reading of the "R.Mack · Otis" mark |
| **Billy Midnight** / "BM" | B.M | gunslinger (duel stranger mission); cf. the bare "BM" mark |
| **Scott Gray** ("S. Gray 1846") | **S.G** | **Gray family → Caliga Hall → the `S+J` matches ([K9])** |
| **"Jm"** + **"Jasper Munson"** (Oregon Wagon Train 1882) | **J.M** | 🟢 **two J.M signals — echo the `J+M` matchsticks ([K9])** |
| A. West | A.W | wiki *speculates* **Adam West** (Batman) — **unconfirmed**; keep as a live candidate (see caution below) |
| B. Ward | B.W | wiki *speculates* **Burt Ward** (Robin) — **unconfirmed**; keep as a live candidate (see caution below) |
| C. Riley ("Wyoming") · A. Pickel ("41") · Doyle ("Missouri") · J.V. Henry (×2) · Henry Matilda · Mary · W.Y.B · R.S · R.S.G | C.R, A.P, … | the remainder — no obvious pairing with the mystery letters |

- **⚠️ Methodological caution ([S13], user's point, important).** Do **not** discard a name just because it *also* reads as a
  real-world or pop-culture reference. The West/Ward = *Batman* link is **wiki speculation, unconfirmed** — and even if true,
  a deliberately-designed puzzle has every incentive to choose names that **double as plausible real-world references**, so
  that players file them as "just a dev in-joke" and never test the in-game connection. **A name doubling as an outside
  reference is camouflage, not disqualification.** This applies to all of them: Otis Miller / Billy Midnight are in-game RDR
  references; West/Ward may be outside ones; both could *also* serve the puzzle. **Keep every name as a live candidate** and
  let the test (not the vibe) decide.
- **Current read (updated 2026-06-13, full list sourced):** two signals now land on existing mystery nodes —
  **(1) J.M appears twice** ("Jm" + "Jasper Munson") echoing the **`J+M`** matchsticks at Cornwall, and **(2) S. Gray** →
  the Gray estate / **`S+J`**. Against that: a real **partial-negative** — **no `LJ`, `SM`, or `EC` anywhere on the rock, and
  no `L`-initial at all.** So Register Rock supplies J, M, S, C from the set **{C,E,J,J,L,M,S,S}** but **not** the `L`/`E`
  legs; if it were the single name-key, that absence is awkward. **A lead to test, not a match** — and per the caution above,
  the "obvious" outside references stay in too.

**Counter-hypothesis — "developer initials" — explicitly weighted DOWN (user's reasoning):**
- RDR2 had **thousands** of credited workers. For *any* two-letter pair, you can almost certainly find *some* matching
  staffer — so a coincidental match is **near-certain and therefore near-worthless as evidence**. "We found a dev with those
  initials" proves nothing on its own.
- Low-level staff are very unlikely to be honoured with initials hidden in the world; only **founders / senior creative
  leads** (e.g. **Sam & Dan Houser**, key directors/producers) would plausibly get that treatment — and even then, a
  *coordinated set of matchstick puzzles beside a Black Widow card at four themed locations* is not how you'd honour someone.
- **Stance:** treat the matchstick/carved letters as an **in-fiction mystery** (related to the spider puzzle, or a parallel
  one). If checking dev initials at all, check **only the short high-rank list**, and treat any hit as *suggestive, not
  proof*. Do **not** spend effort scanning the full credits — by the math above it would "confirm" almost anything.
- The wiki's own "dev initials / modelling error" caveat is for the *separate* Fort Wallace bird-symbols; those at least have
  the geometry-technique fingerprint arguing for intent (see [carving-technique.md](carving-technique.md)).

---

## 2. The outhouse motif (strongest structural link)

Three of our threads center on **outhouses**:
- **Butcher Creek:** 5 outhouses, tally marks 1–5, the `LJ`/`SM` carving on #4.
- **Fort Brennand:** more outhouse/tower tallies (6, 7) + the three pointer symbols.
- **Gertrude Braithwaite:** dies locked in the Braithwaite **outhouse**, reciting numbers.

**Hypothesis H2:** the outhouse is the connective node type, and **Gertrude is a fourth tally-node**, not a disconnected
thread. → Test: look for tally marks in/near Gertrude's outhouse; check if her numbers index the Butcher Creek/Brennand
tallies.

> **⚠️ H2 — what actually bears on it (2026-06-13, [K23] corrected + the #43 hoax exposé).** The GTA/Nazar number is **not** a
> debunk of H2: Gertrude's numbers are **RDR2-original (2018)** and only **echoed** in GTA later (2019) — chronology leaves H2
> untouched. The genuine caution is the **C-tier hoax exposé**, which disputes the Gertrude↔spider *video* and makes a
> **contested geometry claim**: that Gertrude's outhouse line points to **Copperhead Landing (Van Horn way)**, *not* Butcher
> Creek — whereas other (also C-tier) community posts claim it runs to **Butcher Creek centre**. **Both unverified — record
> both, assert neither.** H2's *structural* core (outhouse + numbers recurs across Butcher Creek, Fort Brennand, Gertrude) is a
> real motif; "Gertrude is a 4th node" stays an **open hypothesis**, neither promoted nor dismissed.

---

## 3. The numbers: tallies + Gertrude

**Known number data**
- Butcher Creek outhouses: **1, 2, 3, 4, 5** (tally per outhouse).
- Fort Brennand: **6** (one outhouse) and **7** (tower entrance).
- 2025 trail directional count: **"five poles west."**
- Gertrude's recited sequence: **opening `1, 2, 3, 7, 6, 4, 5, 1, 1, 2`** (`123 7645112`) is now **sourced** ([K23] — the
  GTA/Nazar crossover); the tail (**… 1, 2, 10, 3 …**) is still transcription-only.

**Hypothesis S4:** tallies are one running counter 1→7; Gertrude (reaching ~10–11) extends it. But her sequence is
**scrambled and repeats** (1,2,3,7,6,4,5,…), so it's likely an **ordering/index**, not a simple count.

### Worked attempt A — A1Z26 letter cipher on Gertrude's numbers
Mapping 1→A … 26→Z on `1,2,3,7,6,4,5,11,2,1,2,10,3`:

```
1  2  3  7  6  4  5  11 2  1  2  10 3
A  B  C  G  F  D  E  K  B  A  B  J  C
```
→ **A B C G F D E K B A B J C** — no obvious English word. **Inconclusive / likely null**, but note the late `J` (10→J)
and that the sequence opens `A B C` then jumps. If the transcription is wrong (very possible), the mapping changes. **Do
not treat this as solved or meaningful.**

### Worked attempt B — Gertrude's numbers as an index/permutation
The sequence `1,2,3,7,6,4,5` looks like a **reordering of 1–7** (the exact tally range!): it uses each of 1–7 once
(`1,2,3,4,5,6,7` rearranged), then continues `11,2,…,10,3`. The premise — that the opening really is `1,2,3,7,6,4,5` — is now
**confirmed** ([K23]). → Test: read the carvings/symbols in the order `1,2,3,7,6,4,5` and see if they spell or point to something.

> **⚠️ Status (2026-06-13, [K23] corrected).** The opening `1237645112` is **confirmed and RDR2-original** (the GTA "Nazar
> Speaks" machine echoes it *later*, Dec 2019 — a callback, not the source). So the input to attempt B is **solid**, and a
> spider-cipher reading is **not** ruled out by the crossover. **Two honest caveats remain:** (1) the same digits are *also*
> the Nazar phone-style string, so a tally-index "match" needs **independent** corroboration to mean anything; and (2) the
> seven tally nodes are bare *counts* (1–7) plus the `LJ`/`SM` carving at #4 — there isn't a distinct letter at each node to
> reorder into a word, so the test isn't cleanly executable **without more node-content data** (what, beyond a number, is at
> each node?). **Net: attempt B is a legitimate test, but blocked on node content — gather that first.**

*(Caveat retained: the **tail** past `1237645112` is still transcription-only.)*

---

## 4. The pointer chain (most solid factual spine)

```
Butcher Creek (pentagram + tallies 1–5, outhouse #4: LJ / SM / Fort-Brennand symbol)
        │  Fort Brennand symbol
        ▼
Fort Brennand (tallies 6,7 + tower symbols: telegraph pole · factory · oil pool)
        │  oil-pool / factory symbols
        ▼
Heartland Oil Fields ("KEEP YOUR DREAMS LIGHT" carving; nearby telegraph pole)
        │  spider symbol on telegraph pole (~3–4 AM)
        ▼
2025 Spider-Web trail (8 poles + central tree web 'N') → N, then W×5, then NW + guitar
        ▼
Fort Wallace (waypoint, two guitars)
        │  continues NW (unverified, post-Jan-2026)
        ▼
Calumet Ravine / Giant's birds → "?" carving (out-of-bounds)  ── COLD FRONTIER ──
```

**The seams worth pressing:**
- The **`LJ`/`SM`** letters sit at the **start** of the chain; the **`J+M`** matchsticks sit at the **pivot** (Oil Fields).
  If they're a cipher, the answer may unlock the trail's **cold frontier** past Fort Wallace (now a waypoint, not the end).
- Gertrude's index-of-7 (attempt B) maps onto the **seven tallies** that define the chain's first two stops.

---

## 5. The feathers (colour, order) and the Window Rock cross-check
- **Web feathers:** **5 black + 3 red.** Reds = **Saint Denis, Southfield, Scarlett**; blacks = **Cornwall, Oil Fields,
  Overflow, Emerald, Ringneck**. A documented **non-respawn chain** exists: `Overflow(B23) → Emerald(B45) → Oil Fields(B56) →
  Ringneck(BL56)` — all **black** — implying a correct **order**. The reds' place is unsettled.
- **Window Rock "Strange Statues" mural** is a *solved separate* puzzle: tail-feather counts **2, 3, 5, 7** (first four
  primes). Note **5** and **3** — the exact web colour split — both appear in that set.
- **Hypotheses to test (SPECULATION):**
  - **H3.** The mural's **black/red bird** counts equal the webs' **5 black / 3 red**, making the mural the **order key**.
    Test: count mural birds *by colour* in-game.
  - **H4.** **Feather position/orientation** (undocumented online — your lead) encodes the shooting order; each feather may
    point toward the next web/pole. Test: capture every feather's orientation (see [WEBS-MANIFEST](../images/webs/WEBS-MANIFEST.md)).
  - **H5.** Colour = a **binary** (black/red) reading around the ring, or maps to the **honor** mechanic (a documented
    community guess). Unresolved.

### 5a. The boundary respawn mechanic ([K21]) and the 3-boundary partition ([H9])
**Firsthand investigator finding (2026-06-13):** a shot feather drops to the ground (non-interactable) and **does not
respawn while the player stays inside the boundary that web is tied to** — leaving the boundary respawns it. This is the
*mechanism* behind the K13b non-respawn chain: it isn't only a shooting sequence, it's **spatial**. There are **three
boundaries — north, south, and a connector joining them.**

The Jay_0048 community map ([`web_map-overlay_boundaries.png`](../images/webs/web_map-overlay_boundaries.png)) draws the three
as coloured rectangles and color-codes each web to one — **a [SPECULATION]-tier partition** (one C-tier author):

| Boundary | Webs (codes) | Locations |
|----------|--------------|-----------|
| **North** (orange) | `B34` | Cornwall (the index/start pole) |
| **Connector** (yellow — a tall box bridging New Hanover ↓ Lemoyne) | `B23, B45, B56, B56L` | Overflow, Emerald, Oil Fields, Ringneck |
| **South** (red) | `R23, R45, R34` | Scarlett, Southfield, Saint Denis |

This is **clean and complete**: 1 + 4 + 3 = all 8 webs, each in exactly one boundary. The striking part — **the Connector's
four webs are precisely the [K13b] non-respawn chain** `B23→B45→B56→BL56`. So the chain may simply be "the Connector
boundary's members," and the reds/Cornwall form their own boundaries. **Open ([U22]):** verify each assignment independently;
the map's legend writes Saint Denis as "R56" (typo for `R34`); and the all-black North boundary holding a single web is
unconfirmed. If the partition holds, it likely **scopes the order problem per-boundary** rather than across all 8 at once.

## 6. Cross-site coincidences worth not dismissing
- **Two cheat-carving sites sit on two independent mystery threads:** **Vetter's Echo** (the `EC` matches + Black Widow card)
  and **Braithwaite Manor** (Gertrude). See [cheat-codes.md](cheat-codes.md). Could be coincidence (cheats are scattered
  map-wide) — but worth noting the overlap.
- **The "outhouse + numbers" motif** now spans Butcher Creek, Fort Brennand, **and** Gertrude — see §2 and
  [narrative-connection.md](narrative-connection.md) for the geographic/thematic clustering.
- **GTA↔RDR is an established Rockstar crossover channel ([K23]/[K24]) — full dossier:
  [gta-rdr2-crossover.md](gta-rdr2-crossover.md).** Gertrude's `1237645112` is the **same number** the **Madam Nazar "Nazar
  Speaks"** machine speaks in GTA Online; the same machine also gives the *"web…unraveling"* fortune ([U19]) and names other
  RDR2 places ([S14]). And GTA V's **Mt Chiliad webs are base-game since 2013** ([K24]). ⚠️ **Direction matters (corrected
  2026-06-13):** the RDR2 numbers (2018) and both games' webs (2013/2018) are **original-to-launch**; only the **2019 Nazar
  callback** was added later. So the crossover **raises confidence the material is deliberate** — it does **not** supply a
  "mundane pre-spider origin" that downgrades Gertrude. Net effect on the spider case: Gertrude's numbers are a **deliberate,
  Rockstar-flagged RDR2 cipher-candidate** whose link to the **spider trail specifically** is still **undecided** (could be the
  trail, a standalone Nazar/Braithwaite egg, or undecipherable).

## Open analysis tasks
*Several of these are computational — script them in [`../experiments/`](../experiments/) rather than by hand (a cipher
harness for Gertrude's numbers, a coincidence-odds calc for the dev-initials argument, name-list matching). Results are
[SPECULATION] until sourced; log null results.*
- [ ] Build the RDR2 character/credits name list; test L.J. / S.M. / J.M. (both clue and dev-initial hypotheses).
- [ ] Add **all** the **Register Rock** names ([U24]) to that name-matching script — the **full sourced list** is now in the
  [dossier](../locations/register-rock.md#complete-inscription-list). **Do not pre-filter** the "Batman" (West/Ward) names; per
  the caution above, an outside reference may be deliberate camouflage. The desk check already shows **J.M ×2** (Jm + Jasper
  Munson → `J+M`) and **S.G** (→ `S+J`), but **no `LJ`/`SM`/`EC` and no `L` at all** — script it to confirm and to test surname
  pairings systematically. Confirm first whether the Fort Brennand symbol actually depicts the rock ([H11]).
- [ ] Verify Gertrude's exact sequence, then test attempt B (read tally nodes in her order) — scriptable once U6 lands.
- [ ] Confirm the `J+M` matchsticks and compare the carving "hand"/style to outhouse #4.
- [ ] Capture the under-wood messages (thread 05) — they may directly state what the letters/numbers mean.
- [ ] Once images are in, overlay the spider symbol on a real map and label all poles.

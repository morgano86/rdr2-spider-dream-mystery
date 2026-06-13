# STATUS — start here

The operational dashboard. **This is the single entry point each session**: where the case stands, what's blocked on
what, and what to do next. It holds *pointers and the live frontier*, not content — detail lives in the files it links.
Keep it short; when something changes here, also touch the canonical file and the [log](INVESTIGATION_LOG.md).

> **One-line status (2026-06-13):** **UNSOLVED — no confirmed reward/cutscene/unlock** (Jan 2026 coverage: *"no new loot,
> tools, or cutscenes"*). The community decoded the web-trail to **Fort Wallace** in late 2025; Fort Wallace is a
> **waypoint, not the end** — the trail now runs **cold NW** toward Calumet / the Giant / a **"?" carving**. The egg is
> confirmed *real* by a former Rockstar QA tester ([K3](INDEX.md)), but authorship is unconfirmed.

- **Best one-paragraph understanding:** see [README.md](README.md#one-paragraph-summary-of-the-current-best-understanding).
- **Cold frontier:** NW past Fort Wallace → [thread 06](threads/06-bird-carving-giant-wapiti.md).

---

## Top open questions (ranked)
Full set + IDs in [findings/unknowns.md](findings/unknowns.md). The ones that could break the case open:

| Rank | ID | Question | Best source |
|------|----|----------|-------------|
| 1 | [U0](findings/unknowns.md) | The 8 feathers' **position/orientation** — likely encodes the shooting order | 🌐 video frames → 🎮 only if unclear |
| 2 | [U1](findings/unknowns.md) | The **under-wood pole messages**, verbatim | 🌐 community video/threads |
| 3 | [U22](findings/unknowns.md) | Exact **web↔boundary membership** ([H9]) — likely scopes the visit/shoot order | 🌐 verify Jay_0048 map / 🎮 |
| 4 | [U14](findings/unknowns.md) | **Window Rock mural** birds **by colour** — is it 5 black / 3 red (the order key, [H3])? | 🌐 mural images we hold |
| 5 | [U2](findings/unknowns.md) | Is there an **intended payoff at all**, or is it cut content? | 🌐 new coverage / community |

> **Note (2026-06-13):** [U6] (Gertrude's numbers) sits just off the top-5. Its opening `1237645112` is now **sourced and
> confirmed deliberate** (RDR2-original, Rockstar-echoed cross-game via Nazar, [K23]) — but its **link to the spider trail
> specifically is undecided**, so it ranks below the four trail-direct items above. Tracked in
> [analysis/gta-rdr2-crossover.md](analysis/gta-rdr2-crossover.md).

---

## Next actions, by channel
**Default to web sourcing + verification.** Most open questions are already documented in the wiki, community sites,
forum threads, or the Strange Man video — find the evidence and corroborate it. Reserve in-game capture for detail no
online source records (in practice, only the feather *orientation*).

### 🌐 Web / video sourcing (the default) → [EVIDENCE-CHECKLIST.md](EVIDENCE-CHECKLIST.md)
The actionable worklist, ordered by value. Headline items: the **under-wood pole messages** (U1, in community videos),
**Gertrude's full sequence** (U6, transcribed in late-2025 videos), the **Window Rock mural birds by colour** (H3/U14),
and **feather orientation** (U0) — pull from video frames first.
- Build the RDR2 **character/credits name list** to test `LJ`/`SM`/`J+M` ([U4](findings/unknowns.md), [U16](findings/unknowns.md)).

### 🎮 In-game (only when strictly necessary)
Used only where the web genuinely comes up empty: confirming **feather orientation** (U0) if video frames don't resolve
it, and the long-horizon **H8 test** (does completing the trail clear the dreamcatcher log?).

### 🧠 Analysis (desk work, no sourcing needed)
From [analysis/connections.md](analysis/connections.md#open-analysis-tasks):
- Test Gertrude attempt B (read the 7 tally nodes in her number order) once U6 lands.
- Re-pair the letters `{C,E,J,J,L,M,S,S}`; test the dev-initials-down hypothesis against the name list.
- Decide [U3](findings/unknowns.md): is this one layered puzzle or two parallel eggs?
- **[U22]** Verify the 3-boundary web partition ([H9]) — does it scope the shoot/visit order per-boundary? Cross-check the
  Connector set against the [K13b] chain and feather orientation ([U0]).

> **🧮 When reasoning isn't enough** (combinations, ciphers, geometry, coincidence odds), write a quick Python test in
> [`experiments/`](experiments/) — e.g. [`feather_order.py`](experiments/feather_order.py). Results are evidence, not
> fact; log null results too.

---

## Recently added (2026-06-13)
- **[K23]/[K24] GTA↔RDR2 crossover dossier — new file [analysis/gta-rdr2-crossover.md](analysis/gta-rdr2-crossover.md).**
  Gertrude's recitation **opens `1237645112`**, the *same* string the **Madam Nazar "Nazar Speaks"** machine speaks in
  **GTA Online** (multi-outlet B-tier). ⚠️ **Chronology corrected (user-flagged):** the number is **RDR2-original (base game,
  Oct 2018)**; the GTA echo is a **later callback (Dec 12, 2019)**, **not** a prior origin — so it **corroborates the number is
  deliberate**, it does **not** demote the RDR2 reading. **[K24]:** GTA V's two **Mt Chiliad webs are base-game since 2013, not
  DLC** (same cable shader + 1–2 AM gate as RDR2) — so the webs in *both* games are original-to-launch; only the Nazar number
  callback was added later. Nazar's machine also names our nodes (**Window Rock, Roanoke Ridge, Grizzlies**, the web fortune
  [U19]) → **[S14]** (weak — coincidence-prone). **Net:** the crossover raises confidence this is **deliberate**; the
  **decode/spider-link is exactly as open as before**. A C-tier exposé ([#43]) separately alleges the Strange Man "Gertrude
  solved" *video* is a **hoax** (⇒ treat his Gertrude claim as disputed). Propagated across K23 (reworded)/K24/S14, U6/U18/U19,
  connections §2/§3/§6, speculation, sources #40–46.
- **[U24] Register Rock — full carving list sourced.** Pulled the **complete** inscription set (wiki + reddeadreference
  transcription blog + our journal image): ~14 named carvings + ~10 bare marks ([dossier](locations/register-rock.md#complete-inscription-list)).
  Desk-test vs the matchstick letters: 🟢 **J.M appears twice** ("Jm" + "Jasper Munson") → echoes **`J+M`**; 🟢 **S. Gray** →
  Caliga Hall **`S+J`**; 🔴 but **no `LJ`/`SM`/`EC`, and no `L`-initial at all** — a real partial-negative. Still gated on
  whether the Fort Brennand third symbol actually depicts the rock ([H11]).
- **[K21] boundary respawn mechanic** (investigator data): shot feathers stay down only while you're **inside the web's tied
  boundary**; **3 boundaries** — north, south, + a connector. Sourced the **Jay_0048 boundary map**
  ([`web_map-overlay_boundaries.png`](images/webs/web_map-overlay_boundaries.png)) → partition **[H9]**: N `B34` / Connector
  `B23,B45,B56,B56L` / S `R23,R45,R34`. The **Connector == the [K13b] non-respawn chain** — the spatial mechanic *is* the
  chain. Verify membership next (**[U22]**).
- **+8 images** from the community Google Site (boundary/labelled/chain/trail maps, cable-mesh datamine, Cornwall pole, Fort
  Wallace guitars & birds).
- **Two new frontier leads (investigator data):** **[K22]** a hidden **empty heart** on [Bacchus Bridge](locations/bacchus-bridge.md)
  (blank twin of the Flatneck "Lillie ♥ Alfred" heart) **in line of sight of the bird carving** → [H10]/[U23]; and **[H11]**
  the Fort Brennand "3rd symbol" may depict **[Register Rock](locations/register-rock.md)**, whose carved **names** (incl.
  **S. Gray** → Caliga Hall `S+J`) could be a name-puzzle → [U24]. The earlier "Lillie ♥ Alfred" texture is **re-framed** from
  "rejected" to the heart-motif reference.

## Recently resolved (don't re-litigate)
- **[U8] → [K3]:** dev quote is **Adam Butterworth, ex-Rockstar QA** — confirms *real*, not *authored* (B/C-tier, single X post).
- **[U13] downgraded:** **Spider Gorge** is wiki-only speculation; no secondary source — journalism points the marker at Fort Wallace.
- **[U17] reframed / [K20]:** the spider mystery has **no in-game log at all**; the lingering log entry is the **dreamcatchers'** ([H8](findings/speculation.md) tests the link).

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

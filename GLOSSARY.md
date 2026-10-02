# Glossary - how to read this corpus

The files here are dense with short IDs and project-specific shorthand. This page decodes them. Everything below describes conventions already used throughout the repo.

## Claim tags

| Tag | Meaning |
|---|---|
| `[KNOWN]` | Verifiable in-game, or corroborated across multiple reliable sources. |
| `[UNKNOWN]` | An open question. |
| `[SPECULATION]` | A community or our own theory; not confirmed. |

A claim is **never promoted** to a stronger tag without sourcing, and a shaky fact is **moved** (e.g. to the unknowns) rather than quietly edited in place.

## Source reliability grades

| Grade | Meaning |
|---|---|
| **A** | Primary: in-game, official, or first-hand data read from the shipped game files / scripts. |
| **B** | Established games journalism or a long-standing wiki. |
| **C** | Forum / social / video. Useful *leads* - verify before trusting; never state as fact. |

## Stable IDs

IDs are **append-only** (a number is never reused). [`INDEX.md`](INDEX.md) lists every ID with its status and the file that owns it.

| Prefix | Kind | Rollup |
|---|---|---|
| `K#` (`K13`, `K13a`) | A **known fact** | [`findings/known-facts.md`](findings/known-facts.md) |
| `U#` | An **unknown** / open question | [`findings/unknowns.md`](findings/unknowns.md) |
| `H#` | A **hypothesis** - a worked theory, usually with a test attached | [`findings/speculation.md`](findings/speculation.md) |
| `S#` | A **speculation** - a looser idea or lead | [`findings/speculation.md`](findings/speculation.md) |
| `[#NN]` | **Source number** `NN` in the ledger [`sources/sources.md`](sources/sources.md) | - |

Statuses in the index: **LIVE** (current) · **RESOLVED** (an unknown answered, now a K-fact) · **DOWNGRADED / REFRAMED** (kept, but weakened) · **REFUTED** (killed, history retained).

## Project vocabulary

- **The verified trail / the frontier.** The chain of clues that is actually sourced, ending at the **Fort Wallace bird carvings** ([K16]). Everything after is *contested*, not "the trail". See the boundary rule in [`CLAUDE.md`](CLAUDE.md).
- **Webs.** The 8 spider webs that appear on telegraph poles / a tree at specific night hours, each with a feather, plus a **centre web** (1–2 AM, no feather) that spells `N`. Catalogued in [`images/webs/WEBS-MANIFEST.md`](images/webs/WEBS-MANIFEST.md).
- **Web labels (`B34`, `BL56`, `R34`…).** Short codes for individual webs: the first letter is the feather colour (**B**lack or **R**ed) and the digits are the hour window. `B34` is Cornwall's web (3–4 AM, black); `BL56` is Ringneck (5–6 AM, black). See the manifest for the full table.
- **Black / red feathers.** 5 "black" (actually two-toned white/grey ↔ black, [K13]) and 3 red feathers. The wiki and game files call the mystery's assets `spiderdream01`–`08`, which is where the name comes from.
- **Letters / markings.** The `LJ`, `SM`, `EC`, `J+M`, `S+J` carvings and matchsticks. We call them *letters*, not *initials* - "initials" is an unconfirmed reading.
- **Carving test.** The method in [`analysis/carving-technique.md`](analysis/carving-technique.md) for telling a deliberate carving (hidden-geometry technique) from pareidolia.
- **Pareidolia.** Seeing a pattern (a face, a symbol) in noise. The off-map `?` carving is widely judged to be this.
- **Test A / B / C / D.** The proposed in-game experiments for the feather-order question ([U29]); protocols in [`analysis/web-order-field-test.md`](analysis/web-order-field-test.md). Test A is moot (see [K49]); Test D (a no-shots "witness" tour) is the cheapest.
- **Investigator data / first-hand.** Observations the investigator made in-game. Treated as high-trust and labelled with the date, even where no online source corroborates them.
- **CodeX.** A third-party RDR2 archive and asset explorer / 3D scene viewer, run locally by the investigator to read the shipped game files (`.ymap`, `.ytyp`, `.ydr` and similar). Notes in `datamining/` are verbatim readouts from it, filed in [`datamining/`](datamining/README.md).
- **Script census / script dump.** A search of the game's decompiled scripts (`.ysc`) for strings, hashes and coordinates - either the investigator's own tooling or a public third-party dump. Used to prove things are *absent* ("no script touches the webs") as often as present.
- **Handoff document.** A saved verbatim write-up from an external tool or research relay, filed under [`sources/`](sources/) so claims stay checkable.
- **Streaming extents / ymap.** How the engine loads map chunks by distance. The feather "reset boundaries" turned out to be ordinary ymap streaming extents ([K48]), not designed puzzle geometry.
- **Deflated / closed-negative.** A lead that was tested and found empty. Logged as a finding in its own right.
- **Waypoint.** A location that is a verified stop on the trail but not its end (Fort Wallace).
- **Relay.** The idea ([S41]) that the 2018 Butcher Creek chain and the 2025 web trail are one continuous designed hand-off rather than two puzzles.

## Where things live

- **Dashboard / what next:** [`STATUS.md`](STATUS.md)
- **Evidence worklist:** [`EVIDENCE-CHECKLIST.md`](EVIDENCE-CHECKLIST.md)
- **Chronological log (newest first):** [`INVESTIGATION_LOG.md`](INVESTIGATION_LOG.md)
- **Where each source came from and how to fetch it:** [`sources/RESOURCES.md`](sources/RESOURCES.md)
- **Image naming rules:** [`images/README.md`](images/README.md#naming-convention-enforced)

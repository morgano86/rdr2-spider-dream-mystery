# The Wapiti "smoke" (a separate mystery)

> *New here? See the [README](../README.md) for the overview and the [glossary](../GLOSSARY.md) for the ID/tag conventions (`K13`, `[#89]`, `H27`…).*

**What this file is.** A dossier on the thin plume of "smoke" reported (around 2019) on an empty hillside near the Wapiti Reservation, whose puffs were said to look like symbols. It is **not part of the Spider Dream Mystery** — a closed, deflated side lead, unrelated to the Fort Wallace frontier ([K16]).

## [KNOWN]

*Source: [#94](../sources/sources.md) — file readout + particle-effect decode, 2026-09-14; A for file contents, B for interpretation. Readout: [`codex-file-readout-2026-09-14-wapiti-smoke-geyser-proxy.md`](../datamining/codex-file-readout-2026-09-14-wapiti-smoke-geyser-proxy.md). Rollup: [K57](../findings/known-facts.md).*

- **The source is map data, not weather or script.** Archetype `reg_bgv_vfx_proxy` — a 2 m cube buried about 5 m underground, so nothing shows — at (197.34, 2204.24, 271.16) carries a particle-effect extension for `ent_amb_steam_geyser`, emitting at (197.34, 2204.24, 281.16): ~3.2 m above ground and ~3.7 m from the reported point. It lives in `reg_bgv_00_strm_0.ymap` (base game archive, so present since launch), has **no `timeFlags` and no hour window**, and is the **only map-placed use** of that geyser effect game-wide. The real, **scripted** geysers are at Cotorra Springs, 300–370 m south.
- **Why it looks like a thin plume.** Without the script that sets the `Steam`/`Erupt` evolutions, only the thin fog layer plays (~1.4 puffs/s, 1–5 m, ~4 s life, wind-driven) — matching the investigator's in-game footage of a thin plume beside thick Cotorra steam. The "symbols" were fog puffs.
- **Ruled out:** a weather/fog volume (nearest of 15 is 1,555 m away), a script (no coordinate or reference), a scenario campfire, time-gating, a "smoke-signal" rhythm (no `smoke_signal` string anywhere), and a bespoke texture (all sheets are shared library). The cube carries the UFO-painting material only because it shares a Big Valley pack with `reg_bgv_ufodecal*` — an authoring fingerprint, **not** a link.

## [UNKNOWN]

- Why a script-less geyser emitter sits above Cotorra Springs (leftover layout?).
- The ~100 m visibility range reported by the investigator — an in-game check.

## [SPECULATION]

- None minted.

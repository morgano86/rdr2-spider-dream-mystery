# Contributing

Thanks for your interest. This is a research repo, so "contributing" means **bringing evidence, corrections and careful analysis** - and keeping the corpus honest. Start with [`README.md`](README.md) for the overview, [`GLOSSARY.md`](GLOSSARY.md) for the shorthand, and [`STATUS.md`](STATUS.md) for what's open.

## What's most useful

- **Corrections.** If a claim is wrong, say so with a source. We soften or re-tag rather than delete, so the history stays visible.
- **Sourcing.** A better-graded source for a claim (A > B > C), an archived link for a dead one, or the original post/video behind a relayed claim.
- **First-hand captures.** Clear in-game screenshots with the time, location and conditions noted - especially anything on the open items in [`EVIDENCE-CHECKLIST.md`](EVIDENCE-CHECKLIST.md).
- **Negative results.** A careful "I looked and found nothing" is a finding; please include how you looked.
- **Tests.** A small, deterministic script in [`experiments/`](experiments/) for a combinatorial, cipher, geometry or likelihood question (see [`experiments/README.md`](experiments/README.md)).

## The editorial rules

1. **Tag every factual claim** `[KNOWN]`, `[UNKNOWN]` or `[SPECULATION]`. Don't state anything untagged, and don't promote a claim to a stronger tag without sourcing it.
2. **Grade your sources** (A / B / C - see the [glossary](GLOSSARY.md#source-reliability-grades)). Cite the strongest available. A C-tier lead is not a fact.
3. **Respect the verified-trail boundary.** The Fort Wallace bird carvings are the last verified clue; the Calumet/Giant continuation, the `?` carving and the Bacchus Bridge heart are contested. Don't build chains on top of them. A theory you've heard - even a popular one - is a tagged `[SPECULATION]` lead until it's sourced.
4. **Scripts test; they don't establish fact.** A positive result is `[SPECULATION]` until sourced; a negative result is a real finding. Never feed a script invented data.
5. **Use stable IDs.** When you reference or correct a claim, use its ID and update every place it appears - the thread, the matching [`findings/`](findings/) rollup, any analysis file, and its row in [`INDEX.md`](INDEX.md). IDs are append-only; never reuse a number.
6. **Log the session** at the top of [`INVESTIGATION_LOG.md`](INVESTIGATION_LOG.md) (newest first, absolute dates) when it changes what we know.

## Formatting

- **Don't hard-wrap prose.** One paragraph or list item is one source line. Run `python tools/unwrap_md.py --check` to see whether anything needs unwrapping (drop `--check` to fix it).
- Use **relative Markdown links** and keep them working.
- Name images `<subject>_<detail>[_<qualifier>].<ext>` (lowercase, `_` between fields, `-` within a field) and record provenance in [`images/README.md`](images/README.md).

## Working with an AI assistant

[`CLAUDE.md`](CLAUDE.md) carries the same rules in the form an AI coding assistant reads at the start of a session, plus fetch tips for sites that block automated access (Fandom, Reddit, GTAForums). Humans can use it as a longer reference.

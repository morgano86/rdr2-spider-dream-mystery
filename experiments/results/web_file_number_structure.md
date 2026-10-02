# Result - web file-number structure & provenance (`web_file_number_structure.py`)

**Question.** Is the WEBS-MANIFEST's per-web `spiderdreamNN` numbering (a) sourced, and (b) structured w.r.t. the KNOWN colour/hour lattice? Tests **[U32]** (provenance) and feeds **[S29]** (the conditional reading). [SPECULATION] at most - see the double-edged note.

> ⚠️ **Provenance flag.** The number→location mapping is **uncited** in the corpus (present since the first commit; no source maps a number to a location) and is **not** the #59 post's *Clockwise Order*. Colour/hour are KNOWN ([K13a]); the per-web NUMBER is the datum under test.
>
> ✅ **ADDENDUM 2026-07-02 - [U32] RESOLVED: the mapping is publicly sourced (C-tier) → [K39].** u/Artem_ab6's datamine comment (master thread, 2026-01-02, src [#65]) maps all 8 numbers to locations on a map overlay **matching the manifest 8/8** - so the numbering is a genuine community datamine, **not** a back-fit by this corpus, and the structure below attaches to real file data ([S29] now live, C-tier). The "likelier back-fit" verdict at the bottom of this file is **superseded** for the by-us reading; back-fit *by the source* remains possible but unfavoured (the comment claims located in-game coordinates; author has a datamine record).

## The manifest numbering (ascending)

| file # | location | code | hour | colour |
|-------:|----------|------|------|--------|
| 1 | Ringneck | BL56 | 5-6 | black |
| 2 | Oil Fields | B56 | 5-6 | black |
| 3 | Cornwall | B34 | 3-4 | black |
| 4 | Emerald | B45 | 4-5 | black |
| 5 | Overflow | B23 | 2-3 | black |
| 6 | Scarlett | R23 | 2-3 | RED |
| 7 | Southfield | R45 | 4-5 | RED |
| 8 | Saint Denis | R34 | 3-4 | RED |

## Structure observed

- **Colour-grouped:** files **1–5 = all 5 blacks**, **6–8 = all 3 reds**.
- **Untwinned 5–6 AM black pair** (BL56/B56) = files **[1, 2]**.
- **Hour-twin pairs sum to 11** (mirror around the 1–8 line):
  - B23(#5) ↔ R23(#6) → sum **11**
  - B34(#3) ↔ R34(#8) → sum **11**
  - B45(#4) ↔ R45(#7) → sum **11**

## Coincidence odds (uniform random labeling of 8 webs → 1..8)

- P(blacks = files 1–5) = 720/40320 = **1/56** ≈ 0.0179  *(= 1/C(8,5) = 1/56)*
- P(+ untwinned blacks at 1–2) = 72/40320 = **1/560** ≈ 0.00179
- P(+ all 3 hour-twins sum to 11) **[full structure]** = 12/40320 = **1/3360** ≈ 0.000298

## Reading (evidence, not fact - [SPECULATION])

The full structure is **1/3360** (~0.03%) under random labeling - **far too clean for** **arbitrary internal asset IDs.** That cleanliness is *double-edged*:

- **(i) genuine datamine + deliberate dev numbering** → a real, striking intent finding (the devs grouped the files by colour and mirror-paired the hour-twins), independently corroborating that **colour is a first-class axis** ([H9]/[U29]/[S28]) and that the §5c hour-twin lattice is **deliberate** (currently [SPECULATION]).
- **(ii) the numbers were back-fit to the KNOWN lattice** by a prior session or a community source → the structure is *circular* (it just re-expresses colour+hour, which we already know) and carries **no** independent evidentiary weight.

Because the mapping is **uncited** and (ii) explains the cleanliness at least as well as (i), this **cannot promote** the colour-axis reading. Its real result is a **corpus-integrity flag**: a datum presented with file-data authority (and propagated into location dossiers) is too structured to be arbitrary and has no citation → **source the datamine number→location mapping,** **or mark the numbers as an assignment.** → [U32]; the IF-genuine reading is held at [S29].
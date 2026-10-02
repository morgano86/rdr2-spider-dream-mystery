# 2026-09-19: Why does spiderdream01x bind val_doc_feather01_ma?: findings

**Task:** none (ad-hoc user question) · **Completed:** 2026-09-19 · **Outcome:** positive **One line:** The Wapiti feather source set ships albedo and normal only — no material map — so the spiderdream feather's `speculartex` slot was filled with `val_doc_feather01_ma`, a flat featureless tile whose only surviving copies in the entire game are the two spiderdream prop dictionaries; and the Valentine doctor's "feather" is a ball of down, not a plumed feather, which is why it can't be found by looking for one.

## Answer

The `spiderdreamNNx` feather material binds three textures from three different source assets:

| slot | texture | source set | size |
|---|---|---|---|
| 0 diffuse | `wap_cs_feather01wap_gen_feather01_a` | Wapiti (`wap_`) | 64x256 BC3SRGB |
| 1 normal | `wap_gen_feather01_n` | Wapiti (`wap_`) | 64x256 BC1 |
| 2 specular | `val_doc_feather01_ma` | Valentine doctor (`val_doc_`) | 128x128 BC3 |

This mixed triple is **unique in the game**. Every one of the ~40 other feather materials in RDR2 uses a self-consistent `X_abal` / `X_nm` / `X_ma` triple from a single source asset (`p_eaglefeather01x_*`, `s_egret_feather01x_*`, `val_doc_feather01_*`, ...), falling back to the generic `blank_ma` when no material map was authored. The eight spiderdreams are the only assets that mix sets, and the only assets in the game that reference the `wap_*feather*` textures at all.

**Why the val_doc one specifically: the Wapiti set has no material map.** No texture named `wap_*_ma` (or any `wap_` material map) exists anywhere in the install — the Wapiti feather shipped as albedo + normal only. The shader still needs `speculartex` bound, so the slot had to point at something, and `val_doc_feather01_ma` was the only other *feather-named* material map available to grab.

**Borrowing it is visually free, which is why nobody cared.** `val_doc_feather01_ma` carries no feather shape and no structure at all: one channel is constant 0 across all 16,384 pixels, another is constant 153, and the remaining two are near-flat (sd 11 and 6 out of 255, i.e. 2-4% noise). It is a constant-value PBR tile. It is also 128x128 square while the feather albedo/normal are 64x256 — it is not even UV-compatible with the feather layout, confirming it is used as a flat constant rather than a matched map. Swapping in any other flat `_ma` would render identically.

**The inversion worth knowing: `val_doc_feather01_ma` does not ship in the Valentine doctor's office.** Its only two copies in the whole install are `jklm_11_14_rd_p_d` and `nopq_11_14_rd_p_d` — the spiderdream regional prop dictionaries. `val_doc_feather01_nm` ships nowhere at all. So the doctor's own feather drawable (`val_doc_backroom_details04_amv`) references a normal map and a material map that were never packaged, and the surviving copy of the material map lives exclusively with the spider webs. The `val_doc_` name is a provenance label from the artist's source library, not evidence that the texture is loaded in Valentine.

**Why there is no findable feather in the Valentine doctor's.** `val_doc_feather01_abval_doc_feather01_al` is not a quill feather — it is a **ball of grey-white down / fluff** (see `tex/val_doc_backroom_details04_amv+hidr__*.png`). It is drawn on 140 of the 229 triangles of `val_doc_backroom_details04_amv`, a combined "back room details" building mesh (the other 58 tris are `val_doc_plaster03_damaged_atlas01`, damaged plaster). The interior is `val_03__interior_val_doctor_int_milo_` at **(-286.211, 809.322, 118.410)**; the detail meshes are MLO room contents, not standalone ymap entities, so they have no separate placement coordinate. Look for wadding/stuffing in the back room, not a plume.

Nothing here is anomalous for mystery purposes: it is ordinary texture-library scavenging, of the same kind already documented for `spiderdream03x`'s dangling `jklm_7_10_rd_p_d` dictionary (7.2% of all archetypes have a dangling `textureDictionary`).

## Evidence

- **Pass A** — all 79,720 `.ydr`/`.yft` in the install parsed (1 failure), 34 s: 91 meshes bind a texture whose name contains "feather". `models.tsv`.
  - Only 8 rows reference `wap_` textures: `spiderdream01x`-`08x`. Nothing else in the game uses the Wapiti feather textures.
  - Control group: the other ~40 distinct feather materials, every one a matched `X_abal`/`X_nm`/`X_ma` triple (or `blank_ma`). This is what makes the spiderdream triple's mismatch meaningful rather than a naming quirk.
- **Pass B** — all 88,378 `.ytd` in the install parsed (1 failure), 70 s: 288 textures named `*feather*`. `ytds.tsv`.
  - `wap_cs_feather01wap_gen_feather01_a` and `wap_gen_feather01_n` exist **only** in `jklm_11_14_rd_p_d` and `nopq_11_14_rd_p_d`, not in any Wapiti dictionary.
  - **Zero** `wap_*` material maps exist (the only 4 `wap_` rows are those 2 textures x 2 dictionaries). This is the load-bearing negative, and it is over every `.ytd` in the install, not just base packs.
  - `val_doc_feather01_ma` exists only in those same two dictionaries; `val_doc_feather01_nm` exists nowhere; `val_doctor_int`'s own dictionaries contain only `val_doc_feather01_abval_doc_feather01_al`.
- **Pass C** — 225 PNGs dumped to `tex/`. Channel statistics via `PIL` over `val_doc_feather01_ma`: R constant 0 (sd 0), A constant 153 (sd 0), G mean 236.29 sd 11.19, B mean 250.91 sd 6.01. Both dictionary copies are statistically identical. (Note the dump goes through `Format32bppArgb`, so PNG channel order is the texture's BGRA; the flatness conclusion is order-independent.)
- **Pass D** — 8,023 ymaps walked: `val_doctor_int` at (-286.211, 809.322, 118.410), ymap `val_03__interior_val_doctor_int_milo_`. The `val_doc_*` detail archetypes appear in no ymap entity list (MLO room contents).
- Consistent with the earlier `SpiderSize` result (`completed/2026-07-23-spiderdream-fragment-diff.md`): the 4 textures in each regional dictionary are these 3 plus `blank_mb`, and `spiderdream03x` embeds its own copies because `jklm_7_10_rd_p_d` was never shipped.

## Method and tools

`tasks/tools/feathertex/` — `feathertex.exe` runs passes A-C (~2 min total), `feathertex.exe pos` runs pass D (~1 min). Console harness per `.claude/docs/rdr2-diag-harness.md`; build with MSBuild at `C:\Program Files\Microsoft Visual Studio\18\Community\MSBuild\Current\Bin\amd64\MSBuild.exe` (note: VS **18**, and `/t:Restore` on first build). Outputs: `models.tsv`, `ytds.tsv`, `tex/*.png`, `run.log`.

Reusable beyond feathers: both passes filter on a single `IsFeather(name)` predicate in `Program.cs` — change that one function to census any texture-name family across every model and every texture dictionary in the install.

## Caveats and blind spots

- The sweep covers textures *packaged* in `.ytd` dictionaries. A texture supplied at runtime by another system (ped/clothing pipelines, cutscene-specific dictionaries loaded by name) would not appear; the `wap_*_ma` negative is about the shipped map/prop texture set.
- "The Wapiti set has no material map" is a statement about what shipped, not about what the artist had in their source tree. The reason the spiderdream author reached for a *feather-named* `_ma` rather than `blank_ma` (which other feather assets do use) is inference from the naming, not established fact.
- The identification of the Valentine down-ball as wadding/stuffing is from the texture image and the 140-tri mesh share; the object was not rendered or located in-game. Its exact identity in the back room is unconfirmed.
- `wap_cs_feather01wap_gen_feather01_a` is read here as the blended-texture idiom (`tasks/tools/dockside/`, `<A>` + `<B>_a`), pairing a Wapiti cutscene feather with a Wapiti generic feather. The blend split for this particular suffix form (`_a`, not `_ab`/`_al`) was not independently verified.
- Contrary to `.claude/rules/` guidance for mystery provenance work, this scan read all archives, not base packs only. Every hit landed in `levels_1.rpf` / `levels_3.rpf`, so the positive findings are base-pack facts regardless; the negatives are correspondingly stronger.

## Follow-ups

None raised. `wap_cs_feather01`, `wap_gen_feather01_a/_n` and `val_doc_feather01_ma/_nm` are plaintext texture names read from shader params, not cracked joaat hashes, so the strings-file rule does not apply.

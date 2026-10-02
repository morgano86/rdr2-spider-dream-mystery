# Results - `couples_match.py` (run 2026-07-05)

**Question:** do the `+`-styled markings (`J+M`, `S+J`) name documented in-game **couples** by first-name initials - the test the lovers'-styling readings ([S2]/[S3]) actually predict, never run before (all prior name tests matched *individuals*)? Couples list: 14 wiki-documented pairs (source [#86]; non-exhaustive).

## Output (verbatim summary)

```
LJ   [bare] -> no documented couple
SM   [bare] -> no documented couple
EC   [bare] -> no documented couple
J+M  [PLUS] -> HIT  Joshua Burgess + Miriam Wegner  (EMERALD RANCH (web B45); lover shot dead Aug 1898; Miriam confined since)
S+J  [PLUS] -> HIT  Jake Adler + Sadie Adler        (married 1896-09-07; Jake murdered by O'Driscolls May 1899)

'+'-styled markings matching a couple: 2/2
bare markings matching a couple:       0/3

Partner-reshuffle null (seed 0, N=200,000):
  P(both J+M and S+J pairs appear)            ≈ 0.114
  P(≥2 of the 5 marking-pairs appear)         ≈ 0.535
  P(exactly the two '+' pairs, no bare pair)  ≈ 0.054   (post-hoc statistic)
```

## Read

- **The initial matches alone are cheap** (p ≈ 0.11; J is the commonest initial in the pool - the [S16] lesson applies). The weight is **structural**, outside the null:
  1. **Styling alignment:** the two markings drawn *with* the lovers' `+` are exactly the two with canonical couple readings; the three bare ones (`LJ`, `SM`, `EC` - bareness image-verified for `EC`) have none. The styling rule was fixed before the couples were sought.
  2. **Thematic coherence:** both hit-couples are **tragic** - the man violently killed (Aug 1898 / May 1899), the woman left grieving (Sadie) or confined (Miriam).
  3. **Geography:** Joshua+Miriam *are* the Emerald Ranch story - **web node `B45`** - and the single in-game document narrating them (*Letter to Miriam Wegner*) spawns in the abandoned mail wagon **southwest of Fort Wallace** ([K16], the trail frontier).
  4. **Control negative:** Beau Gray + Penelope Braithwaite ({B,P}) - the flagship forbidden lovers at the very estates the markings inhabit - match **no** marking. Cooper + Lilly ({C,L}, the *other* Emerald Ranch couple) also match no marking.
- **Coverage cap (logged):** RDR2 has no canonical couples registry; the 14-couple list is main-cast romances + sourceable named minor couples. A missed couple can only *add* matches.
- **Status:** → **[S45]**, [SPECULATION]. Home write-up: [thread 03](../../threads/03-matchstick-letters.md).

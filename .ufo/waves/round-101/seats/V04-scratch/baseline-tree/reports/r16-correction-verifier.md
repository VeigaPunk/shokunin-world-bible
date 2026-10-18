# Round 16 correction verifier — independent replay

Role: non-author verification of the three description-only corrections. I made no source or fixture edits; this report is the only file I wrote.

## Description and hash checks

- Recomputed SHA-256 for each current `timeline.json`. All three equal the **new** hashes in `r16-correction.md`: `r16-missing-place` `137cf89d8bca5b22abaf607d779fad4cd48e184ca8bcdec40e693c6a049aa735`; `r16-missing-first` `f3324c998e4eff6369d256ded3f007adb0e013d81e55e34102366bbea7a6c55a`; `r16-mixed-three` `1306b1ce1469448bef4f56e98608543d89a360d63c3c1ba14147928779108345`.
- Read each changed row. The current descriptions state that `unlisted` is an unresolved place ID and do not assert Harbor or Tower. The unchanged control rows in `r16-missing-place` and `r16-mixed-three` still explicitly describe Lantern Harbor and North Tower with their corresponding `harbor` / `tower` IDs.
- The old hashes and old prose are recorded in the correction report, but I could not reproduce the **old** hashes from historical file bytes: no pre-correction copies of the three newly introduced fixture timelines were available in the baseline commit or saved run directory. Thus old→new provenance is partly dependent on that report; current/new hashes are directly verified.

## CLI replay

Ran the current checker with Python against every current fixture directory, capturing exit status, stdout bytes, and stderr bytes independently. All **33/33** match the corresponding saved transcript in `corpus/live/runs/20261012T182817Z/` (including all three corrected fixtures).

Extracted the checker at baseline `3995486def3c9fceb95449362f6e8dab8cc130f7` and replayed it alongside the current checker against the **29 baseline fixture directories**. All **29/29** have identical exit status, stdout, and stderr between baseline and current checker.

Current checker SHA-256 is `bf2061b5c6f4e5f67f6c6f8dfbe31b0141c9541e259fe4ddf333aebef92b19b6`. The baseline checker has a different hash; that is pre-existing checker evolution, not a result of this prose correction. The prior `r16-independent-verifier.md` reports hashing checker plus fixture JSON files before/after its replay and finding identical maps, but that prior run is not a pre-correction snapshot for these newly added fixtures.

## Fixture/checker integrity scope and limits

- Compared all **144 JSON paths** present in baseline fixture tree `3995486...` to current bytes: all match. Current fixture tree has 164 JSON files, including 20 files in the four newly added round-16 fixtures; there are no baseline copies for those additions. The checker and all 164 current JSON files total 165 files now. This baseline comparison confirms the old shared fixtures were untouched, but cannot demonstrate pre-correction contents for new fixtures.
- The 33-case transcript match establishes reproducibility against the saved 18:28:17Z run; it is not proof of narrative/source truth. The prose correction avoids claiming that `unlisted` means Harbor or Tower; it does not establish what place, if any, the unresolved ID denotes. No broader canon conclusion is made.

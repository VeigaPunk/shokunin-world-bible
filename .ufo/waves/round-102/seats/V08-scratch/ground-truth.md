# V08 ground-truth ledger (pre-sweep independent measurements)

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless stated. Measured 2026-10-18 06:19–06:35 -03:00, tree at HEAD `8fa2e87` (r102 declaration), tracked files clean except untracked `.scratch/` + one r98 wave file.

## A. Current byte pins (sha256sum, measured)

- `corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` ✓ matches C9 watch + r98/r99/r100 notes
- `corpus/tools/support_check.py` → `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` ✓
- `corpus/tools/map_obligations.py` → `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` ✓ (r97 delivered)
- `corpus/tools/map-obligations-contract.json` → `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` ✓
- `corpus/tools/dependency_freeze.py` → `60a78bc39440917202488e4f6366a26540aeb494a089e5793864c1a4992fe3bf` (== `git show 542021a:` r101 closure; pinned in NO knowledge note)
- `corpus/tools/dependency-freeze-contract.json` → `b8fc63c3500d626df8d5c34b28327c10716610512a3c72ef56a19f3b46de36ca` (== 542021a; unpinned in notes)
- `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` → `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` ✓ matches r97 note post-repair pin

## B. Commit tokens resolved via `git log --format='%h %s' -1 <t>`

Exist: e97613c(r89 close), ca7f9ef(r90 wave), 1b09f3f(r89 wave), 2ea9ef1(r88 wave), 2b48ca7(r87 evidence), c2ab3d0(r91 C3), a7c6a17(r90 close), 4265df5(r98 freeze), 51b286b(r88 close), ac69044(r94 land), 6332115(r91 wave), 5eb9451(revert), 8e5a68d(r93 deepseek), 28706dc(sync), 7a3a795(r93 replay), 65838f8(r93 wave), 03c6746(r87 C1), e4708cb(r87 C3), dcb2d92(r95 freeze), 9c2eea3(r93 close), 9a3d648(r97 scratch-drop), fe1ce46(r99 freeze), 337f0fa, 396c568, 4780cf0, 542021a(r101 close), 65a9329, 6f86bf2(r100 freeze), 87779a0, 9d25df9(r97 freeze), abbc3e0, ae67105, b5fe472(r100 declare), c4d4823, ceeef43, dfd1fbc, ebec6bb, f3e09f9(r96 freeze), fb118c4, fc2c3cc, a04f986(r100 close).

Not objects in this repo (historical/out-of-repo, verified `git cat-file -t` → fatal): 596f70e(r84 archive), 585a00f(r54 archive), e9324f6(r82/83 archive), e810eb0(r43 archive), 793a3a8(r39 archive), 0aa51a0(r83-era work commit), 49ac1a5(kotodama external lane ref), c65ac3bd(r96-era contract pin), d1c239cc(r95 map_obligations pin — see D), 9224a684(r95 in-flight map pin), 6634e176(r96 in-flight map pin), 8173bb97(r95 contract pin — see D).

## C. Command re-runs (quoted command → observed)

1. `sha256sum corpus/fixtures/check_bible.py` → ff9fd2aa…d1421 ✓
2. `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression`, exit 0 ✓
3. `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved`, exit 2 ✓
4. r101 note's exact relations.json receipt (heredoc over 7 fixtures) → all seven `c279254bc7de0636 139` ✓
5. `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 19/19`, `RESULT PASS`, exit 0; case 19 = repointed_edge ✓
6. freeze chain loop (8 fixtures r88…r100) → 8/8 exit 0 ✓; contract `pins` keys = exactly those 8
7. `python3 corpus/tools/boundary_doc_check.py` → 4 CHECK PASS lines, replay_receipts=3/3, replay_cases=14/14, anchors=2/2, `CERTIFIED (bounded: …)`, exit 0 ✓
8. `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse` → `FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1`, `DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`, `RESULT PASS`, exit 0 ✓ (matches r100 note's receipt+digest)
9. r93 worked-example digest block (98-line heredoc extracted verbatim from note) → `R8 replay: PASS`, `record cells: 12/12`, `canonical record SHA-256: da934a7eea6d108f60c71534e8beb218a532eb55b20217a04ab86d82bc6c7e05`, exit 0 ✓; note's first check block → 5/5 fields PASS exit 0 ✓
10. `python3 corpus/tools/support_check.py corpus/fixtures/{r95,r96,r97}-*` → JSON-FACTS 15/16/17, TOTAL-ROWS 17/18/19, `RESULT PASS`, exit 0 each ✓
11. `python3 corpus/tools/map_obligations.py corpus/fixtures/{r95,r96,r97}-*` → `raw=15/16/17 mapped=15/16/17`, `RESULT PASS`, exit 0 each ✓
12. `python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 ✓
13. Fixture-dir census: `ls -d corpus/fixtures/*/ | wc -l` → 174 ✓

## D. Historical pins reproduced via `git show <commit>:<path> | sha256sum`

- 51b286b:check_bible.py → `dcacffd6981e1af5` ✓ (r88 checker, holder-assessment-boundary.md claim)
- e97613c:check_bible.py → `e2bb9639a3247284` ✓ (r89 checker, same file's claim)
- dcb2d92:map_obligations.py → `d1c239ccb2140449` ✓; dcb2d92:map-obligations-contract.json → `8173bb97592a3777` ✓ (r95 delivered, as r95/r96 addenda state)
- f3e09f9:map_obligations.py → `2b0ba815326b1cb3` ✓; f3e09f9:contract → `97b76bb8b1fea97f` ✓ (r96 delivered, as r96 addendum states)
- fe1ce46:dependency_freeze.py → `fb9bb9ff608c3333` ✓ (r100 note's at-pass tool); a04f986(r100 close):contract → `ea012b9c362bac36` ✓ (r100 note's contract)
- 4265df5:dependency_freeze.py → `03d04365cf00903e` ✓; 4265df5:contract → `153ebc5b2092948e` ✓ (r98 delivered, as r98 addendum/r99 table state)

## E. Known open freshness items for the sweep to address

1. Current freeze tool/contract pins (60a78bc3 / b8fc63c3) appear in NO knowledge note; r98 note's "landed shortly after (03d04365…, c435239d…)" line-64 mention is in-flight, corrected in-file at lines 77–79 (delivered r98 = 03d04365 + 153ebc5b) and LOG:3164.
2. C9 watch (`r91-c9-watch.md`): re-check 10 at r101; "Next re-check: r102" — the due r102 re-check (11th) must land at closure (U2-owned addendum or waiver).
3. Historical-vs-current classification needed for: 596f70e, 585a00f, e9324f6, e810eb0, 793a3a8, 0aa51a0, 49ac1a5, c65ac3bd, 9224a684, 6634e176, 8173bb97, d1c239cc, fb9bb9ff/ea012b9c, 03d04365/153ebc5b/8c2561b0, 70795150, 5093d72e, e8f24162, 88c9b1d0 (r82-era checker).
4. `corpus/knowledge/r96-response-scope-note.md:55` receipts paragraph pins `d1c239cc…`+`8173bb97…` (r95) — the file's own addendum (:65,:75) already corrects these as historical; sweep must confirm, not re-correct.

## F. Poll record

- Window 1 (40 × 20s): ABSENT at 06:31:47 (seats dir existed with V11/V13 reports + U1 scratch; no U2 report, no sweep).
- Window 2 (bounded stall-escape, 40 × 20s max): running, started ~06:32.

# V02 — c1-deltas (round 102, capstone)

- lane: lore-shokunin; round 102; seat V02 (verifier, C1 delta table); model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- target: `corpus/knowledge/r102-push-synthesis-r95-r102.md` §2 per-round capability-delta table vs the SCORECARD r94–r101 closed sections
- baseline r101 closure `542021a`; no commits, no pushes, no network; read-only except this report
- method: independent re-derivation of the delta table from `SCORECARD.md` lines 385–663 FIRST, then 1:1 comparison against the delivered synthesis, then ground-truth spot checks of every statically checkable side-claim

## Poll record

- Protocol window: 40 tries × 20 s — synth=n ledger=n U1report=0 on every try (tries 28–40 matched the `U1-scratch/` directory via a too-loose `grep '^U1'`; corrected to `U1-*.md` in the escape windows).
- Bounded stall-escape 1 (recorded, not fatal): 15 tries × 20 s — `r102-debt-ledger.json` landed at escape-try 8 (06:39); synthesis still absent at try 15.
- Bounded stall-escape 2 (recorded): try 1 → both artifacts present: `r102-push-synthesis-r95-r102.md` 15,803 B (06:41), `r102-debt-ledger.json` 122,763 B (06:39); producer report `U1-synthesis.md` landed 06:42. Verification then proceeded on the delivered bytes.

## Re-derived delta table (from SCORECARD, before reading the synthesis)

| Round | depth | coverage | calibration | operability | freshness | adjacency | capability / census |
|---|---|---|---|---|---|---|---|
| 94 | improved | improved | improved | improved | unchanged | unchanged (PASS) | 5th registry row map_obligations; 4/0/2→5/1/3; 167→168 |
| 95 | improved | improved | improved | improved | unchanged | unchanged | r88 dialect gated; 5/1/3→5/1/4; 168→169 |
| 96 | improved | improved (6th gate dependency_freeze, 14 cases, BR-01 JSON half) | improved | improved | unchanged | unchanged | 5/1/4→5/1/5; 169→170 |
| 97 | improved | improved (freeze hardened 14→16) | improved (case 25; strict loader) | improved | unchanged | unchanged | 5/1/5→5/1/6; 170→171; V12/V46 FAILs stand |
| 98 | improved (5/1/6→6/1/7) | improved (chain six 6/6) | improved (case 17 exit 2) | improved | **improved (first on record)** | unchanged | 171→172 |
| 99 | improved (6/1/7→6/1/8 + blind-spot table) | unchanged | improved (ten-file schema-2, 18/18) | improved | improved | unchanged | 172→173 |
| 100 | improved (6/1/8→6/1/9 + dossier) | improved (chain seven 7/7) | improved (boundary note; rows 10–12) | unchanged | unchanged | unchanged | 173→174 |
| 101 | improved (R10 first worked entry) | improved (chain eight 8/8) | improved (repointed_edge 18→19) | unchanged | unchanged | unchanged | census 174 unchanged |

## 1:1 comparison result — table matches, no overstated delta

Every §2 row (r94–r101) was compared cell-by-cell against its SCORECARD section: models/seats (r94 32+40 with 31/32 usable; r95 5P+59V; r96/97 6P+58V; r98 64+6 hyper; r99 128; r100 4P+30V erratum 32→34; r101 2P+28V erratum 28→30), commits, claims (fixture e/r/e chains 4/0/2→…→6/1/9; obligations 14→22; self-test progressions map 20→22→24→25 and freeze 14→16→17→18→19), all six admitted per-axis verdicts per round, and the capability column (5th gate r94, 6th gate r96, first freshness improvement r98, chain 4→6→7→8, census 167→174). **All cells match. Zero overstated deltas found** — no cell claims a verdict, count, or capability its SCORECARD section does not carry. The §2 preamble census (174) and §1 arc facts (models, errata, `337f0fa` blocked attempt, hyper completion, alias deviation) also match.

Conservative notes (not overstatements): row 94 renders depth "improved (bounded)" where SCORECARD says "improved" (stricter); row 100's commit cell omits pre-dispatch `b5fe472`/`ae67105` (both present in the §4 hash list).

## Ground-truth checks (commands and observed outputs)

- All 24 §4 hashes: `git cat-file -e <h>` → OK for every one of `9c2eea3 abbc3e0 65a9329 ac69044 fb118c4 dcb2d92 60dba0c f3e09f9 2393934 9d25df9 9a3d648 4265df5 111b9a3 337f0fa fe1ce46 ae67105 b5fe472 6f86bf2 a04f986 ebec6bb ceeef43 542021a 60e88bf 8fa2e87` (60dba0c/2393934/111b9a3/a04f986 = the r95/r96/r98/r100 SCORECARD closure commits). §4's "every one answered OK" is TRUE.
- Census: `find corpus/fixtures -maxdepth 1 -mindepth 1 -type d | wc -l` → **174** ✓.
- Freeze contract `pins` keys → exactly 8: r88-m3-maya-cluster, r94, r95, r96, r97, r98, r99, r100 ✓ (§3 chain list exact; no `corpus/fixtures/r101-*` dir exists, consistent with r101 "census 174 unchanged").
- SKILL.md Gate registry: `grep -n '^### '` from the registry heading → exactly **5** rows (Boundary-document check, Checker regression discriminator, Claim-to-excerpt lexical support, Raw-obligation mapping completeness, Dependency-edge freeze check) → §3's five-rows-plus-check_bible counting reconciliation is correct.
- SHONEN: `grep -c '\[~\]' SHONEN.md` → 4; `grep -c '\[x\]' SHONEN.md` → 0 ✓.
- Checker pin: `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` present verbatim in `corpus/tools/boundary-doc-contract.json` ✓.
- r99 "5P+123V": `.ufo/waves/round-99/receipt.json` `collection_snapshot.producer_present = ['S1','S2','S3','S4','S5']`, reports 128/128 ✓ (not in SCORECARD; verified from the receipt).
- r95 late landings: V33, V59, V57 all named in the r95 receipt ✓. V34's eleven standing FAIL seats (V03 V14 V16 V23 V55 V63 V85 V95 V105 V107 V110): all eleven names present in `.ufo/waves/round-99/seats/V34-adjudicator.md` ✓.
- "six authored continuations" (§5.12): `r100-crossing-arc-synthesis.md:8` itself defines six continuation beats r95–r100 after the r94 minute (seven snapshots; r88 register = precursor) — the synthesis matches the dossier's own framing; consistent, not flagged.
- Ledger cross-refs quoted by the synthesis §1: items=264, carry_records=97, totals.source_entries=361 — match the delivered arrays and `totals` ✓.

## Flags

- **F1 (defect, non-blocking, numeric):** §5.9 says "**46** debt items carry past the lane (of 264 consolidated)". The ledger says **45**: `totals.dispositions.carried = 45`, and my direct count of `disposition=="carried"` over `items` = 45 (with `carried_owner: "r103+ (operator; lane closes at r102)"`). U1's own seat report also states 45. Off-by-one in the synthesis doc only; direction is against the lane's interest (overstates carried debt), not a capability overstatement, and the §2 delta table is untouched.
- **F2 (cross-finding → route to the C2 seat):** the ledger's own `bottom_line` string reads "**273 items + 88 carry records** = 361 source entries accounted", contradicting the same file's `totals` (264/97/361) and its arrays (len(items)=264, len(carry_records)=97). Both partitions sum to 361; the string is internally inconsistent with the delivered data it summarizes. The synthesis quotes the correct 264/97.
- **F3 (observation):** §5.7 "r101's fixture is unpinned" — r101 added no fixture (census 174 unchanged; no `corpus/fixtures/r101-*`). The underlying fact (chain stops at r100) is correct; the phrasing presumes a nonexistent r101 fixture.
- **F5 (evidence, already recorded by U1/ledger):** the r102 LOG C2 declaration cites "r100 V33" as a source ledger; no V33 seat or debt file exists in round-100 (surface = V29 conditions + FAILs). The synthesis header correctly cites `V29-adjudicator.md` for r100. LOG wording defect is outside my byte-ownership.

Honest boundary: §3's "this pass" gate re-runs (map 25/25, freeze 19/19, chain 8× RESULT PASS, boundary CERTIFIED, sha256 pin reproduction) are producer-attested; I did not re-run the gates to avoid writing outside my declared scratch. Every statically checkable counterpart was verified and matches (case-count progressions vs SCORECARD, pin count = 8, registry rows = 5, pin digest string, census 174).

## Bottom line

PASS — the synthesis §2 per-round capability-delta table verifies 1:1 against SCORECARD r94–r101 with no overstated delta; one numeric prose defect flagged in the synthesis (§5.9 "46" vs ledger 45 carried) plus one cross-finding for the C2 seat (ledger `bottom_line` 273/88 vs its own arrays/totals 264/97).

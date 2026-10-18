# V16-verdict-calibration — round-102 seat report (verifier, CALIBRATION verdict on C2 debt consolidation)

- lane: lore-shokunin; round 102 (CAPSTONE, final round); seat V16 (verdict-calibration); model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r101 closure `542021a`; HEAD at seat start `8fa2e87` (r102 declaration); wave tree uncommitted per round convention; no commits, no pushes, no network, no nested agents
- assignment: read the C2 seats; issue ONE calibration verdict (debt consolidation) with bounds
- writes: this report + declared scratch `.ufo/waves/round-102/seats/V16-scratch/` only; everything else read-only (all repo invocations were greps/reads/`git cat-file`/`sha256sum`; no producer byte touched)
- artifact under verdict: `corpus/knowledge/r102-debt-ledger.json`, sha256 `70fbed21d45ecf2ed1840d87cd6bfdf0a6a14947c646e8cd8dc7d1829fd2194d` (122,763 bytes) — identical hash to the revision V07-c2-json pinned, so both seats verified the same bytes

## Axes named

accuracy (per-source counts and dispositions vs the source ledgers), coverage (no silent drops), evidence (pointers resolve and spot-check true).

## Poll record (poll-wait protocol; ENDGAME: SELF never counted)

- 06:19–06:28 — wave dir and producer artifacts absent; built the verification rig while waiting (source inventory, below). Polls 1–5.
- 06:28:42–06:40:26 — content-gated loop at 20 s: gate = `U1-*.md` + `U2-*.md` in `seats/` AND `corpus/knowledge/r102-debt-ledger.json` + `r102-freshness-sweep.md`. `r102-freshness-sweep.md` landed 06:35:38; U2 report 06:36:18; `r102-debt-ledger.json` landed 06:38:25 (~try 34/40). **U1's report was still ABSENT at the 40-try cap (06:40:26) — bounded stall-escape recorded (9 further tries to 06:44), not fatal: the artifact of record existed.** U1-synthesis.md landed ~06:44 and was read before this verdict was finalized. Both producer reports and both artifacts are present at write time.

## Source-side inventory (built independently BEFORE reading the ledger)

Normalized inventory of every r94–r101 debt surface, extracted to `V16-scratch/source-inventory.json` by `V16-scratch/build-inventory.py` (reads only):

```
r94-F29          51  .ufo/waves/round-94/followup/F29-debt.md        (14 CC + 28 BR + 8 CR + 1 S; matches F29 bottom line)
r95-V31          51  .ufo/waves/round-95/seats/V31-debt.json         (NB 14, CO 23, CL 10, PR 3, ST 1 — item_counts field)
r96-V40          63  .ufo/waves/round-96/seats/V40-debt.json         (NB 27, CO 10, CL 12, PR 8, ST 6)
r97-V37          70  .ufo/waves/round-97/seats/V37-debt.json         (NB 20, CO 18, CL 12, PR 13, ST 7)
r98-V33          63  .ufo/waves/round-98/seats/V33-debt.json         (12 NB + 21 carried + 10 CL + 13 PR + 7 ST)
r99-V36          42  .ufo/waves/round-99/seats/V36-debt.json         (16 NB + 16 bucket entries + 10 CL)
r99-V74          42  .ufo/waves/round-99/seats/V74-debt-2.md         (11 NB + 11 CO + 9 CL + 6 PR + 5 ST rows)
r100-LOG-notes   11  LOG.md Round-100 closure (6 AC + 3 FAIL + 2 QUAL)
r101-V24-notes   10  .ufo/waves/round-101/seats/V24-adjudicator.md   (6 defects + 4 AC)
TOTAL           403
```

Two claim-text facts established from the sources before opening the ledger: (1) the C2 declaration's falsifier list cites "**r100 V33**" — no V33 seat or debt file exists anywhere in round-100 (roster T1–T4 + V01–V30; `find` over round-100/101 returns no V33 outside r101 scratch mirrors) — a phantom citation; (2) the same list omits r99's **second** debt extraction, `V74-debt-2.md` (V74's own words: "independent debt extraction … merged against V36"; "NB-17 is new").

## Verification 1 — no-drop coverage (mechanical, all 403 source rows)

Method: for each source row, the ledger must contain it as a tracked item (`r94-CC-01` dash form), a carry_record (`r95:CO-01` colon form), or a carry `tracks` target. Result:

- **Every row of the eight declared sources is accounted: 361/361.** r94 51 items; r95 24 own + 27 carry; r96 51+12; r97 50+20; r98 42+21; r99-V36 25+17; r100 11 (`r100-AC-ROSTER`…`r100-FAIL-V15`…`r100-QUAL-V30`); r101 10 (`r101-DEF-1…6`, `r101-AC-1…4`). Aggregate identities verified: Σown = 264 = len(items); Σcarry = 97 = len(carry_records); 264+97 = 361 = Σ items_in_source; dispositions closed 111 + addressed 108 + carried 45 = 264.
- **The V74 surface does NOT fully reconcile: 12 of its 42 rows have no ledger entry.** Present by id-sharing: 30 rows reuse V36's id space. Absent entirely: `NB-17`, `PR-01`, `PR-02`, `PR-03`, `PR-04`, `PR-05`, `PR-08`, `ST-01`…`ST-05`. Of these, PR-02 (V36's ABSENT window) and ST-05 (`1728ed89` MALFORMED-JSON) have substance covered elsewhere (r99-NB-01, r99-NB-11). **The rest are silent drops**, worst first:
  - **NB-17 / its closure-item twin CL-08 — the only genuinely new actionable debt in V74 — is recorded nowhere.** Substance: contract `data_files` still lists the five JSON tables and `pinned_files` lists ten; the tool does not read `data_files` (owner "r99 closure or r100"). Evidence:
    ```
    $ grep -c 'data_files' corpus/knowledge/r102-debt-ledger.json → 0
    $ grep -n 'data_files\|pinned_files' corpus/knowledge/r102-push-synthesis-r95-r102.md corpus/knowledge/r102-freshness-sweep.md corpus/tools/README.md SKILL.md → no output
    ```
    The ledger's anomaly-2 claims V74 was "merged into trails" but names its additions as only "poll record, delivered hashes, C1 re-run" — the NB-17/CL-08, CL-09, PR, and ST rows are dropped without a waiver record. That is exactly what "silently dropped" means.
  - **V74 CL-09** ("rows 1b and row 7 were not replayed by this seat") — different substance from V36's CL-09 ("roster reconcile"); `grep -c 'row 1b' ledger` → 0. A caveat item dropped.
  - **V74 PR-01/03/04/05/08** (content gate held; two recorded stall-escapes; reports landing after verifier caps; no all-reports wait; host-timeout resume) — the ledger's own counting rule 2 counts PR rows as items in r95/r96/r97; zero r99 PR rows exist. Inconsistent convention application; `grep -c 'existence poll\|host timeout\|all-reports'` → 0 each.
  - V74 ST-01…04 are pure status notes (weakest class) — unrepresented, folded under no trail.

## Verification 2 — internal consistency and defects

- Every one of the 264 items carries `disposition` + non-empty `evidence`; all 45 carried items carry `disposition_detail`; `carried_owner` present on 44/45 — **`r97-NB-20` has none**, violating the vocabulary's own field contract ("carried_owner names the holder"); its detail defers to the tracked r94-BR-17 class, so substance survives by reference.
- **The file's own `bottom_line` contradicts its `totals`:** `"273 items + 88 carry records = 361 source entries"` vs totals/items/carry_records 264/97/361. Grand total consistent; the narrative split is stale or wrong.
- Counting rule 1 (carry_records "mirrored into the tracked item's trail") is only partially implemented (38/264 items have trails) — non-arithmetic residue, corroborated by V07 D3.

## Verification 3 — disposition spot-checks (commands + observed outputs)

- `git cat-file -t ac69044` → `commit` (r94-CC-01/CC-10 closure evidence resolves; "lore r94: land admission conditions C-1..C-4,C-6…").
- `grep -c 'README.md:11\|README:11' corpus/knowledge/r101-r10-register-first-entry.md` → `3` (r101 DEF-1/AC-1 "addressed" is true: the wrong locator was repaired in place).
- `grep -c 'schema_drift' corpus/tools/map_obligations.py` → `3`, and tools README:161 documents the persisted 24-case contract incl. `schema_drift` (r96 closed item true).
- `grep -c 'Round-98\|Round 98' corpus/fixtures/README.md` → `4` (r98 closure items landed).
- Ledger's self-recorded anomalies corroborate my independent finds: the "r100 V33" phantom (I established it from the roster before reading the ledger) and the unlanded r98 CL-10 (honest non-close, carried under the BR-17 class).

## Seats read

`U1-synthesis.md` (producer, post-cap landing), `V07-c2-json.md` (C2 verifier — its D1/D2/D3 are exactly my bottom_line/r97-NB-20/trail findings; no contradictions; its scope was arithmetic/schema, mine is source coverage), plus the LOG r102 declaration. No cross-seat contradictions witnessed.

## CALIBRATION VERDICT (one, with bounds)

**Calibration: IMPROVED — bounded, not clean.** The debt-consolidation capability measurably improved: eight rounds of scattered ledgers are consolidated into one machine-readable, self-describing, honest record whose every declared-source count I reproduced independently (361/361), whose dispositions all carry evidence, and whose spot-checks hold against the delivered tree. It self-records the two anomalies a skeptic would raise (the phantom "r100 V33" citation; the unlanded r98 CL-10) instead of smoothing them. That is a real calibration gain over the r94–r101 state, where each round's ledger re-numbered and re-disposed of its predecessors with no single reconciled view.

Bounds (explicit):

1. **The claim's "no item is silently dropped" clause is FALSIFIED IN PART.** 12 ids of the r99 V74-debt-2 surface have no ledger entry; one of them (NB-17/CL-08, the `data_files` vs `pinned_files` contract mismatch) is an actionable, owner-named debt absent from every r102 knowledge surface (ledger, synthesis, freshness sweep, tools README, SKILL — all grep-zero). Strictly, C2 verifies only with this recorded exception; the drop is ~3% of source rows and none of it retro-harms a prior round's admission.
2. The claim's own anchor list is defective twice: "r100 V33" does not exist (phantom), and the V74 second ledger is uncited while being the source of the drops in bound 1.
3. The artifact contains an internal contradiction (bottom_line 273/88 vs totals 264/97) and one vocabulary violation (r97-NB-20 without `carried_owner`) — cosmetic to the arithmetic, material to a document whose purpose is exact accounting.
4. Spot-checks are samples (4 dispositions verified to substance, 1 commit, 1 locator repair), not a full audit of 264 dispositions; coverage was checked mechanically by id, and id-equal rows with changed substance (V74 CL-09 class) can only be caught by reading.
5. U1's seat report landed after my 40-try cap (bounded stall-escape, recorded); it was read before this verdict was finalized and reconciles with the delivered bytes.
6. Adjacency: I wrote only this report and `V16-scratch/` (inventory + builder script); all other reads were read-only.

**Bottom line: PASS — calibration improved (bounded): the r102 debt ledger reconciles 361/361 against every declared source with honest dispositions and resolving evidence, but the "nothing silently dropped" clause fails narrowly for the uncited r99 V74 surface (12 ids, incl. the data_files/pinned_files debt recorded nowhere in the round), and the artifact carries a self-contradicting bottom_line split (273/88 vs 264/97) plus one missing carried_owner — all recorded here as bounds, none axis-harming.**

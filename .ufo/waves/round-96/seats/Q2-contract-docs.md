# Q2 — contract-docs (C1(b) self-test pinning + `corpus/tools/README.md` addendum)

**Seat:** Q2 (producer; exclusive byte-owner of `corpus/tools/map-obligations-contract.json` and `corpus/tools/README.md`)
**Wave:** round-96, single-wave 64-seat swarm (6 producers + 58 verifiers)
**Baseline:** r95 closure `dcb2d92`
**Status: PASS**

Owned writes (only these two corpus files):
- `corpus/tools/map-obligations-contract.json` — sha256 `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6`
- `corpus/tools/README.md` — sha256 `965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24` (119 → 169 lines)

Reference: Q1's delivered tool `corpus/tools/map_obligations.py` sha256 `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (matches Q1's report; unchanged through all runs below).

Scratch: `.ufo/waves/round-96/seats/Q2-scratch/` (battery transcript `battery-after.txt`, self-test transcript `selftest-24.out`, demo copies `demo-del`, `demo-dup*`, draft `addendum-draft.md`). No commits, no pushes, no network.

## Poll-wait on Q1

Protocol: 20 s cadence, 40 tries, requiring the tool to contain `inventory_mismatch` + `dual_pointer` AND Q1's report to exist.

- Poll hit on try 27 (`POLL_HIT i=27 tool-updated q1report=.ufo/waves/round-96/seats/Q1-tool-hardening.md`), tool mtime `2026-10-17 17:47:24`.
- Baseline (r95) tool was still in place at 17:37–17:46 (`SELF_TEST_CASES` = 22). Q1's report is complete (198 lines, declared residuals) and its delivered hash matches mine.
- Before my edit the subset-tolerant r96 loader gave `SELF-TEST CASES 22/24 pinned` / `RESULT PASS` exit 0 (the two new cases implemented but unpinned).

## 1. Contract edit — 22 → 24 persisted cases

Edit applied (inserted after `source_id_mismatch`, order-independent check):

```json
      {"id": "schema_drift", "exit": 1, "finding_ids": ["schema_drift"]},
      {"id": "inventory_mismatch", "exit": 1, "finding_ids": ["inventory_mismatch"]},
```

`python3 -c "…json.load…"` → `cases: 24`. The r96 loader requires all 22 core cases pinned and no unimplemented case pinned, then runs exactly the pinned cases (`load_test_expectations`, `run_self_test`); the contract edit is what turns 22/24 into 24/24.

### Hand derivation (before running `--self-test`)

Derived from the documented semantics (tool module docstring, Q1 report §1(b), r95-documented finding classes); the case mutations come from the delivered implementation, the outcomes below were derived by hand and written down before the run:

- `schema_drift`: fixture rows E1/E2/R1/T1; the `/claims/0` row is dropped; entity 0's `claims` container is renamed to `assertions` with content preserved. The renamed container is no longer an obligation and its map row is gone → no `missing_obligation`/`phantom_obligation`; no `**Expected inventory:**` line in the fixture → no inventory finding; canonical cells → no `dual_pointer`. Derived: exit 1, findings exactly `[schema_drift]`.
- `inventory_mismatch`: intact fixture (4 obligations, 4 mapped rows); the map declares `5 JSON facts; 0 editorial rows; 5 total mapped rows`. Declared-vs-observed disagreement is gating. Derived: exit 1, findings exactly `[inventory_mismatch]`.

### Actual

```
SELF-TEST CASES 24/24 pinned
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
… (24 SELF-TEST PASS lines, 0 FAIL) …
RESULT PASS
exit=0
```

Hand-vs-actual: **exact match on both cases (exit and finding set); no mismatch to disclose.**

### Divergence from my brief (disclosed)

My brief described the `inventory_mismatch` case as "claims key + its map row removed". The delivered self-test case achieves the mismatch differently: an **intact** fixture whose map over-declares (`5/0/5` while 4 rows exist) — no deletion. The finding and exit are identical (`inventory_mismatch`, exit 1), and Q1's report §1(b) documents the case in exactly these terms. The deletion-class scenario itself is gated and verified separately (below), just not as the pinned case's mutation.

## 2. `corpus/tools/README.md` — Round-96 addendum

Appended `### Round-96 addendum: gating inventory mismatch, dual_pointer, 24-case self-test (2026-10-17)` (line 121) after the r95 addendum; **all prior text kept** (the r95 "receipt, not a gate" sentence remains at line 119 as history and is explicitly superseded). Covered:

- **Gating `inventory_mismatch` (deletion class closed)** with before/after quotes (below), stable FINDING ID, gating scope (facts/editorial/total; unparsable declaration also gates; anchor count stays receipt-only; absent declaration unchanged).
- **`dual_pointer` in legacy-dialect cells (V37-D1 closed)** with before/after quote, scan scope, no cascading `missing_obligation`, canonical-header notes unchanged (`unsupported_map` exit 2).
- **24-case self-test** with the exact command and both case descriptions.
- **Unchanged** list (fixtures, frozen replay, r87/r89 fail-closed, 0/1/2 contract, receipts).

## 3. Before/after evidence on scratch copies (no corpus writes)

Deletion class — scratch copy of `corpus/fixtures/r94-paired-crossing`, entity 0 `claims` key deleted + `entities.json#/0/claims/0` row removed:

```
before (r95 revision):  OBLIGATIONS raw=13 mapped=13
                        INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                        RESULT PASS   exit=0
after  (r96 revision):  OBLIGATIONS raw=13 mapped=13
                        INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                        FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 14/2/16; observed 13/2/15
                        RESULT FAIL   exit=1
```

Dual pointer — scratch copy of `corpus/fixtures/r88-m3-maya-cluster`, P1 cell = `` `entities[0].first_appearance` (Aru; also `entities[0].claims[0]`) ``:

```
before (r95 revision):  OBLIGATIONS raw=10 mapped=10 / INVENTORY … 12/12 / RESULT PASS   exit=0
after  (r96 revision):  FINDING dual_pointer: row P1 (line 23) names a second pointer token 'entities[0].claims[0]'
                        alongside entities.json#/0/first_appearance
                        RESULT FAIL   exit=1
```

Extra probes (all exit 1 `dual_pointer`): colon-prose legacy second token; parenthetical canonical second token (`relations.json#/0`); bare legacy token (`entities[9].claims[0]` without backticks); bare index token (`entities[0]`). The scan is lexical and over-detects in the fail-closed direction; no delivered corpus map trips it (all fixture runs below stay exit 0).

## 4. Full regression battery after the contract edit

Transcript: `.ufo/waves/round-96/seats/Q2-scratch/battery-after.txt` (14 `RESULT PASS`, exactly 2 non-zero exits = r87/r89, 4 CLEAN, determinism identical).

| command (cwd = lane root) | observed | exit |
|---|---|---|
| `python3 corpus/tools/map_obligations.py --self-test` | `SELF-TEST CASES 24/24 pinned` / 24 PASS / `RESULT PASS` | 0 |
| `… corpus/fixtures/r88-m3-maya-cluster` | `raw=10 mapped=10` / `INVENTORY … 12/12` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r93-m2-kojiki-cluster` | `raw=12 mapped=12` / `15/15` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r94-paired-crossing` | `raw=14 mapped=14` / `16/16` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r95-crossing-aftermath` | `raw=15 mapped=15` / `17/17` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r96-crossing-response` | `raw=16 mapped=16` / `18/18` / `RESULT PASS` | 0 |
| `… --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `digests=verified` / `FROZEN expected=PASS/0 matched` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r87-myth-cluster` | `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` | 2 |
| `… corpus/fixtures/r89-inspiration-paraphrase` | `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` | 2 |
| `support_check.py` on r87/r88/r89/r93/r94/r95/r96 | `RESULT PASS` (14/14, 10/10, 0/0+1 retelling, 12/12, 14/14, 15/15, 16/16) | 0 ×7 |
| `check_bible.py` on r93/r94/r95/r96 | `CLEAN: schema, citations, relations, timeline; 0 violations` | 0 ×4 |
| r88 run twice | `diff` → `identical` | 0 |

The README edit came after the battery and is documentation-only (no tool reads it); the self-test was re-run after both README edits: still `24/24 pinned` / `RESULT PASS`.

## 5. Environment finding (not fixed; outside my lane)

`/tmp` is a 16 GiB tmpfs at **100% inode use** (`df -i`: 1048576/1048576 used, 0 free) with ~8.5 GiB bytes free. New-file writes to `/tmp` fail with `No space left on device` (hit by one of my early probes; Q1's report §7.6 records the same). Any seat tool that creates files under `/tmp` (e.g. default `tempfile`) is at risk; all my scratch output is under the lane repo. Root cause visible in `/tmp`: accumulated scratch trees (`/tmp/lore-shokunin-d1-r88/` ≈ 21k entries, `/tmp/lore-r89-M2/` ≈ 19k, …). I did not delete anything (outside my write boundary) — recorded for the closure seats.

## 6. Boundary

Wrote only: my two owned corpus files, this report, and `.ufo/waves/round-96/seats/Q2-scratch/`. `git status --short` shows exactly `M LOG.md` (wave owner), `M corpus/tools/README.md`, `M corpus/tools/map-obligations-contract.json` (this seat), `M corpus/tools/map_obligations.py` (Q1), and untracked r96 producer artifacts (Q3/Q4/Q5/Q6).

## Bottom line

**PASS** — contract now persists 24 cases (hand-derived expectations matched actual exactly; `SELF-TEST CASES 24/24 pinned`, `RESULT PASS` exit 0); Round-96 README addendum appended with prior text kept; full battery green after the edit (r88/r93/r94/r95/r96 PASS, frozen PASS, r87/r89 exit 2, 7 support receipts PASS, 4 CLEAN, determinism identical); one brief-vs-implementation divergence (`inventory_mismatch` case mutation) disclosed above; environment note: `/tmp` inode-exhausted.

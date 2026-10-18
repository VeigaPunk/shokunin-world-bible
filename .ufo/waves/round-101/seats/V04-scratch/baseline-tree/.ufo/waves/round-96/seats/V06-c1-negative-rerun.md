# V06 — c1-negative-rerun (round-96)

**Seat:** V06 · **Role:** c1-negative-rerun — re-run the accumulated negative-control
classes (r94 F11 set + r95 `schema_drift` + r96 `inventory_mismatch` / `dual_pointer`) on
scratch copies under the **new r96 tool**, twice each, and check exit codes and finding-ID
stability against the C1 claim text.
**Subject (delivered):** `corpus/tools/map_obligations.py` sha256
`2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (900 lines; mtime
17:47:24; live sha re-checked unchanged after all runs; snapshot
`V06-scratch/map_obligations_r96.py` sha-identical to live).
**Baseline (before):** r95 tool sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` (extracted with
`git show 60dba0c:corpus/tools/map_obligations.py` after the live file had already moved
under Q1; sha matches the r95-closure pin).
**Base subject:** byte copy of `corpus/fixtures/r93-m2-kojiki-cluster` → `V06-scratch/base`
(sorted per-file sha256 tree hash `9de74566782802755a5260a5f02c5c88c389d839ad6ef7a1ce0759aa171ad5d5`);
the same fixture r94 F11 and r95 V04 used, so any finding-ID delta is the tool's, not the
harness's.
**Producer report polled:** `.ufo/waves/round-96/seats/Q1-tool-hardening.md` (mtime 17:50:55;
the seat brief guessed the filename `Q1-tool-code.md`, which never existed — see §1).

---

## 1. Poll-wait record

Poller `V06-scratch/poll-q1.sh` (20 s cadence, 40-try budget) watched the tool sha **and**
`Q1-tool-code.md`. The filename guess was wrong; the actual producer report is
`Q1-tool-hardening.md`. The tool sha itself moved through **9 distinct revisions**, so no
run was taken until the report was seen:

```
first seen at try=1:  d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  (baseline)
first seen at try=11: f92312391a65dbaa13f90f6159852f3579c8fd44a2fbd236ae5b4005757abce2
first seen at try=12: 8729f1f34680cfd6dff871c9687bab6cd7e3eed48f42b3b511416edaaee41495
first seen at try=13: f97e4b72cfe868d272752c2d4a0b48c0b70dda065123551a24fab6a9b5f3be87
first seen at try=14: 8cbcdb51c3bdd90ab03fe175b69e58085e5161ca629d3e3d4acf3d2327fc50f3
first seen at try=15: 44a6ffd4e6d35861fbf89ed18ac59467f4c4444e88072cb5f8b5434dcfa07e8b
first seen at try=16: c2c284c0118cf66bed019c43dde87caabcdce8ccda957a82230d7c5b35d029da
first seen at try=19: 6634e1768f1f05db63b537862d90eca39eec44a77e0079e81a793b215cc6b16c
first seen at try=21: 2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  (delivered)
```

I stopped the poll at try 29 (t≈580 s) after the seats listing showed `Q1-tool-hardening.md`
present; sha `2b0ba815…` had been stable from try 21 through my final post-run re-check. The
report was further written at 17:50:55, i.e. while my battery was running (17:50:36–38);
the **tool bytes did not move** (live sha unchanged before snapshot, after runs, and at
report write). No run was taken against a plan or a mid-iteration revision.

## 2. Method

Harness in `V06-scratch/` (all writes confined there + this report):

| file | sha256 (first 16) | role |
|---|---|---|
| `build-cases.py` | `f6fffdc74251c294` | builds base + 26 case dirs from the r93 byte copy; a–f replicate F11/V04 one-for-one |
| `run-cases.sh` | `542b991e3d190368` | runs every case **twice**, captures stdout+stderr+exit, prints byte-stability + ID table |
| `compare.py` | `ae8b54ba45ee0540` | encodes the post-r96 expectation table (from the C1 claim text) and reports MATCH/CHANGED + honest extras |
| `determinism.sh` | `7f6f976271f1b366` | third pass per case under `PYTHONHASHSEED=0,1,2` |
| `map_obligations_r95.py` | `d1c239ccb2140449` | baseline tool (before) |
| `map_obligations_r96.py` | `2b0ba815326b1cb3` | delivered tool snapshot (after) |

Commands (from the lane repo root):

```
$ python3 .ufo/waves/round-96/seats/V06-scratch/build-cases.py
$ bash .ufo/waves/round-96/seats/V06-scratch/run-cases.sh <abs>/map_obligations_r95.py baseline
$ bash .ufo/waves/round-96/seats/V06-scratch/run-cases.sh <abs>/map_obligations_r96.py new
$ python3 .ufo/waves/round-96/seats/V06-scratch/compare.py new
$ bash .ufo/waves/round-96/seats/V06-scratch/determinism.sh <abs>/map_obligations_r96.py new
```

Case set (26): base; a–f (F11: unmapped raw claim, duplicate row, phantom pointer,
source-ID mismatch, malformed JSON, invalid path ×4); g1/g2 `schema_drift`; h1/h2
`inventory_mismatch` deletion class; i1–i4 V37-D1 dual-pointer forms; i5–i7 boundary
probes; ctrl-legacy-note / ctrl-legacy-prose / ctrl-canonical-note /
ctrl-inv-declared-wrong / ctrl-inv-malformed.

## 3. Before picture — r95 tool `d1c239cc…` (`runs-baseline`)

run1 == run2 byte-identical for **all 26** cases; pass1 rows:

```
base                   PASS  exit=0 findings=[none]
a                      FAIL  exit=1 findings=[missing_obligation]
b                      FAIL  exit=1 findings=[duplicate_mapping]
c                      FAIL  exit=1 findings=[phantom_obligation]
d                      FAIL  exit=1 findings=[source_id_mismatch]
e                      ERROR exit=2 findings=[malformed_json]
f1                     ERROR exit=2 findings=[map_missing]
f2                     ERROR exit=2 findings=[foreign_path]
f3                     ERROR exit=2 findings=[unsafe_path]
f4                     ERROR exit=2 findings=[map_missing]
g1                     FAIL  exit=1 findings=[schema_drift]
g2                     FAIL  exit=1 findings=[phantom_obligation,schema_drift]
h1                     PASS  exit=0 findings=[none]                <-- carried defect
h2                     PASS  exit=0 findings=[none]                <-- carried defect
i1                     PASS  exit=0 findings=[none]                <-- V37-D1
i2                     PASS  exit=0 findings=[none]                <-- V37-D1
i3                     PASS  exit=0 findings=[none]                <-- V37-D1
i4                     FAIL  exit=1 findings=[missing_obligation]  <-- right exit, wrong reason
i5                     PASS  exit=0 findings=[none]
i6                     PASS  exit=0 findings=[none]
i7                     PASS  exit=0 findings=[none]
ctrl-legacy-note       PASS  exit=0 findings=[none]
ctrl-legacy-prose      PASS  exit=0 findings=[none]
ctrl-canonical-note    ERROR exit=2 findings=[unsupported_map]
ctrl-inv-declared-wrong PASS exit=0 findings=[none]               <-- non-gating receipt only
ctrl-inv-malformed     PASS  exit=0 findings=[none]
```

a–f reproduce the r94 F11 / r95 V04 baseline IDs exactly → harness is faithful. The three
carried residuals (deletion class h1/h2, V37-D1 i1–i3, non-gating inventory) are reproduced
on my scratch. Representative raw output:

```
$ python3 …/map_obligations_r95.py …/case-h1
OBLIGATIONS raw=11 mapped=11
INVENTORY JSON-FACTS 11/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 14/15 MISMATCH
RESULT PASS
EXIT=0
```

## 4. After picture — r96 tool `2b0ba815…` (`runs-new`)

run1 == run2 **byte-identical for all 26 cases** (`grep -c IDENTICAL` → 26); the seed sweep
(`PYTHONHASHSEED=0,1,2`) is **STABLE for all 19 classes swept** (exit + ID set identical).
`python3 compare.py new` → **`VERDICT: ALL-MATCH`**. Pass1 rows, with extras (co-firing IDs
beyond the required one) shown explicitly:

```
base                   MATCH  exit=0 findings=[none]
a                      MATCH  exit=1 findings=[missing_obligation]
b                      MATCH  exit=1 findings=[duplicate_mapping]            extras=[inventory_mismatch]
c                      MATCH  exit=1 findings=[inventory_mismatch,phantom_obligation]
d                      MATCH  exit=1 findings=[source_id_mismatch]
e                      MATCH  exit=2 findings=[malformed_json]
f1                     MATCH  exit=2 findings=[map_missing]
f2                     MATCH  exit=2 findings=[foreign_path]
f3                     MATCH  exit=2 findings=[unsafe_path]
f4                     MATCH  exit=2 findings=[map_missing]
g1                     MATCH  exit=1 findings=[inventory_mismatch,schema_drift]
g2                     MATCH  exit=1 findings=[phantom_obligation,schema_drift]
h1                     MATCH  exit=1 findings=[inventory_mismatch]
h2                     MATCH  exit=1 findings=[inventory_mismatch]
i1                     MATCH  exit=1 findings=[dual_pointer]
i2                     MATCH  exit=1 findings=[dual_pointer]
i3                     MATCH  exit=1 findings=[dual_pointer]
i4                     MATCH  exit=1 findings=[dual_pointer,missing_obligation]
i5                     MATCH  exit=1 findings=[dual_pointer]                  (boundary)
i6                     MATCH  exit=1 findings=[dual_pointer]                  (boundary)
i7                     MATCH  exit=1 findings=[dual_pointer]                  (boundary)
ctrl-legacy-note       MATCH  exit=0 findings=[none]
ctrl-legacy-prose      MATCH  exit=0 findings=[none]
ctrl-canonical-note    MATCH  exit=2 findings=[unsupported_map]
ctrl-inv-declared-wrong MATCH exit=1 findings=[inventory_mismatch]
ctrl-inv-malformed     MATCH  exit=1 findings=[inventory_mismatch]           (fail-closed, see §6)
```

Raw evidence for the claimed classes:

```
$ python3 …/map_obligations_r96.py …/case-h1      # deletion class (was exit 0)
OBLIGATIONS raw=11 mapped=11
INVENTORY JSON-FACTS 11/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 14/15 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 12/3/15; observed 11/3/14
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r96.py …/case-i1      # V37-D1 (was exit 0)
OBLIGATIONS raw=3 mapped=3
FINDING dual_pointer: row P1 (line 7) names a second pointer token 'relations.json#/0' alongside entities.json#/0/first_appearance
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r96.py …/case-i3      # V37-D1 colon form (was exit 0)
FINDING dual_pointer: row P1 (line 7) names a second pointer token 'entities[9].claims[0]' alongside entities.json#/0/first_appearance
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r96.py …/case-g1      # schema_drift now co-fires the gate
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 12/3/15; observed 11/3/14
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_records'
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r96.py …/ctrl-legacy-note   # no false fire
OBLIGATIONS raw=3 mapped=3
RESULT PASS
EXIT=0

$ python3 …/map_obligations_r96.py …/ctrl-canonical-note  # unchanged screening
FINDING unsupported_map: co-mapped or unsupported pointer grammar
RESULT ERROR
EXIT=2
```

## 5. C1 claim parts — seat verdicts

**(a) deletion class → GATING: verified.** h1 (whole `entities[0].claims` key + its map row
deleted) and h2 (one claim entry + its row deleted) both moved exit 0 → exit 1 with the
stable `inventory_mismatch` ID; the `INVENTORY … MISMATCH` receipt is byte-unchanged and now
backed by the gate. **Bonus on the delivered r96 fixture** (`case-r96-del`: claims key +
its row removed from a scratch copy of `corpus/fixtures/r96-crossing-response`, fixture
shas `026af0bc…` / `5093d72e…`, stable across both builds):

```
r95 tool:  OBLIGATIONS raw=15 mapped=15 / INVENTORY … 15/16 … MISMATCH / RESULT PASS / EXIT=0
r96 tool:  OBLIGATIONS raw=15 mapped=15 / INVENTORY … 15/16 … MISMATCH
           FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17
           RESULT FAIL / EXIT=1
```

**(b) pinning: context only (V02 owns the self-test seat).** `python3
corpus/tools/map_obligations.py --self-test` → `SELF-TEST CASES 24/24 pinned`, 24
`SELF-TEST PASS` lines including `schema_drift exit=1` and `inventory_mismatch exit=1`,
`RESULT PASS`, tool exit 0; live contract now carries 24 cases. Not gated by this seat.

**(c) dual_pointer: verified.** All four V37-D1 forms exit 1 with the stable `dual_pointer`
ID, and the finding names row, line, second token and first token. The detection is broader
than the three V37 forms — boundary probes also exit 1: i5 (bare second token without
backticks → token reported as `entities[9]`), i6 (parenthetical repeating the same pointer),
i7 (malformed second token `entities[00].claims[0]`). All are fail-closed (exit 1), and the
no-false-fire controls hold: legacy non-pointer note/prose stay exit 0, canonical-header note
stays `unsupported_map` exit 2.

## 6. Honest extras and interactions (not failures)

- **b / c / g1** carry `inventory_mismatch` alongside the required ID because the mutation
  itself makes observed rows differ from the declared count (duplicated / phantom / removed
  row). Exit 1 with the required ID present — the gate reporting the same stale declaration
  Q1 §4 documents.
- **i4** = `dual_pointer` + `missing_obligation`: in that probe `entities.json#/0/claims/0`
  genuinely has no other row (pre-existing missing), and the dual cell is still read by its
  first token, so no double-count; before r96 the same input exited 1 for the wrong reason
  (`missing_obligation` only).
- **ctrl-inv-malformed** (declaration counts unparsable) now exits 1 `inventory_mismatch`
  instead of the r95 exit-0 receipt `INVENTORY declaration-malformed`. This is the fail-closed
  extension Q1 declares explicitly (report §2 and residual 3), not an undocumented change;
  recorded because my seat re-runs the class.
- **Anchor field**: not exercised here; Q1 §7.1 declares the 4th declared field stays
  receipt-only (anchor counting is `support_check.py` scope).

## 7. Environment / hygiene

- One transient `map-obligations-self-test-az13_dtt/` appeared in `git status` at ~17:51:0x
  and had vanished by 17:51:16 — the disclosed BR-05 self-test scratch behavior (Q1 §7.5);
  no persistent residue attributable to my runs.
- All writes confined to `.ufo/waves/round-96/seats/V06-scratch/` and this report. No
  commits, no pushes, no network, no other corpus writes. `git status` after all runs shows
  only other seats' artifacts plus ` M LOG.md` (wave owner).
- Delivered-revision sha re-checked after all runs: still `2b0ba815…`.

**Bottom line: PASS — all nine accumulated negative-control classes (unmapped raw claim,
duplicate row, phantom pointer, source-ID mismatch, malformed JSON, invalid path,
schema_drift, inventory_mismatch, dual_pointer) re-run twice each under the delivered r96
tool exit exactly as the C1 claim requires (1 for the finding classes, 2 for
malformed/invalid) with stable FINDING IDs, byte-identical across runs and across
PYTHONHASHSEED 0/1/2; the two carried defects are closed on my scratch and on the delivered
r96 fixture, and every control shows no false-fire or regression.**

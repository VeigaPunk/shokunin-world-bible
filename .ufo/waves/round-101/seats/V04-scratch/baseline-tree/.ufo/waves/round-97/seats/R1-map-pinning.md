# R1 — map-pinning (round 97)

- **Seat:** R1 map-pinning (producer, exclusive byte-ownership of `corpus/tools/map_obligations.py`).
- **Lane:** lore-shokunin · **Wave:** round-97 single wave (64 seats: 6 producers + 58 verifiers).
- **Baseline:** r96 closure `f3e09f9` (HEAD at seat start `2393934`).
- **Task:** C1/calibration — (a) expose `dual_pointer` so R2 can pin it as a persisted self-test case (contract 24→25); (b) tighten the contract loader so **any** missing pinned case fails the self-test (r96 tolerance: a 23-case contract still passed); (c) keep all 24 current cases passing and the 0/1/2 exit contract + one terminal `RESULT` line intact. Stdlib-only. No commits, no pushes, no network, no nested agents.
- **Writes:** `corpus/tools/map_obligations.py` (owned) plus this report and `.ufo/waves/round-97/seats/scratch-R1/` (scratch). Nothing else.
- **Delivered revision:** `corpus/tools/map_obligations.py` sha256 `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` (`git diff --stat`: 1 file changed, 26 insertions(+), 4 deletions(-)); baseline revision (r96) `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (re-extracted via `git show f3e09f9:corpus/tools/map_obligations.py` and re-hashed in the probe harness).
- **Peer inputs used:** R2's contract `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` (25 cases, pin `{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}`), R4's r96 repair + r97 JSON tables, R5's r97 map.

## 0. Poll-wait evidence

- **R2 contract:** `.ufo/waves/round-97/seats/scratch-R1/poll-r2.sh` (20 s cadence, 40 tries), log `poll-r2.log`.
  `try=3 contract=24 [] sha=97b76bb8… r2_report=absent 21:45:59Z` → `try=4 contract=25 ['dual_pointer'] sha=2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41 r2_report=absent 21:46:19Z` → **POLL_HIT try=4**. Live contract: 25 cases, last id `dual_pointer`.
- **R5 r97 map:** `.ufo/waves/round-97/seats/scratch-R1/poll-r5.sh`, log `poll-r5.log`. Condition: a `timeline.json#/5` row in `corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md` **and** R5's report present.
  First observation (21:47:54Z, try=1): `map_rows=23 newrow=0 mapsha=e851f068cfd7ed02 inv=[**Expected inventory:** 16 JSON facts; 2 editorial rows; 18 total mapped rows] r5_report=absent` — i.e. R5's map was still the 16-row r96 copy, so the r97 battery below is reported **both** pre- and post-R5 (see §4.3). R5's row appeared at try=6 (21:49:34Z, `mapsha=49d4834e124fa6cf inv=[… 17 JSON facts; 2 editorial rows; 19 total mapped rows]`) and held byte-identical through try=12, when **POLL_HIT try=12 map_rows=24 newrow=1 mapsha=49d4834e124fa6cf r5_report=.ufo/waves/round-97/seats/R5-fixture-docs.md** fired. The r97 pin below is verified against those final map bytes (sha256 `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f`), re-confirmed after R5's report landed.

## 1. Edits (all inside the owned file, line numbers on the delivered revision)

1. **`dual_pointer` implemented as a self-test case** — `ADDED_SELF_TEST_CASES = ("schema_drift", "inventory_mismatch", "dual_pointer")` (line 76), so `SELF_TEST_CASES` (line 77) now holds 25 implemented cases and the contract may pin it.
2. **Legacy-dialect fixture helpers** (lines 639–649): `legacy_test_rows()` — the same four obligations written as `entities[0].first_appearance`, `entities[0].claims[0]`, `relations[0]`, `timeline[0]` — and `DUAL_POINTER_CELL = "`entities[0].first_appearance` (also named `entities[1].first_appearance`)"`. `dual_pointer` is only reachable in the legacy dialect (a canonical two-pointer cell stays `unsupported_map` exit 2, per r96 V04), so the case is built in that dialect.
3. **`write_test_fixture(..., legacy=False)`** (line 652) — legacy header `JSON fact and fields` instead of `JSON fact pointer and fields` (line 682); default path unchanged for all existing cases.
4. **`prepare_test_case` branch** (lines 732–734): `dual_pointer` writes the legacy fixture with the dual-pointer cell in row E1 and returns; expected outcome exit 1 with exactly `['dual_pointer']`.
5. **Loader tightening** (line 820): `missing = sorted(set(SELF_TEST_CASES) - set(expected))` (was `set(CORE_SELF_TEST_CASES)`, a 22-case subset that tolerated a contract dropping any r96-added pin). A contract missing **any** implemented case now fails `self_test_contract` / exit 2.
6. Module docstring documents the tightened rule (lines 8–11). No other behavior touched; the tool remains stdlib-only (`argparse, hashlib, json, os, re, subprocess, sys, tempfile, collections, pathlib`).

## 2. `--self-test` against the live 25-case contract (R2's `2142b991…`)

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS complete exit=0 findings=none
… (23 more PASS lines, all with the same exits/finding IDs as r96) …
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
EXIT=0
```

All 24 inherited cases keep their r96 exits/findings (`diff` baseline vs delivered self-test output = the `SELF-TEST CASES 24/24` → `25/25` header line plus the new `dual_pointer` PASS line, nothing else). The self-test internally also asserts exactly one `RESULT` line per case and empty stderr, so the 0/1/2 contract and the single terminal `RESULT` line are enforced for every case.

## 3. Load-bearing / strictness probes (scratch copies; each copy's own `ROOT` is scratch-local)

Harness `.ufo/waves/round-97/seats/scratch-R1/run_probes.py`, log `probes.txt`. Variants are built from the live 25-case contract by dropping cases; the baseline tool is `git show f3e09f9:…`.

| variant | contract | tool | observed |
|---|---|---|---|
| delivered-live25 | 25 (live) | delivered | `SELF-TEST CASES 25/25 pinned` … `RESULT PASS`, exit 0 |
| delivered-drop-dual | 24 (−`dual_pointer`) | delivered | `FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer` `RESULT ERROR`, exit 2 |
| delivered-drop-schema | 24 (−`schema_drift`) | delivered | `… drops implemented self-test cases: schema_drift`, exit 2 |
| delivered-drop-inventory | 24 (−`inventory_mismatch`) | delivered | `… drops implemented self-test cases: inventory_mismatch`, exit 2 |
| delivered-23case | 23 (−`schema_drift`, −`dual_pointer`) | delivered | `… drops implemented self-test cases: dual_pointer, schema_drift`, exit 2 |
| **baseline-23case** | 23 (−`schema_drift`, −`dual_pointer`) | r96 `2b0ba815…` | `SELF-TEST CASES 23/24 pinned` … `RESULT PASS`, **exit 0** ← the r96 tolerance the claim closes |
| baseline-drop-dual | 24 (−`dual_pointer`) | r96 | `SELF-TEST CASES 24/24 pinned` … `RESULT PASS`, exit 0 (a missing new pin stayed green pre-fix) |
| **neutralized-live25** | 25 (live) | delivered, `if mention is not None:` → `if False:` in `parse_map_text` | `SELF-TEST PASS` ×24, then `SELF-TEST FAIL dual_pointer exit=1 findings=[]` / `FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations` / `RESULT ERROR`, exit 2 — **the pin is load-bearing** |

Direct CLI probe of the new case's fixture (`.ufo/waves/round-97/seats/scratch-R1/probe-legacy-dual`, built by `build_probe.py`):

```
$ python3 corpus/tools/map_obligations.py .ufo/…/scratch-R1/probe-legacy-dual
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
EXIT=1
$ python3 corpus/tools/map_obligations.py .ufo/…/scratch-R1/probe-legacy-single   # same rows, single-pointer cell
OBLIGATIONS raw=4 mapped=4
RESULT PASS
EXIT=0
```

Remaining loader branches re-probed on the delivered revision (all `RESULT ERROR`, exit 2): unknown case id → `contract pins unimplemented self-test cases: not_a_case`; repeated id → `contract repeats a self-test case ID`; `exit: 3` or non-string finding IDs → `contract contains an invalid self-test expectation`.

**Ordering note (the 24-case contract).** My first post-edit run, at 21:46Z against the then-live pre-R2 contract `97b76bb8…` (24 cases), printed exactly:

```text
$ python3 corpus/tools/map_obligations.py --self-test
FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer
RESULT ERROR | EXIT=2
```

That is the tightened loader working as specified — a contract missing a pinned case now fails closed — not a case failure: all 24 inherited cases pass unchanged inside the 25-case run (§2), and the same 24-case contract is `SELF-TEST CASES 24/24 pinned` / `RESULT PASS` exit 0 under the r96 tool (row `baseline-drop-dual` above). R2's 25-case contract landed at 21:46:19Z (poll try=4), before the delivered self-test run, so the live revision was never in the "24-case contract" state at verification time.

## 4. Battery (baseline vs delivered, same commands, `.ufo/waves/round-97/seats/scratch-R1/{baseline,delivered}/`)

Harness `capture.sh`. Baseline captured 21:45Z with the r96 tool `2b0ba815…`; delivered captured with `86b52949…`. `cmp -s` per captured file: **SAME** for `map-r87, map-r88, map-r89, map-r93, map-r94, map-r95, map-r96, map-frozen, map-usage-noargs, map-usage-missing, map-usage-bogus, map-usage-conflict`; the only DIFF is `map-selftest.out` (24 → 25 cases).

### 4.1 Map fixtures (delivered)

```text
r87-myth-cluster        FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer | RESULT ERROR | EXIT=2
r88-m3-maya-cluster     OBLIGATIONS raw=10 mapped=10 / INVENTORY 10/10; 2/2; TOTAL-ROWS 12/12 / RESULT PASS | EXIT=0
r89-inspiration-paraphrase FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column | RESULT ERROR | EXIT=2
r93-m2-kojiki-cluster   OBLIGATIONS raw=12 mapped=12 / 12/12; 3/3; 15/15 / RESULT PASS | EXIT=0
r94-paired-crossing     OBLIGATIONS raw=14 mapped=14 / 14/14; 2/2; 16/16 / RESULT PASS | EXIT=0
r95-crossing-aftermath  OBLIGATIONS raw=15 mapped=15 / 15/15; 2/2; 17/17 / RESULT PASS | EXIT=0
r96-crossing-response   OBLIGATIONS raw=16 mapped=16 / 16/16; 2/2; 18/18 / RESULT PASS | EXIT=0
```

Every exit equals the r96 pin (r88 10/10 + 12/12, r93 12/12, r94 14/14, r95 15/15, r96 16/16, r87/r89 exit 2) and every captured byte is identical to the r96-tool baseline.

### 4.2 `--frozen` r93 replay + usage probes (delivered)

```text
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS | EXIT=0

no-args                      FINDING invalid_arguments: cluster directory is required | EXIT=2
missing cluster              FINDING cluster_missing: cannot resolve cluster: [Errno 2] …does-not-exist-r97 | EXIT=2
--bogus-flag                 FINDING invalid_arguments: unrecognized arguments: --bogus-flag | EXIT=2
--self-test + cluster        FINDING invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen | EXIT=2
--frozen <missing dir>       FINDING snapshot_tampered: frozen snapshot directory is missing or unreadable | EXIT=2
--map claim-excerpt-map.md   (explicit map path) | EXIT=0
```

### 4.3 r97 fixture

**First observation (R5's row not yet landed, 21:47Z):**

```text
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
FINDING missing_obligation: timeline.json#/5 has no map row
RESULT FAIL | EXIT=1
```

R4's `timeline.json` already held 6 events (last `acknowledgment-aru-records`) while R5's map was still the 16-row r96 copy declaring `16 JSON facts; 2 editorial rows; 18 total mapped rows`. The tool correctly reported the missing 17th row — R5's deliverable was in flight, not a C1 regression.

**Post-R5 map (sha256 `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f`, stable across poll tries 6–9, `17 JSON facts; 2 editorial rows; 19 total mapped rows`):**

```text
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS | EXIT=0
```

r97 `17/17` matches the round claim. Independent parsed-row cross-check (`scratch-R1/post_r5_check.py`, log `post-r5.txt`, importing the delivered tool): `parsed rows: r96=16 r97=17`; `inherited pointers: 16; identical source binding: True`; `new pointers in r97: ['timeline.json#/5'] -> ['aru-acknowledgment-note']`; `dropped pointers: []`; `row order preserved for inherited rows: True`; `r97 raw obligations=17 drift=[]`; `unmapped raw obligations: []`. (C3's inherited-equality claim is R4/R5's to make; this is an independent corroboration from the tool's own parser.)


## 5. r96 receipt unchanged by R4's cosmetic repair

R4's repair (`git diff -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`) is exactly 2 lines: the editorial delimiter row `|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|` (8→7 cells) and the stale sentence `The new relation encodes only the agreement…` → `The new tick-12 event encodes only Evin's second account…`. Data rows untouched. The delivered tool's r96 run is **byte-identical** to the r96-era delivered capture (`.ufo/waves/round-96/seats/V05-scratch/delivered/map-r96.out`): `cmp -s` → `SAME`, i.e. `OBLIGATIONS raw=16 mapped=16` / `16/16; 2/2; 18/18` / `RESULT PASS` / exit 0, exactly the r96 pin.

## 6. Determinism, hygiene, scope

- **Determinism:** r88 stdout `8d98f0e6888d875f…` ×2; `--self-test` stdout `851fa47f0a2186f3…` ×2 — byte-identical runs. A third full battery after R5's report landed (`scratch-R1/final/`) is byte-identical to the mid-run capture `delivered2/` on all 14 captured files (13 fixture/usage runs + self-test), and the delivered tool/contract/r96-map/r97-map hashes were re-read unchanged at the end: `map_obligations.py` `86b52949…`, contract `2142b991…`, r96 map `e851f068…`, r97 map `49d4834e…`.
- **Stdlib-only:** no new imports; `python3 -m py_compile corpus/tools/map_obligations.py` → COMPILE OK.
- **No strays:** no `map-obligations-self-test-*` residue at the repo root (self-test temp trees are `TemporaryDirectory` under `ROOT` and removed); every write of this seat is under `corpus/tools/map_obligations.py`, `.ufo/waves/round-97/seats/R1-map-pinning.md`, and `.ufo/waves/round-97/seats/scratch-R1/`. `git status --porcelain` shows this seat's only tracked change as `corpus/tools/map_obligations.py`.
- **Non-claims:** I verified the tool's self-test contract/loader behavior, the r87–r96 battery, the frozen replay, and usage exits. I do not judge R2's contract wording, R3's dependency_freeze work, R4/R5's fixture content beyond the receipts above, or any entailment/canon/chronology question.

## Bottom line

**PASS** — on the delivered revision (`map_obligations.py` `86b52949…`) `dual_pointer` is a persisted, executed self-test case (live 25-case contract `2142b991…`: `SELF-TEST CASES 25/25 pinned` … `SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']` → `RESULT PASS` exit 0), the loader now fails closed with exit 2 on any contract that drops a pinned case (the r96 tool still passes the same 23-case contract at `23/24` exit 0), neutralizing the `dual_pointer` emission fails the self-test (exit 2), the r87–r96 battery + frozen-r93 replay + usage probes are byte-identical to the r96 pins, and r97 verifies `raw=17 mapped=17` / `17/17; 2/2; 19/19` / `RESULT PASS` exit 0 with the 16 inherited rows parsed-value identical to r96 (r97 map sha `49d4834e…`, unchanged from R5's row landing through R5's report).

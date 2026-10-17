# F11 — c2-negative (round-94 FOLLOW-UP)

**Seat:** F11 · **Role:** c2-negative — negative controls for the r94 C2 tool `corpus/tools/map_obligations.py` against scratch copies of the r93 fixture + map.
**Verdict on the seat claim:** every one of the six required negative controls reproduces exactly as specified, with stable finding IDs across repeats. Live tree untouched.

---

## 1. Method and scope

- Tool under test: `corpus/tools/map_obligations.py` (sha256 `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790`, identical to `HEAD` = `65a93298cb100fdbf5732ac6de55f01a683c02d8`).
- Contract: `corpus/tools/map-obligations-contract.json` — `"exit_codes": {"0": "PASS", "1": "FAIL", "2": "ERROR"}`.
- Subject copied: `corpus/fixtures/r93-m2-kojiki-cluster/` → `.ufo/waves/round-94/followup/F11-scratch/base/` (`diff -r corpus/fixtures/r93-m2-kojiki-cluster .ufo/waves/round-94/followup/F11-scratch/base` → `IDENTICAL`).
- Scratch path contains no symlinks (checked explicitly, because `resolve_cluster`/`resolve_map` reject symlinked paths — `corpus/tools/map_obligations.py:70-77`).
- All mutations were built by `.ufo/waves/round-94/followup/F11-scratch/build-cases.py`; all runs by `.ufo/waves/round-94/followup/F11-scratch/run-cases.sh`. Raw stdout/exit captures are in `.ufo/waves/round-94/followup/F11-scratch/runs/<case>-run{1,2}.out`; the mutation diffs are in `runs/mutations.diff`.

**Baseline (must be green for the negatives to mean anything)** — `python3 corpus/tools/map_obligations.py .ufo/waves/round-94/followup/F11-scratch/base`:

```
OBLIGATIONS raw=12 mapped=12
RESULT PASS
EXIT=0
```

## 2. Required negative controls — actual observed output

Each case was run twice, back to back, same command, and the two captures are byte-identical (`diff -q` on every pair).

### (a) raw claim with no map row → exit 1 missing-obligation — **CONFIRMED**

Mutation: one extra claim appended to entity 0 (`runs/mutations.diff`, `### base -> case-a`), giving raw pointer `entities.json#/0/claims/1` with no map row.

```
OBLIGATIONS raw=13 mapped=12
FINDING missing_obligation: entities.json#/0/claims/1 has no map row
RESULT FAIL
EXIT=1
```

### (b) duplicate map row → exit 1 duplicate — **CONFIRMED**

Mutation: the `E1` row (`entities.json#/0/first_appearance`) duplicated verbatim (`### base -> case-b`).

```
OBLIGATIONS raw=12 mapped=13
FINDING duplicate_mapping: entities.json#/0/first_appearance appears 2 times
RESULT FAIL
EXIT=1
```

### (c) map row pointing at a non-obligation → exit 1 phantom — **CONFIRMED**

Mutation: extra row `E99` with a syntactically canonical pointer `entities.json#/99/first_appearance` (index out of range in the raw document; `### base -> case-c`).

```
OBLIGATIONS raw=12 mapped=13
FINDING phantom_obligation: entities.json#/99/first_appearance is not a raw source-attributed obligation
RESULT FAIL
EXIT=1
```

### (d) map row source-ID differing from raw → exit 1 mismatch — **CONFIRMED**

Mutation: the `E1` row's source column changed `m2-record-archive` → `m2-other-archive`; raw is untouched (`### base -> case-d`).

```
OBLIGATIONS raw=12 mapped=12
FINDING source_id_mismatch: entities.json#/0/first_appearance does not bind to 'm2-record-archive'
RESULT FAIL
EXIT=1
```

### (e) malformed raw JSON → exit 2 — **CONFIRMED**

Mutation: `entities.json` truncated mid-array (`### base -> case-e`).

```
FINDING malformed_json: cannot parse entities.json: Unterminated string starting at: line 27 column 11 (char 558)
RESULT ERROR
EXIT=2
```

### (f) invalid map path → exit 2 — **CONFIRMED, three distinct routes**

Case-f's cluster is the unmodified base; only `--map` varies.

| Variant | Command tail | Observed |
|---|---|---|
| f1 nonexistent map file | `--map missing-map.md` | `FINDING map_missing: cannot resolve map: [Errno 2] No such file or directory: '.../case-f/missing-map.md'` / `RESULT ERROR` / `EXIT=2` |
| f2 map outside the cluster | `--map <abs>/F11-scratch/outside-map/claim-excerpt-map.md` | `FINDING foreign_path: map path is outside the cluster` / `RESULT ERROR` / `EXIT=2` |
| f3 relative map path with traversal | `--map ../outside-map/claim-excerpt-map.md` | `FINDING unsafe_path: map path contains traversal` / `RESULT ERROR` / `EXIT=2` |
| f4 (extra) map path is a directory | `--map .` | `FINDING map_missing: map path is not a file` / `RESULT ERROR` / `EXIT=2` |

## 3. Stability of finding IDs (each case run twice)

From `runs/*-run{1,2}.out`, run1 vs run2 byte-diff results and the ID sets:

```
base  pass1 result=PASS  exit=0 findings=[none]              base  pass2 IDENTICAL
a     pass1 result=FAIL  exit=1 findings=[missing_obligation]   a     pass2 IDENTICAL
b     pass1 result=FAIL  exit=1 findings=[duplicate_mapping]    b     pass2 IDENTICAL
c     pass1 result=FAIL  exit=1 findings=[phantom_obligation]   c     pass2 IDENTICAL
d     pass1 result=FAIL  exit=1 findings=[source_id_mismatch]   d     pass2 IDENTICAL
e     pass1 result=ERROR exit=2 findings=[malformed_json]       e     pass2 IDENTICAL
f1    pass1 result=ERROR exit=2 findings=[map_missing]          f1    pass2 IDENTICAL
f2    pass1 result=ERROR exit=2 findings=[foreign_path]         f2    pass2 IDENTICAL
f3    pass1 result=ERROR exit=2 findings=[unsafe_path]          f3    pass2 IDENTICAL
f4    pass1 result=ERROR exit=2 findings=[map_missing]          f4    pass2 IDENTICAL
```

Findings are emitted sorted (`emit`, `corpus/tools/map_obligations.py:63-67`), so ID order is deterministic; all ten cases produced byte-identical stdout on repeat.

## 4. Independent corroboration: the tool's own self-test

`python3 corpus/tools/map_obligations.py --self-test` (run twice, identical output both times) → `RESULT PASS`, `EXIT=0`, 20/20 cases. The persisted expectations match my externally observed IDs exactly for the overlapping cases:

```
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
```

## 5. Precision notes worth carrying forward

1. **`phantom_obligation` is a set-membership check, not document resolution.** The self-test's `phantom` case uses `entities.json#/0/name` — a pointer to a real field that is not an obligation (`corpus/tools/map_obligations.py:531-532`) — while my case-c used an out-of-range index `entities.json#/99/first_appearance`. Both yield `phantom_obligation`. So the tool catches a map pointer that is not *exactly* a raw obligation string, but does not independently verify the pointer resolves in the raw document. Consistent with the contract scope ("one-to-one map completeness and source-ID binding", `map-obligations-contract.json`), but it is a real limit of what a green run proves.
2. **Two different `unsafe_path` routes.** The self-test's `traversal_path` is about traversal *inside the pointer* (`../entities.json#/...`, line 552-553); my f3 is traversal in the `--map` argument (`resolve_map`, lines 104-108). Same finding ID, different code path — both confirmed exit 2.
3. **Self-test coverage gap (not a defect).** `map_missing` — my f1 (nonexistent map file) and f4 (map path is a directory) — is *not* among the contract's `self_test.cases` nor `SELF_TEST_CASES` (`corpus/tools/map_obligations.py:19-40`). Behavior is correct and stable (exit 2, `RESULT ERROR`), but it is only covered by external exercise like this seat's. Likewise `invalid_arguments` is exercised nowhere in the self-test.
4. **A duplicate row that also carries a wrong source ID reports both findings** — by construction of `compare` (lines 311-317); my case-b used an exact copy so only `duplicate_mapping` fired, which is the clean single-cause demonstration.

## 6. Live tree untouched

- `git status --porcelain -- corpus/` → empty, both before and after all runs.
- `git status --porcelain` (whole repo) → only `?? .ufo/waves/round-94/followup/` (my scratch + report).
- `git show HEAD:<file> | sha256sum` vs worktree sha256: `MATCH` for `corpus/tools/map_obligations.py`, `corpus/fixtures/r93-m2-kojiki-cluster/claim-excerpt-map.md`, `corpus/fixtures/r93-m2-kojiki-cluster/entities.json`.
- No commits, no edits outside `.ufo/waves/round-94/followup/F11-scratch/` and this report file.

**Bottom line: PASS — all six required negative controls (a–f) reproduce the specified exit codes and finding IDs on scratch copies of the r93 fixture+map, byte-identically across two runs each, and the live tree is verifiably unmodified.**

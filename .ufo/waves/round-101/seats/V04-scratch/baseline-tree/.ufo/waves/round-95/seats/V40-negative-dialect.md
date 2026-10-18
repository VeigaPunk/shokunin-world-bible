# V40 — negative-dialect: r88 map+fixture scratch mutations under dialect mode

- Seat: V40 (verifier). Round 95, baseline `fb118c4`, lore-shokunin.
- Target: P1's delivered `corpus/tools/map_obligations.py` under the r88 map dialect.
- Delivered revision pinned for every run below:
  - `corpus/tools/map_obligations.py` sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`, mtime `2026-10-17 16:26:27 -0300`, size 33320.
  - `corpus/tools/map-obligations-contract.json` sha256 `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` (not needed by this seat's cases; recorded for pinning).
- Method: each case gets a fresh `shutil.copytree` of the live r88 fixture into
  `.ufo/waves/round-95/seats/V40-scratch/dialect/<case>/`, one mutation per copy, then the
  delivered tool runs on the copy **twice**. The live tree is never written by this seat.
- Harness: `.ufo/waves/round-95/seats/V40-scratch/run_mutations.py`; raw captures
  `mutations.json` / `mutations2.json`, logs under the same scratch dir.

## 1. Before-state (captured pre-P1, 16:17, live tree)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
exit=2
```

## 2. Baseline on the delivered revision (live tree, twice, 16:32)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster   (x2, identical)
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

Observed counting: 10 raw source-attributed obligations (`entities.json#/0..3/first_appearance`,
`entities.json#/0..3/claims/0`, `timeline.json#/0`, `timeline.json#/1`), 2 editorial rows, 12 declared
rows — the same 12/12 total `support_check` reports (`RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2;
TOTAL-ROWS 12`). The delivered tool labels both figures; consistent with P1 report §6.1.

## 3. Required mutation matrix (fresh copy per case, two runs per case)

Command form: `python3 corpus/tools/map_obligations.py .ufo/waves/round-95/seats/V40-scratch/dialect/<case>`
(harness ran exactly this via `sys.executable`). Mutation diffs are against the live map (shown in §4).

| Case | Mutation | Run 1 | Run 2 | Finding IDs stable |
|---|---|---|---|---|
| `missing_row` | delete row `T2` (`timeline[1]`) | exit 1 | exit 1 | yes |
| `source_id_mismatch` | row `P1` source `` `paired-clock` `` → `` `bell-tally` `` | exit 1 | exit 1 | yes |
| `duplicate_row` | duplicate row `P1` | exit 1 | exit 1 | yes |
| `malformed_json` | `entities.json` := `{` | exit 2 | exit 2 | yes |

Quoted stdout (run 1; run 2 byte-identical, verified by comparing full stdout strings):

```
== missing_row ==
OBLIGATIONS raw=10 mapped=9
INVENTORY JSON-FACTS 9/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 11/12 MISMATCH
FINDING missing_obligation: timeline.json#/1 has no map row
RESULT FAIL

== source_id_mismatch ==
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
FINDING source_id_mismatch: entities.json#/0/first_appearance does not bind to 'paired-clock'
RESULT FAIL

== duplicate_row ==
OBLIGATIONS raw=10 mapped=11
INVENTORY JSON-FACTS 11/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 13/12 MISMATCH
FINDING duplicate_mapping: entities.json#/0/first_appearance appears 2 times
RESULT FAIL

== malformed_json ==
FINDING malformed_json: cannot parse entities.json: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
RESULT ERROR
```

All eight runs: exit code, sorted finding IDs, terminal `RESULT` line, and full stdout identical
within each case pair; stderr empty in every run; exactly one `RESULT` line per run.

## 4. Mutation diffs actually applied (scratch vs live map)

```
missing_row          - | T2 | `timeline[1]` (`description`, `source_id`): Evin holds the south bell at Salt Court | `paired-clock` | ...
source_id_mismatch   - | P1 | ... | `paired-clock` | ...        (line 23)
                     + | P1 | ... | `bell-tally` | ...          (line 23)
duplicate_row        + | P1 | `entities[0].first_appearance` (Aru) | `paired-clock` | ...   (inserted after line 23)
malformed_json       entities.json begins with "{"
```

## 5. Variant instances (class behavior, not single-instance; each twice, stable)

| Variant | Observed run 1 (run 2 identical) |
|---|---|
| delete `P2` row (`entities[1].first_appearance`) | exit 1 `FINDING missing_obligation: entities.json#/1/first_appearance has no map row` |
| delete `E4` claim row (`entities[3].claims[0]`) | exit 1 `FINDING missing_obligation: entities.json#/3/claims/0 has no map row` |
| mismatch `T1` row (`timeline[0]`) | exit 1 `FINDING source_id_mismatch: timeline.json#/0 does not bind to 'paired-clock'` |
| duplicate `T1` row | exit 1 `FINDING duplicate_mapping: timeline.json#/0 appears 2 times` |
| `timeline.json` := `[{"id": ` (truncated) | exit 2 `FINDING malformed_json: cannot parse timeline.json: Expecting value: line 1 column 9 (char 8)` |

All variants still parsed under the legacy dialect (receipts `INVENTORY ...` printed; no
`unsupported_map` fallback), so the negative outcomes come from the dialect path, not from
dialect-detection collapse.

## 6. Reproducibility

- Full harness re-run on fresh copies: `diff mutations.json mutations2.json` → clean
  (`HARNESS_REPRODUCIBLE_IDENTICAL`).
- Live baseline re-run twice at 16:32: byte-identical output, exit 0 both.
- Delivered tool hash re-checked after all runs: unchanged (`d1c239cc…`).

## 7. Live tree untouched

```
$ sha256sum -c /tmp/v40-r88-before.sha        # all 11 r88 files, recorded 16:17 before any P1 delivery
11 x OK (claim-excerpt-map.md, contradictions.json, entities.json, fictional-excerpts.md,
        inspiration-note.md, README.md, relations.json, source-excerpt.md, sources.json,
        symbolism-clause-map.md, timeline.json)
$ git diff --stat -- corpus/fixtures/r88-m3-maya-cluster   # empty
$ git status --porcelain corpus/fixtures/                  # only: ?? corpus/fixtures/r95-crossing-aftermath/ (P3/P4's declared new fixture)
```

All V40 writes are confined to `.ufo/waves/round-95/seats/V40-scratch/` and this report.
Transient observation: an untracked `map-obligations-self-test-hyt2n5p3/` directory at repo root
was visible in one `git status` (16:31) — a concurrent seat's in-flight `--self-test` tempdir
(`tempfile.TemporaryDirectory(dir=ROOT)`) — and gone at the next check; transient, not a leak, not mine.

## 8. Scope limits

- Results pin the tool revision `d1c239cc…`; any later edit to `map_obligations.py` voids them.
- This seat did not re-verify C1's `schema_drift` demo (V01/V04 axis), the 22-case `--self-test`
  (P2/other seats), r87/r89 fail-closed controls (V05 axis), or the r95 fixture (V08 axis).
- Map-header tampering (dialect-gate rejection) was probed by P1, not independently re-verified here.

## Bottom line

PASS — on the delivered revision all four required negative-dialect mutations fail closed with
stable finding IDs across repeated runs (missing row / source-id mismatch / duplicate row → exit 1;
malformed JSON → exit 2), baseline r88 is exit 0 with `TOTAL-ROWS 12/12`, and the live r88 fixture
is byte-identical throughout.

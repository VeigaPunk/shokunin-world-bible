# V14 — c3-inherited-equality (round 97)

Seat: V14 (verifier). Claim under test: **C3 (depth) — inherited-row equality** of
`corpus/fixtures/r97-crossing-acknowledgment/` against **POST-REPAIR**
`corpus/fixtures/r96-crossing-response/`, plus the byte-unchanged claim for the r96
JSON tables versus baseline `f3e09f9`.

- Repo: `/home/vgpnk/Projects/shokunin/lore-shokunin` (absolute paths; session cwd is the parent repo).
- Baseline: r96 closure commit `f3e09f9`.
- Producer poll: r97 dir (10 files) present from 18:44; R4 report `R4-fixture-author.md` present 18:50 → protocol satisfied (tries 1–25, 20 s cadence).
- Verified revision: working tree after R4 report. All commands below re-run at that point.
- Harness (declared scratch): `.ufo/waves/round-97/seats/V14-scratch/v14_battery.py`.

## Verifier self-validation (before touching artifacts)

- Dry-run on a synthetic r96+appended-row fixture: `FAILURES: 0` — harness mechanics validated.
- Negative controls on mutated copies (values/key-order/bytes):
  - key reorder only, values same → `timeline.json[0] MISMATCH same=False key-order=False` (order-sensitivity load-bearing);
  - one byte changed in a copied file → `entities.json: identical=False` + inherited mismatch;
  - one inherited value changed → `sources.json[0] MISMATCH`.
  - Total: `FAILURES: 6`, `NC_EXIT=1` — every check fires when it should.

## 1. r97 row counts

```
entities.json: rows=5 OK
relations.json: rows=1 OK
contradictions.json: rows=0 OK
timeline.json: rows=6 OK
sources.json: rows=6 OK
```

## 2. Parsed-value equality, KEY-ORDER SENSITIVE, inherited rows (r97 vs POST-REPAIR r96)

Comparison = `json.dumps(row, sort_keys=False, separators=(",",":"))` equality **plus**
explicit `list(row.keys())` order equality (nested structures included).

```
entities.json[:5] (r96 rows=5, r97 rows=5): IDENTICAL (order-sensitive)
relations.json[:1] (r96 rows=1, r97 rows=1): IDENTICAL (order-sensitive)
contradictions.json[:0] (r96 rows=0, r97 rows=0): IDENTICAL (order-sensitive)
timeline.json[:5] (r96 rows=5, r97 rows=6): IDENTICAL (order-sensitive)
sources.json[:5] (r96 rows=5, r97 rows=6): IDENTICAL (order-sensitive)
```

Note: the r96 map repair touched only `claim-excerpt-map.md`, so POST-REPAIR r96 JSON ==
`f3e09f9` JSON (independently confirmed in §5); the comparison above is against the live
post-repair working tree, not a frozen copy.

## 3. Byte-copy claims (literal `cmp`)

Run from `corpus/fixtures/`:

```
cmp entities.json: IDENTICAL (rc=0)
cmp relations.json: IDENTICAL (rc=0)
cmp contradictions.json: IDENTICAL (rc=0)
cmp inspiration-note.md: IDENTICAL (rc=0)
cmp source-excerpt.md: IDENTICAL (rc=0)
```

Sizes: entities 1449 B, relations 139 B, contradictions 3 B, inspiration-note 1956 B,
source-excerpt 640 B on both sides.

## 4. Byte-prefix probe for the extended tables

r96 core = r96 bytes minus trailing whitespace and the final `]` (1674 B timeline / 1738 B sources):

```
cmp -n 1674 timeline.json: PREFIX IDENTICAL (rc=0)
cmp -n 1738 sources.json: PREFIX IDENTICAL (rc=0)
```

`first-divergence-at` equals the core length exactly for both (i.e. divergence begins only at
the inserted separator/append). `diff -u r96/timeline.json r97/timeline.json` shows exactly one
hunk: the appended `acknowledgment-aru-records` tick-13 row. `sources.json` likewise.

## 5. r96 JSON tables byte-unchanged vs `f3e09f9`

```
git diff --stat f3e09f9 -- corpus/fixtures/r96-crossing-response/{entities,relations,contradictions,timeline,sources}.json
  -> (empty), rc=0
git hash-object <wt file> == git rev-parse f3e09f9:<path>  -> SAME for all five
  entities.json       1797bd87bb585909f5f5c2bb9934afe94efef0d0
  relations.json      2804ae91240dbf34753bf955d4fab9ffeab0a8df
  contradictions.json fe51488c7066f6687ef680d6bfaa4f7768ef205c
  timeline.json       7ef3dff33fec2636933f239c51f457ebf467fd20
  sources.json        f3f15bd851646514128456f43e09244d0c20da30
```

Re-checked at the final revision (after R4's report) — still SAME.

## 6. Revision stability across the verification window

sha256 manifest of all 10 r97 files taken pre-report and post-report
(`V14-scratch/hashes-preliminary.txt` vs `hashes-final.txt`): only
`claim-excerpt-map.md` and `README.md` changed — both R5-owned files, extended by R5 during the
window. Every file in V14's mandate (5 JSON tables + `fictional-excerpts.md` + the 2 copied md
files) was byte-stable across the window.

## Supplementary observations (outside the primary mandate, reported as context)

- r96 map repair is exactly 2 lines (`git diff --numstat` → `2  2`): line 44 delimiter
  `|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|` (8→7 cells) and line 50
  "The new relation encodes…" → "The new tick-12 event encodes…". No data row, pointer, anchor,
  span or mode moved.
- New rows match the declared shape and resolve: `timeline.json[5]` = `acknowledgment-aru-records`,
  tick 13, `depends_on: ["response-evin-salt-court"]` (inherited event), `source_id`
  `aru-acknowledgment-note` present in `sources.json[5]`; new-row key sets equal inherited key
  sets; ticks monotone `[9,9,10,11,12,13]`; entity/place ids all resolve.
- Whole-repo surface vs `f3e09f9` at final revision: `LOG.md`, `SCORECARD.md`, r96 map,
  `corpus/tools/{README.md,map-obligations-contract.json,map_obligations.py}` modified; untracked
  `.ufo/waves/round-97/` and `corpus/fixtures/r97-crossing-acknowledgment/`. No unexpected path.
- No blockers, no contradictions found; no ABSENT condition.

## Bottom line

**PASS** — every inherited row of `r97-crossing-acknowledgment` is parsed-value identical
(key-order sensitive) to POST-REPAIR `r96-crossing-response` (entities 5/5, relations 1/1,
timeline[:5], sources[:5], contradictions 0/0), the five copied files are byte-identical by
`cmp`, both extended tables are byte-prefixes of the r96 core, and the r96 JSON tables are
byte-unchanged versus `f3e09f9`; checks proven load-bearing by three negative controls.

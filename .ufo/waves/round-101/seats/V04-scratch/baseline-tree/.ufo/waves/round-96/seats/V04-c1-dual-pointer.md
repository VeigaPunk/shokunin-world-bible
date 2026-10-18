# V04 — c1-dual-pointer (V37-D1 closure)

**Seat:** V04 (verifier) · **Wave:** round-96, 64-seat single-wave swarm · **Lane:** lore-shokunin
**Baseline:** r95 closure `dcb2d92` · **Report written:** 2026-10-17 (session date)
**Scope:** demonstrate V37-D1 closed on the delivered `corpus/tools/map_obligations.py`; no other claim verified here.

## 0. Target revision and poll record

Producer Q1's completion signal (report + `dual_pointer` present in tool) arrived while polling
with the 20 s / 40-try protocol (script `.ufo/waves/round-96/seats/V04-c1-dual-pointer.scratch/poll_q1b.sh`):

```
READY attempt=5 report=.ufo/waves/round-96/seats/Q1-tool-hardening.md dual_pointer_hits=2 contract_cases=22
```

(An earlier poll gated additionally on Q2's contract at ≥24 cases and ran 15 attempts before being
replaced; Q2's contract was observed at 24 cases later in the run — see §6.)

Verified revisions (hashes taken before and after every run; unchanged):

| revision | sha256 | md5 | note |
|---|---|---|---|
| baseline r95 (`git show dcb2d92:corpus/tools/map_obligations.py`) | `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` | `d31b8182953e9088a155f4ed2978af5b` | matches r95 closure pin and Q1's cited baseline |
| delivered r96 (`corpus/tools/map_obligations.py`, blob `010b8b63f49944a310ef907533123f255fa1af7b`) | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` | `869c365d1c4ec106da198c78deca2708` | equals Q1's declared delivered sha256; frozen copy in scratch re-hashes identically after all runs |

Fixtures: 16 scratch clusters built by `.ufo/waves/round-96/seats/V04-c1-dual-pointer.scratch/build_fixtures.py`
under `…/V04-c1-dual-pointer.scratch/fixtures/` (4 JSON files each: `entities.json`, `relations.json`,
`timeline.json`, `claim-excerpt-map.md`; raw=4 obligations, all single mappings except where a cell is
rewritten). Matrix runner `run_matrix.py`; transcripts `matrix-before-r95.json`, `matrix-after-r96.json`,
`after-matrix.txt`, `r88-delivered.txt`, `self-test.txt`.

## 1. Before — V37-D1 reproduced on the r95 baseline

Baseline tool run on the two required scratch forms (legacy-header table, `JSON fact and fields`
pointer column):

```
$ python3 r95-map_obligations.py fixtures/legacy-dup-paren     # cell: `entities[0].first_appearance` (Aru; also `entities[1].first_appearance`)
OBLIGATIONS raw=4 mapped=4
RESULT PASS
exit=0
$ python3 r95-map_obligations.py fixtures/legacy-dup-colon     # cell: `entities[0].claims[0]`: test claim; also `entities[1].first_appearance`
OBLIGATIONS raw=4 mapped=4
RESULT PASS
exit=0
```

All five legacy dual-pointer probes (parenthetical, colon-prose, mapped second token, bare second
token, canonical token in a legacy cell) exited 0 with no finding on the baseline — the hidden
second pointer was silently ignored, exactly as V37-D1 reports.

## 2. After — required demonstrations on the delivered revision

Exact cells (fixture file lines 7–8):

- `legacy-dup-paren` row E1: `` `entities[0].first_appearance` (Aru; also `entities[1].first_appearance`) ``
- `legacy-dup-colon` row E2: `` `entities[0].claims[0]`: test claim; also `entities[1].first_appearance` ``

Delivered tool, direct invocations (each also run twice through `run_matrix.py` repeat=2 with
byte-identical exit/stdout/stderr; a third direct run shown here):

```
$ python3 corpus/tools/map_obligations.py …/fixtures/legacy-dup-paren
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
exit=1

$ python3 corpus/tools/map_obligations.py …/fixtures/legacy-dup-colon
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E2 (line 8) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/claims/0
RESULT FAIL
exit=1
```

Stable ID `dual_pointer` and identical row/line/token detail on every repetition (2× matrix runs +
1 direct run each; run1==run2 for all 16 matrix cases in exit+stdout+stderr). The row is still read
by its first token, so no cascading `missing_obligation` noise — `mapped=4` unchanged.

Additional delivered-revision probes (all exit 1, `FINDING dual_pointer`, stable across the two runs):

| fixture | cell override | finding detail |
|---|---|---|
| `legacy-dup-paren-mapped` | `` `entities[0].claims[0]`: test claim; also `timeline[0]` `` | second token `'timeline[0]'` alongside `entities.json#/0/claims/0` (second token is itself a mapped raw obligation) |
| `legacy-dup-colon-bare` | `` `entities[0].claims[0]`: test claim; see entities[1].first_appearance `` | second token `'entities[1]'` alongside `entities.json#/0/claims/0` (bare, unbackticked) |
| `legacy-dup-paren-canon` | `` `entities[0].first_appearance` (see also `timeline.json#/0`) `` | second token `'timeline.json#/0'` alongside `entities.json#/0/first_appearance` (canonical-style token in legacy cell) |

## 3. Single-pointer legacy cells still PASS

Scratch controls (both runs exit 0, `OBLIGATIONS raw=4 mapped=4`, `RESULT PASS`):
`legacy-base` (all four plain legacy cells), `legacy-single-paren` (`` `entities[0].first_appearance` (Aru) ``),
`legacy-single-colon` (`` `entities[0].claims[0]`: test claim text ``),
`legacy-single-both` (`` `timeline[0]` (`description`, `source_id`): test event `` — note the
backticked field names, not pointer tokens, in the parenthetical), and `legacy-canon-single`
(canonical fallback cell under the legacy header).

Real r88 fixture (`corpus/fixtures/r88-m3-maya-cluster`), whose cells include exactly the three
single-pointer shapes at lines 23/27/31 (`…first_appearance` (Aru); `…claims[0]`: colon prose;
`timeline[0]` (`description`, `source_id`): colon prose):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

Byte-identical to the r95 baseline run on the same fixture — no regression on r88's real cells.

## 4. Canonical-dialect two-pointer cells — pre-existing behavior quoted, not weakened

Pre-existing canonical screening (r95 baseline and delivered revision produce byte-identical
output here; matrix diff shows these three cases unchanged):

```
$ python3 corpus/tools/map_obligations.py …/fixtures/canon-dup-note    # `entities.json#/0/first_appearance` (`entities.json#/0/claims/0`)
FINDING unsupported_map: co-mapped or unsupported pointer grammar
RESULT ERROR
exit=2
$ python3 corpus/tools/map_obligations.py …/fixtures/canon-dup-token   # `entities.json#/0/first_appearance; entities.json#/0/claims/0`
FINDING unsupported_map: co-mapped or unsupported pointer grammar
RESULT ERROR
exit=2
$ python3 corpus/tools/map_obligations.py …/fixtures/canon-two-tokens  # `entities.json#/0/first_appearance` `entities.json#/0/claims/0`
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR
exit=2
```

Canonical single-pointer controls (`canon-base`, `canon-single-note`, `canon-note-plain`) still
exit 0 PASS. So canonical two-pointer cells remain rejected by the pre-existing `unsupported_map`
screening (exit 2), and the new `dual_pointer` gate is confined to the legacy dialect — consistent
with Q1's declared bound (§7.2 of `Q1-tool-hardening.md`).

## 5. Matrix diff — exactly the declared scope changed

Programmatic diff of run-1 outputs, baseline vs delivered (`matrix-before-r95.json` vs
`matrix-after-r96.json`): exactly 5 cases changed, all legacy dual-pointer probes, exit 0 → 1
(`legacy-dup-paren`, `legacy-dup-colon`, `legacy-dup-paren-mapped`, `legacy-dup-colon-bare`,
`legacy-dup-paren-canon`); the other 11 cases are byte-identical (exit + stdout), including all
single-pointer legacy controls and all canonical controls. Run1==run2 for all 16 delivered cases
(exit+stdout+stderr): `all after cases run1==run2: True`.

## 6. Adjacent observations (context; not this seat's claim)

- Q2's contract landed at 24 cases during the run; on the delivered revision
  `python3 corpus/tools/map_obligations.py --self-test` prints `SELF-TEST CASES 24/24 pinned`,
  24 `SELF-TEST PASS` lines including `schema_drift exit=1` and `inventory_mismatch exit=1`,
  `RESULT PASS`, true exit 0 (captured with output redirected, not piped). This is part (b)
  context only — V01/V02-class seats own those claims.
- One transient `map-obligations-self-test-*` directory was visible in the repo root mid-run and
  absent on re-check minutes later (`ls`/`stat` returned nothing), consistent with Q1 §7.5 and the
  documented BR-05 behavior; no action taken (not this seat's ownership).
- Delivered tool sha256 re-checked after all runs: unchanged `2b0ba815…`.

## 7. Method / hygiene

- All mutations ran on scratch fixture copies under `.ufo/waves/round-96/seats/V04-c1-dual-pointer.scratch/`;
  the corpus tree was never written by this seat. Writes: this report (exclusive path) plus that
  scratch dir only. No commits, no pushes, no network, no nested agents.
- Baseline captured from a `git show dcb2d92:…` snapshot before Q1 landed; delivered revision
  frozen into scratch immediately after Q1's report appeared, and re-hashed after each batch.

## Bottom line

**PASS** — on delivered `map_obligations.py` sha256 `2b0ba815…` (== Q1's declared revision,
unchanged throughout): legacy-dialect cells naming a second pointer in parenthetical or
colon-prose exit 1 with the stable `dual_pointer` finding (identical twice each; baseline r95
exits 0 silently, V37-D1 reproduced and closed), single-pointer legacy cells including all of
r88's real cells still PASS 12/12, and canonical two-pointer cells retain their pre-existing
`unsupported_map` exit-2 screening byte-for-byte.

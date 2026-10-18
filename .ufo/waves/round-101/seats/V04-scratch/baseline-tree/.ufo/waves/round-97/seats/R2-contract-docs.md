# R2 — contract-docs (round 97, single-wave swarm)

Seat: R2 contract-docs. Lane: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo; every write below used an absolute path under
the lane repo and was verified there). Baseline: r96 closure `f3e09f9`
(HEAD observed: `2393934 lore r96: close round — SCORECARD admitted section`).

Byte-ownership honoured: I wrote only
`corpus/tools/map-obligations-contract.json`, `corpus/tools/README.md`, this
report, and scratch under `.ufo/waves/round-97/seats/R2-scratch/`. No commits,
no pushes, no network, no nested agents.

## Delivered revision under test

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py        (R1)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json (mine, post-edit)
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md                 (mine, post-edit)
```

Pre-R1 tool revision (for the before-demo):
`2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8`
(r96-revision `map_obligations.py`, copied to scratch before R1 landed).

R1 status: the tool artifact landed and was stable at sha `86b52949…` from
poll try 9 onward; R1's report (`.ufo/waves/round-97/seats/R1-map-pinning.md`)
arrived at 18:48 local, after my probes. Cross-check against it: same delivered
sha `86b52949…`, same baseline `2b0ba815…`, same live contract sha `2142b991…`
(25 cases, pin `dual_pointer`), the same direct-CLI fixture output
(`row E1 (line 7) … alongside entities.json#/0/first_appearance`, exit 1), and
an independently reproduced r96 tolerance (`23/24 pinned` / `RESULT PASS`,
exit 0). R1 neutralized the emission at `parse_map_text`'s `if mention is not
None:` (`exit=1 findings=[]`), I neutralized `second_pointer_mention()`
(`exit=0 findings=none`); both turn the pinned case red — different probe
points, same verdict. No discrepancy found between R1's report and my
independent observations.

## (1) 25th persisted case: `dual_pointer` — hand-derived, then pinned

Hand-derivation was done on scratch clusters of the self-test fixture's shape
(4 obligations: `entities[0].first_appearance`, `entities[0].claims[0]`,
`relations[0]`, `timeline[0]`; legacy header `JSON fact and fields`), built by
`R2-scratch/build.py`, before the pin was added:

```
$ python3 corpus/tools/map_obligations.py handderive/clean     # no hidden token
OBLIGATIONS raw=4 mapped=4
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py handderive/r1cell    # R1's exact cell:
#   | E1 | `entities[0].first_appearance` (also named `entities[1].first_appearance`) | `fixture-source` |
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
exit=1
```

Derived expectation: `exit 1`, exactly `["dual_pointer"]` — the row is still
read by its first token, so no cascading `missing_obligation` /
`phantom_obligation`; the clean twin of the same fixture exits 0, so the case
isolates the `dual_pointer` emission. R1's implementation independently builds
the same shape (`legacy_test_rows()` + `DUAL_POINTER_CELL`,
`map_obligations.py:732-734`), which matches the hand-derived expectation.

Pin added to the contract (diff is exactly one added line):

```diff
       {"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]},
+      {"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}
```

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
… 25 × "SELF-TEST PASS <case> …"
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
exit=0
```

`python3 -m json.tool corpus/tools/map-obligations-contract.json` → valid;
25 cases parsed.

## (2) Tightened loader — demonstrated on scratch contract copies

Because the loader resolves the contract from the tool's own directory
(`Path(__file__).resolve().with_name(...)`), each probe ran a byte-identical
copy of the delivered tool (sha printed and equal to `86b52949…`) beside a
scratch contract copy; the delivered contract was never mutated.

Before (r96 revision `2b0ba815…` + contract copy dropping `schema_drift`):

```
SELF-TEST CASES 23/24 pinned
… 23 PASS lines …
RESULT PASS
exit=0
```

After (delivered revision `86b52949…`):

```
$ (scratch contract: dropped 'schema_drift', cases 25 -> 24)
FINDING self_test_contract: contract drops implemented self-test cases: schema_drift
RESULT ERROR
probe_drop_schema_drift_exit=2

$ (scratch contract: dropped 'complete', cases 25 -> 24)
FINDING self_test_contract: contract drops implemented self-test cases: complete
RESULT ERROR
probe_drop_complete_exit=2
```

Both fail closed before any case is exercised — the subset tolerance is gone
for added pins *and* core pins. Loader line:
`missing = sorted(set(SELF_TEST_CASES) - set(expected))`
(`map_obligations.py:820`; was `set(CORE_SELF_TEST_CASES)`).

## (3) The new pin is load-bearing

Scratch tool copy with the emission neutralized
(`second_pointer_mention()` short-circuited to `return None`):

```
SELF-TEST CASES 25/25 pinned
SELF-TEST FAIL dual_pointer exit=0 findings=none
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

Removing the behavior turns the pinned case red — the pin is not decorative.

## (4) README Round-97 addendum

`corpus/tools/README.md` gained a `### Round-97 addendum` section (dual_pointer
pinned + hand-derived expectation, subset tolerance closed with before/after
output, load-bearing probe, 25-case self-test, unchanged-behavior list). Diff
is additive only: `git diff --numstat` → `49 0`, and
`git diff | grep -c '^-[^-]'` → `0`. All prior text is intact.

## Non-regression battery (delivered revision)

| command | observed |
|---|---|
| `map_obligations.py corpus/fixtures/r88-m3-maya-cluster` | exit 0, `raw=10 mapped=10`, `INVENTORY … 10/10; 2/2; 12/12` |
| `… r93-m2-kojiki-cluster` | exit 0, `raw=12 mapped=12` |
| `… r94-paired-crossing` | exit 0, `raw=14 mapped=14` |
| `… r95-crossing-aftermath` | exit 0, `raw=15 mapped=15` |
| `… r96-crossing-response` | exit 0, `raw=16 mapped=16` |
| `… --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | exit 0, `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` |
| `… corpus/fixtures/r87-myth-cluster` | exit 2 `unsupported_map` (fail-closed, unchanged) |
| `… corpus/fixtures/r89-inspiration-paraphrase` | exit 2 `unsupported_map` (unchanged) |

## Observations / follow-ups (not my writes)

1. `SKILL.md:87` still says "24 cases" and records both r96 residuals
   ("`dual_pointer` behavior is demonstrated by mutation demos, not pinned";
   "the two r96-added pins are droppable") — both are closed by this round.
   `corpus/README.md:37` also still says "24 persisted cases". These two files
   are outside my byte-ownership (read-only for me); flagged for the closure
   doc pass.
2. `corpus/fixtures/r97-crossing-acknowledgment`: mid-flight at my first
   check it showed `OBLIGATIONS raw=17 mapped=16` / `FINDING missing_obligation:
   timeline.json#/5 has no map row`, exit 1 (R5's map not yet landed). Re-run
   after R5 landed: `OBLIGATIONS raw=17 mapped=17` / `INVENTORY JSON-FACTS
   17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19` / `RESULT PASS`, exit 0 — the
   delivered tool (with the r97 pin) passes the r97 fixture. Not my claim
   (C3 belongs to R4/R5 and its verifiers); recorded as observed state.
3. r96 README addendum line 173's "Residuals (r97 debt)" sentence is left as
   delivered history and is superseded by the new Round-97 section (per
   instruction to keep prior text).

Bottom line: **PASS** — contract pins `dual_pointer` as case 25, `--self-test`
is 25/25 green on the delivered revision, a dropped pinned case now fails
closed (exit 2, quoted), the pin is load-bearing under neutralization, and the
r88–r96 corpus battery plus frozen replay are unchanged.

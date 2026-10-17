# V45 — census-paths (round 95)

Seat: V45 `census-paths`. Scope: after P3 lands, confirm the repo-relative argv
convention holds for the new fixture `corpus/fixtures/r95-crossing-aftermath` —
`check_bible` / `support_check` / `map_obligations` all pass with the repo-relative
path, and no absolute-path assumptions appear in outputs.

Baseline: HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (r94 closure `fb118c4`).
All commands run from repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with
`python3`. Scratch files under `/tmp` only; no writes outside this report path.

## Poll-wait (declared protocol: 20 s cadence, 40 tries)

Targets: P3 fixture JSON tables + P4 `claim-excerpt-map.md`.
Observed (log `/tmp/v45-poll.log`): tries 1–12 `missing: claim-excerpt-map.md`;
`TRY 13: COMPLETE at 2026-10-17T16:21:12-03:00` — all 9 watched files present.

Producer revisions landed while I worked: `map_obligations.py` evolved
`cc1df4dc…` (r94 revision, at P3 receipt) → `3f87fe8b…` (P1 landed, 22 self-test
cases) → `d1c239cc…` (final); `map-obligations-contract.json` `349a1956…` (20
cases) → `8173bb97…` (P2 landed 2026-10-17T16:27:05-03:00, 22 cases). A second
poll (`/tmp/v45-poll2.log`) waited for the P1/P2 artifacts and completed with
`TRY 22: ALL PRESENT`.

Fixture files at receipt:

```
sources.json fd9e30e8…, entities.json 026af0bc…, relations.json c279254b…,
timeline.json 3c0faad6…, contradictions.json 37517e5f…, claim-excerpt-map.md 30281ff1…
```

Final tool hashes (working tree, uncommitted, all receipts below re-run on these):
`map_obligations.py` `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`;
`map-obligations-contract.json` `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`;
`support_check.py` `55a5eb27…`; `check_bible.py` `ff9fd2aa…`.

## Receipt — repo-relative argv (final revision, all exit 0)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations          # exit 0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                          # exit 0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                          # exit 0
```

The INVENTORY line reflects the map's own declaration (map line 5: `**Expected
inventory:** 15 JSON facts; 2 editorial rows; 17 total mapped rows; 13 distinct
excerpt anchors`) and shows no `MISMATCH` suffix. Counts agree with the round's C2
claim (15 map obligations = 14 inherited + 1 new event row); r94 control under the
same revision gives 14/14 + 2/2 and `raw=14 mapped=14`, so the delta is exactly the
new row.

## Path-form invariance

Same three commands repeated with `./corpus/...` and with the absolute path
`/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/...`: all 9 runs exit 0 and
`cmp` shows stdout byte-identical across the three forms for each tool:

```
check_bible stdout byte-identical across 3 forms
support_check stdout byte-identical across 3 forms
map_obligations stdout byte-identical across 3 forms
```

## No absolute-path assumptions in outputs

`grep -nE "/home/|/tmp/|(^|[^A-Za-z0-9_.-])/[A-Za-z]"` over captured stdout of all
three passing runs (pre-P1, P1-revision, and final batches):

```
no-absolute-path-tokens
```

Negative control (documents the convention's boundary, run from `/tmp`): with the
repo-relative argv from a non-root cwd the tools fail closed —
`check_bible` exit 1 (`VIOLATION: sources.json: cannot load JSON: [Errno 2] No such
file or directory: 'corpus/fixtures/r95-crossing-aftermath/sources.json'`),
`support_check` exit 2 (`FAIL: cluster directory not found: corpus/fixtures/r95-crossing-aftermath`),
`map_obligations` exit 2 (`FINDING cluster_missing: cannot resolve cluster: [Errno 2]
No such file or directory: '/tmp/corpus'`). Absolute argv from `/tmp` works
(`raw=15 mapped=15 … RESULT PASS` exit 0). So the convention is anchored at repo
root; only failure diagnostics echo a cwd-joined absolute path, never passing
receipts.

## Read-only proof

10 fixture files hashed before/after the 3×3 run batch: `FIXTURE-UNCHANGED`; repeated
on the P1 revision: `FIXTURE-UNCHANGED-ON-P1-REVISION`; final revision re-run:
`FIXTURE-UNCHANGED-FINAL`. No tool writes into the fixture directory.

## Producer-landing transient (resolved)

Before P2's contract landed, `python3 corpus/tools/map_obligations.py --self-test`
transiently exited 2 (`FINDING self_test_contract: contract self-test cases do not
match the implemented cases`) because the P1 tool already carried 22 cases while the
contract still carried 20. After P2 landed (contract `8173bb97…`, 22 cases) the
self-test on the final revision exits 0 with 22 `SELF-TEST PASS` lines:

```
$ python3 corpus/tools/map_obligations.py --self-test
… 22 × SELF-TEST PASS …
RESULT PASS                                                          # exit 0
```

Adjacent observations on the final revision (outside this seat's scope, quoted for
corroboration): `map_obligations` r94 control `raw=14 mapped=14` exit 0, r93
`raw=12 mapped=12` exit 0, r88 `raw=10 mapped=10` + `TOTAL-ROWS 12/12` exit 0;
r87 and r89 still `RESULT ERROR` exit 2.

## Bottom line

PASS — on the final delivered revision (`map_obligations.py` `d1c239cc…`, contract
`8173bb97…`), `check_bible` / `support_check` / `map_obligations` all pass (exit 0)
with repo-relative argv on `corpus/fixtures/r95-crossing-aftermath`, stdout is
byte-identical across relative/./absolute path forms, no absolute-path tokens appear
in passing outputs, the fixture is unmodified by the runs, and the earlier
`self_test_contract` transient is resolved (self-test exit 0, 22/22).

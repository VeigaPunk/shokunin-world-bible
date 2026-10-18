# S1 full-file pins — round 99

Seat: S1. Owned bytes: `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`. No other tracked writes. No commit. Baseline tool/contract identical at `4265df5` and `HEAD` `337f0fa` (`git diff --stat 4265df5 HEAD --` those two paths: empty).

Axes: calibration (pinned-file edits become exit 2 `DIGEST-MISMATCH` naming the file); coverage (six-fixture chain still verifies, semantic inventories unchanged); operability (self-test 17→18, 17 inherited expectations identical); freshness (`payload_schema_version` 2). Depth not this seat. Adjacency: tracked diff is only the two owned files.

## What changed

Pin payload is now all ten declared files, not the five JSON tables. Each pin carries `payload_schema_version: 2` and `pinned_files` equal to:

`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

Contract root `schema_version` 1→2 and `payload_schema_version` 2. A pin missing that version, or not digesting exactly those ten files, is `CONTRACT-INVALID` (exit 2). `--freeze` refuses a fixture missing any of the ten (`FILE-MISSING`) and is still scope-guarded. Verification still lets semantic findings decide first (exit 1). An inventory-clean byte change or deletion of a pinned file exits 2 `DIGEST-MISMATCH` and names the file (`sha256 <before> -> <after>`, or `-> None` if deleted).

`r88-m3-maya-cluster/symbolism-clause-map.md` is outside the declared ten and is not pinned. `r99-window-lapse` was not pinned: C1's chain is the existing six, and that fixture is other seats' bytes (it was being written during this seat).

Self-test case `markdown_tamper` (18th): in the isolated case tree, append one newline to `fictional-excerpts.md`. Persisted expectation: exit 2, finding `DIGEST-MISMATCH`, `names_file: fictional-excerpts.md`. The 17 inherited expectation objects are identical to `HEAD`.

## Chain re-freeze and verify

Cwd: `/home/vgpnk/Projects/shokunin/lore-shokunin`.

```
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r88-m3-maya-cluster
```

```
FROZEN r88-m3-maya-cluster: events 2; dependency-edges 0; relations 0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
```

exit 0. Same command for the other five, each exit 0:

- r94 `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` events 3/3 edges 2/2 relations 1/1
- r95 `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` events 4/4 edges 3/3 relations 1/1
- r96 `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` events 5/5 edges 4/4 relations 1/1
- r97 `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` events 6/6 edges 5/5 relations 1/1
- r98 `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` events 7/7 edges 6/6 relations 1/1

Re-verify on the delivered tool (after the final message-string edit), same cwd:

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>
```

All six printed `RESULT PASS` and exited 0, with the digests above. 6/6.

Against `HEAD` pins: `events`, `relations`, `counts`, and the five JSON file digests are unchanged for all six. Only the content digest and the five Markdown digests were added. Each delivered pin has `payload_schema_version` 2 and exactly the ten files.

Before the successful re-freeze, the new tool against the old pin exited 2:

```
FINDING CONTRACT-INVALID: pin r94-paired-crossing payload_schema_version None != 2 (full-file pin of 10 files)
RESULT ERROR
```

An earlier `--freeze` attempt failed closed before any write (`FINDING MALFORMED-JSON: README.md: Expecting value: line 1 column 1 (char 0)`) because Markdown was parsed as JSON. That path was fixed; only the five tables are parsed. The successful freeze above is the delivered pin set.

Missing pinned file, scratch mirror only (delivered contract hash unchanged):

```
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r94-paired-crossing
```

```
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/r94-paired-crossing: pinned file(s) missing: inspiration-note.md
RESULT ERROR
```

exit 2.

## Self-test

```
python3 corpus/tools/dependency_freeze.py --self-test
```

```
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

exit 0. Re-run after the final detail-string edit: same 18/18, exit 0. Inherited expectation objects compared to `git show HEAD:corpus/tools/dependency-freeze-contract.json`: all 17 `identical=True`. Added case only: `markdown_tamper`. Dropped: none.

## Before / after — dependency wording removed from an r94 excerpt copy

Live fixtures were not edited. Both sides use a path-bound mirror because a foreign path is `PATH-MISMATCH` since r97. The before mirror holds `git show HEAD:` of the tool and contract (r98 closure bytes) plus a copy of `corpus/fixtures/r94-paired-crossing`. In `fictional-excerpts.md` only, this sentence:

`Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court.`

was replaced with the same sentence beginning `Their tick-10 decision follows both ninth-bell entries:`. Confirmed on the scratch copy: `depends on both ninth-bell` absent, `follows both ninth-bell` present.

That sentence is the J14 anchor in `claim-excerpt-map.md` (lines 18-20). So this removal is not invisible to every gate. Quoted, do not smooth it.

Cwd: `.ufo/waves/round-99/seats/S1-scratch/before/mirror`

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
```

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
```

exit 0. That digest is the HEAD JSON-only pin (`2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75`). The old freeze did not see the excerpt edit.

```
python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
```

exit 1. Tail:

```
SOURCE-SUPPORT 13/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 15/16
FAIL: J14: source-support anchor missing
RESULT FAIL
```

```
python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
```

```
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
```

exit 0.

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
```

```
CLEAN: schema, citations, relations, timeline; 0 violations
```

exit 0.

After, same mutation, delivered tool and re-frozen contract. Cwd: `.ufo/waves/round-99/seats/S1-scratch/after/mirror`

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
```

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest 68ae0332a911e4d1cef8b93c18aab567b19ebc656f23ad6089b95810b1882f76 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> 6b67dcdaef2e4048bc466bd1e00a154c627883471415dd40635fbceb66b999b0); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2. Names `fictional-excerpts.md`.

Contradiction with the declaration's "invisible to every gate": the anchored sentence removal is caught by `support_check` (exit 1, J14) on the r98 tool. It is invisible to the r98 `dependency_freeze`, to `map_obligations`, and to `check_bible`. It is not a semantic proof; the new pin detects the edit.

## Non-anchor excerpt edit — the class the five-file pin missed

Same r94 copy, HEAD tool, only the unanchored heading changed (`# Authored in-world excerpts` → that heading plus ` (dependency wording left intact)`). That token is not in the map. Cwd: `.ufo/waves/round-99/seats/S1-scratch/before-nonanchor`

- `dependency_freeze.py` exit 0, `DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75`, `RESULT PASS`
- `support_check.py` exit 0, `SOURCE-SUPPORT 14/14`, `RESULT PASS`
- `map_obligations.py` exit 0, `OBLIGATIONS raw=14 mapped=14`, `RESULT PASS`
- `check_bible.py` exit 0, `CLEAN: schema, citations, relations, timeline; 0 violations`

Same tree, delivered tool and contract swapped in:

```
FINDING DIGEST-MISMATCH: content digest f559baaa7e6facbefb8a65f6be4eb4b5feb622c233e18bd4ace5ba03c332a034 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> 1deff0153f063b504cb4e2414c1d6bfd5d9c889c8a1c92fbf279c41d7f18be33); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2. This is the edit class that was green on every fixture gate before and is named after. BR-01's prose half is edit-detectable, not semantics-provable.

## Any pinned-file edit names the file

Scratch mirror of delivered tool+contract, r94 copy, one trailing newline, then verify. Each exit 2 `DIGEST-MISMATCH` naming that file only: `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`, `entities.json`.

Delete `fictional-excerpts.md` on a fresh copy:

```
FINDING DIGEST-MISMATCH: content digest dec0a20280e2da7fae055459bd7edaba6567acd2cfd980f7d9193cf700c5205f != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2.

## Scope

```
git diff --name-only
```

```
corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency_freeze.py
```

`git diff --stat`: contract +163/−, tool +67/−, 207 insertions, 23 deletions. Scratch only under `.ufo/waves/round-99/seats/S1-scratch/`. Did not write `r99-window-lapse`, README, SKILL.md, or knowledge notes.

PASS — C1 delivered (payload_schema_version 2, ten-file pins, chain 6/6, self-test 18/18, DIGEST-MISMATCH names fictional-excerpts.md). Bound: the anchored r94 "depends on" sentence removal is not invisible to support_check (exit 1, J14) before the pin upgrade; r98 dependency_freeze, map_obligations, and check_bible stay green, and a non-anchor excerpt edit is invisible to all four gates before and named after.

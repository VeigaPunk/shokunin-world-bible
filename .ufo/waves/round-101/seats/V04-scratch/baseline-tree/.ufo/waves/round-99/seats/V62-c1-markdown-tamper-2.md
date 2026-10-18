# V62 c1-markdown-tamper-2

Independent second Markdown-tamper matrix. Copies only, under `.ufo/waves/round-99/seats/V62-scratch/`. No live corpus writes. No commits.

Measured bytes (stable from matrix start through recheck at 2026-10-17T22:30:56-03:00):

- `corpus/tools/dependency_freeze.py` `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`
- `corpus/tools/dependency-freeze-contract.json` `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`

S1 producer report: **ABSENT** at every poll and at recheck (`ls .ufo/waves/round-99/seats/S1*.md` → no such file). The matrix is of the landed tool and contract, not of an S1 narrative. Those bytes did not change during the run (`LIVE_STABLE True`).

## What landed

Contract top-level `schema_version` 2, `payload_schema_version` 2. `pinned_files` is the ten declared names (five JSON + README + claim-excerpt-map + fictional-excerpts + inspiration-note + source-excerpt). All six chain pins (`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`) carry `payload_schema_version` 2 and digests for exactly those ten files. `r99-window-lapse` is not pinned (the claim's chain is 6/6, not 7). Self-test expectation count is 18; `markdown_tamper` is `{"exit": 2, "finding_ids": ["DIGEST-MISMATCH"], "names_file": "fictional-excerpts.md", "forbid_traceback": true}`.

The runner enforces `names_file` (`dependency_freeze.py:611-614`: `names_file in output`). The persisted case appends one newline to `fictional-excerpts.md` (`dependency_freeze.py:576-580`).

## Live chain, before copies

Cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`. Each:

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>
```

Observed, all exit 0:

```
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS

FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS

FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS

FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS

FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS

FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
```

## Copy matrix

Command:

```
python3 .ufo/waves/round-99/seats/V62-scratch/matrix.py
```

Mirror tool sha matched the live tool (`6f81f8be…`). Each case invoked the mirror tool on the mirror fixture, then restored bytes. After the run, `diff -rq` of each of the six mirror fixtures against the live fixtures reported identical. Live `r98-clerk-filing/*.md` modes remained `644`.

Clean copies reproduced the six live digests above, exit 0.

### Single-file interior edit — 30/30

Mutation: insert `V62` after byte 0 of one Markdown file, restore after. Expected: exit 2, one `DIGEST-MISMATCH`, that filename only.

All 30 (6 fixtures × 5 Markdown files) matched. Representative, r98 (the other five fixtures had the same shape: exit 2, `RESULT ERROR`, exactly one `changed:` name):

```
CMD /usr/bin/python3 .../V62-scratch/mirror/corpus/tools/dependency_freeze.py .../mirror/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 2f63bab81919100d10a17fa9cf60f7775ae780dd72211735ceb802ab52a93b64 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: README.md (sha256 32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926 -> 33002e425ab6c6d4658dadd8b471848fc0c4acba2653ddf91f7fe2d0bf2e0771); fixture bytes changed outside the frozen inventory
RESULT ERROR
```

Same command, other r98 files, each exit 2, each naming only itself:

- `claim-excerpt-map.md (sha256 c1099d0e… -> affac51c…)`
- `fictional-excerpts.md (sha256 29e384bf… -> 4c73ebef…)`
- `inspiration-note.md (sha256 58f5390e… -> 4b1f11f6…)`
- `source-excerpt.md (sha256 b5edc2fd… -> 0c7cb81d…)`

Inventory counts stayed at the pin (events/edges/relations unchanged). No exit 1 semantic finding on a Markdown-only edit.

### Dependency-wording removal — edit-detectable, not semantics-provable

On copies of r95 and r98, first `depends on` in `fictional-excerpts.md` replaced with `follows` (the excerpt sentence is `Their tick-10 decision depends on both ninth-bell entries…`). Both exit 2 and name only that file. r98:

```
FINDING DIGEST-MISMATCH: content digest c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> dbcd5f11f4260f0e85c3271698afe1bac79ace52c31e9b651187371fb79e4b26); fixture bytes changed outside the frozen inventory
RESULT ERROR
```

r95 named `fictional-excerpts.md (sha256 0ef6734a… -> b0725e21…)`, exit 2. The finding does not say that dependency wording was removed. BR-01's prose half is byte-detectable here; it is not semantics-provable.

### Two-file simultaneous edit — 6/6

Append `\nV62-TWO\n` to `README.md` and `fictional-excerpts.md` together. All six fixtures exit 2 and name both files, no others. r98:

```
FINDING DIGEST-MISMATCH: content digest 51dbd6788c22901dc611cca67d29c4c29239ea4c8e0df84c20499059fd09487a != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: README.md (sha256 32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926 -> 227c0ded19bb4981c7ffae247146694c0e5775c5a5b6d9f35cbcef3c8e7832a2), fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> 6feb5c36f26f9fe5a61765ae902cbffbacc98faab717ae3c893afd5550f09093); fixture bytes changed outside the frozen inventory
RESULT ERROR
```

Five-file simultaneous append of one newline on r98 also exit 2 and named all five Markdown files in one `changed:` list (`README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`).

### Permission-only observation

On the r98 copy, each of the five Markdown files was `chmod 0o600` with bytes untouched, then restored to `0o644`.

Observed modes (matrix `stat`): all five `0o644 -> 0o600`, sha256 unchanged, restored `0o644`. Verify exit 0 on each:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
```

A readable mode change is invisible. The gate hashes bytes, not mode.

Unreadable mode, same copy, `README.md` `chmod 0o000` (restored to `0o644` after):

```
FINDING FILE-MISSING: README.md is unreadable: [Errno 13] Permission denied: '.../V62-scratch/mirror/corpus/fixtures/r98-clerk-filing/README.md'
RESULT ERROR
```

Exit 2, but `FILE-MISSING`, not `DIGEST-MISMATCH`. A permission change that blocks the read is a different finding and does not name a digest delta.

Sibling metadata observation, not a claim requirement: `os.utime` on `source-excerpt.md` (mtime changed) stayed exit 0 `RESULT PASS` on the same digest. Same-bytes rewrite of `inspiration-note.md` also stayed exit 0.

### Bound: unpinned extra Markdown stays invisible

r88 has `symbolism-clause-map.md`, which is not in the ten-file pin. Appending `\nV62-UNPINNED\n` on the copy:

```
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
```

Exit 0. The pin covers the declared ten, not every file in the directory. This does not contradict the claim; it is the remaining prose blind spot for files outside the pin.

## Self-test on the copy

```
CMD /usr/bin/python3 .../V62-scratch/mirror/corpus/tools/dependency_freeze.py --self-test
EXIT 0
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

Because `names_file` is enforced, the `markdown_tamper` ok line means that case's output contained `fictional-excerpts.md`.

## Tally

55 recorded results, 0 mismatches against the expectations above: clean-copy 6, md-interior 30, wording-removal 2, two-file 6, five-md 1, perm-readable 5, perm-unreadable 1, mtime-only 1, unpinned-md 1, same-bytes-rewrite 1, self-test 1. Full stdout is in `.ufo/waves/round-99/seats/V62-scratch/matrix-results.json`.

## Not claimed

This matrix does not prove that a wording removal is caught as a semantic dependency change. It proves the byte change is named. It does not cover a simultaneous semantic JSON mutation plus a Markdown edit (precedence would exit 1 first; not run). It does not cover an S1 report, which never landed.

PASS — copy matrix: every pinned Markdown edit, including two-file and wording removal, exits 2 DIGEST-MISMATCH naming the file(s); readable permission-only (644→600) stays PASS; self-test 18/18. S1 report ABSENT; bytes are tool 6f81f8be… / contract 8c2561b0….

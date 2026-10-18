# V09 — c1-cross-gates (round 99)

- Seat: V09 c1-cross-gates (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (HEAD at poll start `337f0fa`; wave tree uncommitted). Commands from the lane root. `python3` is `/usr/bin/python3` (`sys.executable` in the runner).
- Task: one scratch copy of `corpus/fixtures/r96-crossing-response`, five independent mutations (edge reduction; prose-word removal; map row drop; span break; source-id change). Tabulate exits of `check_bible`, `support_check`, `map_obligations`, `dependency_freeze`, and `boundary_doc_check` default. `dependency_freeze` must catch the edge reduction and the prose edit. Name which gates catch which mutation. Quote commands and outputs.
- Axes judged here: matrix completeness (5 mutations × 5 gates, plus an intact control), attribution (one mutation per copy), evidence fidelity (quoted exits), isolation (scratch only).
- Writes: this report and `.ufo/waves/round-99/seats/V09-scratch/` only. No commits, no pushes, no network, no nested agents. Seats dir realpath checked before the report write: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats`. No symlink components on that path.

## 0. Poll-wait

Producer reports were absent at the first checks (`round-99/` did not exist at 2026-10-18T01:00:59Z). Cadence 20 s. The freeze tool and contract moved during the poll (schema-1 five-file pins, then schema 2 with pins still five files, then schema-2 ten-file pins). Nothing in §2–§4 was measured on those mid-flight bytes.

Landing gate for this seat: S1's report present, r96 pin `payload_schema_version` 2 with 10 files, and tool+contract sha256 unchanged across a consecutive pair of checks. `POLL_STABLE` in `.ufo/waves/round-99/seats/V09-scratch/poll.log`:

```
POLL_STABLE try=11 s1=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S1-full-file-pins.md tool=fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c contract=8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
```

That line is 2026-10-18T01:49:04Z. S3 (`S3-fixture-author.md`) and S4 (`S4-fixture-docs.md`) were already present. S2 and S5 reports were still absent. This matrix does not read their bytes; it reads S1's delivered tool and contract. Measurement started only after a further 15 s stability check (01:53:38Z → 01:53:53Z) reproduced the same two shas.

## 1. Revision pinned for every measurement

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

Same pair after the matrix (`LIVE_BYTES_UNCHANGED`). r96 pin on that contract: `payload_schema_version` 2, ten files (`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`), counts events 5 / dependency-edges 4 / relations 1, digest `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c`. That digest is the one S1's report records for r96.

Intact live fixture, lane root:

```
$ /usr/bin/python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT=0
```

`dependency_freeze` path-binds, so each scratch fixture was evaluated in a mirror whose tool and contract were byte-copies of the two hashes above (7 mirrors, both shas reproduced) with the mutant at `corpus/fixtures/r96-crossing-response` under that mirror root. The other four gates ran on the foreign scratch path (`check_bible` / `support_check` / `map_obligations`) or with no fixture argument (`boundary_doc_check` default). Full transcripts: `.ufo/waves/round-99/seats/V09-scratch/transcripts/`.

## 2. The one r96 copy and the five mutations

Base copy: `V09-scratch/base/r96-crossing-response` (`python3 V09-scratch/mutate.py`). Each mutant is a fresh copy of that base with one replacement, count asserted equal to 1. Diffs: `V09-scratch/diff-*.txt`.

| mutant | file | change |
|---|---|---|
| edge-reduction | `timeline.json` | `response-evin-salt-court.depends_on` `["aftermath-missing-evin"]` → `[]` (key kept) |
| prose-word | `fictional-excerpts.md` | word `depends` removed from the J14 anchor sentence: `Their tick-10 decision depends on both ninth-bell entries` → `Their tick-10 decision on both ninth-bell entries` |
| map-row-drop | `claim-excerpt-map.md` | J16 table row deleted; expected-inventory line left at 16/2/18/14 |
| span-break | `claim-excerpt-map.md` | J16 span cell `33-42` → `33-36` (anchor is line 37) |
| source-id | `timeline.json` | `response-evin-salt-court.source_id` `evin-response-note` → `paired-clock` (still a source id in `sources.json`) |

Edge-reduction diff:

```
-    "depends_on": [
-      "aftermath-missing-evin"
-    ],
+    "depends_on": [],
```

Prose-word diff (one line):

```
-> Their tick-10 decision depends on both ninth-bell entries: …
+> Their tick-10 decision on both ninth-bell entries: …
```

## 3. Exit matrix

Intact base copy, same five gates: all exit 0 (`CLEAN`; `RESULT PASS` 16/16 and `raw=16 mapped=16`; freeze `DIGEST 43911900…` `RESULT PASS`; boundary `CERTIFIED`). So every non-zero below is the mutation.

| mutation | check_bible | support_check | map_obligations | dependency_freeze | boundary default | gates that catch it |
|---|---:|---:|---:|---:|---:|---|
| edge-reduction | 0 | 0 | 0 | **1** | 0 | `dependency_freeze` only |
| prose-word | 0 | **1** | 0 | **2** | 0 | `support_check` and `dependency_freeze` |
| map-row-drop | 0 | **1** | **1** | **2** | 0 | `support_check`, `map_obligations`, `dependency_freeze` |
| span-break | 0 | **1** | 0 | **2** | 0 | `support_check` and `dependency_freeze` |
| source-id | 0 | 0 | **1** | **2** | 0 | `map_obligations` and `dependency_freeze` |

`check_bible` caught none of the five. `boundary_doc_check` with no arguments caught none (same `CERTIFIED` line every time; it does not take a fixture).

### edge-reduction — freeze catches it; the other four stay green

```
$ /usr/bin/python3 corpus/fixtures/check_bible.py .ufo/waves/round-99/seats/V09-scratch/mutants/edge-reduction/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
$ /usr/bin/python3 corpus/tools/support_check.py …/mutants/edge-reduction/r96-crossing-response
SOURCE-SUPPORT 16/16; … VALIDATED-ROWS 18/18
RESULT PASS
EXIT=0
$ /usr/bin/python3 corpus/tools/map_obligations.py …/mutants/edge-reduction/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
RESULT PASS
EXIT=0
$ /usr/bin/python3 …/mirrors/edge-reduction/corpus/tools/dependency_freeze.py …/mirrors/edge-reduction/corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 3/4; relations 1/1
FINDING REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']
RESULT FAIL
EXIT=1
$ /usr/bin/python3 corpus/tools/boundary_doc_check.py
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
EXIT=0
```

### prose-word — freeze catches it (exit 2, names the file); support_check also catches it

This is the dependency-word removal inside the J14 anchor. It is not invisible to every gate.

```
$ /usr/bin/python3 corpus/tools/support_check.py …/mutants/prose-word/r96-crossing-response
SOURCE-SUPPORT 15/16; … VALIDATED-ROWS 17/18
FAIL: J14: source-support anchor missing
RESULT FAIL
EXIT=1
$ /usr/bin/python3 corpus/tools/map_obligations.py …/mutants/prose-word/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
RESULT PASS
EXIT=0
$ /usr/bin/python3 …/mirrors/prose-word/corpus/tools/dependency_freeze.py …/mirrors/prose-word/corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
FINDING DIGEST-MISMATCH: content digest ebc0bd340ccea31182bb1fdb71cc09d21a1e228698d3c4e3d4dfd754fecf39ff != pin 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c; changed: fictional-excerpts.md (sha256 06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3 -> 291588734b23552583e64431203cd0e9c0516a399a4fc172d105327d02c1e59e); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

`check_bible` exit 0 `CLEAN`. Boundary exit 0 `CERTIFIED`.

### map-row-drop

```
FAIL: inventory JSON facts mismatch: expected=16 parsed=15
FAIL: inventory total mapped rows mismatch: expected=18 parsed=17
FAIL: inventory distinct excerpt anchors mismatch: expected=14 parsed=13
RESULT FAIL
EXIT=1
```

`support_check`. `map_obligations`:

```
OBLIGATIONS raw=16 mapped=15
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17
FINDING missing_obligation: timeline.json#/4 has no map row
RESULT FAIL
EXIT=1
```

`dependency_freeze` exit 2 `DIGEST-MISMATCH` naming `claim-excerpt-map.md` (`e851f068…` → `a96c033d…`). `check_bible` 0. Boundary 0.

### span-break

```
FAIL: J16: anchor hit outside declared line span 33-36 (hit lines: 37)
RESULT FAIL
EXIT=1
```

`support_check` only among the semantic gates. `map_obligations` exit 0 `raw=16 mapped=16`. `dependency_freeze` exit 2 `DIGEST-MISMATCH` naming `claim-excerpt-map.md` (`e851f068…` → `0b2ef260…`). `check_bible` 0. Boundary 0.

### source-id

`check_bible` exit 0 `CLEAN` (the new id exists). `support_check` exit 0 `RESULT PASS`. `map_obligations`:

```
FINDING source_id_mismatch: timeline.json#/4 does not bind to 'paired-clock'
RESULT FAIL
EXIT=1
```

`dependency_freeze` exit 2 `DIGEST-MISMATCH` naming `timeline.json` (`ea0225f9…` → `e2a3418b…`). Semantic inventory unchanged (edges still 4/4); the catch is the content digest, not `REDUCTION-DETECTED`. Boundary 0.

## 4. Isolating control (not one of the five)

The prose-word case above removes a word that is the J14 anchor, so `support_check` was never blind to it. A second scratch copy removed the word `depends` once from map prose that is not a table anchor (`ordered after and depends on both (`aru-ninth-bell`` → `ordered after and on both (`aru-ninth-bell``). On that copy:

- `check_bible` 0 `CLEAN`
- `support_check` 0 `SOURCE-SUPPORT 16/16` `RESULT PASS`
- `map_obligations` 0 `raw=16 mapped=16` `RESULT PASS`
- `dependency_freeze` **2** `FINDING DIGEST-MISMATCH: … changed: claim-excerpt-map.md (sha256 e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de -> b10ac6ac1c45b279f8182f1bdc9adc97707cb22902154bb7dffbf66c0acc2515); pinned-file bytes changed outside the semantic inventory` `RESULT ERROR`
- boundary 0 `CERTIFIED`

That is the edit class the five-file pin missed and the ten-file pin names. It is edit-detection, not a semantic proof of the dependency claim.

## 5. Write audit

Post-run tool sha `fb9bb9ff…` and contract sha `8c2561b0…` match §1. Live `corpus/fixtures/r96-crossing-response/` ten-file sha256 list identical before and after (`r96-before.txt` / `r96-after.txt`). `git status --short` on that fixture is empty. The two freeze files are modified, and those modifications are S1's (present before this seat's first write, hashes unchanged across the matrix). This seat wrote only under `V09-scratch/` and this report.

## Scope

Shown: on the hash-pinned delivered tool and contract, after S1's report landed, the five mutations on one r96 base copy produce the exit table in §3, and `dependency_freeze` catches both required cases (edge reduction exit 1 `REDUCTION-DETECTED`; prose-word removal exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`). Not shown: that the frozen inventories are semantically the right edges, or any C2 claim. S2 and S5 reports were not on disk at measurement time; this matrix does not use their files.

## Bottom line

**PASS** — on one scratch r96 copy, `dependency_freeze` catches the edge reduction (`FINDING REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']`, edges 3/4, exit 1) and the prose-word removal (`FINDING DIGEST-MISMATCH` naming `fictional-excerpts.md`, exit 2); the other catches are `support_check` on prose-word, map-row-drop, and span-break, and `map_obligations` on map-row-drop and source-id; `check_bible` and boundary default catch none of the five.

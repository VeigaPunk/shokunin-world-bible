# V16 — preservation-mutations (2026-10-17)

Axes: calibration (discriminate the accumulated mutations without overstating semantic reach), coverage (six classes across four gates), adjacency/preservation (no live-fixture or tool mutation). This is the V16 verifier result, not round-wide admission.

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` for Python invocations. Declared baseline: `fe1ce46`; observed HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. `git show --stat --oneline HEAD` identified the latter as `lore r100: declare sol-max 32-seat round before dispatch`, changing only LOG.md. No commits, pushes, network, nested agents, live `--freeze`, or live mutations were made by V16.

## Producer prerequisite and ownership

The bounded poll checked all ten r100 fixture files, both new r100 knowledge records, the actual r99 contract pin, and nonempty T1–T4 reports at 20-second intervals, with a 40-check maximum. It succeeded at check 25, within budget:

```text
attempt=25 time=2026-10-17T23:40:30.188480-03:00
missing=[]
T1=.ufo/waves/round-100/seats/T1-chain-seven.md
T2=.ufo/waves/round-100/seats/T2-fixture-author.md
T3=.ufo/waves/round-100/seats/T3-fixture-docs.md
T4=.ufo/waves/round-100/seats/T4-knowledge-author.md
r99_pinned=true ready=true
PRODUCERS_READY
observed_exit=0
```

No artifact-only placeholder was accepted as delivery. No all-seat report poll was performed, so SELF was never included in a wait. No stall escape was needed. Initial observations are not hidden: the first `Read` of lane AGENTS.md returned `does not exist`; the initial lane-root `pwd && ls .ufo/waves/round-100/seats && git status --short` printed the correct cwd, then `ls: cannot access '.ufo/waves/round-100/seats': No such file or directory`, exit 2, before production created the directory. These were prerequisite absences, not delivered-fixture verdicts.

Writes were confined to this report and the declared absolute scratch root `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V16-scratch/`:

- `run_matrix.py`: new isolated mutation/replay harness, checked with `ast.parse` (`HARNESS-SYNTAX PASS`).
- `matrix/{inputs.json,results.json,commands.log}`: input hashes, structured outcomes/expectations, and the complete unabridged 56-command transcript.
- `matrix/{r100,r99}/{control,m1-empty-deps,m2-wrong-earlier,m3-delete-terminal,m4-span-break,m5-source-rebind,m6-coherent-prose}/`: each contains new `corpus/fixtures/<fixture>/` files, exact copies of the four gate scripts and freeze contract at their original relative paths, and `{bible,support,map,freeze}.{stdout,stderr}.txt`.
- `regression/corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json,map_obligations.py,map-obligations-contract.json}`, the ten-file `regression/corpus/fixtures/r95-crossing-aftermath/` base, and `regression/self-tests.log`. Automatically cleaned self-test temporary trees stayed inside that regression mirror.

For the six-class matrix, every mutant was generated into a previously absent path from immutable in-memory input bytes; no matrix fixture or live file was subsequently edited. The mirrored freeze tool derives its root from its own path, so the pinned r99 fixture resolves to the contract's recorded `corpus/fixtures/r99-window-lapse`, not a foreign-path receipt. No matrix or live contract was hand-edited or re-frozen; the persisted self-tests use their own disposable internal cases.

## Binding and delivered controls

Snapshot time: `2026-10-17T23:40:39.487099-03:00`. `matrix/inputs.json` records every input and producer-report hash. The four gate implementations are unchanged from r99 closure: this actual command exited 0 with no output:

```sh
git diff --exit-code fe1ce46 -- corpus/fixtures/check_bible.py corpus/tools/support_check.py corpus/tools/map_obligations.py corpus/tools/dependency_freeze.py
```

Observed SHA-256 values:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5  corpus/tools/dependency-freeze-contract.json
```

Key r100 snapshot hashes are `timeline.json` `008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8`, `claim-excerpt-map.md` `16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244`, and `fictional-excerpts.md` `d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705`.

Actual direct live-fixture control commands and observed excerpts:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
CLEAN: schema, citations, relations, timeline; 0 violations
observed_exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
observed_exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
observed_exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
observed_exit=2
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
observed_exit=0
```

The live r99 bible/support/map controls were also run: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse` produced the same CLEAN line, exit 0; `python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse` produced `SOURCE-SUPPORT 21/21`, `MODES 23/23`, `VALIDATED-ROWS 23/23`, `RESULT PASS`, exit 0; `python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse` produced `OBLIGATIONS raw=21 mapped=21`, `TOTAL-ROWS 23/23`, `RESULT PASS`, exit 0.

## Six accumulated classes and the complete exit matrix

Each class ran on both r100 and its path-bound pinned-r99 counterpart. This additionally demonstrates freeze behavior on the newly admitted r99 pin without inventing an r100 pin.

1. **m1-empty-deps:** set the final event's `depends_on` to `[]`: r100 `clerk-review-first-passage`, r99 `clerk-lapse-recorded`.
2. **m2-wrong-earlier:** replace that final event's predecessor with the event two rows earlier: r100 `clerk-lapse-recorded` → `clerk-filing-open`; r99 `clerk-filing-open` → `acknowledgment-aru-records`. Every substituted predecessor exists and is earlier, isolating the semantic-edge blind spot.
3. **m3-delete-terminal:** remove only the final timeline event, retaining the corresponding map row and its unchanged declaration/anchor. The r100 phantom is `timeline.json#/8`; r99's is `timeline.json#/7`.
4. **m4-span-break:** change only J05's declared span `17` → `20`, leaving the actual anchor at line 17.
5. **m5-source-rebind:** bind the final event to another existing source without changing the map: r100 `clerk-review-note` → `clerk-lapse-note`; r99 `clerk-lapse-note` → `clerk-filing-note`.
6. **m6-coherent-prose:** in both `fictional-excerpts.md` and its J14 map anchor, replace `depends on both ninth-bell entries` with `follows both ninth-bell entries`. JSON and line positions are unchanged, so this is coherent excerpt-plus-anchor replacement, not an excerpt-only missing-anchor probe.

Actual harness command:

```sh
python3 .ufo/waves/round-100/seats/V16-scratch/run_matrix.py
```

Observed complete summary, harness exit 0 (each gate's actual CLI command, stdout, stderr, exit, and expected-finding match is persisted in `matrix/results.json` and `matrix/commands.log`):

```text
r100 control: bible=0[-]; support=0[-]; map=0[-]; freeze=2[UNPINNED-FIXTURE]
r100 m1-empty-deps: bible=0[-]; support=0[-]; map=0[-]; freeze=2[UNPINNED-FIXTURE]
r100 m2-wrong-earlier: bible=0[-]; support=0[-]; map=0[-]; freeze=2[UNPINNED-FIXTURE]
r100 m3-delete-terminal: bible=0[-]; support=0[-]; map=1[phantom_obligation]; freeze=2[UNPINNED-FIXTURE]
r100 m4-span-break: bible=0[-]; support=1[-]; map=0[-]; freeze=2[UNPINNED-FIXTURE]
r100 m5-source-rebind: bible=0[-]; support=0[-]; map=1[source_id_mismatch]; freeze=2[UNPINNED-FIXTURE]
r100 m6-coherent-prose: bible=0[-]; support=0[-]; map=0[-]; freeze=2[UNPINNED-FIXTURE]
r99 control: bible=0[-]; support=0[-]; map=0[-]; freeze=0[-]
r99 m1-empty-deps: bible=0[-]; support=0[-]; map=0[-]; freeze=1[REDUCTION-DETECTED]
r99 m2-wrong-earlier: bible=0[-]; support=0[-]; map=0[-]; freeze=1[ADDITION-DETECTED,REDUCTION-DETECTED]
r99 m3-delete-terminal: bible=0[-]; support=0[-]; map=1[phantom_obligation]; freeze=1[REDUCTION-DETECTED]
r99 m4-span-break: bible=0[-]; support=1[-]; map=0[-]; freeze=2[DIGEST-MISMATCH]
r99 m5-source-rebind: bible=0[-]; support=0[-]; map=1[source_id_mismatch]; freeze=2[DIGEST-MISMATCH]
r99 m6-coherent-prose: bible=0[-]; support=0[-]; map=0[-]; freeze=2[DIGEST-MISMATCH]
EXPECTED-MATCHES 56/56
INPUT-DRIFT {}
EVIDENCE .ufo/waves/round-100/seats/V16-scratch/matrix/results.json
```

`56/56` means expected outcome matches, not 56 green gate results. Non-zero negative probes are the intended evidence. There were no expectation mismatches, unexpected stderr findings, or delivered-control failures. `[-]` means no stable FINDING IDs, not that a support failure had no diagnostic.

## Command-level discriminating receipts

These are actual commands, with selected observed output where indicated; the full outputs are retained in `matrix/commands.log`.

### Empty and wrong-but-earlier edges: pinned r99 catches what structural checks leave clean

```text
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m1-empty-deps/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m1-empty-deps/corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m2-wrong-earlier/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m2-wrong-earlier/corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ADDITION-DETECTED: event clerk-lapse-recorded gained depends_on ['acknowledgment-aru-records']
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1
```

On both fixtures' corresponding m1/m2 copies, bible stayed `CLEAN ... 0 violations`, support stayed `RESULT PASS`, and map stayed `RESULT PASS` (exits 0). The r99 semantic findings precede any digest finding: no `DIGEST-MISMATCH` was emitted.

### Terminal deletion: a retained map row is load-bearing

```text
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r100/m3-delete-terminal/corpus/tools/map_obligations.py .ufo/waves/round-100/seats/V16-scratch/matrix/r100/m3-delete-terminal/corpus/fixtures/r100-docket-review
OBLIGATIONS raw=21 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
FINDING phantom_obligation: timeline.json#/8 is not a raw source-attributed obligation
RESULT FAIL
observed_exit=1
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m3-delete-terminal/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m3-delete-terminal/corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 7/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded is missing; 1 frozen dependency edge(s) gone
RESULT FAIL
observed_exit=1
```

The structural checker and lexical support remained clean on terminal deletion. This probe does not claim that a consistently regenerated map/declaration would fail mapping: the map row was deliberately retained.

### Span break: support is not silent

```text
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r100/m4-span-break/corpus/tools/support_check.py .ufo/waves/round-100/seats/V16-scratch/matrix/r100/m4-span-break/corpus/fixtures/r100-docket-review
```

Observed excerpts, exit 1:

```text
FAIL J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.; span=20; outside-span=17
SOURCE-SUPPORT 21/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 23/24
FAIL: J05: anchor hit outside declared line span 20 (hit lines: 17)
RESULT FAIL
```

The pinned r99 m4 invocation in `matrix/commands.log` exited 2 `DIGEST-MISMATCH`, naming `claim-excerpt-map.md`, with content digest `a9718342a70863ffa0a71ef82b5df5b428b9f45f2d15d91b9465434fa3306b4b`. That is byte-change detection, not a freeze span-rule finding.

### Source-ID rebinding: raw/map agreement is distinct from lexical support

```text
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r100/m5-source-rebind/corpus/tools/map_obligations.py .ufo/waves/round-100/seats/V16-scratch/matrix/r100/m5-source-rebind/corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
FINDING source_id_mismatch: timeline.json#/8 does not bind to 'clerk-lapse-note'
RESULT FAIL
observed_exit=1
```

The structural checker and support stayed clean. The pinned r99 m5 freeze invocation exited 2 `DIGEST-MISMATCH`, naming `timeline.json`, with content digest `88d0f9eb20a46380a6db697de408a923d776e6c4d7d0e030a80ab89e23c02301`; there was no semantic source-ID finding from freeze.

### Coherent prose edit: use pinned r99, never call unpinned r100 a digest proof

```text
$ python3 .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m6-coherent-prose/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/V16-scratch/matrix/r99/m6-coherent-prose/corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest ac372f2ccf46e58cbfced6d70b2ce7615eadd73c350f91ab8ccfa9bc0d895c6a != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: claim-excerpt-map.md (sha256 d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d -> b8f436b78a84b9a4277cd9268dd6175e45e0331f8be21dec081cc501ad8ff4a9), fictional-excerpts.md (sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d -> 44f7b1326350dcfd264b554c3a352edf8ca308285665002590b780aa5ffeaa34); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2
```

The r99 prose mutant remained `CLEAN` (bible exit 0), `SOURCE-SUPPORT 21/21` / `RESULT PASS` (support exit 0), and `OBLIGATIONS raw=21 mapped=21` / `RESULT PASS` (map exit 0). The identical coherent prose class on r100 remained CLEAN / support 22/22 / map 22/22; its freeze result was `UNPINNED-FIXTURE`, exit 2, not `DIGEST-MISMATCH`. Thus r99 demonstrates current prose byte detectability, while r100's tick-16/prose bytes remain outside the declared seven-pin set. No dependency-prose entailment is established by either result.

## Regression suites and final preservation check

The standard persisted suites were replayed on byte-identical tools/contracts in V16's own mirror so their temporary trees did not escape the exclusive scratch root. Actual commands and observed terminal excerpts:

```text
$ python3 .ufo/waves/round-100/seats/V16-scratch/regression/corpus/tools/dependency_freeze.py --self-test
SELF-TEST 18/18
RESULT PASS
observed_exit=0
$ python3 .ufo/waves/round-100/seats/V16-scratch/regression/corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
RESULT PASS
observed_exit=0
```

The full regression transcript contains all 18 freeze `CASE ... ok` and 25 `SELF-TEST PASS` records, including `markdown_tamper`, `schema_drift`, `inventory_mismatch`, and `dual_pointer`.

A final lane-root Python audit loaded `matrix/results.json`, required exactly 56 matching outcomes and no during-run drift, and recomputed SHA-256 for all 31 snapshotted live inputs (four tools, the freeze contract, twenty fixture files, two knowledge records, and four producer reports). Observed exit 0:

```text
FINAL-INPUT-STABILITY 31/31
MATRIX-RESULT-CONTRACT 56 outcomes; all expected matches; zero live-input drift
```

The report path was resolved and checked under the lane before its Write. No production file needed repair. The intentional non-zero probes and the intentional r100-unpinned bound are not unresolved implementation failures; they delimit what was actually tested. Census, whole-claim manual entailment, source authenticity, chronology truth, rights/permission, and round-wide admission are not certified by V16.

PASS — six accumulated mutation classes preserved with 56/56 expected CLI outcomes, pinned-r99 prose edits detected by named-file DIGEST-MISMATCH, r100 explicitly unpinned, regression suites 18/18 and 25/25 green, and 31/31 live inputs unchanged.

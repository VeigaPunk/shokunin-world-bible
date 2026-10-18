# V69 — crosscheck-coverage-2 (round 99, single-wave)

**Seat scope (verbatim):** *V69 verdict-crosscheck-coverage-2 — report
.ufo/waves/round-99/seats/V69-crosscheck-coverage-2.md — Independent coverage
verdict; compare V30.*

Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Baseline r98 closure `4265df5e86e4121bde4125b649b89bb1676676a5`. HEAD during
the wave `337f0fa52b02626b7687eedbb2d99fab30446fe4` (wave tree uncommitted).
Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this
report plus `.ufo/waves/round-99/seats/V69-scratch/` only. Seats-dir realpath
checked before the report write:
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats`.

Coverage is a witnessed axis this round, not a claimed one. The standing
declaration assigns full-file pinning to **C1 calibration** and the lapse
fixture plus blind-spot table to **C2 depth**. This seat judges whether that
work harmed, left unchanged, or expanded the coverage axis. It does not
re-label C1 as a coverage improvement.

## 0. Revision pinned for the verdict

Stable across the battery (22:50:52) and a re-hash after the extra probes
(22:54):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

Contract: `schema_version` 2, top-level `payload_schema_version` 2, exactly
six pins, each `payload_schema_version` 2 and exactly the ten declared files.
`r99-window-lapse` is not a pin. Self-test expectations: 18, added
`markdown_tamper` only. The 17 inherited expectation objects are
`identical=True` against `git show HEAD:corpus/tools/dependency-freeze-contract.json`.
Dropped: none.

Other gate tools, sha256 versus `4265df5`: unchanged —
`check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`,
`map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`,
`support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`,
`boundary_doc_check.py` `ebb6a0843e67bfaa3118eda7fbf69bac124aca8f5b87cd0b9721b5e6346b0053`,
`map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41`.

## 1. Poll-wait record

Cadence 20 s, max 40. Wait set: S1 report, S3 report, S4 report, S5 report,
r99 fixture content (`clerk-lapse-recorded` + `clerk-lapse-note`), a pin with
≥10 files, `r99-gate-blind-spot-table.md`, and V30's report. **SELF (V69) was
never in the wait set.** No all-reports poll.

```
try=1  2026-10-17 22:04:40 -0300  pins10=0 s1=no s3=yes s4=no s5=no v30=no table=no
try=6  2026-10-17 22:13:07 -0300  pins10=6 s1=no s3=yes s4=yes s5=no v30=no table=no
try=40 2026-10-17 22:24:28 -0300  pins10=6 s1=no s3=yes s4=yes s5=no v30=no table=no
ABSENT after 40 tries
```

The ten-file pins were on disk from try 6. S1's report was not. Measuring
those bytes before the report would have been measuring a moving tool: the
tool hash moved `1728ed89…` → `6f81f8be…` → `fb9bb9ff…` (message-string edit
only on the last step; contract stayed `8c2561b0…` from 22:08:46). A recorded
stability watch then held `fb9bb9ff…` / `8c2561b0…` for two consecutive 20 s
checks. S1's report `S1-full-file-pins.md` was present at the first stable
check (22:50:12; file mtime 22:48). The battery below is on that revision.

V30 was still absent. Post-battery stall-escape, 4 × 20 s, recorded in
`V69-scratch/battery.txt`:

```
escape=1 22:50:55 s1=True v30=False
escape=4 22:51:55 s1=True v30=False
ESCAPE-EXPIRED
```

Rechecked again at 22:53:57 and after the newline-gate probe: no
`V30-*.md`. V30's own poll log ends `ABSENT after 40 tries` at 22:15:29;
their 15-try escape expired at 22:34:07. Comparison target **ABSENT**.

S5's report and `corpus/knowledge/r99-gate-blind-spot-table.md` were also
absent. They are C2 depth, not this axis. Not graded here.

## 2. Independent coverage verdict

**Coverage unchanged, not harmed.** The six-fixture chain still verifies.
Semantic inventories (`events`, `relations`) are identical to the r98 pins.
Every inherited detection class still fires at its old exit. The ten-file
payload is C1 (a previously ignored byte class is now a named
`DIGEST-MISMATCH`), not a new semantic coverage class and not a seventh chain
fixture.

### 2a. Before — prose edit invisible to the r98 freeze

Baseline bytes extracted with `git archive 4265df5e86e4121bde4125b649b89bb1676676a5`
into `V69-scratch/before/baseline-root` (tool `03d04365…`, contract
`153ebc5b…`, the r98 closure pair). The tool's `ROOT` is that mirror, so the
pin path resolves inside it. Mutation is in place at
`corpus/fixtures/r98-clerk-filing/` (a renamed copy is `UNPINNED-FIXTURE` and
does not test the pin).

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
EXIT:0
```

Wording removal (`depends on` → `follows`, one occurrence, in
`fictional-excerpts.md`) and a README append both still printed that same
digest, `RESULT PASS`, exit 0. A non-inventory JSON space in `"tick": 14`
was already caught, and already named the file:

```
FINDING DIGEST-MISMATCH: content digest 4a54729c… != pin 59a0f4fa…; changed: timeline.json
(sha256 eb24e084… -> 902783ef…); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT:2
```

So the r98 gap was Markdown, not "digest never names a file."

### 2b. After — chain 6/6, inventories unchanged, pins recompute

Delivered tool on delivered paths:

```
r88-m3-maya-cluster          events 2/2  edges 0/0  rel 0/0  DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae  PASS exit 0
r94-paired-crossing          events 3/3  edges 2/2  rel 1/1  DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef  PASS exit 0
r95-crossing-aftermath       events 4/4  edges 3/3  rel 1/1  DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710  PASS exit 0
r96-crossing-response        events 5/5  edges 4/4  rel 1/1  DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c  PASS exit 0
r97-crossing-acknowledgment  events 6/6  edges 5/5  rel 1/1  DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54  PASS exit 0
r98-clerk-filing             events 7/7  edges 6/6  rel 1/1  DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0  PASS exit 0
```

Independent recompute (does not import the tool; sha256 of the ten raw
files, compact sorted-JSON content digest, event→sorted-`depends_on` sets,
endpoints, relation triples): `files=True digest=True events=True
relations=True` for all six, and `vs-baseline-events=True
vs-baseline-relations=True` against the `4265df5` pins. r88's only extra
file is `symbolism-clause-map.md`. Pin `revision` on all six is HEAD
`337f0fa52b02626b7687eedbb2d99fab30446fe4`.

`r99-window-lapse` on the delivered tool:

```
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json
(pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath',
'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT:2
```

That is the declared 6/6, not a silent chain shrink and not a seventh pin.
The new tick-15 edge is outside the frozen set. Same class as the r97 V46
gap, not discharged this round, not a fail of the declared chain.

### 2c. Inherited detection classes still fire

```
$ python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 18/18
RESULT PASS
EXIT:0
```

All 17 inherited cases `ok` at their old exits (`reduction_edge_drop` exit 1
`REDUCTION-DETECTED`, `addition_edge_phantom` exit 1 `ADDITION-DETECTED`,
`event_endpoint_change` / `relation_endpoint_flip` exit 1 `ENDPOINT-CHANGE`,
`digest_tamper` exit 2 `DIGEST-MISMATCH`, `scope_refused` / `path_mismatch` /
`self_test_mismatch` exit 2). `markdown_tamper` exit 2 `DIGEST-MISMATCH`,
and the case output names `fictional-excerpts.md` (the persisted
`names_file` check passed). Contract sha256 unchanged by the run. No
`dependency-freeze-self-test-*` leftover.

Semantic precedence is unchanged. On a mirror copy of r98, dropping
`clerk-filing-open`'s `depends_on`:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
EXIT:1
```

The same edge drop plus a newline on `fictional-excerpts.md` printed the
same `REDUCTION-DETECTED` and exit 1. The digest finding was not emitted.
An inventory finding still decides first; a Markdown edit does not swallow it.

### 2d. What the ten-file pin adds — and what it does not

Newline appended to each of the five Markdown files, one mirror each, pinned
path, delivered tool. Each exit 2 `DIGEST-MISMATCH` naming only that file.
Example:

```
FINDING DIGEST-MISMATCH: content digest 3e992626… != pin 5ecf84e1…; changed: fictional-excerpts.md
(sha256 29e384bf… -> a6bff890…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT:2
```

Same class for `README.md`, `claim-excerpt-map.md`, `inspiration-note.md`,
`source-excerpt.md`. Deleting `inspiration-note.md` is exit 2 naming
`inspiration-note.md (sha256 58f5390e… -> None)`.

That newline copy is still green on the other fixture gates (anchors are
substrings; a trailing newline does not remove one):

```
check_bible.py        CLEAN … 0 violations                         EXIT:0
map_obligations.py    OBLIGATIONS raw=20 mapped=20  RESULT PASS    EXIT:0
support_check.py      SOURCE-SUPPORT 20/20  RESULT PASS            EXIT:0
```

So a non-anchor prose byte change, invisible to the r98 freeze (section 2a)
and still invisible to `check_bible` / `map_obligations` / `support_check`,
is now a named `DIGEST-MISMATCH`. That is edit-detectability. It is not a
new semantic dependency class.

The declaration's "invisible to every gate" sentence does **not** hold for
the anchored wording removal. Replacing `depends on` with `follows` in r98
`fictional-excerpts.md` (that sentence is the J14 verbatim anchor):

- r98 freeze: `RESULT PASS`, digest `59a0f4fa…`, exit 0 (section 2a).
- delivered freeze: exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`
  (`sha256 29e384bf… -> dbcd5f11…`).
- `support_check.py` on the same mutated copy: `FAIL J14: source-support
  anchor missing`, `SOURCE-SUPPORT 19/20`, `RESULT FAIL`, exit 1.
- `check_bible.py` exit 0 `CLEAN`. `map_obligations.py` exit 0 `raw=20 mapped=20`.

`support_check` already caught that removal before this round, because the
sentence is a mapped anchor, not because it judges dependency semantics.
S1 records the same contradiction (their r94 mirror: freeze digest
`2527beb9…` still PASS before; `support_check` exit 1 J14; after, digest
`68ae0332…` `DIGEST-MISMATCH` naming `fictional-excerpts.md`). I did not
replay S1's exact non-anchor heading string. The newline probe above is the
same class, measured here.

### 2e. Guard still armed; pins reproduce through `--freeze`

Mirror only. The delivered contract was not written (sha256 `8c2561b0…`
before and after every real-tree probe, including the refused `--freeze`).

```
$ python3 corpus/tools/dependency_freeze.py --freeze <V69-scratch>/outscope
FINDING SCOPE-REFUSED: --freeze refuses …/V69-scratch/outscope …;
the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
EXIT:2
```

Foreign-path copy of r98, mirror tool:

```
FINDING PATH-MISMATCH: pin r98-clerk-filing names corpus/fixtures/r98-clerk-filing
(resolves to <mirror>/corpus/fixtures/r98-clerk-filing); invoked fixture resolves to <mirror>/foreign/r98-clerk-filing
RESULT ERROR
EXIT:2
```

`--freeze` of all six fixtures inside a mirror that held the delivered tool
and contract: each exit 0 with the digests in section 2b.
`PIN-REPRODUCIBILITY` all six `EXACT-MATCH` (full pin object, including
`revision` `337f0fa…`). I did not witness S1's original invocation. The
attribution rests on S1's report (same six digests, same `FILE-MISSING`
refusal class) plus this reproduction. No contradiction on the shared numbers.

r88 `symbolism-clause-map.md` plus a newline, mirror, pinned path: still
`DIGEST acf677a7085be3f6…`, `RESULT PASS`, exit 0. Outside the ten, as declared.

## 3. Comparison with V30

**ABSENT.** No file matching `.ufo/waves/round-99/seats/V30-*.md` at poll
try 40 (22:24:28), at the post-battery escape (22:51:55), or at the 22:53
and post-probe rechecks. V30's scratch poll also recorded ABSENT at 22:15:29
and an expired escape at 22:34:07. Nothing of theirs was verified. No
agreement or disagreement to score.

Shared numbers with S1 (`S1-full-file-pins.md`), who is the producer, not
the comparison seat: the six digests, 18/18, r99 unpinned, r88 extra file
unpinned, J14 already visible to `support_check`, and "coverage = chain
still verifies, semantic inventories unchanged" all agree with the
measurements above. S1's `git diff --name-only` quote (only the two owned
files) was true at their write time; by 22:53 `SKILL.md` and
`corpus/tools/README.md` were also dirty (S2's bytes, no S2 report). That
is a docs landing, not a gate-coverage change. Not graded.

## 4. Bounds

1. Coverage here means the detection classes and the frozen chain membership.
   The ten-file payload is C1. It does not add an exit-1 finding and does not
   add r99 to the chain.
2. `r99-window-lapse`'s tick-15 edge is unfrozen (`UNPINNED-FIXTURE` exit 2).
   Declared 6/6. Not a regression of the six, and not a discharge of a new
   V46-class gap.
3. `DIGEST-MISMATCH` is could-not-evaluate (exit 2). It names the file. It
   does not prove that remaining prose still states a dependency. Combined
   with an edge drop, only `REDUCTION-DETECTED` exit 1 is emitted.
4. An anchored "depends on" removal was already exit 1 on `support_check`.
   The declaration's "invisible to every gate" sentence is false for that
   removal. The class the five-file pin missed, and the ten-file pin catches,
   is a non-anchor prose byte change.
5. r88 `symbolism-clause-map.md` is still invisible to the freeze.
6. Pin `revision` is HEAD `337f0fa` while the wave bytes are uncommitted.
   The binding I reproduced is the content digest.
7. No canon-truth, rights, identity, or entailment inference.

## 5. Write audit

`git status --porcelain` excluding `.ufo`, at 22:53:57: `M SKILL.md`,
`M corpus/tools/README.md`, `M corpus/tools/dependency-freeze-contract.json`,
`M corpus/tools/dependency_freeze.py`, `?? corpus/fixtures/r99-window-lapse/`.
No knowledge notes. No self-test leftover. My writes are
`V69-scratch/` (poll.sh, poll.log, battery.py, battery.txt, before/, after/,
outscope/) and this report. Final hashes after every probe: tool
`fb9bb9ff…`, contract `8c2561b0…`, unchanged.

## Bottom line

**PASS — COVERAGE unchanged (not harmed) on tool `fb9bb9ff…` / contract `8c2561b0…` (chain 6/6, semantic inventories identical to the r98 pins, inherited exits preserved, ten-file pin is C1 not a new coverage class); V30 comparison ABSENT (no `V30-*.md` after 40 tries plus a 4-try stall-escape).**

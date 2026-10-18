# V67 operability-2 — round 99

Seat: V67 (verifier, operability-2). Lane repo
`/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`.
Wave tree uncommitted. All live commands ran from the lane root with `python3`
unless a scratch tree's own root is stated. Leaf seat: no nested agents, no
commits, no pushes, no network. Writes: this report and
`.ufo/waves/round-99/seats/V67-scratch/` only. No live-tree file was written
by this seat.

**Axes:** operability (documented commands produce the documented receipts and
exit codes); completeness (every fenced command in both tools' documentation
plus the r99 fixture README); fidelity (quoted commands and observed output,
not producer claims); independence (own replays).

**Scope read:** "both tools' READMEs" is `corpus/tools/README.md` (the one
README that documents `dependency_freeze` and `map_obligations`, and the older
checkers in the same file) plus the SKILL.md gate rows for those two tools
(S2 owns the freeze row). The r99 fixture README is
`corpus/fixtures/r99-window-lapse/README.md`.

## 0. Poll record (content-gated, 20 s, 40 tries)

First poller (`V67-scratch/poll.sh`) was killed by a 300 s harness timeout at
try 15 (`2026-10-18T01:06:59Z`). Continuation `poll2.sh` ran tries 16–40.
Stall-escape of the poller only; recorded, not fatal. No all-reports poll
(dependency set was the docs + S2/S4 reports; SELF not in that set).

- try 1 `2026-10-18T01:02:19Z`: fixture README still the r98 placeholder;
  tools README no r99; SKILL freeze row still "17 cases" / prose-half open;
  S2 and S4 reports absent. S3 report already present.
- try 3 `01:02:59Z`: fixture README content-gate cleared (`r99-window-lapse`
  present, commands present).
- try 6 `01:03:59Z`: `S4-fixture-docs.md` present.
- try 40 `01:22:36Z`: `ABSENT after 40` — tools README still had no r99
  marker, SKILL freeze row still stale, `S2*.md` absent. S1 report also
  absent at that instant.

The r99 addendum and the SKILL freeze-row rewrite landed after the cap
(README sha `837a7f5d…`, 361 lines, mtime `2026-10-17 23:08:16 -0300`;
SKILL sha `e0bcb61a…`). `S2-tools-docs.md` was present by the close check
`2026-10-18T02:11:09Z`. Those bytes were replayed; a plan was not. Close
hashes, unchanged across the final battery:

```
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
```

`map_obligations.py` `86b52949…`, `support_check.py` `55a5eb27…`,
`boundary_doc_check.py` `ebb6a084…` match the pre-replay hashes.
`git diff --name-only 4265df5 -- corpus/tools/` lists only
`README.md`, `dependency-freeze-contract.json`, `dependency_freeze.py`.

## 1. r99 fixture README — `corpus/fixtures/r99-window-lapse/README.md:25-29`

Replayed at `01:04:14Z` and again at `02:09:33Z` (file mtimes unchanged
since `22:03:19 -0300`; sha matches S4's report). Both runs:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
bible_exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
support_exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
map_exit=0
```

The fenced block does not embed expected stdout. The prose count of 21
source-attributed obligations agrees with both receipts. No other command
is in that README.

## 2. Tools README — commands still authoritative after the r99 supersession

Historical fenced comments that the r99 addendum explicitly supersedes
(`# 20/20`, `# 22`, `# 24/24`, `# SELF-TEST 17/17`) were run once; the
latest documented expectation is what was scored. Observed:

| command | observed | exit |
|---|---|---|
| `support_check.py corpus/fixtures/r87-myth-cluster` | `SOURCE-SUPPORT 14/14` / `RESULT PASS` | 0 |
| `support_check.py corpus/fixtures/r88-m3-maya-cluster` | `SOURCE-SUPPORT 10/10` / `RESULT PASS` | 0 |
| `discriminate_check.py` | `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression` | 0 |
| `discriminate_check.py --checker e97613c` | `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present` | 2 |
| `boundary_doc_check.py` | `CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)` | 0 |
| `boundary_doc_check.py --self-test` | nine `SELF-TEST PASS` lines, then `SELF-TEST PASS` | 0 |
| pin-drift probe (README.md:57-66, verbatim subshell) | `FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes` / `observed_exit=1`; `test "$rc" -eq 1` held | probe 1, shell 0 |
| `map_obligations.py corpus/fixtures/r94-paired-crossing` | `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` | 0 |
| `map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster` | `OBLIGATIONS raw=12 mapped=12` / `RESULT PASS` | 0 |
| `map_obligations.py --self-test` | `SELF-TEST CASES 25/25 pinned` / 25 `SELF-TEST PASS` / `RESULT PASS` | 0 |
| `map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` | 0 |
| `map_obligations.py corpus/fixtures/r88-m3-maya-cluster` | `OBLIGATIONS raw=10 mapped=10` / `INVENTORY … TOTAL-ROWS 12/12` / `RESULT PASS` | 0 |
| `map_obligations.py corpus/fixtures/r87-myth-cluster` | `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` / `RESULT ERROR` | 2 |
| `map_obligations.py corpus/fixtures/r89-inspiration-paraphrase` | `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` | 2 |
| `map_obligations.py` r95 / r96 / r97 | `raw=15/15`, `16/16`, `17/17`, each `RESULT PASS` | 0 |
| `map_obligations.py --help` | exit 0, zero `RESULT` lines | 0 |

`git check-ignore -v dependency-freeze-self-test-probe/ map-obligations-self-test-probe/ v05-self-test-scratch/` printed `.gitignore:4:*-self-test-*/` for each, matching the r98 dated correction that the r99 addendum says still stands.

### 2a. Migration fence (README, scratch tree, own tool+contract copy, `pins.r95-crossing-aftermath.fixture = null`)

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
RESULT ERROR
exit=2

$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS
exit=0
```

Post-migration verify: `RESULT PASS` exit 0. Delivered contract not written.

### 2b. Same-named different-path guard

Scratch pin names `corpus/fixtures/r95-crossing-aftermath`; freeze target
`corpus/fixtures/sub/r95-crossing-aftermath`:

```
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/sub/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
exit=2
```

## 3. Round-99 addendum (`corpus/tools/README.md:290-361`)

### 3a. Chain fence (`:342-347`), verbatim

All six `FREEZE …` / `DIGEST …` / `RESULT PASS` / exit 0. Observed digests
match the documented prefixes:

```
r88 acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
r94 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
r95 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
r96 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
r97 a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
r98 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
```

Count lines: r88 `events 2/2; dependency-edges 0/0; relations 0/0`; r94 `3/3; 2/2; 1/1`; r95 `4/4; 3/3; 1/1`; r96 `5/5; 4/4; 1/1`; r97 `6/6; 5/5; 1/1`; r98 `7/7; 6/6; 1/1`.

### 3b. Self-test fence (`:353-355`)

```
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
exit=0
```

18 `CASE … ok` lines, including the 17 prior ids. Matches the comment
`# SELF-TEST 18/18 / RESULT PASS, exit 0`.

### 3c. Before/after prose-edit (`:314-324`)

Scratch `before`: `git show 4265df5:corpus/tools/dependency_freeze.py` and
the matching contract, plus a copy of `corpus/fixtures/r95-crossing-aftermath`.
Removing the first substring `depends on` from `fictional-excerpts.md`
(index 867) produced sha256
`4b13096081476ac2d92694ee26830d981c5095e786f06b64d67b34f9d4ce37fd`
(the documented after-file digest). Both the clean and the tampered before
runs printed:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
exit=0
```

Same removal in a scratch holding the delivered tool and contract
(`fb9bb9ff…` / `8c2561b0…`). Observed stdout was byte-identical to the
documented block, exit 2:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 892d17d3a9a91aab99f1da6aaac66e3854d286dcba9a2178e3a0b8b034d011b8 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> 4b13096081476ac2d92694ee26830d981c5095e786f06b64d67b34f9d4ce37fd); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

### 3d. Ten-file newline census

Each of the ten declared files, in its own scratch copy of r95, with one
trailing newline appended, exited 2 `DIGEST-MISMATCH` naming that file.
Quoted example (`README.md`):

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest c619deac7b7caecd93b8f0fd12ea388ea643ea2424a02d8336f09b88d868003b != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: README.md (sha256 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b -> 983c528cb88f0e589df97c77a8321814aebd61a80ddcb1ab5b45cbba93e40ae7); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

Same exit and naming for `entities.json`, `relations.json`, `timeline.json`,
`sources.json`, `contradictions.json`, `claim-excerpt-map.md`,
`fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

### 3e. Cross-gate fence (`:330-334`), verbatim paths

```
$ python3 corpus/tools/support_check.py .ufo/waves/round-99/seats/S2-scratch/before-r95/corpus/fixtures/r95-crossing-aftermath
SOURCE-SUPPORT 14/15; …
FAIL: J14: source-support anchor missing
RESULT FAIL
support_exit=1

$ python3 corpus/tools/map_obligations.py .ufo/waves/round-99/seats/S2-scratch/before-r95/corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS
map_exit=0

$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-99/seats/S2-scratch/before-r95/corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
bible_exit=0
```

Matches the addendum's parentheticals exactly.

### 3f. Unbound file and pin claims

Appending `V67 unbound marker` to
`corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md` on a scratch
copy (delivered tool+contract): `RESULT PASS` exit 0, digest
`acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae`.

Contract claims, measured, not taken from S2:

- `schema_version` 2, `payload_schema_version` 2.
- All six pins `revision` `337f0fa52b02626b7687eedbb2d99fab30446fe4`,
  `payload_schema_version` 2, 10 files.
- Five JSON-table digests identical to
  `git show 4265df5:corpus/tools/dependency-freeze-contract.json` for every
  chain pin (`json_same=True`); content digests moved (r97
  `3c922d20…` → `a28b9ea0…`, r98 `59a0f4fa…` → `5ecf84e1…`).
- `--freeze` was not run against the delivered contract.

## 4. SKILL.md gate rows

Freeze row (`SKILL.md:96-100`), rewritten: entry command is the six-fixture
chain above (6/6 exit 0); self-test command prints `SELF-TEST 18/18` /
`RESULT PASS` exit 0; 18 cases including `markdown_tamper`. Map row
(`SKILL.md:83-87`) unchanged in this round: cluster entry, `--frozen`
demonstration, and `--self-test` (`25/25`) all reproduced in section 2.

## 5. Findings

1. **F1 (minor, historical fraction).** The r98 mismatch paragraph still
   says a flipped `self_test.expected.clean.exit` prints `SELF-TEST 16/17`.
   The same procedure on the delivered 18-case contract printed
   `SELF-TEST 17/18`, `FINDING SELF-TEST-MISMATCH: cases failed: ['clean']`,
   `RESULT ERROR`, exit 2. The r99 addendum supersedes the `# SELF-TEST 17/17`
   comment and says `SELF-TEST-MISMATCH` still exits 2; it does not rewrite
   the `16/17` fraction, and it says earlier sentences remain as history.
   Exit class matches. Fraction does not. Bounded: no current fenced command
   is affected.

2. **Poll timing, not a command failure.** At try 40 the r99 addendum and
   S2 report were absent. They existed before this report was written and
   were replayed against the close hashes above. S2's reported hashes match
   the close hashes; the replay was not taken from S2's report.

## 6. Hygiene

Live tool/contract/README/SKILL hashes were stable from the r99-addendum
replay through the close check. `git status --short` on those paths shows
only the round's declared modifications (`SKILL.md`, tools README, the two
freeze files, untracked `corpus/fixtures/r99-window-lapse/`). Scratch for
this seat is under `.ufo/waves/round-99/seats/V67-scratch/` (poll logs,
replay captures, `mig/`, `scope/`, `mismatch/`, `v46/`, `r99replay/`).
Repo-root `v05-self-test-scratch/` is another seat's, gitignored, not
created here. `--self-test` left no repo-root residue from this seat.
`--freeze` was not run on the delivered contract.

**Bottom line: PASS** — every documented command in `corpus/tools/README.md`, the SKILL freeze and map rows, and `corpus/fixtures/r99-window-lapse/README.md` runs as written on the close revision (fixture trio exit 0, 21/21 and raw=21; chain 6/6 with the documented digest prefixes; self-test `SELF-TEST 18/18` exit 0; prose-edit `DIGEST-MISMATCH` byte-identical to the addendum, exit 2; ten-file newline census names each file; cross-gate fence matches 14/15 exit 1, raw=15 exit 0, CLEAN exit 0); one historical `16/17` fraction is stale (F1) and does not change a current command's exit.

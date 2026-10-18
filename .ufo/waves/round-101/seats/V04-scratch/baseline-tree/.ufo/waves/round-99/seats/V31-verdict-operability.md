# V31 — verdict-operability (round 99)

Seat: V31 verdict-operability. Exclusive writes: this report and
`.ufo/waves/round-99/seats/V31-scratch/` (absolute under
`/home/vgpnk/Projects/shokunin/lore-shokunin`). No product file written, no
commit, no push, no network, no nested agents. Commands from the lane root
with `python3` (3.14.7). Baseline: r98 closure `4265df5`. HEAD during the
round: `337f0fa`. One operability verdict.

Axes: documented-command replay; 0/1/2 exit contract; C1 prose-edit
detectability; non-interference; poll completeness. A first write of this
file (22:51) recorded FAIL because S2/S5 surfaces were still absent. Those
surfaces landed after the poll window. This file is the re-verification on
the landed revision, not that earlier absence.

## 0. Poll-wait and late landing

First poller started 22:02:47 -0300 and was harness-killed at its 300s cap
after try 15 (last line 22:07:27). Stall-escape, recorded, not fatal.
Restarted 22:20:53; exhausted at try 40:

```
TRY 40 2026-10-17 22:33:54 -0300 MISSING 5 ABSENT:corpus/knowledge/r99-gate-blind-spot-table.md ABSENT:corpus/knowledge/r99-lapse-scope-note.md REPORT:S1 REPORT:S2 REPORT:S5
ABSENT after 40 tries
```

Present then: S3 report, S4 report, r99 fixture (README/map no longer r98
placeholders), freeze tool, schema-2 ten-file contract. After the window,
and before this verdict: S1 report `S1-full-file-pins.md` (22:48), knowledge
notes (by 23:01), Round-99 README addendum, SKILL freeze row, S2 report
`S2-tools-docs.md`, S5 report `S5-knowledge-author.md` (23:10). No
all-reports poll ran, so SELF subtraction did not arise. Nothing below was
verified against a plan; every receipt is a command run on bytes that existed
at the time.

Frozen revision (sha256, 23:11:12 -0300):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
```

The checker hashes match the lapse note's cited revisions. README moved
`646784ae…` → `837a7f5d…` at 23:08:16 after the first addendum read; the
quoted receipts this seat reproduced (`892d17d3…`, chain digest prefixes,
`SELF-TEST 18/18`) are still in that file. Tool and contract did not move
after 22:38:11. The only post-battery tool delta versus `6f81f8be…` is the
mismatch trailing clause (`outside the frozen inventory` → `pinned-file bytes
changed outside the semantic inventory`).

## 1. S4 README and S5 lapse note — r99 replay

`corpus/fixtures/r99-window-lapse/README.md:25-29` and the lapse-note fence
(`r99-lapse-scope-note.md:52-61`), run as written (22:20:53,
`V31-scratch/r99-replay.txt`). Fixture hashes at replay equal the hashes
above.

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
EXIT=0
```

Parsed counts `6 1 8 8` (contradictions `0`). Census `ls -d corpus/fixtures/*/ | wc -l` = `173` (22:20:54 and again 23:10). Note claim that r99 is unpinned:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' … (pinned: the six chain names)
RESULT ERROR
EXIT=2
```

Matches the note and the blind-spot table. Not a missed seventh pin.

## 2. S2 Round-99 addendum — commands as written

Chain loop (`README` Round-99 addendum), all `RESULT PASS` exit 0. Observed
digests match the documented prefixes: r88 `acf677a7085be3f6…`, r94
`048b8ff39e4a5232…`, r95 `97cffd7bfe6e0c92…`, r96 `43911900923c110b…`, r97
`a28b9ea0d65ec355…`, r98 `5ecf84e19121ea12…`. r98 reconfirmed on `fb9bb9ff…`
at 22:47:11 (`RESULT PASS`, digest `5ecf84e19121ea12…`, exit 0).

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT=0
```

18 `CASE … ok` lines. The historical fence comment `# SELF-TEST 17/17` is
marked superseded in the same addendum; the runnable Round-99 fence says
18/18 and that is what printed.

Before, scratch root holding `git show 4265df5:` of the tool and contract,
r95 copy, first `depends on` deleted from `fictional-excerpts.md`:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
EXIT=0
```

After, same deletion, delivered tool and contract. Output matches the
addendum's quoted block verbatim, including both sha256s, exit 2:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 892d17d3a9a91aab99f1da6aaac66e3854d286dcba9a2178e3a0b8b034d011b8 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> 4b13096081476ac2d92694ee26830d981c5095e786f06b64d67b34f9d4ce37fd); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

A trailing newline on each of the ten pinned files of an r95 mirror: exit 2,
`DIGEST-MISMATCH`, file named, 10/10. Appending a marker to
`symbolism-clause-map.md` on an r88 mirror: `RESULT PASS` exit 0, digest
`acf677a7085be3f6…`, as documented (outside the ten). `--freeze` on a mirror
whose r95 copy lacks `inspiration-note.md`: `FILE-MISSING` exit 2, mirror
contract unchanged. Live `--freeze` was not run.

SKILL freeze row (`SKILL.md:98-100`) names 18 cases, ten-file pins, schema 2,
and "any prose edit is detectable, not dependency semantics provable". That
matches the runs above. It is prose, not a second command fence.

## 3. Blind-spot table — replayed commands

Table `verified-at` cites tool `fb9bb9ff…` and contract `8c2561b0…`, the
revision above. Concrete fences and the row-9 probes were re-run
(23:10:41, `V31-scratch/s5-replay.txt`).

- `m1-empty-deps`: `check_bible` CLEAN exit 0; `support_check` RESULT PASS
  exit 0; `map_obligations` `raw=21 mapped=21` RESULT PASS exit 0.
- `m3-delete-terminal`: CLEAN exit 0; `support_check` RESULT PASS exit 0;
  `map_obligations` `raw=20 mapped=21`, `FINDING phantom_obligation:
  timeline.json#/7 is not a raw source-attributed obligation`, RESULT FAIL
  exit 1. The table's `support_check` / `map_obligations` fences use `…/` and
  are not copy-pasteable; the expanded path reproduces the quoted lines.
- `work3/empty` delivered-tool mirror: `REDUCTION-DETECTED: event
  clerk-filing-open lost depends_on ['acknowledgment-aru-records']` RESULT
  FAIL exit 1.
- `work2/edge-drop`: `paired-crossing-decision lost depends_on
  ['evin-ninth-bell']` exit 1.
- `work2/wrong`: both `ADDITION-DETECTED` (`response-evin-salt-court`) and
  `REDUCTION-DETECTED` (`acknowledgment-aru-records`) exit 1.
- `work4/span`: digest `09858d77…` naming `claim-excerpt-map.md` exit 2,
  matching the quoted line. `m4-span-break` `support_check`: the two `FAIL
  J05` lines quoted in the table, RESULT FAIL exit 1; `check_bible` CLEAN
  exit 0; `map_obligations` PASS exit 0.
- `m5-source-id`: `FINDING source_id_mismatch: timeline.json#/7 does not bind
  to 'clerk-filing-note'` exit 1; `check_bible` CLEAN; `support_check` PASS.
- `work4/narr`: digest change names `claim-excerpt-map.md` sha `c1099d0e…` →
  `85b16b4f…`, exit 2, matching the quoted file sha.
- `m7-prose-coherent`: all three lexical gates PASS / CLEAN exit 0
  (`raw=20 mapped=20`). `m7b-excerpt-only`: `support_check` RESULT FAIL exit 1;
  bible and map stay 0.
- `work4/regen` (`<mirror>` fence, not copy-pasteable): `check_bible` CLEAN
  exit 0; `support_check` `19/19` / `DISTINCT-ANCHORS 17/17` / `VALIDATED-ROWS
  21/21` PASS exit 0; `map_obligations` `raw=19 mapped=19` PASS exit 0;
  freeze `REDUCTION-DETECTED: event clerk-filing-open is missing` exit 1.
- `python3 corpus/tools/boundary_doc_check.py`: `CERTIFIED …` exit 0.
  `--checker .ufo/waves/round-99/seats/S5-scratch/work/check_bible-drift.py`:
  `FINDING checker_drift: delivered checker digest differs from the committed
  pin` / `CERTIFICATION FAIL` exit 1.
- Row 9, each exit 1, violation lines match the table: unknown event,
  dangling entity, unknown source, required nonempty list, self dependency
  plus inversion, repeated dependency, tick inversion, deleted predecessor
  unknown event.

## 4. Exit contract on paths this seat invoked

| Path | Exit | Terminal |
|---|---|---|
| r99 check_bible / support_check / map | 0 | CLEAN / RESULT PASS |
| chain ×6 / `--self-test` | 0 | RESULT PASS / `SELF-TEST 18/18` |
| prose deletion, per-file newline, span edit | 2 | `DIGEST-MISMATCH` naming the file |
| emptied or reduced edge, deleted terminal event | 1 | `REDUCTION-DETECTED` |
| wrong-but-earlier edge | 1 | `ADDITION-DETECTED` and `REDUCTION-DETECTED` |
| r99 verify | 2 | `UNPINNED-FIXTURE` |
| no-arg; `--self-test` plus a fixture | 2 | `INVALID-ARGUMENTS` |
| missing dir with a pinned name | 2 | `FIXTURE-MISSING` |
| `--freeze` outside `corpus/fixtures/**` | 2 | `SCOPE-REFUSED`; live contract hash unchanged |
| `--freeze` missing pinned file (mirror) | 2 | `FILE-MISSING`; mirror contract unchanged |
| `--help` | 0 | no RESULT line |
| `boundary_doc_check` default / drifted checker | 0 / 1 | CERTIFIED / CERTIFICATION FAIL |

No traceback on these paths.

## 5. Non-interference

Live corpus fixtures were not edited. Mutations ran under `V31-scratch/mirrors/`
or on S5's already-delivered scratch (read-only from this seat). Scope-refused
`--freeze` left contract `8c2561b0…` unchanged. No `dependency-freeze-self-test-*`
directory remained at the repo root after `--self-test`.

## Findings (bounded; none flip the verdict)

1. Poll window closed at 22:33:54 with S1/S2/S5 reports and both knowledge
   files absent. They landed afterward. The verdict is on that later
   revision, re-run, not on the absent state.
2. Two table fences are not copy-pasteable (`…/m3-delete-terminal`,
   `<mirror>`). The expanded paths reproduce the quoted receipts.
3. r99 stays `UNPINNED-FIXTURE` exit 2. Both new knowledge surfaces say so.
   Edit-detectable, not semantics-provable: a coherent anchor regeneration
   stays green for `support_check` and `map_obligations` and is caught only
   as a named digest mismatch.
4. Verify of a missing pinned Markdown file reports `DIGEST-MISMATCH` with
   `sha256 <before> -> None`, not `FILE-MISSING`. `--freeze` of that absence
   is `FILE-MISSING`. That split matches the tool and the addendum.

## Bottom line

PASS — every documented command in S4's r99 README, S5's lapse note and blind-spot table, and S2's Round-99 tools README addendum runs as written on the frozen revision (`fb9bb9ff…` / contract `8c2561b0…` / README `837a7f5d…`): r99 replay 21/21 CLEAN/PASS exit 0, census 173, chain 6/6 with the documented digests, self-test 18/18 exit 0, the quoted r95 `depends on` deletion is invisible before (digest `d541ae64…` exit 0) and `DIGEST-MISMATCH` naming `fictional-excerpts.md` after (digest `892d17d3…` exit 2, quote-identical), and the table's catch/miss receipts reproduce — with two non-copy-pasteable fences and a post-window landing recorded, and no axis harmed.

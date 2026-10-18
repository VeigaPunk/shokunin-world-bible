# V07 — C2 support-map verification (round 100)

Seat: V07 `c2-support-map`, verifier. Axes: depth (complete canonical support-map coverage); calibration and operability are bounded guardrails. This is a C2 component-1 support/map receipt, not a round-wide admission verdict.

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Declared baseline: r99 closure `fe1ce46`; observed HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (`lore r100: declare sol-max 32-seat round before dispatch`). `git merge-base --is-ancestor fe1ce46 HEAD` exited 0. The uncommitted delivered fixture, not an assumed committed r100 revision, was checked.

Writes are limited to this exclusive report and the declared scratch directory `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch/`. No fixture/tool/contract edits, commits, pushes, network, or nested agents.

## 1. Readiness: artifacts and T3 report, not a plan

Actual bounded-poll command:

```sh
python3 -u /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch/poll.py
```

The persisted script checks all ten required fixture files, requires both T3-owned documents to differ from the r99 copies, and requires a nonempty `T3*.md` producer report. It sleeps 20 seconds between attempts, with a 40-attempt cap. Log: `V07-scratch/poll.log`.

Observed transitions (local timestamps, 2026-10-17, offset -03:00):

- Attempts 1–9, 23:32:36–23:35:16: all ten files existed, both documents were `same-as-r99`, producer reports absent. No r100 gates were run.
- Attempts 10–14, 23:35:36–23:36:56: both documents were `moved`, producer report still absent. No r100 gates were run.
- Attempt 15, 23:37:16: READY, `T3-fixture-docs.md` present. Poll exited 0 after 280 seconds.

Final exact log entry:

```text
{"attempt": 15, "docs": {"README.md": "moved", "claim-excerpt-map.md": "moved"}, "missing": [], "producer_reports": ["T3-fixture-docs.md"], "status": "READY", "time": "2026-10-17T23:37:16-03:00"}
```

T2's completed `T2-fixture-author.md` was also read before verification, as were T3's complete report and the actual fixture documents. T3's report records its own wait for T2's artifacts and report. T3 report at both verification runs: 19,055 bytes, sha256 `50f29495e995ba9ca3cb06cbd4bef9b80da44d7614e27aefb7d1e179509468d4`.

No ABSENT result, no stall escape, and no all-reports poll; the subtract-SELF convention is not needed for this producer-specific poll.

## 2. Delivered-r100 commands and full observed outputs

The two real gate calls were run concurrently by the persisted `verify.py` wrapper. It captures stdout, stderr, return codes, timestamps, and before/after sha256/size snapshots of all ten fixture files, both tools, the map contract, and the producer report.

Actual wrapper commands, both exit 0:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch/verify.py initial /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T3-fixture-docs.md
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch/verify.py rerun /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T3-fixture-docs.md
```

Initial run: 23:37:23. Rerun: 23:37:30. Both gate outputs below were byte-identical on the rerun, with exit 0 and empty stderr again.

### `support_check.py`

Complete initial stdout, followed by the wrapper's exit/stderr receipt:

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 22; EDITORIAL-ROWS 2; TOTAL-ROWS 24
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
exit=0
stderr_bytes=0
```

29 stdout lines; one terminal `RESULT PASS`, no warnings or failures. This is 22 JSON facts, not 24 JSON obligations: the other two rows are explicitly editorial comparisons.

### `map_obligations.py`

Complete initial stdout, followed by the wrapper's exit/stderr receipt:

```text
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
exit=0
stderr_bytes=0
```

Three stdout lines; one terminal `RESULT PASS`, no findings. The actual `raw=22 mapped=22` matches the requested count.

## 3. Byte identity and repeatability

Saved complete receipts: `V07-scratch/initial-verification.json` and `V07-scratch/rerun-verification.json`. Each contains all 14 before/after file identities, both commands, full stdout/stderr, exit codes, and timestamps. All four snapshots (before/after each run) were equal.

Selected delivered sha256 values:

```text
README.md             a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
claim-excerpt-map.md   16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
fictional-excerpts.md  d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
timeline.json         008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
sources.json          effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
support_check.py      55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
map_obligations.py    86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9
map contract          2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41
```

The two documentation hashes agree with T3's producer report. The three payload hashes agree with T2's producer report. Hash equality is identity evidence, not semantic validation.

Actual successful comparison command:

```sh
python3 - <<'PY'
from pathlib import Path
import json
scratch = Path('/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch')
first = json.loads((scratch / 'initial-verification.json').read_text())
second = json.loads((scratch / 'rerun-verification.json').read_text())
print('initial_time=' + first['runs'][0]['started'])
print('rerun_time=' + second['runs'][0]['started'])
stable = first['before'] == first['after'] == second['before'] == second['after']
print('all_four_snapshots_equal=' + str(stable))
assert stable
for run, replay in zip(first['runs'], second['runs']):
    print(run['command'])
    print('stdout_identical=' + str(run['stdout'] == replay['stdout']))
    print('stderr_identical=' + str(run['stderr'] == replay['stderr']))
    print('exit_pair=' + str((run['exit'], replay['exit'])))
    print('stdout_lines=' + str(len(run['stdout'].splitlines())))
    assert run['stdout'] == replay['stdout']
    assert run['stderr'] == replay['stderr'] == ''
    assert run['exit'] == replay['exit'] == 0
print('RESULT PASS: repeatable receipts on identical delivered bytes')
PY
```

Observed stdout, exit 0:

```text
initial_time=2026-10-17T23:37:23-03:00
rerun_time=2026-10-17T23:37:30-03:00
all_four_snapshots_equal=True
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
stdout_identical=True
stderr_identical=True
exit_pair=(0, 0)
stdout_lines=29
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
stdout_identical=True
stderr_identical=True
exit_pair=(0, 0)
stdout_lines=3
RESULT PASS: repeatable receipts on identical delivered bytes
```

## 4. Independent map inspection and raw recount

Actual map comparison command:

```sh
python3 -c 'from pathlib import Path; root=Path.cwd(); base=root/"corpus/fixtures/r99-window-lapse/claim-excerpt-map.md"; current=root/"corpus/fixtures/r100-docket-review/claim-excerpt-map.md"; rows=lambda path:[line for line in path.read_text().splitlines() if line.startswith("| J") and line[3:5].isdigit()]; inherited=rows(base); delivered=rows(current); expected=[line.replace("r99-window-lapse:","r100-docket-review:") for line in inherited]; print("MAP inherited_rows="+str(len(inherited))+" delivered_rows="+str(len(delivered))); print("INHERITED_MAP_ROWS_UNCHANGED_EXCEPT_NAMESPACE="+str(expected==delivered[:len(expected)])); print("NEW_ROW "+delivered[-1]); print("DECLARATION "+next(line for line in current.read_text().splitlines() if line.startswith("**Expected inventory:**")))'
```

Observed stdout, exit 0:

```text
MAP inherited_rows=21 delivered_rows=22
INHERITED_MAP_ROWS_UNCHANGED_EXCEPT_NAMESPACE=True
NEW_ROW | J22 | `timeline.json#/8` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-review-note` | `r100-docket-review:clerk-review-note` | `fictional-excerpts.md` | 78-88 | `verbatim` | `Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.` |
DECLARATION **Expected inventory:** 22 JSON facts; 2 editorial rows; 24 total mapped rows; 20 distinct excerpt anchors.
```

The actual map row is at `corpus/fixtures/r100-docket-review/claim-excerpt-map.md:43`; its complete review-only scope is at line 72. Its hit at `fictional-excerpts.md:82` lies inside 78–88, the isolated appended section. The remaining quoted lines 83–86 explicitly keep the entry open, record no new filings, make no finding, resolve nothing, and keep both accounts unresolved. These are observed authored words, not semantics certified by the two gates.

Actual independent raw recount command:

```sh
python3 -c 'from pathlib import Path; import json; root=Path.cwd(); fixture=root/"corpus/fixtures/r100-docket-review"; tables={name:json.loads((fixture/(name+".json")).read_text()) for name in ("entities","relations","timeline","sources","contradictions")}; claims=sum(len(entity.get("claims",[])) for entity in tables["entities"]); raw=len(tables["entities"])+claims+len(tables["relations"])+len(tables["timeline"]); print("INDEPENDENT entities={entities} claims={claims} relations={relations} timeline={timeline} sources={sources} contradictions={contradictions} raw_obligations={raw}".format(**{key:len(value) for key,value in tables.items()},claims=claims,raw=raw)); print("LAST_EVENT "+json.dumps(tables["timeline"][-1],sort_keys=True)); print("LAST_SOURCE_ID "+tables["sources"][-1]["id"])'
```

Observed stdout, exit 0:

```text
INDEPENDENT entities=6 claims=6 relations=1 timeline=9 sources=9 contradictions=0 raw_obligations=22
LAST_EVENT {"depends_on": ["clerk-lapse-recorded"], "description": "At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.", "entity_id": "clerk-maren", "id": "clerk-review-first-passage", "place_id": "chalk-stair", "source_id": "clerk-review-note", "tick": 16}
LAST_SOURCE_ID clerk-review-note
```

This recount used T2's delivered payload while waiting for T3, not a plan; the later gate snapshots confirm the same payload digests in both post-T3 runs. The formula is 6 first appearances + 6 claims + 1 relation + 9 events = 22.

For baseline contrast, these actual pre-readiness commands both exited 0:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
```

The first's observed final two stdout lines were:

```text
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
```

The second's complete stdout was:

```text
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
```

Thus the requested additional mapped JSON obligation is actually present and lexically supported, not merely counted in prose.

## 5. Failure/absence observations and bounds

- Initial direct `Read` of lane-root `AGENTS.md` returned `does not exist`; corpus-scoped `AGENTS.md` glob found none.
- Initial lane-root command `pwd && realpath .ufo/waves/round-100/seats && ls .ufo/waves/round-100/seats` exited 1: cwd was correct, then `realpath: .ufo/waves/round-100/seats: No such file or directory`; the `ls` was not executed. The directory later existed for the declared scratch and the producer deliveries; this was not a fixture verdict.
- The first one-line JSON-receipt comparison helper had an extra closing parenthesis and exited 1 before execution. It was not either gate, and made no writes. Exact attempted command:

```sh
python3 -c 'from pathlib import Path; import json; scratch=Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch"); first=json.loads((scratch/"initial-verification.json").read_text()); second=json.loads((scratch/"rerun-verification.json").read_text()); print("initial_time="+first["runs"][0]["started"]); print("rerun_time="+second["runs"][0]["started"]); print("all_four_snapshots_equal="+str(first["before"]==first["after"]==second["before"]==second["after"])); [(print(run["command"]+" stdout_identical="+str(run["stdout"]==replay["stdout"])+" stderr_identical="+str(run["stderr"]==replay["stderr"])+" exit_pair="+str((run["exit"],replay["exit"]))+" stdout_lines="+str(len(run["stdout"].splitlines()))))) for run,replay in zip(first["runs"],second["runs"])]; assert first["before"]==first["after"]==second["before"]==second["after"]; assert all(a["stdout"]==b["stdout"] and a["stderr"]==b["stderr"]=="" and a["exit"]==b["exit"]==0 for a,b in zip(first["runs"],second["runs"])); print("RESULT PASS: repeatable receipts on identical delivered bytes")'
```

Observed stderr ended with:

```text
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
```

The corrected, successful comparison and its exact output are recorded in section 3. Neither delivered gate ever failed in this seat's r100 runs.

The two receipts establish lexical anchor/mode/span/inventory validity and one-to-one raw pointer/source-ID mapping. They do not establish whole-claim entailment, dependency semantics, testimony truth, chronology/source authentication, rights, permission, or canon. This seat did not run `check_bible`, census, freeze-chain verification, synthesis-dossier checks, C3 replays, or all-axis adjudication; no such result is claimed. No unresolved support/map blocker remains.

## 6. Written-file manifest

Exclusive report: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-c2-support-map.md`.

All other writes are these 13 files under `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-scratch/`:

```text
poll.py
poll.log
verify.py
initial-verification.json
initial-support_check.stdout
initial-support_check.stderr
initial-map_obligations.stdout
initial-map_obligations.stderr
rerun-verification.json
rerun-support_check.stdout
rerun-support_check.stderr
rerun-map_obligations.stdout
rerun-map_obligations.stderr
```

Before this report's Write, a lane-root `python3` path assertion returned:

```text
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V07-c2-support-map.md
```

PASS — after T3's delivered artifacts and report appeared, r100 support_check returned 22/22 source support and 24/24 validated rows, and map_obligations returned raw=22 mapped=22; both RESULT PASS, exit 0, empty stderr, with byte-identical reruns on unchanged fixture/tool/report snapshots.

# V30 — operability (round 96)

Seat: V30 operability. Exclusive write scope: this report plus
`.ufo/waves/round-96/seats/V30-operability.scratch/`. No product file written, no commit, no
push, no network. All commands run from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` (3.14.7). Baseline: r95 closure
`dcb2d92`; `git log --oneline -1` at start → `60dba0c lore r95: close round — SCORECARD admitted
section`.

Task as seated: after the producers land, run **every documented command in Q5's fixture README,
Q6's knowledge note, and the two tools README addenda exactly as written**, check the **0/1/2
exit contract** on the paths the docs claim, and report failures as written. Never verify a plan;
report ABSENT for anything missing.

## 0. Poll-wait, landing order, frozen revision

Two background polls (20 s cadence): a presence poll over the 16 declared artifact paths + the six
Q-report globs, and a Q1/Q2-specific poll (contract `"id"` count ≥ 24 AND `Round-96` in the tools
README AND Q1/Q2 reports present). Landing order observed by mtime:

| Artifact | Landed |
|---|---|
| Q4 fixture JSON tables | 17:38–17:40 |
| Q5 `README.md`, `claim-excerpt-map.md` | 17:43 |
| Q3 `dependency_freeze.py` / contract | 17:44:37 / 17:44:27 |
| Q6 `r96-response-scope-note.md` | 17:47:02 |
| Q1 `map_obligations.py` (final write) | 17:47:24 |
| Q2 `map-obligations-contract.json` / `README.md` | 17:50:17 / 17:51:26 |
| Producer reports Q5 17:45, Q6 17:47, Q4 17:47, Q3 17:47, Q2 17:52:12, Q1 17:52:17 | |

The presence poll hit its 40-try limit at 17:51:38 with Q2's report still absent (`TIMEOUT_ABSENT`);
the Q1/Q2 poll then reported `READY` at 17:52:32 (`contract_ids=24 q1report=1 q2report=1
readme_r96=1`). No artifact was verified before it existed; every receipt below was taken after
17:52:32. Mid-flight states (tool at 17:44–17:47 with the r95 22-case contract) were not used as
evidence.

Frozen revision for every receipt below (sha256; re-verified **after** all runs, identical):

```
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

Transcripts: `V30-operability.scratch/transcript-blockABC.txt`, `run1.sh` (the replay harness; it
captures stdout+stderr and the true exit code — no pipelines in the harness, after a pre-flight
sweep showed `cmd | tail` masks the tool's exit with `tail`'s).

## 1. Q5 fixture README replay block (README.md:26–28) — run exactly as written

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations                  EXIT=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
… PASS J01–J16, PASS S01, PASS S02 …
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS                                                                  EXIT=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                                  EXIT=0
```

Every count the README states reproduces: README:21 "16 source-attributed JSON pointer
obligations" → `raw=16 mapped=16`; README:3 "5 entities / 1 relation / 5 events / 5 sources" →
`json.load` counts `5 1 5 5 0` (contradictions `[]`); tick-12 row =
`('response-evin-salt-court', 12, 'evin', 'salt-court', ['aftermath-missing-evin'], 'evin-response-note')`.

## 2. Q6 knowledge-note receipts block (note:46–51) — run exactly as written

Same three commands. Observed: `CLEAN … 0 violations` EXIT=0; `SOURCE-SUPPORT 16/16; MODES 18/18;
VALIDATED-ROWS 18/18` / `RESULT PASS` EXIT=0; `OBLIGATIONS raw=16 mapped=16` / `RESULT PASS`
EXIT=0 — each line matches the note's quoted receipt. The note was taken on the r95 tool revision
(`d1c239cc…`) and instructs re-running against the delivered revision; this is that re-run, on
`2b0ba815…`, and the receipts are unchanged. The note's own census claim also reproduces:
`ls -d corpus/fixtures/*/ | wc -l` → **170**. No documented command in the note fails as written.

## 3. Tools README Round-96 addendum (`map_obligations`) — commands and claims

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
… 24 × "SELF-TEST PASS <case> exit=<0|1|2> findings=[…]" (incl. schema_drift exit=1 ['schema_drift'],
   inventory_mismatch exit=1 ['inventory_mismatch']) …
RESULT PASS                                                                  EXIT=0
```

The 24 printed cases match the persisted contract set exactly (24 `"id"` entries; no missing/extra;
exits and finding sets match). Corpus paths, each exactly as the addendum's "Unchanged" paragraph
states:

```
r88-m3-maya-cluster      OBLIGATIONS raw=10 mapped=10 / INVENTORY 10/10; 2/2; 12/12 / RESULT PASS  EXIT=0
r93-m2-kojiki-cluster    OBLIGATIONS raw=12 mapped=12 / INVENTORY 12/12; 3/3; 15/15 / RESULT PASS  EXIT=0
r94-paired-crossing      OBLIGATIONS raw=14 mapped=14 / INVENTORY 14/14; 2/2; 16/16 / RESULT PASS  EXIT=0
r95-crossing-aftermath   OBLIGATIONS raw=15 mapped=15 / INVENTORY 15/15; 2/2; 17/17 / RESULT PASS  EXIT=0
r96-crossing-response    OBLIGATIONS raw=16 mapped=16 / INVENTORY 16/16; 2/2; 18/18 / RESULT PASS  EXIT=0
--frozen .ufo/waves/round-94/frozen/map-obligations-r93
                         SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 findings=none matched / RESULT PASS  EXIT=0
r87-myth-cluster         FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer / RESULT ERROR  EXIT=2
r89-inspiration-paraphrase  FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column / RESULT ERROR  EXIT=2
```

Both scratch-copy demonstrations were reproduced by applying the documented mutation to a scratch
copy (`V30-operability.scratch/demo-del`, `demo-dup`; never in-repo corpus):

```
$ python3 corpus/tools/map_obligations.py .ufo/…/V30-operability.scratch/demo-del
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 14/2/16; observed 13/2/15
RESULT FAIL                                                                  EXIT=1

$ python3 corpus/tools/map_obligations.py .ufo/…/V30-operability.scratch/demo-dup
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
FINDING dual_pointer: row P1 (line 23) names a second pointer token 'entities[0].claims[0]' alongside entities.json#/0/first_appearance
RESULT FAIL                                                                  EXIT=1
```

Output is **verbatim** the addendum's quoted before/after text, exit codes included. Two further
addendum claims probed on scratch copies: a canonical-header cell with an embedded second pointer
still exits 2 `unsupported_map` (`co-mapped or unsupported pointer grammar`, unchanged); a map with
the `**Expected inventory:**` line removed prints **no** INVENTORY line and exits 0.

## 4. The second tool: no README addendum exists (ABSENT)

`dependency_freeze.py` is documented **nowhere** in `corpus/tools/README.md` or any corpus Markdown:

```
$ grep -n "dependency_freeze\|dependency-freeze" corpus/tools/README.md
(no matches; README headings end at "### Round-96 addendum: gating inventory mismatch,
 `dual_pointer`, 24-case self-test" — a map_obligations-only section)
$ grep -rn "dependency_freeze" --include="*.md" corpus/
(no matches)
```

The only in-repo documentation of its CLI is its own `--help`, `corpus/tools/dependency-freeze-contract.json`,
Q3's seat report, and the LOG declaration. So of the seat's "two tools README addenda", one exists
(map_obligations, §3) and one is **ABSENT** — reported exactly, not fabricated. I ran the
dependency_freeze commands from `--help` + the contract's `exit_codes`/`self_test` blocks, which
are the delivered documentation surfaces:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279 / RESULT PASS  EXIT=0
r94-paired-crossing    FREEZE … 3/3; 2/2; 1/1   DIGEST 2527beb9…  RESULT PASS  EXIT=0
r95-crossing-aftermath FREEZE … 4/4; 3/3; 1/1   DIGEST d541ae64…  RESULT PASS  EXIT=0
r96-crossing-response  FREEZE … 5/5; 4/4; 1/1   DIGEST d422a9b3…  RESULT PASS  EXIT=0
```

Each printed digest equals the corresponding `content_sha256` pin in the contract. `--self-test`
prints `SELF-TEST 14/14` / `RESULT PASS`, EXIT=0, matching the contract's 14 persisted expectations
exactly. Exit-1 and exit-2 contract probes on scratch copies (`V30-operability.scratch/df/…`):

```
reduction (drop evin-ninth-bell from tick-10 depends_on)  FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']  EXIT=1
addition (append phantom-edge)                            FINDING ADDITION-DETECTED: event paired-crossing-decision gained depends_on ['phantom-edge']  EXIT=1
endpoint (tick-10 place_id → quiet-rise)                  FINDING ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'quiet-rise'  EXIT=1
digest-only prose edit (inventory unchanged)              FINDING DIGEST-MISMATCH: content digest eb068384… != pin 2527beb9…; fixture bytes changed outside the frozen inventory  EXIT=2
r87-myth-cluster (unpinned)                               FINDING UNPINNED-FIXTURE … RESULT ERROR  EXIT=2
missing timeline.json                                     FINDING FILE-MISSING … RESULT ERROR  EXIT=2
malformed timeline.json                                   FINDING MALFORMED-JSON … RESULT ERROR  EXIT=2
no arguments                                              FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test  EXIT=2
--help                                                    EXIT=0 with 0 RESULT lines
```

The documented BR-01 scenario (dependency reduction previously undetectable) now exits 1
`REDUCTION-DETECTED`, and the digest-only change is exit 2 as the contract's precedence sentence
states. `--freeze` was **not executed** — see §7; it writes the delivered contract.

## 5. Exit contract 0/1/2 and usage behavior on the claimed paths

| Path (as documented) | Documented | Observed exit | Terminal line |
|---|---|---|---|
| r96-crossing-response (Q5 README, Q6 note, both tools' docs) | 0 | 0 | `RESULT PASS` |
| r88 / r93 / r94 / r95 (addendum "Unchanged") | 0 | 0 | `RESULT PASS` |
| `--frozen` r93 snapshot | 0 | 0 | `RESULT PASS` |
| r87-myth-cluster / r89-inspiration-paraphrase | 2 | 2 | `RESULT ERROR` |
| deletion-class demo | 1 | 1 | `RESULT FAIL` (`inventory_mismatch`) |
| dual_pointer demo | 1 | 1 | `RESULT FAIL` (`dual_pointer`) |
| `map_obligations --self-test` | 0 | 0 | `RESULT PASS` (24/24) |
| dependency_freeze chain ×4 / `--self-test` | 0 | 0 | `RESULT PASS` / `SELF-TEST 14/14` |
| dependency_freeze reduction/addition/endpoint | 1 | 1 | `RESULT FAIL` |
| dependency_freeze digest/unpinned/missing/malformed/usage | 2 | 2 | `RESULT ERROR` |

`map_obligations` usage probes (all EXIT=2, one terminal RESULT line, zero stderr on the operational
paths): no args → `invalid_arguments: cluster directory is required`; `--self-test` + cluster →
`invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen`; nonexistent
cluster → `cluster_missing`; `--bogus` → `invalid_arguments: unrecognized arguments: --bogus`.
`--help` on both tools: EXIT=0 with **zero** RESULT lines (consistent with README:99 — exit 0 alone
is not a PASS). Retained documented commands still run: `support_check` r87 `14/14 … MODES 22/22`
PASS exit 0, r88 `10/10 … 12/12` PASS exit 0; `discriminate_check.py` → `RESULT: DISCRIMINATION
HELD` exit 0 and `--checker e97613c` → `REGRESSION-DETECTED` exit 2; `boundary_doc_check.py` →
`CERTIFIED …` exit 0 and `--self-test` → `SELF-TEST PASS` exit 0.

## 6. Environment finding — `/tmp` inode exhaustion makes one documented command wrong-reason-pass

This host's `/tmp` is a 16 G tmpfs with **all 1 048 576 inodes used** (`df -i /tmp` → `1048576
1048576 0 100%`), so `mktemp` fails: `mktemp: failed to create file via template
'/tmp/tmp.XXXXXXXXXX': No space left on device` (exit 1). Python's `tempfile` silently falls back
to `/var/tmp`, which is why every in-repo tool still works.

Consequence for the tools README's r93 addendum negative control, run **exactly as written**:

```
$ tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT; cp corpus/knowledge/holder-assessment-boundary.md "$tmp"; printf '\nDeliberate R05 pin-drift probe.\n' >> "$tmp"; python3 corpus/tools/boundary_doc_check.py --doc "$tmp"; rc=$?; printf 'observed_exit=%s\n' "$rc"; test "$rc" -eq 1
mktemp: failed to create file via template '/tmp/tmp.XXXXXXXXXX': No space left on device
cp: cannot create regular file '': No such file or directory
CHECK pinned inputs: FAIL
FINDING document_unreadable: cannot read document /home/vgpnk/Projects/shokunin/lore-shokunin: [Errno 21] Is a directory: '…'
observed_exit=1
```

The script's own assertion (`test "$rc" -eq 1`) still passes, but the documented `FINDING
document_drift` does **not** appear — the exit 1 comes from `document_unreadable` on the repo
directory. This is a wrong-reason pass induced by the environment, not a defect in the delivered
checker: with a scratch path substituted for `mktemp` (`--doc
V30-operability.scratch/drift-probe.md`) the tool prints the documented `FINDING document_drift:
document digest differs from pinned 65838f86… bytes` and exits 1. Reported as written: the command
as documented does not produce the documented finding on this host.

## 7. Tool hazard — `--freeze` rewrites the delivered contract; a foreign pin is in the delivered contract

The delivered `dependency-freeze-contract.json` (frozen hash `7d568cc4…`) carries a **fifth pin
`c3red`** whose `"fixture"` is `.ufo/waves/round-96/seats/V41-scratch/c3red` — a verifier scratch
path, not a corpus fixture:

```
$ python3 -c "import json; print(list(json.load(open('corpus/tools/dependency-freeze-contract.json'))['pins']))"
['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'c3red']
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r87-myth-cluster
FINDING UNPINNED-FIXTURE: no pin for 'r87-myth-cluster' … (pinned: ['c3red', 'r88-m3-maya-cluster', …])
```

Root cause is visible in the source: `--freeze` writes the delivered artifact —
`corpus/tools/dependency_freeze.py:26` `CONTRACT_PATH = ROOT / "corpus/tools/dependency-freeze-contract.json"`,
line 312 `CONTRACT_PATH.write_text(…)` — with no scope guard, so a verifier's `--freeze` probe on
its own scratch copy silently mutated a producer-owned delivered file. Q3's report §7 discloses the
anomaly and leaves the pin in place (two verifier receipts cite the pinned list); the scratch dir
still exists (`.ufo/.../V41-scratch/c3red`, files dated 17:44). Assessment: verification semantics
are unaffected today (pins are basename-keyed and no corpus fixture is named `c3red`, so the chain
runs 4/4 clean and `--self-test` 14/14), but the delivered artifact now references a scratch path
that is not part of the corpus and may be removed, and any future `--freeze` run again rewrites the
delivered contract. I did **not** run `--freeze` (it writes the delivered contract, outside my
write scope); the write-target claim rests on the source line above plus V41's recorded
`FROZEN c3red … RESULT PASS` receipt cited in Q3 §7. Recommendation for closure: delete `pins.c3red`
or add a `--freeze` scope guard refusing paths outside `corpus/fixtures/`, and document the tool in
`corpus/tools/README.md` (the missing second addendum, §4).

## 8. Preservation and residue

- `git status --porcelain` before and after the whole replay is identical — ` M LOG.md`,
  ` M corpus/tools/{README.md,map-obligations-contract.json,map_obligations.py}`,
  `?? .ufo/waves/round-96/`, `?? corpus/fixtures/r96-crossing-response/`,
  `?? corpus/knowledge/r96-response-scope-note.md`,
  `?? corpus/tools/{dependency-freeze-contract.json,dependency_freeze.py}` — no corpus modification
  from this seat's runs.
- All frozen hashes re-verified identical after the runs (§0). No leftover self-test scratch:
  `ls -d map-obligations-self-test-* dependency-freeze-self-test-*` → none (the map tool's scratch
  is still created under the repo root, `map_obligations.py:809` — BR-05 remains open as documented;
  the freeze tool's self-test uses the system temp dir, `dependency_freeze.py:411`).
- Census 170 (`ls -d corpus/fixtures/*/ | wc -l`), matching Q6's note; documented counts 5/1/5/5/0
  verified by `json.load`.

## Findings summary (all failures/contradictions reported exactly)

1. **Second tools README addendum ABSENT** — `dependency_freeze.py` is undocumented in
   `corpus/tools/README.md` (and in any corpus Markdown); its CLI is discoverable only via
   `--help`/contract/seat report. The tool itself passes every documented-elsewhere command and
   exit-contract probe.
2. **`--freeze` writes the delivered contract** (`dependency_freeze.py:312`) and a verifier probe
   left a foreign pin `c3red` pointing at `.ufo/.../V41-scratch/c3red` inside the delivered
   `dependency-freeze-contract.json` (Q3 §7 discloses; I did not re-run `--freeze`).
3. **Environment: `/tmp` inode exhaustion** — the README's `mktemp` negative control fails as
   written and exits 1 for the wrong reason (`document_unreadable`, not `document_drift`); the
   underlying behavior is correct when a temp path is available.
4. No other documented command failed as written: Q5 README (3 commands), Q6 note (3 commands),
   the tools README Round-96 addendum (self-test 24/24, five clean corpus paths, frozen replay,
   r87/r89 fail-closed, both scratch-copy demos verbatim), and the retained r93/r94/r95 addendum
   commands all reproduce their documented output and exit codes on the frozen revision.

## Bottom line

PASS — every command documented in Q5's r96 README, Q6's r96 note, and the tools README Round-96
map_obligations addendum runs as written on the frozen revision (r96 16/16 CLEAN/PASS, 24/24
self-test, r88–r95 exit 0, r87/r89 exit 2, deletion-class `inventory_mismatch` and `dual_pointer`
demos verbatim exit 1, dependency_freeze 4/4 clean + 14/14 self-test + documented 0/1/2 probes),
with three reported operability gaps: the second tool's README addendum is absent, `--freeze`
rewrites the delivered contract and left a foreign `c3red` scratch pin in it, and the environment's
full `/tmp` makes one documented `mktemp` command wrong-reason-pass.

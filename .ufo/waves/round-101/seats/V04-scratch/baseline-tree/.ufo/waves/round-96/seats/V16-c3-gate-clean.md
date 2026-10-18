# V16 — c3-gate-clean: dependency_freeze on the chain, pins vs independent recompute

Round 96, seat V16. Baseline r95 closure `dcb2d92`; HEAD at verification
`60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 closure commit, matches the
contract's `revision` pin). Repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`.
All commands run from the lane repo root with `python3`. Scratch (absolute):
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/scratch/V16/`.

Seat scope: run `corpus/tools/dependency_freeze.py` on all four chain fixtures
(expect 4/4 exit 0 clean), and independently recompute each fixture's
dependency edges from raw JSON and compare against the contract pins
one-to-one (edges + content digests).

## Artifacts under test (hashes at verification time, 2026-10-17 17:47 -03)

```
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py   (20552 bytes)
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json  (12032 bytes)
```

The chain directory names are **not** the ones the round claim abbreviates:
`r88-m3-maya-cluster` (not `r88-m3`), `r94-paired-crossing`,
`r95-crossing-aftermath`, `r96-crossing-response`.

The contract carries **five** pins: the four chain fixtures plus a foreign
`c3red` pin pointing at `.ufo/waves/round-96/seats/V41-scratch/c3red`
(see "Foreign pin" below). At 17:44, before that pin was written, the contract
listed only the four chain pins; the chain pins themselves were byte-stable
across my runs (hash `7d568cc4…` at 17:45 and 17:47).

## Check 1 — 4/4 clean on the chain: PASS

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS
exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
exit=0
```

4/4 exit 0, no FINDING lines, receipts read `events n/n` and
`dependency-edges n/n` (observed/frozen) for every fixture. Re-run at 17:47
after the tool's final revision: identical output and identical DIGEST values.

## Check 2 — pins vs independent recompute: PASS (84 checks, 0 failures)

Method: `.ufo/waves/round-96/scratch/V16/compare_full.py` — stdlib only, it does
**not** import `dependency_freeze.py`. It re-reads the raw bytes of the five
`data_files` (`entities.json`, `relations.json`, `timeline.json`,
`sources.json`, `contradictions.json`), recomputes per-file sha256, the
composite `content_sha256` (sha256 over `json.dumps({name: sha256(raw)},
sort_keys=True, separators=(",",":"))`, the scheme declared at
`corpus/tools/dependency_freeze.py:77-80`), the event inventory
(`event id -> sorted(set(depends_on))`), the event endpoints
(`tick, entity_id, place_id`), the relation triples (`from, to, type`, sorted)
and the counts, then diffs every field one-to-one against `pins[name]`.

```
$ python3 .ufo/waves/round-96/scratch/V16/compare_full.py
checks run: 84; failures: 0
VERDICT: ALL PINS MATCH INDEPENDENT RECOMPUTE
```

Per-fixture observed values (all matching the pins exactly):

| fixture | events | edges | relations | entities | sources | content_sha256 |
|---|---|---|---|---|---|---|
| r88-m3-maya-cluster | 2 | 0 | 0 | 4 | 2 | 15ef230e…3fc279 |
| r94-paired-crossing | 3 | 2 | 1 | 5 | 3 | 2527beb9…cebe75 |
| r95-crossing-aftermath | 4 | 3 | 1 | 5 | 4 | d541ae64…6d2ec9 |
| r96-crossing-response | 5 | 4 | 1 | 5 | 5 | d422a9b3…57d7f6 |

Edge inventories recomputed independently from raw JSON (identical to the pins
one-to-one, including endpoints):

- `r88-m3-maya-cluster`: `aru-ninth-bell []`, `evin-ninth-bell []`
- `r94-paired-crossing`: + `paired-crossing-decision [aru-ninth-bell, evin-ninth-bell]`
- `r95-crossing-aftermath`: + `aftermath-missing-evin [paired-crossing-decision]`
- `r96-crossing-response`: + `response-evin-salt-court [aftermath-missing-evin]`

Relation triples are `[aru, evin, agreed_co_stewardship_for_this_crossing]` for
r94/r95/r96 and `[]` for r88 — matched by set on all four.

## Check 3 — non-vacuity control: the clean 4/4 is meaningful

A gate that always exits 0 would also produce Check 1. On a scratch copy at a
different path but the same directory basename
(`.ufo/waves/round-96/scratch/V16/negctl2/r95-crossing-aftermath`), dropping
`evin-ninth-bell` from `paired-crossing-decision.depends_on`:

```
$ python3 corpus/tools/dependency_freeze.py .../negctl2/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit=1
```

Exit 1 with a stable FINDING id, and the receipt shows the shortfall
`2/3`. The BR-01 class is actually caught by this gate.

## Check 4 — operability bounds

- cwd-independent: run from `/` with absolute tool and fixture paths → exit 0,
  same DIGEST. `ROOT` resolves from `__file__` (`dependency_freeze.py:25`).
- Pins are keyed by **directory basename**, not by path
  (`pin_for` → `fixture.resolve().name`, `dependency_freeze.py:251-257`). A copy
  of a pinned fixture anywhere on disk verifies against that pin — correct for
  Check 3's control, but it means the gate cannot distinguish "the delivered
  fixture" from "any same-named copy". Bound, not a defect.

## Check 5 — FINDING: `--self-test` was broken on an intermediate revision (since fixed)

Timeline matters here, so it is stated explicitly.

**At 17:44 (tool sha256 `d17297bb2d49c5bb35783824bf0704513cc1f1a692f11878379bb1edad56282f`,
20552 bytes at that moment):**

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE addition_edge_phantom: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE event_removed: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE event_endpoint_change: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE relation_endpoint_flip: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE relation_removed: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE relation_added: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
CASE digest_tamper: exit=2 expected=2 findings=['FILE-MISSING'] MISMATCH
CASE malformed_json: exit=2 expected=2 findings=['FILE-MISSING'] MISMATCH
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
SELF-TEST 5/14
FINDING SELF-TEST-MISMATCH: cases failed: ['addition_edge_phantom', 'digest_tamper', 'event_endpoint_change', 'event_removed', 'malformed_json', 'reduction_edge_drop', 'relation_added', 'relation_endpoint_flip', 'relation_removed']
RESULT FAIL
exit=1
```

Reproducible: 3/3 consecutive runs produced exactly the same 9-case failure set.
**Not environmental** — re-run with `TMPDIR` pointed at a filesystem with free
inodes (`.ufo/waves/round-96/scratch/V16/tmpdir`) produced byte-identical
failures with only the temp path prefix changed.

Root cause, proven by tracing the argv the tool actually passes
(`.ufo/waves/round-96/scratch/V16/trace_selftest.py`, which imports the tool and
wraps `subprocess.run`):

```
reduction_edge_drop      expected_exit=1 argv=['/var/tmp/v16-trace-…/missing_timeline/r95-crossing-aftermath']
addition_edge_phantom    expected_exit=1 argv=['/var/tmp/v16-trace-…/missing_timeline/r95-crossing-aftermath']
… (all 9 failing cases)  argv=['/var/tmp/v16-trace-…/missing_timeline/r95-crossing-aftermath']
clean                    expected_exit=0 argv=['…/corpus/fixtures/r95-crossing-aftermath']
unpinned_fixture         expected_exit=2 argv=['/var/tmp/v16-trace-…/unpinned_fixture']
```

All nine failing cases were handed the **`missing_timeline`** directory, whose
`timeline.json` had been deleted — hence `FILE-MISSING`/exit 2 instead of the
declared findings. Cause: in `self_test_cases` each case lambda closes over the
single reused local `scratch` (`dependency_freeze.py:330-388`), and the last
assignment (`scratch = copy_case("missing_timeline")`, line 386) wins for every
lambda. The four cases that passed are exactly those not built from that
variable (`clean` uses `base`, `unpinned_fixture` uses `unpinned`,
`missing_fixture` and `invalid_arguments` use inline expressions). Classic
late-binding closure defect; deterministic and independent of the environment.

**At 17:45 (tool sha256 `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980`,
20552 bytes — Q3 revised the file in place):**

```
$ python3 corpus/tools/dependency_freeze.py --self-test
…
SELF-TEST 14/14
RESULT PASS
exit=0
```

The contract declares all 14 cases with persisted expectations
(`self_test.expected`: exit codes 0/1/2 and finding ids per case; contract
sha256 `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975`),
and the current revision satisfies them all. Check 1's 4/4 clean and Check 2's
84/84 were re-run against `a3b57978…` and are unchanged.

**Verification revision is final and confirmed.** Q3's producer report
`.ufo/waves/round-96/seats/Q3-dependency-freeze.md` appeared at 17:46 and the
tool hash held at `a3b57978f0cbf314…` for 8 consecutive 20s polls (~2.7 min)
across the write; the contract hash held at `7d568cc422cda422…`. Q3's report
states the same verified revision, so producer and verifier are pinned to the
same bytes. Final confirmation run at 17:48 on that revision:

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f >/dev/null; echo $?; done
0
0
0
0
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 14/14
RESULT PASS
$ python3 .ufo/waves/round-96/scratch/V16/compare_full.py | tail -2
checks run: 84; failures: 0
VERDICT: ALL PINS MATCH INDEPENDENT RECOMPUTE
```

If the delivered revision differs from `a3b57978…` / `7d568cc4…`, Checks 1, 2
and 5 must be re-run; a digest change in any chain fixture would also require
re-freezing, since `content_sha256` is pinned per fixture.

## Foreign pin `c3red` in the delivered contract (corroborates Q3's own anomaly note)

Q3's report closes with "one anomaly reported: the contract carries a foreign
scratch pin `c3red` written by V41's `--freeze` probe". Independently confirmed:

```
$ python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print(sorted(c['pins']))"
['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V41-scratch/c3red
FREEZE c3red: events 3/3; dependency-edges 1/1; relations 1/1
DIGEST eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28
RESULT PASS
exit=0
```

The `c3red` pin records a **reduced mutant** inventory (3 events, 1 dependency
edge, vs 2 edges for the same event set in r94) living in a seat scratch
directory that will not survive round closure. It does not affect the chain
verification — pins are looked up by directory basename, so a stray pin is
inert unless someone runs the tool on that exact scratch path — but it is a
frozen mutant snapshot embedded in a delivered file, and its target becomes a
dangling path at closure. Recommend removing `pins.c3red` before the round is
sealed (Q3 makes the same recommendation). Not my seat's verdict; reported as
witnessed.

## Adjacent observations (not my seat's verdicts)

- Preservation r95 → r96, independently confirmed: `entities.json`,
  `relations.json`, `contradictions.json`, `inspiration-note.md`,
  `source-excerpt.md` are byte-identical (`cmp -s`); all four inherited timeline
  records compare equal as parsed JSON; the only new event is
  `response-evin-salt-court`; sources 4 → 5 with the four inherited entries
  unchanged. `check_bible.py` exits 0 CLEAN on all four chain fixtures.
- Environment hazard (witnessed, affects every seat): `/tmp` is a tmpfs with
  **0 free inodes** (`df -i /tmp`: 1048576 used / 1048576, 100%) while holding
  8.5G of free space. Creating any new file under `/tmp` fails with
  `No space left on device`. My first `check_bible` run died this way. All my
  scratch output is therefore under the lane repo. The tool's own self-test is
  unaffected because `tempfile.gettempdir()` resolves to `/var/tmp` here
  (root filesystem).
- Q3's producer report (`seats/Q3-dependency-freeze.md`, bottom line PASS)
  appeared at 17:46, after my first verification pass; the verified revision was
  unchanged across the write (tool `a3b57978…`, contract `7d568cc4…`), so no
  re-verification beyond the 17:48 confirmation run was needed. The producer's
  scratch dir shows `addition/ endpoint/ reduction/ tamper/ run1.txt run2.txt`.

## Bottom line

**PASS on seat scope** — `dependency_freeze.py` exits 0 clean on 4/4 chain
fixtures and all 84 independently recomputed pin fields (edges, endpoints,
relations, per-file and composite digests, counts) match one-to-one, with the
BR-01 reduction class demonstrably caught (exit 1) — verified at the final
revision, tool hash `a3b57978…` / contract hash `7d568cc4…` / HEAD `60dba0c`;
two witnessed riders: the `--self-test` sub-claim FAILED 5/14 on the
intermediate revision `d17297bb…` (late-binding closure over `scratch`,
`dependency_freeze.py:330-388`, fixed by Q3 before its report) and the delivered
contract still carries a foreign scratch pin `pins.c3red` that should be removed
before the round is sealed.

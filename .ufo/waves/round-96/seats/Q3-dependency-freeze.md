# Q3 — dependency-freeze (round 96)

- Seat: Q3, producer. Claim under test: **C3 / coverage** — close carried debt BR-01
  (dependency reduction is undetectable) with a new stdlib-only gate
  `corpus/tools/dependency_freeze.py` + persisted `corpus/tools/dependency-freeze-contract.json`.
- Exclusive byte ownership respected: only `corpus/tools/dependency_freeze.py`,
  `corpus/tools/dependency-freeze-contract.json`, this report, and
  `.ufo/waves/round-96/seats/Q3-scratch/` were written. No commits, no network, no nested agents.
- Verified revision (hashed at report time, after all measurements below):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
```

  Working-tree HEAD at freeze time: `60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 closure
  `dcb2d92` plus the r95 SCORECARD closure commit; `LOG.md` and later round files uncommitted).
- Poll-wait: Q4's `corpus/fixtures/r96-crossing-response/` JSON tables were present at first
  inspection (17:38–17:40) and `.ufo/waves/round-96/seats/Q4-fixture-json.md` (bottom line PASS)
  was present on the next poll cycle; no sleep cycles were needed. r96 was frozen only after that
  report existed. `--self-test` requires the base fixture `r95-crossing-aftermath`, pinned before
  the self-test ran.

## 1. Delivered gate

`corpus/tools/dependency_freeze.py` (stdlib only: argparse, hashlib, json, re, shutil,
subprocess, sys, tempfile, collections, pathlib). Pins are keyed by fixture **basename**.
Per fixture the pin freezes:

- `events`: event id → sorted `depends_on` set, plus event endpoint `{tick, entity_id, place_id}`;
- `relations`: sorted `(from, to, type)` endpoint triples;
- `content_sha256`: SHA-256 over the canonical JSON of per-file SHA-256s of the present
  data files (`entities.json`, `relations.json`, `timeline.json`, `sources.json`,
  `contradictions.json`), with the per-file digests also stored;
- `counts`, `fixture` (repo-relative label at freeze time), `revision`.

CLI: `python3 corpus/tools/dependency_freeze.py <fixture-dir>` verifies against the pin;
`--freeze <fixture-dir>` (re)builds a pin; `--self-test` runs the isolated cases.

Verdicts and stable FINDING IDs:

| exit | result | finding IDs |
|---|---|---|
| 0 | PASS | — |
| 1 | FAIL | `REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE` |
| 2 | ERROR | `INVALID-ARGUMENTS`, `FIXTURE-MISSING`, `UNPINNED-FIXTURE`, `FILE-MISSING`, `MALFORMED-JSON`, `MALFORMED-MODEL`, `DIGEST-MISMATCH`, `CONTRACT-INVALID`, `SELF-TEST-MISMATCH` |

**Precedence (documented in the contract):** semantic inventory findings decide first (exit 1);
a content digest change the frozen inventory does not model exits 2. Without this order the four
declared demos would be mutually inconsistent (any JSON mutation would exit 2 before the semantic
class could be reported). The digest covers JSON tables only, so Q5's later `README.md` /
`claim-excerpt-map.md` additions do not disturb a pin — confirmed: r96 verifies clean with both
docs present.

`--freeze` was used only at delivery time (three chain pins, then the r96 pin). The admitted path
is verify-only.

## 2. Delivered chain frozen — 4/4 clean

```
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; echo "rc=$?"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS  rc=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS  rc=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS  rc=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS  rc=0
```

Two consecutive runs of the same command produced byte-identical output (`cmp` → identical).
Re-verified 4/4 clean **after** Q5's README/map landed.

## 3. BR-01 closure — the same mutation, old gates green, new gate red

Scratch copy `.ufo/waves/round-96/seats/Q3-scratch/reduction/r94-paired-crossing` with
`evin-ninth-bell` dropped from the tick-10 `depends_on` (the exact BR-01 class):

```
$ python3 corpus/fixtures/check_bible.py .ufo/.../reduction/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations          rc=0
$ python3 corpus/tools/map_obligations.py .ufo/.../reduction/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS                                                          rc=0
$ python3 corpus/tools/dependency_freeze.py .ufo/.../reduction/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL                                                          rc=1
```

The debt is closed by the delivered gate: the mutation that previously left every gate green now
fails with a stable finding ID and exit 1.

## 4. Declared mutation demos (scratch copies; real corpus untouched)

| demo (scratch copy of r94-paired-crossing) | observed |
|---|---|
| drop `evin-ninth-bell` from tick-10 `depends_on` | exit 1 `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` |
| add phantom `depends_on` entry | exit 1 `FINDING ADDITION-DETECTED: event paired-crossing-decision gained depends_on ['phantom-ninth-bell']` |
| flip one relation endpoint (`from`/`to` swapped) | exit 1 `FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [evin, aru, agreed_co_stewardship_for_this_crossing]` |
| one semantic-neutral JSON byte changed (`north lantern` → `north Lantern`) | exit 2 `FINDING DIGEST-MISMATCH: content digest 1d7af1f6… != pin 2527beb9…; fixture bytes changed outside the frozen inventory` |

Receipt lines for the three exit-1 demos show the edge counters moving (`1/2`, `3/2`) with the
pinned totals held. All four exits are exactly as declared; no traceback on any path.

## 5. Self-test — 14/14 PASS

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 … ['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 … ['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 … ['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 … ['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 … ['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 … ['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 … ['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 … ['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 … ['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 … ['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 … ['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 … ['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 … ['INVALID-ARGUMENTS'] ok
SELF-TEST 14/14
RESULT PASS                                                          rc=0
```

Expectations are persisted in `dependency-freeze-contract.json` under `self_test.expected`
(14 cases, each with `exit`, `finding_ids`, `forbid_traceback`); the runner fails closed with
exit 2 `CONTRACT-INVALID` if the persisted case set and the implemented set disagree. Cases run
as isolated subprocesses against copies under a `tempfile.TemporaryDirectory`; scratch copies
keep the pinned basename so the pin resolves.

**Defects the self-test caught in its own first runs (reported as found):** (1) all case lambdas
captured one loop variable, so every mutated copy was verified as the last one built — fixed by
binding paths as lambda defaults; (2) the mutual-exclusion `ToolError` was raised outside `main`'s
handler, producing a raw traceback and exit 1 instead of exit 2 `INVALID-ARGUMENTS` — fixed by
moving argument validation inside the handler. Both were real, both were fixed before the final
14/14 run; verify semantics were unchanged by the fixes.

## 6. Independent corroboration of the C2 inheritance at the dependency layer

From the persisted pins (no re-derivation from prose):

- r88 → r94 and r94 → r95: every inherited event's `depends_on` set and endpoint is identical.
- r95 → r96: the four inherited events are identical; exactly one new event
  (`response-evin-salt-court`, tick 12, `depends_on: ["aftermath-missing-evin"]`); the relation
  triple is identical (`aru → evin, agreed_co_stewardship_for_this_crossing`).
- r96 counts: 5 events, 4 dependency edges, 1 relation, 5 entities, 5 sources — matching Q4's
  report (5/1/5 events, 5 sources, 16 raw obligations).

## 7. Anomaly — a foreign pin in the delivered contract (reported, not hidden)

The contract contains a fifth pin `c3red` that this seat did not create:

```
pins: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
c3red | fixture ".ufo/waves/round-96/seats/V41-scratch/c3red" | digest eff4b354c092 | counts {events 3, edges 1, relations 1}
```

Evidence trail: `V41-scratch/c3-freeze.out` shows `FROZEN c3red … RESULT PASS` (V41 exercising the
`--freeze` path on its own scratch copy); `V41-scratch/c3-interim.log:34` shows the preceding
`UNPINNED-FIXTURE` receipt; `V33-scratch/v33-battery-current.txt:113,119` and
`V22-c3-tamper.scratch/snapshots/rev-1743/…json` already quote the pinned list **including**
`c3red`. Because two verifier receipts cite that list, this seat deliberately did **not** remove
the pin mid-round (removing it would invalidate recorded observations). Assessment: harmless to
verification semantics (pins are basename-keyed; no corpus fixture is named `c3red`), but it is a
real tool hazard — `--freeze` on any out-of-corpus scratch copy rewrites the delivered contract,
and this seat's later r96 freeze read-and-preserved it. Recommendation for closure/r97: either
delete `pins.c3red` at closure, or add a `--freeze` scope guard that refuses paths outside
`corpus/fixtures/`. The guard was **not** implemented now on purpose: the tool hash is already
frozen for the verifier battery, and a behavior change mid-round would invalidate in-flight probes.

## 8. Write audit

```
$ git status --porcelain
 M LOG.md                          # pre-seat round declaration
 M corpus/tools/map_obligations.py # Q1
?? .ufo/waves/round-96/            # seat reports/scratch
?? corpus/fixtures/r96-crossing-response/        # Q4/Q5
?? corpus/knowledge/r96-response-scope-note.md   # Q6
?? corpus/tools/dependency-freeze-contract.json  # Q3
?? corpus/tools/dependency_freeze.py             # Q3
$ git diff --stat HEAD -- corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r94-paired-crossing \
    corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response
(empty)
```

No other paths written; no commits. Mutations were applied only to copies under
`.ufo/waves/round-96/seats/Q3-scratch/`.

## Bottom line

PASS — `dependency_freeze.py` + `dependency-freeze-contract.json` delivered stdlib-only; the
r88/r94/r95/r96 chain is frozen and verifies 4/4 clean (exit 0), the BR-01 mutation that leaves
`check_bible` and `map_obligations` green now exits 1 `REDUCTION-DETECTED`, the declared
addition/endpoint/digest demos reproduce their exact exits and stable finding IDs, and the
persisted self-test is 14/14 PASS; one anomaly reported: the contract carries a foreign
scratch pin `c3red` written by V41's `--freeze` probe (left in place because V22/V33 receipts
quote it).

# V48 — c3-negative-2 (round 96)

- Seat: V48, verifier. Brief: independent BR-01 / addition / endpoint / tamper demos with fresh
  scratch; compare classes/IDs with V17/V18/V22. Claim under test: **C3 / coverage**
  (`corpus/tools/dependency_freeze.py` + `corpus/tools/dependency-freeze-contract.json`, producer Q3).
- Verified revision (hashed at 17:46:54, unchanged through write time):
  - `dependency_freeze.py` sha256 `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` (20552 b, mtime 17:44:37)
  - `dependency-freeze-contract.json` sha256 `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975` (12032 b, mtime 17:44:27)
- Artifacts byte-stable from 17:44:37 (poll: 120 s quiet) before the final battery; producer report
  `.ufo/waves/round-96/seats/Q3-dependency-freeze.md` present before this report was finalized.
- Scratch (fresh, exclusive): `.ufo/waves/round-96/seats/V48-scratch/` — `independent_inventory.py`,
  `check_pins.py`, `apply_mutations2.py`, `mutations/<case>/<pinned-basename>/`. No corpus writes by
  this seat; all mutations on copies whose basename preserves the pin key (`r94-paired-crossing`,
  `r95-crossing-aftermath`, `r96-crossing-response`), otherwise `pin_for()` returns
  `UNPINNED-FIXTURE` before comparison (confirmed by the tool's own error path and by V41's probe).

## 1. Independent pin cross-check — 0 mismatches

`python3 .ufo/waves/round-96/seats/V48-scratch/check_pins.py` recomputed every per-file sha256,
the content digest (per-file sha256 → canonical JSON → sha256), and the counts from the raw fixture
bytes, for **all five** pins in the delivered contract (the four chain fixtures plus `c3red`):

```
TOTAL mismatches: 0
```

Per fixture, observed counts equal pinned counts: r88 2/0/0 (events/edges/relations), r94 3/2/1,
r95 4/3/1, r96 5/4/1, and r96's `files` digests match my recomputation
(`timeline.json ea0225f9270db796…`, `sources.json 9f973f634cf325a3…`). The frozen edge inventory
also matches my independent parse of the raw timelines (e.g. r94 tick-10
`["aru-ninth-bell","evin-ninth-bell"]`, r96 tick-12 `response-evin-salt-court →
["aftermath-missing-evin"]`).

## 2. Delivered chain — 4/4 clean, exit 0

```
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; echo "exit=$?"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS
exit=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
exit=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
exit=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
exit=0
```

r96 was re-verified after Q5's `README.md` / `claim-excerpt-map.md` landed → still PASS exit 0
(digest covers JSON tables only, as documented). This reproduces Q3 §2 independently.

## 3. BR-01 reduction — the carried debt class, closed

Fresh copy `mutations/reduction-r94/r94-paired-crossing` with `evin-ninth-bell` dropped from the
tick-10 `depends_on` (the exact BR-01 mutation):

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit=1
```

Same mutation on `mutations/reduction-r95/r95-crossing-aftermath` → exit 1 `REDUCTION-DETECTED`
(`dependency-edges 2/3`). The class that previously left every gate green now fails with a stable
FINDING ID on both the r94 and the inherited r95 chain link.

## 4. Negative / tamper matrix (fresh scratch; all runs from lane root)

| mutation (fresh copy) | observed |
|---|---|
| r94 tick-10 edge drop | exit 1 `REDUCTION-DETECTED` |
| r95 tick-10 edge drop | exit 1 `REDUCTION-DETECTED` |
| r94 add `aru-ninth-bell → evin-ninth-bell` | exit 1 `ADDITION-DETECTED: event aru-ninth-bell gained depends_on ['evin-ninth-bell']` |
| r95 add `phantom-ninth-bell` to tick-11 | exit 1 `ADDITION-DETECTED` |
| r95 append unpinned event `phantom-event` with `depends_on ["aru-ninth-bell"]` | exit 1 `ADDITION-DETECTED: unpinned event phantom-event introduces depends_on ['aru-ninth-bell']` |
| r96 relation `from`/`to` flip | exit 1 `ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, …]; added [evin, aru, …]` |
| r95 tick-10 `place_id chalk-stair → salt-court` | exit 1 `ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'salt-court'` |
| r94 description text edit (inventory-neutral) | exit 2 `DIGEST-MISMATCH` |
| r95 `south bell` → `South bell` (the tool's own tamper case) | exit 2 `DIGEST-MISMATCH` |
| r95 append event with empty `depends_on` | exit 2 `DIGEST-MISMATCH` |
| r94 duplicate `depends_on` entry | exit 2 `DIGEST-MISMATCH` |
| r94 reordered `depends_on` | exit 2 `DIGEST-MISMATCH` |
| r95 `timeline.json` deleted | exit 2 `FILE-MISSING` |
| r95 `timeline.json` malformed | exit 2 `MALFORMED-JSON` |
| copy with unpinned basename (`not-a-pinned-fixture`) | exit 2 `UNPINNED-FIXTURE` |
| nonexistent dir with unpinned basename | exit 2 `UNPINNED-FIXTURE` |

Notes (bounded behavior, consistent with the contract's documented precedence "semantic findings
decide first; a content change the inventory does not model exits 2"): duplicate/reordered
`depends_on` normalize via `sorted(set(...))`, so they are inventory-neutral and fall through to
exit 2 — i.e. semantic no-ops are still flagged, just at the digest level. `FIXTURE-MISSING` is
reachable only when the path's basename is pinned (the tool's self-test uses
`missing_case/r95-crossing-aftermath`; source line 393) — a nonexistent unpinned path yields
`UNPINNED-FIXTURE` first. No traceback observed on any path.

## 5. Self-test

Final revision: `python3 corpus/tools/dependency_freeze.py --self-test` → all 14 CASE lines `ok`,
`SELF-TEST 14/14`, `RESULT PASS`, exit 0; persisted expectations present in the contract
(`self_test.expected`, 14 cases with `exit`, `finding_ids`, `forbid_traceback`).

Recorded mid-round observation (evidence of the fix landing, corroborates Q3 §5 defect note 1):
at ~17:44, before the 17:44:37 rewrite, `--self-test` ran `SELF-TEST 5/14` exit 1, with nine cases
(`reduction_edge_drop`, `addition_edge_phantom`, `event_removed`, `event_endpoint_change`,
`relation_endpoint_flip`, `relation_removed`, `relation_added`, `digest_tamper`,
`malformed_json`) all leaking the same scratch path:
`FINDING FILE-MISSING: timeline.json is missing from /var/tmp/dependency-freeze-self-test-…/missing_timeline/r95-crossing-aftermath`
— a late-binding closure bug. The failing output preserves the fixture basename, so the run was
against an intermediate revision between the 20457 b one I first read (whose `copy_case` lacked the
basename) and the final 20552 b one; V22 logs the size trail `20457 → 20499 → 20552`. I did not
hash the tool at that instant, so the exact intermediate hash is not claimed. `V41-scratch/c3-selftest.out`
and V17's §6 independently show the same 5/14 with the same nine case names. The final revision
binds paths as lambda defaults and passes 14/14.

## 6. Anomaly — foreign pin `c3red` (independently corroborated; producer self-reported)

The delivered contract carries a fifth pin not in the declared chain:
`c3red | fixture ".ufo/waves/round-96/seats/V41-scratch/c3red" | content eff4b354c092… |
counts {events 3, dependency_edges 1, relations 1}` — its frozen `paired-crossing-decision`
`depends_on` is `["aru-ninth-bell"]`, i.e. **the reduced (BR-01-mutated) state**.

My independent evidence trail:
- `.ufo/waves/round-96/seats/V41-scratch/c3-freeze.out`: `FROZEN c3red: events 3; dependency-edges 1; relations 1` / `DIGEST eff4b354c092a9c4…` / `RESULT PASS` — a `--freeze` probe run on V41's scratch copy.
- `V41-scratch/c3-interim.log:34`: the immediately preceding receipt
  `FINDING UNPINNED-FIXTURE: no pin for 'c3red' … (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])` — four pins before, five after.
- `V33-scratch/v33-battery-current.txt:113,119` and `V22-c3-tamper.scratch/snapshots/rev-1743/`
  (contract snapshot) quote the five-pin list including `c3red` — recorded observations, which is
  why Q3 §7 left the pin in place rather than rewriting the contract mid-round.

Assessment (bounded): harmless to the admitted path — pins are basename-keyed, no corpus fixture is
named `c3red`, the chain verifies 4/4 clean, and the BR-01 mutation on r94 still exits 1 (my §3).
Real hazard confirmed: `--freeze` has no scope guard, so any scratch path rewrites the delivered
contract and can "legalize" a red state under its own key; running
`dependency_freeze.py .ufo/…/V41-scratch/c3red` now exits 0 PASS on the mutated copy. Recommended
closure action (delete `pins.c3red` or add a corpus-scope guard) is for round adjudication, not
this seat.

## 7. Byte-modification check

`git status --porcelain corpus/` at 17:46: `M corpus/tools/map_obligations.py` (C1),
`?? corpus/fixtures/r96-crossing-response/` (C2), `?? corpus/knowledge/r96-response-scope-note.md`
(C2), `?? corpus/tools/dependency-freeze-contract.json` + `?? corpus/tools/dependency_freeze.py`
(C3). C3 added exactly its two declared files and modified nothing else in corpus/. (Side
observation, not this seat's claim: `corpus/tools/map-obligations-contract.json` and
`corpus/tools/README.md` were unmodified at that time — mtimes 16:27/16:28, pre-round.)

## 8. Comparison with V17/V18/V22 (all three reports landed during this run)

All three peers verified the **same frozen revision** (`a3b57978…` / `7d568cc4…`) and report the
same class/ID taxonomy I observed; no class or ID disagreement anywhere.

- **V17** (`V17-c3-br01-demo.md`): two-sided BR-01 evidence at the r94, r95 and r96 chain links —
  the mutation exits 1 `REDUCTION-DETECTED` while `check_bible` (CLEAN), `support_check` (PASS) and
  the hardened `map_obligations` (PASS) all exit 0 on the same bytes; chain 4/4 clean; self-test
  14/14; independently records the same intermediate-revision `SELF-TEST 5/14` with the same nine
  case names; same bounds (basename-keyed pins, `c3red`, `--freeze` rewrites the contract).
- **V18** (`V18-c3-addition-endpoint.md`): phantom addition → `ADDITION-DETECTED`; relation flip /
  true endpoint change → `ENDPOINT-CHANGE`; event-row deletion with its edges → two
  `REDUCTION-DETECTED` lines (a variant I did not run — complements my §4); digest-only tamper →
  exit 2 `DIGEST-MISMATCH`; added event without deps → exit 2 (same boundary I found); relation
  addition → `ADDITION-DETECTED`; self-test 14/14 with fail-closed `CONTRACT-INVALID` coupling;
  its 17:43 contract read showed four pins (`2601c18a…`), corroborating the mid-round 4-pin → 5-pin
  transition my §6 evidences.
- **V22** (`V22-c3-tamper.md`): two-method independent digest recomputation equals the pinned
  digests; non-edge JSON edit exits 2 `DIGEST-MISMATCH`; BR-01 drop exits 1 `REDUCTION-DETECTED`;
  `--freeze` on copies re-pins and re-verifies clean; records the same `c3red` pin; adds T4c —
  freezing a **mutated** copy named `r94-paired-crossing` rebinds that basename's pin and then
  reports a false `ADDITION-DETECTED` on the pristine fixture (workspace demo, contract restored);
  notes Markdown files sit outside the digest (README edits stay green).

Combined with my matrix, every declared C3 behavior now has at least two independent reproductions,
and the one delivered-bytes defect (`c3red`) plus the unguarded `--freeze` hazard are corroborated
by Q3 §7, V17, V18 and V22.

## Bottom line

PASS — C3 verified on the frozen revision (pins 0-mismatch, chain 4/4 clean, BR-01 reduction and
addition/endpoint mutations exit 1 with the declared stable IDs, could-not-evaluate paths exit 2,
self-test 14/14) with one independently corroborated, producer-self-reported anomaly (foreign
`c3red` scratch pin freezing a reduced state; harmless to the admitted path, real `--freeze`
hazard for closure); V17, V18 and V22 all verified the same revision with no class/ID
disagreement and the same residual.

# V17 — c3-br01-demo (round 96)

- Seat: V17, verifier. Claim under test: **C3 / coverage** — `corpus/tools/dependency_freeze.py`
  + `corpus/tools/dependency-freeze-contract.json` close carried debt BR-01 (dependency reduction
  undetectable). Seat task: reproduce the BR-01 demonstration on scratch copies — drop
  `evin-ninth-bell` from the r94 tick-10 `depends_on` → exit 1 `REDUCTION-DETECTED`; and show that
  without this gate `check_bible` / `support_check` / `map_obligations` all stay green on the
  **same mutated copy**.
- Verdict: **C3 BR-01 closure VERIFIES** on the delivered revision. The blind spot is real, and the
  new gate is the only delivered check that sees it.
- Revision pinned for every measurement below (hashes identical before and after my runs):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
$ sha256sum corpus/tools/map_obligations.py   # Q1's hardened revision, the one the "old world" ran against
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
```

  Working-tree HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27`. All scratch work under
  `.ufo/waves/round-96/seats/scratch/V17/`; no corpus byte written by this seat (`git status`
  audit in §8). No `--freeze` invocation: that path rewrites Q3's byte-owned contract (§7).

## 0. Poll-wait record

Q3's two artifacts were absent at first inspection (17:38) and landed at 17:42; `Q3-dependency-freeze.md`
(bottom line PASS) was present by 17:52. One mid-flight observation: the tool was rewritten at
`17:44:37` while I was probing it — my first `--self-test` run at the pre-fix revision failed 9/14
(§6). All verification below was re-run after the report existed and the mtime/hash were stable;
no result in this report comes from the pre-fix revision except the explicitly labeled §6 artifact.

## 1. Core demo — BR-01 reduction on r94 (the wave's declared demonstration)

Scratch copy `.ufo/waves/round-96/seats/scratch/V17/br01-demo/r94-paired-crossing` (copy of the
delivered fixture; the directory keeps the pinned basename so the pin resolves — see §7), then:

```
$ python3 - <<'PY'   # mutation: drop evin-ninth-bell from the tick-10 depends_on
before: paired-crossing-decision ['aru-ninth-bell', 'evin-ninth-bell']
after : paired-crossing-decision ['aru-ninth-bell']
PY
$ for f in entities.json relations.json sources.json contradictions.json claim-excerpt-map.md README.md \
    fictional-excerpts.md inspiration-note.md source-excerpt.md; do cmp -s <pristine>/$f <copy>/$f \
    && echo "same: $f"; done
same: entities.json / relations.json / sources.json / contradictions.json / claim-excerpt-map.md /
      README.md / fictional-excerpts.md / inspiration-note.md / source-excerpt.md
```

Exactly one byte-run differs from the pristine fixture (the `depends_on` array), verified by `diff -u`
and by `timeline.json` digests (`f0209f90…` pristine → `dd66ded2…` mutated).

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/scratch/V17/br01-demo/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit=1
```

Two consecutive runs produced byte-identical output (`cmp` → identical) with `rc=1` both times.

## 2. OLD world on the *same* mutated bytes — every pre-r96 gate stays green

Same directory, same bytes, no further edits:

```
$ python3 corpus/fixtures/check_bible.py .ufo/.../br01-demo/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/tools/support_check.py .ufo/.../br01-demo/r94-paired-crossing
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py .ufo/.../br01-demo/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
exit=0
```

The blind spot is not a strawman: the mutated fixture's **own map prose asserts the deleted edge by
event ID** — `claim-excerpt-map.md:48` still reads "the new tick-10 decision is ordered after and
depends on both (`aru-ninth-bell` and `evin-ninth-bell`)" — and `map_obligations` still reports
`raw=14 mapped=14 PASS` because the pointer→row binding and source IDs are untouched. No delivered
pre-r96 gate compares the JSON `depends_on` set against the map's dependency wording; that is
precisely the BR-01 gap, and `dependency_freeze` closes it with a stable FINDING ID.

## 3. Breadth — the same class across the chain, and it is *not* a duplicate of the C1 hardening

The reduction was repeated on the r95 and r96 members (the r95 case is exactly the one carried in
the r95 debt ledger as NB-05 / BR-01):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/.../br01-r95/r95-crossing-aftermath   # tick-11 depends_on emptied
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']
RESULT FAIL   exit=1
  check_bible → CLEAN 0 violations, exit=0 ; support_check → RESULT PASS 15/15, exit=0 ;
  map_obligations → OBLIGATIONS raw=15 mapped=15, RESULT PASS, exit=0

$ python3 corpus/tools/dependency_freeze.py .ufo/.../br01-r96/r96-crossing-response   # tick-12 depends_on emptied
FREEZE r96-crossing-response: events 5/5; dependency-edges 3/4; relations 1/1
FINDING REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']
RESULT FAIL   exit=1
  check_bible → CLEAN 0 violations, exit=0 ; support_check → RESULT PASS 16/16, exit=0 ;
  map_obligations → OBLIGATIONS raw=16 mapped=16, RESULT PASS, exit=0
```

r95's map `claim-excerpt-map.md:49` and r96's `:50` both assert the deleted edges in prose
("…the new tick-11 aftermath event is ordered after and depends on the tick-10 decision
(`paired-crossing-decision`)" / "…the new tick-12 response event is ordered after and depends on the
tick-11 report (`aftermath-missing-evin`)"), and both copies still pass every legacy gate. The
`map_obligations` runs above are against Q1's **C1-hardened** revision (`2b0ba815…`, the file that now
gates inventory mismatch): the deletion class and the dependency-reduction class are disjoint, so C3
closes a gap C1 does not touch.

## 4. Supplementary mutation classes (my own copies, same revision)

| copy | mutation | dependency_freeze | check_bible | support_check | map_obligations |
|---|---|---|---|---|---|
| `br01-demo` | drop `evin-ninth-bell` (r94 tick-10) | exit 1 `REDUCTION-DETECTED` | 0 | 0 | 0 |
| `br01-add` | add existing `aru-ninth-bell` to tick-9 `evin-ninth-bell` | exit 1 `ADDITION-DETECTED` | **exit 1** `timeline inversion 'aru-ninth-bell' tick 9 not before 'evin-ninth-bell' tick 9` | 0 | 0 |
| `br01-phantom` | add nonexistent `phantom-ninth-bell` | exit 1 `ADDITION-DETECTED` | **exit 1** `unknown event 'phantom-ninth-bell'` | (n/a) | (n/a) |
| `br01-endpoint` | swap relation `from`/`to` | exit 1 `ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [evin, aru, …]` | 0 | 0 | 0 |

Honest reading: the **addition** class is partially covered by `check_bible` when the added edge
dangles or violates tick order (F15's a2 behaviour, reproduced here) — the strictly new coverage is
the **reduction** class and the **relation-endpoint** class, where all three legacy gates stay green
(`br01-endpoint`: CLEAN / PASS / PASS, all exit 0). The wave's claim says "an added-edge mutation must
also exit 1", which holds; the gate's distinct value-add is the reduction + endpoint classes.

## 5. Delivered chain verifies 4/4 clean, including r96 with Q5's docs present

```
r88-m3-maya-cluster     events 2/2; dependency-edges 0/0; relations 0/0  DIGEST 15ef230e…  RESULT PASS exit=0
r94-paired-crossing     events 3/3; dependency-edges 2/2; relations 1/1  DIGEST 2527beb9…  RESULT PASS exit=0
r95-crossing-aftermath  events 4/4; dependency-edges 3/3; relations 1/1  DIGEST d541ae64…  RESULT PASS exit=0
r96-crossing-response   events 5/5; dependency-edges 4/4; relations 1/1  DIGEST d422a9b3…  RESULT PASS exit=0
```

All four exit 0; the r96 run is with `README.md` and `claim-excerpt-map.md` present, confirming the
digest covers JSON tables only and Q5's doc writes do not disturb a pin.

## 6. Self-test — 14/14 PASS at the frozen revision (plus a mid-flight artifact, reported)

At the frozen revision:

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
... (14 cases, all ok) ...
SELF-TEST 14/14
RESULT PASS   exit=0
```

Mid-flight artifact, reported because it is real evidence about the producer's process: my first
`--self-test` run (pre-fix tool, before the 17:44:37 rewrite) returned `SELF-TEST 5/14` with
`FINDING SELF-TEST-MISMATCH: cases failed: ['addition_edge_phantom', 'digest_tamper',
'event_endpoint_change', 'event_removed', 'malformed_json', 'reduction_edge_drop', 'relation_added',
'relation_endpoint_flip', 'relation_removed']`, every failing case reporting
`FINDING FILE-MISSING: timeline.json is missing from /var/tmp/dependency-freeze-self-test-…/missing_timeline/r95-crossing-aftermath`.
Cause: all case lambdas captured the single rebinding `scratch` variable, so each case verified the
last copy built. The delivered revision binds paths as lambda defaults (`lambda p=scratch: [p]`) and
passes 14/14 — independently matching Q3's §5 defect (1). No stale copy of the broken revision is in
the tree; the revision I measured is the one hashed at the top of this report.

## 7. Bounds and hazards observed (not C3 blockers; recorded for closure)

1. **Pins are keyed by directory basename.** `verify()` resolves the pin via
   `fixture.resolve().name`, and there is no pin-name override flag. A scratch copy with any other
   name cannot be verified at all:

   ```
   $ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/scratch/V17/mut-reduction
   FINDING UNPINNED-FIXTURE: no pin for 'mut-reduction' in corpus/tools/dependency-freeze-contract.json
   (pinned: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
   RESULT ERROR   exit=2
   ```

   So the BR-01 demo is only reproducible with a pin-faithful copy name (what §1 does). Bound, not a
   defect: exit 2 fail-closed is the declared contract for unpinned fixtures — but a verifier
   following "copy to a scratch dir" naively gets exit 2, not exit 1.
2. **A foreign pin `c3red` is inside the delivered contract** (independently confirmed here, matching
   Q3 §7): `pin keys: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath',
   'r96-crossing-response']`, `c3red fixture: .ufo/waves/round-96/seats/V41-scratch/c3red`,
   `c3red counts: {'events': 3, 'dependency_edges': 1, 'relations': 1, 'entities': 5, 'sources': 3}`.
   Verification semantics are unaffected (no corpus fixture is named `c3red`; chain runs above are
   exit 0), but the delivered contract carries an out-of-corpus scratch pin.
3. **`--freeze` writes the delivered contract file.** Combined with (1)+(2) this is how `c3red` got
   in: any verifier running `--freeze` on a scratch copy silently mutates Q3's byte-owned artifact
   and changes the delivered revision hash. I did not run `--freeze` at any point; a scope guard
   (refuse paths outside `corpus/fixtures/`) or a closure-time `pins.c3red` removal is a real r97
   candidate.
4. **Digest coverage is JSON-only** (`entities/relations/timeline/sources/contradictions`), so prose
   doc edits never move a pin — correct for Q5's late doc writes, but it means the freeze says
   nothing about map/README wording (that stays with `support_check`/`map_obligations`).
5. **Precedence is semantic-first** (contract `precedence` field): a mutation that is both semantic
   and byte-level reports exit 1, not 2. Consistent with the observed four-way demo matrix.

## 8. Write audit

```
$ git status --porcelain corpus/
 M corpus/tools/map_obligations.py                    # Q1
?? corpus/fixtures/r96-crossing-response/             # Q4/Q5
?? corpus/knowledge/r96-response-scope-note.md        # Q6
?? corpus/tools/dependency-freeze-contract.json       # Q3
?? corpus/tools/dependency_freeze.py                  # Q3
```

No path in this list was written by V17. All my mutations live under
`.ufo/waves/round-96/seats/scratch/V17/` (`br01-demo`, `br01-add`, `br01-phantom`, `br01-r95`,
`br01-r96`, `br01-endpoint`, `mut-reduction`, `run1.txt`, `run2.txt`). No commits, no pushes, no
network, no nested agents. `--freeze` never invoked.

## Bottom line

PASS — on the frozen revision (`dependency_freeze.py` `a3b57978…`), the BR-01 mutation (drop
`evin-ninth-bell` from the r94 tick-10 `depends_on`) exits 1
`FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']`
while `check_bible` (CLEAN), `support_check` (PASS) and the C1-hardened `map_obligations` (PASS) all
exit 0 on the very same bytes; the same pattern reproduces on r95 and r96, the delivered chain
verifies 4/4 clean, and `--self-test` is 14/14 PASS — with three recorded bounds: basename-keyed pins
(a non-pin-named scratch copy gets exit 2 `UNPINNED-FIXTURE`), a foreign `c3red` scratch pin inside
the delivered contract, and `--freeze` rewriting that contract.

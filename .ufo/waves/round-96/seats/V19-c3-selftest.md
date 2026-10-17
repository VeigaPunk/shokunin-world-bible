# V19 — C3 self-test / contract verification (round 96)

Seat: V19 `c3-selftest-contract`. Lane repo root: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(cwd for every command below; all paths quoted as run). Baseline r95 closure `dcb2d92`; HEAD at
verification `60dba0c2aa344860b10a2fc63e00468d1b134f27`.

Producer under test: Q3 — `corpus/tools/dependency_freeze.py` +
`corpus/tools/dependency-freeze-contract.json`. Producer report:
`.ufo/waves/round-96/seats/Q3-dependency-freeze.md` (note: not the `Q3-c3-dependency-freeze.md`
name my poll condition assumed; my poll timed out on the name while the report existed — reported
here so the round's poll-hygiene record is accurate). Q3's report-time digests are identical to the
revision I verified, so all results below are on the producer's final declared revision.

## 0. Verified revisions (digests pinned at every run)

| revision | tool sha256 | contract sha256 | mtime (local) | self-test |
|---|---|---|---|---|
| R1 (superseded mid-flight) | `d17297bb2d49c5bb35783824bf0704513cc1f1a692f11878379bb1edad56282f` | `2601c18afa6a75435562d1877eaf430525141eddacdaa112b985980119f11cc5` | 17:42 | **FAIL 5/14, exit 1** |
| R2 (final, = Q3 report-time) | `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` | `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975` | 17:44:37 / 17:44:27 | **PASS 14/14, exit 0** |

R1 → R2 is a real mid-round repair by Q3 (documented in its report §5); both receipts are kept
below because the R1 defect is the strongest available evidence that the persisted expectations are
*load-bearing*: they caught a real harness bug and refused to pass.

## 1. `--self-test` on the final revision R2 — PASS, exit 0

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
SELF-TEST 14/14
RESULT PASS
EXIT=0
```

All 14 cases run as subprocesses inside `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")`
(`dependency_freeze.py:411-417`); expectations are read from `contract["self_test"]["expected"]`
(`:400-406`), and the expectation set is pinned as a whole — `FROZEN_CASES` vs `expected` mismatch is
`CONTRACT-INVALID` (`:403-406`).

Final battery re-run after Q3's report landed (report-time digests, unchanged):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2   → SELF-TEST 14/14 / RESULT PASS   (exit 0)
$ (4 × verify chain fixtures)                                       → RESULT PASS ×4                  (exit 0 each)
```

## 2. R1 failure receipt (superseded revision — kept as evidence)

```
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=2 expected=1 findings=['FILE-MISSING'] MISMATCH
  observed stdout: ['FINDING FILE-MISSING: timeline.json is missing from /var/tmp/dependency-freeze-self-test-nzc588z5/missing_timeline/r95-crossing-aftermath', 'RESULT ERROR']
... (same FILE-MISSING/missing_timeline path for 8 further cases) ...
SELF-TEST 5/14
FINDING SELF-TEST-MISMATCH: cases failed: ['addition_edge_phantom', 'digest_tamper', 'event_endpoint_change', 'event_removed', 'malformed_json', 'reduction_edge_drop', 'relation_added', 'relation_endpoint_flip', 'relation_removed']
RESULT FAIL
EXIT=1
```

Cause: in R1 every case lambda was `lambda: [scratch]` capturing the *name* `scratch`, so all nine
mutated cases resolved to the last assignment (the `missing_timeline` scratch dir). The persisted
expectations caught it: exit 1, never a false PASS. Q3's R2 (17:44:37) fixed it; V41's scratch log
`V41-scratch/c3-selftest.out` (17:44) recorded the same 5/14 against R1, independently confirming
the defect. Q3's report §5 discloses both R1 defects (the closure bug and a `ToolError`-outside-handler
traceback) as found-and-fixed; my receipts corroborate both.

## 3. Persisted expectations are independently meaningful — hand-derived, not tool-derived

I read the raw fixture JSON directly (`cat corpus/fixtures/<f>/timeline.json relations.json sources.json`)
and recomputed the inventories and digests with an independent extractor
(`.ufo/waves/round-96/scratch/V19/independent_edges.py`, written without reading `dependency_freeze.py`).

Hand-derived vs persisted pin (2 fully quoted, all 4 chain fixtures checked):

* `r95-crossing-aftermath` — events `{aru-ninth-bell: [], evin-ninth-bell: [], paired-crossing-decision: [aru-ninth-bell, evin-ninth-bell], aftermath-missing-evin: [paired-crossing-decision]}` (4 events, 3 edges); relations `[[aru, evin, agreed_co_stewardship_for_this_crossing]]`; `sha256(timeline.json)=3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177`; `sha256(relations.json)=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9`.
  Persisted pin: identical events/relations; identical both digests; counts `events 4, dependency_edges 3, relations 1, entities 5, sources 4`. **Match.**
* `r96-crossing-response` — events 5 / edges 4 (`response-evin-salt-court: [aftermath-missing-evin]` appended); relations 1; sources 5 (`veil-verse, paired-clock, crossing-minute, aru-aftermath-note, evin-response-note`).
  Persisted pin: `events 5, dependency_edges 4, relations 1, entities 5, sources 5`. **Match.**

Full independent re-check of all five pins in the delivered contract (per-file sha256 vs recomputed
sha256, and counts recomputed from raw JSON):

```
c3red: file-digest mismatches=none; count mismatches=none; counts observed={'events': 3, 'dependency_edges': 1, 'relations': 1, 'entities': 5, 'sources': 3}
r88-m3-maya-cluster: file-digest mismatches=none; count mismatches=none; counts observed={'events': 2, 'dependency_edges': 0, 'relations': 0, 'entities': 4, 'sources': 2}
r94-paired-crossing: file-digest mismatches=none; count mismatches=none; counts observed={'events': 3, 'dependency_edges': 2, 'relations': 1, 'entities': 5, 'sources': 3}
r95-crossing-aftermath: file-digest mismatches=none; count mismatches=none; counts observed={'events': 4, 'dependency_edges': 3, 'relations': 1, 'entities': 5, 'sources': 4}
r96-crossing-response: file-digest mismatches=none; count mismatches=none; counts observed={'events': 5, 'dependency_edges': 4, 'relations': 1, 'entities': 5, 'sources': 5}
contract revision field: 60dba0c2aa344860b10a2fc63e00468d1b134f27
git HEAD: 60dba0c2aa344860b10a2fc63e00468d1b134f27
```

Two expectation classes demonstrated independently on scratch copies of the live fixture
(copied under my scratch so the pinned basename still resolves):

BR-01 reduction (drop `evin-ninth-bell` from `paired-crossing-decision.depends_on`):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/scratch/V19/mut-reduction/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
EXIT=1
```

Digest-only tamper (description case change; inventory untouched):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/scratch/V19/mut-tamper/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 871a3981bf58cca98cc034f5f6aeee8fe39643c16d9c9ab70929b49d13bcd835 != pin d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9; fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT=2
```

This also demonstrates the declared precedence (`dependency-freeze-contract.json: "precedence"`):
the reduction case changed both the inventory *and* the digest, and semantic inventory decided
first (exit 1, not exit 2). Matches `verify()` ordering at `dependency_freeze.py:271-280`.

Chain verification (delivered fixtures, delivered revision):

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0   RESULT PASS  EXIT=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1   RESULT PASS  EXIT=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1 RESULT PASS EXIT=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1 RESULT PASS EXIT=0
```

Exit-code contract also exercised on the error paths:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r93-m2-kojiki-cluster
FINDING UNPINNED-FIXTURE: no pin for 'r93-m2-kojiki-cluster' in corpus/tools/dependency-freeze-contract.json (pinned: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR  EXIT=2
$ python3 corpus/tools/dependency_freeze.py                     → INVALID-ARGUMENTS  EXIT=2
$ python3 corpus/tools/dependency_freeze.py --self-test corpus/fixtures/r94-paired-crossing → INVALID-ARGUMENTS  EXIT=2
```

## 4. No live-tree writes (admitted path)

Bracketed the whole admitted path (self-test + 4 fixture verifies) with a full-corpus digest
snapshot:

```
$ find corpus -type f | LC_ALL=C sort | xargs sha256sum > $S/pre3.digests
$ python3 corpus/tools/dependency_freeze.py --self-test   # EXIT=0, SELF-TEST 14/14
$ (4 × verify)                                            # all EXIT=0
$ find corpus -type f | LC_ALL=C sort | xargs sha256sum > $S/post3.digests
$ diff $S/pre3.digests $S/post3.digests
NO-WRITES-IN-WINDOW
```

`verify()`/`build_model()` open fixtures read-only; only `freeze()` writes, and only to
`CONTRACT_PATH` (`dependency_freeze.py:310-312`). The admitted path (verify, `--self-test`) writes
nothing. `git status --porcelain corpus/` after all runs showed only the round's expected entries
(`M corpus/tools/map_obligations.py` = Q1; `?? corpus/fixtures/r96-crossing-response/` = Q4/Q5;
`?? corpus/knowledge/r96-response-scope-note.md` = Q6; `?? corpus/tools/dependency_freeze.py`,
`?? corpus/tools/dependency-freeze-contract.json` = Q3) — no writes attributable to this tool.

## 5. Perturbed scratch expectation → fails closed (6 perturbations)

Each perturbation applied to a *copy* of tool+contract+base fixture under my scratch dir
(`.ufo/waves/round-96/scratch/V19/P1..P8`); the live tree was never the target.

| # | perturbation | observed | exit |
|---|---|---|---|
| P1 | `self_test.expected.reduction_edge_drop.finding_ids = ["ENDPOINT-CHANGE"]` | `SELF-TEST 13/14`, `FINDING SELF-TEST-MISMATCH: cases failed: ['reduction_edge_drop']`, `RESULT FAIL` | **1** |
| P2 | `self_test.expected.clean.exit = 1` | `CASE clean: exit=0 expected=1 findings=[] MISMATCH`, `SELF-TEST 13/14`, `RESULT FAIL` | **1** |
| P3 | delete `expected.digest_tamper` | `FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['digest_tamper'] extra=[]`, `RESULT ERROR` | **2** |
| P4 | tool regression: `compare()` forced to `return []` (no inventory finding ever) | reduction/addition/endpoint cases fall through to `DIGEST-MISMATCH`; `SELF-TEST 11/14`, `RESULT FAIL` | **1** |
| P5 | `--freeze` run from a *copied* tree on a copied r96 fixture | copied contract rewritten (byte-identical rebuild); live contract untouched (`sha256sum -c` → `OK`) | 0 |
| P6 | add a sixth bogus pin (`bogus-foreign-pin`, `fixture: /tmp/not-a-delivered-fixture`) | **`SELF-TEST 14/14`, `RESULT PASS`** — foreign pin *not* detected | **0** |
| P7 | `self_test.base_fixture = "does-not-exist-fixture"` | **`SELF-TEST 14/14`, `RESULT PASS`** — persisted field ignored | **0** |
| P8 | mutate the *delivered* base fixture bytes in the copy (drop the r95 tick-10 edge) | `CASE clean: exit=1 expected=0 findings=['REDUCTION-DETECTED'] MISMATCH`, plus cascading mismatches; `RAW_EXIT=1` | **1** |

P1/P2 show the persisted expectations are consulted, not decorative. P3 shows the expectation set
is pinned as a whole. P4 shows the self-test would catch a real gate regression rather than
rubber-stamping it. P8 shows the self-test doubles as a delivered-fixture integrity guard (the
`clean` case runs against the live base fixture path). Every perturbation failed closed; none
produced a false PASS. P6/P7 are the two places where nothing is checked (findings F2/F6).

## 6. Findings

**F1 (MEDIUM, delivered artifact — also disclosed by Q3 itself) — the delivered contract carries a
foreign pin for a verifier scratch directory, written by the unguarded `--freeze` path.**

`corpus/tools/dependency-freeze-contract.json` pins **five** fixtures, not the four declared chain
fixtures. The extra pin:

```json
"c3red": {
  "fixture": ".ufo/waves/round-96/seats/V41-scratch/c3red",
  "content_sha256": "eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28",
  "events": { "...": "paired-crossing-decision depends_on = [aru-ninth-bell] only" },
  "counts": { "events": 3, "dependency_edges": 1, "relations": 1, "entities": 5, "sources": 3 }
}
```

Provenance is unambiguous: `V41-scratch/c3-freeze.out` reads
`FROZEN c3red: events 3; dependency-edges 1; relations 1 / DIGEST eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28`
— byte-identical to the pin's `content_sha256`. `stat` ordering: c3red `timeline.json` 17:44:26.98
→ contract mtime 17:44:27.30. V41 ran the *live* tool with `--freeze <scratch dir>`; because
`freeze()` writes `CONTRACT_PATH` unconditionally (`dependency_freeze.py:310-312`), the pin landed
in the delivered contract. The pinned inventory is the BR-01 *reduction* mutation, i.e. the
delivered contract freezes a mutated scratch copy as if it were a fixture.

Impact: inert for the four chain fixtures and for `--self-test` (pin lookup is by basename), so it
does not change any chain verdict — but the delivered contract is no longer self-contained
(`fixture` points outside `corpus/fixtures/`, into a seat scratch dir that is not part of the
delivered corpus), it contradicts the declared C3 shape ("frozen per-fixture dependency-edge
inventory ... for the chain r88-m3 / r94-paired-crossing / r95-crossing-aftermath /
r96-crossing-response"), and it is visible in the gate's own output (`UNPINNED-FIXTURE ... (pinned:
['c3red', ...])`).

Q3's report §7 discloses the same anomaly independently (convergent finding) and states it was left
in place deliberately because two verifier receipts already quote the pinned list. I checked that
rationale rather than accepting it: `V33-scratch/v33-battery-current.txt:113,119` does quote the
five-name pinned list, and `V22-c3-tamper.scratch/snapshots/rev-1743/dependency-freeze-contract.json`
does contain the `c3red` pin — both claims are true. Q3's stated remedy for closure/r97 (delete
`pins.c3red`, or add a `--freeze` scope guard refusing paths outside `corpus/fixtures/`) is the
right one; the guard was intentionally not added mid-round so as not to change the tool hash under
the verifier battery. My verdict treats F1 as a disclosed, deliberately-carried artifact defect,
not a hidden one.

**F2 (MEDIUM, gap) — nothing validates the pin set.** P6: with a sixth bogus pin added, the
self-test still printed `SELF-TEST 14/14 / RESULT PASS` (exit 0). There is no check that `pins`
equals the declared chain and no self-test case for pin-set hygiene, so a foreign pin can neither
be prevented (F1) nor detected. Adding `"pins"`-set validation to `--self-test` would have caught
F1 the moment it happened.

**F3 (LOW / informational) — `--freeze` mutates the live contract from any invocation context.**
Confirmed in isolation (P5): running `--freeze` from a *copied* tree writes the copied contract and
leaves the live one byte-identical, so the write target is `__file__`-relative — but any seat
running the live tool with a scratch target rewrites the delivered contract. The round declares
`--freeze` "not used in the admitted path"; it was in fact used, by V41, on the delivered artifact.

**F4 (LOW, superseded) — R1 harness defects, fixed in R2.** Recorded in §2; the persisted
expectations turned the closure bug into exit 1 rather than a false PASS, which is the behavior the
seat claim requires. Q3's report discloses both; V41's log corroborates the self-test one.

**F5 (informational) — `r96-crossing-response` appeared at 17:43 (Q4), after the tool's first
revision; its pin was already present and correct in the R1 contract and verifies clean in R2.**
No drift found between the r96 pin and the delivered fixture bytes; Q5's later `README.md` /
`claim-excerpt-map.md` additions do not disturb the pin (digest covers the five JSON tables only),
which I confirmed by re-verifying r96 clean with both docs present.

**F6 (LOW, informational) — the persisted `self_test.base_fixture` field is decorative.** P7: with
`base_fixture` set to `does-not-exist-fixture`, the self-test still passed 14/14 because the base is
hardcoded at `dependency_freeze.py:48` (`SELF_TEST_BASE = "r95-crossing-aftermath"`). The contract
field invites a maintainer to believe the base is configurable; it is not. Either honour it or drop
it.

## 7. Seat claim verdict

* `dependency_freeze.py --self-test` → **PASS, exit 0 (14/14)** on the final revision `a3b57978` / `7d568cc4`. ✔
* Expectations persisted in `dependency-freeze-contract.json` are independently meaningful → **confirmed**: hand-derived inventories and digests match for all pinned chain fixtures, and the two demonstrated classes (reduction → exit 1 `REDUCTION-DETECTED`; digest-only tamper → exit 2 `DIGEST-MISMATCH`) match their persisted expectations; P4/P8 show the expectations discriminate against a broken gate and a mutated delivered fixture. ✔
* No live-tree writes → **confirmed for the admitted path** (verify + `--self-test`, corpus digest window identical); **not** true of `--freeze`, which is how F1 happened. ✔ (with F1/F3 caveat)
* Perturb one scratch expectation → fails closed → **confirmed** (P1/P2 exit 1, P3 exit 2 `CONTRACT-INVALID`; plus P4 regression catch and P8 delivered-fixture guard). ✔

**Bottom line: PASS on the seat's four checks (self-test 14/14 exit 0 on the producer's final
revision; persisted expectations independently meaningful by hand-derivation; no writes on the
admitted path; perturbations fail closed) — with one MEDIUM delivered-artifact defect (F1: the
contract carries a foreign `c3red` pin pointing at `.ufo/waves/round-96/seats/V41-scratch/c3red`,
written by the unguarded `--freeze` path; also disclosed by Q3, whose leave-in-place rationale I
verified against V22/V33 receipts) and one MEDIUM gap (F2: nothing detects a foreign pin — P6 shows
a bogus pin still yields 14/14 PASS), plus LOW notes F3 (unguarded `--freeze` write target) and F6
(decorative `base_fixture`). The chain gate itself verifies 4/4 clean and none of these alter a
chain verdict; F1 makes the delivered contract non-self-contained and contradict the declared
four-fixture pin shape, and should be resolved at closure or r97.**

## Reproduction

```
cd /home/vgpnk/Projects/shokunin/lore-shokunin
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
python3 corpus/tools/dependency_freeze.py --self-test                       # expect 14/14, exit 0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response  # expect PASS, exit 0
python3 -c "import json;print(sorted(json.load(open('corpus/tools/dependency-freeze-contract.json'))['pins']))"
  # observed: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
```

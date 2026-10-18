# V21-verdict-operability — round-101 seat report (verifier)

- lane: lore-shokunin; round 101; seat V21; model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r100 closure `6f86bf2`; tree HEAD at seat start `ebec6bb` (round declaration); wave tree uncommitted; no commits, no pushes, no network
- writes: this report only; declared scratch `.ufo/waves/round-101/seats/V21-scratch/` (isolated tool/contract/fixture mirrors for the guard test and the independent probe; nothing outside it was executed in a writing mode — `--freeze` was never invoked against delivered bytes from this seat)
- verdict: **one OPERABILITY verdict — PASS** (nothing inoperable observed on the delivered revision), with one recorded exception: **U2 producer report ABSENT at 40/40 poll tries** (the U2 *artifact* is present and was verified on its own surface; the producer-report cross-check for C2 could not be performed)

## Axes used (godspeed)

presence (artifacts + reports exist) → operability (claimed commands run as stated) → fidelity (outputs match C1/C2/C3 wording) → verifiability (independent, quotable command→output pairs). All four walked; the frontier settled on operability, as seated.

## Baseline captured before delivery landed (read-only, ~00:07)

```
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -8
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT=0

$ for f in <seven chain fixtures>; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
r88-m3-maya-cluster exit=0 :: RESULT PASS      r97-crossing-acknowledgment exit=0 :: RESULT PASS
r94-paired-crossing exit=0 :: RESULT PASS      r98-clerk-filing exit=0 :: RESULT PASS
r95-crossing-aftermath exit=0 :: RESULT PASS   r99-window-lapse exit=0 :: RESULT PASS
r96-crossing-response exit=0 :: RESULT PASS
r100-docket-review exit=2 :: RESULT ERROR
```

Pre-state: 7/7 clean, the eighth fixture present-but-unpinned (exit 2), self-test 18/18, SKILL.md still said "18 cases … 7/7 clean", `grep -c r100-docket-review` on the contract = 0, `git diff HEAD` empty. This is the exact delta C1/C3 claim to close.

## C1 operability — verified on delivered bytes (all commands mine, repository root)

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing r99-window-lapse r100-docket-review; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo exit=$?; done
→ all eight: RESULT PASS, exit=0        # 8/8 clean, r100-docket-review now exit 0

$ git diff HEAD --stat
 corpus/tools/dependency-freeze-contract.json | 143 ++++++++++++++++++++++++++-
 corpus/tools/dependency_freeze.py            |  18 ++++
 (later: + SKILL.md 7 +- , corpus/tools/README.md 59 ++)
```

Pin-field stability (C1's "no other pin's fields change"), measured by comparing every inherited pin object HEAD↔worktree:

```
pins old: 7 new: 8 | changed existing pins: [] | top revision b5fe4729… → ebec6bbd…
```

Exactly the disclosed shape: one added pin (`r100-docket-review`), zero changed fields on the seven inherited pins, writer-managed top-level `revision` refresh only. The guarded writer itself was exercised by U1 (integration-time, once; correctly not re-run by this seat); the guard's refusing behavior I tested on an isolated copy in declared scratch:

```
$ cp dependency_freeze.py dependency-freeze-contract.json V21-scratch/fakeroot/corpus/tools/
$ cd V21-scratch/fakeroot && python3 corpus/tools/dependency_freeze.py --freeze /tmp/definitely-outside-corpus
FINDING SCOPE-REFUSED: --freeze refuses /tmp/definitely-outside-corpus …; the frozen scope is corpus/fixtures/**
exit 2 ; contract md5 unchanged (99c5b16b75a0e548f133a7d4b8be3ece) after refusal
```

Guard operable: refuses foreign paths before any write.

## C3 operability — verified on delivered bytes (all commands mine)

```
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -6
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
EXIT=0
```

Persisted expectation diff HEAD↔worktree: `expected` 18 → 19 entries; added exactly `repointed_edge: {exit: 1, finding_ids: ["ADDITION-DETECTED", "REDUCTION-DETECTED"], forbid_traceback: true}`; no case removed or altered; `git diff HEAD -- corpus/tools/dependency_freeze.py` = +18 lines (FROZEN_CASES entry, case body swapping `aftermath-missing-evin`'s `paired-crossing-decision` → `aru-ninth-bell`, dated docstring paragraph). Independent reproduction of the class outside the harness (my scratch mirror of delivered tool + contract + r95 fixture, swap applied by hand):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath   # in V21-scratch/fakeroot
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']
FINDING REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']
RESULT FAIL
PROBE-EXIT=1
```

Both findings in one run, exit 1 — matches C3's claim and U1's quoted cross-check byte-for-byte in finding text. The blind-spot "wrong-but-earlier edge" row is now exercisable from the delivered gate.

## C2 operability — artifact present; producer report ABSENT (recorded)

`corpus/knowledge/r101-r10-register-first-entry.md` landed during polling (try 3). Reference-surface check: every cited local record resolves (r88 decision table, r89 format demo, r93 worked example, r95/r96 scope notes, r100 synthesis, all three crossing fixtures, LOG.md). The one non-resolving path, `corpus/knowledge/cross-cluster-contradictions.md`, is asserted-absent by the entry itself and that absence is the required state ("the register destination remains uncreated, exactly as the R10 appendix requires") — MISS is expected, not a defect. The entry's pointers (line ranges, `file.json#/pointer` rows, fixture claims) are therefore followable as written; operability surface PASS. **Not verified from this seat:** the entry's semantic claims (compatibility demonstration) are the depth axis, other seats' mandate; and U2's producer report never landed, so no producer-side receipts were available to cross-check — the poll record stands as evidence.

## Poll-wait record (protocol-conformant)

40 tries at 20 s spacing (~00:07–00:30 -03:00), max reached. Landing order observed: contract pin + U1 scratch (pre-try-1), knowledge file (try 3 of poll 2), SKILL 19-case row + README addendum (by try 1–3 of poll 2), U1 report (try 7 of poll 2). **U2-*.md: absent at try 40.** All-reports polls subtracted SELF per endgame convention; the stall-escape is this record, not fatal — the U2 artifact itself is present, so C2 was adjudicated on delivered bytes, not on a plan.

## Cross-checks against U1's report (landed try 27 overall)

Every U1 claim I can independently re-run reproduced exactly: 19/19 self-test with the quoted `repointed_edge` line; 8/8 chain; contract diff = 3 hunks (pin + case + revision refresh); inherited pins field-identical; guard message text matches; SKILL.md/README diffs match the described dated-supersession edits (chain list now eight, "19 cases … r101 added `repointed_edge`", "exactly the eight chain fixtures, verifying 8/8 clean", new 2026-10-18 supersession bullet, prior r100 bullet kept as history). U1's claim of exactly four owned modified files matches `git diff HEAD --stat` at my final read. One first-attempt scratch probe failed mechanically (missing target dir before `cp`) and was redone cleanly; the failure left no trace outside declared scratch and is recorded here as evidence of method, not of tool defect.

## Disclosures / bounds

- No `--freeze` was ever run against delivered bytes from this seat; the guard test and probe used copies under `V21-scratch/`. Self-test runs create gitignored `*-self-test-*/` scratch at repo root; the tool cleans its own `TemporaryDirectory`.
- The r100 pin's recorded revision `ebec6bb…` is the r101 declaration commit — the tree HEAD at freeze time; the wave tree remains uncommitted, so a future commit hash will not match the pin's revision field. Pre-disclosed writer behavior (r100 precedent); noted, not an operability defect.
- C2's depth/semantics and C1/C3's admission are other seats' axes; this seat witnessed operability only.
- Scratch retained as evidence: `.ufo/waves/round-101/seats/V21-scratch/` (guard outputs `guard1.out`/`guard2.out`, probe fakeroot).

## Bottom line

PASS — every delivered command reproduces on the delivered revision (chain 8/8 clean incl. the new guarded r100 pin, self-test 19/19 with `repointed_edge` exit 1 carrying both findings in one run, `--freeze` guard refuses foreign paths without writing, inherited pins field-identical, docs superseded with dates); U2 producer report ABSENT at 40/40 polls, recorded, with the U2 artifact itself present and surface-verified.

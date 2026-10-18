# V03-c1-repointed — round-101 seat report (verifier)

- lane: lore-shokunin; round 101; seat V03; model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r100 closure `6f86bf2`; tree HEAD at seat start `ebec6bb` (round declaration); no commits, no pushes, no network
- assignment: poll for U1, then verify the new persisted self-test case pins the repointed-edge class: (a) scratch copy with `clerk-review-first-passage`'s `depends_on` repointed to a different valid earlier event → BOTH `REDUCTION-DETECTED` and `ADDITION-DETECTED`, exit 1, run twice for stable IDs; (b) a scratch contract missing the new case → self-test fails closed
- writes: this report + declared scratch `.ufo/waves/round-101/seats/V03-scratch/` only; everything else read-only (verified: `git status` before my first scratch write showed only U1's two owned `M` files; my probe never touched delivered bytes — the repoint was applied to a mirror copy under the declared scratch)

## Poll log (poll-wait protocol)

- 00:03 — seats dir absent; `corpus/tools/` bytes still the r100 state (contract `self_test.expected` = 18 cases, 7 pins, no `repointed_edge` anywhere; `git status` clean for the owned files). Self-test baseline `SELF-TEST 18/18 / RESULT PASS`, exit 0; `r100-docket-review` verify → `FINDING UNPINNED-FIXTURE … RESULT ERROR`, exit 2 (before-picture).
- 00:10–00:12 — U1's writes landed: 8 pins (incl. `r100-docket-review`), 19 cases in both tool `FROZEN_CASES` and contract `self_test.expected` (new case `repointed_edge`).
- 00:21:43 — poll loop try 7 (20 s interval) found the producer report `seats/U1-chain-eight.md`. Not ABSENT; verified against delivered bytes + the report.

Byte snapshot verified against: `dependency_freeze.py` sha256 `60a78bc39440917202488e4f6366a26540aeb494a089e5793864c1a4992fe3bf`; `dependency-freeze-contract.json` sha256 `b8fc63c3500d626df8d5c34b28327c10716610512a3c72ef56a19f3b46de36ca`.

## Check B — repointed edge on the r100 fixture (mandated probe)

Method: mirror the delivered tool + contract + `r100-docket-review` into a scratch root (the tool derives `ROOT` from its own path, so the pin's repo-relative `fixture` path resolves inside the mirror — no `PATH-MISMATCH`, and the mirror receipt confirms the landed pin was used); repoint `clerk-review-first-passage` (tick 16, `depends_on ['clerk-lapse-recorded']`) to `acknowledgment-aru-records` — a different valid earlier event in the same fixture (tick 13 < 16); verify.

Run twice (harness `V03-scratch/repoint_probe.sh`), full tool output:

```
$ bash repoint_probe.sh <mirror> corpus/fixtures/r100-docket-review acknowledgment-aru-records
EDIT clerk-review-first-passage depends_on ['clerk-lapse-recorded'] -> ["acknowledgment-aru-records"]
--- run on mirror ---
FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1
FINDING ADDITION-DETECTED: event clerk-review-first-passage gained depends_on ['acknowledgment-aru-records']
FINDING REDUCTION-DETECTED: event clerk-review-first-passage lost depends_on ['clerk-lapse-recorded']
RESULT FAIL
exit=1
```

Run 1 and run 2: identical findings, `RESULT FAIL`, exit 1 each; `diff` of the two tool-output sections → `OUTPUTS-IDENTICAL` (stable IDs, no timestamps/pids in output). Both findings in a single run on the same event, exactly the persisted class.

## Check C — fail closed when the new case is missing

(a) Mandated: mirror with the delivered tool + contract **minus** `self_test.expected.repointed_edge` (18 cases) + base fixture:

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py --self-test
exit=2
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['repointed_edge'] extra=[]
RESULT ERROR
```

Fails closed before any case runs (the missing/extra set check precedes case construction in `run_self_test`).

(b) Complementary direction: delivered contract + tool with `"repointed_edge"` removed from `FROZEN_CASES`:

```
$ python3 <mirror2>/corpus/tools/dependency_freeze.py --self-test
exit=2
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=[] extra=['repointed_edge']
RESULT ERROR
```

Both directions exit 2 (the could-not-evaluate class) — no silent pass possible when tool and contract disagree about the case set.

## Supporting observations (context; other seats own these axes)

- Delivered `--self-test`: `SELF-TEST 19/19 / RESULT PASS`, exit 0, including `CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok`. The persisted case uses the r95 base (`aftermath-missing-evin`: `paired-crossing-decision` → `aru-ninth-bell`, tick 9 < 11 per U1); my seat probe independently exercises the same class on the r100 event per this seat's assignment.
- Chain: all eight pinned fixtures verify exit 0 `RESULT PASS`; r100 digest `77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19` — identical to the value in U1's freeze receipt. 8/8 clean.
- Contract delta vs HEAD, structurally: added pins `['r100-docket-review']`, removed `[]`; all seven inherited pins field-identical (`pre-existing pins with field changes: NONE`); `self_test.expected` added `['repointed_edge']`, removed `[]`; new expectation `{"exit": 1, "finding_ids": ["ADDITION-DETECTED", "REDUCTION-DETECTED"], "forbid_traceback": true}`; base fixture unchanged; top-level `revision` refreshed `b5fe4729…` → `ebec6bb…` (the disclosed writer-managed refresh). `git diff 6f86bf2 -- corpus/tools/dependency-freeze-contract.json | grep '^@@'` → exactly three hunks (`-32,7 +32,7`, `-677,6 +677,139`, `-806,6 +939,14`), matching U1's report verbatim.
- Docs: at 00:12 `SKILL.md` and `corpus/tools/README.md` were still git-clean; both are now `M` with the eight-fixture / 19-case wording, `r101 added repointed_edge`, and dated-supersession bullets (SKILL.md lines 96–103; README Round-101 addendum from line 423).

## Producer-report cross-check

U1's report claims match my independent evidence on every point I can check: 19/19, 8/8 + digests, three-hunk diff, revision refresh, persisted expectation JSON, fail-closed exit-2 semantics, docs supersession. No contradictions found.

## Disclosures

- My first fail-closed attempt produced void results due to **my own** harness bugs (a stdin heredoc consumed the tool source instead of the file; the stripped contract was never copied into the mirror), yielding `CONTRACT-INVALID: contract not found` exit 2 and an inert `exit=0`. Both were discarded and redone cleanly; the void outputs are not evidence about the delivered tool. Recorded as a bounded stall-escape.
- My mandated probe is a scratch-mirror variant (mirrored tool/contract/fixture), not an in-place edit of delivered bytes — required by the read-only rule and by the tool's path binding. The mirrored receipt line proves the landed r100 pin was the comparator.
- I did not rerun `--freeze` (integration-time only, per U1's own report and the tool's contract); verification only.
- Wave tree left uncommitted per round convention; my writes confined to this report + `V03-scratch/`.

## Bottom line

PASS — the delivered gate pins the repointed-edge class end to end: r100 repoint probe → REDUCTION-DETECTED + ADDITION-DETECTED in one run, exit 1, stable across two runs; contract-missing-case and tool-missing-case both fail closed with exit 2 `CONTRACT-INVALID`; self-test 19/19, chain 8/8, inherited pins and expectations untouched; U1's report consistent with the delivered bytes.

# V28 — late-bookkeeper (round 101, failsafe census + receipt reconciliation)

**Seat:** V28 late-bookkeeper, round-101 single wave (28 seats: 2 producers + 26
verifiers), lane `lore-shokunin`, model `zai-coding-plan/glm-5.3-flash-low`.
Baseline: r101 declaration `ebec6bb` (2026-10-17T23:59:55-03:00); r100 closure
`6f86bf2`; wave tree uncommitted during the round. This seat is the FAILSAFE:
it wrote near its deadline regardless of wave state, records which seats were
missing at cutoff, and reconciles the wave's landed artifacts against the
declared claims C1/C2/C3. All commands were run from the lane root with
`python3`. No repo byte outside this report and `.v28-scratch/` was modified;
no commits, no pushes, no network.

## Axes worked

1. **Census completeness** — empirical seat census at cutoff (all-reports polls subtract SELF).
2. **Receipt reconciliation** — every claim checked against artifacts by direct run, with quoted output.
3. **Timeliness** — bounded poll (40 × 20 s), then file anyway.
4. **Evidence fidelity** — baseline locked before producer writes; hashes recorded for delta proof.

## 1. Baseline receipts (locked 00:01:38–00:03:00, before any producer write)

- `git log --oneline -3` → `ebec6bb` (r101 declaration), `a04f986`, `6f86bf2`.
  `git status --short` at 00:01:40 → only `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`
  (inherited stray; V13 later showed mtime 2026-10-17 22:32:40, predates round start).
- Contract pin census: `pins` = 7 — `['r88-m3-maya-cluster', 'r94-paired-crossing',
  'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment',
  'r98-clerk-filing', 'r99-window-lapse']`; no `r100-docket-review`.
- `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 18/18` /
  `RESULT PASS`, exit 0 (18 case ids enumerated from `self_test.expected`).
- `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review` →
  `FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review' … (pinned: [all seven])`,
  `RESULT ERROR`, exit 2. (Note: the gate has no all-fixtures mode and no
  `--fixture` flag; verify is positional.)
- Baseline file digests (sha256): `dependency_freeze.py` `fb9bb9ff…`,
  `dependency-freeze-contract.json` `ea012b9c…`, `corpus/tools/README.md` `c99217cd…`,
  `SKILL.md` `09b2949a…`. HEAD blob anchors (`git rev-parse HEAD:<f>`) at first
  check matched V22's independent table (`ac590a83…`, `936a2082…`, `309341ba…`,
  `27b9b6ff…`) — my baseline is corroborated by a second seat.
- `corpus/knowledge/r101-r10-register-first-entry.md` — ABSENT at baseline.

## 2. Poll-wait record (protocol: 20 s interval, max 40 tries)

Background loop sampled every 20 s from 00:02:35; full log retained in scratch.
Key transitions:

| try | time (-03) | state |
|---|---|---|
| 1 | 00:02:35 | `round-101/` absent entirely |
| 2 | 00:02:55 | `seats/` exists; no reports; pins 7 |
| 18 | 00:08:16 | last sample with pins 7 |
| 19 | 00:08:36 | **pins 8** (U1's contract landed ~00:08) |
| 40 | 00:15:37 | bound exhausted: U1_reports=0, U2_reports=0, knowledge_missing=1 |

`POLL-LOOP-DONE tries=40`. Bounded stall-escape recorded, not fatal.

## 3. Landed-artifact reconciliation (direct runs, quoted)

### C1 — eight-fixture chain (landed mid-poll; verified twice, 00:11 and 00:17)

Pin census: 8 pins, `r100-docket-review` present; **baseline pins with changed
fields: NONE** (each of the 7 prior pins byte-compared against
`git show HEAD:…`); top-level `revision` `b5fe4729…` → `ebec6bb…` (the
writer-managed refresh the claim discloses). Chain run, per-fixture positional
(the gate has no all-fixtures mode):

```
r88-m3-maya-cluster exit=0 :: RESULT PASS     r96-crossing-response exit=0 :: RESULT PASS
r94-paired-crossing exit=0 :: RESULT PASS     r97-crossing-acknowledgment exit=0 :: RESULT PASS
r95-crossing-aftermath exit=0 :: RESULT PASS  r98-clerk-filing exit=0 :: RESULT PASS
r99-window-lapse exit=0 :: RESULT PASS        r100-docket-review exit=0 :: RESULT PASS
```

8/8 clean, exit 0 each, stable across both runs. The prior baseline
`UNPINNED-FIXTURE` exit 2 for r100 flipped to PASS — the pin is live against
the delivered tree. V02's independent scratch-mutation discharge (drop tick-16
`depends_on` → `REDUCTION-DETECTED`, exit 1, digest `77debadf…` matching) was
read and corroborates pin liveness beyond my clean-run receipt.

### C3 — self-test 18 → 19 (landed; verified)

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS          (exit=0)
```

Persisted expectation: `repointed_edge {"exit": 1, "finding_ids":
["ADDITION-DETECTED", "REDUCTION-DETECTED"], "forbid_traceback": true}` — both
findings in one run, exit 1, exactly the claimed repointed-edge class. Tool
diff is +18 lines (`repointed_edge` docstring note, `FROZEN_CASES` entry,
mirror builder, registration); code at `dependency_freeze.py:591-598` repoints
`aftermath-missing-evin`'s `depends_on` from `paired-crossing-decision` to the
valid-but-earlier `aru-ninth-bell` (tick 9 < 11) in a scratch mirror. The
`--freeze` writer itself is unchanged (r97 guard retained) — consistent with
the ownership note "guarded --freeze for the pin; direct edit for the
self-test case".

**C3 tail NOT landed at cutoff:** `corpus/tools/README.md` and `SKILL.md`
still match baseline digests (`c99217cd…` / `09b2949a…`); grep for
`19 case|19/19|repoint` in both returned nothing. README still documents the
seven-fixture chain and 18 cases.

### C2 — ABSENT at cutoff; corpus pre-receipts recorded for the later verifier

`corpus/knowledge/r101-r10-register-first-entry.md` did not exist at baseline
and at every one of the 40 poll samples plus the 00:18:01 final check. Per
protocol it is reported ABSENT and NOT adjudicated — never verify a plan. For
whoever verifies when it lands, the corpus receipts it must cite were located
and are real:

- Aru's account: `r95-crossing-aftermath/fictional-excerpts.md:26` "Tick 11: I
  waited at the Chalk Stair through the agreed bell." (timeline
  `aftermath-missing-evin`, tick 11).
- Evin's account: `r96-crossing-response/fictional-excerpts.md:37` "Tick 12: I
  was at Salt Court through the same agreed bell." (timeline
  `response-evin-salt-court`, tick 12).
- Shared referent: `r94-paired-crossing/relations.json` — `aru` →`agreed_co_stewardship_for_this_crossing`→ `evin`, source `crossing-minute`.
- Both accounts are compatible with non-performance at the Chalk Stair (the
  NON-conflict reading is corpus-supported), and r89's R10 note requires
  shared event identity/date/occasion from cited in-world accounts, forbids
  canon assertion, and names `corpus/knowledge/cross-cluster-contradictions.md`
  as the live register destination — a file that also does not exist yet, so
  the declared r101 path is a new knowledge file, not an append to an
  existing register. Worth one adjudicator glance when U2 lands.

## 4. Seat census at cutoff (00:18:01; all-reports polls subtract SELF)

Filed verifier reports (3): `V02-c1-discharge.md` (bottom line
`PENDING-FINAL-POLL`), `V13-scope-creep.md` (stub `IN PROGRESS`),
`V22-verdict-freshness.md` (verdict `PENDING`, sequence-2 poll in progress).
All three corroborate my baseline and landed-state receipts; none records a
completed final verdict yet.

Scratch evidence, active-but-unfiled seats (14): V03, V04, V05, V06, V09,
V11, V14, V16, V17, V20, V21, V23, V25, plus U1's `U1-chain-eight-scratch`
and lane-root `.scratch/` (V02 + `v26` poll scratch, per V13's scope report —
permitted but non-standard location, flagged by V13).

**ABSENT at cutoff (the failsafe record):**

1. **U1 producer report** (`U1-*.md`) — never appeared in 40 tries, though
   U1's artifacts demonstrably landed (contract+tool modified 00:07–00:08,
   scratch dir 00:08). Artifact-without-receipt at cutoff.
2. **U2 producer report** (`U2-*.md`) — never appeared; U2's artifact (C2
   knowledge file) also absent — no artifact, no receipt.
3. **C2 artifact** `corpus/knowledge/r101-r10-register-first-entry.md` — absent
   (0/41 checks).
4. **U1 doc updates** — `corpus/tools/README.md` + `SKILL.md` freeze-row /
   case-count edits not landed (digests unchanged).
5. Verifier reports from the remaining ~23 seats (V01, V07, V08, V10, V12,
   V15, V18, V19, V24, V26, V27 and any others in the declared 26) — none
   filed; ~14 left scratch only, the rest no trace in `seats/`.

Delivered-state digests at cutoff (stable from 00:11 to 00:17):
`dependency_freeze.py` `60a78bc39440917202488e4f6366a26540aeb494a089e5793864c1a4992fe3bf`,
`dependency-freeze-contract.json` `b8fc63c3500d626df8d5c34b28327c10716610512a3c72ef56a19f3b46de36ca`.

## 5. Contradictions observed

None. My receipts, V02's discharge, V13's scope census, and V22's freshness
sequence agree on every overlapping fact (baseline 7 pins/18 cases, 8-pin +
19-case landing ~00:08, docs and C2 file outstanding, revision refresh to
`ebec6bb`). `git status` at cutoff: ` M` on the two U1-owned tool files, `??`
on `.scratch/`, `.ufo/waves/round-101/`, and the inherited round-98 stray —
no unexpected writes to any non-owned corpus byte.

## Bottom line

**ABSENT** — at the 40-try cutoff (00:15:37–00:18:01 -03) both producer
reports (U1, U2), the C2 knowledge file, and the README/SKILL doc updates had
not landed, so the round's claims cannot be closed from receipts; the landed
C1/C3 artifacts themselves verified clean by direct run (8/8 chain exit 0,
self-test 19/19 with `repointed_edge` exit 1 both-findings, no baseline pin
fields changed), corroborated by V02/V13/V22.

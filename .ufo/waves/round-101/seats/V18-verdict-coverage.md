# V18 — verdict-coverage (round 101, lore-shokunin)

- Seat: V18 verdict-coverage · model zai-coding-plan/glm-5.3-flash-low · date 2026-10-18
- Baseline: r100 closure `6f86bf2`; tree HEAD at round start `ebec6bb` (r101 declaration); wave tree uncommitted.
- Assignment: read the C1 seats; own chain replay; ONE COVERAGE verdict with bounds. Writes confined to this report; no repo byte otherwise touched; no commits, no pushes, no network.
- Verdict axis: C1 coverage only. C2/C3 witnessed, not adjudicated (their seats own those verdicts).

## Poll record (20 s cadence, interleaved with verification; budget not exhausted)

- ~00:04–00:15: first ~8 tries — only `V22-verdict-freshness.md` (stub, PENDING); U1/U2 reports absent.
- ~00:15–00:18: V02, V13 (stub), V26, V28 land. None had U1's receipt (their 40-try windows had closed; all recorded U1-report ABSENT at their cutoffs — accurate at cutoff, superseded below).
- ~00:22: `U1-chain-eight.md` present (producer receipt landed ~00:21:43 per V03's independent poll log). `V03-c1-repointed.md`, `V12-gates-boundary.md` also in.
- Final check ~00:24: U2 producer report still ABSENT; C2 artifact `corpus/knowledge/r101-r10-register-first-entry.md` landed 00:20:29 (existence noted only; C2 not adjudicated here).
- Bounded stall-escape recorded: seats V22/V13 and V02's `PENDING-FINAL-POLL` bottom line were still open at my write time — their axes, not blocking this verdict, which rests on my own replay.

## Own chain replay (not producer prose)

Replay 1 — per-fixture verify, all eight, positional (the gate has no all-fixtures mode), via a python driver:

```
r88-m3-maya-cluster          exit=0 RESULT PASS
r94-paired-crossing          exit=0 RESULT PASS
r95-crossing-aftermath       exit=0 RESULT PASS
r96-crossing-response        exit=0 RESULT PASS
r97-crossing-acknowledgment  exit=0 RESULT PASS
r98-clerk-filing             exit=0 RESULT PASS
r99-window-lapse             exit=0 RESULT PASS
r100-docket-review           exit=0 RESULT PASS
CLEAN 8/8
```

Replay 2 — digest-level, capturing each gate-printed DIGEST:

```
r88 acf677a7  r94 048b8ff3  r95 97cffd7b  r96 43911900
r97 a28b9ea0  r98 5ecf84e1  r99 7fe7e3b0  r100 77debadf   (all exit=0 RESULT PASS)
```

All eight digests identical to U1's receipt table and to V26's independently reproduced values, byte-for-byte.

## Byte-level scope of the change (vs `6f86bf2` and vs HEAD)

Structured JSON compare of `pins`, `git show HEAD:contract` vs worktree:

- HEAD pins 7 → worktree pins 8; added `['r100-docket-review']`; removed `[]`.
- **Pre-existing pins whose fields changed: NONE** — all seven inherited pins field-identical (stronger than hunk-counting: whole-subtree equality per pin).
- Top-level `revision`: `b5fe4729…` → `ebec6bb…` (the disclosed writer-managed refresh).
- `self_test.expected`: added `['repointed_edge']` only; the 18 inherited expectations unchanged.
- `git diff 6f86bf2 -- …contract.json | grep -c '^@@'` → `3`; `git diff --stat 6f86bf2 -- corpus/tools/` → contract +143/−1, `dependency_freeze.py` +18, README +59 — matches U1's stated deltas exactly.
- New pin payload checked directly: counts `{events 9, dependency_edges 8, relations 1, entities 6, sources 9}` (9 events / 8 edges re-counted from the pin body — consistent); tick-16 event `clerk-review-first-passage` pinned with `depends_on ['clerk-lapse-recorded']`; all ten `pinned_files` exist on disk; `content_sha256 77debadf…` reproduced by the gate at verify time (Replay 2).

## Guard behavior (refusal paths only — the writer was NOT re-run)

```
$ python3 corpus/tools/dependency_freeze.py --freeze .ufo
FINDING SCOPE-REFUSED: --freeze refuses .ufo (resolves to …/lore-shokunin/.ufo); the frozen scope is corpus/fixtures/** …
RESULT ERROR          exit=2
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
RESULT ERROR          exit=2
```

`git status` after both probes: unchanged (same two U1-owned `M` files) — refusal paths write nothing. The guard is r97 hardening retained unchanged: `git show HEAD:corpus/tools/dependency_freeze.py` already contains `SCOPE-REFUSED` (HEAD lines 13–14, 289–293); this round's tool diff is the self-test case only (+18 lines). Consistent with U1's ownership note ("guarded `--freeze` for the pin; direct edit for the self-test case").

Per U1's own disclosure ("must not be rerun to check a delivery") and V26's recorded incident (an accidental re-freeze refreshes both revision fields), I did **not** execute `--freeze` on the delivered fixture. Provenance acceptance therefore rests on: the quoted FROZEN receipt (U1 report; also recorded in the README Round-101 addendum), the guard verified live above, the writer byte-unchanged this round, and delivered bytes reproducing the receipt's digests — not on my own re-execution of the freeze.

## Adjacent witnesses (quoted from my own runs; not verdict claims)

- Self-test on delivered bytes: `CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok` / `SELF-TEST 19/19` / `RESULT PASS` / exit 0 — C3's persisted class enforced by the same gate that carries the C1 chain (calibration seats own the C3 verdict).
- Pin liveness beyond clean runs is covered by C1-sibling seats I read and whose methods I checked against my own numbers: V02 (drop tick-16 edge → `REDUCTION-DETECTED`, exit 1, same digest), V03 (repoint tick-16 edge to a valid earlier event → both findings in one run, exit 1, stable across two runs; fail-closed `CONTRACT-INVALID` exit 2 in both missing-case directions). My replay cannot contradict them: identical tool/contract snapshots (tool sha256 `60a78bc3…`, contract `b8fc63c3…` — equal to V03's and V28's recorded values).
- Doc tail landed and read in diff form: SKILL.md freeze row now lists the eight-fixture chain, "19 cases … r101 added `repointed_edge`", and a dated r101 supersession bullet; README carries the Round-101 addendum including the freeze receipt. V02/V26/V28's "docs not yet landed" gap records were true at their cutoffs (README/SKILL mtimes 00:20:30/00:20:06) and are superseded by the current state.

## Cross-seat coherence on C1

U1 (producer receipt), V02 (discharge), V03 (repoint probe + fail-closed), V26 (6/6 reproduced), V28 (failsafe reconciliation) agree with my independent replay on every overlapping fact: 8/8 chain with identical digests, pin-addition-only contract delta, three-hunk diff, revision refresh to `ebec6bb`, 19/19 self-test, docs landed ~00:20, U1 report ~00:21:43. One minor discrepancy, not C1-load-bearing: V22's stub asserts the freeze guard "must appear in the diff" — it does not, because the guard predates the round (r97 hardening, present at HEAD). Flagged for V22's final; does not weaken C1, whose claim is that the pin went through the (already guarded) writer.

## Verdict

**COVERAGE (C1): PASS** — `r100-docket-review` is pinned into the frozen chain; the chain is eight fixtures verifying 8/8 clean (my own replay, twice, digest-identical to the producer receipt and to two independent seats); the contract delta is exactly the new pin + the disclosed writer-managed top-level revision refresh + the C3 expectation, with zero field changes to the seven inherited pins; the `--freeze` writer is scope-guarded and unchanged, with refusals verified live (exit 2, no writes); the doc tail (README addendum, SKILL.md freeze row) is landed with dated supersession.

Bounds: (1) provenance "pinned via guarded `--freeze`" accepted from the quoted receipt + live guard-refusal evidence + byte-identical delivered results, not from re-running the integration-time writer; (2) verdict covers C1 only — C2 artifact landed 00:20:29 and U2's report was still ABSENT at my final poll; both left to C2's seats; C3 witnessed (19/19), not adjudicated; (3) V22/V13 finals and V02's pending bottom line were open at write time and may add freshness/scope findings that do not touch these bytes; (4) ABSENT records in earlier seats' reports (U1 report, docs, C2 file) were accurate at their cutoffs and are superseded by the landings verified here — no re-rolls of their other findings.

## Bottom line

PASS — C1 coverage verified end-to-end by own replay: eight-fixture chain 8/8 clean with byte-stable digests, additive-only pin addition, guard live and unchanged, docs superseded; bounds as listed.

# S2 tools-docs — round-98 seat report

Seat: S2 (tools-docs), leaf, single-wave r98 swarm.
Owned file: `corpus/tools/README.md` (only file I wrote in the repo, plus this report).
Baseline: r97 closure `9a3d648`; wave tree uncommitted during the round. No commits, no pushes, no network.

## Deliverable

Round-98 addendum appended to `corpus/tools/README.md`. Diff shape:

```
$ git diff --stat 9a3d648 -- corpus/tools/README.md
 corpus/tools/README.md | 56 ++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 56 insertions(+)
```

Pure addition — no prior sentence rewritten; every stale number is superseded by a dated note ("prior text kept as delivered history"), matching the r95/r96/r97 addendum convention. README sha256 after my edit: `1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84`.

The addendum covers, per the seat brief: `SELF-TEST-MISMATCH` now exit 2 (aligned with `map_obligations`, pinned), legacy path-less pin migration by `--freeze`, the chain extended to six fixtures (r88/r94/r95/r96/r97/r98), the 17-case self-test, and the contract `precedence` text. Superseded numbers: the r96 paragraph's "(14/14, persisted in the contract)" and "freezes 4/4 clean"; the r97 supersession's "the self-test carries 16 persisted cases" and "the frozen chain is the declared four fixtures (`r97-crossing-acknowledgment` unpinned)".

## Byte state verified

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
```

The contract changed several times while I polled (`b06275f3…` r97 → `3a940a9f…` → `c435239d…` → `153ebc5b…`); **every result below was re-run against the final `153ebc5b…` contract and `03d04365…` tool**, not the intermediate bytes.

## Claim verification (commands + observed output)

### C1(a) `SELF-TEST-MISMATCH` exits 2

Probe: scratch tree in `/tmp/s2-r98/{before,after2}` holding each revision beside a copy of the contract with `self_test.expected.clean.exit` flipped 0→1. Delivered contract not modified.

Before (r97 tool from `git show 9a3d648:corpus/tools/dependency_freeze.py`):

```
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
exit=1
```

After (delivered tool):

```
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
mismatch_exit=2
```

Aligned with `map_obligations.py`, whose own mismatch path is `print("FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations"); print("RESULT ERROR"); return 2` (`corpus/tools/map_obligations.py:877-879`).

### C1(b) legacy path-less pin migrated by `--freeze`

Probe: scratch tree `/tmp/s2-r98/{before,after}` with `pins.r95-crossing-aftermath.fixture = null`.

Before (r97 tool):

```
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
exit=2
```

After (delivered tool):

```
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS
freeze_exit=0
# re-verify after migration:
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS
verify_exit=0
```

Bounded correctly: verification alone on a path-less pin still fails closed (`FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path`, exit 2), and a pin recording a *different* path is still refused `SCOPE-REFUSED` exit 2 (`dependency_freeze.py:369-374`).

### C1(c) contract `precedence` names the exit-2 order and finding IDs

Delivered `precedence` text (quoted in the addendum): semantic findings decide first (exit 1: `REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`); then exit-2 checks in order — `UNPINNED-FIXTURE`/`CONTRACT-INVALID`, `FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`/`MALFORMED-JSON`/`MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`; `--freeze` additionally raises `SCOPE-REFUSED`; path-less legacy pin migrated in place.

### C1(d) the 16 inherited cases are unchanged

```
old case count: 16 new case count: 17
added case ids: ['self_test_mismatch']
dropped case ids: []
changed inherited expectations: []
INHERITED-UNCHANGED: True
```

(compared case-by-case against `git show 9a3d648:corpus/tools/dependency-freeze-contract.json`).

### C2 chain six fixtures + V46 discharge

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"; echo "$f exit=$?"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0     … RESULT PASS, exit=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1     … RESULT PASS, exit=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1  … RESULT PASS, exit=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1   … RESULT PASS, exit=0
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1  … RESULT PASS, exit=0  (digest 3c922d20…)
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1        … RESULT PASS, exit=0  (digest 59a0f4fa…)
```

Pre-state for the same loop: r88/r94/r95/r96 exit 0, `r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … RESULT ERROR` exit 2.

V46 discharge, demonstrated on a scratch copy of r97 (pin path rewritten to the scratch copy; delivered contract and fixture untouched):

```
-- control, unmodified scratch copy --
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS
control_exit=0
-- mutation: acknowledgment-aru-records.depends_on := [] (tick-13 edge dropped) --
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL
reduction_exit=1
```

Before the pin existed this mutation was unreachable — the fixture produced only `UNPINNED-FIXTURE` exit 2.

### Self-test battery

```
$ python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 17/17
RESULT PASS
exit=0
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned … RESULT PASS
exit=0
```

`git diff --stat 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and `dependency-freeze-contract.json` — `map_obligations.py`, `support_check.py` and `boundary_doc_check.py` are byte-unchanged, as the addendum states.

## Cross-seat observations (not my claims)

- r98 fixture and map: at 20:31:18 `map_obligations.py corpus/fixtures/r98-clerk-filing` exited 1 with `FINDING missing_obligation` × 3 (`entities.json#/5/claims/0`, `entities.json#/5/first_appearance`, `timeline.json#/6`) while S4's map was mid-write; by 20:36 the same command prints `OBLIGATIONS raw=20 mapped=20` / `INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22` / `RESULT PASS`, exit 0. Recorded as a transient, not a defect.
- At 20:31 the contract's `provenance_note` still read "frozen set is exactly the four declared chain fixtures" while six pins existed; by the final `153ebc5b…` contract S1 had extended it to describe the r98 freeze (r97/r98 digests, V46 discharge). Resolved by the owner; no action taken.
- `corpus/tools/README.md` is referenced by no checker in the tree (`grep -rn "tools/README" --include=*.py --include=*.json --include=*.sh .` → no non-`.ufo` hits), so the addendum edit cannot break a pin.
- **Stray write observed in the PARENT tree (r94-F01 class), not mine:** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 bytes, mtime 2026-10-17 20:30, untracked in the parent repo) containing `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory` — a shell-redirect artifact from a seat running `python3 analyze.py > baseline-analyze.txt` with the parent as cwd. My own writes were confined to `corpus/tools/README.md`, this report, and `/tmp/s2-r98/**` (scratch), so this is another seat's stray; left in place as evidence for the closure sweep.

## Poll record

S1's report was polled from 20:27 with two background pollers (20 s cadence, 40-try budget) plus manual checks until 20:36+; at report time the seats directory holds `S1-scratch/` but **no `S1-*.md` report — ABSENT**. Per protocol I did not verify a plan: all C1/C2 claims above were verified against the delivered tool/contract bytes themselves, and every behavior was independently reproduced by my own probes rather than read from S1's (absent) report.

## Bounds

- I verified `dependency_freeze` behavior and documented it; I did not author or re-freeze any pin, and I did not modify the tool or contract (S1's bytes).
- The addendum's r98 pin numbers describe the contract as of `153ebc5b…`; if S1 re-freezes again before closure, the digests/revisions quoted would need a re-check.
- The r94 BR-05 residual (self-test scratch under the repository root, not gitignored) remains open and is recorded as such in the addendum.

**Bottom line: PASS** — C1 and C2 verified on the delivered revision by independent probes (17/17 self-test; exit-1→exit-2 mismatch flip; path-less pin migration; chain 6/6; r97 tick-13 edge REDUCTION-DETECTED), and the Round-98 addendum is appended to `corpus/tools/README.md` as a pure 56-line addition with dated supersession notes; S1's seat report was ABSENT at hand-off (artifacts verified, not a plan).

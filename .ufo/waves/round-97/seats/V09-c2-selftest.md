# V09 — c2-selftest (round 97, single-wave)

**Seat scope:** `dependency_freeze --self-test` 16/16 PASS; hand-derive 2 of the new
expectations; perturb one scratch expectation → fails closed.

**Claim under test:** C2 — `dependency_freeze` hardening (R3 byte-ownership:
`corpus/tools/dependency_freeze.py` + `corpus/tools/dependency-freeze-contract.json`).

Repo root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo). Writes confined to
`.ufo/waves/round-97/seats/V09-scratch/` and this report. No commits, no network.

## Delivered revision under test

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
```

Both hashes **match R3's report verbatim** (`R3-freeze-hardening.md`, delivered
revisions line). Drift re-check after all verification work:

```
$ sha256sum -c .ufo/waves/round-97/seats/V09-scratch/delivered.sha256
corpus/tools/dependency_freeze.py: OK
corpus/tools/dependency-freeze-contract.json: OK
```

No byte changed during verification. Baseline at seat start was the pre-change
revision (tool `a3b57978…` = committed `f3e09f9`, self-test 14/14, no
`PATH-MISMATCH` logic).

**Poll note:** the 40-try poll window (18:43:14 → 18:56:15) expired with R3's report
absent, although the artifacts had landed by 18:53–18:55. The report appeared at
18:56:23. I verified the delivered bytes (hash-pinned, drift-checked) and treat the
artifact as delivered; the timing gap is recorded, not hidden.

## Check 1 — self-test 16/16 PASS

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
... (14 legacy cases, all ok)
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS
EXIT=0
```

Case-set parity between the tool's `FROZEN_CASES` and the contract's
`self_test.expected` (so the suite cannot silently skip a pinned case):

```
tool FROZEN_CASES n= 16
contract expected n= 16
identical sets: True
```

New keys are `scope_refused` and `path_mismatch` — exactly the 14→16 growth the claim
declares. `self_test.base_fixture` remains `r95-crossing-aftermath`.

The two new cases are **non-vacuous** (read from the delivered source,
`dependency_freeze.py:494-500`): `path_mismatch` copies the base fixture to a real
foreign path (`workdir/path_mismatch/foreign/<base>`) and runs the real CLI against
it; `scope_refused` runs the real CLI with `--freeze` on a real out-of-scope target.
Neither can pass by triviality.

## Check 2 — hand-derived new expectations, independently reproduced

I derived both new expectations from the contract's exit-code semantics (semantic
inventory findings → exit 1; identity/argument errors → exit 2) *before* reading the
tool's own case construction, then reproduced each scenario by hand outside the
self-test harness.

### 2a. `path_mismatch` → exit 2, exactly `PATH-MISMATCH`

Derivation: the pin records the fixture's repo-relative path; a byte-identical copy at
any other path has no semantic inventory difference and no digest difference, so the
only possible signal is path identity — an identity error, i.e. ERROR class (exit 2)
with a single finding. Contract expectation: `{"exit": 2, "finding_ids":
["PATH-MISMATCH"], "forbid_traceback": true}`.

Reproduction on the real tree (read-only; copy staged in seat scratch):

```
$ diff -r corpus/fixtures/r95-crossing-aftermath $SC/foreign/r95-crossing-aftermath
copy is byte-identical (diff -r clean)
$ python3 corpus/tools/dependency_freeze.py $SC/foreign/r95-crossing-aftermath
EXIT=2
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath
  (resolves to /home/vgpnk/.../lore-shokunin/corpus/fixtures/r95-crossing-aftermath); invoked fixture
  resolves to /home/vgpnk/.../lore-shokunin/.ufo/waves/round-97/seats/V09-scratch/foreign/r95-crossing-aftermath
RESULT ERROR
```

Positive control — same fixture at its pinned path:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
EXIT=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
```

Derived expectation matches observed exactly (exit 2, one finding `PATH-MISMATCH`).
The pre-change baseline for the same scenario was `RESULT PASS` exit 0 — the hazard is
genuinely closed.

### 2b. `scope_refused` → exit 2, `SCOPE-REFUSED`, and no write on refusal

Derivation: `--freeze` is declared an integration-time operation limited to
`corpus/fixtures/**`; refusing an operation argument is ERROR class (exit 2), and the
refusal must leave the contract untouched. Contract expectation: `{"exit": 2,
"finding_ids": ["SCOPE-REFUSED"], "forbid_traceback": true}`.

Reproduction in a byte-copy sandbox (never the real contract — R3/R4 own those bytes):

```
$ sha256sum sandbox2/corpus/tools/dependency-freeze-contract.json   # before
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
$ python3 sandbox2/corpus/tools/dependency_freeze.py --freeze sandbox2/outside-fixtures/r95-crossing-aftermath
EXIT=2
FINDING SCOPE-REFUSED: --freeze refuses .../sandbox2/outside-fixtures/r95-crossing-aftermath (resolves to
  .../sandbox2/outside-fixtures/r95-crossing-aftermath); the frozen scope is corpus/fixtures/**
  (integration-time operation only)
RESULT ERROR
$ sha256sum sandbox2/corpus/tools/dependency-freeze-contract.json   # after
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
```

Contract hash unchanged → refusal performs no write (the claim's "scope-guarded"
property holds, not merely a message). Positive control — in-scope freeze accepted:

```
$ python3 sandbox2/corpus/tools/dependency_freeze.py --freeze sandbox2/corpus/fixtures/r95-crossing-aftermath
EXIT=0
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
RESULT PASS
pin fixture path now: corpus/fixtures/r95-crossing-aftermath
```

Pre-change baseline for the same scenario: `RESULT PASS` exit 0 with the pin rewritten
to `outside-fixtures/r95-crossing-aftermath` — closed.

## Check 3 — perturbed scratch expectation fails closed

Harness: sandbox byte-copy (`sandbox2/`) mirroring the repo layout so
`ROOT = Path(__file__).resolve().parents[2]` resolves to the sandbox; delivered tool +
delivered contract copied in, fixtures copied in. Two perturbations, each starting from
a fresh copy of the delivered contract:

**P1 — flip a new expectation's finding id** (`scope_refused.finding_ids` →
`["INVALID-ARGUMENTS"]`):

```
$ python3 sandbox2/corpus/tools/dependency_freeze.py --self-test
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['scope_refused']
RESULT FAIL
EXIT=1
```

**P2 — delete a new expectation** (`path_mismatch` removed from `self_test.expected`):

```
$ python3 sandbox2/corpus/tools/dependency_freeze.py --self-test
EXIT=2
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['path_mismatch'] extra=[]
RESULT ERROR
```

Both fail closed: a wrong expectation fails the named case (exit 1), and a missing pin
is rejected outright (exit 2) rather than silently skipped. A pre-change control run
(flipping `clean.exit` 0→1 on the 14-case contract) gave `SELF-TEST 13/14 … RESULT
FAIL`, confirming the harness was already sensitive and the new pins are wired into
the same machinery.

## Environment note (transient, not a tool defect)

At 18:44 `/tmp` had **inodes exhausted** (`df -i /tmp`: 1048576 used / 0 free, 100%),
so the then-current pre-change tool's self-test died with
`OSError: [Errno 28] No space left on device: '/tmp/dependency-freeze-self-test-…'`.
By 18:57 inodes had recovered (15694 used / 1032882 free, 2%).

The delivered tool is structurally immune: it moved the self-test tempdir from the
default `/tmp` into the repo root —

```
pre-change (f3e09f9:411):  tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")
delivered  (:517):         tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-", dir=ROOT)
```

so the delivered `--self-test` passes 16/16 both with and without a `TMPDIR` redirect,
and leaves no `dependency-freeze-self-test-*` leftovers in the repo root (checked).

## Cross-checks and discrepancies

- R3's report declares the same tool/contract sha256 I measured — no revision drift
  between claim and delivery.
- R3's own flagged discrepancy (the r96 pin refresh did **not** move
  `content_sha256`, because the cosmetic repair touched a non-JSON file outside
  `DATA_FILES`) is consistent with what I see: the r96 pin now records
  `fixture: corpus/fixtures/r96-crossing-response`, `revision:
  2393934237ea076366f3db6dceeff033edb52ab1`, counts 5/4/1/5/5. I did not re-derive
  that pin (R4/R3 territory); noting only that the claim's digest-change parenthetical
  is inaccurate, as R3 already reports.
- Seat V45 (`c2-guard-2`) independently reproduced the same three pre-change hazards I
  did (shadow copy PASS, out-of-scope `--freeze` accepted, DIGEST-MISMATCH unnamed) —
  convergent baseline, no contradiction.

## Bottom line

**PASS** — on the drift-checked delivered revision (tool `b06275f3…`, contract
`27273be2…`): `--self-test` is 16/16 with `scope_refused`/`path_mismatch` pinned in the
contract; both new expectations were hand-derived from the exit-code semantics and
reproduced independently outside the harness (exit 2 `PATH-MISMATCH` on a byte-identical
foreign copy with the in-scope path still exit 0; exit 2 `SCOPE-REFUSED` on an
out-of-scope `--freeze` with the contract hash unchanged, in-scope freeze still exit 0);
and two perturbed scratch expectations fail closed (15/16 exit 1; missing pin exit 2).
Only timing caveat: R3's report landed after my 40-try poll window, so the artifact was
verified hash-pinned against R3's declared revisions rather than after the report.

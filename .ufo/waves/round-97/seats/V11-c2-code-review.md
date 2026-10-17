# V11 — c2-code-review: line-by-line review of the `dependency_freeze` hardening (round 97)

Seat: V11 `c2-code-review`. Claim under test: **C2 — `dependency_freeze` hardening** (R3's bytes).
Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; every command run from that root with `python3`.
Baseline `f3e09f9` (HEAD `2393934`). No commits, no pushes, no network; writes confined to
`.ufo/waves/round-97/seats/V11-scratch/` and this report.

**Revision under test (final, stable across all end-state probes):**

| artifact | sha256 | note |
|---|---|---|
| `corpus/tools/dependency_freeze.py` | `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130` | 575 lines; diff vs baseline `+147/-42` (matches R3's report) |
| `corpus/tools/dependency-freeze-contract.json` | `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781` | 374 lines; 16 self-test expectations, 4 pins |

Baseline snapshots kept at `V11-scratch/baseline_dependency_freeze.py` / `baseline_contract.json`
(sha `a3b57978…` / `c65ac3bd…`, byte-identical to `git show f3e09f9:`).

## Poll protocol

Polled for artifacts **and** the producer report (20 s cadence, 40 tries; two background pollers,
plus manual checks). Timeline: tool bytes first moved at 18:51:30 (`fbaca38f…`, 480 lines — a
mid-write stub whose `FROZEN_CASES` already declared the two new cases while `self_test_cases` did
not implement them; recorded transient behavior: `FINDING CONTRACT-INVALID: self-test expectation
set mismatch; missing=['path_mismatch', 'scope_refused'] extra=[]`, exit 2 — the fail-closed loader
held even mid-write). R3's report `R3-freeze-hardening.md` and the final contract landed by
18:56. All verdict-bearing probes below were run against the final hashes; the delivered hashes are
still unchanged at the time of writing.

## 1. Diff shape

```
$ git diff --no-index --stat V11-scratch/baseline_dependency_freeze.py corpus/tools/dependency_freeze.py
 .../tools/dependency_freeze.py | 189 ++++++++++++++++-----
 1 file changed, 147 insertions(+), 42 deletions(-)
```

New/changed definitions (`corpus/tools/dependency_freeze.py`): `FIXTURE_SCOPE` (34),
`repo_relpath` (236), `scope_guard` (243), `validate_pin` (256, extended), `bind_path` (290),
`changed_files` (308), `verify` (320, reordered), `freeze` (351, guarded), `self_test_cases` (390,
mirror-root redesign), `run_self_test` (504). Contract: same 11 top-level keys, same 4 pins; only
`scope` (text), `provenance_note` (text), `revision` (→ HEAD) changed plus r96's pin `revision`;
`precedence`, `schema_version`, `data_files`, `required_files`, `exit_codes`, `tool` unchanged; the
file was re-indented 1→2 spaces by the tool's own `indent=2` writer (R3 disclosed it; content
verified field-by-field identical apart from the two deliberate text updates).

## 2. Line-by-line review

### 2.1 Guard placement — runtime, not argparse (sound)

`freeze()` (351) calls `scope_guard(target)` as its **first statement** — a runtime guard, not an
`argparse` `type=`/`action`. `scope_guard` (243) resolves the target and `corpus/fixtures` and
`relative_to`-tests containment, refusing both escapes and the scope root itself (empty `parts`).
Rationale visible in the code: a distinct, pinned finding id (`SCOPE-REFUSED`) and resolve-based
semantics; argparse placement could not emit that id without an `ArgumentTypeError`-to-`ToolError`
shim, and would report `INVALID-ARGUMENTS` instead. Exit contract unaffected (both exit 2), and the
argparse-layer mutual-exclusion check in `main()` (`--freeze` + fixture → `INVALID-ARGUMENTS`) is
unchanged. No-write on refusal is structural (nothing before the guard writes) and measured:

```
$ hash-before: 20fbefce…  (fakerepo, path-less-pin refusal)
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin
  r95-crossing-aftermath already names None; freezing a same-named path elsewhere would
  rewrite the delivered pin
RESULT ERROR  exit=2
$ hash-after:  20fbefce…  (unchanged)
```

Guard bypass attempts (all in a **fakerepo** mirror of the repo, so the delivered contract was
never at risk):

```
$ --freeze elsewhere/r95-crossing-aftermath
FINDING SCOPE-REFUSED: … resolves to …/fakerepo/elsewhere/r95-crossing-aftermath … exit=2
$ --freeze corpus/fixtures/../../elsewhere/r95-crossing-aftermath        # traversal
FINDING SCOPE-REFUSED: … resolves to …/fakerepo/elsewhere/r95-crossing-aftermath … exit=2
$ --freeze corpus/fixtures/lnk-foreign                                  # symlink in-scope -> outside
FINDING SCOPE-REFUSED: … (resolves to …/fakerepo/elsewhere/r95-crossing-aftermath) … exit=2
$ --freeze corpus/fixtures
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**  exit=2
$ --freeze corpus/fixtures/does-not-exist
FINDING FIXTURE-MISSING: fixture directory not found: corpus/fixtures/does-not-exist  exit=2
$ --freeze corpus/fixtures/alt/r95-crossing-aftermath                   # same-named shadow, in scope
FINDING SCOPE-REFUSED: … pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath' … exit=2
$ --freeze corpus/fixtures/r95-crossing-aftermath                       # the accept path, in the mirror
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1 … RESULT PASS exit=0
```

### 2.2 PATH-MISMATCH precedence vs DIGEST-MISMATCH — deterministic, but `precedence` was not updated (D2)

`verify()` (320) order is now: pin lookup by resolved basename (`UNPINNED-FIXTURE`) → pin
self-validation (`CONTRACT-INVALID`) → **fixture existence** (`FIXTURE-MISSING`, a new early check)
→ **path binding** (`PATH-MISMATCH`, 290) → semantic inventory findings (exit 1) → digest
(`DIGEST-MISMATCH`, exit 2). Measured end-to-end:

| probe (real tree) | observed |
|---|---|
| foreign byte-identical copy of r96 | `FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …/corpus/fixtures/r96-crossing-response); invoked fixture resolves to …/V11-scratch/foreign/r96-crossing-response` → exit 2 |
| foreign **tampered** copy (path + digest both wrong) | `PATH-MISMATCH` only → exit 2 (path binding wins over digest) |
| tamper **at the pinned path** (fakerepo, re-indented `sources.json`) | `DIGEST-MISMATCH … changed: sources.json (sha256 fd9e30e8… -> 107520e7…)` → exit 2 |
| semantic reduction **plus** byte change at the pinned path (fakerepo) | `REDUCTION-DETECTED` only → exit 1 (findings still win, unchanged) |
| pinned file **removed** at the pinned path (fakerepo) | `DIGEST-MISMATCH … changed: sources.json (sha256 fd9e30e8… -> None)` → exit 2 |
| pin key/path mismatch (key `r95-crossing-aftermath`, path `…/alt-name`, fakerepo) | `PATH-MISMATCH` → exit 2 (fail-closed) |

**Defect D2 (low, documentation):** the contract's `precedence` field is byte-unchanged —
`"semantic inventory findings decide first (exit 1); a content digest change the frozen inventory
does not model exits 2"` — and mentions neither `SCOPE-REFUSED` nor `PATH-MISMATCH`, so the order
the seat brief asks about is not stated where the tool documents its own contract. The `scope`
field *does* name both ids (`… --freeze is scope-guarded to corpus/fixtures/** and every pin
records the fixture's repo-relative path, which verification enforces (SCOPE-REFUSED /
PATH-MISMATCH)`), and `provenance_note` documents the rest; only the ordering sentence is stale.
Impact: none on behavior (order is deterministic and probe-proven above); it is a doc-parity gap in
R3's own owned file.

### 2.3 Pin schema migration path-less → path-ful (D1)

`validate_pin` (256) now **requires** `pin["fixture"]` to be a non-empty, non-absolute,
repo-relative path resolving inside `corpus/fixtures/**`; otherwise `CONTRACT-INVALID`. The
schema uses the pre-existing `fixture` field (no new key), so no pin *shape* change was needed for
the four delivered pins — all four already carried it. Legacy (path-less) pins fail closed:

```
$ (fakerepo: del pins["r95-crossing-aftermath"]["fixture"]) ; verify corpus/fixtures/r95-crossing-aftermath
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path  exit=2
```

**Defect D1 (low, fail-closed):** such a pin can also **not be migrated by re-freezing in place** —
`freeze()`'s existing-pin check compares `existing.get("fixture") != fixture_label`, so `None` never
matches and the correct in-scope path is refused (`SCOPE-REFUSED … already names None`, quoted in
§2.1). The migration route for a path-less pin is therefore a manual contract edit (or pin
deletion), not a tool operation. Impact: none on the delivered contract (no path-less pins), and
the failure is closed, not silent; but the round's own migration story is incomplete. A
`existing.get("fixture") in (None, fixture_label)` relaxation (or a dedicated `CONTRACT-INVALID`
message on freeze) would close it.

### 2.4 `--freeze` refresh path safety

Order inside `freeze()` (351): `scope_guard` → `build_model` (so a malformed target cannot corrupt
the contract) → resolved label → same-named-different-path refusal → `validate_pin` on the new pin
→ only then `CONTRACT_PATH.write_text(...)`. The refresh preserves the whole parsed contract
(mirror test after an accepted freeze: all 11 top-level keys present, `self_test` still 16,
`provenance_note` intact), and `freeze()` now returns the post-write `verify(...)` exit code
instead of a hardcoded 0. Residuals (both pre-existing or cosmetic): the write is a non-atomic
`write_text` (O6), and the writer's `indent=2` reformatted the whole delivered contract (O6).
Measured refresh result, independently reproduced against the delivered contract:

- `pins.r88/r94/r95`: byte-identical; `pins.r96-crossing-response`: only `revision`
  `60dba0c2… -> 2393934…`; `content_sha256` still `d422a9b3…`, `files/events/relations/counts/fixture`
  unchanged; top-level `revision` → `2393934…`; pins 4 → 4.

The r96 re-freeze therefore **cannot** show a digest move: R4's cosmetic repair touched only
`claim-excerpt-map.md`, which is not in `DATA_FILES`. R3 records exactly this as a claim
discrepancy (its report's "Recorded discrepancy"); I confirm it independently (O3).

### 2.5 Self-test redesign (14 → 16) — genuine strengthening, no weakening found

`self_test_cases` (390) now builds a per-case **mirror root** under the harness tempdir:
`corpus/tools/dependency_freeze.py` (a `copy2` of the running tool) + `corpus/tools/dependency-freeze-contract.json`
(a `copy2` of the delivered contract) + `corpus/fixtures/<pinned basename>` (the case fixture). The
14 legacy mutation cases run the *mirror* tool in a subprocess, so the fixture path still equals
the pin's repo-relative path inside that mirror and strict binding holds while the semantic cases
stay reachable. Checks I made against a possible weakening:

- the mirror contract is a **byte copy of the delivered contract**, and the harness reads the
  persisted expectations from the delivered contract itself — the pinned expectations are the
  delivered ones, exercised against a faithful copy;
- `clean`, `invalid_arguments`, `path_mismatch` and `scope_refused` use the **real** tool against
  the real contract/tree, so the new classes are pinned end-to-end;
- `digest_tamper` still reaches `DIGEST-MISMATCH` because the tamper is applied at the pinned path
  *inside the mirror* — the case was not weakened to a path check;
- no case writes the real contract (hash unchanged across two full runs, below).

`run_self_test` (504) now uses `TemporaryDirectory(prefix=…, dir=ROOT)` instead of the system temp
dir. With `/tmp` inode-exhausted this round (`df -i /tmp` → `IUsed 1048576 / IFree 0 / IUse% 100`,
independently confirmed), the old harness failed with `OSError: [Errno 28]`; the delivered harness
passes both with and without a `TMPDIR` override (O8). Trade-off: the harness now needs a writable
repo root, and the r94 BR-05 residual (scratch under the repo root, not gitignored) is unchanged.

## 3. End-state evidence (final hashes)

```
$ python3 corpus/tools/dependency_freeze.py --self-test          # default TMPDIR; /tmp exhausted
CASE clean … ok   … CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS   exit=0

$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f | tail -2; done
r88 … DIGEST 15ef230e… RESULT PASS ; r94 … DIGEST 2527beb9… RESULT PASS ;
r95 … DIGEST d541ae64… RESULT PASS ; r96 … DIGEST d422a9b3… RESULT PASS        # chain 4/4 clean

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' in
  corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster',
  'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])   exit=2   (by declaration)

$ contract hash before self-test: 27273be2… ; after: 27273be2…   -> NO-WRITE by the self-test
$ ls -d dependency-freeze-self-test-*   -> no stray self-test dirs
$ python3 -m py_compile corpus/tools/dependency_freeze.py   -> OK
```

Symlink identity semantics (fakerepo, both directions): a symlink *inside* the scope pointing at
the pinned fixture verifies `RESULT PASS exit=0`; a symlink inside the scope pointing outside is
refused. Binding is by resolved path identity, not lexical path (O4).

## 4. Defects by severity

| id | severity | defect | evidence | impact |
|---|---|---|---|---|
| D1 | low (fail-closed) | A path-less (legacy) pin cannot be refreshed in place: `--freeze` on its correct in-scope path exits 2 `SCOPE-REFUSED … already names None`; verify exits 2 `CONTRACT-INVALID`. Migration requires a manual contract edit. | §2.3 quotes; fakerepo probes G4/G5 | none on the delivered contract (all 4 pins path-ful); no silent pass |
| D2 | low (documentation) | Contract `precedence` left unchanged: does not state the new exit-2 order (existence → path binding) nor name `SCOPE-REFUSED`/`PATH-MISMATCH`; the order is only in code and in the `scope`/`provenance_note` text. | §2.2 quotes; `grep` of the field | none on behavior; doc-parity gap in R3's owned file |

No high/medium defects found; no fail-open path found in any probe (each refusal exits 2 with a
stable finding id and writes nothing).

**Observations (not defects):** O1 README (`corpus/tools/README.md`, R2-owned) still carries the
r96 text — `grep -c PATH-MISMATCH` → `0`, self-test "14/14", the three hazards listed as open; R3
self-reports this as an open doc-parity item outside its byte-ownership. O2 `r97-crossing-acknowledgment`
is not pinned (4-pin chain by declaration; `UNPINNED-FIXTURE` exit 2), a candidate for r98.
O3 the r96 pin refresh moved only `revision`; the claim's "digest changes by the repair"
parenthetical is inaccurate (independently confirmed; R3 records the discrepancy). O4 resolved-path
identity: symlink-to-pinned verifies PASS, symlink-escaping is refused. O5 a copied tool+contract
rooted elsewhere still verifies copies (binding is to the running tool's `ROOT`) — inherent scope
limit, stated by R3. O6 contract write is non-atomic `write_text` (pre-existing) and the `indent=2`
writer reformatted the delivered contract 1→2 spaces (content-preserving; field-by-field verified).
O7 `schema_version` stayed `1` although the pin schema tightened (a bump would make the tightening
visible). O8 self-test harness now needs a writable repo root instead of `TMPDIR`; works despite
`/tmp` inode exhaustion; BR-05 residual unchanged; no stray dirs. O9 probe hygiene: I removed the
`.pyc` my `py_compile` created under the gitignored `corpus/tools/__pycache__/`; no other live-tree
write.

## 5. Write audit

```
$ git status --porcelain
 M LOG.md                                   # round declaration (pre-seat)
 M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md   # R4 cosmetic repair (2 insertions/2 deletions)
 M corpus/tools/README.md                   # R2
 M corpus/tools/dependency-freeze-contract.json   # R3 (+ R4's guarded re-freeze)
 M corpus/tools/dependency_freeze.py        # R3
 M corpus/tools/map-obligations-contract.json     # R2
 M corpus/tools/map_obligations.py          # R1
?? .ufo/waves/round-97/                     # seat reports/scratch
?? corpus/fixtures/r97-crossing-acknowledgment/  # R4/R5
?? corpus/knowledge/r97-acknowledgment-scope-note.md  # R6
$ git diff --stat f3e09f9 -- corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r94-paired-crossing \
    corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response
 corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | 4 ++--   (R4's declared repair; JSON tables untouched)
```

All V11 writes are under `.ufo/waves/round-97/seats/V11-scratch/` (baseline snapshots, fakerepo
mirrors, probe drivers) plus this report; the delivered tool/contract hashes were `b06275f3…` /
`27273be2…` before and after every probe.

## Bottom line

**PASS** — R3's `dependency_freeze` hardening is delivered as claimed on the final revision
(`b06275f3…` / `27273be2…`): runtime scope guard with no-write refusals (traversal, symlink,
scope-root, same-named shadow all `SCOPE-REFUSED` exit 2), resolve-based pin path binding that turns
the r96 shadow-copy trick into `PATH-MISMATCH` exit 2 ahead of the digest check, `DIGEST-MISMATCH`
naming the changed file (including removals as `-> None`), self-test 14→16 with a faithful
mirror-root harness and no real-contract writes, chain 4/4 clean, semantic-first precedence intact;
two low-severity fail-closed defects reported (D1 path-less pins cannot be refreshed in place, D2
the contract's `precedence` field was not updated) and one out-of-ownership doc gap (README, R2).

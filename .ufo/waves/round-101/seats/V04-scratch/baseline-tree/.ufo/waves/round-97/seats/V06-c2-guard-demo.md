# V06 — c2-guard-demo (round 97, single-wave)

- Seat: V06 `c2-guard-demo` (leaf, verifier). Mandate: **C2 — `dependency_freeze` hardening.**
  Scope guard demo (`--freeze` outside `corpus/fixtures/**` → exit 2, stable FINDING quoted),
  the in-scope `--freeze` path (via self-test case + code path, per seat instructions), and
  confirmation that the real r96 refresh through the guarded path succeeded — with an exact
  statement of what was and was not exercised.
- Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`; every command below ran from there
  with `python3` (the session cwd is the parent repo — no relative-path writes were made from it).
- Baseline: r96 closure `f3e09f9` (worktree HEAD `2393934`, the r96 SCORECARD closure commit).
- Writes by this seat: this report + `.ufo/waves/round-97/seats/V06-scratch/**` (absolute paths,
  verified to resolve under `lore-shokunin/`). **No producer-owned bytes were written by this
  seat.** The real contract was sha256-checked before/after every probe that could have touched it.

## 0. Poll record (20 s cadence; never verified a plan)

- 18:42 — poll started (`V06-scratch`, background loop, 40 tries). Baseline on disk: tool
  `a3b57978…` (= `git show f3e09f9:corpus/tools/dependency_freeze.py`), contract `c65ac3bd…`;
  R3 report absent.
- 18:52 — mid-flight tool bytes sampled but **not credited** (mtime 18:52:21; guard ids visible).
- 18:53:00 tool mtime advances (25044 bytes), 18:53:21 contract mtime advances (9445 bytes);
  `R3-scratch/` appears.
- 18:56 — `R3-freeze-hardening.md` present; revision credited. No ABSENT condition arose.

## 1. Credited revision (hashed at report time)

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
```

Both hashes are byte-identical to the ones R3's report claims for its delivered revision. All
measurements below ran on these bytes; `git status --porcelain` shows both files modified (uncommitted),
`git log --oneline -1` → `2393934 lore r96: close round — SCORECARD admitted section`.

## 2. Before-state (baseline tool, reproduced independently in sandboxes — real contract untouched)

Sandbox `V06-scratch/sandbox-baseline/` = copy of the `f3e09f9` tool + contract + `r96-crossing-response`
copy, plus a byte-identical same-named copy at a foreign path.

- **(b) hazard — foreign same-named copy verifies identically (old tool):**
  `python3 corpus/tools/dependency_freeze.py $SC/sandbox-baseline/foreign/r96-crossing-response`
  → `FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1` /
  `DIGEST d422a9b3…` / `RESULT PASS` / `EXIT=0`.
- **(a) hazard — `--freeze` accepts an out-of-scope path (old tool, sandbox contract):**
  `--freeze $SC/sandbox-baseline/rogue-fixture` → `FROZEN rogue-fixture: …` / `RESULT PASS` / `EXIT=0`;
  the sandbox contract then contains `pins['rogue-fixture']` with an **absolute** `fixture` label.
  (This is the V41 breach class, reproduced safely in a sandbox — the real contract was never at risk.)
- Baseline self-test on the real tree at 18:44: `SELF-TEST 14/14 / RESULT PASS / EXIT=0`.

Independent corroboration of the same before-state landed from V45's seat (`V45-c2-guard-2.md`
§B-A/B-B/B-C); our captures agree.

## 3. After-state — battery on the delivered revision

All commands quoted with observed output. Scratch root `$SC = .ufo/waves/round-97/seats/V06-scratch`
(absolute path in the real runs).

### B1. Self-test 16/16 (both TMPDIR modes)

```
$ TMPDIR=$SC/tmp python3 corpus/tools/dependency_freeze.py --self-test
… 14 legacy cases ok …
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS            EXIT=0
```

The default-TMPDIR run also returned `SELF-TEST 16/16 / RESULT PASS / EXIT=0`. Host note: `/tmp` was
inode-exhausted this round (`df -i /tmp` → `IUsed 1048576 / IFree 1 / IUse% 100`); the baseline tool
crashed its self-test under default TMPDIR (`OSError: [Errno 28] No space left on device:
'/tmp/dependency-freeze-self-test-sh0jw1kh/reduction_edge_drop'`, exit 1) while the delivered harness
uses `tempfile.TemporaryDirectory(..., dir=ROOT)` (`dependency_freeze.py:517`) and is therefore
**independent of /tmp**. This is a host condition, not a tool finding. No stray self-test dirs remain
(`ls -d dependency-freeze-self-test-*` → none).

### B2. Real scope guard — `--freeze` on a scratch dir outside `corpus/fixtures/**`

```
$ python3 corpus/tools/dependency_freeze.py --freeze $SC/foreign-target
FINDING SCOPE-REFUSED: --freeze refuses /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V06-scratch/foreign-target (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V06-scratch/foreign-target); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
EXIT=2
contract sha before=27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781 after=27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
NO-WRITE: OK
```

`$SC/foreign-target` held a full copy of the r96 fixture, so absent the guard this exact invocation
would have frozen successfully (as the old tool did in §2). The contract sha is unchanged → the
refusal is fail-closed with **no write**. A backup of the contract was kept at
`$SC/contract-backup-pre-probe.json` in case restoration had been needed; it was not.

### B3. Sandbox mirror battery (delivered tool + contract + fixture at the pinned repo-relative path)

Sandbox `$SC/sandbox-r97/repo/` = copy of the delivered tool + delivered contract + an in-scope copy
of `r96-crossing-response`; `$SC/sandbox-r97/foreign/` holds a byte-identical same-named copy.

- **B3a in-scope verify → 0:** `FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4;
  relations 1/1` / `DIGEST d422a9b3…` / `RESULT PASS` / `EXIT=0`.
- **B3b foreign same-named copy → 2 PATH-MISMATCH:**
  ```
  FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …/sandbox-r97/repo/corpus/fixtures/r96-crossing-response); invoked fixture resolves to …/sandbox-r97/foreign/r96-crossing-response
  RESULT ERROR   EXIT=2
  ```
  This is the exact r96 trick path, now red.
- **B3c sandbox `--freeze` foreign → 2 SCOPE-REFUSED, sandbox contract sha unchanged
  (27273be2… before = after).**
- **B3d sandbox `--freeze` in-scope → 0, works:** `FROZEN r96-crossing-response: events 5; …` then
  the post-freeze verify `RESULT PASS / EXIT=0`; a following plain verify also `RESULT PASS / EXIT=0`.
- **B3e digest tamper (timeline text drift, inventory-neutral) → 2, names the file:**
  ```
  FINDING DIGEST-MISMATCH: content digest daeb21fd… != pin d422a9b3…; changed: timeline.json (sha256 ea0225f9… -> be77a509…); fixture bytes changed outside the frozen inventory
  RESULT ERROR   EXIT=2
  ```
- **B6 symlink escape (sandbox `corpus/fixtures/evil-link` → `/etc`) → 2:**
  `FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/evil-link (resolves to /etc); …`
- **B7 same-named in-scope shadow freeze (sandbox `corpus/fixtures/shadow/r96-crossing-response`) → 2:**
  `FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/shadow/r96-crossing-response: pin
  r96-crossing-response already names 'corpus/fixtures/r96-crossing-response'; freezing a same-named
  path elsewhere would rewrite the delivered pin`

### B4. Real chain, read-only (delivered tool, delivered contract)

```
r88-m3-maya-cluster    RESULT PASS exit 0  (15ef230e…)
r94-paired-crossing    RESULT PASS exit 0  (2527beb9…)
r95-crossing-aftermath RESULT PASS exit 0  (d541ae64…)
r96-crossing-response  RESULT PASS exit 0  (d422a9b3…)
```

### B5. Contract post-state (delivered)

`pins` = the same four declared fixtures (no foreign pin, no `r97-crossing-acknowledgment` pin);
`self_test.expected` has exactly 16 cases with `scope_refused: {exit: 2, finding_ids: ['SCOPE-REFUSED']}`
and `path_mismatch: {exit: 2, finding_ids: ['PATH-MISMATCH']}`; `pins['r96-crossing-response']` =
`fixture: corpus/fixtures/r96-crossing-response`, `revision: 2393934…`, `content_sha256: d422a9b3…`.

### B8. Independent semantic diff of the refresh (R3's pre-freeze copy vs delivered contract)

`json` deep-compare of `.ufo/waves/round-97/seats/R3-scratch/contract-prefreeze.json` vs the delivered
contract → exactly **4 semantic diffs**, all accounted for:

- `/revision` and `/pins/r96-crossing-response/revision`: `60dba0c2…` → `2393934…` (the refresh);
- `/scope` and `/provenance_note`: doc-text additions describing the r97 guard/binding/digest
  behavior and recording the refresh (quoted in §4).

No other field moved: pin `content_sha256`/`files`/`events`/`relations`/`counts`/`fixture` unchanged
for all four pins; pins count 4 → 4.

## 4. Code-path reading (delivered revision, `corpus/tools/dependency_freeze.py`)

- Guard: `scope_guard()` at lines 243–253 — resolves the target and requires it strictly inside
  `ROOT/corpus/fixtures` (`SCOPE-REFUSED` otherwise; `corpus/fixtures` itself refused); called first
  in `freeze()` (line 352), i.e. **before** `build_model` and before the only write
  (`CONTRACT_PATH.write_text`, line 382). Symlinks are neutralized by `.resolve()`.
- Pin path validation: `validate_pin()` lines 259–267 — `fixture` must be a non-absolute repo-relative
  path resolving inside `corpus/fixtures/**` (`CONTRACT-INVALID` otherwise).
- Binding: `bind_path()` lines 290–296 — verify requires the invoked fixture to resolve to
  `ROOT/pin['fixture']` (`PATH-MISMATCH`), called at line 324 before any receipt is printed.
- Digest naming: `changed_files()` lines 308–317, consumed at line 342.
- Same-named in-scope shadow refusal: lines 358–362 (extra fail-closed beyond the four enumerated
  items; reported under the pinned `SCOPE-REFUSED` id).
- Post-freeze verify exit propagation: line 387 (`return verify(target, read_contract())`).
- Self-test: `FROZEN_CASES` = 16 (lines 40–57); `scope_refused` case runs the **real** tool with the
  **real** contract against a temp target under `ROOT` (lines 498–500) — refused pre-write, so the
  case cannot pollute the contract; `path_mismatch` case (lines 494–496) verifies a foreign copy.
  Legacy mutation cases now run inside per-case mirror roots (lines 394–405) so strict binding still
  exercises the real CLI.

## 5. Real refresh through the guarded path — what is confirmed and how

R3's transcript (quoted from `R3-freeze-hardening.md`):

```
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r96-crossing-response
FROZEN r96-crossing-response: events 5; dependency-edges 4; relations 1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
exit=0
```

Independently confirmed by this seat from the post-state: the r96 pin carries `revision 2393934…`
(HEAD at refresh time) and `fixture corpus/fixtures/r96-crossing-response`; my B8 diff shows the only
pin-field change is that revision; B4 verifies the refreshed pin green; B2/B3d prove the guarded
`--freeze` path itself accepts in-scope targets and refuses out-of-scope ones with no write. I did
**not** re-run the real refresh (it would rewrite the producer-owned contract); the invocation
transcript is R3's, and the resulting state is independently consistent with it.

**Recorded claim-vs-measurement discrepancy (confirms R3's own disclosure):** the r97 declaration
says the pin refresh follows from "the digest changes by the repair". Measured, it does not: the
repair touched `claim-excerpt-map.md`, which is not one of `DATA_FILES`, so `content_sha256` stayed
`d422a9b3…` and only the `revision` fields moved. The refresh is real (through the guarded path), but
the digest-change parenthetical in the claim is inaccurate. R3 records the same; my B8 diff confirms.

## 6. Exactly what was exercised — and what was not

**Exercised on the delivered revision:** real `--self-test` (16/16, both TMPDIR modes); real
`--freeze` on an out-of-scope scratch target (exit 2 `SCOPE-REFUSED`, contract sha before = after →
no write); real read-only verify of all four chain fixtures (4/4 PASS); sandboxed `--freeze`
(in-scope works; foreign refused; symlink escape refused; same-named in-scope shadow refused),
sandboxed PATH-MISMATCH on a byte-identical foreign same-named copy, sandboxed digest-naming;
full code-path read of guard/binding/naming/self-test wiring; independent semantic diff of the
refresh.

**Not exercised / by design not done:** I never wrote foreign fixtures into the real
`corpus/fixtures/` and never ran `--freeze` against a real in-scope target (per seat instructions —
the real refresh is credited from R3's transcript + post-state, not re-run). Symlink and shadow
refusals were demonstrated only in the mirror sandbox. The in-scope `--freeze` write path on the
real contract is proven by the self-test's `clean`/`path_mismatch` mirror harness and by R3's real
refresh, not by a fresh in-scope freeze by this seat. The README doc-parity gap for the new ids
(R3 residual #1) is outside this seat's scope and was not assessed here.

## Bottom line

**PASS** — on the delivered revision (`b06275f3…` / `27273be2…`, matching R3's report): `--freeze`
outside `corpus/fixtures/**` exits 2 with the stable `SCOPE-REFUSED` finding and provably writes
nothing (contract sha unchanged), the in-scope freeze path works (self-test case + mirror demo +
R3's real r96 refresh, whose post-state I independently diffed), the foreign same-named copy that
verified identically at baseline now exits 2 `PATH-MISMATCH`, `DIGEST-MISMATCH` names the changed
file, self-test is 16/16 (host-/tmp-independent), chain verifies 4/4 — with the one recorded
claim-text inaccuracy that R4's repair did not change the r96 content digest (revision-only refresh).

# V07 c2-path-binding — round 97 seat report

- Seat: V07 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; HEAD at test time `2393934…`. All commands run from the lane repo root with `python3`.
- Tested revision: `dependency_freeze.py` sha256 `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`; `dependency-freeze-contract.json` sha256 `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781` — both match R3's declared delivered revisions (`R3-freeze-hardening.md` line 5) and were stable across my entire battery.
- Writes: only `.ufo/waves/round-97/seats/V07-scratch/**` (foreign copies, mirror root, captured outputs) plus this report. No commits, no pushes, no network. The delivered `r94-paired-crossing` fixture is untouched by the round (absent from `git status`; my foreign copy `diff -r`-identical to it).

## Poll log (protocol: 20 s cadence)

- Tries 1–25 (through 18:51:13): R3 not ready — report absent, no `PATH-MISMATCH` token in the tool, contract still 14 self-test cases.
- Try 26 (18:51:33): `PATH-MISMATCH` token appears in the tool (R3 actively writing; tool mtime 18:53:00).
- Try 32 (18:53:33): contract reaches 16 self-test cases (mtime 18:55:14 for R3's final touch).
- Report found 18:56:26: `R3-freeze-hardening.md`. Verification began after this, on the hash-stable delivery. Never verified a plan; no fabrication.
- Pre-R3 baseline captured at 18:46 with tool sha `a3b57978…` (HEAD bytes) — see A.

## Primary checks (seat demand)

**A. Foreign same-named byte-identical copy → exit 2 PATH-MISMATCH.**

```
$ diff -r corpus/fixtures/r94-paired-crossing .ufo/waves/round-97/seats/V07-scratch/foreign/r94-paired-crossing
(diff -r: IDENTICAL)
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V07-scratch/foreign/r94-paired-crossing
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V07-scratch/foreign/r94-paired-crossing
RESULT ERROR
exit=2
```

Same copy, pre-R3 tool (`a3b57978…`, captured 18:46 before any R3 edit) — the hazard, reproduced independently of R3's own probe:

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V07-scratch/foreign/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
exit=0
```

**B. Delivered `corpus/fixtures/` path → clean.**

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
exit=0
```

**C. Pin file records repo-relative paths for all four fixtures** (not leading `/`, no `..`, equals canonical, directory exists):

```
r88-m3-maya-cluster: fixture='corpus/fixtures/r88-m3-maya-cluster' relpath=True equals_canonical=True dir_exists=True
r94-paired-crossing: fixture='corpus/fixtures/r94-paired-crossing' relpath=True equals_canonical=True dir_exists=True
r95-crossing-aftermath: fixture='corpus/fixtures/r95-crossing-aftermath' relpath=True equals_canonical=True dir_exists=True
r96-crossing-response: fixture='corpus/fixtures/r96-crossing-response' relpath=True equals_canonical=True dir_exists=True
```

## Secondary probes (cheap, labelled extras)

- **D — no false positives on equivalent invocation spellings** (each `RESULT PASS`, `exit=0`): absolute path; trailing slash; `corpus/fixtures/../fixtures/r94-paired-crossing`; bare `r94-paired-crossing` invoked from `cwd=corpus/fixtures`. Binding is resolution-based, not string-based.
- **E — control, differently-named copy** → `FINDING UNPINNED-FIXTURE: no pin for 'r94-paired-crossing-copy' … RESULT ERROR exit=2` (name lookup unchanged).
- **F — chain 4/4 clean**: r88 `PASS`, r94 `PASS` (digest `2527beb9…`), r95 `PASS` (`d541ae64…`), r96 `PASS` (`d422a9b3…`), all exit 0.
- **G — self-test 16/16**: `SELF-TEST 16/16`, `RESULT PASS`, exit 0; contract `self_test.expected` has 16 cases including `path_mismatch -> {'exit': 2, 'finding_ids': ['PATH-MISMATCH'], 'forbid_traceback': True}` and `scope_refused -> {'exit': 2, 'finding_ids': ['SCOPE-REFUSED'], …}`. No stray `dependency-freeze-self-test-*` left by my run.
- **H — pin-path loader validation (mirror root in my scratch, delivered contract never at risk)**: H0 unmodified mirror control `PASS`; H1 pin `fixture` set to an absolute path → `FINDING CONTRACT-INVALID: pin r94-paired-crossing needs a repo-relative fixture path`, exit 2; H2 pin `fixture='corpus/tools/dependency_freeze.py'` → `FINDING CONTRACT-INVALID: pin r94-paired-crossing names corpus/tools/dependency_freeze.py, outside corpus/fixtures/**`, exit 2.
- **H3 — symlink alias to the delivered fixture** → `RESULT PASS exit=0`: identity semantics (a path that *is* the pinned fixture by resolution passes); a foreign path that resolves elsewhere mismatches. Observation, not a defect.
- **H4 — foreign copy via relative invocation from its own directory** → same `PATH-MISMATCH` finding, exit 2 (binding holds under any invocation spelling).
- **I2 — precedence**: same-named copy at a foreign parent with a mutated `timeline.json` (prose change invisible to the inventory) → `PATH-MISMATCH exit=2`, i.e. binding decides before digest comparison.

## Stability and boundary notes

- Tool and contract sha256 re-checked after the full battery — unchanged; `git status` shows only producer-owned files plus `LOG.md` and untracked round artifacts. A transient `dependency-freeze-self-test-o2h65984/` at repo root (18:57:33) was a concurrent verifier seat's in-flight self-test and was gone by 18:58:06 — cleanup works; not a stray.
- r96 pin refresh is observable in the contract: pin + top-level `revision` updated to `2393934237ea076366f3db6dceeff033edb52ab1`, digest `d422a9b3…` unchanged; my chain check confirms r96 verifies `PASS` on that digest. This corroborates R3's recorded discrepancy (R4's repair touched only `claim-excerpt-map.md`, outside `DATA_FILES`), so the refresh is format/revision-level, not digest-level.
- Out of scope here (other seats): `--freeze` scope-guard internals, `DIGEST-MISMATCH` file naming, self-test harness internals. I witnessed self-test 16/16 and the two new contract expectations only.

## Bottom line

**PASS** — path binding is delivered and load-bearing: the byte-identical foreign same-named r94 copy flipped from `exit 0` (pre-R3 tool `a3b57978…`) to `exit 2 PATH-MISMATCH` (delivered tool `b06275f3…`) naming both resolved paths, the delivered path verifies clean, all four pins record repo-relative paths, and normalization controls show no false positives on equivalent invocation spellings.

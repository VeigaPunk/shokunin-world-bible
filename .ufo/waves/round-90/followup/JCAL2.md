# JCAL2 — Calibration judge #2 (adversarial)

Target: delivered tree at `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (baseline `e97613cc276f5fa9cac49ff1900798cf6863c020`). Checker: `corpus/fixtures/check_bible.py`. Machine receipts: `.ufo/waves/round-90/followup/JCAL2-receipts.json`.

## Work performed

- **Axes judged:** (1) calibration — the delivered checker must say *definite* exactly where the finding is definite and *qualified* exactly where identity is genuinely unresolved; (2) compatibility — zero corpus delta on the 164 delivered outputs and zero exit changes; (3) falsification — construct new attempts to force a false definite or a reappearing vacuous clause.
- **Freeze-then-verify (r88-I1):** composed `X2-c1-nullonly.patch` + `X3-c1-tickonly.patch` onto the git-archived `e97613c` checker with `patch --fuzz=0`. Result: composed bytes **byte-identical** to the delivered file (`cmp` clean; both `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`). No mismatch → no blocking finding on this gate.
- **Census:** ran the delivered checker and the archived `e97613c` checker (`e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`) over all **164** fixture directories using the same repo-relative paths B1's receipt uses, comparing exact `(exit, stdout, stderr)` tuples; cross-checked the 160 pinned dirs against `patches/B1-tuples.json`.
- **Vacuous-clause sweep:** every one of the 164 delivered outputs scanned for the `N raw entity rows carry this id, but only M is in the resolved index` clause, with `N == 0` and `N == M` flagged, plus a scan for any `None is not uniquely resolvable` text.
- **Repaired-shape probes on the delivered checker:** P1 null-chain; P2 unrelated/compared-identity tick; durable r89-fn2 pair. **Two new falsification attempts:** F1 `from_holder` null with the *other* holder genuinely unresolved (must stay qualified via the non-null side); F2 the mirror — an unresolved non-null observed `from_holder` with a clean expected side, with a tick inversion (must stay qualified on the observed side, tick definite). **Controls:** C1 null first record (clean), C2 first-record non-null unresolved (qualified), C3 tick line with an earlier ambiguous *source* in the chain.
- Probe fixtures were built in memory and executed through memfd launchers with `Path.read_text` monkeypatched for a virtual directory (`/jcal2virt`); the same harness was run against the baseline checker bytes for before/after contrast. `/tmp` was at 100 % inode use in this wave (`df -i /tmp`: 1048335 / 1048576 used, 241 free at seat start), so no scratch files were written; 0 scratch inodes consumed.
- No commit, no push. Only writes: this report and `followup/JCAL2-receipts.json`. Untracked sibling artifacts (`H2/H3/H4/JCAL1/JCAL5`) were observed to appear concurrently and were not touched.

## Before → after measurements

### 1. Freeze-then-verify: delivered checker == X2∘X3 on e97613c

```sh
git show e97613c:corpus/fixtures/check_bible.py > /tmp/jcal2/tree/corpus/fixtures/check_bible.py
patch -p1 -d /tmp/jcal2/tree --fuzz=0 -i .ufo/waves/round-90/patches/X2-c1-nullonly.patch
patch -p1 -d /tmp/jcal2/tree --fuzz=0 -i .ufo/waves/round-90/patches/X3-c1-tickonly.patch
sha256sum /tmp/jcal2/tree/corpus/fixtures/check_bible.py corpus/fixtures/check_bible.py
cmp /tmp/jcal2/tree/corpus/fixtures/check_bible.py corpus/fixtures/check_bible.py
```

Observed:

```text
patching file corpus/fixtures/check_bible.py
patching file corpus/fixtures/check_bible.py
Hunk #1 succeeded at 321 (offset 2 lines).
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  /tmp/jcal2/tree/corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
COMPOSED_HASH_MATCH=PASS
```

`baseline_checker_sha256=e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556` (matches X3's recorded baseline hash). The delivered diff `e97613c..ca7f9ef -- corpus/fixtures/check_bible.py` contains exactly the union of the two patches (the null gate at `corpus/fixtures/check_bible.py:168` and the tick-gate removal at `corpus/fixtures/check_bible.py:324`); nothing else.

### 2. Census 164 and pinned-160 receipt check

Command (repo root; exact script body paired with the receipt check and sweep in the same run):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, json, os, subprocess, sys
root = Path.cwd()
delivered = root/'corpus/fixtures/check_bible.py'
baseline = Path('/tmp/jcal2/base.py')          # git show e97613c:corpus/fixtures/check_bible.py
receipt = json.loads((root/'.ufo/waves/round-90/patches/B1-tuples.json').read_text())
dirs = sorted(p for p in (root/'corpus/fixtures').iterdir() if p.is_dir())
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
def run(script, rel):
    r = subprocess.run([sys.executable, str(script), rel], cwd=root, capture_output=True, env=env)
    return r.returncode, r.stdout, r.stderr
rels = [f'corpus/fixtures/{d.name}' for d in dirs]
base_runs = {r: run(baseline, r) for r in rels}
deliv_runs = {r: run(delivered, r) for r in rels}
print('changed_tuples=', [r for r in rels if base_runs[r] != deliv_runs[r]])
print('exit_flips=', [r for r in rels if base_runs[r][0] != deliv_runs[r][0]])
shared = sorted(r for r in rels if r in receipt)
print('pinned_shared=', len(shared), 'mismatches=', [r for r in shared if (deliv_runs[r][0],
      hashlib.sha256(deliv_runs[r][1]).hexdigest(),
      sum(l.startswith(b'VIOLATION:') for l in deliv_runs[r][1].splitlines())) !=
      (receipt[r]['exit'], receipt[r]['stdout_sha256'], receipt[r]['violation_count'])])
print('new_since_baseline=', sorted(set(rels)-set(receipt)))
PY
```

Observed:

```text
delivered_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
baseline_sha256=e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
baseline_tree_stats(exit,viol,stderr): ({1: 132, 0: 32}, 417, [])
delivered_tree_stats(exit,viol,stderr): ({1: 132, 0: 32}, 417, [])
changed_tuples_all164=0 []
exit_flips_all164=0 []
pinned_shared=160 receipt_mismatches=0 []
new_since_baseline=4 ['r90-c1-rawpresent-from', 'r90-c1-rawpresent-source', 'r90-c1-rawpresent-to', 'r90-c1-three-causes']
  r90-c1-rawpresent-from: exit 1->1 violations 5->5 stdout_same=True
  r90-c1-rawpresent-source: exit 1->1 violations 4->4 stdout_same=True
  r90-c1-rawpresent-to: exit 1->1 violations 5->5 stdout_same=True
  r90-c1-three-causes: exit 1->1 violations 4->4 stdout_same=True
```

417 = 399 pinned violation lines + 18 from the four new fixtures; 32 clean / 132 violation exits on the delivered corpus; stderr empty everywhere.

### 3. Vacuous-clause sweep over all 164 delivered outputs

Same run, on the delivered stdout of every directory:

```text
vacuous_0raw0indexed=0 []
zero_raw_anywhere=0 []
raw_equals_indexed_clauses=0 []
"None is not uniquely resolvable" outputs=0 []
total_unresolvable_clauses=1     # r89-fn2-unresolved-chain-break: "2 raw ... 1 ... resolved index" (non-vacuous, correct)
```

### 4. Repaired-shape probes (delivered vs baseline, same fixtures)

Harness (`SOURCE`/`PAYLOAD` substituted per run, executed as `python3 /proc/self/fd/<memfd> /jcal2virt`):

```python
import contextlib, io, json, sys
from pathlib import Path
_data = PAYLOAD
_orig = Path.read_text
def _rt(self, *a, **k):
    if str(self.parent) == '/jcal2virt' and self.name in _data:
        return json.dumps(_data[self.name])
    return _orig(self, *a, **k)
Path.read_text = _rt
_buf = io.StringIO(); sys.argv = ['check_bible.py', '/jcal2virt']; _code = 0
try:
    with contextlib.redirect_stdout(_buf):
        exec(compile(SOURCE, 'check_bible.py', 'exec'), {'__name__': '__main__'})
except SystemExit as exc:
    _code = exc.code or 0
sys.stdout.write(_buf.getvalue()); sys.exit(_code)
```

**P1 `null-chain`** (item `seal` provenance: `tick 2 → mira`, then `tick 1, from_holder null → harbor`):

```text
--- BASELINE (e97613c) exit=1
VIOLATION: entities[2].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index); provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[2].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
--- DELIVERED (ca7f9ef) exit=1
VIOLATION: entities[2].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[2].provenance[1]: provenance chain break; expected from_holder 'mira', got None
```

**P2 `unresolved-compared-holder-tick`** (previous holder `uncertain-holder` raw 2 / indexed 1 — genuinely unresolved — and a tick inversion with a clean observed holder `mira`):

```text
--- BASELINE exit=1
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'uncertain-holder' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'uncertain-holder' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
--- DELIVERED exit=1
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[3].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'uncertain-holder' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
```

**Durable r89-fn2 pair (unchanged by the delivered checker):**

```sh
python3 /tmp/jcal2/base.py corpus/fixtures/r89-fn2-unresolved-chain-break   # and the delivered checker, same path
python3 /tmp/jcal2/base.py corpus/fixtures/r89-fn2-control
```

```text
r89-fn2-unresolved-chain-break: exit 1->1 stdout_identical=True stderr_both_empty=True sha256_delivered=66ed1438c6d1af003492d29569492ec0990e5b01b041fba1b4e21147eab4327a
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
r89-fn2-control: exit 1->1 stdout_identical=True stderr_both_empty=True sha256_delivered=4283f6955f40d49f6036ad61f55ab94e682cdb3c475af73c3d8350920cf06951
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'
```

### 5. New falsification attempts (F1, F2) and controls (C1–C3)

**F1** — `null from_holder` with the OTHER holder genuinely unresolved (`rdup` raw 2 / indexed 1 as the previous `to_holder`); record 2 also inverts the tick (`tick 1` after `tick 1`):

```text
--- BASELINE exit=1
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[3].provenance[1].tick: ... holder identity is not uniquely resolvable: expected from_holder 'rdup' ... ; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index); provenance tick 1 must be greater than previous tick 1
VIOLATION: entities[3].provenance[1]: ... possible provenance chain break, not a definite identity mismatch: expected from_holder 'rdup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
--- DELIVERED exit=1
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[3].provenance[1].tick: provenance tick 1 must be greater than previous tick 1
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'rdup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got None
```

F1 does **not** falsify: the null side no longer injects a vacuous clause, the non-null side still governs qualification, and the tick finding is definite.

**F2** — mirror: clean expected holder `mira`, unresolved non-null observed `from_holder` `rdup`, tick inversion (`tick 1` after `tick 2`):

```text
--- DELIVERED exit=1
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[3].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got 'rdup'; from_holder 'rdup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index)
```

F2 does **not** falsify either: qualification is symmetric across the two sides of the comparison, and the tick line stays definite. Both F1 and F2 changed stdout vs baseline (`stdout_changed=True`) in exactly the intended direction only.

**Controls** (baseline and delivered outputs byte-identical for all three):

```text
C1_null-first-record-clean:          exit 0->0 identical=True   CLEAN: schema, citations, relations, timeline; 0 violations
C2_first-record_nonnull_unresolved:  exit 1->1 identical=True   VIOLATION: entities[3].provenance[0]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: from_holder 'rdup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); first record must have from_holder null
C3_tick_with_ambiguous-source:       exit 1->1 identical=True   VIOLATION: entities[2].provenance[1].tick: input-structural finding, not sourced-canon; provenance tick 1 must be greater than previous tick 2
```

C3 pins the residual source gate: a tick finding keeps the `input-structural finding, not sourced-canon;` prefix when an earlier record in the same chain cited an ambiguous source id. That gate is source-based, not identity-based, and is unchanged by the repair (durable pin: `corpus/fixtures/r87-probe-source-prefix`).

## Findings & named debt

- **Freeze-then-verify PASS.** The delivered `corpus/fixtures/check_bible.py` is byte-identical to X2∘X3 composed on `e97613c` (`ff9fd2aa…`). No composition mismatch; no blocking finding.
- **Calibration verified on the delivered tree.** Null-chain breaks and null-associated tick inversions are now definite; tick order is judged as an integer comparison even when a compared holder is genuinely unresolved (P2); non-null unresolved holders still qualify chain breaks on either side (fn2 pair unchanged; F1; F2). No false definite and no false qualified shape appeared in P1/P2/F1/F2/C1–C3.
- **Vacuous clause eliminated corpus-wide.** 0 occurrences of `0 raw entity rows … 0 is in the resolved index` (and 0 `N == M` variants) across all 164 outputs; the only surviving unresolvable clause is fn2's correct `2 raw / 1 indexed`. The `None` sentinel can no longer print a count statement (`corpus/fixtures/check_bible.py:168`).
- **Census claim reproduced exactly.** 164 dirs = 160 pinned (0 mismatches vs `patches/B1-tuples.json`, 0 exit flips) + 4 new `r90-c1-*` fixtures; 0 changed tuples, 0 exit changes, 0 stderr bytes; 417 violation lines = 399 + 18. Exits: 32 clean / 132 violation.
- **NAMED DEBT D1 (adversarial, material): the repaired shapes are pinned by no durable artifact.** All 164 delivered outputs are byte-identical under the baseline and delivered checkers, and no delivered fixture emits the definite `… got None` line. Targeted sweep for later `from_holder: null` records: only `r87-probe-record-and-chain` contains them (9 records across `entities[3]` and `entities[6]`), and there every one is preceded by a recorded first stop (`entities[3]` stops at `provenance[0]` "malformed record (expected object)"; `entities[6]` stops at `provenance[0]` on an unknown source), so the null comparison is never reached and the output says "remain unassessed". So the durable corpus cannot detect a regression of either repaired shape. The committed C9 harness (`.ufo/waves/round-90/patches/C9-rerun-probes.sh`) rebuilds the X1 candidate (`12866e73…`), **not** the delivered checker, and the B3/C5/C9 probe fixtures lived in `/tmp` and are gone; the before/after receipts exist as text only. This seat's in-memory reconstructions reproduce those deltas against the delivered bytes, so the evidence stands — but it is not reproducible by one committed command against `ca7f9ef`. Recommended r91 debt: add one durable fixture per repaired shape (a later `from_holder: null` break and an unresolved-compared-holder tick inversion) or a committed harness that runs against the delivered checker.
- **NAMED DEBT D2 (wording scope):** "tick findings are definite" holds modulo the pre-existing ambiguous-source gate (C3; durable pin `r87-probe-source-prefix`, which keeps the `not sourced-canon` prefix on the tick line). This is unchanged by design and consistent with the C9 ruling, but the C1 claim should be read with that qualifier.
- **Observation (not this seat's write):** `corpus/tools/__pycache__/` is untracked in the repo tree (apparently bytecode from an earlier run of `corpus/tools/support_check.py` without `PYTHONDONTWRITEBYTECODE`). Flagged for cleanliness; not touched by this seat. Sibling followup artifacts (H2/H3/H4/JCAL1/JCAL3/JCAL4/JCAL5/JCOV*/JDEP*/CB1/Q2) also appeared concurrently. `git status --porcelain` additionally shows `M .ufo/waves/round-90/followup/Q1-r90-debt.json` — a tracked file modified by a sibling seat, not by this seat.
- **Measured code is exactly the commit:** `git status --porcelain` lists no entry for `corpus/fixtures/check_bible.py`, so the worktree checker bytes measured here are the `ca7f9ef` bytes (`ff9fd2aa…`), matching the frozen composition.
- Scope note: the C9 ruling supersedes the spec's written C1 boundary and is recorded in the wave spec's closure amendments (`.ufo/waves/round-90/wave-spec.md:135`), so the delivered integer-only tick reading is spec-aligned as amended; C9's spec-alignment debt is closed.

## Handoff

- **Verdict recommendation (per axis, no scalars):**
  - **C1 calibration — improved (bounded).** Every repaired shape behaves as ruled on the delivered tree, both new falsification attempts fail, the vacuous clause is gone corpus-wide, and there is no compensating trade on any other axis.
  - **Compatibility/regression axis — unchanged behavior, which is the required non-harm condition.** 164/164 tuples byte-identical to baseline, 160/160 receipt parity, 0 exit flips, 0 stderr.
  - **Durability/pinning sub-axis — unchanged (debt D1, not harm).** No durable fixture or committed command pins the repaired wording; carry D1 to r91.
  - Overall: recommend accepting C1 as delivered, with D1 named as the follow-up debt; no blocking finding.
- Writes from this seat: `.ufo/waves/round-90/followup/JCAL2.md`, `.ufo/waves/round-90/followup/JCAL2-receipts.json` (sha256 `c4df7d84402b20a5a41adef518ca6666e6200db4ba424123ff874dd52ad3dc93`). No commit, no push, no other tracked write. Scratch: `/tmp/jcal2` already existed with earlier seats' files; this seat added only `/tmp/jcal2/base.py` (the `git show e97613c:` checker) and `/tmp/jcal2/composed.py`, and its temporary `/tmp/jcal2/tree/` was removed on exit — everything else ran from memory/shell heredocs.
- Reproducibility: the census/sweep/receipt-check commands are given verbatim above; the probe harness and every probe's exact baseline/delivered stdout, exit and stderr are stored in `JCAL2-receipts.json` (keys `freeze_then_verify`, `census_164`, `pinned_160_receipt_check`, `vacuous_clause_sweep`, `probes`, `durable_fn2_pair`).
- Dependency note: no 60-second wait-checks were required or used by this seat; all inputs (patch files, receipts, fixtures) were present at seat start on `ca7f9ef`.

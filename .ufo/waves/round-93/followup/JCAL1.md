## Work performed

- Axes: **census completeness**, **no-regression calibration**, and **checker pin integrity**.
- Seat JCAL1, full 167-dir census at HEAD `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` on `main`, diffed against the 166-row baseline `.ufo/waves/round-93/patches/B1-tuples.json`.
- Verified the tracked tree clean (0 porcelain-tracked lines; only untracked `?? .ufo/waves/round-93/followup/` after my writes), working `corpus/fixtures` identical to `HEAD:corpus/fixtures`, and current + HEAD direct fixture dir counts both 167.
- Re-ran B1's exact census procedure (sorted repo-relative direct fixture dirs, each via `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>`), tuple receipts `exit` / `stdout_sha256` / `violation_count`, into `/tmp/lore-JCAL1` scratch (removed after archiving the receipt as `JCAL1-tuples.json`).
- No cross-seat dependency wait-checks were needed: my comparison target `B1-tuples.json` was already present at the committed tree on the first check, so the two 60s polls were skipped (block named no dependency).
- Wrote only `.ufo/waves/round-93/followup/JCAL1-delta.json`, `JCAL1-tuples.json`, and this `JCAL1.md`. No commit, no push.

## Before → after measurements

**Baseline identity** — exact command:

```sh
git status --short && printf 'tracked_diff_exit=' && git diff --quiet HEAD --; printf '%s\n' "$?" && git rev-parse HEAD && git branch --show-current && sha256sum corpus/fixtures/check_bible.py && printf 'current_direct_fixture_dirs=' && python3 -I -c "from pathlib import Path; print(sum(p.is_dir() for p in Path('corpus/fixtures').iterdir()))" && printf 'head_direct_fixture_dirs=' && python3 -I -c "
import subprocess
out=subprocess.run(['git','ls-tree','HEAD:corpus/fixtures'],check=True,capture_output=True,text=True).stdout.splitlines()
print(sum(line.startswith('040000 tree ') for line in out))" && git diff --quiet HEAD -- corpus/fixtures && printf 'tracked_fixtures_match_HEAD=YES\n'
```

Observed output:

```text
tracked_diff_exit=0
65838f867d6ece8e7b8bdcc4ffc667a08a1b785e
main
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
current_direct_fixture_dirs=167
head_direct_fixture_dirs=167
tracked_fixtures_match_HEAD=YES
```

**Full census** (each checker subprocess `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>`; tuples written to `/tmp/lore-JCAL1/JCAL1-tuples.json` — same procedure as B1, expectation widened from 166 to observed-count) — exact command:

```sh
mkdir -p /tmp/lore-JCAL1 && PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY'
import hashlib, json, pathlib, subprocess, time
root = pathlib.Path.cwd()
fixtures = root / 'corpus/fixtures'
names = sorted(p.name for p in fixtures.iterdir() if p.is_dir())
rows = {}
exit_counts = {}
stderr_nonempty = []
unexpected = []
t0 = time.time()
for name in names:
    rel = f'corpus/fixtures/{name}'
    p = subprocess.run(['python3', '-I', 'corpus/fixtures/check_bible.py', rel], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_counts[p.returncode] = exit_counts.get(p.returncode, 0) + 1
    if p.stderr:
        stderr_nonempty.append(rel)
    if p.returncode not in (0, 1):
        unexpected.append((rel, p.returncode))
    rows[rel] = {'exit': p.returncode, 'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(), 'violation_count': sum(line.startswith(b'VIOLATION:') for line in p.stdout.splitlines())}
raw = (json.dumps(rows, indent=2, sort_keys=True) + '\n').encode('utf-8')
out = pathlib.Path('/tmp/lore-JCAL1/JCAL1-tuples.json')
out.write_bytes(raw)
print(f'fixture_dirs={len(names)}')
print(f'first={names[0]} last={names[-1]}')
print(f'exit_counts={dict(sorted(exit_counts.items()))} violation_lines={sum(row["violation_count"] for row in rows.values())}')
print(f'stderr_nonempty_count={len(stderr_nonempty)} unexpected_exit_count={len(unexpected)}')
print(f'elapsed_s={time.time()-t0:.1f}')
print(f'checker_sha256={hashlib.sha256((fixtures / "check_bible.py").read_bytes()).hexdigest()}')
print(f'written=/tmp/lore-JCAL1/JCAL1-tuples.json bytes={len(raw)} sha256={hashlib.sha256(raw).hexdigest()}')
print('census_exit=0' if not unexpected and not stderr_nonempty else 'census_exit=1')
if unexpected or stderr_nonempty:
    raise SystemExit(1)
PY
```

Observed output:

```text
fixture_dirs=167
first=ally-one-way last=r93-m2-kojiki-cluster
exit_counts={0: 33, 1: 134} violation_lines=421
stderr_nonempty_count=0 unexpected_exit_count=0
elapsed_s=4.1
checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
written=/tmp/lore-JCAL1/JCAL1-tuples.json bytes=29586 sha256=6cc12f7fefb8c37f15f9a52b1fd1ee8e75d1174215eef11c78a9e3be5402888d
census_exit=0
```

**Delta vs baseline** — exact command:

```sh
python3 -I - <<'PY'
import json, pathlib
base = json.loads(pathlib.Path('.ufo/waves/round-93/patches/B1-tuples.json').read_bytes())
mine = json.loads(pathlib.Path('/tmp/lore-JCAL1/JCAL1-tuples.json').read_bytes())
missing = sorted(set(base) - set(mine)); new = sorted(set(mine) - set(base))
common  = sorted(set(base) & set(mine))
changed = sorted(k for k in common if base[k] != mine[k])
flips   = sorted(k for k in common if base[k]['exit'] != mine[k]['exit'])
print(f'baseline_rows={len(base)} census_rows={len(mine)} common={len(common)}')
print(f'missing_from_census={len(missing)} {missing}')
print(f'new_in_census={len(new)} {new}')
print(f'changed_tuples={len(changed)} {changed}')
print(f'exit_flips={len(flips)} {flips}')
print(f'baseline_exit_counts={{0: {sum(r["exit"]==0 for r in base.values())}, 1: {sum(r["exit"]==1 for r in base.values())}}} baseline_violation_lines={sum(r["violation_count"] for r in base.values())}')
print(f'common_violation_lines={sum(mine[k]["violation_count"] for k in common)}')
for k in new:
    print(f'new_tuple {k}: {mine[k]}')
PY
```

Observed output:

```text
baseline_rows=166 census_rows=167 common=166
missing_from_census=0 []
new_in_census=1 ['corpus/fixtures/r93-m2-kojiki-cluster']
changed_tuples=0 []
exit_flips=0 []
baseline_exit_counts={0: 32, 1: 134} baseline_violation_lines=421
common_violation_lines=421
new_tuple corpus/fixtures/r93-m2-kojiki-cluster: {'exit': 0, 'stdout_sha256': 'afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e', 'violation_count': 0}
```

**Baseline receipt integrity + B2 cross-check** — exact command:

```sh
sha256sum .ufo/waves/round-93/patches/B1-tuples.json .ufo/waves/round-93/patches/B2-tuples.json && python3 -I -c "
import json
b=json.load(open('.ufo/waves/round-93/patches/B1-tuples.json')); b2=json.load(open('.ufo/waves/round-93/patches/B2-tuples.json'))
print('B1_rows',len(b),'B2_rows',len(b2))
print('B1_vs_B2_mismatches',len([k for k in set(b)&set(b2) if b[k]!=b2[k]]))"
```

Observed output:

```text
185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf  .ufo/waves/round-93/patches/B1-tuples.json
185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf  .ufo/waves/round-93/patches/B2-tuples.json
B1_rows 166 B2_rows 166
B1_vs_B2_mismatches 0
```

(B1/B2 are byte-identical at sha `185ce02d…`, matching the sha recorded in `.ufo/waves/round-93/B1.md` — the comparison baseline is exactly what B1 recorded.)

## Findings & named debt

- **Claim confirmed exactly as stated**: 167 dirs (0 changed + 1 new), 0 exit flips. All 166 baseline rows reproduce tuple-for-tuple (exit, stdout_sha256, violation_count) under the unchanged pinned checker; the only delta is the new `corpus/fixtures/r93-m2-kojiki-cluster`, which exits 0 with 0 violations and the canonical clean-run stdout hash `afe570fc…` (same stdout hash as every passing fixture, e.g. `consistent`).
- Per-axis verdicts (evidence above, committed tree 65838f8 only):
  - **census completeness: improved** — coverage 166 → 167 with the third sourced-mythology cluster fixture inventoried and passing; no gaps, no stderr, no exits outside 0/1.
  - **preexisting-fixture behavior: unchanged** (the desired no-regression property, not a trade) — 0 changed tuples, 0 exit flips, common violation lines identical (421 = 421); exit mix moved only by the new passing dir ({0: 32→33, 1: 134 unchanged}).
  - **checker pin integrity: unchanged** — `corpus/fixtures/check_bible.py` sha256 still `ff9fd2aa…1421`, matching the C9 pin, so the before/after tuples are same-instrument and directly comparable.
  - **Overall r93 census axis: improved**, no trade observed within this seat's scope.
- The new fixture dir contains the full layout (`entities.json`, `relations.json`, `timeline.json`, `contradictions.json`, `sources.json`, `README.md`, `archive-record-excerpt.md`, `kojiki-chamberlain-excerpt.md`, `inspiration-note.md`, `claim-excerpt-map.md`, `symbolism-clause-map.md`) — consistent with the C2 cluster claim at fixture granularity.
- Named debt (not new, carried forward): my tuples cover observable checker behavior per direct fixture dir (exit / stdout hash / violation count). Byte-level diffs of pre-existing fixture file contents were not in scope and are not proven byte-identical — only behavior-identical under the unchanged checker. The AST-anchor validation gap in `corpus/tools/boundary_doc_check.py` named by C1 remains r94 debt and was not re-examined here.
- Verdict recommendation for the wave's census judge: **improved** on C2 coverage with zero calibration regression on C3.

## Handoff

- `.ufo/waves/round-93/followup/JCAL1.md` — this report (commands + outputs).
- `.ufo/waves/round-93/followup/JCAL1-delta.json` — machine-readable delta (sha256 `42f42378320f776eb2fbdc8bbfec5738a64534d99287ff29483211bfcd164614`, JSON-validated PASS).
- `.ufo/waves/round-93/followup/JCAL1-tuples.json` — full 167-row census receipt (29,586 bytes, sha256 `6cc12f7fefb8c37f15f9a52b1fd1ee8e75d1174215eef11c78a9e3be5402888d`) for any later seat to diff against without re-running.
- Tracked files unchanged (`git diff --quiet HEAD` exit 0; only untracked `?? .ufo/waves/round-93/followup/` from my own writes). `/tmp/lore-JCAL1` scratch removed. No commit, no push.
- A second independent census (JCAL2) diffing against this receipt would close the reproducibility loop the way B1/B2 did.

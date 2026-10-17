# JCAL1 — Census judge #1 at c4d4823

Seat JCAL1. Wave: round-92 follow-up (world-bible lane), repo `lore-shokunin/`.
Judged tree: HEAD `c4d4823b9a8165a88e8199af136e62d6e961b6b9` — the single r92 WORK integration commit (`c4d4823 lore r92: C1 anchor-based doc re-derivation + residual edges, C2 Spence rows + contract cleanup, C3 watch re-check — work wave (31+2 luna-max seats)`), 1 commit since baseline `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`; tracked tree clean at every check (verified). Census measured `2026-10-17T10:26:06-03:00`.
Mission: independent full 166-directory census at the committed tree; diff vs `.ufo/waves/round-92/patches/B1-tuples.json`; confirm 0 changed, 0 exit flips; verdict recommendation. Every number below comes from the committed tree. No `/tmp` scratch was created; the only repo writes from this seat are this report and `JCAL1-delta.json`.

## Work performed

- Verified the dependency: HEAD pinned at `c4d4823` and tracked tree clean, with two 60-second wait-checks (t=0/60/120) around the census run; only untracked follow-up seat artifacts appeared during the window, all under `.ufo/waves/round-92/followup/`.
- Ran the full 166-directory census at the committed tree (`python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` per sorted direct child dir; fields `{exit, stdout_sha256, violation_count}`) and diffed every row against `.ufo/waves/round-92/patches/B1-tuples.json`, whose SHA-256 was first checked against its recorded hash `185ce02d…`.
- Triple-checked checker identity: working-tree bytes == `git show HEAD:` blob == C9 pin `ff9fd2aa…`; verified the worktree fixture tree equals HEAD (`git diff --quiet HEAD -- corpus/fixtures` exit 0) and that the integration's only `corpus/fixtures` changes are docs (README.md, r88-m3-maya-cluster/claim-excerpt-map.md).
- Confirmed the checker reads only `<section>.json` files inside each input dir (checker lines 44–47), so doc-side edits cannot reach the census surface; empirically zero drift confirms.
- Ran a live spot-check probe (`r91-c1-tick-unresolved`) whose stdout hash equals B1's stored tuple hash — liveness proof that the census actually re-executed rather than echoed.
- Wrote only the two permitted artifacts; no tracked file was modified; no commit or push.

## Before → after measurements

**(1) Dependency identity and the two 60s wait-checks.** Exact command (also recorded in `JCAL1-delta.json` → `wait_checks.command`):

```sh
cd lore-shokunin && PIN=c4d4823b9a8165a88e8199af136e62d6e961b6b9; chk(){ t="$1"; h=$(git rev-parse HEAD); d=$(git diff --name-only HEAD | wc -l); u=$(git status --porcelain | grep -c '^??'); printf 'STAB t=%ss at=%s head=%s tracked_dirty=%s untracked=%s head_pinned=%s tracked_clean=%s\n' "$t" "$(date -Is)" "$h" "$d" "$u" "$([ "$h" = "$PIN" ] && echo YES || echo NO)" "$([ "$d" = 0 ] && echo YES || echo NO)"; git status --porcelain; }; chk 0; sleep 60; chk 60; sleep 60; chk 120
```

Observed output:

```text
STAB t=0s at=2026-10-17T10:26:02-03:00 head=c4d4823b9a8165a88e8199af136e62d6e961b6b9 tracked_dirty=0 untracked=1 head_pinned=YES tracked_clean=YES
?? .ufo/waves/round-92/followup/H4-census.json
STAB t=60s at=2026-10-17T10:27:02-03:00 head=c4d4823b9a8165a88e8199af136e62d6e961b6b9 tracked_dirty=0 untracked=6 head_pinned=YES tracked_clean=YES
?? .ufo/waves/round-92/followup/H4-census.json
?? .ufo/waves/round-92/followup/H4-lineage.json
?? .ufo/waves/round-92/followup/H4-probes.json
?? .ufo/waves/round-92/followup/JCAL1-delta.json
?? .ufo/waves/round-92/followup/JCAL3-evidence.json
?? .ufo/waves/round-92/followup/JCAL3.md
STAB t=120s at=2026-10-17T10:28:02-03:00 head=c4d4823b9a8165a88e8199af136e62d6e961b6b9 tracked_dirty=0 untracked=15 head_pinned=YES tracked_clean=YES
?? .ufo/waves/round-92/followup/H3-r92-discrimination.json
?? .ufo/waves/round-92/followup/H3-r92-replay.json
?? .ufo/waves/round-92/followup/H3-r92-scan.json
?? .ufo/waves/round-92/followup/H3.md
?? .ufo/waves/round-92/followup/H4-census.json
?? .ufo/waves/round-92/followup/H4-lineage.json
?? .ufo/waves/round-92/followup/H4-probes.json
?? .ufo/waves/round-92/followup/H4.md
?? .ufo/waves/round-92/followup/JCAL1-delta.json
?? .ufo/waves/round-92/followup/JCAL3-evidence.json
?? .ufo/waves/round-92/followup/JCAL3.md
?? .ufo/waves/round-92/followup/JCAL5-delta.json
?? .ufo/waves/round-92/followup/JCOV1.md
?? .ufo/waves/round-92/followup/JCOV2.md
?? .ufo/waves/round-92/followup/JCOV3-census.json
STAB_VERDICT two_60s_checks_complete=YES
```

The census ran at 10:26:06 inside the 0s..60s interval; both endpoints of that interval were pinned and tracked-clean. The only untracked additions are follow-up seat artifacts under `.ufo/waves/round-92/followup/` — outside the judgment surface; nothing dirty or untracked appeared inside `corpus/`.

**(2) Full 166-directory census and diff vs B1.** Exact command (run from `lore-shokunin/`):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY'
import hashlib, json, pathlib, subprocess, sys
root = pathlib.Path.cwd()
fixtures = root / 'corpus/fixtures'
names = sorted(p.name for p in fixtures.iterdir() if p.is_dir())
assert len(names) == 166, f'expected 166 direct fixture dirs; observed {len(names)}'
b1p = root / '.ufo/waves/round-92/patches/B1-tuples.json'
b1raw = b1p.read_bytes(); b1 = json.loads(b1raw)
EXPECT_B1_SHA = '185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf'
PIN_CHECKER = 'ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421'
def git(*a): return subprocess.run(['git', *a], cwd=root, capture_output=True, text=True)
head = git('rev-parse','HEAD').stdout.strip()
porcelain = git('status','--porcelain').stdout.strip()
dirty_paths = [l[3:] for l in porcelain.splitlines() if not l.startswith('??')]
lsout = git('ls-tree','HEAD:corpus/fixtures').stdout.splitlines()
head_dirs = sum(l.startswith('040000 tree ') for l in lsout)
head_checker = subprocess.run(['git','show','HEAD:corpus/fixtures/check_bible.py'], cwd=root, capture_output=True).stdout
checker_bytes = (fixtures / 'check_bible.py').read_bytes()
rows = {}; exit_counts = {}; stderr_nonempty = []; unexpected = []; violation_lines = 0
for name in names:
    rel = f'corpus/fixtures/{name}'
    p = subprocess.run(['python3','-I','corpus/fixtures/check_bible.py',rel], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_counts[p.returncode] = exit_counts.get(p.returncode, 0) + 1
    vc = sum(line.startswith(b'VIOLATION:') for line in p.stdout.splitlines())
    violation_lines += vc
    if p.stderr: stderr_nonempty.append(rel)
    if p.returncode not in (0,1): unexpected.append([rel, p.returncode])
    rows[rel] = {'exit': p.returncode, 'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(), 'violation_count': vc}
missing = sorted(set(b1)-set(rows)); extra = sorted(set(rows)-set(b1)); common = sorted(set(rows)&set(b1))
changed = [k for k in common if rows[k] != b1[k]]
exit_flips = [k for k in common if rows[k]['exit'] != b1[k]['exit']]
field_diffs = {k: {f: {'before': b1[k][f], 'after': rows[k][f]} for f in ('exit','stdout_sha256','violation_count') if b1[k][f] != rows[k][f]} for k in changed}
canon = lambda d: hashlib.sha256(json.dumps(d, sort_keys=True, separators=(',',':')).encode()).hexdigest()
census_sha = canon(rows); b1_sha = canon(b1)
measured_at = subprocess.run(['date','-Is'], capture_output=True, text=True).stdout.strip()
head_blob_sha = hashlib.sha256(head_checker).hexdigest(); wt_sha = hashlib.sha256(checker_bytes).hexdigest()
print(f'JCAL1 measured_at={measured_at}')
print(f'head={head} baseline=396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f')
print(f'porcelain_lines={len(porcelain.splitlines())} tracked_dirty_paths={dirty_paths}')
print(f'fixture_dirs={len(names)} head_tree_dirs={head_dirs} fixture_tree_matches_head={git("diff","--quiet","HEAD","--","corpus/fixtures").returncode == 0}')
print(f'checker_worktree_sha256={wt_sha}')
print(f'checker_head_blob_sha256={head_blob_sha} head_blob_equal={wt_sha == head_blob_sha} c9_pin_equal={wt_sha == PIN_CHECKER}')
print(f'b1_bytes={len(b1raw)} b1_sha256={hashlib.sha256(b1raw).hexdigest()} recorded_sha_match={hashlib.sha256(b1raw).hexdigest() == EXPECT_B1_SHA} b1_rows={len(b1)}')
print(f'exit_counts={dict(sorted(exit_counts.items()))} violation_lines={violation_lines}')
print(f'stderr_nonempty={len(stderr_nonempty)} unexpected_exits={len(unexpected)}')
print(f'missing_from_census={missing} extra_in_census={extra} changed_count={len(changed)} exit_flips={exit_flips}')
print(f'changed_paths={changed}')
print(f'field_diffs={json.dumps(field_diffs)}')
print(f'census_canonical_sha256={census_sha}')
print(f'b1_canonical_sha256={b1_sha} canonical_equal={census_sha == b1_sha}')
print(f'stderr_nonempty_paths={stderr_nonempty}')
# (delta JSON written here — see receipt below)
print(f'written=.ufo/waves/round-92/followup/JCAL1-delta.json bytes={len(raw)} sha256={hashlib.sha256(raw).hexdigest()}')
print(f'porcelain_after_write=')
print(git('status','--porcelain').stdout.strip())
PY
```

(Abridged only at the delta-writing `delta = {...}` construction, marked above; everything else is verbatim as run.)

Observed output:

```text
JCAL1 measured_at=2026-10-17T10:26:06-03:00
head=c4d4823b9a8165a88e8199af136e62d6e961b6b9 baseline=396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f
porcelain_lines=1 tracked_dirty_paths=[]
fixture_dirs=166 head_tree_dirs=166 fixture_tree_matches_head=True
checker_worktree_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
checker_head_blob_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 head_blob_equal=True c9_pin_equal=True
b1_bytes=29407 b1_sha256=185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf recorded_sha_match=True b1_rows=166
exit_counts={0: 32, 1: 134} violation_lines=421
stderr_nonempty=0 unexpected_exits=0
missing_from_census=[] extra_in_census=[] changed_count=0 exit_flips=[]
changed_paths=[]
field_diffs={}
census_canonical_sha256=a92a4f222804db5cbdc88a558568aa81cc62f459f2aa6b6a7981400c455203df
b1_canonical_sha256=a92a4f222804db5cbdc88a558568aa81cc62f459f2aa6b6a7981400c455203df canonical_equal=True
stderr_nonempty_paths=[]
written=.ufo/waves/round-92/followup/JCAL1-delta.json bytes=2549 sha256=4dc06d00f1b7439562c123b044799b19205d9e8a8f835c5ab28189bc909ea81e
porcelain_after_write=
?? .ufo/waves/round-92/followup/H4-census.json
?? .ufo/waves/round-92/followup/JCAL1-delta.json
```

The single untracked line at start (`porcelain_lines=1`) was the peer artifact `H4-census.json` (mtime 10:26:01), not a fixture-tree change. The delta file was subsequently extended with the wait-check and spot-check receipts (final: 4,790 bytes, SHA-256 `0e6738376cf4b5f0be05f5d50b6ad3292c9a2cb99e2ef498fd16b0e7a64dc629`); the interim receipt above is kept for audit continuity.

**(3) Baseline receipt, checker identity, fixture-tree scope.** Exact commands and observed output:

```sh
sha256sum corpus/fixtures/check_bible.py .ufo/waves/round-92/patches/B2-tuples.json
git show HEAD:corpus/fixtures/check_bible.py | sha256sum
git diff --quiet HEAD -- corpus/fixtures; echo $?
git diff --stat 396c568..c4d4823 -- corpus/fixtures
sed -n '38,52p' corpus/fixtures/check_bible.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf  .ufo/waves/round-92/patches/B2-tuples.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
fixture_diff_exit=0

--- 396c568..c4d4823 fixture changes ---
 corpus/fixtures/README.md                          | 44 ++++++++++++++++++++++
 .../r88-m3-maya-cluster/claim-excerpt-map.md       | 14 ++++---
 2 files changed, 52 insertions(+), 6 deletions(-)

(38,52 excerpt)
    for section, fields in FIELDS.items():
        path = directory / (section + '.json')
        loaded = True
        try:
            rows = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
```

So: B2 is byte-identical to B1 (same SHA-256); the checker is identical across worktree, HEAD, and the C9 pin; the fixture tree matches HEAD; the integration's fixture-surface diff is docs-only; and the checker's input scope is exactly each dir's `<section>.json` files.

**(4) Live liveness spot-check.** Exact command and observed output:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -I corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved | sha256sum
```

```text
d754e96f7c01e6fb6eff12168a732d5a6125f428a9207bd74fc49bbdcbb25d88  -
```

That digest equals B1's stored tuple for this path (`{'exit': 1, 'stdout_sha256': 'd754e96f…', 'violation_count': 3}`; the probe itself exits 1 with the 3 expected VIOLATION lines and empty stderr — full text in the raw run above).

**(5) Delta artifact.** `python3 -I -m json.tool .ufo/waves/round-92/followup/JCAL1-delta.json` → `delta_json_validation=PASS`; final size 4,790 bytes, SHA-256 `0e6738376cf4b5f0be05f5d50b6ad3292c9a2cb99e2ef498fd16b0e7a64dc629`. It carries the canonical digests, empty delta sets, wait checks, and the spot-check.

## Findings & named debt

**Verdict recommendation — census axis: unchanged (no drift; nothing traded).** At committed HEAD `c4d4823`: 166/166 census tuples identical to B1 — 0 changed, 0 exit flips, canonical digest equality (`a92a4f22…`), 32×exit-0 / 134×exit-1, 421 violation lines, zero stderr, zero unexpected exits. The `ff9fd2aa…` checker pin is intact (worktree == HEAD blob == C9 pin). Recommend recording the lemma "r92 checker unchanged / no fixture-surface regression" as **confirmed (unchanged)**; no axis is harmed on this surface, and the integration is census-neutral. C1/C2/C3 content verdicts remain with their judging seats.

- **Nothing to investigate under the "ANY change" clause** — it is vacuously satisfied. The two tracked `corpus/fixtures` changes in the integration (README.md +44; r88-m3-maya-cluster/claim-excerpt-map.md +14/−6) are doc-side; the checker reads only `<section>.json` per input dir (lines 44–47 excerpt above), and the empirical zero drift confirms they cannot move any tuple. This was checked specifically because the r88-m3 map edit lives inside a census-counted fixture directory.
- **Baseline receipt integrity holds:** B1's SHA-256 equals its recorded hash `185ce02d…`, and B2 is byte-identical to B1.
- **Tree stability:** HEAD pinned and tracked tree clean at 0s/60s/120s; the census executed inside the 0s..60s window. All untracked activity in the window is follow-up artifacts under `.ufo/waves/round-92/followup/` (H3, H4, JCAL1-delta, JCAL3, JCAL5, JCOV1-3) — none inside `corpus/`, none tracked.
- **Peer corroboration (context only, not this seat's evidence):** the peer artifact `H4-census.json` (written 10:26:01) reports the same summary ({0:32, 1:134}, 421 violation lines, 0 stderr, empty `delta_vs_B1`). It was not audited by this seat and is not part of my evidence.

Named debt / gaps:

- Equivalence is proven over the 166 covered fixture inputs (plus the spot-check), not over all possible inputs; behavior outside the fixtures surface is out of scope.
- Scope is `corpus/fixtures/check_bible.py` only; the support-command receipts (C2) belong to other seats.
- Peer artifacts present during the window (H3/H4/JCAL3/JCAL5/JCOV1-3) were not audited here.
- Untracked follow-up accumulation is expected batch behavior and is isolated from the committed judgment surface; the committed tree was the only measurement input.

## Handoff

- Deliverables: `.ufo/waves/round-92/followup/JCAL1.md` (this report) and `.ufo/waves/round-92/followup/JCAL1-delta.json` — 4,790 bytes, SHA-256 `0e6738376cf4b5f0be05f5d50b6ad3292c9a2cb99e2ef498fd16b0e7a64dc629`; JSON-valid; contains per-field machine evidence, canonical digests, wait-check receipts, and the spot check.
- Result: **PASS — 0 changed, 0 exit flips at c4d4823; checker `ff9fd2aa…` unchanged.**
- For JCAL2 (census judge #2, if present): cross-check `census_canonical_sha256 == b1_canonical_sha256 == a92a4f222804db5cbdc88a558568aa81cc62f459f2aa6b6a7981400c455203df`; the replay recipe is in the delta `census.method` and section (2) above.
- No commit, no push; no tracked file touched; repo writes limited to the two follow-up artifacts; no `/tmp` scratch created.
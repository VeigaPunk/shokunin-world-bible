# JDEP4 — mechanical regression-discrimination check (verbatim)

Runnable pass/fail companion for the candidate capabilities row
`checker-regression discrimination`. Run from `lore-shokunin/` (delivered tree
HEAD `c2ab3d0`). No files are created; the e97613c checker source is fed
through `python3 -c` without touching `/tmp`.

Properties verified 2026-10-17 on the delivered tree:

- `run_check delivered` → `RESULT: DISCRIMINATION HELD`, exit 0, while the
  delivered checker still produces the pinned delivered lines;
- `run_check e97613c` → `REGRESSION-DETECTED`, exit 2 — this feeds the
  pre-repair `e97613c` source as the checker (silent-revert simulation);
- each fixture's complete stdout is compared byte-for-byte against both README
  expectation blocks; the definite/qualified phrase gates are asserted; the
  e97613c↔delivered line-pair delta is printed per fixture.

The script is the tracked X1 verifier shape (`.ufo/waves/round-91/X1.md`)
collapsed into two modes; expectations are parsed from the fixture READMEs.

```sh
run_check() {
JDEP4_CHECKER="$1" python3 -I - "$PWD" <<'PY'
import os, pathlib, re, subprocess, sys, difflib
repo = pathlib.Path(sys.argv[1]); chk = repo/'corpus/fixtures/check_bible.py'
PIN='ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421'
OLD='e97613cc276f5fa9cac49ff1900798cf6863c020'
mode=os.environ['JDEP4_CHECKER']
names=('r91-c1-null-chain','r91-c1-tick-unresolved')
h=subprocess.run(['sha256sum',str(chk)],capture_output=True,text=True,cwd=repo).stdout.split()[0]
print(f'mode={mode} checker_sha256={h} matches_pin={h==PIN}')
def run_new(d): return subprocess.run([sys.executable,'-I',str(chk),str(d)],capture_output=True,text=True,cwd=repo)
oldsrc=subprocess.run(['git','show',f'{OLD}:corpus/fixtures/check_bible.py'],capture_output=True,text=True,cwd=repo,check=True).stdout
WRAP="import sys; code=sys.stdin.read(); sys.argv=['check_bible.py',*sys.argv[1:]]; exec(compile(code,'check_bible.py','exec'),{'__name__':'__main__','__file__':'check_bible.py'})"
def run_old(d): return subprocess.run([sys.executable,'-I','-c',WRAP,str(d)],input=oldsrc,capture_output=True,text=True,cwd=repo)
run=run_new if mode=='delivered' else run_old
fails=[]
for n in names:
    text=(repo/'corpus/fixtures'/n/'README.md').read_text(encoding='utf-8')
    exp=dict(re.findall(r'## Expected output with (e97613c|the delivered checker) \(exit 1; stderr empty\)\n\nComplete stdout:\n\n```text\n(.*?)\n```',text,re.S))
    assert set(exp)=={'e97613c','the delivered checker'}
    r=run(repo/'corpus/fixtures'/n)
    before=run_old(repo/'corpus/fixtures'/n); after=run_new(repo/'corpus/fixtures'/n)
    removed=[l[2:] for l in difflib.ndiff(before.stdout.splitlines(),after.stdout.splitlines()) if l.startswith('- ')]
    added=[l[2:] for l in difflib.ndiff(before.stdout.splitlines(),after.stdout.splitlines()) if l.startswith('+ ')]
    print(f'{n}: run_exit={r.returncode} stderr_empty={r.stderr==""} README_exact={r.stdout==exp["the delivered checker"]+"\n"} changed_line_pairs={len(added)}/{len(removed)} (old<->new)')
    if n=='r91-c1-null-chain':
        gate = ('provenance chain break; expected from_holder \'mira\', got None' in r.stdout) and ('is not uniquely resolvable' not in r.stdout)
    else:
        gate = ('VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3' in r.stdout) and ('holder identity is not uniquely resolvable' not in r.stdout) and ('possible provenance chain break' in r.stdout)
    print(f'  pinned_semantic_gate={"PASS" if gate else "FAIL"}')
    if not (r.returncode==1 and r.stderr=='' and r.stdout==exp['the delivered checker']+'\n' and len(added)==1 and len(removed)==1 and gate):
        fails.append(n)
if mode=='delivered':
    if fails: print('RESULT: FAILED on',fails); sys.exit(1)
    print('RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression'); sys.exit(0)
else:
    if fails: print('REGRESSION-DETECTED on',','.join(fails),'— pinned delivered semantics not present'); sys.exit(2)
    print('RESULT: no divergence detected (unexpected for reverted checker)'); sys.exit(0)
PY
}
run_check delivered; echo "exit=$?"
run_check e97613c; echo "exit=$?"
```

## Observed output, delivered tree (2026-10-17)

```text
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
exit=0
```

## Observed output, silent-revert simulation (e97613c source as checker)

```text
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
exit=2
```

Note: the `checker_sha256` line always hashes the repository file (the pinned
delivered checker); in `e97613c` mode the *executed* checker is the e97613c
source, so that hash line is informational, while `matches_pin` refers to the
repository file. In `e97613c` mode the script intentionally fails the delivered
expectations — that failure is the detection.
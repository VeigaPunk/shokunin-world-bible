import hashlib, json, subprocess, sys
from pathlib import Path
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
BASE = '6f86bf2'
def git(*a):
    return subprocess.run(['git',*a],cwd=root,capture_output=True,text=True)
def sha(b): return hashlib.sha256(b).hexdigest()

# 1. PROVINCE byte-identity vs baseline and vs HEAD
base_bytes = subprocess.check_output(['git','show',f'{BASE}:PROVINCE.md'],cwd=root)
work_bytes = (root/'PROVINCE.md').read_bytes()
head_bytes = subprocess.check_output(['git','show','HEAD:PROVINCE.md'],cwd=root)
print('PROVINCE_BASE_SHA256 ', sha(base_bytes))
print('PROVINCE_HEAD_SHA256 ', sha(head_bytes))
print('PROVINCE_WORK_SHA256 ', sha(work_bytes))
print('PROVINCE_BYTE_IDENTICAL_VS_BASELINE', work_bytes == base_bytes)
print('PROVINCE_BYTE_IDENTICAL_VS_HEAD   ', work_bytes == head_bytes)
d = git('diff','--exit-code',BASE,'--','PROVINCE.md')
print('GIT_DIFF_BASELINE_PROVINCE_EXIT', d.returncode)

# 2. Write confinement vs producer byte-ownership
tracked = git('diff','--name-only','HEAD','--').stdout.splitlines()
untracked = git('ls-files','--others','--exclude-standard').stdout.splitlines()
allowed_tracked = {
    'SKILL.md',
    'corpus/tools/README.md',
    'corpus/tools/dependency_freeze.py',
    'corpus/tools/dependency-freeze-contract.json',
}
allowed_new = {
    'corpus/knowledge/r101-r10-register-first-entry.md',
    '.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md',  # pre-existing stray
}
seat_areas = ('.ufo/waves/round-101/seats/',)
unauth_t = [p for p in tracked if p not in allowed_tracked]
unauth_u = [p for p in untracked if p not in allowed_new and not p.startswith(seat_areas)]
print('TRACKED_CHANGES   ', json.dumps(sorted(tracked)))
print('NEW_UNTRACKED     ', json.dumps(sorted(p for p in untracked if p not in allowed_new)))
print('UNAUTHORIZED_TRACKED', json.dumps(unauth_t))
print('UNAUTHORIZED_UNTRACKED', json.dumps(unauth_u))
outside = [p for p in set(tracked+untracked) if not (root/p).resolve().is_relative_to(root)]
print('OUTSIDE_RESOLUTIONS', json.dumps(outside))

# 3. SKILL.md delta confinement: everything before the freeze heading must be baseline-identical
skill_base = subprocess.check_output(['git','show',f'{BASE}:SKILL.md'],cwd=root)
skill_work = (root/'SKILL.md').read_bytes()
marker = b'### Dependency-edge freeze check'
i_base, i_work = skill_base.find(marker), skill_work.find(marker)
print('SKILL_PREFIX_IDENTICAL', i_base!=-1 and i_work!=-1 and skill_base[:i_base]==skill_work[:i_work])
print('SKILL_PREFIX_LEN_BASE_WORK', i_base, i_work)

# 4. Mechanics: no new commits during the round
log = git('log','--oneline','-3')
print('GIT_LOG_HEAD3:'); print(log.stdout, end='')
st = git('status','--porcelain','--branch')
print('GIT_STATUS_BRANCH:'); print(st.stdout, end='')

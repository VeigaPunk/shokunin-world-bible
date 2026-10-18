import json, shutil, subprocess, sys, os
from pathlib import Path
REPO = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCR = REPO/'.ufo/waves/round-98/seats/V52-scratch'
TOOL = REPO/'corpus/tools/dependency_freeze.py'
CONTRACT = REPO/'corpus/tools/dependency-freeze-contract.json'
PY = sys.executable

def mirror(name):
    root = SCR/'mirror'/name
    if root.exists(): shutil.rmtree(root)
    (root/'corpus/tools').mkdir(parents=True)
    shutil.copy2(TOOL, root/'corpus/tools/dependency_freeze.py')
    shutil.copy2(CONTRACT, root/'corpus/tools/dependency-freeze-contract.json')
    return root

def add_fixture(root, src, name=None):
    dst = root/'corpus/fixtures'/(name or src.name)
    shutil.copytree(src, dst)
    return dst

def run(args, cwd):
    p = subprocess.run([PY, *args], cwd=cwd, capture_output=True, text=True)
    return p.returncode, (p.stdout+p.stderr).strip()

print('== A. r97 edge drop on pinned r97 (V46 discharge) ==')
root = mirror('edge')
fx = add_fixture(root, REPO/'corpus/fixtures/r97-crossing-acknowledgment')
tl = fx/'timeline.json'
data = json.loads(tl.read_text())
ev = [e for e in data if e['id']=='acknowledgment-aru-records'][0]
print('before depends_on:', ev['depends_on'])
ev['depends_on'] = [d for d in ev['depends_on'] if d != 'response-evin-salt-court']
tl.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
rc, out = run([str(root/'corpus/tools/dependency_freeze.py'), 'corpus/fixtures/r97-crossing-acknowledgment'], root)
print(out); print('exit =', rc)

print()
print('== B1. path-less legacy pin migrated by --freeze ==')
root = mirror('legacy')
fx = add_fixture(root, REPO/'corpus/fixtures/r97-crossing-acknowledgment')
mc = root/'corpus/tools/dependency-freeze-contract.json'
c = json.loads(mc.read_text())
pin = c['pins']['r97-crossing-acknowledgment']
del pin['fixture']
mc.write_text(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
rc, out = run([str(root/'corpus/tools/dependency_freeze.py'), '--freeze', 'corpus/fixtures/r97-crossing-acknowledgment'], root)
print(out); print('exit =', rc)
after = json.loads(mc.read_text())['pins']['r97-crossing-acknowledgment']
print('pin fixture after:', after.get('fixture'))

print()
print('== B2. same-named in-scope elsewhere still refused ==')
root2 = mirror('shadow')
add_fixture(root2, REPO/'corpus/fixtures/r97-crossing-acknowledgment', 'shadow/r97-crossing-acknowledgment')
rc, out = run([str(root2/'corpus/tools/dependency_freeze.py'), '--freeze', 'corpus/fixtures/shadow/r97-crossing-acknowledgment'], root2)
print(out); print('exit =', rc)

print()
print('== C. independent SELF-TEST-MISMATCH exit-2 probe (digest_tamper expectation flipped) ==')
root = mirror('mismatch')
add_fixture(root, REPO/'corpus/fixtures/r95-crossing-aftermath')
mc = root/'corpus/tools/dependency-freeze-contract.json'
c = json.loads(mc.read_text())
c['self_test']['expected']['digest_tamper']['exit'] = 0
mc.write_text(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
rc, out = run([str(root/'corpus/tools/dependency_freeze.py'), '--self-test'], root)
lines = out.splitlines()
print('\n'.join([l for l in lines if 'MISMATCH' in l or 'CASE digest_tamper' in l or l.startswith('FINDING') or l.startswith('RESULT') or l.startswith('SELF-TEST')]))
print('exit =', rc)

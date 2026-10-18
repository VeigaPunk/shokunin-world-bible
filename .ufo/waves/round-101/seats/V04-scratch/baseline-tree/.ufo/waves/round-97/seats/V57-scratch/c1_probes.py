import json, pathlib, shutil, subprocess, sys

ROOT = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
S = ROOT / '.ufo/waves/round-97/seats/V57-scratch'
TOOL = ROOT / 'corpus/tools/map_obligations.py'
CONTRACT = ROOT / 'corpus/tools/map-obligations-contract.json'

def variant(name, drop=None, patch_emission=False):
    d = S / name / 'tool'
    d.mkdir(parents=True, exist_ok=True)
    shutil.copy(TOOL, d / 'map_obligations.py')
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    if drop:
        c['self_test']['cases'] = [x for x in c['self_test']['cases'] if x['id'] != drop]
    (d / 'map-obligations-contract.json').write_text(json.dumps(c, indent=1), encoding='utf-8')
    if patch_emission:
        src = (d / 'map_obligations.py').read_text(encoding='utf-8')
        needle = '            if mention is not None:'
        assert src.count(needle) == 1, 'needle not unique'
        src = src.replace(needle, '            if False:  # V57 load-bearing probe')
        (d / 'map_obligations.py').write_text(src, encoding='utf-8')
    r = subprocess.run([sys.executable, str(d / 'map_obligations.py'), '--self-test'],
                       capture_output=True, text=True, cwd=ROOT)
    print(f'=== {name} ===')
    for line in r.stdout.splitlines():
        if line.startswith(('SELF-TEST CASES', 'FINDING', 'RESULT', 'SELF-TEST FAIL')):
            print(' ', line)
    print(f'  exit={r.returncode} stderr={r.stderr.strip()[:120]!r}')

variant('probe-A-drop-dual', drop='dual_pointer')
variant('probe-B-drop-core', drop='complete')
variant('probe-C-drop-added', drop='inventory_mismatch')
variant('probe-D-neutralize', patch_emission=True)
variant('probe-E-control')

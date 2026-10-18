import json, shutil, subprocess, sys
from pathlib import Path
REPO = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCR = REPO/'.ufo/waves/round-98/seats/V52-scratch'
PY = sys.executable
FILES = ['corpus/tools/map_obligations.py','corpus/tools/map-obligations-contract.json',
         'corpus/tools/support_check.py','corpus/fixtures/check_bible.py']
def build(tag, map_bytes=None):
    root = SCR/'mirror'/tag
    if root.exists(): shutil.rmtree(root)
    for f in FILES:
        dst = root/f
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO/f, dst)
    fx = root/'corpus/fixtures/r95-crossing-aftermath'
    shutil.copytree(REPO/'corpus/fixtures/r95-crossing-aftermath', fx)
    if map_bytes is not None:
        (fx/'claim-excerpt-map.md').write_bytes(map_bytes)
    return root
base_map = subprocess.run(['git','show','9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md'],cwd=REPO,capture_output=True).stdout
roots = {'pre': build('r95pre', base_map), 'post': build('r95post')}
def run(root, cmd):
    p = subprocess.run([PY, *cmd], cwd=root, capture_output=True, text=True)
    return p.returncode, (p.stdout+p.stderr).strip()
cmds = {
 'check_bible': ['corpus/fixtures/check_bible.py','corpus/fixtures/r95-crossing-aftermath'],
 'support_check': ['corpus/tools/support_check.py','corpus/fixtures/r95-crossing-aftermath'],
 'map_obligations': ['corpus/tools/map_obligations.py','corpus/fixtures/r95-crossing-aftermath'],
}
outs = {}
for tag, root in roots.items():
    for name, cmd in cmds.items():
        rc, out = run(root, cmd)
        outs[(tag,name)] = (rc,out)
        print(f'--- {tag} {name}: exit={rc}')
        print(out)
print()
for name in cmds:
    same = outs[('pre',name)] == outs[('post',name)]
    print(f'{name}: pre==post -> {same}')

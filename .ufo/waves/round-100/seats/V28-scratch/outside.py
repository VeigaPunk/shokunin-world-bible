from pathlib import Path
import datetime
import json
import os
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
PARENT = ROOT.parent
S = ROOT / '.ufo/waves/round-100/seats/V28-scratch'
assert Path.cwd().resolve() == ROOT
assert (S / 'ready-manifest.json').is_file()
since = int(subprocess.check_output(['git', 'show', '-s', '--format=%ct', 'b5fe472'], cwd=ROOT, text=True).strip())
recent = {}
for base, dirs, files in os.walk(PARENT):
    here = Path(base)
    dirs[:] = [name for name in dirs if name not in ['.git', 'node_modules', '.venv', '__pycache__', 'target', 'dist'] and not (here / name).is_symlink() and (here / name).resolve() != ROOT]
    for name in files:
        p = here / name
        if p.is_symlink() or name.startswith('.env') or name in {'auth.json', 'credentials.json', 'id_rsa', 'id_ed25519'}:
            continue
        try:
            info = p.stat()
        except FileNotFoundError:
            continue
        if info.st_mtime >= since:
            rel = str(p.relative_to(PARENT))
            key = p.relative_to(PARENT).parts[0]
            recent.setdefault(key, []).append({'path': rel, 'size': info.st_size, 'mtime': datetime.datetime.fromtimestamp(info.st_mtime).astimezone().isoformat()})
parent_status = subprocess.check_output(['git', '-C', str(PARENT), 'status', '--porcelain', '-uall'], cwd=ROOT, text=True)
parent_wave = PARENT / '.ufo/waves/round-100'
strays = []
if parent_wave.exists():
    for base, dirs, files in os.walk(parent_wave):
        dirs[:] = [name for name in dirs if not (Path(base) / name).is_symlink()]
        for name in files:
            p = Path(base) / name
            strays.append({'path': str(p), 'size': p.stat().st_size})
report = {'timestamp': datetime.datetime.now().astimezone().isoformat(), 'since': datetime.datetime.fromtimestamp(since).astimezone().isoformat(), 'sweep_root': str(PARENT), 'parent_git_status': parent_status, 'parent_round100_wave_exists': parent_wave.exists(), 'parent_round100_strays': strays, 'recent_counts': {key: len(value) for key, value in recent.items()}, 'recent': recent}
(S / 'outside.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))

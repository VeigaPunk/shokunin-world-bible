from pathlib import Path
import datetime
import hashlib
import json
import os
import stat
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
S = ROOT / '.ufo/waves/round-100/seats/V28-scratch'
BASE = 'fe1ce466e9d7427948c0abe4ecfbf961880b72ff'
assert Path.cwd().resolve() == ROOT
ready = json.loads((S / 'ready-manifest.json').read_text())
assert all(list(S.parent.glob(f'T{i}-*.md')) for i in range(1, 5))

def git(*args):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True)
    return r.stdout

def old(name):
    return git('show', f'{BASE}:{name}')

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def oid(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()

out = {'timestamp': datetime.datetime.now().astimezone().isoformat(), 'baseline': BASE, 'head': git('rev-parse', 'HEAD').decode().strip(), 'ready_at': ready['ready_at']}
chars = {}
for name in ['PROVINCE.md', 'SHONEN.md', 'README.md', 'l0-questions.md', 'corpus/fixtures/check_bible.py', 'corpus/tools/dependency_freeze.py', 'corpus/tools/map_obligations.py', 'corpus/tools/support_check.py', 'corpus/tools/boundary_doc_check.py']:
    a, b = old(name), (ROOT / name).read_bytes()
    chars[name] = {'identical': a == b, 'base_sha256': sha(a), 'work_sha256': sha(b), 'base_blob': oid(a), 'work_blob': oid(b)}
out['charter_and_tools'] = chars
tracked = []
changed = []
missing = []
symlinks = []
for record in git('ls-tree', '-rz', BASE).split(b'\0'):
    if not record:
        continue
    meta, name_b = record.split(b'\t', 1)
    name = name_b.decode()
    mode, kind, expected = meta.decode().split()
    if name.startswith('.ufo/'):
        continue
    if any(part.startswith('.env') or part in {'id_rsa', 'id_ed25519', 'credentials.json', 'auth.json'} for part in Path(name).parts):
        raise RuntimeError(f'sensitive path excluded from audit: {name}')
    if kind != 'blob':
        continue
    tracked.append(name)
    p = ROOT / name
    if p.is_symlink():
        symlinks.append(name)
        raw = os.readlink(p).encode()
    elif p.is_file():
        raw = p.read_bytes()
    else:
        missing.append(name)
        continue
    if oid(raw) != expected:
        changed.append(name)
out['tracked_non_ufo'] = {'count': len(tracked), 'changed': changed, 'missing': missing, 'symlinks': symlinks}
others = [p.decode() for p in git('ls-files', '--others', '--exclude-standard', '-z').split(b'\0') if p]
out['untracked'] = {'total': len(others), 'non_ufo': [p for p in others if not p.startswith('.ufo/')], 'outside_round_wave': [p for p in others if p.startswith('.ufo/') and not p.startswith('.ufo/waves/round-100/')]}
out['git_diff_head'] = git('diff', '--name-status', 'HEAD').decode()
out['git_diff_base_numstat'] = git('diff', '--numstat', BASE).decode()
out['git_diff_charter_bytes'] = len(git('diff', BASE, '--', 'PROVINCE.md'))
out['past_waves_tracked_changes'] = git('diff', '--name-only', BASE, '--', '.ufo').decode()
fixture = ROOT / 'corpus/fixtures/r100-docket-review'
prior = ROOT / 'corpus/fixtures/r99-window-lapse'
expected_files = ['README.md', 'claim-excerpt-map.md', 'contradictions.json', 'entities.json', 'fictional-excerpts.md', 'inspiration-note.md', 'relations.json', 'source-excerpt.md', 'sources.json', 'timeline.json']
out['fixture_files'] = [{'name': p.name, 'mode': oct(stat.S_IMODE(p.lstat().st_mode)), 'symlink': p.is_symlink(), 'regular': p.is_file(), 'sha256': sha(p.read_bytes()) if p.is_file() and not p.is_symlink() else None} for p in sorted(fixture.iterdir())]
assert sorted(p.name for p in fixture.iterdir()) == expected_files
pres = {}
for name in ['entities.json', 'relations.json', 'contradictions.json', 'sources.json', 'timeline.json']:
    a = json.loads((prior / name).read_text())
    b = json.loads((fixture / name).read_text())
    pres[name] = {'before': len(a), 'after': len(b), 'inherited_value_equal': b[:len(a)] == a, 'whole_value_equal': a == b}
for name in ['entities.json', 'relations.json', 'contradictions.json']:
    pres[name]['byte_identical'] = (prior / name).read_bytes() == (fixture / name).read_bytes()
for name in ['inspiration-note.md', 'source-excerpt.md']:
    pres[name] = {'byte_identical': (prior / name).read_bytes() == (fixture / name).read_bytes()}
a, b = (prior / 'fictional-excerpts.md').read_bytes(), (fixture / 'fictional-excerpts.md').read_bytes()
pres['fictional-excerpts.md'] = {'before_bytes': len(a), 'after_bytes': len(b), 'strict_byte_prefix': b.startswith(a) and len(b) > len(a)}
out['preservation'] = pres
out['fixture_counts'] = {p.stem: len(json.loads(p.read_text())) for p in fixture.glob('*.json')}
out['new_sources'] = json.loads((fixture / 'sources.json').read_text())[8:]
out['new_events'] = json.loads((fixture / 'timeline.json').read_text())[8:]
out['source_kinds'] = [x['kind'] for x in json.loads((fixture / 'sources.json').read_text())]
out['contradictions'] = json.loads((fixture / 'contradictions.json').read_text())
contract_name = 'corpus/tools/dependency-freeze-contract.json'
a, b = json.loads(old(contract_name)), json.loads((ROOT / contract_name).read_text())
out['contract'] = {'schema_version': b.get('schema_version'), 'payload_schema_version': b.get('payload_schema_version'), 'pin_count': len(b['pins']), 'added_pins': sorted(set(b['pins']) - set(a['pins'])), 'removed_pins': sorted(set(a['pins']) - set(b['pins'])), 'prior_pins_changed': [name for name in a['pins'] if b['pins'].get(name) != a['pins'][name]], 'other_top_level_changes': [name for name in set(a) | set(b) if name not in ['pins', 'revision'] and a.get(name) != b.get(name)], 'before_revision': a.get('revision'), 'after_revision': b.get('revision'), 'pins': {name: {'fixture': pin.get('fixture'), 'file_count': len(pin.get('files', {})), 'payload_schema_version': pin.get('payload_schema_version'), 'digest': pin.get('content_sha256'), 'inside_fixture_scope': (ROOT / pin['fixture']).resolve().is_relative_to(ROOT / 'corpus/fixtures')} for name, pin in b['pins'].items()}}
for name in ['corpus/tools/README.md', 'corpus/knowledge/r99-gate-blind-spot-table.md', 'LOG.md', 'SCORECARD.md']:
    a, b = old(name), (ROOT / name).read_bytes()
    out.setdefault('append_only', {})[name] = {'baseline_prefix': b.startswith(a), 'baseline_bytes': len(a), 'current_bytes': len(b), 'worktree_matches_head': git('show', f'HEAD:{name}') == b}
a, b = old('SKILL.md'), (ROOT / 'SKILL.md').read_bytes()
marker = b'### Dependency-edge freeze check\n'
out['skill_freeze_row_only'] = a.count(marker) == b.count(marker) == 1 and a.split(marker)[0] == b.split(marker)[0] and b'\n## ' not in b.split(marker)[-1] and b'\n### ' not in b.split(marker)[-1]
scan_names = ['SKILL.md', 'corpus/tools/README.md', contract_name, 'corpus/knowledge/r99-gate-blind-spot-table.md']
scan = b''
for name in scan_names:
    scan += f'\n=== DIFF {name} ===\n'.encode() + git('diff', '--unified=0', BASE, '--', name)
for name in ['corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md'] + [str(p.relative_to(ROOT)) for p in sorted(fixture.iterdir())]:
    scan += f'\n=== FULL {name} ===\n'.encode() + (ROOT / name).read_bytes()
(S / 'round-new-bytes.txt').write_bytes(scan)
out['scan'] = {'path': str((S / 'round-new-bytes.txt').relative_to(ROOT)), 'bytes': len(scan), 'sha256': sha(scan)}
owned = {'T1': ['corpus/tools/dependency-freeze-contract.json', 'corpus/tools/README.md', 'SKILL.md'], 'T2': [f'corpus/fixtures/r100-docket-review/{name}' for name in expected_files if name not in ['README.md', 'claim-excerpt-map.md']], 'T3': ['corpus/fixtures/r100-docket-review/README.md', 'corpus/fixtures/r100-docket-review/claim-excerpt-map.md'], 'T4': ['corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md', 'corpus/knowledge/r99-gate-blind-spot-table.md']}
for seat, paths in owned.items():
    report = max(S.parent.glob(f'{seat}-*.md'), key=lambda p: p.stat().st_mtime_ns)
    stamp = report.stat().st_mtime_ns
    out.setdefault('report_order', {})[seat] = {'report': str(report.relative_to(ROOT)), 'report_mtime': datetime.datetime.fromtimestamp(stamp / 1e9).astimezone().isoformat(), 'artifact_max_mtime': datetime.datetime.fromtimestamp(max((ROOT / name).stat().st_mtime_ns for name in paths) / 1e9).astimezone().isoformat(), 'newer_than_report': [name for name in paths if (ROOT / name).stat().st_mtime_ns > stamp]}
out['changed_since_ready'] = [name for name, item in ready['files'].items() if not (ROOT / name).is_file() or sha((ROOT / name).read_bytes()) != item['sha256']]
out['fixture_directory_count'] = sum(p.is_dir() for p in (ROOT / 'corpus/fixtures').iterdir())
(S / 'audit.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))

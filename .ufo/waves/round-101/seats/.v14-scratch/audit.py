#!/usr/bin/env python3
"""V14 freshness audit — round-101 stale-pin sweep, entry metadata header, C9 state.
Read-only. Full log -> .v14-scratch/audit-output.txt; stdout is a compact summary.
"""
import hashlib, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
BASELINE = '6f86bf2'
os.chdir(ROOT)
LOG = []

def emit(*a):
    LOG.append(' '.join(str(x) for x in a))

def say(*a):
    line = ' '.join(str(x) for x in a)
    LOG.append(line)
    print(line, flush=True)

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def gitsha(rev, rel):
    r = subprocess.run(['git', 'show', f'{rev}:{rel}'], capture_output=True)
    return hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else None

# ---------- canonical digest map: corpus/ (no live/, no scratch) + root docs ----------
digest_map = {}
nfiles = 0
for dirpath, dirnames, filenames in os.walk('corpus'):
    dirnames[:] = [d for d in dirnames
                   if d != '__pycache__' and 'scratch' not in d.lower() and d != 'live']
    for fn in filenames:
        p = Path(dirpath) / fn
        try:
            if p.is_file() and p.stat().st_size < 4_000_000:
                digest_map.setdefault(sha(p), []).append(str(p))
                nfiles += 1
        except OSError:
            pass
for rel in ['SKILL.md', 'LOG.md', 'README.md', 'SCORECARD.md']:
    p = ROOT / rel
    if p.is_file():
        digest_map.setdefault(sha(p), []).append(rel)
        nfiles += 1
say(f'== SECTION 0: canonical map files={nfiles}')

NEW_BYTES = [
    'corpus/tools/dependency_freeze.py',
    'corpus/tools/dependency-freeze-contract.json',
    'corpus/tools/README.md',
    'SKILL.md',
    'corpus/knowledge/r101-r10-register-first-entry.md',
]
HEX64 = re.compile(r'\b[0-9a-f]{64}\b')

# ---------- 1. changed-byte inventory ----------
say(f'== SECTION 1: changed-byte inventory vs baseline {BASELINE}')
changed = {}
for rel in NEW_BYTES:
    p = ROOT / rel
    if not p.is_file() or not p.stat().st_size:
        say('MISSING', rel)
        continue
    cur, base = sha(p), gitsha(BASELINE, rel)
    changed[rel] = (cur == base)
    base_text = subprocess.run(['git', 'show', f'{BASELINE}:{rel}'],
                               capture_output=True, text=True).stdout if base else ''
    say(f'{"UNCHANGED" if cur == base else "CHANGED":9} {rel} cur={cur}')
say('CHANGED_COUNT', sum(1 for v in changed.values() if not v))

cpath = ROOT / 'corpus/tools/dependency-freeze-contract.json'
contract = json.loads(cpath.read_text())
base_contract = json.loads(subprocess.run(
    ['git', 'show', f'{BASELINE}:corpus/tools/dependency-freeze-contract.json'],
    capture_output=True).stdout)
pins = contract.get('pins', {})
agg = {pin.get('content_sha256') for pin in pins.values()}
base_agg = {pin.get('content_sha256') for pin in base_contract.get('pins', {}).values()}

# ---------- 2. digest-token sweep ----------
say('== SECTION 2: 64-hex tokens in new bytes')
for rel in NEW_BYTES:
    p = ROOT / rel
    if not p.is_file():
        continue
    unchanged = changed.get(rel, False)
    base_text = subprocess.run(['git', 'show', f'{BASELINE}:{rel}'],
                               capture_output=True, text=True).stdout
    for i, line in enumerate(p.read_text(errors='replace').splitlines(), 1):
        for m in HEX64.finditer(line):
            tok = m.group(0)
            if unchanged and tok in base_text:
                continue  # carried token in a byte-identical file
            if tok in agg:
                say(f'AGGREGATE {rel}:{i} {tok[:12]} (verified in SECTION 5)')
                continue
            where = digest_map.get(tok)
            if where:
                say(f'CUR {rel}:{i} {tok[:12]} n={len(where)} first={where[0]}')
            else:
                hist = tok in base_text
                say(f'NOTCURRENT {rel}:{i} {tok[:12]} '
                    f'{"carried-historical" if hist else "NEW-not-current"} ctx="{line.strip()[:150]}"')

# ---------- 3. pin integrity ----------
say('== SECTION 3: pins')
say('PIN_COUNT', len(pins), sorted(pins))
base_pins = base_contract.get('pins', {})
say('PINS_ADDED', sorted(k for k in pins if k not in base_pins),
    'PINS_REMOVED', sorted(k for k in base_pins if k not in pins))
field_changed = [k for k in pins if k in base_pins and pins[k] != base_pins[k]]
say('INHERITED_PINS_FIELDS_UNCHANGED', not field_changed, field_changed)
mismatch = []
for name, pin in sorted(pins.items()):
    fixdir = Path(pin['fixture'])
    bad = [f for f, want in sorted(pin.get('files', {}).items())
           if not (fixdir / f).is_file() or sha(fixdir / f) != want]
    if bad:
        mismatch.append((name, bad))
    emit(f'PIN {name} fixture={pin["fixture"]} files={len(pin.get("files", {}))} '
         f'payload_match={not bad} content_sha256={pin.get("content_sha256")}')
    say(f'PIN {name} files={len(pin.get("files", {}))} payload_match={not bad} '
        f'rev={str(pin.get("revision", ""))[:12]} agg={str(pin.get("content_sha256"))[:12]}')
say('PIN_PAYLOAD_MISMATCHES', mismatch)
say('TOPLEVEL_REVISION cur', contract.get('revision'),
    'base', base_contract.get('revision'))

# ---------- 4. self-test inventory + live run ----------
say('== SECTION 4: self-test')
st_new = contract.get('self_test', {}).get('expected', {})
st_base = base_contract.get('self_test', {}).get('expected', {})
say('CASE_COUNT base', len(st_base), 'new', len(st_new))
say('CASES_ADDED', [k for k in st_new if k not in st_base])
say('CASES_REMOVED', [k for k in st_base if k not in st_new])
say('CASES_CHANGED_VALUE',
    [k for k in st_new if k in st_base and st_new[k] != st_base[k]])
if 'repointed_edge' in st_new:
    say('NEW_CASE_REPOINTED_EDGE', json.dumps(st_new['repointed_edge']))
r = subprocess.run([sys.executable, 'corpus/tools/dependency_freeze.py', '--self-test'],
                   capture_output=True, text=True)
say('SELF_TEST_EXIT', r.returncode)
say('SELF_TEST_STDOUT', r.stdout.strip().replace('\n', ' | ')[:400])
if r.stderr.strip():
    say('SELF_TEST_STDERR', r.stderr.strip()[:300])

# ---------- 5. live chain verify ----------
say('== SECTION 5: live chain verify')
CHAIN = ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath',
         'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing',
         'r99-window-lapse', 'r100-docket-review']
ok = agg_match = 0
for name in CHAIN:
    r = subprocess.run([sys.executable, 'corpus/tools/dependency_freeze.py',
                        f'corpus/fixtures/{name}'], capture_output=True, text=True)
    lines = [l for l in r.stdout.strip().splitlines() if l.strip()]
    dig = next((l.split()[1] for l in lines if l.startswith('DIGEST ')), '')
    pin_agg = pins.get(name, {}).get('content_sha256')
    passed = r.returncode == 0 and 'RESULT PASS' in r.stdout
    am = bool(pin_agg) and dig == pin_agg
    ok += passed
    agg_match += am
    emit(f'CHAIN {name} exit={r.returncode} digest={dig} pin_agg={pin_agg} agg_match={am}')
    say(f'CHAIN {name} exit={r.returncode} {"PASS" if passed else "FAIL"} '
        f'agg_match={am} dig={dig[:12]}')
say(f'CHAIN_CLEAN {ok}/{len(CHAIN)} AGG_MATCH {agg_match}/{len(CHAIN)}')

# ---------- 6. count-claim scan ----------
say('== SECTION 6: count-claim scan in owned docs')
PAT = re.compile(r'(18/18|18 cases|18 persisted|18 expectation|SELF-TEST 18|'
                 r'seven fixtures|seven-fixture|seven chain|chain of seven|chain seven|'
                 r'seven files|six-fixture|6/6\b|7/7\b|five JSON|five-JSON|'
                 r'ten files|ten-file|eight fixtures|eight-fixture|19/19|19 cases|'
                 r'19 persisted|19 expectation|SELF-TEST 19|eight chain)', re.I)
for rel in ['corpus/tools/README.md', 'SKILL.md',
            'corpus/knowledge/r101-r10-register-first-entry.md']:
    p = ROOT / rel
    if not p.is_file():
        say('MISSING', rel)
        continue
    base_text = subprocess.run(['git', 'show', f'{BASELINE}:{rel}'],
                               capture_output=True, text=True).stdout
    hits = new_hits = 0
    for i, line in enumerate(p.read_text(errors='replace').splitlines(), 1):
        if PAT.search(line):
            hits += 1
            emit(f'COUNT {rel}:{i}: {line.strip()[:200]}')
            if line not in base_text:
                new_hits += 1
    say(f'COUNT_HITS {rel}: total={hits} new-vs-baseline={new_hits} (lines in log)')

# ---------- 7. entry metadata header ----------
say('== SECTION 7: entry metadata header')
ENTRY = ROOT / 'corpus/knowledge/r101-r10-register-first-entry.md'
if ENTRY.is_file():
    body = ENTRY.read_text(errors='replace')
    lines = body.splitlines()
    for i, line in enumerate(lines[:30], 1):
        if re.match(r'^(source|verified-at|recheck|citation-convention):', line):
            say(f'HEADER:{i}: {line.strip()[:260]}')
    for k in ('source:', 'verified-at:', 'recheck:'):
        say('HAS_HEADER', k, any(l.startswith(k) for l in lines[:30]))
    for c in sorted(set(re.findall(r'(?:corpus|\.ufo)/[A-Za-z0-9_./-]+', body))):
        cq = c.rstrip('.').rstrip(',')
        (emit(f'CITED_PATH {cq} EXISTS') if (ROOT / cq).is_file()
         else say('CITED_PATH_MISSING', cq))
    vat = re.search(r'verified-at:\s*([0-9-]{10})', body)
    say('VERIFIED_AT', vat.group(1) if vat else 'ABSENT')
    say('ENTRY_LINES', len(lines))
else:
    say('ENTRY_ABSENT')

# ---------- 8. C9 ----------
say('== SECTION 8: C9 watch')
WATCH = 'corpus/knowledge/r91-c9-watch.md'
wtext = (ROOT / WATCH).read_text(errors='replace')
rows = re.findall(r'Next re-check:\s*r(\d+)', wtext)
say('C9_NEXT_RECHECK_TAIL', ('r' + rows[-1]) if rows else 'ABSENT')
say('C9_BASELINE_EQUAL', sha(ROOT / WATCH) == gitsha(BASELINE, WATCH))
cb = ROOT / 'corpus/fixtures/check_bible.py'
say('CHECKER_SHA', sha(cb))
say('C9_R101_ROW_PRESENT', bool(re.search(r'\(r101\)', wtext)))

(Path('.ufo/waves/round-101/seats/.v14-scratch/audit-output.txt')
 .write_text('\n'.join(LOG) + '\n'))
say('AUDIT_DONE log_bytes', len('\n'.join(LOG)))

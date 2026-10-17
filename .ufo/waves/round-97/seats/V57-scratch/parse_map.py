import re, sys, json

def rows(path):
    text = open(path, encoding='utf-8').read()
    out = {}
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if not cells or not re.fullmatch(r'J\d{2}', cells[0]):
            continue
        out[cells[0]] = cells
    return out

a = rows(sys.argv[1]); b = rows(sys.argv[2])
print('rows A:', len(a), 'rows B:', len(b))
keys = sorted(set(a) | set(b))
diffs = 0
for k in keys:
    if k not in a: print(k, 'ONLY-B'); diffs += 1; continue
    if k not in b: print(k, 'ONLY-A'); diffs += 1; continue
    ca, cb = a[k], b[k]
    if ca == cb:
        continue
    if len(ca) != len(cb):
        print(k, 'CELL-COUNT', len(ca), len(cb)); diffs += 1; continue
    changed = [i for i, (x, y) in enumerate(zip(ca, cb)) if x != y]
    print(k, 'changed-cell-indexes', changed)
    for i in changed:
        print('   A:', ca[i]); print('   B:', cb[i])
    diffs += 1
print('DIFF-ROWS', diffs)

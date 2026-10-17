import re, sys

def rows(path):
    lines = open(path).read().splitlines()
    # JSON facts section only
    start = [k for k, l in enumerate(lines) if re.match(r'^##\s+JSON facts', l)][0]
    end = next(k for k in range(start + 1, len(lines)) if re.match(r'^#{1,6}\s+', lines[k]))
    out = []
    for l in lines[start:end]:
        if not l.lstrip().startswith('|'):
            continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if all(set(c) <= set('-: ') for c in cells):
            continue
        if cells[0] == 'ID':
            continue
        out.append(cells)
    return out

r95 = rows('corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md')
r96 = rows('corpus/fixtures/r96-crossing-response/claim-excerpt-map.md')
print(f'r95 rows={len(r95)} r96 rows={len(r96)}')
if len(r96) != len(r95) + 1:
    print('UNEXPECTED ROW COUNT'); sys.exit(1)
diff = 0
for a, b in zip(r95, r96):
    if a != b:
        diff += 1
        print(f'ROW {a[0]} differs:')
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print(f'  col{i}: r95={x!r}')
                print(f'  col{i}: r96={y!r}')
print(f'identical inherited rows: {len(r95) - diff}/{len(r95)}')
print(f'new row: {r96[-1][0]} :: {r96[-1][1]}')

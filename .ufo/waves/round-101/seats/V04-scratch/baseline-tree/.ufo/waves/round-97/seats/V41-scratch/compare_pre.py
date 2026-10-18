import json
import pathlib
import sys

v21_path = pathlib.Path(sys.argv[1])
mine_path = pathlib.Path(sys.argv[2])

v21 = {}
for line in v21_path.read_text().splitlines():
    if not line.strip():
        continue
    d, rc, n = line.split('\t')
    name = d.split('/')[-1]
    v21[name] = (int(rc), int(n))

mine = {}
for line in mine_path.read_text().splitlines():
    row = json.loads(line)
    if 'summary' in row:
        continue
    mine[row['name']] = (row['exit'], row['lines_nonempty'])

only_v21 = sorted(set(v21) - set(mine))
only_mine = sorted(set(mine) - set(v21))
mismatch = []
for name in sorted(set(v21) & set(mine)):
    if v21[name] != mine[name]:
        mismatch.append((name, v21[name], mine[name]))
print(f'v21_dirs={len(v21)} mine_dirs={len(mine)}')
print(f'only_v21={only_v21}')
print(f'only_mine={only_mine}')
print(f'rc_or_lines_mismatches={len(mismatch)}')
for m in mismatch[:30]:
    print('MISMATCH', m)

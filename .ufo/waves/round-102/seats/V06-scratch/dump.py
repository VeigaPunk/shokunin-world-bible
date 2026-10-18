import json, sys
r, f = sys.argv[1], sys.argv[2]
d = json.load(open(f))
with open(f'/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-102/seats/V06-scratch/src-r{r}.txt', 'w') as out:
    def w(line): out.write(str(line).rstrip() + '\n')
    if 'items' in d:
        for it in d['items']:
            w(f"{it['id']}\t{it.get('axis','')}\t{it['description'][:160]}\tEV: {str(it.get('evidence_pointer',''))[:160]}")
    else:
        for sec in ('bounds_new',):
            w(f'== {sec} ==')
            for it in d.get(sec, []): w(f"{it['id']}\t{it.get('axis','')}\t{it['summary'][:160]}\tEV: {str(it.get('evidence',''))[:160]}")
        w('== closure_items ==')
        for it in d.get('closure_items', []): w(str(it)[:200])
        for bucket, items in (d.get('bounds_carried') or {}).items():
            w(f'== carried/{bucket} ==')
            for it in items or []: w(str(it)[:200])
print(f'r{r} dumped')

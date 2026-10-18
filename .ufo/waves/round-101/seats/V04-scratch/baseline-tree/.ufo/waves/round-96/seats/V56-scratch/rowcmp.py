import re, sys
def rows(path):
    out={}
    for line in open(path, encoding='utf-8'):
        m=re.match(r'\|\s*(J\d+)\s*\|(.*)', line)
        if m:
            cells=[c.strip() for c in m.group(2).split('|')]
            out[m.group(1)]=cells
    return out
a=rows('corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md')
b=rows('corpus/fixtures/r96-crossing-response/claim-excerpt-map.md')
print('r95 rows:',len(a),'r96 rows:',len(b))
ids_a, ids_b = set(a), set(b)
print('only in r95:',sorted(ids_a-ids_b))
print('only in r96:',sorted(ids_b-ids_a))
common=sorted(ids_a & ids_b)
diff=[i for i in common if a[i]!=b[i]]
print('common rows:',len(common),'differing:',diff)
for i in diff:
    print('---',i); print(' r95:',a[i]); print(' r96:',b[i])

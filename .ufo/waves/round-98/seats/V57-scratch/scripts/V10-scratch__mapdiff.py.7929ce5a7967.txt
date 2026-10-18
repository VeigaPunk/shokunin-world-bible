import re, sys, os
REPO="/home/vgpnk/Projects/shokunin/lore-shokunin"
def rows(p):
    out=[]
    for ln in open(p,encoding="utf-8"):
        if ln.startswith("| J"):
            cells=[c.strip() for c in ln.rstrip("\n").strip("|").split("|")]
            out.append(cells)
    return out
a=rows(f"{REPO}/corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md")
b=rows(f"{REPO}/corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md")
print(f"r97 map JSON-fact rows={len(a)}  r98 map JSON-fact rows={len(b)}")
n=min(len(a),len(b))
diffcols={}
for i in range(n):
    if a[i]==b[i]: continue
    for c in range(max(len(a[i]),len(b[i]))):
        x=a[i][c] if c<len(a[i]) else "<none>"; y=b[i][c] if c<len(b[i]) else "<none>"
        if x!=y: diffcols.setdefault(c,[]).append((a[i][0],x,y))
print("columns differing across inherited rows (col idx -> count):",{k:len(v) for k,v in diffcols.items()})
for k,v in sorted(diffcols.items()):
    print(f" col {k}: {len(v)} rows; sample: {v[0][0]}: {v[0][1]!r} -> {v[0][2]!r}")
# per-row full-equality count
same=sum(1 for i in range(n) if a[i]==b[i])
print(f"byte-identical rows among first {n}: {same}")
# new rows
for i in range(n,len(b)):
    print("NEW ROW:", b[i][0], "|", b[i][1], "|", b[i][3])

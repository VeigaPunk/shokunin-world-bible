import re, os
note = open('corpus/knowledge/r96-response-scope-note.md', encoding='utf-8').read()
R96='corpus/fixtures/r96-crossing-response/'
R95='corpus/fixtures/r95-crossing-aftermath/'
R35='corpus/fixtures/r35-bell7-conflict/'
def resolve(name):
    if name.startswith('corpus/'): return name
    for d in (R96,R95,R35,'corpus/fixtures/','corpus/knowledge/'):
        if os.path.exists(d+name): return d+name
    return None
bad=0
for m in re.finditer(r'`([A-Za-z0-9_./-]+\.(?:json|md|py)):(\d+)(?:-(\d+))?`', note):
    p,a,b=m.group(1),int(m.group(2)),m.group(3)
    rp=resolve(p)
    if not rp: print("UNRESOLVED",m.group(0)); bad+=1; continue
    n=len(open(rp,encoding='utf-8').read().split("\n"))
    hi=int(b) if b else a
    status = "OK  " if hi<=n else "OOR "
    if hi>n: bad+=1
    print(status, m.group(0), "->", rp, f"({n} lines)")
print("BAD:",bad)

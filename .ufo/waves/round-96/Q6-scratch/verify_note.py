import re, os
note = open('corpus/knowledge/r96-response-scope-note.md', encoding='utf-8').read()
# tokens that look like corpus paths
toks = set(re.findall(r'`([A-Za-z0-9_./{},\-]+\.(?:json|md|py))`', note))
base = 'corpus/'
paths = set()
for t in toks:
    if t.startswith('corpus/'):
        paths.add(t)
# handle brace-expanded groups like corpus/fixtures/r96-crossing-response/{a.json,b.md}
for t in toks:
    m = re.match(r'^(.*/)\{([^}]+)\}$', t)
    if m:
        pre, names = m.group(1), m.group(2).split(',')
        for n in names:
            paths.add(pre + n)
missing = sorted(p for p in paths if not os.path.exists(p))
print("cited paths:", len(paths))
print("MISSING:", missing if missing else "none")
# line citations of the form `path:NN` or `path:NN-NN` or bare `:NN`
for m in re.finditer(r'`([A-Za-z0-9_./-]+\.(?:json|md|py)):(\d+)(?:-(\d+))?`', note):
    p, a, b = m.group(1), int(m.group(2)), m.group(3)
    p = p if p.startswith('corpus/') else None
    if not p or not os.path.exists(p):
        print("BAD-LINE-CITE", m.group(0)); continue
    n = len(open(p, encoding='utf-8').read().split("\n"))
    hi = int(b) if b else a
    print(("OK  " if hi <= n else "OOR "), m.group(0), f"(file lines {n})")

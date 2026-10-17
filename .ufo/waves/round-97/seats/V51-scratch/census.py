import json, subprocess, sys, os
def types_from_pairs(pairs):
    out = {}
    for path, text in pairs:
        try:
            data = json.loads(text)
        except Exception as e:
            out.setdefault("__parse_error__", []).append(f"{path}: {e}")
            continue
        rows = data if isinstance(data, list) else [data]
        for i, r in enumerate(rows):
            if not isinstance(r, dict):
                out.setdefault("__nondict__", []).append(f"{path}#/{i}")
                continue
            t = r.get("type")
            out.setdefault(t, []).append(f"{path}#/{i}")
    return out

def git_pairs():
    files = subprocess.run(["git","ls-tree","-r","--name-only","f3e09f9"],
                           capture_output=True, text=True, check=True).stdout.split()
    fs = [f for f in files if f.endswith("relations.json")]
    pairs = []
    for f in fs:
        text = subprocess.run(["git","show",f"f3e09f9:{f}"],capture_output=True,text=True,check=True).stdout
        pairs.append((f,text))
    return pairs

def wt_pairs():
    pairs = []
    for root, dirs, names in os.walk("corpus/fixtures"):
        for n in names:
            if n == "relations.json":
                p = os.path.join(root,n)
                pairs.append((p, open(p).read()))
    return pairs

for label, pairs in (("BASELINE f3e09f9", git_pairs()), ("WORKTREE", wt_pairs())):
    t = types_from_pairs(pairs)
    total = sum(len(v) for v in t.values())
    print(f"=== {label}: {len(pairs)} relations.json files, {total} rows, {len(t)} distinct types")
    for k in sorted(t, key=lambda x: (-len(t[x]), str(x))):
        print(f"  {len(t[k]):3d}  {k!r}")
    print()

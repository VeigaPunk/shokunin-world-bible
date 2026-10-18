import json, hashlib, os, sys, glob
ROOT = "corpus/fixtures"
CHAIN = ["r88-m3-maya-cluster","r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response"]
out = {}
for f in CHAIN:
    d = os.path.join(ROOT, f)
    rec = {"exists": os.path.isdir(d)}
    if not rec["exists"]:
        out[f] = rec; continue
    tl = json.load(open(os.path.join(d,"timeline.json")))
    edges = {e["id"]: sorted(e.get("depends_on", [])) for e in tl}
    rel = json.load(open(os.path.join(d,"relations.json")))
    eps = sorted([f'{r.get("from")}->{r.get("to")}:{r.get("type")}' for r in rel])
    files = {}
    for p in sorted(glob.glob(os.path.join(d,"*"))):
        if os.path.isfile(p):
            files[os.path.basename(p)] = hashlib.sha256(open(p,"rb").read()).hexdigest()
    rec.update({"n_events": len(tl), "edges": edges, "endpoints": eps, "n_relations": len(rel), "files": files})
    out[f] = rec
print(json.dumps(out, indent=2, sort_keys=True))

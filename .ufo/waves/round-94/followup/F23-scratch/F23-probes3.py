import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
SCRATCH = Path(__file__).resolve().parent
MAPOBL = ROOT / "corpus/tools/map_obligations.py"
SRC = ROOT / "corpus/fixtures/r93-m2-kojiki-cluster"
def run(cmd):
    p = subprocess.run([str(c) for c in cmd], cwd=ROOT, capture_output=True, text=True, check=False)
    return p.returncode, p.stdout, p.stderr
def show(label, c, o, e):
    term=[l for l in o.splitlines() if l.startswith("RESULT ")]
    found=[l for l in o.splitlines() if l.startswith("FINDING ")]
    print(f"{label}: exit={c} {term} {found[:4]}")
with tempfile.TemporaryDirectory(prefix="f23c-", dir=SCRATCH) as tmp:
    tmp=Path(tmp)
    # A. legacy bracket grammar, direct CLI
    p=tmp/"a"; shutil.copytree(SRC,p)
    mp=p/"claim-excerpt-map.md"
    mp.write_text(mp.read_text(encoding="utf-8").replace("`entities.json#/0/first_appearance`","`entities[0].first_appearance`"),encoding="utf-8")
    c,o,e=run([sys.executable,"-B",MAPOBL,p]); show("A legacy bracket grammar",c,o,e)
    # B. co-mapped grammar, direct CLI
    p=tmp/"b"; shutil.copytree(SRC,p)
    mp=p/"claim-excerpt-map.md"
    mp.write_text(mp.read_text(encoding="utf-8").replace("`entities.json#/0/first_appearance`","`entities.json#/0/first_appearance; relations.json#/0`"),encoding="utf-8")
    c,o,e=run([sys.executable,"-B",MAPOBL,p]); show("B co-mapped grammar",c,o,e)
    # C. residual: entity claims under a non-canonical key AND its map rows removed
    p=tmp/"c"; shutil.copytree(SRC,p)
    ep=p/"entities.json"; ents=json.loads(ep.read_text(encoding="utf-8"))
    ents[0]["claim_list"]=ents[0].pop("claims")
    ep.write_text(json.dumps(ents,indent=2)+"\n",encoding="utf-8")
    mp=p/"claim-excerpt-map.md"; lines=mp.read_text(encoding="utf-8").splitlines()
    lines=[l for l in lines if "entities.json#/0/claims/0" not in l]
    mp.write_text("\n".join(lines)+"\n",encoding="utf-8")
    c,o,e=run([sys.executable,"-B",MAPOBL,p]); show("C renamed claims key + row removed",c,o,e)
    # C2. same, map rows NOT removed -> phantom should fire
    p=tmp/"c2"; shutil.copytree(SRC,p)
    ep=p/"entities.json"; ents=json.loads(ep.read_text(encoding="utf-8"))
    ents[0]["claim_list"]=ents[0].pop("claims")
    ep.write_text(json.dumps(ents,indent=2)+"\n",encoding="utf-8")
    c,o,e=run([sys.executable,"-B",MAPOBL,p]); show("C2 renamed claims key, rows kept",c,o,e)
    # D. claims key as dict (wrong type) -> should be ERROR
    p=tmp/"d"; shutil.copytree(SRC,p)
    ep=p/"entities.json"; ents=json.loads(ep.read_text(encoding="utf-8"))
    ents[0]["claims"]={"0": ents[0]["claims"][0]}
    ep.write_text(json.dumps(ents,indent=2)+"\n",encoding="utf-8")
    c,o,e=run([sys.executable,"-B",MAPOBL,p]); show("D claims as object",c,o,e)

import json, subprocess, sys, os
REPO="/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE="9a3d648"
R97="corpus/fixtures/r97-crossing-acknowledgment"
R98="corpus/fixtures/r98-clerk-filing"

def load_base(rel):
    out=subprocess.run(["git","show",f"{BASE}:{rel}"],cwd=REPO,capture_output=True)
    if out.returncode!=0: return None,None
    return out.stdout, json.loads(out.stdout)

def load_wt(rel):
    p=os.path.join(REPO,rel)
    if not os.path.exists(p): return None,None
    b=open(p,"rb").read()
    return b, json.loads(b)

fails=[]
def check(name,cond,detail=""):
    print(("PASS " if cond else "FAIL ")+name+((" :: "+detail) if detail else ""))
    if not cond: fails.append(name)

for f in ["entities.json","relations.json","timeline.json","sources.json","contradictions.json"]:
    b97,j97=load_base(f"{R97}/{f}")
    b98,j98=load_wt(f"{R98}/{f}")
    if j98 is None:
        print(f"ABSENT {R98}/{f}"); fails.append(f"{f} absent"); continue
    if f=="entities.json":
        check("entities len==6",len(j98)==6,f"got {len(j98)}")
        check("entities[:5] parsed-equal",j98[:5]==j97,f"r97 len {len(j97)}")
        check("entities[5].id==clerk-maren",len(j98)>5 and j98[5].get("id")=="clerk-maren",str(j98[5].get("id") if len(j98)>5 else None))
        check("entities[5].kind==character",len(j98)>5 and j98[5].get("kind")=="character","")
        check("entities[5] one claim citing new source",len(j98)>5 and len(j98[5].get("claims",[]))==1 and j98[5]["claims"][0].get("source_id")=="clerk-filing-note","")
        ids=[e.get("id") for e in j98]
        check("only new entity id",ids[:5]==[e.get("id") for e in j97],"")
    elif f=="relations.json":
        check("relations parsed-equal (len 1)",j98==j97,f"r98 {j98}")
    elif f=="timeline.json":
        check("timeline len==7",len(j98)==7,f"got {len(j98)}")
        check("timeline[:6] parsed-equal",j98[:6]==j97,f"r97 len {len(j97)}")
        if len(j98)>6:
            t=j98[6]
            check("timeline[6].id==clerk-filing-open",t.get("id")=="clerk-filing-open",str(t.get("id")))
            check("timeline[6].tick==14",t.get("tick")==14,str(t.get("tick")))
            check("timeline[6].entity_id==clerk-maren",t.get("entity_id")=="clerk-maren",str(t.get("entity_id")))
            check("timeline[6].place_id==chalk-stair",t.get("place_id")=="chalk-stair",str(t.get("place_id")))
            check("timeline[6].depends_on==[acknowledgment-aru-records]",t.get("depends_on")==["acknowledgment-aru-records"],str(t.get("depends_on")))
            check("timeline[6].source_id==clerk-filing-note",t.get("source_id")=="clerk-filing-note",str(t.get("source_id")))
    elif f=="sources.json":
        check("sources len==7",len(j98)==7,f"got {len(j98)}")
        check("sources[:6] parsed-equal",j98[:6]==j97,f"r97 len {len(j97)}")
        check("sources[6].id==clerk-filing-note",len(j98)>6 and j98[6].get("id")=="clerk-filing-note",str(j98[6].get("id") if len(j98)>6 else None))
    elif f=="contradictions.json":
        check("contradictions parsed-equal ([])",j98==j97,str(j98))
print("FAILS:",len(fails))
sys.exit(1 if fails else 0)

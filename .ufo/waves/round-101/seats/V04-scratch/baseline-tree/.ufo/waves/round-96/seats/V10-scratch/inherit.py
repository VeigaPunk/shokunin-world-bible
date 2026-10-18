import re, sys
def cells(line): return [c.strip() for c in line.strip().strip("|").split("|")]
def norm(v): return re.sub(r"[^a-z0-9]+"," ",v.strip().strip("`").lower()).strip()
def roles(headers):
    r={}
    for i,h in enumerate(headers):
        n=norm(h)
        if n in {"fact","fact id","fact identifier","id","claim pointer","claim id"}: r.setdefault("id",i)
        elif "delivery mode" in n or n.endswith(" mode") or n in {"mode","mode author"}: r.setdefault("mode",i)
        elif "anchor" in n: r.setdefault("anchor",i)
        elif "excerpt" in n and ("path" in n or n=="excerpt"): r.setdefault("path",i)
        elif n in {"line","lines","line span","excerpt lines","line numbers"}: r.setdefault("span",i)
    return r
def parse(path):
    lines=open(path).read().splitlines()
    rows={}; section=None; i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith("## "):
            h=norm(line[3:])
            section="json" if re.match(r"json facts(?:$| )",h) else ("editorial" if re.match(r"editorial rows(?:$| )",h) else None)
        if line.lstrip().startswith("|"):
            headers=cells(line); r=roles(headers)
            if {"mode","path"}.issubset(r) and {"id","anchor"}.issubset(r):
                j=i+1
                while j<len(lines) and lines[j].lstrip().startswith("|"):
                    row=cells(lines[j])
                    if row and all(re.fullmatch(r":?-{3,}:?",c.replace(" ","")) for c in row):
                        j+=1; continue
                    if len(row)==len(headers):
                        fid=row[r["id"]].strip().strip("`")
                        rows[fid]={"kind":section,"id":fid,"mode":row[r["mode"]].strip().strip("`"),
                                   "path":row[r["path"]].strip().strip("`"),
                                   "span":row[r["span"]].strip().strip("`") if "span" in r else "",
                                   "anchor":row[r["anchor"]].strip().strip("`"),
                                   "src":row[2].strip().strip("`") if len(row)>2 else "",
                                   "ptr":row[1].strip().strip("`") if len(row)>1 else ""}
                    j+=1
                i=j; continue
        i+=1
    return rows
old=parse(sys.argv[1]); new=parse(sys.argv[2])
print("old rows",len(old),"new rows",len(new))
same=0; diff=[]
for k,v in old.items():
    if k not in new: diff.append((k,"MISSING in new")); continue
    n=new[k]
    keys=["kind","mode","path","span","anchor"]
    d={key:(v[key],n[key]) for key in keys if v[key]!=n[key]}
    # pointer: compare ignoring namespace prefix
    def tail(p):
        p=p.strip().strip("`")
        m=re.match(r"^[^:]+:(.*)$",p)
        return m.group(1) if m and ":" in p else p
    if tail(v["ptr"])!=tail(n["ptr"]): d["ptr"]=(v["ptr"],n["ptr"])
    if v["src"]!=n["src"]: d["src"]=(v["src"],n["src"])
    if d: diff.append((k,d))
    else: same+=1
print("parse-value identical inherited rows:",same)
new_rows=[k for k in new if k not in old]
print("new rows:",new_rows)
for k,d in diff: print("DIFF",k,d)

import subprocess, tarfile, tempfile, os, hashlib, sys, json
REF = sys.argv[1] if len(sys.argv)>1 else 'dcb2d92'
root = 'corpus/fixtures'
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda: f.read(65536), b''): h.update(b)
    return h.hexdigest()
with tempfile.TemporaryDirectory() as td:
    tar = subprocess.run(['git','archive','--format=tar',REF,root],capture_output=True,check=True).stdout
    with open(os.path.join(td,'a.tar'),'wb') as f: f.write(tar)
    with tarfile.open(os.path.join(td,'a.tar')) as t: t.extractall(td)
    base=os.path.join(td,root)
    def walk(d):
        out={}
        for dp,dn,fn in os.walk(d):
            for x in fn: 
                p=os.path.join(dp,x); out[os.path.relpath(p,d)]=sha(p)
        return out
    b=walk(base); w=walk(root)
    bdirs=sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base,d)))
    wdirs=sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root,d)))
    mod=sorted(k for k in b if k in w and b[k]!=w[k])
    dele=sorted(k for k in b if k not in w)
    new=sorted(k for k in w if k not in b)
    print(json.dumps({'ref':REF,'baseline_top_dirs':len(bdirs),'work_top_dirs':len(wdirs),
      'baseline_files':len(b),'work_files':len(w),'modified':mod,'deleted':dele,'new':new,
      'new_top_dirs':sorted(set(wdirs)-set(bdirs)),'verdict':'PASS' if not mod and not dele else 'FAIL'},indent=1))

import hashlib, json, subprocess, sys, os
os.chdir('/home/vgpnk/Projects/shokunin/lore-shokunin')
def sha(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()
def git(*a):
    return subprocess.run(['git']+list(a),capture_output=True,text=True)
BASE='542021a'
base_prov=subprocess.run(['git','show',BASE+':PROVINCE.md'],capture_output=True).stdout
head_prov=subprocess.run(['git','show','HEAD:PROVINCE.md'],capture_output=True).stdout
work_prov=open('PROVINCE.md','rb').read()
h=lambda b: hashlib.sha256(b).hexdigest()
print('PROVINCE_BASE_SHA256 ',h(base_prov))
print('PROVINCE_HEAD_SHA256 ',h(head_prov))
print('PROVINCE_WORK_SHA256 ',h(work_prov))
print('PROVINCE_IDENT_BASE_WORK', base_prov==work_prov)
print('PROVINCE_IDENT_HEAD_WORK', head_prov==work_prov)
tr=[l for l in git('diff','--name-only','HEAD').stdout.splitlines() if l]
un=[l for l in git('ls-files','--others','--exclude-standard').stdout.splitlines() if l]
print('TRACKED_CHANGES',json.dumps(tr))
print('UNTRACKED',json.dumps(un))
U1={'corpus/knowledge/r102-push-synthesis-r95-r102.md','corpus/knowledge/r102-debt-ledger.json'}
U2_AUTH={'corpus/knowledge/r102-freshness-sweep.md'}
# U2 also owns dated correction addenda in knowledge files -> any tracked M under corpus/knowledge/*.md is U2-candidate
u2_addenda={p for p in tr if p.startswith('corpus/knowledge/') and p.endswith('.md') and p not in U1|U2_AUTH}
unauth_tr=[p for p in tr if p not in U1|U2_AUTH|u2_addenda]
unauth_un=[p for p in un if not (p.startswith('.ufo/waves/round-102/seats/') or p in U1|U2_AUTH|u2_addenda or p=='.scratch/' or p.startswith('.scratch/'))]
# pre-existing stray from earlier rounds
stray='.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md'
print('U2_ADDENDA_CANDIDATES',json.dumps(sorted(u2_addenda)))
print('UNAUTHORIZED_TRACKED',json.dumps(sorted(unauth_tr)))
print('UNTRACKED_OUTSIDE',json.dumps(sorted(p for p in unauth_un if p!=stray)))
print('PREEXISTING_STRAY_PRESENT', stray in un)
print('HEAD', git('log','--oneline','-1').stdout.strip())
print('PUSH_REMOTE', git('log','--oneline','origin/main..HEAD' if git('rev-parse','--verify','origin/main').returncode==0 else 'HEAD').stdout.count(chr(10)))

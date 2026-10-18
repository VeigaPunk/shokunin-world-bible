# V06 — C2 inherited equality and byte preservation (2026-10-17)

Scope: T2's delivered fixture payload, not a round-wide admission verdict. Axes: depth preservation, byte provenance, evidence completeness. Read the r100 declaration in `LOG.md:3349-3404` and producer report `.ufo/waves/round-100/seats/T2-fixture-author.md` before adjudicating. All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`; subprocess commands are quoted exactly as invoked. No corpus bytes, scratch files, commits, pushes, network calls, or nested agents were produced by V06. The only V06-created file is this report.

## Result

- All 23 inherited top-level JSON rows are parsed-value identical at their original indices, including every nested field and JSON type: entities 6/6, relations 1/1, sources 8/8, timeline 8/8. `contradictions.json` remains exactly `[]` (zero inherited rows, zero additions).
- Exactly one source and one event were appended; counts are 6 entities / 1 relation / 9 events / 9 sources / 0 contradictions, with 22 raw source-attributed obligations.
- Five preserved payload files pass whole-file `cmp`: entities, relations, contradictions, source excerpt, inspiration note.
- All 5,114 r99 excerpt bytes (76 lines) pass prefix `cmp`; r100 appends 847 bytes, making 5,961 bytes total.
- All ten files of `r99-window-lapse` remain byte-identical to closure commit `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`, with no extra or deleted files. This was checked before and after T2 landed.
- The delivered r100 fixture returns `CLEAN: schema, citations, relations, timeline; 0 violations`.

## Producer-artifact poll

The bounded protocol required both T2's eight payload files and its report, not just the fixture directory. Exact poll command (exit 0 after check 6; 100 seconds elapsed):

```sh
python3 -u - <<'PY'
from pathlib import Path
import time
root = Path.cwd().resolve()
assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
fixture = root/'corpus/fixtures/r100-docket-review'
seats = root/'.ufo/waves/round-100/seats'
required=['entities.json','relations.json','sources.json','timeline.json','contradictions.json','fictional-excerpts.md','inspiration-note.md','source-excerpt.md']
for attempt in range(1,41):
    missing=[name for name in required if not (fixture/name).is_file()]
    reports=sorted(p for p in seats.glob('T2*.md') if p.is_file())
    ready=not missing and bool(reports)
    print(f'POLL {attempt}/40 ready={ready} missing={missing} T2_reports={[p.name for p in reports]}', flush=True)
    if ready:
        print('READY: T2 artifacts and producer report exist',flush=True)
        break
    if attempt<40: time.sleep(20)
else:
    print('ABSENT: T2 artifacts/report missing after 40 checks',flush=True)
PY
```

Observed:

```text
POLL 1/40 ready=False missing=['entities.json', 'relations.json', 'sources.json', 'timeline.json', 'contradictions.json', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md'] T2_reports=[]
POLL 2/40 ready=False missing=[] T2_reports=[]
POLL 3/40 ready=False missing=[] T2_reports=[]
POLL 4/40 ready=False missing=[] T2_reports=[]
POLL 5/40 ready=False missing=[] T2_reports=[]
POLL 6/40 ready=True missing=[] T2_reports=['T2-fixture-author.md']
READY: T2 artifacts and producer report exist
```

No all-reports poll, self-dependency, or stall escape was used.

## Strict inherited-row replay

The comparator rejects duplicate object members, compares complete rows rather than selected fields, preserves array order, and distinguishes JSON value types. Exact command (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, json
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
old=root/'corpus/fixtures/r99-window-lapse'
new=root/'corpus/fixtures/r100-docket-review'
def unique(pairs):
    result={}
    for key,value in pairs:
        if key in result: raise ValueError('duplicate member: '+key)
        result[key]=value
    return result
def same(a,b):
    if type(a) is not type(b): return False
    if isinstance(a,dict): return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list): return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b
expected={'entities':(6,6),'relations':(1,1),'contradictions':(0,0),'sources':(8,9),'timeline':(8,9)}
data={}
total=0
for name,counts in expected.items():
    before=json.loads((old/(name+'.json')).read_bytes(),object_pairs_hook=unique)
    after=json.loads((new/(name+'.json')).read_bytes(),object_pairs_hook=unique)
    assert (len(before),len(after))==counts,(name,'counts')
    assert same(before,after[:len(before)]),(name,'parsed prefix')
    if name not in ('sources','timeline'): assert same(before,after),(name,'unexpected addition')
    for i,row in enumerate(before):
        assert same(row,after[i]),(name,i)
        label=row.get('id',row.get('type','(no id)'))
        print(f'ROW PASS {name}.json#/{i} {label}')
    if name in ('entities','sources','timeline'):
        ids=[row['id'] for row in after]
        assert len(set(ids))==len(ids),(name,'duplicate IDs')
    print(f'TABLE PASS {name}.json inherited={len(before)}/{len(before)} appended={len(after)-len(before)}')
    total+=len(before)
    data[name]=after
assert data['sources'][-1]['id']=='clerk-review-note'
review=data['timeline'][-1]
assert {k:review[k] for k in ('id','tick','entity_id','place_id','depends_on','source_id')}=={'id':'clerk-review-first-passage','tick':16,'entity_id':'clerk-maren','place_id':'chalk-stair','depends_on':['clerk-lapse-recorded'],'source_id':'clerk-review-note'}
claims=sum(len(row['claims']) for row in data['entities'])
obligations=len(data['entities'])+claims+len(data['relations'])+len(data['timeline'])
assert obligations==22
print(f'INHERITED_ROWS PASS {total}/23 (nested values and JSON types included)')
print('ADDITIONS',json.dumps({'source_id':data['sources'][-1]['id'],'event':review},sort_keys=True))
print(f'INVENTORY entities={len(data["entities"])} relations={len(data["relations"])} events={len(data["timeline"])} sources={len(data["sources"])} contradictions={len(data["contradictions"])} obligations={obligations}')
for path in sorted(new.iterdir()):
    if path.is_file(): print('DELIVERED_SHA256',path.name,hashlib.sha256(path.read_bytes()).hexdigest())
PY
```

Observed complete stdout:

```text
ROW PASS entities.json#/0 aru
ROW PASS entities.json#/1 evin
ROW PASS entities.json#/2 quiet-rise
ROW PASS entities.json#/3 salt-court
ROW PASS entities.json#/4 chalk-stair
ROW PASS entities.json#/5 clerk-maren
TABLE PASS entities.json inherited=6/6 appended=0
ROW PASS relations.json#/0 agreed_co_stewardship_for_this_crossing
TABLE PASS relations.json inherited=1/1 appended=0
TABLE PASS contradictions.json inherited=0/0 appended=0
ROW PASS sources.json#/0 veil-verse
ROW PASS sources.json#/1 paired-clock
ROW PASS sources.json#/2 crossing-minute
ROW PASS sources.json#/3 aru-aftermath-note
ROW PASS sources.json#/4 evin-response-note
ROW PASS sources.json#/5 aru-acknowledgment-note
ROW PASS sources.json#/6 clerk-filing-note
ROW PASS sources.json#/7 clerk-lapse-note
TABLE PASS sources.json inherited=8/8 appended=1
ROW PASS timeline.json#/0 aru-ninth-bell
ROW PASS timeline.json#/1 evin-ninth-bell
ROW PASS timeline.json#/2 paired-crossing-decision
ROW PASS timeline.json#/3 aftermath-missing-evin
ROW PASS timeline.json#/4 response-evin-salt-court
ROW PASS timeline.json#/5 acknowledgment-aru-records
ROW PASS timeline.json#/6 clerk-filing-open
ROW PASS timeline.json#/7 clerk-lapse-recorded
TABLE PASS timeline.json inherited=8/8 appended=1
INHERITED_ROWS PASS 23/23 (nested values and JSON types included)
ADDITIONS {"event": {"depends_on": ["clerk-lapse-recorded"], "description": "At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.", "entity_id": "clerk-maren", "id": "clerk-review-first-passage", "place_id": "chalk-stair", "source_id": "clerk-review-note", "tick": 16}, "source_id": "clerk-review-note"}
INVENTORY entities=6 relations=1 events=9 sources=9 contradictions=0 obligations=22
DELIVERED_SHA256 README.md b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049
DELIVERED_SHA256 claim-excerpt-map.md d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d
DELIVERED_SHA256 contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
DELIVERED_SHA256 entities.json db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
DELIVERED_SHA256 fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
DELIVERED_SHA256 inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
DELIVERED_SHA256 relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
DELIVERED_SHA256 source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
DELIVERED_SHA256 sources.json effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
DELIVERED_SHA256 timeline.json 008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
```

## Byte-copy and prefix replay with cmp

Exact commands invoked through `python3` subprocesses and observed exit codes/output:

```text
$ cmp -s corpus/fixtures/r99-window-lapse/entities.json corpus/fixtures/r100-docket-review/entities.json
exit=0 stdout='' stderr=''
$ cmp -s corpus/fixtures/r99-window-lapse/relations.json corpus/fixtures/r100-docket-review/relations.json
exit=0 stdout='' stderr=''
$ cmp -s corpus/fixtures/r99-window-lapse/contradictions.json corpus/fixtures/r100-docket-review/contradictions.json
exit=0 stdout='' stderr=''
$ cmp -s corpus/fixtures/r99-window-lapse/source-excerpt.md corpus/fixtures/r100-docket-review/source-excerpt.md
exit=0 stdout='' stderr=''
$ cmp -s corpus/fixtures/r99-window-lapse/inspiration-note.md corpus/fixtures/r100-docket-review/inspiration-note.md
exit=0 stdout='' stderr=''
$ cmp -n 5114 corpus/fixtures/r99-window-lapse/fictional-excerpts.md corpus/fixtures/r100-docket-review/fictional-excerpts.md
exit=0 stdout='' stderr=''
BYTE_PREFIX PASS inherited_bytes=5114 appended_bytes=847 inherited_lines=76
$ cmp -s corpus/fixtures/r99-window-lapse/sources.json corpus/fixtures/r100-docket-review/sources.json
exit=1 stdout='' stderr=''
$ cmp -s corpus/fixtures/r99-window-lapse/timeline.json corpus/fixtures/r100-docket-review/timeline.json
exit=1 stdout='' stderr=''
CMP PASS: five whole-file copies equal; excerpt prefix equal; extended JSON files differ as expected
```

The wrapper additionally asserted `len(base)==5114`, `len(current)==5961`, and `current[len(base):].startswith(b'\n## Round 100 docket review note (2026-10-17)\n')`. The last two `cmp` exit-1 results are expected evidence of appended JSON content, not failures: the JSON inheritance claim is parsed-value equality, not whole-file byte identity or preservation of the closing array delimiter as a byte prefix. The excerpt's prefix claim is a literal byte-prefix claim and passes.

## r99 baseline immutability replay

Exact post-delivery command (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib,subprocess
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
rel=Path('corpus/fixtures/r99-window-lapse')
files=subprocess.check_output(['git','ls-tree','-r','--name-only','fe1ce46','--',str(rel)],text=True).splitlines()
assert len(files)==10
actual=sorted(str(p.relative_to(root)) for p in (root/rel).rglob('*') if p.is_file())
assert actual==sorted(files),('unexpected path set',actual)
for file in files:
    baseline=subprocess.check_output(['git','show',f'fe1ce46:{file}'])
    current=(root/file).read_bytes()
    assert current==baseline,file
    print('R99_BASELINE_BYTE_MATCH',Path(file).name,hashlib.sha256(current).hexdigest())
print('R99_BASELINE PASS files=10/10 extra_files=0 deleted_files=0')
args=['git','diff','--exit-code','fe1ce46','--',str(rel)]
result=subprocess.run(args,capture_output=True,text=True)
print('$ '+' '.join(args))
print(f'exit={result.returncode} stdout={result.stdout!r} stderr={result.stderr!r}')
assert result.returncode==0
PY
```

Observed:

```text
R99_BASELINE_BYTE_MATCH README.md b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049
R99_BASELINE_BYTE_MATCH claim-excerpt-map.md d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d
R99_BASELINE_BYTE_MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
R99_BASELINE_BYTE_MATCH entities.json db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
R99_BASELINE_BYTE_MATCH fictional-excerpts.md fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d
R99_BASELINE_BYTE_MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
R99_BASELINE_BYTE_MATCH relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
R99_BASELINE_BYTE_MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
R99_BASELINE_BYTE_MATCH sources.json 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15
R99_BASELINE_BYTE_MATCH timeline.json 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069
R99_BASELINE PASS files=10/10 extra_files=0 deleted_files=0
$ git diff --exit-code fe1ce46 -- corpus/fixtures/r99-window-lapse
exit=0 stdout='' stderr=''
```

The initial pre-delivery replay had also reported `BASELINE_R99 PASS files=10 mismatches=0`; its `git diff --exit-code fe1ce46 -- corpus/fixtures/r99-window-lapse` and `git ls-files --others --exclude-standard -- corpus/fixtures/r99-window-lapse` subprocesses both exited 0 with empty stdout/stderr. Byte identity is a state assertion at observation time, not a forensic claim that transient writes followed by restoration could be detected.

## Structural gate

Both actual commands exited 0:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Each independently printed:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

## Final stability check, report path, and verifier error record

The final path/stability command below exited 0 immediately before the report Write:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve()==root
report=root/'.ufo/waves/round-100/seats/V06-c2-inherited-equality.md'
assert report.resolve()==root/'.ufo/waves/round-100/seats/V06-c2-inherited-equality.md'
assert not report.exists()
assert not report.is_symlink()
print('REPORT_PATH_VERIFIED',report.resolve())
fixture=root/'corpus/fixtures/r100-docket-review'
expected={
'contradictions.json':'37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570',
'entities.json':'db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984',
'fictional-excerpts.md':'d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705',
'inspiration-note.md':'58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37',
'relations.json':'c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9',
'source-excerpt.md':'b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd',
'sources.json':'effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e',
'timeline.json':'008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8'}
for name,want in expected.items():
    assert hashlib.sha256((fixture/name).read_bytes()).hexdigest()==want,name
print('DELIVERED_INPUT_STABILITY PASS 8/8 T2-owned files unchanged since verification')
PY
```

Observed:

```text
REPORT_PATH_VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V06-c2-inherited-equality.md
DELIVERED_INPUT_STABILITY PASS 8/8 T2-owned files unchanged since verification
```

One earlier run of this same stability command failed because V06 transcribed the relations expected hash as the 55-character value `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9` instead of its actual 64-character SHA-256. Actual failing output (exit 1), retained rather than hidden:

```text
REPORT_PATH_VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V06-c2-inherited-equality.md
Traceback (most recent call last):
  File "<stdin>", line 21, in <module>
AssertionError: relations.json
```

Exact diagnostic command (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib,subprocess
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
old=root/'corpus/fixtures/r99-window-lapse/relations.json'
new=root/'corpus/fixtures/r100-docket-review/relations.json'
baseline=subprocess.check_output(['git','show','fe1ce46:corpus/fixtures/r99-window-lapse/relations.json'])
bad='c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9'
actual=hashlib.sha256(new.read_bytes()).hexdigest()
print('FAILED_HARNESS_EXPECTED',bad,'length='+str(len(bad)))
print('OBSERVED_SHA256',actual,'length='+str(len(actual)))
assert baseline==old.read_bytes()==new.read_bytes()
print('DIAGNOSIS PASS: relations bytes unchanged; prior assertion used a truncated verifier hash')
PY
```

Observed:

```text
FAILED_HARNESS_EXPECTED c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9 length=55
OBSERVED_SHA256 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 length=64
DIAGNOSIS PASS: relations bytes unchanged; prior assertion used a truncated verifier hash
```

No artifact fix was made or required; the corrected verifier replay passes. Initial lane `AGENTS.md` lookup returned absent and the repo-wide `**/AGENTS.md` glob returned no matches; initial seats-directory glob also returned absent before production. These discovery misses are not missing deliverables after the successful bounded poll.

## Bounds and handoff

`README.md` and `claim-excerpt-map.md` were still T2's baseline copies at this seat's snapshot (hashes above); T2 explicitly released them to T3. This report does not certify T3's eventual documentation, 22/22 mapped coverage, lexical support, census 174, the arc synthesis, semantics dossier, freeze chain, C3, or round-wide admission. Those are outside V06's assigned T2 inheritance/preservation scope. The preservation checks do not establish source truth, authentic chronology, prose entailment, rights, permission, or canon.

PASS — V06 scope: every inherited JSON row is identical (23/23), all ten r99 baseline files are unchanged, five whole-file copies and the 5,114-byte excerpt prefix pass cmp, and r100 is CLEAN; T3 documentation and other round claims remain outside this verdict.

# V04 — C1 code review (2026-10-17)

Seat: `V04-c1-code-review`. Axes: frozen-contract integrity, executable immutability, documentation scope. Baseline: `fe1ce46`; delivered HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (round-100 declaration, uncommitted wave changes). All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, with `python3` for Python.

Only file written by this seat: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V04-c1-code-review.md`. Its resolved path and nonexistence were checked immediately before Write. No scratch, producer-file edits, nested agents, commits, pushes, network, or live `--freeze` invocation by this seat.

## Findings

- **C1 integrity PASS, with a literal-diff qualification.** The sole added pin is `r99-window-lapse` at `corpus/tools/dependency-freeze-contract.json:558-680`. All fields of the six inherited pins are identical to `fe1ce46`. Root schema and payload schema remain 2; the new pin has the exact nine fields emitted by the unchanged writer, ten declared file digests, exact event/relation inventories, and counts 8 events / 7 dependency edges / 1 relation / 6 entities / 8 sources. The tick-15 `clerk-lapse-recorded -> clerk-filing-open` edge is pinned.
- **Do not describe the entire contract diff as literally addition-only.** The other changed root field is `revision` (`:35`), from `337f0fa52b02626b7687eedbb2d99fab30446fe4` to `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. This is exactly the unchanged `freeze()` writer's `contract["revision"] = revision` behavior (`corpus/tools/dependency_freeze.py:418-443`), not an inherited-pin change. Both documentation changes disclose it. Reconstructing the complete serialization from the baseline contract plus the live model and current revision reproduced every delivered contract byte.
- **Executable immutability PASS.** `dependency_freeze.py` is byte-identical to `fe1ce46`, SHA-256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`. The tracked `*.py` diff is empty; the delivered r99 fixture diff is also empty. No production Python-tool changes were found.
- **Documentation scope PASS.** `corpus/tools/README.md` preserves every baseline byte and appends only a 60-line dated freeze addendum (`:363-421`). `SKILL.md` changes are confined to dependency-freeze registry lines 96 and 99 plus the dated supersession at 102; its entire prefix before that section is unchanged. Other registry rows, exit mappings, self-test count/expectations, scope, and non-establishment bounds are not changed.
- **Delivered behavior PASS.** All seven live fixtures independently returned exit 0 and `RESULT PASS`, including a concurrent seven-command replay.

## Producer readiness and bounded poll

The initial seat directory was absent (`ls .ufo/waves/round-100/seats` exited 2); this was startup absence, not a final artifact failure. The following actual poll waited for the r99 pin, both r100 documentation markers, and T1's report together. It slept 20 seconds between failed attempts, succeeded on attempt 10/40, and did not use a stall-escape or all-reports poll.

```sh
python3 -u - <<'PY'
from pathlib import Path
import json,time
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve()==root
contract=root/'corpus/tools/dependency-freeze-contract.json'
seats=root/'.ufo/waves/round-100/seats'
for attempt in range(1,15):
    reports=sorted(seats.glob('T1*.md')) if seats.is_dir() else []
    try:
        pin=json.loads(contract.read_text()).get('pins',{}).get('r99-window-lapse')
    except (OSError,ValueError):
        pin=None
    docs=all('Round-100' in (root/p).read_text() or 'round 100' in (root/p).read_text() or 'r100' in (root/p).read_text() for p in ('corpus/tools/README.md','SKILL.md'))
    ready=bool(reports and pin and docs)
    print(f'poll={attempt}/40 r99_pin={bool(pin)} docs_r100={docs} T1_reports={[p.name for p in reports]} ready={ready}',flush=True)
    if ready:
        break
    if attempt<14:
        time.sleep(20)
else:
    print('POLL_CONTINUE next_attempt=15 max_attempts=40',flush=True)
PY
```

Observed output excerpts, exit 0 (all ten attempts were returned; no omitted successful attempt):

```text
poll=1/40 r99_pin=False docs_r100=False T1_reports=[] ready=False
poll=2/40 r99_pin=True docs_r100=False T1_reports=[] ready=False
poll=6/40 r99_pin=True docs_r100=True T1_reports=[] ready=False
poll=9/40 r99_pin=True docs_r100=True T1_reports=[] ready=False
poll=10/40 r99_pin=True docs_r100=True T1_reports=['T1-chain-seven.md'] ready=True
```

Then read `.ufo/waves/round-100/seats/T1-chain-seven.md` in full. T1 records its one authorized `python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r99-window-lapse` invocation at lines 29-43, and explicitly discloses the root-revision qualification at lines 15 and 96. Process history is producer testimony; the independent byte/model/diff checks below confirm exact consistency with that unchanged guarded writer, not historical observation of the producer's subprocess.

## Actual Git diff review

Commands:

```sh
git diff --stat fe1ce46 -- corpus/tools SKILL.md
git diff --check fe1ce46 -- corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
git diff fe1ce46 -- corpus/tools/dependency-freeze-contract.json
git diff fe1ce46 -- corpus/tools/README.md SKILL.md
```

Observed stat (exit 0):

```text
 SKILL.md                                     |   5 +-
 corpus/tools/README.md                       |  60 +++++++++++++
 corpus/tools/dependency-freeze-contract.json | 125 ++++++++++++++++++++++++++-
 3 files changed, 187 insertions(+), 3 deletions(-)
```

`--check` returned no output, exit 0. The contract diff has exactly two hunks: `@@ -32,7 +32,7 @@` changes the root revision, and `@@ -554,6 +554,129 @@` appends the r99 pin. No inherited pin field changes. The reviewed documentation diff has only the README append and SKILL freeze-section changes. A second actual command, `git diff --unified=0 fe1ce46 -- corpus/tools/README.md SKILL.md`, exposed exactly these hunk headers (exit 0):

```text
@@ -96 +96 @@
@@ -99 +99 @@
@@ -101,0 +102 @@
@@ -361,0 +362,60 @@
```

The historical six-pin wording is explicitly superseded at `corpus/tools/README.md:367` and `SKILL.md:102`; the metadata refresh is disclosed at README:389 and SKILL:99. The addendum says not to re-freeze for verification (README:371), retains the semantics/chronology/canon bounds, and explicitly excludes r100 from this seven-fixture frozen chain (README:421).

## Independent final structural, digest, writer, code, and documentation proof

Actual command, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib,json,runpy,subprocess
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve()==root
base='fe1ce46'
rel='corpus/tools/dependency-freeze-contract.json'
baseline=json.loads(subprocess.check_output(['git','show',base+':'+rel]))
raw=(root/rel).read_bytes()
now=json.loads(raw)
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert set(now)==set(baseline)
assert [k for k in sorted(now) if now[k]!=baseline[k]]==['pins','revision']
assert set(now['pins'])-set(baseline['pins'])=={'r99-window-lapse'}
assert not (set(baseline['pins'])-set(now['pins']))
assert all(now['pins'][name]==pin for name,pin in baseline['pins'].items())
assert now['revision']==head
assert now['schema_version']==now['payload_schema_version']==2
print('ROOT_CHANGED_FIELDS pins,revision; schemas 2/2; pins 6->7; inherited pins 6/6 identical')
print('ROOT_REVISION',baseline['revision'],'->',now['revision'])
ns=runpy.run_path(str(root/'corpus/tools/dependency_freeze.py'),run_name='v04_final_read_only')
fixture=root/'corpus/fixtures/r99-window-lapse'
ns['scope_guard'](fixture)
model=ns['build_model'](fixture)
expected_pin={'fixture':str(fixture.resolve().relative_to(root)),'revision':head,'payload_schema_version':ns['PAYLOAD_SCHEMA_VERSION'],'pinned_files':list(ns['PINNED_FILES']),'content_sha256':model['content_sha256'],'files':model['files'],'events':model['events'],'relations':model['relations'],'counts':model['counts']}
assert now['pins']['r99-window-lapse']==expected_pin
ns['validate_pin']('r99-window-lapse',expected_pin)
assert model['counts']=={'events':8,'dependency_edges':7,'relations':1,'entities':6,'sources':8}
assert model['events']['clerk-lapse-recorded']=={'depends_on':['clerk-filing-open'],'endpoint':{'tick':15,'entity_id':'clerk-maren','place_id':'chalk-stair'}}
print('R99_PIN nine exact keys; scope guard PASS; payload schema 2; inventories/counts exact; tick-15 edge pinned')
for name,digest in model['files'].items():
    assert now['pins']['r99-window-lapse']['files'][name]==digest
    print('MATCH_SHA256',name,digest)
baseline['pins']['r99-window-lapse']=expected_pin
baseline['revision']=head
assert (json.dumps(baseline,indent=2,ensure_ascii=False)+'\n').encode()==raw
print('WRITER_RECONSTRUCTION full delivered contract bytes EXACT; sha256',hashlib.sha256(raw).hexdigest())
for args in (['git','diff','--exit-code',base,'--','*.py'],['git','diff','--exit-code',base,'--','corpus/fixtures/r99-window-lapse'],['git','diff','--check',base,'--',rel,'corpus/tools/README.md','SKILL.md']):
    result=subprocess.run(args,text=True,capture_output=True)
    assert result.returncode==0 and result.stdout=='' and result.stderr=='',result
    print('COMMAND',subprocess.list2cmdline(args),'EXIT 0; stdout empty; stderr empty')
code=(root/'corpus/tools/dependency_freeze.py').read_bytes()
assert code==subprocess.check_output(['git','show',base+':corpus/tools/dependency_freeze.py'])
print('DEPENDENCY_FREEZE_PY_BYTE_IDENTICAL sha256',hashlib.sha256(code).hexdigest())
old_readme=subprocess.check_output(['git','show',base+':corpus/tools/README.md'])
new_readme=(root/'corpus/tools/README.md').read_bytes()
assert new_readme.startswith(old_readme)
assert len(new_readme.splitlines())-len(old_readme.splitlines())==60
assert new_readme.splitlines()[362].startswith(b'### Round-100 addendum:')
print('README append-only 60 lines; new freeze addendum at line 363; historical bytes preserved')
old_skill=subprocess.check_output(['git','show',base+':SKILL.md'])
new_skill=(root/'SKILL.md').read_bytes()
heading=b'### Dependency-edge freeze check\n'
assert old_skill.split(heading)[0]==new_skill.split(heading)[0]
print('SKILL prefix before dependency-freeze section identical; scoped edits at 96/99/102 per reviewed diff')
for name in (rel,'corpus/tools/README.md','SKILL.md'):
    print('DELIVERED_SHA256',name,hashlib.sha256((root/name).read_bytes()).hexdigest())
report=root/'.ufo/waves/round-100/seats/V04-c1-code-review.md'
assert report.resolve().is_relative_to(root/'.ufo/waves/round-100/seats')
assert report.parent.is_dir() and not report.exists()
print('RESOLVED_REPORT',report.resolve())
print('FINAL_READ_ONLY_PROOF PASS')
PY
```

Complete observed output:

```text
ROOT_CHANGED_FIELDS pins,revision; schemas 2/2; pins 6->7; inherited pins 6/6 identical
ROOT_REVISION 337f0fa52b02626b7687eedbb2d99fab30446fe4 -> b5fe472957ab1e4e9c90f5613acc14cd24a288ae
R99_PIN nine exact keys; scope guard PASS; payload schema 2; inventories/counts exact; tick-15 edge pinned
MATCH_SHA256 README.md b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049
MATCH_SHA256 claim-excerpt-map.md d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d
MATCH_SHA256 contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
MATCH_SHA256 entities.json db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
MATCH_SHA256 fictional-excerpts.md fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d
MATCH_SHA256 inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
MATCH_SHA256 relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
MATCH_SHA256 source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
MATCH_SHA256 sources.json 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15
MATCH_SHA256 timeline.json 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069
WRITER_RECONSTRUCTION full delivered contract bytes EXACT; sha256 ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
COMMAND git diff --exit-code fe1ce46 -- *.py EXIT 0; stdout empty; stderr empty
COMMAND git diff --exit-code fe1ce46 -- corpus/fixtures/r99-window-lapse EXIT 0; stdout empty; stderr empty
COMMAND git diff --check fe1ce46 -- corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md EXIT 0; stdout empty; stderr empty
DEPENDENCY_FREEZE_PY_BYTE_IDENTICAL sha256 fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
README append-only 60 lines; new freeze addendum at line 363; historical bytes preserved
SKILL prefix before dependency-freeze section identical; scoped edits at 96/99/102 per reviewed diff
DELIVERED_SHA256 corpus/tools/dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
DELIVERED_SHA256 corpus/tools/README.md c99217cd0663125214cee7007951a1b9ae98f466f7081344c03ad0f45f87f399
DELIVERED_SHA256 SKILL.md 09b2949ae26ec5e257fce0e879749d8abccaf75c888151159ef857597f418ac6
RESOLVED_REPORT /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V04-c1-code-review.md
FINAL_READ_ONLY_PROOF PASS
```

The `*.py` argument above was passed literally by `subprocess.run` to Git, not shell-expanded. The report nonexistence assertion intentionally applies only before report creation. No source or contract writes occur in this proof; it invokes only the read-only scope/model/pin validation functions, not `freeze()`.

## Concurrent live seven-fixture verification

Actual command:

```sh
python3 - <<'PY'
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json,subprocess
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve()==root
pins=json.loads((root/'corpus/tools/dependency-freeze-contract.json').read_text())['pins']
commands=[['python3','corpus/tools/dependency_freeze.py',pin['fixture']] for pin in pins.values()]
def run(command):
    result=subprocess.run(command,cwd=root,text=True,capture_output=True)
    return command,result
with ThreadPoolExecutor(max_workers=7) as pool:
    results=list(pool.map(run,commands))
for command,result in results:
    print('COMMAND',subprocess.list2cmdline(command))
    print(result.stdout,end='')
    print('EXIT',result.returncode)
    if result.stderr:
        print('STDERR',repr(result.stderr))
print(f'PARALLEL_CHAIN {sum(result.returncode==0 and result.stdout.rstrip().endswith("RESULT PASS") for _,result in results)}/{len(results)} CLEAN')
PY
```

Complete observed output, wrapper exit 0:

```text
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT 0
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT 0
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT 0
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT 0
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT 0
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT 0
COMMAND python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
EXIT 0
PARALLEL_CHAIN 7/7 CLEAN
```

## Bounds

This is the V04 C1 code/diff review, not a C2/C3 judgment or overall round admission. No semantics, testimony truth, chronology authentication, rights, permission, or canon is established. The pin set remains exactly the seven declared fixtures and ten declared files each; r100 is unpinned and r88's extra `symbolism-clause-map.md` remains outside that file set. I did not independently rerun the producer's scratch mutation or `--self-test`; T1 reports their results, while this seat directly exercised all seven delivered fixture verifications and independently proved the persisted self-test contract unchanged as part of the unchanged-root-fields check.

The only qualification requiring parent wording is the guarded writer's root revision refresh: the new r99 pin is the only pin change, but the whole JSON diff is not literally addition-only. No corrective hand-edit is appropriate.

PASS — C1's r99 schema-2 ten-file pin and seven clean live receipts verified; all inherited pins and Python tools unchanged; documentation freeze-scoped; expected guarded root-revision refresh explicitly qualified.

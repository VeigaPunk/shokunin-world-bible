# V24 — depth verdict (2026-10-17)

Scope: C2, both components, against r99 closure `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`. Observed HEAD is the pre-dispatch declaration commit `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`; the delivered round-100 changes were uncommitted. Axes: depth, with inherited-byte/row preservation, unresolved-state continuity, provenance/calibration bounds, and executable operability as guardrails. Counts are measurements, not scores.

Only V24-authored file: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V24-verdict-depth.md`. No V24 scratch, corpus/tool/contract edits, nested agents, network, commits, or pushes. All Python commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

## One depth verdict

**Depth improved — PASS, bounded, for both C2 components.**

- Component 1 is an actual preserving continuation, not a count-only claim: 6/1/8 → 6/1/9, sources 8 → 9, exactly one new source and event, 22/22 mapped obligations, CLEAN, and 22/22 lexical source support. The inherited JSON prefixes, five copied files, 5,114-byte fictional-excerpt prefix, and inherited map cells are preserved; map namespaces intentionally change to the new fixture. My full structural census observed 174 fixtures: 40 clean, 134 intentional negatives, 421 violation lines, no stderr or unexpected exits.
- Component 2 is a delivered, internally consistent seven-snapshot dossier: r94 seed plus six continuation beats r95–r100. Every contextual event/source pointer and count matches the underlying fixture; all six adjacent preservation steps replay. The dossier keeps the unresolved-throughout invariant explicitly temporal and non-adjudicative, rather than inventing two accounts or an OPEN docket at r94/r95.
- The new event is review only. The note explicitly retains an open entry, no new filings, no finding, no resolution, and unresolved accounts. It does not renew the crossing-only agreement, assign blame, select a winner, authenticate testimony, or authenticate chronology.

This is **not round-wide ADMIT**. V15's strict baseline/allowlist finding and V20's shared-document closure gaps remain recorded below. No C1 guarded-authoring certification, C3 mutation-replay certification, or global no-axis-harm verdict is implied. The new r100 tick-16 edge is explicitly **unpinned**; the dossier's seven snapshots are not the seven frozen fixtures.

## C2 seats read, both components

Read the complete producer reports `T2-fixture-author.md`, `T3-fixture-docs.md`, and `T4-knowledge-author.md`, plus the complete delivered fixture README/map/excerpts/sources/timeline and final 111-line synthesis. Read the complete C2 verifier reports:

- `V05-c2-checker.md`: CLEAN, exact new event/reference inventory, inherited r99 bytes; its mistaken `facts.json` readiness predicate was corrected and disclosed, not attributed to the fixture.
- `V06-c2-inherited-equality.md`: 23/23 inherited top-level rows with nested JSON types, five whole-file copies and excerpt prefix; its initial truncated-hash assertion failure was diagnosed and corrected. Its early README/map hashes are explicitly T2's pre-T3 copies, not the final documentation.
- `V07-c2-support-map.md`: raw=22 mapped=22, support 22/22, repeated post-T3 receipts on identical bytes; one verifier-helper syntax error was corrected and disclosed.
- `V08-c2-anchors.md`: independent 22-row anchor/span implementation, inherited line positions, four in-memory rejection controls, and J22 isolated to review section 78–88.
- `V09-c2-whole-claim.md`: manual clause-by-clause support, not anchor-only entailment; review records are not newly lodged accounts or findings.
- `V10-c2-anti-overclaim.md`: adversarial window/case closure, default judgment, renewed duty, global first-review, chronology, and semantic-promotion readings fail against explicit delivered wording. Its actual r100 freeze call remains exit 2 `UNPINNED-FIXTURE`, not relabeled green.
- `V11-c2-synthesis.md`: independent final-dossier count/pointer/preservation/manual-bound audit and 21 live arc gates, all passing. Its final citation scan includes LOG/scratch references beyond my narrower fully qualified backtick-range scan.

These reports corroborate, but do not replace, V24's own two replay groups below. Also read V15 preservation/census, V17 boundary/discriminator, and V20 doc-parity reports to avoid turning the scoped depth result into a global admission claim.

## Readiness: actual artifacts and reports

The actual producer-specific bounded poll was:

```sh
python3 - <<'PY'
from pathlib import Path
import time
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
seats=root/'.ufo/waves/round-100/seats'
fixture=root/'corpus/fixtures/r100-docket-review'
files=['entities.json','relations.json','timeline.json','sources.json','contradictions.json','README.md','claim-excerpt-map.md','fictional-excerpts.md','inspiration-note.md','source-excerpt.md']
required=[fixture/name for name in files]+[root/'corpus/knowledge/r100-crossing-arc-synthesis.md']
for attempt in range(1,41):
    missing=[str(p.relative_to(root)) for p in required if not p.is_file() or p.stat().st_size==0]
    reports={tag:sorted(p.name for p in seats.glob(tag+'*.md') if p.is_file() and p.stat().st_size>0) for tag in ['T2','T3','T4']}
    missing_reports=[tag for tag,names in reports.items() if not names]
    print(f'POLL {attempt}/40 missing_artifacts={missing} missing_producer_reports={missing_reports} producer_reports={reports}',flush=True)
    if not missing and not missing_reports:
        print('READY: C2 delivered artifacts and T2/T3/T4 producer reports exist',flush=True)
        break
    if attempt<40:
        time.sleep(20)
else:
    print('ABSENT: bounded artifact/producer poll exhausted (40 tries, 20-second cadence)',flush=True)
    raise SystemExit(3)
PY
```

Observed selected stdout, exit 0 at attempt 25 (480 seconds):

```text
POLL 1/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md'] missing_producer_reports=['T2', 'T3', 'T4'] producer_reports={'T2': [], 'T3': [], 'T4': []}
POLL 5/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md'] missing_producer_reports=['T3', 'T4'] producer_reports={'T2': ['T2-fixture-author.md'], 'T3': [], 'T4': []}
POLL 16/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md'] missing_producer_reports=['T4'] producer_reports={'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md'], 'T4': []}
POLL 17/40 missing_artifacts=[] missing_producer_reports=['T4'] producer_reports={'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md'], 'T4': []}
POLL 25/40 missing_artifacts=[] missing_producer_reports=[] producer_reports={'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md'], 'T4': ['T4-knowledge-author.md']}
READY: C2 delivered artifacts and T2/T3/T4 producer reports exist
```

T2's payload/report was read before the first payload/census replay; T3's completed report/documents were read before map/support calls; T4's completed report and final dossier were read before the dossier replay. No plan was accepted as delivery.

A second narrow 20-second/40-attempt poll waited for the remaining V10 C2 peer report, not every seat. It exited 0 at attempt 9 (160 seconds):

```text
C2-SYNTHESIS-SEAT-POLL 9/40 reports=['V10-c2-anti-overclaim.md']
READY: synthesis verifier report delivered; SELF V24 not part of this dependency
```

That poll's label was imprecise: V10 is the anti-overclaim reviewer; V11 is the synthesis auditor. Both actual reports were read. Its predicate was `seats.glob('V10*.md')`, not a claimed V11 dependency. No all-reports poll, self-dependency, exhausted cap, or stall escape was used. Both background polls completed and were consumed before handoff.

## Own replay 1 — fixture, inheritance, and complete census

Actual command, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
fixture=Path('corpus/fixtures/r100-docket-review')
assert (root/'.ufo/waves/round-100/seats/T2-fixture-author.md').is_file()
base='fe1ce46'
def original(name):
    return subprocess.check_output(['git','show',f'{base}:corpus/fixtures/r99-window-lapse/{name}'])
for name in ['entities.json','relations.json','contradictions.json','source-excerpt.md','inspiration-note.md']:
    assert (fixture/name).read_bytes()==original(name),name
    print('BASELINE-BYTES IDENTICAL',name)
data={name:json.loads((fixture/(name+'.json')).read_bytes()) for name in ['entities','relations','contradictions','sources','timeline']}
for name in ['sources','timeline']:
    old=json.loads(original(name+'.json'))
    assert data[name][:-1]==old and len(data[name])==len(old)+1
    print(f'PARSED-PREFIX {name} {len(old)}/{len(old)} appended=1')
old=original('fictional-excerpts.md')
assert (fixture/'fictional-excerpts.md').read_bytes().startswith(old)
print('EXCERPT-PREFIX',len(old),'bytes preserved')
assert tuple(len(data[n]) for n in ['entities','relations','timeline','sources','contradictions'])==(6,1,9,9,0)
obligations=len(data['entities'])+sum(len(e['claims']) for e in data['entities'])+len(data['relations'])+len(data['timeline'])
assert obligations==22
print('INVENTORY 6 entities / 1 relation / 9 events / 9 sources / 0 contradictions; raw obligations=22')
e=data['timeline'][-1]
assert (e['id'],e['tick'],e['entity_id'],e['place_id'],e['depends_on'],e['source_id'])==('clerk-review-first-passage',16,'clerk-maren','chalk-stair',['clerk-lapse-recorded'],'clerk-review-note')
print('EVENT',json.dumps(e,sort_keys=True))
cmd=['python3','corpus/fixtures/check_bible.py',str(fixture)]
p=subprocess.run(cmd,text=True,capture_output=True)
print('COMMAND',' '.join(cmd)); print(p.stdout,end=''); print('EXIT',p.returncode)
assert p.returncode==0 and p.stdout=='CLEAN: schema, citations, relations, timeline; 0 violations\n' and not p.stderr
old_dirs=subprocess.check_output(['git','ls-tree','-d','--name-only',f'{base}:corpus/fixtures'],text=True).splitlines()
current=sorted(p.name for p in Path('corpus/fixtures').iterdir() if p.is_dir() and any(p.glob('*.json')))
assert set(current)-set(old_dirs)=={'r100-docket-review'} and not set(old_dirs)-set(current)
print(f'FIXTURE-DIRECTORIES baseline={len(old_dirs)} delivered={len(current)} added=r100-docket-review removed=none')
def check(name):
    cmd=['python3','corpus/fixtures/check_bible.py','corpus/fixtures/'+name]
    r=subprocess.run(cmd,text=True,capture_output=True)
    return name,r.returncode,r.stdout,r.stderr
with ThreadPoolExecutor(max_workers=8) as pool:
    census=list(pool.map(check,current))
counts={code:sum(row[1]==code for row in census) for code in sorted(set(row[1] for row in census))}
violations=sum(row[2].count('VIOLATION:') for row in census)
assert counts=={0:40,1:134} and violations==421 and not any(row[3] for row in census)
print('CENSUS',json.dumps(counts,sort_keys=True),'violations='+str(violations),'stderr=none')
changed=subprocess.check_output(['git','diff','--name-only',base,'--','corpus/fixtures'],text=True).splitlines()
inherited_changes=[p for p in changed if not p.startswith(str(fixture)+'/')]
assert not inherited_changes,inherited_changes
print('TRACKED-INHERITED-FIXTURE-CHANGES',inherited_changes)
for name in ['sources.json','timeline.json','fictional-excerpts.md']:
    print('SHA256',str(fixture/name),hashlib.sha256((fixture/name).read_bytes()).hexdigest())
print('RESULT PASS: independent fixture/inheritance/census replay; map and dossier not yet adjudicated')
PY
```

Observed complete stdout:

```text
BASELINE-BYTES IDENTICAL entities.json
BASELINE-BYTES IDENTICAL relations.json
BASELINE-BYTES IDENTICAL contradictions.json
BASELINE-BYTES IDENTICAL source-excerpt.md
BASELINE-BYTES IDENTICAL inspiration-note.md
PARSED-PREFIX sources 8/8 appended=1
PARSED-PREFIX timeline 8/8 appended=1
EXCERPT-PREFIX 5114 bytes preserved
INVENTORY 6 entities / 1 relation / 9 events / 9 sources / 0 contradictions; raw obligations=22
EVENT {"depends_on": ["clerk-lapse-recorded"], "description": "At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.", "entity_id": "clerk-maren", "id": "clerk-review-first-passage", "place_id": "chalk-stair", "source_id": "clerk-review-note", "tick": 16}
COMMAND python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0
FIXTURE-DIRECTORIES baseline=173 delivered=174 added=r100-docket-review removed=none
CENSUS {"0": 40, "1": 134} violations=421 stderr=none
TRACKED-INHERITED-FIXTURE-CHANGES []
SHA256 corpus/fixtures/r100-docket-review/sources.json effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
SHA256 corpus/fixtures/r100-docket-review/timeline.json 008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
SHA256 corpus/fixtures/r100-docket-review/fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
RESULT PASS: independent fixture/inheritance/census replay; map and dossier not yet adjudicated
```

The last line accurately scopes that earlier pass: it was not a premature full-C2 verdict. The final input stability check below confirms those payload bytes remained unchanged through the later documentation/dossier verification. The census checks all 174 structural calls, but I do not claim a separate byte-for-byte comparison of all 173 historical stdout tuples.

### Own post-T3 canonical and lexical calls

Actual commands, issued concurrently; both exit 0:

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Complete map stdout:

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

Selected exact support stdout; every omitted J01–J21/S01–S02 row was PASS:

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
RECEIPT JSON-FACTS 22; EDITORIAL-ROWS 2; TOTAL-ROWS 24
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

These are 22 JSON obligations plus two editorial comparisons, not 24 JSON obligations or 22 distinct anchors. The distinct-anchor count is 20.

## Own replay 2 — final dossier, six preservation steps, real arc gates, citations

Actual command after T2/T3/T4 reports existed and the final dossier was read; exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import subprocess
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
seats=root/'.ufo/waves/round-100/seats'
assert all(any(p.is_file() and p.stat().st_size for p in seats.glob(tag+'*.md')) for tag in ['T2','T3','T4'])
doc=root/'corpus/knowledge/r100-crossing-arc-synthesis.md'
text=doc.read_text()
rows=[line for line in text.splitlines() if line.startswith('| Seed ') or line.startswith('| Beat ')]
assert len(rows)==7
snapshots=[]
for line in rows:
    cells=[s.strip() for s in line.strip('|').split('|')]
    path=cells[1].strip('`').rstrip('/')
    tables={name:json.loads((root/path/(name+'.json')).read_bytes()) for name in ['entities','relations','timeline','sources','contradictions']}
    event_id,event_ptr=re.findall(r'`([^`]+)`',cells[2])
    source_id,source_ptr=re.findall(r'`([^`]+)`',cells[3])
    event=tables['timeline'][int(event_ptr.split('#/')[1])]
    source=tables['sources'][int(source_ptr.split('#/')[1])]
    tick=int(re.search(r'tick (\d+)',cells[2]).group(1))
    counts=tuple(len(tables[n]) for n in ['entities','relations','timeline'])
    obligations=len(tables['entities'])+sum(len(e['claims']) for e in tables['entities'])+len(tables['relations'])+len(tables['timeline'])
    assert counts==tuple(map(int,cells[4].split('/')))
    assert len(tables['sources'])==int(cells[5]) and obligations==int(cells[6])
    assert event['id']==event_id and event['tick']==tick and event['source_id']==source_id and source['id']==source_id
    assert tables['contradictions']==[]
    print(f'DOCKET {path} E/R/T={cells[4]} sources={len(tables["sources"])} obligations={obligations} event={event_id} source={source_id} pointers=VALID contradictions=[]')
    snapshots.append((path,tables))
for (old_path,old),(new_path,new) in zip(snapshots,snapshots[1:]):
    for name in ['entities','timeline','sources']:
        assert new[name][:len(old[name])]==old[name],(old_path,new_path,name)
    assert new['relations']==old['relations']
    for name in ['source-excerpt.md','inspiration-note.md']:
        assert (root/new_path/name).read_bytes()==(root/old_path/name).read_bytes()
    assert (root/new_path/'fictional-excerpts.md').read_bytes().startswith((root/old_path/'fictional-excerpts.md').read_bytes())
    old_rows=[s for s in (root/old_path/'claim-excerpt-map.md').read_text().splitlines() if re.match(r'^\| J\d+',s)]
    new_rows=[s for s in (root/new_path/'claim-excerpt-map.md').read_text().splitlines() if re.match(r'^\| J\d+',s)]
    before=Path(old_path).name+':'
    after=Path(new_path).name+':'
    assert [s.replace(after,before) for s in new_rows[:len(old_rows)]]==old_rows
    print(f'PRESERVATION {Path(old_path).name}->{Path(new_path).name} JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS')
commands=[['python3',tool,path] for path,_ in snapshots for tool in ['corpus/fixtures/check_bible.py','corpus/tools/map_obligations.py']]
def run(cmd):
    p=subprocess.run(cmd,text=True,capture_output=True)
    return cmd,p
with ThreadPoolExecutor(max_workers=8) as pool:
    runs=list(pool.map(run,commands))
for cmd,p in runs:
    print('COMMAND',' '.join(cmd)); print(p.stdout,end=''); print('EXIT',p.returncode,'STDERR',repr(p.stderr))
    assert p.returncode==0 and not p.stderr
missing=[]
bad_ranges=[]
path_count=range_count=0
for token in re.findall(r'`([^`]+)`',text):
    if not token.startswith(('corpus/','.ufo/')):
        continue
    match=re.fullmatch(r'(.+):(\d+)(?:[-–](\d+))?',token)
    path=match.group(1) if match else token
    paths=[path]
    if '{' in path:
        start,rest=path.split('{',1)
        inside,end=rest.split('}',1)
        paths=[start+part+end for part in inside.split(',')]
    for name in paths:
        p=root/name
        path_count+=1
        if not p.exists(): missing.append(name)
        if match:
            range_count+=1
            a=int(match.group(2)); b=int(match.group(3) or a)
            if not p.is_file() or not 1<=a<=b<=len(p.read_text().splitlines()): bad_ranges.append(token)
assert not missing and not bad_ranges,(missing,bad_ranges)
print(f'CITED-PATHS {path_count} explicit-ranges={range_count} missing={missing} invalid-ranges={bad_ranges}')
for heading in ['**unresolved throughout**','**No testimony truth.**','**No chronology authentication.**','editorial normalizations','first explicit two-account unresolved statement','seven snapshot records']:
    assert heading in text,heading
print('DOCUMENTED-BOUNDS present: six continuations/seven snapshots; unresolved status temporally scoped; no testimony/chronology proof; editorial ticks/IDs')
pins=json.loads((root/'corpus/tools/dependency-freeze-contract.json').read_text())['pins']
assert 'r100-docket-review' not in pins and 'r99-window-lapse' in pins
print('COVERAGE-BOUND r99 pinned=True; r100 review pinned=False; dossier snapshots are not frozen-chain set')
print('SYNTHESIS-SHA256',hashlib.sha256(doc.read_bytes()).hexdigest())
print('RESULT PASS: independent docket, preservation, real gate, and local-citation replay; bounds are documented statements, not automated semantic proof')
PY
```

Selected exact stdout (the seven real checker calls each printed the CLEAN line and exit 0, and all seven map calls printed the matching inventory and RESULT PASS, exit 0, empty stderr):

```text
DOCKET corpus/fixtures/r94-paired-crossing E/R/T=5/1/3 sources=3 obligations=14 event=paired-crossing-decision source=crossing-minute pointers=VALID contradictions=[]
DOCKET corpus/fixtures/r95-crossing-aftermath E/R/T=5/1/4 sources=4 obligations=15 event=aftermath-missing-evin source=aru-aftermath-note pointers=VALID contradictions=[]
DOCKET corpus/fixtures/r96-crossing-response E/R/T=5/1/5 sources=5 obligations=16 event=response-evin-salt-court source=evin-response-note pointers=VALID contradictions=[]
DOCKET corpus/fixtures/r97-crossing-acknowledgment E/R/T=5/1/6 sources=6 obligations=17 event=acknowledgment-aru-records source=aru-acknowledgment-note pointers=VALID contradictions=[]
DOCKET corpus/fixtures/r98-clerk-filing E/R/T=6/1/7 sources=7 obligations=20 event=clerk-filing-open source=clerk-filing-note pointers=VALID contradictions=[]
DOCKET corpus/fixtures/r99-window-lapse E/R/T=6/1/8 sources=8 obligations=21 event=clerk-lapse-recorded source=clerk-lapse-note pointers=VALID contradictions=[]
DOCKET corpus/fixtures/r100-docket-review E/R/T=6/1/9 sources=9 obligations=22 event=clerk-review-first-passage source=clerk-review-note pointers=VALID contradictions=[]
PRESERVATION r94-paired-crossing->r95-crossing-aftermath JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS
PRESERVATION r95-crossing-aftermath->r96-crossing-response JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS
PRESERVATION r96-crossing-response->r97-crossing-acknowledgment JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS
PRESERVATION r97-crossing-acknowledgment->r98-clerk-filing JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS
PRESERVATION r98-clerk-filing->r99-window-lapse JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS
PRESERVATION r99-window-lapse->r100-docket-review JSON-prefixes/relations/excerpt-prefix/external-bytes/map-rows=PASS
CITED-PATHS 88 explicit-ranges=15 missing=[] invalid-ranges=[]
DOCUMENTED-BOUNDS present: six continuations/seven snapshots; unresolved status temporally scoped; no testimony/chronology proof; editorial ticks/IDs
COVERAGE-BOUND r99 pinned=True; r100 review pinned=False; dossier snapshots are not frozen-chain set
SYNTHESIS-SHA256 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
RESULT PASS: independent docket, preservation, real gate, and local-citation replay; bounds are documented statements, not automated semantic proof
```

Representative final live pair, complete stdout/exit receipts from that same pass:

```text
COMMAND python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0 STDERR ''
COMMAND python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
EXIT 0 STDERR ''
```

My citation figures count occurrences, including expanded brace-list paths, not 88 unique paths. The automated numeric-range scan covers fully specified backtick citations beginning `corpus/` or `.ufo/`; it is not a claim of generalized/contextual anchor inference. V11's fuller scan separately reports 77 path identities and 16 ranges, including LOG/absolute-root contexts. The two counting scopes differ, not the existence of a missing path.

## Manual unresolved-throughout judgment and non-establishment bounds

The actual new quote at `corpus/fixtures/r100-docket-review/fictional-excerpts.md:82-86` is:

```text
> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
> The entry remains open.
> No new filings have been lodged.
> I make no finding and resolve nothing.
> Both accounts stand unresolved.
```

The first sentence supports the review occasion, attributed order, and place; the remaining four sentences support the other clauses of `timeline.json:95`, rather than relying on the J22 anchor alone. The source attribution is `clerk-review-note` (`sources.json:51-54`); the event is `timeline.json#/8`, actor `clerk-maren`, place `chalk-stair`, tick 16, dependency `clerk-lapse-recorded`. The actor already exists and retains `first_appearance: clerk-filing-note`.

The new source/event represent the review, not a newly lodged account. They do not erase the inherited tick-14 filing or convert absence of new filings into default judgment. `README.md:11-13` and `claim-excerpt-map.md:72` make those distinctions explicit. The inherited lapse closes the crossing-window, not the case. Its denial of resolution/blame/reconciliation is not a positive finding.

The final synthesis's numbering and bounds are substantive:

- `r100-crossing-arc-synthesis.md:8` has r94 seed plus r95–r100 six continuations; no one of the seven listed snapshots is discarded. The cited r98/r99 scope notes at line 14 independently use fourth/fifth beat.
- Lines 10, 34, and 48 do not invent an earlier two-account docket: r95 introduces the first account, r96 first explicitly states the two-account unresolved status, and OPEN is first recorded at r98. “Unresolved throughout” means non-adjudication, not a claim that two accounts/OPEN literally existed at r94.
- Lines 32–38 preserve each record's attributed scope; receipt is not agreement/retraction, filing is not adjudication, window closure is not matter closure, and review is not a disposition.
- Lines 54–59 disclaim testimony and institutional-authority authentication; authentic chronology; new or continuing duties; bare-ID identity proof; semantic/canon certification by gates; rights and AI-training permission. Ticks, IDs, and edges remain editorial normalizations. Spence remains an external English editorial comparison, not an authenticated K'iche-language source or in-world witness.
- Line 50 correctly treats `contradictions.json == []` as an authored inventory fact, not proof of universal semantic compatibility. Different actors at different places do not by themselves assert one actor's incompatible occupancy.
- Line 63 names the separate frozen set: r88 plus r94–r99, not the dossier's r94–r100. No pin credit is claimed for the new review.

This is a manual judgment about support and wording of authored records. The script's heading checks and green gates do not mechanically prove these semantics, fictional truth, chronology, dependency meaning, canon, rights, or permission. No future continuation is constrained to stay unresolved by this report.

## Non-blocking receipt discrepancy: T2 relation hash

V05/V06 disclosed this discrepancy; V24 independently reproduced it. Actual command, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
import re
import subprocess
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
fixture=root/'corpus/fixtures/r100-docket-review'
paths=sorted(p for p in fixture.iterdir() if p.is_file())+[root/'corpus/knowledge/r100-crossing-arc-synthesis.md']+[root/name for name in ['corpus/fixtures/check_bible.py','corpus/tools/map_obligations.py','corpus/tools/support_check.py','corpus/tools/dependency-freeze-contract.json']]
assert len(paths)==15
for p in paths:
    print('DELIVERED-SHA256',str(p.relative_to(root)),hashlib.sha256(p.read_bytes()).hexdigest())
t2=(root/'.ufo/waves/round-100/seats/T2-fixture-author.md').read_text()
reported=re.findall(r'relations\.json(?: bytes=\d+)? sha256=([a-f0-9]+)',t2)
actual=hashlib.sha256((fixture/'relations.json').read_bytes()).hexdigest()
baseline=subprocess.check_output(['git','show','fe1ce46:corpus/fixtures/r99-window-lapse/relations.json'])
assert baseline==(root/'corpus/fixtures/r99-window-lapse/relations.json').read_bytes()==(fixture/'relations.json').read_bytes()
print('T2-RELATIONS-RECEIPT',repr(reported),'reported_lengths='+repr([len(x) for x in reported]),'actual='+actual,'actual_length='+str(len(actual)),'baseline_bytes_equal=True')
print('NOTE: truncated producer-receipt hashes do not match actual SHA-256; actual relation bytes are independently baseline-identical')
PY
```

Observed discrepancy lines:

```text
T2-RELATIONS-RECEIPT ['c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9', 'c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9'] reported_lengths=[55, 55] actual=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 actual_length=64 baseline_bytes_equal=True
NOTE: truncated producer-receipt hashes do not match actual SHA-256; actual relation bytes are independently baseline-identical
```

The two 55-character strings remain at T2 report lines 66 and 153 at this snapshot. They are not valid full SHA-256 receipts. This is a producer-report transcription defect, not a relation-byte or depth defect: the actual relation bytes equal both r99 and `fe1ce46`. V24 did not edit another seat's report; parent should retain an explicit receipt correction rather than silently trusting the truncated values.

## Round-wide limits retained, not waived

V15 reports strict baseline preservation **FAIL** because the literal `fe1ce46` comparison includes additional inherited `LOG.md` and `SCORECARD.md` changes. V15 attributes both to committed pre-dispatch bookkeeping, not to producers; inherited fixtures and the producer worktree scope pass. V24 independently confirmed the distinction. V20 reports pre-integration doc parity **FAIL**: the fixtures index/census, corpus current navigation, and C9 r100 row have not been updated under the producers' read-only shared-file boundary.

Actual V24 command, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
import subprocess
root=Path.cwd().resolve()
assert root==Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
for cmd in [
 ['git','diff','--name-only','fe1ce46','HEAD','--'],
 ['git','diff','--name-only','HEAD','--'],
 ['git','log','--format=%h %s','--name-only','fe1ce46..HEAD','--','LOG.md','SCORECARD.md'],
]:
    p=subprocess.run(cmd,text=True,capture_output=True)
    print('COMMAND',' '.join(cmd)); print(p.stdout,end=''); print('EXIT',p.returncode,'STDERR',repr(p.stderr))
    assert p.returncode==0 and not p.stderr
fixtures=(root/'corpus/fixtures/README.md').read_text()
corpus=(root/'corpus/README.md').read_text()
c9=(root/'corpus/knowledge/r91-c9-watch.md').read_text()
print('SHARED-DOC-OBSERVATION fixtures_round100_section='+str(any(s.startswith('## Round 100') for s in fixtures.splitlines())))
print('SHARED-DOC-OBSERVATION corpus_r100_bullet='+str(any(s.startswith('- `fixtures/r100-docket-review/README.md`') for s in corpus.splitlines())))
print('SHARED-DOC-OBSERVATION c9_r100_row='+str(any(s.startswith('| 2026-10-17 (r100) |') for s in c9.splitlines())))
PY
```

Complete observed stdout:

```text
COMMAND git diff --name-only fe1ce46 HEAD --
LOG.md
SCORECARD.md
EXIT 0 STDERR ''
COMMAND git diff --name-only HEAD --
SKILL.md
corpus/knowledge/r99-gate-blind-spot-table.md
corpus/tools/README.md
corpus/tools/dependency-freeze-contract.json
EXIT 0 STDERR ''
COMMAND git log --format=%h %s --name-only fe1ce46..HEAD -- LOG.md SCORECARD.md
b5fe472 lore r100: declare sol-max 32-seat round before dispatch

LOG.md
ae67105 lore r99: close round — SCORECARD admitted section

SCORECARD.md
EXIT 0 STDERR ''
SHARED-DOC-OBSERVATION fixtures_round100_section=False
SHARED-DOC-OBSERVATION corpus_r100_bullet=False
SHARED-DOC-OBSERVATION c9_r100_row=False
```

These are not reasons to claim either C2 artifact is absent or unsupported, and not authorization for V24 to repair shared files. They are reasons **not** to infer global admission or whole-round no-axis-harm from the scoped depth PASS. Parent must reconcile the declared baseline versus dispatch bookkeeping and complete/verify the shared-document closure work. In particular, V20 identifies the active corpus freeze bullet's stale six-pin/five-JSON/17-case wording; the new knowledge documents correctly state the delivered seven-pin/ten-file/18-case boundaries.

## Final delivered-byte identity and ownership check

The fingerprint command above printed these complete hashes, and the final pre-write `python3` assertion checked all 15 against this same map:

```text
corpus/fixtures/r100-docket-review/README.md a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
corpus/fixtures/r100-docket-review/claim-excerpt-map.md 16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
corpus/fixtures/r100-docket-review/contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
corpus/fixtures/r100-docket-review/entities.json db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
corpus/fixtures/r100-docket-review/fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
corpus/fixtures/r100-docket-review/inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
corpus/fixtures/r100-docket-review/relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
corpus/fixtures/r100-docket-review/source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
corpus/fixtures/r100-docket-review/sources.json effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
corpus/fixtures/r100-docket-review/timeline.json 008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
corpus/knowledge/r100-crossing-arc-synthesis.md 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
corpus/fixtures/check_bible.py ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
corpus/tools/map_obligations.py 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9
corpus/tools/support_check.py 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
corpus/tools/dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
```

Immediately before the only report Write, the same lane-root assertion also checked the exact absolute report resolution, exact resolved parent, existing parent, absent report, and absence of a report symlink. Observed exit 0:

```text
INPUT-STABILITY 15/15 delivered fixture/dossier/tool/contract hashes unchanged
REPORT-PATH-VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V24-verdict-depth.md
WRITE-SCOPE V24-verdict-depth.md only; no V24 scratch files
```

Initial discovery observed `ls: cannot access '.ufo/waves/round-100/seats': No such file or directory`; the subsequent bounded readiness poll resolved that setup absence. The lane `AGENTS.md` glob found none. No V24 verification assertion or live positive gate failed. The 134 nonzero census fixtures are the standing intentional-negative set, not concealed unexpected failures. There is no needed background task or unresolved V24 depth-evidence blocker.

PASS — depth improved (bounded): both C2 components verify on the delivered bytes, inherited records and unresolved non-adjudication are preserved, and the two independent replay groups pass; r100 remains unpinned, semantic/truth claims remain unestablished, and global baseline/doc-closure findings are not waived.

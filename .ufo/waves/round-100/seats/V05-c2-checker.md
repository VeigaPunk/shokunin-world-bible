# V05 — C2 structural checker (2026-10-17)

Scope: independently verify T2's landed r100 fixture, not the round-wide admission claim. Axes: depth (6/1/9, the new review event), operability (CLEAN; no dangling references or duplicates), adjacency (r99 remains CLEAN and baseline-identical). All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. No corpus, tool, contract, or other seat bytes were changed. This report is the only file this seat created; no scratch, agents, network, commits, or pushes.

## Artifact readiness and bounded stall escape

The first root check observed the fixture absent and no T2 report. I read the standing declaration at `LOG.md:3349-3404` and the checker at `corpus/fixtures/check_bible.py`. No lane `AGENTS.md` exists (the direct Read returned a missing-file error; the lane glob also found none).

An initial 20-second, at-most-40-attempt poll mistakenly included `facts.json` in its readiness set. This was a verifier predicate error: `check_bible.py:25-32` requires sources/entities/relations/timeline/contradictions, not facts. The erroneous poll was stopped after 15 observed attempts (~300 seconds), rather than letting an impossible file requirement produce a false ABSENT. Its observed output included:

```text
2026-10-17T23:32:01.671703-03:00 attempt=1 missing=['entities.json', 'facts.json', 'timeline.json', 'sources.json', 'fictional-excerpts.md'] T2_reports=[]
2026-10-17T23:33:41.672966-03:00 attempt=6 missing=['facts.json'] T2_reports=['.ufo/waves/round-100/seats/T2-fixture-author.md']
2026-10-17T23:36:41.675420-03:00 attempt=15 missing=['facts.json'] T2_reports=['.ufo/waves/round-100/seats/T2-fixture-author.md']
```

The task-stop result was `status: killed`, with reason: `Correct readiness predicate after reading check_bible.py: fixtures use relations.json and contradictions.json, not facts.json. T2 report landed at attempt 6; replacing erroneous poll with delivered-schema check.` This is a recorded bounded stall escape, not a fixture failure. No all-reports poll was used, so SELF subtraction was not needed.

The corrected actual command (exit 0), before verification:

```sh
python3 -c 'from pathlib import Path; root=Path.cwd().resolve(); assert str(root)=="/home/vgpnk/Projects/shokunin/lore-shokunin"; fixture=root/"corpus/fixtures/r100-docket-review"; required=("sources.json","entities.json","relations.json","timeline.json","contradictions.json","fictional-excerpts.md"); missing=[name for name in required if not (fixture/name).is_file()]; reports=sorted(p for p in (root/".ufo/waves/round-100/seats").glob("T2*.md") if p.is_file()); print("root="+str(root)); print("missing="+repr(missing)); print("T2_reports="+repr([str(p.relative_to(root)) for p in reports])); print("READY="+str(not missing and bool(reports))); assert not missing and reports'
```

Observed stdout:

```text
root=/home/vgpnk/Projects/shokunin/lore-shokunin
missing=[]
T2_reports=['.ufo/waves/round-100/seats/T2-fixture-author.md']
READY=True
```

I read the landed T2 report and the actual r100 `timeline.json` and `sources.json`. No plan or unlanded artifact was substituted for the delivered fixture.

## Real checker calls

Actual command (exit 0):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Observed stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Actual command (exit 0), independently of r100:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
```

Observed stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

The r99 command also returned the same CLEAN output before the fixture/report poll.

## Independent inventory, uniqueness, references, inheritance, and byte receipts

Actual command (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
from collections import Counter
import hashlib
import json
import subprocess

root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
fixture = root / 'corpus/fixtures/r100-docket-review'
prior = root / 'corpus/fixtures/r99-window-lapse'
assert fixture.resolve() == fixture and prior.resolve() == prior

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f'duplicate JSON member: {key}'
        result[key] = value
    return result

sections = ('sources', 'entities', 'relations', 'timeline', 'contradictions')
data = {name: json.loads((fixture / f'{name}.json').read_text(), object_pairs_hook=unique_object) for name in sections}
counts = {name: len(data[name]) for name in sections}
assert counts == {'sources': 9, 'entities': 6, 'relations': 1, 'timeline': 9, 'contradictions': 0}, counts
print('COUNTS entities=6 relations=1 timeline=9 sources=9 contradictions=0')
for name in ('sources', 'entities', 'timeline', 'contradictions'):
    duplicates = {key: count for key, count in Counter(row['id'] for row in data[name]).items() if count != 1}
    assert not duplicates, (name, duplicates)
assert len({json.dumps(row, sort_keys=True) for row in data['relations']}) == len(data['relations'])
print('DUPLICATES JSON_members=0 source_ids=0 entity_ids=0 event_ids=0 contradiction_ids=0 relation_rows=0')
entities = {row['id']: row for row in data['entities']}
events = {row['id']: row for row in data['timeline']}
sources = {row['id'] for row in data['sources']}
source_refs = [row['first_appearance'] for row in data['entities']]
source_refs += [claim['source_id'] for row in data['entities'] for claim in row['claims']]
source_refs += [row['source_id'] for name in ('relations', 'timeline') for row in data[name]]
entity_refs = [row[key] for row in data['relations'] for key in ('from', 'to')]
entity_refs += [row[key] for row in data['timeline'] for key in ('entity_id', 'place_id')]
assert all(ref in sources for ref in source_refs)
assert all(ref in entities for ref in entity_refs)
dependency_count = 0
for row in data['timeline']:
    deps = row['depends_on']
    assert len(deps) == len(set(deps)), row['id']
    assert entities[row['place_id']]['kind'] == 'place'
    for dep in deps:
        assert dep in events and events[dep]['tick'] < row['tick'], (row['id'], dep)
        dependency_count += 1
print(f'REFERENCES source_refs={len(source_refs)} entity_refs={len(entity_refs)} dependency_edges={dependency_count}; dangling=0 duplicate_dependencies=0 inversions=0')
review = events['clerk-review-first-passage']
expected = {'tick': 16, 'entity_id': 'clerk-maren', 'place_id': 'chalk-stair', 'depends_on': ['clerk-lapse-recorded'], 'source_id': 'clerk-review-note'}
assert all(review[key] == value for key, value in expected.items())
assert events['clerk-lapse-recorded']['tick'] == 15
print('REVIEW ' + json.dumps(review, sort_keys=True))
for name in sections:
    before = json.loads((prior / f'{name}.json').read_text(), object_pairs_hook=unique_object)
    after = data[name]
    if name in ('sources', 'timeline'):
        assert len(after) == len(before) + 1 and after[:-1] == before, name
    else:
        assert after == before, name
print('INHERITANCE all five r99 tables preserved as parsed values; sources 8->9; timeline 8->9')
files = subprocess.check_output(['git', 'ls-tree', '--name-only', 'fe1ce46:corpus/fixtures/r99-window-lapse'], text=True).splitlines()
assert len(files) == 10
for name in files:
    baseline = subprocess.check_output(['git', 'show', f'fe1ce46:corpus/fixtures/r99-window-lapse/{name}'])
    assert (prior / name).read_bytes() == baseline, name
print('R99_PRESERVATION baseline=fe1ce46 files_byte_identical=10/10')
for name in ('sources.json', 'entities.json', 'relations.json', 'timeline.json', 'contradictions.json', 'fictional-excerpts.md'):
    print(f'SHA256 r100/{name} {hashlib.sha256((fixture / name).read_bytes()).hexdigest()}')
print('SHA256 check_bible.py ' + hashlib.sha256((root / 'corpus/fixtures/check_bible.py').read_bytes()).hexdigest())
print('RESULT PASS')
PY
```

Observed stdout:

```text
COUNTS entities=6 relations=1 timeline=9 sources=9 contradictions=0
DUPLICATES JSON_members=0 source_ids=0 entity_ids=0 event_ids=0 contradiction_ids=0 relation_rows=0
REFERENCES source_refs=22 entity_refs=20 dependency_edges=8; dangling=0 duplicate_dependencies=0 inversions=0
REVIEW {"depends_on": ["clerk-lapse-recorded"], "description": "At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.", "entity_id": "clerk-maren", "id": "clerk-review-first-passage", "place_id": "chalk-stair", "source_id": "clerk-review-note", "tick": 16}
INHERITANCE all five r99 tables preserved as parsed values; sources 8->9; timeline 8->9
R99_PRESERVATION baseline=fe1ce46 files_byte_identical=10/10
SHA256 r100/sources.json effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
SHA256 r100/entities.json db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
SHA256 r100/relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
SHA256 r100/timeline.json 008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
SHA256 r100/contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
SHA256 r100/fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
SHA256 check_bible.py ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
RESULT PASS
```

This establishes the assigned event at `corpus/fixtures/r100-docket-review/timeline.json:87-97`: tick 16, actor `clerk-maren`, place `chalk-stair`, dependency exactly `["clerk-lapse-recorded"]`, and source `clerk-review-note` (source row at `sources.json:50-55`). The dependency resolves uniquely to the inherited tick-15 event. The independent reference inventory checks 22 source references, 20 entity references, and 8 dependency edges; those 22 references are not being offered as a 22/22 claim-map or support-check result.

## Receipt discrepancy and bounds

Non-blocking producer-report discrepancy: T2's `relations.json` SHA-256 text at `.ufo/waves/round-100/seats/T2-fixture-author.md:66` and `:153` is `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9`, whereas the independently measured full SHA-256 is `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (above). This is a receipt transcription discrepancy, not a structural or preservation failure: all ten actual r99 files match `fe1ce46`, and the r100 inherited relations table matches r99. T2 owns any correction to its report; I did not edit it.

No fixture validation command failed. The checker and these inventory checks do not prove prose entailment, testimony truth, authenticated chronology, full C2 dossier completeness, map/support coverage, census, C1, C3, or round-wide admission. Those remain outside this seat's assignment. The authored description's open-entry/no-finding wording is reported, not promoted to checker-proven semantics.

## Exclusive output path verification

Actual command immediately before this report's Write (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
report = root / '.ufo/waves/round-100/seats/V05-c2-checker.md'
assert report.resolve() == report
assert not report.exists()
assert report.parent.is_dir()
assert not report.is_symlink()
print('REPORT PATH VERIFIED ' + str(report.resolve()))
PY
```

Observed stdout:

```text
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V05-c2-checker.md
```

PASS — assigned C2 structural checks: r100 CLEAN, 6/1/9 with 9 sources, exact tick-16 review dependency, no dangling references or duplicates; r99 CLEAN and 10/10 baseline-identical; bounded poll correction and T2 receipt typo recorded above.

# T2 — fixture author (2026-10-17)

Scope: authored the r100 fixture JSON tables and fictional excerpt for C2 component 1, from baseline `fe1ce46`. Axes: depth, coverage, calibration; preservation checks bound operability, freshness, and adjacency. This is a producer report, not the round-wide admission verdict.

## Delivered bytes and ownership

All paths below are under `/home/vgpnk/Projects/shokunin/lore-shokunin/`.

Created the ten files in `corpus/fixtures/r100-docket-review/` using `git show fe1ce46:corpus/fixtures/r99-window-lapse/<file>`:

- `sources.json`: retained the eight existing rows and appended `clerk-review-note` at `sources.json:50-55`.
- `timeline.json`: retained the eight existing rows and appended `clerk-review-first-passage` at `timeline.json:87-97`, tick 16, actor `clerk-maren`, place `chalk-stair`, dependency `["clerk-lapse-recorded"]`, source `clerk-review-note`.
- `fictional-excerpts.md`: preserved all 5,114 baseline bytes as a prefix and appended the dated first-person review section at lines 78-88.
- `contradictions.json`, `entities.json`, `relations.json`, `inspiration-note.md`, `source-excerpt.md`: byte-identical to the baseline.
- `README.md`, `claim-excerpt-map.md`: initialized as baseline byte copies only, then released to T3's exclusive edit ownership. T2 does not certify these two files' eventual contents.

The only other T2-created file is this report. No per-seat scratch, tool/contract edits, commits, pushes, network calls, or nested agents.

## Baseline copy receipt

Exact command, run from the lane root with `python3` (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
import subprocess

root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
target = root / 'corpus/fixtures/r100-docket-review'
assert target.resolve() == root.resolve() / 'corpus/fixtures/r100-docket-review'
assert not target.is_symlink()
files = subprocess.check_output(['git', 'ls-tree', '--name-only', 'fe1ce46:corpus/fixtures/r99-window-lapse'], cwd=root, text=True).splitlines()
assert len(files) == 10, files
target.mkdir(parents=True, exist_ok=True)
for name in files:
    output = target / name
    assert output.resolve() == target.resolve() / name
    payload = subprocess.check_output(['git', 'show', f'fe1ce46:corpus/fixtures/r99-window-lapse/{name}'], cwd=root)
    try:
        with output.open('xb') as handle:
            handle.write(payload)
    except FileExistsError:
        if name in {'README.md', 'claim-excerpt-map.md'}:
            print(f'PRESERVED T3-owned existing file {name}')
            continue
        assert output.read_bytes() == payload, f'existing nonbaseline file: {output}'
        print(f'ALREADY BASELINE {name}')
    else:
        assert output.read_bytes() == payload
        print(f'COPIED {name} bytes={len(payload)} sha256={hashlib.sha256(payload).hexdigest()}')
print(f'TARGET {target.resolve()}')
PY
```

Observed stdout:

```text
COPIED README.md bytes=6176 sha256=b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049
COPIED claim-excerpt-map.md bytes=17119 sha256=d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d
COPIED contradictions.json bytes=3 sha256=37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
COPIED entities.json bytes=1793 sha256=db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
COPIED fictional-excerpts.md bytes=5114 sha256=fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d
COPIED inspiration-note.md bytes=1956 sha256=58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
COPIED relations.json bytes=139 sha256=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9
COPIED source-excerpt.md bytes=640 sha256=b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
COPIED sources.json bytes=3293 sha256=8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15
COPIED timeline.json bytes=2998 sha256=2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069
TARGET /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r100-docket-review
```

Subsequent modifications used three exact `Edit` replacements, one each in `sources.json`, `timeline.json`, and `fictional-excerpts.md`. No existing file was overwritten wholesale.

## Structural gate

Exact command, run from the lane root (exit 0):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Observed stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

## Inheritance, inventory, and payload receipt

Exact command, run from the lane root (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
import json
import subprocess

root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
fixture = root / 'corpus/fixtures/r100-docket-review'
assert fixture.resolve() == root.resolve() / 'corpus/fixtures/r100-docket-review'
def original(name):
    return subprocess.check_output(['git', 'show', f'fe1ce46:corpus/fixtures/r99-window-lapse/{name}'], cwd=root)
for name in ('contradictions.json', 'entities.json', 'inspiration-note.md', 'relations.json', 'source-excerpt.md'):
    payload = (fixture / name).read_bytes()
    assert payload == original(name), name
    print(f'BYTE-IDENTICAL {name} sha256={hashlib.sha256(payload).hexdigest()}')
data = {}
for name in ('entities', 'relations', 'contradictions', 'sources', 'timeline'):
    baseline = json.loads(original(f'{name}.json'))
    delivered = json.loads((fixture / f'{name}.json').read_bytes())
    if name in ('sources', 'timeline'):
        assert delivered[:-1] == baseline, name
        assert len(delivered) == len(baseline) + 1, name
        print(f'PARSED-PREFIX {name}.json inherited={len(baseline)}/{len(baseline)} appended=1')
    else:
        assert delivered == baseline, name
    data[name] = delivered
assert data['sources'][-1]['id'] == 'clerk-review-note'
assert data['timeline'][-1] == {
    'id': 'clerk-review-first-passage',
    'tick': 16,
    'entity_id': 'clerk-maren',
    'place_id': 'chalk-stair',
    'depends_on': ['clerk-lapse-recorded'],
    'description': 'At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.',
    'source_id': 'clerk-review-note',
}
base = original('fictional-excerpts.md')
current = (fixture / 'fictional-excerpts.md').read_bytes()
assert current.startswith(base)
assert current[len(base):].startswith(b'\n## Round 100 docket review note (2026-10-17)\n')
print(f'BYTE-PREFIX fictional-excerpts.md inherited_bytes={len(base)}/{len(base)} appended_bytes={len(current)-len(base)}')
claims = sum(len(entity['claims']) for entity in data['entities'])
obligations = len(data['entities']) + claims + len(data['relations']) + len(data['timeline'])
assert (len(data['entities']), len(data['relations']), len(data['timeline']), len(data['sources']), len(data['contradictions'])) == (6, 1, 9, 9, 0)
assert obligations == 22
print(f'INVENTORY entities={len(data["entities"])} relations={len(data["relations"])} timeline={len(data["timeline"])} sources={len(data["sources"])} entity_claims={claims} contradictions={len(data["contradictions"])} raw_obligations={obligations}')
for name in ('sources.json', 'timeline.json', 'fictional-excerpts.md'):
    print(f'DELIVERED {name} sha256={hashlib.sha256((fixture / name).read_bytes()).hexdigest()}')
print('RESULT PASS: inherited rows preserved; one review source/event; excerpt byte-prefix preserved')
PY
```

Observed stdout:

```text
BYTE-IDENTICAL contradictions.json sha256=37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
BYTE-IDENTICAL entities.json sha256=db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
BYTE-IDENTICAL inspiration-note.md sha256=58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
BYTE-IDENTICAL relations.json sha256=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9
BYTE-IDENTICAL source-excerpt.md sha256=b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
PARSED-PREFIX sources.json inherited=8/8 appended=1
PARSED-PREFIX timeline.json inherited=8/8 appended=1
BYTE-PREFIX fictional-excerpts.md inherited_bytes=5114/5114 appended_bytes=847
INVENTORY entities=6 relations=1 timeline=9 sources=9 entity_claims=6 contradictions=0 raw_obligations=22
DELIVERED sources.json sha256=effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
DELIVERED timeline.json sha256=008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
DELIVERED fictional-excerpts.md sha256=d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
RESULT PASS: inherited rows preserved; one review source/event; excerpt byte-prefix preserved
```

## Authored semantics and map handoff

Final `Read` inspection of `fictional-excerpts.md:78-88` showed the delivered dated section and this exact five-line quotation at lines 82-86:

```text
> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
> The entry remains open.
> No new filings have been lodged.
> I make no finding and resolve nothing.
> Both accounts stand unresolved.
```

Its source ID is `clerk-review-note`; folio 10, lines 1-5; delivery mode inherits `verbatim` from line 3. The event is `timeline.json#/8`. The new source's reliability note explicitly declines testimony truth, chronology authentication, breach findings, continuing duties, selection of a winner, and external historical fact. These are authored bounds, not claims that the structural gate proves prose entailment.

T2's raw-obligation count is 22, not a claim of 22/22 mapped or lexical support: T3 owns the map and README. No map/support/census/round-wide gate result is claimed here. T2 has no dependency on another producer's plan or unlanded artifact; no poll-wait or stall escape was needed for this producer task.

## Path and status receipts

Before the report Write, this exact lane-root command returned exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
report = root / '.ufo/waves/round-100/seats/T2-fixture-author.md'
assert report.resolve() == root.resolve() / '.ufo/waves/round-100/seats/T2-fixture-author.md'
assert not report.exists()
print(f'REPORT PATH VERIFIED {report.resolve()}')
PY
```

Observed stdout:

```text
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T2-fixture-author.md
```

The earlier scoped status command (before report creation) was:

```sh
git status --short -- corpus/fixtures/r100-docket-review .ufo/waves/round-100/seats/T2-fixture-author.md && git diff --check -- corpus/fixtures/r100-docket-review
```

Observed stdout (exit 0):

```text
?? corpus/fixtures/r100-docket-review/
```

Because the fixture is untracked, `git diff --check` here is not offered as a whitespace-validation claim. There were no failed implementation or validation commands. An initial `Read` confirmed no lane-root `AGENTS.md`; initial globbing found no fixture and no producer reports before production.

PASS — T2 fixture payload delivered: CLEAN exit 0, 6/1/9 with 9 sources and 22 raw obligations; inherited rows and excerpt byte-prefix preserved, review leaves the entry open and resolves nothing; T3 map/README certification remains outside this seat.

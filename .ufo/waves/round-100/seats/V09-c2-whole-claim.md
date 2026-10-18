# V09 — C2 whole-proposition review (2026-10-17)

Scope: manual review of the delivered tick-16 docket-review proposition, C2 component 1 only. Axes: depth (one review-only continuation), calibration (all description clauses supported by the authored note), preservation (no new filing, resolution, adjudication, or duty smuggled into the continuation). This is not a round-wide admission verdict or certification of the C2 synthesis dossier, C1, C3, census, source truth, or dependency semantics.

## Delivered-revision and ownership boundary

Read `LOG.md:3349-3404`, both complete producer reports (`T2-fixture-author.md`, `T3-fixture-docs.md`), and the complete delivered README, claim map, excerpt, sources, and timeline. Observed HEAD was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`; preservation comparisons deliberately used the declared r99 closure `fe1ce46`, not an assumed current HEAD. All shell commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

Only V09-created file: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V09-c2-whole-claim.md`. No scratch, corpus/tool/contract edits, nested agents, network, commits, or pushes.

## Producer poll: delivered artifacts, not a plan

Exact command (background only to permit baseline reading; exit 0 after 320 seconds, fully joined before handoff):

```sh
python3 -u -c 'from pathlib import Path; import time; from datetime import datetime; root=Path.cwd().resolve(); assert str(root)=="/home/vgpnk/Projects/shokunin/lore-shokunin"; seats=root/".ufo/waves/round-100/seats"; fixture=root/"corpus/fixtures/r100-docket-review"; required=["README.md","claim-excerpt-map.md","fictional-excerpts.md","sources.json","timeline.json"]; print("root="+str(root),flush=True)
for attempt in range(1,41):
    artifacts={name:(fixture/name).is_file() for name in required}; reports={prefix:sorted(p.name for p in seats.glob(prefix+"*") if p.is_file()) for prefix in ("T2","T3")}; ready=all(artifacts.values()) and all(reports.values()); print(datetime.now().isoformat(timespec="seconds"),"attempt="+str(attempt),"artifacts="+repr(artifacts),"reports="+repr(reports),"READY" if ready else "WAIT",flush=True)
    if ready: break
    if attempt<40: time.sleep(20)
else:
    print("ABSENT after 40 checks",flush=True); raise SystemExit(3)'
```

Selected exact observed lines (intervening checks were WAIT at the same 20-second cadence):

```text
root=/home/vgpnk/Projects/shokunin/lore-shokunin
2026-10-17T23:32:08 attempt=1 artifacts={'README.md': False, 'claim-excerpt-map.md': False, 'fictional-excerpts.md': False, 'sources.json': False, 'timeline.json': False} reports={'T2': [], 'T3': []} WAIT
2026-10-17T23:33:48 attempt=6 artifacts={'README.md': True, 'claim-excerpt-map.md': True, 'fictional-excerpts.md': True, 'sources.json': True, 'timeline.json': True} reports={'T2': ['T2-fixture-author.md'], 'T3': []} WAIT
2026-10-17T23:37:28 attempt=17 artifacts={'README.md': True, 'claim-excerpt-map.md': True, 'fictional-excerpts.md': True, 'sources.json': True, 'timeline.json': True} reports={'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md']} READY
```

No all-reports poll or bounded stall escape was needed. Direct nonempty-file checks also observed both producer reports and all five review inputs present before the delivered-revision verification. The initial direct `Read` of lane-root `AGENTS.md` returned `does not exist`; the corpus `AGENTS.md` glob found none. These were pre-delivery observations, not failed fixture gates.

## Manual whole-proposition verdict

All paths in this section are relative to `corpus/fixtures/r100-docket-review/`.

- **Review occasion, place, and order:** `fictional-excerpts.md:82` explicitly says, “Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.” That supports the described review, tick label, Chalk Stair location, and after-lapse order in `timeline.json:88-96` (`timeline.json#/8`). The actor is the existing clerk, not a new entity: the note is attributed to `clerk-review-note` at excerpt line 80, `sources.json:51-54` titles it Maren's note, and the inherited naming at excerpt line 60 identifies Maren as the registry clerk. The event-ID edge `clerk-lapse-recorded` is editorial encoding, not quoted syntax or proof of causal necessity; README line 13 and map lines 56/72 explicitly bound it that way.
- **Entry remains open:** excerpt line 83 says exactly “The entry remains open.” The event description at timeline line 95 repeats that claim, and source reliability at sources line 54 repeats it as the clerk's report. This retains the historical open entry at excerpt line 73; it does not close the matter or reopen a resolved one.
- **No new filings / nothing newly lodged:** excerpt line 84 says exactly “No new filings have been lodged.” Timeline line 95 and sources line 54 preserve that qualifier. The claim concerns the docket-review occasion and existing entry; it does **not** erase the inherited tick-14 filing of both accounts at excerpt lines 59-60. README line 11 and map line 72 say this is a review, not a new filing. The additional authored source and event are representations of a review, not evidence that a further in-world claim or filing was lodged.
- **No finding, no resolution, accounts still unresolved:** excerpt line 85 says “I make no finding and resolve nothing.” Line 86 adds “Both accounts stand unresolved.” Timeline line 95 carries the first denial; source reliability at sources line 54 carries both. No inference of a winner, breach judgment, reconciliation, or testimony truth is needed. The new prose explicitly declines those outcomes; it does not merely omit an outcome and invite the reviewer to supply one.
- **Description is scoped:** every positive clause of timeline line 95 is supported by excerpt lines 82-85, rather than only by the lexical anchor's first sentence. Excerpt line 88 says review only, settles neither account, creates no new duty, and changes no agreement term. README line 11 and map line 72 retain those limits. Sources line 54 explicitly declines testimony truth, authenticated chronology, breach findings, continuing duty, a winner, and external historical fact. No newly established duty, renewal, authority, or settlement appears in the review description.
- **Whole span rather than anchor-only acceptance:** J22 at `claim-excerpt-map.md:43` points to `timeline.json#/8`, source `clerk-review-note`, namespace `r100-docket-review:clerk-review-note`, `verbatim`, span `78-88`. Its anchor is the review sentence at line 82; the **other four quoted lines within that span** supply the open-entry/no-new-filings/no-finding/unresolved clauses. Map line 72 traces each separately. Thus the manual verdict does not treat `support_check`'s single-anchor PASS as entailment of the whole proposition.

**Manual result: PASS (bounded).** The new note and its normalized row agree on a review-only continuation: entry open, no new filings, no finding, no resolution, both accounts unresolved. Preservation checks below independently show that earlier rows were not rewritten to manufacture that outcome. This verdict concerns authored fictional support, not whether any clerk's testimony is true or whether the chronology is authenticated.

## Independent replay: structural and lexical gates

Issued concurrently, all exit 0:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Complete observed stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

Complete observed stdout:

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Selected exact observed stdout (the omitted lines were the passing J01-J21/S01-S02 anchor receipts):

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
RECEIPT JSON-FACTS 22; EDITORIAL-ROWS 2; TOTAL-ROWS 24
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

These gates check structure, inventory, and lexical support, not the manual semantic judgment above.

## Independent exact proposition and inheritance trace

Exact command, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
import json
import subprocess
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
fixture = root / 'corpus/fixtures/r100-docket-review'
assert fixture.resolve() == root / 'corpus/fixtures/r100-docket-review'
print('HEAD=' + subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip())
def baseline(name):
    return subprocess.check_output(['git', 'show', f'fe1ce46:corpus/fixtures/r99-window-lapse/{name}'])
tables = {}
for name in ('entities', 'relations', 'timeline', 'sources', 'contradictions'):
    old = json.loads(baseline(name + '.json'))
    new = json.loads((fixture / (name + '.json')).read_text())
    assert (new[:-1] if name in ('timeline', 'sources') else new) == old
    tables[name] = new
print('INHERITED JSON: entities 6/6; relations 1/1; events 8/8; sources 8/8; contradictions unchanged []')
print('COUNTS=' + json.dumps({name: len(rows) for name, rows in tables.items()}, sort_keys=True))
assert (len(tables['entities']), len(tables['relations']), len(tables['timeline']), len(tables['sources']), len(tables['contradictions'])) == (6, 1, 9, 9, 0)
text = (fixture / 'fictional-excerpts.md').read_text()
assert (fixture / 'fictional-excerpts.md').read_bytes().startswith(baseline('fictional-excerpts.md'))
print('INHERITED EXCERPT PREFIX: 5114/5114 bytes preserved')
lines = text.splitlines()
expected = (
    '> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.',
    '> The entry remains open.',
    '> No new filings have been lodged.',
    '> I make no finding and resolve nothing.',
    '> Both accounts stand unresolved.',
)
assert tuple(lines[81:86]) == expected
for number in range(78, 89):
    print(f'fictional-excerpts.md:{number}: {lines[number - 1]}')
event = tables['timeline'][8]
assert event == {
    'id': 'clerk-review-first-passage', 'tick': 16,
    'entity_id': 'clerk-maren', 'place_id': 'chalk-stair',
    'depends_on': ['clerk-lapse-recorded'],
    'description': 'At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.',
    'source_id': 'clerk-review-note',
}
source = tables['sources'][8]
assert source['id'] == event['source_id']
assert source['kind'] == 'fictional first-person note'
print('timeline.json#/8=' + json.dumps(event, sort_keys=True))
print('sources.json#/8=' + json.dumps(source, sort_keys=True))
map_lines = (fixture / 'claim-excerpt-map.md').read_text().splitlines()
row = map_lines[42]
assert row.startswith('| J22 | `timeline.json#/8` ')
for token in ('`clerk-review-note`', '`r100-docket-review:clerk-review-note`', '| 78-88 | `verbatim` |', expected[0][2:]):
    assert token in row
print('claim-excerpt-map.md:43: ' + row)
print('NEW ROWS ONLY: one review event and one fictional review source; no new entity/relation/contradiction')
for name in ('README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'sources.json', 'timeline.json'):
    print('SHA256 ' + name + ' ' + hashlib.sha256((fixture / name).read_bytes()).hexdigest())
print('RESULT PASS: review proposition trace and preservation checks; semantic verdict requires the manual reading recorded in V09')
PY
```

Complete observed stdout:

```text
HEAD=b5fe472957ab1e4e9c90f5613acc14cd24a288ae
INHERITED JSON: entities 6/6; relations 1/1; events 8/8; sources 8/8; contradictions unchanged []
COUNTS={"contradictions": 0, "entities": 6, "relations": 1, "sources": 9, "timeline": 9}
INHERITED EXCERPT PREFIX: 5114/5114 bytes preserved
fictional-excerpts.md:78: ## Round 100 docket review note (2026-10-17)
fictional-excerpts.md:79: 
fictional-excerpts.md:80: Newly authored fictional first-person note, attributed to in-world source ID `clerk-review-note`, folio 10, lines 1–5. This section is appended after the preserved r99 text above; the inherited wording is unchanged.
fictional-excerpts.md:81: 
fictional-excerpts.md:82: > Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
fictional-excerpts.md:83: > The entry remains open.
fictional-excerpts.md:84: > No new filings have been lodged.
fictional-excerpts.md:85: > I make no finding and resolve nothing.
fictional-excerpts.md:86: > Both accounts stand unresolved.
fictional-excerpts.md:87: 
fictional-excerpts.md:88: Scope: this appended section is the clerk's first-person docket review record. It records review only: the entry remains open, nothing new has been lodged, and the clerk makes no finding and resolves nothing. It settles neither account, creates no new duty, and changes no term of the crossing-scoped agreement above; both accounts remain unresolved.
timeline.json#/8={"depends_on": ["clerk-lapse-recorded"], "description": "At the Chalk Stair at tick 16, the clerk makes a first-passage docket review after the lapse record; the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing.", "entity_id": "clerk-maren", "id": "clerk-review-first-passage", "place_id": "chalk-stair", "source_id": "clerk-review-note", "tick": 16}
sources.json#/8={"id": "clerk-review-note", "kind": "fictional first-person note", "reliability_note": "Newly authored fictional note; the clerk reports a first-passage docket review after the lapse record: the entry remains open, no new filings have been lodged, and the clerk makes no finding and resolves nothing. Both accounts stand unresolved; the note is not evidence of testimony truth, an authenticated chronology, a breach finding, a continuing duty, a winner between the accounts, or an external historical fact.", "title": "Maren's Chalk Stair Docket Review Note"}
claim-excerpt-map.md:43: | J22 | `timeline.json#/8` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-review-note` | `r100-docket-review:clerk-review-note` | `fictional-excerpts.md` | 78-88 | `verbatim` | `Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.` |
NEW ROWS ONLY: one review event and one fictional review source; no new entity/relation/contradiction
SHA256 README.md a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
SHA256 claim-excerpt-map.md 16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
SHA256 fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
SHA256 sources.json effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
SHA256 timeline.json 008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
RESULT PASS: review proposition trace and preservation checks; semantic verdict requires the manual reading recorded in V09
```

## Final input stability and report-path receipt

Immediately before this report's Write, exact command (exit 0):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
fixture = root / 'corpus/fixtures/r100-docket-review'
expected = {
    'README.md': 'a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa',
    'claim-excerpt-map.md': '16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244',
    'fictional-excerpts.md': 'd01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705',
    'sources.json': 'effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e',
    'timeline.json': '008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8',
}
for name, digest in expected.items():
    assert hashlib.sha256((fixture / name).read_bytes()).hexdigest() == digest, name
print('FINAL REVIEW INPUTS: 5/5 digests unchanged since independent replay')
report = root / '.ufo/waves/round-100/seats/V09-c2-whole-claim.md'
assert report.resolve() == root / '.ufo/waves/round-100/seats/V09-c2-whole-claim.md'
assert report.parent.resolve() == root / '.ufo/waves/round-100/seats'
assert not report.exists()
assert not report.is_symlink()
print('REPORT PATH VERIFIED ' + str(report.resolve()))
print('V09 WRITES: this report only; no scratch')
PY
```

Observed stdout:

```text
FINAL REVIEW INPUTS: 5/5 digests unchanged since independent replay
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V09-c2-whole-claim.md
V09 WRITES: this report only; no scratch
```

No fixture verification failed, no contradiction was found in the new proposition, and no unresolved V09 blocker remains. Scoped axis verdict: depth witnessed by the additional review-only beat; calibration and preservation show no observed harm in this reviewed fixture. No wider fleet-axis or round-admission result is implied.

PASS — C2 review note is whole-proposition supported by excerpt lines 82-86 and JSON/map rows; entry remains open, no new filing or finding is introduced, nothing is resolved, and the description remains explicitly bounded.

# C7B — Selected-cluster discipline audit

## Work performed

- Axes audited: M3 passage evidence and clause→element index; attribution/rights/training separation; M4 OBS-1 repair; kotodama generation versus lore canon-record boundary.
- Archived baseline `dfd1fbc3711f2b28597d74444819aca91fe6bc31` under `/tmp/lore-c7b-round88-JKsNEQ`, then applied `M3-cluster2.patch` followed by `M4-obs1-excerpt.patch`. All inspection and checks below used that combined scratch tree.
- Read M3's delivered excerpt (`corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md:3,5,7`), note (`inspiration-note.md:5-7,9-21`), symbolism map (`symbolism-clause-map.md:3,5-10`), authored text (`fictional-excerpts.md:3-11`), and M4's revised r87 excerpt/map.
- M3 provides one unique printed-page locator (p. 209), not three distinct source locations. I checked that locator and both indexed clauses in its delivered passage; this satisfies three text-anchor spot checks, but not a strict requirement for three distinct passage locators.
- No repository source files or sibling repositories were changed. This seat wrote only this report; no patch or commit was created.

## Before → after measurements

All patch tests, content audits, and checker replays used the scratch archive, not the live repository.

**Patch application** — cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`:

```sh
scratch=$(mktemp -d /tmp/lore-c7b-round88-XXXXXX) && printf 'scratch=%s\n' "$scratch" && git archive dfd1fbc3711f2b28597d74444819aca91fe6bc31 | tar -x -C "$scratch" && git -C "$scratch" apply --check /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-88/patches/M3-cluster2.patch && git -C "$scratch" apply /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-88/patches/M3-cluster2.patch && git -C "$scratch" apply --check /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-88/patches/M4-obs1-excerpt.patch && git -C "$scratch" apply /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-88/patches/M4-obs1-excerpt.patch && printf 'patches=M3-cluster2.patch,M4-obs1-excerpt.patch; status=applied\n'
```

Observed:

```text
scratch=/tmp/lore-c7b-round88-JKsNEQ
patches=M3-cluster2.patch,M4-obs1-excerpt.patch; status=applied
```

**Checker replays** — cwd `/tmp/lore-c7b-round88-JKsNEQ`:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster && python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster
```

Observed (exit 0):

```text
CLEAN: schema, citations, relations, timeline; 0 violations
CLEAN: schema, citations, relations, timeline; 0 violations
```

**M3 locator spot checks** — cwd `/tmp/lore-c7b-round88-JKsNEQ`:

```sh
python3 - <<'PY'
from pathlib import Path
p = Path('corpus/fixtures/r88-m3-maya-cluster')
excerpt = (p / 'source-excerpt.md').read_text()
note = (p / 'inspiration-note.md').read_text()
print(f'locator_in_delivered_excerpt={"printed p. 209" in excerpt}')
print(f'locator_in_inspiration_note={"printed p. 209" in note}')
print(f'clause_1_in_delivered_excerpt={"He called out “Earth,”" in excerpt}')
print(f'clause_2_in_delivered_excerpt={"and the solid land appeared." in excerpt}')
print('distinct_printed_page_locators=1')
PY
```

Observed:

```text
locator_in_delivered_excerpt=True
locator_in_inspiration_note=True
clause_1_in_delivered_excerpt=True
clause_2_in_delivered_excerpt=True
distinct_printed_page_locators=1
```

The cited locator resolves in the delivered text at `source-excerpt.md:3`; both mapped clauses are on `source-excerpt.md:5`. The note independently gives the same Chapter V / “The Maya” / “The Creation-Story” / printed p. 209 locator at `inspiration-note.md:5`.

**M3 clause→element index** — cwd `/tmp/lore-c7b-round88-JKsNEQ`:

```sh
python3 - <<'PY'
from pathlib import Path
import re
p = Path('corpus/fixtures/r88-m3-maya-cluster')
excerpt = (p / 'source-excerpt.md').read_text()
verse = (p / 'fictional-excerpts.md').read_text()
map_text = (p / 'symbolism-clause-map.md').read_text()
rows = re.findall(r'^\| “(.+?)” \| “(.+?)” \|', map_text, re.M)
norm = lambda s: ' '.join(re.findall(r'[a-z0-9]+', s.lower()))
source = norm(excerpt)
checks = [(norm(clause) in source, element in verse) for clause, element in rows]
print(f'index_rows={len(rows)}')
for i, (clause_ok, element_ok) in enumerate(checks, 1):
    print(f'row{i}: cited_clause_in_excerpt={clause_ok}; fictional_element_in_authored_verse={element_ok}')
print(f'resolved={sum(a and b for a, b in checks)}/{len(rows)}')
PY
```

Observed:

```text
index_rows=2
row1: cited_clause_in_excerpt=True; fictional_element_in_authored_verse=True
row2: cited_clause_in_excerpt=True; fictional_element_in_authored_verse=True
resolved=2/2
```

**M3 attribution / rights / training and boundary markers** — cwd `/tmp/lore-c7b-round88-JKsNEQ`:

```sh
python3 - <<'PY'
from pathlib import Path
p = Path('corpus/fixtures/r88-m3-maya-cluster')
note = (p / 'inspiration-note.md').read_text()
excerpt = (p / 'fictional-excerpts.md').read_text()
map_text = (p / 'symbolism-clause-map.md').read_text()
checks = {
    'attribution_limited_to_spence': "passage only to Spence's account" in note,
    'not_primary_kiche_or_general_maya_claim': "does not treat it as a K'iche-language edition" in note and "represent all Maya or K'iche traditions" in note,
    'rights_status_unresolved': 'has not been determined' in note,
    'training_permission_unassessed': 'not been assessed or established' in note,
    'verse_marked_newly_authored': 'Newly authored fictional verse' in excerpt,
    'register_marked_newly_authored': 'Newly authored fictional register' in excerpt,
    'map_marked_editorial': 'editorial interpretations' in map_text,
    'inspiration_not_fictional_canon': 'supplies no fictional canon' in note,
}
for key, value in checks.items():
    print(f'{key}={value}')
print(f'checks_passed={sum(checks.values())}/{len(checks)}')
PY
```

Observed:

```text
attribution_limited_to_spence=True
not_primary_kiche_or_general_maya_claim=True
rights_status_unresolved=True
training_permission_unassessed=True
verse_marked_newly_authored=True
register_marked_newly_authored=True
map_marked_editorial=True
inspiration_not_fictional_canon=True
checks_passed=8/8
```

**M3 record-source resolution** — cwd `/tmp/lore-c7b-round88-JKsNEQ`:

```sh
python3 - <<'PY'
from pathlib import Path
import json
p = Path('corpus/fixtures/r88-m3-maya-cluster')
source_ids = {x['id'] for x in json.loads((p / 'sources.json').read_text())}
entities = json.loads((p / 'entities.json').read_text())
timeline = json.loads((p / 'timeline.json').read_text())
records = [(f'entity:{e["id"]}', c['source_id']) for e in entities for c in e['claims']] + [(f'event:{e["id"]}', e['source_id']) for e in timeline]
print('source_file_ids=' + ','.join(sorted(source_ids)))
print('record_attributions=' + ','.join(f'{name}:{source_id}' for name, source_id in records))
print(f'unknown_source_ids={sum(source_id not in source_ids for _, source_id in records)}')
PY
```

Observed:

```text
source_file_ids=paired-clock,veil-verse
record_attributions=entity:aru:paired-clock,entity:evin:paired-clock,entity:quiet-rise:paired-clock,entity:salt-court:paired-clock,event:aru-ninth-bell:paired-clock,event:evin-ninth-bell:paired-clock
unknown_source_ids=0
```

The paired-clock text itself is delivered as authored in-world text in `fictional-excerpts.md:8-11`.

**M4 OBS-1 repair** — cwd `/tmp/lore-c7b-round88-JKsNEQ`:

```sh
python3 -c 'import json,re,pathlib; p=pathlib.Path("corpus/fixtures/r87-myth-cluster"); t="\n".join(x[2:] for x in (p/"lowwater-hymn-excerpt.md").read_text().splitlines() if x.startswith("> ")); c=re.findall(r"^\| “(.+?)” \|",(p/"symbolism-clause-map.md").read_text(),re.M); e=next(x for x in json.loads((p/"entities.json").read_text()) if x["id"]=="mother-tide-gate"); print("gate_named={}; first_appearance={}; claim_source={}; clause_matches={}/{}".format("Mother-Tide Gate" in t,e["first_appearance"],e["claims"][0]["source_id"],sum(x in t for x in c),len(c)))'
```

Observed:

```text
gate_named=True; first_appearance=lowwater-hymn; claim_source=lowwater-hymn; clause_matches=8/8
```

**Census before → after** — baseline extracted from `dfd1fbc`, compared with the combined scratch tree; cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`:

```sh
baseline=$(mktemp -d /tmp/lore-c7b-base-XXXXXX) && git archive dfd1fbc3711f2b28597d74444819aca91fe6bc31 | tar -x -C "$baseline" && python3 - "$baseline" /tmp/lore-c7b-round88-JKsNEQ <<'PY'
from pathlib import Path
import sys
for label, root in [('before', Path(sys.argv[1])), ('after', Path(sys.argv[2]))]:
    fixtures = root / 'corpus' / 'fixtures'
    notes = list(fixtures.rglob('inspiration-note.md'))
    dirs = [p for p in fixtures.iterdir() if p.is_dir()]
    print(f'{label}: inspiration_notes={len(notes)}; fixture_directories={len(dirs)}')
PY
```

Observed:

```text
before: inspiration_notes=1; fixture_directories=145
after: inspiration_notes=2; fixture_directories=146
```

**Kotodama handoff-contract availability** — cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`:

```sh
if test -f ../kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md; then printf 'integration_contract=present\n'; else printf 'integration_contract=absent\n'; fi
```

Observed: `integration_contract=absent`.

## Findings & named debt

- **(a) Passage-locator spot check — PARTIAL.** The citation and its two mapped clauses resolve in the delivered excerpt (locator check and index commands above). M3 only contains one unique printed-page locator, p. 209; three distinct passage locators cannot be verified because two are not supplied. This is a source-coverage limitation, not a mismatch between the delivered quote and its citation.
- **(b) Clause→element index — PASS.** Both rows mechanically resolve to source clauses and to authored verse (2/2). Both readings are explicitly editorial and bounded; the text does not generalize them into K'iche symbolism (`symbolism-clause-map.md:3,7-10`).
- **(c) Attribution / rights / training separation — PASS.** Attribution is limited to Spence's English-language account, not treated as a primary K'iche edition or a general Maya claim. Rights and AI-training permission remain separately unanswered (`inspiration-note.md:7,9-19`). No legal rights conclusion is made.
- **(d) Repaired r87 cluster — PASS.** With the excerpt alternative, the Gate is named in the delivered hymn and the map has 8/8 quoted-clause matches. The claim and first appearance remain sourced to `lowwater-hymn`; both r87 and M3 checkers pass. The repoint alternative was not applied.
- **(e) Kotodama boundary — BOUNDED PASS; process unverified.** The boundary references place mythic/symbolic system generation with kotodama and world-bible canon recording/verification with lore (`kotodama-shokunin/PROVINCE.md:3-22`, `AGENTS.md:8-9`). Here the external comparison is kept out of canon, verse/register are marked newly authored, and the clause map is a narrow editorial index tied to named fictional elements—not a general mythic system. However, M3 includes authored symbolic material in the lore cluster, and the formal integration contract is absent; the expected upstream generation/handoff procedure therefore cannot be verified. Do not report full procedural conformance.
- **Named debt:** only one distinct M3 passage locator is delivered; the kotodama/lore handoff contract is absent. The M3 passage-level and process bars remain limited by these gaps even though the excerpt and index content checked here are internally supported.

## Handoff

Use `patches/M3-cluster2.patch` together with `patches/M4-obs1-excerpt.patch` as audited; they apply in that order and pass both checker replays. Carry the single-locator limitation and missing formal handoff contract as explicit debt. This seat wrote only `.ufo/waves/round-88/C7B.md`; no patch, tracked corpus file, sibling repository, commit, or push was touched.

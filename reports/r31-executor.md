# Round 31 executor — controlled ambiguous-source pair

## Artifacts
Created only `corpus/fixtures/r31-source-unique/` and `corpus/fixtures/r31-source-ambiguous/` (five JSON files each), plus this report. Unique is byte-identical to `consistent/`. Ambiguous adds one structurally valid source row to `sources.json` with duplicate ID `courier-log`, distinct title/kind/reliability note and no story claim. `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical between pair; notably `relations[0]` remains Mira → seal, `carries`, source `courier-log`.

## Checker replay (complete output)
Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`

`r31-source-unique`: exit 0; stdout:
```
CLEAN: schema, citations, relations, timeline; 0 violations
```
stderr: empty.

`r31-source-ambiguous`: exit 1; stdout:
```
VIOLATION: sources[2].id: duplicate sources id 'courier-log'
VIOLATION: entities[0].first_appearance: ambiguous in-world source 'courier-log'
VIOLATION: entities[0].claims[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: entities[3].first_appearance: ambiguous in-world source 'courier-log'
VIOLATION: entities[3].claims[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: relations[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[1].source_id: ambiguous in-world source 'courier-log'
8 violation(s); no canon changed
```
stderr: empty. Thus the relation-local ambiguity is present, alongside all other affected references; it is not an isolated relation-only delta.

Prior-art replay: `r7-ally-reverse-ambiguous` exit 1; stdout:
```
VIOLATION: sources[2].id: duplicate sources id 'harbor-compact'
VIOLATION: relations[1].source_id: ambiguous in-world source 'harbor-compact'
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
3 violation(s); no canon changed
```
stderr: empty. This is prior ambiguous citation coverage for a reverse `allied_with` relation, not the controlled non-alliance `carries` case.

## Pair diff and boundary
The byte difference is confined to `sources.json` in ambiguous: one appended source row. The other four JSON files match each other byte-for-byte, and unique matches `consistent/` in all five. Duplicate source identity yields unresolved reference ambiguity, not evidence that the carries claim is false, true, or canonically resolved; no source authenticity, real-world rights, or usage-rights conclusion follows.

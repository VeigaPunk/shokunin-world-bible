# Round 7 alliance reverse-witness scout

## Scope

Scout-only probe of how duplicate `sources.json` IDs affect the alliance reciprocal-witness check. No checker, fixture, shared document, or commit was changed. The probes were temporary copies under `/tmp/r7-alliance-bmkcg76j/`.

## Observed evidence

- In `.shokunin/lore/corpus/fixtures/check_bible.py`, `index(section)` (lines 39–45) emits a duplicate-ID error but overwrites `result[row['id']]` with the later row. Thus `sources` is a last-wins mapping. In the alliance check (lines 177–188), a candidate reverse edge qualifies when `candidate['source_id'] in sources`; it does not establish uniqueness.
- Control CLI replay from the repo root: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-reciprocal` (correct path spelling: `.shokunin/...`) exits 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`. The one-way control exits 1 with `relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`.
- Duplicate-source reciprocal probe: copied `ally-reciprocal`, duplicated its `harbor-compact` source row, retained the two reciprocal edges, and ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r7-alliance-bmkcg76j/duplicate-reciprocal`. Exit 1, but output was only `sources[1].id: duplicate sources id 'harbor-compact'`; the reverse edge was still accepted as a sourced witness.
- More targeted probe: `/tmp/r7-alliance-bmkcg76j/duplicate-reverse-only` retained a uniquely sourced forward edge and made only the reverse edge cite a duplicated `harbor-compact` ID. CLI exit 1 output only `sources[2].id: duplicate sources id 'harbor-compact'`. It did **not** report the forward relation as lacking a sourced reciprocal. This demonstrates directly that a duplicate-ID reverse citation still qualifies.

## Narrow recommendation (proposal, not observed behavior)

Treat a source ID as a qualifying alliance witness only when it resolves to exactly one valid source row. Keep both duplicate source records and the existing duplicate-ID diagnostic; do not pick a winner. For a reverse relation whose `source_id` is ambiguous, do not let that relation satisfy reciprocity. The uniquely sourced forward edge should then get the existing local `lacks a sourced reciprocal relation` finding, alongside the duplicate-ID finding. Do not make this a blanket invalidation of every relation or every claim that happens to use the duplicated ID: report ambiguity at affected references, and let only the specific decision requiring an unambiguous witness fail qualification. A reciprocal edge with a different unique source should still qualify.

This is citation-ID qualification only: it does not inspect whether source text supports the alliance, prove either faction's actual canon status, or decide which duplicate record is authoritative.

## Boundary probes still needed

- Duplicate ID appears on an unrelated source while the reverse edge uses a different unique source: reciprocity should remain satisfied.
- Both directions cite the same ambiguous ID: neither is a qualified witness; avoid cascading unrelated entity/claim semantics beyond the explicit reference diagnostics.
- Duplicate reverse record and a separate unique reverse record: the latter should qualify; ambiguity of one candidate should not poison a distinct unique witness.

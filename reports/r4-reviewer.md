# Round 4 independent review — exact display-name check

## Scope and method

Read the Round 4 LOG declaration and scope clarification, current checker, fixture README and raw JSON for all seven fixtures. I did not rely on the executor report for outcomes. Replayed each fixture with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` and captured exit/stdout in memory. Also loaded the checker from baseline commit `5ceb0e431f686ed0ee29f11b66939c8f661dcc63` using `git show`, executed that baseline implementation against the same seven raw fixture directories, and compared diagnostics. No implementation edits; no commit. Only this report path is written.

## Seven-fixture replay

| Fixture | Current exit / result | Baseline diagnostics preserved? |
|---|---|---|
| `consistent` | 0; clean | Yes (0) |
| `contradictions` | 1; dangling `missing-map`, timeline inversion, double booking | Yes (same three, same order) |
| `ally-reciprocal` | 0; clean | Yes (0) |
| `ally-one-way` | 1; missing sourced reciprocal relation | Yes (same one) |
| `contradictions-ledger-malformed` | 1; malformed ledger pointer plus the three preceding contradiction findings | Yes (same four, same order) |
| `name-unique` | 0; clean | Yes (0) |
| `name-duplicate` | 1; one name diagnostic for `entities[0]`/`entities[1]`, IDs `mira-one`/`mira-two`, exact `'Mira'` | Baseline is clean; this is the intended new finding |

The name fixture pair is well isolated structurally: each contains all five JSON sections; parsed entity arrays have two rows each, with only `entities[1].name` differing (`Mira Two` versus `Mira`). Raw `sources.json`, `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical across the pair. The checker reports both locations and IDs, preserves the records, and says “review, do not merge.” The exact-string, case-sensitive implementation is restricted to schema-valid rows whose IDs each occur exactly once; duplicate-ID groups do not create a name finding. No normalization is apparent in code.

## Fixture/source integrity and evidence limits

Both entity rows cite `registry` for `first_appearance` and their claim; that source ID resolves to the shared fictional source record. Its title is “Lantern Harbor Names Register, year 12,” and reliability note says it is an invented in-world record of display names, not proof of identity or unique naming. This supports describing the data as fictional and limits identity claims. However, checker citation validation is ID resolution only. It does not inspect source contents or establish that the register actually assigns the exact `name` values. The claim statements say “Mira One” and “Mira Two,” while the display-name fields are `Mira` / `Mira Two` in the clean pair and `Mira` / `Mira` in the duplicate pair. The source is only a metadata record, not quoted/source text establishing either exact field. Thus fixture provenance is internally referenced, but actual name attestation cannot be independently verified from these artifacts. Do not claim the source proves the names or that the duplicate is a canon error.

## False-positive caveat / assessment

The critical limitation is real: two distinct entities can legitimately share a name (homonyms), and the available schema, examples, and sources establish no uniqueness invariant. The checker will flag such an intentional homonym exactly like an accidental collision. This is a **false positive if interpreted as a canon violation**. The LOG and fixture README scope it as an editorial review diagnostic, not identity proof, invalid canon, or a command to merge; under that narrow interpretation it is a useful candidate for human attention, not a demonstrated correctness rule. Because this rule now exits nonzero, consumers must understand that the exit is a review stop, not proof of a lore inconsistency. There is no exception/disambiguation field, intentionally.

Coverage is narrowly demonstrated for exact equal raw strings among unique-ID valid entity rows, with one positive and one clean negative; it says nothing about aliases, case/whitespace/Unicode variants, or semantic identity. The old behavior is intact on the five prior fixtures by direct baseline replay, and clean/contradiction outcomes match exactly. I found no implementation defect within the declared scope. The scope itself remains a chosen editorial convention, and a source-backed claim that these names are attested is unproven by the available source metadata.

## Limits

This review covers the current seven fixtures, direct comparison to the stated baseline checker, and a code/schema inspection. It does not exhaust malformed rows, duplicate-ID interactions, Unicode behavior, other bibles, or production consumers. I made no temporary fixture edits or extra probes. I did not independently verify any fictional source beyond its raw JSON metadata; there is no source text to inspect.

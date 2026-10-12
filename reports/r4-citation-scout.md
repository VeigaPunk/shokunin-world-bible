# Round 4 citation scout: what duplicate entity names establish

## Observed source path

Round 4's stated proposal is specifically an exact, case-sensitive duplicate of `entities[].name` across distinct entity IDs; it preserves IDs and is not meant to merge canon (`.shokunin/lore/LOG.md`, Round 4 declaration).

In the fixture schema, the displayed name is a required nonempty string on each entity record, but is not itself a citation object (`corpus/fixtures/check_bible.py`, `FIELDS['entities']`). Each entity instead has `first_appearance` and `claims`; the checker resolves `first_appearance` as an in-world source ID and checks each claim's `source_id` similarly. The source IDs resolve against `sources.json`, whose entries provide title, kind, and a reliability note. This is a resolution check: the checker does not establish that a source actually uses or supports the entity's `name`, nor does it compare source text to a name (`corpus/fixtures/check_bible.py`, entity/source validation; `corpus/fixtures/consistent/sources.json`).

Examples make the distinction concrete. `mira` has display name `Mira`, first-appearance source `courier-log`, and a claim citing that source; `harbor` has name `Lantern Harbor`, first-appearance and claim source `archive-ledger` (`corpus/fixtures/consistent/entities.json`; `corpus/fixtures/consistent/sources.json`). The records identify these as a fictional first-person route log and a fictional municipal record respectively; their reliability notes explicitly limit what they attest. The faction entities `quay-guild` and `bell-wardens` each cite `harbor-compact` for first appearance and a claim that each is named as a party to that mutual compact (`corpus/fixtures/ally-reciprocal/entities.json`; `corpus/fixtures/ally-reciprocal/sources.json`). These are source-backed fixture assertions, not external or universal facts. Fixture documentation says all entries are invented and that `source_id`/`first_appearance` point to in-world records (`corpus/fixtures/README.md`).

## What duplicate names do not prove

- Two different IDs with the same exact `name` do not prove the records denote one entity. The IDs remain separate in this data model; a name-only collision is not an identity or merge instruction.
- A collision does not prove the name is an alias, a title, a transliteration, or a mistaken duplicate. No alias/disambiguation semantics are represented by the observed entity fields.
- A collision does not prove either name is canonically wrong, that an in-world source supports the spelling, or that the source is truthful. Current validation resolves source IDs but does not inspect citation contents or corroborate names (`corpus/fixtures/check_bible.py`; `corpus/fixtures/README.md`).
- Conversely, distinct spellings or distinct IDs do not prove distinct in-world referents. This exact-name test cannot find alias, near-match, case-folded, transliterated, or semantic identity cases; the round claim explicitly excludes those broader interpretations (`.shokunin/lore/LOG.md`, Round 4 declaration).
- Repeated name text within one entity's claims or sources is not, by itself, a duplicate entity-name condition: the proposed scope is names on distinct valid entity records.

## Recommendations (not observations)

1. Keep any diagnostic narrowly factual: report the exact matching name, both entity array locations, and both IDs; retain both records and all references. Phrase it as a duplicate display-name collision requiring editorial review, not as a resolved identity conflict.
2. If a policy permits intentional same-name entities, require an explicit, documented disambiguation mechanism and cite the source for the disambiguating assertion. Do not invent that mechanism from the current schema or silently exempt records.
3. Keep source-ID resolution distinct from source-content verification. If the project later wants to establish that a name is attested, define that as a separate citation/content policy; the current checker only verifies reference resolution.
4. Preserve the declared limits: exact case-sensitive equality only; no claim about aliases, canon impossibility, source reliability, or real-world names.

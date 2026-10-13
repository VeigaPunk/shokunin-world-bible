# Round 64 citation-scout — malformed entity rows and identity boundary

## Independent calibration verdict: **NO-GO on current materiality evidence**

The hypothesis is narrow and worth a paired probe, but I do not find enough demonstrated operator benefit to recommend admitting a new finding/status. Existing checker intentionally builds its reference index from schema-admitted rows. Treating a rejected row’s raw `id` as making a reference indeterminate would create a second, non-admitted identity index and could suppress a precise `dangling entity` repair pointer. The raw ID does not qualify the row as a valid entity. Any future implementation needs matched evidence that its benefit outweighs that loss; no checker or fixture change is warranted on this scout.

## Observed baseline (path:line)

- `.shokunin/lore/corpus/fixtures/check_bible.py:65-76` reports a non-object row or required-field/type/nonempty errors and retains only rows passing the required-field screen in `data[section]`. For entities, required fields include `id`, `kind`, `name`, `first_appearance`, and `claims` (`:25-28`). A row with a usable string `id` but a missing/invalid other required field therefore is not indexed.
- `check_bible.py:78-84` builds `entities` from those admitted rows and counts duplicate IDs among admitted entity rows. `:157-160` separately counts those same admitted entity IDs. The checker does not currently preserve or consult raw rejected-row IDs for entity reference resolution.
- Relation endpoints, when the entity table loaded, are checked against that admitted index at `:161-169`; absent IDs produce `dangling entity`, duplicates produce `ambiguous entity`. Provenance holders use admitted-row counts at `:206-224`: zero yields field-local dangling output; multiple makes the record invalid and suppresses chain comparison, without selecting a row. Timeline reference handling likewise uses the `entities` index/counts (inspect current code around `:250-280`). These are assertions about input-table membership/resolution only.
- R60 is adjacent but different: its tested rule separates a wholly unavailable entity table from a successfully loaded empty/partial array; it does not change the admission rule for malformed rows inside a loaded array. Its reports explicitly retain rows that pass screening and do not infer fictional-world absence.
- R56 is also adjacent: duplicate IDs among admitted rows already make provenance chain checks invalid; its proposed improvement concerned locating an ambiguous admitted ID at a holder field, not treating a rejected row as a candidate identity. R16–18 likewise resolve/count schema-admitted raw IDs and keep names/source references distinct. These precedents do not establish that a rejected row's ID should suppress dangling findings.

## Proposed comparison and falsifier (not observed results)

No temporary probes were run for this assignment; do not describe any output as observed. A material candidate would need matched copies differing only in the entity row: (a) valid row with the referenced ID, (b) loaded empty array, (c) schema-rejected row with the same nonempty ID but a missing/invalid required field, (d) rejected row without usable ID, (e) valid duplicate ID, and (f) unavailable file. Exercise relation endpoints, timeline actor/place, provenance holder, and source-independent findings. Proposed status must retain the row-local schema diagnostic and every independent check, avoid counting the rejected row as a valid entity/kind/occupancy witness, and keep a repair pointer identifying the rejected row and reference. It must not turn a raw ID into fictional-entity existence.

The falsifier for this NO-GO is a demonstrated concrete decision where current dangling output is materially misleading or costly to repair, while a narrowly scoped “matching entity row invalid; reference unresolved” message is reliably more actionable across those controls and does not mask genuine absence/duplicate issues. Conversely, if both messages are needed for repair, or invalid-row IDs can conceal an actually missing valid row and add complexity without changing action, reject the candidate.

## Boundary

A JSON `id` is only an input identifier. The checker cannot establish that a fictional-world entity exists, that a source text supports it, or that any source/prose is true. Neither ID matching nor a citation establishes canon, copyright, license, permission, or training/use rights. No source prose or rights evidence was examined. No checker, fixture, README, LOG, corpus, or commit was changed.

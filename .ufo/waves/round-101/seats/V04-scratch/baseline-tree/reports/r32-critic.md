# Round 32 critic — source admission ambiguity challenge

## Falsification attempt

The declared behavior follows the implementation, but the absence of an ambiguity diagnostic is easy to overread. `.shokunin/lore/corpus/fixtures/check_bible.py:21-43` validates each source row against required fields and appends only valid rows to `data['sources']`. The duplicate-ID index and `source_id_counts` are built from that screened collection (`check_bible.py:45-56`); `source_status` therefore calls an ID ambiguous only when more than one admitted row remains (`:64-74`). Relation citations use that status at `:123-130`. Thus a malformed second row can coexist in raw `sources.json` while being invisible to this particular count. Its schema error is not a finding that it is false, irrelevant, or absent from the fictional world.

The key falsification risk is whether the proposed mutation truly isolates admission. Blank `title` must be the only changed field on the second `courier-log` row; the ID must remain the same, and all other fixture tables and source-row fields must match the valid duplicate comparator. A missing/wrong-type/blank title produces a row-local required-field error at `sources[1].title` (or the actual row index), and screening prevents that row from contributing either a duplicate-ID index error or citation multiplicity. But the proposed expected “seven ambiguous citation-reference findings” is conditional on the exact r31 pair inventory: it is not justified merely by the code path, and should be checked against the actual source-ID references and complete output. Other errors in the valid duplicate fixture may also remain in the malformed variant.

This is analogous to r26 only at the level of an admitted-row boundary: `.shokunin/lore/reports/r26-critic.md` and `.shokunin/lore/reports/r26-screen-scout.md` describe malformed duplicate *entity* rows excluded before entity-ID counts. That precedent does not establish behavior for source rows, whose count/index and consumers differ (`check_bible.py:53-56,64-74`); the controlled source pair is still needed. Nor does one blank-title probe establish screening behavior for every malformed field/type or duplicate ordering.

## Risks and calibration

- Say “no duplicate among admitted source rows” or “the checker emits no ambiguous-source-ID finding for this screened row,” not “the source ID is unique.” The raw duplicate remains present.
- Do not say the malformed source is disproven, invalid evidence in-world, canonically absent, or rights-cleared. The check validates record shape and counts admitted IDs; it does not inspect source prose or establish support, truth, or permissions.
- Preserve the row-local schema violation in the report. Omitting it would turn an input-quality failure into a misleading clean result.
- Count all output deltas. The expected loss of ambiguous citation findings should be attributable to the source count; unrelated diagnostics must not be silently erased or classified as reference fan-out without replay.
- The valid r31 duplicate is a positive comparator, not a novelty claim: r31 already demonstrated admitted duplicate behavior. r26 is precedent for entity screening, not proof of source behavior.

## Falsifiable test

Compare the valid r31 admitted-duplicate fixture with the proposed malformed-source fixture. Byte-compare all tables except `sources.json`; within that file verify exactly one changed value (`title` on the second duplicate row), retaining its duplicate `id`. Run the checker on the unique r31 control, valid duplicate, and malformed duplicate, capturing exact stdout/stderr/exit. Require: unique control clean; valid duplicate retains its duplicate-source diagnostic and eight-finding observed inventory; malformed variant reports the title schema error, does not report an admitted duplicate-source-ID error, and does not report the ambiguous `courier-log` citations (including the relation-local citation). Enumerate every remaining diagnostic rather than assuming they all disappear. Replay the declared 83-fixture output baseline and 414 pre-existing JSON bytes unchanged before admitting any round-level result.

This test can falsify the narrow calibration claim if the malformed row still contributes to the count, if the valid positive comparator lacks the expected ambiguity, or if unexplained diagnostics disappear. A passing test supports only this one required-field screening boundary in this checker; it does not resolve the raw duplicate, source content, canon, or rights.

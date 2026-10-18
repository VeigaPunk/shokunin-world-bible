# Round 60 loader-scout — section failure and entity-reference calibration

## Independent verdict: GO (narrow; entity-table availability only)

The current checker converts every load/parse failure into an empty row list, then runs ordinary reference resolution over that list. For a failed `entities.json`, this reports every valid reference as dangling, although the checker has no entity rows to establish either presence or absence. A tri-state table status (`loaded` versus `unavailable`) with dependent entity lookups skipped only in the unavailable case would correct that specific calibration error. This is not a judgment that any entity exists in the fictional world. Scope should be limited to entity-dependent checks; avoid claiming all cascades are suppressed.

## Observed loader and check flow

- `corpus/fixtures/check_bible.py:35-47`: `check()` iterates required `FIELDS`, reads each `<section>.json`, and catches duplicate-member, filesystem, decoding, and JSON syntax exceptions. Each catch appends a section-file error and assigns `rows = []`.
- `:48-63`: non-array top-level values also become `[]`; row-shape and required-field validation determines which rows enter `data[section]`. Thus valid empty array, unavailable file, malformed JSON, duplicate-member rejection, wrong top-level shape, and an array whose rows are all invalid converge to an empty usable section, but only the first means successfully loaded empty data.
- `:65-82`: indexes/counts for sources, entities and events are built from usable rows. Duplicate entity IDs are retained in `data['entities']`, counted, and the last row wins in the dictionary index; the checker still identifies ambiguity through `entity_id_counts` at some call sites.
- `:127-136`: entity rows validate kind and source references for first appearance/claims. These are source-table lookups, not entity lookups.
- `:138-150`: relations check each `from`/`to` against `entities` (`:146-149`) and independently check `source_id` (`:150`).
- `corpus/fixtures/check_bible.py:152-228` (provenance block): item-holder refs use `entity_id_counts` (`:193-205`); chain continuity/tick checks run only when row/reference validity permits (`:215-228`). These are entity-table dependent. Provenance source citations are separately checked at `:206-214`.
- `corpus/fixtures/check_bible.py:97-125`: contradiction-ledger references resolve timeline events and event source IDs, not entity IDs; they can remain assessable when entities are unavailable.
- `corpus/fixtures/check_bible.py:248-272` (timeline occupancy block): `entity_id` and `place_id` are checked against entities (`:250-261`); actor/place counts and place kind gate double-booking (`:253-272`). Dependencies use event indexes instead (`:273-294`) and can remain assessable.
- `:185-198`: findings are emitted and exit status is failure if any exist. The CLI's final text does not distinguish known-missing from unassessable references.

## Raw probe evidence (temporary copies outside repository)

I copied the active `r59-nested-duplicate` input to `/tmp` and independently ran `python3 check_bible.py <copy>` with four entity-table variants. These are observed current-checker outputs, not candidate outputs:

1. **Duplicate-member entities file** (the original nested duplicate): exit 1; `entities.json: duplicate object member 'source_id'; cannot load JSON`, followed by six `dangling entity` findings: relation `from mira`, `to seal`, timeline actor `mira` twice, and places `harbor` and `tower`.
2. **Missing entities.json**: exit 1; filesystem load error followed by the same six dangling-reference messages. Load failure does not establish that those entities are absent.
3. **Successfully loaded entities array with only `mira` removed**: exit 1; exactly three dangling findings (`relations[0].from` and the two timeline actor refs to `mira`); valid `seal`, `harbor`, `tower` references are accepted. This is known absence from the loaded input table and must not be suppressed.
4. **Successfully loaded empty `[]` entities table**: exit 1; six dangling findings, with no load error. Empty-but-loaded is not unavailable and must retain its dangling findings.

Additional duplicate-ID control: appended a second valid `mira` row (not a repeated JSON object member) to the loaded entities table. Current output was a duplicate entity-ID finding plus ambiguous `mira` references in relation `from` and both timeline actor fields; it did not call them dangling. This is an important preserved distinction: an available but non-unique entity registry is ambiguity, not unavailability or absence. Duplicate-ID ambiguity can continue using the existing loaded-row logic.

## Entity-reference inventory and risk boundary

For an unavailable `entities` table, suppress/mark unassessable only checks whose conclusion is a lookup into that table: relation endpoint existence/ambiguity (`:143-149`); provenance holder existence/cardinality and resulting chain eligibility (`:77-95`, `:105-118`); timeline actor/place existence, ambiguity, place-kind, and occupancy comparability (`:138-160`). Preserve the `entities.json` load/shape diagnostic itself. Retain source validation for relations and entity rows when available, event-ID/dependency validation (`:163-184`), and contradiction event-reference checks (`:97-125`) because their indexes are independent. Entity-row first-appearance/claim source checks cannot run if entity rows did not load, but should not be fabricated as dangling entity findings.

A minimal implementation must use explicit availability state, not `if not entities`, because a valid empty table is loaded and genuinely makes every referenced ID absent. Consider separately whether a structurally loaded partial table (some valid rows plus invalid rows) warrants partial findings: current loader retains valid rows and separately emits row errors. Do not conflate this with whole-file failure; it may be reasonable to keep findings for IDs absent from successfully loaded valid rows, but document that they are input-table conclusions, not world absence. Failed `sources.json` and `timeline.json` create analogous cascades (e.g. citation/event lookups), but are outside this narrow recommendation; do not claim comprehensive unavailable-section handling without analogous probes and explicit section-specific policy.

## Prior art, falsifier, regression/cascade risk

- R5 missing-file precedent (`fixtures/r5-missing-file/`, checker behavior evidenced in live history): missing `contradictions.json` emits its file error without reference cascades because no other section consults contradiction rows. It is not evidence that a heavily referenced unavailable entities table is already gated.
- R59 closure explicitly recorded that nested duplicate `entities.json` produced six dependent dangling findings, and admitted them as a bounded cascade rather than proof entities were absent. This round can improve calibration without revising parser policy or declaring duplicate members legal.
- R11/r12 and r16-r19 existing families cover dangling, duplicate/ambiguous actors/places, kind checks, and occupancy only with loaded entity registries; they do not establish behavior for unavailable tables. The dedicated loaded-table probe above supplies the missing contrast.
- Falsifier: an implementation that suppresses findings for loaded empty/partial entities tables, changes duplicate-ID ambiguity to unavailable/absent, or skips independent source/event checks would be overbroad and should be NO-GO. Another falsifier is evidence that operators need the dangling lines as a meaningful, already-unambiguous statement specifically after failed entity loading; current raw output gives no qualifier and the r59 duplicate-member failure makes that reading unsafe.
- Regression risk: global suppression keyed to empty `data['entities']` would silently hide genuine dangling references in valid `[]` and wrong-top-level cases. Suppression must key on explicit loader status. Whole-table unavailability makes duplicate/absence/kind conclusions unassessable; it does not validate references. A checker policy must choose whether to omit dependent findings or label them `unassessable`; omission minimizes noisy cascades, whereas explicit marking preserves visibility but can multiply output. Either way preserve parser and other-section diagnostics, test missing/invalid/duplicate-member table failures, loaded-empty and loaded-no-mira controls, and duplicate-ID ambiguity. Compare all pinned 99 raw outputs/494 JSON bytes, accounting for the intentional r59 nested-duplicate delta. No claim about actual lore, canon, source-text support, rights, or permission.

## Axis assessment

- **Calibration: GO**, narrowly for entity lookup dependent on a failed `entities.json`: current output states “dangling” without qualification although the table was not assessable; a loaded-empty/loaded-no-mira control proves a distinct input condition where dangling is meaningful.
- **Depth: unchanged. Coverage: unchanged.** This is interpretation of existing checker outputs, not a new world fact or new check class.
- **Observed:** current raw outputs above. **Proposed:** explicit loaded/unavailable distinction and withholding or marking entity-reference results unassessable only when the entity table is unavailable. No candidate implementation/output has been observed by this scout.

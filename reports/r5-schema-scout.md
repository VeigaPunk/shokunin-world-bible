# Round 5 schema scout — malformed row shape versus crash

## Observation

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py` and clean input `.shokunin/lore/corpus/fixtures/consistent/`. The loader catches file/JSON decoding failures, then requires each table to be a list. For each list element it checks `isinstance(row, dict)` before field access; non-object elements produce `SECTION[index]: expected object` and are skipped. Object rows missing required fields or with wrong exact Python types produce field-local violations and are skipped from semantic processing (`valid = False`). The existing claim and timeline subrecord loops have their own type checks.

I probed by copying the clean fixture to disposable `/tmp/lore-r5-schema-probe-0dodfsob/` directories, changing only `entities.json`, and running:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-schema-probe-0dodfsob/null-row
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-schema-probe-0dodfsob/string-row
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-schema-probe-0dodfsob/empty-object
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-schema-probe-0dodfsob/wrong-list-field
```

All returned exit 1 with stdout diagnostics, empty stderr, and no traceback. A `null` or string row produced `entities[4]: expected object`; `{}` produced five required-field errors; a string in `claims` produced `entities[4].claims: required nonempty list`. The untouched baseline command `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` returned 0 and `CLEAN: schema, citations, relations, timeline; 0 violations`.

Additional probes with an array-valued entity ID / source reference and relation endpoint were stopped by required-field type checks, also exit 1 without traceback. In the tested cases, malformed row shapes are reported as violations, not crashes. These probes do not establish that all malformed nested values are safe, nor exhaustive crash-freedom.

## Bounded table conditions (recommendation)

For a fair round-5 table, use the committed clean fixture as the single parent, copy it per case, and mutate one field/row only. Table columns should be: case, exact fixture path, one mutation, exact CLI command, exit status, diagnostic class (and stable location/message fragment), stderr/traceback observed, interpretation. Include one untouched clean baseline and one representative of each declared class only. For row shape, keep the bounded distinction between (a) non-object list element (`expected object`) and (b) object row with missing/wrong-typed required field (field-local required-type diagnostic); do not imply every nested schema shape was tested. Capture stdout/stderr and exit code as raw run artifacts; do not infer “crash” from exit 1—crash means traceback/nonzero without the checker's normal violation summary, and must be recorded separately.

Use committed fixture directories and root-relative invocations, e.g. `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`. Keep case mutations independent; no combining malformed row shape with bad citations. Temporary probes named above were disposable and are not committed evidence. No checker, fixture, or shared-document changes were made.

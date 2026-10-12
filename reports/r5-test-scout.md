# Round 5 test scout — independent replay plan

## Observation

The round-5 claim is a calibration/evidence claim: document actual CLI behavior for isolated malformed-input classes while leaving `corpus/fixtures/check_bible.py` unchanged. The loader catches missing/unreadable files, Unicode errors, and JSON decode errors under a common `cannot load JSON` class; decoded non-arrays become `expected array`; non-object rows become `expected object`; unresolved entity citations produce `unknown in-world source`. Any nonempty error list prints `VIOLATION:` diagnostics and exits 1. A clean bible prints `CLEAN:` and exits 0. These are diagnostic *classes*, not asserted exact full output strings.

## Replay protocol (recommendation)

From repository root, use committed independent fixture directories under `.shokunin/lore/corpus/fixtures/r5-malformed/`. Each malformed directory should be copied from `consistent` and change exactly one aspect. Do not edit the checker or the source fixture. The fixture paths below are proposed names; the implementation lane should ensure these exact committed paths exist, or report any naming deviation before replay.

| Case | Raw fixture path | Single mutation from `consistent` | Expected exit | Expected diagnostic class |
|---|---|---|---:|---|
| clean control | `.shokunin/lore/corpus/fixtures/consistent` | none | 0 | `CLEAN` |
| missing file | `.shokunin/lore/corpus/fixtures/r5-malformed/missing-file` | omit `contradictions.json` | 1 | `cannot load JSON` on that file |
| invalid JSON | `.shokunin/lore/corpus/fixtures/r5-malformed/invalid-json` | make `sources.json` syntactically invalid JSON | 1 | `cannot load JSON` on that file |
| wrong top-level type | `.shokunin/lore/corpus/fixtures/r5-malformed/wrong-top-level` | make `sources.json` valid JSON but an object, not an array | 1 | `expected array` |
| row shape | `.shokunin/lore/corpus/fixtures/r5-malformed/row-shape` | replace one source array row with a scalar | 1 | `expected object` |
| invalid citation | `.shokunin/lore/corpus/fixtures/r5-malformed/invalid-citation` | change one entity `first_appearance` to a nonexistent source ID | 1 | `unknown in-world source` |

Run each raw fixture with the unchanged checker, recording exit status and stdout/stderr separately:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-malformed/missing-file
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-malformed/invalid-json
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-malformed/wrong-top-level
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-malformed/row-shape
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-malformed/invalid-citation
```

For each run, verify the class by a bounded category match (e.g. `expected array`, not exact full diagnostic text); verify exit 0 only for clean and 1 for each malformed case. Do not require diagnostic ordering or punctuation. The non-author verifier should independently inspect the raw JSON mutations, establish each case differs from `consistent` only in its specified aspect, then execute the commands above. Capture outputs and exit codes as raw evidence under a distinct run directory such as `.shokunin/lore/corpus/live/runs/<timestamp>/`; do not treat a prose table alone as replay evidence.

## Regression bounds

To support “preserved old outcomes,” also replay the established cases using the same checker and compare by outcome class, not a copy of full strings: `consistent` exits 0 / clean; `contradictions` exits 1 / three seeded violations; `ally-reciprocal` exits 0 / clean; `ally-one-way` exits 1 / missing-reciprocal relation class; `contradictions-ledger-malformed` exits 1 / ledger pointer class plus the three seeded violations. Their concrete commands are the README commands under `.shokunin/lore/corpus/fixtures/`. Verify checker bytes are unchanged against the round-5 baseline commit (`git diff <baseline> -- .shokunin/lore/corpus/fixtures/check_bible.py`) and that no fixture mutation touches `consistent` or prior cases. This bounds regression testing; it is not an exhaustive malformed-input claim.

## Interpretation / limits

The five malformed rows test one representative of each named class, not all parser, filesystem, or schema failures. `cannot load JSON` intentionally groups several causes; the proposed missing-file and invalid-JSON cases exercise two causes, not every caught exception. These probes establish observed diagnostics and exit classes only. They do not establish usability for all malformed bibles, input repair, canon validity, or correctness of citations. Keep the checker unchanged and state any mismatch rather than adapting the expected result after seeing it.

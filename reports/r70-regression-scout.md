# Round 70 regression scout — 130-case replay and R62 preservation

## Pin and scope

Round 70 in `.shokunin/lore/LOG.md` pins baseline `5ccbffaf4b593dcfa34bf92a8ac351c83a105ab3` (short `5ccbffa`). `git rev-parse HEAD` matched that pin. At inspection time `git status --short` showed only a pre-existing modification to `.shokunin/lore/LOG.md`; I did not edit it. The checker at the pin is `.shokunin/lore/corpus/fixtures/check_bible.py`. Its current final ledger-pair comparison tests dictionaries with equal `.get('event_id')` and `.get('field')`, without requiring nonempty event IDs. The Round 70 declaration instead proposes requiring each event ID to be a nonempty string, while retaining raw field equality and other field validation.

This report checks old fixture preservation against a temporary, uncommitted candidate generated from the pinned checker with exactly that proposed comparison gate: both sides must have nonempty string event IDs, then event IDs and fields must match. No repository checker or fixture was modified. This is regression evidence only, not an admission or calibration judgment.

## Baseline corpus and raw outcomes

I enumerated all immediate fixture directories and ran the pinned checker on all **130** using repository-root cwd and root-relative checker and fixture arguments (`python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`). For each case I retained the process status and raw stdout/stderr bytes. All 130 stderr streams were empty. The fixture tree has **709 tracked paths** (645 JSON files); pin and working tree have the same path set, all 709 raw file contents match the pin, and `git diff <pin> -- .shokunin/lore/corpus/fixtures` is empty. The pinned checker bytes equal the checked-out checker bytes.

I replayed the same 130 directories through the temporary candidate with the same cwd and fixture argv, comparing exit status, stdout bytes, and stderr bytes separately and exactly. Result: **130/130 tuples identical; zero changed cases**. No normalization was used. The proposed gate therefore does not change any current fixture outcome, including the special malformed-side case below. The old corpus does not itself exercise absent/blank event IDs that the candidate gate is intended to distinguish.

## R62 preservation and relevant fixtures

`.shokunin/lore/corpus/fixtures/r62-malformed-side/` is the key preservation check. It has a malformed timeline and equal, nonempty event IDs (`tarin-envelope-observation`) paired with equal unsupported fields (`bogus`). Baseline and candidate both exit 1 and emit, in the same order: the timeline parse error; invalid-field findings for `claim_a` and `claim_b`; `claim_a and claim_b references must differ`; and `4 violation(s); no canon changed`. Thus the Round 70 event-ID-only gate preserves the R62 pair warning despite invalid fields, as declared. This avoids the Round 69 broad gate’s changed behavior on that tuple.

Other directly relevant old cases also remained byte-identical: `contradictions` (valid identical pair); `r37-ledger-unique` (valid distinct pair); `r37-ledger-ambiguous`; `contradictions-ledger-malformed`; and the R62 empty, loaded, partial, missing, malformed, nonarray, duplicate-member, and duplicate-ID timeline variants. These results establish only what current committed fixtures cover; some do not contain identical ledger pairs.

## Limits and next evidence

This is an exact old-fixture replay against a **temporary synthetic candidate**, not a committed candidate, independent implementation, full matched-probe study, or reviewer judgment. Because no old fixture has missing or blank event IDs on equal sides, the 130-case replay proves preservation but does not show the intended delta. A materiality review still needs matched cases for both IDs absent, both blank, one absent/blank and one usable, valid identical references, and valid distinct references; it should confirm that only the unsupported pair-level finding disappears in the unusable-ID cases, while independent required-ID/field diagnostics and the R62 warning remain. Results should be captured with exact stdout/stderr/exit, and the distinction between unusable ID and valid-but-unresolved ID must remain explicit.

No source text was assessed. This is solely a structural checker/fixture diagnostic analysis, not a claim about event occurrence, what sources say, story contradiction, canon, rights, permissions, or game mechanics. Only this report is intended to be written; no checker, fixture, README, LOG, corpus file, commit, push, or merge was changed by this scout.

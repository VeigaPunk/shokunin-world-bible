# Round 36 pair scout — controlled source-only date near-miss

## Proposed controlled substitution

Use `r35-bell7-conflict/` as the positive control and make a separate near-miss copy. Preserve all five JSON files byte-for-byte (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`). Change only the date phrase in Sella's excerpt line 1 from “the seventh day of Embermonth, year 12” to “the eighth day of Embermonth, year 12”; leave the Bell-7 wording and the rest of the excerpt untouched. Keep Tarin's excerpt and maps untouched as fixture artifacts, but the near-miss's comparison map must accurately flag that its inherited r35 text now disagrees with Sella's altered source.

Evidence for this single substitution: `.shokunin/lore/LOG.md:575` specifies exactly this source-only change, five unchanged JSON tables, and the expected limitation. Positive-control Tarin date is `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/tarin-note-excerpt.md:1`; positive-control Sella date and Bell-7 definition are `.../sella-bell7-note-excerpt.md:1`. Sella's excerpt limitation is `.../sella-bell7-note-excerpt.md:3`. The earlier ambiguity matters: `.shokunin/lore/reports/r35-reviewer.md` describes why two “day of this note” descriptions did not independently identify a common date; the remediation reviewer accepted explicit matching dates (`r35-remediation-reviewer.md`, “Shared occasion and report conflict”).

## Interpretation / calibration signal

The substitution leaves Tarin's claim on the seventh and Sella's own dated account on the eighth. Thus the text no longer supports that their Bell-7 references name one occasion; identical Bell-7 label and editorial tick 3 cannot bridge dates. Do not infer that Sella was at Harbor on the seventh, that either account is false, or that a conflict is impossible for reasons beyond this mismatched occasion. JSON `timeline.json` and ledger `contradictions.json` retain the r35 same-occasion descriptions/rationale and will therefore be stale relative to the altered excerpt. That mismatch is deliberate evidence for the source-support probe, not an invitation to silently fix the structured rows. The checker can still establish structural/citation cleanliness but does not parse prose: `.shokunin/lore/LOG.md:574-575`; also `reports/r35-axis-adjudicator.md` (“checker validates structural references, not those assumptions or semantic incompatibility”). A clean exit must not be described as semantic pass or canon.

## Risks and controls

- **Accidental multi-variable edit:** replacing every “seventh” or altering maps/JSON would invalidate the controlled substitution. Limit the changed bytes to the one date phrase in Sella line 1; verify a byte diff shows only that excerpt changed.
- **Overclaiming contradiction/falsity:** the near-miss only withdraws same-occasion support; it does not establish a seventh-day Sella location or resolve either testimony. Preserve attribution and uncertainty.
- **Stale-map confusion:** keep the positive-control map as-is only if clearly identified as inherited; in the near-miss comparison map explicitly state its r35 JSON/map asserts the seventh while Sella excerpt says eighth. Do not imply map text independently repairs the source.
- **False confidence from checker:** run the checker on both controls if desired, record structural output separately from human source-entailment review. Five JSON files should hash identically across positive and near-miss.
- **Scope drift:** this is calibration only; no checker enhancement, fixture/checker/LOG/README changes, commit, or canon adjudication belongs to this scout task.

## Falsifiable check

For a later executor/reviewer: compare the r35 positive and near-miss trees. Expected: hashes of all five JSON files match exactly; the sole differing fixture file is `sella-bell7-note-excerpt.md`, with exactly the stated date substitution. The checker should remain structurally clean if the five tables are preserved. Independently, a blinded reviewer given the two excerpts should accept the shared-date/same-occasion premise for the r35 positive and decline it for the near-miss, citing seventh versus eighth; if the reviewer still finds same-occasion support in the near-miss, or any JSON bytes differ, the calibration claim fails. Checker success alone neither passes nor falsifies that semantic criterion.

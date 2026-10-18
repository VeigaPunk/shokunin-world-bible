# Round 75 fixture scout — exact relation duplicate controls

## Scope and recommendation

Scout-only. No fixture or checker file was changed. I used temporary copies under `/tmp/r75-scout-yyoy10fb/` of `corpus/fixtures/consistent`; the only modified input in each copy was `relations.json`. The three baseline CLI runs all exit **0** with `CLEAN: schema, citations, relations, timeline; 0 violations`.

**GO** for this small matched baseline probe: the cases isolate exact repeated directed rows from same-edge/different-source and reverse-edge controls. **NO-GO** for treating the probe as evidence that a repeated row is false, unsupported, harmful, or a checker violation under current policy. Whether repeated assertions are unwanted input duplication or intentional separate mentions remains unresolved; an eventual policy needs explicit scope and review.

## Checker and fixture evidence

`corpus/fixtures/check_bible.py` defines relation rows by exactly `from`, `to`, `type`, and `source_id` (`FIELDS`). Its relation pass checks endpoint membership/ambiguity and source-ID status. It does not compare relation rows for repetition. The later reciprocal pass is limited to `allied_with` faction relations and should not be confused with a general duplicate rule. The `consistent` fixture supplies existing valid IDs `mira`, `seal`, `courier-log`, and `archive-ledger`; its original `mira -> seal / carries / courier-log` is a useful unchanged semantic baseline, though the temporary probe replaces that relation array.

The baseline stdout/exit results for all proposed controls:

| Temporary case | `relations.json` | Expected baseline |
|---|---|---|
| `duplicate_exact` | Two identical rows: `mira -> seal`, `carries`, `courier-log` | Exit 0 / CLEAN; no duplicate-row finding |
| `same_edge_different_source` | Same `from`, `to`, and `type`, with one row citing `courier-log`, the other `archive-ledger` | Exit 0 / CLEAN; source IDs both resolve uniquely, and no row-level repetition check exists |
| `reverse_edge` | `mira -> seal / carries / courier-log` plus `seal -> mira / carries / courier-log` | Exit 0 / CLEAN; `carries` is not subject to reciprocity checks |

These outcomes are structural checker behavior only. The reverse-edge control deliberately demonstrates that direction is part of the tuple; it does not declare `carries` symmetric in the story. Likewise, same endpoints/type with a different source is not an exact full-record duplicate. It tests that any eventual full-tuple rule would leave distinct source pointers alone, not that the second source independently supports the claim.

## Predecessor guidance

- `reports/r2-rule-scout.md` explicitly distinguishes duplicate same-direction alliance rows from reverse edges and warns not to make all relation types reciprocal. The round-2 rule is a narrow `allied_with` convention, not a general duplicate policy.
- `reports/r7-fixture-scout.md` models ambiguous source IDs as retained rows and emphasizes that ID uniqueness is not source-text support. This matters for interpreting `source_id` as a pointer, not validation of the cited record's content.
- `reports/r45-fixture-scout.md` and checker scout establish the general boundary: a baseline structural finding can demonstrate code behavior, but does not establish a domain convention or justify a calibration change without independent evidence. (R45 is a cautionary precedent, not a relation-duplicate precedent.)
- The r75 claim in `LOG.md` records the 132-fixture inventory as having no exact repeated `(from,to,type,source_id)` tuples and leaves harmfulness versus legitimate multiple mentions open. This scout did not rerun the full inventory; the temporary probes are not additions to that corpus.

## Boundaries and limitations

An exact repeated tuple is a repeated **input record**, and a later-row index could make a future structural diagnostic actionable. It does not show that the assertion is untrue or that one occurrence should be deleted. A source ID is only a reference to an in-world source row: checker cleanliness/uniqueness does not establish source authenticity, source truth, textual support, independence, canon, or rights. Even two different IDs need not mean independent or corroborating sources. Conversely, one identical row could encode repeated mentions, but this schema has no mention/quotation/provenance key by which to establish that interpretation. The controls cannot settle that modeling question.

No source-text, real-world rights, game mechanics, or canon inference follows. No output should characterize duplicate structure as a unique fictional relationship or as proof that another report is absent. Baseline fixture runs are not implementation approval or admission evidence.

# Round 42 regression scout — calibration candidate

## Recommendation: no-go

Do not build the proposed r35 clean/negative pair or claim a calibration gain for changing `claim_a.field` from `place_id` to `description`. The candidate is a valid regression probe for an already-exercised malformed-selector path, but its proposed “structural selector versus human reading of prose” lesson is not materially new: the r3 reviewer explicitly says evidence supports structural pointers/citations, not semantic truth/entailment and that nonempty `why` is not semantically validated (`.shokunin/lore/reports/r3-reviewer.md:19-21`). That is the same boundary the candidate's decision table would restate. The r3 reviewer also records a temporary unsupported-field probe and its diagnostic/no-crash outcome (`.shokunin/lore/reports/r3-reviewer.md:15`); LOG confirms it as prior executed coverage, not a new branch (`.shokunin/lore/LOG.md:700-701`).

The proposed distinction itself is sound but largely documented already. README limits ledger fields to `place_id`, `tick`, `depends_on`, and says ledger does not copy source text/paraphrase; validation checks pointers/required text, not truth or whether `why` explains a semantic contradiction (`.shokunin/lore/corpus/fixtures/README.md:48-54`). Checker independently makes the same schema distinction: event rows include free-form `description`, while ledger selectors are exactly the three allowed fields (`.shokunin/lore/corpus/fixtures/check_bible.py:8-13,76`). A `description` rejection therefore tests known schema enforcement, not a demonstrably new calibration behavior. Calling it a new distinction risks overstating what r3 and README already teach.

## Regression/replay obligation if reconsidered

Pinned baseline is r41 work `f1c776abe1255d08b92fad1457ef298908f89bc2`, report `ba50a55169359c217710a09ed22510023c5be484`; LOG records 94 fixture directories and 469 JSON paths (`.shokunin/lore/LOG.md:699-701`). Any future experiment must prove all 94 prior CLI tuples (stdout, stderr, exit status) and all 469 prior JSON path bytes unchanged against that exact baseline; also record complete control/negative checker output. A pair should change only the selector value, with control clean and negative reporting the unsupported selector before any dereference. This is a falsifiable regression check, not grounds by itself to admit calibration.

## Risks and limits

- Do not infer checker validation of event `description`, `why`, source support, semantic contradiction, or canon. The checker only gates ledger selector names; prose remains human-readable input, not proof.
- Do not treat a failed unsupported selector as evidence its text is false or unusable to a human.
- Avoid spending a round on an exact replay of r3's temporary probe unless a genuinely distinct calibration failure is identified and falsifiable beyond restating existing README/reviewer limits.

## Falsifiable gate for any revised proposal

Before fixture work, name the exact calibration error the new artifact would prevent that r3 reviewer and README do not already prevent. A non-author reviewer must be able to distinguish that lesson from r3's explicit structural-pointer/non-semantic-evidence boundary without relying on the fact that a new fixture or map exists. If the explanation reduces to “unsupported `description` is rejected; pointers are not semantic proof,” reject as repeat coverage/documentation. Do not infer canon in either outcome.

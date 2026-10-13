# Round 78 critic — falsification of copied ledger-side source citation

## Verdict

**NO-GO on material calibration; do not implement or admit a checker rule on this record.** The candidate field is optional extension data that the active checker does not consume. The public fixture contract explicitly says contradiction sides are `{event_id, field}` pointers and that the event's own source is the citation. No evidence shows that a reader treats an ignored extra `source_id` as authoritative, or that rejecting it repairs an independent review decision. The narrow counterexample shows permissive parsing, not material reader confusion.

## Evidence inspected and reproduced

- Active `corpus/fixtures/README.md`, “Round 3: explicit contradiction records,” specifies each side as `{ "event_id": "...", "field": "..." }`, says the event's own source is the citation, and says the ledger does not copy a source, text, or paraphrase that could disagree. It also limits checking to pointers/required text, not citation truth or semantic contradiction. The Round 78 proposal therefore targets an extra member outside the documented side form, not a promised side citation.
- `check_bible.py` validates each contradiction's required top-level fields, then reads only `claim_a`/`claim_b`'s `event_id` and `field`. It neither reads nor rejects extra side members. Generic row validation checks required fields; it does not enforce an allowlist. The event pointer is resolved and its actual `source_id` status is checked. README explicitly keeps that actual event citation as the source of record.
- I made four temporary copies of `r35-bell7-conflict` outside the repository: unchanged control; matching extra side `source_id` values; extra values that conflict with the target events' actual source IDs; and absent side `source_id` members. Under the active checker, all four returned exit 0 and exactly `CLEAN: schema, citations, relations, timeline; 0 violations`. The test confirms the extra member is inert for checker behavior, not that a reader mistakes it for a citation. No repository input or checker was changed.
- Precedent reinforces this boundary: `reports/r63-critic.md` and `reports/r63-axis-adjudicator.md` found ignored extra fields can carry accepted values without changing any checked result, and rejected a material-calibration claim without a consumed-result risk, producer contract, or consequential review effect. That analogy does not decide this round, but the current evidence has the same gap: accepted extension data is not itself a harmful inference.

## Falsification of the materiality claim

The strongest pro-change case is that a contradictory copied citation *could* confuse a reviewer. That remains hypothetical. The README tells readers the field is not part of the side schema and identifies the event's citation as authoritative; the checker and existing reports do not signal that extra metadata is validated. There is no observed reader, downstream consumer, or review example relying on the ignored member. No independent repair is demonstrated: a reviewer can follow the event pointer to its actual source, and the proposal offers only rejecting an optional field, not correcting that pointer or adding a diagnostic tied to an established interpretation.

The matched probe also fails to show a meaningful outcome contrast: missing, equal, and conflicting copies are all structurally indistinguishable to the checker by design. A rule rejecting only a conflicting copy would create a new constraint on otherwise tolerated extension fields without evidence that this field has a supported meaning or users rely on such rejection. If the goal is to revise the documented side schema, that needs a concrete reader-facing ambiguity and explicit schema decision, not inference from an ignored key.

## Axis judgment and limits

- **Calibration: unchanged; no material improvement demonstrated.** A hypothetical ambiguity is not measured confusion or a demonstrated repair benefit.
- **Depth: unchanged.** No source text, claim, setting, or lore decision is added or clarified.
- **Coverage: unchanged for the active checker.** The temporary probes only confirm existing behavior; no justified new validation boundary is established.
- **Harm: no candidate was tested.** I do not claim a regression occurred. Rejection could constrain extension metadata or create noisy failures, but that cost is prospective, not measured.

This is a narrow checker/documentation calibration assessment only. It makes no claim about source-text authenticity/support, fictional truth, canon, chronology, rights, or mechanics. The probe did not test a modified checker or real reader behavior, and cannot establish compatibility across external producers. Recommendation: leave checker, fixtures, README, and LOG unchanged; seek a concrete reader-confusion case and evidence of a distinct repair before reopening.

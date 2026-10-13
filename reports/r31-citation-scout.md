# Round 31 citation scout — in-world citation versus real rights and training

## Scope

Read-only interpretation of round 31's proposed generic relation-source ambiguity probe, with the prior r7 ambiguous-citation fixture as context. No fixture, checker, log, README, or other file was changed. The proposed coverage axis is narrow: a non-alliance `relations[].source_id` with duplicate in-world source IDs should expose its ambiguity; it is not a new checker rule or a finding about canon.

## Evidence

- The existing r7 fixture `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:1-14` has two `allied_with` rows: the first cites unique `separate-compact` (`:2-7`), the reverse row cites duplicated `harbor-compact` (`:8-13`). Its `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/sources.json:1-19` contains two rows with ID `harbor-compact` (`:2-7`, `:15-19`). Thus r7 already has an ambiguous citation on a relation, but specifically the reverse alliance edge; it is not evidence of a controlled non-alliance relation probe.
- Checker `.shokunin/lore/corpus/fixtures/check_bible.py:45-53` indexes sources and emits duplicate-ID errors; `:54-74` counts IDs and `source()` emits `ambiguous in-world source` when the count exceeds one. Relation rows call `source()` at `:123-130`. These lines indicate that an ambiguous relation citation is diagnosed as input ambiguity, independently of relation type. The r7 report `.shokunin/lore/reports/r7-alliance-scout.md` also observed the reverse-edge duplicate and expressly bounds it to alliance reciprocity; `.shokunin/lore/reports/r7-source-scout.md` describes ordinary relation citations separately from support checks.
- Round 31's LOG declaration `.shokunin/lore/LOG.md` identifies the proposed control as `consistent/`'s `relations[0]` (`mira -> seal / carries`) with `courier-log`, unchanged in both variants, and the treatment as one additional source row reusing that ID. This would test generic relation citation diagnostics on a non-alliance relation, not discover source-text semantics.

## Rights/training distinction and risks

“In-world source” here means a fictional record named inside fixture data. An ID's uniqueness or ambiguity says nothing about whether any real document exists, who owns it, whether its text is licensed, or whether it may be used for model training. Likewise, the checker diagnostics establish structural/reference status only; they do not establish that `courier-log` supports the `carries` proposition, that Mira carried the seal in canon, or that any source is true or authoritative.

Risk: readers may conflate “citation” with an external bibliographic citation or rights clearance, or read an ambiguity diagnostic as invalidating the relation itself. Keep the report and any eventual fixture prose explicit that duplicate IDs make the in-world reference unresolved; they do not prove falsehood, support, provenance authenticity, legal permission, or training consent. The test must not add a new checker rule or claim that this round establishes canon.

## Suggested test / coverage boundary

Use the declared controlled pair only: same `relations[0]` and all other tables held constant; control has a single `courier-log` source, treatment adds a second structurally valid row with that ID. Replay the fixture checker on each. Expect the control clean; in treatment, expect `relations[0].source_id: ambiguous in-world source 'courier-log'` alongside the duplicate-source finding and inventory any other legitimate diagnostics rather than attributing the whole output delta to the relation. This tests that an existing generic relation citation path surfaces duplicate-ID ambiguity. It does not test or warrant a new rule, support verification, rights/training review, or canon conclusion.

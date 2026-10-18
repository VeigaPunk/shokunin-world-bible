# Round 29 simplifier — minimal fixture-only negative control

## Recommendation

Keep the move to a single negative excerpt and one short manual map. Do not add a checker rule: the checker does not read Markdown, and a structurally clean result cannot certify prose support. Compare only the selected `relations[0]` `carries` assertion against the clause. “Unsupported by this clause” means it is not entailed here; it does **not** mean false, contradicted, or false in canon.

## Evidence (path:line)

- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:3` says “I, Mira, carried the blue seal.” The positive map identifies “carried” as the lexical action (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:3,9`).
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:7` makes speaker/name-to-ID alignment editorial, not text-entitled. Its lines 13–17 limit coverage to `relations[0]`, exclude other JSON claims/events, state that Markdown is not read by the checker, and say the proximity near-miss does not entail carrying.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relations.json:2-7` is the unchanged structured `mira -> seal`, `carries`, `courier-log` row; this is the assertion under review, not proof of prose support.
- `.shokunin/lore/reports/r29-scribe.md:3-6` specifies the paired decision: positive lexical support conditional on editorial alignment; “The blue seal was near Mira” is unsupported, not contradicted/false; checker cleanliness remains structural only.
- `.shokunin/lore/reports/r29-critic.md:3-12` explains why omission cannot establish falsity, repeats the ID-alignment and checker boundaries, and makes explicit that no committed r29 fixture or reviewer artifact was available to inspect. Thus the proposed test is not evidence of a completed replay or independent review.

## Risk

The main risk is converting a one-clause entailment judgment into a closed-world verdict: lack of carrying language in the near-miss does not show that carrying never occurred or that another source does not support the relation. A second risk is treating “Mira” and “the blue seal” as textual proof of IDs; the alignment remains an editorial stipulation. Do not imply that the draft table, itself, proves fixture creation, byte identity, clean exits, replay, or non-author acceptance.

## Falsifiable test

Create the matched negative fixture by retaining the r28 fixture’s five JSON tables and source IDs byte-for-byte, replacing only the excerpt sentence with “The blue seal was near Mira,” and mapping that clause as **unsupported by this excerpt**, not false/contradicted. Run the checker on both fixtures: both should exit 0, which establishes only structural acceptance. A named non-author reviewer must quote both clauses, accept the positive `carries` reading only conditional on editorial ID alignment, and reject proximity as support while refusing a canon-falsity inference. Compare the five JSON files byte-for-byte. The claim fails if proximity is accepted as carrying, unsupportedness is reported as falsity, any JSON/source ID differs, or the claimed replay/review lacks evidence. This is a test specification; current report evidence does not establish that it has passed.

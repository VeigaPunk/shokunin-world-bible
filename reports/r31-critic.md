# Round 31 critic — novelty and citation calibration

## Challenge to novelty

The broad capability is not new: Round 7 already exercised an ambiguous source ID on a relation, specifically `relations[1]` in `r7-ally-reverse-ambiguous/relations.json:9-12`, citing duplicated `harbor-compact` (`sources.json:2-6,15-19`). That is a reverse `allied_with` edge, and the old critic reports no relation-local ambiguity diagnostic for that fixture; it is therefore prior evidence of the input condition, not evidence that the current checker covers or reports it correctly (`reports/r7-critic.md`, “Replayed…” and “What the evidence…” paragraphs). Round 31 can only claim a narrower new probe: the generic source-resolution diagnostic on a non-alliance `carries` relation. Avoid saying this is the first ambiguous relation citation or first relation source ambiguity.

## Calibration and inference risks

The proposed controlled pair is useful because it holds the `mira -> seal / carries / courier-log` relation constant (`corpus/fixtures/consistent/relations.json:2-7`) and varies source-ID multiplicity. But duplicate-ID ambiguity is structural resolution status, not evidence the relation is false, unsupported by source text, or canonically unsettled. `sources.json` here contains in-world metadata (e.g. `consistent/sources.json:9-13`), not source prose. The diagnostic's wording `ambiguous in-world source` should be reported verbatim, not paraphrased as “ambiguous citation truth.”

The LOG prediction that the control exits 0 deserves scrutiny: a duplicate `courier-log` source may already be referenced by other claims/events, and generic `source()` is called at multiple locations (`corpus/fixtures/check_bible.py:68-74`, `113-116`, `130`, `242`). The duplicate can produce a fan-out of legitimate findings. Inventory every output delta, including non-relation references; do not promise a single relation-only violation. The source counting/status logic is at `check_bible.py:53-74`; relation rows call it at `:130`. A clean control is only expected if copied fixture is otherwise clean and the duplicate is the sole mutation.

## Falsification / test

1. Compare both fixture directories bytewise: five common JSON tables except the intended `sources.json` multiplicity difference must match; verify `relations[0]` is byte-identical and still cites `courier-log`.
2. Run the documented checker (`python3`) on both. Require clean unique control, and in duplicate case require the exact `relations[0].source_id: ambiguous in-world source 'courier-log'` diagnostic. Capture and enumerate every additional diagnostic from references to that ID; reject claims that output is relation-only unless replay proves it.
3. Re-run the old `r7-ally-reverse-ambiguous` fixture. It must be described as prior ambiguous relation-citation precedent, not as the same generic carries probe. Compare observed output with its report and current checker; if it now reports relation-local ambiguity, update novelty framing rather than hiding that evidence.
4. Preserve exact prior-fixture stdout/stderr/exit and JSON-byte baseline as declared; this guards regression only, not semantic truth.

A passing test supports coverage of one generic non-alliance relation citation under duplicate source-ID input. It does not establish source-text support, citation rights, relation falsity, or canon.

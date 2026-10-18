# Round 75 simplifier — exact duplicate relation rows

## Verdict: NO-GO on checker change

Do not add a duplicate-relation violation or guard on the present schema/evidence. The narrowest observable key is exact equality of all four required relation strings `(from, to, type, source_id)` within one `relations.json` array. But the checker and schema provide no basis to decide that a repeated row is invalid, rather than an intended repeated mention that this representation cannot distinguish. A matched control can prove the detector is scoped; it cannot resolve that policy question.

## Evidence

- The r75 declaration in `.shokunin/lore/LOG.md` states that all 132 shipped fixture directories contain no exact repeated tuple; `consistent/relations.json` has one `mira -> seal / carries / courier-log` relation. That inventory establishes no observed existing repeat, not that repeats are forbidden.
- `.shokunin/lore/corpus/fixtures/check_bible.py`: `FIELDS['relations']` requires `from`, `to`, `type`, and `source_id`, all nonempty strings. The relation loop validates endpoint membership/ambiguity and source-ID resolution. There is no relation identity or multiplicity rule. It does not read source text.
- `.shokunin/lore/corpus/fixtures/README.md` describes `source_id` as an in-world record reference and repeatedly limits clean checks to structure/reference validity, not source-text support or canon. It declares the r2 `allied_with` reverse-edge requirement a chosen convention, not universal symmetry; that different rule does not decide same-direction duplicate semantics.
- `.shokunin/lore/reports/r2-simplifier.md` scopes reciprocity to an explicit `allied_with` convention and leaves other relation types untouched. `r7-simplifier.md` / `r7-axis-adjudicator.md` treat citation uniqueness as identifier qualification only, not evidence that the source supports the relation. These do not authorize deduplicating relation rows.
- `.shokunin/lore/reports/r4-critic.md` and reviewer warn that exact-name equality can conflate distinct homonyms. This is not directly the same schema case, but cautions against elevating surface equality into semantic identity. `.shokunin/lore/reports/r45-simplifier.md` likewise declines a mechanically small guard where the necessary domain convention is ungrounded. The relevant current r75 schema scout, `.shokunin/lore/reports/r75-schema-scout.md`, finds the same representational gap: no row ID, passage locator, claim text, time/scope, or multiplicity rationale.

## Policy boundary and limits

An exact four-field repeat is detectable as repeated **input structure**. The data cannot represent two independently addressable attestations with identical tuples; but that limitation does not prove that repeated mentions or independent underlying claims are impossible. A different `source_id` and a reversed edge are structurally distinguishable, but neither establishes independent source truth or semantic correctness. Do not normalize strings, merge/remove rows, treat reverse edges or different predicates as duplicates, or infer one uniquely true/canonical relationship.

This decision concerns structural duplication only. It says nothing about source truth/authenticity, canon, rights or permissions, or game mechanics. No source prose, production consumer behavior, or real-world rights evidence was inspected. No implementation or candidate probe was performed by this report; the 132-fixture count is the declaration's inventory, not an independent replay. The schema scout also did not run candidate probes.

## Reconsideration gate

Revisit only after an explicit project-level convention says whether exact repeated relation records are invalid regardless of underlying mentions, or after the schema gives distinct claims/evidence locations stable identity and a clear duplicate key. Then test exact-repeat, changed-source, reverse-direction, and changed-type controls, retain every input row, and label any result strictly as an input-structure finding. Until then, **NO-GO**; no checker/corpus edit or axis-gain claim is warranted.

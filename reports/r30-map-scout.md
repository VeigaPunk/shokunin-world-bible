# Round 30 map-scout — explicit textual conflict, not canon judgment

## Bounded classification

The r30 sentence “I, Mira, did not carry the blue seal” explicitly negates the carrying proposition stated positively in the unchanged selected record. At most, this is a **textual conflict between this constructed excerpt and `relations[0].type=carries`**, conditional on the fixture’s editorial identity alignment. It does not establish that the record is false, that the excerpt is authoritative, or which account should prevail. Keep the assertion and report the conflict; do not resolve it as canon. Distinguish this from r29: proximity is merely unsupported for carrying, not a denial.

## Evidence (path:line)

- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:3` states “I, Mira, carried the blue seal.”
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:9` makes Mira/seal-to-ID correspondence an editorial stipulation, not lexical entailment or external verification; line 13 maps the positive verb only to `relations[0]`.
- `.shokunin/lore/corpus/fixtures/r29-near-miss/courier-log-excerpt.md:3` states “The blue seal was near Mira.” This supports neither carrying nor its negation; the round-29 declaration in `.shokunin/lore/LOG.md` distinguishes it as unsupported, not false.
- `.shokunin/lore/corpus/fixtures/r29-near-miss/relations.json:2-6` retains `mira` → `seal`, `carries`, `courier-log`, so the prose contrast is against the unchanged row rather than a changed structured proposition.
- `.shokunin/lore/corpus/fixtures/r30-explicit-negation/relations.json:2-6` (if created as declared) must retain that same selected row; `.shokunin/lore/corpus/fixtures/r30-explicit-negation/courier-log-excerpt.md:3` (if created) is the explicit negative clause. These are proposed target paths, not existing evidence.
- `.shokunin/lore/corpus/fixtures/r29-near-miss/contradictions.json:1` is empty; a textual conflict classification should not be confused with a checker-generated or canon-resolved contradiction ledger entry.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:17` states the checker does not read Markdown; clean structural acceptance cannot establish clause meaning.

## Risk

Calling the explicit denial merely “unsupported” erases the meaningful difference from proximity; calling it “false” or canon-resolving promotes one constructed sentence over the structured assertion without authority. Identity is editorially aligned, and temporal scope, speaker reliability, source authority, truth, and canon are not established here. Also avoid treating an empty contradiction ledger or checker pass as a semantic verdict.

## Falsifiable check

A non-author reviewer can falsify this bounded map by showing that the exact r30 clause does not explicitly deny the same carrying proposition, that the r30 relation row differs from r28/r29, or that the map labels canon truth rather than excerpt-to-row textual conflict. The reviewer should classify the trio distinctly: r28 “carried” = positive lexical support conditional on editorial IDs; r29 “near” = unsupported (not negated); r30 “did not carry” = explicit textual conflict only. Compare the five JSON tables byte-for-byte to confirm the selected assertion is held fixed and run each fixture checker only as a structural check. A successful textual distinction does not settle truth/canon; no checker output can do so.

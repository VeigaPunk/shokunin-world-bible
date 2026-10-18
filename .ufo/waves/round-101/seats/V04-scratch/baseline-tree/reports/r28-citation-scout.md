# Round 28 citation scout — in-world citation vs rights ledger

## Evidence and distinction

- `.shokunin/lore/corpus/knowledge/reference-ledger.md:1-7` explicitly labels its entries real-world method references and separates rights/reuse questions from AI-training permission; the table makes no rights grant or permission inference. These citations document inspiration, not fictional story evidence.
- `.shokunin/lore/corpus/knowledge/reference-ledger.md:9-11` says the references attribute method inspiration, while fictional facts are separately cited to fixture `sources.json`; no reference work is ingested as canon.
- `.shokunin/lore/corpus/fixtures/README.md:36-41` defines `source_id` and `first_appearance` as references to in-world fictional records, and limits fixture claims to invented entries.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json:9-13` supplies `courier-log` as a fictional personal log, with an explicit first-person reliability limit. `.shokunin/lore/corpus/fixtures/consistent/relations.json:2-7` attaches that ID to `mira -> seal / carries`.
- `.shokunin/lore/corpus/fixtures/README.md:214-216` and `:116-119` distinguish structural/citation-ID validation from source-text support, transfer truth, corroboration, or canon. Round 23 likewise says its clause map is not read by checker (`.shokunin/lore/corpus/fixtures/README.md:496-512`).

Thus `source_id` is an in-world pointer, not a rights/permission record and not evidence by itself that source wording supports a relation. The real-world reference ledger has the inverse scope: rights/method attribution, not an in-world story citation. Do not merge either ledger or infer that public availability grants reuse or training permission. Round 28's constructed excerpt and clause map can support a manual internal correspondence check only; it cannot authenticate an actual historical text or establish story truth beyond the constructed excerpt.

## Risks

1. Conflating a resolvable ID with textual entailment: clean structural output can be mistaken for verified support.
2. Conflating method-source citation with story evidence, or treating rights/AI-training questions as answered by the existence of a citation.
3. Overreading a short constructed clause (e.g. carrying) as ownership, a transfer chain, chronology, motive, or canon beyond its words.
4. Treating a manual clause map as checker-enforced evidence or as proof that a source is true; existing docs explicitly limit the checker and clause map.

## Proposed falsifiable check

For the new separate fixture only, have a reviewer who did not author it trace every mapped field for the single `mira -> seal` `carries` relation to an exact quoted clause in the newly constructed fictional excerpt. Pass only if the excerpt literally entails the mapped subject, object and carrying assertion, every mapped fact has a clause citation, and the reviewer marks unsupported additions (including rights, ownership, duration, chronology and truth) out of scope. Fail if any mapped fact lacks a clause or the map asserts more than the excerpt. Separately run the existing checker and compare its structural result; do not represent that run as prose verification. This tests human traceability of the constructed excerpt, not source-text truth, canon, or any rights/permission status.

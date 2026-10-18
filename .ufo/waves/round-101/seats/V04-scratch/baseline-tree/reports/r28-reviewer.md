# Round 28 reviewer report

## Scope and trace

Reviewed the newly authored `r28-courier-excerpt/courier-log-excerpt.md` and `relation-clause-map.md`, and the fixture JSON. The excerpt is explicitly labeled newly authored fiction; its complete sentence is: “I, Mira, carried the blue seal.” The map addresses only `relations[0]`, whose record is `from=mira`, `type=carries`, `to=seal`, `source_id=courier-log`.

Clause-level trace:

- “I, Mira” presents the first-person speaker and names that speaker Mira. It does not by itself prove which database identity that name denotes. The map correctly calls the alignment from the text's “Mira” to ID `mira` an editorial, fixture-local source-to-ID match, not a lexical entailment.
- “carried” explicitly supplies the carrying action and is the lexical basis for `type=carries`. The map does not treat the checker or source citation as proof that the action occurred.
- “the blue seal” supplies the grammatical object. The map appropriately separates its editorial alignment to ID `seal` from what the words alone establish.
- Given those declared editorial alignments, the clause supports the narrow actor/action/object mapping `mira -> seal / carries` for this constructed fixture. The map does not assert other relation rows.

## Negative control and limits

The near-miss “the seal was near Mira” expresses proximity, not an action by Mira of carrying the seal. It does not support `type=carries` or the directed carrying relation; the map correctly rejects it.

No location, time, route, destination, duration, ownership, provenance, continued possession, motive, or outcome is entailed by the excerpt. Nor does it establish the uniqueness of the named people/items, external source authenticity, or canon. The other fixture JSON claims remain outside this excerpt's support: the harbor/registry and tower/watch-bell entity claims, Mira's timeline departure and arrival and their places/ticks/order, and the seal-accompanied-Mira claim are not mapped or validated by this clause. `courier-log` linkage/first-appearance and source metadata are record relationships, not textual evidence supplied by the excerpt. Empty contradictions add no claim.

The map explicitly says the checker reads neither Markdown file. Thus a structural clean result cannot validate the manual entailment or editorial ID alignment. No canon promotion is warranted. I did not read checker Markdown or treat it as evidence. No edits beyond this report.

## Finding

The requested narrow clause-to-`relations[0]` mapping is traceable and appropriately separates lexical carries from editorial source-to-ID matching; the negative near-miss is correctly rejected. Unsupported fixture claims are explicitly kept out of scope, with no identified overreach in the map.

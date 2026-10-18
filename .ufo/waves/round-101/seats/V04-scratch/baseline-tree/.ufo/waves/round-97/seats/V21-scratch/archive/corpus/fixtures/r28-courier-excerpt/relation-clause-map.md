# Relation clause map

## Literal clause

“I, Mira, carried the blue seal.” The words state a first-person speaker identified in the text as Mira, an action of carrying, and the blue seal as its object.

## Editorial source-to-ID alignment (not lexical entailment)

For this fixture only, the authored speaker label “Mira” is editorially aligned to `entities` ID `mira`, and “the blue seal” to ID `seal`; these text-to-record identity matches are editorial stipulations, not conclusions entailed by the words alone or external verification.

## Lexical relation mapping

The verb “carried” is the literal lexical basis for encoding the selected relation as `type=carries`; the subject and object, after the editorial alignments above, map to `relations[0].from=mira` and `relations[0].to=seal`. This manual map covers only `relations[0]`.

## Limits

The checker does not read either Markdown file. All other existing JSON claims and events are unsupported by this excerpt and are not mapped here. The excerpt/map establish no ownership, duration, destination, provenance, or canon. The near-miss “the seal was near Mira” would not entail carrying and would not support `carries`.

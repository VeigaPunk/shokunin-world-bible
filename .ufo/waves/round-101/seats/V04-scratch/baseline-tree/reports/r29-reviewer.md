# Round 29 reviewer report

## Scope and paired trace

Compared the r28 positive excerpt/map with the r29 near-miss excerpt/map and the unchanged selected relation and source records. The r28 clause says “I, Mira, carried the blue seal.” The verb “carried” is direct lexical support for the narrow `type=carries` mapping. Conditional on the map’s explicitly editorial, fixture-local alignments of “Mira” to `mira` and “the blue seal” to `seal`, it supports `relations[0]` (`mira` → `seal`, `carries`). Those identity alignments are not proved by the words themselves.

The r29 excerpt instead says “The blue seal was near Mira.” This asserts proximity, not a carrying action. Its map correctly labels only `relations[0].type=carries` **unsupported by this excerpt**, not contradicted or false: the sentence neither says Mira carried it nor says she did not. The same editorial ID alignment remains a stipulation, not external verification.

The selected relation row (`from=mira`, `to=seal`, `type=carries`, `source_id=courier-log`) and `courier-log` source row are unchanged. The source citation/reference remains a record link; it does not make this near-miss sentence support carrying, nor establish truth of the relation. No map overclaim identified: the negative map limits its assessment to the selected type claim, calls the rest unassessed, and makes no canon/source-truth assertion.

## Checker boundary

Both fixture checker runs are clean (exit 0), but this says only that the JSON passes the checker’s structural rules. The checker ignores Markdown; clean output says nothing about whether either prose clause supports the relation. That judgment above is manual. This pair establishes no canon, source authenticity, or broader JSON support.

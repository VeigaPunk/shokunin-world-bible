# Round 42 selector scout — field gate and semantic limits

## Gate/order trace

- The README defines ledger sides as `{ "event_id": "...", "field": "..." }`, with allowed fields `place_id`, `tick`, `depends_on` on a uniquely identified timeline event with resolvable source; it explicitly says the checker validates pointers/required text, not citation truth or whether `why` explains a semantic contradiction (`.shokunin/lore/corpus/fixtures/README.md:45-54`).
- Checker sets the allowlist to exactly those three names before iterating ledger rows (`.shokunin/lore/corpus/fixtures/check_bible.py:76-80`). For each side, it first requires an object (`81-83`), then checks nonempty string `event_id` (`84-88`), then validates `field` against allowlist and continues immediately on failure (`89-91`). Thus unsupported field is rejected before event-count lookup/dereference (`92-95`) and before source resolution (`96-100`). A later same-reference check compares only event_id and field (`101-105`).
- Event schema includes free-form `description`, unlike the ledger selector allowlist (`.shokunin/lore/corpus/fixtures/check_bible.py:8-18`; event required fields also README:31-36). The field name being valid on the event does not make it an admissible ledger selector.
- The r3 reviewer already executed a temporary unsupported-field probe and recorded diagnostic/no-crash behavior; it also stated the semantic boundary explicitly: `why` is only checked nonempty and validation does not prove selected fields conflict (`.shokunin/lore/reports/r3-reviewer.md:15,19-22`). Therefore an r42 unsupported-`description` fixture is not new branch coverage, and the structural-pointer-versus-semantic-proof distinction is already documented.

## Calibration assessment / risks

No-go on the proposed `description` negative as a new calibration candidate. It would repeat the r3 unsupported-field test and its stated semantics; changing the unsupported token does not make the gate/order distinction novel. The README already says copied text/paraphrase is omitted and `why` is not semantically validated. A narrowly useful reminder might distinguish an event's human-readable prose from a machine-checkable field pointer, but evidence here does not establish that this warrants a new fixture or axis gain. Do not imply descriptions are unusable to human readers, forbidden on events, or false; do not claim checker proves conflict, source support, or `why` correctness. No canon inference.

## Falsifiable check

A non-author reviewer can falsify this no-go by identifying a documented calibration distinction not already covered by r3 reviewer lines 15/19-22 and README lines 48-54, then showing a one-field, otherwise identical control/negative pair teaches that distinction without merely repeating unsupported-selector rejection. If no such distinct lesson is articulated, reject the candidate; in any event verify no claim treats checker acceptance as semantic entailment or canon truth.

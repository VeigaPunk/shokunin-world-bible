# Round 75 independent reviewer — coverage only

## Decision

**Provisional NO-GO on a material coverage gain; do not admit a checker change on the present evidence.** Exact tuple detection would cover an input pattern the current checker does not inspect, but detection alone does not establish a justified or materially useful validation rule. The declared key `(from, to, type, source_id)` identifies repeated field values, not whether the repeated row is redundant serialization or an intended second mention. There is no explicit uniqueness policy or row/claim identity in the schema to ground that distinction. Rejecting every repeat as invalid risks rejecting a legitimate representation.

This is a coverage-only independent review, not a candidate review. I did not alter or run the checker, fixtures, corpus, or LOG.

## Evidence and interpretation

The active LOG declaration identifies baseline `58edd17eb080fc707e959bf3dfc56d01afa54234`, reports no exact tuple repeats among 132 shipped fixtures, and explicitly leaves harmful input duplication versus legitimate repeated mentions open. The append-only correction says the competing depth declaration was withdrawn and unexecuted; it is incident telemetry, not this round's mission or evidence. I have not treated it as a candidate or inferred any registry-entry idea.

The checker (`corpus/fixtures/check_bible.py`) validates relation row fields, endpoint IDs, and source-ID membership; its relation pass has no general exact-row repetition test. The r75 fixture scout's three temporary matched probes—exact repeat, same edge with a different source ID, and reverse edge—each ran against the baseline checker and exited 0/CLEAN. These are **baseline probes**, not candidate results: they show the baseline accepts all three and demonstrate how a future detector could be scoped, but cannot show that flagging the first is warranted, actionable, or materially useful. The regression scout's 132/132 raw CLI tuple preservation and corpus-byte equality likewise establish a pre-candidate baseline only, not candidate regression safety or coverage gain.

The schema scout finds no relation-row ID, passage/claim locator, occurrence, or multiplicity contract. A same-source repeated tuple could encode redundant input, or multiple mentions that this representation cannot distinguish. Different source IDs and reversed direction are structurally distinguishable, but a source ID is only an in-world reference; it establishes neither independence nor support. A later-row index would localize equality, not resolve its meaning.

The reports are appropriately scoped: checker and fixture scouts establish missing detection and baseline behavior, while schema, prior, critic, and simplifier reports explain why that does not justify a hard-invalidity rule. The scribe's documentation outline is explicitly conditional on a policy and candidate evidence; it is not evidence of either. The regression scout supplies a sound future replay method but no candidate comparison. I found no contradiction that would turn these materials into affirmative admission evidence.

R2 is especially relevant: its rule scout says identical forward alliance rows do not supply a reverse edge, and explicitly leaves generic duplicate-relation policy undeclared. The r2 reciprocal convention is not a uniqueness rule. R2 therefore supports keeping direction and duplicate-row questions separate, not extending its convention to reject repeats. Other duplicate precedents (for example repeated dependency-list members) are specific to structures whose policy was separately declared; they do not fill this gap.

## Provisional axis reasons

| Axis | Provisional finding | Reason |
|---|---|---|
| **Coverage** | **Not materially improved / NO-GO** | A checker could detect a new equality condition, but no established input contract says that condition is invalid or useful to reject. Matched controls establish scope, not policy or materiality. |
| **Depth** | **Unchanged** | This narrow input check would not add source passages, claim identity, or richer lore/source interpretation. No depth claim is in scope. |
| **Calibration** | **At risk; harm not yet measured** | Treating every exact repeat as an error could reject intentional repeated mentions or imply rows are disposable. Explicit, narrowly labeled policy and review could mitigate this, but controls alone cannot. |

A future reconsideration would need an explicit project-level convention that relation rows are unique by this key (including how intended repeated mentions are represented), or a schema that gives claims/occurrences distinct identity and a defensible duplicate key. Only then would a non-repairing, precisely labeled input diagnostic and matched controls merit candidate review. Nothing here implies source truth, canon, rights, or mechanics.

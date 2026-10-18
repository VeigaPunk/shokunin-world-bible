# Round 28 clause scout — narrow source-to-relation map

## Direct observation

The committed `consistent/` fixture contains a relation `mira -> seal` of type `carries`, citing `courier-log` (`.shokunin/lore/corpus/fixtures/consistent/relations.json:1-7`). Its source row labels `courier-log` “Courier Mira’s Route Log, year 12” and calls it a fictional first-person account (`.../consistent/sources.json:7-12`). The entity claim says “Mira carried the blue seal” and cites that same source (`.../consistent/entities.json:1-17`). These are constructed records; no committed excerpt for `courier-log` is present, so they do not let me inspect or verify the source clause.

## Proposed clause (fixture text only)

> I, Mira, carried the blue seal.

This is a proposed newly authored sentence for a new fixture excerpt, not a quotation recovered from an existing source. It minimally states actor, carrying action, and object; avoid adding where, when, destination, motive, acquisition, or outcome.

## Clause-to-record map

| Exact proposed words | Candidate field | Limit |
|---|---|---|
| “I, Mira” | `relations[0].from = mira`; entity `mira` is named Mira | speaker identity as asserted by this constructed excerpt only |
| “carried” | `relations[0].type = carries` | no implied duration, direction, custody before/after, or continuing possession |
| “the blue seal” | `relations[0].to = seal`; entity `seal` is named Blue Seal | no inferred uniqueness, provenance, ownership, or link to any other seal |

## Risks / deliberately excluded

The existing structured claim is not independent source-text evidence. The proposed text must be introduced as newly authored fixture material, not treated as a true/canonical quotation. A relation row’s citation is linkage, not proof that the event occurred. “Carried” is only a lexical match for the schema’s `carries` label; the checker cannot adjudicate entailment. Do not infer location, time, route, destination, why Mira carried it, whether the seal was blue in-world, or any further story fact.

## Falsifiable check

For a separate fixture, add the exact excerpt above and a manual map that identifies only those three directly stated components; have a non-author reviewer trace each mapped component to the exact clause and reject any unmapped asserted fact. The fixture checker should exit 0 structurally. The proposal fails if the excerpt has to rely on existing JSON rather than its own words, if reviewer cannot trace actor/action/object, or if the mapped record claims anything beyond the clause. Preserve all prior fixture stdout/stderr/exit and JSON-path bytes exactly as round 28 declared.

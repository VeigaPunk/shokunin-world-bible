# Round 25 critic — coverage falsification attempt

## Finding

The declaration's proposed fixture evidence is not present in this checkout, so the coverage claim is not presently demonstrated. `LOG.md` says round 25 requires paired `to` duplicate, optional both-endpoint duplicate, and unique control (lines 524–527); however, the current fixture tree has no `r25-*` directories. The checker code at `corpus/fixtures/check_bible.py:123–130` applies one generic loop to both endpoint fields and increments counts from schema-admitted rows (`:119–121`), which makes implementation symmetry plausible but does not independently test `to` behavior.

## Risks / falsification limits

- Existing round-24 observations are `from`-side only: `.shokunin/lore/LOG.md:514–533` describes `r12-ambiguous-actor` duplicating `mira` and specifically naming it from the relation endpoint (`:529–532`). This cannot establish the `to` path.
- The declaration asserts fixture files absent at baseline and requests all 73 prior fixture outputs plus 364 JSON paths unchanged (`.shokunin/lore/LOG.md:524–527`). No executor/reviewer/verifier round-25 reports or artifacts are visible in `.shokunin/lore/reports/`; therefore neither the claimed target diagnostic nor regression boundary can be checked here.
- A paired fixture must isolate endpoint position: same cited relation and all other tables/rows, with only duplicate target entity row added; unique control should retain the same relation target and unique target ID. Otherwise unrelated pre-existing violations could obscure whether the new diagnostic is attributable to `to` ambiguity.
- A both-sides-duplicated fixture, if included, should assert two independent local diagnostics (one per endpoint), not imply two independent canon relationships. Duplicate entity IDs are structural ambiguity only; checker does not choose a row (`check_bible.py:123–130`, `README.md:516–520`).
- Citation-ID validity does not substantiate relation wording: README explicitly limits this to identifier resolution, not source-text support (`README.md:529–533`). Keep claims strictly structural; no source truth or canon conclusion.

## Verdict

Coverage improvement is **unproven** from current evidence. Generic code symmetry is not a substitute for the declared non-author paired replay. No claim about relationship truth, canon, or game mechanics is made.

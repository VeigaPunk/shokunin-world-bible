# Round 28 simplifier — smallest fixture-only artifact

## Evidence and proposed shape

- `.shokunin/lore/LOG.md: Round 28` declares the depth move: a new separate fictional fixture, a short courier-log excerpt, and a manual clause-to-record map for only `mira -> seal`; it explicitly excludes checker prose verification and canon claims.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json:1-13,39-48` supplies the existing cited Mira and seal rows; `.shokunin/lore/corpus/fixtures/consistent/relations.json:1-8` supplies the single `carries` relation citing `courier-log`.
- `.shokunin/lore/corpus/fixtures/README.md:36-41,53-54` distinguishes fictional source-ID linkage from checking source-text support; `.shokunin/lore/corpus/fixtures/README.md:195-216` already models an invented excerpt plus manual correspondence, while warning that comparison does not establish truth.
- `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md:1-20` is a compact precedent for explicit unmapped limitations, but its absence-note proposition is not evidence for carrying a seal.

Use one new directory, e.g. `r28-courier-excerpt/`, copied from `consistent/`, with only two added Markdown artifacts: `courier-log-excerpt.md` and `relation-clause-map.md`. Keep all five JSON tables byte-identical to `consistent/`; this isolates the manual source-to-record interpretation from any schema/input delta. In the newly authored fictional excerpt use one sentence only, narrowly: “I, Mira, carried the blue seal.” The map points that sentence to the existing `relations[0]` (`from=mira`, `type=carries`, `to=seal`, source ID `courier-log`) and records that its words support only the asserted carrier/item relation within this constructed excerpt. Do not add chronology, location, ownership, transfer, motive, or corroboration. State plainly that prose and map are not read by the checker.

## Risks / limits

The sentence is constructed solely to entail the selected relation, so this tests human clause-to-record traceability on a deliberately easy example, not whether any source text is authentic or whether the relation is canonically true. “Carried” must not be broadened to ownership, continuous possession, or a timeline event. The existing entity claims and events remain in the copied JSON; they are not newly supported by this one-sentence excerpt and must be marked outside this map’s scope. A clean checker exit establishes only the existing structural/citation checks, not prose entailment.

## Falsifiable check

From repo root run `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt`; require exit 0. Independently compare all five JSON files byte-for-byte with `consistent/` and inspect the excerpt/map: the map must cite the exact sentence, each mapped element must correspond to `relations[0]`, and it must make no inference beyond `carries`. A reviewer can falsify the proposed match by identifying any mapped field not entailed by that exact sentence, or any extra JSON difference. Replay all 78 pre-round fixtures against the declared baseline and verify all stdout/stderr/exit tuples and 389 pre-existing JSON paths remain identical. This is a manual check of a constructed excerpt only; it is not a source-text truth or canon claim.

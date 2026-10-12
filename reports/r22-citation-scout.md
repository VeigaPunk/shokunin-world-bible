# Round 22 citation scout — dependency inputs versus source/canon truth

## Scope and evidence

Read-only inspection of the round-22 baseline checker at `cc92ece` as named in `.shokunin/lore/LOG.md`, the current checker, the `consistent` fixture's timeline and source registry, and corpus documentation. No dependency probe was run for this citation-only assignment; no checker, fixture, shared document, or canon file was changed.

## Raw observations (not recommendations)

- The checker's timeline rows are **input data**: each row supplies `id`, integer `tick`, `depends_on`, `description`, and `source_id`. The active `consistent/timeline.json` input, for example, gives `departure` tick 1 with no dependencies and `arrival` tick 2 depending on `departure`; both rows name `courier-log` as `source_id`.
- The active checker resolves dependency IDs using the timeline input's event-ID index and compares the corresponding input tick values. A uniquely resolved edge is called an inversion when prerequisite tick is greater than or equal to dependent tick, provided both ticks are nonnegative. It does not parse or retrieve source text while making this check. The current malformed-member branch reports `expected event-id strings` and skips traversal of the entire row's dependency list; this is checker behavior, not evidence about what any source says.
- `consistent/sources.json` contains registry metadata for `courier-log` (title “Courier Mira’s Route Log, year 12”, kind “fictional personal log”, reliability note “in-world fiction; first-person account”) and `archive-ledger`. The inspected fixture contains no underlying log/ledger passages. A source registry entry and matching `source_id` therefore establish an input reference to a registered ID, not that the cited text exists in this repository or supports a stated event, tick, or dependency.
- The input's `description` is not compared against source text by the dependency checker. `fixtures/README.md` describes ticks and strict earlier-tick dependency conventions as invented local-sequence rules; it also says citations are validated structurally, not for truth. That documentation specifies the checker convention, not independent evidence that a particular in-world event or ordering is canon.
- The dependency input, source reference, and underlying source-text/canon truth are distinct evidence layers: a dependency string and ticks are values provided to the checker; `source_id` resolves against the local metadata registry; whether a cited passage attests those values is not observed here. Inversion output thus describes the supplied data under the checker rule, not a source-authenticated chronology or canon contradiction.

## Recommendations (separate from observations)

- Describe any round-22 paired probe as an input-level checker result. State exactly which `depends_on` and tick values were supplied and which diagnostics appeared; do not say the source proves an inversion or that a malformed member is canonically satisfied/unsatisfied.
- Keep source-reference claims narrow: “the row's `source_id` resolves uniquely in this fixture registry,” if demonstrated. Do not upgrade ID resolution to citation support, source-text verification, reliability judgment, or canon truth.
- If discussing a source-supported ordering in future work, inspect the actual cited passage and report its contents separately from checker results. No such passage was inspected for this report.
- Preserve the input-only scope in descriptions and summaries. An observed checker inversion is not by itself an in-world contradiction; the checker reports structural comparison results and does not adjudicate canon.

This is a citation-scope scout report, not a dependency probe, implementation recommendation beyond citation boundaries, axis verdict, or round-admission decision.

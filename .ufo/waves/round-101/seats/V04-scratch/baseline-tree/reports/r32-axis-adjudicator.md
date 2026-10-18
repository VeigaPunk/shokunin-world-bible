# Round 32 — independent per-axis adjudication

**Verdict: admit the narrow calibration move.** Calibration improved; depth unchanged; coverage unchanged. At least one axis improved and none was harmed. This is an admitted-source-count distinction, not a new checker rule or proof of unique evidence in-world.

| Axis | Judgment | Basis |
|---|---|---|
| Depth | **unchanged** | No richer lore, source prose, relation model, or canon determination was added. The checker and four non-source tables remain unchanged. |
| Coverage | **unchanged** | The added malformed-source fixture exercises a source-specific screening boundary, but does not establish a wider new input class or checker behavior beyond the declared one-field case. r26 already demonstrated analogous malformed **entity** screening; that did not establish the source-specific result. |
| Calibration | **improved** | The controlled comparison distinguishes a duplicate raw source ID from *two admitted* source IDs: the malformed second `courier-log` row gets a required-title error and is excluded from this checker's source-ID count, while the admitted comparator has eight findings and the unique control is clean. The absent ambiguity findings are expressly not in-world uniqueness or source-content evidence. |

I read the round-32 declaration and post-scout policy in `LOG.md`, `corpus/fixtures/README.md`, the r32 critic and source-screen scout, and the non-author reviewer and independent verifier reports. I independently inspected the fixture pair: the only parsed value changed from `r31-source-ambiguous` to `r32-source-malformed` is `sources[2].title`, `"Courier Log Registry Duplicate Index"` → `""`; the raw `sources[2].id` remains `courier-log`, matching `sources[1].id`. The other four JSON tables are byte-identical. `check_bible.py` admits rows only after required-field checks (`:21–43`); `index('sources')` and `source_id_counts` consume admitted rows (`:45–56`), and citation status uses that count (`:64–74`). This explains the observed diagnostic change without silently deleting the raw row.

Independent spot replay from the repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` produced:

- `r32-source-malformed`: exit **1**, only `VIOLATION: sources[2].title: required nonempty str` and `1 violation(s); no canon changed`; no duplicate admitted source ID and no ambiguous citation finding.
- `r31-source-ambiguous`: exit **1**, exactly **eight** findings: duplicate `sources[2].id`, four entity citation locations (`entities[0]` and `[3]`, first appearance and claim each), `relations[0].source_id`, and `timeline[0]`/`[1].source_id`, all seven citation locations ambiguous for `courier-log`.
- `r31-source-unique`: exit **0**, `CLEAN: schema, citations, relations, timeline; 0 violations`.

For regression I extracted the baseline `cfaf03a885f36fb6398b5c9dc0810a39cb573807` fixture tree with `git archive`: **83/83** pre-existing fixture directories replayed at the same current fixture argument with baseline and worktree checker, matching exit and displayed output; baseline and worktree checker bytes themselves are identical. I compared **414/414** baseline fixture JSON paths byte-for-byte against the worktree: zero differences. The non-author verifier separately compared exact `(exit status, stdout bytes, stderr bytes)` for all 83/83 and reported empty stderr on the target triad, corroborating the replay without treating a merged terminal stream as independent stderr evidence.

**Boundary:** r26's malformed `entities[4].name` demonstrates prior entity-row admission screening, so this is neither novel general screening nor a source-truth finding. This fixture specifically establishes one required-title screening boundary for admitted **source** counts and downstream citation ambiguity in this checker. The raw duplicate remains; the sole title error is still a failed input, not clean evidence. No source authenticity or textual support, in-world uniqueness, canon, real-world rights, or AI-training permission follows. No SHONEN checkmark, promotion, push, or merge is inferred.

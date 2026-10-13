# Round 79 fixture scout — safe clone and append-only boundaries

## Scope

Report-only map of the Round 79 declaration and the delivered r73 fixture. I did not edit a fixture, checker, LOG, or any file other than this report; did not run the checker; and made no commit, push, or merge. At inspection, no r79 fixture existed. The working tree already showed `.shokunin/lore/LOG.md` modified; I left that declaration untouched.

## What Round 79 permits and protects

The declaration proposes a depth hypothesis: an explicitly fictional first-person account and cited entity claim should support one concrete, bounded editorial scene/action choice—not merely add decorative texture or a generic character trait. Its test requires an exact excerpt→claim→source mapping, with the use decision still warranted after removing title/authority, unrelated r72/r73 slate linkage, and editor speculation. It rejects unsupported event/timeline/relation/contradiction additions and requires non-author review to see a distinct useful choice.

The permitted implementation, only if later authorized after scouts, is a five-table clone of `r73-jorin-slate-claim`, with tightly scoped source/claim additions and new prose pointer material. Protected: all existing corpus files/fixtures, `check_bible.py`, `LOG.md`, and all other reports. In particular, do not modify r73 to make the new case fit; do not add or rewrite its existing sources, claims, prose, relations, timeline, or contradiction ledger. This scout itself is limited to `.shokunin/lore/reports/r79-fixture-scout.md`. No source-truth, canon, rights, or mechanics conclusion is in scope.

## r73 baseline and safe structural route

The r73 fixture has 19 files. It is already a clone of r72: eight source rows and eight entity rows. The fixture-local pointers of interest are:

- `sources.json` `/7`: existing `jorin-slate-note`; do not reuse for a new speaker/account.
- `entities.json` `/7`: existing Jorin; `/7/claims/1` is his r73 slate-reading claim. Do not attach a new speaker’s account to Jorin merely to avoid a new entity or imply a connection.
- `relations.json`, `timeline.json`, `contradictions.json`: preserve byte-for-byte; add no relation, event/tick/dependency, or contradiction row under the declared claim-only approach.
- Existing prose includes `jorin-slate-note-excerpt.md`, its clause map, and an editorial comparison of the r72/r73 attributed slate wordings. These are inherited context, not evidence linking the new proposal to that slate or occasion.

If an executor is later authorized, make a separate candidate by copying r73 unchanged, then append (do not reorder or rewrite) one distinct, unique fictional-source row and the minimum appropriate attributed entity claim. For an actually new character, append a separate entity rather than conflating it with Jorin/Vela/Neri; if the proposed character is already represented, preserve all existing fields and append only the justified claim. Add a new exact excerpt and clause-map/report prose with precise pointers. Avoid a timeline/event row unless the contract is explicitly changed and justified; the current Round 79 declaration rules out unsupported such additions. Keep the editorial use decision explicit, narrow, and supported by the quoted source text, not by a source title or editor inference. This is a structural strategy, not approval to invent a candidate before the remaining reports settle.

An append-only candidate should retain every old r73 path and raw bytes except the declared JSON append targets; new files should be additions. `sources.json` and `entities.json` JSON serialization may change when arrays are appended, but old rows and their order/values must be preserved exactly. The regression lane must compare pinned old corpus bytes and the old raw checker `(exit, stdout, stderr)` tuples; checker cleanliness alone is not a regression or prose test.

## Citation and evidence limits

`check_bible.py` resolves a claim’s `source_id` against source IDs in `sources.json` and checks structure. That establishes only that the fixture claim points to an existing identifier. It does **not** read the Markdown excerpt or clause map, validate quotation spans or semantic entailment, authenticate a source, or prove any claimed event/action occurred. Human review must compare each material claim clause against exact excerpt text; the map is an aid, not independent evidence.

Treat the source and excerpt as invented, unverified in-world fiction. A source ID is a fixture-local attribution pointer—not proof of source-text truth, speaker identity, canon, chronology, physical artifact, or a shared slate/occasion. Do not promote editorial suggestion to canon. An invented source or its ID does not establish copyright/license/reuse/training rights; no rights finding is made. No game mechanics are established or changed by this fixture structure.

## Recommendation

For any eventual candidate, the safe form is a clean r73 clone with only append-only source/entity additions plus new attributed prose/pointer files, while preserving all inherited paths/bytes and all protected files. Keep the character/action decision concrete and independently defensible without borrowed slate linkage. If that decision cannot be supported directly by the fictional excerpt after stripping authority/title/editorial speculation, recommend no-go rather than adding generic texture or structural world events.

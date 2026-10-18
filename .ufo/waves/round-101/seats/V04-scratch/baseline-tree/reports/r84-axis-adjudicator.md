# Round 84 — independent final axis adjudication

**Decision: NO-GO.** The declared duplicate-event-ID-only suppression or qualifier has no demonstrated material gain. No checker/fixture candidate was installed. The work/evidence pin is `539a53126a9347c75b7c4a3b59f109f1e532ae4d`, against report-last baseline `596f70e417c794f6d09279ee26cf9a03dd17eea9`.

| Axis | Judgment | Reason |
| --- | --- | --- |
| Depth | **Unchanged** | No new independently supported account, event interpretation, source reading, or stronger inference was added. The temporary rows are invented structural inputs. |
| Coverage | **Unchanged** | No new rule or corpus fixture was retained, and no existing case class changed. Existing duplicate-ID and occupancy findings remain separately available; preservation of prior cases is not new coverage. |
| Calibration | **Unchanged** | The observed double-booking line describes a comparison of two admitted raw rows, which is still assessable despite their ambiguous shared event label. No reader outcome or changed safe first action shows that suppressing or specially qualifying it improves use of the checker. This is not a judgment that every reader interprets the present wording correctly. |

The admission threshold requires at least one **improved** axis and none harmed; it is not met. Suppressing the line would plausibly **harm** actionability by hiding the row-field collision, but that prospective risk is not scored as an observed harmed axis because no candidate was built. A carefully scoped generic wording change remains possible, not proven beneficial by this event-ID pair. This rejects the proposed move, not the utility of independently diagnosing duplicate event IDs.

## Independent inspection and replay

I read the Round 84 LOG declaration and settlement, all ten pinned `r84-*.md` scout/reviewer/verifier reports, the active checker, and R9, R12, R16, R19, R37, R52, and R70 axis judgments. `git diff --name-status 596f70e 539a531 -- .shokunin/lore` contains only the LOG update and ten reports: no corpus/checker/config change. The active checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`. The non-author verifier's separate pinned-archive comparison reports 1,368/1,368 corpus paths and bytes identical and 133/133 prior root-relative `(exit, stdout, stderr)` tuples identical (28 exit 0, 105 exit 1). I did not independently replay that entire old suite; its preservation evidence is not a validation of a proposed implementation.

I separately recreated the relevant pair outside the repository from `fixtures/consistent`'s five JSON tables. Only `timeline.json` was replaced: two admitted rows cite existing unique source IDs, use unique actor `mira`, nonnegative local tick `7`, and the distinct uniquely typed places `harbor` and `tower`. Their first event ID is `pair-event-a`; only the second ID differs across copies, `pair-event-b` versus `pair-event-a`. Running the unchanged checker from the repository root with stdout/stderr separately captured yielded exactly:

```text
Distinct IDs — exit 1, stderr empty:
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed

Duplicated ID — exit 1, stderr empty:
VIOLATION: timeline[1].id: duplicate timeline id 'pair-event-a'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
```

This independently matches the pair scout and verifier. The checker admits schema-valid rows into `data['timeline']` (`check_bible.py:41–76`), reports repeated event IDs from its index, and counts those IDs for dependency/ledger endpoint dereferencing (`:78–95, :113–141, :295–316`). Occupancy instead iterates **both admitted rows** directly (`:269–294`); it requires a uniquely resolved actor, a uniquely resolved entity of kind `place`, and a nonnegative tick. Its key is `(entity_id, tick)` and it compares supplied `place_id` fields. Event-ID uniqueness and source status do not gate that branch. Thus an ambiguous *reference to an event ID* does not make these already-present row operands ambiguous. The identical booking line in the matched pair is warranted **as a supplied-input inconsistency**, not as a claim that two actual events occurred or that two independent witnesses corroborate either row.

R9's dependency and R37's ledger endpoint must resolve an event-ID pointer, so their exact-one guards cannot transfer to this row-wise comparison. R12's ambiguous **actor** strikes the occupancy identity operand itself; R16's unresolved/non-place place and R19's negative tick strike its comparability/domain. All those operands are eligible in this pair. R52's source-ID ambiguity likewise left the independently available raw actor/tick/place collision intact, and R70 cautions that a removed warning may have its own first-repair value even when old tuples are preserved. These are bounded analogies, not substitutes for the pair replay.

## Editor action and falsifier

For the duplicate-ID copy, first inspect what the rows and citations are intended to represent, preserve both raw assertions, and repair the reused label/reference **only if** separate record identities are supported; update dependent pointers where needed. Never select first/last, merge, delete, or silently invent a distinct event. Also inspect the actor/tick/place assertions against cited material and correct or reconcile unsupported fields. For the distinct-ID copy, the label repair is absent, but **the same field check remains**. Suppression hides that check; a duplicate-only qualifier repeats the existing ID warning without demonstrating a safer action. The word `double-booked` might be overread as in-world truth, but the present record supplies no blinded editor misreading or intervention showing an event-ID-specific qualifier fixes it without a misleading converse for uniquely named but unverified sources.

Reopen only with controlled evidence that the extant pair leads to a consequential unsafe first edit and that a precisely specified suppression/qualifier produces a distinct safer action **while retaining the row-field finding's utility**, including both row orders and regression replay. An independently justified general input-structural wording proposal would be a separate move, not an admission of this one.

All names, descriptions, cited source rows and local ticks here are authored, fictional and unverified. Unique source IDs resolve registry pointers, not prose support; checker outputs prove neither real occurrence, actual location, independent chronology, fictional-world canon, rights, nor mechanics. No source truth or ambiguity resolution is attributed to the input pair.

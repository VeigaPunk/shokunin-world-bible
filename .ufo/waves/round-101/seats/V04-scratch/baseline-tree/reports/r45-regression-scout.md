# Round 45 regression scout — pinned replay and paired controls

## Result

**Replay PASS for preservation; candidate semantics remain unproven.** I independently archived the declared r44 report baseline `7ef761d639c18f3a09a61477956b234042a91ebf` (`.shokunin/lore/LOG.md:754`) to `/tmp/r45-regression-qokxehd_`. It contained 95 fixture directories and 474 JSON paths. All 474 current JSON files are byte-identical to that archive; `check_bible.py` is byte-identical (SHA-256 `5a389f1f5c0ccf104d9109f7a4740f398a73d6b372ad82c4e9abb3d4a4052d27`). Running the standard root-relative checker command in both trees matched raw stdout, stderr and exit code for **95/95** fixtures. No r45 fixture is present. The only current worktree modification observed was the parent-owned `LOG.md`; I changed no fixture, checker, README, LOG, nor committed anything.

This verifies historical replay/preservation, not a calibration improvement. Baseline and controls:

| Input/control | Observable | Meaning / limit |
|---|---|---|
| Existing `r12-unique-actor` | Two distinct `mira` events at tick 7, `harbor`/`tower`; `double-booked` | Existing character conflict control (README lines 245-265). |
| Existing `r12-ambiguous-actor` | Duplicate actor identity yields ambiguity, not definite occupancy | Existing uncertainty guard, not a faction control (README lines 247-260). |
| Existing `r21-clean` / malformed pair | Occupancy independent of malformed dependency list under unique actor/place/tick guards | Not evidence about non-character occupancy (README lines 445-468). |
| Proposed faction pair | Not implemented or run by this scout; no source prose authenticated | Need a same-tick, two-place faction case and a paired character case before any behavior change. |

The checker contract admits four entity kinds and `timeline.entity_id` is only typed `str` (`check_bible.py:7-14`). Occupancy indexes `(entity_id,tick)` and reports different-place bookings for any uniquely indexed ID when place and tick qualify (`check_bible.py:228-252`). Fixture README says only “A character cannot occupy different places at the same tick” (`README.md:29-34`). It does not say every faction is distributed, that a faction is never singularly located, or that every event's faction subject denotes outposts/membership rather than a focal location. The candidate's invented report can describe separate outposts, but cannot independently authenticate that premise or impose it on the schema.

## Risks and decision rule

**Risk:** excluding factions wholesale from occupancy would suppress an existing structural finding for any uniquely identified faction, including a faction whose event rows intentionally assert one focal location. Conversely, retaining the rule may flag a distributed-faction account. Neither is established as the universally correct ontology by current README/schema. Do not widen this to all non-character entities: items and places have different meanings, and the source gives no basis for exempting them. Preserve character double-booking exactly.

**Falsifiable go/no-go:** GO only if a documented project convention or clearly bounded event semantics support that these timeline faction rows mean distributed group presence rather than one focal-location assertion, and temporary paired inputs show: (1) unchanged baseline character conflict still emits `double-booked`; (2) otherwise-identical valid faction distributed-presence pair changes only actor kind and does not emit that finding under the proposed narrow rule; (3) a faction focal-location conflict remains reported (or an explicit contract justifies its exclusion); (4) unrelated kinds/diagnostics remain unchanged; and (5) the pinned 95/474 replay remains exact. Have a non-author reviewer judge the source wording and scope, not merely observe CLEAN. NO-GO if support is just an invented excerpt, generic `faction` kind, structural CLEAN, or the README's character-specific sentence; also NO-GO if the guard suppresses the character control or silently exempts every faction without grounded scope. Source IDs establish identity/resolution only; checker output does not validate textual support, truth, source authenticity, or canon (`README.md:32-41`, `r12` lines 256-265).

No candidate is admitted by this replay scout. Temporary replay artifacts are outside the repository. No files beyond this requested report were written.

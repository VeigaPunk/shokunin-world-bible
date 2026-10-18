# Round 38 scribe — ledger source-ambiguity decision table

Scope: decision aid for the declared Bell-7 ledger probe, not a checker change or canon interpretation. Round 38 holds the r35 ledger and unique event IDs fixed while adding one duplicate `sella-bell7-note` source row (`.shokunin/lore/LOG.md:354-359`). This report alone makes no claim that the proposed output has been independently replayed.

## Decision table

| Matching valid `sources.json` rows for a uniquely resolved ledger event's `source_id` | Checker result at that ledger side | Bounded conclusion |
|---:|---|---|
| 0 | `<side>.event_id`: event has no resolvable `source_id` | Event pointer identifies one timeline row, but its cited source ID is unknown; this does not falsify the event or its account. |
| 1 | No source-ambiguity diagnostic for that side | The event pointer and source ID resolve structurally. This establishes neither source-text support nor report truth. |
| 2+ | `<side>.source_id: ambiguous in-world source '<id>'`; duplicate source row also gets `sources[i].id: duplicate sources id '<id>'` | The timeline event remains uniquely identified, but this ledger side's citation is ambiguous. Do not choose/merge a source row or infer which report is true. The other ledger side is checked independently. |

A ledger side reaches this source check only after its `event_id` names exactly one valid timeline row: zero or multiple matching events instead produces the side-local exact-one event diagnostic and skips source lookup (`.shokunin/lore/corpus/fixtures/check_bible.py:92-100`). The code obtains each event's `source_id`, checks its multiplicity, and reports ambiguity at `<side>.source_id` (`check_bible.py:95-100`); source counts include admitted source rows (`:53-56,64-74`). General source-ID multiplicity behavior is documented for relation citations in the r31 precedent (`.shokunin/lore/reports/r31-scribe.md:5-13`); r7 exercised alliance/provenance citation sites, not this two-sided ledger branch (`.shokunin/lore/reports/r7-scribe.md:18-30`). R37's duplicate-event ledger endpoint case is a different ambiguity layer (`.shokunin/lore/reports/r37-scribe.md:7-13`).

## Bell-7 ledger mapping

| Ledger endpoint | Unique event pointer | Event citation | Decision if source ID has two rows |
|---|---|---|---|
| `claim_a` | `tarin-envelope-observation`, `field=place_id` (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:3-7`) | `tarin-note` (`.../timeline.json:23-30`) | Its ID remains unique in the declared negative; no Sella-source ambiguity follows for this side. |
| `claim_b` | `sella-bell7-presence`, `field=place_id` (`.../contradictions.json:8-11`) | `sella-bell7-note` (`.../timeline.json:32-39`) | The declared duplicate makes the unique Sella event's citation ambiguous; expect a side-local `claim_b.source_id` finding, not an event-ID ambiguity. |

The two distinct `place_id` pointers and `why` preserve an editorial comparison of attributed reports (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:3-12`). A structurally ambiguous citation weakens attribution resolution for `claim_b`; it does not erase the timeline row, choose between Sella's reports, prove the account unsupported or false, decide the apparent conflict, or establish a canon winner. Even a unique ID only resolves a reference, not prose entailment or authenticity (`.shokunin/lore/reports/r31-scribe.md:11-13`; `.shokunin/lore/reports/r35-scribe.md:14-15`).

## Risks

- Do not conflate duplicate **source** ID with r37's duplicate **event** ID: here the event pointer is unique while its cited source identity is not (`r37-scribe.md:9-13`; checker `:92-100`).
- Duplicating a source ID can cause local ambiguity findings at every reference to that ID, not only the ledger side. The full CLI output must inventory any additional locations; do not promise exactly two findings from the declared duplicate (`LOG.md:357-359`; checker `:68-74,107-116,242`).
- A duplicate row is not evidence that either source text is authentic, supportive, or canonically correct. The source ID checker does not parse the excerpt or validate `why` (`check_bible.py:18-43,64-74,76-105`).
- Tarin's `place_id=harbor` describes his reported observation scene; the ledger's rationale explicitly distinguishes it from the claimed Sella location (`r35-scribe.md:9,14`; r35 `contradictions.json:12`). Avoid turning it into a claim that Tarin was Sella or that either account is independently verified.

## Falsifiable check

Run the declared control and negative commands from repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r38-ledger-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r38-ledger-ambiguous
```

The declared control should exit 0. The negative should retain unique event IDs and both ledger endpoints, report the duplicate `sella-bell7-note` source ID and `contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'`; all other output must be captured and explained, not assumed (`LOG.md:357-359`). The claim is falsified if the unique control fails, the duplicate is not diagnosed, the claim_b source ambiguity is absent, a source row is selected as canonical, or the event pointer is misreported as ambiguous. Compare all 90 prior CLI stdout/stderr/exit tuples and 449 prior JSON path bytes to the declared baseline; any mismatch requires explicit accounting (`LOG.md:357-359`). This checks only that source-ID ambiguity is surfaced at a uniquely resolved ledger endpoint; it cannot prove excerpt support, account truth, or a semantic contradiction.

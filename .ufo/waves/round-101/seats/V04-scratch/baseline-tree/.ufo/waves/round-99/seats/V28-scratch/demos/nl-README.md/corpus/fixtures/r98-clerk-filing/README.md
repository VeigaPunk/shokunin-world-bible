# Round 98 clerk-filing continuation

This is an explicit continuation of `r97-crossing-acknowledgment`, itself a continuation of `r96-crossing-response`, itself a continuation of `r95-crossing-aftermath`, itself a continuation of `r94-paired-crossing`, itself a continuation of `r88-m3-maya-cluster`; it is not an unrelated bible and not a rewrite of any snapshot. The five inherited entity records, the one inherited relation, the six inherited events, and the six inherited sources are copied by JSON value; their source IDs, the paired-clock and crossing-minute excerpt wording, the Spence excerpt, and the inspiration context are retained. The added `clerk-maren` entity, the added tick-14 filing event, and its note make the counts 6 entities / 1 relation / 7 events / 7 sources.

## Namespace and occasion comparison

Source IDs are cluster-local. Compare them as path-qualified pairs, for example `(r97-crossing-acknowledgment, paired-clock)` and `(r98-clerk-filing, paired-clock)`, not by bare ID alone. This continuation intentionally reuses the inherited IDs and records; path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction. The added source is `clerk-filing-note`, the harbor clerk's first-person filing record, the added entity is `clerk-maren`, and the added event is `clerk-filing-open`.

The inherited paired-clock entries remain distinct tick-9 events: Aru's north lantern at Quiet Rise and Evin's south bell at Salt Court. The inherited tick-10 meeting at the Chalk Stair remains ordered after and explicitly dependent on both named tick-9 entries. The inherited tick-11 event is ordered after and depends on the tick-10 decision (`paired-crossing-decision`), and it records only Aru's report that he waited through the agreed bell and that Evin did not come. The inherited tick-12 event is ordered after and depends on that tick-11 report (`aftermath-missing-evin`), and it records only Evin's second account of the same occasion: that he was at Salt Court through the same agreed bell. The inherited tick-13 event is ordered after and depends on that tick-12 response (`response-evin-salt-court`), and it records only Aru's acknowledgment that he received Evin's response while holding to his own account. The new tick-14 event is ordered after and depends on the tick-13 acknowledgment (`acknowledgment-aru-records`), and it records only that the clerk filed both pending accounts and recorded the matter OPEN. It adds one filing record; it does not change earlier locations, resolve or create a contradiction, or convert either account into a verdict.

The clerk bound is explicit in the record: the filing note is an institutional filing record that asserts no finding and no resolution; it reaches no verdict, reconciles nothing, and selects no winner between the two first-person accounts, which stand unresolved. The filing does not overturn, confirm, adjudicate, or reconcile the accounts, and `contradictions.json` remains empty; the accounts name different actors at different places (Aru at the Chalk Stair, Evin at Salt Court), so no contradiction is asserted. The crossing-only bound is likewise retained: the agreement covered this crossing only, and the record asserts no other duty, no breach, no continuing obligation, and no obligation beyond this crossing. It is not evidence of an alliance, a continuing practice, perpetual performance, a standing duty, an adjudication, or an external historical fact. The tick-14 event's `entity_id` is `clerk-maren` because the schema has one actor slot; its description names both pending accounts, so the field does not exclude the two participants.

The integer ticks and event-ID edges in `timeline.json` are editorial encodings of the excerpts' tick labels and stated order/dependence, not literal JSON wording in the sources. Inherited empty `depends_on` arrays mean no earlier dependency is represented for those entries in this mapped sequence; they do not assert that no earlier event exists anywhere.

`first_appearance: crossing-minute` identifies the source that first presents Chalk Stair as a specific place in the JSON bible, not the earliest occurrence of the words: the inherited r88 verse already uses “chalk stair” as an unowned crossing metaphor. That image is retained and is not retroactively made a map/location record. Likewise, `first_appearance: clerk-filing-note` identifies the source that first presents the clerk Maren as a named entity in this JSON bible; it asserts no office beyond the filing, no finding, and no other record.

## Bounded external design prompt

The copied Spence passage is his English prose about a story he labels “Kiche,” not an authenticated K'iche-language primary text. It is an editorial design prompt only: the comparison sets Spence's narrated naming/land appearance beside this invented crossing's name-without-map framing. It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here.

`claim-excerpt-map.md` has 20 source-attributed JSON pointer obligations (the 17 inherited rows carried unchanged plus the three new clerk rows: `clerk-maren`'s first-appearance pointer and claim, and the tick-14 filing event) and separately labeled editorial comparisons. The `support_check.py` receipt is lexical preflight only, not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
```


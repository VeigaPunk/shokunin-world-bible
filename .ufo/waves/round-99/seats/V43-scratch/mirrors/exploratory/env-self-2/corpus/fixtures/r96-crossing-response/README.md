# Round 96 crossing-response continuation

This is an explicit continuation of `r95-crossing-aftermath`, itself a continuation of `r94-paired-crossing`, itself a continuation of `r88-m3-maya-cluster`; it is not an unrelated bible and not a rewrite of any snapshot. The five inherited entity records, the one inherited relation, the four inherited events, and the four inherited sources are copied by JSON value; their source IDs, the paired-clock and crossing-minute excerpt wording, the Spence excerpt, and the inspiration context are retained. The added tick-12 response event and its note make the counts 5 entities / 1 relation / 5 events / 5 sources.

## Namespace and occasion comparison

Source IDs are cluster-local. Compare them as path-qualified pairs, for example `(r95-crossing-aftermath, paired-clock)` and `(r96-crossing-response, paired-clock)`, not by bare ID alone. This continuation intentionally reuses the inherited IDs and records; path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction. The added source is `evin-response-note`, Evin's first-person response note, and the added event is `response-evin-salt-court`.

The inherited paired-clock entries remain distinct tick-9 events: Aru's north lantern at Quiet Rise and Evin's south bell at Salt Court. The inherited tick-10 meeting at the Chalk Stair remains ordered after and explicitly dependent on both named tick-9 entries. The inherited tick-11 event is ordered after and depends on the tick-10 decision (`paired-crossing-decision`), and it records only Aru's report that he waited through the agreed bell and that Evin did not come. The new tick-12 event is ordered after and depends on that tick-11 report (`aftermath-missing-evin`), and it records only Evin's second account of the same occasion: that he was at Salt Court through the same agreed bell. It adds one second first-person account; it does not change earlier locations, resolve or create a contradiction, or convert either account into a verdict.

The unresolved-two-accounts bound is explicit in the record: Evin's note makes no accusation against Aru and selects no winner between the two accounts, and the two first-person accounts stand unresolved. The accounts name different actors at different places (Aru at the Chalk Stair, Evin at Salt Court), so no contradiction is asserted and `contradictions.json` remains empty; the second account does not overturn, confirm, or adjudicate the first. The crossing-only bound is likewise retained: the agreement covered this crossing only, and the record asserts no other duty, no breach, no continuing obligation, and no obligation beyond this crossing. It is not evidence of an alliance, a continuing practice, perpetual performance, a standing duty, or an external historical fact. The tick-12 event's `entity_id` is Evin because the schema has one actor slot; its description and the note name the other account, so the field does not exclude Aru.

The integer ticks and event-ID edges in `timeline.json` are editorial encodings of the excerpts' tick labels and stated order/dependence, not literal JSON wording in the sources. Inherited empty `depends_on` arrays mean no earlier dependency is represented for those entries in this mapped sequence; they do not assert that no earlier event exists anywhere.

`first_appearance: crossing-minute` identifies the source that first presents Chalk Stair as a specific place in the JSON bible, not the earliest occurrence of the words: the inherited r88 verse already uses “chalk stair” as an unowned crossing metaphor. That image is retained and is not retroactively made a map/location record.

## Bounded external design prompt

The copied Spence passage is his English prose about a story he labels “Kiche,” not an authenticated K'iche-language primary text. It is an editorial design prompt only: the comparison sets Spence's narrated naming/land appearance beside this invented crossing's name-without-map framing. It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here.

`claim-excerpt-map.md` has 16 source-attributed JSON pointer obligations (the 15 inherited rows carried unchanged plus the new tick-12 event row) and separately labeled editorial comparisons. The `support_check.py` receipt is lexical preflight only, not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
```

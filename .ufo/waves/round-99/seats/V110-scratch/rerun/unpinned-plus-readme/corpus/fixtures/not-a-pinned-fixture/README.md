# Round 95 crossing-aftermath continuation

This is an explicit continuation of `r94-paired-crossing`, itself a continuation of `r88-m3-maya-cluster`; it is not an unrelated bible and not a rewrite of either snapshot. The five inherited entity records and the one inherited relation are copied by JSON value; their source IDs, the paired-clock and crossing-minute excerpt wording, the Spence excerpt, and the inspiration context are retained. The added tick-11 aftermath event and its note make the counts 5 entities / 1 relation / 4 events / 4 sources.

## Namespace and occasion comparison

Source IDs are cluster-local. Compare them as path-qualified pairs, for example `(r94-paired-crossing, paired-clock)` and `(r95-crossing-aftermath, paired-clock)`, not by bare ID alone. This continuation intentionally reuses the inherited IDs and records; path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction. The added source is `aru-aftermath-note`, Aru's first-person note, and the added event is `aftermath-missing-evin`.

The inherited paired-clock entries remain distinct tick-9 events: Aru's north lantern at Quiet Rise and Evin's south bell at Salt Court. The inherited tick-10 meeting at the Chalk Stair remains ordered after and explicitly dependent on both named tick-9 entries. The new tick-11 event is ordered after and depends on the tick-10 decision (`paired-crossing-decision`), and it records only Aru's report that he waited through the agreed bell and that Evin did not come. It adds one reported non-arrival; it does not change earlier locations, resolve or create a contradiction, or convert the non-arrival into a verdict.

The crossing-only bound is explicit in the record: the agreement covered this crossing only, and the record asserts no other duty, no breach, no continuing obligation, and no obligation beyond this crossing. It is not evidence of an alliance, a continuing practice, perpetual performance, a standing duty, or an external historical fact. The tick-11 event's `entity_id` is Aru because the schema has one actor slot; its description and the note name the second participant, so the field does not exclude Evin.

The integer ticks and event-ID edges in `timeline.json` are editorial encodings of the excerpts' tick labels and stated order/dependence, not literal JSON wording in the sources. Inherited empty `depends_on` arrays mean no earlier dependency is represented for those entries in this mapped sequence; they do not assert that no earlier event exists anywhere.

`first_appearance: crossing-minute` identifies the source that first presents Chalk Stair as a specific place in the JSON bible, not the earliest occurrence of the words: the inherited r88 verse already uses “chalk stair” as an unowned crossing metaphor. That image is retained and is not retroactively made a map/location record.

## Bounded external design prompt

The copied Spence passage is his English prose about a story he labels “Kiche,” not an authenticated K'iche-language primary text. It is an editorial design prompt only: the comparison sets Spence's narrated naming/land appearance beside this invented crossing's name-without-map framing. It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here.

`claim-excerpt-map.md` has 15 source-attributed JSON pointer obligations (the 14 inherited rows carried unchanged plus the new tick-11 event row) and separately labeled editorial comparisons. The `support_check.py` receipt is lexical preflight only, not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
```


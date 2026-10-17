# Round 94 paired-crossing continuation

This is an explicit continuation of `r88-m3-maya-cluster`, not an unrelated bible and not a rewrite of that snapshot. The four inherited entity records and two tick-9 events are copied by JSON value; their source IDs, paired-clock excerpt wording, Spence excerpt, and inspiration context are retained. The added place, agreement, minute, and tick-10 decision make the counts 5 entities / 1 relation / 3 events.

## Namespace and occasion comparison

Source IDs are cluster-local. Compare them as path-qualified pairs, for example `(r88-m3-maya-cluster, paired-clock)` and `(r94-paired-crossing, paired-clock)`, not by bare ID alone. This continuation intentionally reuses the inherited ID and records; path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction.

The inherited paired-clock entries remain distinct tick-9 events: Aru's north lantern at Quiet Rise and Evin's south bell at Salt Court. The new occasion is one tick-10 meeting at the Chalk Stair between those places, after and explicitly dependent on both named tick-9 entries. It adds a consequence; it does not change the earlier locations or turn their near-miss into a contradiction. The relation records only the source-supported agreement between Aru and Evin to share stewardship for this crossing. It is not evidence of an alliance, a continuing practice, or perpetual performance. The minute's event `entity_id` is Aru because the schema has one actor slot; its description and excerpt name both participants, so the field does not exclude Evin.

The integer ticks and event-ID edges in `timeline.json` are editorial encodings of the excerpt's tick labels and stated order/dependence, not literal JSON wording in the minute. Inherited empty `depends_on` arrays mean no earlier dependency is represented for those entries in this mapped sequence; they do not assert that no earlier event exists anywhere. The tick-10 list names both inherited event IDs because the minute says its decision depends on both entries.

`first_appearance: crossing-minute` identifies the source that first presents Chalk Stair as a specific place in the JSON bible, not the earliest occurrence of the words: the inherited r88 verse already uses “chalk stair” as an unowned crossing metaphor. That image is retained and is not retroactively made a map/location record.

## Bounded external design prompt

The copied Spence passage is his English prose about a story he labels “Kiche,” not an authenticated K'iche-language primary text. It is an editorial design prompt only: the comparison sets Spence's narrated naming/land appearance beside this invented crossing's name-without-map framing. It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here.

`claim-excerpt-map.md` has 14 source-attributed JSON pointer obligations and separately labeled editorial comparisons. The `support_check.py` receipt is lexical preflight only, not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
```

probe

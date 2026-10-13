# Round 33 non-author reviewer — Tarin envelope observation

## Scope and verdict

Read-only review of `.shokunin/lore/corpus/fixtures/r33-tarin-envelope/`, its excerpt and clause map, and the appended source/entity/event JSON rows. Compared novelty and evidentiary bounds with r10 and r23. **The bounded observation is traceable and distinct**: Tarin reports seeing Sella perform a positive placement action, unlike r10’s Sella reporting her own registry entry/observation and r23’s Sella reporting a non-finding. It is not independent verification of the event or canon. Tick 3 is arbitrary fixture chronology, not excerpt chronology.

## Exact text and row trace

The entire excerpt (`tarin-note-excerpt.md`) reads: “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.” The clause map correctly treats “I, Tarin” and “Sella” → `tarin`/`sella`, and “Lantern Harbor” → `harbor`, as editorial fixture-local ID alignments, not names-to-IDs proven by the text. “saw” makes this Tarin’s reported observation; it does not independently establish the world event.

| Appended assertion | Exact excerpt support | Assessment |
|---|---|---|
| `sources[2]` `tarin-note` title/kind/reliability note | No excerpt clause asserts metadata. The note appropriately labels this a newly authored fictional first-person observation and non-omniscient report. | Editorial source metadata, not excerpt fact. |
| `entities[4]` `tarin`, name / first appearance | “I, Tarin” | Direct name match; first-appearance source ID is editorial alignment. |
| `entities[4].claims[0]` — Tarin reports seeing Sella place an unlabeled paper envelope on the Lantern Harbor registry desk | “I, Tarin”; “saw”; “Sella place an unlabeled paper envelope”; “on the Lantern Harbor registry desk” | Faithful, explicitly report-attributed paraphrase. Does not upgrade observation to verified fact. |
| `entities[5]` `sella`, name / first appearance | “Sella” | Direct name match; source assignment is editorial. |
| `entities[5].claims[0]` — Tarin reports that Sella placed the envelope on the desk | “Tarin saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.” | Correctly attributes the placement claim to Tarin; not Sella’s own testimony or an independently established action. |
| `timeline[2]` id `tarin-envelope-observation`, `entity_id: tarin`, `place_id: harbor` | “I, Tarin”; “on the Lantern Harbor registry desk” | Participants/place trace by editorial ID alignment. Event description accurately says Tarin reports seeing the action. |
| `timeline[2].description` | Whole sentence paraphrases the sole excerpt sentence | Supported as a report, not as a claim of independently verified occurrence. |
| `tick: 3`, `depends_on: []` | None | Tick is arbitrary local sequence metadata; excerpt supplies no date, sequence number, or chronology. Empty dependency means no ordering is asserted. |

The earlier rows in the copied files are baseline, not new claims: `mira`, `harbor`, `tower`, `seal`, the `mira → seal carries` relation, and the `departure`/`arrival` events retain their original IDs and `courier-log`/`archive-ledger` citations. They are not supported by this excerpt. In particular the baseline Mira/Blue Seal claim is not new evidence from Tarin.

## Novelty vs precedents

- **r10:** Sella’s own registrar-copy says she recorded seeing Mira leave and left a destination blank/kept a carbon. That is Sella’s first-person record of her own act and her account of a departure. r33 instead has Tarin as observer and Sella as the observed actor in a positive placement action. This third-party-reported observation class is distinct; shared Sella/harbor framing does not itself make it novel, but the observer/action roles do. It supplies no synchronized second perspective on r10’s departure.
- **r23:** Sella’s note says she looked for a route strip and did not find it on a rack. That is a speaker-bounded negative search report. r33 is a positive placement observation about a distinct object and scene; it neither establishes the strip’s status nor connects the envelope to it.

## Unsupported-envelope / canon scan

The excerpt and appended claims do not establish envelope contents, recipient, owner, intent, Blue Seal association, carbon, route strip, destination, or causal connection to another event. The envelope is not separately identified as an entity; “unlabeled” only describes what Tarin reports seeing. No relation or contradiction row adds such a link. `sources.json`’s `archive-ledger`/`courier-log` metadata and unchanged baseline claims do not become supported by `tarin-note`. The checker’s clean status establishes structural/citation-ID validity only, not prose entailment or canon truth.

## Conclusion

The clause map accounts for each newly asserted participant, location, action, and event description, while correctly labeling ID alignment and tick 3 as editorial/arbitrary. Sella’s placement is specifically **Tarin’s claim**, not Sella’s claim and not a verified fact. Novelty over r10/r23 is narrow but real: third-party positive placement observation. No unsupported envelope contents, recipient, owner, Blue Seal, carbon, route-strip, route, or canon inference found.

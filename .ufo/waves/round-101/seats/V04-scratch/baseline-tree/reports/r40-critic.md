# Round 40 critic — auditory report depth challenge

## Scope and baseline evidence

The r40 declaration proposes an independently authored Vela note: “I, Vela, stood on the Lantern Harbor east steps and heard two strokes I took to be the registry bell during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12. I did not see Sella or an envelope.” It calls this a third-party auditory-only report with a bounded non-sighting limit, and explicitly disclaims bell-origin proof, corroboration of Sella's location/envelope, and objective chronology (`.shokunin/lore/LOG.md:659`). This is a candidate, not evidence that a fixture exists; the same declaration says no r40 fixture was in baseline (`LOG.md:658`).

Round 14 cautions that newly authored prose tailored to existing rows is circular fixture consistency, not independent support, and that additional text/maps can be legibility rather than substantive depth (`reports/r14-critic.md`, sections “Challenge” and “Recommendation”). Round 23 says a named speaker's distinct bounded report can add an inspectable distinction only if not a relabeling of an existing predicate; clause maps and structural checks alone do not establish truth (`reports/r23-critic.md`, sections 1, 4, 5). Round 35 warns that bell labels identify only a fictional occasion claim, not authenticated time, and same tick/pointers do not prove semantic alignment (`reports/r35-critic.md`, “Falsification finding” and “Risks / limits”).

The r35 fixture already names a watch bell at North Tower (`corpus/fixtures/r35-bell7-conflict/entities.json`, tower claim) and describes the registry bell as the sole seventh-watch sounding for the stated fictional date in both accounts (`corpus/fixtures/r35-bell7-conflict/tarin-note-excerpt.md:1`, `sella-bell7-note-excerpt.md:2`). Tarin reports seeing Sella place an envelope at Harbor during that named ringing (`tarin-note-excerpt.md:1`); Sella reports her own Tower presence and Harbor non-presence during it (`sella-bell7-note-excerpt.md:1`). Their event rows share local tick 3, but the map states tick is arbitrary sequence metadata, not Bell-7/date evidence (`manual-clause-pointer-map.md`, “Exact clause map,” Tarin event row).

## Falsification: what is and is not new

There is a plausible, narrow depth gain if the Vela text is actually added and manually mapped: it contributes an additional attributed sensory modality (hearing two strokes) and a distinct reporter's explicit non-sighting of Sella/envelope. Neither is entailed by Tarin's visual placement report or Sella's own location report. The speaker's “I took [them] to be” wording is crucial: it records Vela's interpretation, not that the registry bell objectively sounded or that the strokes were Bell-7. This may enrich the set of fictional perspectives; it does not corroborate the other accounts.

But a third source row, character, event, and prose volume are not themselves depth. If the file merely mirrors the proposed JSON description, or the map treats source IDs / event rows as proving source-text support, this repeats r14's circular backfill. “Did not see Sella or an envelope” is a bounded report of non-sighting, not proof either was absent; do not upgrade to an absence event or contradiction. Likewise, two strokes “I took to be the registry bell” must not become “the registry bell rang twice,” “Bell-7 sounded,” or a second witness to either location account. A matching Bell-7 label can be a source-claimed occasion only; it cannot establish objective synchrony or make local tick 3 chronology.

The depth case is therefore conditional and modest: distinct authored observation/report detail, not new world fact, truth, canon, event-origin identification, confirmation of Tarin, support for Sella, or adjudication of their incompatible reports. A checker exit 0 only attests to whatever structural constraints it checks, not the prose's truth or entailment.

## Risks

- **Objective-origin laundering:** replacing Vela's uncertain identification with an objectively identified registry bell would overstate the sentence.
- **False corroboration:** hearing ambiguous strokes does not independently corroborate either person's place, Tarin's sighting, Sella's absence, or the envelope's existence.
- **Non-sighting inflation:** “I did not see” does not mean “was not there”; it is Vela's perceptual limit, not an objective negative.
- **Occasion/tick conflation:** the Bell-7/date wording is fictional testimony; tick 3 is editorial local order. Neither authenticates simultaneity or an external timeline.
- **Circular source support:** an authored excerpt drafted to match a new JSON row is not independent evidence. A manual map is an editorial aid, not validation.
- **Scope creep:** do not infer bell mechanism/location, exact time, Sella/envelope interaction, speaker reliability, or canon.

## Falsifiable check

On the implemented fixture (if one exists), an independent reader should compare the exact Vela excerpt and clause map against r35's Tarin/Sella excerpts and rows. Admit even a narrow depth improvement only if the excerpt actually says (1) Vela heard two strokes, (2) she *took them to be* the registry bell rather than asserting objective source, and (3) she did not see Sella or envelope, with all three clauses attributed to Vela and explicitly bounded as newly authored fictional report. Verify the map does not turn these into objective ringing/absence or corroboration; verify the r35 Tarin/Sella excerpts, rows, and unresolved ledger are byte-for-byte unchanged if preservation was claimed; and keep tick 3 explicitly non-chronological. If the operative novelty is only a new source/entity/event/label, if prose asserts actual bell origin, or if any existing report is upgraded by inference, classify depth unchanged or calibration harmed. This is a text-level check, not a test of whether Vela's fictional report is true.

## Stance

The declaration's wording offers a potentially distinct, bounded fictional perspective, unlike a pure restatement, but depth is not demonstrated by declaration or structural acceptance. Conditional narrow improvement if implemented and independently reviewed as above; otherwise unchanged. No claims about the objective bell, other reports' truth, or canon.

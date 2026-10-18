# Round 47 simplifier — object-centered link or no-go

## Evidence and smallest candidate

- The round-47 declaration proposes a new intake slip reporting an unlabeled envelope at the registry desk during what its writer calls Bell-7, with depositor unrecorded; it explicitly forbids inferring identity, occasion, or Sella placement (`.shokunin/lore/LOG.md: Round 47 declaration`).
- Tarin’s existing claim/event is already an attributed report that Sella placed an unlabeled envelope at that desk (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/entities.json:51-71`; `timeline.json:23-29`). The r35 ledger compares Tarin’s harbor and Sella’s tower accounts conditionally on same-bell identity/occasion (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/timeline.json:23-38`; `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:1-13`). R43 adds another attributed observation with an explicit occasion limitation; it does not identify an object (`.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/timeline.json:41-58`).
- Prior art already includes a cited registrar carbon about Sella’s record of Mira’s departure (`.shokunin/lore/corpus/fixtures/r10-registry-witness/timeline.json:23-29`; `.shokunin/lore/reports/r10-simplifier.md`, “Least new assertion set”) and an authored absence note whose failure to find a strip is not proof of absence (`.shokunin/lore/corpus/fixtures/r23-note-class/timeline.json:23-29`; `.shokunin/lore/reports/r23-simplifier.md`). A new source/title or another event row alone is not a distinct depth gain.

The smallest potentially useful move is one attributed object-presence assertion, not an agent/activity claim: an authored slip excerpt says only that an unlabeled paper envelope was on the Lantern Harbor registry desk during what the writer called Bell-7, and that the depositor was not recorded. If schema permits, represent `envelope` as an item and cite one observation event to the new source; the event actor must be a named observer only if the excerpt actually names one. Otherwise do not invent an observer/actor just to satisfy a schema. Do not add a relation to Tarin or Sella, a depositor entity, a second event, or any “same envelope” identifier. Keep this candidate separate from existing rows.

## Risks and decision

The envelope report could provide a narrow object-centered comparison with Tarin’s account, but the common object description and desk are not a stable identity key. It does not establish the same envelope, deposit, depositor, source, or occasion; “Bell-7” is only the slip writer’s label. In particular, an envelope-at-desk report does not identify the depositor, the same envelope or occasion, prove Tarin/Sella, canon, or rights. “Depositor not recorded” means only that this slip records no depositor; it does not prove nobody deposited it, Sella was absent, or Tarin was right. The new slip is invented in-world text, not independently authenticated evidence. A checker-clean result would attest structure/references only, not textual entailment or truth.

**Recommendation: no-go on implementation absent a concrete non-author demonstration that the object-specific comparison adds narrative depth beyond another attributed witness/record.** The candidate is falsifiable: go only if a reviewer can map every asserted clause to the new excerpt, identify a useful object-centered link that remains valid without asserting envelope identity or shared occasion, and show that the link contributes more than source/row count. If the reviewer needs an unstated object identity, depositor, Sella connection, or common Bell-7 event to make it meaningful, no-go. No checker output, fixture result, or preserved-regression result is asserted here.

## Axis assessment

- **Depth:** not demonstrated; at most a candidate narrow object-presence comparison, contingent on the falsifiable review above.
- **Calibration:** unchanged in any proposed artifact; uncertainty bounds are necessary constraints, not a calibration gain.
- **Coverage:** unchanged; this adds no demonstrated new checker-detectable case class.

Scope: report only. No fixture, checker, README, LOG, or commit changes.

# Round 35 critic — same-occasion identity and conflict

## Falsification finding

The proposed pair does not establish a semantic contradiction merely by assigning both events the same bell/tick and different places. The identity/occasion bridge is editorial: the shared label must denote one occasion, both reports must refer to that exact occasion (not merely the same bell recurring), and “I was at North Tower” must mean Sella was physically there throughout the relevant interval. A bell is a recurring signal, not a unique timestamp. Without explicit wording, an account could concern hearing the bell, being present before/after it, or a different ringing. Even with unambiguous prose, these remain two conflicting fictional reports—not independently established fact or proof either speaker is truthful.

## Evidence and precedent

- `.shokunin/lore/LOG.md`, Round 35 declaration, says the proposed events share a local tick and calls for a ledger pair on `place_id`; it also explicitly says the checker is structural and must not choose a winner. Thus same tick/pointers are not themselves semantic conflict evidence.
- `.shokunin/lore/LOG.md`, Round 33 declaration and “post-scout observation policy,” bounds Tarin’s source to “Tarin reports seeing Sella place” and requires tick 3 to be artificial local sequence metadata, not observed time. `.shokunin/lore/reports/r33-reviewer.md` confirms the excerpt “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk” is a report, with tick 3 arbitrary and not excerpt chronology. It contains no bell or occasion identity.
- `.shokunin/lore/LOG.md`, Round 34 declaration and closure, treats “heard that” as hearsay, and explicitly distinguishes source modality from the unchanged event record. `.shokunin/lore/reports/r34-reviewer.md` says r34 does not support direct-sight fields, while not proving them false. This cautions against upgrading Tarin’s report or metadata into a verified event.
- `.shokunin/lore/reports/r3-critic.md` observes that a nonempty ledger `why` is arbitrary free text and does not prove incompatibility; `.shokunin/lore/reports/r3-reviewer.md` likewise limits successful ledger validation to structural pointers/citations, not semantic truth or entailment. A two-sided `place_id` ledger cannot cure an ambiguous occasion.
- `.shokunin/lore/corpus/fixtures/r33-tarin-envelope/timeline.json` gives Tarin event `tick: 3`, `place_id: harbor`; `.shokunin/lore/corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md` has no bell/time phrase. Those concrete rows do not supply the proposed shared-occasion bridge.

## Risks / limits

1. **Repeated signal:** “the same bell” can identify a bell object, not a unique ringing. A reused bell-time label can collapse distinct occasions.
2. **Temporal scope:** Sella could be at the tower at the instant of a bell while Tarin's placement occurs later during the same broad bell period, or vice versa. A point event and a presence interval are not necessarily mutually exclusive absent precise bounds.
3. **Modality and attribution:** Tarin’s first-person text reports seeing the placement; it does not independently verify it. Sella’s account is also authored testimony, not an authoritative location fact. The records can conflict as reports without either being canonically true.
4. **Identity/role:** Aligning “Sella” to `sella`, Tarin to `tarin`, “North Tower” to `tower`, and harbor to `harbor` is fixture-local editorial mapping, as r33 reviewer noted; it does not validate real-world identity or shared occasion.
5. **Tick/ledger overclaim:** Structural acceptance of equal ticks, valid `place_id` pointers, and nonempty `why` establishes neither that tick means a bell nor that records refer to the same unique instant. It cannot decide which report wins.

## Falsifiable check

A non-author reviewer should test the exact prose, not infer meaning from JSON: require both excerpts to name the same *single identified ringing* (for example, a unique bell occurrence explicitly labeled “Bell-7,” with that label defined only as a shared occasion) and state contemporaneous location without interval ambiguity: Tarin explicitly reports seeing Sella place the envelope at Lantern Harbor during Bell-7; Sella explicitly says she herself was physically at North Tower throughout Bell-7 and did not go to Lantern Harbor during it. Check the clause map against each phrase and verify both ledger pointers target these precise `place_id` assertions. Then ask whether the text allows both reports to be accurate under the stated same-occasion/identity assumptions. If any timing/identity link is inferred only from a matching `tick`, generic bell name, or ledger `why`, classify semantic incompatibility as unproven. Preserve both accounts as conflicting reports; do not infer a canon winner, envelope contents, Blue Seal/carbon/route-strip association, or any Blue Seal inference. This check tests compatibility of the authored claims, not truth of either source.

## Conclusion

The round can add a useful paired-report case only if unique occasion and contemporaneous physical presence are explicit in authored prose and independently reviewed. As proposed, common bell/tick plus contrary places risks mistaking co-occurrence metadata for semantic identity. Even a successful exact-wording review warrants only “these two attributed reports conflict under their explicit shared-occasion assumptions,” not truth, canon, or a winner.

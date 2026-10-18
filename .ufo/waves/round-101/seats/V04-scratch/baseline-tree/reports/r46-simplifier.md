# Round 46 simplifier — tentative person identification

## Smallest bounded test

If the candidate proceeds, clone `r43-jorin-vela-sighting` and alter only the identification clause in Jorin’s excerpt: “I saw someone I took to be Vela standing on the Lantern Harbor east steps during what I called Bell-7.” Keep all five JSON tables and inherited maps byte-identical; do not add records. The exact r43 excerpt currently says “I saw Vela standing on the Lantern Harbor east steps during what I called Bell-7” (`.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/jorin-note-excerpt.md:1`). The unchanged entity claim explicitly says Jorin reports “seeing Vela” (`.../entities.json:87-95`), and the event likewise says he reports “seeing Vela” (`.../timeline.json:50-56`); the source is expressly newly authored, unverified, and not omniscient (`.../sources.json:33-36`).

The changed sentence tentatively identifies the person Jorin says he saw; it does not directly identify that person as Vela. The fixed JSON may be logically compatible if the person was Vela, but it overstates what this excerpt directly identifies. That is a source-to-record fidelity contrast, not proof that the JSON is false or that the person was not Vela. The unchanged event/map must not be treated as establishing Vela’s position or a shared Bell-7 occasion.

## Novelty risk and no-go

This is a serious novelty challenge, not a cleanly new class: r41 already contrasted tentative versus direct identification, albeit of the bell’s source rather than the person (`.shokunin/lore/reports/r41-strength-scout.md`, “Novelty and precedent”). R34 separately tested direct sight versus “heard that” hearsay (`.shokunin/lore/reports/r34-simplifier.md`, “Minimum fixture-only proposal”). A person referent is a meaningful difference from an auditory source, but the underlying move remains changing epistemic strength while retaining a stronger compatible JSON claim. Merely reversing r41’s direction is not novelty. Recommend **no-go absent independent evidence that reviewers reliably recognize the person-identity distinction as materially different and useful**, rather than repeating confidence/modality calibration.

## Falsifiable go/no-go

Before any fixture edit, show independent reviewers the exact proposed excerpt alongside the unchanged Jorin claim/event. Go only if they consistently distinguish (1) the tentative identification “someone I took to be Vela” from direct identification of Vela, and (2) logical compatibility of the fixed JSON from evidentiary support: it may fit if the person was Vela, but the altered excerpt alone does not directly identify them as Vela. They must not infer an objectively non-Vela person, a shared occasion, or canon. If reviewers call the JSON necessarily false, treat it as directly identified Vela, infer common Bell-7 occurrence, or cannot articulate a useful distinction from r41’s confidence contrast, no-go. Any admitted calibration claim is limited to source-to-record direct-identification fidelity; depth and coverage remain unchanged.

Scope: report only; no fixture, checker, README, LOG, or commit changes.

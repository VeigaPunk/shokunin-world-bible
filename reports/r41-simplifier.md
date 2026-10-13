# Round 41 simplifier — epistemic-strength calibration

## Minimal fixture and map

Use a separate r40-derived fixture. Preserve all five JSON tables and every inherited artifact byte-for-byte; change only the new Vela excerpt's auditory clause from “heard two strokes I took to be the registry bell” to “heard the registry bell strike twice.” Add one short editorial contrast map. This is a one-clause prose-only minimal pair, not a checker change.

Evidence: the baseline Vela excerpt contains the tentative phrasing and unchanged non-sighting (`.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md:1`); its map distinguishes hearing from her tentative identification and limits the inference (`.../vela-clause-map.md:7-13`). The fixed character claim says she heard strokes “she took to be” the bell (`.../entities.json:66-75`); the event repeats that weaker formulation (`.../timeline.json:39-48`). Map the new direct wording to Vela's stronger attributed identification, then explicitly state it still reports her experience and does not prove an objective bell/source. Note the unchanged claim/event now paraphrase more weakly than the excerpt; they are not necessarily logically incompatible, because hearing the bell strike twice entails hearing two strokes she could take to be the bell. The contrast tests fidelity/calibration of strength, not truth or contradiction.

## Risks and bounds

Novelty over r34 (saw vs heard-that) and r36 (different explicit dates) is narrow: a direct-vs-tentative identification distinction within one sensory report. It may be too subtle to demonstrate useful calibration, and a reviewer could reasonably find the fixed weaker JSON compatible rather than a genuine mismatch. Do not call it a contradiction, false JSON, objective ringing, independent corroboration, or canon. The citation ID and structurally clean checker do not authenticate the account. Keep non-sighting, occasion/date and all other wording unchanged; do not infer Sella/envelope presence or absence.

## Falsifiable check

A non-author reviewer compares the exact changed clause with the unchanged claim/event and map. The candidate passes only if the reviewer can identify that the excerpt now asserts Vela's bell identification directly while the JSON records only her tentative identification, and explains why this is an epistemic-strength/fidelity difference yet remains logically compatible (not a contradiction). The reviewer must also reject inference to objective bell occurrence. If they find no meaningful distinction from r34/r36, cannot ground the strength distinction in the wording, or treat the JSON as proven false/incompatible, the calibration/novelty claim fails. Verify the sole inherited excerpt delta, exact preservation of JSON and all other inherited artifacts, and checker output as structural-only; no broader regression claim absent replay evidence.

Scope: report only; no fixture, checker, README, LOG, or commit changes.

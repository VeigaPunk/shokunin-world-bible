# Round 50 source scout

## Verdict: conditional GO; modest incremental calibration

The proposed README correction addresses an active operator-facing instruction, not a new lore conclusion. Recommend only if it says current r41/r43 maps have been repaired and keeps the historical creation-time statements in their proper tense. This is distinct from r48: r48 corrected the two local maps but deliberately left the README unchanged; a reader following the present Round 43 guidance is still directed to disregard the actual, now-correct local map. A concise current-state note is justified, though the gain is narrow and not a new source distinction.

## Evidence and interpretation

- `.shokunin/lore/LOG.md:...` Round 50 declaration records the exact README instruction and proposed bounded change. In the corpus, `.shokunin/lore/corpus/fixtures/README.md:907-909` says the inherited r41 map “quotes the older r40 wording” and advises using the actual excerpt and strength map. That is stale as a present-tense description after r48.
- r40 remains the tentative control: `.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md:1` says Vela heard two strokes “I took to be the registry bell.” Its map retains this correct interpretation.
- r41 and r43 excerpts each directly say Vela “heard the registry bell strike twice” (`r41-vela-direct-bell/vela-note-excerpt.md:1`; `r43-jorin-vela-sighting/vela-note-excerpt.md:1`). Their current local maps quote that clause and preserve its attributed, unverified status (`.../vela-clause-map.md:3-12` in each directory). The maps explicitly distinguish source identification from proof of objective ringing.
- In both fixtures, `entities.json` Vela claim and `timeline.json` listening event still use “she took to be” (r41 entities around line 64, timeline around line 40; r43 corresponding Vela rows). The maps/strength maps characterize this as logically compatible but under-specific, not false; it must not be “fixed” or represented as a contradiction in this README-only scope.
- r41/r43 `strength-contrast-map.md:3-5` already explains the r40-to-r41 difference and fixed JSON limitation. Round 48 reviewer and adjudicator reports record that historical r41/r43 map byte-identity/staleness statements were accurate at creation, while current map bytes now intentionally differ. README wording must not retroactively invalidate those historical snapshots.

## Risks / falsifiable test

**GO** only for replacing the active Round 43 stale instruction with a short current-state pointer: r41/r43 maps now quote their local excerpts after r48; historical reports describe creation-time state; the strength contrast remains the r40/r41 comparison. Keep the r40 tentative map, excerpts, JSON, maps, and historical reports untouched. No claims about a real bell, shared Bell-7 chronology, objective timing, canon, source authenticity, rights, or permissions.

**NO-GO** if the edit leaves the operator directed to distrust the current maps, rewrites historical reports as though their creation-time observation was false, labels the weaker JSON interpretation false/contradictory, or implies the maps authenticate ringing. Materiality falsifier: if the proposed README wording merely repeats general cautions without correcting the explicit stale current instruction, it adds no calibration.

This is a single-document, operator-guidance correction that may modestly reduce misdirection beyond r48. It is not an independent new calibration discovery, depth gain, coverage gain, or objective-lore change. Source scout did not edit corpus, fixtures, README, LOG, or commit.

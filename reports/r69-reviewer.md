# Round 69 independent reviewer — broad same-reference validity gate

## Verdict

**NO-GO for the declared broad gate.** The proposed rule would suppress the same-reference finding whenever either side fails the combined event-ID-and-field validity test. That includes the clearly weak empty-both case, but also the committed R62 case where both sides share a valid, nonempty event ID and only their fields are invalid. The latter warning can independently guide repair: correcting both fields to the same allowed value would leave a duplicate reference, so the editor would still need to change one side. No evidence shows that losing this hint is harmless or outweighed by the empty-both calibration gain. Do not implement the declared broad rule on this round’s evidence.

This does not establish that the pair warning is useful in every malformed case. It establishes that the declaration’s single broad gate merges materially different cases and has not shown no harm. A narrower future proposal separating missing/unusable event IDs from valid shared IDs with invalid fields would need a fresh declaration and its own controls; that is not an in-round reframe.

## Independent probes and exact evidence

I ran the active checker on scratch copies of `.shokunin/lore/corpus/fixtures/r37-ledger-unique`, changing only the first row’s `claim_a`/`claim_b` objects. The temporary scratch directory was outside the repository and removed. Commands used the active `.shokunin/lore/corpus/fixtures/check_bible.py`; all captured stderr was empty.

- **Empty-both:** both side objects `{}`; exit 1. Output contains `claim_a.event_id: required nonempty string`, `claim_b.event_id: required nonempty string`, and `claim_a and claim_b references must differ` (3 violations). The extra pair finding compares two absent `.get()` values and does not identify a usable reference. This is the broad gate’s clearest calibration case.
- **Valid-identical:** both sides use `tarin-envelope-observation/place_id`; exit 1 with `claim_a and claim_b references must differ` (1 violation). The positive finding must remain.
- **Valid-different:** `tarin-envelope-observation/place_id` versus `sella-bell7-presence/place_id`; exit 0, `CLEAN: schema, citations, relations, timeline; 0 violations`. No pair finding is appropriate.
- **R62 malformed-field control:** replayed `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r62-malformed-side`; exit 1, 4 violations: the malformed timeline load error, each side’s `field: expected one of ['depends_on', 'place_id', 'tick']`, and `claim_a and claim_b references must differ`. Its `.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json` has the same valid event ID `tarin-envelope-observation` on both sides and `bogus` as both fields. A gate requiring both fields valid drops the pair finding here. If an editor repairs each field to the same allowed field, the duplicate-reference problem remains; the existing message can prevent that incomplete repair.

The probes support the code-path description in `.shokunin/lore/corpus/fixtures/check_bible.py:111-143`: side-local validation accepts only a nonempty string event ID and one of `place_id`, `tick`, `depends_on`, while the final comparison unconditionally compares `.get()` values for two dictionaries. They demonstrate a real empty-both false-positive-like output and a concrete potential loss of repair information on R62. They are not a user repair study and do not settle every malformed shape.

## Scout and declaration assessment

I reviewed all eight reports: `r69-ledger-scout.md`, `r69-prior-scout.md`, `r69-fixture-scout.md`, `r69-schema-scout.md`, `r69-critic.md`, `r69-simplifier.md`, `r69-scribe.md`, and `r69-regression-scout.md`. The ledger/schema/simplifier reports accurately map the separate local checks and propose the intended structural—not timeline-resolvability—gate. The prior report correctly treats R62 as direct behavior precedent but not proof of intended utility. The critic identifies the central harm precisely: R62 has valid equal IDs despite invalid fields, and the finding can warn against an incomplete repair. Fixture and regression scouts correctly note that the required four-way controls are incomplete in committed fixtures and that R62 is the one currently observed same-reference fixture. Scribe appropriately limits all claims to supplied ledger structure.

The declaration requires matched malformed-both, malformed-one, valid-identical, and valid-different controls, and inspection of all 130 old fixture tuples. The scratch probes cover empty-both, valid-identical, and valid-different; R62 provides the existing invalid-field case. They do not provide a matched malformed-one experiment or an independent repair-value measurement. More importantly, the broad rule’s known R62 delta is already a credible risk, not an unexamined hypothetical. The 130-case baseline inventory in `r69-regression-scout.md` identifies R62 as the sole existing same-reference finding; it is baseline inventory, not candidate validation. Since the candidate is rejected, I did not edit or rerun fixtures, checker, or corpus, and make no candidate-preservation claim.

## Axis limits

- **Calibration: NO-GO / improvement unproved, with a concrete harm risk.** Empty dictionaries receive an unsupported pair-level finding, but suppressing every malformed-side pair also removes the R62 hint despite shared usable IDs. No net material improvement is demonstrated.
- **Depth: unchanged.** The proposal changes a validity condition on an existing input-ledger check; it adds no new analysis. No depth gain or loss is evidenced.
- **Coverage: unchanged/unmeasured.** No checker or fixtures changed. Existing valid-identical and valid-different behavior is observed in focused probes, but there is no candidate suite or full old/new raw tuple comparison. No coverage improvement or preservation claim follows.

These are input-ledger diagnostics only. Nothing here establishes a story contradiction, event occurrence, source-text support, canon, chronology, rights, or game mechanics. No source prose was inspected. I changed no checker, fixture, README, LOG, or other file; this report is the sole write.

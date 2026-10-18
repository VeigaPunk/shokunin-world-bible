# Round 68 fixture scout — matched dependency cases

## Existing evidence and candidate controls

The active checker is `.shokunin/lore/corpus/fixtures/check_bible.py`. In its timeline dependency loop, it first diagnoses non-strings (`expected event-id strings`), then treats every string as an ID: self/repeat checks and `event_id_counts.get(dep, 0)`, with count zero reported as `unknown event {dep!r}`. There is no `.strip()`/nonempty check on dependency strings. Thus `""` and whitespace-only strings currently fall through to the same unknown-event branch as ordinary nonempty missing IDs. This is a statement about the active input/checker logic, not about any fictional event.

Useful existing matched-data starting points:

- `.shokunin/lore/corpus/fixtures/r22-valid-order/` has the standard five JSON inputs and a valid dependency `r20-prereq` from the dependent row. It is a clean positive control; current CLI prints `CLEAN: schema, citations, relations, timeline; 0 violations`.
- `.shokunin/lore/corpus/fixtures/r20-valid-order/` supplies the same standard world with an ordinary dependency and earlier prerequisite. `.shokunin/lore/corpus/fixtures/r20-valid-inversion/` and `r20-valid-equal/` retain valid nonempty IDs while exercising inversion/equal-tick behavior. They can check these behaviors remain distinct from blank-ID handling.
- `.shokunin/lore/corpus/fixtures/r22-unknown-mixed/` has `depends_on: ["missing", null]`; current CLI reports both `expected event-id strings` and `unknown event 'missing'`. This is evidence for the non-string plus nonempty-unknown diagnoses, but is **not** a clean sole-unknown control because of the `null` confound.
- `.shokunin/lore/corpus/fixtures/r22-self-repeated/` exercises self and repeated references (plus a null/non-string and resulting inversion). It is a regression source for preserving self/repeat behavior, though not a minimal control.
- `.shokunin/lore/corpus/fixtures/r22-malformed-only/` has a null dependency and reports the event-id-strings type diagnostic; it can guard that the proposed blank-string check does not replace type checking.

The fixture README `.shokunin/lore/corpus/fixtures/README.md` describes dependencies as event IDs that must have strictly earlier ticks. Fixture descriptions in the cited r20/r22 timelines explicitly say they are fixture input and do not assert source-text chronology.

## Recommended matched design (design only; no fixture files created)

Use a clean shared base, preferably the five files in `r22-valid-order`, and vary only the dependent row's `timeline[1].depends_on` value. Make each case a distinct copy for CLI invocation, with all other JSON bytes held constant:

1. **Valid nonempty known ID**: existing `r22-valid-order` (`["r20-prereq"]`) — expected clean; protects accepted dependency behavior.
2. **Empty string**: `depends_on: [""]` — current checker is expected to say `timeline[1].depends_on: unknown event ''`; candidate behavior should instead give a dependency-index/field-local required-nonempty-string diagnostic, not an event-absence claim.
3. **Whitespace-only string**: `depends_on: ["   "]` — current checker is expected to say `unknown event '   '`; candidate should give the same structural required-nonempty diagnosis as empty.
4. **Nonempty unknown ID**: `depends_on: ["missing"]` — should continue to report `unknown event 'missing'`, demonstrating the meaningful distinction from the two malformed strings. Derive this isolated control by changing only the value in the valid base; `r22-unknown-mixed` itself is not isolated.
5. **Existing dependency anomalies**: preserve/use r20 inversion and equal tick controls plus r22 self/repeated and malformed controls above. They test no change to inversion, self, repeated, or non-string behavior. They are supplemental regression controls, not matched blank-vs-unknown pairs.

For strongest comparability, make blank, whitespace, and nonempty-unknown siblings from the exact same valid base rather than use r20/r22 variants with unrelated timeline differences. Compare exact stdout and exit status; also check stderr and that only the targeted `depends_on` JSON value differs. Retain the clean-known dependency control and run the existing prior CLI fixture set before accepting any diagnostic change. The relevant assertion is classifier/output behavior on these input values, not source text or fictional-world truth.

## Limitations

No existing fixture directory found in the inspected fixture listing targets an empty or whitespace-only dependency string. The suggested cases are a design, not executed fixtures or verified candidate outputs. The current checker behavior for those values is inferred directly from the quoted control flow; no scratch files or fixture variants were created. Existing `r22-unknown-mixed` and `r22-self-repeated` contain extra conditions, so neither alone establishes a clean matched contrast. This scout makes no claim about whether the proposed diagnostic is materially useful, whether the change is safe beyond these controls, or about source text, canon, rights, chronology, or game mechanics.

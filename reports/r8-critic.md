# Round 8 critic — falsification of dependency-list rule

## Observed evidence

- In `.shokunin/lore/corpus/fixtures/check_bible.py`, `events = index('timeline')` is a dictionary keyed by event ID. The timeline loop visits each `depends_on` entry independently: unknown IDs get an `unknown event` finding, and known dependencies with `events[dep]['tick'] >= row['tick']` get `timeline inversion`.
- `.shokunin/lore/corpus/fixtures/consistent/timeline.json` has `arrival` at tick 2 depending once on `departure` at tick 1. Replacing that list with `["departure", "departure"]` in a temporary copy of the fixture still returned clean under the current checker. This supports one genuinely unhandled case: repeated entries for an otherwise earlier prerequisite.
- Replacing `arrival.depends_on` with `["arrival"]` in a temporary copy produced `timeline inversion 'arrival' tick 2 not before 'arrival' tick 2`. Thus, under the observed unique-ID case, self-dependency already fails existing validation. A new self-dependency message would relabel/duplicate a detected failure, not add a newly detected invalid input.
- A temporary probe with `arrival.depends_on: ["later", "later"]` and a unique `later` event at tick 3 produced the same `timeline inversion` twice, once per occurrence. So a duplicate-list finding added without care would be a third report about the same repeated inverted edge; duplicate list entries can amplify existing diagnostics.
- `.shokunin/lore/corpus/fixtures/contradictions/timeline.json` already includes `arrival -> later` where `later` is tick 3 and `arrival` tick 2; it is an inversion control, not evidence that a separate self-list rule is needed. `.shokunin/lore/fixtures/README.md` is not the path; the actual relevant documentation is `.shokunin/lore/corpus/fixtures/README.md`, which specifies strictly earlier ticks and editorial review, not list uniqueness or causal truth.

## Falsification / calibration limits

The bundled claim treats self and duplicate dependencies as a single new rule class, but their evidence differs. Self is already rejected as an equal-tick inversion. Duplicate membership is currently unreported when its prerequisite is earlier, but the evidence only establishes repeated input tokens, not that repetition is a canon inconsistency or that dependencies are mathematically a set. The checker may reasonably adopt a local input-convention rule, but should call it that and not imply causal-cycle detection or source-backed error.

The proposed claim that both anomalies yield relation-local diagnostics is not enough to guarantee low noise. A duplicate of a future prerequisite currently generates repeated identical inversions; adding a duplicate diagnostic can cascade. A self edge could yield both a new self diagnostic and the existing inversion. Unknown repeated IDs may likewise produce repeated unknown-event messages. These are observed consequences of the per-entry loop and should be made explicit in any expected-output matrix.

## Recommendations (separate from observations)

1. Narrow the coverage claim to **duplicate prerequisite IDs within one event's list**; do not count self-dependency as a new detected class. If retaining a self-specific diagnostic for clarity, define how it interacts with the already observed equal-tick inversion so it does not create redundant output, and report that as diagnostic refinement rather than coverage gain.
2. Decide explicitly whether `depends_on` is a set-like list convention. If it is, document the convention as input-list integrity, not a claim that repeated dependencies are false in-world.
3. Keep duplicate detection orthogonal to lookup/tick checks. Avoid emitting one identical unknown/inversion finding per duplicate occurrence, or explicitly accept and fixture that multiplicity. Do not silently remove entries.
4. Test separate cases: unique earlier duplicate (isolates new detection), self-only (shows overlap with inversion), duplicate future (tests cascade/noise), and duplicate unknown (tests repeated unknown diagnostics). Preserve old outcomes outside deliberate expected changes.
5. Keep source validation separate: an event's unique `source_id` establishes ID resolution only. It does not attest that the source supports a dependency edge; see `.shokunin/lore/reports/r8-citation-scout.md` for the observed citation boundary.

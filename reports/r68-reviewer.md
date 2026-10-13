# Round 68 independent reviewer — blank dependency IDs

## Verdict: NO-GO on the claimed calibration move

The checker has a real schema inconsistency: `timeline[*].depends_on` members must be strings, but blank strings are not rejected as nonempty fields. I find the distinction plausible as input taxonomy, but not materially different in repair action on the evidence available. Both a blank dependency and a nonempty unknown dependency require the operator to supply a usable reference to an intended timeline event (or otherwise repair the supplied timeline data). The current field-local `unknown event ''` already identifies the exact dependency field, exposes the blank value, and says it has no match in the checker’s event index. Replacing that with “required nonempty event ID” more accurately classifies the defect, but does not demonstrate a new action the old output failed to support. No operator evidence shows that the existing message led to a different or blocked repair. Under the Round 68 declaration’s own falsifier (“reviewer finds no material distinction”), I reject this move as wording/taxonomy refinement rather than demonstrated calibration improvement.

This is distinct from Round 67’s admitted case. There, a global `sources.json` load failure was identical for empty and nonempty claim IDs and could not reveal the second blank-field defect; the claim-local finding exposed an independently hidden repair. Here the old unknown-event finding is already dependency-local and directly reports the blank member as unmatched. The r67 precedent supports validating required fields consistently, but does not by itself establish equal materiality here.

## Independent probes and prior controls

I reviewed the Round 68 declaration/synthesis in `.shokunin/lore/LOG.md`, all eight reports `r68-{dependency,prior,fixture,schema}-scout.md`, `r68-critic.md`, `r68-simplifier.md`, `r68-scribe.md`, `r68-regression-scout.md`, the active checker, Round 67 reviewer report, and Round 20/22 controls. No r68 candidate exists; this is a baseline-only review.

I copied `corpus/fixtures/r22-valid-order/` to temporary directories, changed only `timeline[1].depends_on` to the single value shown, then ran each with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-copy>
```

Observed stdout and exit status:

| Value | Output | Exit |
|---|---|---:|
| `""` | `VIOLATION: timeline[1].depends_on: unknown event ''` then `1 violation(s); no canon changed` | 1 |
| `"   "` | `VIOLATION: timeline[1].depends_on: unknown event '   '` then `1 violation(s); no canon changed` | 1 |
| `"ghost"` | `VIOLATION: timeline[1].depends_on: unknown event 'ghost'` then `1 violation(s); no canon changed` | 1 |
| `"r20-prereq"` | `CLEAN: schema, citations, relations, timeline; 0 violations` | 0 |

These matched probes confirm that the current checker reports the blank member rather than silently accepting it. They do not show the proposed output or user repair behavior. Focused existing commands and outputs also confirm nearby semantics: `r20-valid-order` and `r22-valid-order` exit 0 CLEAN; `r20-valid-inversion` exits 1 with `timeline[1].depends_on: timeline inversion 'r20-prereq' tick 2 not before 'r20-dependent' tick 1`; `r22-malformed-only` exits 1 with `expected event-id strings`; `r22-unknown-mixed` exits 1 with that finding plus `unknown event 'missing'`; and `r22-self-repeated` exits 1 with type, self, inversion, and repeat findings (five total). This supports that r20 covers tick ordering, while r22 already processes string siblings and separately flags non-strings; neither establishes materiality of relabeling a blank string.

## Axes, risks, and bounds

- **Calibration: not improved / NO-GO.** A required-nonempty diagnostic would be more structurally precise, but no distinct repair action is established over the existing exact-field unknown-ID finding. The critic’s NO-GO argument is persuasive and remains unanswered by matched output differences alone.
- **Depth: unchanged.** Neither baseline nor proposed validation adds source content or lore. No evidence supports a depth claim.
- **Coverage: unchanged, not a fallback gain.** This is an input validation refinement within an already checked dependency member, not evidence of broader timeline consistency coverage. Do not relabel a rejected calibration claim as coverage improvement.

If a future candidate is nevertheless considered, the narrow guard suggested by the simplifier should run per string member and continue before self/repeat/membership/order checks. A candidate needs an explicit policy for repeated blank values (current behavior can report unknown and repeated), plus empty, whitespace, nonempty-unknown, known, self/repeat, and full baseline tuple comparisons. Emitting both required-nonempty and unknown for one blank member risks redundant noise; suppressing unknown discards a true statement about the supplied index, so either choice should be described as diagnostic replacement/addition, not newly discovered event absence. Keep `depends_on: []` valid. The diagnostics must remain about supplied JSON/index results, not fictional event truth, source-text support, chronology, canon, rights, or game mechanics.

No checker, fixture, README, or other file was changed by this review. No candidate replay or full regression replay was possible because the round is provisionally NO-GO and has no candidate. This report makes no source, canon, or rights conclusion.

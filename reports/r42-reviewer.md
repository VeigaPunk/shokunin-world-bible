# Round 42 independent reviewer — description selector

## Verdict: no-go; no material calibration gain

The proposed negative changes only `claim_a.field` from `place_id` to `description`. This is an unbuilt design, not an observed test: Round 42 LOG explicitly says no r42 fixture exists and the negative remains a design (`.shokunin/lore/LOG.md:700-701,705`). I did not execute a candidate fixture. Thus there is no r42 exit code or diagnostic to report.

The prior executed evidence directly covers unsupported-selector rejection. The r3 reviewer says temporary copies tested an unsupported field; each exited 1 with a diagnostic and no crash (`.shokunin/lore/reports/r3-reviewer.md:7`). It characterizes the checker as validating structural pointers/citations, not semantic truth or entailment, and says `why` is checked only for nonempty text (`r3-reviewer.md:15-21`). This is not merely a prior statement of intent: it is a recorded executed probe. The exact unsupported token/output is not preserved in that report, so it cannot establish that `description` itself was tested; nevertheless the candidate asks about the same allowlist failure class, and offers no distinct measured human decision criterion.

The structural-versus-semantic boundary is independently explicit in the r3-era fixture README: allowed selectors are `place_id`, `tick`, and `depends_on`; the event's own source is the citation, no source text/paraphrase is copied, and validation does not prove citation truth or whether `why` explains a semantic contradiction (`.shokunin/lore/corpus/fixtures/README.md:48-54`). The checker schema includes timeline `description` (`check_bible.py:12-14`), but its ledger allowlist is limited to the three structured fields (`check_bible.py:76-90`). Invalid fields short-circuit before event lookup and source resolution (`check_bible.py:89-100`). Therefore the proposed `description` value demonstrates only that a real timeline field can still be an unsupported ledger selector; it does not add a new boundary to the already documented and probed unsupported-field class.

Round 35's ledger example is also a positive instance of structured `place_id` references, not copied prose (`.shokunin/lore/reports/r35-ledger-scout.md:5-8`). It cautions that pointer shape/targets do not establish semantic warrant (`r35-ledger-scout.md:11-14`). This further weakens any claim that the prose-vs-selector lesson is newly calibrated.

## Axis assessment and risks

- **Calibration: unchanged.** The candidate could make the existing selector rule more concrete or easier to audit, but no evidence shows a changed prediction or decision beyond r3's already recorded unsupported-field rejection and structural/non-semantic explanation.
- **Coverage: unchanged.** The unsupported-field branch was already exercised in r3. A new spelling/fixture would not establish a new checker class.
- **Depth: unchanged.** No checker, lore representation, source-text validation, or semantic interpretation is added.

A persisted negative might improve discoverability or regression documentation, but those are not demonstrated axis improvements under the declared calibration claim. Counting it as a new calibration gain risks relabeling repetition as novelty. Conversely, the no-go does not imply event descriptions are false, forbidden, or useless to a human reader. The checker only disallows them as ledger selectors; it does not assess their meaning, source support, `why`, contradiction truth, or canon. Do not infer rights or AI-training permission from these fictional citations; those are separate questions (r35 ledger-scout, lines 12-14).

**Recommendation: no-go / reject this calibration candidate; do not build the fixture pair or claim a pass.** Reconsider only if a future proposal names a distinct, independently observable calibration decision not already captured by r3's unsupported-field probe and README boundary. No r42 candidate fixture was executed for this review.

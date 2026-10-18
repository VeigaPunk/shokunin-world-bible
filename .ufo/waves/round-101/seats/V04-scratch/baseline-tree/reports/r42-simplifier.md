# Round 42 simplifier — no-go on calibration fixture

## Recommendation

**No-go: do not build the proposed fixture pair.** The sole proposed mutation (`claim_a.field: place_id` → `description`) is already covered by the executed r3 unsupported-field probe. The r3 reviewer records a temporary ledger test of an unsupported field and a diagnostic without crash at `reports/r3-reviewer.md:15`; its summary explicitly says unsupported selectors are checked before event dereference (`reports/r3-reviewer.md:19`). The primary checker shows the branch is field allowlisting, followed by event/source resolution only for allowed fields (`corpus/fixtures/check_bible.py:76-100`). Thus the proposed failure is a repeat of known structural behavior, not new calibration evidence.

The proposed interpretive distinction is also already stated: README says selectors are only `place_id`, `tick`, `depends_on` (`corpus/fixtures/README.md:48-52`), and cautions that validation does not decide whether `why` accurately describes a semantic contradiction (`README.md:53-54`). R3 reviewer likewise says the checker validates pointers and required text, not semantic truth or whether a source supports an event (`reports/r3-reviewer.md:21`). A table contrasting `description` prose with selectors would restate these boundaries; it would not demonstrate a new human calibration outcome.

R35 provides the relevant positive example: its ledger points to Tarin and Sella `place_id` fields and frames the accounts conditionally (`reports/r35-simplifier.md:7,13`). Its falsifiable check already asks a reviewer to inspect exact wording and pointers without choosing a winner (`reports/r35-simplifier.md:15-17`). A second negative fixture would add an invalid-pointer result, but no distinct semantic judgment beyond this established structural-versus-human-reading boundary.

## Risks

- Re-running an already executed unsupported-field probe risks overstating novelty as calibration improvement.
- `description` is timeline prose, but its exclusion from ledger selectors does not make the prose false, unusable by a human, or canonically invalid. The checker only rejects it as a selector; it cannot establish what the prose means (`check_bible.py:76-100`; `README.md:53-54`).
- No inference about which Bell-7 report is true, whether the accounts conflict, or whether either should be canon follows from a selector diagnostic. Keep both attributed accounts unresolved as in the r35 boundary (`reports/r35-simplifier.md:13`).
- This is a no-go recommendation, not evidence that all possible calibration work is exhausted. It is specifically a rejection of this proposed one-field pair as non-novel.

## Falsifiable check for reconsideration

Before any implementation, a non-author reviewer should inspect the proposed one-field pair against `reports/r3-reviewer.md:15,19,21`, `corpus/fixtures/README.md:48-54`, and `check_bible.py:76-100`. Reconsider only if the reviewer can state a concrete, previously untested human decision that distinguishes the proposed `description` case from the r3 unsupported-field probe and the already documented prose/selector boundary, and can specify mutually exclusive pass/fail outcomes without treating checker output as semantic evidence. If the reviewer cannot do so, retain no-go and do not create fixtures. Any future accepted test must still leave source truth and canon undecided.

Scope: recommendation only; no fixture, checker, README, LOG, or commit changes.

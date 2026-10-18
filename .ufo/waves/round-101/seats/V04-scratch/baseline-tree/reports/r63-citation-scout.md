# Round 63 — citation-scout: non-finite JSON tokens

## Judgment

**NO-GO on material calibration from the citation/source-truth and rights boundary.** The observed `NaN` acceptance is a parser/input-validity issue. It does not test whether a cited source supports a claim, whether an account is true, or whether any fictional event occurred. I found no evidence that this parser behavior changes a source-truth, chronology, canon, or rights decision. A possible strict-JSON policy may merit separate format-owner review, but this scout does not establish material calibration or compatibility.

## Evidence and scope

- `.shokunin/lore/LOG.md` Round 63 declaration (2026-10-13T05:49:26Z) reports a temporary out-of-repository copy of `consistent/` with `extra: NaN` in `sources[0]`; current checker exited 0 CLEAN. The declaration explicitly labels this malformed-input acceptance, not a lore fact. I did not independently rerun that probe; it is observed per the round record, not my experiment.
- `.shokunin/lore/corpus/fixtures/check_bible.py:45-57` calls Python `json.loads` with `object_pairs_hook=unique_object`. That hook rejects repeated member names (lines 16-22), but no `parse_constant` hook is supplied. Python's JSON decoder therefore retains its non-finite-constant default; a value in an ignored extra property can pass the later required-field checks. The checker does not validate unknown object properties or source prose.
- The `NaN` example is not a duplicate-key case. R59's repeated-member rejection and the r5 malformed-JSON matrix do not by themselves specify a policy for Python's accepted non-finite extensions. `.shokunin/lore/reports/r59-citation-scout.md` carefully treats that earlier duplicate-member policy as a new input-format choice, not source evidence.

## Parser validity versus lore claims

At most, rejecting `NaN`, `Infinity`, or `-Infinity` would say that a supplied JSON file contains a token disallowed by the chosen strict-input policy, and the file cannot be assessed under that policy. It cannot establish which value an author intended, that a source ID is authentic, that source text supports a statement, that a reported event happened, or that an event's chronology is true. A clean parse likewise does not authenticate sources or establish canon. Do not convert either outcome into a verdict on fictional-world truth, canon, real-world history, copyright ownership, licensing, permission, or other rights.

## Materiality, compatibility, and falsifier

The logged extra-member probe is a real parser-boundary concern, but the token sits in an unrecognized field and the checker has no documented strict-JSON producer contract in the evidence I reviewed. Rejecting a whole table could also trigger the existing unavailable-table behavior and downstream cascades (including source/entity/timeline membership and ledger checks). Whether the existing producer emits these constants, whether typed positions already fail, and what candidate outputs/cascades would be are unverified here. Do not describe those possibilities as observed.

A future GO would need a format/producer compatibility check and matched probes distinguishing ignored metadata, typed numeric fields, nested objects, and valid finite-number controls; report actual file-level and downstream output. A falsifier for my NO-GO would be evidence that a supported producer emits such tokens or that their acceptance creates a concrete, materially misleading checker decision, while a narrow rejection has bounded cascades and preserves finite JSON behavior. No such evidence is present in this citation review. **Recommendation: NO-GO from this axis; parser-format decision remains open.**

No checker, fixture, README, LOG, source text, or canon was changed by this scout.

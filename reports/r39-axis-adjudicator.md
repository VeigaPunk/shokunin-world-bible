# Round 39 — final non-author axis adjudication

**ADMIT the narrow coverage move.** The observed, uniquely identified ledger endpoint with **zero** matching source rows exercises a distinct input-status outcome from round 7's executed **ambiguous** (multiple matching rows) ledger endpoint and round 38's rejected repetition of that ambiguous outcome. This is an additional replayable case of existing checker behavior, not a new checker rule. One axis improves and none is harmed.

| Axis | Verdict | Basis |
| --- | --- | --- |
| Coverage | **Improved** | At `check_bible.py:64–66,92–100`, after exactly one event ID resolves, zero matching source IDs emits `contradictions[0].claim_b: event 'sella-bell7-presence' has no resolvable source_id`; multiple rows instead emit the `.source_id` ambiguity. The new negative directly observes the zero-source case and its timeline consumer with a one-field mutation; r7's executed probe and r38's archived pair observed only the multiple-row case. These are materially different input cardinalities and ledger diagnostics. |
| Depth | **Unchanged** | Both fixtures inherit the nine r35 files, with only one negative citation value changed. They add no source prose, account, semantic comparison, or evidence about Bell-7. The clean control retains r35's conditional manual comparison; the negative cannot structurally qualify its ledger B citation. |
| Calibration | **Unchanged** | Reports and fixture README separate a missing citation pointer from an absent or false authored excerpt, testimony truth, source support, and canon. This maintains, rather than newly extends, the existing boundary; no harmful inference is needed. |

## Independent evidence and replay

I read the r39 LOG declaration, go decision and pre-adjudication record; `reports/r7-reviewer.md:38,52` and `r7-source-scout.md`; the rejected `reports/r38-axis-adjudicator.md`; r35 adjudication and the r35/r39 fixture pair; the checker, fixture README, and r39 executor/reviewer/verifier/critic (including the critic's conflicting claims). I independently extracted `793a3a8863b9361ca89a514069f3a4c46f739ebd`'s checker and complete fixture tree outside the working tree with `git archive`. The archive contains **90 prior fixture directories** and **449 prior JSON paths**. From each root I ran the identical root-relative argv `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` with that root as cwd, capturing separate raw stdout and stderr bytes and exit status. **90/90 `(exit, stdout, stderr)` tuples match**; all **449/449** archived JSON path bytes equal their current counterparts. This preserves old observed behavior and bytes, not universal checker correctness.

Independently compared every r35, `r39-ledger-source-unique`, and `r39-ledger-source-missing` file: each has the same **nine** files, and the control is byte-identical to r35 throughout. The negative differs from the control only in `timeline.json`, in a single field at `timeline[3].source_id`: `sella-bell7-note` → `missing-sella-note`. `sources.json`, both excerpts, event IDs, and unchanged ledger endpoints are identical. Four timeline IDs are distinct; `claim_a` (`tarin-envelope-observation`) and `claim_b` (`sella-bell7-presence`) each resolve once. The negative's new citation has **zero** matching source rows; the original Sella source row remains present once, but the event no longer points to it.

Independent complete outputs from root-relative checker runs (stderr empty in both):

```text
r39-ledger-source-unique: exit 0
CLEAN: schema, citations, relations, timeline; 0 violations

r39-ledger-source-missing: exit 1
VIOLATION: contradictions[0].claim_b: event 'sella-bell7-presence' has no resolvable source_id
VIOLATION: timeline[3].source_id: unknown in-world source 'missing-sella-note'
2 violation(s); no canon changed
```

These are exactly **two** findings, not an unknown event ID or ambiguous source ID. The timeline finding is the expected second consumer of the same missing citation, not a second independent missing source. The fixture README accurately identifies this as zero-source versus duplicate-source input and cites the runnable commands.

## Prior-art decision and bounds

`r7-reviewer.md:38` **describes** the unknown-source branch; description/code inspection is not an executed probe. Its actual temporary ledger probe at line 52 **duplicated** `archive-ledger`, made `departure` cite it, and observed an **ambiguous** `claim_a.source_id` among seven findings, with no generic “no resolvable source” diagnostic. `r7-source-scout.md` also describes the then-existing absence check, rather than recording a zero-source ledger execution. R38 duplicated `sella-bell7-note`, independently observed `claim_b.source_id` ambiguity and a timeline ambiguity, and was rightly rejected because side choice/durable packaging did not distinguish its status from r7. R39 changes the status tested **from 2+ to 0**, and the side-local result changes to “event ... has no resolvable source_id.” That is the material coverage distinction, not the opposite side, Bell-7 story, or durable packaging by itself.

`r39-critic.md` initially asserts r7 *executed* an unknown-source ledger probe, but its own “Evidence and limits” and the cited primary `r7-reviewer.md:47–52` explicitly identify that executed probe as ambiguity, **not unknown**. I use the primary execution record rather than that unsupported assertion. A retained-report search and the cited scout review expose no earlier executed unique-event/zero-source ledger probe; this cannot rule out unrecorded private tests and does not mean this checker path was newly invented. The current checker routes unknown and ambiguous statuses through different diagnostics at `:97–100`; this verdict credits measured input-boundary coverage only.

The unresolved event citation does **not** delete Sella's authored fictional excerpt, make Sella's report false, prove Tarin's report, authenticate their shared-date claims, resolve their reported incompatibility, or choose canon. The checker reads JSON references, not excerpt truth. This admission is **not** a SHONEN checkmark, promotion, push, or merge.

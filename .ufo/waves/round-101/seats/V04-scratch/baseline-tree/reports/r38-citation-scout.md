# r38 citation scout — source citation is not truth, canon, or rights

## Boundary findings

- The proposed case preserves unique event identities (`r35-bell7-conflict/timeline.json:23-29,32-38`) while duplicating the source identifier `sella-bell7-note` in a separate source row. The ledger side B points to `sella-bell7-presence` (`r35-bell7-conflict/contradictions.json:8-11`); the event carries that source ID (`timeline.json:32-38`). A uniquely addressable event can therefore still have an ambiguous source citation.
- Checker logic distinguishes these identities: it counts source rows by ID (`check_bible.py:53-66`), requires exactly one timeline event for a ledger pointer (`:92-100`), then reports an ambiguous event source at the side-local `.source_id` path (`:95-100`). The duplicate source row also produces the general duplicate-ID diagnostic (`:45-50`). This tests the ledger's source-resolution branch, not source-text support.
- The cited material is explicitly framed as authored fictional reports, not omniscient truth (`r35-bell7-conflict/sources.json:15-24`). Tarin reports seeing Sella place an envelope (`tarin-note-excerpt.md:1-3`); Sella reports her own Tower presence and Harbor absence (`sella-bell7-note-excerpt.md:1-3`). The editorial map states that citation is structural attribution only and does not establish authenticity, text support, honesty, truth, or canon (`manual-clause-pointer-map.md:14-17,19-21`). An ambiguous source ID says neither account wins nor either account is false.
- Precedent limits novelty: r7 already exercised duplicate-source ambiguity on relation references and ledger source ambiguity in a different fixture (`reports/r7-reviewer.md`, “Reference-site inspection” and “Contradiction-ledger ambiguity probe”); r31 exercised a controlled non-alliance relation case (`reports/r31-reviewer.md`, “Prior round / novelty boundary”). The narrow new coverage claim is specifically duplicate source resolution for claim_b of the Bell-7 two-sided ledger while both event IDs stay unique—not general duplicate-source behavior.
- Rights are a separate question. Neither source ID, successful/failed structural validation, nor fictional excerpt establishes ownership, license, permission, consent, or entitlement to reproduce or train on the text. Make no rights determination from this test.

## Risks

1. Conflating unique event resolution with unique source resolution; the ledger endpoint can resolve while its cited source does not.
2. Treating “ambiguous” as discrediting Sella, validating Tarin, or selecting a canon winner. It establishes only multiple source rows for one ID and leaves the attribution unresolved.
3. Implying the checker verified that the source supports the timeline description or ledger rationale. It does not parse prose for support (`check_bible.py:64-74,92-100`).
4. Inferring rights or reuse permission from in-world citation metadata or checker status.

## Falsifiable check

Run the clean r35-derived control and the proposed source-duplicate negative with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`. Control should exit 0. Negative should exit nonzero and include `sources[4].id: duplicate sources id 'sella-bell7-note'` and `contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'`; `claim_a` should not have that ambiguity, and both event IDs should remain unique. Inventory the complete output rather than assuming no collateral findings. If the side-B ambiguity is absent, the claimed coverage is falsified. Either outcome is structural reference evidence only—not source support, truth, canon, authenticity, or rights.

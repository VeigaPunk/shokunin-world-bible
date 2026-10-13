# Round 37 simplifier — minimum ambiguous ledger endpoint fixture

## Minimal duplication

Use exactly two r35-derived fixture directories: a byte-for-byte copy as the unique-endpoint control, and one negative copy differing only by a second `timeline.json` row with ID `tarin-envelope-observation`. Keep the existing `bell7-location-reports` contradiction pair and every citation/source/excerpt unchanged. The r35 fixture already has the two endpoint events and one ledger row (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/timeline.json:12-29`; `contradictions.json:1-10`). Add no canon rows, claims, sources, or ledger records. In the negative, duplicate the event row rather than editing/removing/reassigning either original endpoint. This isolates multiplicity as the input delta; preserve both versions as data, not a selected winner.

The checker already counts IDs from all timeline rows, reports duplicate IDs during indexing, and requires each contradiction endpoint to resolve to exactly one event (`.shokunin/lore/corpus/fixtures/check_bible.py:46-50,58-62,76-95`). Therefore the negative should report the duplicate timeline ID plus the ledger-local exact-one failure for `claim_a`; `claim_b` remains uniquely resolvable. Do not add a new checker rule: this round is fixture coverage of existing behavior. r9 fixtures show duplicate IDs with no ledger (`r9-dup-low-high/timeline.json:1-30`, `contradictions.json:1`), so they do not cover this interaction. The unique r9 control confirms the precedent for a one-row ID (`r9-unique-control/timeline.json:1-20`).

## Risks and limits

This demonstrates an ambiguous ledger endpoint, not false testimony and not a canon resolution. The r35 notes remain attributed reports: their event descriptions identify Tarin’s report and Sella’s self-report for Bell-7 (`r35-bell7-conflict/timeline.json:12-29`), while the ledger itself explicitly leaves them unresolved and says the checker does not prove contradiction (`r35-bell7-conflict/contradictions.json:1-10`). A duplicate ID makes `claim_a` non-unique; it does not invalidate either prose account or establish which timeline row is authoritative. Avoid wording that calls the checker’s structural finding a factual contradiction.

A copied control and one-row duplication are sufficient; extra permutations or additional duplicated IDs add no coverage for the declared claim. The checker indexes duplicate IDs with last-row assignment (`check_bible.py:46-50`) but endpoint validation uses the count before dereferencing, so this probe should not depend on which duplicate row wins that map assignment (`check_bible.py:60-62,92-95`). Do not infer or report exact ancillary diagnostics without executing the fixture.

## Falsifiable check

Run `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>` on both new directories. The unique control must exit 0. The duplicated case must exit 1 and include both `timeline[4].id: duplicate timeline id 'tarin-envelope-observation'` and `contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'`; record all additional output rather than assuming it. Confirm the only JSON difference between control and negative is the added timeline row, and that all unchanged r35 source/citation payloads remain byte-identical. If the negative lacks the endpoint-local diagnostic, or the control is not clean, the claimed endpoint-ambiguity coverage fails. This check establishes structural resolution behavior only; it must not label either account false or choose a canon winner.

Scope: report only; no fixture, checker, LOG, README, or commit changes.

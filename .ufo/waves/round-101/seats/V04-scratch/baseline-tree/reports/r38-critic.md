# Round 38 critic — novelty and collateral ambiguity

## Novelty challenge

The broad condition is not novel: Round 7 already duplicated a source ID cited by a relation (`reports/r7-critic.md`, “Replayed…”; `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:9-12`, `sources.json:2-6,15-19`), and round 31 exercised source ambiguity on a non-alliance `carries` relation (`reports/r31-critic.md`, “Challenge to novelty”). Those precedents do not, however, exercise the present distinct path: a uniquely resolved contradiction-ledger event whose own `source_id` is ambiguous. The checker guards the event ID count at `check_bible.py:92-95`, then checks the resolved event’s source status and reports against the ledger side at `:96-100`. That is a plausible narrow coverage increment, not first duplicate-source ambiguity or first local ambiguity reporting in general.

## Collateral and inference risks

- Duplicating `sella-bell7-note` in `sources.json` should produce both the duplicate row finding from `index()` (`check_bible.py:45-56`) and any ambiguity diagnostics from every consumer of that ID, not just the ledger. Source validation runs for the Sella timeline row (`:242`) and for the ledger side (`:96-100`); enumerate the complete output. Do not assume an additional copied source row is otherwise inert if its content is malformed or changed.
- The reported path is ledger-side ambiguity, not a claim that Sella’s report is false or that Tarin wins. The Bell-7 ledger explicitly says reports are retained unresolved and this is not a checker-proven contradiction or canon verdict (`corpus/fixtures/r35-bell7-conflict/contradictions.json:1-22`). `sources.json` contains source metadata; it is not the cited prose itself (`r35-bell7-conflict/sources.json:1-29`).
- A unique event ID does not guarantee a unique source citation. Conversely, the duplicated source ID does not make the event ID ambiguous: checker keeps independent counts (`check_bible.py:53-66`, `:60-62`) and only follows the event after the exact-one guard (`:92-100`). Avoid conflating these two axes.
- The checker’s generic `source()` is called at multiple locations (`:68-74`, `:107-116`, `:123-130`, `:229-242`). A broader claim that all source references are now handled, or that duplicate rows’ metadata is semantically compared, is unsupported.

## Falsifiable check

Compare the proposed clean r35-derived control and negative bytewise: the negative should differ only by one copied `sources.json` row with ID `sella-bell7-note`; preserve event IDs and ledger rows. Run `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` on both and record full stdout/stderr/exit. Require clean control exit 0, both event IDs still unique, the duplicate source-ID finding, and the exact ledger-local `contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'` finding. Enumerate all collateral findings—especially the Sella timeline source diagnostic—and confirm `claim_a` remains unique with no matching ambiguity. If the ledger-side finding is absent, the coverage claim is falsified; if it appears, describe only the source-resolution diagnostic at a unique contradiction endpoint, not contradiction detection, provenance/authenticity, canon resolution, or generic duplicate-ID novelty. Prior r7/r31 evidence must remain acknowledged.

## Evidence

- Checker source index/count/status and source diagnostic: `.shokunin/lore/corpus/fixtures/check_bible.py:45-74`.
- Contradiction event exact-one guard and endpoint-source check: `.shokunin/lore/corpus/fixtures/check_bible.py:77-105`.
- Other source consumers, including timeline: `.shokunin/lore/corpus/fixtures/check_bible.py:107-116`, `:123-130`, `:229-242`.
- Prior duplicate source citation: `.shokunin/lore/reports/r7-critic.md`; `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:9-12`.
- Prior non-alliance relation ambiguity: `.shokunin/lore/reports/r31-critic.md`.
- Bell-7 citation and explicit non-canon scope: `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:1-22`; metadata rows: `sources.json:1-29`.
- Round-38 declared narrow novelty/baseline: `.shokunin/lore/LOG.md` under “Round 38 — 2026-10-13T02:21:43.604145+00:00”.

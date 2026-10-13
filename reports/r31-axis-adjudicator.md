# Round 31 — independent per-axis adjudication

**Verdict: admit the narrow coverage move.** Coverage improved; depth unchanged; calibration unchanged. At least one axis improved and none was harmed. This is a controlled non-alliance relation-citation input, not a new checker rule or the first ambiguous relation citation.

| Axis | Judgment | Basis |
|---|---|---|
| Depth | **unchanged** | The pair adds no richer source prose, lore inference, relationship model, or canon decision. The `carries` relation is copied unchanged. |
| Coverage | **improved** | The new byte-controlled pair isolates source-ID multiplicity for the otherwise identical `mira -> seal / carries / courier-log` relation. The unique input is clean; the duplicate input includes `relations[0].source_id: ambiguous in-world source 'courier-log'`. Round 7 already covered an ambiguous reverse `allied_with` relation and must be credited as prior art. What is newly exercised is the **non-alliance** relation citation with a clean control, not generic source resolution itself. |
| Calibration | **unchanged** | The report and README name all collateral findings, and keep identifier ambiguity separate from textual support or truth. This preserves the prior boundary, rather than adding a new calibration distinction. |

Independent inspection: all five `r31-source-unique/` JSON files equal `consistent/` byte-for-byte. Between the pair, four tables including `relations.json` are identical. The only mutation is a third structurally admitted `sources.json` row with the already used ID `courier-log`, distinct metadata and no independent story claim. I independently ran the documented Python 3 checker: unique exits 0 with the exact CLEAN line; ambiguous exits 1, empty stderr, with **eight findings**, in output order:

1. `sources[2].id`: duplicate `courier-log`.
2. `entities[0].first_appearance`: ambiguous `courier-log`.
3. `entities[0].claims[0].source_id`: ambiguous `courier-log`.
4. `entities[3].first_appearance`: ambiguous `courier-log`.
5. `entities[3].claims[0].source_id`: ambiguous `courier-log`.
6. `relations[0].source_id`: ambiguous `courier-log`.
7. `timeline[0].source_id`: ambiguous `courier-log`.
8. `timeline[1].source_id`: ambiguous `courier-log`.

Thus the relation finding is **one of eight**, not the sole output change: one duplicate-ID finding plus four entity, one relation, and two timeline citation findings. Independently replayed `r7-ally-reverse-ambiguous` exits 1 with three findings: duplicated `harbor-compact`, `relations[1].source_id` ambiguity on the reverse `allied_with` edge, and missing sourced reciprocal. It is real prior relation-source ambiguity evidence, though not this controlled non-alliance probe.

Regression replay against the checker extracted from baseline `4da4b949aa03e6595cf9a0d947fb2ba0c44f6fb0`, passing **the same current fixture path** to both checker versions, yielded exact `(exit, stdout bytes, stderr bytes)` equality for **81/81** pre-existing fixture directories and both new pair cases. All **404/404** baseline fixture JSON paths remain byte-identical. This independently corroborates the reviewer and verifier; it does not turn clean structural output into source-text evidence. Consult the round-31 LOG declaration/policy, `corpus/fixtures/README.md`, `reports/r31-reviewer.md`, `reports/r31-independent-verifier.md`, and round-7 prior adjudication.

**Limits:** A duplicate fictional source ID leaves the reference unresolved; it neither proves nor refutes the `carries` relation. Neither source authenticity, source-prose support, canon, real-world rights, nor AI-training permission follows. No SHONEN checkmark, promotion, push, or merge is inferred here.

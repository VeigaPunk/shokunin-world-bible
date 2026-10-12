# Round 20 non-author reviewer — dependency inversion at negative ticks

## Independent replay

I inspected the Round 20 declaration in `.shokunin/lore/LOG.md`, executor report and checker diff, all seven raw `r20-*` fixture directories, the saved run transcript set, and the decision-table/source wording. I made no source or fixture edits.

I extracted baseline checker `47733bf` to `/tmp/r20-independent-baseline.py` and independently replayed all 49 pre-round-20 saved commands from `corpus/live/runs/20261012T190807Z/`. Each matched the saved exit code, stdout bytes, and empty stderr: **49/49 baseline exact**. I replayed all 56 saved commands in `corpus/live/runs/20261012T191902Z/` against the working checker: **56/56 exact**. Against baseline, the prior 49 remain exact; the only difference among all 56 is expected `r20-negative-dependent`, where baseline additionally emits an inversion finding. This confirms the stated bounded before/after behavior, not general checker correctness.

## Seven fixture results and boundary

The seven raw inputs support the intended edge-local rule:

| Fixture | Independent current result |
|---|---|
| `r20-valid-order` | Clean (0 violations). |
| `r20-negative-dependent` | Negative tick only; no inversion. Baseline emits the inversion too. |
| `r20-negative-prereq` | Negative tick only; no inversion. |
| `r20-both-negative` | Two negative-tick findings; no inversion. |
| `r20-valid-inversion` | Valid-endpoint inversion retained. |
| `r20-valid-equal` | Equal-tick inversion retained, alongside the distinct occupancy finding. |
| `r20-mixed-edges` | Negative-endpoint edge has no inversion; separate valid `2 -> 1` edge still reports inversion. |

Each paired fixture differs from its stated control only in relevant tick value(s); all fixture descriptions explicitly identify themselves as input fields and deny source-text chronology. The code diff is limited to adding `events[dep]['tick'] >= 0 and row['tick'] >= 0` to the existing unique-ID inversion condition. It retains tick diagnostics, row/index data, per-edge processing, and self/repeated/unknown/ambiguous checks. It does not alter occupancy or other validation.

## Additional diagnostic probes

I made temporary copies of the raw negative-dependent fixture (outside the repo) and compared current versus baseline for self, repeated, unknown, and ambiguous references. Self-dependency remained reported in both; repeated dependency remained reported in both; unknown remained reported in both; ambiguous ID remained reported in both. The current checker withheld the negative-tick inversion while baseline could emit one. Thus the finding-specific guard does not suppress these independent diagnostics. These probes are narrow examples, not exhaustive ID-resolution tests.

## Wording and calibration judgment

The decision-table row is properly scoped to uniquely resolved dependencies and negative integer endpoint ticks. It says the comparison is withheld, not that chronology is valid, an edge is satisfied, or an event did not occur. Fixture descriptions are input-scoped, and the source ID `courier-log` is not presented as proof of a timeline claim. The README does not make a broader chronology claim. This is consistent with the checker’s documented role as an input consistency checker, not source-text entailment or canon adjudication.

**Critical axis recommendation: calibration improved; depth unchanged; coverage unchanged; no axis harmed on this bounded evidence.** The move calibrates a definite inversion finding to the admitted nonnegative tick domain while preserving the invalid-tick finding and valid-endpoint inversions. It does not validate general chronology, dependency graph semantics, or source truth. The ambiguity policy remains count-based and separate; no treatment of malformed or excluded rows is implied. Recommend admission only as this narrow calibration move, subject to the separate verifier/adjudicator evidence and process gates.

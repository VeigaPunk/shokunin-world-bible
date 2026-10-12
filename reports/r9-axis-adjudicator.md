# Round 9 — independent axis adjudication

**Admission: yes.** One axis improved, none harmed, within the declared narrow event-ID ambiguity rule.

| Axis | Verdict | Basis |
|---|---|---|
| Depth | **Unchanged** | No additional canon facts, source-text attestation, or causal model. The guard counts schema-valid event rows; it cannot choose which duplicate record is true. |
| Coverage | **Unchanged** | No new lore consistency-rule class is established. The checker already reported duplicate timeline IDs and already checked dependency order; this change calibrates what it can infer when a referenced ID has multiple valid rows. |
| Calibration | **Improved** | Baseline last-wins lookup produced an inversion for low-then-high duplicates but not high-then-low. The current guard reports an indexed ambiguous dependency in both orders and does not select either tick. It retains the duplicate-ID finding, while the unique-ID control remains clean. |

I read the round-9 LOG claim and post-scout clarification, current checker, raw order-swapped pair and unique control, saved r9 CLI outputs, and the non-author reviewer and independent-verifier reports. The two pair fixtures have the same event-row multiset and identical other JSON inputs. My direct replay produced the same two findings and exit 1 for both orders, versus `CLEAN` and exit 0 for the unique control. The checker calls `events[dep]` in dependency ordering only when `event_id_counts[dep] == 1`; absent targets still report unknown, and repeated dependency entries retain round-8's separate indexed diagnostics. The independent verifier compared all 16 pre-r9 fixtures byte-for-byte against baseline output, replayed all 19, and matched pre/post hashes of the checker and 94 fixture JSON files. Its baseline pair replay independently established the original order dependence; the reviewer also probed duplicate references and malformed rows.

**Boundary of the verdict:** `ambiguous dependency event` means the referenced ID occurs in more than one *schema-valid* timeline row. A malformed duplicate candidate excluded by initial row validation does not qualify for that count. This is ambiguity reporting, not a contradiction resolution, proof of canon truth, proof that `courier-log` text supports an event, or proof that a uniquely named event is causally valid. The observed invariance is for this raw pair and targeted probes, not a universal statement about malformed inputs. No harmed axis is supported by the available replay evidence.

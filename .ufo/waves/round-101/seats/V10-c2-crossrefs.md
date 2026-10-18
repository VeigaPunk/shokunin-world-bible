# V10 — c2-crossrefs (round 101)

Seat: V10 · Target: U2 dossier `corpus/knowledge/r101-r10-register-first-entry.md` · Date: 2026-10-18
Mandate: every cited path and quoted clause resolves at the cited location (spot-check ≥6 anchors); dossier cross-reference numbers match the r100 synthesis. Read-only except this report.

## Poll record (POLL-WAIT PROTOCOL)

- Main window: 40 polls × 20s from lane root — ABSENT after 40/40 (`ABSENT after 40 polls (13min)`, exit 1). Artifact and seats dir both absent at window start.
- Bounded stall-escape (recorded, not fatal): 15 polls × 20s — `FOUND at escape-poll 13/15`; artifact delivered `-rw-r--r-- 20565 Oct 18 00:20 corpus/knowledge/r101-r10-register-first-entry.md`.
- Protocol nuance: the loop's FOUND trigger was `ls seats | grep -q '^U2'`, which matched the `U2-scratch/` **directory**, not a report. **U2's producer seat report (`U2-*.md`) was still ABSENT at verification close** after 6 further polls (`U2 producer report still ABSENT after 6 extra polls`). I verified the delivered artifact against primary sources, not the producer's report or plan.
- Other seats landing during the window: V02/V13/V22/V26/V28 reports + producer scratches — consistent with a live wave, which justified the bounded escape.

## Anchor spot-checks (19 anchors; mandate asked ≥6)

Command form (all from lane root): `sed -n '<N>p' <cited-file>` / `python3` line compares; observed outputs quoted in the transcript below per anchor.

| # | Dossier cite | Observed at cited location | Verdict |
|---|---|---|---|
| 1 | `r94-paired-crossing/fictional-excerpts.md:19` = "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair." | exact (`> There, they agreed, …`) | PASS |
| 2 | `r94 fictional-excerpts.md:20` minute names two ninth-bell entries + tick-10 meeting | exact | PASS |
| 3 | `r95 fictional-excerpts.md:26` "Tick 11: I waited at the Chalk Stair through the agreed bell." | exact | PASS |
| 4 | `r95 :27` "Evin did not come." / `:28` "The agreement we chalked covered this crossing only." / `:29` "I assert no other duty, no breach, and no obligation beyond this crossing." | exact, all three | PASS |
| 5 | `r96-crossing-response/fictional-excerpts.md:37` "Tick 12: I was at Salt Court through the same agreed bell." + `:38-40` accusation/winner/unresolved lines | exact, all four | PASS |
| 6 | Both note sections present in `r100-docket-review/fictional-excerpts.md` at lines 26 and 37 | exact, both | PASS |
| 7 | `r88 table:26` R10 row quote "Before integrating a new cluster, … confirm a shared referent, field, and occasion." + "cross-cluster comparison and register-reference checks are an explicit manual integration gate" | both verbatim in line 26 | PASS |
| 8 | `r88 :93-94` gate "Only a source-backed shared referent, field, and occasion with incompatible assertions enters" | verbatim across 93–94 | PASS |
| 9 | `r88 :97` "the register's first real entry awaits a genuine conflict." | verbatim | PASS |
| 10 | `r88 :99-100` namespace rule; `:90-92` dismissed-overlaps heading | verbatim | PASS |
| 11 | `LOG.md:2656-2658` r93 R10 negative case "zero shared referents or supported conflicts" | verbatim at :2657 | PASS |
| 12 | Source IDs: `r94 sources.json:15` crossing-minute / `r95 sources.json:21` aru-aftermath-note / `r96 sources.json:27` evin-response-note | `"id": …` at each cited line | PASS |
| 13 | `r95 README:11` no-breach bound; `r96 README:3` one-lineage declaration | verbatim | PASS |
| 14 | `r96-response-scope-note.md:13` class distinction / `:31` different actors+places / `:40` r35 precedent | verbatim | PASS |
| 15 | `fixtures/README.md:761` "Neither wins."; r35 `manual-clause-pointer-map.md:3`,`:21` | verbatim | PASS |
| 16 | r35 `contradictions.json#/0` = `bell7-location-reports`, field `place_id` on `timeline.json#/2-3`, conditional `why` | exact (`claim_a/claim_b` `.field="place_id"`, events tl#/2 `tarin-envelope-observation`(harbor), tl#/3 `sella-bell7-presence`(tower), why begins "If the names … align") | PASS |
| 17 | `r89-cross-cluster-contradiction.md:5` hypothetical-second-cluster demo | verbatim | PASS |
| 18 | **`r94 README.md:13`** = ticks-editorial clause (dossier §Referent :58, §Bounds :81) | **MISATTRIBUTED** — line 13 is the `first_appearance` row; the clause "The integer ticks and event-ID edges in `timeline.json` are editorial encodings of the excerpt's tick labels and stated order/dependence, not literal JSON wording…" is at **r94 README:11** | **FAIL (±2-line offset)** |
| 19 | **`r96-crossing-response/README.md:11`** = "records only Evin's second account of the same occasion" (dossier §Referent :54) | **MISATTRIBUTED** — verbatim phrase is at **r96 README:9**; line 11 carries a different sentence ("the second account does not overturn, confirm, or adjudicate the first") | **FAIL (±2-line offset)** |

Both FAILs are path-correct, line-offset (−2) citations; the quoted clauses exist verbatim in the cited files. No semantic change to any dossier claim.

Nuance (recorded, not a FAIL): dossier :84's unquoted paraphrase "a per-cluster CLEAN is not cross-cluster evidence" is cited to `r88 table:110`; the near-verbatim phrase sits in `r88 table:26`'s verification column, while :110 carries the adjacent governance sentence ("Do not mark any of those surfaces mechanically verified solely from a clean fixture replay."). Paraphrase-level support holds at :110; verbatim at :26.

## Receipt re-measurement (reproduced byte-exact)

```
python3 - <<'PY'  (sha256/len of relations.json, 7 fixtures)
r94…r100  →  c279254bc7de0636 139   (all seven, identical to dossier lines 107–113)
```
- `relations.json#/0` (r94) = `{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}` — exact.
- `r95 timeline.json#/3` = `aftermath-missing-evin`, tick 11, aru, chalk-stair, `["paired-crossing-decision"]`, `aru-aftermath-note` — exact (4 events). `r96 timeline.json#/4` = `response-evin-salt-court`, tick 12, evin, salt-court, `["aftermath-missing-evin"]`, `evin-response-note` — exact (5 events).
- Prefix chain: `r95 starts with r94: True | r96 starts with r95: True`.
- `contradictions.json` = `[]` in both compared clusters; `corpus/knowledge/cross-cluster-contradictions.md` absent (`exists() → False`).
- r94/r95/r96 README line 5 all read `## Namespace and occasion comparison` — the dossier's recorded r90-heading variance is accurate.

## Cross-reference numbers vs r100 synthesis — all match

`r100-crossing-arc-synthesis.md` docket :32-38 (seven beats), invariant :10/:48, occupancy quote :50 and relation-quote :46 — both verbatim as the dossier quotes them; :54 testimony bound. Numbers: claim A = beat 1 (r95, `timeline.json#/3`, tick 11, `sources.json#/3`), claim B = beat 2 (r96, `#/4`, tick 12, `#/4`), referent sourced `sources.json#/2` (r94, tick 10, deps = both tick-9 entries) — identical to the synthesis docket rows; measured E/R/S r95 5/1/4, r96 5/1/5 consistent; every `contradictions.json` `[]` as synthesis :50 states.

## Limits

Author-seat artifact, so this is evidence for the integrator, not admission. I did not run the fixture gates (not my mandate). U2's producer report was never observed; if the integrator requires it, it postdates this close. No commits, no pushes, no network; only this file written.

**Bottom line: PASS (qualified) — C2 dossier delivered and substantively verified (all quoted clauses resolve in-file; receipts reproduce byte-exact; cross-refs match the r100 synthesis exactly), with 2 recorded ±2-line citation offsets (r94 README:11-not-13, r96 README:9-not-11) and U2's producer report ABSENT at close.**

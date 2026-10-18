# JCOV4 — Fresh-eyes province audit (round 91 follow-up)

Seat JCOV4. Audited state: HEAD `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (`6332115` + `c2ab3d0` on baseline `a7c6a17`), tree clean at start.
Scope per block: the hardened script, the maps, the Inventory contract, and the C9 watch against `PROVINCE.md` refusals + the three-question rule; then compare with `.ufo/waves/round-91/C7.md`.
Order disclosed: spec/`PROVINCE.md` first; `C7.md` was read before probe execution (not blind); every claim below was re-derived first-hand from the delivered tree. Scratch `/tmp/lore-r91-jcov4` (27 files, 168K) swept at the end. Dependencies: two 60 s wait-checks ran (both dependency artifacts present at both checks; no gap).

## Work performed

- **Axes touched by this seat's evidence:** coverage (C2 contract correctness on the delivered tree), calibration (C1/C9 receipts), and province/three-question compliance. Depth (C3) was audited only for province compliance; the edge decisions themselves are JDEP seats' axes.
- Re-ran the delivered vs `e97613c` checkers on both C1 fixtures; re-ran `support_check.py` on all three delivered maps; replayed an 8-mutation attack matrix and the two documented contract deviations on the delivered script; recomputed the raw JSON census; re-applied the C2 patch stack in scratch for provenance; ran refusal/three-question sweeps over script, maps, watch, and fixture READMEs; then compared with C7.
- No tracked writes besides this report; no commit or push; sibling repos untouched.

## Before → after measurements

### Starting state, hashes, wait-checks

```sh
git log --oneline -2 && git rev-parse HEAD && git status --porcelain
```

```text
c2ab3d0 lore r91: C3 R8/R10 r91 edge decisions ... (c2ab3d0)
6332115 lore r91: C1 discriminating fixtures + C9 watch, C2 hardened support command, ...
c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
(status: empty)
df -i /tmp at start: tmpfs 1048576 1046701 1875 100% /tmp
```

Wait-check receipt (one background call, 2 checks, 60 s apart):

```text
[2026-10-17T08:32:40-03:00] check1: C7.md=present JCOV4.md=absent support_check.py=present r91-c9-watch.md=present
[2026-10-17T08:33:40-03:00] check2: C7.md=present JCOV4.md=absent support_check.py=present r91-c9-watch.md=present
wait_checks_done=2
```

Hashes:

```sh
sha256sum corpus/fixtures/check_bible.py corpus/tools/support_check.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
9da149b8e51f5c6c39477f17b8b19d17da3568a1a7c72412079efccff1f330bf  corpus/tools/support_check.py
```

`check_bible.py` last changed at `ca7f9ef` (r90); nothing modified it at r91 — "the r91 checker is UNCHANGED (ff9fd2aa)" verified. `support_check.py` blob in the delivered tree: `f75af1ce66ba45a70189d1ed9540fff0a76d5fee` (changed by `6332115`, i.e. the r91 hardening).

### Calibration: the discriminating pair, both checkers

Commands (`sha256sum` of the extracted historical checker: `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
git show e97613c:corpus/fixtures/check_bible.py > /tmp/.../check_bible_e97613c.py && python3 .../check_bible_e97613c.py corpus/fixtures/r91-c1-null-chain
python3 .../check_bible_e97613c.py corpus/fixtures/r91-c1-tick-unresolved
```

Delivered (`ff9fd2aa`), exit 1, stderr empty for both:

```text
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
```

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

`diff` old-vs-new, exactly one repaired line per fixture (nothing else differs):

```text
null-chain: 1c1 — old: "…input-structural finding, not sourced-canon; possible provenance chain break…got None; from_holder None is not uniquely resolvable (0 raw entity rows…)"; new: "…provenance chain break; expected from_holder 'mira', got None"
tick:       2c2 — old hedged with "holder identity is not uniquely resolvable … previous tick 3"; new: "provenance tick 1 must be greater than previous tick 3"
```

Both fixture READMEs' per-checker expected outputs are byte-exact matches of the above four runs; the C9 watch's stated lines/exit/violation counts match. Bounded parity spot-check on legacy fixtures (`r87-myth-cluster`, `r89-fn2-unresolved-chain-break`): checker outputs identical between `e97613c` and delivered, corroborating (not re-proving) B1/B2's "0 changed" census direction.

### Coverage: hardened support command on the delivered maps

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster    # exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster # exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase # exit 0
```

```text
r87: INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
     ANCHORS repeated-references=0; DUPLICATE-ROWS 0
     SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22; RESULT PASS
r88: INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
     ANCHORS repeated-references=4; DUPLICATE-ROWS 0
     SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10; VALIDATED-ROWS 10/10
     WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim); RESULT PASS WITH WARNINGS
r89: INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
     SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1; RESULT PASS
```

Mutation matrix (minimal scratch copies of the delivered maps/excerpts, delivered script; base = delivered files):

| # | mutation | observed key output | exit |
|---|---|---|---|
| T1 | r87 JSON-table `ID` header renamed to `Ref` | `JSON-FACTS 0/14; TOTAL 8/22` + FAIL inventory lines | 1 |
| T2 | r87 `## Editorial rows` section dropped (inventory untouched) | `EDITORIAL-ROWS 0/8; TOTAL 14/22` + FAILs + WARN unreferenced hymn | 1 |
| T3 | r87 `E1` row duplicated | `JSON-FACTS 15/14; TOTAL 23/22; ANCHORS repeated-references=1; DUPLICATE-ROWS 1`; `SOURCE-SUPPORT 15/15` in the failing receipt + FAILs | 1 |
| T4 | r87 hymn excerpt-declaration mode flipped `verbatim`→`summary` (referenced) | 8× `FAIL H*: delivery mode missing or mismatched`; `MODES 14/22; EDITORIAL-ANCHORS 0/8` | 1 |
| T5 | r88 Spence declaration mode flipped `verbatim`→`summary` (unreferenced) | `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=summary)`; `SOURCE-SUPPORT 10/10` unchanged; `RESULT PASS WITH WARNINGS` | 0 |
| T6 | r89 paraphrase anchor made absent | `RETELLING-SUPPORT-ONLY 1 entries (0/1 anchors)`; `SOURCE-SUPPORT 0/0` unchanged; WARN excluded-from-source-support | 0 |
| T7 | r87 inventory declaration line removed | stdout empty; stderr `FAIL: map must contain exactly one expected inventory declaration` | 2 |
| T8 | r87 distinct-anchor declaration off by one (22→21) | `DISTINCT-ANCHORS 22/21` + `FAIL: inventory distinct excerpt anchors mismatch`; no `RESULT` terminal line | 1 |

T1/T2 confirm both r90 silent vectors (header rename, dropped section) now fail non-zero; T3/T5/T6 confirm duplicate/inflation and mode/retelling surfacing without inflating source support; T7/T8 confirm both README-documented S2 terminal-status deviations exactly as written (`corpus/tools/README.md:16-21`). The README's other claims (single inventory line, sections required, exact duplicate rows fail while repeated anchors are reported, in-span `grep -nF --` without a shell) match the delivered script's code paths (`support_check.py:186-207, 232-370`).

### Provenance of the delivered C2 file set

Re-applied the patch stack to a scratch baseline copy of the five C2 files (`git show a7c6a17:<file>`):

```text
apply M2-hardening-alt → applied OK
apply M3-mapwording    → APPLY FAILED (context conflict on both maps at line 1 and README line 10)
apply M6-reconcile     → applied OK
diff scratch vs delivered, all five files:
  IDENTICAL corpus/tools/support_check.py
  IDENTICAL corpus/tools/README.md
  IDENTICAL corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md
  IDENTICAL corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
  IDENTICAL corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md
```

So the delivered hardening is byte-identical to baseline+M2+M6; M3's overlapping M1-format patch was not the landing vehicle (M6.md's handoff line 80 says exactly this). The one-checker format C7 preferred (M2) landed verbatim.

### Raw JSON census (independent recompute) and the maps

```sh
python3 - <<'PY'   # counts claims / first_appearance pointers / relations / timeline from entities.json etc.
PY
```

```text
r87-myth-cluster:        entity_rows=7 claims=7 pointers=7 relations=4 timeline=4 raw_obligations=22
r88-m3-maya-cluster:     entity_rows=4 claims=4 pointers=4 relations=0 timeline=2 raw_obligations=10
r89-inspiration-paraphrase: entity_rows=1 claims=1 pointers=1 relations=0 timeline=0 raw_obligations=2
r87 entities[2] = mother-tide-gate | first_appearance: lowwater-hymn | claims[0].source_id: lowwater-hymn
```

Row coverage of the 14+8=22 mapped rows: `E1-E6` each co-map one claim **and** one `first_appearance` pointer (12 obligations in 6 rows) + `R1-R4` + `T1-T4` = **20 of 22** raw obligations row-represented; the remaining two (`entities[2].claims[0]` and its pointer) are disclosed in the r87 map's "Full D1 crosswalk" note but are not fact-table rows. r88's 10 rows do match its 10 raw obligations one-to-one. The r87 map explicitly scopes itself to "14 JSON facts from S2's r89 map" and disclaims the rest — the numbers behind C7's D-C7-1 hold exactly.

### Province refusals and the three-question rule

Grep sweeps (pattern `public domain|licen[cs]e|rights|permission|permitted|prohibited|canon|mechanic|gameplay|damage|balance`, case-insensitive) over the audit targets:

- `corpus/tools/`: one hit, `README.md:23` — the disclaimer "not a judgment … faithful, permitted, or canonical". The script itself: zero hits.
- `r91-c9-watch.md`: one hit, line 8 — "not real-world chronology, source reliability, ownership, or canon".
- `r91-c1-*` READMEs: hits only inside quoted checker output ("not sourced-canon", "no canon changed"); both fixtures' `contradictions.json` are `[]`; no canon claimed (both open "Fixture scaffolding only; not sourced story evidence").
- Three maps: five hits, all disclaimers (`not extra JSON canon claims`, T3/T4 "preserve both … unresolved; neither excerpt refutes the other or selects canon", "not new canon", `check_bible.py` scope note).
- Zero hits for mechanics/gameplay/damage/balance anywhere in the audit targets.
- Reference ledger (context check for the r88 map's Spence row): `reference-ledger.md:13` keeps attribution / `Rights question` / `AI-training permission question` in separate cells, both questions open, "no rights grant is asserted", "no permission is inferred".

No PROVINCE refusal is breached by the script, the maps, the Inventory contract, or the C9 watch; the three-question rule is intact on every audited surface (no merge, no inference, no rights claim).

### C9 watch details

- Pinned hash verified (above); the four falsification gates are operational, the probe block names concrete commands, and ownership hands from S1 to the next C1 owner; the ruling explicitly stays checker-local (no chronology/canon claim). Gate 4's demand ("delivered checker reports a definite inversion that this evidence makes indeterminate") is satisfiable by construction — the delivered checker does emit the definite tick line on an unresolved holder, so a qualifying counterexample is a real possibility, not a dead letter.
- The watch's claim that the `e97613c` comparison is pinned in `B3-before-state.json` and the fixture READMEs verified: B3 pins the historical checker invocations/hedged outputs (its scratch probes used `previous tick 2`; the durable fixture uses `tick 3` — my own runs against the durable fixtures match both READMEs byte-for-byte, so the discrimination is verified on the durable pair independent of B3's scratch probes).

### Compare with C7.md

| C7 item | Status at `c2ab3d0` (fresh eyes) |
|---|---|
| Preferred M2 over M1 as integration base | Realized byte-exact; M1 did not land (provenance above). |
| D-C7-1: `JSON-FACTS 14/14` is a row receipt, not a raw census; only 20/22 r87 obligations row-represented | Confirmed with exact arithmetic; map crosswalk note discloses the two prose-only obligations. |
| D-C7-2: expected inventory is self-declared (declaration vs parsed rows only) | Confirmed; declaration is not checked against raw JSON, and the tools README does not restate this limitation (only the map note discloses the r87 gap). Named below as residual. |
| C2 WARNs do not inflate source support; `RESULT PASS WITH WARNINGS` is not support | Confirmed (T5/T6; numerators unchanged). |
| Duplicate-row run must not be read as a valid receipt | Confirmed in delivered format (T3: `SOURCE-SUPPORT 15/15` while exit 1). |
| M2's two S2 terminal-status deviations | Confirmed and now README-documented (T7/T8); behavior matches the README text. |
| R9 editorial/manual gate + source/version parity limitation persists | Confirmed; README final paragraph and the r89 map's "Fails:" editorial column carry it; checker itself cannot see it. |
| C7 poll debt (wrong patch glob, missing deadline branch) | Not applicable to this seat; my two 60 s checks and all probes ran clean. |

## Findings & named debt

- **Verdicts (per axis, bounded):** coverage — **improved (bounded)**: every r90 silent-failure vector now fails or warns on the delivered tree (T1–T6), the Inventory contract matches its README, and both documented deviations are reproduced as documented; bounded by the self-declared-inventory limitation below. Calibration — **improved (bounded)**: the durable pair discriminates exactly on the repaired lines, hash pinned and matching, watch/probe receipt clean; bounded in that I spot-checked two legacy fixtures rather than re-running the full 164-fixture census (that remains B1/B2's receipt). Depth — **unchanged by this seat** (audited only for province compliance; no C3 edit was mine to judge).
- **JCOV4-1 (residual, extends C7 D-C7-1/D-C7-2):** the expected-inventory declaration remains self-declared. `corpus/tools/README.md` says counts are checked "against the declaration" but never says the declaration is not raw-JSON-derived; only the r87 map's crosswalk note makes the 20/22 row/obligation gap explicit. Q1's debt file does not name this under the searched terms (`self-declared|raw JSON|row receipt|14/14|inventory assertion` → no matches). Suggested r92 move: one README sentence plus an explicit row-vs-obligation note (or an optional raw-JSON coverage crosswalk), not an assertion change.
- **JCOV4-2 (doc nit):** the r88 expected unreferenced-declaration WARN is structurally explained (symbolism comparisons use `source-excerpt.md` while no fact row does; semantics in tools README line 14) but neither the map nor the fixture README labels it "expected", so a green-with-WARN run reads as a surprise. One parenthetical would close it.
- **JCOV4-3 (watch completeness, minor):** the C9 watch pins the delivered checker's SHA-256 but not `e97613c`'s; its own trigger protocol asks the recorder for "the two checker hashes". The comparison outputs are pinned (B3 + READMEs, both verified) and the blob is retrievable; pinning `e97613c`'s hash would make the record self-contained. No breach.
- **Confirmations carried forward:** C7's D-C7-1, D-C7-2, WARN semantics, duplicate caution, and M2-selection all remain accurate at the delivered commit; nothing C7 reported was refuted. No province refusal or three-question breach found in the audited surfaces.

## Handoff

- This report is the only seat write: `.ufo/waves/round-91/followup/JCOV4.md`. No commits, no pushes, no tracked edits, sibling repos read-only.
- For integration/debt: JCOV4-1 (README row/fact limitation statement) is the one candidate worth an r92 line; JCOV4-2/JCOV4-3 are documentation polish only. Nothing here blocks the r91 closure record.
- Scratch hygiene: `/tmp/lore-r91-jcov4` (27 files) removed; `df -i /tmp` re-checked after sweep; final `git status --porcelain` limited to `.ufo/waves/round-91/followup/` (this report).
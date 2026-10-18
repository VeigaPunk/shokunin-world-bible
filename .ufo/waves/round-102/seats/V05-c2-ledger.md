# V05 — c2-ledger-audit (round 102)

**Seat:** V05, verifier, C2/calibration. **Model:** zai-coding-plan/glm-5.3-flash-low.
**Scope:** independently extract the debt items from the source ledgers (r94–r101), compare counts against `corpus/knowledge/r102-debt-ledger.json`, verify every disposition's evidence pointer resolves, and prove no item was dropped (set difference both directions). Leaf seat; read-only except this report; no commits, no network.
**Poll record:** producer artifacts polled 14 times, 20 s cadence (06:19→06:48 local): ABSENT through poll 13; `r102-debt-ledger.json` landed 06:39:33-03:00 (poll 13), `U1-synthesis.md` landed 06:42:30 (poll 14). All-reports polls subtracted SELF. No stall-escape used; U1 was verified on delivered bytes, never on plan.

## Ground truth (independent extraction, before reading U1's file)

Sources read directly with python3/json:

| round | source file | my count |
|---|---|---|
| r94 | `.ufo/waves/round-94/followup/F29-debt.json` | 51 items (CC×15 ids where CC-14 is class `superseded`, BR×28, CR×8) |
| r95 | `.ufo/waves/round-95/seats/V31-debt.json` | 51 items (NB 14, CO 23, CL 10, PR 3, ST 1) |
| r96 | `.ufo/waves/round-96/seats/V40-debt.json` | 63 items (NB 27, CL 12, CO 10, PR 8, ST 6) |
| r97 | `.ufo/waves/round-97/seats/V37-debt.json` | 70 items (NB 20, CO 18, CL 12, PR 13, ST 7) |
| r98 | `.ufo/waves/round-98/seats/V33-debt.json` | 42 dict items (NB 12, CL 10, PR 13, ST 7) **+ bounds_carried dict = 4+4+12+1 = 21 bucket entries** |
| r99 | `.ufo/waves/round-99/seats/V36-debt.json` | 16 NB dicts + 10 string closure items **+ bounds_carried = 5+5+4+2 = 16 bucket entries** |
| r100 | NO debt file exists (see D2) | — |
| r101 | NO debt file exists; "carried notes" = V24 defects 1–6 + AC-1…4 | 10 |

All IDs unique within each round. My scratch extraction: `/tmp/v05-scratch/` (audit harness + JSON dumps).

## Results

**R1 — Count match vs sources: PASS.** Ledger `sources[]` = 51/51/63/70/63/42/11/10 (= 361), exactly matching my extraction, including the two non-obvious rows: r98 = 42 section items + 21 bounds_carried buckets (I re-counted the buckets in the source dict: closed 4 + recurring 4 + open_or_accepted 12 + not_recurring 1 = 21 ✓) and r99 = 26 sections + 16 buckets + NB-07-as-carry = 42 with own = 25 ✓ (16+5+4+2 = 16 buckets ✓). `totals`: 264 items + 97 carry_records = 361 = Σ items_in_source ✓; per-round own-sum 51+24+51+50+42+25+11+10 = 264 ✓; carry-sum 0+27+12+20+21+17+0+0 = 97 ✓. Dispositions 111 closed / 108 addressed / 45 carried sum to 264 ✓.

**R2 — Set difference both directions: PASS (0 missing, 0 phantom).** Under the ledger's declared carry rules (r95 CO-01…23 + NB-05/06/10/11; r96 CO-01…10 + NB-07/NB-18; r97 CO-01…18 + NB-10/11; r99 NB-07), the (origin_round, source_id) item set equals my own-item ground truth exactly in all six rounds — 243/243, no duplicates in the ledger. Carry coverage exact: r95 27/27, r96 12/12, r97 20/20 ids; r98 21 bucket carries, r99 17 (16 buckets + NB-07). XOR union over all 303 r94–r99 source ids: every id appears exactly once (own item XOR carry record), 0 neither, 0 double. Track references: 89/97 carry records cite source ids that all validate (compound refs like "r94-BR-19 + r94-BR-20" parse and resolve); 8/97 carry prose-only track labels ("r98 C9 row-7", "r99 ten-file pin record"…) — content real, but weaker as machine pointers (observation O1, not a drop).

**R3 — Evidence-pointer resolution: PASS (320/320 item refs + 97/97 carry paths).** Battery over all 264 items' `evidence` arrays: every file path resolves (repo-relative, wave-relative, and 3 absolute parent-level paths all exist), every cited line number is inside its file, every commit hash resolves via `git cat-file -t` (ac69044, dcb2d92, 9d25df9, 4265df5, f3e09f9, 2393934, ceeef43, 542021a, …). Three initial flags were my resolver's bugs, corrected and re-verified: `/home/vgpnk/Projects/shokunin/MANIFEST.json` EXISTS; `/home/vgpnk/Projects/shokunin/.ufo/reports/round-95/lore.md` EXISTS; "`.ufo/waves/round-95..101/receipt.json`" is a range expression and all seven round receipts exist. No item has empty evidence — the "every disposition carries an evidence pointer" claim holds.

**R4 — Disposition truth (spot-checks): PASS.** (a) r101-DEF-1/AC-1 `closed`: the r101 register entry at lines 58 and 81 now cites `r94-paired-crossing/README.md:11` (repair landed) — verified by grep on delivered bytes. (b) r96-CL-02 `closed`: `## Round 96` section exists in `corpus/fixtures/README.md:1198`. (c) r96-NB-21/r97-NB-09 `carried` with evidence "blind-spot row 7": row 7 and `## Row 7` exist in `r99-gate-blind-spot-table.md`. (d) r98-CL-10 `carried` (anomaly-disclosed NOT-landed): `grep -c exit corpus/fixtures/r98-clerk-filing/README.md` → 0, the recorded exits are indeed absent — carried, not falsely closed. (e) r100 items = V29's six admission conditions (AC-ROSTER…AC-CLOSE, V29-adjudicator.md §5) + three standing FAILs (V15/V18/V20, §4 lines 251–253) + two qualifications (V21/V30) = 11, titles matching the source text; all six `closed` per LOG r100 closure discharge. (f) r101 items = V24 "Recorded defects" 1–6 + AC-1…AC-4 = 10, titles matching V24's filed list verbatim in substance.

**R5 — Claim-side citation defect, independently found and disclosed: D2.** The r102 LOG declaration cites "r100 V33" as a source ledger; round-100's roster was T1–T4 + V01–V30 (34 seats), no V33 seat or debt file exists anywhere in the wave or in git history (`git log --all -- '.ufo/waves/round-100/seats/V33*'` → empty). U1 discloses this verbatim in `anomalies[0]` and in the synthesis, and substitutes the real r100 surface (V29 conditions + FAILs/quals), which I verified above. Claim-side defect, honestly surfaced, substitute surface verified — recorded, not smoothed.

**D1 — the one defect found in the deliverable (non-blocking):** the JSON's `bottom_line` says "273 items + 88 carry records = 361 source entries accounted" while the same file's `totals`/`sources`/`items`/`carry_records` all say **264 + 97 = 361** (verified by my own sums). The 361 total is correct in both; the bottom_line split is stale (U1's synthesis reports 264/97, and its text says a pre-delivery self-audit fixed three count defects — the bottom_line string was evidently not regenerated). Same-total, wrong-split internal contradiction inside the machine-readable deliverable.

## Verdict per axis

- **calibration (C2 core claim "item count and dispositions match the source debt ledgers; nothing silently dropped"): VERIFIED** — exact set equality both directions over 361 source entries, all pointers resolve, dispositions truthful on every spot-check.
- **honesty: VERIFIED** — the two defects in play (bottom_line split; "r100 V33" citation) are exactly the kind the ledger's own anomaly block exists to carry; one is disclosed by the producer, one is mine to record.

**Conditions/observations for the adjudicator:**
- D1 (blocking for a literal "parse-and-sum" consumer? no — `totals` is the authoritative block and is correct; bottom_line is a prose summary): recommend a dated one-line addendum or regenerated bottom_line.
- D2 (claim text, operator-owned, not producer-owned bytes): the C2 declaration's source list contains a dangling pointer; U1's substitute is verified correct.
- O1: 8/97 carry_records carry prose-only `tracks` labels.

**Bottom line: PASS — r102-debt-ledger.json verified against the eight sources with exact two-direction set equality (361/361 entries, 0 dropped, 0 phantom), all 417 evidence pointers resolve, dispositions truthful on delivered bytes; two defects recorded: D1 stale bottom_line split (273+88 vs correct 264+97, total 361 correct in both) and D2 the operator-declaration's dangling "r100 V33" citation (disclosed by U1, substitute surface verified).**

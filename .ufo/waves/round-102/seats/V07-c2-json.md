# V07 — c2-json-validity — round-102 capstone

- Seat: V07 (verifier, c2-json-validity), lore-shokunin, round-102 single-wave CAPSTONE
- Date: 2026-10-18
- Claim under verification (LOG.md r102 C2): `corpus/knowledge/r102-debt-ledger.json` parses; schema is self-describing; counts internally consistent (items = closed + addressed + carried).
- Baseline: r101 closure 542021a; HEAD at verification: 8fa2e87 (r102 declaration).
- Artifact pinned revision: sha256 `70fbed21d45ecf2ed1840d87cd6bfdf0a6a14947c646e8cd8dc7d1829fd2194d`, 122,763 bytes, mtime 2026-10-18 06:39:33 -0300.

## 1. Parses — PASS

```
$ wc -c corpus/knowledge/r102-debt-ledger.json
122654 corpus/knowledge/r102-debt-ledger.json     # first read; rewritten mid-verification, see §5
$ python3 -c "import json; d=json.load(open('corpus/knowledge/r102-debt-ledger.json')); print('PARSE: OK')"
PARSE: OK
```
15 top-level keys: artifact, lane, round, compiled_at, compiled_by, baseline, scope, disposition_vocabulary, counting_rules, totals, sources, items, carry_records, anomalies, bottom_line. No trailing-garbage or duplicate-key anomalies surfaced.

## 2. Schema self-describing — PASS

- `disposition_vocabulary` defines all three dispositions with meanings, including the field contract for carried: `"carried": "still open in the delivered r102 tree; carried_owner names the holder"`.
- `counting_rules` states 4 rules (carry_record mirroring; ST/PR as addressed items; r100 has no debt file — anomaly noted; source_entries = own_items + carry_records = sum of items_in_source).
- Observed item keys: `id, origin_round, source_id, group, title, disposition, disposition_detail, evidence` (+ `carried_owner`, `trail` on carried items). All 264 items carry the full core set (no missing `disposition_detail`, no empty `evidence`). Minor: `source_id`/`origin_round`/`group` are not named in the metadata prose, but their semantics are unambiguous from structure — not a defect.

## 3. Counts internally consistent — the claimed identity HOLDS, all arithmetic identities hold

```
observed dispositions: {'closed': 111, 'addressed': 108, 'carried': 45} == totals.dispositions  → True
sum(dispositions) = 264 == len(items) = 264                                      → True
len(items) + len(carry_records) = 264 + 97 = 361 == totals.source_entries = 361  → True
totals.items == len(items) and totals.carry_records == len(carry_records)        → True
sources: Σ items_in_source = 361, Σ own_items = 264, Σ carry_records = 97;
own_items + carry_records == items_in_source for all 8 sources                  → True
dispositions outside vocabulary: NONE; missing/empty evidence: NONE; duplicate ids: NONE
origin_round all within 94–101; id prefix always matches origin_round
```
So items = closed + addressed + carried: **111 + 108 + 45 = 264 ✓** — the seat claim's literal identity verifies on the pinned bytes.

## 4. Defects found (evidence, exactly)

**D1 — the file's own `bottom_line` contradicts its `totals` (material).**
```
$ grep -o '"bottom_line": "[^"]*"' corpus/knowledge/r102-debt-ledger.json
"bottom_line": "273 items + 88 carry records = 361 source entries accounted; ..."
totals + observed: items=264, carry_records=97 (264 + 97 = 361)
```
Both splits sum to 361, but the narrative 273/88 contradicts the machine totals 264/97 and the actual array lengths. The narrative split is stale or wrong; the grand total is consistent.

**D2 — carried item `r97-NB-20` has no `carried_owner`, violating the vocabulary's own rule.** 44/45 carried items carry `"carried_owner": "r103+ (operator; lane closes at r102)"`; r97-NB-20 ("r97 fixture README replay without exits") has none — its detail defers to the r94-BR-17 class, which itself carries an owner, but the declared field contract is unmet.

**D3 — declared trail-mirroring rule only partially implemented (non-arithmetic).** Counting rule 1 says carry_records are "mirrored into the tracked item's trail": only 38/264 items have any non-empty trail; of 68 carry records whose `tracks` names exactly one existing item id, only 25 appear in that item's trail; tracked carried item r94-BR-04 has `trail: null`. The other 29 carry records use multi-target/free-text `tracks` (e.g. `"r94-BR-19 + r94-BR-20"`, `"r94 carry-overs (CR/BR set)"`) — not machine-resolvable, not counted as a numeric defect. No count identity depends on D3.

## 5. Verification conditions (recorded)

- **Poll-wait:** 42 tries at 20 s before artifact appeared at ~06:38:40 (over the 40 budget — bounded stall-escape, recorded, not fatal: the target artifact existed, only U1's seat report was pending). U1's seat report (`U1-*.md`) was **still ABSENT** at final check (~06:44), while 5 other seat reports were present. This seat verified the artifact bytes themselves; the absent U1 report did not gate any check above.
- **Mid-verification rewrite:** the artifact grew 122,654 → 122,763 bytes (mtime 06:39:33) between my first parse and the metadata reads; D1 and D2 were present in both revisions. All §2–§4 results re-run and reproduced on the final pinned revision (sha256 above); re-checked stable (identical hash) after a 45 s wait.

## Bottom line

PASS — `r102-debt-ledger.json` (sha256 70fbed21…) parses, schema is self-describing, and the claimed identity holds exactly (closed 111 + addressed 108 + carried 45 = 264 items; +97 carry records = 361 = source entries, all totals/sources identities verified) — with recorded residue: the file's own `bottom_line` narrates a contradicting split (273/88 vs 264/97), carried item r97-NB-20 lacks `carried_owner`, and the declared trail-mirror rule is only partially implemented; U1's seat report remained absent throughout.

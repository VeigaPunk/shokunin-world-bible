# V55 fixture-readme-review — round 98

Seat: V55 (verifier). Baseline: r97 closure `9a3d648`. All commands ran from the lane
root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no pushes, no network. Writes: this report (absolute path) and
`.ufo/waves/round-98/seats/V55-scratch/` (poll script, receipts).

Scope: run every command in S4's README as written; check counts/scope wording in S4's
two owned files:

1. `corpus/fixtures/r98-clerk-filing/README.md` — sha256
   `32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926` (5,829 B)
2. `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` — sha256
   `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` (15,028 B)

Both hashes were identical at first read (post-rewrite), at the final frozen-byte
re-run, and as declared in S4's report (`S4-fixture-docs.md` section "Owned and
delivered").

## 0. Poll-wait record (protocol: 20 s cadence, 40 tries)

- 20:28:24: `corpus/fixtures/r98-clerk-filing/` appeared with 10 files byte-identical
  to r97 (S3's placeholder copy phase; README.md sha256 was `d9387b7d…`, the r97 bytes).
- 20:28:55: S3's data edits landed (entities/sources/timeline/fictional-excerpts).
- 20:30: README.md changed to `32efc78f…` and claim-excerpt-map.md to `c1099d0e…`
  (S4's rewrite).
- Poll script (V55-scratch/poll.sh, background) hit at **try 13**: "ALL PRESENT:
  .ufo/waves/round-98/seats/S4-fixture-docs.md". No stall-escape needed; no ABSENT
  condition arose.
- Mid-flight hazard observed and handled (recorded, not fatal): an existence-only
  check is satisfied by the r97 placeholder copy — README/map existed with r97 bytes
  from 20:28:24 to ~20:30. My verification was performed only after the rewrite, and
  the two hashes were re-confirmed unchanged at the end (see section 4).

## 1. Commands in S4's README, run as written

README block (lines 25-29, "Replay from the repository root"):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
```

Observed (exact, run from the lane root):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J17 (lines 12/13/12/13/17/12/13/12/13/18/19/12/13/18-20/22-31/33-42/44-53)
PASS J18: anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS S01, PASS S02 (editorial rows)
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
exit=0
```

All three commands exit 0; final frozen-byte re-run (after S4's report landed)
reproduced exit 0/0/0 on the same two hashes.

## 2. Counts check (README and map vs actual JSON/tool receipts)

| Claim (source) | Declared | Actual | Verdict |
|---|---|---|---|
| README line 3 | 6 entities / 1 relation / 7 events / 7 sources | `entities=6 relations=1 timeline=7 sources=7` (python json.load, also check_bible CLEAN) | match |
| README line 3 inheritance | 5 inherited entities, 1 relation, 6 events, 6 sources copied by JSON value | r97 has 5/1/6/6; r98 diffs are pure appends (see section 3) | match |
| README line 21 | 20 obligations = 17 inherited + 3 new (first_appearance + claim + event) | map rows J01-J20; new rows J18=`entities.json#/5/first_appearance`, J19=`entities.json#/5/claims/0`, J20=`timeline.json#/6` | match |
| Map line 5 | 20 JSON facts; 2 editorial rows; 22 total; 18 distinct anchors | support_check receipt 20/20, 2/2, 22/22, 18/18 | match |
| Map line 3 | six first-appearance pointers, six entity claims, one relation, seven timeline events | 6+6+1+7 = 20 rows present | match |
| Map line 18 | 3 new rows anchored only in appended section lines 55-64 | J18 anchor@60, J19@59, J20@59; section = file lines 55-64 (file has 64 lines) | match |

## 3. Inherited-rows-unchanged check (independent of S4's script)

Parsed both maps' `| J…` table rows and compared columns (ID, pointer, source ID,
excerpt path, span, mode, anchor), excluding the path-qualification namespace column
(intentionally renamed r97→r98):

```
r97 rows: 17  r98 rows: 20
inherited-row mismatches (excluding namespace col): 0
new rows: ['J18', 'J19', 'J20']
```

Map line numbers of inherited rows are unchanged (J01 at line 22, J17 at line 38 in
both maps). New rows are appended after (J18 line 39, J19 line 40, J20 line 41). New
anchors verified in the excerpt file at the declared lines via the tool receipt
(J18→60, J19→59, J20→59), all inside the declared spans (60 / 59-60 / 55-64).

## 4. Scope-wording check (no finding / no resolution / bounds)

Checked README and map against the authored excerpt (`fictional-excerpts.md:55-64`,
note lines 59-62: "I record the matter OPEN.", "I assert no finding.", "I reach no
verdict and reconcile nothing.") and the JSON:

- README line 9: tick-14 event "ordered after and depends on the tick-13
  acknowledgment (`acknowledgment-aru-records`)" — matches `timeline.json#/6`
  (`tick: 14`, `entity_id: clerk-maren`, `place_id: chalk-stair`,
  `depends_on: ["acknowledgment-aru-records"]`). Match.
- README line 11: "institutional filing record that asserts no finding and no
  resolution; it reaches no verdict, reconciles nothing, and selects no winner …
  `contradictions.json` remains empty … no other duty, no breach, no continuing
  obligation … not evidence of an alliance, a continuing practice, perpetual
  performance, a standing duty, an adjudication, or an external historical fact."
  All consistent with excerpt lines 59-62 and `contradictions.json = []`. No
  canon-truth or resolution assertion found anywhere.
- README line 15: `first_appearance: clerk-filing-note` bound for Maren — "asserts no
  office beyond the filing, no finding, and no other record" — matches entity row
  `clerk-maren` (`first_appearance: clerk-filing-note`). No identity inference.
- README line 19: Spence passage remains a bounded external design prompt; "Rights and
  AI-training permission remain unassessed; neither is granted or inferred here." OK.
- Map lines 62/64/66 (J18/J19/J20 paragraphs): each span matches the excerpt section
  exactly (60 alone; 59-60; 55-64); scope sentences ("asserts no finding, no verdict,
  no reconciliation, and no resolution"; "assigns no authority beyond the filing
  itself") are supported by lines 60-62. No stale count or stale r97-path wording in
  headings or replay commands (r97/r96/… references occur only as correct
  continuation history and inherited-namespace lists).
- Grep sweep for `finding|verdict|resolution|reconcil|winner|rights|permission|canon|
  authority` over both files: all hits are bounded negations or bounds, none assert a
  finding, verdict, resolution, rights grant, or canon truth.

## 5. Cross-checks, contradictions, bounds

- S4's report declares the same two sha256 values I measured; S4's reported tool
  receipts (check_bible CLEAN, support_check 20/20 PASS, map_obligations raw=20
  mapped=20 PASS) are identical to mine.
- Nit (report wording, not deliverable): S4's report says "lines 26-29 are the three
  replay commands"; the commands are on README lines 26-28 with the closing fence on
  line 29. The commands themselves are exactly as quoted and pass.
- S3's report note "README.md is still byte-identical to r97's" was true at S3's check
  time (pre-20:30) and is stale for the delivered tree; S4's report records the same
  and my hashes confirm the rewrite. Not a defect in either deliverable.
- Bounds of my receipts: the three tools are lexical preflight (row inventory,
  fixed-string anchors, spans, R9 modes, pointer↔row mapping), not whole-claim
  entailment or canon review; my wording review is a manual read of the delivered
  files, not a truth or rights assessment. The r95 map repair (S3's other ownership)
  is out of this seat's scope (V15 covers it).
- No stray writes: this seat wrote only its report and `V55-scratch/`.

## Bottom line

**PASS** — every command in S4's README runs as written on the delivered bytes with
exit 0 (check_bible CLEAN; support_check 20/20, 2/2, 22/22, 18/18 anchors PASS;
map_obligations raw=20 mapped=20 PASS), counts 6/1/7 entities/relations/events plus
7 sources and 20 obligations (17 inherited unchanged + J18/J19/J20) all match the
JSON and tool receipts, and the scope wording (institutional filing, no finding, no
verdict, no resolution, no winner, rights unassessed) is consistent with the excerpt
and JSON; both file hashes stable at verification and re-confirmed at the end
(README `32efc78f…`, map `c1099d0e…`), S4 report present at poll try 13.

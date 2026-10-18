# V42 — receipt-wording (round 98)

Seat: **V42 receipt-wording** — verifier. Mandate: audit the declared receipt ratios
(**20/20 obligations vs TOTAL 22/22; 17/17; 6/6; 172 census**) against measured outputs on the
delivered revision; produce a corrections list.

Baseline: r97 closure `9a3d648` (pre-round bytes via `git show 9a3d648:<path>`); HEAD during the
round `dd4df1b` (wave tree uncommitted). All commands run from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no
commits, no network. Writes: this report (absolute path) and
`.ufo/waves/round-98/seats/V42-scratch/` only (census harness, mirror trees, captured receipts).

## 0. Poll-wait record (artifact-based; no plan was ever verified)

Poller `V42-scratch/V42-poll.sh` (20 s cadence, 40 tries, logged to `V42-scratch/V42-poll.log`);
endgame convention applied — the all-reports check enumerates `S1..S5` reports only (SELF = V42
never waited on).

- try 1 20:29:29 — `corpus/fixtures/r98-clerk-filing/` present as 10 **r97 byte-copies**
  (dir created 20:28:24); no pins, no reports.
- **Mid-flight nuance recorded (the r98 placeholder class V46 also observed):** my first
  `map_obligations.py corpus/fixtures/r98-clerk-filing` run (~20:28:45, before S3's 20:28:55
  content write) printed `OBLIGATIONS raw=17 mapped=17 … RESULT PASS` — r97-shaped, because both
  the JSON tables and the map were still r97 byte-copies. A second run (~20:29:30, after the JSON
  write) printed `raw=20 mapped=17 … RESULT FAIL` with three `missing_obligation` findings (map
  still the r97 copy). **No receipt was claimed against either state.**
- try 5 20:30:49 — S4's r98 map landed; try 6 — S4's r98 README landed; try 11 20:32:49 — S1's
  r97+r98 pins landed; try 12–14 — S2's tools README, S5's notes/report landed; try 17 — S2's
  report landed; **try 19 20:35:29 — `ALL PRESENT`, S1's report landed** (the poll exited on its
  success condition, well inside the 40-try budget; no stall escape needed).
- All measurements below were taken on bytes verified hash-stable after the last producer write
  (r98 map `c1099d0e…`, README `32efc78f…`, r95 map `80440d61…`, tool `03d04365…`, contract
  `153ebc5b…`, tools README `1d299c16…`).

## 1. Ratio audit — declared vs measured

| Declared ratio | Measured on the delivered revision | Verdict |
|---|---|---|
| 20/20 obligations | `python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing` → `OBLIGATIONS raw=20 mapped=20` / `INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22` / `RESULT PASS`, exit 0 | **matches** |
| TOTAL 22/22 | same run (`TOTAL-ROWS 22/22`), and `python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing` → `INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18` / `RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22` / `SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; …; MODES 22/22; VALIDATED-ROWS 22/22` / `RESULT PASS`, exit 0 | **matches** |
| 17/17 | `map_obligations.py corpus/fixtures/r97-crossing-acknowledgment` → `raw=17 mapped=17` / `INVENTORY … 17/17; 2/2; 19/19` / `RESULT PASS`, exit 0; `support_check.py` same dir → `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19` / `RESULT PASS`, exit 0 | **matches** |
| 6/6 chain | `dependency_freeze.py` on each of the six pinned fixtures: `r88-m3` `events 2/2; dependency-edges 0/0; relations 0/0`, `r94` `3/3; 2/2; 1/1`, `r95` `4/4; 3/3; 1/1`, `r96` `5/5; 4/4; 1/1`, `r97` `6/6; 5/5; 1/1` (digest `3c922d20…`), `r98` `7/7; 6/6; 1/1` (digest `59a0f4fa…`) — each `RESULT PASS`, exit 0; contract pins now `['r88-m3-maya-cluster','r94-paired-crossing','r95-crossing-aftermath','r96-crossing-response','r97-crossing-acknowledgment','r98-clerk-filing']` | **matches** |
| 172 census | census harness `V42-scratch/census_v42.py` (repo-relative `check_bible.py` over every `corpus/fixtures/*` dir, VIOLATION-line count per the r94–r97 convention) → `{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}`; baseline `git ls-tree 9a3d648:corpus/fixtures` tree count = 171 | **matches** (171→172, 37→38 clean, negative 134 and 421 violation lines unchanged) |

Declared counts cross-checked independently of the tools: r97 `entities 5 / claims 5 / relations 1 /
events 6 / sources 6`; r98 `6 / 6 / 1 / 7 / 7` (declared "5/1/6→6/1/7, sources 6→7"). Inherited
rows parsed-value identical r97→r98 for `entities[0:5]`, `timeline[0:6]`, `sources[0:6]`,
`relations`, and the 4 non-authored files (`contradictions.json`, `inspiration-note.md`,
`relations.json`, `source-excerpt.md`) are byte-identical `cmp` to the r97 bytes; new event
`clerk-filing-open` has `depends_on: ["acknowledgment-aru-records"]` and tick 14. `check_bible.py
corpus/fixtures/r98-clerk-filing` → `CLEAN: schema, citations, relations, timeline; 0 violations`,
exit 0.

## 2. Supporting receipts (corrections-relevant wording checks)

**Map row inventory.** Parsed r97 map 19 rows vs r98 map 22 rows: new rows `J18/J19/J20` only;
S01/S02 parsed-identical; **all 17 inherited J-rows differ in exactly one column — the
path-qualification namespace (`r97-crossing-acknowledgment:*` → `r98-clerk-filing:*`)**; pointer,
source ID, excerpt path, span, mode, and anchor are identical. The r98 map prose itself declares
this ("only the path-qualification column names this fixture's cluster path", the r97 precedent),
and the tool receipts consume pointers, so no receipt changes. New-row anchors verified in-span by
`grep -nF` (J18 anchor line 60, J19 line 59, J20 line 59; spans 60, 59-60, 55-64 within the
64-line excerpt file).

**r95 repair.** `git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`
is exactly one line (the carried "new relation" sentence → relation sentence + "the new tick-11
aftermath event records one reported non-arrival on one occasion"). Receipts on a scratch
restoration of the pre-repair cluster (baseline bytes) vs the delivered cluster: `map_obligations`
(`raw=15 mapped=15 … RESULT PASS`), `support_check` (`SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS
2/2; … TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13 … RESULT PASS`), and `check_bible` (`CLEAN`) are
all **byte-identical pre/post** (`diff` empty).

**C1 calibration, independent mirror negatives** (baseline tool+contract vs delivered
tool+contract, each in a scratch mirror root under `V42-scratch/mirror-{base,live}/`; live contract
never modified):
- Corrupted persisted expectation (`self_test.expected.clean.exit` 0→1): baseline prints
  `SELF-TEST 15/16` / `FINDING SELF-TEST-MISMATCH: cases failed: ['clean']` / `RESULT FAIL`,
  **exit 1**; delivered prints `SELF-TEST 16/17` / same finding / `RESULT ERROR`, **exit 2** —
  exactly the declared exit-1→2 change.
- Path-less legacy pin + `--freeze`: baseline `FINDING SCOPE-REFUSED: … pin r95-crossing-aftermath
  already names None …` exit 2, pin unchanged; delivered `MIGRATED r95-crossing-aftermath:
  path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath` / `RESULT PASS` exit 0,
  pin now carries the path. Verify-only with a path-less pin: `FINDING CONTRACT-INVALID: pin
  r95-crossing-aftermath needs a repo-relative fixture path` exit 2. Different recorded path
  guard still refuses: `SCOPE-REFUSED … already names 'corpus/fixtures/r95-elsewhere'` exit 2.
- Delivered `--self-test` → `SELF-TEST 17/17` / `RESULT PASS` exit 0; the 16 inherited contract
  cases are **byte-identical** to `9a3d648` expectations; the 17th is `{exit: 2, finding_ids:
  ['SELF-TEST-MISMATCH']}`. `map_obligations.py --self-test` unchanged: `SELF-TEST CASES 25/25
  pinned` / `RESULT PASS` exit 0.

**C2 discharge, independent r97-edge REDUCTION** (scratch mirror `V42-scratch/mirror-red/`):
intact r97 fixture `RESULT PASS` exit 0; with the tick-13 edge dropped in the mirror copy
(`acknowledgment-aru-records.depends_on = []`) →
`FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on
['response-evin-salt-court']` exit 1. Pre-pin state (baseline tool+contract) on the r97 fixture →
`FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' …` exit 2 — the V46-recorded
unfrozen-edge gap is closed by the delivered pin.

**S2 tools README claims (each re-measured):** `SELF-TEST 15/16 … RESULT FAIL` baseline vs
`16/17 … RESULT ERROR` delivered ✓; migration demo ✓; `UNPINNED-FIXTURE` pre-pin ✓;
`CONTRACT-INVALID` verify-only ✓; same-named-different-path refusal ✓; chain 6/6 with the two
quoted receipts ✓; `map_obligations` 25/25 unchanged ✓.

**S1 producer report cross-check (landed try 19).** S1 declares tool `03d04365…` and contract
`153ebc5b…` — equal to my measured hashes; its quoted receipts (`SELF-TEST 17/17`, `15/16` pre-state
exit 1, `MIGRATED …`, chain digests `3c922d20…`/`59a0f4fa…`, r97-edge `REDUCTION-DETECTED` exit 1)
all equal my independent measurements; its 16-case-unchanged claim equals my byte-compare of the
contract expectations.

## 3. Corrections list

1. **"17 inherited rows unchanged" (LOG C3 and S4 README) is precise only for the tool-consumed
   fields.** Measured: all 17 inherited rows differ from r97 in exactly the path-qualification
   column (`r97-crossing-acknowledgment:` → `r98-clerk-filing:`). The r98 map prose itself states
   this, and no receipt is affected; a literal reading of "unchanged" over-reaches. Recommended
   qualifier: "unchanged except the declared path-qualification column".
2. **The "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and
   `dependency-freeze-contract.json`" claim is false as written in two delivered places** — S2's
   tools README (line 284) and S1's report (line 236, whose own preceding status bullet lists
   `corpus/tools/README.md` as modified). Measured: `git diff 9a3d648 --name-only -- corpus/tools/`
   lists **three** paths (`corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`,
   `corpus/tools/dependency_freeze.py`); S2's README landed at 20:34:06 and was already modified
   when the claim was written. Recommended: scope to the tool scripts, or add "and the README
   addendum".
3. **Process (not a defect in the delivered bytes):** existence-only polling on this round can be
   satisfied by r97 placeholder byte-copies (my first run and V46's observation) — content-aware
   polling (as V11/S5 adopted) is required before measuring; recorded so future receipts quote the
   post-rewrite hash.
4. **Process (recorded, not this lane's write):** an untracked `baseline-analyze.txt` (105 bytes,
   mtime 20:30) sits at the **parent** tree root `/home/vgpnk/Projects/shokunin/` — the r94-F01
   stray-write class, unattributed; recorded by S3's report (D5) and S1's report, existence
   confirmed here (`ls -la`, read-only). Not written by this seat.

No correction affects any measured ratio; all five declared ratios hold on the delivered bytes.

## 4. Non-claims

I did not judge narrative/entailment/canon/rights/chronology, S4/S5 prose quality beyond the
receipt wording above, or C1's contract prose beyond the presence and order of the named exit-2
checks and finding IDs. I did not re-run other seats' verifications; V10/V46 reports corroborate
the namespace-only row change independently. All five producer reports (S1–S5) were present and
S1's receipts cross-checked before this report was finalized.

## 5. Hygiene

Writes confined to this report and `V42-scratch/` (census harness, mirror trees, captured
receipts; mirrors are under the wave tree). No commits, no pushes, no network, no nested agents;
the delivered tools/contract/fixtures were never modified by this seat.

## Bottom line

**PASS** — all five declared receipt ratios measured true on the delivered revision (r98
`raw=20 mapped=20` / inventory `20/20; 2/2; 22/22`; r97 `17/17`; chain `6/6` with the r97 pin
discharging V46 and an independently reproduced tick-13-edge `REDUCTION-DETECTED`; census
`172/38/134/421`, zero non-0/1 exits), with wording-level corrections recorded (LOG/S4
"17 inherited rows unchanged" needs the namespace-column qualifier; S2 README line 284 and S1
report line 236's `git diff` claim lists three files, not two) plus two process observations
(placeholder-satisfiable existence polls; parent-tree stray `baseline-analyze.txt`), none
affecting any receipt.

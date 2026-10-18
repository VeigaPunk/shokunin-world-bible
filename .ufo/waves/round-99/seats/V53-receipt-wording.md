# V53 — receipt-wording (round 99)

Seat: **V53 receipt-wording** — verifier. Mandate: audit the declared receipt ratios
(**21/21 obligations vs TOTAL 23/23; 18/18; 6/6; 173 census**) against measured outputs on the
delivered revision; produce a corrections list.

Baseline: r98 closure `4265df5` (pre-round bytes via `git show 4265df5:<path>`). HEAD during the
round `337f0fa` (blocked-dispatch commit; wave tree uncommitted). All commands ran from the lane
root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no
commits, no pushes, no network. Writes: this report (absolute path) and
`.ufo/waves/round-99/seats/V53-scratch/` only.

Standing declaration read from `LOG.md` "Round 99 — declaration before dispatch": C2 component 1
is 6/1/8, 8 sources, 21 map obligations (20 inherited + 1 event), census 172→173; C1 is a
ten-file pin, self-test 17→18, chain re-frozen **6/6** (the existing six fixtures, not r99).

## 0. Poll-wait record (artifact-based; no plan was scored)

Poller `V53-scratch/poll.sh` (20 s cadence, 40 tries, log `V53-scratch/poll.log`). Endgame
convention: the all-reports check enumerates producer reports only (SELF = V53 never waited on).

- try 1 22:01:38 — `corpus/fixtures/r99-window-lapse/` present as an r98 placeholder (README still
  "Round 98 clerk-filing"). No producer reports. **No receipt was claimed against that state.**
- try 5 22:02:58 — content gate passed (README mentioned the lapse). S3's report was already on
  disk; map/README were still moving (S4).
- **Stall-escape 1 (harness, not absence):** the first poller was killed by a 300 s tool timeout
  after try 15 (22:06:18). Restarted the same script (nohup, pid 1757320). Recorded in `poll.log`.
- Restarted poll try 40 22:25:30 — `ABSENT after 40`. That ABSENT was a **filename miss**: the
  script required the r98 names `S1-freeze-hygiene.md`, `S2-tools-docs.md`,
  `S5-knowledge-notes.md`. This wave did not use those names.
- **Stall-escape 2:** a 6-try name-agnostic check at 22:52:29 found `S1-full-file-pins.md`
  (mtime 22:48). S2 and S5 **reports** were still absent at close (23:09). Their artifacts had
  landed and were audited directly: `corpus/tools/README.md` and `SKILL.md` (mtime 22:51:39);
  `corpus/knowledge/r99-gate-blind-spot-table.md` and `r99-lapse-scope-note.md` (mtime 22:57:50).

Final measurements below are on bytes re-hashed at 23:09:42, unchanged since the post-22:38
re-run: tool `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`, contract
`8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`, r99 README
`b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`, r99 map
`d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`. An earlier self-test on the
pre-refreeze contract (pins still schema-less, five files) printed `SELF-TEST 4/18` /
`CONTRACT-INVALID` exit 2. **That mid-flight receipt was not claimed.**

## 1. Ratio audit — declared vs measured

| Declared ratio | Measured on the delivered revision | Verdict |
|---|---|---|
| 21/21 obligations | `python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse` → `OBLIGATIONS raw=21 mapped=21` / `INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23` / `RESULT PASS`, exit 0. Independent count: 6 `first_appearance` + 6 claims + 1 relation + 8 events = 21. Map file has J01–J21 + S01–S02 (23 rows). | **matches** |
| TOTAL 23/23 | same `map_obligations` run (`TOTAL-ROWS 23/23`). `python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse` → `INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19` / `RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23` / `SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; …; MODES 23/23; VALIDATED-ROWS 23/23` / `RESULT PASS`, exit 0. `check_bible.py` on the same dir → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. | **matches** |
| 18/18 | `python3 corpus/tools/dependency_freeze.py --self-test` → 18 `CASE … ok` lines, including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`, then `SELF-TEST 18/18` / `RESULT PASS`, exit 0. Contract `self_test.expected` has 18 keys; the only addition vs `git show 4265df5:…` (and vs `HEAD`, which is byte-identical for that file) is `markdown_tamper`; the other 17 expectation objects are identical (`changed inherited []`). | **matches** (this 18/18 is the freeze self-test, not anchors — see corrections) |
| 6/6 chain | `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` on each of r88, r94, r95, r96, r97, r98: each `RESULT PASS`, exit 0. Receipts: r88 `events 2/2; dependency-edges 0/0; relations 0/0` digest `acf677a7085be3f6…`; r94 `3/3; 2/2; 1/1` `048b8ff39e4a5232…`; r95 `4/4; 3/3; 1/1` `97cffd7bfe6e0c92…`; r96 `5/5; 4/4; 1/1` `43911900923c110b…`; r97 `6/6; 5/5; 1/1` `a28b9ea0d65ec355…`; r98 `7/7; 6/6; 1/1` `5ecf84e19121ea12…`. Each pin has `payload_schema_version` 2 and exactly the ten declared files. | **matches** (six fixtures, not seven — r99 is unpinned) |
| 173 census | `python3 .ufo/waves/round-99/seats/V53-scratch/census_v53.py final` (repo-relative `check_bible.py` over every `corpus/fixtures/*` dir, VIOLATION-line count per the r94–r98 convention) → `{"fixture_dirs": 173, "clean_exit0": 39, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}`. `ls -d corpus/fixtures/*/ \| wc -l` → `173`. Baseline `git ls-tree -d --name-only 4265df5:corpus/fixtures` → 172. | **matches** (172→173; clean 38→39; negative 134 and 421 violation lines unchanged) |

Declared shape cross-checked independently of the ratio tools: r98 `entities 6 / relations 1 / timeline 7 / sources 7`; r99 `6 / 1 / 8 / 8`. Parsed prefixes equal (`entities` identical, `timeline[:7] == r98`, `sources[:7] == r98`, `relations` identical). New event `clerk-lapse-recorded` is tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on: ["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. r98 `map_obligations` still prints `raw=20 mapped=20` / `TOTAL-ROWS 22/22` / `RESULT PASS`, exit 0 — the 21/23 receipts are the r99 increment, not a recount of r98.

JSON-table digests vs `4265df5` pins: for all six chain fixtures, the five JSON file digests, `events`, `relations`, and `counts` are unchanged; only `content_sha256` moved (Markdown files now in the payload). That matches S1's report and the tools README r99 addendum (line 306). Contract `revision` is `337f0fa52b02626b7687eedbb2d99fab30446fe4` (HEAD), not `4265df5`. The README states that revision explicitly.

`r99-window-lapse` is not on the chain. Verify-only:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT:2
```

That matches the declaration (6/6, not 7/7) and S1's report ("`r99-window-lapse` was not pinned").

Supporting probe (scratch mirror; delivered fixture and contract not modified). Append one newline to `fictional-excerpts.md` inside a mirror root whose tool `ROOT` is the mirror, then verify:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 3e992626a155faba… != pin 5ecf84e19121ea12…; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80… -> a6bff890dd8821e2…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

A same-named copy at a foreign path, without a mirror root, exits 2 `PATH-MISMATCH` before the digest check. That is the r97 path binding, not a failed tamper.

## 2. Producer and doc wording checked against those receipts

**S1** (`S1-full-file-pins.md`). Quoted chain digests and the `SELF-TEST 18/18` line equal the re-run above. "17 inherited expectation objects identical to HEAD" is true (`HEAD` contract == `4265df5` contract; 17 identical, added `markdown_tamper` only). "Five JSON file digests unchanged" is true for all six pins (script in section 1).

**S4** (`S4-fixture-docs.md`). Quoted map sha `d2fe20e5…` and README sha `b9320941…` equal the files on disk. Quoted gates (`21/21`, `TOTAL-ROWS 23/23`, `DISTINCT-ANCHORS 19/19`, `raw=21 mapped=21`) equal the re-run. "20 inherited rows unchanged modulo namespace" matches the row compare below.

**S3** (`S3-fixture-author.md`). Counts 6/1/8 and `check_bible` CLEAN were true. The follow-up that the map is still the r98 map, and the PASS line "seven inherited files byte-identical", are **not** true of the delivered tree. See corrections.

**S2 artifact, report absent.** `corpus/tools/README.md` r99 addendum (line 344) says the self-test prints `SELF-TEST 18/18` / `RESULT PASS` exit 0 — matches. Line 339 digest prefixes match the six measured digests. `SKILL.md` freeze row says 18 cases and ten files per pin — matches. Historical r98 sentences that still say `17/17` and "five JSON tables only" are explicitly superseded in the same addendum (lines 296–298); they are history, not the live receipt.

**S5 artifact, report absent.** `r99-lapse-scope-note.md` quotes `21/21`, `TOTAL-ROWS 23/23`, `DISTINCT-ANCHORS 19/19`, and census `ls -d corpus/fixtures/*/ | wc -l` = 173. All four match this pass. Tool shas it cites (`check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`) match `sha256sum`. The blind-spot table header quotes chain 6/6 and `SELF-TEST 18/18` — both match. Mutation-row replays in that table were **not** re-run by this seat; only the ratio sentences were.

## 3. Corrections list

1. **"20 inherited rows unchanged" (LOG C2, and r99 README line 21 "carried unchanged") is precise only for the tool-consumed fields.** Measured: all 20 inherited J-rows differ from the r98 map in exactly one column — the path-qualification namespace (`r98-clerk-filing:` → `r99-window-lapse:`, column index 3). Pointer, source id, excerpt path, span, mode, and anchor are identical. S01/S02 are byte-identical. J21 is the only new row. S4's report already says "unchanged modulo namespace", and the map discloses the inherited namespaces. No receipt changes (`map_obligations` compares as a set and PASSes). Recommended qualifier: "unchanged except the declared path-qualification column".

2. **S3's report is stale on the delivered tree.** The "Not done" section says README and `claim-excerpt-map.md` still say r98 (20 obligations, 6/1/7) and that the gates should be expected to see the inherited r98 map. The PASS line says seven inherited files are byte-identical to `4265df5` r98. That was true at S3's write (22:01). After S4, README sha is `b9320941…` (not the r98 `32efc78f…`) and the map sha is `d2fe20e5…`, and both gates print 21/21 and 23/23. Do not cite S3's follow-up as the delivered receipt.

3. **`corpus/fixtures/README.md` still ends at the r98 census (line 1263: 172/38/134/421).** Measured this pass: **173/39/134/421**, zero non-0/1 exits. That file is outside producer ownership, so the lag is expected, not a failed LOG ratio (LOG says 172→173, and 173 was measured). A citation of the fixtures README as the current census would be wrong.

4. **Do not conflate the four "18" / "6" surfaces.** `18/18` in this mandate is `SELF-TEST 18/18` only. `support_check` prints `DISTINCT-ANCHORS 19/19`, not 18/18. The chain `6/6` is six fixtures each `RESULT PASS`, not r98's `dependency-edges 6/6` (that edge count is one field of the r98 receipt, which also passed). r99 is `UNPINNED-FIXTURE` exit 2; a "7/7" reading of the declaration would be wrong. No landed producer report claimed 7/7 or anchors 18/18.

5. **S1 line 5 ("tracked diff is only the two owned files") is true of S1's writes at 22:48 and false of the tree at this audit.** `git diff --name-only HEAD` now lists `SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`, and `corpus/tools/dependency_freeze.py`. `git diff --name-only 4265df5` also lists `LOG.md` and `SCORECARD.md` (the blocked-dispatch commit, already in HEAD). Not a ratio defect. The r99 fixture and the two knowledge files are untracked, so they do not appear in either diff.

No correction moves any of the five declared ratios.

## 4. Non-claims

I did not judge narrative, entailment, canon, rights, or chronology. I did not replay the blind-spot table's mutation rows. I did not re-run `--freeze` (it rewrites the contract; S2's README says not to). S2 and S5 seat reports were absent at 23:09, so report-only sentences in those two seats were not cross-checked; their delivered files were. S1, S3, and S4 reports were read.

## 5. Hygiene

Writes confined to this report and `V53-scratch/` (poll log, census harness and `census_final_receipts.json`, tamper mirror, captured self-test/chain/gate text). No commits, no pushes, no network, no nested agents. Delivered tools, contract, fixtures, and knowledge files were not modified by this seat.

## Bottom line

**PASS** — all five declared receipt ratios match measured output on the delivered revision (r99 `raw=21 mapped=21` / inventory `21/21; 2/2; 23/23`; freeze `SELF-TEST 18/18` exit 0 with `markdown_tamper` naming `DIGEST-MISMATCH`; chain 6/6 exit 0, r99 unpinned exit 2; census `173/39/134/421`), with wording corrections that do not move any ratio (LOG/README "20 inherited rows unchanged" needs the namespace-column qualifier; S3's follow-up is stale after S4; fixtures README census line still says 172/38/134/421; do not read 18/18 as anchors or 6/6 as r98's edge count).

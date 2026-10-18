# V25 — doc-parity (round 99)

Seat: **V25 doc-parity** — verifier. Scope: pre-integration documentation parity for the closure-pass documents — `corpus/fixtures/README.md` (Round-99 section, census 173 expected), `corpus/README.md` bullets (r99 fixture; 18-case freeze self-test; ten-file payload), `SKILL.md` freeze-row state, `corpus/knowledge/r91-c9-watch.md` r99 row — plus the stale-wording list. Axes: completeness of those five items, evidence fidelity (quoted commands), freshness (delivered bytes, not plans), non-harm (read-only outside this report and `.ufo/waves/round-99/seats/V25-scratch/`).

Baseline named in the r99 declaration: `4265df5`. Working-tree HEAD at measurement was `337f0fa` (`lore r99: record blocked dispatch attempt`), one commit past `111b9a3` (r98 SCORECARD). `git diff --stat 4265df5..HEAD` is only `LOG.md` and `SCORECARD.md` (123 insertions). Corpus docs below were compared to `4265df5`, not to HEAD.

## 1. Unowned closure docs are still the r98 bytes

Snapshot 22:25:13. All five documentation files that a closure pass would edit were byte-identical to `4265df5`. `git status --porcelain` outside `.ufo/` was only `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, and the untracked `corpus/fixtures/r99-window-lapse/` tree. No unowned doc drift.

```sh
for f in SKILL.md corpus/README.md corpus/fixtures/README.md \
         corpus/knowledge/r91-c9-watch.md corpus/tools/README.md; do
  now=$(sha256sum "$f" | awk '{print $1}')
  base=$(git show 4265df5:"$f" | sha256sum | awk '{print $1}')
  # all five printed IDENTICAL
done
# SKILL.md                         22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5
# corpus/README.md                 dee558be7a819de16ec3922784cd7261956776bf2975aab6ab88460038de6076
# corpus/fixtures/README.md        e401cc64d1b79680153cc2d026ed7a3599974afd2e29ee080b492238d364c57b
# corpus/knowledge/r91-c9-watch.md ced043984ee1798de4442cf8a6a9f4eb2480244252eb9ae733b532ae327ab9dc
# corpus/tools/README.md           294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207
```

`rg -n "Round 99|r99|18 cases|ten-file|ten files|payload_schema_version 2"` over those five files returned one hit, and it is a forward pointer, not an r99 row: `corpus/knowledge/r91-c9-watch.md:319` ends "Next re-check: r99."

## 2. Item inventory

### 2a. `corpus/fixtures/README.md` — Round-99 section ABSENT; census 173 measured

File ends at the Round-98 section (`:1244`) and the r98 census re-declaration (`:1261`–`:1265`). No `## Round 99` heading.

`:1263` still declares the r98 census: **172 fixture directories: 38 clean (exit 0), 134 intentional negative (exit 1), 421 violation lines, zero non-0/1 exits**.

Independent census at the delivered fixture tree (`.ufo/waves/round-99/seats/V25-scratch/census_v25.py`, repo-relative `check_bible.py` per direct fixture dir, same counting rule as the r98 V22 census):

```sh
python3 .ufo/waves/round-99/seats/V25-scratch/census_v25.py
# {"clean": 39, "dirs": 173, "negative": 134, "non01": [], "r99": {"exit": 0, "violations": 0}, "r99_present": true, "violation_lines": 421}
```

The Round-99 re-declaration must supersede `:1263` with **173 / 39 / 134 / 421 / zero non-0/1**. One directory added (`r99-window-lapse`), clean 38→39, negative and violation lines unchanged. That increment is measured, not planned.

`:1259` is the other sentence the Round-99 section must supersede in its own text (historical bytes stay): self-test "17 cases"; frozen chain "six fixtures — r88-m3, r94, r95, r96, r97, r98"; "the pin payload covers the five JSON tables only (fixture Markdown is not pinned); BR-01's prose half remains open."

Measured replacement facts (not a seventh chain member — see §3): self-test **18/18**; pin payload **ten files**, `payload_schema_version` 2; chain still the same six, verifying 6/6; `r99-window-lapse` is **not pinned** (`UNPINNED-FIXTURE`, exit 2). BR-01's prose half is edit-detectable (`DIGEST-MISMATCH` names the file) and is still not semantics-provable. The Round-99 section must not say the frozen chain is seven fixtures.

Fixture shape the section should record, read from the delivered tables and confirmed by the gates in §3: preserving continuation of `r98-clerk-filing`; 6 entities / 1 relation / 8 events / 8 sources / 0 contradictions; new source `clerk-lapse-note`; new tick-15 event `clerk-lapse-recorded` (actor `clerk-maren`, place `chalk-stair`, `depends_on: ["clerk-filing-open"]`); 21 map obligations (20 inherited + the new event row). The lapse record says the crossing-window named in the original minute has closed, the agreement was unfulfilled, no claim was lodged, and the matter stands as a historical open entry. Excerpt lines 70–74 and the source reliability note assert no resolution, no blame, and no reconciliation. Inherited entity and relation arrays are parsed-value identical to r98; timeline and sources prefixes are the r98 arrays.

### 2b. `corpus/README.md` — bullets stale (r99 fixture; 18-case; ten-file payload)

- **Missing fixture bullet.** The myth-comparison list ends at `fixtures/r98-clerk-filing/README.md` (`:25`). There is no `r99-window-lapse` bullet. Expected: a fifth-beat bullet — window closed per the original minute, agreement unfulfilled, no claim lodged, matter stays open; 6/1/8, 8 sources, 21 obligations; navigate `claim-excerpt-map.md` and `fictional-excerpts.md`. No resolution, blame, or reconciliation.
- **`:40` `tools/dependency_freeze.py` bullet — two stale clauses, one still-true clause.** "(rounds 96–98)" and "17-case persisted self-test" and "the pin payload covers the five JSON tables only" are stale. The chain clause "r88-m3 → r94 → r95 → r96 → r97 → r98" is still the delivered chain: r99 is not a pin. Expected: 18-case self-test; ten-file payload (`payload_schema_version` 2); chain remains those six. Do not append r99 to that arrow.
- **`:33` C9 bullet.** "including the r93 re-check entry" is stale by five rounds. The log holds rows through r98, and an r99 row is due. Expected after the closure row: a phrase covering the r93–r99 re-check entries (or equivalent).
- **`:39` `map_obligations` bullet** ("rounds 94–97", "25 persisted cases") is unchanged by the r99 claims. Leave it.

### 2c. `SKILL.md` freeze-row state — still the r98 text; S2 update ABSENT

S2 owns this row. At 22:36:25 there was no `S2*.md` report, and `SKILL.md` was still the `4265df5` hash. Current row, and which tokens are stale against the delivered tool:

- `:96` frozen chain lists the six fixtures through `r98-clerk-filing`. **Still accurate.** Do not add `r99-window-lapse` unless a later pin appears. None had at 22:11 or 22:36.
- `:98` "17 cases (r97 added `SCOPE-REFUSED`, `PATH-MISMATCH`; r98 added `self_test_mismatch`)" — **stale.** Delivered contract `self_test.expected` has 18 names, including `markdown_tamper` (`exit` 2, `finding_ids` `["DIGEST-MISMATCH"]`, `names_file` `fictional-excerpts.md`).
- `:99` "content SHA-256 over the five JSON tables" — **stale.** "exactly the six chain fixtures" — **still accurate.** Contract `pinned_files` is the five JSON tables plus `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`. Top-level `schema_version` 2 and `payload_schema_version` 2. Each of the six pins has `payload_schema_version` 2 and 10 file digests. Pin `revision` on all six is `337f0fa52b02626b7687eedbb2d99fab30446fe4` (working HEAD at freeze time), not `4265df5`. A closure sentence that says the pins were taken at `4265df5` would be false.
- `:100` "the pin payload covers the JSON tables only — fixture Markdown (maps, excerpts) is not pinned; BR-01's markdown/prose half remains open." — **stale.** Markdown edits of pinned files exit 2 `DIGEST-MISMATCH` and name the file (§3). The prose half is edit-detectable, not semantics-provable. The path-binding, `--freeze` scope guard, and path-less migration sentences in this row are not contradicted by this round's claim and were not re-probed here.

`:87` (`map_obligations` "25 cases") — no change expected, and that file was not in the porcelain set.

### 2d. `corpus/knowledge/r91-c9-watch.md` — r99 row ABSENT (due)

Last check-log row is `:319` (r98, re-check 7) ending "Next re-check: r99." The file ends at `:321`. No r99 section. No round-99 producer owns this watch.

Pre-verified content for that row, reproduced at 22:08 on the delivered checker (hash unchanged from the r98 row):

```sh
sha256sum corpus/fixtures/check_bible.py
# ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
python3 corpus/tools/discriminate_check.py
# RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
# EXIT:0
python3 corpus/tools/discriminate_check.py --checker e97613c
# REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
# EXIT:2
```

Expected r99 row: checker pin `ff9fd2aa…d1421`; DISCRIMINATION HELD; control REGRESSION-DETECTED; ruling retained; next re-check r100. Only the append is pending. This does not verify S5's blind-spot table; those files were absent (§5).

## 3. Receipts the closure sentences depend on (delivered bytes)

Fixture gates, run from the lane root after S4's README and map had landed (README sha256 `b93209417a918a88…`, map sha256 `d2fe20e581d1c29b…`, matching S4's report):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
# CLEAN: schema, citations, relations, timeline; 0 violations
# EXIT:0
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
# OBLIGATIONS raw=21 mapped=21
# INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
# RESULT PASS
# EXIT:0
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
# SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
# RESULT PASS
# EXIT:0
```

`support_check` PASS J21 cited excerpt line 70: `Tick 15: The crossing-window named in the original minute has closed.`

Freeze, after the contract pins reached ten-file schema v2 (22:11:28). Tool sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`. Contract sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. Same two hashes again at 22:25:13.

```sh
python3 corpus/tools/dependency_freeze.py --self-test
# CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
# SELF-TEST 18/18
# RESULT PASS
# EXIT:0
```

The 18 case names in `self_test.expected`: the prior 17 plus `markdown_tamper`. Chain:

```sh
# r88-m3-maya-cluster          FREEZE events 2/2; dependency-edges 0/0; relations 0/0  RESULT PASS  EXIT:0
# r94-paired-crossing          FREEZE events 3/3; dependency-edges 2/2; relations 1/1  RESULT PASS  EXIT:0
# r95-crossing-aftermath       FREEZE events 4/4; dependency-edges 3/3; relations 1/1  RESULT PASS  EXIT:0
# r96-crossing-response        FREEZE events 5/5; dependency-edges 4/4; relations 1/1  RESULT PASS  EXIT:0
# r97-crossing-acknowledgment  FREEZE events 6/6; dependency-edges 5/5; relations 1/1  RESULT PASS  EXIT:0
# r98-clerk-filing             FREEZE events 7/7; dependency-edges 6/6; relations 1/1  RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
# FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' ...
#   (pinned: the six names above)
# RESULT ERROR
# EXIT:2
```

That unpinned result matches the declaration (re-freeze the existing chain 6/6; r99 is not declared as a seventh pin). A closure sentence that pins r99, or that says the chain is seven, would over-claim the delivered contract.

Markdown tamper, replayed through the tool's own `markdown_tamper` case (trailing newline on `fictional-excerpts.md` in an isolated mirror; delivered contract not modified):

```text
FINDING DIGEST-MISMATCH: content digest dbf67f5c107b19eea87ad5311e634db2ae54b8760a92c0430060e61635ad6102 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> a89d278834f74cdeb87d0a46fca94cfd41a0f7cc4fa1c565b2b50c2b5912d7db); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT: 2
```

The self-test treats that case as ok only if `fictional-excerpts.md` appears in the output (`dependency_freeze.py:611`). It printed ok. This is edit detection, not a proof that the prose means anything.

Mid-write, recorded not final: at 22:04:30 the tool already required `payload_schema_version` 2, but each pin still lacked it (`files` was the five JSON digests). `--self-test` printed `SELF-TEST 4/18`, `FINDING SELF-TEST-MISMATCH`, `RESULT ERROR`, exit 2, with most cases observing `CONTRACT-INVALID: pin r95-crossing-aftermath payload_schema_version None != 2`. Poll try=11 (22:09:02) was the first try with `ten_v2=6`. The 22:11 receipts above are the post-upgrade bytes, and the hashes were unchanged at 22:25.

## 4. Stale-wording list (for the closure doc pass)

1. `corpus/fixtures/README.md:1263` — census 172/38/134/421. Needs a Round-99 re-declaration **173/39/134/421 / zero non-0/1** (measured in §2a) and a Round-99 section (absent).
2. `corpus/fixtures/README.md:1259` — "17 cases"; "five JSON tables only"; "BR-01's prose half remains open." The six-fixture chain list in that sentence is still true; do not extend it to r99.
3. `corpus/README.md:25` — list ends at the r98 bullet. No `r99-window-lapse` navigation bullet.
4. `corpus/README.md:40` — "17-case"; "five JSON tables only." Chain arrow through r98 is still the delivered pin set.
5. `corpus/README.md:33` — C9 bullet still says "including the r93 re-check entry."
6. `SKILL.md:98` — "17 cases." S2 owns this row and had not written it by 22:36.
7. `SKILL.md:99` — "five JSON tables." The "exactly the six chain fixtures" clause is still true. If the row quotes a pin revision, the delivered value is `337f0fa…`, not `4265df5`.
8. `SKILL.md:100` — "fixture Markdown … is not pinned; BR-01's markdown/prose half remains open."
9. `corpus/knowledge/r91-c9-watch.md` — no r99 row (due; content pre-verified in §2d). `:319` already points at r99.
10. `corpus/tools/README.md` (S2-owned; still the `4265df5` hash; no S2 report) — no Round-99 addendum. Stale against the delivered tool: `:236` and `:276` "17 cases"; `:238` "five JSON tables only" and "BR-01's markdown/prose half remains open"; `:279` documents `SELF-TEST 17/17`. The six-fixture chain statements at `:236`–`:237` are still true. The r98 closure supersession at `:286`–`:288` (gitignore class; "lists only two files") is historical and was not re-opened by this measurement.

Not stale, and must not be "fixed" into falsehood: `SKILL.md:96` and the chain-membership clauses above. `r99-window-lapse` verifies as `UNPINNED-FIXTURE` exit 2.

Not verified, because the files were absent: `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md`. Nothing in the five closure docs cites them yet, so their absence does not add a stale sentence. It does mean this inventory does not confirm component 2 of C2.

## 5. Poll record

Poll script `.ufo/waves/round-99/seats/V25-scratch/poll.sh`, log `poll.log`. Cadence 20s, 40 tries, 22:05:42 through 22:18:42, then `TIMEOUT tries=40 ts=2026-10-17T22:19:02-03:00`. Gate was S1 report and S2 report and S5 report and at least one `corpus/knowledge/r99-*` file. That gate never opened.

- try=1–10: contract header already `schema=2 payload=2 cases=18`, pins still `ten_v2=0`.
- try=11 (22:09:02) through try=40: `pins=6 ten_v2=6 cases=18`, and still `s1rep=0 s2rep=0 s5rep=0 know=0 skill18=0 tools18=0`.
- 22:36:25 recheck (bounded stall-escape, 17 minutes after timeout): `S1*.md`, `S2*.md`, `S5*.md`, and `corpus/knowledge/r99*` still absent. Not treated as fatal to the inventory of bytes that had landed. Not used to verify S2's or S5's planned text.

Producer reports on disk: `S3-fixture-author.md`, `S4-fixture-docs.md`. S3's report says README and the map were still r98 copies at its write time; that was true then and is stale for the delivered tree (S4 rewrote both; gates in §3 ran on those bytes). S1's tool and contract landed without a report. S2's two owned docs did not change. S5's two knowledge files did not appear.

Endgame convention: this seat did not poll for every verifier report, and any such count must subtract SELF. This report is the SELF file.

## 6. Bottom line

**PASS (pre-integration doc-parity inventory)** — the four closure docs are byte-identical to `4265df5` (no unowned drift); Round-99 section absent; census independently **173/39/134/421** with `r99-window-lapse` exit 0; corpus README still lacks the r99 bullet and still says 17-case / five JSON tables; SKILL.md freeze row is still the r98 text (17 cases, five JSON tables, prose half open) because S2 had not written; C9 r99 row absent and its pair reproduced (`ff9fd2aa…d1421`, DISCRIMINATION HELD exit 0, control REGRESSION-DETECTED exit 2). Delivered freeze, measured not planned: self-test 18/18, ten-file pins on the existing six, chain 6/6, r99 `UNPINNED-FIXTURE` exit 2, markdown tamper `DIGEST-MISMATCH` naming `fictional-excerpts.md`. Ten stale anchors are listed for the closure pass. **ABSENT, not verified:** S1/S2/S5 reports after 40 polls plus a 22:36 recheck, and both S5 knowledge files — the blind-spot table was not checked.

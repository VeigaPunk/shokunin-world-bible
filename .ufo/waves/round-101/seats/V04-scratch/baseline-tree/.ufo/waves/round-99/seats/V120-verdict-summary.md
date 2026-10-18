# V120 — verdict-summary (round 99)

Seat: V120 verdict-summary. Report path (resolved before write): `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V120-verdict-summary.md`. Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline named by the standing r99 declaration: `4265df5`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `seats/V120-scratch/` only.

Charter: after V28–V33 and the six verdict-crosschecks land, tabulate them and flag unresolved divergence for the adjudicator (V34). Roster source (read, not authored): `seats/V99-scratch/roster.txt` lines 33–38 and 56, 57, 74, 87, 96, 112, 125.

| Axis | Verdict seat | Crosscheck |
|---|---|---|
| calibration | `V28-verdict-calibration.md` | `V52-crosscheck-calibration.md` |
| depth | `V29-verdict-depth.md` | `V51-crosscheck-depth.md` |
| coverage | `V30-verdict-coverage.md` | `V69-crosscheck-coverage-2.md` |
| operability | `V31-verdict-operability.md` | `V82-crosscheck-operability.md` |
| freshness | `V32-verdict-freshness.md` | `V91-crosscheck-freshness.md` |
| adjacency | `V33-verdict-adjacency.md` | `V107-crosscheck-adjacency.md` |

This seat did not re-run gates and did not score C1 or C2. Bottoms below are quoted from the files named. A missing file is ABSENT. A landed file that itself says ABSENT was not turned into a pass.

## 1. Poll record

`V120-scratch/poll.sh`. Cadence 20 s, max 40. SELF excluded. A file counted as landed only if non-empty and carrying a bottom-line marker. Gate was all 12 reports plus the declared artifacts plus S1–S5 reports. The script exited 2.

```
POLL_START 2026-10-17T22:30:07-0300 self=V120 excluded
try=1  t=2026-10-17T22:30:07-0300 art_miss=2 prod=2/5 verdicts=1/12
try=40 t=2026-10-17T22:43:07-0300 art_miss=2 prod=2/5 verdicts=7/12 miss=[ V28-verdict-calibration.md V30-verdict-coverage.md V31-verdict-operability.md V69-crosscheck-coverage-2.md V107-crosscheck-adjacency.md] prod_present=[ S3-fixture-author.md S4-fixture-docs.md]
POLL_EXPIRE try=40 2026-10-17T22:43:07-0300 art_miss=2 prod=2/5 verdicts=7/12
```

Observed process result: `POLL_EXPIRE`, exit code 2. That is the stall-escape. No try 41.

Landing inside the window (inferred from which names dropped out of `miss=`): V33 by try 1; V91 by try 7 (22:32:07); V32 by try 8; V29 by try 12 (22:33:47); V52 by try 25 (22:38:07); V51 by try 36 (22:41:47); V82 by try 37 (22:42:07). Still missing at expire: V28, V30, V31, V69, V107.

Post-expire reads are not extra protocol tries. They are recorded because files appeared after the cap and before this write. The 23:06:57 recheck is the roster this table uses.

## 2. Commands this seat ran

Producer/artifact check at `2026-10-17T22:47:38-0300` (the `ls` of missing paths made the shell exit 2; that exit is the absence evidence):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207  corpus/tools/README.md
22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5  SKILL.md
$ stat -c '%y %n' corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
2026-10-17 22:38:11.814368253 -0300 corpus/tools/dependency_freeze.py
2026-10-17 22:08:46.248249589 -0300 corpus/tools/dependency-freeze-contract.json
$ git diff --quiet 4265df5 -- corpus/tools/README.md; echo readme_vs_4265df5_exit=$?
readme_vs_4265df5_exit=0
$ git diff --quiet 4265df5 -- SKILL.md; echo skill_vs_4265df5_exit=$?
skill_vs_4265df5_exit=0
$ git diff --quiet 4265df5 -- corpus/tools/dependency_freeze.py; echo tool_vs_4265df5_exit=$?
tool_vs_4265df5_exit=1
$ ls corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access 'corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access 'corpus/knowledge/r99-lapse-scope-note.md': No such file or directory
```

Same tool/contract hashes again at `2026-10-17T22:51:58-0300`. Knowledge files still missing (`knowledge_ls_exit=2`). At that instant S1's report existed and S2/S5 did not:

```
PRESENT S1-full-file-pins.md bytes=11971 mtime=2026-10-17T22:48:57-0300 sha256=1fda9ff7f02e75c9b34d0f0e514cbc8f799f596bb0cedc2d363fd6f33aee54a3
ABSENT  S2-tools-docs.md
PRESENT S3-fixture-author.md bytes=5069  mtime=2026-10-17T22:01:40-0300 sha256=3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a
PRESENT S4-fixture-docs.md   bytes=9303  mtime=2026-10-17T22:03:54-0300 sha256=61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f
ABSENT  S5-knowledge-author.md
```

S1 was not read. No verdict in this set cites it. V28's last S1 check (quoted in V28) is `22:48:54`, three seconds before this mtime.

Verdict-file recheck at `2026-10-17T23:06:57-0300` (python `sha256` of the bytes on disk):

```
PRESENT V28-verdict-calibration.md   bytes=8670  mtime=22:50:40 sha256=84058e09fb813032d715897f43f808078d95badce05ddfe3a5640dba2451a344
PRESENT V29-verdict-depth.md         bytes=18341 mtime=22:33:40 sha256=1f8eb8316b844dd64cd832561976dfddbd98c2674778a2d2fef8d5eb156b5e1e
ABSENT  V30-verdict-coverage.md
PRESENT V31-verdict-operability.md   bytes=13039 mtime=22:51:03 sha256=b7b19a4b7dc226983e63b226274598e48836ac7ebd7152b5f3f8c8e15e87991d
PRESENT V32-verdict-freshness.md     bytes=5550  mtime=22:32:25 sha256=e94a49e63825fcdeaad4561b45dec05d8676b255317dbe3008e778ca098ad711
PRESENT V33-verdict-adjacency.md     bytes=7506  mtime=22:27:58 sha256=61ba3ac0f6f3aced04ff5d3764086f7136cb7869ccd5ab24a25b512ec9448138
PRESENT V51-crosscheck-depth.md      bytes=22374 mtime=23:04:28 sha256=02f0c48bd9afdc3cd31fe5ab2008afffbf4d2f9c10cbb99f92702950b0f385a4
PRESENT V52-crosscheck-calibration.md bytes=4890 mtime=22:37:55 sha256=d4253addd96a9b99faa0fa702292696d08844ea70b8a4f3fd5f254dad2950073
ABSENT  V69-crosscheck-coverage-2.md
PRESENT V82-crosscheck-operability.md bytes=7817 mtime=22:41:53 sha256=00eb1b0984dcf9490ce07f8de3ef1eed79901c9cb9c52fe1ee75ba4ce9d7fa39
PRESENT V91-crosscheck-freshness.md  bytes=10799 mtime=22:47:03 sha256=ca0e4d2930bc29c4e1e9f88ef3ee0f8c418073a9c8725f60b30099a4e4674cd2
ABSENT  V107-crosscheck-adjacency.md
```

V51 was rewritten after this seat's first read. The first file (`sha256=dc034db60cbfff474b796f61e96870ee8e30a856962a69e00d52ba8709f7adaf`, 17197 bytes, mtime 22:41:28) said the V29 crosscheck was ABSENT. The 23:04:28 file supersedes that. The table uses the rewrite. V91 was also rewritten once (8228 bytes at 22:31 → 10799 bytes at 22:47:03); the table uses the rewrite, which is the file that read V32.

Tool-hash note, not a verdict: seats that quoted the freeze tool inside the poll window quoted `6f81f8be…`. The live file at 22:47:38 and 22:51:58 was `fb9bb9ff…`, mtime 22:38:11. Contract stayed `8c2561b0…`. No S1 report had landed when those seats measured. This seat did not decide which hash is the delivered pin.

## 3. Bottom lines (quoted)

**V28 calibration** (`84058e09…`), no axis call:

> Bottom line: ABSENT — S1 and S2 reports never landed (40/40 tries, post-checks through 22:48:54 still zero `S1*.md`/`S2*.md`); C1 seats unread; no after-demo and no calibration verdict on the unreported revision.

V28 did run the r98-tool before half. It records that deleting the mapped sentence `Their tick-10 decision depends on both ninth-bell entries…` from `fictional-excerpts.md` is invisible to the r98 freeze, `check_bible`, and `map_obligations`, and is not invisible to `support_check` (`EXIT=1 FAIL J14`). V28's own sentence: "The declaration's phrase 'invisible to every gate' is already false for this mutation. That bound is a baseline fact. It is not a judgment of the r99 tool, which was not run."

**V29 depth** (`1f8eb831…`):

> INCONCLUSIVE — C2 component 1 verifies on the delivered bytes (6/1/7→6/1/8, 7→8 sources, 20→21 obligations, J21 load-bearing, CLEAN/PASS, census dirs 172→173) with the locative and "per the terms" gloss bounds; C2 component 2 ABSENT after 40 polls (no blind-spot table, no lapse scope note, no S5 report), so the one depth axis-move is not established as a whole.

**V30 coverage:** file ABSENT at 23:06:57. No bottom line. Not scored by this seat.

**V31 operability** (`b7b19a4b…`):

> FAIL — C1 freeze behavior is operable on the delivered revision (`fb9bb9ff…` / contract `8c2561b0…`: chain 6/6 exit 0, self-test 18/18 exit 0, prose-wording removal exit 2 `DIGEST-MISMATCH` naming the file; r99 README replay 21/21 CLEAN/PASS), but the round's documented-command surface is not: S2 README/SKILL and S5's blind-spot table and lapse note were ABSENT after 40 tries, and the standing documented receipts (17/17, digests `3c922d20…`/`59a0f4fa…`, prose half open) contradict the delivered tool.

V31 finding 1 also says S1/S2/S5 reports were still absent at 22:47:12. That predates S1's 22:48:57 report. The FAIL bottom does not depend on S1 remaining absent; it depends on the standing docs and the missing S5 notes.

**V32 freshness** (`e94a49e6…`):

> ABSENT — after 40 poll tries (expire `2026-10-17T22:22:20-0300`) and a 22:31:14 recheck, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and producer reports S1/S2/S5 were absent; freshness was not scored.

**V33 adjacency** (`61ba3ac0…`):

> ABSENT — after 40 poll tries (22:01:29–22:19:09 -0300, with a disclosed tool-timeout gap between try 30 and try 31) the producer gate was not met: S1/S2/S5 reports missing, and `corpus/knowledge/r99-gate-blind-spot-table.md` plus `corpus/knowledge/r99-lapse-scope-note.md` never appeared (still absent at the 22:25:40 recheck); the adjacency battery was not run.

**V51 depth crosscheck** (`02f0c48b…`, the rewrite):

> INCONCLUSIVE — C2 component 1 depth improved (bounded) on the hash-pinned fixture (6/1/7→6/1/8, sources 7→8, 21/21 obligations, CLEAN/PASS, census 172→173), with the locative and "per the terms" gloss bounds confirmed; C2 component 2 ABSENT (no blind-spot table, no S5 report); V29 crosscheck AGREE, no material divergence (V29 also INCONCLUSIVE: component 1 verifies, component 2 absent, axis-move not established)

V51's addendum: the 22:41 first write said V29 was ABSENT; that was true of the 22:33:06 check; V29's mtime is 22:33:40; §5 of the rewrite replaces that ABSENT. Component 2 still absent at V51's 22:50:35 recheck.

**V52 calibration crosscheck** (`d4253add…`):

> ABSENT — S1 and S2 reports never landed (40 tries); C1 not verified; V28 report absent, no comparison.

V52 did not read V28. V28 landed at 22:50:40, after V52's 22:37:55 mtime.

**V69 coverage crosscheck:** file ABSENT at 23:06:57.

**V82 operability crosscheck** (`00eb1b09…`):

> ABSENT — after 40 tries (22:14:57–22:27:58 -03) the operability surfaces were still missing (S1/S2/S5 reports, tools README Round-99 addendum, both r99 knowledge files) and V31's report was absent, so no independent operability verdict and no comparison were issued.

V82 §3: "There is no agreement, contradiction, or divergence to record." That sentence is about the absence of V31 at 22:41:53. It is not a concurrence with V31's later FAIL.

**V91 freshness crosscheck** (`ca0e4d29…`, the rewrite):

> ABSENT — knowledge notes and S1/S2/S5 reports still missing at 22:43:02 after a 40-try expire (22:16:32-0300); freshness not scored; agrees with V32's ABSENT (`e94a49e6…`, landed 22:32:25); freeze `.py` moved again after both windows (`6f81f8be…` → `fb9bb9ff…`) and was not scored.

**V107 adjacency crosscheck:** file ABSENT at 23:06:57.

## 4. Pair table

| Axis | Verdict | Crosscheck | Pair | For V34 |
|---|---|---|---|---|
| calibration | V28 ABSENT, no score | V52 ABSENT, no score | unread; bottoms agree on not scoring | not a scored split |
| depth | V29 INCONCLUSIVE | V51 INCONCLUSIVE, AGREE | resolved by V51's rewrite | no material divergence |
| coverage | V30 file ABSENT | V69 file ABSENT | no pair | gap; do not invent a coverage call |
| operability | V31 FAIL | V82 ABSENT, comparison not done | unresolved | do not treat V82 as concurring |
| freshness | V32 ABSENT, not scored | V91 ABSENT, agrees with V32 | resolved | not scored; hash drift not scored |
| adjacency | V33 ABSENT, battery not run | V107 file ABSENT | no pair | gap; not a harmed finding |

No landed bottom in this set uses the word `harmed`. V31's FAIL is the only non-ABSENT / non-INCONCLUSIVE axis call, and it is uncorroborated by its crosscheck.

## 5. Unresolved items for the adjudicator

1. **Operability split — unresolved.** V31 issued FAIL: tool behavior on `fb9bb9ff…` / `8c2561b0…` operable (chain 6/6, self-test 18/18, prose-wording removal exit 2 naming the file), documented-command surface not (standing README/SKILL still say 17 cases, five JSON tables, prose half open; S5 notes absent). V82 issued no axis call and never read V31. V82's "no divergence" sentence does not agree with the FAIL. This seat does not re-roll the FAIL and does not convert V82's ABSENT into a pass or a harm.

2. **Coverage and adjacency crosscheck gaps.** `V30-verdict-coverage.md`, `V69-crosscheck-coverage-2.md`, and `V107-crosscheck-adjacency.md` were absent at the 23:06:57 recheck. V33 is a landed ABSENT (battery not run), not an adjacency pass and not an adjacency harm. No coverage verdict exists.

3. **Calibration comparison unread, bottoms not in conflict.** V52 wrote before V28 existed and says "no comparison." Both refuse a calibration score. V28's "S1 never landed" is stale against S1's 22:48:57 report; V28 still did not run the after-demo and did not read S1. Do not promote either ABSENT into improved or unchanged.

4. **Do not merge the before-half mutations.** V28 deleted the mapped anchor sentence and did not regenerate the map: `support_check` FAIL J14, so "invisible to every gate" is false for that mutation. V31's green other-gates result is a different edit (README `explicitly dependent on` → `ordered after`, and a non-anchor excerpt sentence; the anchor replacement that left `support_check` PASS also regenerated the map anchor). Compatible if kept apart. Not scored here as a contradiction.

5. **Depth is not an open split.** V51's rewrite (23:04:28, `02f0c48b…`) supersedes its first-write "V29 ABSENT" and records AGREE. Both INCONCLUSIVE. Component 1 holds with the locative and "per the terms" bounds. Component 2 absent. V51's "improved (bounded) on component 1" and V29's "verifies" / "UNPROVEN as a whole" are the wording difference V51 itself calls non-material. This seat does not reopen it.

6. **Freshness is not an open split.** V91 read V32. Both ABSENT, not scored. Both record the freeze-tool move `6f81f8be…` → `fb9bb9ff…` as unscored. This seat reproduced `fb9bb9ff…` at 22:47:38 and 22:51:58.

7. **Producer gate at 22:51:58, not rechecked at 23:06:57.** S1 report present and unread by this seat. S2 and S5 reports absent. Both r99 knowledge files absent (`ls` exit 2). README and SKILL `git diff --quiet 4265df5` exit 0 at 22:47:38. Unsigned tool flux is not a delivered pin until a producer report this seat did not read says so.

## 6. What this seat did not do

- Did not verify a plan. Missing reports were not filled in from scratch, from the declaration, or from in-flight tool bytes.
- Did not issue improved / unchanged / harmed / unprovable on any axis.
- Did not admit or reject the round.
- Did not extend the poll past 40 tries. Later files were read once they existed; the three still missing at 23:06:57 stay ABSENT.
- Did not write under `corpus/`, `SKILL.md`, `LOG.md`, or any other seat path.

## Bottom line

ABSENT — V30, V69, and V107 still missing at the 23:06:57 recheck after a 40-try expire (22:43:07); the nine landed reports are tabulated; unresolved operability split (V31 FAIL vs V82 ABSENT, comparison not performed) flagged for the adjudicator; depth and freshness pairs agree and are not open splits.

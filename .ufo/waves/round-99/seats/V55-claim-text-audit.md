# V55 claim-text-audit — round 99

- Seat: V55 claim-text-audit (verifier). Task: r99 LOG declaration against delivered reality; corrections list.
- Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the round `337f0fa` (`337f0fa52b02626b7687eedbb2d99fab30446fe4`), the blocked-dispatch commit; no commit from this seat. Commands from the lane root with `python3` unless a scratch mirror is named.
- Writes: this report and `.ufo/waves/round-99/seats/V55-scratch/` only (`poll.sh`, `poll.log`, `audit.py`, `probes.py`, `audit-out/`, `probe/`). No commits, no pushes, no network, no nested agents. Live contract was not rewritten; the re-freeze probe patched `CONTRACT_PATH` on a scratch copy of the tool.

## Revision pinned for the measurements below

Re-hashed at 23:10. `dependency_freeze.py` mtime 22:38:11; contract mtime 22:08:46; SKILL.md mtime 22:51:39; knowledge notes mtime 22:57:50. README was rewritten again at 23:08:16 (sha256 moved `646784ae…` → `837a7f5d…`, 38397 → 39310 bytes). Line 310 still reads "Any edit to any of the ten pinned files exits 2 `DIGEST-MISMATCH` naming that file." The C-1 citation is that sentence, not the earlier hash.

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  corpus/fixtures/r99-window-lapse/sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
```

Cited unchanged tools match the lapse note: `check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`.

## 0. Poll-wait record

`V55-scratch/poll.sh` then a continuation after the first wrapper hit its 300s cap (recorded in `poll.log` as `RESTART note=wrapper-timeout-at-300s prior_tries=15`). Cadence 20s, 40 tries. Content gates: nonempty producer reports under the r98 names, knowledge files, lapse markers, and `minfiles>=10`. Final line:

```
try=40 ts=2026-10-17 22:21:52 -0300 s1=no s2=no s3=yes s4=yes s5=no table=no note=no ev=1 src=1 map21=3 freeze=6f81f8be1974 contract=8c2561b043c2 minfiles=10
ABSENT after 40 tries ts=2026-10-17 22:21:52 -0300
```

That ABSENT is the poll record, not the final tree. Two process notes, not fatal:

- The poll looked for `S1-freeze-hygiene.md` / `S2-tools-docs.md` / `S5-knowledge-notes.md` (r98 names). S1's report landed at 22:48 as `S1-full-file-pins.md`. It was absent at try 40 even under the name it actually used.
- Post-deadline landings, read before this report: S1 report 22:48; README+SKILL.md 22:51; knowledge notes 22:57. S2 and S5 reports were still absent at 23:07. Their files were audited anyway. No second 40-try wait.

## 1. C1 — ten-file pins, schema 2, 6/6, 18/18: holds

Against `git show 4265df5:corpus/tools/dependency-freeze-contract.json`: schema 1 → 2; contract also has `payload_schema_version` 2 and a top-level `pinned_files` list of the ten declared names; self-test 17 → 18, only addition `markdown_tamper`, inherited expectation objects unchanged (`inherited expectation changes NONE`).

Each of the six pins has `payload_schema_version` 2, `pinned_files` equal to that ten, and exactly those ten file digests. Inherited JSON file digests, `events`, `relations`, and `counts` are unchanged versus the baseline pins. Content digests moved (markdown now in the payload). Pin `revision` is `337f0fa…` (HEAD at freeze time), not `4265df5`. The declaration does not require the baseline hash as the pin revision; `--freeze` records `git rev-parse HEAD`. Not a correction.

Live verify, this seat, on `fb9bb9ff…` / `8c2561b0…`:

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo exit=$?; done
RESULT PASS / exit=0   (x6)
digests: r88 acf677a7085be3f6…  r94 048b8ff39e4a5232…  r95 97cffd7bfe6e0c92…
         r96 43911900923c110b…  r97 a28b9ea0d65ec355…  r98 5ecf84e19121ea12…
```

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
exit=0
```

Scratch re-freeze (live fixtures, scratch contract, tool copy with `ROOT` pointed at the lane and `CONTRACT_PATH` pointed at the scratch contract): all six `--freeze` exits 0, and each regenerated pin compared equal to the delivered pin (`pin <name> equal=True` for all six). Transcript: `V55-scratch/audit-out/probes.txt`.

`r88-m3-maya-cluster/symbolism-clause-map.md` is the only extra file in the six directories. Appending a newline to it on a path-bound mirror still printed `RESULT PASS` / exit 0 (digest `acf677a7085be3f6…` unchanged). The declaration's ten are the listed files, not every directory entry. SKILL.md, the contract provenance note, and S1's report all say this. Scope note, not a failed claim.

`r99-window-lapse` is not pinned. Declaration says 6/6, not 7/7.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
exit=2
```

A markdown edit to the new fixture is therefore not freeze-detectable. The lapse note and the blind-spot table both say so. Not a contradiction of the 6/6 sentence.

## 2. C1 — "any edit → exit 2 DIGEST-MISMATCH naming the file": false as written

Non-semantic edits do what the sentence says. On a path-bound mirror of delivered tool+contract+`r98-clerk-filing`, a trailing newline on each of the ten pinned files exited 2 `DIGEST-MISMATCH` and named that file only (`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`). A non-inventory JSON edit (append ` (probe)` to `sources.json` `reliability_note`) also exited 2 and named `sources.json`.

A semantic inventory edit does not. Same mirror, `clerk-filing-open.depends_on` set to `[]`:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
exit=1
```

No `DIGEST-MISMATCH` line. `verify()` returns on semantic findings before the digest check (`dependency_freeze.py` `compare` then the `if findings: return 1` branch). The declaration (`LOG.md` Round 99 C1), `corpus/tools/README.md:310` ("Any edit to any of the ten pinned files exits 2 `DIGEST-MISMATCH` naming that file."), and `SKILL.md:100` ("any pinned-file edit exits 2 `DIGEST-MISMATCH` naming the file") all state the false universal. S1's report and the blind-spot table do not: both say semantic findings decide first (exit 1). The precise sentence that matches the tool is the one already in the contract `precedence` text: semantic inventory findings decide first; a content change the inventory does not model exits 2 and names the file.

## 3. C1 — "invisible to every gate before": false for the J14 anchor, true for non-anchor prose

The excerpt sentence `Their tick-10 decision depends on both ninth-bell entries…` is the J14 anchor (`r98-clerk-filing/claim-excerpt-map.md:35`, span 18-20). Replacing `depends on` with `comes after` in that sentence, scratch copies only:

- Baseline tool (`git show 4265df5:corpus/tools/dependency_freeze.py`) + baseline contract: `RESULT PASS` exit 0, digest `59a0f4fa3d4a47e0…` (the JSON-only pin). Freeze did not see it.
- `check_bible` exit 0 CLEAN; `map_obligations` exit 0 `raw=20 mapped=20`.
- `support_check` exit 1: `FAIL: J14: source-support anchor missing` / `RESULT FAIL`. Not invisible to every gate.
- Delivered tool+contract: exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md` (`29e384bf… -> 6fff9391…`).

Non-anchor excerpt edit (first `the inherited wording is unchanged` → `the inherited wording is retained`; not an anchor cell):

- Before: freeze exit 0 digest `59a0f4fa…`; `check_bible` / `support_check` (`SOURCE-SUPPORT 20/20`) / `map_obligations` all exit 0.
- After: exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`; the same three gates still exit 0.

So the BR-01 prose half that every prior gate missed is non-anchor (or anchor-and-map-together) prose. That class is edit-detectable after C1 and is not a semantic proof — the finding names the file and the hashes, not the wording. The declaration's "invisible to every gate" sentence does not survive the J14 case. S1's report and table row 6 already record that bound, including a coherent excerpt+anchor edit that stays green for the lexical gates and exits 2 on the delivered pin. I did not re-run S1's exact r94 digest `1f73326f…`; the class matches what I ran.

## 4. C2 component 1 — lapse fixture: holds

Delivered `corpus/fixtures/r99-window-lapse/`: entities 6, relations 1, timeline 8, sources 8, contradictions 0. Parsed prefixes versus `r98-clerk-filing`: `entities` and `relations` identical (tail empty); `sources[:-1]` and `timeline[:-1]` equal, tails `clerk-lapse-note` and `clerk-lapse-recorded`. `fictional-excerpts.md` startswith the r98 bytes. Byte-identical to r98: `contradictions.json`, `entities.json`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`. README and the map are rewrites (S4), not r98 copies. S3's report still says those two files are r98 copies and that map/support should see 20 rows. That was true at S3's 22:01 hand-off and is stale for the tree S4 rewrote (map 22:02:39, README final sha256 `b9320941…`). S4's report says the same.

Last event, `timeline.json`:

```
id clerk-lapse-recorded, tick 15, entity_id clerk-maren, place_id chalk-stair,
depends_on ["clerk-filing-open"], source_id clerk-lapse-note
description: the crossing-window named in the original minute has closed;
the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.
```

Excerpt lines 70-74 are those four statements plus `I record no resolution, assign no blame, and reconcile nothing.` A scan of the ten fixture files for `resolution|blame|reconcil` found no line that lacked a negation. "No claim was lodged" is the note's statement. The fixture still has the six inherited entity claims (`entities.json` byte-identical to r98; one claim on `clerk-maren`, statement at line 69, source `clerk-filing-note`). The scope note says this. Not a contradiction of the declaration if "no claim lodged" is read as the lapse record's content, not as "claims array empty".

Map: 21 `J` rows. J01–J20 differ from r98 only by `r98-clerk-filing` → `r99-window-lapse` in the namespace cell (`J01-J20 normalized diffs NONE`). J21 is `timeline.json#/7`, span 66-76, anchor the tick-15 sentence, at `claim-excerpt-map.md:42`. That is the declaration's "20 inherited rows unchanged + 1 new event row", with the same namespace qualification r98 itself used.

Gates on the delivered fixture, re-run 22:47 after the README phrase edits:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
exit=0
```

Census (`V55-scratch/audit.py census`, `check_bible` on every `corpus/fixtures/*/` directory):

```
{"fixture_dirs": 173, "clean_exit0": 39, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": [], "has_r99": true}
```

172 without `r99-window-lapse`. Declaration says 172→173 and does not restate the 38/134/421 split. The increment is +1 clean, negatives and violation lines unchanged versus the r98 fixtures README sentence (172/38/134/421). Holds. The fixtures README itself still declares the r98 census; no producer owns that file. Closure item, not a false declaration sentence.

## 5. C2 component 2 — blind-spot table and lapse note: present, and more precise than the declaration

Both files exist (mtime 22:57:50). They were absent at poll try 40. Audited on the bytes hashed above, not on a plan.

The table's rows cover the declaration's list: emptied `depends_on` (row 1), wrong-but-earlier edge (row 2), deleted terminal row (row 3), F15 mutants (row 1b = F15-a; row 4 = F15-c, explicitly not support_check-silent; row 5 = F15-d, the silent source-id mutant), dependency-wording removal with both the baseline invisibility and the C1 close (row 6), consistent regeneration (row 7), checker frozen-pin status (row 8, `ff9fd2aa…`, `CERTIFIED` claimed). Row 9 is the complementary "checker does catch" class, not a required row.

F15-b2 (r98 V47: drop a fact row and restate inventory; `support_check` stays PASS, `map_obligations` exits 1) is not named. Row 7 is that class (delete the terminal event, delete the map row, restate the inventory line; lexical gates PASS, freeze exits 1). Label gap, not a missing class. I did not re-run rows 2–5 or 7–9; those quotes are S5's, and this seat does not confirm the declaration's "replay-verified by at least two seats" count. Rows I did reproduce match the table's distinction: empty-deps exit 1 `REDUCTION-DETECTED` (table row 1's finding text matches my probe, including `dependency-edges 5/6`); J14 excerpt-only removal is a `support_check` fail; non-anchor prose is green on the lexical gates and exit 2 on the delivered pin; r99 is `UNPINNED-FIXTURE`.

Lapse-note citations I checked against the fixture: `sources.json:45` `clerk-lapse-note`, `:46` title, `:48` reliability note; `timeline.json:77` id, description at `:84`; excerpt lines 70-74 and scope at 76; `entities.json:63` / `:66` / `:69`; `claim-excerpt-map.md:5` inventory 21/2/23/19 and `:42` J21; README `:3` counts and `:21` 21 obligations; `:11` states the matter stays open, nothing is resolved, it closes no one. Prefix and byte-identity claims match section 4. Cited tool hashes match. Census 173 matches. The note's "not independent verification" limit is accurate for an author note.

## 6. Corrections list

- **C-1 (declaration and delivered docs — false universal).** `LOG.md` Round 99 C1, `corpus/tools/README.md:310`, and `SKILL.md:100` say any edit to any pinned file exits 2 `DIGEST-MISMATCH` and names the file. Observed on a path-bound r98 copy: emptying `clerk-filing-open.depends_on` prints `FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']`, `RESULT FAIL`, exit 1, and does not name the file. Suggested sentence: semantic inventory edits exit 1 and decide first; an inventory-clean edit of any of the ten files exits 2 `DIGEST-MISMATCH` naming the file. The contract `precedence` text, S1's report, and table rows 1 and 6 already say this.
- **C-2 (declaration — "every gate" overclaim, already bounded in the delivery).** "prose-wording removal was invisible to every gate before" is false for the J14 anchor sentence: baseline freeze, `check_bible`, and `map_obligations` stay green, `support_check` exits 1 `J14: source-support anchor missing`. A non-anchor excerpt edit was green on all four before and is exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md` after. Table row 6 and S1's report already record both. The LOG sentence should say "invisible to the freeze and to gates that do not tokenize that wording", not "every gate".
- **C-3 (scope, disclosed, not a failed 6/6 claim).** `r99-window-lapse` is `UNPINNED-FIXTURE` exit 2, so C1 does not make that fixture's prose edit-detectable. `symbolism-clause-map.md` stays outside the ten; a newline there is still `RESULT PASS`. Both are stated in the delivered notes.
- **C-4 (producer-report staleness).** S3's "Not done" section says README and `claim-excerpt-map.md` still say r98 and that map/support should see 20 rows. False on the delivered tree (21/21, CLEAN). S4 already recorded the supersession.
- **C-5 (label, not a missing class).** The declaration's "F15 support_check-silent mutants" includes F15-b2 (V47: row dropped and inventory restated). The table covers that behavior as row 7 and does not use the F15-b2 name. F15-d is named (row 5). F15-c is correctly marked not silent (row 4).
- **Not a correction.** Inherited map rows change the namespace string. Normalized to a placeholder, J01–J20 are identical. Same qualification the r98 declaration needed. Pin revision `337f0fa` is what guarded `--freeze` writes at this HEAD. Fixtures README still states the r98 census (172/38/134/421); measured state is 173/39/134/421. No producer owns that file.

## 7. What this seat did not verify

- Did not re-run table rows 2, 3, 4, 5, 7, 8, 9, and did not count two independent seat replays of each row. The "at least two seats" clause in the declaration is not confirmed here.
- S2 and S5 reports were absent at 23:07. Their files were present and were read. S1's report was read after the poll deadline.
- Did not treat other verifier reports as evidence for these claims.

## Bottom line

**FAIL** — the declaration sentence "any edit to any pinned file → exit 2 `DIGEST-MISMATCH` naming the file" is false on the delivered tool (emptying `clerk-filing-open.depends_on` exits 1 `REDUCTION-DETECTED` and does not name the file); the same false universal is now in `corpus/tools/README.md:310` and `SKILL.md:100`. Ten-file schema-2 pins, guarded re-freeze (pins byte-equal on a scratch re-freeze), chain 6/6, self-test 18/18, the r99 lapse fixture (6/1/8, 21/21, CLEAN, census 173), and the blind-spot table's own more precise wording otherwise match the measured bytes.

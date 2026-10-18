# V44 — inherited-tools (round 98)

Seat: **V44 inherited-tools** — verifier. Claim under test: `git diff 9a3d648` shows the
inherited tools `check_bible.py`, `support_check.py`, `boundary_doc_check.py`,
`discriminate_check.py` **and all fixture JSON tables byte-untouched** (the r95
`claim-excerpt-map.md` repair excepted, verified by V15, not here).

Baseline: r97 closure `9a3d648`. All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents,
no commits, no network. Writes: this report (absolute path) and
`.ufo/waves/round-98/seats/V44-scratch/` only. Wave tree is uncommitted; every comparison is
against `git ls-tree`/`git hash-object` blobs at `9a3d648`.

Method (three independent layers, so a single tool bug cannot fake a pass):

1. **Blob identity** — `git ls-tree -r 9a3d648 <dirs>` records the baseline blob SHA-1 per path;
   `git hash-object <path>` re-computes it in the working tree. Path sets are diffed too, so a
   *deleted* or *added* table also surfaces.
2. **Byte identity** — `cmp` against `git show 9a3d648:<path>` extracted bytes (tools only).
3. **Pin identity** — the delivered `check_bible.py` sha256 is compared with the persisted
   `/checker/sha256` in `corpus/tools/boundary-doc-contract.json`, and the r97/r98 fixture
   sha256 sets are compared with the freeze-contract pins.

Scope note on naming: the seat brief says `boundary`/`discriminate`; the actual paths are
`corpus/tools/boundary_doc_check.py` and `corpus/tools/discriminate_check.py`. `check_bible.py`
lives at `corpus/fixtures/check_bible.py` (plus a live copy at `corpus/live/rejected-r4/check_bible.py`).
Both copies are in scope below.

## Claim 1 — the four inherited tools are byte-identical

```
$ git diff --stat 9a3d648 -- corpus/fixtures/check_bible.py corpus/tools/support_check.py \
      corpus/tools/boundary_doc_check.py corpus/tools/discriminate_check.py
(no output; exit 0)
$ for f in <the four>; do base=$(git rev-parse 9a3d648:"$f"); cur=$(git hash-object "$f"); ... done
IDENTICAL corpus/fixtures/check_bible.py          20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
IDENTICAL corpus/tools/support_check.py           a69ae9d27ad1e848c3188fa832352d00b7c0ffc7
IDENTICAL corpus/tools/boundary_doc_check.py      4daa9998023f247fef7ca07d7cf2723f95cab0be
IDENTICAL corpus/tools/discriminate_check.py      aa601eee3ec288eccf21e5bb78cd01caaacfea7c
$ for f in <the four>; do git show 9a3d648:"$f" | cmp -s - "$f" && echo "CMP-EQUAL $f"; done
CMP-EQUAL corpus/fixtures/check_bible.py
CMP-EQUAL corpus/tools/support_check.py
CMP-EQUAL corpus/tools/boundary_doc_check.py
CMP-EQUAL corpus/tools/discriminate_check.py
$ sha256sum corpus/fixtures/check_bible.py corpus/tools/support_check.py \
      corpus/tools/boundary_doc_check.py corpus/tools/discriminate_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ebb6a0843e67bfaa3118eda7fbf69bac124aca8f5b87cd0b9721b5e6346b0053  corpus/tools/boundary_doc_check.py
6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef  corpus/tools/discriminate_check.py
```

Pin identity (third layer) — the frozen checker is not merely "equal to the baseline", it still
equals the pin the boundary contract froze it at:

```
$ python3 -c "... boundary-doc-contract.json ..."
/document/sha256               = 7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e
/checker/sha256                = ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
/checker/legacy_baseline_sha256 = 88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81
# observed corpus/fixtures/check_bible.py sha256 == /checker/sha256  -> MATCH
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
...
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
exit=0
```

Wider inherited-tool sweep — every `*.py` inherited under `corpus/` (7 paths) was compared the
same way. Six are unchanged; the only change is S1's declared byte-owned
`corpus/tools/dependency_freeze.py` (round C1/C2 work, not this seat's untouched-set):

```
CHANGED   corpus/tools/dependency_freeze.py  base=001ad47390a04c4b20f17ac7fa0555c5175a506d cur=<S1 delivered>
UNCHANGED corpus/live/rejected-r4/check_bible.py
UNCHANGED corpus/fixtures/check_bible.py
UNCHANGED corpus/tools/boundary_doc_check.py
UNCHANGED corpus/tools/map_obligations.py      # unowned this round — untouched
UNCHANGED corpus/tools/support_check.py
UNCHANGED corpus/tools/discriminate_check.py
```

Behavioural corroboration on the delivered revision (frozen bytes still behave as at closure):

```
$ python3 corpus/tools/boundary_doc_check.py            -> CERTIFIED, replay_receipts=3/3 replay_cases=14/14 anchors=2/2, exit=0
$ python3 corpus/tools/boundary_doc_check.py --self-test -> SELF-TEST PASS (9 lines, incl. anchor_range_control exit=1 findings=['anchor_range']), exit=0
$ python3 corpus/tools/discriminate_check.py            -> DISCRIMINATION HELD, exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
      SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19; RESULT PASS, exit=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
      CLEAN: schema, citations, relations, timeline; 0 violations, exit=0
```

## Claim 2 — all fixture JSON tables are byte-untouched

Class-by-class blob comparison (baseline manifest `git ls-tree -r 9a3d648 corpus/`, 1815 paths;
898 of them `*.json`):

```
[1 four-tools]          paths=5   changed=0
[2 fixture-JSON]        paths=850 changed=0
[3 live-probe-JSON]     paths=45  changed=0
[4 tool-contract-JSON]  paths=3   changed=1
    < 1f0a4dc03851fb41c54a60a32aa5b64b4c26aaa4 corpus/tools/dependency-freeze-contract.json
    > acb6daf2db190e124f57b93f696b8812112bebf3 corpus/tools/dependency-freeze-contract.json   (S1-declared)
[5 all-corpus-JSON]     paths=898 changed=1   (the same declared contract file)
```

So: **850/850 inherited fixture tables unchanged, 45/45 live probe-input tables unchanged, and
the only changed JSON anywhere under `corpus/` is S1's declared contract file** (class 4 is not a
"fixture table"; it is S1's declared byte-ownership for C1/C2). Zero deletions in any class
(`missing=0`), so no table was dropped or moved.

Whole-tree sweep — `git status --porcelain --untracked-files=all`, classified against the
round-98 declared write set, gave **STRAYS=0**: the only entries are the three declared markdown
files (`r95-crossing-aftermath/claim-excerpt-map.md`, `knowledge/r95-aftermath-scope-note.md`,
`knowledge/r96-response-scope-note.md`) plus the ten new `corpus/fixtures/r98-clerk-filing/` files
(plus the declared `LOG.md` round declaration and `.ufo/waves/round-98/` scratch). Nothing was
written outside a declared path — the r94-F01 stray-write class did not recur.

The 11 JSON files that fail `json.load` (r5-invalid-json, r60-unavailable*, r61-*-malformed/
unavailable, r62-malformed*) are **intentionally malformed fixtures**; all 11 are byte-identical
to baseline, so the invalidity is inherited by design, not introduced this round.

## Claim 3 — the one changed JSON (S1's contract) is confined to the declared classes

Semantic leaf diff, baseline `9a3d648:corpus/tools/dependency-freeze-contract.json` vs delivered:

```
baseline_keys=176 current_keys=261 changed_leaves=87
```

Every changed leaf falls in a declared class, and **no inherited pin object changed**:

- `.pins.r97-crossing-acknowledgment.*` — new pin (C2): counts 5/1/6/6, five events with endpoints
  and `depends_on`, five `files.*` sha256, `revision=dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`.
- `.pins.r98-clerk-filing.*` — new pin (C2/C3): counts 6/1/7/7, `clerk-filing-open`
  `depends_on=[acknowledgment-aru-records]`, `files.*` sha256, same revision.
- `.precedence` — extended with the FINDING IDs `(exit 1: REDUCTION-DETECTED, ADDITION-DETECTED,
  ENDPOINT-CHANGE) … exits 2 (DIGEST-MISMATCH)` (C1c).
- `.self_test.expected.self_test_mismatch.{exit=2, finding_ids=['SELF-TEST-MISMATCH'], forbid_traceback=true}` — new persisted case (C1a, 16→17).
- `.revision` — updated to the r97 closure revision.

Not present in the changed list: `.pins.r95-crossing-aftermath.*`, `.pins.r96-*`, `.pins.r94-*`,
`.pins.r88-*` — i.e. **all inherited pins are semantically identical to baseline**, which
independently corroborates V15's "r95 pin object semantically identical after S1's contract edit".

Cross-check of the pins against the delivered bytes:

```
$ sha256sum corpus/fixtures/r97-crossing-acknowledgment/{contradictions,entities,relations,sources,timeline}.json
37517e5f…  contradictions.json   026af0bc… entities.json   c279254b… relations.json
438fb513…  sources.json          73063a86… timeline.json      # all five == the r97 pin values
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6   RESULT PASS  exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133   RESULT PASS  exit=0
```

Both digests equal the contract pins (`3c922d20…`, `59a0f4fa…`), and the r97 table hashes equal
the r97 pins — the pinned content is the untouched inherited content, and the new r98 pin covers
exactly the delivered new tables.

## Claim 4 — the new r98 tables (new paths, not "untouched" paths) match their declared shape

The ten new files are all under the declared path `corpus/fixtures/r98-clerk-filing/`. Five are
JSON tables; the other five are markdown. Copy fidelity vs r97 (S3's declared 10-file copy):

```
IDENTICAL contradictions.json  37517e5f…   (byte copy)
IDENTICAL relations.json       c279254b…   (byte copy)
IDENTICAL inspiration-note.md / source-excerpt.md            (byte copies)
DIFFERS   entities.json  r97=026af0bc… r98=db2d8e5d…   (declared: +clerk-maren)
DIFFERS   sources.json   r97=438fb513… r98=32ee15b1…   (declared: +clerk-filing-note)
DIFFERS   timeline.json  r97=73063a86… r98=eb24e084…   (declared: +clerk-filing-open)
DIFFERS   fictional-excerpts.md / README.md / claim-excerpt-map.md  (declared rewrites)
```

Parsed-value comparison of the inherited rows inside the new tables — **no inherited row was
altered**, only appended:

```
entities.json:  r97rows=5 r98rows=6 inherited_present=5 altered=[] new=['clerk-maren']
relations.json: r97rows=1 r98rows=1 inherited_present=1 altered=[] new=[]
timeline.json:  r97rows=6 r98rows=7 inherited_present=6 altered=[] new=['clerk-filing-open']
sources.json:   r97rows=6 r98rows=7 inherited_present=6 altered=[] new=['clerk-filing-note']
contradictions.json: r97rows=0 r98rows=0 altered=[] new=[]
INHERITED_ROWS_PARSED_VALUE_IDENTICAL: True
```

Declared new rows, observed verbatim: `clerk-maren` (kind `character`, name `Maren`,
`first_appearance` `clerk-filing-note`, one claim citing `clerk-filing-note`);
`clerk-filing-note` (title `Maren's Chalk Stair Registry Filing Note`, kind
`fictional first-person note`, reliability note asserting no finding/verdict/reconciliation/
resolution); `clerk-filing-open` (tick 14, `entity_id` `clerk-maren`, `place_id` `chalk-stair`,
`depends_on` `["acknowledgment-aru-records"]`, `source_id` `clerk-filing-note`).

Producer-declared sha256 cross-check — S3's four and S4's two declared hashes all match observed
bytes: entities `db2d8e5d…`, sources `32ee15b1…`, timeline `eb24e084…`, fictional-excerpts
`29e384bf…`, README `32efc78f…` (5829 bytes), map `c1099d0e…` (15028 bytes).

Gates re-run by this seat on the delivered r98 fixture (read-only; independent of S3/S4's runs):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS   exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20; INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS   exit=0
```

## The r95 repair exception (delegated)

`corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` is the one fixture file this seat
excludes; per the brief it is verified via V15. Independently confirmed here only that the repair
is **markdown-only**: all five r95 JSON tables plus its other markdown files are byte-identical to
baseline (`git diff --name-status 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/` lists exactly
that one `M` path). V15's report exists (`.ufo/waves/round-98/seats/V15-c3-r95-repair.md`) and
closes **PASS** — byte-minimal one-line diff, data rows byte-unchanged, receipts identical pre/post,
no re-pin needed.

## Final verification on the delivered revision

All five producer reports were present and the three out-of-scope moving files (S1's tool +
contract, S2's README) were stable across consecutive samples at **23:35:23Z**; the whole sweep
was then re-run on that frozen revision:

```
$ .ufo/waves/round-98/seats/V44-scratch/scope-receipt2.sh        # FINAL
[1 four-tools]          paths=5   changed=0
[2 fixture-JSON]        paths=850 changed=0
[3 live-probe-JSON]     paths=45  changed=0
[4 tool-contract-JSON]  paths=3   changed=1   (S1's declared dependency-freeze-contract.json)
[5 all-corpus-JSON]     paths=898 changed=1   (same declared file)
$ for f in <the four tools>; do git show 9a3d648:"$f" | cmp -s - "$f" && echo "CMP-EQUAL $f"; done
CMP-EQUAL corpus/fixtures/check_bible.py
CMP-EQUAL corpus/tools/support_check.py
CMP-EQUAL corpus/tools/boundary_doc_check.py
CMP-EQUAL corpus/tools/discriminate_check.py
$ .ufo/waves/round-98/seats/V44-scratch/check-corpus.sh          # FINAL
--- baseline=1815 current=1826 modified=6 missing=0 new=11 ---
$ .ufo/waves/round-98/seats/V44-scratch/classify.sh             # FINAL
... STRAYS=0
```

The 6 modified + 11 new paths are exactly the declared write set — S1
`dependency_freeze.py` + `dependency-freeze-contract.json`, S2 `tools/README.md`, S3
`r95-crossing-aftermath/claim-excerpt-map.md`, S5 `r95-aftermath-scope-note.md` +
`r96-response-scope-note.md` + new `r98-clerk-scope-note.md`, S3/S4 the ten
`r98-clerk-filing/` files — with `LOG.md` (round declaration) and `.ufo/waves/round-98/` scratch.
**No file outside the declared set was written in the lane tree.**

Producer-declared hashes vs observed on the delivered bytes (all match): S1
`03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` (dependency_freeze.py) and
`153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` (contract); S2
`1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84` (tools/README.md); S3/S4
fixture hashes as listed above.

## Poll record

Producer reports and byte stability were polled (20 s cadence, ~6 min wall) in
`.ufo/waves/round-98/seats/V44-scratch/poll.log`; raw snapshot lines are in
`check-corpus-out.txt`, `scope-*.txt`, `baseline-corpus-hashes.txt` (1815 baseline blobs) and
`baseline-hashes.txt` (1029 fixture+tools blobs). Observed cadence: r98 fixture files present at
20:28 (S3), r95 map repair 20:28, S5 addenda + note by 20:32, S2 README final 20:35. Producer
reports: S3 (20:31), S4 (20:31), S5 (20:34), S1 and S2 by 23:35:23Z — **all five present, no
stall-escape needed** (ENDGAME convention not triggered; no all-reports poll was used, so no
SELF-subtraction applies). Mid-round hazard noted for the record: S3's copy step left r97's
README/map bytes at the r98 path between 20:28 and S4's rewrites, so an existence-only poll could
have been satisfied by a placeholder — my comparisons are content-based (`cmp`/blob), never
existence-based.

## Cross-lane observation (outside this seat's claim, evidence only)

S2's report flags, and I independently confirmed, a **stray write in the PARENT tree**
(`/home/vgpnk/Projects/shokunin`, not the lane):

```
$ ls -la baseline-analyze.txt
-rw-r--r-- 1 vgpnk vgpnk 105 Oct 17 20:30 baseline-analyze.txt
$ cat baseline-analyze.txt
python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory
$ cd /home/vgpnk/Projects/shokunin && git status --porcelain
?? baseline-analyze.txt
```

That is the r94-F01 class (a seat ran `python3 analyze.py > baseline-analyze.txt` with the parent
as cwd). It is outside `lore-shokunin/`, was not written by this seat, and is left in place as
evidence for the closure sweep — my lane-level stray count is 0.

## Bottom line

**PASS** — on the delivered revision (all five producer reports present, bytes stable at
23:35:23Z) the four inherited tools are byte-identical to `9a3d648` (blob + `cmp` + sha256 vs the
persisted `/checker/sha256` pin, `matches_pin=True`), all 850 inherited fixture JSON tables and all
45 live probe-input tables are blob-identical with zero deletions, the only changed JSON under
`corpus/` is S1's declared `dependency-freeze-contract.json` (87 leaves, all in declared classes,
no inherited pin object changed), the new r98 tables are confined to the declared path with
inherited rows parsed-value identical and their declared sha256s/pins matching, and the lane
stray-write count is 0 (one parent-tree stray of the r94-F01 class recorded as evidence).

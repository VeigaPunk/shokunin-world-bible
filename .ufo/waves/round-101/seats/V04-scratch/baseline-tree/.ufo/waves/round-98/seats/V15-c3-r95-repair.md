# V15 — c3-r95-repair (round 98)

Seat: **V15 c3-r95-repair** — verifier. Claim under test (C3 repair half): after S3's repair,
`git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` shows **exactly
the one declared sentence** and nothing else; the **data rows are byte-unchanged**; the r95
**receipts are identical pre/post** (both runs quoted); and **the r95 pin in the freeze contract
needs no refresh** (the map is not a pinned file — verified and stated).

Baseline: r97 closure `9a3d648`. Pre-repair map byte-identical to baseline (`sha256
30281ff1…`, 8563 bytes, `diff <(git show 9a3d648:…) <file>` → empty, `IDENTICAL-TO-BASELINE`),
captured at 20:27 before S3's write. Post-repair map `sha256 80440d61…`, 8641 bytes, mtime 20:28.

Protocol: poll-wait honoured — pre-repair receipts for all four r95 commands were captured
**before** the repair landed (20:27, map still `30281ff1…`, all tools at frozen revisions), plus a
scratch-cluster copy of the pre-repair map (`V15-scratch/precluster/`) so the map change can be
isolated from any tool-revision change. Artifact poll observed the map change at try=3
(20:28:53, `30281ff1…` → `80440d61…`); the producer-report half of the poll required S3's seat
report and was satisfied at **try=10 (20:31:13, `S3-fixture-author.md`)**, well inside the 40-try
bound — no stall-escape was needed. The post-repair map was stable at `80440d61…` across
tries 3–10 (mtime 20:28:34) and still `80440d61…` at finalization (20:31+), so all post-repair
runs below are on the frozen final revision. S3's report declares exactly the change observed
here (`S3-fixture-author.md:32-33`, section A) — agreement, independently derived.

S1's C1 contract/tool edit landed **mid-verification** (after the pre-run and the first post-run):
`dependency_freeze.py` moved `b06275f3…` → `1a01fd17…` and the contract gained the completed
`precedence` text + a 17th self-test case. Everything was therefore re-run against the edited
revision (see the cross-tool-revision note in Claim 2 and the re-check in Claim 3); the r95
receipts and the r95 pin are unaffected by that edit.

Nothing was written outside this report and `.ufo/waves/round-98/seats/V15-scratch/` (verified by
`find . -newermt '-15 minutes' -type f -not -path './.git/*' -not -path './.ufo/*'`: no V15-authored
path appears at the lane root or in the parent tree).

## Claim 1 — the diff is exactly the one sentence, data rows byte-unchanged

Commands and observed output (post-repair revision):

```
$ git diff --numstat 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/
1	1	corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
$ git diff --stat 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/
 corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git diff -U0 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | grep -c '^@@'
1                      # single hunk, @@ -49 +49 @@
$ git diff --check 9a3d648 -- …   → exit 0, no output
```

One line, line 49, changed. Byte-level shape (python3, `pre` = `git show 9a3d648:…`, `post` =
working tree):

```
pre bytes 8563   post bytes 8641   (+78)
pre lines 53     post lines 53
trailing newline pre True  post True
differing line numbers (1-based): [49]
common prefix chars: 615
```

The line-49 paragraph is 4 sentences on both sides; the first **3** are byte-identical and only the
**4th (final) sentence** differs:

```
PRE  sent[3]: The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
POST sent[3]: The relation encodes only the agreement for this crossing, not perpetual performance or alliance; the new tick-11 aftermath event records one reported non-arrival on one occasion.
```

Reading note (stated, not hidden): the replacement is one sentence in the paragraph's sentence
inventory, and it is itself a single sentence carrying one semicolon-joined second clause
(`; ` count = 1). The stale claim is removed and the accurate one added: r95's new row is event
J15, not a relation (the relation J11 is inherited from r94 — consistent with the r97 V19
residual that flagged this same sentence as the r95 staleness class). `grep -n "new relation"`
on the post-repair map → **no occurrence** (exit 1).

Nothing else moved:

```
$ pre  = git show 9a3d648:… | grep -E '^\| (J[0-9]{2}|S[0-9]{2}) '
$ post = grep -E '^\| (J[0-9]{2}|S[0-9]{2}) ' <file>
$ cmp datarows-pre.txt datarows-post.txt  → DATAROWS-IDENTICAL 17 rows
  sha256 206fe137e8c24d243801eac1ea1ad42e9a5fc321b47f789d2624413c698af6e6  (both sides)
$ diff <(pre minus data rows) <(post minus data rows)  → only the line-49 sentence above
```

So all 15 J rows and 2 S rows (pointers, source IDs, namespaces, excerpt paths, spans, R9 modes,
anchors) are byte-identical, and no other file in the r95 fixture changed (`--numstat` names only
the map; `git status --porcelain` shows no other r95 path).

Cross-reference stability (line count unchanged at 53, only line 49 differs in its final
sentence): the r95 knowledge note's citations still resolve —
`corpus/knowledge/r95-aftermath-scope-note.md:31` cites `claim-excerpt-map.md:49` for
"editorial encodings … not literal JSON syntax", which is the **byte-unchanged 615-char prefix** of
that same line (verified by `sed -n '49p' … | grep -o …`); `:30` cites `:51` (unchanged); `:23`
cites `:36` (J15 row, unchanged).

## Claim 2 — the r95 receipts are identical pre vs post (both runs quoted)

Pre captured 20:27 against the pristine `9a3d648` tree; post re-run on the repaired tree. All four
tools were at their **frozen r97 revisions at both runs** — `support_check.py` `55a5eb27…`,
`map_obligations.py` `86b52949…`, `dependency_freeze.py` `b06275f3…`, `check_bible.py`
`ff9fd2aa…` (each verified equal to `git show 9a3d648:<path>` at pre-run time), so the comparison
isolates the map change with no tool-revision confound.

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
  PRE  exit 0: CLEAN: schema, citations, relations, timeline; 0 violations
  POST exit 0: CLEAN: schema, citations, relations, timeline; 0 violations
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
  PRE  exit 0: INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
              ANCHORS repeated-references=4; DUPLICATE-ROWS 0
              RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
              SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
              RESULT PASS
  POST exit 0: <byte-identical, same 20 lines>
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
  PRE  exit 0: OBLIGATIONS raw=15 mapped=15
              INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
              RESULT PASS
  POST exit 0: <byte-identical>
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
  PRE  exit 0: FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
              DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
              RESULT PASS
  POST exit 0: <byte-identical, same DIGEST d541ae64…>
```

```
$ diff r95-support-pre.txt r95-support-post.txt       → empty  → SUPPORT-RECEIPT-IDENTICAL
$ diff r95-mapobl-pre.txt  r95-mapobl-post.txt        → empty  → MAPOBL-RECEIPT-IDENTICAL
$ diff r95-checkbible-pre.txt r95-checkbible-post.txt → empty  → CHECKBIBLE-RECEIPT-IDENTICAL
$ diff r95-freeze-pre.txt  r95-freeze-post.txt        → empty  → FREEZE-RECEIPT-IDENTICAL
```

Cross-tool-revision re-check (S1's C1 edit landed after the runs above): `dependency_freeze.py`
was `b06275f3…` at the pre-run and `1a01fd17…` afterwards. Re-running the repaired tree under the
edited tool (`tool-at-run: 1a01fd17…`, exit 0) produced output **byte-identical** to the pre-run
receipt from the old tool — `FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3;
relations 1/1` / `DIGEST d541ae64…` / `RESULT PASS` — so the repair is receipt-neutral across both
tool revisions, not merely within one. `support_check.py` (`55a5eb27…`) and `map_obligations.py`
(`86b52949…`) were unchanged by the edit and re-run clean after it.

The post-repair values match the receipt block recorded at r95 closure
(`corpus/knowledge/r95-aftermath-scope-note.md:44-49`: `JSON-FACTS 15/15 … VALIDATED-ROWS 17/17 /
RESULT PASS` and `OBLIGATIONS raw=15 mapped=15 / RESULT PASS`), i.e. the repair moved no receipt
field. Map-only isolation also holds independently: the pre-repair map copied into
`V15-scratch/precluster/` re-runs under the current tools to `SOURCE-SUPPORT 15/15 … RESULT PASS`
and `OBLIGATIONS raw=15 mapped=15 … RESULT PASS` — identical to the live post-repair runs.

## Claim 3 — the r95 pin needs no refresh (map is not pinned)

Verified programmatically against the contract — first while it was still **byte-identical** to
`9a3d648:corpus/tools/dependency-freeze-contract.json`, then re-checked **after S1's C1 contract
edit landed** (which rewrote `precedence` and added a 17th self-test case):

```
r95 pin keys:        ['content_sha256', 'counts', 'events', 'files', 'fixture', 'relations', 'revision']
r95 pin files:       ['contradictions.json', 'entities.json', 'relations.json', 'sources.json', 'timeline.json']
map pinned?          False
map in data_files:   False
contract mentions 'claim-excerpt-map': 1   (in the provenance_note prose, not in any pin's files map)
r95 pin equal baseline vs now:  True   (whole pin object)
r95 files map equal baseline vs now: True
data_files equal baseline vs now: True
r95 content_sha256:  d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9  (unchanged)
r95 revision:        60dba0c2aa344860b10a2fc63e00468d1b134f27  (unchanged)
```

So the pin's `files` map covers exactly the five `data_files` JSON tables; `claim-excerpt-map.md`
is not a pinned data file, and S1's mid-round contract edit left the r95 pin semantically
identical. Consistent with that, the live verify against the unchanged pin passes **on the
repaired tree without any refresh**: `FREEZE r95-crossing-aftermath: events 4/4;
dependency-edges 3/3; relations 1/1` + `DIGEST d541ae64…` + `RESULT PASS`, exit 0 — the same
digest as pre-repair, and the same again under the edited tool `1a01fd17…`. The map sentence
repair is digest-neutral by construction; no `--freeze` for r95 is required or performed. (This
mirrors the recorded r97 precedent for the r96 map repair in `provenance_note`.)

## Observations / residuals (outside this seat's verdict, reported as evidence)

- The repair's added clause ("the new tick-11 aftermath event records one reported non-arrival on
  one occasion") is consistent with the unchanged map line 51 ("The event records one non-arrival
  on one occasion") and with `corpus/knowledge/r95-aftermath-scope-note.md:30`. No contradiction
  introduced; wording quality is other seats' call.
- Only line 49's final sentence changed, so no line-number drift for the r95 knowledge note's
  `:36`, `:49`, `:51` citations. (S5 owns the note's addenda; this is observation only.)
- The `new relation` stale-sentence class now remains only in `r94-paired-crossing`, where it is
  accurate (r94's new row is relation J11). Not in this seat's byte scope.
- Hygiene observation, outside this seat's verdict: a scratch tree `v05-self-test-scratch/`
  (`poll.log`, `poll.out`, `poll.sh`, `recompute.py`, `redemo.sh`) exists at the **lane root**, not
  under `.ufo/waves/round-98/seats/`. At my sweep time V05's seat report was not yet written, so I
  cannot confirm whether that path is declared scratch; flagging it as witnessed, not as a finding.
  No V15-authored path exists outside this report and `V15-scratch/`.

## Bottom line

**PASS** — the r95 map repair is byte-minimal (exactly one line and exactly the one declared final
sentence of the line-49 paragraph; all 17 data rows and every other file in the r95 fixture
byte-identical), all four r95 receipts (`check_bible` CLEAN, `support_check` 15/15 PASS,
`map_obligations` raw=15 mapped=15 PASS, `dependency_freeze` DIGEST d541ae64… PASS) are
byte-identical before vs after — including across S1's mid-round tool edit — and the r95 freeze pin
needs no refresh because `claim-excerpt-map.md` is not a pinned data file: the unchanged pin
(r95 pin object semantically identical after S1's contract edit) still verifies exit 0 on the
repaired tree. Producer report present at poll try=10 (20:31:13), no stall-escape needed.

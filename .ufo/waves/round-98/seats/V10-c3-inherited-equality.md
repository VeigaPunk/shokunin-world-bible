# V10 c3-inherited-equality — round 98

Seat: V10 (verifier, C3 inherited-equality). Baseline: r97 closure `9a3d648`; pre-round
bytes read via `git show 9a3d648:<path>`. All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no network. Only writes: this report (absolute path) and
`.ufo/waves/round-98/seats/V10-scratch/` (harness `parity.py`, `mapdiff.py`,
`evidence.sh`, `evidence-out.txt`, `r95-pre/` scratch copy). No other file written.

Verification subject: `corpus/fixtures/r98-clerk-filing/` (delivered revision, as of
2026-10-17 20:32:25 -03) and the untouched status of
`corpus/fixtures/r97-crossing-acknowledgment/`. Poll target: S3 —
`S3-fixture-author.md` landed and was read before any verdict (poll record in §7).

## 1. Parsed-value equality, every inherited row (r98 vs r97)

Method: `git show 9a3d648:...` → `json.loads` for r97; worktree bytes → `json.loads`
for r98; deep Python equality on the inherited slices. Harness:
`.ufo/waves/round-98/seats/V10-scratch/parity.py` (r97 side always from the baseline
commit, never the worktree). Full output in `V10-scratch/evidence-out.txt` §2:

```
PASS entities len==6 :: got 6
PASS entities[:5] parsed-equal :: r97 len 5
PASS entities[5].id==clerk-maren :: clerk-maren
PASS entities[5].kind==character
PASS entities[5] one claim citing new source
PASS only new entity id
PASS relations parsed-equal (len 1) :: r98 [{'from': 'aru', 'to': 'evin', 'type': 'agreed_co_stewardship_for_this_crossing', 'source_id': 'crossing-minute'}]
PASS timeline len==7 :: got 7
PASS timeline[:6] parsed-equal :: r97 len 6
PASS timeline[6].id==clerk-filing-open :: clerk-filing-open
PASS timeline[6].tick==14 :: 14
PASS timeline[6].entity_id==clerk-maren :: clerk-maren
PASS timeline[6].place_id==chalk-stair :: chalk-stair
PASS timeline[6].depends_on==[acknowledgment-aru-records] :: ['acknowledgment-aru-records']
PASS timeline[6].source_id==clerk-filing-note :: clerk-filing-note
PASS sources len==7 :: got 7
PASS sources[:6] parsed-equal :: r97 len 6
PASS sources[6].id==clerk-filing-note :: clerk-filing-note
PASS contradictions parsed-equal ([]) :: []
FAILS: 0
```

20/20 checks PASS. The only new entity is `clerk-maren` (id sequence
`aru, evin, quiet-rise, salt-court, chalk-stair, clerk-maren`; `entities[:5]` deep-equal
including the nested `claims` arrays, so no field of any inherited entity changed).
Counts are exactly as declared: entities 5→6, relations 1→1, events 6→7, sources 6→7,
contradictions 0→0. New rows match C3: `clerk-maren` (character, name `Maren`,
`first_appearance: clerk-filing-note`, one claim citing `clerk-filing-note`);
`clerk-filing-open` (tick 14, `entity_id: clerk-maren`, `place_id: chalk-stair`,
`depends_on: ["acknowledgment-aru-records"]`, `source_id: clerk-filing-note`,
description records the filing and the matter OPEN with no finding / no resolution);
`clerk-filing-note` source (title `Maren's Chalk Stair Registry Filing Note`, kind
`fictional first-person note`).

## 2. Byte-level inheritance (cmp / prefix exactness)

**2a. r97 dir byte-untouched** — `git diff --stat 9a3d648 -- corpus/fixtures/r97-crossing-acknowledgment/`
is empty and `git status --porcelain` prints nothing for that dir, checked at 20:27,
20:29 (after S3's r95 repair landed) and again at 20:32:36 (final). All ten r97 file
sha256s equal their `9a3d648` blobs (e.g. entities `026af0bc…`, timeline `73063a86…`).
The r97 fixture was not touched by any producer.

**2b. r98's three extended JSON tables preserve the inherited bytes exactly.** For each
file the longest common byte prefix with r97 equals `len(r97) - 3` (the start of the
trailing `"\n]\n"`), the divergence is the inserted `",\n"` + new row, and the file still
ends `"\n]\n"`:

```
entities.json: LCP=1446 == len(r97)-3 (1446) -> True; prefix_exact=True; r98[L:L+2]=b',\n'; r98_tail=b'\n]\n'
sources.json:  LCP=2232 == len(r97)-3 (2232) -> True; prefix_exact=True; r98[L:L+2]=b',\n'; r98_tail=b'\n]\n'
timeline.json: LCP=2170 == len(r97)-3 (2170) -> True; prefix_exact=True; r98[L:L+2]=b',\n'; r98_tail=b'\n]\n'
fictional-excerpts.md: strict byte-extension = True ; appended = 777 bytes
```

So every inherited row is byte-identical, not merely value-identical, and the new rows
are appended at the end of each array (no inherited row moved).

**2c. Per-file `cmp` against the `9a3d648` r97 counterpart** (whole r98 dir, 10 files):

```
differs: claim-excerpt-map.md      (S4 rewrite — map)
IDENTICAL: contradictions.json
differs: entities.json             (S3 extension)
differs: fictional-excerpts.md     (S3 extension)
IDENTICAL: inspiration-note.md
differs: README.md                 (S4 rewrite — README)
IDENTICAL: relations.json
IDENTICAL: source-excerpt.md
differs: sources.json              (S3 extension)
differs: timeline.json             (S3 extension)
```

Four files remain byte-identical to the closure blobs (the S3-declared preserving copies:
`contradictions.json` `37517e5f…`, `inspiration-note.md` `58f5390e…`,
`relations.json` `c279254b…`, `source-excerpt.md` `b5edc2fd…`); `fictional-excerpts.md`
is a strict byte-extension (prefix sha256 `8ba491cb…` = the r97 file, matching S3's
claim); the two S4-rewritten docs differ by design. Note on the LOG declaration's
"byte copies of the other 7 files": the 7 files other than the three JSON tables were
all copied byte-identically from `9a3d648` (S3 report §B); at the delivered revision 4
of those 7 remain byte-identical, `fictional-excerpts.md` was extended by S3, and
`README.md` + `claim-excerpt-map.md` were rewritten by S4 — measured state, not a
contradiction of the copy-stage claim.

## 3. Map rows: 17 inherited + 3 new

`V10-scratch/mapdiff.py` compares the r97 and r98 map JSON-fact tables cell by cell:

```
r97 map JSON-fact rows=17  r98 map JSON-fact rows=20
columns differing across inherited rows (col idx -> count): {3: 17}
 col 3: 17 rows; sample: J01: '`r97-crossing-acknowledgment:paired-clock`' -> '`r98-clerk-filing:paired-clock`'
byte-identical rows among first 17: 0
NEW ROW: J18 | `entities.json#/5/first_appearance` (`clerk-maren`) | `r98-clerk-filing:clerk-filing-note`
NEW ROW: J19 | `entities.json#/5/claims/0` (`statement`, `source_id`) | `r98-clerk-filing:clerk-filing-note`
NEW ROW: J20 | `timeline.json#/6` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `r98-clerk-filing:clerk-filing-note`
```

All 17 inherited rows are identical in every column except the path-qualification column
(column 3), which names the r98 namespace — exactly the exception the r98 map's own
prose states ("only the path-qualification column names this fixture's cluster path"),
and the same class as r97's r96-inheritance note. The 2 Spence editorial rows (`| S0…`)
are byte-identical between the two maps (`diff` empty). The r98 map's new-row spans
(lines 55–64 of the extended `fictional-excerpts.md`) match the file: section heading at
55, quoted filing lines 59–62, scope at 64, total 64 lines.

## 4. Receipts on the delivered r98 bytes (corroboration, own runs)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
```

Census: baseline `git ls-tree -d 9a3d648 corpus/fixtures/` = 171 dirs; worktree
`ls -d corpus/fixtures/*/` = 172; the only set difference is
`corpus/fixtures/r98-clerk-filing` — 171→172 as declared, no other fixture dir added or
removed. All changed/untracked paths under `corpus/fixtures/` are exactly the r95 map
(modification) and the r98 dir (untracked).

## 5. S3 claim cross-checks (the polled producer)

Every checkable claim in `S3-fixture-author.md` was re-run independently:

- delivered hashes match exactly: entities `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984`,
  sources `32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3`,
  timeline `eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af`,
  fictional-excerpts `29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de`;
- prefix claim: `head -c 3410 fictional-excerpts.md | sha256sum` = `8ba491cb…` = the r97 file
  sha256 (`git show 9a3d648:…fictional-excerpts.md | sha256sum`);
- interim state claim: while the r98 dir still carried the copied r97 map, my own run
  produced exactly the three `missing_obligation` findings
  (`entities.json#/5/claims/0`, `entities.json#/5/first_appearance`, `timeline.json#/6`)
  and nothing else, then PASS after S4's rewrite;
- r95 repair: `git diff --stat 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/` =
  `1 file changed, 1 insertion(+), 1 deletion(-)` (line 49 only), file sha256
  `80440d61…`; I replayed both map versions in `V10-scratch/r95-pre/` (baseline map
  restored from `9a3d648` over a scratch copy) and the `map_obligations` (15/15 PASS),
  `check_bible` (CLEAN) and `support_check` (15/15 + 2/2 PASS) receipts are identical
  before vs after; `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath`
  → `DIGEST d541ae64…` `RESULT PASS` (pin unbroken).

## 6. Observations / residuals (evidence, outside my verdict)

1. **Placeholder-poll hazard, observed live.** At 20:28 (before S3's extension) the
   whole r98 dir existed as 10 files byte-identical to r97 — counts 5/1/6/6, all 10
   `cmp`-same — so an existence-only or dir-existence poll would have been satisfied by
   the placeholder copy; `map_obligations` was `raw=20 mapped=17 FAIL` in that window.
   I verified only after the content condition (6/7/7 rows) was met. Confirms S3's
   report item D1.
2. **Freeze pin state at verification time.** `corpus/tools/dependency-freeze-contract.json`
   still listed 4 pins (`r88-m3-maya-cluster`, `r94-paired-crossing`,
   `r95-crossing-aftermath`, `r96-crossing-response`) at 20:32 — the r97/r98 pins (C2)
   were not yet present, so pin-side equality is S1/other seats' scope, not verified here.
3. **S3's hashes were stable** across my runs (20:29 → 20:32); the r98 JSON mtimes are
   20:28:55 and S4's docs 20:30:21/20:30:41, all predating my final verification, so the
   revision I report on is the settled one.
4. S3's report item D5 (parent-repo stray `baseline-analyze.txt`) is outside the lane and
   outside my byte scope; recorded as reported evidence, not independently re-verified here.

## 7. Poll record (stall-escape, per protocol)

- 20:27: r98 dir absent; S reports absent. Baseline captured.
- 20:28: r98 dir appeared as a 10-file byte copy of r97 (placeholder) — not verified;
  content condition (6/7/7) enforced instead of existence.
- 20:29–20:30: S3's JSON extension landed (6/7/7); r95 map repair landed; S4's map
  landed at 20:30:21, README 20:30:41.
- ~20:31: `S3-fixture-author.md` (poll target) and `S4-fixture-docs.md` present; read
  before verdict. Background polls exited on these conditions; no wait for ALL reports
  was performed, so no self-subtraction hazard arose.
- At report time S1/S2/S5 were still mid-flight (freeze contract modified but not
  re-pinned; `corpus/tools/README.md` unchanged; no `r98-clerk-scope-note.md`), which is
  expected for the mid-wave state and does not affect the r98-fixture equality claims
  verified here. If closure changes any r98/r97 fixture byte after 20:32:36, this
  verification must be re-run.

## Bottom line

**PASS** — on the delivered r98 revision (2026-10-17 20:32:25): all inherited rows are
parsed-value identical to r97 (`entities[:5]`, `relations`, `timeline[:6]`, `sources[:6]`,
`contradictions`; 20/20 checks), `clerk-maren` is the only new entity, the three extended
JSON tables preserve the inherited bytes exactly (LCP = len−3, `cmp`-verified) and
`fictional-excerpts.md` is a strict byte-extension, the r97 dir is byte-untouched vs
`9a3d648`, the map carries 17 inherited rows (namespace column only) + 3 new rows, and
the r98 receipts are `check_bible` CLEAN, `map_obligations` 20/20 PASS, `support_check`
20/20 + 2/2 PASS with census 171→172.

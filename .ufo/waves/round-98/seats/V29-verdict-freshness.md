# V29 — verdict-freshness (round 98)

Seat: **V29 verdict-freshness** (verifier). Role: one **FRESHNESS** verdict on the delivered
bytes of round 98, with the two **dated correction addenda** (S5: `corpus/knowledge/
r95-aftermath-scope-note.md`, `corpus/knowledge/r96-response-scope-note.md`) as the judged bytes.
Baseline: r97 closure `9a3d648`; wave tree uncommitted; HEAD `dd4df1b`. All commands ran from the
lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`; every write resolved under
`lore-shokunin/` (report path absolute; scratch under `V29-scratch/`). Read-only outside this
report and `.ufo/waves/round-98/seats/V29-scratch/`. Leaf seat: no nested agents, no commits, no pushes, no
network. I did not verify C1/C2/C3 semantics (other seats' scope); this report covers freshness
only, with adjacent producer-doc facts noted where they are freshness facts.

## Verdict question, answered directly

Do the two dated addenda repair the carried stale tool pins (r97 closure: "two carried stale
knowledge-note tool pins unrepaired, correctable next touch") with accurate, dated, append-only
bytes — and does the round's own new durable bytes introduce any stale pin? **Yes, and no.**
Every factual claim in both addenda reproduced under my own commands and git history; both are
append-only (14 insertions / 0 deletions each) with the historical text preserved unrewritten;
no live corpus doc cites the superseded shas as current; every live pin on the delivered revision
is fresh (map pair `86b52949…`/`2142b991…`, checker `ff9fd2aa…`, support `55a5eb27…`, all six
chain digests, revision labels resolving). Two bounded observations are recorded for L1 (§F-1
S2's README diff sentence; §F-2 the r98 note's time-indexed dependency_freeze snapshot); neither
touches the addenda. Net movement of the axis: **improved (bounded)** — the two carried items are
repaired, and the round adds no stale live pin.

## Poll-wait record (artifact-based; never verified a plan)

- Poll 1 (`V29-scratch/poll.sh`, 20 s cadence, log `V29-scratch/poll.log`): targets = r98 note +
  both addenda. `t=60s` addenda detected (`r95add=yes r96add=yes`); `t=260s` r98 note detected →
  `POLL_HIT elapsed=260s checks=13`. S5's report was absent at hit time.
- Poll 2 (`V29-scratch/poll2.sh`, log `V29-scratch/poll2.log`): targets = S1/S2/S5 producer
  reports (ENDGAME convention: subtract SELF — no V-seat report was ever a gate). `t=40s` S5
  present; `t=160s` S1+S2 present → `POLL2_HIT elapsed=160s`. No stall escape needed; no wait
  exceeded budget. Intermediate states were never verified as final: the r98 note was revised at
  `20:33:01` (my first read, sha `a73cd57b…`, was superseded by the delivered `1162262c…`, which
  matches S5's own report) and S1's pair moved through `b06275f3…`→`3b6cf892…`→`1a01fd17…`→`03d04365…`
  (final) before freezing.
- Host condition: `/tmp` inodes fine this round (`df -i /tmp` → `2%` used); no scratch relocation
  needed.

## Delivered revision measured (freeze 2026-10-17T20:37-03:00, drift-checked twice)

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
```

`git status --porcelain -uall | grep -v '^?? .ufo/'` at freeze shows exactly the declared change
set: `M LOG.md`, `M` r95 map, `M` the two knowledge notes, `M` the three `corpus/tools/` files,
and the eleven new `r98-clerk-filing/` + r98-note paths. Nothing else.

## The two addenda — judged byte by byte

### Shape, dating, append-only discipline

```
$ git diff --numstat 9a3d648 -- corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md
14	0	corpus/knowledge/r95-aftermath-scope-note.md
14	0	corpus/knowledge/r96-response-scope-note.md
```

One hunk each, at EOF, additions only; the original receipt paragraphs are byte-preserved
("The receipts paragraph above is preserved unrewritten"; "The historical text above stays
unrewritten; this addendum is the correction of record"). Both sections are dated
"Correction addendum (2026-10-17, round 98, S5 knowledge-notes seat)" with a quoted measurement
timestamp `2026-10-17T20:28:35-03:00`; file mtimes `20:29:14` are after that measurement — the
stated order holds. Byte hygiene: 71 / 75 lines, trailing newline true, zero CRLF. No
re-certification: the addenda explicitly mark the old pins as stale and historical, and instruct
future re-derivation instead of asserting the old values remain current.

### Claim-by-claim verification (my own runs)

**Commit-history claims.** All commits touching the two files, across all refs, hashed by me:

```
$ git log --all --pretty=%H -- corpus/tools/map_obligations.py | while read c; do ... done
abbc3e01 cc1df4dc4068   (r94 checkpoint commit)
dcb2d928 d1c239ccb214   (r95 closure)
f3e09f93 2b0ba815326b   (r96 closure)
9d25df9b 86b529496214   (r97 closure)
$ ... -- corpus/tools/map-obligations-contract.json
abbc3e01 349a1956714c
dcb2d928 8173bb97592a
f3e09f93 97b76bb8b1fe
9d25df9b 2142b9917694
```

The addenda's committed sets (`cc1df4dc`/`d1c239cc`/`2b0ba815`/`86b52949` for the tool;
`8173bb97` = r95, `97b76bb8` = r96 for the contract) match exactly; `8173bb97…` at commit
`dcb2d92` and `d1c239cc…` = r95 delivered (accurate as history) are both correct.

**"Never entered committed history."**

```
$ git rev-list --all --objects | grep -E "9224a684|6634e176|ca05159e"
(no output)
```

`9224a684…` and `6634e176…` appear in no commit tree; the r95 P5 seat report independently
records `9224a68410aea890…` as the in-flight value at 16:25 (`.ufo/waves/round-95/seats/
P5-knowledge-note.md:53`), and the r96 note records `6634e176…` as its in-flight value — the
addenda's "in-flight, never committed" characterisation is correct.

**Current-pin claims.** My own `sha256sum` (above) matches every current hash quoted in both
addenda: `map_obligations.py 86b52949…`, contract `2142b991…`, `check_bible.py ff9fd2aa…`,
`support_check.py 55a5eb27…`. The r95 addendum's forward-looking sentence — round 98's C1 owns
only the dependency_freeze pair, "so the two hashes above should hold unless a later round
changes them" — is confirmed: at freeze `git diff --name-only 9a3d648 -- corpus/tools/` contains
no map-tool file; the map pair is byte-identical to its r97 closure value throughout the round.

**Receipt claims, re-derived at the quoted revision.** All green, exit 0, values identical to
those quoted in the addenda:

```
check_bible r95 → CLEAN: schema, citations, relations, timeline; 0 violations
map_obligations r95 → OBLIGATIONS raw=15 mapped=15 / INVENTORY 15/15; 2/2; 17/17 / RESULT PASS
support_check r95 → SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17 / RESULT PASS
check_bible r96 → CLEAN: schema, citations, relations, timeline; 0 violations
map_obligations r96 → OBLIGATIONS raw=16 mapped=16 / INVENTORY 16/16; 2/2; 18/18 / RESULT PASS
support_check r96 → SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18 / RESULT PASS
map_obligations r97 → raw=17 mapped=17 / RESULT PASS      (quoted by the r98 note, verified)
```

**No live doc cites the superseded shas as current.**

```
$ grep -rn "9224a684\|6634e176\|8173bb97" --include="*.md" corpus/
→ only the two notes themselves (their historical text + their own addenda);
  SCORECARD.md:451 and LOG.md:2830/3059 are historical closure/declaration records
```

## Freshness surface — the round's own bytes (adjacent evidence)

- **r98 fixture pin-free.** `grep -rnoE "[0-9a-f]{12,64}|\bHEAD\b|9a3d648|dd4df1b"
  corpus/fixtures/r98-clerk-filing/` → no matches. Its quoted receipts replay green:
  `check_bible` CLEAN exit 0; `map_obligations` `raw=20 mapped=20` / `20/20; 2/2; 22/22` PASS;
  `support_check` `20/20; 2/2; 22/22` PASS.
- **r95 map repair (S3)** removes the carried stale "new relation" sentence:
  `grep -c "new relation" corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` → `0`;
  no sha/HEAD pins inside; receipts unchanged (above).
- **r98 note (S5)** carries the standard metadata header plus a citation convention; its pins
  (map pair, checker, support) are current. One bounded observation: §F-2.
- **tools README (S2)** Round-98 addendum (`:230+`) quotes receipts I reproduced:
  six-fixture chain digests match exactly (`r97 3c922d20a01bbd3f…`, `r98 59a0f4fa3d4a47e0…`,
  all six `RESULT PASS` exit 0), `--self-test` → `SELF-TEST 17/17 / RESULT PASS` exit 0, and the
  REDUCTION-DETECTED demo reproduced verbatim on my own mirror tree (intact copy exit 0 digest
  `3c922d20…`; edge-dropped copy `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records
  lost depends_on ['response-evin-salt-court']` / `RESULT FAIL` exit 1). Contract revision labels
  all resolve (`60dba0c2`, `23939342`, `dd4df1b3` → `git rev-parse --verify` OK); all six pins
  carry repo-relative paths; `self_test.expected` = 17 keys. One bounded observation: §F-1.
- **Closure-side doc sites (V22 inventory, L1-owned, pending state as in every round):**
  `corpus/fixtures/README.md` Round-98 section + census re-declaration (measured 172/38/134/421),
  `corpus/README.md:31/37/38`, `SKILL.md:96–100`, `corpus/knowledge/r91-c9-watch.md` r98 row.
  Judged here as pending closure state, not producer omissions.

## F-1 — tools README "Unchanged" diff sentence does not reproduce (bounded, S2 bytes)

`corpus/tools/README.md` (final bytes, `1d299c16…`) says: "`git diff 9a3d648 -- corpus/tools/`
lists only `dependency_freeze.py` and `dependency-freeze-contract.json`". On the delivered tree
the same command lists **three** files — the README's own round-98 change is part of that diff:

```
$ git diff --name-only 9a3d648 -- corpus/tools/
corpus/tools/README.md
corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency_freeze.py
$ git diff --stat 9a3d648 -- corpus/tools/
 corpus/tools/README.md                       |  56 ++++++++
 corpus/tools/dependency-freeze-contract.json | 193 ++++++++++++++++++++++++++-
 corpus/tools/dependency_freeze.py            |  42 +++++-
```

The sentence's evident intent (only the two tool-code files changed) is true; the literal command
claim is false on delivered bytes. S2's report repeats the same claim (`S2-tools-docs.md:146`).
Bounded doc inaccuracy, disclosed for L1; it does not affect any gate or any quoted receipt
(all replay). Under the r96 convention this is a **condition**, not material axis harm.

## F-2 — r98 note's dependency_freeze snapshot is time-indexed (bounded, not the addenda)

The r98 note's receipt paragraph (final bytes `1162262c…`, measured `20:31`) records S1's landing
as "`dependency_freeze.py` `03d04365…`, contract `c435239d…` at `20:32:51-03:00`". At freeze,
`dependency_freeze.py` is still `03d04365…` but the contract is `153ebc5b…` — S1 moved it once
more after the note's snapshot. The statement is explicitly time-stamped, the note instructs
"Re-run all three commands and re-measure the tool revisions against the delivered revision
before citing these receipts", and the note's own pins (map pair, checker, support) are current.
Same class as r97's F-2 (labelled in-flight value + caveat): bounded, disclosed, not a stale live
pin; correctable on the next touch if L1 wants the note's snapshot superseded.

## Historical captures, strays, and hygiene

- `LOG.md` append-only: `git diff --numstat 9a3d648 -- LOG.md` → `61 0` (r98 declaration only).
- Round-97 tree untouched: `git status --porcelain .ufo/waves/round-97/` → empty; `SCORECARD.md`
  unmodified this round (`git status --porcelain SCORECARD.md` → empty).
- Parent-tree check: one untracked `baseline-analyze.txt` in `/home/vgpnk/Projects/shokunin`
  (105 bytes, mtime 20:30:10, content = a `python3: can't open file '…/analyze.py'` error). Not
  written by this seat (all my writes are absolute under `lore-shokunin/`); attribution unknown —
  recorded for the adjacency seat/L1, outside my axis. No other parent stray.
- My writes: this report and `V29-scratch/` only; scratch poll logs, mirror tree, drafts.

## Reconciliation with other seats

- **V22 doc-parity**: independently re-verified the addenda's hash claims
  (`86b52949…`/`2142b991…`/`ff9fd2aa…`/`55a5eb27…` all match) and measured census 172/38/134/421 —
  matches my runs. Its stale-wording list is the closure-side pending set quoted above.
- **V15 c3-r95-repair / V11 c3-support-map / S3 / S4 / S5 / S1 / S2**: their receipts and mine
  agree where they overlap (r95 repair one-line; r98 receipts 20/20; six-fixture chain digests;
  self-test 17/17; S1's final hashes match its report).

## What improved, what was repaired, what was harmed

- **Repaired on this axis:** the two carried stale knowledge-note tool pins (r95 `9224a684…`;
  r96 `6634e176…` + contract `8173bb97…`) — dated, append-only, factually verified addenda.
- **Maintained:** all live pins fresh at freeze; new fixture bytes pin-free; receipts quoted in
  new durable bytes reproduce (fixture receipts, chain digests, self-test, REDUCTION demo);
  historical captures unedited; LOG append-only.
- **Newly harmed (bounded, disclosed):** F-1 (S2 README diff sentence, doc-surface only). F-2 is
  a labelled time-indexed snapshot, not harm under the r97 convention.
- **Pending (L1 closure, as every round):** the V22 doc-parity list (fixtures README Round-98
  section + census, corpus/README bullets, SKILL.md row, C9 r98 row).

## Verdict

**FRESHNESS: IMPROVED (bounded)** — on the delivered r98 revision the two carried stale
knowledge-note tool pins are repaired by dated, append-only addenda whose every hash, history,
and receipt claim I reproduced myself (committed-revision sets `cc1df4dc`/`d1c239cc`/`2b0ba815`/
`86b52949` and `8173bb97`/`97b76bb8`/`2142b991`; the superseded shas in no commit tree; current
pins `86b52949…`/`2142b991…`/`ff9fd2aa…`/`55a5eb27…`; all quoted receipts green), with no live
doc citing a superseded sha as current; the round's own bytes add no stale live pin (r98 fixture
pin-free; all quoted receipts replay, including the REDUCTION-DETECTED demo reproduced on my own
mirror), and historical captures stay unedited (LOG append-only 61/0; round-97 tree and
SCORECARD untouched). Bounds: F-1 (S2 README diff sentence, condition-class) and F-2 (r98 note's
time-indexed dependency_freeze snapshot, labelled and caveated); closure-side doc sites pending
as in every round.

Bottom line: **PASS** — both dated addenda are delivered, accurate, append-only, and verifiably
repair the carried stale pins; freshness improved (bounded), with F-1/F-2 recorded as disclosed
conditions.

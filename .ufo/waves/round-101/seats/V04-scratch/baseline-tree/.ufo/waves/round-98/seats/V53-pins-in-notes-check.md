# V53 — pins-in-notes-check (round 98)

Seat: **V53 pins-in-notes-check** — verifier. Task: verify **every hash quoted in S5's three
note files** (`corpus/knowledge/r98-clerk-scope-note.md`, plus the dated correction addenda in
`corpus/knowledge/r95-aftermath-scope-note.md` and
`corpus/knowledge/r96-response-scope-note.md`) **against delivered bytes at my run time**.
Mismatches are findings, except pins explicitly labeled historical.

Baseline: r97 closure `9a3d648`. All commands from the lane root
(`/home/vgpnk/Projects/shokunin/lore-shokunin`), `python3`, absolute report/scratch paths.
Nothing was written outside this report and `.ufo/waves/round-98/seats/V53-scratch/`.

Protocol: poll-wait honoured — artifact poll (20 s cadence) observed the r95/r96 addenda at
try=4 (20:29:21) and the r98 note at try=14 (20:32:41); **no stall-escape was needed** (well
under the 40-try bound). A second stability watcher was run because the r98 note was caught
**mid-write** (see Finding F1 and the drift note below).

## Verdict summary

| Note | self sha256 | pins | MATCH at run time | findings |
|---|---|---|---|---|
| `r98-clerk-scope-note.md` | `1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8` | 6 | 5 | **1 (F1: `c435239d…` stale)** |
| `r95-aftermath-scope-note.md` (addendum) | `8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827` | 15 | all delivered pins | 0 |
| `r96-response-scope-note.md` (addendum) | `a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048` | 23 | all delivered pins | 0 |

**One finding (F1), non-fatal to the notes' design but real: S5's r98 pin
`c435239d…` for `corpus/tools/dependency-freeze-contract.json` no longer matches delivered
bytes.** It matched when written; S1 rewrote the contract ~45 s later, inside the same round.
Every other quoted hash in all three notes verifies, including every explicitly historical pin.

## Method

Three independent checks, all quoted with observed output below:

1. **Delivered-bytes prefix match** — extract every hash-like token (backticked, with optional
   trailing `…`, plus bare 64-hex tokens from the `sha256sum` code blocks) and brute-force
   match the 8-char prefix against sha256 of every file in the lane tree (scratch excluded from
   the "delivered" verdict).
2. **Path-scoped git history index** — all distinct committed blobs for
   `corpus/tools/map_obligations.py` and `corpus/tools/map-obligations-contract.json`, so
   "never entered the committed history" and "revision X was round N" claims are checkable.
3. **All-objects blob scan** — hash all **5167** blobs reachable from all refs, so a
   "never committed" claim is verified positively rather than by absence of a path hit.

Extraction completeness was checked two ways: a broad case-insensitive sweep for any hex run
the lowercase pattern would miss returned `[]` for both addenda, and a bare-ellipsis sweep
(`[0-9a-f]{7,64}…` outside backticks) returned `count: 0`. So the pin lists below are exhaustive
for these files.

## F1 — r98 pin `c435239d…` is stale at run time (the only mismatch)

S5's r98 note, line 64:

> S1's C1 revisions landed shortly after (`dependency_freeze.py` `03d04365…`, contract
> `c435239d…` at 20:32:51-03:00), while the three checker revisions above were re-measured
> unchanged at that later time.

Observed (final pass, run time `2026-10-17T20:35:42-0300`):

```
== corpus/knowledge/r98-clerk-scope-note.md self= 1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8
  L64  ff9fd2aa     MATCH -> corpus/fixtures/check_bible.py
  L64  55a5eb27     MATCH -> corpus/tools/support_check.py
  L64  86b52949     MATCH -> corpus/tools/map_obligations.py
  L64  2142b991     MATCH -> corpus/tools/map-obligations-contract.json
  L64  03d04365     MATCH -> corpus/tools/dependency_freeze.py
  L64  c435239d     SCRATCH-ONLY(16)
```

The delivered contract at run time:

```
$ sha256sum corpus/tools/dependency-freeze-contract.json
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
$ stat -c '%n %y' corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency-freeze-contract.json 2026-10-17 20:33:36.… -0300
```

`c435239d…` now resolves to **16 scratch copies only** (e.g.
`.ufo/waves/round-98/seats/V39-scratch/chain-demo/corpus/tools/dependency-freeze-contract.json`,
`V07-scratch/contract-frozen-snapshot.json`, `V22-scratch/c2/…`) and **not** to the delivered
path. A direct delivered-path probe confirms the same:

```
$ python3 <scratch>/probe.py     # hash every file, list holders of each prefix
c435239d 17 hits, none at corpus/tools/dependency-freeze-contract.json
153ebc5b 15 hits, incl. corpus/tools/dependency-freeze-contract.json
```

**Attribution — live-write race, not fabrication.** S5's pin was *accurate when written*: I
measured the contract at `c435239d…` myself at 20:33:28 in an earlier pass of this same seat
before S1's next write landed. The churn is S1's continued in-flight work **after** S5's seat
closed: contract mtime `20:32:41` (`c435239d…`, S5's measurement `20:32:51` still saw it) →
mtime `20:33:36` (`153ebc5b…`, current and stable through 20:35:24). S5's *other* C1 pin,
`dependency_freeze.py` `03d04365…`, still matches (mtime 20:31:49, stable).

**Severity:** low-to-moderate. The note's own recheck instruction ("re-measure the tool
revisions against the delivered revision before citing these receipts") already covers this, and
the pin is time-stamped. But the pin is **presented as the current landed revision, not as a
superseded historical value**, so by this seat's rule it is a mismatch and is reported as one.
No receipt in the note depends on it: the three checker revisions it cites
(`ff9fd2aa…`, `55a5eb27…`, `86b52949…` / `2142b991…`) are all still exact.

**Confirmed against S1's own delivery.** S1's seat report (`S1-freeze-hygiene.md`) landed at
20:36:24 and declares its two delivered files as `dependency_freeze.py`
`03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` and the contract
`153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`. S5's `dependency_freeze.py`
pin therefore matches S1's final delivery, and S5's contract pin does not. The contract held
`153ebc5b…` (mtime 20:33:36) through my last check at 20:36:24, so F1 is not a transient
in-flight artifact — it stands against S1's declared final revision.

## r98-clerk-scope-note.md — remaining pins (5/6 MATCH)

```
run_at 2026-10-17T20:35:42-0300
ff9fd2aa  -> corpus/fixtures/check_bible.py                  ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
55a5eb27  -> corpus/tools/support_check.py                   55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
86b52949  -> corpus/tools/map_obligations.py                 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9
2142b991  -> corpus/tools/map-obligations-contract.json      2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41
03d04365  -> corpus/tools/dependency_freeze.py               03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b
```

The note's own self-hash, quoted in S5's seat report, verifies:

```
$ sha256sum corpus/knowledge/r98-clerk-scope-note.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
```

**Drift note (recorded, not a finding).** The r98 note was caught mid-write: at 20:32:58 it read
`a73cd57b…` with 4 pins; at 20:33:14 it read `1162262c…` with 6 pins (S5 added the two C1 pins).
I discarded the first reading and re-verified everything at the frozen `1162262c…` revision,
which S5's own report names. The r95/r96 addenda never drifted (both mtime 20:29:14, unchanged
through finalization).

**Receipts re-derived at my run time (not hash claims, but the paragraph carrying the pins):**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations      exit 0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                      exit 0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                      exit 0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17 … RESULT PASS                       exit 0
```

Every line matches the note's quoted receipt text **verbatim**, including
`DISTINCT-ANCHORS 18/18` and `ANCHORS repeated-references=4; DUPLICATE-ROWS 0`, which I
reproduced from the full (untruncated) output.

## r95 addendum — 15 pins, all verified

```
L51 (historical paragraph, preserved unrewritten)
  ff9fd2aa  MATCH -> corpus/fixtures/check_bible.py
  55a5eb27  MATCH -> corpus/tools/support_check.py
  9224a684  SCRATCH-ONLY(2)
  cc1df4dc  SCRATCH-ONLY(20)
  ca05159e  NO-MATCH
L61 (addendum)
  9224a684 SCRATCH-ONLY(2)   cc1df4dc SCRATCH-ONLY(20)   d1c239cc SCRATCH-ONLY(50)
  2b0ba815 SCRATCH-ONLY(130) 86b52949 MATCH -> corpus/tools/map_obligations.py
L65  86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9 MATCH -> corpus/tools/map_obligations.py
L66  2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41 MATCH -> corpus/tools/map-obligations-contract.json
L69  ff9fd2aa MATCH  55a5eb27 MATCH      L71  9224a684 (instruction "do not cite as current")
```

Both **full 64-hex** pins match delivered bytes exactly. The addendum's structural claims check
out:

- **"the committed revisions are `cc1df4dc…` r94, `d1c239cc…` r95, `2b0ba815…` r96,
  `86b52949…` r97"** — path-scoped history yields **exactly four** distinct committed blobs for
  `corpus/tools/map_obligations.py`, one per named revision:

  ```
  cc1df4dc  map_obligations.py  rev abbc3e01   -> "lore r94: checkpoint Luna WORK candidate pending DeepSeek review"
  d1c239cc  map_obligations.py  rev dcb2d928   -> "lore r95: freeze admitted wave + closure docs …"
  2b0ba815  map_obligations.py  rev f3e09f93   -> "lore r96: freeze admitted wave + closure docs …"
  86b52949  map_obligations.py  rev 9d25df9b   -> "lore r97: freeze admitted wave + closure docs …"
  ```

- **"`9224a684…` … never entered the file's committed history"** — verified positively by the
  all-objects scan: the only holder is `.ufo/waves/round-95/seats/V01-scratch/map_obligations_NEW.py`
  (a round-95 scratch copy), never `corpus/tools/map_obligations.py`.

- **Receipts re-derived unchanged** (matches the addendum's claim exactly):
  `check_bible` CLEAN exit 0; `support_check` `JSON-FACTS 15/15; EDITORIAL-ROWS 2/2;
  TOTAL-ROWS 17/17` + `SOURCE-SUPPORT 15/15; MODES 17/17; VALIDATED-ROWS 17/17` / `RESULT PASS`
  exit 0; `map_obligations` `raw=15 mapped=15` / `RESULT PASS` exit 0.

**`ca05159e…` — observation, not a finding.** This pin (historical paragraph: "an intermediate
in-flight revision (`ca05159e…`) raised an uncaught `ValueError`") matches **no blob anywhere**
in the repository — not delivered, not scratch, not in history. It is explicitly labeled an
in-flight intermediate, which is exactly what an uncommitted, since-deleted scratch revision
looks like, so by this seat's rule it is **not** a finding. Recorded for completeness: it is the
one quoted hash in all three notes that cannot be positively corroborated.

## r96 addendum — 23 pins, all verified

Same shape as r95; every delivered pin matches, every historical pin is correctly labeled.
Additional checks specific to this addendum:

```
L55  6634e176 SCRATCH-ONLY(2)  8173bb97 SCRATCH-ONLY(22)  d1c239cc SCRATCH-ONLY(50)
L65  6634e176 cc1df4dc d1c239cc 2b0ba815 86b52949(MATCH) 8173bb97(x2) dcb2d92 97b76bb8 d1c239cc
L69  86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9 MATCH -> map_obligations.py
L70  2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41 MATCH -> map-obligations-contract.json
L73  ff9fd2aa MATCH  55a5eb27 MATCH     L75  6634e176  8173bb97
```

- **`dcb2d92`** shows `NO-MATCH` in my blob index **by design** — it is a **commit** hash, not a
  file digest. Verified separately as the addendum claims: `git log -1 dcb2d92` →
  `dcb2d92 lore r95: freeze admitted wave + closure docs (corrections, README/C9/SKILL updates, receipt 64/64)`.
- **"`8173bb97…` is `corpus/tools/map-obligations-contract.json` at its r95 revision (…, commit
  `dcb2d92`)"** — confirmed twice: path-scoped history places blob `8173bb97` at rev `dcb2d928`
  (= commit `dcb2d92`), and the all-objects scan finds it as
  `.ufo/waves/round-96/scratch/V02/contract.r95.json`.
- **"the r96 closure delivered `97b76bb8…`"** — path-scoped history places blob `97b76bb8` at
  rev `f3e09f93` (the r96 closure commit); all-objects holder:
  `.ufo/waves/round-96/seats/V01-scratch/new/tool/map-obligations-contract.json`.
- **"`6634e176…` … never entered the file's committed history"** — positively confirmed: sole
  holder is `.ufo/waves/round-96/seats/V47-scratch/tool-intermediate.py`.
- **"`d1c239cc…` … is the r95 delivered revision — accurate as history, not current"** — correct;
  it is also the current value **only** for nothing (current is `86b52949…`), so the
  "not current" framing is right.
- **Receipts re-derived unchanged**: `check_bible` CLEAN exit 0; `support_check`
  `JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` + `SOURCE-SUPPORT 16/16; MODES 18/18;
  VALIDATED-ROWS 18/18` / `RESULT PASS` exit 0; `map_obligations` `raw=16 mapped=16` /
  `RESULT PASS` exit 0.

## Adjacency observations (recorded, outside this seat's core claim)

- **No stray writes by S5.** All three S5 files are under `corpus/knowledge/` as declared; no
  parent-tree or out-of-lane writes observed. The r94-F01 stray-write class did not recur from
  this seat.
- **`v05-self-test-scratch/` at the lane repo root is not a stray.** It is covered by the
  declared `.gitignore` rule `*-self-test-*/` ("self-test scratch for corpus tools (transient,
  repo root)"), so `git status --porcelain` does not show it. A transient sibling
  `dependency-freeze-self-test-n030adgq/` appeared during my scan and was gone by 20:35 — also
  covered by the same rule.
- **Timestamp coincidence, recorded for transparency.** S5's addenda state their measurement
  time as `2026-10-17T20:28:35-03:00`; my own unrelated pre-scan also stamped `20:28:35-0300`.
  Both are independent measurements of the same files and agree on every hash, so nothing turns
  on it, but a reviewer diffing timestamps should not read it as a shared run.
- **Tool-revision drift in the round.** The r95/r96 addenda's forward-looking sentence
  ("Round 98's C1 work owns `dependency_freeze.py` and its contract, not `map_obligations.py` or
  its contract, so the two hashes above should hold") **holds at my run time**:
  `map_obligations.py` `86b52949…` and `map-obligations-contract.json` `2142b991…` are unchanged
  from r97, while S1's two files moved (`dependency_freeze.py` `b06275f3…`→`03d04365…`;
  contract `27273be2…`→`c435239d…`→`153ebc5b…`).

## Limits of this verification

This is a hash-pin audit only. It confirms that quoted digests match delivered bytes and that
quoted commit/revision attributions match git history; it does **not** judge whether the notes'
prose claims are correct, whether the receipts mean what the notes say, whether the fiction is
consistent, or anything about rights, permission, or canon. I did not re-verify the fixture
content itself (other seats own that). Findings are stated against the tree as it stood at
`2026-10-17T20:36:24-0300`; the wave tree is uncommitted, so any further write to a pinned file
before closure re-opens F1.

**Bottom line: FAIL (narrow) — all 44 quoted hash occurrences across S5's three notes are
accounted for and 43 verify; the single mismatch is `c435239d…` for
`corpus/tools/dependency-freeze-contract.json` in the r98 note. It was accurate when written
(20:32:51), was superseded by S1's rewrite at 20:33:36, and contradicts S1's own declared final
delivery of `153ebc5b…`. Every explicitly historical pin is correctly labeled, and no receipt in
any of the three notes depends on the stale pin.**

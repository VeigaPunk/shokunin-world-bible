# V45 byte-prefix-2 — round 98

Seat: V45 (verifier, byte-prefix-2). Baseline: r97 closure `9a3d648` (pre-round bytes
via `git show 9a3d648:<path>`). All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no pushes, no network. Writes: this report (absolute path),
`.ufo/waves/round-98/seats/V45-scratch/` (poll script/log, verify script, hash
snapshots, baseline byte copies). No producer-owned file was written by this seat.

Scope: `corpus/fixtures/r98-clerk-filing/` versus `corpus/fixtures/r97-crossing-acknowledgment/`
— (1) `cmp` of the copied files, (2) JSON-level diff of `sources.json` / `timeline.json` /
`entities.json` (appended rows only), (3) `fictional-excerpts.md` strict byte-prefix.
Everything below is on the frozen final revision (hashes re-confirmed stable across
four snapshots, `hashes-1..4.txt`, spanning 20:31–20:34; final list in §6).

## 0. Poll-wait record (ENDGAME: SELF subtracted)

Poll script `.ufo/waves/round-98/seats/V45-scratch/poll.sh` (20 s cadence, 40 tries)
watched only my seat's inputs — S3's four files plus S4's two files. Log
(`V45-scratch/poll.log`):

```
try 1 20:28:16 missing: entities.json sources.json timeline.json fictional-excerpts.md README.md claim-excerpt-map.md
try 2 20:28:36 ALL-PRESENT
```

`ALL-PRESENT` at 20:28:36 was S3's delivery with S4's two files still present as S3's
r97 placeholder byte-copies (S3's report confirms: "copied as placeholders and are
S4's to rewrite"). Bounded waits then tracked S4's landing:

- 20:30:34 `claim-excerpt-map.md` changed (`49d4834e124f…` → `c1099d0ee9ee…`) — S4-LANDED.
- 20:30:57 `README.md` changed (`d9387b7d7326…` → `32efc78f70e6…`) — README-LANDED.
- 20:32:28 `S4-fixture-docs.md` report present (poll for the producer report).

No unbounded stall, no stall-escape needed; every wait was bounded and returned.
S3's four owned files were never modified after their first appearance (hashes
identical in all four snapshots).

## 1. `cmp` — pure copied files (r97 and 9a3d648)

```
$ for f in contradictions.json inspiration-note.md relations.json source-excerpt.md; do
    cmp corpus/fixtures/r97-crossing-acknowledgment/$f corpus/fixtures/r98-clerk-filing/$f; done
```
Observed: `cmp` rc=0 for all four (empty output). Re-run directly against the
closure bytes (baseline copies extracted with `git show 9a3d648:…` into
`V45-scratch/baseline/`):

```
IDENTICAL-to-9a3d648  contradictions.json
IDENTICAL-to-9a3d648  inspiration-note.md
IDENTICAL-to-9a3d648  relations.json
IDENTICAL-to-9a3d648  source-excerpt.md
```

**Verdict: PASS** — the four non-extended copies are byte-identical to both r97 and
the r97-closure revision.

## 2. JSON-level diff — appended rows only

Parser check on both revisions, then row-wise prefix comparison (`V45-scratch/verify.py`,
`verify-final.out`):

```
entities.json: r97=5 r98=6 prefix-exact=True appended=['clerk-maren']
sources.json:  r97=6 r98=7 prefix-exact=True appended=['clerk-filing-note']
timeline.json: r97=6 r98=7 prefix-exact=True appended=['clerk-filing-open']
```

- Every r97 row survives as an exact parsed prefix (deep equality on the first
  `len(r97)` rows); exactly one row appended per table; nothing removed or reordered.
- Appended rows (verbatim from the diff):
  - `entities.json` → `{"id": "clerk-maren", "kind": "character", "name": "Maren",
    "first_appearance": "clerk-filing-note", "claims": [{"statement": "The filing note
    names Maren, the clerk of the Chalk Stair registry, as the officer who filed both
    pending accounts.", "source_id": "clerk-filing-note"}]}`
  - `sources.json` → `{"id": "clerk-filing-note", "title": "Maren's Chalk Stair Registry
    Filing Note", "kind": "fictional first-person note", "reliability_note": "…records
    the matter OPEN. It asserts no finding, no verdict, no reconciliation, and no
    resolution; it is not evidence of a breach, a continuing duty, a winner between the
    accounts, or an external historical fact."}`
  - `timeline.json` → `{"id": "clerk-filing-open", "tick": 14, "entity_id": "clerk-maren",
    "place_id": "chalk-stair", "depends_on": ["acknowledgment-aru-records"],
    "description": "At the Chalk Stair at tick 14, the clerk filed both pending accounts
    and recorded the matter OPEN, asserting no finding and no resolution.",
    "source_id": "clerk-filing-note"}`
- Stronger raw-byte check at the append junction: r98 shares r97's bytes up to the
  final newline before r97's closing `]`, which became `,`:

```
entities.json: r97=1449B r98=1793B raw-shared-prefix=1446B of r97-pre-bracket=1447B  next-r98-bytes=b',\n  {\n    "id": "clerk-maren",'
sources.json:  r97=2235B r98=2725B raw-shared-prefix=2232B of r97-pre-bracket=2233B  next-r98-bytes=b',\n  {\n    "id": "clerk-filing-'
timeline.json: r97=2173B r98=2552B raw-shared-prefix=2170B of r97-pre-bracket=2171B  next-r98-bytes=b',\n  {\n    "id": "clerk-filing-'
```
  (The one unshared byte is r97's newline before `]`; r98 inserts `,\n  {new row}\n`
  there — i.e. a pure append, no inherited byte touched.)
- Counts and referential integrity of the new rows (strict `json.load` on all five
  JSON files): entities 6, relations 1, events 7, sources 7, contradictions 0; ticks
  `[9, 9, 10, 11, 12, 13, 14]`; new entity source resolves, new event source/entity/
  place resolve, `depends_on ["acknowledgment-aru-records"]` resolves to an existing
  timeline event (all True).

**Verdict: PASS** — appended rows only, in all three tables.

## 3. `fictional-excerpts.md` strict byte-prefix

```
$ python3 -c "b97=open('corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md','rb').read();
              b98=open('corpus/fixtures/r98-clerk-filing/fictional-excerpts.md','rb').read();
              print(len(b97), len(b98), b98.startswith(b97))"
3410 4187 True
```

r97's exact 3410 bytes are preserved; 777 bytes appended, beginning:

```
b'\n## Round 98 clerk filing (2026-10-17)\n\nNewly authored fictional first-person note,
attributed to in-world source ID `clerk-filing-note`, folio 8, lines 1\xe2\x80\x934. This
section is appended after the preserved r97 text above; the inherited wording is unchanged.
\n\n> Tick 14: I filed both pending accounts at the Chalk Stair registry.\n> I am Maren, clerk
of the Chalk Stair registry, and I record the matter'
```

Line accounting: r97 = 53 lines; r98 = 64 lines; appended region = lines 54–64 (blank
separator line 54, `## Round 98 clerk filing` heading line 55, quoted note lines 59–62,
scope paragraph line 64). Both files end with a newline. S4's r98 map anchors its three
new rows only inside that region (`J18` line 60, `J19` lines 59–60, `J20` lines 55–64),
consistent with the inherited anchors being untouched.

**Verdict: PASS** — strict byte-prefix, append-only.

## 4. Informational (outside my three checks, recorded for the wave)

- `README.md` and `claim-excerpt-map.md` in r98 are S4-authored rewrites, **not**
  copies of r97 (r98 map 15028B vs r97 12117B; r98 README 5829B vs r97 5304B; neither
  is an r97 prefix). That is the declared ownership (S4 authors them new), and both
  landed after S3's placeholder copies.
- `corpus/fixtures/r97-crossing-acknowledgment/` is unchanged versus `9a3d648`
  (`git diff --stat 9a3d648 -- corpus/fixtures/r97-crossing-acknowledgment/` empty),
  so the copy source itself was not mutated during the round.
- Adjacent C3 repair corroboration (S3's other half, not my verdict): the r95 map diff
  versus `9a3d648` is exactly one changed line (line 49, the carried "new relation"
  sentence), and S3's receipts are byte-identical BEFORE/AFTER —
  `receipt-map-BEFORE.txt` = `receipt-map-AFTER.txt` (sha256 `4c645d63…`),
  `receipt-support-BEFORE.txt` = `receipt-support-AFTER.txt` (sha256 `efae7be2…`).

## 5. Non-findings / limitations

- Nothing contradicted the round's byte-level claims; no failures observed on my axis.
- I did not re-verify the map-obligation count (20), `check_bible`, the frozen chain,
  or the dependency-freeze hygiene — those are other seats' axes.
- Verification is on the working-tree revision at 20:31–20:34, uncommitted by design
  (rounds are committed at closure). If any producer rewrites a fixture file after
  that window, this verdict is superseded.

## 6. Frozen revision hashes (working tree, `sha256sum`)

```
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r98-clerk-filing/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r98-clerk-filing/inspiration-note.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r98-clerk-filing/source-excerpt.md
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
```

r97 source hashes (working tree = `9a3d648`, verified): entities `026af0bc…`, sources
`438fb513…`, timeline `73063a86…`, fictional-excerpts `8ba491cb…`, contradictions
`37517e5f…`, relations `c279254b…`, source-excerpt `b5edc2fd…`, inspiration-note
`58f5390e…`, README `d9387b7d…`, map `49d4834e…`.

## 7. Cross-lane hygiene observation: parent-tree stray write (r94-F01 class)

Not my write, but recorded as evidence for the wave — a file exists in the PARENT
tree, outside any lane:

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
?? baseline-analyze.txt
$ ls -la baseline-analyze.txt; stat -c '%y %n' baseline-analyze.txt
-rw-r--r-- 1 vgpnk vgpnk 105 Oct 17 20:30 baseline-analyze.txt
2026-10-17 20:30:10 -0300 baseline-analyze.txt
$ head -20 baseline-analyze.txt
python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory
```

Timing (20:30:10) is inside the round window; the content is a captured stderr from
a `python3 analyze.py` run executed from the parent cwd instead of the lane root —
the r94-F01 stray-write class recurring in the parent tree. I did not create it and
did not remove it (not my ownership, and deletion is out of scope for this seat).
All of my own writes resolved under
`/home/vgpnk/Projects/shokunin/lore-shokunin/` (report + `V45-scratch/` only).

**Bottom line: PASS — r98-clerk-filing reproduces r97 byte-for-byte for the four pure copies (also versus `9a3d648`), appends exactly one row per JSON table with all inherited rows an exact prefix (raw append junction `,\n  {…}\n`), and `fictional-excerpts.md` is a strict byte-prefix (3410B preserved + 777B appended), all on a hash-stable frozen revision.**

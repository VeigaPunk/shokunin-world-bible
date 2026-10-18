# V47 byte-prefix-2 — round 99

Seat: V47 (verifier, byte-prefix-2). Baseline: r98 closure `4265df5`
(`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at verification
was `337f0fa` (the blocked-dispatch log commit; `4265df5` is an ancestor). All
commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`
with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network.
Writes: this report (absolute path) and
`.ufo/waves/round-99/seats/V47-scratch/` (poll script/log, verify script,
hash snapshots, `git show` baseline copies, quoted-command transcript). No
producer-owned file was written by this seat.

Axes (this seat only): (1) `cmp` of the files that remain r98 copies,
(2) JSON-level diff of `sources.json` / `timeline.json` (appended rows only),
(3) `fictional-excerpts.md` strict byte-prefix. Everything below is on the
frozen delivered revision (hashes identical in `hashes-2.txt` and
`hashes-3.txt`, 22:06:46 and 22:07:06 -0300). S3-owned data files were already
that same sha256 in the earlier `hashes-1.txt` snapshot; only README moved
between hashes-1 and hashes-2, and it landed on the sha256 S4 declared.

## 0. Poll-wait record (not an all-reports poll; SELF not in the watch set)

Poll script `.ufo/waves/round-99/seats/V47-scratch/poll.sh` (20 s cadence, max
40). Content gate, not existence: nonempty `S3-fixture-author.md` and
`S4-fixture-docs.md`, plus `clerk-lapse-recorded` in `timeline.json`,
`clerk-lapse-note` in `sources.json`, and `fictional-excerpts.md` differing
from r98 (the r98 placeholder class). Log (`V47-scratch/poll.log`):

```
try=1 ts=2026-10-17 22:01:32 -0300 s3=no s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=2 ts=2026-10-17 22:01:52 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=3 ts=2026-10-17 22:02:12 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=4 ts=2026-10-17 22:02:32 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=5 ts=2026-10-17 22:02:52 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=6 ts=2026-10-17 22:03:12 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=7 ts=2026-10-17 22:03:32 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=8 ts=2026-10-17 22:03:52 -0300 s3=yes s4=no tl=yes ev=1 src=yes note=1 fic=differs
try=9 ts=2026-10-17 22:04:12 -0300 s3=yes s4=yes tl=yes ev=1 src=yes note=1 fic=differs
HIT try=9 ts=2026-10-17 22:04:12 -0300
```

No ABSENT, no stall-escape. Try 1 already had the lapse markers (S3 data
files mtime 22:01:13) while both producer reports were still absent. S3 report
landed by try 2 (mtime 22:01:40, 5069 bytes). S4 report landed by try 9
(mtime 22:03:54, 9303 bytes). README was still moving through try 5–8
(intermediate sha256 `1c95ca05aab6669f…` in `hashes-1.txt`; final
`b93209417a918a88…` at mtime 22:03:19, matching S4's receipt). Verdict below
is on that final README plus the unchanged S3 bytes, re-hashed stable at
22:06:46 and 22:07:06.

## 1. `cmp` — files that remain copies (r98 working tree and `4265df5`)

Declaration: S3 byte-copies r98, then edits only `sources.json`,
`timeline.json`, and `fictional-excerpts.md`. The other seven start as copies;
S4 then rewrites `README.md` and `claim-excerpt-map.md`. The copy-identity
check is the five files neither seat is supposed to change.

```
$ for f in contradictions.json entities.json inspiration-note.md relations.json source-excerpt.md; do
    cmp corpus/fixtures/r98-clerk-filing/$f corpus/fixtures/r99-window-lapse/$f; done
```

Observed: `cmp` rc=0 for all five (empty output; transcript
`V47-scratch/quoted-cmds.out` prints `cmp-rc0` for each). Same five extracted
with `git show 4265df5:corpus/fixtures/r98-clerk-filing/<f>` into
`V47-scratch/baseline/`:

```
r98-wt IDENTICAL-to-4265df5  contradictions.json
r99    IDENTICAL-to-4265df5  contradictions.json
r98-wt IDENTICAL-to-4265df5  entities.json
r99    IDENTICAL-to-4265df5  entities.json
r98-wt IDENTICAL-to-4265df5  inspiration-note.md
r99    IDENTICAL-to-4265df5  inspiration-note.md
r98-wt IDENTICAL-to-4265df5  relations.json
r99    IDENTICAL-to-4265df5  relations.json
r98-wt IDENTICAL-to-4265df5  source-excerpt.md
r99    IDENTICAL-to-4265df5  source-excerpt.md
```

`contradictions.json` is the 3-byte file `[]\n` (`od` `5b 5d 0a` on both the
working tree and `git show`). It has no `\n]` junction; identity is the `cmp`,
not an append-junction check. A later script line that prints
`shared-to-\n]=False` for that file is that accounting artifact, not a diff.

`git diff --stat 4265df5 -- corpus/fixtures/r98-clerk-filing/` was empty, and
`git diff --stat 4265df5 HEAD -- corpus/fixtures/r98-clerk-filing/` was empty.
The copy source was not mutated during the round. All ten r98 working-tree
files also matched `git show 4265df5:…` byte for byte.

**Verdict: PASS** — the five non-extended copies are byte-identical to both
the r98 working tree and `4265df5`.

## 2. JSON-level diff — `sources.json` / `timeline.json`, appended rows only

Parser check (`json.loads`) then row-wise prefix comparison
(`V47-scratch/verify.py`, `verify-final.out`):

```
sources.json:  r98=7 r99=8 prefix-exact=True appended=['clerk-lapse-note']
timeline.json: r98=7 r99=8 prefix-exact=True appended=['clerk-lapse-recorded']
```

- Every r98 row survives as an exact parsed prefix (deep equality on the first
  `len(r98)` rows); exactly one row appended per table; nothing removed or
  reordered.
- Appended rows (verbatim from the diff):
  - `sources.json` → `{"id": "clerk-lapse-note", "title": "Maren's Chalk Stair Lapse Note", "kind": "fictional first-person note", "reliability_note": "Newly authored fictional note; the clerk reports that the crossing-window named in the original minute has closed, that the agreement was unfulfilled, that no claim was lodged, and that the matter stands as a historical open entry. It asserts no resolution, no blame, and no reconciliation; it is not evidence of a breach finding, a continuing duty, a winner between the accounts, or an external historical fact."}`
  - `timeline.json` → `{"id": "clerk-lapse-recorded", "tick": 15, "entity_id": "clerk-maren", "place_id": "chalk-stair", "depends_on": ["clerk-filing-open"], "description": "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.", "source_id": "clerk-lapse-note"}`
- Stronger raw-byte check at the append junction: r99 shares r98's bytes up to
  the final newline before r98's closing `]`, which became `,`:

```
sources.json:  r98=2725B r99=3293B raw-shared-prefix=2722B of r98-pre-bracket=2723B  next-r99-bytes=b',\n  {\n    "id": "clerk-lapse-note",\n    '
timeline.json: r98=2552B r99=2998B raw-shared-prefix=2549B of r98-pre-bracket=2550B  next-r99-bytes=b',\n  {\n    "id": "clerk-lapse-recorded",\n'
```

  (`startswith` of r98's bytes through the newline-before-`]` is True for both.
  The one unshared byte of the pre-bracket region is r98's newline before `]`;
  r99 inserts `,\n  {new row}\n` there — a pure append, no inherited byte
  touched. Neither file is a whole-file prefix of the other, which is expected:
  the closing `]\n` moves.)
- Same parser on the other three JSON tables, which the declaration does not
  extend: `entities.json` 6=6 appended=[], `relations.json` 1=1 appended=[],
  `contradictions.json` 0=0 appended=[]. Those three are also the `cmp`
  identities in §1 (entities included here because it is a JSON table that
  must not grow).
- Referential integrity of the two new rows (strict `json.loads` on all five
  JSON files): entities 6, relations 1, events 8, sources 8, contradictions 0;
  ticks `[9, 9, 10, 11, 12, 13, 14, 15]`; new event `source_id`
  `clerk-lapse-note` resolves, `entity_id` `clerk-maren` resolves, `place_id`
  `chalk-stair` resolves, `depends_on ["clerk-filing-open"]` resolves to an
  existing timeline event (all True).

**Verdict: PASS** — appended rows only, in both tables the seat was asked to
diff. No inherited row edited, removed, or reordered.

## 3. `fictional-excerpts.md` strict byte-prefix

```
$ python3 -c "b98=open('corpus/fixtures/r98-clerk-filing/fictional-excerpts.md','rb').read();
              b99=open('corpus/fixtures/r99-window-lapse/fictional-excerpts.md','rb').read();
              print(len(b98), len(b99), b99.startswith(b98))"
4187 5114 True
```

r98's exact 4187 bytes are preserved (and those 4187 bytes match
`git show 4265df5:corpus/fixtures/r98-clerk-filing/fictional-excerpts.md`).
927 bytes appended, beginning:

```
b'\n## Round 99 lapse note (2026-10-17)\n\nNewly authored fictional first-person note,
attributed to in-world source ID `clerk-lapse-note`, folio 9, lines 1\xe2\x80\x935. This
section is appended after the preserved r98 text above; the inherited wording is unchanged.
\n\n> Tick 15: The crossing-window named in the original minute has closed.\n> The agreement
was unfulfilled.\n> No claim was lodged.\n> The matter stands as a historical open entry.\n>
I record no resolution, assign no blame, and reconcile nothing.\n\nSc'
```

Line accounting (`wc -l`, both files end with a newline): r98 = 64 lines;
r99 = 76 lines; appended region = lines 65–76 (blank separator line 65 from
the leading `\n` of the append, `## Round 99 lapse note` heading line 66,
quoted note lines 70–74, scope paragraph line 76). S4's map anchors the new
row inside lines 66–76 (hit at line 70). That is consistent with the inherited
64 lines being untouched; this seat did not re-run `map_obligations`.

S3's report line "excerpt starts with base then newline" matches this
measurement: `startswith(r98)` is True, and the first appended byte is `\n`.

**Verdict: PASS** — strict byte-prefix, append-only.

## 4. Informational (outside the three checks, recorded for the wave)

- `README.md` and `claim-excerpt-map.md` in the delivered r99 tree are
  S4-authored rewrites, **not** copies of r98 (r99 map 17119B vs r98 15028B;
  r99 README 6176B vs r98 5829B; neither is an r98 prefix). That is the
  declared ownership. Both were r98-sized placeholders at 21:36:10 (S3's
  report and the early directory listing); map landed 22:02:39, README final
  22:03:19. Delivered shas match S4's report exactly:
  map `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`,
  README `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`.
- `hashes-1.txt` captured an intermediate README sha256
  `1c95ca05aab6669fc9bff7b2e8be86daf7112ed51c24f847d13084cfd8a104b4` while S4
  was still editing phrases. That hash is not the delivered revision. Every
  other r99 file was unchanged from hashes-1 through hashes-3.
- S3's "Not done" note that README and the map still say r98 was true at
  S3's report time and is stale on the frozen tree. No contradiction with
  the byte checks in §1–§3.
- Lane porcelain at freeze (not a verdict): `M corpus/tools/dependency_freeze.py`,
  `M corpus/tools/dependency-freeze-contract.json`,
  `?? corpus/fixtures/r99-window-lapse/`. Those tool edits are S1's ownership.
- Parent-tree porcelain at 22:07:06 was empty (`git -C /home/vgpnk/Projects/shokunin status --porcelain`
  produced no lines). No r94-F01 stray observed in this window. This seat did
  not create or delete anything outside
  `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/`.

## 5. Non-findings / limitations

- Nothing contradicted the round's byte-level claims on this axis; no failures
  observed.
- I did not re-verify map-obligation count (21), `check_bible`,
  `support_check`, the frozen chain, census 172→173, or the absence of
  resolution/blame wording outside the appended JSON objects and the appended
  excerpt region. Those are other seats' axes. The appended objects and the
  appended excerpt do contain the declared lapse sentences; that is a quote,
  not a whole-fixture semantic proof.
- Verification is on the working-tree revision at 22:06:46–22:07:06,
  uncommitted by design. If any producer rewrites a fixture file after that
  window, this verdict is superseded. S3 data-file mtimes were still 22:01:13
  and the five pure-copy mtimes still 21:36:10 at the second hash.

## 6. Frozen revision hashes (working tree, `sha256sum`, hashes-3)

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r99-window-lapse/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r99-window-lapse/entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r99-window-lapse/inspiration-note.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r99-window-lapse/source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  corpus/fixtures/r99-window-lapse/sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
```

r98 source hashes (working tree = `4265df5`, verified): entities `db2d8e5d…`,
sources `32ee15b1…`, timeline `eb24e084…`, fictional-excerpts `29e384bf…`,
contradictions `37517e5f…`, relations `c279254b…`, source-excerpt `b5edc2fd…`,
inspiration-note `58f5390e…`, README `32efc78f…`, map `c1099d0e…`.

**Bottom line: PASS — r99-window-lapse is byte-identical to r98 and to `4265df5` for the five unextended copies; `sources.json` and `timeline.json` each append exactly one row with every inherited row an exact parsed prefix and a raw append junction `,\n  {…}`; `fictional-excerpts.md` is a strict byte-prefix (4187B preserved + 927B appended), all on a hash-stable delivered revision.**

# V05 c2-chain-six — round 98

- Seat: V05 c2-chain-six (verifier). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`;
  wave tree uncommitted; HEAD during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`.
- Verified revision (frozen for this verdict; stable over 6 checks / 90 s):
  `corpus/tools/dependency_freeze.py` sha256
  `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`,
  `corpus/tools/dependency-freeze-contract.json` sha256
  `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`
  (both match S1's report hashes).
- Writes: this report (absolute path) and my scratch
  `v05-self-test-scratch/` (gitignored by `.gitignore:4: *-self-test-*/`).
  Leaf seat: no nested agents, no commits, no pushes, no network, no other lane
  file written. All commands run from the lane root with `python3`.

## 0. Poll-wait record (S1 + S3; 20 s cadence, 40 tries max)

Poller `v05-self-test-scratch/poll.sh` (log `v05-self-test-scratch/poll.log`),
checking S1's contract pins, S3/S4's r98 files, the r95 map repair, and producer
reports. Key lines:

```
CHECK n=1  t=20:27:53 S1contract_pins_r98=0 pins_r97=0 stmismatch=0 S3_timeline=0 ... r95map=same
CHECK n=3  t=20:28:33 S1contract_pins_r98=0 pins_r97=0 ... S3_timeline=1 sources=1 entities=1 S4_readme=1 map=1
CHECK n=4  t=20:28:53 ... r95map=diff
CHECK n=12 t=20:31:33 S1contract_pins_r98=0 pins_r97=0 stmismatch=1 ...
CHECK n=16 t=20:32:53 S1contract_pins_r98=1 pins_r97=1 stmismatch=1 ... S5_note=1 r95map=diff
POLL_HIT_ALL n=16 t=20:32:53
```

S3/S4's fixture copy landed 20:28:24, S3's authored additions 20:28:55, the r95
map repair by 20:28:53, S1's C1 half 20:31:20 (contract) / 20:31:49 (tool), the
two `--freeze` pins by 20:32:53. The poll exited on the hit at n=16, not on the
deadline; no stall escape was needed (the r96/r97 mutual-wait class did not
recur for this seat). `S1-freeze-hygiene.md` landed 20:35:33 and
`S3-fixture-author.md` 20:31; both read. No plan was verified: every check below
ran against delivered bytes.

## 1. Chain verify 6/6 clean at delivered paths

Command: `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` for
each of the six, delivered tool and contract:

```
### corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS        exit=0
### corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS        exit=0
### corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS        exit=0
### corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS        exit=0
### corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS        exit=0
### corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS        exit=0
```

Pre-state (before S1's freezes, same tool path, baseline contract):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' ... (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR  exit=2
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FINDING UNPINNED-FIXTURE: no pin for 'r98-clerk-filing' ... RESULT ERROR  exit=2
```

## 2. Contract pins exactly six fixtures, each with a repo-relative path

```
pin keys: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
r88-m3-maya-cluster:      fixture='corpus/fixtures/r88-m3-maya-cluster'      is_absolute=False resolves_exists=True
r94-paired-crossing:      fixture='corpus/fixtures/r94-paired-crossing'      is_absolute=False resolves_exists=True
r95-crossing-aftermath:   fixture='corpus/fixtures/r95-crossing-aftermath'   is_absolute=False resolves_exists=True
r96-crossing-response:    fixture='corpus/fixtures/r96-crossing-response'    is_absolute=False resolves_exists=True
r97-crossing-acknowledgment: fixture='corpus/fixtures/r97-crossing-acknowledgment' is_absolute=False resolves_exists=True
r98-clerk-filing:         fixture='corpus/fixtures/r98-clerk-filing'         is_absolute=False resolves_exists=True
top-level keys: ['data_files', 'exit_codes', 'pins', 'precedence', 'provenance_note', 'required_files', 'revision', 'schema_version', 'scope', 'self_test', 'tool']; contract revision=dd4df1b3...
```

The four inherited pins are byte-identical to the baseline contract
(`base[k] == now[k]` for r88/r94/r95/r96; only r97/r98 were added), so the chain
extension rewrote no earlier pin — including r95, whose Markdown map S3 repaired
(the pin payload covers the five JSON tables only, so d541ae64… is unchanged).
r98's frozen sixth link: `clerk-filing-open` `depends_on
['acknowledgment-aru-records']`, endpoint tick 14 / `clerk-maren` / `chalk-stair`.

## 3. r97 and r98 pin digests match delivered bytes (independent recompute)

`python3 v05-self-test-scratch/recompute.py .` — recomputes, without importing
the tool, per-file sha256 over the five data files present and
`content_sha256 = sha256(json.dumps({name: sha256(raw)}, sort_keys=True,
separators=(",",":")))`:

```
r97-crossing-acknowledgment
   contradictions.json pin=37517e5f...b570 delivered=37517e5f...b570 MATCH
   entities.json       pin=026af0bc...e03b delivered=026af0bc...e03b MATCH
   relations.json      pin=c279254b...6ff9 delivered=c279254b...6ff9 MATCH
   sources.json        pin=438fb513...dc73 delivered=438fb513...dc73 MATCH
   timeline.json       pin=73063a86...895b delivered=73063a86...895b MATCH
   content pin=3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6 delivered=3c922d20... MATCH
r98-clerk-filing
   contradictions.json pin=37517e5f...b570 delivered=37517e5f...b570 MATCH
   entities.json       pin=db2d8e5d...2984 delivered=db2d8e5d...2984 MATCH
   relations.json      pin=c279254b...6ff9 delivered=c279254b...6ff9 MATCH
   sources.json        pin=32ee15b1...d0f3 delivered=32ee15b1...d0f3 MATCH
   timeline.json       pin=eb24e084...e7af delivered=eb24e084...e7af MATCH
   content pin=59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133 delivered=59a0f4fa... MATCH
```

(full 64-hex values were printed by the harness; ellipses here only for width).
The same run re-derived the inventories independently: for all six pins
`events`/`depends_on`/endpoints and relation triples are identical to the pin
(`inventory_identical=True`, `identical=True`), and counts match
(r98: `{'events': 7, 'dependency_edges': 6, 'relations': 1, 'entities': 6, 'sources': 7}`).
The r97/r98 content digests also equal the values I precomputed from the
delivered bytes before S1's freezes ran, so the pins recorded the delivered
bytes, not a private copy.

## 4. V46's recorded FAIL discharged — r97 tick-13 edge

Mirrored root (`v05-self-test-scratch/redemo.sh`: delivered tool + contract at
the mirror's own `corpus/tools/`, r97 fixture copied to the mirror's
`corpus/fixtures/`, then `acknowledgment-aru-records.depends_on` emptied):

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL  exit=1
```

The r97 edge is now frozen and load-bearing (the unmutated mirror verifies
clean). Path binding was not weakened by the new pins: byte-identical
same-named copies of r97 and r98 at foreign paths exit 2
`PATH-MISMATCH: pin r97-… names corpus/fixtures/r97-crossing-acknowledgment …
invoked fixture resolves to …/v05-self-test-scratch/foreign98/r97-crossing-acknowledgment`.

## 5. Supporting checks (C1 load-bearing, self-test integrity)

- `python3 corpus/tools/dependency_freeze.py --self-test` → `CASE
  self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok`,
  `SELF-TEST 17/17`, `RESULT PASS`, exit 0.
- Expectations diff vs baseline: `added: ['self_test_mismatch'] removed: []
  changed expectations among shared cases: []` — the 16 inherited cases are
  unchanged.
- C1(a) neutrality (corrupt the persisted `clean` expectation in a mirror
  contract, run `--self-test`): delivered `SELF-TEST 16/17` + `FINDING
  SELF-TEST-MISMATCH` + `RESULT ERROR exit=2`; baseline `SELF-TEST 15/16` +
  `RESULT FAIL exit=1`.
- C1(b) path-less legacy pin (r95 pin's `fixture` set to `null`, then
  `--freeze` on the in-scope r95 fixture): delivered prints `MIGRATED
  r95-crossing-aftermath: path-less legacy pin now names
  corpus/fixtures/r95-crossing-aftermath`, exit 0, pin now carries the path;
  baseline exits 2 `FINDING SCOPE-REFUSED: --freeze refuses
  corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already
  names None …`, pin stays `None`. (First probe attempt was invalid — it used
  r97, which is not pinned in the baseline contract, so the baseline leg could
  not exercise the refusal; the corrected probe above uses r95, pinned in both.)
- Contract `precedence` names the full exit-2 order and FINDING IDs including
  `SELF-TEST-MISMATCH`, and states "A path-less legacy pin is migrated in place
  by --freeze instead of refused."

## 6. Hygiene

- Lane `git status --porcelain` shows exactly the declared set: `M LOG.md`
  (round declaration), `M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`,
  `M corpus/knowledge/r95-aftermath-scope-note.md`,
  `M corpus/knowledge/r96-response-scope-note.md`, `M corpus/tools/README.md`,
  `M corpus/tools/dependency-freeze-contract.json`,
  `M corpus/tools/dependency_freeze.py`, `?? corpus/fixtures/r98-clerk-filing/`,
  `?? corpus/knowledge/r98-clerk-scope-note.md`,
  `?? .ufo/waves/round-98/`. No seat-made strays in the lane tree.
- Parent-tree hygiene note (not this lane, not mine): an untracked
  `baseline-analyze.txt` (105 bytes, mtime 20:30:10) appeared at
  `/home/vgpnk/Projects/shokunin/`; its content is a stderr capture of a failed
  `python3 analyze.py` run ("can't open file
  '/home/vgpnk/Projects/shokunin/analyze.py'"). It is the r94-F01 stray-write
  class recurring at the parent root by an unidentified seat; recorded as
  evidence, not fatal for this seat.

## 7. Verdict — C2 (coverage): improved (bounded)

Chain extended 4/4 → 6/6 with both new links frozen and independently
recomputed; V46's r97 FAIL discharged by a reproduced REDUCTION-DETECTED on the
frozen edge; no earlier pin moved. Bounds (carried, unchanged): (i) the pin
payload covers the five JSON tables only — fixture Markdown (maps, READMEs) is
not pinned; (ii) chain completeness is by declaration: a newly authored fixture
is not discovered, only a named invocation of an unpinned fixture exits 2
`UNPINNED-FIXTURE`; (iii) the pin `revision` field is HEAD at freeze time
(`dd4df1b3…`) and is informational — later commits do not invalidate pins;
(iv) the 17th case's recursion bound is the `DEPENDENCY_FREEZE_SELF_TEST_CHILD`
marker plus a fail-closed `FIXTURE-MISSING` in the nested replay (observed
passing; neutralization demonstrated above). No axis harmed by this seat's
observations.

Bottom line: PASS — chain verifies 6/6 clean at delivered paths, the contract
pins exactly six fixtures each by repo-relative path, and the r97/r98 pins'
per-file and content digests recompute to the delivered bytes (V46's FAIL
discharged by the r97 tick-13 edge).

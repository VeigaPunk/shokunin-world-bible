# V08 — c2-checker (round 96)

Seat: V08, verifier for C2 (depth). Report path exclusive.
Repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`, HEAD `60dba0c` ("lore r95: close round —
SCORECARD admitted section"); the declared baseline `dcb2d92` differs from HEAD only in
`SCORECARD.md` (`git diff --stat dcb2d92 HEAD` → `SCORECARD.md | 32 +++`, 1 file changed).
r96 producer output present as an **uncommitted working tree** (`git status --porcelain` →
` M LOG.md`, `?? .ufo/waves/round-96/`, `?? corpus/fixtures/r96-crossing-response/`).
No commits, no pushes, no nested agents, no network. All commands run from repo root with `python3`.

## Poll result

Poll target Q4 (`corpus/fixtures/r96-crossing-response/` tables + `fictional-excerpts.md`) and Q4's
report `.ufo/waves/round-96/seats/Q4-fixture-json.md`:

- 17:38 — fixture dir present with 7/8 files, `timeline.json` absent (mid-write); Q4 report absent.
- 17:40 — all 8 files present; `sources.json` and `timeline.json` rewritten (byte sizes 1742→1741,
  1678→1677).
- 17:42 — Q4 report `Q4-fixture-json.md` (9586 B) landed. **PRESENT**; poll ended, no ABSENT cutoff reached.

**Mid-seat revision change (material to method):** my first pass ran against the 17:38 revision of
`sources.json`/`timeline.json`. Q4's report explains the rewrite as a comma-placement correction
(`  }\n,\n  {` → `  },\n  {`, valid JSON but off-convention) applied at 17:39–17:40, i.e. **before**
Q4's own receipts. My pass-1 hashes differ from the delivered hashes on exactly those two files:

```
pass1: 10da97ee… sources.json   50e3d2b6… timeline.json
final: 9f973f63… sources.json   ea0225f9… timeline.json
```

All results below are from a **full re-run on the delivered revision**; nothing is reported from the
superseded intermediate. No artifact was verified from a plan.

## Check 1 — check_bible on r96-crossing-response (expected CLEAN exit 0)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

Run three times total (dry pass, delivered-revision pass, stability re-check 20 s later) — identical
output, exit 0 every time. `check_bible.py` at tool revision
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (unchanged during the round; no
producer owns it in r96).

## Check 2 — table counts (expected 5 entities / 1 relation / 5 events / 5 sources)

`check_bible.py` has no JSON output mode, so counts were parsed directly from the delivered tables
with `json.loads`:

```
$ python3 .ufo/waves/round-96/seats/V08-c2-checker.scratch/v08_verify.py
[entities] 5   [relations] 1   [events] 5   [sources] 5   [contradictions] 0
entity ids: ['aru', 'evin', 'quiet-rise', 'salt-court', 'chalk-stair']
source ids: ['veil-verse', 'paired-clock', 'crossing-minute', 'aru-aftermath-note', 'evin-response-note']
event ids: ['aru-ninth-bell', 'evin-ninth-bell', 'paired-crossing-decision', 'aftermath-missing-evin', 'response-evin-salt-court']
```

Exactly as declared (5/1/5/5; r95 was 5/1/4/4 — one source and one event added, no new
claims/entities/relations).

## Check 3 — response-evin-salt-court tick 12

```
{
  "id": "response-evin-salt-court",
  "tick": 12,
  "entity_id": "evin",
  "place_id": "salt-court",
  "depends_on": ["aftermath-missing-evin"],
  "description": "Evin reports being at Salt Court through the same agreed bell; the note asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved.",
  "source_id": "evin-response-note"
}
```

All four declared attributes hold (tick 12; actor `evin`; place `salt-court`;
`depends_on == ["aftermath-missing-evin"]` exactly). Full delivered chain:

```
aru-ninth-bell           tick= 9 actor=aru  place=quiet-rise  dep=[]                                   src=paired-clock
evin-ninth-bell          tick= 9 actor=evin place=salt-court  dep=[]                                   src=paired-clock
paired-crossing-decision tick=10 actor=aru  place=chalk-stair dep=['aru-ninth-bell','evin-ninth-bell'] src=crossing-minute
aftermath-missing-evin   tick=11 actor=aru  place=chalk-stair dep=['paired-crossing-decision']          src=aru-aftermath-note
response-evin-salt-court tick=12 actor=evin place=salt-court  dep=['aftermath-missing-evin']            src=evin-response-note
```

Tick order 11 < 12 satisfied, so `check_bible`'s timeline-inversion rule holds independently of the
gate's own exit 0.

## Check 4 — dangling / duplicate id sweep (independent of check_bible)

Independent sweep (duplicate detection by `collections.Counter`, dangling by set membership over
entity/source/event id universes):

```
entity ids: 5 total, duplicates=[]    source ids: 5 total, duplicates=[]    event ids: 5 total, duplicates=[]
relation endpoints: ['aru->evin']
dangling sweep complete
```

- relations `from`/`to` → entities: resolved; relation `source_id` → sources: resolved.
- every entity `first_appearance` and every claim `source_id` → sources: resolved.
- every event `entity_id`/`place_id` → entities and `source_id` → sources: resolved.
- every `depends_on` entry → existing event: resolved.
- no duplicate id in any of the three id universes; no self-dependency; no repeated dependency.

Zero dangling and zero duplicate findings. (This is a stricter, independent re-derivation, not a
re-reading of `check_bible`'s output.)

## Check 5 — r95 fixture still CLEAN

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

And r95 was **not mutated in place**: all 10 r95 file hashes equal the hashes recorded in the r95
V08 report (`30281ff1…`, `37517e5f…`, `026af0bc…`, `0ef6734a…`, `58f5390e…`, `9d27af4a…`,
`c279254b…`, `b5edc2fd…`, `fd9e30e8…`, `3c0faad6…`), and the 7 files that also exist in `dcb2d92`
match their git blobs byte-for-byte (`git show dcb2d92:… | sha256sum` == on-disk `sha256sum`, all
`match=YES`). r95 is untouched; r96 is a preserving copy.

## Check 6 — preservation of the copy (beyond seat scope, cheap)

- Declared byte copies — `entities.json`, `relations.json`, `contradictions.json`,
  `inspiration-note.md`, `source-excerpt.md` — are byte-identical to their r95 counterparts
  (`identical=True`, sizes 1449/139/3/1956/640 both sides).
- `fictional-excerpts.md` is a **pure append**: `diff r95 r96` output is exactly `31a32,42` (adds
  lines 32–42, changes nothing inherited); r95 wording keeps its original line numbers.
- Inherited rows: all 4 r95 sources and all 4 r95 events are present in r96 with **parsed value
  unchanged** (dict equality per row); added = `evin-response-note` and `response-evin-salt-court`
  only.
- Unresolved framing: `contradictions.json` is `[]` (0 rows, byte-identical to r95); the two
  first-person accounts differ in tick (11 vs 12), actor (aru vs evin) and place (chalk-stair vs
  salt-court), so no same-slot double-booking conflict exists and no contradiction is asserted. The
  new note's text negates accusation/winner explicitly ("no accusation", "selects no winner",
  "both first-person accounts stand unresolved").

## Delivered-revision hashes (stable across a 20 s re-check; `diff` of the two captures empty)

```
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  timeline.json
```

These match Q4's declared delivered hashes field-for-field (Q4 report "Facts for verifiers"),
including `sources.json` `9f973f63…` and `timeline.json` `ea0225f9…` — i.e. the verified revision is
the one Q4 receipted, not the discarded 17:38 intermediate.

## Notes for the parent (not my seat's claim to adjudicate)

- Q4's `map_obligations` receipt on the r96 fixture exits 2 `map_missing` because Q5's
  `claim-excerpt-map.md` had not landed at Q4's receipt time. That end-to-end map receipt is
  therefore **pending Q5** and is outside my scope (V08 verifies the C2 fixture's structure and
  gates, not the obligation count). Q4's "16 obligations" figure is also outside my seat and was
  not independently re-derived here.
- `README.md` and `claim-excerpt-map.md` (Q5) were not present at my verification time; my checks
  do not depend on them.

## Addendum — post-report arrival of Q5's files (17:43)

While this report was being written, Q5's `README.md` and `claim-excerpt-map.md` landed in the
fixture directory. Re-hashed after the write: the **eight files I verified are byte-unchanged**
(`diff` of the two hash captures filtered to those eight is empty — `VERIFIED-8 UNCHANGED`), and
`check_bible` on the fixture still prints CLEAN with `EXIT=0`. My verdict therefore still attests the
same eight-file revision recorded above; the two Q5 files are additions I did not verify (Q5's scope).
Scope audit at that moment: `git status --porcelain` in the lane repo shows only ` M LOG.md`,
`?? .ufo/waves/round-96/`, `?? corpus/fixtures/r96-crossing-response/`, and Q3's two new tool files —
no stray writes in the parent `/home/vgpnk/Projects/shokunin` tree (grep for r96/round-96/V08 names
there returns no match).

## Bottom line

PASS — on the delivered revision (`sources.json` `9f973f63…`, `timeline.json` `ea0225f9…`):
`check_bible` CLEAN exit 0 on r96-crossing-response and r95-crossing-aftermath; counts 5 entities /
1 relation / 5 events / 5 sources / 0 contradictions; `response-evin-salt-court` at tick 12 (evin,
salt-court) with `depends_on ["aftermath-missing-evin"]`; zero dangling and zero duplicate ids;
r95 byte-identical to baseline and its gate still CLEAN.

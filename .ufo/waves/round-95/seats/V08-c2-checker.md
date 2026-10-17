# V08 — c2-checker (round 95)

Seat: V08, verifier for C2 (depth). Report path exclusive.
Repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`, revision `fb118c42038ed27a747eec704b9aab41bb4b2ebe`
(r94 closure `fb118c4`) with r95 producer output present as an **uncommitted working tree**
(`git status --porcelain` → `M LOG.md`, `?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`).
No commits, no pushes, no nested agents, no network. All commands run from repo root with `python3`.

## Poll result

Poll target P3 (`corpus/fixtures/r95-crossing-aftermath/` tables + `fictional-excerpts.md`) and P3's
report `.ufo/waves/round-95/seats/P3-fixture-json.md` were **PRESENT** on first inspection (fixture dir
16:18, P3 report 16:20); no ABSENT cutoff was reached. A background 20 s-cadence poll was started and
then killed once presence was confirmed; no artifact was verified from a plan. P4's `README.md` landed
at 16:21 mid-verification and is included in the hash-stability re-check below.

## Check 1 — check_bible on r95 (expected CLEAN exit 0)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

Run twice (before and after P4's README landed); identical output and exit 0 both times.
sha256 of all 10 files in the fixture dir identical across the two runs (`diff` of the two
`sha256sum` captures empty) — the verified revision is the one on disk:

```
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  timeline.json
```

**Note on method:** `check_bible.py` has **no JSON output mode** (`--help` shows only the positional
`bible` argument; no `--json`/`-o` flags). The counts below were therefore parsed directly from the
fixture's own JSON tables, which is the only available source for them.

## Check 2 — table counts (expected 5 entities / 1 relation / 4 events / 4 sources)

Parsed with `json.loads` per table:

```
entities: 5
relations: 1
timeline: 4
sources: 4
contradictions: 0
--- sources ids: ['veil-verse', 'paired-clock', 'crossing-minute', 'aru-aftermath-note']
```

Exactly as declared. 3→4 sources and 3→4 events versus r94 (see Check 6 diffs); entities/relations
unchanged.

## Check 3 — aftermath-missing-evin

```
event aru-ninth-bell tick 9 actor aru place quiet-rise depends_on [] src paired-clock
event evin-ninth-bell tick 9 actor evin place salt-court depends_on [] src paired-clock
event paired-crossing-decision tick 10 actor aru place chalk-stair depends_on ['aru-ninth-bell', 'evin-ninth-bell'] src crossing-minute
event aftermath-missing-evin tick 11 actor aru place chalk-stair depends_on ['paired-crossing-decision'] src aru-aftermath-note
```

`aftermath-missing-evin`: tick **11**, actor `aru`, place `chalk-stair`,
`depends_on == ["paired-crossing-decision"]` — **confirmed exactly** (single-element list, no extra
dependency).

## Check 4 — dangling / duplicate ids across all tables

Independent scan (not a re-run of check_bible): duplicate ids per section; relation `from`/`to`
endpoints; event `entity_id`/`place_id`/`source_id`; `depends_on` resolvability **and** tick ordering;
entity `first_appearance`; every claim `source_id`.

```
ID-INTEGRITY: CLEAN
claim source refs: ['crossing-minute', 'paired-clock']
entity ids: ['aru', 'evin', 'quiet-rise', 'salt-court', 'chalk-stair']
```

Zero dangling references, zero duplicate ids, zero timeline inversions. All 5 entity claim refs
resolve to `paired-clock`/`crossing-minute`; the new source `aru-aftermath-note` is cited by the new
event row only.

## Check 5 — r94-paired-crossing still CLEAN

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
$ git status --porcelain corpus/fixtures/r94-paired-crossing/
(empty)
```

r94 is unchanged in the working tree and still CLEAN — the r95 fixture did not mutate its source.

## Check 6 — preservation of the inherited r94 material (extra, within C2's "preserving copy")

- `diff` rc=0 (byte-identical) for the five declared byte-copies: `entities.json`, `relations.json`,
  `contradictions.json`, `inspiration-note.md`, `source-excerpt.md`.
- `timeline.json` and `sources.json` diffs are **pure appends** (`30a31,41` and `18a19,24`) — no
  inherited line changed or removed; inherited rows `#/0…#/2` are value-identical.
- `fictional-excerpts.md` diff is a **pure append** (`20a21,31`): the r94 verse/register/minute text
  and its line numbers 12–20 are untouched; the new "Round 95 aftermath note" section follows.

## Check 7 — scope language (crossing-only; no breach/other-duty assertion)

The only occurrences of `breach`/`duty`/`obligation`/`perpetual` in the JSON tables are explicit
**disclaimers**, not assertions:

- `sources.json:24` (`aru-aftermath-note.reliability_note`): "…is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact."
- `timeline.json:40` (event description): "…the note scopes the agreement to this crossing only and asserts no other duty or breach."

The authored note itself (`fictional-excerpts.md:26–29,31`) states the agreement "covered this crossing
only" and "I assert no other duty, no breach, and no obligation beyond this crossing." No breach,
perpetual-duty, canon-truth, or identity inference is asserted anywhere I can see.

## Secondary corroboration (not this seat's axis)

`python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath` →
`OBLIGATIONS raw=15 mapped=15` / `RESULT PASS` / exit 0, matching the C2 "15 map obligations" figure.
This is P1/P4 territory and was run read-only, once, as a cross-check only — V08 does not certify the
tool or the map here.

## Process note (tooling, for the integrator)

This seat's report was first written by relative path and landed in the **parent** repo
(`/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/V08-c2-checker.md`) because the Write tool
resolves relative paths against the session cwd, not the lane root. The stray copy was deleted and the
report re-written to the lane-absolute path. Two other seats' reports are stranded in the parent's
`round-95/seats/` and are **not** present in the lane's seats dir: `V30-shonen-format.md` (16:19) and
`V14-c2-dependency-probe.md` (16:23) — those seats likely hit the same cwd resolution
(observation only; not this seat's artifacts, left in place untouched for the integrator to collect).

## Bottom line

PASS — r95-crossing-aftermath `check_bible` CLEAN exit 0 (hashes stable across the verify window),
counts exactly 5 entities / 1 relation / 4 events / 4 sources, `aftermath-missing-evin` tick 11 with
`depends_on == ["paired-crossing-decision"]`, zero dangling/duplicate ids in an independent scan, and
r94-paired-crossing still CLEAN with a byte-preserved inherited copy.

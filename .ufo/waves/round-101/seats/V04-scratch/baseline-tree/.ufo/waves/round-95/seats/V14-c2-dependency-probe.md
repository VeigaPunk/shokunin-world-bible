# V14 — c2-dependency-probe (round 95)

Seat: V14 `c2-dependency-probe`. Exclusive report path: this file. Scratch:
`.ufo/waves/round-95/seats/scratch/V14/` (`dry-a..c` from r94 pre-study, `probe-a..f`
from this fixture). Baseline HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe`
(r94 closure `fb118c4`). No commits, no nested agents, no network. Live tree
untouched (evidence in §6).

Task: on scratch copies of `corpus/fixtures/r95-crossing-aftermath/`, probe four
dependency mutations with `check_bible`: (a) drop `paired-crossing-decision` from the
tick-11 `depends_on`, (b) point `depends_on` at an unknown id, (c) set tick 9 on the
aftermath event, (d) remove the tick-10 row.

## 1. Artifact status (poll-wait)

`corpus/fixtures/r95-crossing-aftermath/` was absent at seat start. Poll loop
(20 s cadence): JSON tables landed at 16:19:02; P4's `README.md` +
`claim-excerpt-map.md` landed later (poll task `READY` at ~300 s wall). Probes were
run only after all five JSON tables existed and again against the final bytes after
P4's docs landed. P3's seat report `.ufo/waves/round-95/seats/P3-fixture-json.md`
and P4's `.ufo/waves/round-95/seats/P4-fixture-docs.md` are present.

Final fixture (10 files) counts and hashes (stable across every run below):

```
$ python3 -c "... len(json.load(...))"   # entities/relations/timeline/sources/contradictions
entities 5
relations 1
timeline 4
sources 4
contradictions 0

$ sha256sum *.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  timeline.json
```

Tool revisions used (sha256): `check_bible.py` =
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
(matches P3's receipt); `map_obligations.py` =
`cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790` — the **r94
revision** at report time (P1's C1 tool had not landed; every map observation below
is therefore on the r94 tool and is flagged as such).

Baseline on the live fixture:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

The tick-11 event as delivered: `id aftermath-missing-evin`, `tick 11`, `entity_id
aru`, `place_id chalk-stair`, `depends_on ["paired-crossing-decision"]`, `source_id
aru-aftermath-note`.

## 2. Probes (a)–(d) — scratch copies, final bytes

Copy fidelity was verified before probing (source vs `probe-a`: all five JSON tables
`SAME`). Mutations applied by event-id lookup, never by row index except where the
row is deleted.

### (a) drop `paired-crossing-decision` from the tick-11 `depends_on`

```
(a) aftermath depends_on -> []
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-95/seats/scratch/V14/probe-a
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

**check_bible does not report — exit 0, no FINDING/VIOLATION line.** This
contradicts the seat prompt's expectation ("check_bible must report"). The checker
only validates the *listed* dependencies (self / repeated / unknown / ambiguous /
inversion, `check_bible.py:393-414`); nothing asserts that an event carries any
dependency at all, so a removed dependency is invisible. The fixture's own docs do
assert the linkage in prose (`README.md:9`: "The new tick-11 event is ordered after
and depends on the tick-10 decision (`paired-crossing-decision`)";
`claim-excerpt-map.md:49`: "the new tick-11 aftermath event is ordered after and
depends on the tick-10 decision (`paired-crossing-decision`)"). After mutation (a)
the docs and the table disagree and `check_bible` still prints CLEAN. Same for the
r94 `map_obligations` revision: `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`
exit=0 on `probe-a`. This is a checker blind spot, reported as evidence, not as a
fixture defect.

### (b) unknown dependency id

```
(b) aftermath depends_on -> ['ghost-event-r95']
$ python3 corpus/fixtures/check_bible.py .../probe-b
VIOLATION: timeline[3].depends_on: unknown event 'ghost-event-r95'
1 violation(s); no canon changed
exit=1
```

Fires as specified, stable message. (`map_obligations` r94 rev on `probe-b`:
`raw=15 mapped=15` / `RESULT PASS` exit=0 — the unknown id is not a map concern.)

### (c) tick 9 on the aftermath event

```
(c) aftermath tick -> 9
$ python3 corpus/fixtures/check_bible.py .../probe-c
VIOLATION: timeline[3]: double-booked 'aru' at tick 9 in timeline[0] ('quiet-rise') and 'chalk-stair'
VIOLATION: timeline[3].depends_on: timeline inversion 'paired-crossing-decision' tick 10 not before 'aftermath-missing-evin' tick 9
2 violation(s); no canon changed
exit=1
```

The required inversion report is present; the double-booking line is an additional
rule that also fires because actor `aru` already occupies tick 9 at `quiet-rise`.
Both quoted. (`map_obligations` r94 rev: `raw=15 mapped=15` / `RESULT PASS` exit=0.)

### (d) remove the tick-10 row

```
(d) removed paired-crossing-decision -> ids ['aru-ninth-bell', 'evin-ninth-bell', 'aftermath-missing-evin']
$ python3 corpus/fixtures/check_bible.py .../probe-d
VIOLATION: timeline[2].depends_on: unknown event 'paired-crossing-decision'
1 violation(s); no canon changed
exit=1
```

The dangling reference is reported exactly (index shifts 3→2). Cross-tool: the r94
`map_obligations` revision **also** fails on this mutation:

```
$ python3 corpus/tools/map_obligations.py .../probe-d
OBLIGATIONS raw=14 mapped=15
FINDING phantom_obligation: timeline.json#/3 is not a raw source-attributed obligation
FINDING source_id_mismatch: timeline.json#/2 does not bind to 'aru-aftermath-note'
RESULT FAIL
exit=1
```

## 3. Bonus probes — full dependency surface (same fixture, scratch)

```
(e) repeated dep ['paired-crossing-decision','paired-crossing-decision']
VIOLATION: timeline[3].depends_on[1]: repeated dependency 'paired-crossing-decision'
exit=1
(f) self dep ['aftermath-missing-evin']
VIOLATION: timeline[3].depends_on[0]: self dependency 'aftermath-missing-evin'
VIOLATION: timeline[3].depends_on: timeline inversion 'aftermath-missing-evin' tick 11 not before 'aftermath-missing-evin' tick 11
exit=1
```

Summary of the `depends_on` surface on this fixture: unknown / inversion / repeated /
self all fire; **omission is silent**.

## 4. Live-fixture map observation (timing-qualified)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS
exit=0
```

Consistent with C2's "15 map obligations" on the delivered fixture, but recorded
with the r94 tool revision `cc1df4dc` — P1's C1 revision was not in the tree at
report time, so this is not a C1-verified receipt. (Earlier, before P4's
`claim-excerpt-map.md` landed, the same command was exit 2 `FINDING map_missing`;
that was a mid-round timing artifact, not a defect.)

## 5. Findings

1. **Blind spot (primary):** `check_bible` cannot detect a dropped dependency.
   Probe (a) is CLEAN exit 0 while the fixture's README and claim-excerpt-map still
   assert the dependency. The seat prompt's stated expectation for (a) does not hold;
   reported as observed.
2. Probes (b), (c), (d) report as specified with stable message text and exit 1;
   (c) additionally fires double-booking, (d) is additionally caught by the r94
   `map_obligations` revision via `phantom_obligation` + `source_id_mismatch`.
3. Fixture integrity: 5/1/4/4 counts, baseline CLEAN exit 0, JSON hashes byte-stable
   across all probe runs; my copies match the delivered bytes.

## 6. Live-tree-touch check

Fixture JSON hashes before probing and at report time are identical (§1). Probe
mutations exist only under `.ufo/waves/round-95/seats/scratch/V14/probe-*`.
`git status --porcelain` at report time:

```
 M LOG.md
?? .ufo/waves/round-95/
?? corpus/fixtures/r95-crossing-aftermath/
```

`LOG.md` modification and both untracked paths are the round's declared artifacts
(round-95 declaration + new fixture), not this seat's writes.

**Bottom line: PASS — all four probes executed on the delivered fixture bytes; (b),
(c), (d) report exactly as specified, and (a) returns CLEAN exit 0, exposing that
`check_bible` has no dependency-presence rule (the seat prompt's expected report for
(a) does not occur; reported as a blind-spot finding, not forced).**

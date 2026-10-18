# V53 — byte-prefix-2 (round 96)

Seat: V53 byte-prefix-2. Verifies Q4's preservation claim for
`corpus/fixtures/r96-crossing-response/` against `corpus/fixtures/r95-crossing-aftermath/`:

1. the five copied files are byte-identical (`cmp`);
2. `sources.json` / `timeline.json` differ only by appended rows (json-level diff);
3. `fictional-excerpts.md` is a strict byte-prefix of r95's plus an appended section.

Read-only except this report and scratch dir
`.ufo/waves/round-96/seats/V53-scratch/` (poll.sh, verify_v53.py, r95-hashes.txt,
r96-frozen-hashes.txt, verify-preliminary.txt, verify-frozen.txt).

## Poll-wait / revision freeze

- First check ~17:38: fixture dir absent → started poll loop (20 s cadence, 40 tries).
- First sighting ~17:39: all 8 Q4 files present, but `sources.json`/`timeline.json`
  at intermediate sizes 1742/1678 B (Q4's disclosed mid-seat comma correction not yet
  applied); Q4 producer report absent → held.
- Preliminary pass against the intermediate: all three checks green (kept as
  `verify-preliminary.txt`; not the verdict basis).
- 17:40:16: `sources.json`/`timeline.json` rewritten (1741/1677 B, mtime 17:40:16-03:00).
- Poll returned `READY after 10 tries` (~200 s); Q4 report present:
  `.ufo/waves/round-96/seats/Q4-fixture-json.md`.
- Frozen revision re-hashed at 2026-10-17T17:42:38-03:00; identical to the hash set
  taken immediately after the Q4 report landed. All checks below ran on this revision.

Frozen sha256 (all eight Q4 files), each matching Q4's declared delivered hashes:

```
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  timeline.json
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  fictional-excerpts.md
```

Reference integrity: `git status --porcelain -- corpus/fixtures/r95-crossing-aftermath/`
→ 0 paths (r95 reference is git-clean); r95 working-tree hashes match Q4's quoted
`dcb2d92` baseline hashes.

## Check 1 — five copied files byte-identical (cmp)

Command (cwd `corpus/fixtures/`):

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
    cmp r95-crossing-aftermath/$f r96-crossing-response/$f && echo "cmp OK: $f (byte-identical)"; done
```

Observed (exit 0 for every `cmp`, no diff output):

```
cmp OK: entities.json (byte-identical)
cmp OK: relations.json (byte-identical)
cmp OK: contradictions.json (byte-identical)
cmp OK: inspiration-note.md (byte-identical)
cmp OK: source-excerpt.md (byte-identical)
```

Corroborated by sha256 equality (r95 == r96) for all five; sizes 1449/139/3/1956/640 B
equal on both sides.

## Check 2 — sources.json / timeline.json: exactly one appended row each, shared prefix parsed-equal

Command: `python3 .ufo/waves/round-96/seats/V53-scratch/verify_v53.py`
(full transcript `verify-frozen.txt`). Observed:

```
sources.json: r95 rows=4 r96 rows=5 delta=1
  shared-prefix parsed-equal: True
  supplementary raw-text inherited-rows prefix (r95 minus closing ]): True
  r96 ids: ['veil-verse', 'paired-clock', 'crossing-minute', 'aru-aftermath-note', 'evin-response-note']
timeline.json: r95 rows=4 r96 rows=5 delta=1
  shared-prefix parsed-equal: True
  supplementary raw-text inherited-rows prefix (r95 minus closing ]): True
  r96 ids: ['aru-ninth-bell', 'evin-ninth-bell', 'paired-crossing-decision', 'aftermath-missing-evin', 'response-evin-salt-court']
```

Appended rows (verbatim, parsed values):

- `sources.json#/4`: `{"id": "evin-response-note", "title": "Evin's Salt Court Response Note", "kind": "fictional first-person note", "reliability_note": "Newly authored fictional note; Evin reports being at Salt Court through the same agreed bell. It asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved. It records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact."}`
- `timeline.json#/4`: `{"id": "response-evin-salt-court", "tick": 12, "entity_id": "evin", "place_id": "salt-court", "depends_on": ["aftermath-missing-evin"], "description": "Evin reports being at Salt Court through the same agreed bell; the note asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved.", "source_id": "evin-response-note"}`

Raw `diff` (line-level, stronger than required — pure appends, no changed/removed lines):

```
$ diff r95-crossing-aftermath/sources.json r96-crossing-response/sources.json
24a25,30
>   },
>   { ... appended object ... }        # full text in verify-frozen.txt / Q4 report

$ diff r95-crossing-aftermath/timeline.json r96-crossing-response/timeline.json
41a42,52
>   },
>   { ... appended object ... }
```

Both files are valid JSON (parsed), ids unique, both end with newline, sizes 1741/1677 B
(32/54 lines). No row before the append changed at parsed level, and none changed at raw
text level either.

## Check 3 — fictional-excerpts.md strict byte-prefix + appended section

```
r95 bytes=1845 r96 bytes=2588
strict byte-prefix (rb.startswith(ra)): True
appended bytes=743
```

The first 1845 bytes of the r96 file are exactly the r95 file's bytes; the appended
743 bytes begin after r95's final line ("Scope: ... supplies no other duty.") and are:

```
(blank line)
## Round 96 response note (2026-10-17)

Newly authored fictional first-person note, attributed to in-world source ID `evin-response-note`, folio 6, lines 1–4. This section is appended after the preserved r95 text above; the inherited wording is unchanged.

> Tick 12: I was at Salt Court through the same agreed bell.
> I make no accusation against Aru.
> I select no winner between our two accounts.
> Both accounts stand unresolved.

Scope: this appended section is Evin's first-person report of one crossing occasion. It asserts no accusation and no breach, selects no winner, and does not resolve the two first-person accounts against each other; the crossing-scoped agreement above is unchanged, and the record supplies no other duty.
```

Raw `diff` shows `31a32,42` (append only; r95's line 31 preserved). Content matches the
C2 wording: second account, same occasion, unresolved — no accusation, no winner;
`contradictions.json` remains the byte-copy `[]\n`.

## Observations (non-failing)

- Producer mid-flight rewrite observed: my preliminary pass ran against intermediate
  `sources.json`/`timeline.json` (1742/1678 B) that passed the same three checks; the
  frozen revision (1741/1677 B, mtime 17:40:16) also passes. Q4 disclosed this correction
  ("rewritten at 17:39" in its narrative; file mtime reads 17:40:16-03:00 — narrative
  timestamp is approximate). Frozen bytes match Q4's declared delivered hashes, so the
  discrepancy has no effect on the verdict.
- All three checks were also green on the intermediate, so even the discarded revision
  did not violate the preservation claim.

## Verdict

All three checks PASS on the frozen revision (Q4 report present; hashes stable across
two independent reads at 17:41 and 17:42:38-03:00; declared == observed). No check
failed; no contradiction found.

Bottom line: PASS — five copied files byte-identical (cmp), sources/timeline differ only
by one appended row each (json-level and raw-diff pure appends), fictional-excerpts.md is
a strict 1845-byte prefix of r95 plus a 743-byte appended Round 96 section; frozen hashes
match Q4's declared hashes.

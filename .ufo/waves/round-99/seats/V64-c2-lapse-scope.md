# V64 — c2-lapse-scope (round 99)

- **Seat:** V64 c2-lapse-scope (verifier). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Every command below ran from that root with `python3` unless noted. Session cwd is the parent `/home/vgpnk/Projects/shokunin`; writes used absolute paths.
- **Baseline:** r98 closure `4265df5` (declaration in `LOG.md` lines 3200–3265, read this pass). Re-dispatch; declaration unchanged.
- **Seat claim under test:** the lapse note does not modify the inherited `for this crossing only` relation bound anywhere; the window-close claim traces to the original minute's wording (quote both).
- **Required artifacts:** `corpus/knowledge/r99-lapse-scope-note.md` (S5) and an S5 producer report under `.ufo/waves/round-99/seats/S5*.md`. Sibling S5 file `corpus/knowledge/r99-gate-blind-spot-table.md` was also checked and was absent.
- **Writes:** this report only, plus scratch `.ufo/waves/round-99/seats/V64-scratch/poll.log`. No commits, no pushes, no network, no nested agents, no corpus bytes.
- **Axes:** presence of the lapse note and S5 report; non-modification of the inherited relation bound; trace of the window-close claim to the original minute's wording. Only presence was testable. It failed. The other two axes are not judged.

## Verdict

**ABSENT.** The lapse note and the S5 producer report never appeared. This seat does not confirm or falsify the claim. Fixture prose already on disk is not a substitute for the note.

## Poll-wait

Protocol: artifacts AND producer report; 20 s cadence; 40 tries; ABSENT, never verify a plan. Stall-escape recorded, not treated as fatal.

Tries 1–6 were manual 20 s sleeps (22:02:24, 22:02:50, 22:03:14, 22:03:39, 22:04:03, 22:04:26 -03:00). Each `ls corpus/knowledge/r99*` and `ls .ufo/waves/round-99/seats/S5*` failed with "No such file or directory". S3's report was present from 22:01; S4's report from 22:03. Those are not this seat's producer.

Tries 7–36 are in `.ufo/waves/round-99/seats/V64-scratch/poll.log`, started 2026-10-17T22:05:46-03:00. Every line is `ABSENT … note_exists=no s5=none`. The host killed that poller at the 600 s background cap after try 36 (22:15:26). Resume tries 37–40, same log:

```
ABSENT try=37 2026-10-17T22:24:28-03:00 note_exists=no table_exists=no s5=none
ABSENT try=38 2026-10-17T22:24:48-03:00 note_exists=no table_exists=no s5=none
ABSENT try=39 2026-10-17T22:25:08-03:00 note_exists=no table_exists=no s5=none
ABSENT try=40 2026-10-17T22:25:28-03:00 note_exists=no table_exists=no s5=none
POLL_EXHAUSTED try=40 2026-10-17T22:25:28-03:00
ls: cannot access 'corpus/knowledge/r99*': No such file or directory
ls: cannot access '.ufo/waves/round-99/seats/S5*': No such file or directory
```

Final check after exhaustion, 2026-10-17T22:27:43-03:00:

```
$ ls -la corpus/knowledge/r99-lapse-scope-note.md corpus/knowledge/r99-gate-blind-spot-table.md .ufo/waves/round-99/seats/S5*.md
ls: cannot access 'corpus/knowledge/r99-lapse-scope-note.md': No such file or directory
ls: cannot access 'corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access '.ufo/waves/round-99/seats/S5*.md': No such file or directory
$ ls corpus/knowledge | rg 'r99|lapse'
(no output)
```

`find corpus .ufo/waves/round-99 -name '*lapse*' -o -name 'S5*'` at 22:19:24 returned only `corpus/fixtures/r99-window-lapse`, other seats' scratch copies of that fixture, and an archived r98 `S5-knowledge-notes.md` under `V40-scratch`. No r99 lapse note.

## What was not judged

- Whether `r99-lapse-scope-note.md` rewrites, extends, narrows, or restates the inherited `agreed_co_stewardship_for_this_crossing` / "for this crossing only" bound. The file does not exist. Not confirmed. Not failed.
- Whether that note's window-close claim traces to the original minute. The note does not exist, so its wording was not quoted from a delivered note.

The r99 declaration in `LOG.md` (lines 3225–3236 and 3263–3264) names the intended note. That is a plan. It was not verified.

## Witnessed fixture text (not a verdict)

S3 and S4 did deliver `corpus/fixtures/r99-window-lapse/`. Recorded so a later pass can quote the same lines. This does not stand in for the missing note.

Relation file, r94 through r99, one parsed row, sha256 `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9`, 139 bytes, `identical_to_r98=True` for every file in that chain:

```
[{'from': 'aru', 'to': 'evin', 'type': 'agreed_co_stewardship_for_this_crossing', 'source_id': 'crossing-minute'}]
```

Original minute, `corpus/fixtures/r99-window-lapse/fictional-excerpts.md:17-20` (r99 bytes start with the r94 minute file; `startswith` was `True`). The word `window` is absent from `corpus/fixtures/r94-paired-crossing` and from `corpus/fixtures/r88-m3-maya-cluster` (`rg '\bwindow\b'` → no matches).

```
> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
```

Window-close sentence in the delivered fixture, `fictional-excerpts.md:70`:

```
> Tick 15: The crossing-window named in the original minute has closed.
```

Same sentence is the J21 anchor (`claim-excerpt-map.md:42`), the tick-15 description (`timeline.json:84`), and the `clerk-lapse-note` reliability note (`sources.json:48`). The minute does not contain the token `window` or the phrase `crossing-window`. Any trace from that sentence to the minute is a paraphrase of "for this crossing only" / "the named rain-dark crossing", not a verbatim quotation of "window". That observation is about the fixture. It is not a verdict on the absent lapse note.

Map row J11 still points at `relations.json#/0` with anchor `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` (`claim-excerpt-map.md:32`). Namespace cell is `r99-window-lapse:crossing-minute`. Not re-checked against the missing note.

## Not done

- No read of `r99-lapse-scope-note.md` (absent).
- No read of an S5 report (absent).
- No PASS/FAIL on bound non-modification or on the note's trace.

ABSENT: `corpus/knowledge/r99-lapse-scope-note.md` and the S5 producer report were missing after 40 polls (stall-escape after the host killed the poller at try 36); the lapse-note claim was not verified.

# P4 — fixture-docs seat report (round 95)

Seat: P4 fixture-docs. Exclusive ownership: `corpus/fixtures/r95-crossing-aftermath/README.md` and
`corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`. No other files written; no commits; no network.

Repo root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline: r94 closure `fb118c4`
(working tree at start: `M LOG.md` + `?? .ufo/waves/round-95/` only).

## Poll-wait for P3

Background poll (`for i in $(seq 1 40)`, 20 s cadence) on the eight P3 fixture files with a
timeline=4 / sources=4 completeness gate:

```
attempt=1..4 missing files
attempt=5..6 present but timeline=3 sources=3
READY attempt=7 timeline=4 sources=4
```

No file was authored before the P3 bytes were present and complete. P3's copies verified:
`cmp` on `entities.json`, `relations.json`, `contradictions.json`, `source-excerpt.md`,
`inspiration-note.md` → `IDENTICAL` to `r94-paired-crossing`; `diff` of
`fictional-excerpts.md` shows only the appended section (r94 lines 1–20 byte-preserved,
new lines 21–31).

## Artifact 1 — `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`

Canonical one-obligation-per-row form, modeled on `r94-paired-crossing/claim-excerpt-map.md`:
15 JSON-fact rows (J01–J15), 2 editorial rows (S01/S02), `**Expected inventory:** 15 JSON facts;
2 editorial rows; 17 total mapped rows; 13 distinct excerpt anchors.`

- J01–J14 are the r94 rows carried with pointer, source ID, path, span, mode, and anchor
  unchanged; only the path-qualification column names this fixture's cluster path
  (`r95-crossing-aftermath:paired-clock`, `r95-crossing-aftermath:crossing-minute`), with the
  prior namespaces stated in prose.
- J15: pointer `` `timeline.json#/3` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) ``,
  source `aru-aftermath-note`, namespace `r95-crossing-aftermath:aru-aftermath-note`,
  excerpt `fictional-excerpts.md`, span `22-31`, mode `verbatim`, anchor
  `Tick 11: I waited at the Chalk Stair through the agreed bell.`
- Span 22–31 is exactly the appended aftermath section (P3 diff added lines 21–31; line 21 is
  the blank separator), so it includes no inherited line. The four quoted sentences sit on
  lines 26–29; the anchor is on line 26. Prose records that lines 27–29 carry the non-arrival,
  the crossing-only bound, and the no-other-duty/no-breach assertion.

### Fidelity check vs r94 map (command + output)

```
$ python3 - <<'PY'   # parse both JSON-facts tables; compare cells [ID,pointer,source,path,span,mode,anchor]
...
r94 rows 14 r95 rows 15
inherited identical rows: 14 ['J01',...,'J14']
diffs: []
J15 row: ('`timeline.json#/3` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`)', '`aru-aftermath-note`', '`fictional-excerpts.md`', '22-31', '`verbatim`', '`Tick 11: I waited at the Chalk Stair through the agreed bell.`')
new rows: ['J15']
```

### Anchor preflight (grep -nF, all in-span)

```
Aru carried the north lantern at Quiet Rise => 12
Evin held the south bell at Salt Court => 13
The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court. => 17
Tick 9: Aru carried the north lantern at Quiet Rise. => 12
Tick 9: Evin held the south bell at Salt Court. => 13
north lantern at Quiet Rise => 12
south bell at Salt Court => 13
After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10. => 18
There, they agreed, for this crossing only, to share stewardship of the Chalk Stair. => 19
Their tick-10 decision depends ... midpoint. => 20
He called out “Earth,” => source-excerpt.md:5
and the solid land appeared. => source-excerpt.md:5
Tick 11: I waited at the Chalk Stair through the agreed bell. => 26
```

`grep -n -i 'delivery mode' fictional-excerpts.md source-excerpt.md` → exactly one declaration
(`fictional-excerpts.md:3`), so the inline-mode read is unambiguous.

## Artifact 2 — `corpus/fixtures/r95-crossing-aftermath/README.md`

Modeled on the r94 fixture README: continuation framing; namespace/occasion comparison (tick-9
entries, inherited tick-10 decision, new tick-11 event depending on `paired-crossing-decision`);
counts **5 entities / 1 relation / 4 events / 4 sources**; the crossing-only bound; the explicit
statement that the record asserts no other duty, no breach, no continuing obligation, and no
obligation beyond this crossing; 15 source-attributed JSON pointer obligations (14 inherited +
the new tick-11 row); bounded Spence design prompt; replay block with the three commands.

## Checker receipts (delivered revision)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
... PASS J01..J15, PASS S01, PASS S02 ...
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
EXIT=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS
EXIT=0
```

Tool state at measurement: two receipts are recorded.

1. Pre-P1 revision, `md5sum corpus/tools/map_obligations.py` =
   `882eeebdeb2ac6ea05a8cdb1afff7ba3` — the outputs quoted in the block above.
2. Settled P1 revision, bracketed in one command:

```
$ md5sum corpus/tools/map_obligations.py
bcea56042588acfc444ac6629d6d7ce2  corpus/tools/map_obligations.py
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
EXIT=0
$ md5sum corpus/tools/map_obligations.py
bcea56042588acfc444ac6629d6d7ce2  corpus/tools/map_obligations.py
```

Counts cross-check: `python3 -c "json.load(...)"` → entities 5, relations 1, timeline 4,
sources 4, contradictions `[]`.

Hashes of my two artifacts: map `a872889e86a10127750ba0647e4829ff`, README
`5ccf979d845c20d00ad34e8462ef3b90` (md5; unchanged at report time).

## Boundaries / caveats

- Structural CLEAN, the support receipt, and `map_obligations` are map/lexical checks; they are
  not semantic support, canon truth, or rights review.
- I did not modify any P1/P2/P3/P5 file and did not run any command that writes outside my two
  artifacts.

## Addendum — post-P1 re-run and tool-lane observations

- P1's tool changed repeatedly during this seat's window (observed md5s in order:
  `882eeebd…` r94 revision, `123039aa…`, `a7e38f9d…`, `986e4c64…`, `bcea5604…`). Against the
  `123039aa`/`a7e38f9d` snapshots, r95 gave `OBLIGATIONS raw=15 mapped=15 / RESULT PASS`
  (exit 0), r94 14/14, r93 12/12.
- Transient in-flight state (recorded as observed, not charged to any seat): at md5
  `986e4c646721317752c84750161671d1` the tool raised
  `ValueError: too many values to unpack (expected 2, got 15)` on the r95 fixture and the same
  traceback with `got 14` on r94 — P1 mid-edit, both fixtures failing identically, not a map
  defect.
- Settled revision `bcea56042588acfc444ac6629d6d7ce2` (stable ≥60 s, bracketed above): r95
  15/15 PASS exit 0; r94 `raw=14 mapped=14`, `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2;
  TOTAL-ROWS 16/16` PASS exit 0; r93 `raw=12 mapped=12`, `INVENTORY JSON-FACTS 12/12;
  EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15` PASS exit 0.
- At that same revision `map_obligations.py --self-test` exits 2 with
  `FINDING self_test_contract: contract self-test cases do not match the implemented cases`
  (observed, true exit 2), because `map-obligations-contract.json` (md5 `bb8069ab…`, still 20
  cases) had not yet been updated by P2 to the 22-case set the tool implements. That is the
  P1/P2 lane's in-flight state, outside this seat's ownership; recorded for the round
  integrator. `support_check.py` is unchanged (md5 `90b6a739…`) and gives `SOURCE-SUPPORT
  15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17; RESULT PASS` exit 0;
  `check_bible.py` re-run gives `CLEAN … 0 violations` exit 0.
- The tool moved once more after that: at `md5 d31b8182953e9088a155f4ed2978af5b`
  (stable across the bracketed run) r95 gives `OBLIGATIONS raw=15 mapped=15`,
  `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17`, `RESULT PASS` exit 0, and
  r94 `raw=14 mapped=14`, `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16`,
  `RESULT PASS` exit 0.
- P2's contract then landed (md5 `d2a77aa09e5cd38d73d772bb11a5914e`, 22 cases), resolving the
  transient self-test mismatch: `map_obligations.py --self-test` at tool md5 `d31b8182…` now
  ends `SELF-TEST PASS frozen_verdict_mismatch …` / `RESULT PASS` exit 0 over all 22 cases.
- Final sweep at report time: `support_check` r95 `RESULT PASS` exit 0; `check_bible` r95
  `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0; my map md5
  `a872889e86a10127750ba0647e4829ff` and README md5 `5ccf979d845c20d00ad34e8462ef3b90`
  (unchanged).

## Bottom line

PASS — both owned artifacts authored on P3's complete delivered bytes (all 8 fixture files
match P3's reported delivered sha256); support_check 15/15 + 2/2 PASS (exit 0), map_obligations
15/15 PASS (exit 0) on the r94 revision, on `bcea5604…`, and on the delivered `d31b8182…` with
the 22-case contract (`--self-test` RESULT PASS exit 0), check_bible CLEAN, all 14 inherited
rows unchanged. No caveats outstanding.

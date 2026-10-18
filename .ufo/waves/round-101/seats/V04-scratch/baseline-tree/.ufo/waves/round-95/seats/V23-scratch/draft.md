# V23 — verdict-depth (round 95) — DRAFT

Seat: V23 verdict-depth. Scope per seat spec: read the C2 verification seats
(V08–V14), run 2 own spot replays, issue exactly one DEPTH verdict on the
declared C2 before→after ("first reported-non-performance class", 5/1/3→5/1/4
preserving continuation) with named bounds.

Baseline `fb118c4`; working tree during window: `M LOG.md`,
`?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`,
`M corpus/tools/map_obligations.py` (P1 landed 16:22:37 mid-window).

## Before-state replayed (r94-paired-crossing)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS
exit=0
counts: entities 5 relations 1 events 3 sources 3
```

## Spot replay 1 — check_bible on r95-crossing-aftermath

(command, output, exit; hash of checker; fixture hashes before/after)

## Spot replay 2 — map_obligations on r95-crossing-aftermath (+ preservation)

(command, output, exit; tool sha256 at run; counts 5/1/4/4;
5 byte-copy files identical; timeline/sources parsed prefix identical;
fictional-excerpts 1116-byte prefix preserved; map rows J01–J14 identical
modulo cluster path, J15 new; support_check 15/15+2/2)

## C2 verification seats read

- V08 c2-checker: PASS ...
- V44 exit-contract-c2: PASS ...
- V20 doc-parity: PASS ...
- (V09–V14: status at cutoff)

## Verdict

DEPTH: <improved/harmed/unchanged/unprovable-but-better> — with named bounds.

## Non-axis observations

## Bottom line

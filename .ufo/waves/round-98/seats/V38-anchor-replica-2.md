# V38 — anchor-replica-2 (round 98)

**Seat:** V38 `anchor-replica-2` (verifier). **Scope:** independent anchor
re-verification, python method, of `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md`
— all 20 JSON-fact anchors in-span, verified with my own implementation (not
`support_check.py`), plus inheritance/placement/inventory/pointer checks.
**Baseline:** r97 closure `9a3d648`. **Repo root:**
`/home/vgpnk/Projects/shokunin/lore-shokunin`. **Scratch (exclusive):**
`.ufo/waves/round-98/seats/V38-scratch/` (absolute lane path; checker, poll
script, logs, receipts). Leaf seat: no nested agents, no commits, no pushes, no
network. My only writes are this report and that scratch dir — `git status`
shows only the producers' declared paths, `LOG.md`, and the untracked
`.ufo/waves/round-98/` + `corpus/fixtures/r98-clerk-filing/` trees; no strays
from this seat.

## 0. Poll-wait evidence (target = S3 payload + S4 map/README + S3/S4 reports)

Poller `.ufo/waves/round-98/seats/V38-scratch/poll.sh` (20 s cadence, 40 tries;
requires the six key fixture files AND `S3-*.md`/`S4-*.md` producer reports,
plus a one-try md5 byte-stability window), log `V38-scratch/poll.log`:

```
try 1 23:28:28 missing: REPORT:S3 REPORT:S4
...
try 8 23:30:48 missing: REPORT:S3 REPORT:S4
try 9..11 23:31:08-23:31:48 missing: REPORT:S4
PRESENT-UNSTABLE try=12 23:32:08 md5set=88fccff017399b64a122fcc64f9385d8
READY-STABLE try=13 23:32:28 md5set=88fccff017399b64a122fcc64f9385d8
```

Verification ran only after `READY-STABLE`. Endgame convention honored: the poll
waited for S3/S4 reports only — SELF (V38) subtracted — and no stall-escape was
needed (ready at try 13/40).

Hazard observed (recorded, not fatal): between 20:28:24 and ~20:31 the new
directory existed with **r97 placeholder bytes** (`README.md`/`claim-excerpt-map.md`
byte-identical to r97; matches S4's report section A). An existence-only poll
would have verified placeholders; this seat's poll required byte-stability plus
the producer reports, and the verified map hash equals S4's declared hash
(section 1), so the verified revision is the final S4 delivery, not a placeholder.

## 1. Method and frozen revision

Checker `V38-scratch/v38_check.py` (own parser; pure-Python substring scan per
line cross-checked against `grep -nF`; in-span iff ≥1 occurrence and **every**
occurrence line inside the declared span; inherited rows compared by ID against
r97 for anchor/span/path equality and resolved line-set equality; new rows must
occur only beyond r97's last excerpt line; byte-prefix preservation; declared
inventory equality; JSON-pointer resolution; supplementary pointed-`source_id`
vs map-source match). Parser validated first on r97↔r96
(`V38-scratch/validate-r97-vs-r96.txt`): `RESULT ALL-ANCHOR-CHECKS-PASS` — it
reproduces r97's map exactly (19 rows; J17 appended-only vs r96's 42-line
excerpt; S01/S02 in-span at `source-excerpt.md:5`), matching V16's r97 result.

Frozen revision (sha256, `V38-scratch/frozen-hashes.txt`; re-checked with
`sha256sum -c` **after** the run: all OK):

| File | sha256 |
|---|---|
| `claim-excerpt-map.md` | `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` |
| `fictional-excerpts.md` | `29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de` |
| `entities.json` | `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` |
| `sources.json` | `32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3` |
| `timeline.json` | `eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af` |
| `README.md` | `32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926` |

S4's report independently declares the same map (`c1099d0e…`) and README
(`32efc78f…`) hashes — reproduced. `contradictions.json`, `inspiration-note.md`,
`relations.json`, `source-excerpt.md` are sha-identical to r97.

## 2. Result — checker output (verbatim, `V38-scratch/final-run.txt`)

```
== V38 checker: NEW=r98-clerk-filing (22 rows: 20 json / 2 editorial) vs REF=r97-crossing-acknowledgment (19 rows) ==
ref excerpt last line=53; new excerpt prefix-identical=True; new excerpt lines=64
inventory declared=(20, 2, 22, 18) parsed=(20, 2, 22, 18)
new rows (vs ref ids): ['J18', 'J19', 'J20']
dropped ref ids: []
J01  span=12 py=[12] grep=[12] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[12] == this=[12] same=True ptr=OK
J02  span=13 py=[13] grep=[13] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[13] == this=[13] same=True ptr=OK
J03  span=12 py=[12] grep=[12] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[12] == this=[12] same=True ptr=OK
J04  span=13 py=[13] grep=[13] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[13] == this=[13] same=True ptr=OK
J05  span=17 py=[17] grep=[17] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[17] == this=[17] same=True ptr=OK
J06  span=12 py=[12] grep=[12] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[12] == this=[12] same=True ptr=OK
J07  span=13 py=[13] grep=[13] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[13] == this=[13] same=True ptr=OK
J08  span=12 py=[12] grep=[12] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[12] == this=[12] same=True ptr=OK
J09  span=13 py=[13] grep=[13] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[13] == this=[13] same=True ptr=OK
J10  span=18 py=[18] grep=[18] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[18] == this=[18] same=True ptr=OK
J11  span=19 py=[19] grep=[19] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[19] == this=[19] same=True ptr=OK
J12  span=12 py=[12] grep=[12] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[12] == this=[12] same=True ptr=OK
J13  span=13 py=[13] grep=[13] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[13] == this=[13] same=True ptr=OK
J14  span=18-20 py=[20] grep=[20] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[20] == this=[20] same=True ptr=OK
J15  span=22-31 py=[26] grep=[26] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[26] == this=[26] same=True ptr=OK
J16  span=33-42 py=[37] grep=[37] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[37] == this=[37] same=True ptr=OK
J17  span=44-53 py=[48] grep=[48] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[48] == this=[48] same=True ptr=OK
J18  span=60 py=[60] grep=[60] agree=True IN-SPAN=True outside=[] appended-only=True (ref file 53 lines) ptr=OK
J19  span=59-60 py=[59] grep=[59] agree=True IN-SPAN=True outside=[] appended-only=True (ref file 53 lines) ptr=OK
J20  span=55-64 py=[59] grep=[59] agree=True IN-SPAN=True outside=[] appended-only=True (ref file 53 lines) ptr=OK
S01  span=5 py=[5] grep=[5] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[5] == this=[5] same=True
S02  span=5 py=[5] grep=[5] agree=True IN-SPAN=True outside=[] vs-ref anchor-identical=True span-same=True path-same=True lines ref=[5] == this=[5] same=True
NOTES: none
RESULT ALL-ANCHOR-CHECKS-PASS
```

(Verbatim, matching `V38-scratch/final-run.txt`.)

**All 20 JSON-fact anchors are in-span**, each with exactly one occurrence
inside its declared span and zero outside-span occurrences; pure-Python scan and
`grep -nF` agree on every one of the 22 rows; every inherited row J01–J17
(and editorial S01/S02) is anchor/span/path identical to r97 and resolves to the
**same line numbers**; the three new rows occur only past r97's 53-line excerpt;
the excerpt file is a byte-prefix-preserving copy (`prefix-identical=True`);
declared inventory `(20, 2, 22, 18)` equals parsed; all JSON pointers resolve
with no `source_id` mismatch notes.

## 3. New-row evidence (map lines 39–41; excerpt lines 55–64)

```
| J18 | `entities.json#/5/first_appearance` (`clerk-maren`) | `clerk-filing-note` | `r98-clerk-filing:clerk-filing-note` | `fictional-excerpts.md` | 60 | `verbatim` | `I am Maren, clerk of the Chalk Stair registry` |
| J19 | `entities.json#/5/claims/0` (`statement`, `source_id`) | `clerk-filing-note` | `r98-clerk-filing:clerk-filing-note` | `fictional-excerpts.md` | 59-60 | `verbatim` | `I filed both pending accounts at the Chalk Stair registry.` |
| J20 | `timeline.json#/6` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-filing-note` | `r98-clerk-filing:clerk-filing-note` | `fictional-excerpts.md` | 55-64 | `verbatim` | `Tick 14: I filed both pending accounts at the Chalk Stair registry.` |
```

Appended excerpt block (lines 55–64) quoted in section 2 of the archive; the
anchors resolve to line 60 (J18), 59 (J19), 59 (J20) — all within spans, all
past the preserved 53-line r97 text.

## 4. Supplementary cross-check (repo tool, not the primary method)

`python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing` →
`SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; VALIDATED-ROWS 22/22` `RESULT PASS`
(exit 0; full output `V38-scratch/support-check-cross.txt`). This is a lexical
preflight only; it agrees with my independent result.

## 5. Limitations / non-claims

- Lexical anchors only: this seat verified that quoted anchor strings occur
  in-span; it makes no entailment, canon-truth, rights, or authenticity
  judgment (same boundary `support_check.py` declares).
- The verified revision is the byte-stable READY-STABLE revision (hashes in
  section 1, re-confirmed unchanged after my run); any later edit invalidates
  this receipt for the changed bytes only.

**Bottom line: PASS** — all 20 r98 JSON-fact anchors independently re-verified
in-span (python method, grep cross-checked) on the frozen S4 revision
`c1099d0e…`/`29e384bf…`, with inherited rows line-identical to r97 and new rows
appended-only.

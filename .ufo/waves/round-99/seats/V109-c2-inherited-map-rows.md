# V109 c2-inherited-map-rows — round 99

Seat: V109 (verifier). Claim under test: the 20 inherited map rows in `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` versus r98's `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` are identical modulo the path-qualified source-namespace column; zero pointer / anchor / span / mode drift.

Baseline: r98 closure `4265df5`. Lane HEAD at verification was `337f0fa` (the blocked-dispatch zero-increment commit); `4265df5` is an ancestor. The r98 map worktree blob equals `4265df5:corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` (`46f538e0859ad8cabd8650a4af28f0fd9ff3732a`; `git diff --stat 4265df5 --` that path empty). Comparison used `git show 4265df5:…`, not a later rewrite.

Leaf seat. No nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V109-scratch/` (`poll-start.txt`, `poll.log`). Did not edit corpus bytes.

## Poll-wait

Artifact required: delivered `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` that is not the r98 byte copy. Producer report required: an `S4*.md` under `.ufo/waves/round-99/seats/`. Cadence 20s. Did not score the plan or the pre-delivery placeholder.

```
poll 0 2026-10-17T22:01:…  map sha256 c1099d0ee9ee… == r98, 15028 bytes, 68 lines; S4 report absent
try=1 2026-10-17T22:02:02-03:00 identical_to_r98=YES lines=68 S4_report=none nreports=1
try=2 2026-10-17T22:02:22-03:00 identical_to_r98=YES lines=68 S4_report=none nreports=1
try=3 2026-10-17T22:02:42-03:00 identical_to_r98=YES lines=68 S4_report=none nreports=1
try=4 2026-10-17T22:03:02-03:00 identical_to_r98=NO  lines=70 sha=d2fe20e581d1 S4_report=none
try=5 2026-10-17T22:03:22-03:00 map unchanged; S4_report=none nreports=3
try=6 2026-10-17T22:03:42-03:00 map unchanged; S4_report=none
try=7 2026-10-17T22:04:02-03:00 READY S4_report=S4-fixture-docs.md nreports=4
```

S4 report present at scoring time: `S4-fixture-docs.md` 9303 bytes, mtime `2026-10-17 22:03:54 -0300`. Delivered map re-hashed at `2026-10-17T22:08:27-03:00`:

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
```

That matches the sha256 S4 recorded (17,119 bytes). r98 map sha256 `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` (15,028 bytes).

## Method

JSON-fact table only (`| ID | JSON fact pointer…`). Header identical in both files:

`ID | JSON fact pointer and fields | In-world source ID | Path-qualified source namespace | Excerpt path | Line span | R9 delivery mode | Exact anchor`

Inherited set = J01–J20. J21 is the new r99 row and was excluded from the inherited comparison (present only in r99, appended at map line 42). Cells split on `|` with no trim for the deciding comparison (no cell contains a literal `|`). Allowed delta: namespace cell equals the r98 cell with the single token `r98-clerk-filing` replaced by `r99-window-lapse`. Pointer = column 2, anchor = column 8, span = column 6, mode = column 7.

## Observed

```
worktree_r98_equals_4265df5 True
r99_json_fact_rows 21 [J01 … J20, J21]
r98_json_fact_rows 20 [J01 … J20]
missing_in_r99 []
missing_in_r98 []
inherited_positions_same True
inherited map lines r98 and r99 both 22–41
line_numbers_identical True
raw_line_swap_mismatches 0
raw_line_swap_identical_all_20 True
```

Untrimmed column mismatch counts, J01–J20:

| column | mismatches |
|---|---:|
| ID | 0 |
| JSON fact pointer and fields | 0 |
| In-world source ID | 0 |
| Path-qualified source namespace | 20 |
| Excerpt path | 0 |
| Line span | 0 |
| R9 delivery mode | 0 |
| Exact anchor | 0 |

Focus: pointer drift 0, anchor drift 0, span drift 0, mode drift 0. `namespace_not_pure_prefix_swap []`. Every inherited namespace cell changed, and every change was exactly that one prefix swap (source-id suffix unchanged). Examples:

```
J01  r98=`r98-clerk-filing:paired-clock`   r99=`r99-window-lapse:paired-clock`
J05  r98=`r98-clerk-filing:crossing-minute` r99=`r99-window-lapse:crossing-minute`
J15  r98=`r98-clerk-filing:aru-aftermath-note` r99=`r99-window-lapse:aru-aftermath-note`
J18  r98=`r98-clerk-filing:clerk-filing-note` r99=`r99-window-lapse:clerk-filing-note`
J20  r98=`r98-clerk-filing:clerk-filing-note` r99=`r99-window-lapse:clerk-filing-note`
```

Same pattern for J02–J04, J06–J14, J16, J17, J19 (20/20 `swap_exact=True`). Raw full-line substitution of `r98-clerk-filing` → `r99-window-lapse` reproduced each inherited r99 row byte-for-byte (`raw_line_swap_mismatches 0`). Each inherited r98 line contains that token exactly once.

## Out of scope (not scored)

Editorial rows S01–S02 are not part of the 20 inherited JSON-fact rows. Observed raw-equal to r98, shifted one line (r98 lines 49–50, r99 lines 50–51) because J21 was inserted above them. The R9 declaration table and the prose paragraphs were not column-diffed; they are not map rows. This seat did not re-run `support_check` or `map_obligations`.

## Verdict

PASS — 20/20 inherited rows identical modulo the namespace column (exact `r98-clerk-filing` → `r99-window-lapse` prefix swap); pointer/anchor/span/mode drift = 0.

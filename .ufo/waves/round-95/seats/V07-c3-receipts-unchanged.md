# V07 — c3-receipts-unchanged (round 95)

Seat: V07 c3-receipts-unchanged. Scope per seat spec: poll for P1, then on the
delivered tree re-run `support_check.py` on four fixtures and confirm the
fixtures' map+JSON files are byte-identical to `git show fb118c4`, i.e. that
C3's tool-only change left all support_check receipts unchanged.

- Baseline: r94 closure `fb118c4`. Expected receipts: r88-m3 = 10 JSON + 2
  editorial, r93-m2 = 12+3, r94-paired-crossing = 14+2, r87-myth-cluster = 14+8.
- Verified tool revision (delivered by P1, captured at verification time
  16:28 local): `corpus/tools/map_obligations.py` sha256
  `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`, mtime
  `2026-10-17 16:26:27 -0300`, `git diff --numstat fb118c4` = `130 12` (matches
  P1's declared footprint). `corpus/tools/support_check.py` untouched
  (blob `a69ae9d2…`, sha256 `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`).
- Other tree state at verification: `M LOG.md`, `M corpus/tools/map_obligations.py`,
  untracked `.ufo/waves/round-95/` and `corpus/fixtures/r95-crossing-aftermath/`
  (P3/P4/P5 artifacts; none touch the four C3 fixtures).

## 0. Poll-wait log

- Poll loop (20 s cadence) started 16:17:31. P1's tool diff first appeared at
  try 16, 16:22:31; the file was still being edited then (mtime 16:26:27 was
  only 4 s old when checked at 16:26:31). P1's report
  `.ufo/waves/round-95/seats/P1-tool-code.md` appeared at try 32, 16:27:51
  (poll exit 0, READY). All verification below ran only after the report
  existed, and was re-checked for a frozen revision at 16:28:45 (tool sha256
  and mtime unchanged, fixtures clean).

## 1. Receipts on the delivered tree (post-P1)

Command (run once per fixture from repo root):

```sh
python3 corpus/tools/support_check.py corpus/fixtures/<dir>
```

Observed terminal lines and exit codes (quoted):

```text
=== r88-m3-maya-cluster ===
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
exit=0

=== r93-m2-kojiki-cluster ===
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15
SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 15/15; VALIDATED-ROWS 15/15
RESULT PASS
exit=0

=== r94-paired-crossing ===
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
exit=0

=== r87-myth-cluster ===
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0
```

All four match the seat-spec expectations exactly (10+2, 12+3, 14+2, 14+8),
each `RESULT PASS` exit 0.

Pre-delivery baseline: the same four commands were run at 16:17 (before P1's
first write at 16:22:31) and produced identical `SOURCE-SUPPORT` /
`EDITORIAL-ANCHORS` / `RESULT PASS` / exit-0 lines. Receipts are therefore
identical before and after the tool change, not merely at target values.

## 2. Fixture byte-identity vs `fb118c4`

Per-file Git blob identity for the map + JSON files of each fixture
(`claim-excerpt-map.md`, `entities.json`, `relations.json`,
`contradictions.json`, `sources.json`, `timeline.json`):

```sh
for d in r88-m3-maya-cluster r93-m2-kojiki-cluster r94-paired-crossing r87-myth-cluster; do
  for f in claim-excerpt-map.md entities.json relations.json contradictions.json sources.json timeline.json; do
    p="corpus/fixtures/$d/$f"
    old=$(git rev-parse "fb118c4:$p"); new=$(git hash-object "$p")
    [ "$old" = "$new" ] && echo "SAME $p" || echo "DIFF $p old=$old new=$new"
  done
done
```

Observed: `SAME` for all 24 files, 0 `DIFF` (e.g. r88
`claim-excerpt-map.md dcd669db…`, r93 `7b97d7d5…`, r94 `7edafa24…`,
r87 `90072da0…`; identical hashes for the JSON tables likewise).

Literal byte comparison against the baseline revision:

```sh
git show "fb118c4:$p" | cmp -s - "$p"
```

Observed: `cmp SAME=24 DIFF=0`.

Full-tree checks on the four fixture directories:

```sh
git diff --name-status fb118c4 -- corpus/fixtures/{r88-m3-maya-cluster,r93-m2-kojiki-cluster,r94-paired-crossing,r87-myth-cluster}
git ls-files --others --exclude-standard -- <same four dirs>
```

Observed: both empty (no tracked-file diffs, no untracked additions), and
`git ls-tree -r --name-only fb118c4 -- <dir>` equals `find <dir> -type f` for
all four (11/11/10/14 files). So every file in the four fixture trees is
byte-identical to `fb118c4`, and the 24 map+JSON files are additionally
confirmed by literal `cmp`.

## 3. Tool-only change confirmation

- `support_check.py` blob `a69ae9d2…` unchanged vs `fb118c4` — the receipt
  tool itself is byte-frozen, so the receipts are a function of frozen
  fixtures + frozen checker.
- The four fixture directories are byte-frozen (§2); the only corpus/tools
  change is P1's `map_obligations.py` (numstat 130/12), which `support_check.py`
  does not import or invoke (verified by reading its interface: standalone
  stdlib script; the receipt path was re-run clean on the delivered tree).
- C3's "zero corpus modifications" therefore holds for the receipts path on
  the delivered revision.

## 4. Caveats / observations

- P1's own report declares the live-contract `--self-test` pending P2's 22-case
  contract (scratch-copy 22/22 PASS). That is C1's coordination item, not this
  seat's; the receipts claim verified here does not depend on the contract.
- `contradictions.json` in r88/r93/r94 share blob `fe51488c…` (identical empty
  content); expected, not a finding.
- Nothing in this seat touched the tree; all commands were read-only. No
  scratch dir was declared for V07 and none was created.

## Bottom line

PASS — on the delivered revision all four `support_check` receipts are
identical before/after P1's change and at expected counts (r88 10+2, r93 12+3,
r94 14+2, r87 14+8; each `RESULT PASS`, exit 0), all 24 map+JSON fixture files
(and the full four fixture trees) are byte-identical to `fb118c4`, and
`support_check.py` itself is byte-frozen; C3's tool-only-change /
receipts-unchanged obligation holds.

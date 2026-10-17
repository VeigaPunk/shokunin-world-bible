# V59 — presence-final (round 95 collection closure)

**Seat role:** last seat of the round-95 64-seat wave, presence/mechanics finalization. Scope: count
seat reports under `.ufo/waves/round-95/seats/`, verify exclusive report paths and seat-ID headers,
verify the five producer artifact sets exist, and finalize `.ufo/waves/round-95/receipt.json` with
the real `collection_snapshot` (counts, missing lists, curves) leaving `agent_id`/`outcome` null for
the integrator (L1) to fill. Presence only — this seat does not judge any report's content, any claim
(C1/C2/C3), or any axis. Writes: this report, the receipt JSON (explicitly assigned to this seat),
and seat scratch `.ufo/waves/round-95/seats/V59-scratch/`. No corpus edits, no commits, no pushes,
no nested agents.

**Environment pin:** lane HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (`git rev-parse HEAD`) =
r94 closure `fb118c4`; working tree carries only the round's producer edits (`git status --short`:
` M LOG.md`, ` M corpus/tools/map_obligations.py`, ` M corpus/tools/map-obligations-contract.json`,
` M corpus/tools/README.md`, `?? corpus/fixtures/r95-crossing-aftermath/`,
`?? corpus/knowledge/r95-aftermath-scope-note.md`, `?? .ufo/waves/round-95/`). All commands run from
repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

## Declared roster (evidence)

- `LOG.md` round-95 declaration (tail, uncommitted): "One batched AgentSwarm, 64 seats: 5 producer
  seats (exclusive file ownership) + 59 verifier/judge seats … Seat reports exclusive under
  `.ufo/waves/round-95/seats/`."
- Roster used: `P1`–`P5` (producers) + `V01`–`V59` (verifiers) = 64 seats. Observed verifier scratch
  dirs (`V01-scratch`, `V20`, `V32-scratch`, `V42-scratch` at 16:16) confirm the `V<NN>` form.
- No committed `round-95/wave-spec.json` exists at snapshot time (`ls .ufo/waves/round-95/` → only
  `scratch/`, `seats/`), so the roster is taken from the LOG declaration, per this seat's instruction.

## Collection window (observed counts)

A 30 s-cadence watcher and a 20 s-cadence poller ran from 16:19:52 and 16:17:34 respectively; both
logs are preserved in `.ufo/waves/round-95/seats/V59-scratch/watch.txt` and `collection-curve.txt`
(111 and 120 lines). Condensed curve (exact logged `HH:MM:SS=count` values; 16:53:25 and 17:03:11
are direct `find … | wc -l` checks, all others from the two logs):

```
16:19:52=1   16:24:34=12  16:29:14=24  16:33:54=50  16:39:54=56  16:53:25=59  17:03:11=60
16:20:22=3   16:26:34=16  16:31:14=38  16:36:54=54  16:44:14=56  16:57:14=59  17:14:23=60 WATCH_TIMEOUT
```

Full curves are embedded in the receipt JSON (`collection_curve_20s_poller`,
`collection_curve_30s_watcher`). Collection growth stopped at 17:03 (`V57-concurrency-audit.md`,
last report written); audit snapshot 17:19:28 −03:00; the receipt was regenerated after two quote
corrections (curve values, README `r95` count) — its own `snapshot_time_local` records the exact
regeneration time.

## Findings at final snapshot (2026-10-17 17:19 −03:00)

1. **Count vs expected 64: 60 other-seat reports present when audited; 61/64 after this report.**
   All five producer reports (`P1-tool-code.md` … `P5-knowledge-note.md`) and 55 of 59 verifier
   reports are present. **Missing: `V09`, `V18`, `V33`** — no report, no scratch dir, no writes
   observed for any of the three through the final snapshot (~63 min after dispatch start). Per the
   round's poll-wait protocol these are reported ABSENT rather than waited on indefinitely; nothing
   about them is fabricated here.
2. **No two seats wrote the same report file; no header mismatches.** For all 60 reports, the seat
   ID in filename prefix equals the seat ID in the header line 1 and within the first five lines;
   `duplicate prefixes = {}`, `line1 mismatches = []`, `first5 mismatches = []`,
   `unexpected prefixes = []`. Prefix/header consistency only — authorship of bytes cannot be proven
   from content.
3. **Exclusive paths hold.** Every report is a regular `.md` file directly under
   `.ufo/waves/round-95/seats/` (`find … -maxdepth 1 -name '*.md' -type f`); no seat wrote into
   another seat's namespace.
4. **All five producer artifact sets exist** (existence/size only; content is other seats' scope):
   - P1 `corpus/tools/map_obligations.py` 33,320 B, mtime 16:26:27, sha256 `d1c239cc…`
   - P2 `corpus/tools/map-obligations-contract.json` 2,955 B, mtime 16:27:02, sha256 `8173bb97…`;
     `corpus/tools/README.md` 14,082 B, mtime 16:28:26 (`grep -c "r95"` → 2 in the final state:
     line 99 residual pointer + line 103 addendum)
   - P3 `corpus/fixtures/r95-crossing-aftermath/` — `entities.json` 1,449 B, `relations.json` 139 B,
     `contradictions.json` 3 B, `sources.json` 1,225 B, `timeline.json` 1,254 B,
     `inspiration-note.md` 1,956 B, `source-excerpt.md` 640 B, `fictional-excerpts.md` 1,845 B
   - P4 `…/README.md` 4,070 B, `…/claim-excerpt-map.md` 8,563 B
   - P5 `corpus/knowledge/r95-aftermath-scope-note.md` 9,718 B, mtime 16:25:15, sha256 `f87ed42a…`
5. **Receipt finalized** at `.ufo/waves/round-95/receipt.json` by
   `python3 .ufo/waves/round-95/seats/V59-scratch/gen_receipt.py` (read-only audit + one write):
   61 seat entries with `seat`, `report_path`, `report_sha256`, and `agent_id: null` /
   `outcome: null` on every entry — the integrator fills agent IDs and outcomes from the AgentSwarm
   dispatch result after collection. No agent ID, dispatch ID, or served-backend echo is invented.
6. **Auxiliary artifacts (not reports):** `V31-debt.json` (top-level, V31 debt-ledger evidence),
   the scratch directories `V01,V04,V06,V16,V23,V32,V34,V37,V39,V40,V44,V52,V55,V59-scratch` plus
   shared `seats/scratch/{V14,V17,V19,V42,V54}`, and top-level `round-95/scratch/V20`. Recorded so
   the integrator can account for them; report counting used `seats/*.md` only.

### Header/collision audit — command and observed output

```sh
$ python3 - <<'EOF'
import glob, os
base = ".ufo/waves/round-95/seats"
files = sorted(glob.glob(base + "/*.md"))
print("count =", len(files))
dups = {}; mismatch1 = []; mismatch5 = []
for p in files:
    name = os.path.basename(p); seat = name.split("-", 1)[0]
    dups.setdefault(seat, []).append(name)
    txt = open(p, encoding="utf-8", errors="replace")
    lines = [next(txt, "") for _ in range(5)]
    if seat not in lines[0].strip(): mismatch1.append((name, lines[0][:90]))
    if not any(seat in l for l in lines): mismatch5.append(name)
print("duplicate prefixes:", {k: v for k, v in dups.items() if len(v) > 1})
print("line1 mismatches:", mismatch1)
print("first5 mismatches:", mismatch5)
EOF
count = 60
duplicate prefixes: {}
line1 mismatches: []
first5 mismatches: []
```

Missing-seat check (same run, before this report existed):

```sh
$ present=$(find .ufo/waves/round-95/seats -maxdepth 1 -name '*.md' -type f -printf '%f\n' | sed 's/-.*//' | sort)
$ for s in P1 P2 P3 P4 P5 $(seq -f 'V%02g' 1 59); do echo "$present" | grep -qx "$s" || printf '%s ' "$s"; done
V09 V18 V33 V59
```

(`V59` is this seat, written after the audit; `V09`, `V18`, `V33` remain absent.)

## Bottom line

PASS — presence audit and receipt finalization completed: 61/64 reports collected (V09, V18, V33
absent and recorded, not fabricated), all exclusive paths and seat-ID headers clean, all five
producer artifact sets present, receipt finalized with real counts/missing lists and null
agent_id/outcome for L1 fill.

# V02 c1-markdown-tamper — round 99

- Seat: V02 c1-markdown-tamper (verifier, C1 prose-edit detectability). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`; HEAD during the round `337f0fa` (blocked-dispatch commit; S1 states the two owned files are identical at `4265df5` and `HEAD`). All commands used `python3`.
- Polled producer: S1. Report landed as `.ufo/waves/round-99/seats/S1-full-file-pins.md` (mtime 22:48:57, 11971 bytes). S1 does not publish sha256 of the owned files. This seat hashed them independently and verified those bytes.
- Verified bytes (unchanged from the matrix at 22:38:33 through the post-report re-run at 23:00:17 and a final check at 23:02:20):
  - `corpus/tools/dependency_freeze.py` sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (mtime 22:38:11, 29110 bytes)
  - `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (mtime 22:08:46, 25987 bytes)
  - r94 pin content digest `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef`; `payload_schema_version` 2; ten file digests (five JSON + five Markdown).
- Scratch (declared): `.ufo/waves/round-99/seats/V02-scratch/` (`poll.log`, `matrix-transcript.txt`, `runs/`, `runs-postreport/`, `probe-parse/`). This report. Leaf seat: no nested agents, no commits, no pushes, no network. No other path written.
- Axes for this seat: calibration (a one-word Markdown edit that the r98 pin ignored is now exit 2 `DIGEST-MISMATCH` naming the file); completeness (all five Markdown files, and inventory-clean edits of all five JSON tables, each named); evidence (quoted commands and stdout); live-tree integrity (scratch copies only).

## 0. Poll record (20 s cadence, 40 tries max; never verify a plan)

Opening snapshot 22:00:29, before any seat directory existed: tool `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`, contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` (r98 hashes). Full log: `.ufo/waves/round-99/seats/V02-scratch/poll.log`.

```
try 1  22:01:55 tool=c620324f543b (changed) contract=153ebc5b2092 s1=[none]
try 2  22:02:25 tool=65c1ae309385feed… contract unchanged
        (rglob false positive on V40-scratch/archive/**/S1.md discarded; not S1's report)
try 3  22:03:31 tool=1728ed892442c498… contract unchanged s1_reports=[none]
try 4  22:04:02 unchanged
try 5  22:04:43 contract=8f9c1f5316141b61 payload_schema present; pins still 5-file
try 6  22:07:32 pins10=False s1_reports=[none]
try 7  22:07:52 tool=6f81f8be19742372… (Markdown no longer JSON-parsed)
try 8–9 stable, pins10=False, no S1 report
try 10 22:08:52 contract=8c2561b043c25db7… pins10=True S1-scratch present, no report
try 11–19 22:09:12–22:23:08 stable, s1_reports=[none]
```

Cadence gap (disclosed, not a stall escape): between try 19 (22:23:08) and try 20 (22:44:37) this seat ran the scratch matrix instead of sleeping. During that gap the tool mtime moved to 22:38:11 (`6f81f8be…` → `fb9bb9ff…`). The matrix and the post-report re-run both used `fb9bb9ff…`. Contract stayed `8c2561b0…` from try 10 onward.

```
try 20–32 22:44:37–22:48:37 tool=fb9bb9ff… contract=8c2561b0… s1_reports=[none]
try 33 22:50:49 s1_reports=['S1-full-file-pins.md'] hashes still fb9bb9ff… / 8c2561b0…
```

Stopped at try 33. Report mtime 22:48:57, so it landed between try 32 and try 33. No all-reports poll (this seat's dependency is S1 only). No stall escape. Budget not exhausted.

Interim, not credited as the delivery: at 22:02 a scratch `--freeze` of an r94 copy against tool `65c1ae30…` (contract not yet re-frozen) exited 2 `FINDING MALFORMED-JSON: README.md: Expecting value: line 1 column 1 (char 0)` and did not write a pin. S1's report discloses the same failed attempt and says it was fixed before the delivered freeze. The matrix below is on the post-fix bytes only.

## 1. Clean control on the delivered bytes

Read-only verify of the live fixture (no write):

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing
(cwd=/home/vgpnk/Projects/shokunin/lore-shokunin)
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
exit=0
```

Same PASS, same digest, on a scratch mirror whose tool ROOT is the mirror (path-binding satisfied). Transcript: `V02-scratch/matrix-transcript.txt` section `scratch-clean`.

## 2. Before control — r98 pin does not see the same one-word edit

Scratch mirror `V02-scratch/runs/baseline-4265df5/` = `git show 4265df5:` of the tool and contract (sha256 `03d04365…` and `153ebc5b…`, matching the opening snapshot) plus a copy of live `r94-paired-crossing`. Unedited verify exited 0, digest `2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75`. Then one word in `fictional-excerpts.md` only: `unowned in the rain.` → `unowned in the mist.` (1 occurrence).

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/baseline-4265df5/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/baseline-4265df5/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
exit=0
```

Digest unchanged. The r98 five-file pin does not name `fictional-excerpts.md`. The prose edit is invisible to `dependency_freeze` before the r99 pin.

## 3. Five Markdown one-word edits — each named, exit 2

Each case is a fresh scratch mirror of the delivered tool, delivered contract, and live r94 fixture. One unique substring, one occurrence, then verify. First run 22:38:33 (`V02-scratch/runs/`). Post-report re-run 23:00:17 (`V02-scratch/runs-postreport/`) on the same hashes reproduced the same stdout, including the same observed digests. Quoted stdout is that shared observation. Commands below are the first-run argv (absolute). Post-report argv is the same shape under `runs-postreport/<filename>/`.

Edits (each count=1):

- `fictional-excerpts.md`: `unowned in the rain.` → `unowned in the mist.`
- `README.md`: `not an unrelated bible` → `not an distinct bible` (one word; the resulting phrase is ungrammatical and still one word)
- `claim-excerpt-map.md`: `separately labeled` → `independently labeled`
- `inspiration-note.md`: `## Parallel cited` → `## Adjacent cited`
- `source-excerpt.md`: `this interesting book` → `this notable book`

`fictional-excerpts.md`:

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-fictional-excerpts.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-fictional-excerpts.md/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest c16885525cc07a02e1d477e36c773b9aa8fa4e322be659b0fd69f81fc78a27ba != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> 99b90daf3df4207e3b6fa567a24885d35fcd748bdbfc3c6b7d4e977f26d897a9); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

`README.md`:

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-README.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-README.md/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest d3350806d2ec1dff7773ed87278f4b5cf714d484f9e8c8a73dc4d6a735322196 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: README.md (sha256 36796479658cc4eaa95ac50cd38713a934df56d3c430f10b1bab6211ff2a360a -> e59ea4ff6933b3b7fac103dd7c01794e00178f2d5c62641fd191ce9cdebcec36); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

`claim-excerpt-map.md`:

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-claim-excerpt-map.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-claim-excerpt-map.md/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest 4ec90f4110c4b1bc10c6c43e465f36ccf0b7c7d344791ddbb254140a3955c8e5 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: claim-excerpt-map.md (sha256 ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47 -> b68407745d344d0f6b750063f8ed823382760b6199ac6365750d23652e01000b); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

`inspiration-note.md`:

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-inspiration-note.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-inspiration-note.md/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest c026b433305e9d4654fd55d5b4e7ec889b07d22bfc5845c194d7d40a0440aebe != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> d81c3696cdb00adf0220b57a412242a670cd544dc38b54beb137d8e0d61fd3d1); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

`source-excerpt.md`:

```
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-source-excerpt.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V02-scratch/runs/tamper-source-excerpt.md/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest 3e894b2e67204da8428f2e4f22286420f5a66d768d307413327ddbfd35e81a67 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> cf55603bd9d5935b9418dbb2b73e9099cea6acaf8d9d977f55ee422fb51ca7f9); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

Each `changed:` clause names only that file. Inventory receipt stays 3/3, 2/2, 1/1. Finding id is `DIGEST-MISMATCH`, result `ERROR`, exit 2. The five Markdown files are the seat's required five edits.

## 4. JSON-table edits still named

Same mirror method. Edits are inventory-clean on purpose (description / statement / `source_id` / whitespace), so a semantic exit-1 finding would not hide the digest check. This seat did not re-test an endpoint or `depends_on` mutation; S1 states those still decide first at exit 1. Not claimed here.

- `entities.json`: `carrying` → `bearing` (1)
- `sources.json`: `fictional poem` → `fictional verse` (1)
- `relations.json`: `"source_id": "crossing-minute"` → `"source_id": "crossing-record"` (1; not `from`/`to`/`type`)
- `timeline.json`: `Aru carries the north lantern` → `Aru bears the north lantern` (1; description, not tick/entity/place)
- `contradictions.json`: the file is `[]` and contains no word. Edit was `[]` → `[ ]` (1). Still a pinned-file byte change.

```
entities.json exit=2
FINDING DIGEST-MISMATCH: … changed: entities.json (sha256 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b -> 0eca93944846df24a8c90eb27606c99a0f374d27d2eb86c15341991e9921601c); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

sources.json exit=2
FINDING DIGEST-MISMATCH: … changed: sources.json (sha256 2b627c4c166edf44e1e54bb006964a00e267ab4a4ce0b7b7c0681a0d9f0355d5 -> 8463bf853528ac2585716a27a0e82cf01af1a0b3276f1156d36a9ae778ff2ff4); …

relations.json exit=2
FINDING DIGEST-MISMATCH: … changed: relations.json (sha256 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 -> c56af879d0fe5642defb7c371be9c1fe24c7cdf0d22572324c3405418a8cbaf0); …

timeline.json exit=2
FINDING DIGEST-MISMATCH: … changed: timeline.json (sha256 f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c -> 1be105e53b143382a06615b6999b02f03399e6dbd5de263660d09b38049ca07f); …

contradictions.json exit=2
FINDING DIGEST-MISMATCH: … changed: contradictions.json (sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 -> 25f881c3c71d326fd737fc9e76c6ce2f03de67a957d97a2cef3282ec2d0cc80f); …
```

Full stdout for each is in `matrix-transcript.txt` and `runs-postreport/summary.txt`. All five name the edited file only, exit 2, `RESULT ERROR`. Post-report re-run matched.

## 5. Live tree untouched

Hashes of the tool, the contract, and all ten r94 files were identical before the matrix (22:38:33), after it (22:38:34), and at 23:02:20 (`ALL_SAME True`). Live `fictional-excerpts.md` remained `585f4d07…` after the post-report re-run. Edits exist only under `V02-scratch/`.

## 6. Bounds (not failures of this seat's claim)

- Edit-detectable, not semantics-provable. The before control shows the r98 freeze ignored the word change. This seat did not run `support_check`, `map_obligations`, or `check_bible` on the tampered copies. S1 reports an anchored "depends on" removal is already exit 1 on `support_check` before the pin upgrade, and a non-anchor excerpt edit was green on all four gates before and `DIGEST-MISMATCH` after. Those other-gate rows were not replayed here.
- `contradictions.json` has no word to replace; the named result is a whitespace edit.
- Chain 6/6 and self-test 17→18 were not this seat's checks and were not run.
- An intermediate tool (`65c1ae30…`) failed closed on Markdown-as-JSON. That is not the delivered behavior. Delivered clean verify is PASS; delivered Markdown tamper is `DIGEST-MISMATCH`, not `MALFORMED-JSON`.

PASS — one-word edits of all five r94 Markdown files, and inventory-clean edits of all five JSON tables, each exit 2 DIGEST-MISMATCH naming that file on the delivered tool/contract; the same excerpt edit is invisible to the r98 freeze; live tree untouched.

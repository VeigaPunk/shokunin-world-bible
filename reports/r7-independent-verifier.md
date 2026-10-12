# Round 7 independent verifier — raw fixture CLI replay

## Scope and method

Non-author replay of all 14 active fixture directories, with no checker or fixture edits. I read the raw fixture JSON directly and ran these exact command forms from the repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
python3 /tmp/lore-r7-baseline-checker.py .shokunin/lore/corpus/fixtures/<old-case>
```

The baseline script was extracted read-only from commit `4f6eaba9c7f4807b4a28ba9883af5bf479252294` using:

```sh
git show 4f6eaba9c7f4807b4a28ba9883af5bf479252294:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/lore-r7-baseline-checker.py
```

Its SHA-256 was `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78`. For each old-case execution, I compared stdout bytes plus the appended process exit code marker (`__EXIT:<n>`) against the baseline execution; all 12 matched byte-for-byte. No text normalization was applied.

## Existing cases — active versus baseline

| Case | Exit | Stdout bytes equal baseline | Bytes | SHA-256(stdout) |
|---|---:|:---:|---:|---|
| `ally-one-way` | 1 | yes | 155 | `98275e2d5d5ddb6b49ec7320adaad9608d4bc5a46ec14a3c1cf3998f9c65ea12` |
| `ally-reciprocal` | 0 | yes | 61 | `2850c4d154b4008925e04366b30efd42544f5959d4555460df6457f8966725b7` |
| `consistent` | 0 | yes | 61 | `2850c4d154b4008925e04366b30efd42544f5959d4555460df6457f8966725b7` |
| `contradictions` | 1 | yes | 282 | `d9ab246772a7cc52b6631083bd4e2ef26cf64c5e446667d65799f0ba7d25f682` |
| `contradictions-ledger-malformed` | 1 | yes | 380 | `d7d0e2bde3bda847e5902864b75cccadba2f91677d07cc1de2ace555010dfe55` |
| `item-chain-broken` | 1 | yes | 138 | `2ed8e085947384a3076996a061ce57cc312632011ba06f0cd91ab9f8c9119989` |
| `item-chain-valid` | 0 | yes | 61 | `2850c4d154b4008925e04366b30efd42544f5959d4555460df6457f8966725b7` |
| `r5-invalid-citation` | 1 | yes | 109 | `1c4d3e1236527a4a3eaf5a895004beff359e4e205fbb7a76181c7712fffb74db` |
| `r5-invalid-json` | 1 | yes | 160 | `9040b8d72429ac9d9588856be8e689326cebe3080b41cf0bf1e679aead817e66` |
| `r5-missing-file` | 1 | yes | 190 | `e6b1c9e1b5ed7218c6aadda79d4ce816be5459d346791b4a1bdc87ec96b0d00d` |
| `r5-row-shape` | 1 | yes | 80 | `d64fa6c79f9e067d5d0069500f19679011d5c465b1eebad7b19aa5d414256d3f` |
| `r5-wrong-top-level` | 1 | yes | 81 | `6487cca246e4536f8d5e1640714c6011f7b8d4645329fba9a212eb05d2366ddf` |

The `contradictions` CLI exits 1 (one process failure) while printing its seeded three violations. Other exit-1 cases likewise indicate checker findings/invalid input, not a crash classification.

## New round-7 cases — active checker actual output

### `r7-ally-reverse-ambiguous`
```text
VIOLATION: sources[2].id: duplicate sources id 'harbor-compact'
VIOLATION: relations[1].source_id: ambiguous in-world source 'harbor-compact'
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
3 violation(s); no canon changed

__EXIT:1
```
### `r7-item-ambiguous`
```text
VIOLATION: sources[2].id: duplicate sources id 'archive-ledger'
VIOLATION: entities[1].first_appearance: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[1].claims[0].source_id: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[2].first_appearance: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[2].claims[0].source_id: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[3].provenance[1].source_id: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[3].provenance[2].source_id: ambiguous in-world source 'archive-ledger'
7 violation(s); no canon changed

__EXIT:1
```

The alliance case demonstrates the expected local ambiguous reverse-edge reference and the absence of a uniquely sourced reciprocal; the ambiguous edge does not satisfy reciprocity. The item case reports ambiguous citation locations at first appearances, claims, and provenance entries. Neither output claims source-text support or canon truth. These were the two round-7 directories present at replay.

## Integrity

I SHA-256 hashed the active checker and every `*.json` recursively under `corpus/fixtures/` immediately before and after all 14 CLI executions. Checker before/after was `99e68a27eb8caeea741bde10935ae7b54a318d6ea61ee522d4e821a67a9772f6` / `99e68a27eb8caeea741bde10935ae7b54a318d6ea61ee522d4e821a67a9772f6` (equal). Fixture JSON inventory was 69 files; before/after path-to-hash maps were exactly equal (`True`). The full captured map follows; every listed hash applies both before and after replay.

- Checker: `.shokunin/lore/corpus/fixtures/check_bible.py` — `99e68a27eb8caeea741bde10935ae7b54a318d6ea61ee522d4e821a67a9772f6`
- Baseline checker temp copy (not part of fixture scope): `/tmp/lore-r7-baseline-checker.py` — `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78`
- Fixture JSON manifest:
- `ally-one-way/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `ally-one-way/entities.json`: `317ff21e03e7038eba6e414a97a37f1c2adfd8f0e98b4e3eba864120609f7c45`
- `ally-one-way/relations.json`: `933839488045e6b6bda4b885a5766d90a4d6034c4f7107059ed83798580f2726`
- `ally-one-way/sources.json`: `ded882756d6cfaf4bb7f542e27c0030b0af10312a25b89301636cacedd4214d1`
- `ally-one-way/timeline.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `ally-reciprocal/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `ally-reciprocal/entities.json`: `317ff21e03e7038eba6e414a97a37f1c2adfd8f0e98b4e3eba864120609f7c45`
- `ally-reciprocal/relations.json`: `7882d138cb8178c0d674ee8d3ea64954eef5ce9428a0c2f7efbb6017a71e81c2`
- `ally-reciprocal/sources.json`: `ded882756d6cfaf4bb7f542e27c0030b0af10312a25b89301636cacedd4214d1`
- `ally-reciprocal/timeline.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `consistent/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `consistent/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `consistent/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `consistent/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `consistent/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `contradictions/contradictions.json`: `131890ede960716bcc46da5e0afa1a4a8e10b52300e3f10beafda4acd79c5621`
- `contradictions/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `contradictions/relations.json`: `5ba89505e83b4d8c999619f253bc8c8c2bffbc15073836f6eab009cb56964a19`
- `contradictions/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `contradictions/timeline.json`: `0050252d49dc0596b110c2d2dff6f03e87f3ba0cb18072162db4743f8d834b50`
- `contradictions-ledger-malformed/contradictions.json`: `3f479df414f98274e75811657051c1dacb9c905dedc0b4d51ebf4282f8950a35`
- `contradictions-ledger-malformed/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `contradictions-ledger-malformed/relations.json`: `5ba89505e83b4d8c999619f253bc8c8c2bffbc15073836f6eab009cb56964a19`
- `contradictions-ledger-malformed/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `contradictions-ledger-malformed/timeline.json`: `0050252d49dc0596b110c2d2dff6f03e87f3ba0cb18072162db4743f8d834b50`
- `item-chain-broken/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `item-chain-broken/entities.json`: `65374c8cafc05330ad39e05a9aff492ba13875a8994460b936b9e979b0757a74`
- `item-chain-broken/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `item-chain-broken/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `item-chain-broken/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `item-chain-valid/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `item-chain-valid/entities.json`: `fc1d000f9a17ead19e0f541fffd9752710dcfc7a12d73ec9cbc2a78db5ced637`
- `item-chain-valid/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `item-chain-valid/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `item-chain-valid/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `r5-invalid-citation/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `r5-invalid-citation/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `r5-invalid-citation/relations.json`: `004fde3fbea3f0410a15e358ba4f8b86b402b92879bb0a35c7f15f9a04e492b0`
- `r5-invalid-citation/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `r5-invalid-citation/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `r5-invalid-json/contradictions.json`: `a6fb08fda1acb957b6116bd37811a1fe41a01611c0631edbf786d6889a27a55c`
- `r5-invalid-json/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `r5-invalid-json/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `r5-invalid-json/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `r5-invalid-json/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `r5-missing-file/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `r5-missing-file/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `r5-missing-file/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `r5-missing-file/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `r5-row-shape/contradictions.json`: `3fd749edd9d66aefcae32cac2b69026e4f11f37edd763160d42db7945dee8c32`
- `r5-row-shape/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `r5-row-shape/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `r5-row-shape/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `r5-row-shape/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `r5-wrong-top-level/contradictions.json`: `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`
- `r5-wrong-top-level/entities.json`: `b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac`
- `r5-wrong-top-level/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `r5-wrong-top-level/sources.json`: `644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4`
- `r5-wrong-top-level/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`
- `r7-ally-reverse-ambiguous/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `r7-ally-reverse-ambiguous/entities.json`: `69fca014657e5eb9c162485684f94a38ca4a59c36c136c8a4664b2b386996e05`
- `r7-ally-reverse-ambiguous/relations.json`: `04251734848cb251b87a4870df24f6c1743817c37a5e5989c3ec19bcd2e2f785`
- `r7-ally-reverse-ambiguous/sources.json`: `f44297d16ecf26b6ae5fe54e954b82ce565087c662c2b83cc44c6443323eddee`
- `r7-ally-reverse-ambiguous/timeline.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `r7-item-ambiguous/contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `r7-item-ambiguous/entities.json`: `fc1d000f9a17ead19e0f541fffd9752710dcfc7a12d73ec9cbc2a78db5ced637`
- `r7-item-ambiguous/relations.json`: `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `r7-item-ambiguous/sources.json`: `d64265e5c38eb876dcae5a7a1e387f55dc51a19ead52c67f7bb04ca29835bf26`
- `r7-item-ambiguous/timeline.json`: `2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968`

No `__pycache__` or other generated files are included in this integrity scope. No checker or fixture files were modified by this replay. The only repository write is this report.

## Limits

This verifies repeatable CLI output and input/checker byte integrity for the active cases, not exhaustive fixture behavior, source-text validity, citation support, or canon truth. The baseline comparison covers the twelve pre-existing active cases only; the round-7 cases intentionally have no old-output equality claim. Standard output and process exit status were captured; stderr was not separately redirected into an independent stream. Temporary baseline extraction occurred outside the repository. The fixtures remain examples, not evidence about any real-world source.

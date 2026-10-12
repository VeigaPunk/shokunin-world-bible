# Round 16 second-correction verifier — independent replay

Role: non-author verification of the second correction only. I made no source, fixture, or checker edits. This report is the only file I wrote.

## Three hash and description checks

| Fixture / row | Current SHA-256 | Expected second-correction SHA-256 | First-correction SHA-256 reconstructed from current JSON |
|---|---|---|---|
| `r16-missing-place` / row 1 | `777d49be0f69ba0573e96f371c32eb61ca53c73be0b7f71c4259e36429355629` | same | `137cf89d8bca5b22abaf607d779fad4cd48e184ca8bcdec40e693c6a049aa735` |
| `r16-missing-first` / row 0 | `21f6826ee45f0201d388f90ee2574e4dc6f8be54f0924dee8e1fcbc1fb250449` | same | `f3324c998e4eff6369d256ded3f007adb0e013d81e55e34102366bbea7a6c55a` |
| `r16-mixed-three` / row 1 | `a8c64d562aa2367c5bec5d0e76d0afdf7c9821c0a00528b55ba5e42b947e7027` | same | `1306b1ce1469448bef4f56e98608543d89a360d63c3c1ba14147928779108345` |

All three current hashes match `r16-correction.md`'s second-correction hashes. To independently test the first-correction hash values, I loaded each current JSON, restored only the first-correction description recorded in `r16-correction.md`, serialized with the file's existing JSON indentation/UTF-8/newline format, and recomputed SHA-256. All three reconstructed hashes match the recorded first-correction values (which `r16-correction-verifier.md` independently verified against then-current bytes). The current changed-row descriptions exactly read `Fixture input: Mira's place is unspecified at tick 7.`

Parsed JSON comparison confirms the sole difference between the first-correction representation and the current representation is the targeted row's `description`. Each targeted row retains `place_id: "unlisted"`, its original event ID, tick, actor ID, dependencies, and `source_id: "courier-log"`; all other rows/fields are unchanged. Thus this verifies a description-only second correction, not a change to source attribution or place identity.

## CLI replay and integrity

Replayed current `check_bible.py` against all **33** current fixture directories, capturing exit status, stdout, and stderr. All **33/33** exactly match the saved CLI transcripts under `corpus/live/runs/20261012T182817Z/`, including the four round-16 fixtures. The replay uses the same repository-relative CLI paths as the transcripts (important for the missing-file fixture's diagnostic path).

Before and after replay, SHA-256 maps were equal for the checker and all current fixture JSON: **165/165 files stable** (the checker plus 164 JSON files). Checker SHA-256: `bf2061b5c6f4e5f67f6c6f8dfbe31b0141c9541e259fe4ddf333aebef92b19b6`.

Extracted baseline checker `3995486def3c9fceb95449362f6e8dab8cc130f7` and replayed it and the current checker against all **29 baseline fixture directories**. Exit status, stdout, and stderr matched for **29/29**. Additionally, all **144 JSON paths** present in the baseline fixture tree have byte-identical current contents. The four new round-16 fixtures are not baseline fixtures; baseline comparison therefore says nothing about their pre-correction bytes.

## Limits

- The hash reconstruction verifies the reported first-correction bytes only under the JSON formatting preserved by the current files; it is not a recovered historical artifact. It is corroborative alongside the independent first-correction verifier.
- CLI transcript agreement establishes reproducibility, not source-text truth or canon. The description is explicitly fixture-input-scoped; this check makes no claim about what the cited `courier-log` says or what place `unlisted` denotes.
- No source, fixture, or checker files were changed. No commit was made.

# Round 16 correction record — before fresh review

The initial axis adjudicator rejected the submission because the prose of three `unlisted` place references asserted known Harbor/Tower locations. Only those description strings were edited; `place_id`, event IDs, ticks, actor IDs, citations, dependencies, other JSON rows and checker were not changed. This is an input calibration correction, not retroactive alteration of the first verdict.

| Fixture / row | Old description | New description | SHA-256 old → new `timeline.json` |
|---|---|---|---|
| `r16-missing-place` row 1 | A separate record places Mira at North Tower at tick 7. | A separate record uses unresolved place ID unlisted for Mira at tick 7. | `d202a679aae9307be3e8c389b4adf710eac660d8413eb328d036a55de6aa6014` → `137cf89d8bca5b22abaf607d779fad4cd48e184ca8bcdec40e693c6a049aa735` |
| `r16-missing-first` row 0 | A record places Mira at Lantern Harbor at tick 7. | A record uses unresolved place ID unlisted for Mira at tick 7. | `afe07bff983d35f40305581a0735cb8c7da3e5f991d662a25d58f5f0c0877b2a` → `f3324c998e4eff6369d256ded3f007adb0e013d81e55e34102366bbea7a6c55a` |
| `r16-mixed-three` row 1 | A separate record places Mira at North Tower at tick 7. | A separate record uses unresolved place ID unlisted for Mira at tick 7. | `bb264249ff50c48417bc6b5e37e67596850641bb07c86b3a5962a9312d86b3a5` → `1306b1ce1469448bef4f56e98608543d89a360d63c3c1ba14147928779108345` |

The new description identifies `unlisted` as an unresolved input place ID, not a fictional named place attested by the source. Source-ID uniqueness alone does not establish textual support or canon. Fresh non-author verification and readjudication are still required; no axis improvement is claimed here.

## Second correction after first non-author review

The first correction reviewer found “record uses” could imply the cited `courier-log` text supplies the unresolved key. The three descriptions below now expressly describe fixture input, not an in-world record; no other field or checker changed. The prior correction and its rejected review remain above.

| Fixture / row | First-correction wording | Second-correction wording | SHA-256 first → second `timeline.json` |
|---|---|---|---|
| `r16-missing-place` row 1 | A separate record uses unresolved place ID unlisted for Mira at tick 7. | Fixture input: Mira's place is unspecified at tick 7. | `137cf89d8bca5b22abaf607d779fad4cd48e184ca8bcdec40e693c6a049aa735` → `777d49be0f69ba0573e96f371c32eb61ca53c73be0b7f71c4259e36429355629` |
| `r16-missing-first` row 0 | A record uses unresolved place ID unlisted for Mira at tick 7. | Fixture input: Mira's place is unspecified at tick 7. | `f3324c998e4eff6369d256ded3f007adb0e013d81e55e34102366bbea7a6c55a` → `21f6826ee45f0201d388f90ee2574e4dc6f8be54f0924dee8e1fcbc1fb250449` |
| `r16-mixed-three` row 1 | A separate record uses unresolved place ID unlisted for Mira at tick 7. | Fixture input: Mira's place is unspecified at tick 7. | `1306b1ce1469448bef4f56e98608543d89a360d63c3c1ba14147928779108345` → `a8c64d562aa2367c5bec5d0e76d0afdf7c9821c0a00528b55ba5e42b947e7027` |

This is a prospective correction record, not an axis verdict.

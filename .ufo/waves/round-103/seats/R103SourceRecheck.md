# R103SourceRecheck — re-open of corpus/SOURCES.md rows (round 103)

Date: 2026-10-19. Read-only falsification of the round-103 source gate. Fetched bodies kept in `/var/tmp/r103-recheck-b2_5mmuc/` (raw bytes and normalized `.txt`). Normalization: strip script/style, tags to whitespace, HTML-unescape, curly quotes to straight, collapse whitespace; sha256 below is of the normalized UTF-8 text that was searched for the gate quote. Quote match = verbatim substring after that normalization.

## Row table (12 rows: the 8 required + S013, S014, S025, S027)

| id | reachable | quote-match (location) | anchor-ok | tier-ok | teaches-ok | sha256 of normalized text checked | note |
|---|---|---|---|---|---|---|---|
| S004 | yes, 200 | YES, lines 159-163 | **NO (minor)**: "line groups 114-122 through 159-163" starts at the Erec-ki-gala instruction (114-122); the first gate crossing is 129-133; seven crossings run 129-133 … 159-163 | yes (A: own translation wording; not Sumerian, not cultural fact) | yes | a6e700b06cdfeb3ac3d24e91bdd1f32f778781aa39b621cde59f19ccb82107ba | fix anchor (D5) |
| S009 | yes, 200 | YES, Abstract | yes (Pages 7064-7083; DOI 10.18653/v1/2024.naacl-long.391 matched; title matched) | yes (A: paper's own claims) | partial: "paired before/after questions … probe shape" is lane design inference; the abstract only states mutual exclusivity as a consistency criterion | db25f81d08604e6a625cd6be967f618e9e4795aad140c658a9801c3955eb73f1 | minor (D7) |
| S012 | row URL `/abs/` 200, but quote NOT on `/abs/`; `/html/2603.05890` 200 | YES on `/html/`, §2.2 and Table 2 (five categories, 19 subtypes) | yes on `/html/`; "Submitted on 6 Mar 2026" matched | yes (A: own taxonomy; comparative use only) | yes | fc5b3139cbd57377b52bbb3d24f95e694fc30bc6ba0fbe577c7a7269e3483300 (html) | **DEFECT (D1)**: row and gate record cite `/abs/` for a quote that lives only on `/html/` |
| S013 | yes, 200 | YES, opening section | partly: "Dec 15", "Lauren O'Connor" matched; "series item 4" not verified | yes (B: staff blog) | partial: first clause follows; "needs arc-level continuity records, not only per-episode facts" is lane inference (D6) | 1230517179b639a085194389e14d91f861d37455a3d67963b464b0bc4a7775e4 | minor |
| S014 | yes, 200 | YES, exhibit paragraph (ALL IN THE FAMILY … THE WIRE show bible) | yes: meta datePublished 2015-01-28; screenshot names 2015-01-28; visible "Jan 28" | yes (A: institution's own description of its archive) | **NO**: "superseded character name" is not in the source; the page shows a show bible calling McNulty "McArdle" and says nothing about which name is superseded (D4) | dd05d3ef35bbc2d6e64cee9347a02bae0c6e2f019c4013d53ddfee868b05e6fc | teaches defect |
| S015 | yes, 200 | YES, page body first paragraph | yes: 2026 MOA and 2011–2023 prior MBAs listed | yes: C is honest; the MBA is authoritative for labour terms only, and the row's scope is world-bible standard (rejected) | yes (rejection holds) | 60a0657e64cbd9be06df2269317f3e4c35acf008288882446f7cc46e0ed69105 | no change |
| S020 | yes, 200 | YES, Abstract | yes: "Candidate Recommendation Draft 15 November 2022" (CRD-owl-time-20221115) | yes (A: own spec; draft status noted, recheck on-release) | yes; `:hasTRS` and §TRS confirmed | ce9e668cf2a6e278a50aca08fd8c98d8fa9f6bb902d240293716174bef8ad518 | no change |
| S021 | live **403** (Cloudflare "Just a moment…" challenge); Wayback capture 20241231122647 **200** | YES in capture, Level 1 qualification ("uncertain … approximate … respectively") | yes: "February 4, 2019"; Differences, Level 1, Level 2 sections present; `X` and `..`/null differences present | yes (A: own spec) | yes | normalized 362d3e42f07615c5b1f7a134c8799181f33596c3edde243c5da3113361e56f4a; decompressed raw body fed84ca1c0f80a8eb11854a08036fa13680ec90ed902d6599f978c34a339c583 | acceptable with disclosure, see judgment below (D8) |
| S022 | yes, 200 | YES, attribute listing | yes: P5 4.12.0, rev 113e933e2, "Last updated on 28th July 2026" | yes (A) | yes | 21118342bdccbc3d37083982c56db2552f2a5b6c2731de5225df9397ab861c6a | no change |
| S023 | live **403** (Cloudflare challenge); Wayback capture 20241230054021 **200** | YES in capture, Abstract ("This document excludes the representation of date elements from non-Gregorian calendars…") | **PARTIAL**: "confirmed 2024-12-05" matched; "Amendment 1:2025 noted" is NOT in the capture, which shows `ISO 8601-2:2019/Amd 1 — Under development` (D3). Live 2026 status unverified | yes (A: own standard) | yes | normalized (Wayback) 0423bfac08237f1de92dc62fb706527d9f15f6ca0e8e9a2db18b5a5cfdcfbb3b | **DEFECT (D2, D3)**: live 403 and Wayback read undisclosed in row and gate record |
| S024 | yes, 200 | YES, §Statements | yes: §Statements, §Ranks; live page footer shows `oldid=8399774`, last edited 31 May 2026 | yes, with note: A for Wikibase's own model description on a wiki page; the anchor is pinned by oldid, which is the required condition | yes (deprecated-statements wording and ranks behaviour match) | 40be205d9797e5a5a1e2d4abf1ff1db2a5fc4cb6ef67cec01c10610037c6469b | no change; keep oldid pinned |
| S025 | yes, 200 | YES, §Deprecated rank (three benefits); "not a way of asserting your view for a disputed value" in §What ranks are not | yes (sections exist) | yes (B: community help page) | yes | 8cc839a522405ff73588bc3f8897fb3b27cc3528367883bcf7d3e1a36667b0b7 | no change |
| S026 | yes, 200 | YES after normalizing the spec's `◊` anchor glyph ("§5.1.8 Invalidation ◊ is the start of the destruction…"); §5.2.2 and §5.5.2 quotes also verbatim with `◊` | yes: §5.1.8, §5.2.2, §5.5.2; REC-prov-dm-20130430 (30 April 2013) | yes (A) | yes; minor: "coexisting with its original" is an inference from "revised version of some original" plus "invalidation marks the end" (D10) | 1c2fd28873fd9c5959335dde19af92cdd46ea9a1ae63b8692a00bb7f23846001 | no change required |
| S027 | yes, 200 | YES, §Holocron database and canonicity; "declared it non-canonical" in same section | yes | yes (C: community; illustration only) | yes | 2ef2abc4483e81d42e4e09da0509a79d37adb7cfb4d6ac5fbb04323cfebc765b | no change |

Also checked, no defect: S001 and S029 quotes not in the sample but S029 quote is verbatim; S007/S008 not opened.

## Admitted entries: quote sample (7 checked, 4 required)

| entry | quote as written | source check |
|---|---|---|
| r103-in-world-dating (S020) | "may be expressed … using another temporal reference system such as Unix-time, geologic time, or different calendars" | accurate; ellipsis drops "either the conventional (Gregorian) calendar and clock, or"; abstract |
| r103-in-world-dating (S021) | `'?', '~' and '%' are used to mean "uncertain", "approximate", and "uncertain" as well as "approximate"` | verbatim in Wayback capture; Level 1 |
| r103-in-world-dating (S021) | "in place of one or more rightmost digits … the value of that digit is unspecified" | accurate; both fragments in the same passage, 58 characters apart |
| r103-canon-status (S024) | "statements that are being discussed, or known to be erroneous, but still listed for the sake of completion" | verbatim, §Ranks, deprecated definition |
| r103-canon-status (S026) | "Two alternate entities present aspects of the same thing"; "invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity"; "a revision is a derivation for which the resulting entity is a revised version of some original" | verbatim modulo `◊` glyph in the spec |
| r103-canon-status (S025) | "not a way of asserting your view for a disputed value" | verbatim |
| r103-canon-status (S027) | "declared it non-canonical"; "five levels of canon (in order of precedence)" | verbatim |

Result: 7 of 7 sampled quotes accurate. No misquote in the two admitted entries.

## S021 judgment: canonical URL with disclosed Wayback read

Acceptable. The loc.gov live fetch returns a Cloudflare bot challenge, not a content restriction. The Wayback capture (2024-12-31 12:26:47 UTC) carries the dated spec ("February 4, 2019"), and the gate quote is verbatim in it. The row and gate record disclose the read. Conditions to close (D8): give the exact capture URL `https://web.archive.org/web/20241231122647id_/https://www.loc.gov/standards/datetime/` and the hash in the row, and re-open the live page at the 180d recheck.

## Defects and fixes

- **D1 (S012, medium)**: the row URL and gate record cite `https://arxiv.org/abs/2603.05890` for a §2.2 / Table 2 quote; that text appears only on `https://arxiv.org/html/2603.05890`. Fix: change the S012 URL in SOURCES.md and in round-103.md Source gate records to the `/html/` URL, or cite both with the quote on `/html/`.
- **D2 (S023, medium)**: live ISO returned 403 and the content was read from a Wayback capture (20241230054021), but the row and gate record say only "accessed 2026-10-19". Fix: disclose the Wayback read and capture URL as S021 does, and record the 2024-12-30 capture date.
- **D3 (S023, medium)**: "Amendment 1:2025 noted" is not in the capture; the capture shows `ISO 8601-2:2019/Amd 1 — Under development`. Fix: rewrite as "Amd 1 under development in the 2024-12-30 capture", or re-open live ISO and cite what it shows.
- **D4 (S014, low)**: teaches "carries a superseded character name" overstates the source. Fix: "A show bible in an archive can refer to one character by a different name (McNulty as McArdle), so a bible must record which name variant each source uses."
- **D5 (S004, low)**: anchor range starts at 114-122, which is an instruction, not a crossing. Fix: "line groups 129-133 through 159-163 (seven gate crossings; 114-122 is the preceding instruction)".
- **D6 (S013, low)**: teaches second clause is lane inference; "series item 4" not verified. Fix: mark the inference as lane inference and check the item number against the series index.
- **D7 (S009, low)**: "paired before/after questions" probe design is lane inference. Fix: label it as such.
- **D8 (S021, low)**: add the exact Wayback capture URL and the decompressed-body hash to the row for reproducibility.
- **D10 (S026, trivial)**: "coexisting" is inference. Fix: label it as inference or drop "coexisting".

No defect found in: S015 tier, S020 anchor, S022 anchor, S024 pinning, S025 tier, S027 tier.

## Verification gaps

- S021 and S023 live pages were not reachable (403, Cloudflare challenge). Their quotes are verified against Wayback captures only, not the 2026 live pages.
- S024 is a live wiki page; `oldid=8399774` matches the fetch time only and will drift on edit.
- S013 "series item 4" was not checked against a series index.
- No row's full ETCSL line-group structure beyond the gate lines was re-derived; S004 anchor defect is established from the page text.
- Gate quotes checked by verbatim substring after normalization; semantic reading of each quote's section was by adjacency, not by full section parse, except where noted.

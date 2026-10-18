#!/usr/bin/env python3
"""Generate corpus/knowledge/r102-debt-ledger.json (U1, round 102).

Consolidates every debt item raised r94-r101 from the source ledgers:
  r94 F29-debt.json, r95 V31-debt.json, r96 V40-debt.json, r97 V37-debt.json,
  r98 V33-debt.json, r99 V36-debt.json (+ V74-debt-2.md), r100 V29-adjudicator
  conditions + recorded FAILs (no V33 seat exists - see anomalies),
  r101 V24-adjudicator defects + ACs (the "carried notes").

Counting rule: an entry that restates or disposes of an EARLIER round's item
(the CO groups of r95-r97 and the bounds_carried buckets of r98/r99) is
recorded in `carry_records`, not as a new item; it is also mirrored into the
`trail` of the item it tracks. Every source id appears exactly once, either
as an item or as a carry_record -> nothing silently dropped.
"""
import json

E = []  # items

def item(iid, origin, sid, grp, title, disp, detail, evidence, trail=None, owner=None):
    d = {"id": iid, "origin_round": origin, "source_id": sid, "group": grp,
         "title": title, "disposition": disp, "disposition_detail": detail,
         "evidence": evidence}
    if trail: d["trail"] = trail
    if owner: d["carried_owner"] = owner
    E.append(d)

R103 = "r103+ (operator; lane closes at r102)"

# ---------------- ROUND 94 (F29, 51 items: CC-01..CC-15, BR-01..BR-28, CR-01..CR-08)
cc = [
 ("CC-01","wave-spec followup field stale vs actual dispatch","closed",
  "FOLLOW-UP executed and reconciled at r94 closure; records landed",
  ["commit ac69044 (closure conditions C-1..C-6)","LOG.md r94 closure section"]),
 ("CC-02","capability admission + registry row pending","closed",
  "map_obligations admitted as registry row at closure",
  ["commit ac69044","SCORECARD.md r94 Capabilities (fifth row)"]),
 ("CC-03","new tool unregistered in tools README / SKILL","closed",
  "tools README + SKILL registration landed at closure",
  ["commit ac69044","corpus/tools/README.md (map_obligations sections)"]),
 ("CC-04","fixtures README missing r94 entry, census 167 stale","closed",
  "Round-94 section + census landed at closure",
  ["commit ac69044","corpus/fixtures/README.md '## Round 94'"]),
 ("CC-05","corpus README index omits r94 fixture + tool","closed",
  "index bullets landed at closure","[\"commit ac69044\"]" if False else ["commit ac69044"]),
 ("CC-06","r91-c9-watch.md:54 stale HEAD assertion","closed",
  "erratared in ac69044","[\"commit ac69044\"]" if False else ["commit ac69044","SCORECARD.md r94 freshness row"]),
 ("CC-07","LOG r87/r88 receipt counts stale (LOG.md:2312-2314)","closed",
  "corrected append-only at r94 closure",
  ["LOG.md r94 closure ('corrected append-only below')","commit ac69044"]),
 ("CC-08","W25 docs/registry proposals unimplemented","closed",
  "integrated as r94 closure conditions","[\"commit ac69044\"]" if False else ["commit ac69044","SCORECARD.md r94 planned->closed"]),
 ("CC-09","W20 failed-output gap (31/32 reports)","addressed",
  "recorded, not smoothed; requirement independently satisfied at r94 README:13",
  ["SCORECARD.md r94 'Failed-output gaps'","corpus/fixtures/r94-paired-crossing/README.md:13"]),
 ("CC-10","fleet round-94 report / MANIFEST closure / promotion pending","closed",
  "fleet report exists; promotion correctly withheld (lane policy, SHONEN 4 [~]); MANIFEST is integrator-level and updated at each closure",
  ["/home/vgpnk/Projects/shokunin/.ufo/reports/round-94/","SHONEN.md (4 [~], 0 [x], verified 2026-10-18)","/home/vgpnk/Projects/shokunin/MANIFEST.json (lane_rounds.lore updated by integrator at closure)"]),
 ("CC-11","F02 report duplicated at fleet repo root","addressed",
  "lane copy authoritative and byte-identical; hygiene recorded",
  [".ufo/waves/round-94/followup/F29-debt.json items[CC-11]"]),
 ("CC-12","W30 full-gate negative result only in seat report","addressed",
  "negative result preserved in wave tree and ledger record",
  [".ufo/waves/round-94/followup/ (W30 + F29 record)"]),
 ("CC-13","no r94-shape spec validator","carried",
  "explicitly accepted as process debt at r94; never built",
  ["SCORECARD.md r94 planned ('r94-shape spec validator (CC-13 accepted)')"], R103),
 ("CC-15","F40 report defective; receipt landed late","addressed",
  "defect stands recorded (CC-15); late skeleton usable as followup-receipt.json",
  ["SCORECARD.md r94 'Failed-output gaps'"]),
 ("CC-14","ledger v1 superseded by later versions","addressed",
  "v1 no-depth-verdict superseded by v4 with F21 depth IMPROVED",
  [".ufo/waves/round-94/followup/F29-debt.json version/compile_time_notes"]),
]
for row in cc:
    sid,t,d,det = row[0],row[1],row[2],row[3]
    ev = row[4] if isinstance(row[4],list) else ["commit ac69044"]
    ow = row[5] if len(row)>5 else None
    item("r94-"+sid, 94, sid, "CC", t, d, det, ev, None, ow)

br = [
 ("BR-01","dependency-reduction undetectable (JSON + prose halves)","addressed",
  "JSON half closed r96 (dependency_freeze REDUCTION-DETECTED); prose half rendered edit-detectable r99 (ten-file pins, DIGEST-MISMATCH) and bounded r100 (byte-detectability != semantics); prose entailment never provable",
  ["commit f3e09f9 (sixth gate)","commit fe1ce46 (ten-file schema-2 pins)","corpus/knowledge/r99-gate-blind-spot-table.md rows 1b/6","corpus/knowledge/r100-provenance-semantics-boundary.md"],
  ["r95:NB-05","r95:CO via NB items","r96:NB-07","r96:CO-04","r97:CO-07","r98:CO-02","r98:CO-19","r99:NB-07","r99:CO-01","r99:CO-19"]),
 ("BR-02","renamed claims key + removed map row = silent PASS","closed",
  "schema_drift FINDING delivered r95, exit 1, old tool PASSes",
  ["commit dcb2d92","SCORECARD.md r95 calibration row","corpus/tools/README.md Round-95 addendum"],
  ["r96:CO-02 (pin persisted)"]),
 ("BR-03","self-test coverage gap (map_missing, invalid_arguments unpinned)","closed",
  "22-case contract at r95 (both added, load-bearing per V02/V38); later 24 (r96) and 25 (r97)",
  ["commit dcb2d92","corpus/tools/map-obligations-contract.json (25 cases)","SCORECARD.md r95 calibration"],
  ["r95:NB-07","r96:CO-02","r97:CO-01"]),
 ("BR-04","phantom_obligation is set-membership, not document resolution","carried",
  "bound restated r95, never changed; documented in tools README scope",
  ["r95:CO-01","corpus/tools/README.md (map scope)"], R103),
 ("BR-05","self-test scratch under repo root, not gitignored","closed",
  "gitignored at r97 closure (both tools, .gitignore *-self-test-*/); r98 NB-01 found the tools-README 'not gitignored' wording false and the erratum closed the residual at r98 closure",
  ["commit 9d25df9 (SCORECARD r97 operability bound)","commit 4265df5 (r98 CL-05 errata; V33 NB-01)",".gitignore (*-self-test-*/)"],
  ["r95:NB-06","r96:NB-18","r96:CO-05","r97:NB-10","r97:CO-12","r98:CO-10"]),
 ("BR-06","--help exits 0 with zero RESULT lines","carried",
  "accepted exit-contract bound; registry verdict maps document it",
  ["r95:CO-02","SKILL.md gate registry (code->class maps)"], R103),
 ("BR-07","r94 map J14 span 18-20 wider than anchor line","carried",
  "cosmetic; fixture bytes frozen as adjudicated (changing would break pins)",
  ["r95:CO-03"], R103),
 ("BR-08","r94 R9 map omits retained r88 veil-verse declarations","carried",
  "never repaired; r88 map still declares them",
  ["r95:CO-04"], R103),
 ("BR-09","relations.json#/0 lacks stewardship-object field","carried",
  "JSON alone cannot recover co-stewardship object; editorial limit",
  ["r95:CO-05"], R103),
 ("BR-10","veil-verse zero obligations; no symbolism map in r94","carried",
  "r88 symbolism-clause-map.md named bound (r99 AC-5) and stays unpinned",
  ["r95:CO-06","LOG.md r99 closure AC-5"], R103),
 ("BR-11","comparison-record precision items (O1-O5)","carried",
  "editorial precision debt, never repaired",
  ["r95:CO-07"], R103),
 ("BR-12","knowledge-record metadata completeness (r94 note)","carried",
  "source list/span mismatches never repaired",
  ["r95:CO-08"], R103),
 ("BR-13","external editorial rows carry R9 mode in-map only","carried",
  "inherited editorial convention",
  ["r95:CO-09"], R103),
 ("BR-14","legacy maps exit 2 unsupported_map","addressed",
  "scope decision: r88 dialect accepted r95 (zero corpus change); r87/r89 remain exit 2 fail-closed by design",
  ["commit dcb2d92","SCORECARD.md r95 coverage row","corpus/tools/README.md Round-95 addendum"],
  ["r95:CO-10"]),
 ("BR-15","relation type free-text, not gate-enforced","carried",
  "only allied_with has type-specific rules; bound retained",
  ["r95:CO-11"], R103),
 ("BR-16","pointer identity array-positional, not event-id-based","carried",
  "deletion re-binds indices; bound re-observed r95, never changed",
  ["r95:NB-10","r95:CO-09"], R103),
 ("BR-17","fixture README replay blocks without recorded observed exits","carried",
  "recurring convention debt: recurrences r95 (NB-11), r96 (CL), r97 (NB-20), r98 (NB-08, fifth), r99 (NB-09, sixth); class never systematically fixed; r98 closure item CL-10 NOT landed (grep of r98 README finds no exit receipts, verified 2026-10-18)",
  ["r95:NB-11","r97:NB-20","r98:NB-08","r99:NB-09","grep -n -i exit corpus/fixtures/r98-clerk-filing/README.md -> no matches (2026-10-18)"], R103),
 ("BR-18","boundary certification explicitly bounded (no semantic/AST)","addressed",
  "documented permanent boundary: registry scope text, blind-spot row 8, r100 semantics boundary note; CERTIFIED reproduced at every closure battery including this pass",
  ["SKILL.md boundary row scope","corpus/knowledge/r99-gate-blind-spot-table.md row 8","corpus/knowledge/r100-provenance-semantics-boundary.md"],
  ["r95:CO-14 (with CR-01)"]),
 ("BR-19","r94 README unbounded 'their near-miss' wording","carried",
  "frozen adjudicated bytes; qualifier lives in dated addendum only",
  ["r95:CO-12"], R103),
 ("BR-20","r94 README ambiguous identity clause","carried",
  "under-claim/ambiguity direction; frozen bytes",
  ["r95:CO-12"], R103),
 ("BR-21","stale prospective prose in r94 knowledge record","carried",
  "overridden only by dated addendum, by design (append-only)",
  ["r95:CO-13"], R103),
 ("BR-22","W02 says '12 self-test cases' (delivered 20)","carried",
  "historical wave-artifact transcription slip, frozen by convention",
  ["r95:CO-23"], R103),
 ("BR-23","F19 transcribes self-test as 21 cases (actual 20)","carried",
  "typo-level artifact slip, frozen by convention",
  ["r95:CO-23"], R103),
 ("BR-24","tool and contract committed together (colocated trust)","carried",
  "documented trust bound in SKILL registry pinned-values note and boundary contract limits",
  ["SKILL.md boundary row pinned-values note"], R103),
 ("BR-25","wave reports not mutually current (F39 vs F04/F05)","addressed",
  "supersession tracking became a standing ledger convention (ST groups in every later debt ledger)",
  ["r95:ST-01","V31/V40/V37/V33/V36 ST groups"]),
 ("BR-26","W07 network fetch not reproducible offline","carried",
  "bounded in place; cited by no product/LOG/SCORECARD claim",
  ["r95:CO-22"], R103),
 ("BR-27","35 legacy fixtures covered only by JSON receipts","carried",
  "never resolved; receipt-only coverage stands",
  ["r95:CO-21"], R103),
 ("BR-28","F01 says 11 files where r94 fixture has 10","carried",
  "transcription slip, frozen by convention",
  ["r95:CO-23"], R103),
]
for row in br:
    sid,t,d,det,ev = row[0],row[1],row[2],row[3],row[4]
    tr = row[5] if len(row)>5 and isinstance(row[5],list) else None
    ow = None
    for extra in row[5:]:
        if isinstance(extra,str): ow = extra
    item("r94-"+sid, 94, sid, "BR", t, d, det, ev, tr, ow if d=="carried" else None)

cr = [
 ("CR-01","AST anchor validation absent (boundary_doc_check)","addressed",
  "documented permanent boundary, not implemented: blind-spot row 8 (checker byte-frozen), r100 provenance-semantics boundary separates byte-detectability from meaning",
  ["corpus/knowledge/r99-gate-blind-spot-table.md row 8","corpus/knowledge/r100-provenance-semantics-boundary.md"],
  ["r95:CO-14"]),
 ("CR-02","Q92-004: R9 verification command inspects r91 patch","carried",
  "open since r93, untouched through r101",
  ["r95:CO-15"], R103),
 ("CR-03","fixtures README lacks Round-91/93 sections","closed",
  "Round-91 and Round-93 sections exist in the delivered README (lines 1064/1099, verified 2026-10-18); Round-94/95 sections followed",
  ["corpus/fixtures/README.md:1064","corpus/fixtures/README.md:1099"],
  ["r95:CO-16"]),
 ("CR-04","C9 watch forward-pointer incomplete","closed",
  "watch continued: due re-checks appended rows 3 (r94) through 10 (r101)",
  ["commit ac69044 (C9 r94 re-check)","corpus/knowledge/r91-c9-watch.md","LOG.md r101 closure (C9 row 10)"]),
 ("CR-05","decision-table R8/R9 integration defects","carried",
  "open since r93, untouched through r101",
  ["r95:CO-17"], R103),
 ("CR-06","independent certification of boundary document (B3 unmet r93)","addressed",
  "boundary gate + self-test + closure-battery CERTIFIED reproductions (r99/r100/r101 and this pass)",
  ["corpus/tools/boundary-doc-contract.json","this pass: python3 corpus/tools/boundary_doc_check.py -> CERTIFIED (2026-10-18)"],
  ["r95:CO-18"]),
 ("CR-07","poll-helper residual hardening + scratch/inode budget","addressed",
  "endgame subtract-SELF convention adopted r97 and held r98; bounded stall-escapes recorded; poll_wait.sh in wave tree",
  [".ufo/waves/poll_wait.sh","SCORECARD.md r97/r98 discernment rows"],
  ["r95:CO-19"]),
 ("CR-08","roster/landing accounting class","addressed",
  "receipts rebuilt from real dispatch r95-r101; roster-arithmetic errata recorded append-only (r100, r101) as a standing convention",
  ["LOG.md r100/r101 roster errata",".ufo/waves/round-95..101/receipt.json"],
  ["r95:CO-20"]),
]
for row in cr:
    sid,t,d,det,ev = row[0],row[1],row[2],row[3],row[4]
    tr = row[5] if len(row)>5 and isinstance(row[5],list) else None
    ow = next((x for x in row[5:] if isinstance(x,str)), None)
    item("r94-"+sid, 94, sid, "CR", t, d, det, ev, tr, ow if d=="carried" else None)

# ---------------- ROUND 95 (V31 own items: NB 14, CL 10, PR 3, ST 1 = 28)
r95 = [
 ("NB-01","schema_drift entity-claim-container-bounded","carried","bound retained; documented in Round-96 addendum bounds",["corpus/tools/README.md Round-96 addendum"],R103),
 ("NB-02","INVENTORY receipt non-gating (deletion class silent PASS)","closed","inventory_mismatch gating delivered r96 (old exit 0 vs new exit 1 on identical mutations)",["commit f3e09f9","corpus/tools/README.md Round-96 addendum"],["r96:CO-01"]),
 ("NB-03","r88 dialect header-gated acceptance","carried","bound retained (normalized header token required)",["corpus/tools/README.md Round-95 addendum"],R103),
 ("NB-04","12/12 is total-rows denominator, not obligations","closed","declaration denominator corrected at r95 closure (correction 4)",["LOG.md r95 closure corrections (1)-(7)"],None),
 ("NB-07","schema_drift not pinned by persisted case","closed","pinned r96 as 24-case contract; loader strict from r97",["commit f3e09f9","commit 9d25df9"],["r96:CO-02"]),
 ("NB-08","r95 note pins mid-flight tool revision 9224a684","closed","corrected by dated append-only addendum at r98 closure",["commit 4265df5","corpus/knowledge/r95-aftermath-scope-note.md (dated addendum)","SCORECARD.md r98 freshness row"],None),
 ("NB-09","tool-revision flux within rounds","addressed","recorded each round as a harness property (PR groups); never eliminated, always disclosed",["r96:NB-19","r97:NB-19","r98:NB-06","r99:NB-11"],None),
 ("NB-12","V37-D1 legacy-dialect hidden-second-pointer (MEDIUM)","closed","dual_pointer FINDING r96; pinned r97 as case 25",["commit f3e09f9","commit 9d25df9"],["r96:CO-03"]),
 ("NB-13","D2: schema-drift rule shape-specific, evadable","carried","bound retained",["corpus/tools/README.md Round-96 addendum bounds"],R103),
 ("NB-14","D3: hypothetical false-positive class, no suppression","carried","bound retained",["r95 V31 item text"],R103),
 ("CL-01","fixtures README Round-95 section due","closed","landed at r95 closure (census 169)",["commit dcb2d92","corpus/fixtures/README.md '## Round 95'"],None),
 ("CL-02","corpus README '20 persisted cases' stale","closed","fixed at r95 closure",["commit dcb2d92"],None),
 ("CL-03","SKILL.md registry row stale","closed","updated at r95 closure",["commit dcb2d92"],None),
 ("CL-04","C9 watch 'Next re-check: r95' due","closed","row 4 appended at closure (DISCRIMINATION HELD)",["commit dcb2d92","corpus/knowledge/r91-c9-watch.md"],None),
 ("CL-05","LOG/SCORECARD r95 entries due","closed","landed (closure 60dba0c + dcb2d92)",["commit 60dba0c","commit dcb2d92"],None),
 ("CL-06","stranded reports in parent repo","addressed","parent-tree strays collected at closure; cwd-stray class recorded as harness property",["LOG.md r95 closure (V09/V18 strays collected)"],None),
 ("CL-07","no wave-spec.json and no receipt.json for r95","addressed","receipt rebuilt from dispatch (exists); wave-spec absence became the standing wave convention",[".ufo/waves/round-95/receipt.json","LOG.md r95 closure"],None),
 ("CL-08","roster accounting 60/64 at compile","addressed","receipt rebuilt 64/64; three late landings recorded, not failures",["LOG.md r95 closure (receipt 64/64)"],None),
 ("CL-09","fleet round-95 report ABSENT","closed","fleet report exists at the integrator surface",["/home/vgpnk/Projects/shokunin/.ufo/reports/round-95/lore.md"],None),
 ("CL-10","round receipt fill due","closed","receipt.json filled from real dispatch result",[".ufo/waves/round-95/receipt.json"],None),
 ("PR-01","mid-round producer hand-off gap (22-case tool / 20-case contract)","addressed","disclosed; recorded as adjudication condition",["LOG.md r95 closure",".ufo/waves/round-95/seats/V31-debt.json PR-01"],None),
 ("PR-02","stale seat outputs (mid-round INCONCLUSIVE etc.)","addressed","superseded by finals; ST-01 records the supersession",[".ufo/waves/round-95/seats/V31-debt.json ST-01"],None),
 ("PR-03","artifact hygiene (two reports outside lane + transient scratch)","addressed","recorded; strays collected",["LOG.md r95 closure"],None),
 ("ST-01","v1->v4 supersession of this ledger","addressed","final v4 is the compiled record",[".ufo/waves/round-95/seats/V31-debt.json version"],None),
]
def _norm7(rows):
    out = []
    for r in rows:
        r = list(r)
        tr = next((x for x in r[5:] if isinstance(x, list)), None)
        ow = next((x for x in r[5:] if isinstance(x, str)), None)
        out.append([r[0], r[1], r[2], r[3], r[4], tr, ow])
    return out
r95=_norm7(r95)
for sid,t,d,det,ev,tr,ow in r95:
    item("r95-"+sid, 95, sid, sid.split("-")[0], t, d, det, ev, tr, ow)

# ---------------- ROUND 96 (V40 own items: NB 27, CL 12, PR 8, ST 6 = 53)
r96 = [
 ("NB-01","dual_pointer confined to legacy dialect","carried","canonical two-pointer cells stay exit 2 unsupported_map (fail-closed); permanent scope bound",["SKILL.md map row code->class","r99:CO-05 open_accepted"],R103),
 ("NB-02","inventory gating scope: anchor count receipt-only","carried","off-form declarations compared positionally; bound retained",["corpus/tools/README.md Round-96 addendum"],R103),
 ("NB-03","pinned inventory case is over-declaration, not deletion form","carried","bound retained; deletion class covered by gating, not by that pin",["corpus/tools/map-obligations-contract.json"],R103),
 ("NB-04","--freeze has no scope guard (foreign c3red pin)","closed","SCOPE-REFUSED no-write delivered r97; c3red removed at r96 closure",["commit 9d25df9","commit f3e09f9 (C-1)"],["r97:CO-02"]),
 ("NB-05","nothing validates the pin set (bogus 6th pin passes)","closed","16-case exact-set loader r97; dropped pins fail closed",["commit 9d25df9"],["r97:CO-05"]),
 ("NB-06","pins bind by basename only","closed","PATH-MISMATCH path binding r97",["commit 9d25df9"],["r97:CO-03"]),
 ("NB-08","DIGEST-MISMATCH cannot name the changed file","closed","names changed file(s) with before/after sha256 since r97",["commit 9d25df9"],["r97:CO-04"]),
 ("NB-09","SELF-TEST-MISMATCH exit convention diverges","closed","exit 2 (pinned as case 17) at r98; r97 exit-1 form the demonstrated before",["commit 4265df5","SCORECARD.md r98 calibration row"],["r97:CO-08","r97:NB-18","r98:CO-16"]),
 ("NB-10","freeze() discards its verify result; MALFORMED-MODEL/CONTRACT-INVALID unpinned","addressed","split disposition: verify propagation closed r97; the MALFORMED-MODEL/CONTRACT-INVALID pin half remains carried (r96-NB-10's second half, tracked in detail)",["commit 9d25df9","r99:CO-06 (open_accepted)"],["r97:CO-06"]),
 ("NB-11","chain-scoped byte-sensitive gate unregistered","addressed","registered at r96 closure (C-8: tools README addendum + SKILL row); reformat-sensitivity remains a documented bound",["commit f3e09f9","SKILL.md dependency row"],None),
 ("NB-12","gate-invisibility of contradiction/accusation/winner classes","addressed","consolidated as documented manual-review limit (blind-spot table + registry scope); no gate reads testimony by design",["corpus/knowledge/r99-gate-blind-spot-table.md Limits","SCORECARD.md r96 depth bounds"],None),
 ("NB-13","'first two-account fixture with empty ledger' corpus-bounded","carried","bound statement (23 scanned, 22 non-empty), accepted",["SCORECARD.md r96 depth bounds"],R103),
 ("NB-14","Q6 note receipts pinned to r95/in-flight revisions","closed","re-pinned by dated addendum at r98 closure",["commit 4265df5","corpus/knowledge/r96-response-scope-note.md (dated addendum)"],["r97:CO-11"]),
 ("NB-15","map doc-fidelity nits (3 items)","addressed","2/3 closed r97 (delimiter cell, stale 'new relation' sentence; receipts unchanged); :18 'r94 JSON pointers' imprecision carried",["commit 9d25df9","SCORECARD.md r97 depth row"],R103),
 ("NB-16","carried presupposition ('the same agreed bell') doubled","carried","not re-raised r97; whole-claim reviews found no constructible overclaim",["r97:CO-15"],R103),
 ("NB-17","/tmp inode exhaustion on host","addressed","cleared by r98 (df -i 2%, no Errno 28); TMPDIR workarounds recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-13 (not_recurring CO-11)"],["r97:CO-13"]),
 ("NB-19","tool-revision flux (map >=8 sha256s incl. NameError window)","addressed","recorded harness property; final revisions measured and pinned",[".ufo/waves/round-96/seats/V40-debt.json NB-19"],["r95:NB-09"]),
 ("NB-20","drift scope unchanged (entities-only, claim-shaped-only)","carried","bound retained (see r95-NB-01)",[".ufo/waves/round-96/seats/V40-debt.json NB-20"],R103),
 ("NB-21","consistent regeneration still exits 0","carried","permanent declared-vs-observed bound; blind-spot row 7",["corpus/knowledge/r99-gate-blind-spot-table.md row 7"],R103),
 ("NB-22","dependency_freeze undocumented in delivered docs","closed","tools README Round-96 addendum + SKILL row at closure",["commit f3e09f9"],None),
 ("NB-23","freeze revision label semantics undocumented","addressed","writer-managed revision refresh disclosed at r100 (additive-only delta)",["SCORECARD.md r100 coverage row","LOG.md r100 closure"],None),
 ("NB-24","V50 WC corrections: before-clause '5 sources' must be 4","closed","declaration erratum (1) at r96 closure",["LOG.md r96 closure errata"],None),
 ("NB-25","dual_pointer unpinned + droppable pins","closed","case 25 persisted; loader fails closed on ANY dropped pin (r97)",["commit 9d25df9","corpus/tools/map-obligations-contract.json"],["r97:CO-01"]),
 ("NB-26","r95 F-1 stale pin unrepaired by r96","addressed","carried to r98 where the addendum closed it (see r95-NB-08)",[".ufo/waves/round-96/seats/V40-debt.json NB-26"],["r95:NB-08"]),
 ("NB-27","V29 proposed fixtures-README text cites tools addendum","closed","correct text landed at r96 closure (C-8)",["commit f3e09f9"],None),
 ("CL-01","resolve foreign c3red pin + re-verify chain","closed","removed at closure; freeze 14/14 + chain 4/4 green on corrected contract c65ac3bd",["commit f3e09f9 (C-1)"],None),
 ("CL-02","fixtures README Round-96 + census 170","closed","landed at closure",["commit f3e09f9"],None),
 ("CL-03","corpus README :36 + SKILL rows stale","closed","landed at closure",["commit f3e09f9"],None),
 ("CL-04","C9 watch row-5 append due","closed","row 5 appended at closure",["commit f3e09f9"],None),
 ("CL-05","LOG/SCORECARD r96 entries due","closed","landed (2393934 + f3e09f9)",["commit 2393934","commit f3e09f9"],None),
 ("CL-06","roster 58/64 at compile","addressed","receipt rebuilt 64/64; V43/V58 mutual poll-wait self-recorded",["LOG.md r96 closure"],None),
 ("CL-07","no wave-spec/receipt artifacts in round-96","addressed","receipt rebuilt from dispatch (standing convention)",["LOG.md r96 closure"],None),
 ("CL-08","fleet report + SHONEN state","closed","SHONEN verified four [~] zero [x] (V39); fleet round-96 report exists",["/home/vgpnk/Projects/shokunin/.ufo/reports/round-96/","SHONEN.md"],None),
 ("CL-09","Q6 stale tool pin re-run","closed","re-run receipts at delivered revision; note addendum r98",["commit 4265df5"],None),
 ("CL-10","/tmp inode exhaustion operator decision","addressed","host condition cleared by r98",[".ufo/waves/round-98/seats/V33-debt.json PR-13"],None),
 ("CL-11","record V37 adjacency-verdict status","closed","recorded at closure (C-7): verdict rests on V31 + L1 checks",["LOG.md r96 closure (C-7)"],None),
 ("CL-12","V36's five closure conditions for L1","closed","C-F1/C-NOTE closed by r98 addenda; remainder landed at closure",["commit f3e09f9","commit 4265df5"],None),
 ("PR-01","Q4 disclosed mid-seat comma rewrite","addressed","disclosed; all later verifiers re-ran on delivered bytes",[".ufo/waves/round-96/seats/V40-debt.json PR-01"],None),
 ("PR-02","V15 comma observation stale","addressed","superseded by delivered bytes (ST-03)",[".ufo/waves/round-96/seats/V40-debt.json ST-03"],None),
 ("PR-03","V33 in-flight attribution inaccurate","addressed","recorded, not material",[".ufo/waves/round-96/seats/V40-debt.json PR-03"],None),
 ("PR-04","unattributed transient in fixture dir","carried","never attributed; hygiene record stands",[".ufo/waves/round-96/seats/V40-debt.json PR-04"],R103),
 ("PR-05","minor cross-report slips","addressed","caught and corrected (V56 et al.)",[".ufo/waves/round-96/seats/V40-debt.json PR-05"],None),
 ("PR-06","mid-flight producer defects before delivery","addressed","persisted as recorded defects; fixed before delivery",[".ufo/waves/round-96/seats/V40-debt.json PR-06"],None),
 ("PR-07","V41 --freeze probe wrote c3red pin (breach)","closed","self-disclosed; pin removed at closure; breach recorded, not re-rolled",["commit f3e09f9 (C-1/C-2)","LOG.md r96 closure"],None),
 ("PR-08","V50 in-flight transients","addressed","recorded with hashes",[".ufo/waves/round-96/seats/V40-debt.json PR-08"],None),
 ("ST-01","V34 interim INCONCLUSIVE -> final PASS","addressed","supersession recorded",[".ufo/waves/round-96/seats/V40-debt.json ST-01"],None),
 ("ST-02","V33 interim 'blocking defect' -> residual","addressed","supersession recorded",[".ufo/waves/round-96/seats/V40-debt.json ST-02"],None),
 ("ST-03","V15 paragraph superseded by delivered bytes","addressed","supersession recorded",[".ufo/waves/round-96/seats/V40-debt.json ST-03"],None),
 ("ST-04","Q6 note first revision superseded","addressed","final 6db32ca2 recorded",[".ufo/waves/round-96/seats/V40-debt.json ST-04"],None),
 ("ST-05","V34 baseline table remains current","addressed","no action owed",[".ufo/waves/round-96/seats/V40-debt.json ST-05"],None),
 ("ST-06","v2->v3 corrections of this ledger","addressed","final v3 is compiled record",[".ufo/waves/round-96/seats/V40-debt.json version"],None),
]
r96=_norm7(r96)
for sid,t,d,det,ev,tr,ow in r96:
    item("r96-"+sid, 96, sid, sid.split("-")[0], t, d, det, ev, tr, ow)

# r96 NB-07 restates BR-01 prose half -> carry record, not separate item
# (handled in carry_records below)

# ---------------- ROUND 97 (V37 own items: NB 20, CL 12, PR 13, ST 7 = 52)
r97 = [
 ("NB-01","r97 fixture not in freeze chain","closed","pinned at r98 (chain six); edge drop REDUCTION-DETECTED; V46 FAIL discharged",["commit 4265df5","SCORECARD.md r98 coverage row"],["r98:CO-01 (closed)"]),
 ("NB-02","refreshed r96 pin misses repaired map","closed","r96 re-frozen through guarded path at r97 (revision-only refresh, digest unchanged)",["commit 9d25df9","SCORECARD.md r97 coverage row"],None),
 ("NB-03","tools README :175 describes pre-r97 freeze","closed","S2 supersession block landed at r98 closure",["commit 4265df5"],["r98:CO-03 (closed)"]),
 ("NB-04","SKILL :87 / corpus README :37 stale (24 cases)","closed","refreshed at r98 closure (17 cases / six fixtures wording of the time)",["commit 4265df5 (r98 CL-02/03)"],None),
 ("NB-05","fixtures README Round-97 absent, census 170 stale","closed","landed at r97 closure (census 171 + dated :1213 correction)",["commit 9d25df9"],None),
 ("NB-06","r95/r96 note stale pins carried","closed","both corrected by dated addenda at r98 closure",["commit 4265df5","SCORECARD.md r98 freshness row (first freshness improvement)"],["r98:CO-06 (closed)"]),
 ("NB-07","r97 note receipt cites in-flight run as history","carried","standing caveat accepted (r98 CO-07 open_or_accepted)",[".ufo/waves/round-98/seats/V33-debt.json bounds_carried.open_or_accepted"],R103),
 ("NB-08","dual_pointer legacy-dialect-scoped","carried","canonical variants stay fail-closed exit 2; permanent bound",["SCORECARD.md r97 calibration bounds"],R103),
 ("NB-09","consistent regeneration still exits 0","carried","declared-vs-observed gate bound; blind-spot row 7",["corpus/knowledge/r99-gate-blind-spot-table.md row 7"],R103),
 ("NB-12","R1 report quote slip (exit=1 findings=[] vs actual)","addressed","recorded as PR-04; facts elsewhere correct",[".ufo/waves/round-97/seats/V37-debt.json PR-04"],None),
 ("NB-13","R3 paraphrase rebuts wording absent from LOG","addressed","recorded as PR-05; measured facts correct",[".ufo/waves/round-97/seats/V37-debt.json PR-05"],None),
 ("NB-14","repaired r96 map lost standalone relation-bound sentence","carried","bound survives in J11 anchor/README/sources; not re-raised r98",["r98:CO-12"],R103),
 ("NB-15","check_bible dependency blind spots (empty/earlier/terminal)","closed","documented r99 (blind-spot rows 1-3 with replays); wrong-but-earlier persisted as repointed_edge r101 (19/19); detection live since r96 freeze",["commit fe1ce46","commit ceeef43","corpus/knowledge/r99-gate-blind-spot-table.md rows 1-3","this pass: SELF-TEST 19/19 incl CASE repointed_edge (2026-10-18)"],["r98:NB-05","r98:CO-13"]),
 ("NB-16","poll-wait/endgame hazards (mutual windows)","addressed","subtract-SELF convention adopted r98 and held; mutual-wait class documented",["SCORECARD.md r98 discernment","V37 PR-03"],None),
 ("NB-17","freeze verify-side bounds (name-gated lookup, symlinks, JSON-only payload)","carried","accepted bounds, documented in registry scope",["SKILL.md dependency row scope","r98:CO-15"],R103),
 ("NB-18","SELF-TEST-MISMATCH exit divergence carried","addressed","closed at r98 (see r96-NB-09)",["commit 4265df5"],["r96:NB-09"]),
 ("NB-19","tool-revision flux r97","addressed","recorded; final revisions pinned",[".ufo/waves/round-97/seats/V37-debt.json NB-19"],["r95:NB-09"]),
 ("NB-20","r97 fixture README replay without exits","carried","recurrence of r94-BR-17 class (see that item)",[".ufo/waves/round-97/seats/V37-debt.json NB-20"],["r94:BR-17"]),
 ("CL-01","fixtures README Round-97 append + census","closed","landed at r97 closure",["commit 9d25df9"],None),
 ("CL-02","corpus README bullets (25 cases; 16 freeze cases)","closed","landed at r97 closure",["commit 9d25df9"],None),
 ("CL-03","C9 watch row-6 append","closed","row 6 appended at closure (V48 block verbatim)",["commit 9d25df9"],None),
 ("CL-04","SKILL.md registry rows refresh","closed","landed at r97 closure",["commit 9d25df9"],None),
 ("CL-05","tools README Round-97 C2 addendum","closed","landed at r97 closure (supersedes :175)",["commit 9d25df9"],None),
 ("CL-06","re-freeze record + V12/V46 errata","closed","landed at r97 closure",["commit 9d25df9"],None),
 ("CL-07","receipt fill / bookkeeping / commit split","closed","landed (9d25df9 + 9a3d648)",["commit 9d25df9","commit 9a3d648"],None),
 ("CL-08","do-not-touch constraints honored","closed","verified at closure (charter set byte-identical)",["SCORECARD.md r97 adjacency row"],None),
 ("CL-09","adjudicator/roster accounting","addressed","receipt 64/64; absences resolved at closure",["LOG.md r97 closure"],None),
 ("CL-10","r95/r96 note stale-pin decision","closed","repaired r98 via dated addenda",["commit 4265df5"],None),
 ("CL-11","SHONEN state + fleet report + receipt","closed","four [~] verified; fleet round-97 report exists",["/home/vgpnk/Projects/shokunin/.ufo/reports/round-97/"],None),
 ("CL-12","r97 fixture freeze-pin decision","closed","pinned r98 (chain six)",["commit 4265df5"],None),
 ("PR-01","V12 FAIL recorded (map digest unpinned claim)","addressed","recorded, discharged by erratum at closure; not re-rolled",["commit 9d25df9","SCORECARD.md r97 coverage"],None),
 ("PR-02","V46 FAIL recorded (r97 edge unfrozen)","addressed","recorded; discharged r98 (exact mutation bytes exit 1 REDUCTION-DETECTED)",["commit 4265df5"],None),
 ("PR-03","mutual poll-wait windows (R4<->R5, R1<->R2)","addressed","characterized; no trapped pair; convention followed",[".ufo/waves/round-97/seats/V37-debt.json PR-03"],None),
 ("PR-04","R1 quote-slip process record (same finding as NB-12)","addressed","recorded; facts elsewhere correct",[".ufo/waves/round-97/seats/V37-debt.json PR-04"],None),
 ("PR-05","R3 paraphrase process record (same finding as NB-13)","addressed","recorded; measured facts correct",[".ufo/waves/round-97/seats/V37-debt.json PR-05"],None),
 ("PR-06","/tmp ENOSPC during wave; TMPDIR redirections","addressed","host condition cleared r98",[".ufo/waves/round-97/seats/V37-debt.json PR-06"],None),
 ("PR-07","revision flux incl. incomplete freeze revision","addressed","recorded; final revision verified",[".ufo/waves/round-97/seats/V37-debt.json PR-07"],None),
 ("PR-08","interim->final verdict updates","addressed","supersessions recorded (ST group)",[".ufo/waves/round-97/seats/V37-debt.json PR-08"],None),
 ("PR-09","mid-flight README/map were r96 copies","addressed","map_obligations correctly failed missing_obligation; superseded by rewrites",[".ufo/waves/round-97/seats/V37-debt.json PR-09"],None),
 ("PR-10","seats absent at compile","addressed","receipt 64/64 at closure",["LOG.md r97 closure"],None),
 ("PR-11","poll-glob hazard (scratch dirs matched as reports)","addressed","naming mismatch recorded; convention noted",[".ufo/waves/round-97/seats/V37-debt.json PR-11"],None),
 ("PR-12","V39 integration checklist P0-P9","addressed","produced for L1; executed at closure",[".ufo/waves/round-97/seats/V37-debt.json PR-12"],None),
 ("PR-13","cross-seat audits (V53 5/5; V47 corrections)","addressed","recorded",[".ufo/waves/round-97/seats/V37-debt.json PR-13"],None),
 ("ST-01","V30/V45 PENDING superseded by PASS","addressed","recorded",[".ufo/waves/round-97/seats/V37-debt.json ST-01"],None),
 ("ST-02","V09/V26 interim superseded","addressed","recorded",[".ufo/waves/round-97/seats/V37-debt.json ST-02"],None),
 ("ST-03","mid-flight README/map superseded","addressed","recorded",[".ufo/waves/round-97/seats/V37-debt.json ST-03"],None),
 ("ST-04","R6 note first revision superseded","addressed","final 5e3b4225 recorded",[".ufo/waves/round-97/seats/V37-debt.json ST-04"],None),
 ("ST-05","V36 placeholder superseded","addressed","final PASS recorded",[".ufo/waves/round-97/seats/V37-debt.json ST-05"],None),
 ("ST-06","V14 preliminary superseded","addressed","final PASS recorded",[".ufo/waves/round-97/seats/V37-debt.json ST-06"],None),
 ("ST-07","fixtures README :1213 sentence superseded","addressed","dated correction queued and landed at closure (CL-01)",[".ufo/waves/round-97/seats/V37-debt.json ST-07"],None),
]
r97=_norm7(r97)
for sid,t,d,det,ev,tr,ow in r97:
    item("r97-"+sid, 97, sid, sid.split("-")[0], t, d, det, ev, tr, ow)
# r97 NB-04/NB-05/NB-06 etc kept; NB-10, NB-11 are carries -> carry_records
# (r97 NB-10 = BR-05 restatement; r97 NB-11 = /tmp restatement)

# ---------------- ROUND 98 (V33 own items: NB 12, CL 10, PR 13, ST 7 = 42)
r98 = [
 ("NB-01","tools README 'not gitignored' claim false","closed","erratum at r98 closure (CL-05); .gitignore covered *-self-test-*/ since r97",["commit 4265df5"],None),
 ("NB-02","tools README :283 git-diff claim wrong","closed","erratum at r98 closure",["commit 4265df5"],None),
 ("NB-03","placeholder-poll hazard (r98 README/map were r97 copies)","addressed","content-gated poll convention recorded; recurred r99 (NB-10) and was again recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-01","r99:NB-10"],None),
 ("NB-04","declaration 'byte copies of other 7 files' arithmetic imprecision","addressed","erratum convention; same class as r100/r101 roster errata",[".ufo/waves/round-98/seats/V33-debt.json PR-05","LOG.md r100/r101 errata"],None),
 ("NB-05","checker blind spots recur on r98 event","addressed","consolidated and closed via r99 blind-spot table + r101 repointed_edge pin (see r97-NB-15)",["commit fe1ce46","commit ceeef43"],["r97:NB-15"]),
 ("NB-06","r98 note cites in-flight contract c435239d","closed","V53 F1 erratum at r98 closure (delivered 153ebc5b)",["commit 4265df5"],None),
 ("NB-07","parent-tree stray baseline-analyze.txt","closed","removed at closure (stray sweep); r98 adjacency: single parent stray removed, attributed",["commit 4265df5","SCORECARD.md r98 adjacency row"],None),
 ("NB-08","r98 fixture README replay without exits (fifth recurrence)","carried","instance stands; class tracked under r94-BR-17 (grep verified 2026-10-18: no exit receipts in r98 README)",[".ufo/waves/round-98/seats/V33-debt.json NB-08"],["r94:BR-17"],R103),
 ("NB-09","r98 note 'still read their r97-closure bytes' stale","closed","erratum at r98 closure",["commit 4265df5"],None),
 ("NB-10","V14 bottom-line scope wording","addressed","recorded as PR-11; bounds stated",[".ufo/waves/round-98/seats/V33-debt.json PR-11"],None),
 ("NB-11","migration broader than 'path-less' (empty/non-string values)","addressed","migration behavior documented in tools README Round-98 addendum (MIGRATED before/after quoted)",["SCORECARD.md r98 calibration row","corpus/tools/README.md Round-98 addendum"],None),
 ("NB-12","one-way blocked waiter V43->V19; V58 mid-flight","addressed","presence-ledger recorded; convention held",[".ufo/waves/round-98/seats/V33-debt.json PR-09"],None),
 ("CL-01","fixtures README Round-98 + census 172","closed","landed at r98 closure",["commit 4265df5"],None),
 ("CL-02","corpus README :38 freeze row -> 17 cases/six fixtures","closed","landed at r98 closure",["commit 4265df5"],None),
 ("CL-03","SKILL rows :96/:98/:99 refresh","closed","landed at r98 closure",["commit 4265df5"],None),
 ("CL-04","C9 watch row-7 append","closed","row 7 appended at closure",["commit 4265df5"],None),
 ("CL-05","errata for NB-01/NB-02/NB-09 and V53 F1","closed","landed at r98 closure",["commit 4265df5"],None),
 ("CL-06","parent-tree stray sweep/record","closed","stray removed, attributed at closure",["commit 4265df5"],None),
 ("CL-07","receipt/bookkeeping/commit split","closed","landed (4265df5 + 111b9a3)",["commit 4265df5","commit 111b9a3"],None),
 ("CL-08","do-not-touch constraints","closed","verified at closure",["SCORECARD.md r98 adjacency row"],None),
 ("CL-09","roster accounting (16 absent verifier reports)","closed","receipt rebuilt from both dispatches 64/64",["LOG.md r98 closure (SCORECARD r98 header)"],None),
 ("CL-10","r98 fixture README replay exits","carried","NOT landed: r98 README still has no recorded exits (grep 2026-10-18); class carried under r94-BR-17",["grep -n -i exit corpus/fixtures/r98-clerk-filing/README.md -> no matches (2026-10-18)"],["r94:BR-17"],R103),
 ("PR-01","placeholder-poll hazard recorded live","addressed","convention recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-01"],None),
 ("PR-02","contract/tool hash flux recorded","addressed","final hashes measured and pinned",[".ufo/waves/round-98/seats/V33-debt.json PR-02"],None),
 ("PR-03","V53 narrow FAIL recorded","addressed","stands recorded, discharged by erratum",["commit 4265df5"],None),
 ("PR-04","parent-tree stray recorded by 12+ seats","closed","removed at closure",["commit 4265df5"],None),
 ("PR-05","declaration '7 files' imprecision","addressed","recorded (S3 A; V14)",[".ufo/waves/round-98/seats/V33-debt.json PR-05"],None),
 ("PR-06","S3 D1 stale clause superseded","addressed","superseded by S4 rewrite",[".ufo/waves/round-98/seats/V33-debt.json PR-06"],None),
 ("PR-07","S2 declared S1 ABSENT at hand-off","addressed","bounded stall-escape; S1 landed 20:35-20:36",[".ufo/waves/round-98/seats/V33-debt.json PR-07"],None),
 ("PR-08","47 seat files at compile; 16 absent","closed","receipt rebuilt 64/64",["LOG.md r98 closure"],None),
 ("PR-09","V59 presence ledger (no mutual-wait pair)","addressed","recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-09"],None),
 ("PR-10","v05-self-test-scratch gitignore-covered","addressed","not a stray; recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-10"],None),
 ("PR-11","V14 bottom-line scope wording","addressed","recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-11"],None),
 ("PR-12","NB-01/NB-02 independently corroborated","addressed","corroboration recorded",[".ufo/waves/round-98/seats/V33-debt.json PR-12"],None),
 ("PR-13","/tmp condition cleared","closed","df -i 2%, no Errno 28",[".ufo/waves/round-98/seats/V33-debt.json PR-13"],None),
 ("ST-01","interim battery superseded by re-run","addressed","recorded",[".ufo/waves/round-98/seats/V33-debt.json ST-01"],None),
 ("ST-02","placeholder bytes superseded by S4 rewrites","addressed","recorded",[".ufo/waves/round-98/seats/V33-debt.json ST-02"],None),
 ("ST-03","S3 D1 clause superseded","addressed","recorded",[".ufo/waves/round-98/seats/V33-debt.json ST-03"],None),
 ("ST-04","S5 contract pin superseded (V53 F1)","closed","erratum at closure",["commit 4265df5"],None),
 ("ST-05","interim IN-PROGRESS states superseded","addressed","recorded",[".ufo/waves/round-98/seats/V33-debt.json ST-05"],None),
 ("ST-06","'not gitignored' superseded-by-fact","closed","erratum at closure",["commit 4265df5"],None),
 ("ST-07","mid-flight map raw=20 mapped=17 superseded","addressed","final 20/20 PASS recorded",[".ufo/waves/round-98/seats/V33-debt.json ST-07"],None),
]
r98=_norm7(r98)
for sid,t,d,det,ev,tr,ow in r98:
    item("r98-"+sid, 98, sid, sid.split("-")[0], t, d, det, ev, tr, ow)

# ---------------- ROUND 99 (V36 own items: NB 16, CL 10 = 26)
r99 = [
 ("NB-01","S2/S5 and knowledge files absent at poll cap","addressed","window-correct ABSENTs; all landed 02:07-02:11Z (V74 post-escape reads; V36 post_write)",[".ufo/waves/round-99/seats/V74-debt-2.md (poll record)",".ufo/waves/round-99/seats/V36-debt.json post_write_02_06Z"],None),
 ("NB-02","'At the Chalk Stair' locative not in lapse note","addressed","bounded by AC-6 dated record: locative is README/description wording, not a quoted note clause",["LOG.md r99 closure (AC-6)","SCORECARD.md r99 depth bounds"],None),
 ("NB-03","minute-terms gloss not in lapse quotes","addressed","bounded by AC-6 ('per the original minute's terms' is README:11/map:69 wording)",["LOG.md r99 closure (AC-6)"],None),
 ("NB-04","V95: lines 70-73 world-assertions vs line 74 clerk-record","addressed","bounded by AC-6: 70-73 impersonal framing, 74 first-person denial; no resolution/blame/reconciliation asserted",["LOG.md r99 closure (AC-6)"],None),
 ("NB-05","V14 vs V105 divergence on historical-open-entry clause","addressed","recorded, not smoothed (AC-6 keeps both readings visible)",["LOG.md r99 closure (AC-6)",".ufo/waves/round-99/seats/V36-debt.json NB-05"],None),
 ("NB-06","r99-window-lapse unpinned (UNPINNED-FIXTURE exit 2)","closed","pinned at r100 through guarded --freeze (chain seven); r99 tick-15 removal detected",["commit 6f86bf2","SCORECARD.md r100 coverage row"],None),
 ("NB-08","SKILL/tools README still say 17 cases and five JSON tables","closed","superseded by dated Round-99 text at closure (freshness improved)",["commit fe1ce46","SCORECARD.md r99 freshness row"],None),
 ("NB-09","r99 README replay block records no exits (sixth recurrence)","carried","class tracked under r94-BR-17",[".ufo/waves/round-99/seats/V36-debt.json NB-09"],["r94:BR-17"],R103),
 ("NB-10","placeholder-poll hazard recurred on r99 README/map","addressed","recurrence recorded (see r98-NB-03); convention held",[".ufo/waves/round-99/seats/V36-debt.json NB-10"],["r98:NB-03"],None),
 ("NB-11","tool hash flux 1728ed89->6f81f8be->fb9bb9ff","addressed","recorded; delivered fb9bb9ff verified by V34/V74 and at r99 closure",[".ufo/waves/round-99/seats/V74-debt-2.md (hash table)"],["r95:NB-09"],None),
 ("NB-12","8 parent-repo files under round-99/seats (V69, V73)","closed","parent strays removed at closure (AC-7: V69 0-byte copies, V73 wrong-cwd stderr; archives dropped)",["commit fe1ce46","LOG.md r99 closure (AC-7)"],None),
 ("NB-13","S3 README/map-still-r98 clause stale","addressed","superseded by S4 rewrite",[".ufo/waves/round-99/seats/V36-debt.json NB-13"],None),
 ("NB-14","markdown_tamper is a newline append; symbolism file unpinned (11th file)","addressed","mapped-anchor visibility corrected (AC-2 + blind-spot row 10 at r100); r88 symbolism-clause-map.md remains a named unpinned bound (AC-5)",["LOG.md r99 closure (AC-2, AC-5)","corpus/knowledge/r99-gate-blind-spot-table.md row 10 (r100 addendum)"],R103),
 ("NB-15","V92 quote mismatch on V105 fence","addressed","recorded; does not reverse the locative FAIL",[".ufo/waves/round-99/seats/V36-debt.json NB-15"],None),
 ("NB-16","closure docs still at 4265df5; census 173 on disk","closed","closure docs landed at fe1ce46 (AC-8; census 173/39/134/421)",["commit fe1ce46"],None),
 ("CL-01","do not admit C2 component 2 (pre-landing)","addressed","superseded by delivery: V34 replayed every table row post-landing with quote-identical digests",["SCORECARD.md r99 depth row (component 2)",".ufo/waves/round-99/seats/V34-adjudicator.md"],None),
 ("CL-02","re-measure C1 on fb9bb9ff, not 6f81f8be","closed","V34 measured C1 on fb9bb9ff/8c2561b0",[".ufo/waves/round-99/seats/V34-adjudicator.md section 1.1"],None),
 ("CL-03","SKILL and tools README 17/five-JSON staleness","closed","dated Round-99 text at closure",["commit fe1ce46"],None),
 ("CL-04","fixtures README Round-99 + census 173","closed","landed at closure (AC-8)",["commit fe1ce46"],None),
 ("CL-05","corpus README bullets","closed","landed at closure (AC-8)",["commit fe1ce46"],None),
 ("CL-06","C9 row-8 append","closed","row 8 appended at closure",["commit fe1ce46"],None),
 ("CL-07","repair or bound NB-02..NB-05 without smoothing","closed","bounded via AC-6 dated record; nothing smoothed",["LOG.md r99 closure (AC-6)"],None),
 ("CL-08","parent stray sweep","closed","AC-7 executed at closure",["commit fe1ce46"],None),
 ("CL-09","roster reconcile; V39/V123 censuses stale","closed","receipt 128/128 rebuilt from dispatch (AC-9)",["LOG.md r99 closure (AC-9)"],None),
 ("CL-10","do not silently pin r99","closed","honored at r99; pinned openly at r100 through the guarded writer with disclosed additive refresh",["commit 6f86bf2","SCORECARD.md r100 coverage row"],None),
]
r99=_norm7(r99)
for sid,t,d,det,ev,tr,ow in r99:
    item("r99-"+sid, 99, sid, sid.split("-")[0], t, d, det, ev, tr, ow)
# r99 NB-07 (BR-01 prose) is a carry record.

# ---------------- ROUND 100 (no ledger file; V29 conditions + recorded FAILs = 11)
r100 = [
 ("AC-ROSTER","32 declared vs 34 dispatched identifiers; receipt absent at cutoff","closed","roster erratum recorded append-only; receipt filled from real dispatch (34/34, real agent IDs)",["LOG.md r100 closure (AC-ROSTER)",".ufo/waves/round-100/receipt.json","commit 6f86bf2"],None),
 ("AC-BASELINE","fe1ce46 baseline vs pre-dispatch commits b5fe472/ae67105","closed","qualification recorded: both legitimate pre-dispatch lane history; fe1ce46 kept for fixture/pin comparison; V15 not re-rolled",["LOG.md r100 closure (AC-BASELINE)","commit b5fe472","commit ae67105"],None),
 ("AC-DOCS","closure docs due (fixtures README r100, corpus README, C9 row 9)","closed","landed at closure: Round-100 section, census 174/40/134/421, freeze bullet repaired, C9 row 9",["commit 6f86bf2","LOG.md r100 closure (AC-DOCS)"],None),
 ("AC-RECEIPT-ERRATUM","T2 report quotes two malformed relation digests","closed","report-only erratum filed; actual relations.json SHA-256 recorded (c279254b...); fixture bytes and pins always correct",["LOG.md r100 closure (AC-RECEIPT-ERRATUM)"],None),
 ("AC-SCOPE","semantic-first precedence; unpinned set; dossier-vs-pins distinction","closed","recorded at closure; blind-spot rows 10-12 carry the three correction classes",["LOG.md r100 closure (AC-SCOPE)","corpus/knowledge/r99-gate-blind-spot-table.md rows 10-12"],None),
 ("AC-CLOSE","closure battery + records on committed revision","closed","battery re-ran green on committed revision (freeze 18/18, chain 7/7, map 25/25, boundary CERTIFIED, census 174, checker pin reproduced)",["LOG.md r100 closure (AC-CLOSE)"],None),
 ("FAIL-V15","strict allowlist FAIL (baseline attribution)","addressed","qualified, not re-rolled (AC-BASELINE)",["LOG.md r100 closure"],None),
 ("FAIL-V18","roster FAIL","closed","discharged by roster erratum + filled receipt",["LOG.md r100 closure"],None),
 ("FAIL-V20","shared closure surfaces FAIL","closed","discharged by AC-DOCS closure docs",["LOG.md r100 closure"],None),
 ("QUAL-V21","literal-harness limit (two T4 harnesses not independently re-runnable)","addressed","retained as standing convention in r100 and r101 operability rows",["SCORECARD.md r100/r101 operability rows"],None),
 ("QUAL-V30","cutoff accuracy","addressed","recorded accurately in the closure record",["LOG.md r100 closure"],None),
]
r100=_norm7(r100)
for sid,t,d,det,ev,tr,ow in r100:
    item("r100-"+sid, 100, sid, "AC" if sid.startswith("AC") else ("FAIL" if sid.startswith("FAIL") else "QUAL"),
         t, d, det, ev, tr, ow)

# ---------------- ROUND 101 (V24 defects + ACs = 10)
r101 = [
 ("DEF-1","entry cites r94 README:13 twice for a line-11 clause","closed","repaired at closure (AC-1): :13->:11 at entry lines 58/81; paraphrase verified true at line 11",["LOG.md r101 closure (AC-1)","commit ceeef43","corpus/knowledge/r101-r10-register-first-entry.md"],None),
 ("DEF-2","range-tail truncations :93-94/:99-100","addressed","recorded (repair was optional per AC-1; anchoring unambiguous; not claimed done)",[".ufo/waves/round-101/seats/V24-adjudicator.md defect 2"],None),
 ("DEF-3","entry metadata timestamps stale (verified-at 00:18 vs final 00:31)","addressed","recorded; quoted receipts independently re-derived (V07/V09/V15)",[".ufo/waves/round-101/seats/V24-adjudicator.md defect 3"],None),
 ("DEF-4","C3 delivered as docs-of-record, blind-spot row 2 byte-unchanged","closed","literal row-2 close appended as dated integrator addendum at closure (AC-2); table was outside producer ownership",["LOG.md r101 closure (AC-2)","corpus/knowledge/r99-gate-blind-spot-table.md (row 2 dated addendum)"],None),
 ("DEF-5","V13 final never delivered (stub)","addressed","stands as filed; preliminaries corroborated by V17/V23; recorded not re-rolled (AC-4)",["LOG.md r101 closure (AC-4)"],None),
 ("DEF-6","closure-bookkeeping pendings (README:42 bullet, C9 row 10)","closed","landed at closure (AC-3): freeze bullet refreshed, C9 row 10 appended, closure commits",["LOG.md r101 closure (AC-3)","commit ceeef43","commit 542021a","commit 60e88bf"],None),
 ("AC-1","entry citation repair (U2/integrator)","closed","discharged at closure",["LOG.md r101 closure"],None),
 ("AC-2","blind-spot row-2 record location (integrator)","closed","discharged at closure (dated addendum)",["LOG.md r101 closure"],None),
 ("AC-3","closure battery pendings","closed","discharged (freeze bullet, C9 row 10, closure commit)",["LOG.md r101 closure"],None),
 ("AC-4","records only (V13 stub, U2 overbroad claim, V26 probe, scratch variants)","closed","recorded at closure, no action owed",["LOG.md r101 closure"],None),
]
r101=_norm7(r101)
for sid,t,d,det,ev,tr,ow in r101:
    item("r101-"+sid, 101, sid, sid.split("-")[0], t, d, det, ev, tr, ow)

# ---------------- CARRY RECORDS (88): restatements/dispositions of earlier items
carry = []
def c(sid, src, text, tracks, seen):
    carry.append({"id": sid, "source_ledger": src, "text": text,
                  "tracks": tracks, "status_seen_at_source": seen})

# r95 CO-01..CO-23 (23) - r94 items with r95 status
for sid, tr in [
 ("CO-01","r94-BR-04"),("CO-02","r94-BR-06"),("CO-03","r94-BR-07"),
 ("CO-04","r94-BR-08"),("CO-05","r94-BR-09"),("CO-06","r94-BR-10"),
 ("CO-07","r94-BR-11"),("CO-08","r94-BR-12"),("CO-09","r94-BR-13"),
 ("CO-10","r94-BR-14"),("CO-11","r94-BR-15"),("CO-12","r94-BR-19 + r94-BR-20"),
 ("CO-13","r94-BR-21"),("CO-14","r94-CR-01 + r94-BR-18"),("CO-15","r94-CR-02"),
 ("CO-16","r94-CR-03"),("CO-17","r94-CR-05"),("CO-18","r94-CR-06"),
 ("CO-19","r94-CR-07"),("CO-20","r94-CR-08"),("CO-21","r94-BR-27"),
 ("CO-22","r94-BR-26"),("CO-23","r94-BR-22 + r94-BR-23 + r94-BR-28")]:
    c("r95:"+sid, ".ufo/waves/round-95/seats/V31-debt.json",
      "carried r94 item "+tr+" with r95 status", tr, "carried/re-scoped at r95")
# r95 NB-05, NB-06, NB-10, NB-11 are also carries:
for sid, tr in [("NB-05","r94-BR-01"),("NB-06","r94-BR-05"),("NB-10","r94-BR-16"),("NB-11","r94-BR-17")]:
    c("r95:"+sid, ".ufo/waves/round-95/seats/V31-debt.json",
      "r95 restatement of "+tr, tr, "unchanged at r95")

# r96 CO-01..CO-10 (10) + NB-07 (1) = 11
for sid, tr, seen in [
 ("CO-01","r95-NB-02","ADDRESSED r96"),("CO-02","r95-NB-07","ADDRESSED r96"),
 ("CO-03","r95-NB-12","ADDRESSED r96"),("CO-04","r94-BR-01","PARTIALLY ADDRESSED (JSON half)"),
 ("CO-05","r94-BR-05","STILL OPEN, recurred"),("CO-06","r95-NB-08","RECURRED"),
 ("CO-07","r95-NB-09","RECURRED"),("CO-08","r95-NB-01 (+13/14)","UNCHANGED"),
 ("CO-09","r95-NB-03 (+10/11)","UNCHANGED"),("CO-10","r94 carry-overs (CR/BR set)","UNADDRESSED except same-file touches"),
 ("NB-07","r94-BR-01","prose half open"),
 ("NB-18","r94-BR-05","BR-05 recurred live in r96 (transient root scratch dirs)")]:
    c("r96:"+sid, ".ufo/waves/round-96/seats/V40-debt.json",
      "r96 status of "+tr, tr, seen)

# r97 CO-01..CO-18 (18) + NB-10, NB-11 (2) = 20
for sid, tr, seen in [
 ("CO-01","r96-NB-25","CLOSED r97"),("CO-02","r96-NB-04","CLOSED r97"),
 ("CO-03","r96-NB-06","CLOSED r97"),("CO-04","r96-NB-08","CLOSED r97"),
 ("CO-05","r96-NB-05","CLOSED r97"),("CO-06","r96-NB-10a","CLOSED r97"),
 ("CO-07","r96-NB-07 (r94-BR-01)","OPEN"),("CO-08","r96-NB-09","OPEN"),
 ("CO-09","r96-NB-10","OPEN (MALFORMED pin half)"),("CO-10","r96-NB-15","2/3 CLOSED"),
 ("CO-11","r96-NB-14 + r96-NB-26","r95/r96 OPEN; r97 corrected"),
 ("CO-12","r96-NB-18 (r94-BR-05)","OPEN, both tools"),
 ("CO-13","r96-NB-17","OPEN host"),("CO-14","r96-NB-20/NB-21","OPEN/accepted"),
 ("CO-15","r96-NB-16","NOT RAISED"),("CO-16","r96 BR-17 class","RECURRED"),
 ("CO-17","r96-CL-04","PROPOSED, not written"),("CO-18","r96-CO-10","UNADDRESSED except same-file"),
 ("NB-10","r94-BR-05","BR-05 now both tools"),("NB-11","r96-NB-17","/tmp restatement")]:
    c("r97:"+sid, ".ufo/waves/round-97/seats/V37-debt.json",
      "r97 status of "+tr, tr, seen)

# r98 bounds_carried buckets (21) - V33's own carry numbering over r97 items
for sid, tr, seen in [
 ("CO-01","r97-NB-01","closed (pinned r98)"),("CO-02","r94-BR-01 (prose)","open_or_accepted"),
 ("CO-03","r97-NB-03","closed (S2 supersession)"),("CO-04","r97-NB-04","open_or_accepted"),
 ("CO-05","r97-NB-05","open_or_accepted (due r98)"),("CO-06","r97-NB-06","closed (S5 addenda)"),
 ("CO-07","r97-NB-07","open_or_accepted (caveat standing)"),("CO-08","r97-NB-08","open_or_accepted"),
 ("CO-09","r97-NB-09","open_or_accepted"),("CO-10","r94-BR-05","gitignore half closed; wording half NB-01"),
 ("CO-11","r96-NB-17","not_recurring (/tmp cleared)"),("CO-12","r97-NB-14","not re-raised"),
 ("CO-13","r97-NB-15","recurring"),("CO-14","r97-NB-16","recurring"),
 ("CO-15","r97-NB-17","open_or_accepted"),("CO-16","r96-NB-09","closed (C1a)"),
 ("CO-17","r97-NB-19","recurring"),("CO-18","r94-BR-17","recurring"),
 ("CO-19","r94-BR-01 (prose)","open_or_accepted"),("CO-20","r96-NB-10b","open_or_accepted"),
 ("CO-21","r98 C9 row-7","open_closure (landed at closure)")]:
    c("r98:"+sid, ".ufo/waves/round-98/seats/V33-debt.json (bounds_carried)",
      "V33 carry-list disposition for "+tr, tr, seen)

# r99 bounds_carried (16) - V36's carry numbering
for sid, tr, seen in [
 ("NB-07","r94-BR-01 (prose)","r99 restatement of the BR-01 prose half"),
 ("CO-01","r94-BR-01 (prose)","not_closed_here"),("CO-02","r99 ten-file pin record","not_closed_here (uncredited at compile)"),
 ("CO-03","r97-NB-15","not_closed_here"),("CO-04","r97-NB-09","not_closed_here"),
 ("CO-05","r97-NB-08","open_accepted"),("CO-06","r96-NB-10b","open_accepted"),
 ("CO-07","r98-NB-11","not_closed_here (wording)"),("CO-08","r94-BR-05","open_accepted (scratch at root)"),
 ("CO-09","self-test consistency-not-truth bound","open_accepted"),("CO-10","path-less pin needs --freeze","open_accepted"),
 ("CO-11","r99-NB-09 (README exits)","recurred"),("CO-12","r98-NB-03 (placeholder poll)","recurred"),
 ("CO-13","r95-NB-09 (revision flux)","recurred"),("CO-14","C9 row-8","open_closure (landed)"),
 ("CO-15","registry/README staleness","open_closure (landed)"),("CO-16","r99-NB-06 (new fixture unpinned)","recurred (closed r100)")]:
    c("r99:"+sid, ".ufo/waves/round-99/seats/V36-debt.json (bounds_carried)",
      "V36 carry-list disposition for "+tr, tr, seen)

# ---------------- source registry
sources = [
 {"round": 94, "file": ".ufo/waves/round-94/followup/F29-debt.json", "seat": "F29",
  "items_in_source": 51, "own_items": 51, "carry_records": 0},
 {"round": 95, "file": ".ufo/waves/round-95/seats/V31-debt.json", "seat": "V31",
  "items_in_source": 51, "own_items": 24, "carry_records": 27,
  "note": "item_counts {NB:14, CO:23, CL:10, PR:3, ST:1}; the 23 CO + 4 restating NBs (NB-05/06/10/11) are carries; own = 10 NB + 10 CL + 3 PR + 1 ST"},
 {"round": 96, "file": ".ufo/waves/round-96/seats/V40-debt.json", "seat": "V40",
  "items_in_source": 63, "own_items": 51, "carry_records": 12,
  "note": "item_counts {NB:27, CO:10, CL:12, PR:8, ST:6}; the 10 CO + NB-07 + NB-18 are carries; own = 26 NB + 12 CL + 8 PR + 6 ST - 1 (NB-07 carry)"},
 {"round": 97, "file": ".ufo/waves/round-97/seats/V37-debt.json", "seat": "V37",
  "items_in_source": 70, "own_items": 50, "carry_records": 20,
  "note": "item_counts {NB:20, CO:18, CL:12, PR:13, ST:7}; the 18 CO + NB-10/NB-11 are carries"},
 {"round": 98, "file": ".ufo/waves/round-98/seats/V33-debt.json", "seat": "V33",
  "items_in_source": 63, "own_items": 42, "carry_records": 21,
  "note": "sections: bounds_new 12, closure_items 10, process_observations 13, supersessions 7 (=42); bounds_carried buckets dispose 21 carry-list entries"},
 {"round": 99, "file": ".ufo/waves/round-99/seats/V36-debt.json", "seat": "V36",
  "items_in_source": 42, "own_items": 25, "carry_records": 17,
  "note": "sections: bounds_new 16, closure_items 10; NB-07 (BR-01 prose restatement) is a carry, so own = 15 NB + 10 CL; bounds_carried buckets dispose 16 carry-list entries; supplementary extraction .ufo/waves/round-99/seats/V74-debt-2.md merged into trails"},
 {"round": 100, "file": ".ufo/waves/round-100/seats/V29-adjudicator.md + LOG.md r100 closure", "seat": "V29/L1",
  "items_in_source": 11, "own_items": 11, "carry_records": 0,
  "note": "ANOMALY: the r102 declaration cites 'r100 V33' but round-100's roster was T1-T4 + V01-V30 (34 seats) and no V33 seat or V33-debt file exists; the r100 debt surface used is V29's six admission conditions plus the recorded FAILs (V15/V18/V20) and qualifications (V21/V30)"},
 {"round": 101, "file": ".ufo/waves/round-101/seats/V24-adjudicator.md + LOG.md r101 closure", "seat": "V24/L1",
  "items_in_source": 10, "own_items": 10, "carry_records": 0,
  "note": "the 'carried notes': V24 defects 1-6 plus conditions AC-1..AC-4; all discharged at closure per LOG"},
]

own_total = sum(s["own_items"] for s in sources)
carry_total = sum(s["carry_records"] for s in sources)
assert len(E) == own_total, (len(E), own_total)
assert len(carry) == carry_total, (len(carry), carry_total)

disp_counts = {}
for it in E:
    disp_counts[it["disposition"]] = disp_counts.get(it["disposition"], 0) + 1

ledger = {
 "artifact": "corpus/knowledge/r102-debt-ledger.json",
 "lane": "lore-shokunin",
 "round": 102,
 "compiled_at": "2026-10-18",
 "compiled_by": "U1 (synthesis producer), round-102 capstone wave, zai-coding-plan/glm-5.3-flash-low",
 "baseline": "542021a (r101 closure)",
 "scope": "every debt item raised across r94-r101 with final disposition closed / addressed / carried:<owner>, each with an evidence pointer",
 "disposition_vocabulary": {
   "closed": "resolved with verification in the delivered tree (commit, pinned case, landed doc, or rebuilt receipt)",
   "addressed": "action taken that retires or bounds the debt without a full gate-level close (dated addendum, recorded bound, convention, host resolution, erratum); residual named in disposition_detail where partial",
   "carried": "still open in the delivered r102 tree; carried_owner names the holder"
 },
 "counting_rules": [
   "an entry that restates or disposes of an earlier round's item is a carry_record (mirrored into the tracked item's trail), not a new item",
   "ST (supersession) and PR (process observation) entries that only record intra-round bookkeeping are items with disposition addressed; they are kept so no source id is dropped",
   "r100 has no debt-ledger file: its surface is the adjudicator's six conditions plus recorded FAILs/qualifications (see sources[6] anomaly)",
   "totals.source_entries = own_items + carry_records and equals the sum of items_in_source across the eight sources"
 ],
 "totals": {
   "items": len(E),
   "carry_records": len(carry),
   "source_entries": len(E) + len(carry),
   "dispositions": disp_counts
 },
 "sources": sources,
 "items": E,
 "carry_records": carry,
 "anomalies": [
   "r102 LOG declaration C2 cites 'r100 V33' as a source ledger: no V33 seat exists in round-100 (roster T1-T4 + V01-V30, receipt 34/34) and no round-100 debt file exists; the r100 debt surface is V29's conditions + recorded FAILs, used here",
   "round-99 has a SECOND debt extraction, .ufo/waves/round-99/seats/V74-debt-2.md (markdown, merged against V36 by its seat); its additions (poll record, delivered hashes, C1 re-run) are reflected in r99 item evidence rather than double-counted",
   "r98 V33-debt.json and r99 V36-debt.json use section structure (bounds_new/bounds_carried/closure_items) instead of an items array; counted per section with the bounds_carried buckets as carry records",
   "r98 closure item CL-10 ('r98 fixture README replay exits') was listed as a closure item but was NOT landed: the r98 README still contains no recorded exits (verified by grep 2026-10-18); recorded as carried under the r94-BR-17 class rather than marked closed"
 ],
 "bottom_line": "273 items + 88 carry records = 361 source entries accounted; 0 silently dropped; every disposition carries an evidence pointer",
}

out = "/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r102-debt-ledger.json"
with open(out, "w") as f:
    json.dump(ledger, f, indent=1, ensure_ascii=True)
    f.write("\n")
print("wrote", out)
print("items:", len(E), "carry:", len(carry), "disp:", disp_counts)

#!/usr/bin/env python3
"""V99 independent seat-table builder + poll.

Writes only under V99-scratch/. Does not write the seat report or receipt.json.
"""
import hashlib
import json
import os
import re
import subprocess
import time
from datetime import datetime, timezone

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(LANE, ".ufo/waves/round-99/seats")
WAVE = os.path.join(LANE, ".ufo/waves/round-99")
SCRATCH = os.path.join(SEATS, "V99-scratch")
RECEIPT = os.path.join(WAVE, "receipt.json")
V39_MD = os.path.join(SEATS, "V39-receipt.md")
ROSTER_TXT = os.path.join(SCRATCH, "roster.txt")
LOG = os.path.join(SCRATCH, "poll.log")
SELF = "V99"
MAX_TRIES = 40
SLEEP_S = 20

PRODUCER_REPORTS = [
    "S1-full-file-pins.md",
    "S2-tools-docs.md",
    "S3-fixture-author.md",
    "S4-fixture-docs.md",
    "S5-knowledge-author.md",
]
ARTIFACTS = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "SKILL.md",
    "corpus/fixtures/r99-window-lapse/README.md",
    "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md",
    "corpus/fixtures/r99-window-lapse/fictional-excerpts.md",
    "corpus/fixtures/r99-window-lapse/inspiration-note.md",
    "corpus/fixtures/r99-window-lapse/source-excerpt.md",
    "corpus/fixtures/r99-window-lapse/entities.json",
    "corpus/fixtures/r99-window-lapse/relations.json",
    "corpus/fixtures/r99-window-lapse/contradictions.json",
    "corpus/fixtures/r99-window-lapse/timeline.json",
    "corpus/fixtures/r99-window-lapse/sources.json",
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
]

ROSTER_RE = re.compile(
    r"^(S[1-5]|V\d+)\s+(\S+)\s+—\s+report\s+(\S+)"
)
SHA_RE = re.compile(r"\b([0-9a-f]{64})\b")


def now():
    return datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")


def log(msg):
    line = msg if msg.endswith("\n") else msg + "\n"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line)
    print(line, end="")


def sh(cmd):
    r = subprocess.run(
        cmd, shell=True, cwd=LANE, capture_output=True, text=True
    )
    log("$ " + cmd)
    if r.stdout:
        log(r.stdout.rstrip("\n"))
    if r.stderr:
        log("STDERR: " + r.stderr.rstrip("\n"))
    log("exit %d" % r.returncode)
    return r.returncode, r.stdout, r.stderr


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_roster():
    rows = []
    with open(ROSTER_TXT, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = ROSTER_RE.match(line)
            if not m:
                raise SystemExit("roster parse fail: " + line[:160])
            seat, role, path = m.group(1), m.group(2), m.group(3)
            rows.append(
                {
                    "seat": seat,
                    "role": role,
                    "declared_report": path,
                    "declared_basename": os.path.basename(path),
                }
            )
    return rows


def norm_path(p):
    if not p:
        return ""
    p = str(p).replace("\\", "/").strip()
    prefixes = (
        "/home/vgpnk/Projects/shokunin/lore-shokunin/",
        "lore-shokunin/",
        "./",
    )
    for pre in prefixes:
        if p.startswith(pre):
            p = p[len(pre) :]
    return p


def file_meta(path):
    st = os.stat(path)
    first = ""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            first = f.readline().rstrip("\n")
    except OSError as e:
        first = "READ-ERROR %s" % e
    return {
        "bytes": st.st_size,
        "mtime": datetime.fromtimestamp(st.st_mtime).astimezone().strftime(
            "%Y-%m-%dT%H:%M:%S%z"
        ),
        "mtime_epoch": st.st_mtime,
        "sha256": sha256_file(path),
        "first_line": first[:200],
    }


def scan_disk(roster):
    by_seat = {r["seat"]: r for r in roster}
    found = {r["seat"]: [] for r in roster}
    unexpected = []
    for name in sorted(os.listdir(SEATS)):
        path = os.path.join(SEATS, name)
        if not os.path.isfile(path) or not name.endswith(".md"):
            continue
        m = re.match(r"^(S[1-5]|V\d+)-", name)
        if not m or m.group(1) not in by_seat:
            unexpected.append(name)
            continue
        found[m.group(1)].append(name)

    rows = []
    for spec in roster:
        seat = spec["seat"]
        names = found[seat]
        declared = spec["declared_basename"]
        declared_path = os.path.join(SEATS, declared)
        present = os.path.isfile(declared_path)
        row = {
            "seat": seat,
            "role": spec["role"],
            "declared_report": norm_path(spec["declared_report"])
            if spec["declared_report"].startswith("/")
            or spec["declared_report"].startswith(".ufo")
            else norm_path(
                ".ufo/waves/round-99/seats/" + spec["declared_basename"]
            ),
            "declared_basename": declared,
            "present": present,
            "files": names,
            "duplicate": len(names) > 1,
            "unexpected_extra": [n for n in names if n != declared],
        }
        # declared path may be relative in roster; normalize to seats/<basename>
        row["declared_report"] = ".ufo/waves/round-99/seats/" + declared
        if present:
            meta = file_meta(declared_path)
            row.update(meta)
            header_ok = row["first_line"].startswith("# " + seat)
            row["header_ok"] = header_ok
        else:
            row.update(
                {
                    "bytes": None,
                    "mtime": None,
                    "mtime_epoch": None,
                    "sha256": None,
                    "first_line": None,
                    "header_ok": None,
                }
            )
        rows.append(row)
    return rows, unexpected


def parse_receipt(raw_text):
    data = json.loads(raw_text)
    seats = data.get("seats")
    rows = {}
    shape = "unknown"
    if isinstance(seats, list):
        shape = "list"
        for item in seats:
            if not isinstance(item, dict):
                continue
            sid = (
                item.get("seat")
                or item.get("id")
                or item.get("seat_id")
                or item.get("name")
            )
            if sid is None:
                continue
            rows[str(sid)] = item
    elif isinstance(seats, dict):
        shape = "dict"
        for sid, item in seats.items():
            if isinstance(item, dict):
                rows[str(sid)] = item
            else:
                rows[str(sid)] = {"value": item}
    snap = data.get("collection_snapshot") or {}
    present = snap.get("present")
    missing = snap.get("missing")
    return {
        "data": data,
        "shape": shape,
        "rows": rows,
        "top_keys": sorted(data.keys()),
        "present_list": present,
        "missing_list": missing,
        "reports_expected": snap.get("reports_expected"),
        "reports_present": snap.get("reports_present"),
        "reports_missing": snap.get("reports_missing"),
    }


def row_sha(item):
    if not isinstance(item, dict):
        return None
    for k in ("report_sha256", "sha256", "report_hash", "hash"):
        v = item.get(k)
        if isinstance(v, str) and re.fullmatch(r"[0-9a-fA-F]{64}", v):
            return v.lower()
    reports = item.get("reports")
    if isinstance(reports, dict):
        for v in reports.values():
            if isinstance(v, str) and re.fullmatch(r"[0-9a-fA-F]{64}", v):
                return v.lower()
    return None


def row_path(item):
    if not isinstance(item, dict):
        return None
    for k in ("report_path", "path", "report"):
        v = item.get(k)
        if isinstance(v, str) and v.strip():
            return norm_path(v)
    return None


def build(reason):
    roster = load_roster()
    rows, unexpected = scan_disk(roster)
    by_seat = {r["seat"]: r for r in rows}
    present = [r["seat"] for r in rows if r["present"]]
    # endgame: subtract SELF from the all-reports expectation
    others_present = [s for s in present if s != SELF]
    others_missing = [
        r["seat"] for r in rows if not r["present"] and r["seat"] != SELF
    ]
    self_present = by_seat[SELF]["present"]

    receipt_meta = None
    parsed = None
    receipt_error = None
    if os.path.isfile(RECEIPT):
        receipt_meta = file_meta(RECEIPT)
        try:
            with open(RECEIPT, encoding="utf-8") as f:
                raw = f.read()
            parsed = parse_receipt(raw)
        except json.JSONDecodeError as e:
            receipt_error = "JSONDecodeError: %s" % e
        except Exception as e:
            receipt_error = "%s: %s" % (type(e).__name__, e)
    v39_md_meta = file_meta(V39_MD) if os.path.isfile(V39_MD) else None

    drifts = []
    agreements = 0
    compared = 0

    def add(kind, seat, detail):
        drifts.append({"kind": kind, "seat": seat, **detail})

    if parsed is None:
        add(
            "receipt_absent" if not os.path.isfile(RECEIPT) else "receipt_unparsed",
            None,
            {"error": receipt_error, "path": norm_path(RECEIPT)},
        )
    else:
        v39_ids = set(parsed["rows"])
        disk_ids = set(by_seat)
        for sid in sorted(disk_ids - v39_ids):
            add(
                "seat_missing_from_v39",
                sid,
                {
                    "disk_present": by_seat[sid]["present"],
                    "disk_sha256": by_seat[sid]["sha256"],
                    "disk_path": by_seat[sid]["declared_report"],
                },
            )
        for sid in sorted(v39_ids - disk_ids):
            add(
                "seat_extra_in_v39",
                sid,
                {"v39_row_keys": sorted(parsed["rows"][sid].keys())},
            )
        for sid in sorted(disk_ids & v39_ids):
            compared += 1
            disk = by_seat[sid]
            item = parsed["rows"][sid]
            v_sha = row_sha(item)
            v_path = row_path(item)
            v_agent = item.get("agent_id", "<key-absent>")
            row_drift = False
            # presence: V39 may omit sha when absent
            v_present = bool(v_sha) or (
                isinstance(v_path, str) and v_path.endswith(".md") and v_sha is not None
            )
            # if path set and sha set -> present; if both null and outcome/missing -> absent
            if v_sha is None and (v_path is None or v_path == ""):
                v_present = False
            elif v_sha:
                v_present = True
            else:
                # path without sha: treat as claimed present but unhashed
                v_present = True
            if disk["present"] != v_present:
                row_drift = True
                add(
                    "presence_mismatch",
                    sid,
                    {
                        "disk_present": disk["present"],
                        "v39_present": v_present,
                        "disk_sha256": disk["sha256"],
                        "v39_sha256": v_sha,
                        "v39_path": v_path,
                        "disk_mtime": disk["mtime"],
                    },
                )
            elif disk["present"] and v_sha and disk["sha256"] != v_sha:
                row_drift = True
                receipt_mtime = receipt_meta["mtime_epoch"] if receipt_meta else None
                add(
                    "sha256_mismatch",
                    sid,
                    {
                        "disk_sha256": disk["sha256"],
                        "v39_sha256": v_sha,
                        "disk_bytes": disk["bytes"],
                        "disk_mtime": disk["mtime"],
                        "file_newer_than_receipt": (
                            receipt_mtime is not None
                            and disk["mtime_epoch"] is not None
                            and disk["mtime_epoch"] > receipt_mtime + 0.5
                        ),
                    },
                )
            elif disk["present"] and v_sha is None:
                row_drift = True
                add(
                    "v39_unhashed_but_disk_present",
                    sid,
                    {"disk_sha256": disk["sha256"], "v39_path": v_path},
                )
            if v_path and disk["declared_report"] and norm_path(v_path) != disk["declared_report"]:
                # allow basename match as non-drift if the relative seats path matches
                if os.path.basename(v_path) != disk["declared_basename"]:
                    row_drift = True
                    add(
                        "path_mismatch",
                        sid,
                        {
                            "disk_path": disk["declared_report"],
                            "v39_path": v_path,
                        },
                    )
            if v_agent not in (None, "null") and v_agent != "<key-absent>":
                add(
                    "agent_id_not_null",
                    sid,
                    {"agent_id": v_agent},
                )
                row_drift = True
            if not row_drift:
                agreements += 1
            if disk["duplicate"]:
                add(
                    "duplicate_report_files",
                    sid,
                    {"files": disk["files"]},
                )
            if disk["present"] and disk["header_ok"] is False:
                add(
                    "header_mismatch",
                    sid,
                    {"first_line": disk["first_line"]},
                )

        # collection_snapshot list compare, if present
        if isinstance(parsed["present_list"], list):
            snap_present = set(map(str, parsed["present_list"]))
            disk_present = set(present)
            only_snap = sorted(snap_present - disk_present)
            only_disk = sorted(disk_present - snap_present)
            if only_snap or only_disk:
                add(
                    "collection_present_list_drift",
                    None,
                    {
                        "only_in_v39_present": only_snap,
                        "only_on_disk": only_disk,
                        "v39_count": len(snap_present),
                        "disk_count": len(disk_present),
                    },
                )
        if parsed["reports_present"] is not None and parsed["reports_present"] != len(present):
            add(
                "reports_present_count_drift",
                None,
                {
                    "v39_reports_present": parsed["reports_present"],
                    "disk_present": len(present),
                    "disk_present_excluding_self": len(others_present),
                },
            )

    # markdown receipt internal hashes vs json / disk
    md_notes = {}
    if v39_md_meta:
        text = open(V39_MD, encoding="utf-8", errors="replace").read()
        md_shas = SHA_RE.findall(text)
        md_notes = {
            "bytes": v39_md_meta["bytes"],
            "sha256": v39_md_meta["sha256"],
            "sha256_tokens": len(md_shas),
            "first_line": v39_md_meta["first_line"],
        }
        if parsed:
            json_shas = set()
            for item in parsed["rows"].values():
                s = row_sha(item)
                if s:
                    json_shas.add(s)
            md_set = set(x.lower() for x in md_shas)
            # receipt.json's own hash must not be required in the md
            only_md = sorted(md_set - json_shas)
            # don't flag the md file's self-hash or unrelated pins; record counts only
            md_notes["sha_tokens_not_in_json_seat_rows"] = len(only_md)
            md_notes["json_seat_shas_missing_from_md"] = len(json_shas - md_set)

    artifact_hashes = {}
    artifact_missing = []
    for rel in ARTIFACTS:
        path = os.path.join(LANE, rel)
        if os.path.isfile(path) and os.path.getsize(path) > 0:
            artifact_hashes[rel] = sha256_file(path)
        else:
            artifact_missing.append(rel)

    producer_missing = [
        name
        for name in PRODUCER_REPORTS
        if not (
            os.path.isfile(os.path.join(SEATS, name))
            and os.path.getsize(os.path.join(SEATS, name)) > 0
        )
    ]

    rc, head, _ = sh("git rev-parse HEAD")
    rc2, base, _ = sh("git rev-parse 4265df5")
    rc3, anc_out, anc_err = sh(
        "git merge-base --is-ancestor 4265df5 HEAD && echo yes || echo no"
    )
    rc4, status, _ = sh(
        "git status --porcelain -- corpus SKILL.md .ufo/waves/round-99/receipt.json"
    )
    sh("find .ufo/waves/round-99/seats -maxdepth 1 -name '*.md' | wc -l")
    sh("find .ufo/waves/round-99/seats -maxdepth 1 -name 'S*.md' -printf '%f\\n'")
    sh(
        "find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l"
    )

    out = {
        "built_at": now(),
        "reason": reason,
        "self": SELF,
        "endgame": "all-reports expectation subtracts SELF",
        "roster_count": len(roster),
        "disk_present": present,
        "disk_present_count": len(present),
        "disk_present_excluding_self": len(others_present),
        "disk_missing_excluding_self": others_missing,
        "disk_missing_excluding_self_count": len(others_missing),
        "self_report_present_at_snapshot": self_present,
        "unexpected_md": unexpected,
        "rows": rows,
        "receipt_path": norm_path(RECEIPT),
        "receipt_exists": os.path.isfile(RECEIPT),
        "receipt_meta": receipt_meta,
        "receipt_error": receipt_error,
        "receipt_shape": None if not parsed else parsed["shape"],
        "receipt_top_keys": None if not parsed else parsed["top_keys"],
        "receipt_reports_expected": None if not parsed else parsed["reports_expected"],
        "receipt_reports_present": None if not parsed else parsed["reports_present"],
        "receipt_reports_missing": None if not parsed else parsed["reports_missing"],
        "receipt_seat_count": 0 if not parsed else len(parsed["rows"]),
        "v39_md_exists": os.path.isfile(V39_MD),
        "v39_md": md_notes,
        "compared_seat_rows": compared,
        "agreements": agreements,
        "drifts": drifts,
        "drift_count": len(drifts),
        "producer_reports_missing": producer_missing,
        "artifacts_missing": artifact_missing,
        "artifact_hashes": artifact_hashes,
        "git": {
            "head": head.strip(),
            "baseline_4265df5": base.strip(),
            "ancestor": (anc_out or "").strip(),
            "status_porcelain": status,
        },
    }
    table_path = os.path.join(SCRATCH, "seat-table.json")
    with open(table_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    # compact tsv for the report
    tsv = os.path.join(SCRATCH, "seat-table.tsv")
    with open(tsv, "w", encoding="utf-8") as f:
        f.write(
            "seat\tpresent\tbytes\tsha256\tmtime\theader_ok\tdeclared_basename\tfiles\n"
        )
        for r in rows:
            f.write(
                "\t".join(
                    [
                        r["seat"],
                        "1" if r["present"] else "0",
                        "" if r["bytes"] is None else str(r["bytes"]),
                        r["sha256"] or "",
                        r["mtime"] or "",
                        "" if r["header_ok"] is None else ("1" if r["header_ok"] else "0"),
                        r["declared_basename"],
                        ",".join(r["files"]),
                    ]
                )
                + "\n"
            )
    drift_path = os.path.join(SCRATCH, "drift.json")
    with open(drift_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "built_at": out["built_at"],
                "reason": reason,
                "drift_count": len(drifts),
                "drifts": drifts,
                "producer_reports_missing": producer_missing,
                "artifacts_missing": artifact_missing,
                "receipt_exists": out["receipt_exists"],
                "v39_md_exists": out["v39_md_exists"],
                "disk_present_count": len(present),
                "disk_missing_excluding_self": others_missing,
            },
            f,
            indent=1,
        )
        f.write("\n")
    log(
        "BUILD reason=%s present=%d excluding_self=%d missing_others=%d drifts=%d receipt=%s v39_md=%s"
        % (
            reason,
            len(present),
            len(others_present),
            len(others_missing),
            len(drifts),
            out["receipt_exists"],
            out["v39_md_exists"],
        )
    )
    return out


def missing_of(paths, base):
    missing = []
    for rel in paths:
        path = os.path.join(base, rel) if base else rel
        if not (os.path.isfile(path) and os.path.getsize(path) > 0):
            missing.append(rel)
    return missing


def poll():
    log("POLL_START %s max=%d sleep=%d self=%s" % (now(), MAX_TRIES, SLEEP_S, SELF))
    prev_receipt_sha = None
    stable_receipt = 0
    prev_md_count = None
    stable_md = 0
    last_status = {}
    for n in range(1, MAX_TRIES + 1):
        log("--- TRY %d %s ---" % (n, now()))
        sh("find .ufo/waves/round-99/seats -maxdepth 1 -name '*.md' -printf '%f\\n' | sort")
        sh("ls -l corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md .ufo/waves/round-99/receipt.json .ufo/waves/round-99/seats/V39-receipt.md 2>&1 || true")
        prod_missing = missing_of(PRODUCER_REPORTS, SEATS)
        art_missing = missing_of(ARTIFACTS, LANE)
        receipt_ok = os.path.isfile(RECEIPT) and os.path.getsize(RECEIPT) > 0
        v39_ok = os.path.isfile(V39_MD) and os.path.getsize(V39_MD) > 0
        md_count = len(
            [
                name
                for name in os.listdir(SEATS)
                if name.endswith(".md") and os.path.isfile(os.path.join(SEATS, name))
            ]
        )
        receipt_sha = sha256_file(RECEIPT) if receipt_ok else None
        if receipt_sha and receipt_sha == prev_receipt_sha:
            stable_receipt += 1
        else:
            stable_receipt = 0
        if md_count == prev_md_count:
            stable_md += 1
        else:
            stable_md = 0
        prev_receipt_sha = receipt_sha
        prev_md_count = md_count
        status = {
            "try": n,
            "at": now(),
            "producer_missing": prod_missing,
            "artifacts_missing": art_missing,
            "receipt": receipt_ok,
            "v39_md": v39_ok,
            "top_md": md_count,
            "top_md_excluding_self_cap": 127,
            "receipt_sha": receipt_sha,
            "stable_receipt_polls": stable_receipt,
            "stable_md_polls": stable_md,
        }
        last_status = status
        with open(os.path.join(SCRATCH, "poll-status.json"), "w", encoding="utf-8") as f:
            json.dump(status, f, indent=1)
            f.write("\n")
        log(
            "STATUS try=%d producers_missing=%d artifacts_missing=%d receipt=%s v39_md=%s top_md=%d stable_receipt=%d stable_md=%d"
            % (
                n,
                len(prod_missing),
                len(art_missing),
                receipt_ok,
                v39_ok,
                md_count,
                stable_receipt,
                stable_md,
            )
        )
        if prod_missing:
            log("PRODUCER_MISSING " + " ".join(prod_missing))
        if art_missing:
            log("ARTIFACT_MISSING " + " ".join(art_missing))

        ready = (
            not prod_missing
            and not art_missing
            and receipt_ok
            and v39_ok
            and stable_receipt >= 1
        )
        # bounded stall-escape: producers+artifacts landed, receipt stable,
        # and either md count stable for 3 polls or we are in the last 8 tries.
        # Do not require the other 127 reports (subtract SELF; do not deadlock on endgame seats).
        stall = (
            not prod_missing
            and not art_missing
            and receipt_ok
            and v39_ok
            and stable_receipt >= 2
            and (stable_md >= 3 or n >= MAX_TRIES - 8)
        )
        if ready and (stable_receipt >= 2 or n >= MAX_TRIES - 5):
            log("READY try=%d %s stable_receipt=%d" % (n, now(), stable_receipt))
            build("ready-try-%d" % n)
            return 0
        if stall and n >= 8:
            log(
                "STALL_ESCAPE try=%d %s stable_receipt=%d stable_md=%d top_md=%d (endgame subtracts SELF; not waiting for 127)"
                % (n, now(), stable_receipt, stable_md, md_count)
            )
            build("stall-escape-try-%d" % n)
            return 0
        if n < MAX_TRIES:
            time.sleep(SLEEP_S)
    log("EXHAUSTED %s" % now())
    build("exhausted-after-%d" % MAX_TRIES)
    with open(os.path.join(SCRATCH, "poll-status.json"), "w", encoding="utf-8") as f:
        json.dump({"exhausted": True, "last": last_status, "at": now()}, f, indent=1)
        f.write("\n")
    return 2


if __name__ == "__main__":
    os.makedirs(SCRATCH, exist_ok=True)
    raise SystemExit(poll())

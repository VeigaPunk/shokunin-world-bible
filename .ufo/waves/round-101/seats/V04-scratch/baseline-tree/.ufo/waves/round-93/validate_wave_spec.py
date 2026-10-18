import argparse
import copy
import json
import sys
import tempfile
from pathlib import Path


BASELINE = "65838f867d6ece8e7b8bdcc4ffc667a08a1b785e"
SCHEMA = "shokunin-wave-spec/v2"
FOLLOWUP_MODEL = "opencode-go/deepseek-v4.1-flash"
WORK_MODEL = "openai-codex/gpt-6-luna-max"
CORRECTIVE_TOOL_CALL_ID = "call_00f870dca2ba4de8bb43ea4358f338c5"
CORRECTIVE_RESULT_SHA256 = "bb03705fc65fdc5a78cfbfa5e641878b4ab72c105797e340a72a74eb75376320"
CORRECTIVE_AGENT_IDS = {
    "R01": "agent-522", "R02": "agent-523", "R03": "agent-524", "R04": "agent-525",
    "R05": "agent-526", "R06": "agent-527", "R07": "agent-528", "R08": "agent-529",
    "R09": "agent-530", "R10": "agent-531", "R11": "agent-532", "R12": "agent-533",
    "R13": "agent-534", "R14": "agent-535", "R15": "agent-536", "R16": "agent-537",
    "R17": "agent-538", "R18": "agent-539", "R19": "agent-540", "R20": "agent-541",
    "R21": "agent-542", "R22": "agent-543", "R23": "agent-544", "R24": "agent-545",
    "R25": "agent-546", "R26": "agent-547", "R27": "agent-548", "R28": "agent-549",
    "R29": "agent-550", "R30": "agent-551", "R31": "agent-552", "R32": "agent-553",
}
INITIAL_WORK_SEATS = 31
CORRECTIVE_WORK_SEATS = 32
AUTHORIZED_WORK_TOTAL = 63
RECEIPT_POLICY = "parent-only-after-actual-results"
SEAT_STATES = {"pending", "failed", "complete"}
PHASE_STATES = SEAT_STATES | {"in_progress"}


def phase_status(seats):
    states = [seat.get("status") for seat in seats if isinstance(seat, dict)]
    if states and all(state == "complete" for state in states):
        return "complete"
    if states and all(state == "pending" for state in states):
        return "pending"
    if states and all(state == "failed" for state in states):
        return "failed"
    return "in_progress"


def safe_report_path(root, value):
    if not isinstance(value, str) or not value:
        return None
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        return None
    root = root.resolve()
    target = (root / relative).resolve()
    try:
        target.relative_to(root)
    except ValueError:
        return None
    return target


def has_result_report_receipt(phase, seat):
    evidence = phase.get("result_evidence") if isinstance(phase, dict) else None
    receipt = seat.get("report_receipt") if isinstance(seat, dict) else None
    return (
        isinstance(evidence, dict)
        and isinstance(receipt, dict)
        and seat.get("status") == "complete"
        and seat.get("result_outcome") == "completed"
        and receipt.get("tool_call_id") == evidence.get("tool_call_id")
        and receipt.get("agent_id") == seat.get("agent_id")
        and receipt.get("outcome") == "completed"
        and receipt.get("result_sha256") == evidence.get("saved_result_sha256")
    )


def validate_phase(phase, root, findings, all_ids, all_reports, expected_kind=None):
    if not isinstance(phase, dict):
        findings.append("phase_invalid")
        return 0

    phase_id = phase.get("id")
    if not isinstance(phase_id, str) or not phase_id:
        phase_id = "unknown"
        findings.append("phase_id_invalid")
    kind = phase.get("kind")
    if expected_kind is not None and kind != expected_kind:
        findings.append(f"phase_kind_invalid:{phase_id}")
    if phase.get("authorization_status") not in {"authorized", "not-authorized"}:
        findings.append(f"authorization_status_invalid:{phase_id}")
    if phase.get("status") not in PHASE_STATES:
        findings.append(f"phase_status_invalid:{phase_id}")
    if phase.get("receipt_update_policy") != RECEIPT_POLICY:
        findings.append(f"receipt_policy_invalid:{phase_id}")

    requested_model = phase.get("requested_model")
    if not isinstance(requested_model, str) or not requested_model:
        findings.append(f"requested_model_missing:{phase_id}")
    verified = phase.get("served_model_independently_verified")
    served_model = phase.get("served_model")
    if verified is True:
        if not isinstance(served_model, str) or not served_model:
            findings.append(f"served_model_receipt_missing:{phase_id}")
        elif served_model != requested_model:
            findings.append(f"served_model_mismatch:{phase_id}")
    elif served_model not in (None, "") and served_model != requested_model:
        findings.append(f"served_model_mismatch:{phase_id}")
    backend_echo = phase.get("served_backend_echo")
    if backend_echo not in (None, "") and backend_echo != requested_model:
        findings.append(f"served_backend_echo_mismatch:{phase_id}")

    seats = phase.get("seats")
    if not isinstance(seats, list) or not seats:
        findings.append(f"phase_seats_missing:{phase_id}")
        return 0

    phase_ids = []
    statuses = []
    for seat in seats:
        if not isinstance(seat, dict):
            findings.append(f"seat_invalid:{phase_id}")
            continue
        seat_id = seat.get("id")
        if not isinstance(seat_id, str) or not seat_id:
            findings.append(f"seat_id_invalid:{phase_id}")
            continue
        phase_ids.append(seat_id)
        if seat_id in all_ids:
            findings.append(f"duplicate_seat_id:{seat_id}")
        all_ids.add(seat_id)

        status = seat.get("status")
        statuses.append(status)
        if status not in SEAT_STATES:
            findings.append(f"seat_status_invalid:{phase_id}:{seat_id}")
        elif status == "failed" and not isinstance(seat.get("failure_reason"), str):
            findings.append(f"failure_reason_missing:{phase_id}:{seat_id}")
        result_receipt_valid = has_result_report_receipt(phase, seat)
        report_path = safe_report_path(root, seat.get("report"))
        if report_path is None:
            if seat.get("report") is not None or not result_receipt_valid:
                findings.append(f"report_path_invalid:{phase_id}:{seat_id}")
                continue
            relative_report = f"agent-result:{phase.get('result_evidence', {}).get('tool_call_id')}:{seat.get('agent_id')}"
        else:
            relative_report = report_path.relative_to(root.resolve()).as_posix()
        if relative_report in all_reports:
            findings.append(f"duplicate_report_path:{relative_report}")
        all_reports.add(relative_report)
        if status == "complete" and report_path is not None and not report_path.is_file() and not result_receipt_valid:
            findings.append(f"required_report_missing:{phase_id}:{seat_id}")

    if not phase_ids:
        findings.append(f"phase_seats_invalid:{phase_id}")
    expected_status = phase_status(seats)
    if phase.get("status") != expected_status:
        findings.append(f"phase_status_mismatch:{phase_id}:expected_{expected_status}")
    if any(status != "complete" for status in statuses):
        findings.append(f"phase_unresolved:{phase_id}")
    return len(seats)


def validate_corrective_result(phase, root, findings, warnings=None):
    phase_id = "corrective-luna-work"
    if not isinstance(phase, dict):
        findings.append("corrective_result_phase_missing")
        return
    evidence = phase.get("result_evidence")
    if not isinstance(evidence, dict):
        findings.append("corrective_result_evidence_missing")
        return
    if phase.get("requested_model") != WORK_MODEL or evidence.get("requested_model") != WORK_MODEL:
        findings.append(f"requested_model_mismatch:{phase_id}")
    if evidence.get("requested_model") != phase.get("requested_model"):
        findings.append(f"requested_model_receipt_mismatch:{phase_id}")
    if evidence.get("tool") != "AgentSwarm" or evidence.get("tool_call_id") != CORRECTIVE_TOOL_CALL_ID:
        findings.append(f"corrective_result_call_mismatch:{phase_id}")
    if evidence.get("saved_result_sha256") != CORRECTIVE_RESULT_SHA256:
        findings.append(f"corrective_result_hash_mismatch:{phase_id}")
    if not isinstance(evidence.get("saved_result_path"), str) or not evidence.get("saved_result_path"):
        findings.append(f"corrective_result_path_missing:{phase_id}")

    backend_echo = evidence.get("served_backend_echo")
    if backend_echo in (None, ""):
        if warnings is not None:
            warnings.append(f"served_backend_echo_unknown:{phase_id}")
    elif backend_echo != phase.get("requested_model"):
        findings.append(f"served_backend_echo_mismatch:{phase_id}")

    seats = phase.get("seats") if isinstance(phase.get("seats"), list) else []
    seen_agents = set()
    outcome_counts = {"requested": len(seats), "completed": 0, "failed": 0}
    for seat in seats:
        if not isinstance(seat, dict):
            continue
        seat_id = seat.get("id")
        agent_id = seat.get("agent_id")
        expected_agent = CORRECTIVE_AGENT_IDS.get(seat_id)
        if not isinstance(agent_id, str) or not agent_id:
            findings.append(f"corrective_agent_id_missing:{seat_id}")
        else:
            if agent_id in seen_agents:
                findings.append(f"duplicate_agent_id:{agent_id}")
            seen_agents.add(agent_id)
            if agent_id != expected_agent:
                findings.append(f"corrective_agent_id_mismatch:{seat_id}")
        outcome = seat.get("result_outcome")
        if outcome not in {"completed", "failed"}:
            findings.append(f"corrective_result_outcome_invalid:{seat_id}")
        elif outcome == "completed":
            outcome_counts["completed"] += 1
            if seat.get("status") != "complete":
                findings.append(f"corrective_result_status_mismatch:{seat_id}")
        else:
            outcome_counts["failed"] += 1
            if seat.get("status") != "failed":
                findings.append(f"corrective_result_status_mismatch:{seat_id}")

    if evidence.get("reported_counts") != outcome_counts:
        findings.append(f"corrective_result_counts_mismatch:{phase_id}")
    if outcome_counts != {"requested": 32, "completed": 32, "failed": 0}:
        findings.append(f"corrective_actual_counts_mismatch:{phase_id}")

    dispatch_path = root / "recovery" / "work-dispatch.json"
    try:
        dispatch = json.loads(dispatch_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        findings.append("corrective_dispatch_receipt_unreadable")
        return
    dispatch_evidence = dispatch.get("actual_result_receipt") if isinstance(dispatch, dict) else None
    if not isinstance(dispatch_evidence, dict):
        findings.append("corrective_dispatch_receipt_unreadable")
        return
    if (
        dispatch_evidence.get("tool") != evidence.get("tool")
        or dispatch_evidence.get("tool_call_id") != evidence.get("tool_call_id")
        or dispatch_evidence.get("saved_result_path") != evidence.get("saved_result_path")
        or dispatch_evidence.get("saved_result_sha256") != evidence.get("saved_result_sha256")
        or dispatch_evidence.get("counts") != evidence.get("reported_counts")
        or dispatch_evidence.get("requested_model") != evidence.get("requested_model")
        or dispatch_evidence.get("served_backend_echo") != backend_echo
    ):
        findings.append("corrective_dispatch_receipt_mismatch")
    dispatch_seats = dispatch_evidence.get("seat_receipts")
    if not isinstance(dispatch_seats, list) or len(dispatch_seats) != len(seats):
        findings.append("corrective_dispatch_seat_count_mismatch")
    else:
        dispatch_by_id = {seat.get("seat_id"): seat for seat in dispatch_seats if isinstance(seat, dict)}
        if len(dispatch_by_id) != len(dispatch_seats):
            findings.append("corrective_dispatch_duplicate_seat_id")
        for seat in seats:
            if not isinstance(seat, dict):
                continue
            seat_id = seat.get("id")
            row = dispatch_by_id.get(seat_id)
            if not isinstance(row, dict) or (
                row.get("agent_id") != seat.get("agent_id")
                or row.get("status") != seat.get("status")
            ):
                findings.append(f"corrective_dispatch_seat_mismatch:{seat_id}")
                continue
            if seat.get("report") is None:
                if row.get("report_result_record") != seat.get("agent_id"):
                    findings.append(f"corrective_dispatch_report_receipt_mismatch:{seat_id}")
            else:
                report_path = row.get("report_path")
                suffix = f"/{seat.get('report')}"
                if not isinstance(report_path, str) or not (
                    report_path == seat.get("report") or report_path.endswith(suffix)
                ):
                    findings.append(f"corrective_dispatch_report_path_mismatch:{seat_id}")


def validate_spec(spec, reports_root, warnings=None):
    findings = []
    warnings = warnings if warnings is not None else []
    if not isinstance(spec, dict):
        return ["spec_invalid"], 0
    if spec.get("schema") != SCHEMA:
        findings.append("schema_mismatch")
    if spec.get("round") != 93:
        findings.append("round_mismatch")
    if spec.get("baseline_commit") != BASELINE:
        findings.append("baseline_mismatch")
    if spec.get("receipt_update_policy") != RECEIPT_POLICY:
        findings.append("receipt_policy_invalid:spec")

    all_ids = set()
    all_reports = set()
    authorized_work_total = 0
    work_phases = spec.get("work_phases")
    if not isinstance(work_phases, list) or not work_phases:
        findings.append("work_phases_missing")
        work_phases = []
    phase_ids = set()
    phases_by_id = {}
    for phase in work_phases:
        if isinstance(phase, dict):
            phase_id = phase.get("id")
            if isinstance(phase_id, str):
                if phase_id in phase_ids:
                    findings.append(f"duplicate_phase_id:{phase_id}")
                phase_ids.add(phase_id)
                phases_by_id[phase_id] = phase
        count = validate_phase(phase, reports_root, findings, all_ids, all_reports, "WORK")
        if isinstance(phase, dict) and phase.get("authorization_status") == "authorized":
            authorized_work_total += count

    if len(work_phases) != 2:
        findings.append(f"work_phase_count_mismatch:{len(work_phases)}")
    initial_phase = phases_by_id.get("initial-luna-work")
    initial_seats = initial_phase.get("seats") if isinstance(initial_phase, dict) else None
    if not isinstance(initial_seats, list) or len(initial_seats) != INITIAL_WORK_SEATS:
        actual = len(initial_seats) if isinstance(initial_seats, list) else "invalid"
        findings.append(f"initial_work_seat_count:{actual}:expected_{INITIAL_WORK_SEATS}")
    corrective_phase = phases_by_id.get("corrective-luna-work")
    corrective_seats = corrective_phase.get("seats") if isinstance(corrective_phase, dict) else None
    if not isinstance(corrective_seats, list) or len(corrective_seats) != CORRECTIVE_WORK_SEATS:
        actual = len(corrective_seats) if isinstance(corrective_seats, list) else "invalid"
        findings.append(f"corrective_work_seat_count:{actual}:expected_{CORRECTIVE_WORK_SEATS}")
    elif [seat.get("id") if isinstance(seat, dict) else None for seat in corrective_seats] != [
        f"R{index:02d}" for index in range(1, CORRECTIVE_WORK_SEATS + 1)
    ]:
        findings.append("corrective_work_slot_ids_mismatch")
    validate_corrective_result(corrective_phase, reports_root, findings, warnings)

    expected_total = spec.get("authorized_work_seat_total")
    seat_range = spec.get("authorized_work_seat_range")
    if not isinstance(seat_range, dict):
        findings.append("authorized_work_range_missing")
        seat_range = {"min": 32, "max": 64}
    minimum = seat_range.get("min")
    maximum = seat_range.get("max")
    if not isinstance(minimum, int) or not isinstance(maximum, int) or minimum > maximum:
        findings.append("authorized_work_range_invalid")
    elif not minimum <= authorized_work_total <= maximum:
        findings.append(f"authorized_work_total_out_of_range:{authorized_work_total}")
    if authorized_work_total != AUTHORIZED_WORK_TOTAL:
        findings.append(f"authorized_work_total_expected:{authorized_work_total}:expected_{AUTHORIZED_WORK_TOTAL}")
    if expected_total != authorized_work_total:
        findings.append(f"authorized_work_total_mismatch:{authorized_work_total}")

    followup = spec.get("required_followup")
    if not isinstance(followup, dict):
        findings.append("required_followup_missing")
    else:
        if followup.get("id") in phase_ids:
            findings.append(f"duplicate_phase_id:{followup.get('id')}")
        if followup.get("kind") != "FOLLOW-UP":
            findings.append("required_followup_kind_invalid")
        if followup.get("authorization_status") != "authorized":
            findings.append("required_followup_not_authorized")
        if followup.get("requested_model") != FOLLOWUP_MODEL:
            findings.append("required_followup_model_mismatch")
        seats = followup.get("seats")
        if not isinstance(seats, list) or len(seats) != 32:
            actual = len(seats) if isinstance(seats, list) else "invalid"
            findings.append(f"required_followup_seat_count:{actual}:expected_32")
        else:
            expected_ids = [f"F{index:02d}" for index in range(1, 33)]
            actual_ids = [seat.get("id") if isinstance(seat, dict) else None for seat in seats]
            if actual_ids != expected_ids:
                findings.append("required_followup_slot_ids_mismatch")
        validate_phase(followup, reports_root, findings, all_ids, all_reports, "FOLLOW-UP")

    attempts = spec.get("prior_followup_attempts")
    if not isinstance(attempts, list):
        findings.append("prior_followup_attempts_missing")
        attempts = []
    attempts_by_id = {item.get("id"): item for item in attempts if isinstance(item, dict)}
    deepseek = attempts_by_id.get("original-deepseek-transport-attempt")
    if not isinstance(deepseek, dict) or not (
        deepseek.get("status") == "failed"
        and deepseek.get("seat_count") == 31
        and deepseek.get("failure_class") == "transport"
        and deepseek.get("counts_as_required_followup") is False
    ):
        findings.append("prior_deepseek_transport_accounting_invalid")
    glm = attempts_by_id.get("glm-preliminary-batch")
    if not isinstance(glm, dict) or not (
        glm.get("status") == "ineligible"
        and glm.get("seat_count") == 33
        and glm.get("results") == {"complete": 32, "failed": 1}
        and glm.get("counts_as_required_followup") is False
    ):
        findings.append("glm_preliminary_accounting_invalid")

    if not findings:
        findings.append("closure_ready")
    return findings, authorized_work_total


def fixture_spec(root):
    initial_seats = []
    corrective_seats = []
    followup_seats = []
    dispatch_seats = []
    for index in range(1, INITIAL_WORK_SEATS + 1):
        seat_id = f"I{index:02d}"
        report = f"work/initial/{seat_id}.md"
        path = root / report
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("isolated self-test receipt\n", encoding="utf-8")
        initial_seats.append({"id": seat_id, "status": "complete", "report": report})
    for index in range(1, CORRECTIVE_WORK_SEATS + 1):
        seat_id = f"R{index:02d}"
        agent_id = CORRECTIVE_AGENT_IDS[seat_id]
        report = None if seat_id in {"R23", "R29", "R31"} else f"work/corrective/{seat_id}.md"
        seat = {
            "id": seat_id,
            "status": "complete",
            "agent_id": agent_id,
            "result_outcome": "completed",
            "report": report,
        }
        if report is None:
            seat["report_receipt"] = {
                "tool_call_id": CORRECTIVE_TOOL_CALL_ID,
                "agent_id": agent_id,
                "outcome": "completed",
                "result_sha256": CORRECTIVE_RESULT_SHA256,
            }
            dispatch_seats.append({
                "seat_id": seat_id,
                "agent_id": agent_id,
                "status": "complete",
                "report_path": None,
                "report_result_record": agent_id,
            })
        else:
            path = root / report
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("isolated self-test receipt\n", encoding="utf-8")
            dispatch_seats.append({
                "seat_id": seat_id,
                "agent_id": agent_id,
                "status": "complete",
                "report_path": report,
            })
        corrective_seats.append(seat)
    for index in range(1, 33):
        seat_id = f"F{index:02d}"
        report = f"deepseek/{seat_id}.md"
        path = root / report
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("isolated self-test receipt\n", encoding="utf-8")
        followup_seats.append({"id": seat_id, "status": "complete", "report": report})

    model = "self-test-requested-model"
    phase_fields = {
        "authorization_status": "authorized",
        "status": "complete",
        "requested_model": model,
        "served_model": model,
        "served_model_independently_verified": True,
        "receipt_update_policy": RECEIPT_POLICY,
    }
    corrective_fields = {
        "authorization_status": "authorized",
        "status": "complete",
        "requested_model": WORK_MODEL,
        "served_model": None,
        "served_model_independently_verified": False,
        "served_backend_echo": None,
        "receipt_update_policy": RECEIPT_POLICY,
        "result_evidence": {
            "tool": "AgentSwarm",
            "tool_call_id": CORRECTIVE_TOOL_CALL_ID,
            "saved_result_path": "/self-test/tool-results/corrective.txt",
            "saved_result_sha256": CORRECTIVE_RESULT_SHA256,
            "reported_counts": {"requested": 32, "completed": 32, "failed": 0},
            "requested_model": WORK_MODEL,
            "served_backend_echo": None,
        },
    }
    receipt = {
        "tool": "AgentSwarm",
        "tool_call_id": CORRECTIVE_TOOL_CALL_ID,
        "saved_result_path": "/self-test/tool-results/corrective.txt",
        "saved_result_sha256": CORRECTIVE_RESULT_SHA256,
        "counts": {"requested": 32, "completed": 32, "failed": 0},
        "requested_model": WORK_MODEL,
        "served_backend_echo": None,
        "seat_receipts": dispatch_seats,
    }
    recovery = root / "recovery"
    recovery.mkdir(parents=True, exist_ok=True)
    (recovery / "work-dispatch.json").write_text(
        json.dumps({"actual_result_receipt": receipt}), encoding="utf-8"
    )
    return {
        "schema": SCHEMA,
        "round": 93,
        "baseline_commit": BASELINE,
        "receipt_update_policy": RECEIPT_POLICY,
        "authorized_work_seat_total": AUTHORIZED_WORK_TOTAL,
        "authorized_work_seat_range": {"min": 32, "max": 64},
        "work_phases": [
            {"id": "initial-luna-work", "kind": "WORK", "seats": initial_seats, **phase_fields},
            {"id": "corrective-luna-work", "kind": "WORK", "seats": corrective_seats, **corrective_fields},
        ],
        "required_followup": {
            "id": "fresh-deepseek-followup",
            "kind": "FOLLOW-UP",
            "seats": followup_seats,
            **{**phase_fields, "requested_model": FOLLOWUP_MODEL, "served_model": FOLLOWUP_MODEL},
        },
        "prior_followup_attempts": [
            {
                "id": "original-deepseek-transport-attempt",
                "status": "failed",
                "seat_count": 31,
                "failure_class": "transport",
                "counts_as_required_followup": False,
            },
            {
                "id": "glm-preliminary-batch",
                "status": "ineligible",
                "seat_count": 33,
                "results": {"complete": 32, "failed": 1},
                "counts_as_required_followup": False,
            },
        ],
    }


def run_self_tests():
    cases = []
    with tempfile.TemporaryDirectory(prefix="lore-r93-wave-selftest-") as directory:
        root = Path(directory)
        base = fixture_spec(root)
        warnings = []
        findings, _ = validate_spec(base, root, warnings)
        cases.append(("closure_ready", 0, "closure_ready", findings))
        warning_ok = warnings == ["served_backend_echo_unknown:corrective-luna-work"]

        count_mismatch = copy.deepcopy(base)
        count_mismatch["work_phases"][1]["result_evidence"]["reported_counts"]["completed"] = 31
        findings, _ = validate_spec(count_mismatch, root)
        cases.append((
            "corrective_result_counts_mismatch:corrective-luna-work",
            1,
            "corrective_result_counts_mismatch:corrective-luna-work",
            findings,
        ))

        model_mismatch = copy.deepcopy(base)
        model_mismatch["work_phases"][1]["result_evidence"]["requested_model"] = "wrong-model"
        findings, _ = validate_spec(model_mismatch, root)
        cases.append((
            "requested_model_mismatch:corrective-luna-work",
            1,
            "requested_model_mismatch:corrective-luna-work",
            findings,
        ))

        echo_mismatch = copy.deepcopy(base)
        echo_mismatch["work_phases"][1]["result_evidence"]["served_backend_echo"] = "wrong-model"
        findings, _ = validate_spec(echo_mismatch, root)
        cases.append((
            "served_backend_echo_mismatch:corrective-luna-work",
            1,
            "served_backend_echo_mismatch:corrective-luna-work",
            findings,
        ))

        duplicate = copy.deepcopy(base)
        duplicate["work_phases"][0]["seats"].append(copy.deepcopy(duplicate["work_phases"][0]["seats"][0]))
        findings, _ = validate_spec(duplicate, root)
        cases.append(("duplicate_seat_id:I01", 1, "duplicate_seat_id:I01", findings))

        missing = copy.deepcopy(base)
        missing["work_phases"][0]["seats"][0]["report"] = "missing/I01.md"
        findings, _ = validate_spec(missing, root)
        cases.append(("required_report_missing:initial-luna-work:I01", 1, "required_report_missing:initial-luna-work:I01", findings))

        pending = copy.deepcopy(base)
        pending["required_followup"]["seats"][0]["status"] = "pending"
        pending["required_followup"]["status"] = "in_progress"
        findings, _ = validate_spec(pending, root)
        cases.append(("phase_unresolved:fresh-deepseek-followup", 1, "phase_unresolved:fresh-deepseek-followup", findings))

        failed_seat = copy.deepcopy(base)
        failed_seat["required_followup"]["seats"][0]["status"] = "failed"
        failed_seat["required_followup"]["status"] = "in_progress"
        findings, _ = validate_spec(failed_seat, root)
        cases.append(("failure_reason_missing:fresh-deepseek-followup:F01", 1, "failure_reason_missing:fresh-deepseek-followup:F01", findings))

    failed = False
    for label, expected_exit, expected_id, findings in cases:
        observed_exit = 0 if findings == ["closure_ready"] else 1
        observed_id = findings[0] if findings else "no_finding"
        passed = observed_exit == expected_exit and observed_id == expected_id
        print(
            f"{'PASS' if passed else 'FAIL'} selftest:{label} "
            f"expected_id={expected_id} expected_exit={expected_exit} "
            f"observed_id={observed_id} observed_exit={observed_exit}"
        )
        failed |= not passed
    print(
        f"{'PASS' if warning_ok else 'FAIL'} selftest:unknown_backend_echo_is_warning "
        f"observed_warning={warning_ok} closure_findings=closure_ready"
    )
    failed |= not warning_ok
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(description="Validate round-93 phase accounting and closure receipts.")
    parser.add_argument("--spec", type=Path, help="wave-spec.json; defaults beside this script")
    parser.add_argument("--self-test", action="store_true", help="run isolated fixtures with pinned IDs and exits")
    args = parser.parse_args()
    if args.self_test:
        return run_self_tests()

    spec_path = args.spec or Path(__file__).resolve().with_name("wave-spec.json")
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL input_error:{exc}", file=sys.stderr)
        return 1

    warnings = []
    findings, authorized_work_total = validate_spec(spec, spec_path.resolve().parent, warnings)
    print(f"authorized_work_seat_total={authorized_work_total} allowed=32..64")
    for warning in warnings:
        print(f"WARN {warning}")
    if findings == ["closure_ready"]:
        print("PASS closure_ready")
        print("CLOSURE_GATE=PASS")
        return 0
    for finding in findings:
        print(f"FAIL {finding}")
    print("CLOSURE_GATE=FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

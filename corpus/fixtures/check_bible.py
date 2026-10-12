#!/usr/bin/env python3
"""Validate a small cited fictional-world bible; report, never resolve, contradictions."""
import argparse
import json
from pathlib import Path

KINDS = {'character', 'place', 'faction', 'item'}
FIELDS = {
    'sources': {'id': str, 'title': str, 'kind': str, 'reliability_note': str},
    'entities': {'id': str, 'kind': str, 'name': str, 'first_appearance': str, 'claims': list},
    'relations': {'from': str, 'to': str, 'type': str, 'source_id': str},
    'timeline': {'id': str, 'tick': int, 'entity_id': str, 'place_id': str,
                 'depends_on': list, 'description': str, 'source_id': str},
    'contradictions': {'id': str, 'claim_a': dict, 'claim_b': dict, 'why': str},
}


def check(directory):
    errors = []
    data = {}
    for section, fields in FIELDS.items():
        path = directory / (section + '.json')
        try:
            rows = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f'{path.name}: cannot load JSON: {exc}')
            rows = []
        if not isinstance(rows, list):
            errors.append(f'{path.name}: expected array')
            rows = []
        data[section] = []
        for index, row in enumerate(rows):
            location = f'{section}[{index}]'
            if not isinstance(row, dict):
                errors.append(f'{location}: expected object')
                continue
            valid = True
            for field, expected in fields.items():
                if field not in row or type(row[field]) is not expected or (expected is str and not row[field].strip()):
                    errors.append(f'{location}.{field}: required nonempty {expected.__name__}')
                    valid = False
            if valid:
                data[section].append((location, row))

    def index(section):
        result = {}
        for location, row in data[section]:
            if row['id'] in result:
                errors.append(f'{location}.id: duplicate {section} id {row["id"]!r}')
            result[row['id']] = row
        return result

    sources = index('sources')
    source_id_counts = {}
    for _, source_row in data['sources']:
        source_id_counts[source_row['id']] = source_id_counts.get(source_row['id'], 0) + 1
    entities = index('entities')
    events = index('timeline')
    index('contradictions')
    event_id_counts = {}
    for _, event in data['timeline']:
        event_id_counts[event['id']] = event_id_counts.get(event['id'], 0) + 1

    def source_status(source_id):
        count = source_id_counts.get(source_id, 0)
        return 'unknown' if count == 0 else 'unique' if count == 1 else 'ambiguous'

    def source(source_id, location):
        status = source_status(source_id)
        if status == 'unknown':
            errors.append(f'{location}: unknown in-world source {source_id!r}')
        elif status == 'ambiguous':
            errors.append(f'{location}: ambiguous in-world source {source_id!r}')
        return status

    allowed_assertion_fields = {'place_id', 'tick', 'depends_on'}
    for location, row in data['contradictions']:
        for side_name in ('claim_a', 'claim_b'):
            side = row[side_name]
            side_location = f'{location}.{side_name}'
            if not isinstance(side, dict):
                errors.append(f'{side_location}: expected object with event_id and field')
                continue
            event_id = side.get('event_id')
            field = side.get('field')
            if not isinstance(event_id, str) or not event_id.strip():
                errors.append(f'{side_location}.event_id: required nonempty string')
                continue
            if not isinstance(field, str) or field not in allowed_assertion_fields:
                errors.append(f'{side_location}.field: expected one of {sorted(allowed_assertion_fields)}')
                continue
            if event_id_counts.get(event_id, 0) != 1:
                errors.append(f'{side_location}.event_id: expected exactly one timeline event {event_id!r}')
                continue
            event = events[event_id]
            event_source_status = source_status(event['source_id'])
            if event_source_status == 'unknown':
                errors.append(f'{side_location}: event {event_id!r} has no resolvable source_id')
            elif event_source_status == 'ambiguous':
                source(event['source_id'], side_location + '.source_id')
        claim_a, claim_b = row['claim_a'], row['claim_b']
        if (isinstance(claim_a, dict) and isinstance(claim_b, dict)
                and claim_a.get('event_id') == claim_b.get('event_id')
                and claim_a.get('field') == claim_b.get('field')):
            errors.append(f'{location}: claim_a and claim_b references must differ')

    for location, row in data['entities']:
        if row['kind'] not in KINDS:
            errors.append(f'{location}.kind: unknown kind {row["kind"]!r}')
        source(row['first_appearance'], location + '.first_appearance')
        for i, claim in enumerate(row['claims']):
            label = f'{location}.claims[{i}]'
            if not isinstance(claim, dict) or not isinstance(claim.get('statement'), str) or not claim['statement'].strip() or not isinstance(claim.get('source_id'), str):
                errors.append(f'{label}: expected nonempty statement and source_id')
            else:
                source(claim['source_id'], label + '.source_id')

    for location, row in data['relations']:
        for endpoint in ('from', 'to'):
            if row[endpoint] not in entities:
                errors.append(f'{location}.{endpoint}: dangling entity {row[endpoint]!r}')
        source(row['source_id'], location + '.source_id')

    # Only distinct, resolvable faction pairs participate; self-edges are out of scope.
    entity_id_counts = {}
    for _, entity in data['entities']:
        entity_id_counts[entity['id']] = entity_id_counts.get(entity['id'], 0) + 1

    for location, item in data['entities']:
        if 'provenance' not in item:
            continue
        label = location + '.provenance'
        records = item['provenance']
        if item['kind'] != 'item':
            errors.append(f'{label}: only valid on item entities')
        if not isinstance(records, list):
            errors.append(f'{label}: expected array')
            continue
        previous_holder = None
        previous_tick = None
        can_check_chain = item['kind'] == 'item' and entity_id_counts[item['id']] == 1
        chain_has_ambiguous_source = False
        for i, record in enumerate(records):
            record_label = f'{label}[{i}]'
            if not isinstance(record, dict):
                errors.append(f'{record_label}: expected object')
                previous_holder = previous_tick = None
                can_check_chain = False
                continue
            expected_keys = {'tick', 'from_holder', 'to_holder', 'source_id'}
            if set(record) != expected_keys:
                errors.append(f'{record_label}: expected exactly tick, from_holder, to_holder, source_id')
                previous_holder = previous_tick = None
                can_check_chain = False
                continue
            tick = record['tick']
            from_holder = record['from_holder']
            to_holder = record['to_holder']
            source_id = record['source_id']
            valid = True
            if type(tick) is not int or tick < 0:
                errors.append(f'{record_label}.tick: required nonnegative integer')
                valid = False
            if from_holder is not None and (not isinstance(from_holder, str) or not from_holder.strip()):
                errors.append(f'{record_label}.from_holder: required null or nonempty entity id')
                valid = False
            if not isinstance(to_holder, str) or not to_holder.strip():
                errors.append(f'{record_label}.to_holder: required nonempty entity id')
                valid = False
            elif entity_id_counts.get(to_holder, 0) == 0:
                errors.append(f'{record_label}.to_holder: dangling entity {to_holder!r}')
                valid = False
            elif entity_id_counts[to_holder] != 1:
                valid = False
            if from_holder is not None:
                if not isinstance(from_holder, str) or not from_holder.strip():
                    valid = False
                elif entity_id_counts.get(from_holder, 0) == 0:
                    errors.append(f'{record_label}.from_holder: dangling entity {from_holder!r}')
                    valid = False
                elif entity_id_counts[from_holder] != 1:
                    valid = False
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append(f'{record_label}.source_id: required nonempty source id')
                valid = False
            else:
                citation_status = source(source_id, record_label + '.source_id')
                if citation_status == 'unknown':
                    valid = False
                elif citation_status == 'ambiguous':
                    chain_has_ambiguous_source = True
            if not valid:
                previous_holder = previous_tick = None
                can_check_chain = False
                continue
            if can_check_chain:
                if previous_tick is not None:
                    if tick <= previous_tick:
                        errors.append(f'{record_label}.tick: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance tick {tick} must be greater than previous tick {previous_tick}')
                    if from_holder != previous_holder:
                        errors.append(f'{record_label}: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance chain break; expected from_holder {previous_holder!r}, got {from_holder!r}')
                elif from_holder is not None:
                    errors.append(f'{record_label}: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance chain break; first record must have from_holder null')
            previous_holder = to_holder
            previous_tick = tick

    allied = [row for _, row in data['relations'] if row['type'] == 'allied_with']
    for location, row in data['relations']:
        left, right = row['from'], row['to']
        if row['type'] != 'allied_with' or left == right:
            continue
        if (left not in entities or right not in entities
                or entity_id_counts[left] != 1 or entity_id_counts[right] != 1
                or entities[left]['kind'] != 'faction' or entities[right]['kind'] != 'faction'):
            continue
        reciprocal = any(
            candidate['from'] == right and candidate['to'] == left
            and candidate['type'] == 'allied_with'
            and source_status(candidate['source_id']) == 'unique'
            for candidate in allied
        )
        if not reciprocal:
            errors.append(f'{location}: allied_with faction relation {left!r} -> {right!r} lacks a sourced reciprocal relation')

    occupied = {}
    for location, row in data['timeline']:
        for field in ('entity_id', 'place_id'):
            if row[field] not in entities:
                errors.append(f'{location}.{field}: dangling entity {row[field]!r}')
        if row['place_id'] in entities and entities[row['place_id']]['kind'] != 'place':
            errors.append(f'{location}.place_id: not a place {row["place_id"]!r}')
        source(row['source_id'], location + '.source_id')
        if row['tick'] < 0:
            errors.append(f'{location}.tick: must be nonnegative')
        if not all(isinstance(dep, str) for dep in row['depends_on']):
            errors.append(f'{location}.depends_on: expected event-id strings')
            continue
        slot = (row['entity_id'], row['tick'])
        if slot in occupied and occupied[slot][1] != row['place_id']:
            previous, prior_place = occupied[slot]
            errors.append(f'{location}: double-booked {row["entity_id"]!r} at tick {row["tick"]} in {previous} ({prior_place!r}) and {row["place_id"]!r}')
        else:
            occupied[slot] = (location, row['place_id'])
        for dep in row['depends_on']:
            if dep not in events:
                errors.append(f'{location}.depends_on: unknown event {dep!r}')
            elif events[dep]['tick'] >= row['tick']:
                errors.append(f'{location}.depends_on: timeline inversion {dep!r} tick {events[dep]["tick"]} not before {row["id"]!r} tick {row["tick"]}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bible', type=Path, help='directory with sources, entities, relations, timeline JSON arrays')
    args = parser.parse_args()
    violations = check(args.bible)
    for violation in violations:
        print('VIOLATION:', violation)
    if violations:
        print(f'{len(violations)} violation(s); no canon changed')
        raise SystemExit(1)
    print('CLEAN: schema, citations, relations, timeline; 0 violations')

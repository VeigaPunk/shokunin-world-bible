#!/usr/bin/env python3
"""Validate a small cited fictional-world bible; report, never resolve, contradictions."""
import argparse
import json
from pathlib import Path

KINDS = {'character', 'place', 'faction', 'item'}


class DuplicateMemberError(ValueError):
    def __init__(self, name):
        self.name = name
        super().__init__(name)


def unique_object(pairs):
    result = {}
    for name, value in pairs:
        if name in result:
            raise DuplicateMemberError(name)
        result[name] = value
    return result


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
    raw_entity_id_counts = {}
    raw_source_id_counts = {}
    entities_available = False
    sources_available = False
    timeline_available = False
    for section, fields in FIELDS.items():
        path = directory / (section + '.json')
        loaded = True
        try:
            rows = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
        except DuplicateMemberError as exc:
            errors.append(f"{path.name}: duplicate object member {exc.name!r}; cannot load JSON")
            rows = []
            loaded = False
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f'{path.name}: cannot load JSON: {exc}')
            rows = []
            loaded = False
        if not isinstance(rows, list):
            errors.append(f'{path.name}: expected array')
            rows = []
            loaded = False
        if section == 'entities' and loaded:
            entities_available = True
        elif section == 'sources' and loaded:
            sources_available = True
        elif section == 'timeline' and loaded:
            timeline_available = True
        data[section] = []
        for index, row in enumerate(rows):
            location = f'{section}[{index}]'
            if not isinstance(row, dict):
                errors.append(f'{location}: expected object')
                continue
            if section in ('entities', 'sources'):
                identifier = row.get('id')
                raw_id_counts = raw_entity_id_counts if section == 'entities' else raw_source_id_counts
                if isinstance(identifier, str) and identifier.strip():
                    raw_id_counts[identifier] = raw_id_counts.get(identifier, 0) + 1
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
        if not sources_available:
            return 'unavailable'
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
            if not timeline_available:
                errors.append(f'{side_location}.event_id: cannot assess event {event_id!r}: timeline.json unavailable')
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
            if not isinstance(claim, dict) or not isinstance(claim.get('statement'), str) or not claim['statement'].strip() or not isinstance(claim.get('source_id'), str) or not claim['source_id'].strip():
                errors.append(f'{label}: expected nonempty statement and source_id')
            else:
                source(claim['source_id'], label + '.source_id')

    # Only distinct, resolvable faction pairs participate; self-edges are out of scope.
    entity_id_counts = {}
    for _, entity in data['entities']:
        entity_id_counts[entity['id']] = entity_id_counts.get(entity['id'], 0) + 1

    def holder_identity_detail(holder_id, reference):
        if holder_id is None:
            return None
        raw_count = raw_entity_id_counts.get(holder_id, 0)
        indexed_count = entity_id_counts.get(holder_id, 0)
        if raw_count == 1 and indexed_count == 1:
            return None
        return f'{reference} {holder_id!r} is not uniquely resolvable ({raw_count} raw entity rows carry this id, but only {indexed_count} is in the resolved index)'

    for location, row in data['relations']:
        if entities_available:
            for endpoint in ('from', 'to'):
                entity_id = row[endpoint]
                if entity_id not in entities:
                    errors.append(f'{location}.{endpoint}: dangling entity {entity_id!r}')
                elif entity_id_counts[entity_id] > 1:
                    errors.append(f'{location}.{endpoint}: ambiguous entity {entity_id!r}')
        source(row['source_id'], location + '.source_id')

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
        first_stop = None
        if not sources_available:
            first_stop = ('source table unavailable', label)
        elif item['kind'] != 'item':
            first_stop = ('provenance attached to a non-item entity', label)
        elif entity_id_counts[item['id']] != 1:
            first_stop = (f'duplicate item id {item["id"]!r}', label)
        chain_has_ambiguous_source = False

        def report_unassessed(record_label):
            cause, origin_label = first_stop
            errors.append(f'{record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: {cause} at {origin_label}')

        for i, record in enumerate(records):
            record_label = f'{label}[{i}]'
            disclosure_emitted = first_stop is not None
            if disclosure_emitted:
                report_unassessed(record_label)
            if not isinstance(record, dict):
                errors.append(f'{record_label}: expected object')
                previous_holder = previous_tick = None
                if first_stop is None:
                    first_stop = ('malformed record (expected object)', record_label)
                    report_unassessed(record_label)
                continue
            expected_keys = {'tick', 'from_holder', 'to_holder', 'source_id'}
            if set(record) != expected_keys:
                errors.append(f'{record_label}: expected exactly tick, from_holder, to_holder, source_id')
                ambiguous_holder_references = []
                for field in ('to_holder', 'from_holder'):
                    holder_id = record.get(field)
                    has_holder_id = isinstance(holder_id, str) and bool(holder_id.strip())
                    if field == 'from_holder' and holder_id is None:
                        has_holder_id = False
                    if has_holder_id and entity_id_counts.get(holder_id, 0) > 1:
                        errors.append(f'{record_label}.{field}: ambiguous entity {holder_id!r}')
                        ambiguous_holder_references.append((field, holder_id))
                previous_holder = previous_tick = None
                if first_stop is None:
                    if ambiguous_holder_references:
                        cause = ', '.join(
                            f'{field} {holder_id!r}'
                            for field, holder_id in ambiguous_holder_references
                        )
                        first_stop = (
                            f'malformed record (unexpected field set); ambiguous holder identity {cause}',
                            record_label,
                        )
                    else:
                        first_stop = ('malformed record (unexpected field set)', record_label)
                    report_unassessed(record_label)
                continue
            tick = record['tick']
            from_holder = record['from_holder']
            to_holder = record['to_holder']
            source_id = record['source_id']
            valid = True
            record_holder_ambiguous = False
            ambiguous_holder_references = []
            record_stop_causes = []
            if type(tick) is not int or tick < 0:
                errors.append(f'{record_label}.tick: required nonnegative integer')
                valid = False
                record_stop_causes.append('malformed record (invalid tick)')
            if from_holder is not None and (not isinstance(from_holder, str) or not from_holder.strip()):
                errors.append(f'{record_label}.from_holder: required null or nonempty entity id')
                valid = False
                record_stop_causes.append('malformed record (invalid from_holder)')
            if not isinstance(to_holder, str) or not to_holder.strip():
                errors.append(f'{record_label}.to_holder: required nonempty entity id')
                valid = False
                record_stop_causes.append('malformed record (invalid to_holder)')
            elif entity_id_counts.get(to_holder, 0) == 0:
                errors.append(f'{record_label}.to_holder: dangling entity {to_holder!r}')
                valid = False
                raw_presence = 'present in raw entities but' if raw_entity_id_counts.get(to_holder, 0) else 'absent from raw entities and'
                record_stop_causes.append(f'holder reference to_holder {to_holder!r} {raw_presence} absent from the resolved index')
            elif entity_id_counts[to_holder] != 1:
                errors.append(f'{record_label}.to_holder: ambiguous entity {to_holder!r}')
                record_holder_ambiguous = True
                ambiguous_holder_references.append(('to_holder', to_holder))
                valid = False
            if from_holder is not None:
                if not isinstance(from_holder, str) or not from_holder.strip():
                    valid = False
                elif entity_id_counts.get(from_holder, 0) == 0:
                    errors.append(f'{record_label}.from_holder: dangling entity {from_holder!r}')
                    valid = False
                    raw_presence = 'present in raw entities but' if raw_entity_id_counts.get(from_holder, 0) else 'absent from raw entities and'
                    record_stop_causes.append(f'holder reference from_holder {from_holder!r} {raw_presence} absent from the resolved index')
                elif entity_id_counts[from_holder] != 1:
                    errors.append(f'{record_label}.from_holder: ambiguous entity {from_holder!r}')
                    record_holder_ambiguous = True
                    ambiguous_holder_references.append(('from_holder', from_holder))
                    valid = False
            if record_holder_ambiguous:
                cause = ', '.join(
                    f'{field} {holder_id!r}'
                    for field, holder_id in ambiguous_holder_references
                )
                record_stop_causes.append(f'ambiguous holder identity {cause}')
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append(f'{record_label}.source_id: required nonempty source id')
                valid = False
                record_stop_causes.append('malformed record (invalid source_id)')
            else:
                citation_status = source(source_id, record_label + '.source_id')
                if citation_status == 'unknown':
                    valid = False
                    raw_presence = 'present in raw sources but' if raw_source_id_counts.get(source_id, 0) else 'absent from raw sources and'
                    record_stop_causes.append(f'source reference {source_id!r} {raw_presence} absent from the resolved index')
                elif citation_status == 'unavailable':
                    valid = False
                    record_stop_causes.append('source table unavailable')
                elif citation_status == 'ambiguous':
                    chain_has_ambiguous_source = True
            if not valid:
                previous_holder = previous_tick = None
                if first_stop is None:
                    first_stop = ('; '.join(record_stop_causes) or 'malformed record', record_label)
                    if not disclosure_emitted:
                        report_unassessed(record_label)
                continue
            if first_stop is None:
                if previous_tick is not None:
                    if tick <= previous_tick:
                        prefix = 'input-structural finding, not sourced-canon; ' if chain_has_ambiguous_source else ''
                        errors.append(f'{record_label}.tick: {prefix}provenance tick {tick} must be greater than previous tick {previous_tick}')
                    if from_holder != previous_holder:
                        expected_detail = holder_identity_detail(previous_holder, 'expected from_holder')
                        from_detail = holder_identity_detail(from_holder, 'from_holder')
                        if expected_detail or from_detail:
                            expected_clause = expected_detail or f'expected from_holder {previous_holder!r}'
                            observed_clause = f'got {from_holder!r}'
                            if from_detail:
                                observed_clause += f'; {from_detail}'
                            errors.append(f'{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {expected_clause}; {observed_clause}')
                        else:
                            errors.append(f'{record_label}: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance chain break; expected from_holder {previous_holder!r}, got {from_holder!r}')
                elif from_holder is not None:
                    from_detail = holder_identity_detail(from_holder, 'from_holder')
                    if from_detail:
                        errors.append(f'{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {from_detail}; first record must have from_holder null')
                    else:
                        errors.append(f'{record_label}: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance chain break; first record must have from_holder null')
            previous_holder = to_holder
            previous_tick = tick

    allied = [row for _, row in data['relations'] if row['type'] == 'allied_with']
    for location, row in data['relations']:
        if not entities_available:
            continue
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
        if not reciprocal and sources_available:
            errors.append(f'{location}: allied_with faction relation {left!r} -> {right!r} lacks a sourced reciprocal relation')

    occupied = {}
    for location, row in data['timeline']:
        actor_id_count = entity_id_counts.get(row['entity_id'], 0)
        place_id_count = entity_id_counts.get(row['place_id'], 0)
        comparable_place = False
        if entities_available:
            for field in ('entity_id', 'place_id'):
                if row[field] not in entities:
                    errors.append(f'{location}.{field}: dangling entity {row[field]!r}')
            if actor_id_count > 1:
                errors.append(f'{location}.entity_id: ambiguous actor entity {row["entity_id"]!r}')
            if place_id_count > 1:
                errors.append(f'{location}.place_id: ambiguous place entity {row["place_id"]!r}')
            elif place_id_count == 1 and entities[row['place_id']]['kind'] != 'place':
                errors.append(f'{location}.place_id: not a place {row["place_id"]!r}')
            comparable_place = place_id_count == 1 and entities[row['place_id']]['kind'] == 'place'
        source(row['source_id'], location + '.source_id')
        if row['tick'] < 0:
            errors.append(f'{location}.tick: must be nonnegative')
        if entities_available and actor_id_count == 1 and comparable_place and row['tick'] >= 0:
            slot = (row['entity_id'], row['tick'])
            if slot in occupied and occupied[slot][1] != row['place_id']:
                previous, prior_place = occupied[slot]
                errors.append(f'{location}: double-booked {row["entity_id"]!r} at tick {row["tick"]} in {previous} ({prior_place!r}) and {row["place_id"]!r}')
            else:
                occupied[slot] = (location, row['place_id'])
        dependencies = row['depends_on']
        if not all(isinstance(dep, str) for dep in dependencies):
            errors.append(f'{location}.depends_on: expected event-id strings')
        seen_dependencies = set()
        for dep_index, dep in enumerate(dependencies):
            if not isinstance(dep, str):
                continue
            dep_location = f'{location}.depends_on[{dep_index}]'
            if dep == row['id']:
                errors.append(f'{dep_location}: self dependency {dep!r}')
            if dep in seen_dependencies:
                errors.append(f'{dep_location}: repeated dependency {dep!r}')
            else:
                seen_dependencies.add(dep)
                count = event_id_counts.get(dep, 0)
                if count == 0:
                    errors.append(f'{location}.depends_on: unknown event {dep!r}')
                elif count > 1:
                    errors.append(f'{dep_location}: ambiguous dependency event {dep!r}')
                elif (events[dep]['tick'] >= 0 and row['tick'] >= 0
                      and events[dep]['tick'] >= row['tick']):
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

# drift
